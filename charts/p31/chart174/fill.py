#!/usr/bin/env python3
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
