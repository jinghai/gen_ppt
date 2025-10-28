#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAGES_DIR = ROOT / 'charts' / 'charts'
OUT_MD = ROOT / 'charts' / 'output' / 'audit_assets.md'
OUT_JSON = ROOT / 'charts' / 'output' / 'audit_assets.json'


def audit():
    pages = sorted([p for p in PAGES_DIR.iterdir() if p.is_dir() and re.match(r'^p\d+$', p.name)])
    report = {
        'root': str(ROOT),
        'pages_dir': str(PAGES_DIR),
        'pages': [],
        'summary': {
            'pages_count': 0,
            'charts_count': 0,
            'charts_missing_any': 0,
        }
    }
    md_lines = [
        '# Charts Assets Audit',
        '',
        f'- Root: {ROOT}',
        f'- Pages dir: {PAGES_DIR}',
        '',
        '## Pages'
    ]

    for page in pages:
        charts = sorted([c for c in page.iterdir() if c.is_dir() and re.match(r'^chart\d+$', c.name)])
        page_item = {'page': page.name, 'charts': []}
        md_lines.append(f'### {page.name}')
        for chart in charts:
            data_json = chart / 'data.json'
            final_json = chart / 'final_data.json'
            chart_path = chart / 'chart_path.txt'
            chart_xml_exists = False
            if chart_path.exists():
                try:
                    chart_xml_exists = Path(chart_path.read_text(encoding='utf-8').strip()).exists()
                except Exception:
                    chart_xml_exists = False
            orig_dir = chart / 'original'
            orig_meta = orig_dir / 'original_meta.json'
            orig_labels = orig_dir / 'original_labels.json'
            orig_series = orig_dir / 'original_series.json'
            orig_scatter = orig_dir / 'original_scatter.json'
            preview_png = chart / 'preview_original.png'
            item = {
                'chart': chart.name,
                'exists': {
                    'data.json': data_json.exists(),
                    'final_data.json': final_json.exists(),
                    'chart_path.txt': chart_path.exists(),
                    'chart_xml': chart_xml_exists,
                    'original_meta.json': orig_meta.exists(),
                    'original_labels.json': orig_labels.exists(),
                    'original_series.json': orig_series.exists(),
                    'original_scatter.json': orig_scatter.exists(),
                    'preview_original.png': preview_png.exists(),
                },
            }
            missing = [k for k, v in item['exists'].items() if not v]
            item['missing'] = missing
            page_item['charts'].append(item)
            report['summary']['charts_count'] += 1
            if missing:
                report['summary']['charts_missing_any'] += 1
            md_lines.append(f'- {chart.name}: missing {", ".join(missing) if missing else "none"}')
        report['pages'].append(page_item)
        report['summary']['pages_count'] += 1
        md_lines.append('')

    OUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    OUT_MD.write_text('\n'.join(md_lines), encoding='utf-8')
    print('Audit report written to:', OUT_MD)


if __name__ == '__main__':
    audit()