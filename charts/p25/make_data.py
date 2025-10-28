#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 生成该页的真实数据 JSON：
# - 类别图（bar/pie/area/doughnut）：7 品牌 SOV（当月占比，百分比，保留 1 位）
# - 散点/线图：Lenovo vs Others 的日级趋势（y 为品牌提及数；x 按 axis_day_base 映射）
# 缺失数据保持为空或根据 fill_policy 保留原始缓存。
from __future__ import annotations
import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Tuple

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parent
# gen_ppt 根目录（charts/pXX/ 的上两级）
GEN = Path(__file__).resolve().parents[2]

# 可选的仓库根（用于读取 compute_metrics.yaml 的时间窗口）
REPO_CANDIDATES = [GEN.parent, GEN]
REPO_ROOT = None
CFG_PATH = None
for base in REPO_CANDIDATES:
    candidate = base / 'compute_metrics.yaml'
    if candidate.exists():
        REPO_ROOT = base
        CFG_PATH = candidate
        break
if REPO_ROOT is None:
    REPO_ROOT = GEN.parent
    CFG_PATH = REPO_ROOT / 'compute_metrics.yaml'

METRICS_DB_DEFAULT = GEN / 'input' / 'metrics_v5.db'

def _resolve_unz_root() -> Path:
    try:
        cfg = yaml.safe_load((GEN / 'config.yaml').read_text(encoding='utf-8')) or {}
    except Exception:
        cfg = {}
    tr = (cfg.get('project') or {}).get('template_root', 'input/LRTBH-unzip')
    p = Path(tr)
    if not p.is_absolute():
        p = GEN / tr
    return p

def _charts_dir(unz: Path) -> Path:
    d = unz / 'ppt' / 'charts'
    return d if d.exists() else unz / 'charts'

UNZIPPED_CHARTS = _charts_dir(_resolve_unz_root())

@dataclass
class Config:
    brands_order: List[str]
    output_db: Path
    start_date: str
    end_date: str
    axis_day_base: int


def _load_yaml_cfg() -> Config:
    # 全局填充策略与品牌/时间
    base_cfg = yaml.safe_load((GEN / 'config.yaml').read_text(encoding='utf-8'))
    brands_order = (base_cfg.get('filters') or {}).get('brands') or []
    output_db = Path(((base_cfg.get('data_sources') or {}).get('metrics_db') or METRICS_DB_DEFAULT))
    if not output_db.is_absolute():
        output_db = GEN / output_db
    tr = (yaml.safe_load(CFG_PATH.read_text(encoding='utf-8')).get('time_range') or {}) if CFG_PATH and CFG_PATH.exists() else {}
    start_date = str(tr.get('start_date') or '2025-08-01')
    end_date = str(tr.get('end_date') or '2025-08-31')
    axis_day_base = int((base_cfg.get('fill_policy') or {}).get('axis_day_base', 20300))
    return Config(brands_order=brands_order, output_db=output_db, start_date=start_date, end_date=end_date, axis_day_base=axis_day_base)


def _connect_sqlite(path: Path) -> sqlite3.Connection:
    return sqlite3.connect(str(path))


def _month_label(date_str: str) -> str:
    return date_str[:7]


def _days_range(start_date: str, end_date: str) -> List[str]:
    idx = pd.date_range(start=start_date, end=end_date, freq='D')
    return [d.strftime('%Y-%m-%d') for d in idx]


# ---------- SOV 百分比 ----------

def make_sov(cfg: Config, conn: sqlite3.Connection) -> Tuple[List[str], List[float]]:
    month_label = _month_label(cfg.start_date)
    q = f"""
    SELECT countryId, month, brand, brand_mentions, total_mentions
    FROM brand_metrics_month
    WHERE month = ?
      AND brand IN ({','.join(['?'] * len(cfg.brands_order))})
    """
    params = [month_label] + cfg.brands_order
    df = pd.read_sql_query(q, conn, params=params)
    if df.empty:
        return [], []
    denom = df.groupby(['countryId','month'])['total_mentions'].max().sum()
    if denom <= 0:
        return [], []
    brand_mentions = (
        df.groupby('brand')['brand_mentions']
          .sum()
          .reindex(cfg.brands_order)
          .fillna(0)
          .astype(float)
          .tolist()
    )
    sov = [round(v / float(denom) * 100.0, 1) for v in brand_mentions]
    labels = [b.capitalize() for b in cfg.brands_order]
    return labels, sov


# ---------- Lenovo vs Others 日级 ----------

def make_trend_lenovo_vs_others(cfg: Config, conn: sqlite3.Connection) -> List[Dict[str, object]]:
    brands = cfg.brands_order
    if not brands:
        return []
    base_brand = 'lenovo' if 'lenovo' in brands else brands[0]
    days = _days_range(cfg.start_date, cfg.end_date)
    q = f"""
    SELECT countryId, day, brand, brand_mentions
    FROM brand_metrics_day
    WHERE day >= ? AND day <= ?
      AND brand IN ({','.join(['?'] * len(brands))})
    """
    params = [cfg.start_date, cfg.end_date] + brands
    df = pd.read_sql_query(q, conn, params=params)
    if df.empty:
        return []
    gb = df.groupby(['day','brand'])['brand_mentions'].sum().reset_index()
    y1: List[float] = []
    y2: List[float] = []
    for d in days:
        v_brand = gb.loc[(gb['day'] == d) & (gb['brand'] == base_brand), 'brand_mentions']
        v_brand = float(v_brand.sum()) if not v_brand.empty else 0.0
        v_others = gb.loc[(gb['day'] == d) & (gb['brand'] != base_brand), 'brand_mentions']
        v_others = float(v_others.sum()) if not v_others.empty else 0.0
        y1.append(v_brand)
        y2.append(v_others)
    x = [float(cfg.axis_day_base + i + 1) for i in range(len(days))]
    return [
        {'name': base_brand.capitalize(), 'x': x, 'y': y1, 'points': [[x[i], y1[i]] for i in range(len(x))]},
        {'name': 'Others', 'x': x, 'y': y2, 'points': [[x[i], y2[i]] for i in range(len(x))]},
    ]


def write_cat_json(chart_dir: Path, labels: List[str], values: List[float]):
    obj = {'labels': labels, 'series': [{'name': None, 'values': values}]}
    (chart_dir / 'data.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')
    (chart_dir / 'final_data.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')


def write_scatter_json(chart_dir: Path, series: List[Dict[str, object]]):
    obj = {'scatter_series': series}
    (chart_dir / 'data.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')
    (chart_dir / 'final_data.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')


def _chart_type(chart_xml: Path) -> str:
    from lxml import etree
    NS = {'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart'}
    tree = etree.parse(str(chart_xml))
    plot = tree.getroot().find('c:chart/c:plotArea', namespaces=NS)
    for t in ['scatterChart','lineChart','barChart','pieChart','areaChart','doughnutChart']:
        el = plot.find(f'c:{t}', namespaces=NS) if plot is not None else None
        if el is not None:
            return t
    return 'unknown'


def main() -> int:
    page_dir = ROOT
    cfg = _load_yaml_cfg()
    if not cfg.output_db.exists():
        print('metrics_v5.db 不存在：', cfg.output_db)
        return 1
    with _connect_sqlite(cfg.output_db) as conn:
        # 遍历当前页所有 chart*
        import re as _re
        for chart_dir in sorted([p for p in page_dir.iterdir() if p.is_dir() and _re.match(r'^chart\d+$', p.name)]):
            chart_name = chart_dir.name.replace('chart','') + '.xml'
            chart_xml = UNZIPPED_CHARTS / chart_name
            if not chart_xml.exists():
                print('缺少图表 XML：', chart_xml)
                continue
            t = _chart_type(chart_xml)
            if t == 'scatterChart' or t == 'lineChart':
                series = make_trend_lenovo_vs_others(cfg, conn)
                write_scatter_json(chart_dir, series)
            elif t in ('barChart','pieChart','areaChart','doughnutChart'):
                labels, values = make_sov(cfg, conn)
                write_cat_json(chart_dir, labels, values)
            else:
                print('未知图表类型，跳过：', chart_xml)
    print('数据已生成：', ROOT)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
