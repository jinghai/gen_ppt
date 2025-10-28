#!/usr/bin/env python3
import argparse
import json
import os
import re
from pathlib import Path
from collections import Counter
try:
    from lxml import etree
except Exception:
    etree = None

NS = {
    'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
}

def find_files(root: Path, pattern: str):
    return list(root.glob(pattern))

def read_text(p: Path):
    try:
        return p.read_text(encoding='utf-8')
    except Exception:
        try:
            return p.read_text(encoding='latin-1')
        except Exception:
            return ''

def chart_type_counts(charts_dir: Path):
    types = ['lineChart','barChart','pieChart','scatterChart','areaChart','doughnutChart']
    cnt = Counter()
    for chart_xml in charts_dir.glob('chart*.xml'):
        txt = read_text(chart_xml)
        for t in types:
            if f'<c:{t}' in txt:
                cnt[t] += 1
                break
    return cnt

def parse_chart_rels(chart_rels: Path):
    mapping = {}
    if chart_rels.exists():
        txt = read_text(chart_rels)
        for m in re.finditer(r'Relationship[^>]+Id="([^"]+)"[^>]+Target="([^"]+)"', txt):
            mapping[m.group(1)] = m.group(2)
    return mapping

def verify(root: Path):
    charts_dir = root / 'charts'
    slides_dir = root / 'slides'
    slides_rels_dir = slides_dir / '_rels'
    charts_rels_dir = root / 'charts' / '_rels'
    embeddings_dir = root / 'embeddings'

    chart_files = sorted([p.name for p in charts_dir.glob('chart*.xml')])
    slide_files = sorted([p.name for p in slides_dir.glob('slide*.xml')])

    # referenced charts from slides rels
    ref_charts = set()
    for rel in slides_rels_dir.glob('slide*.xml.rels'):
        txt = read_text(rel)
        for m in re.finditer(r'charts/(chart[0-9]+\.xml)', txt):
            ref_charts.add(m.group(1))

    # check each referenced chart has rels, externalData targets exist
    missing_chart = [c for c in ref_charts if not (charts_dir / c).exists()]
    missing_chart_rels = []
    missing_external_targets = []
    external_total = 0
    for c in ref_charts:
        c_xml = charts_dir / c
        c_rels = charts_rels_dir / f'{c}.rels'
        if not c_rels.exists():
            missing_chart_rels.append(c)
        else:
            # check externalData id in chart xml
            txt = read_text(c_xml)
            if '<c:externalData' in txt:
                external_total += 1
                m = re.search(r'c:externalData[^>]+r:id="([^"]+)"', txt)
                if m:
                    rId = m.group(1)
                    mapping = parse_chart_rels(c_rels)
                    target = mapping.get(rId)
                    if not target:
                        missing_external_targets.append({'chart': c, 'rId': rId, 'target': None})
                    else:
                        # normalize path relative to charts dir
                        target_path = (charts_dir / Path(target)).resolve()
                        # handle ../embeddings
                        if '..' in target:
                            target_path = (charts_rels_dir / target).resolve()
                        if not target_path.exists():
                            missing_external_targets.append({'chart': c, 'rId': rId, 'target': target})

    type_counts = chart_type_counts(charts_dir)

    report = {
        'root': str(root),
        'counts': {
            'charts_total': len(chart_files),
            'slides_total': len(slide_files),
            'charts_referenced_unique': len(ref_charts),
            'charts_referenced_list': sorted(ref_charts),
            'externalData_in_referenced': external_total,
        },
        'type_distribution': dict(type_counts),
        'issues': {
            'missing_chart_files': missing_chart,
            'missing_chart_rels': missing_chart_rels,
            'missing_external_targets': missing_external_targets,
        },
        'status': 'ok' if not (missing_chart or missing_chart_rels or missing_external_targets) else 'incomplete'
    }
    return report

def write_md(md_path: Path, report: dict):
    lines = []
    lines.append(f"# 解压完整性报告\n")
    lines.append(f"根目录: `{report['root']}`\n")
    c = report['counts']
    lines.append(f"- 图表总数: {c['charts_total']}\n")
    lines.append(f"- 幻灯片总数: {c['slides_total']}\n")
    lines.append(f"- 被引用唯一图表数: {c['charts_referenced_unique']}\n")
    lines.append(f"- 被引用图表列表: {', '.join(c['charts_referenced_list'])}\n")
    lines.append(f"- 引用 externalData 的图表数: {c['externalData_in_referenced']}\n")
    lines.append("\n## 类型分布\n")
    for t, n in sorted(report['type_distribution'].items(), key=lambda x: -x[1]):
        lines.append(f"- {t}: {n}\n")
    lines.append("\n## 问题\n")
    issues = report['issues']
    lines.append(f"- 缺失图表文件: {len(issues['missing_chart_files'])} -> {issues['missing_chart_files']}\n")
    lines.append(f"- 缺失图表关系(.rels): {len(issues['missing_chart_rels'])} -> {issues['missing_chart_rels']}\n")
    lines.append(f"- 缺失 externalData 目标: {len(issues['missing_external_targets'])} -> {issues['missing_external_targets']}\n")
    lines.append(f"\n状态: {report['status']}\n")
    md_path.write_text(''.join(lines), encoding='utf-8')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True, help='解压根目录，如 ppt/input/LRTBH-unzip')
    ap.add_argument('--out', required=True, help='输出 JSON 报告路径')
    args = ap.parse_args()
    root = Path(args.root)
    out_json = Path(args.out)
    out_md = out_json.with_suffix('.md')
    report = verify(root)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    write_md(out_md, report)
    print(f"written: {out_json}")
    print(f"written: {out_md}")
    if report['status'] != 'ok':
        print('status: incomplete')

if __name__ == '__main__':
    main()