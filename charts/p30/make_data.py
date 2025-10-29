#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 生成该页的真实数据 JSON：
# - 类别图（bar/pie/area/doughnut/lineChart）：按渠道分布的单品牌 SOV（该品牌在各渠道的占比，百分比，保留 1 位）
# - 散点图（仅 scatterChart）：Lenovo vs Others 的日级趋势（y 为品牌提及数；x 按 axis_day_base 映射）
# 说明：P30 页面大量使用 lineChart 作为“类别图”的极简样式，属于分类轴，不应按散点/趋势处理。
# 缺失数据保持为空或根据 fill_policy 保留原始缓存。
from __future__ import annotations
import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Tuple, Optional

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parent
# gen_ppt 根目录（charts/pXX/ 的上两级）
GEN = Path(__file__).resolve().parents[2]

# 可选的仓库根（用于读取 compute_metrics.yaml 的时间窗口；优先用全局 config.yaml.update）
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
NETICLE_DB_DEFAULT = GEN / 'input' / 'neticle-v5-08.sqlite'

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
    channel_map: Dict[str, List[str]]  # Channel label -> list of source names
    channel_order: List[str]


def _load_yaml_cfg() -> Config:
    # 全局填充策略与品牌/时间
    base_cfg = yaml.safe_load((GEN / 'config.yaml').read_text(encoding='utf-8'))
    filters = (base_cfg.get('filters') or {})
    brands_order = filters.get('brands') or []
    brands_display = filters.get('brands_display') or [b.capitalize() for b in brands_order]
    data_sources = (base_cfg.get('data_sources') or {})
    metrics_db = Path(data_sources.get('metrics_db') or METRICS_DB_DEFAULT)
    if not metrics_db.is_absolute():
        metrics_db = GEN / metrics_db
    neticle_db = Path(data_sources.get('neticle_db') or NETICLE_DB_DEFAULT)
    if not neticle_db.is_absolute():
        neticle_db = GEN / neticle_db

    # 时间范围：优先使用全局 config.yaml.update，其次 compute_metrics.yaml.time_range
    upd = (base_cfg.get('update') or {})
    tr = (yaml.safe_load(CFG_PATH.read_text(encoding='utf-8')).get('time_range') or {}) if CFG_PATH and CFG_PATH.exists() else {}
    start_date = str(upd.get('start_date') or tr.get('start_date') or '2025-08-01')
    end_date = str(upd.get('end_date') or tr.get('end_date') or '2025-08-31')

    axis_day_base = int((base_cfg.get('fill_policy') or {}).get('axis_day_base', 20300))
    country_id = int(filters.get('countryId') or 0)
    channel_map = (base_cfg.get('channels') or {})
    channel_order = (base_cfg.get('fill_policy') or {}).get('channel_order') or list(channel_map.keys())
    return Config(
        brands_order=brands_order,
        brands_display=brands_display,
        metrics_db=metrics_db,
        neticle_db=neticle_db,
        start_date=start_date,
        end_date=end_date,
        axis_day_base=axis_day_base,
        country_id=country_id,
        channel_map=channel_map,
        channel_order=channel_order,
    )


def _connect_sqlite(path: Path) -> sqlite3.Connection:
    return sqlite3.connect(str(path))


def _month_label(date_str: str) -> str:
    return date_str[:7]


def _days_range(start_date: str, end_date: str) -> List[str]:
    idx = pd.date_range(start=start_date, end=end_date, freq='D')
    return [d.strftime('%Y-%m-%d') for d in idx]


# ---------- SOV 百分比（总盘，供其它页面使用） ----------

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
    labels = cfg.brands_display
    return labels, sov


# ---------- Lenovo vs Others 日级（散点） ----------

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


# ---------- 单品牌 × 渠道分布（该品牌在各渠道的份额） ----------

def _to_epoch_ms(date_str: str, end: bool = False) -> int:
    # UTC 零点/日末（+1 天的零点-1ms 更安全，这里用 < next_day ）
    dt = pd.to_datetime(date_str)
    if end:
        dt = (dt + pd.Timedelta(days=1))  # 用 < end_next_day
    return int(dt.timestamp() * 1000)


def _brand_case_expr(brands: List[str]) -> str:
    parts = []
    for b in brands:
        b_esc = b.replace("'", "''").lower()
        parts.append(f"WHEN lower(k.name) LIKE '{b_esc}%' THEN '{b_esc}'")
    return "CASE\n        " + "\n        ".join(parts) + "\n        ELSE NULL END"


def make_channel_distribution(cfg: Config, conn: sqlite3.Connection) -> Dict[str, Dict[str, float]]:
    """
    返回：brand_key -> {channel_label -> percent}
    百分比为该品牌在该渠道的 mentions 占该品牌全渠道总 mentions 的比例（和约等于 100）。
    """
    if not cfg.channel_map or not cfg.brands_order:
        return {}

    # 扁平化渠道源列表，限制 SQL 范围
    all_sources = sorted({s for lst in cfg.channel_map.values() for s in (lst or [])})
    if not all_sources:
        return {}

    start_ms = _to_epoch_ms(cfg.start_date, end=False)
    end_ms = _to_epoch_ms(cfg.end_date, end=True)
    brand_case = _brand_case_expr(cfg.brands_order)
    terms = []
    for b in cfg.brands_order:
        b_esc = b.replace("'", "''").lower()
        terms.append(f"lower(k.name) LIKE '{b_esc}%'")
    like_clause = " OR ".join(terms)
    src_placeholders = ",".join(["?"] * len(all_sources))
    sql = f"""
    SELECT
      ({brand_case}) AS brand_key,
      s.name AS source_name,
      COUNT(1) AS n
    FROM mentions m
    JOIN keywords k ON k.id = m.keywordId
    LEFT JOIN sources s ON s.id = COALESCE(m.subSourceId, m.sourceId)
    WHERE k.countryId = ?
      AND m.createdAtUtcMs >= ?
      AND m.createdAtUtcMs < ?
      AND ({like_clause})
      AND s.name IS NOT NULL
      AND s.name IN ({src_placeholders})
    GROUP BY brand_key, source_name
    """
    params: List[object] = [cfg.country_id, start_ms, end_ms] + all_sources
    df = pd.read_sql_query(sql, conn, params=params)
    if df.empty:
        # 返回全部为 0 的映射
        zero_map: Dict[str, Dict[str, float]] = {}
        for b in cfg.brands_order:
            zero_map[b] = {ch: 0.0 for ch in cfg.channel_order}
        return zero_map

    # 汇总 source_name -> channel_label
    src2ch: Dict[str, str] = {}
    for ch, names in (cfg.channel_map or {}).items():
        for n in names or []:
            src2ch[str(n)] = ch

    # 累加 brand×channel 的 mentions
    bc = {}
    for _, row in df.iterrows():
        b = str(row['brand_key']) if pd.notna(row['brand_key']) else None
        sname = str(row['source_name']) if pd.notna(row['source_name']) else None
        if not b or not sname:
            continue
        ch = src2ch.get(sname)
        if not ch:
            continue
        bc.setdefault(b, {}).setdefault(ch, 0)
        bc[b][ch] += int(row['n'])

    # 转换为百分比
    out: Dict[str, Dict[str, float]] = {}
    for b in cfg.brands_order:
        ch_counts = {ch: float(bc.get(b, {}).get(ch, 0.0)) for ch in cfg.channel_order}
        total = sum(ch_counts.values())
        if total <= 0:
            out[b] = {ch: 0.0 for ch in cfg.channel_order}
        else:
            out[b] = {ch: round(v / total * 100.0, 1) for ch, v in ch_counts.items()}
    return out


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
    # 连接两个库：metrics（备用）与 neticle（渠道聚合）
    if not cfg.neticle_db.exists():
        print('neticle 数据库不存在：', cfg.neticle_db)
        return 1
    # 预计算品牌×渠道分布
    with _connect_sqlite(cfg.neticle_db) as conn_net:
        brand_channel_pct = make_channel_distribution(cfg, conn_net)

    # metrics 连接仅在需要时才打开
    conn_metrics: Optional[sqlite3.Connection] = None
    if cfg.metrics_db.exists():
        conn_metrics = _connect_sqlite(cfg.metrics_db)

    # 遍历当前页所有 chart*（尽量保持与 config.yaml.output.replace_charts 的顺序一致）
    import re as _re
    # 读取本页配置
    page_cfg_path = ROOT / 'config.yaml'
    replace_order: List[str] = []
    if page_cfg_path.exists():
        try:
            pc = yaml.safe_load(page_cfg_path.read_text(encoding='utf-8')) or {}
            replace_order = (pc.get('output') or {}).get('replace_charts') or []
        except Exception:
            replace_order = []

    chart_dirs = [p for p in page_dir.iterdir() if p.is_dir() and _re.match(r'^chart\d+$', p.name)]
    # 将目录按 replace_order 对应的 xml 名排序，找不到时退回目录名排序
    def chart_sort_key(p: Path) -> Tuple[int, str]:
        name = p.name  # chart123
        xml = f'{name}.xml'
        idx = replace_order.index(xml) if xml in replace_order else 10_000
        return (idx, name)
    chart_dirs_sorted = sorted(chart_dirs, key=chart_sort_key)

    # 按品牌轮询赋值：第 i 个图使用 brands_order[i % len(brands)] 的渠道分布
    for i, chart_dir in enumerate(chart_dirs_sorted):
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
        if t == 'scatterChart':
            # 仅散点走趋势（极少出现在本页，逻辑保留）
            if conn_metrics is None:
                print('缺少 metrics 库，无法生成散点趋势，跳过：', chart_xml)
                continue
            series = make_trend_lenovo_vs_others(cfg, conn_metrics)
            write_scatter_json(chart_dir, series)
        else:
            # 类别类：按渠道分布的单品牌占比
            brand_key = cfg.brands_order[i % len(cfg.brands_order)] if cfg.brands_order else 'lenovo'
            ch_order = cfg.channel_order or list((cfg.channel_map or {}).keys())
            pct_map = brand_channel_pct.get(brand_key) or {ch: 0.0 for ch in ch_order}
            values = [float(pct_map.get(ch, 0.0)) for ch in ch_order]
            write_cat_json(chart_dir, ch_order, values)

    if conn_metrics is not None:
        conn_metrics.close()
    print('数据已生成：', ROOT)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
