#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
审计指定页面（如 p8..p31）的图表与脚本资产：
- 顶层：build_all.py, build_original.py, build.py, config.yaml, gen_preview.py, make_data.py, readme.md, validate.py
- 图表：data.json, final_data.json, chart_path.txt, chart XML 可访问
- 原始缓存 original_*：同时兼容 chart 根目录与 original/ 子目录，记录位置与存在情况
输出：charts/output/audit_subset.json 与 audit_subset.md
"""
import json
import re
import sys
from pathlib import Path
from typing import List, Dict, Any

ROOT = Path(__file__).resolve().parents[2]
PAGES_DIR = ROOT / 'charts' / 'charts'
OUT_MD = ROOT / 'charts' / 'output' / 'audit_subset.md'
OUT_JSON = ROOT / 'charts' / 'output' / 'audit_subset.json'

# 允许导入同目录工具以解析 chart XML 类型
TOOLS_DIR = Path(__file__).resolve().parent
sys.path.append(str(TOOLS_DIR))
from extract_chart_cache import parse_chart_xml  # type: ignore

REQUIRED_TOP = [
    'build_all.py','build_original.py','build.py','config.yaml',
    'gen_preview.py','make_data.py','readme.md','validate.py'
]


def _exists_original(chart_dir: Path) -> Dict[str, Any]:
    # 兼容两种布局：根目录与 original/ 子目录
    root_files = {
        'original_meta.json': chart_dir / 'original_meta.json',
        'original_labels.json': chart_dir / 'original_labels.json',
        'original_series.json': chart_dir / 'original_series.json',
        'original_scatter.json': chart_dir / 'original_scatter.json',
    }
    subdir = chart_dir / 'original'
    sub_files = {
        'original_meta.json': subdir / 'original_meta.json',
        'original_labels.json': subdir / 'original_labels.json',
        'original_series.json': subdir / 'original_series.json',
        'original_scatter.json': subdir / 'original_scatter.json',
    }
    exists_root = {k: p.exists() for k, p in root_files.items()}
    exists_sub = {k: p.exists() for k, p in sub_files.items()}
    any_root = any(exists_root.values())
    any_sub = any(exists_sub.values())
    location = 'none'
    if any_root and any_sub:
        location = 'both'
    elif any_sub:
        location = 'subdir'
    elif any_root:
        location = 'root'
    return {
        'location': location,
        'root': exists_root,
        'subdir': exists_sub,
        'exists': {k: (exists_root[k] or exists_sub[k]) for k in root_files.keys()},
    }


def audit_subset(pages: List[str]) -> Dict[str, Any]:
    pages = sorted(pages, key=lambda x: int(x[1:]) if x.startswith('p') else x)
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
        '# Charts Assets Audit (subset)',
        '',
        f'- Root: {ROOT}',
        f'- Pages dir: {PAGES_DIR}',
        '',
        '## Pages'
    ]
    for pname in pages:
        page = PAGES_DIR / pname
        charts = sorted([c for c in page.iterdir() if c.is_dir() and re.match(r'^chart\d+$', c.name)])
        top = {fn: (page / fn).exists() for fn in REQUIRED_TOP}
        page_item = {'page': page.name, 'top_level': top, 'charts': []}
        md_lines.append(f'### {page.name}')
        md_lines.append('- Top-level: ' + ', '.join([f"{k}={'OK' if v else 'MISS'}" for k, v in top.items()]))
        for chart in charts:
            data_json = chart / 'data.json'
            final_json = chart / 'final_data.json'
            chart_path = chart / 'chart_path.txt'
            chart_xml_exists = False
            chart_type: str | None = None
            xml_path: Path | None = None
            if chart_path.exists():
                try:
                    target = chart_path.read_text(encoding='utf-8').strip()
                    xml_path = Path(target)
                    chart_xml_exists = xml_path.exists()
                    if chart_xml_exists:
                        try:
                            parsed = parse_chart_xml(xml_path.read_bytes())
                            chart_type = parsed.get('chart_type')
                        except Exception:
                            chart_type = None
                except Exception:
                    chart_xml_exists = False
                    chart_type = None
            orig = _exists_original(chart)
            preview_png = chart / 'preview_original.png'
            # 仅针对图表类型所需 original_* 文件计算缺失
            required_original = ['original_meta.json']
            if chart_type == 'scatterChart':
                required_original += ['original_scatter.json']
            else:
                required_original += ['original_labels.json', 'original_series.json']
            base_required = ['data.json','final_data.json','chart_path.txt','chart_xml','preview_original.png']
            exists_map = {
                'data.json': data_json.exists(),
                'final_data.json': final_json.exists(),
                'chart_path.txt': chart_path.exists(),
                'chart_xml': chart_xml_exists,
                'preview_original.png': preview_png.exists(),
                **orig['exists'],
            }
            missing = [k for k in base_required + required_original if not exists_map.get(k, False)]
            item = {
                'chart': chart.name,
                'chart_type': chart_type,
                'exists': exists_map,
                'original_location': orig['location'],
                'missing': missing,
            }
            page_item['charts'].append(item)
            report['summary']['charts_count'] += 1
            if missing:
                report['summary']['charts_missing_any'] += 1
            md_lines.append(f"- {chart.name} (type={chart_type or 'unknown'}): missing {', '.join(missing) if missing else 'none'}; original_location={orig['location']}")
        report['pages'].append(page_item)
        report['summary']['pages_count'] += 1
        md_lines.append('')
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    OUT_MD.write_text('\n'.join(md_lines), encoding='utf-8')
    return report


if __name__ == '__main__':
    # 默认审计 p8..p31（跳过 p20）
    subset = [f'p{i}' for i in [8,10,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,29,30,31]]
    rep = audit_subset(subset)
    print(json.dumps(rep['summary'], ensure_ascii=False, indent=2))