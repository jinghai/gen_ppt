#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET
import yaml

# 解析 gen_ppt 根目录（需包含 config.yaml 与 input）
def _find_root(start: Path) -> Path:
    p = start
    while p.parent != p:
        if (p / 'config.yaml').exists() and (p / 'input').exists():
            return p
        p = p.parent
    return start

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = _find_root(SCRIPT_DIR)
CONFIG = ROOT / 'config.yaml'

CHART_REL_TYPE = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/chart'


def load_original_ppt() -> Path:
    if CONFIG.exists():
        try:
            cfg = yaml.safe_load(CONFIG.read_text(encoding='utf-8')) or {}
            val = (cfg.get('project') or {}).get('original_ppt')
            if val:
                p = Path(val)
                return p if p.is_absolute() else ROOT / val
        except Exception:
            pass
    return ROOT / 'input' / 'LRTBH.pptx'


def parse_index_from_pptx(pptx_path: Path) -> dict:
    if not pptx_path.exists():
        raise FileNotFoundError(pptx_path)
    slides = []
    with zipfile.ZipFile(pptx_path, 'r') as z:
        slide_names = sorted([n for n in z.namelist() if n.startswith('ppt/slides/slide') and n.endswith('.xml')])
        for slide_xml_name in slide_names:
            snum = int(Path(slide_xml_name).stem.replace('slide', ''))
            rel_name = f"ppt/slides/_rels/slide{snum}.xml.rels"
            charts = []
            if rel_name in z.namelist():
                rel_xml = z.read(rel_name)
                try:
                    root = ET.fromstring(rel_xml)
                    for rel in root.findall('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
                        rtype = rel.get('Type')
                        target = rel.get('Target')
                        if rtype == CHART_REL_TYPE and target:
                            if 'charts/' in target:
                                charts.append(Path(target).name)
                except Exception:
                    pass
            slides.append({'slide': snum, 'charts': charts})
    slides.sort(key=lambda s: s['slide'])
    return {'root': str(pptx_path), 'slides': slides}


def main():
    ap = argparse.ArgumentParser(description='Parse slides->charts index from original PPTX')
    ap.add_argument('--pptx', help='PPTX path, defaults to config.yaml project.original_ppt')
    ap.add_argument('--out', required=True, help='Output JSON path')
    args = ap.parse_args()
    pptx = Path(args.pptx) if args.pptx else load_original_ppt()
    index = parse_index_from_pptx(pptx)
    out_path = ROOT / args.out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding='utf-8')
    print('written:', out_path)


if __name__ == '__main__':
    main()