#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
根据 charts/output/index_from_pptx.json 自动为 charts/charts 下的各页面（除 p10）生成：
- 每个图表的目录 chartN/，包含 chart_path.txt 与统一 fill.py
- 每页的 make_data.py：按图表类型生成数据（类别：SOV；散点/线：日级趋势）
- 每页的 build_all.py：运行 make_data 并依次执行所有 chart 的 fill
- 每页的 config.yaml：写入 output.replace_charts 与 final_mode=updated

依赖：
- charts/tools/fill_chart_xml.py
- ppt/config.yaml 中的 channels、brands、fill_policy（axis_day_base等）
- 图表 XML 来自 ppt/input/LRTBH-unzip/ppt/charts
- 指标库 data/metrics_v5.db，口径配置 compute_metrics.yaml
"""
from __future__ import annotations
import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import yaml


def _find_root(start: Path) -> Path:
    p = start
    while p.parent != p:
        if (p / 'config.yaml').exists() and (p / 'input').exists():
            return p
        p = p.parent
    return start

TOOLS_DIR = Path(__file__).resolve().parent
ROOT = _find_root(TOOLS_DIR)
CHARTS_ROOT = ROOT / 'charts'

def _resolve_unz_root() -> Path:
    try:
        cfg = yaml.safe_load((ROOT / 'config.yaml').read_text(encoding='utf-8')) or {}
    except Exception:
        cfg = {}
    tr = (cfg.get('project') or {}).get('template_root', 'input/LRTBH-unzip')
    p = Path(tr)
    if not p.is_absolute():
        p = ROOT / tr
    return p

def _charts_dir(unz: Path) -> Path:
    d = unz / 'ppt' / 'charts'
    return d if d.exists() else unz / 'charts'

UNZIP_ROOT = _resolve_unz_root()
def _index_json_path() -> Path:
    candidates = [
        ROOT / 'output' / 'index_from_pptx.json',
        ROOT / 'charts' / 'output' / 'index_from_pptx.json',
    ]
    for c in candidates:
        if c.exists():
            return c
    # 默认返回新结构路径（若不存在由调用处报错）
    return candidates[0]

INDEX_JSON = _index_json_path()
GLOBAL_CFG = ROOT / 'config.yaml'
TOOLS_DIR = ROOT / 'tools'

FILL_TEMPLATE = """#!/usr/bin/env python3
import json
from pathlib import Path
import sys
from lxml import etree

TOOL_CANDIDATES = [
    Path(__file__).resolve().parents[3] / 'tools',
    Path(__file__).resolve().parents[2] / 'tools',
]
for tc in TOOL_CANDIDATES:
    if tc.exists():
        sys.path.append(str(tc))
from fill_chart_xml import fill_chart  # type: ignore

NS = {
  'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart',
}

ROOT = Path(__file__).resolve().parents[0]


def _chart_type(chart_xml: Path) -> str:
    tree = etree.parse(str(chart_xml))
    plot = tree.getroot().find('c:chart/c:plotArea', namespaces=NS)
    for t in ['scatterChart','lineChart','barChart','pieChart','areaChart','doughnutChart']:
        el = plot.find(f'c:{t}', namespaces=NS) if plot is not None else None
        if el is not None:
            return t
    return 'unknown'


def _load_cat_json(fp: Path):
    try:
        data = json.loads(fp.read_text(encoding='utf-8'))
    except Exception:
        return [], []
    labels = []
    series = []
    if isinstance(data, dict):
        labels = data.get('labels') or []
        sr = data.get('series') or []
        if sr:
            if isinstance(sr[0], dict):
                series = [s.get('values', []) for s in sr]
            elif isinstance(sr[0], (int, float)):
                series = [sr]
            else:
                series = sr
    elif isinstance(data, list):
        if data and isinstance(data[0], (int, float)):
            series = [data]
        else:
            series = data
    return labels, series


def _load_scatter_json(fp: Path):
    try:
        data = json.loads(fp.read_text(encoding='utf-8'))
    except Exception:
        return []
    series = []
    if isinstance(data, dict) and 'scatter_series' in data:
        arr = data.get('scatter_series') or []
        for s in arr:
            y = s.get('y') or [p[1] for p in (s.get('points') or [])]
            series.append(y)
    elif isinstance(data, list):
        for s in data:
            if isinstance(s, dict):
                y = s.get('y') or [p[1] for p in (s.get('points') or [])]
                series.append(y)
            elif isinstance(s, (int, float)):
                series = [data]
                break
    return series


def main():
    chart_path = Path((ROOT / 'chart_path.txt').read_text(encoding='utf-8').strip())
    t = _chart_type(chart_path)
    final_json = ROOT / 'final_data.json'
    data_json = ROOT / 'data.json'
    src_desc = None
    if final_json.exists():
        src_desc = final_json
    elif data_json.exists():
        src_desc = data_json
    else:
        raise FileNotFoundError('缺少数据：final_data.json 或 data.json')
    labels = None
    series = []
    if t == 'scatterChart':
        series = _load_scatter_json(src_desc)
    else:
        labels, series = _load_cat_json(src_desc)
    fill_chart(chart_path, series, labels)
    print('filled', chart_path.name, 'from', src_desc)

if __name__ == '__main__':
    main()
"""

MAKE_DATA_TEMPLATE = '''#!/usr/bin/env python3
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
'''

BUILD_ALL_TEMPLATE = """#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
import subprocess
import re

ROOT = Path(__file__).resolve().parent


def run_make_data():
    sys.path.append(str(ROOT))
    import make_data as make_data_mod  # type: ignore
    try:
        rc = make_data_mod.main()
        print('make_data.py finished with code', rc)
    except Exception as e:
        print('make_data.py failed:', e)


def run_fillers():
    for chart_dir in sorted([p for p in ROOT.iterdir() if p.is_dir() and re.match(r'^chart\d+$', p.name)]):
        try:
            subprocess.run([sys.executable, str(chart_dir / 'fill.py')], check=True)
        except Exception as e:
            print('filler failed for', chart_dir, e)


def main():
    ap = argparse.ArgumentParser(description='page build_all: run data generation and fill charts')
    ap.add_argument('--mode', choices=['modified','original','both'], default='both')
    args = ap.parse_args()
    run_make_data()
    run_fillers()
    print(ROOT.name, 'build_all done, mode =', args.mode)

if __name__ == '__main__':
    main()
"""


def _load_index() -> Dict[int, List[str]]:
    idx = json.loads(INDEX_JSON.read_text(encoding='utf-8'))
    mapping: Dict[int, List[str]] = {}
    for s in idx.get('slides', []):
        mapping[int(s.get('slide'))] = [str(x) for x in (s.get('charts') or [])]
    return mapping


def _page_number(name: str) -> int | None:
    m = re.match(r'^p(\d+)$', name)
    return int(m.group(1)) if m else None


def _ensure_page_config(page_dir: Path, chart_names: List[str]):
    cfg_path = page_dir / 'config.yaml'
    payload = {
        'output': {
            'replace_charts': chart_names,
            'final_mode': 'updated',
        },
        'fill_policy': {
            'axis_day_base': 20300,
        },
    }
    cfg_path.write_text(yaml.safe_dump(payload, allow_unicode=True, sort_keys=False), encoding='utf-8')


def _ensure_chart_dir(page_dir: Path, chart_name: str):
    num = chart_name.replace('chart','').replace('.xml','')
    chart_dir = page_dir / f'chart{num}'
    chart_dir.mkdir(parents=True, exist_ok=True)
    # chart_path.txt
    (chart_dir / 'chart_path.txt').write_text(str(_charts_dir(UNZIP_ROOT) / chart_name), encoding='utf-8')
    # fill.py
    (chart_dir / 'fill.py').write_text(FILL_TEMPLATE, encoding='utf-8')


def scaffold_pages():
    if not CHARTS_ROOT.exists():
        raise FileNotFoundError(CHARTS_ROOT)
    idx = _load_index()
    for page in CHARTS_ROOT.iterdir():
        if not page.is_dir():
            continue
        if page.name == 'p10':
            continue
        pno = _page_number(page.name)
        if not pno:
            continue
        chart_list = idx.get(pno) or []
        if not chart_list:
            # 仍然写入空 config 以参与最终合成（不替换任何图表）
            _ensure_page_config(page, [])
            # 写入 make_data/build_all（无图表时运行也不报错）
            (page / 'make_data.py').write_text(MAKE_DATA_TEMPLATE, encoding='utf-8')
            (page / 'build_all.py').write_text(BUILD_ALL_TEMPLATE, encoding='utf-8')
            print('页面无图表，保留占位：', page.name)
            continue
        _ensure_page_config(page, chart_list)
        # 生成 chart 目录与脚本
        for ch in chart_list:
            _ensure_chart_dir(page, ch)
        # make_data/build_all
        (page / 'make_data.py').write_text(MAKE_DATA_TEMPLATE, encoding='utf-8')
        (page / 'build_all.py').write_text(BUILD_ALL_TEMPLATE, encoding='utf-8')
        print('完成页面脚手架：', page.name, 'charts=', chart_list)


if __name__ == '__main__':
    scaffold_pages()