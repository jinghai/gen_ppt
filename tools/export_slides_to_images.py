#!/usr/bin/env python3
import sys
import zipfile
import shutil
import subprocess
from pathlib import Path
from typing import Optional
import yaml
from lxml import etree as ET


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / 'config.yaml'


def _cfg_value(section: str, key: str, default: str) -> Path:
    try:
        cfg = yaml.safe_load(CONFIG.read_text(encoding='utf-8')) or {}
    except Exception:
        cfg = {}
    proj = cfg.get('project') or {}
    val = proj.get(key, default) if section == 'project' else default
    p = Path(val)
    if not p.is_absolute():
        p = ROOT / p
    return p


TPL = _cfg_value('project', 'original_ppt', 'input/LRTBH.pptx')
UNZ = _cfg_value('project', 'template_root', 'input/LRTBH-unzip')
TMP_DIR = ROOT / 'tmp'
SLIDES_WORK = TMP_DIR / '_slides'


APP_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Office PowerPoint</Application>
</Properties>
'''


def _load_tpl_parts():
    with zipfile.ZipFile(TPL, 'r') as tpl:
        pres_rels_bytes = tpl.read('ppt/_rels/presentation.xml.rels')
        pres_xml_bytes = tpl.read('ppt/presentation.xml')
        ct_bytes = tpl.read('[Content_Types].xml')
    return pres_rels_bytes, pres_xml_bytes, ct_bytes


def _filter_pres_rels(rels_bytes: bytes, slide_no: int):
    root = ET.fromstring(rels_bytes)
    new_root = ET.Element('Relationships', xmlns='http://schemas.openxmlformats.org/package/2006/relationships')
    slide_rel_id = None
    for rel in root.findall('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
        t = rel.get('Target') or ''
        typ = rel.get('Type') or ''
        if typ.endswith('/slide') and t == f'slides/slide{slide_no}.xml':
            slide_rel_id = rel.get('Id')
            e = ET.SubElement(new_root, 'Relationship')
            for k, v in rel.attrib.items():
                e.set(k, v)
            e.set('Target', 'slides/slide1.xml')
        elif not typ.endswith('/slide'):
            e = ET.SubElement(new_root, 'Relationship')
            for k, v in rel.attrib.items():
                e.set(k, v)
    return ET.tostring(new_root, xml_declaration=True, encoding='UTF-8', standalone="yes"), slide_rel_id


def _filter_pres_xml(pres_bytes: bytes, slide_rel_id: Optional[str]):
    NS = {
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
        'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    }
    tree = ET.fromstring(pres_bytes)
    sldIdLst = tree.find('{%s}sldIdLst' % NS['p'])
    if sldIdLst is None:
        sldIdLst = ET.SubElement(tree, '{%s}sldIdLst' % NS['p'])
    for ch in list(sldIdLst):
        sldIdLst.remove(ch)
    ET.SubElement(sldIdLst, '{%s}sldId' % NS['p'], attrib={'id': '256', '{%s}id' % NS['r']: slide_rel_id or 'rId1'})
    return ET.tostring(tree, xml_declaration=True, encoding='UTF-8', standalone="yes")


def _filter_content_types(ct_bytes: bytes):
    ct = ET.fromstring(ct_bytes)
    ns_ct = 'http://schemas.openxmlformats.org/package/2006/content-types'
    for o in list(ct.findall('{%s}Override' % ns_ct)):
        part = o.get('PartName') or ''
        if part.startswith('/ppt/slides/slide'):
            ct.remove(o)
    ET.SubElement(ct, '{%s}Override' % ns_ct, PartName='/ppt/slides/slide1.xml', ContentType='application/vnd.openxmlformats-officedocument.presentationml.slide+xml')
    has_app = any((o.get('PartName') == '/docProps/app.xml') for o in ct.findall('{%s}Override' % ns_ct))
    if not has_app:
        ET.SubElement(ct, '{%s}Override' % ns_ct, PartName='/docProps/app.xml', ContentType='application/vnd.openxmlformats-officedocument.extended-properties+xml')
    return ET.tostring(ct, xml_declaration=True, encoding='UTF-8', standalone="yes")


def build_single_slide_pptx(slide_no: int, out_pptx: Path):
    SLIDES_WORK.mkdir(parents=True, exist_ok=True)
    pres_rels_bytes, pres_xml_bytes, ct_bytes = _load_tpl_parts()

    charts_dir = (UNZ / 'ppt' / 'charts') if (UNZ / 'ppt' / 'charts').exists() else (UNZ / 'charts')
    charts_rels_dir = charts_dir / '_rels'

    charts_fallback = {}
    if charts_dir.exists():
        for chart_file in charts_dir.glob('chart*.xml'):
            charts_fallback[chart_file.name] = chart_file.read_bytes()
        for rels_file in charts_rels_dir.glob('chart*.xml.rels'):
            charts_fallback[f'rels:{rels_file.name}'] = rels_file.read_bytes()

    new_pres_rels_xml, slide_rel_id = _filter_pres_rels(pres_rels_bytes, slide_no)
    new_pres_xml = _filter_pres_xml(pres_xml_bytes, slide_rel_id)
    new_ct_xml = _filter_content_types(ct_bytes)

    with zipfile.ZipFile(TPL, 'r') as tpl:
        with zipfile.ZipFile(out_pptx, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            for name in tpl.namelist():
                if name.startswith('ppt/slides/slide') and name != f'ppt/slides/slide{slide_no}.xml':
                    continue
                if name.startswith('ppt/slides/_rels/slide') and name != f'ppt/slides/_rels/slide{slide_no}.xml.rels':
                    continue
                if name == 'ppt/_rels/presentation.xml.rels':
                    z.writestr(name, new_pres_rels_xml)
                elif name == 'ppt/presentation.xml':
                    z.writestr(name, new_pres_xml)
                elif name == '[Content_Types].xml':
                    z.writestr(name, new_ct_xml)
                elif name == f'ppt/slides/slide{slide_no}.xml':
                    z.writestr('ppt/slides/slide1.xml', tpl.read(name))
                elif name == f'ppt/slides/_rels/slide{slide_no}.xml.rels':
                    z.writestr('ppt/slides/_rels/slide1.xml.rels', tpl.read(name))
                elif name.startswith('ppt/charts/chart') and name.endswith('.xml'):
                    chart_name = name.split('/')[-1]
                    fallback_data = charts_fallback.get(chart_name)
                    z.writestr(name, fallback_data if fallback_data is not None else tpl.read(name))
                elif name.startswith('ppt/charts/_rels/chart') and name.endswith('.xml.rels'):
                    rels_name = name.split('/')[-1]
                    fallback_data = charts_fallback.get(f'rels:{rels_name}')
                    z.writestr(name, fallback_data if fallback_data is not None else tpl.read(name))
                else:
                    z.writestr(name, tpl.read(name))
            if 'docProps/app.xml' not in tpl.namelist():
                z.writestr('docProps/app.xml', APP_XML)


def export_images(out_pattern: str = 'p{num}.png', size: int = 1920):
    slides_dir = UNZ / 'ppt' / 'slides'
    if not slides_dir.exists():
        slides_dir = UNZ / 'slides'
    slide_files = sorted([p for p in slides_dir.glob('slide*.xml')], key=lambda p: int(p.stem.replace('slide','')))
    if not slide_files:
        print('No slides found in', slides_dir)
        sys.exit(2)
    SLIDES_WORK.mkdir(parents=True, exist_ok=True)
    TMP_DIR.mkdir(parents=True, exist_ok=True)

    # 1) build single-slide pptx for each slide
    built = []
    for sf in slide_files:
        num = int(sf.stem.replace('slide',''))
        out_pptx = SLIDES_WORK / f'slide{num}.pptx'
        print(f'Build single-slide PPTX for slide {num} -> {out_pptx.name}')
        build_single_slide_pptx(num, out_pptx)
        built.append((num, out_pptx))

    # 2) generate thumbnails via qlmanage
    for num, pptx_path in built:
        print(f'Generate image for slide {num}')
        subprocess.run(['qlmanage', '-t', '-s', str(size), '-o', str(SLIDES_WORK), str(pptx_path)], check=True)
        # qlmanage outputs e.g. slideN.pptx.png
        src_img = SLIDES_WORK / f'{pptx_path.name}.png'
        if not src_img.exists():
            # fallback TIFF
            tiff_img = SLIDES_WORK / f'{pptx_path.name}.tiff'
            if tiff_img.exists():
                # convert tiff to png via sips
                png_tmp = SLIDES_WORK / f'{pptx_path.name}.png'
                subprocess.run(['sips', '-s', 'format', 'png', str(tiff_img), '--out', str(png_tmp)], check=True)
                src_img = png_tmp
        dst_name = out_pattern.format(num=num)
        dst_path = TMP_DIR / dst_name
        shutil.move(str(src_img), str(dst_path))
        print(f'Wrote {dst_path}')


def main():
    # Usage: python tools/export_slides_to_images.py [--size 1920] [--pattern p{num}.png]
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--size', type=int, default=1920, help='export image size (pixels)')
    ap.add_argument('--pattern', type=str, default='p{num}.png', help='output filename pattern, use {num} as slide number placeholder')
    args = ap.parse_args()
    export_images(out_pattern=args.pattern, size=args.size)


if __name__ == '__main__':
    main()