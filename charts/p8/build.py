#!/usr/bin/env python3
import zipfile
from pathlib import Path
import yaml
from lxml import etree as ET
from typing import Optional

SLIDE_NO = 8
BASE = Path(__file__).resolve().parents[2]
def _resolve_tpl() -> Path:
    try:
        cfg = yaml.safe_load((BASE / 'config.yaml').read_text(encoding='utf-8')) or {}
    except Exception:
        cfg = {}
    op = (cfg.get('project') or {}).get('original_ppt', 'ppt/input/LRTBH.pptx')
    p = Path(op)
    if not p.is_absolute():
        p = BASE.parent.parent / op
    return p

TPL = _resolve_tpl()

def _resolve_unz_root() -> Path:
    try:
        cfg = yaml.safe_load((BASE / 'config.yaml').read_text(encoding='utf-8')) or {}
    except Exception:
        cfg = {}
    tr = (cfg.get('project') or {}).get('template_root', 'ppt/input/LRTBH-unzip')
    p = Path(tr)
    if not p.is_absolute():
        p = BASE.parent.parent / tr
    return p

UNZ = _resolve_unz_root()
OUT = BASE / 'output' / f'p{SLIDE_NO}.pptx'

# 图表缓存目录
CHARTS_DIR = (UNZ / 'ppt' / 'charts') if (UNZ / 'ppt' / 'charts').exists() else (UNZ / 'charts')
CHARTS_RELS_DIR = CHARTS_DIR / '_rels'

APP_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
<Application>Microsoft Office PowerPoint</Application>
<PresentationFormat>Widescreen</PresentationFormat>
<Paragraphs>0</Paragraphs>
<Slides>1</Slides>
<Notes>0</Notes>
<HiddenSlides>0</HiddenSlides>
<MMClips>0</MMClips>
<ScaleCrop>false</ScaleCrop>
<HeadingPairs>
<vt:vector size="6" baseType="variant">
<vt:variant><vt:lpstr>Fonts Used</vt:lpstr></vt:variant>
<vt:variant><vt:i4>2</vt:i4></vt:variant>
<vt:variant><vt:lpstr>Theme</vt:lpstr></vt:variant>
<vt:variant><vt:i4>1</vt:i4></vt:variant>
<vt:variant><vt:lpstr>Slide Titles</vt:lpstr></vt:variant>
<vt:variant><vt:i4>1</vt:i4></vt:variant>
</vt:vector>
</HeadingPairs>
<TitlesOfParts>
<vt:vector size="4" baseType="lpstr">
<vt:lpstr>Calibri</vt:lpstr>
<vt:lpstr>宋体</vt:lpstr>
<vt:lpstr>Office Theme</vt:lpstr>
<vt:lpstr>Slide 1</vt:lpstr>
</vt:vector>
</TitlesOfParts>
<Company></Company>
<LinksUpToDate>false</LinksUpToDate>
<SharedDoc>false</SharedDoc>
<HyperlinksChanged>false</HyperlinksChanged>
<AppVersion>16.0000</AppVersion>
</Properties>'''

def build():
    # 使用完整模板复制并仅保留第8页，同时替换图表（如有）
    with zipfile.ZipFile(TPL, 'r') as tpl:
        pres_rels_bytes = tpl.read('ppt/_rels/presentation.xml.rels')
        pres_xml_bytes = tpl.read('ppt/presentation.xml')
        ct_bytes = tpl.read('[Content_Types].xml')

    # 过滤 presentation.rels：仅保留 slide8（重定向到 slide1）与非 slide 关系
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
                elif name.startswith('ppt/charts/chart'):
                    # 使用缓存的图表文件（如果存在）
                    chart_name = name.split('/')[-1]
                    chart_path = CHARTS_DIR / chart_name
                    if chart_path.exists():
                        z.writestr(name, chart_path.read_bytes())
                    else:
                        z.writestr(name, tpl.read(name))
                elif name.startswith('ppt/charts/_rels/chart'):
                    # 使用缓存的图表关系文件（如果存在）
                    rels_name = name.split('/')[-1]
                    rels_path = CHARTS_RELS_DIR / rels_name
                    if rels_path.exists():
                        z.writestr(name, rels_path.read_bytes())
                    else:
                        z.writestr(name, tpl.read(name))
                else:
                    z.writestr(name, tpl.read(name))
            if 'docProps/app.xml' not in tpl.namelist():
                z.writestr('docProps/app.xml', APP_XML)

    print('Built', OUT)

if __name__=='__main__':
    build()