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
from datetime import datetime, timedelta, timezone
from collections import defaultdict

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
    brands_display: List[str]
    metrics_db: Path
    neticle_db: Path
    start_date: str
    end_date: str
    axis_day_base: int
    country_id: int
    channel_order: List[str]
    channel_name_map: Dict[str, str]


def _load_yaml_cfg() -> Config:
    # 全局填充策略与品牌/时间
    base_cfg = yaml.safe_load((GEN / 'config.yaml').read_text(encoding='utf-8'))
    filters = base_cfg.get('filters') or {}
    brands_order = (filters.get('brands') or [])
    brands_display = (filters.get('brands_display') or [b.capitalize() for b in brands_order])

    ds = base_cfg.get('data_sources') or {}
    metrics_db = Path((ds.get('metrics_db') or METRICS_DB_DEFAULT))
    if not metrics_db.is_absolute():
        metrics_db = GEN / metrics_db
    neticle_db = Path((ds.get('neticle_db') or GEN / 'input' / 'neticle-v5.sqlite'))
    if not neticle_db.is_absolute():
        neticle_db = GEN / neticle_db

    tr = (yaml.safe_load(CFG_PATH.read_text(encoding='utf-8')).get('time_range') or {}) if CFG_PATH and CFG_PATH.exists() else {}
    start_date = str(tr.get('start_date') or '2025-08-01')
    end_date = str(tr.get('end_date') or '2025-08-31')
    fp = (base_cfg.get('fill_policy') or {})
    axis_day_base = int(fp.get('axis_day_base', 20300))
    country_id = int(filters.get('countryId') or 39)

    # 渠道排序与映射
    channel_order = (fp.get('channel_order') or ["Online News", "Forum", "Blog", "X", "Instagram", "YouTube"])
    raw_channels = (base_cfg.get('channels') or {})
    channel_name_map: Dict[str, str] = {}
    for ch_name, raw_list in raw_channels.items():
        for raw in (raw_list or []):
            channel_name_map[str(raw).strip().lower()] = ch_name

    return Config(
        brands_order=brands_order,
        brands_display=brands_display,
        metrics_db=metrics_db,
        neticle_db=neticle_db,
        start_date=start_date,
        end_date=end_date,
        axis_day_base=axis_day_base,
        country_id=country_id,
        channel_order=channel_order,
        channel_name_map=channel_name_map,
    )


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
    # 使用展示名称
    labels = cfg.brands_display
    return labels, sov


# ---------- 渠道内 SOV（多系列，X=渠道，Series=品牌） ----------

def _to_utc_ms(date_str: str) -> int:
    dt = datetime.strptime(date_str, '%Y-%m-%d').replace(tzinfo=timezone.utc)
    return int(dt.timestamp() * 1000)


def make_channel_sov_by_brand(cfg: Config) -> Tuple[List[str], List[Dict[str, object]]]:
    # 读取 mentions_wide 中目标渠道与品牌标签
    raw_names = sorted(set(cfg.channel_name_map.keys()))
    if not raw_names:
        return [], []
    start_ms = _to_utc_ms(cfg.start_date)
    end_ms = _to_utc_ms((datetime.strptime(cfg.end_date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d'))

    placeholders = ','.join(['?'] * len(raw_names))
    sql = f"""
    SELECT sourceName as src, brandLabelNames as brands
    FROM mentions_wide
    WHERE countryId = ?
      AND createdAtUtcMs >= ? AND createdAtUtcMs < ?
      AND brandLabelCount > 0
      AND sourceName IN ({placeholders})
    """
    params = [cfg.country_id, start_ms, end_ms] + raw_names
    with _connect_sqlite(cfg.neticle_db) as conn:
        df = pd.read_sql_query(sql, conn, params=params)

    if df.empty:
        return cfg.channel_order, [
            {'name': disp, 'values': [0.0 for _ in cfg.channel_order]}
            for disp in cfg.brands_display
        ]

    brands_set = set(cfg.brands_order)
    # 计数（加权）：每条 mention 如包含多品牌，则 1/品牌数 分配
    counts = {b: defaultdict(float) for b in cfg.brands_order}

    for _, row in df.iterrows():
        raw = str(row['src']).strip().lower()
        ch = cfg.channel_name_map.get(raw)
        if not ch:
            continue
        names = row['brands']
        if names is None:
            continue
        toks = [t.strip().lower() for t in str(names).split('|') if t and isinstance(t, str)]
        present = [t for t in toks if t in brands_set]
        if not present:
            continue
        w = 1.0 / float(len(present))
        for b in present:
            counts[b][ch] += w

    # 渠道口径内 SOV：每个渠道内按品牌占比（和为 100%）
    labels = cfg.channel_order
    series: List[Dict[str, object]] = []
    for b, disp in zip(cfg.brands_order, cfg.brands_display):
        vals: List[float] = []
        for ch in labels:
            denom = sum(counts[bb][ch] for bb in cfg.brands_order)
            v = counts[b][ch]
            vals.append(round((v / denom * 100.0), 1) if denom > 0 else 0.0)
        series.append({'name': disp, 'values': vals})
    return labels, series


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


def write_cat_multi_json(chart_dir: Path, labels: List[str], series: List[Dict[str, object]]):
    obj = {'labels': labels, 'series': series}
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
    # metrics_db 可缺省（本页 barChart 走 neticle DB）
    if not cfg.metrics_db.exists():
        print('metrics_v5.db 不存在：', cfg.metrics_db)
    # 遍历当前页所有 chart*
    import re as _re
    for chart_dir in sorted([p for p in page_dir.iterdir() if p.is_dir() and _re.match(r'^chart\d+$', p.name)]):
        chart_path_txt = chart_dir / 'chart_path.txt'
        xml_name = None
        if chart_path_txt.exists():
            try:
                raw = chart_path_txt.read_text(encoding='utf-8').strip()
                xml_name = Path(raw).name if raw else None
            except Exception:
                xml_name = None
        if not xml_name:
            xml_name = f"{chart_dir.name}.xml"
        chart_xml = UNZIPPED_CHARTS / xml_name
        if not chart_xml.exists():
            print('缺少图表 XML：', chart_xml)
            continue
        t = _chart_type(chart_xml)
        if t == 'scatterChart' or t == 'lineChart':
            # 趋势图仍走 metrics_db
            if cfg.metrics_db.exists():
                with _connect_sqlite(cfg.metrics_db) as conn:
                    series = make_trend_lenovo_vs_others(cfg, conn)
            else:
                series = []
            write_scatter_json(chart_dir, series)
        elif t == 'barChart':
            labels, series = make_channel_sov_by_brand(cfg)
            write_cat_multi_json(chart_dir, labels, series)
        elif t in ('pieChart','areaChart','doughnutChart'):
            # 其他类别图按品牌整体 SOV（保留向后兼容）
            if cfg.metrics_db.exists():
                with _connect_sqlite(cfg.metrics_db) as conn:
                    labels, values = make_sov(cfg, conn)
            else:
                labels, values = [], []
            write_cat_json(chart_dir, labels, values)
        else:
            print('未知图表类型，跳过：', chart_xml)
    print('数据已生成：', ROOT)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
