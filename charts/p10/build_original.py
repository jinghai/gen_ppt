#!/usr/bin/env python3
import zipfile
from pathlib import Path
from datetime import datetime
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
    # 兜底：回退到当前文件上三级目录
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

TEMPLATE_PPTX = _resolve(_proj.get('original_ppt', 'input/LRTBH.pptx'))
UNZIP = _resolve(_proj.get('template_root', 'input/LRTBH-unzip'))
OUT = _resolve(_proj.get('output_root', 'output')) / 'p10-original.pptx'

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
    'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
}

# 已不使用：顶级 _rels/.rels 构造器移除，避免误用 officeDocument 命名空间


def content_types(overrides: list) -> bytes:
    Types = ET.Element('Types', xmlns='http://schemas.openxmlformats.org/package/2006/content-types')
    # defaults
    ET.SubElement(Types, 'Default', Extension='rels', ContentType='application/vnd.openxmlformats-package.relationships+xml')
    ET.SubElement(Types, 'Default', Extension='xml', ContentType='application/xml')
    ET.SubElement(Types, 'Default', Extension='png', ContentType='image/png')
    # overrides（保持最小化且与 build.py 一致的必需项）
    base_overrides = [
        ('/ppt/presentation.xml','application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml'),
        ('/ppt/slides/slide1.xml','application/vnd.openxmlformats-officedocument.presentationml.slide+xml'),
        ('/ppt/theme/theme1.xml','application/vnd.openxmlformats-officedocument.theme+xml'),
        ('/docProps/core.xml','application/vnd.openxmlformats-package.core-properties+xml'),
        ('/docProps/app.xml','application/vnd.openxmlformats-officedocument.extended-properties+xml'),
        ('/ppt/charts/chart8.xml','application/vnd.openxmlformats-officedocument.drawingml.chart+xml'),
        ('/ppt/charts/chart9.xml','application/vnd.openxmlformats-officedocument.drawingml.chart+xml'),
        ('/ppt/slideLayouts/slideLayout5.xml','application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml'),
        ('/ppt/slideMasters/slideMaster2.xml','application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml'),
    ]
    for p, t in base_overrides:
        ET.SubElement(Types, 'Override', PartName=p, ContentType=t)
    for p, t in overrides:
        ET.SubElement(Types, 'Override', PartName=p, ContentType=t)
    return ET.tostring(Types, xml_declaration=True, encoding='UTF-8', standalone="yes")


def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)

    # 读取模板中的 presentation 关系、结构与内容类型
    with zipfile.ZipFile(TEMPLATE_PPTX, 'r') as tpl:
        pres_rels_bytes = tpl.read('ppt/_rels/presentation.xml.rels')
        pres_xml_bytes = tpl.read('ppt/presentation.xml')
        ct_bytes = tpl.read('[Content_Types].xml')

    # 过滤 presentation.xml.rels，仅保留指向 slide10 的关系（重定向到 slide1）以及非 slide 的其他关系
    def filter_pres_rels(rels_bytes: bytes):
        root = ET.fromstring(rels_bytes)
        # presentation.xml.rels 使用的是 package relationships 命名空间，而不是 officeDocument
        pkg_ns = 'http://schemas.openxmlformats.org/package/2006/relationships'
        new_root = ET.Element('Relationships', xmlns=pkg_ns)
        slide_rel_id = None
        for rel in root.findall('{%s}Relationship' % pkg_ns):
            t = rel.get('Target') or ''
            typ = rel.get('Type') or ''
            if typ.endswith('/slide') and t == f'slides/slide{SLIDE_NO}.xml':
                slide_rel_id = rel.get('Id')
                e = ET.SubElement(new_root, 'Relationship')
                for k, v in rel.attrib.items():
                    e.set(k, v)
                # 重定向为 slide1
                e.set('Target', 'slides/slide1.xml')
            elif not typ.endswith('/slide'):
                e = ET.SubElement(new_root, 'Relationship')
                for k, v in rel.attrib.items():
                    e.set(k, v)
        return ET.tostring(new_root, xml_declaration=True, encoding='UTF-8', standalone="yes"), slide_rel_id

    # 过滤 presentation.xml，仅保留对应 slide_rel_id 的 sldId
    def filter_pres_xml(pres_bytes: bytes, slide_rel_id: Optional[str]):
        tree = ET.fromstring(pres_bytes)
        sldIdLst = tree.find('{%s}sldIdLst' % NS['p'])
        if sldIdLst is None:
            sldIdLst = ET.SubElement(tree, '{%s}sldIdLst' % NS['p'])
        for ch in list(sldIdLst):
            sldIdLst.remove(ch)
        ET.SubElement(sldIdLst, '{%s}sldId' % NS['p'], attrib={'id': '256', '{%s}id' % NS['r']: slide_rel_id or 'rId1'})
        return ET.tostring(tree, xml_declaration=True, encoding='UTF-8', standalone="yes")

    # 过滤 Content_Types：移除全部 slide 覆盖项后添加 slide1
    def filter_content_types(ct_bytes: bytes):
        ct = ET.fromstring(ct_bytes)
        ns_ct = 'http://schemas.openxmlformats.org/package/2006/content-types'
        for o in list(ct.findall('{%s}Override' % ns_ct)):
            part = o.get('PartName') or ''
            if part.startswith('/ppt/slides/slide'):
                ct.remove(o)
        # 确保 docProps/app.xml 覆盖存在
        has_app = False
        for o in ct.findall('{%s}Override' % ns_ct):
            if o.get('PartName') == '/docProps/app.xml':
                has_app = True
                break
        if not has_app:
            ET.SubElement(ct, '{%s}Override' % ns_ct, PartName='/docProps/app.xml', ContentType='application/vnd.openxmlformats-officedocument.extended-properties+xml')
        ET.SubElement(ct, '{%s}Override' % ns_ct, PartName='/ppt/slides/slide1.xml', ContentType='application/vnd.openxmlformats-officedocument.presentationml.slide+xml')
        return ET.tostring(ct, xml_declaration=True, encoding='UTF-8', standalone="yes")

    # 生成新文件：复制模板的所有项，删除除 slide10 之外的其它幻灯片及其 rels，替换 presentation 与 Content_Types；并重命名 slide10→slide1
    with zipfile.ZipFile(TEMPLATE_PPTX, 'r') as tpl:
        new_pres_rels_xml, slide_rel_id = filter_pres_rels(pres_rels_bytes)
        new_pres_xml = filter_pres_xml(pres_xml_bytes, slide_rel_id)
        new_ct_xml = filter_content_types(ct_bytes)
        with zipfile.ZipFile(OUT, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            for name in tpl.namelist():
                # 去除非第10页的幻灯片
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
                else:
                    z.writestr(name, tpl.read(name))
            # Write docProps/app.xml if it doesn't exist
            if 'docProps/app.xml' not in tpl.namelist():
                z.writestr('docProps/app.xml', APP_XML)
    print(f'Wrote {OUT}')


if __name__ == '__main__':
    build()