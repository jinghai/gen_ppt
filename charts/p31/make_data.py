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
from typing import List, Dict, Tuple, Optional

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
    neticle_db: Path
    start_date: str
    end_date: str
    axis_day_base: int
    channels: Dict[str, List[str]]


def _load_yaml_cfg() -> Config:
    # 全局填充策略与品牌/时间
    base_cfg = yaml.safe_load((GEN / 'config.yaml').read_text(encoding='utf-8'))
    brands_order = (base_cfg.get('filters') or {}).get('brands') or []
    output_db = Path(((base_cfg.get('data_sources') or {}).get('metrics_db') or METRICS_DB_DEFAULT))
    if not output_db.is_absolute():
        output_db = GEN / output_db
    neticle_db = Path(((base_cfg.get('data_sources') or {}).get('neticle_db') or (GEN / 'input' / 'neticle.sqlite')))
    if not neticle_db.is_absolute():
        neticle_db = GEN / neticle_db
    tr = (yaml.safe_load(CFG_PATH.read_text(encoding='utf-8')).get('time_range') or {}) if CFG_PATH and CFG_PATH.exists() else {}
    start_date = str(tr.get('start_date') or '2025-08-01')
    end_date = str(tr.get('end_date') or '2025-08-31')
    axis_day_base = int((base_cfg.get('fill_policy') or {}).get('axis_day_base', 20300))
    channels = (base_cfg.get('channels') or {})
    return Config(
        brands_order=brands_order,
        output_db=output_db,
        neticle_db=neticle_db,
        start_date=start_date,
        end_date=end_date,
        axis_day_base=axis_day_base,
        channels=channels,
    )


def _connect_sqlite(path: Path) -> sqlite3.Connection:
    return sqlite3.connect(str(path))


def _month_label(date_str: str) -> str:
    return date_str[:7]


def _days_range(start_date: str, end_date: str) -> List[str]:
    idx = pd.date_range(start=start_date, end=end_date, freq='D')
    return [d.strftime('%Y-%m-%d') for d in idx]


def _weeks_bins_labels(start_date: str, end_date: str) -> Tuple[pd.Series, List[str]]:
    # 将日期均分为4个时间段（尽量等长），返回每个day对应的bin索引以及显示标签
    idx = pd.date_range(start=start_date, end=end_date, freq='D')
    n = len(idx)
    if n == 0:
        return pd.Series(dtype='int'), []
    # 计算分割点（四等分，最后一段包含剩余）
    edges = [0, max(1, n // 4), max(2, (n * 2) // 4), max(3, (n * 3) // 4), n]
    # 确保严格递增且覆盖n
    edges = [0] + sorted(set(edges[1:-1])) + [n]
    if len(edges) != 5:
        # 兜底：均匀切分为4段
        q = [round(n * k / 4) for k in range(5)]
        edges = [q[0], q[1], q[2], q[3], q[4]]
    bins = pd.cut(range(n), bins=edges, labels=False, include_lowest=True, right=False)
    # 生成标签：使用日期范围的简短展示
    labels: List[str] = []
    for i in range(4):
        start_i = idx[edges[i]] if edges[i] < n else idx[n - 1]
        end_i = idx[edges[i + 1] - 1] if edges[i + 1] - 1 < n else idx[n - 1]
        labels.append(f"{start_i.strftime('%m/%d')}-{end_i.strftime('%m/%d')}")
    return pd.Series(bins, index=[d.strftime('%Y-%m-%d') for d in idx]), labels


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


# ---------- 按渠道的4周SOV（Lenovo占比） ----------

def make_weekly_channel_sov_lenovo(cfg: Config, channel: str, country_id: Optional[int] = None) -> Tuple[List[str], List[float]]:
    # 载入 neticle 原始库，基于 mentions_wide：countryId、sourceCode、keyword_label
    if not cfg.neticle_db.exists():
        return [], []
    # 解析国家过滤
    try:
        base_cfg = yaml.safe_load((GEN / 'config.yaml').read_text(encoding='utf-8'))
    except Exception:
        base_cfg = {}
    country_id = country_id or (base_cfg.get('filters') or {}).get('countryId')
    # 渠道映射：取得该渠道对应的 sourceCode 列表
    src_codes = [s.lower() for s in (cfg.channels.get(channel) or [])]
    if not src_codes:
        return [], []
    # 计算 bins 映射与标签
    bin_map, labels = _weeks_bins_labels(cfg.start_date, cfg.end_date)
    if bin_map.empty:
        return [], []
    # 目标品牌（lenovo优先）
    brands = cfg.brands_order
    if not brands:
        return labels, [0.0, 0.0, 0.0, 0.0]
    base_brand = 'lenovo' if 'lenovo' in brands else brands[0]
    start_ms = int(pd.Timestamp(cfg.start_date).timestamp() * 1000)
    end_ms = int((pd.Timestamp(cfg.end_date) + pd.Timedelta(days=1) - pd.Timedelta(milliseconds=1)).timestamp() * 1000)

    # 查询 mentions_wide 聚合到 day、brand_lower
    q = """
        SELECT date(datetime(createdAtUtcMs/1000,'unixepoch')) AS day,
               LOWER(keyword_label) AS brand_lower,
               sourceCode
        FROM mentions_wide
        WHERE createdAtUtcMs BETWEEN ? AND ?
    """
    params = [start_ms, end_ms]
    if country_id is not None:
        q += " AND countryId = ?"
        params.append(country_id)
    # 限定渠道
    # 为避免 SQLite 的 '?' 数量问题，如 src_codes 为空已提前 return
    q += f" AND LOWER(sourceCode) IN ({','.join(['?'] * len(src_codes))})"
    params.extend(src_codes)
    # 限定品牌（通过 keyword_label 模糊为小写品牌名，简单口径）
    # 这里假设 keyword_label 即品牌名标签，已在预计算中统一
    brand_set = [b.lower() for b in brands]
    q += f" AND LOWER(keyword_label) IN ({','.join(['?'] * len(brand_set))})"
    params.extend(brand_set)

    with _connect_sqlite(cfg.neticle_db) as conn:
        df = pd.read_sql_query(q, conn, params=params)
    if df.empty:
        return labels, [0.0, 0.0, 0.0, 0.0]
    df['day'] = df['day'].astype(str)
    # 过滤非映射到 bins 的日期（跨月边界兜底）
    df = df[df['day'].isin(bin_map.index)]
    if df.empty:
        return labels, [0.0, 0.0, 0.0, 0.0]
    df['bin'] = df['day'].map(bin_map)
    # 计算各bin的分子与分母
    # 分子：base_brand 计数；分母：所有 brands 计数之和
    gb_all = df.groupby('bin')['brand_lower'].count().rename('denom')
    gb_base = df[df['brand_lower'] == base_brand].groupby('bin')['brand_lower'].count().rename('num')
    merged = pd.concat([gb_base, gb_all], axis=1).fillna(0.0)
    values = []
    for i in range(4):
        num = float(merged.loc[i, 'num']) if i in merged.index else 0.0
        denom = float(merged.loc[i, 'denom']) if i in merged.index else 0.0
        v = round((num / denom * 100.0), 1) if denom > 0 else 0.0
        values.append(v)
    return labels, values


# ---------- Slide 解析：图表→渠道 近邻匹配 ----------

def _parse_slide_chart_channel_map(slide_xml: Path, slide_rels_xml: Path, channels: List[str]) -> Dict[str, str]:
    from lxml import etree as ET
    NS = {
        'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
        'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart',
    }
    if not slide_xml.exists():
        return {}
    # 读取 rels 映射 rId -> chartXML 名
    rid_to_chart: Dict[str, str] = {}
    if slide_rels_xml.exists():
        rels_tree = ET.parse(str(slide_rels_xml))
        pkg_ns = 'http://schemas.openxmlformats.org/package/2006/relationships'
        for rel in rels_tree.getroot().findall('{%s}Relationship' % pkg_ns):
            t = rel.get('Type') or ''
            if t.endswith('/chart'):
                rid_to_chart[rel.get('Id')] = Path(rel.get('Target') or '').name
    tree = ET.parse(str(slide_xml))
    root = tree.getroot()
    # 收集所有含图表的 graphicFrame 及其位置
    charts_pos: List[Tuple[str, Tuple[int, int, int, int]]] = []  # (chartXMLName, (x,y,cx,cy))
    for gf in root.findall('.//p:graphicFrame', namespaces=NS):
        chart_el = gf.find('.//a:graphic/a:graphicData/c:chart', namespaces=NS)
        if chart_el is None:
            continue
        rid = chart_el.get('{%s}id' % NS['r'])
        if not rid:
            continue
        chart_name = rid_to_chart.get(rid)
        xfrm = gf.find('p:xfrm', namespaces=NS)
        if chart_name and xfrm is not None:
            off = xfrm.find('a:off', namespaces=NS)
            ext = xfrm.find('a:ext', namespaces=NS)
            if off is not None and ext is not None:
                x = int(off.get('x', '0'))
                y = int(off.get('y', '0'))
                cx = int(ext.get('cx', '0'))
                cy = int(ext.get('cy', '0'))
                charts_pos.append((chart_name, (x, y, cx, cy)))
    # 收集所有文本 shape 及其位置与内容
    labels_pos: List[Tuple[str, Tuple[int, int, int, int]]] = []  # (text, (x,y,cx,cy))
    for sp in root.findall('.//p:sp', namespaces=NS):
        # 位置
        xfrm = sp.find('p:spPr/a:xfrm', namespaces=NS)
        if xfrm is None:
            continue
        off = xfrm.find('a:off', namespaces=NS)
        ext = xfrm.find('a:ext', namespaces=NS)
        if off is None or ext is None:
            continue
        x = int(off.get('x', '0'))
        y = int(off.get('y', '0'))
        cx = int(ext.get('cx', '0'))
        cy = int(ext.get('cy', '0'))
        # 文本
        tx = sp.find('p:txBody', namespaces=NS)
        if tx is None:
            continue
        texts = [t.text.strip() for t in tx.findall('.//a:t', namespaces=NS) if (t.text or '').strip()]
        if not texts:
            continue
        text_all = ' '.join(texts)
        # 只保留可能的渠道标签（大小写不敏感）
        for ch in channels:
            if ch.lower() in text_all.lower():
                labels_pos.append((ch, (x, y, cx, cy)))
                break
    # 简单最近邻：按矩形中心距离最近的文本 shape 作为该 chart 的渠道
    def center(box: Tuple[int, int, int, int]) -> Tuple[int, int]:
        x, y, cx, cy = box
        return x + cx // 2, y + cy // 2
    mapping: Dict[str, str] = {}
    for chart_name, cbox in charts_pos:
        cx, cy = center(cbox)
        best = None
        best_dist = None
        for label, lbox in labels_pos:
            lx, ly = center(lbox)
            d = (cx - lx) ** 2 + (cy - ly) ** 2
            if best is None or d < best_dist:
                best = label
                best_dist = d
        if best:
            mapping[chart_name] = best
    return mapping


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
    # 解析 slide 与 rels，建立 chart→channel 映射
    slide_xml = _resolve_unz_root() / 'ppt' / 'slides' / 'slide31.xml'
    slide_rels = _resolve_unz_root() / 'ppt' / 'slides' / '_rels' / 'slide31.xml.rels'
    channel_order = list((yaml.safe_load((GEN / 'config.yaml').read_text(encoding='utf-8')).get('fill_policy') or {}).get('channel_order') or (cfg.channels.keys()))
    channel_map = _parse_slide_chart_channel_map(slide_xml, slide_rels, [str(c) for c in channel_order])

    with _connect_sqlite(cfg.output_db) as conn:
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
            if t == 'scatterChart':
                series = make_trend_lenovo_vs_others(cfg, conn)
                write_scatter_json(chart_dir, series)
            elif t == 'lineChart':
                # 优先作为小图的“渠道4周SOV（Lenovo占比）”处理；若无法映射渠道则退化为整体 SOV（单序列）
                ch = channel_map.get(xml_name or '')
                if ch:
                    labels, values = make_weekly_channel_sov_lenovo(cfg, ch)
                    if labels and values:
                        obj = {'labels': labels, 'series': [{'name': ch, 'values': values}]}
                        (chart_dir / 'data.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')
                        (chart_dir / 'final_data.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')
                        continue
                # fallback：使用整月品牌SOV单序列（与模板一致的4点可复制）
                labels_fallback, values_fallback = make_sov(cfg, conn)
                if values_fallback:
                    # 压缩/广播到4个点：用相同值填充
                    v = round(values_fallback[(cfg.brands_order.index('lenovo') if 'lenovo' in cfg.brands_order else 0)], 1)
                    obj = {'labels': ['W1', 'W2', 'W3', 'W4'], 'series': [{'name': 'Lenovo SOV', 'values': [v, v, v, v]}]}
                    (chart_dir / 'data.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')
                    (chart_dir / 'final_data.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')
                else:
                    # 空写，交由 keep_original 兜底
                    (chart_dir / 'data.json').write_text(json.dumps({'labels': [], 'series': []}, ensure_ascii=False, indent=2), encoding='utf-8')
                    (chart_dir / 'final_data.json').write_text(json.dumps({'labels': [], 'series': []}, ensure_ascii=False, indent=2), encoding='utf-8')
            elif t in ('barChart','pieChart','areaChart','doughnutChart'):
                labels, values = make_sov(cfg, conn)
                write_cat_json(chart_dir, labels, values)
            else:
                print('未知图表类型，跳过：', chart_xml)
    print('数据已生成：', ROOT)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
