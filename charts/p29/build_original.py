#!/usr/bin/env python3
import zipfile
from pathlib import Path
from typing import Optional
from lxml import etree as ET
import yaml

SLIDE_NO = 29
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
def _resolve_out() -> Path:
    try:
        cfg = yaml.safe_load((BASE / 'config.yaml').read_text(encoding='utf-8')) or {}
    except Exception:
        cfg = {}
    root = (cfg.get('project') or {}).get('output_root', 'output')
    p = Path(root)
    if not p.is_absolute():
        p = BASE / root
    return p / f'p{SLIDE_NO}-original.pptx'
TPL = _resolve_tpl()
OUT = _resolve_out()

APP_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
<Application>Microsoft Office PowerPoint</Application>
<PresentationFormat>Widescreen</PresentationFormat>
<TotalTime>0</TotalTime>
<Words>0</Words>
<Slides>1</Slides>
<Notes>0</Notes>
<HiddenSlides>0</HiddenSlides>
<MMClips>0</MMClips>
<ScaleCrop>false</ScaleCrop>
<LinksUpToDate>false</LinksUpToDate>
<SharedDoc>false</SharedDoc>
<HyperlinksChanged>false</HyperlinksChanged>
<AppVersion>16.0000</AppVersion>
</Properties>'''

NS = {
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
}


def filter_pres_rels(rels_bytes: bytes) -> tuple[bytes, Optional[str]]:
    pkg_ns = 'http://schemas.openxmlformats.org/package/2006/relationships'
    root = ET.fromstring(rels_bytes)
    new_root = ET.Element('Relationships', xmlns=pkg_ns)
    slide_rel_id: Optional[str] = None
    for rel in root.findall('{%s}Relationship' % pkg_ns):
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


def filter_pres_xml(pres_bytes: bytes, slide_rel_id: Optional[str]) -> bytes:
    tree = ET.fromstring(pres_bytes)
    sldIdLst = tree.find('{%s}sldIdLst' % NS['p'])
    if sldIdLst is None:
        sldIdLst = ET.SubElement(tree, '{%s}sldIdLst' % NS['p'])
    for ch in list(sldIdLst):
        sldIdLst.remove(ch)
    ET.SubElement(sldIdLst, '{%s}sldId' % NS['p'], attrib={'id': '256', '{%s}id' % NS['r']: slide_rel_id or 'rId1'})
    return ET.tostring(tree, xml_declaration=True, encoding='UTF-8', standalone="yes")


def filter_content_types(ct_bytes: bytes) -> bytes:
    ct = ET.fromstring(ct_bytes)
    ns_ct = 'http://schemas.openxmlformats.org/package/2006/content-types'
    for o in list(ct.findall('{%s}Override' % ns_ct)):
        part = o.get('PartName') or ''
        if part.startswith('/ppt/slides/slide'):
            ct.remove(o)
    has_app = any(o.get('PartName') == '/docProps/app.xml' for o in ct.findall('{%s}Override' % ns_ct))
    if not has_app:
        ET.SubElement(ct, '{%s}Override' % ns_ct, PartName='/docProps/app.xml', ContentType='application/vnd.openxmlformats-officedocument.extended-properties+xml')
    ET.SubElement(ct, '{%s}Override' % ns_ct, PartName='/ppt/slides/slide1.xml', ContentType='application/vnd.openxmlformats-officedocument.presentationml.slide+xml')
    return ET.tostring(ct, xml_declaration=True, encoding='UTF-8', standalone="yes")


def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(TPL, 'r') as tpl:
        pres_rels_bytes = tpl.read('ppt/_rels/presentation.xml.rels')
        pres_xml_bytes = tpl.read('ppt/presentation.xml')
        ct_bytes = tpl.read('[Content_Types].xml')
    new_pres_rels_xml, slide_rel_id = filter_pres_rels(pres_rels_bytes)
    new_pres_xml = filter_pres_xml(pres_xml_bytes, slide_rel_id)
    new_ct_xml = filter_content_types(ct_bytes)
    with zipfile.ZipFile(TPL, 'r') as tpl:
        with zipfile.ZipFile(OUT, 'w', compression=zipfile.ZIP_DEFLATED) as z:
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
                    z.writestr('ppt/slides/slide1.xml', tpl.read(name))
                elif name == f'ppt/slides/_rels/slide{SLIDE_NO}.xml.rels':
                    z.writestr('ppt/slides/_rels/slide1.xml.rels', tpl.read(name))
                else:
                    z.writestr(name, tpl.read(name))
            if 'docProps/app.xml' not in tpl.namelist():
                z.writestr('docProps/app.xml', APP_XML)
    print('Built', OUT)


if __name__ == '__main__':
    build()