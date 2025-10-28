#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path

SLIDE_RE = re.compile(r'slide([0-9]+)\.xml')
CHART_RE = re.compile(r'charts/(chart[0-9]+\.xml)')

# Parse slides/_rels to map slide -> charts

def parse_slide_chart_map(slides_rels_dir: Path):
    mapping = {}
    for rel in sorted(slides_rels_dir.glob('slide*.xml.rels')):
        txt = rel.read_text(encoding='utf-8', errors='ignore')
        slide_m = SLIDE_RE.search(rel.name)
        if not slide_m:
            continue
        slide_no = int(slide_m.group(1))
        charts = CHART_RE.findall(txt)
        mapping[slide_no] = sorted(set(charts))
    return mapping

# Extract chart meta: type and external target

def chart_meta(charts_dir: Path, chart_rels_dir: Path, chart_name: str):
    meta = {'name': chart_name, 'type': None, 'external': None}
    c_xml = charts_dir / chart_name
    types = ['lineChart','barChart','pieChart','scatterChart','areaChart','doughnutChart']
    txt = c_xml.read_text(encoding='utf-8', errors='ignore')
    for t in types:
        if f'<c:{t}' in txt:
            meta['type'] = t
            break
    # externalData id
    m = re.search(r'c:externalData[^>]+r:id="([^"]+)"', txt)
    if m:
        rId = m.group(1)
        rels = chart_rels_dir / f'{chart_name}.rels'
        if rels.exists():
            rel_txt = rels.read_text(encoding='utf-8', errors='ignore')
            mm = re.search(rf'Id="{re.escape(rId)}"[^>]+Target="([^"]+)"', rel_txt)
            if mm:
                meta['external'] = mm.group(1)
    return meta


def build_index(root: Path):
    slides_rels_dir = root / 'slides' / '_rels'
    charts_dir = root / 'charts'
    chart_rels_dir = charts_dir / '_rels'
    slide_chart = parse_slide_chart_map(slides_rels_dir)
    index = {
        'root': str(root),
        'slides': [],
    }
    for slide_no, charts in sorted(slide_chart.items()):
        entry = {
            'slide': slide_no,
            'charts': [],
        }
        for c in charts:
            entry['charts'].append(chart_meta(charts_dir, chart_rels_dir, c))
        index['slides'].append(entry)
    return index


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    root = Path(args.root)
    out = Path(args.out)
    idx = build_index(root)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(idx, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'written: {out}')

if __name__ == '__main__':
    main()