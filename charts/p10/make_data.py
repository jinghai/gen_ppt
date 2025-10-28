#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成 p10 的真实数据 JSON（chart8 / chart9），来源于 metrics_v5.db。

本页按“情感三分类”产出数据：
- chart8：Lenovo 当月情感分布（Positive/Neutral/Negative，百分比，保留 1 位）
- chart9：Lenovo 日级情感趋势（3 条序列：Pos/Neu/Neg；x 轴按 axis_day_base 映射）

若数据缺失，则回退到 original_* 文件，保证流程不中断。
"""
from __future__ import annotations
import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Optional, Tuple

import pandas as pd
import yaml
import calendar

ROOT = Path(__file__).resolve().parent

def _find_gen_root() -> Path:
    # 自下而上查找同时包含 config.yaml 与 input/ 的 gen_ppt 根目录
    cur = ROOT
    while cur.parent != cur:
        if (cur / 'config.yaml').exists() and (cur / 'input').exists():
            return cur
        cur = cur.parent
    # 兜底：回退到上两级（通常为 gen_ppt）
    return Path(__file__).resolve().parents[2]

GEN_ROOT = _find_gen_root()
METRICS_DB_DEFAULT = GEN_ROOT / 'input' / 'metrics_v5.db'

CHART8_DIR = ROOT / 'chart8'
CHART9_DIR = ROOT / 'chart9'


@dataclass
class Config:
    brands_order: List[str]
    brands_display: List[str]
    country_id: int
    output_db: Path
    start_date: str
    end_date: str
    axis_day_base: int
    base_brand: str
    smooth_percent: bool
    smooth_window: int


def _load_yaml_cfg() -> Config:
    base_cfg = yaml.safe_load((GEN_ROOT / 'config.yaml').read_text(encoding='utf-8'))
    filters_cfg = (base_cfg.get('filters') or {})
    brands_order = filters_cfg.get('brands') or []
    brands_display = filters_cfg.get('brands_display') or [b.capitalize() for b in brands_order]
    country_id = int(filters_cfg.get('countryId') or 39)
    base_brand = (filters_cfg.get('brand_key') or 'Lenovo')
    base_brand_lc = str(base_brand).strip().lower()

    metrics_db_value = ((base_cfg.get('data_sources') or {}).get('metrics_db') or METRICS_DB_DEFAULT)
    metrics_db_path = metrics_db_value if isinstance(metrics_db_value, Path) else Path(metrics_db_value)
    if not metrics_db_path.is_absolute():
        metrics_db_path = (GEN_ROOT / metrics_db_path).resolve()
    output_db = metrics_db_path

    update_cfg = (base_cfg.get('update') or {})
    start_date = str(update_cfg.get('start_date') or '2025-01-01')
    end_date = str(update_cfg.get('end_date') or '2025-12-12')

    axis_day_base = int((base_cfg.get('fill_policy') or {}).get('axis_day_base', 20300))

    # 叠加 p10 局部配置（用于轴与平滑开关）
    smooth_percent = False
    smooth_window = 7
    try:
        local_cfg = yaml.safe_load((ROOT / 'config.yaml').read_text(encoding='utf-8')) or {}
    except Exception:
        local_cfg = {}
    # p10 覆盖 axis_day_base（如果提供）
    if isinstance(local_cfg.get('fill_policy'), dict) and 'axis_day_base' in local_cfg['fill_policy']:
        try:
            axis_day_base = int(local_cfg['fill_policy']['axis_day_base'])
        except Exception:
            pass
    # 读取 chart9 平滑开关
    c9 = local_cfg.get('chart9') or {}
    smooth_percent = bool(c9.get('smooth_percent', smooth_percent))
    try:
        smooth_window = int(c9.get('smooth_window', smooth_window))
    except Exception:
        smooth_window = 7
    return Config(
        brands_order=brands_order,
        brands_display=brands_display,
        country_id=country_id,
        output_db=output_db,
        start_date=start_date,
        end_date=end_date,
        axis_day_base=axis_day_base,
        base_brand=base_brand_lc,
        smooth_percent=smooth_percent,
        smooth_window=smooth_window,
    )


def _connect_sqlite(path: Path) -> sqlite3.Connection:
    return sqlite3.connect(str(path))


def _month_label(date_str: str) -> str:
    # YYYY-MM-DD → YYYY-MM
    return date_str[:7]


def _days_range(start_date: str, end_date: str) -> List[str]:
    idx = pd.date_range(start=start_date, end=end_date, freq='D')
    return [d.strftime('%Y-%m-%d') for d in idx]


# ---------- chart8：Lenovo 当月情感分布（百分比） ----------

def make_chart8(cfg: Config, conn: sqlite3.Connection) -> Tuple[List[str], List[float]]:
    month_label = _month_label(cfg.start_date)
    # 选取目标品牌（lenovo）在目标国家的当月情感计数
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
        return _fallback_chart8()
    p = float(df['positive_mentions'].sum())
    n = float(df['neutral_mentions'].sum())
    ng = float(df['negative_mentions'].sum())
    denom = p + n + ng
    if denom <= 0:
        return _fallback_chart8()
    vals = [round(p/denom*100.0, 1), round(n/denom*100.0, 1), round(ng/denom*100.0, 1)]
    labels = ['Positive','Neutral','Negative']
    return labels, vals


def _fallback_chart8() -> Tuple[List[str], List[float]]:
    try:
        series_raw = json.loads((CHART8_DIR / 'original_series.json').read_text(encoding='utf-8'))
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


# ---------- chart9：Lenovo 日级情感趋势（Pos/Neu/Neg 三条曲线） ----------

def make_chart9(cfg: Config, conn: sqlite3.Connection) -> List[Dict[str, object]]:
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
        return _fallback_chart9()
    df = df.set_index('day')
    # 先构建计数序列（缺失天置 0）
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

    if cfg.smooth_percent:
        # 滚动求和后计算占比：sum(pos)/sum(all) * 100
        w = max(int(cfg.smooth_window or 1), 1)
        s_pos = pd.Series(pos_counts).rolling(window=w, min_periods=1).sum()
        s_neu = pd.Series(neu_counts).rolling(window=w, min_periods=1).sum()
        s_neg = pd.Series(neg_counts).rolling(window=w, min_periods=1).sum()
        denom = s_pos + s_neu + s_neg
        y_pos = [round((p / d * 100.0), 1) if d > 0 else 0.0 for p, d in zip(s_pos, denom)]
        y_neu = [round((n / d * 100.0), 1) if d > 0 else 0.0 for n, d in zip(s_neu, denom)]
        y_neg = [round((ng / d * 100.0), 1) if d > 0 else 0.0 for ng, d in zip(s_neg, denom)]
    else:
        # 当日占比
        y_pos = []
        y_neu = []
        y_neg = []
        for p, n, ng in zip(pos_counts, neu_counts, neg_counts):
            denom = p + n + ng
            if denom > 0:
                y_pos.append(round(p / denom * 100.0, 1))
                y_neu.append(round(n / denom * 100.0, 1))
                y_neg.append(round(ng / denom * 100.0, 1))
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


def _fallback_chart9() -> List[Dict[str, object]]:
    try:
        data = json.loads((CHART9_DIR / 'original_scatter.json').read_text(encoding='utf-8'))
        out = []
        for s in data:
            name = s.get('name') or None
            x = s.get('x') or [p[0] for p in (s.get('points') or [])]
            y = s.get('y') or [p[1] for p in (s.get('points') or [])]
            out.append({'name': name, 'x': x, 'y': y, 'points': [[x[i] if i < len(x) else None, y[i] if i < len(y) else None] for i in range(max(len(x or []), len(y or [])))]})
        return out
    except Exception:
        return []


def write_chart8(labels: List[str], values: List[float]):
    obj = {'labels': labels, 'series': [{'name': None, 'values': values}]}
    (CHART8_DIR / 'data.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')
    (CHART8_DIR / 'final_data.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')


def write_chart9(series: List[Dict[str, object]]):
    obj = {'scatter_series': series}
    (CHART9_DIR / 'data.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')
    (CHART9_DIR / 'final_data.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')


def main() -> int:
    cfg = _load_yaml_cfg()
    if not cfg.output_db.exists():
        print('metrics_v5.db 不存在：', cfg.output_db)
        # 仍然写入兜底 original_*，保证流程不中断
        labels, values = _fallback_chart8()
        write_chart8(labels, values)
        series = _fallback_chart9()
        write_chart9(series)
        return 1
    with _connect_sqlite(cfg.output_db) as conn:
        labels, values = make_chart8(cfg, conn)
        write_chart8(labels, values)
        series = make_chart9(cfg, conn)
        write_chart9(series)
    print('p10 数据已生成：chart8/chart9 的 data.json 与 final_data.json')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())