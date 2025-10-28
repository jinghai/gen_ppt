#!/usr/bin/env python3
import zipfile
from pathlib import Path
import yaml
from lxml import etree as ET
from typing import Optional

SLIDE_NO = 13
BASE = Path(__file__).resolve().parents[2]
def _resolve_tpl() -> Path:
    try:
        cfg = yaml.safe_load((BASE / 'config.yaml').read_text(encoding='utf-8')) or {}
    except Exception:
        cfg = {}
    op = (cfg.get('project') or {}).get('original_ppt', 'input/LRTBH.pptx')
    p = Path(op)
    if not p.is_absolute():
        p = BASE / op
    return p

TPL = _resolve_tpl()

def _resolve_unz_root() -> Path:
    try:
        cfg = yaml.safe_load((BASE / 'config.yaml').read_text(encoding='utf-8')) or {}
    except Exception:
        cfg = {}
    tr = (cfg.get('project') or {}).get('template_root', 'input/LRTBH-unzip')
    p = Path(tr)
    if not p.is_absolute():
        p = BASE / tr
    return p

UNZ = _resolve_unz_root()
OUT = BASE / 'output' / f'p{SLIDE_NO}.pptx'

APP_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Office PowerPoint</Application>
</Properties>
'''

CHARTS_DIR = (UNZ / 'ppt' / 'charts') if (UNZ / 'ppt' / 'charts').exists() else (UNZ / 'charts')
CHARTS_RELS_DIR = CHARTS_DIR / '_rels'

def build():
    # 使用完整模板复制并仅保留第13页，同时替换图表（如有）
    with zipfile.ZipFile(TPL, 'r') as tpl:
        pres_rels_bytes = tpl.read('ppt/_rels/presentation.xml.rels')
        pres_xml_bytes = tpl.read('ppt/presentation.xml')
        ct_bytes = tpl.read('[Content_Types].xml')
        
        # 预加载模板中的图表及关系（作为回退）
        chart10_tpl = tpl.read('ppt/charts/chart10.xml')
        chart11_tpl = tpl.read('ppt/charts/chart11.xml')
        chart10_rels_tpl = tpl.read('ppt/charts/_rels/chart10.xml.rels')
        chart11_rels_tpl = tpl.read('ppt/charts/_rels/chart11.xml.rels')

    # 使用缓存的图表文件（如果存在）
    chart10_bytes = (CHARTS_DIR / 'chart10.xml').read_bytes() if (CHARTS_DIR / 'chart10.xml').exists() else chart10_tpl
    chart11_bytes = (CHARTS_DIR / 'chart11.xml').read_bytes() if (CHARTS_DIR / 'chart11.xml').exists() else chart11_tpl
    chart10_rels_bytes = (CHARTS_RELS_DIR / 'chart10.xml.rels').read_bytes() if (CHARTS_RELS_DIR / 'chart10.xml.rels').exists() else chart10_rels_tpl
    chart11_rels_bytes = (CHARTS_RELS_DIR / 'chart11.xml.rels').read_bytes() if (CHARTS_RELS_DIR / 'chart11.xml.rels').exists() else chart11_rels_tpl

    # 过滤 presentation.rels：仅保留 slide13（重定向到 slide1）与非 slide 关系
    def filter_pres_rels(rels_bytes: bytes):
        root = ET.fromstring(rels_bytes)
        new_root = ET.Element('Relationships', xmlns='http://schemas.openxmlformats.org/package/2006/relationships')
        slide_rel_id = None
        for rel in root.findall('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
            t = rel.get('Target') or ''
            typ = rel.get('Type') or ''
            if typ.endswith('/slide') and t == f'slides/slide{SLIDE_NO}.xml':
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

    # 过滤 presentation.xml：只保留对应 slide 的 sldId
    def filter_pres_xml(pres_bytes: bytes, slide_rel_id: Optional[str]):
        tree = ET.fromstring(pres_bytes)
        sldIdLst = tree.find('{http://schemas.openxmlformats.org/presentationml/2006/main}sldIdLst')
        if sldIdLst is None:
            sldIdLst = ET.SubElement(tree, '{http://schemas.openxmlformats.org/presentationml/2006/main}sldIdLst')
        for ch in list(sldIdLst):
            sldIdLst.remove(ch)
        ET.SubElement(sldIdLst, '{http://schemas.openxmlformats.org/presentationml/2006/main}sldId', attrib={'id': '256', '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id': slide_rel_id or 'rId1'})
        return ET.tostring(tree, xml_declaration=True, encoding='UTF-8', standalone="yes")

    # 过滤 Content_Types：仅保留 slide1 覆盖项，并补充 docProps/app.xml 覆盖
    def filter_content_types(ct_bytes: bytes):
        ct = ET.fromstring(ct_bytes)
        ns_ct = 'http://schemas.openxmlformats.org/package/2006/content-types'
        for o in list(ct.findall('{%s}Override' % ns_ct)):
            part = o.get('PartName') or ''
            if part.startswith('/ppt/slides/slide'):
                ct.remove(o)
        ET.SubElement(ct, '{%s}Override' % ns_ct, PartName='/ppt/slides/slide1.xml', ContentType='application/vnd.openxmlformats-officedocument.presentationml.slide+xml')
        ET.SubElement(ct, '{%s}Override' % ns_ct, PartName='/docProps/app.xml', ContentType='application/vnd.openxmlformats-officedocument.extended-properties+xml')
        return ET.tostring(ct, xml_declaration=True, encoding='UTF-8', standalone="yes")

    new_pres_rels_xml, slide_rel_id = filter_pres_rels(pres_rels_bytes)
    new_pres_xml = filter_pres_xml(pres_xml_bytes, slide_rel_id)
    new_ct_xml = filter_content_types(ct_bytes)

    with zipfile.ZipFile(TPL, 'r') as tpl:
        with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
            for name in tpl.namelist():
                if name.startswith('ppt/slides/slide') and name != f'ppt/slides/slide{SLIDE_NO}.xml':
                    continue
                if name.startswith('ppt/slides/_rels/slide') and name != f'ppt/slides/_rels/slide{SLIDE_NO}.xml.rels':
                    continue
                if name == 'ppt/_rels/presentation.xml.rels':
                    z.writestr(name, new_pres_rels_xml)
                elif name == 'ppt/presentation.xml':
                    z.writestr(name, new_pres_xml)
                elif name == '[Content_Types].xml':
                    z.writestr(name, new_ct_xml)
                elif name == f'ppt/slides/slide{SLIDE_NO}.xml':
                    # 重命名为 slide1.xml
                    z.writestr('ppt/slides/slide1.xml', tpl.read(name))
                elif name == f'ppt/slides/_rels/slide{SLIDE_NO}.xml.rels':
                    # 重命名为 slide1.xml.rels
                    z.writestr('ppt/slides/_rels/slide1.xml.rels', tpl.read(name))
                elif name == 'ppt/charts/chart10.xml':
                    z.writestr(name, chart10_bytes)
                elif name == 'ppt/charts/chart11.xml':
                    z.writestr(name, chart11_bytes)
                elif name == 'ppt/charts/_rels/chart10.xml.rels':
                    z.writestr(name, chart10_rels_bytes)
                elif name == 'ppt/charts/_rels/chart11.xml.rels':
                    z.writestr(name, chart11_rels_bytes)
                else:
                    z.writestr(name, tpl.read(name))
            if 'docProps/app.xml' not in tpl.namelist():
                z.writestr('docProps/app.xml', APP_XML)

    print('Built', OUT)

import subprocess, sys, re

def run_make_data():
    page_dir = Path(__file__).resolve().parent
    script = page_dir / 'make_data.py'
    if script.exists():
        print(f'[p{SLIDE_NO}] run make_data.py')
        subprocess.run([sys.executable, str(script)], check=True, cwd=str(page_dir))
    else:
        print(f'[p{SLIDE_NO}] skip make_data.py (not found)')

def run_fillers():
    page_dir = Path(__file__).resolve().parent
    chart_dirs = sorted([d for d in page_dir.iterdir() if d.is_dir() and re.match(r'^chart\d+$', d.name)])
    for d in chart_dirs:
        fill = d / 'fill.py'
        if fill.exists():
            print(f'[p{SLIDE_NO}] run {fill.name} in {d.name}')
            subprocess.run([sys.executable, str(fill)], check=True, cwd=str(d))
        else:
            print(f'[p{SLIDE_NO}] skip {d.name}/fill.py (not found)')

if __name__=='__main__':
    run_make_data()
    run_fillers()
    build()
