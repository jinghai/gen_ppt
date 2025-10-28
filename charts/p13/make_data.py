#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 生成该页的真实数据 JSON：
# - 类别图（pie/bar/area/doughnut）：Lenovo 当月情感分布（Positive/Neutral/Negative 占比，保留 1 位）
# - 散点/线图：Lenovo 日级情感趋势（3 条序列：Pos/Neu/Neg；y 为百分比，x 按 axis_day_base 映射）
# 若数据缺失，回退到 original_* 缓存以保证流程不中断。
from __future__ import annotations
import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Tuple, Optional

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parent

def _find_gen_root() -> Path:
    cur = ROOT
    while cur.parent != cur:
        if (cur / 'config.yaml').exists() and (cur / 'input').exists():
            return cur
        cur = cur.parent
    return Path(__file__).resolve().parents[2]

GEN = _find_gen_root()
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
    country_id: int
    base_brand: str
    output_db: Path
    start_date: str
    end_date: str
    axis_day_base: int


def _load_yaml_cfg() -> Config:
    base_cfg = yaml.safe_load((GEN / 'config.yaml').read_text(encoding='utf-8'))
    filters_cfg = (base_cfg.get('filters') or {})
    brands_order = filters_cfg.get('brands') or []
    country_id = int(filters_cfg.get('countryId') or 39)
    base_brand = str(filters_cfg.get('brand_key') or (brands_order[0] if brands_order else 'Lenovo')).strip().lower()

    metrics_db_value = ((base_cfg.get('data_sources') or {}).get('metrics_db') or METRICS_DB_DEFAULT)
    metrics_db_path = metrics_db_value if isinstance(metrics_db_value, Path) else Path(metrics_db_value)
    if not metrics_db_path.is_absolute():
        metrics_db_path = (GEN / metrics_db_path).resolve()
    output_db = metrics_db_path

    update_cfg = (base_cfg.get('update') or {})
    start_date = str(update_cfg.get('start_date') or '2025-08-01')
    end_date = str(update_cfg.get('end_date') or '2025-08-31')

    axis_day_base = int((base_cfg.get('fill_policy') or {}).get('axis_day_base', 20300))
    # 允许局部覆盖 axis_day_base
    try:
        local_cfg = yaml.safe_load((ROOT / 'config.yaml').read_text(encoding='utf-8')) or {}
    except Exception:
        local_cfg = {}
    if isinstance(local_cfg.get('fill_policy'), dict) and 'axis_day_base' in local_cfg['fill_policy']:
        try:
            axis_day_base = int(local_cfg['fill_policy']['axis_day_base'])
        except Exception:
            pass
    return Config(
        brands_order=brands_order,
        country_id=country_id,
        base_brand=base_brand,
        output_db=output_db,
        start_date=start_date,
        end_date=end_date,
        axis_day_base=axis_day_base,
    )


def _connect_sqlite(path: Path) -> sqlite3.Connection:
    return sqlite3.connect(str(path))


def _month_label(date_str: str) -> str:
    return date_str[:7]


def _days_range(start_date: str, end_date: str) -> List[str]:
    idx = pd.date_range(start=start_date, end=end_date, freq='D')
    return [d.strftime('%Y-%m-%d') for d in idx]


def _normalize_100(values: List[float]) -> List[float]:
    """Adjust values so that their rounded sum equals 100.0.
    Keep one decimal place and add the residual to the largest component.
    """
    if not values:
        return values
    rounded = [round(v, 1) for v in values]
    s = round(sum(rounded), 1)
    diff = round(100.0 - s, 1)
    if abs(diff) >= 0.05:  # avoid floating noise like -0.0
        # add the residual to the max component to preserve ordering
        i = max(range(len(rounded)), key=lambda k: rounded[k])
        rounded[i] = round(rounded[i] + diff, 1)
        # clamp
        rounded[i] = max(0.0, min(100.0, rounded[i]))
    # ensure overall bounds
    return rounded


# ---------- chart10：Lenovo 当月情感分布（百分比） ----------

def make_chart10(cfg: Config, conn: sqlite3.Connection) -> Tuple[List[str], List[float]]:
    month_label = _month_label(cfg.start_date)
    q = """
    SELECT countryId, month, brand,
           SUM(COALESCE(positive_mentions,0)) as positive_mentions,
           SUM(COALESCE(neutral_mentions,0))  as neutral_mentions,
           SUM(COALESCE(negative_mentions,0)) as negative_mentions
    FROM brand_metrics_month
    WHERE month = ?
      AND countryId = ?
      AND LOWER(brand) = ?
    GROUP BY countryId, month, brand
    """
    params = [month_label, cfg.country_id, cfg.base_brand]
    df = pd.read_sql_query(q, conn, params=params)
    if df.empty:
        return _fallback_chart10()
    p = float(df['positive_mentions'].sum())
    n = float(df['neutral_mentions'].sum())
    ng = float(df['negative_mentions'].sum())
    denom = p + n + ng
    if denom <= 0:
        return _fallback_chart10()
    vals = [p/denom*100.0, n/denom*100.0, ng/denom*100.0]
    vals = _normalize_100(vals)
    labels = ['Positive','Neutral','Negative']
    return labels, vals


def _fallback_chart10() -> Tuple[List[str], List[float]]:
    chart_dir = ROOT / 'chart10'
    try:
        series_raw = json.loads((chart_dir / 'original_series.json').read_text(encoding='utf-8'))
        if isinstance(series_raw, list) and series_raw:
            if isinstance(series_raw[0], dict):
                values = series_raw[0].get('values', [])
            elif isinstance(series_raw[0], (int, float)):
                values = series_raw
            else:
                values = series_raw[0]
        else:
            values = []
    except Exception:
        values = []
    labels = []
    if not values:
        labels = []
    else:
        labels = [f'Slice {i+1}' for i in range(len(values))]
    return labels, [float(x) for x in values]


# ---------- chart11：Lenovo 日级情感趋势（Pos/Neu/Neg 三条曲线） ----------

def make_chart11(cfg: Config, conn: sqlite3.Connection) -> List[Dict[str, object]]:
    days = _days_range(cfg.start_date, cfg.end_date)
    q = """
    SELECT day,
           SUM(COALESCE(positive_mentions,0)) as positive_mentions,
           SUM(COALESCE(neutral_mentions,0))  as neutral_mentions,
           SUM(COALESCE(negative_mentions,0)) as negative_mentions
    FROM brand_metrics_day
    WHERE day >= ? AND day <= ?
      AND countryId = ?
      AND LOWER(brand) = ?
    GROUP BY day
    """
    params = [cfg.start_date, cfg.end_date, cfg.country_id, cfg.base_brand]
    df = pd.read_sql_query(q, conn, params=params)
    if df.empty:
        return _fallback_chart11()
    df = df.set_index('day')
    pos_counts: List[float] = []
    neu_counts: List[float] = []
    neg_counts: List[float] = []
    for d in days:
        if d in df.index:
            row = df.loc[d]
            pos_counts.append(float(row['positive_mentions']))
            neu_counts.append(float(row['neutral_mentions']))
            neg_counts.append(float(row['negative_mentions']))
        else:
            pos_counts.append(0.0)
            neu_counts.append(0.0)
            neg_counts.append(0.0)
    y_pos: List[float] = []
    y_neu: List[float] = []
    y_neg: List[float] = []
    for p, n, ng in zip(pos_counts, neu_counts, neg_counts):
        denom = p + n + ng
        if denom > 0:
            vals = _normalize_100([p / denom * 100.0, n / denom * 100.0, ng / denom * 100.0])
            y_pos.append(vals[0])
            y_neu.append(vals[1])
            y_neg.append(vals[2])
        else:
            y_pos.append(0.0)
            y_neu.append(0.0)
            y_neg.append(0.0)
    x = [float(cfg.axis_day_base + i + 1) for i in range(len(days))]
    return [
        {'name': 'Positive', 'x': x, 'y': y_pos, 'points': [[x[i], y_pos[i]] for i in range(len(x))]},
        {'name': 'Neutral',  'x': x, 'y': y_neu, 'points': [[x[i], y_neu[i]] for i in range(len(x))]},
        {'name': 'Negative', 'x': x, 'y': y_neg, 'points': [[x[i], y_neg[i]] for i in range(len(x))]},
    ]


def _fallback_chart11() -> List[Dict[str, object]]:
    chart_dir = ROOT / 'chart11'
    try:
        data = json.loads((chart_dir / 'original_scatter.json').read_text(encoding='utf-8'))
        out = []
        for s in data:
            name = s.get('name') or None
            x = s.get('x') or [p[0] for p in (s.get('points') or [])]
            y = s.get('y') or [p[1] for p in (s.get('points') or [])]
            out.append({'name': name, 'x': x, 'y': y, 'points': [[x[i] if i < len(x) else None, y[i] if i < len(y) else None] for i in range(max(len(x or []), len(y or [])))]})
        return out
    except Exception:
        return []


def write_cat_json(chart_dir: Path, labels: List[str], values: List[float]):
    obj: Dict[str, object] = {'labels': labels, 'series': [{'name': None, 'values': values}]}
    (chart_dir / 'data.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')
    (chart_dir / 'final_data.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')


def write_scatter_json(chart_dir: Path, series: List[Dict[str, object]]):
    obj: Dict[str, object] = {'scatter_series': series}
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


def compute_engagement_metrics(cfg: Config, conn: sqlite3.Connection) -> Dict[str, object]:
    """Compute Lenovo engagement metrics within the date window.
    Engagement volume = total_interactions.
    IPM (interactions per mention) = total_interactions / total_mentions.
    Returns a dict to be embedded under 'metrics'.
    """
    days = _days_range(cfg.start_date, cfg.end_date)
    q = """
    SELECT day,
           SUM(COALESCE(total_interactions,0)) as total_interactions,
           SUM(COALESCE(total_mentions,0))      as total_mentions
    FROM brand_metrics_day
    WHERE day >= ? AND day <= ?
      AND countryId = ?
      AND LOWER(brand) = ?
    GROUP BY day
    """
    params = [cfg.start_date, cfg.end_date, cfg.country_id, cfg.base_brand]
    df = pd.read_sql_query(q, conn, params=params)
    if df.empty:
        return {
            'engagement_total_month': 0,
            'ipm_month': 0.0,
            'by_day': {'date': days, 'engagement': [0.0]*len(days), 'ipm': [0.0]*len(days)},
        }
    df = df.set_index('day')
    eng_day: List[float] = []
    ipm_day: List[float] = []
    mentions_day_sum = 0.0
    for d in days:
        if d in df.index:
            row = df.loc[d]
            eng = float(row['total_interactions'] or 0.0)
            m = float(row['total_mentions'] or 0.0)
            eng_day.append(eng)
            ipm_day.append(round(eng / m, 4) if m > 0 else 0.0)
            mentions_day_sum += m
        else:
            eng_day.append(0.0)
            ipm_day.append(0.0)
    eng_month = float(sum(eng_day))
    ipm_month = round(eng_month / mentions_day_sum, 4) if mentions_day_sum > 0 else 0.0
    return {
        'engagement_total_month': int(eng_month),
        'ipm_month': ipm_month,
        'by_day': {'date': days, 'engagement': eng_day, 'ipm': ipm_day},
    }


def main() -> int:
    page_dir = ROOT
    cfg = _load_yaml_cfg()
    if not cfg.output_db.exists():
        print('metrics_v5.db 不存在：', cfg.output_db)
        # 仍写入兜底，保证流程不中断
        # chart10
        labels10, values10 = _fallback_chart10()
        write_cat_json(page_dir / 'chart10', labels10, values10)
        # chart11
        series11 = _fallback_chart11()
        write_scatter_json(page_dir / 'chart11', series11)
        return 1
    with _connect_sqlite(cfg.output_db) as conn:
        # 计算本页 Engagement 指标，附加到 JSON（方便备注或其它页面复用）
        metrics = compute_engagement_metrics(cfg, conn)
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
                series = make_chart11(cfg, conn)
                obj: Dict[str, object] = {'scatter_series': series, 'metrics': metrics}
                (chart_dir / 'data.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')
                (chart_dir / 'final_data.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')
            elif t in ('barChart','pieChart','areaChart','doughnutChart'):
                labels, values = make_chart10(cfg, conn)
                obj: Dict[str, object] = {'labels': labels, 'series': [{'name': None, 'values': values}], 'metrics': metrics}
                (chart_dir / 'data.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')
                (chart_dir / 'final_data.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')
            else:
                print('未知图表类型，跳过：', chart_xml)
    print('数据已生成：', ROOT)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
