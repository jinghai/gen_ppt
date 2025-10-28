#!/usr/bin/env python3
import zipfile
from pathlib import Path
import re
from lxml import etree as ET
from typing import Optional
import yaml

SLIDE_NO = 10

def find_root() -> Path:
    # 向上查找同时包含 config.yaml 和 input 目录的 gen_ppt 根目录
    root = Path(__file__).resolve().parent
    while root.parent != root:
        if (root / 'config.yaml').exists() and (root / 'input').exists():
            return root
        root = root.parent
    # 兜底：回到当前文件上四级目录（通常为仓库根/或 gen_ppt）
    return Path(__file__).resolve().parents[3]

ROOT = find_root()
CONFIG = ROOT / 'config.yaml'
try:
    _cfg = yaml.safe_load(CONFIG.read_text(encoding='utf-8')) or {}
except Exception:
    _cfg = {}
_proj = _cfg.get('project') or {}

def _resolve(p: str) -> Path:
    rp = Path(p)
    return rp if rp.is_absolute() else ROOT / p

TEMPLATE_PPT = _resolve(_proj.get('original_ppt', 'input/LRTBH.pptx'))
OUT_PPTX = _resolve((_proj.get('output_root', 'output'))) / 'p10.pptx'
APP_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Office PowerPoint</Application>
</Properties>
'''

UNZIP = _resolve(_proj.get('template_root', 'input/LRTBH-unzip'))

def _pref(*parts: str) -> Path:
    nested = UNZIP / 'ppt'
    cand = nested.joinpath(*parts)
    return cand if cand.exists() else UNZIP.joinpath(*parts)

SLIDE_SRC = _pref('slides', f'slide{SLIDE_NO}.xml')
SLIDE_RELS_SRC = _pref('slides', '_rels', f'slide{SLIDE_NO}.xml.rels')
THEME_SRC = _pref('theme', 'theme1.xml')

def _charts_dir() -> Path:
    d = UNZIP / 'ppt' / 'charts'
    return d if d.exists() else UNZIP / 'charts'

CHARTS_DIR = _charts_dir()
CHARTS_RELS_DIR = CHARTS_DIR / '_rels'
EMBED_DIR = _pref('embeddings')
MEDIA_DIR = _pref('media')


def _read(p: Path) -> str:
    return p.read_text(encoding='utf-8')


def build():
    # 使用完整模板复制并仅保留第10页，同时替换 chart8/9（如有）
    with zipfile.ZipFile(TEMPLATE_PPT, 'r') as tpl:
        pres_rels_bytes = tpl.read('ppt/_rels/presentation.xml.rels')
        pres_xml_bytes = tpl.read('ppt/presentation.xml')
        ct_bytes = tpl.read('[Content_Types].xml')
        # 预加载模板中的图表及关系（作为回退）
        chart8_tpl = tpl.read('ppt/charts/chart8.xml')
        chart9_tpl = tpl.read('ppt/charts/chart9.xml')
        chart8_rels_tpl = tpl.read('ppt/charts/_rels/chart8.xml.rels')
        chart9_rels_tpl = tpl.read('ppt/charts/_rels/chart9.xml.rels')

    chart8_bytes = (CHARTS_DIR / 'chart8.xml').read_bytes() if (CHARTS_DIR / 'chart8.xml').exists() else chart8_tpl
    chart9_bytes = (CHARTS_DIR / 'chart9.xml').read_bytes() if (CHARTS_DIR / 'chart9.xml').exists() else chart9_tpl
    chart8_rels_bytes = (CHARTS_RELS_DIR / 'chart8.xml.rels').read_bytes() if (CHARTS_RELS_DIR / 'chart8.xml.rels').exists() else chart8_rels_tpl
    chart9_rels_bytes = (CHARTS_RELS_DIR / 'chart9.xml.rels').read_bytes() if (CHARTS_RELS_DIR / 'chart9.xml.rels').exists() else chart9_rels_tpl

    # 过滤 presentation.rels：仅保留 slide10（重定向到 slide1）与非 slide 关系
    def filter_pres_rels(rels_bytes: bytes):
        root = ET.fromstring(rels_bytes)
        new_root = ET.Element('Relationships', xmlns='http://schemas.openxmlformats.org/package/2006/relationships')
        slide_rel_id = None
        for rel in root.findall('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
            t = rel.get('Target') or ''
            typ = rel.get('Type') or ''
            if typ.endswith('/slide') and t == 'slides/slide10.xml':
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

    with zipfile.ZipFile(TEMPLATE_PPT, 'r') as tpl:
        with zipfile.ZipFile(OUT_PPTX, 'w', zipfile.ZIP_DEFLATED) as z:
            for name in tpl.namelist():
                if name.startswith('ppt/slides/slide') and name != 'ppt/slides/slide10.xml':
                    continue
                if name.startswith('ppt/slides/_rels/slide') and name != 'ppt/slides/_rels/slide10.xml.rels':
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
                elif name == 'ppt/charts/chart8.xml':
                    z.writestr(name, chart8_bytes)
                elif name == 'ppt/charts/chart9.xml':
                    z.writestr(name, chart9_bytes)
                elif name == 'ppt/charts/_rels/chart8.xml.rels':
                    z.writestr(name, chart8_rels_bytes)
                elif name == 'ppt/charts/_rels/chart9.xml.rels':
                    z.writestr(name, chart9_rels_bytes)
                else:
                    z.writestr(name, tpl.read(name))
            if 'docProps/app.xml' not in tpl.namelist():
                z.writestr('docProps/app.xml', APP_XML)

    print('Built', OUT_PPTX)


if __name__ == '__main__':
    build()