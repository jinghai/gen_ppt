#!/usr/bin/env python3
# 增加文件日志输出：将 stdout/stderr 同步写入当前页 logs/build.log（MVP，不改动现有逻辑）
import sys, atexit
from datetime import datetime
from pathlib import Path as _PathForLogging

def _init_file_logging():
    """初始化文件日志，将标准输出与错误输出双写到 logs/build.log。
    - 不侵入式：不替换现有 print 调用与逻辑，仅增加输出目标
    - 目录：charts/pXX/logs/build.log（按页独立）
    - 关闭：使用 atexit 在进程退出时刷新并关闭文件句柄
    """
    page_dir = _PathForLogging(__file__).resolve().parent
    logs_dir = page_dir / 'logs'
    logs_dir.mkdir(parents=True, exist_ok=True)
    log_file = logs_dir / 'build.log'
    fh = open(log_file, 'a', encoding='utf-8')

    class _Tee:
        def __init__(self, *streams):
            self.streams = streams
        def write(self, data):
            for s in self.streams:
                try:
                    s.write(data)
                    s.flush()
                except Exception:
                    pass
        def flush(self):
            for s in self.streams:
                try:
                    s.flush()
                except Exception:
                    pass

    # 双写到原始 stdout/stderr 与文件
    sys.stdout = _Tee(sys.__stdout__, fh)
    sys.stderr = _Tee(sys.__stderr__, fh)
    print(f"[log] start {datetime.utcnow().isoformat()}Z")

    def _close():
        print(f"[log] end {datetime.utcnow().isoformat()}Z")
        try:
            fh.flush()
            fh.close()
        except Exception:
            pass
    atexit.register(_close)

_init_file_logging()
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
# 标准化输出目录至 page 目录下：charts/p8/output/p8.pptx
OUT = Path(__file__).resolve().parent / 'output' / f'p{SLIDE_NO}.pptx'

# 嵌入工作簿目录：严格使用页面微模板；缺失则报错
PAGE_DIR = Path(__file__).resolve().parent
EMBED_DIR = PAGE_DIR / 'template' / 'ppt' / 'embeddings'
if not EMBED_DIR.exists():
    raise FileNotFoundError(f"Page micro-template embeddings missing: {EMBED_DIR}")

# 图表目录：严格使用页面微模板；缺失则报错
PAGE_CHARTS_DIR = PAGE_DIR / 'template' / 'ppt' / 'charts'
if not PAGE_CHARTS_DIR.exists():
    raise FileNotFoundError(f"Page micro-template charts missing: {PAGE_CHARTS_DIR}")
CHARTS_DIR = PAGE_CHARTS_DIR
CHARTS_RELS_DIR = CHARTS_DIR / '_rels'
if not CHARTS_RELS_DIR.exists():
    raise FileNotFoundError(f"Chart rels directory missing: {CHARTS_RELS_DIR}")

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
    # 确保输出目录存在（charts/p8/output）
    OUT.parent.mkdir(parents=True, exist_ok=True)
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

    # 过滤 Content_Types：仅保留 slide1 覆盖项，补充 docProps/app.xml 覆盖，并添加嵌入 xlsx 覆盖
    def filter_content_types(ct_bytes: bytes, embed_files: list[str]):
        ct = ET.fromstring(ct_bytes)
        ns_ct = 'http://schemas.openxmlformats.org/package/2006/content-types'
        for o in list(ct.findall('{%s}Override' % ns_ct)):
            part = o.get('PartName') or ''
            if part.startswith('/ppt/slides/slide'):
                ct.remove(o)
        ET.SubElement(ct, '{%s}Override' % ns_ct, PartName='/ppt/slides/slide1.xml', ContentType='application/vnd.openxmlformats-officedocument.presentationml.slide+xml')
        ET.SubElement(ct, '{%s}Override' % ns_ct, PartName='/docProps/app.xml', ContentType='application/vnd.openxmlformats-officedocument.extended-properties+xml')
        # 追加嵌入 .xlsx 覆盖项
        for nm in embed_files:
            ET.SubElement(ct, '{%s}Override' % ns_ct, PartName=f'/ppt/embeddings/{nm}', ContentType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        return ET.tostring(ct, xml_declaration=True, encoding='UTF-8', standalone="yes")

    new_pres_rels_xml, slide_rel_id = filter_pres_rels(pres_rels_bytes)
    new_pres_xml = filter_pres_xml(pres_xml_bytes, slide_rel_id)
    # 收集嵌入式 xlsx（跳过 xlsb），兼容所有命名
    embed_files = []
    try:
        if EMBED_DIR.exists():
            for f in EMBED_DIR.glob('*.xlsx'):
                embed_files.append(f.name)
    except Exception:
        embed_files = []
    new_ct_xml = filter_content_types(ct_bytes, embed_files)

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
                    # 使用缓存的图表文件，优先页面模板，其次全局模板
                    chart_name = name.split('/')[-1]
                    # 优先页面内 charts 目录
                    page_chart_path = PAGE_DIR / 'template' / 'ppt' / 'charts' / chart_name
                    chart_path = chart_name and (page_chart_path if page_chart_path.exists() else (CHARTS_DIR / chart_name))
                    if chart_path and chart_path.exists():
                        z.writestr(name, chart_path.read_bytes())
                    else:
                        z.writestr(name, tpl.read(name))
                elif name.startswith('ppt/charts/_rels/chart'):
                    # 使用缓存的图表关系文件，优先页面模板，其次全局模板
                    rels_name = name.split('/')[-1]
                    page_rels_path = PAGE_DIR / 'template' / 'ppt' / 'charts' / '_rels' / rels_name
                    rels_path = page_rels_path if page_rels_path.exists() else (CHARTS_RELS_DIR / rels_name)
                    if rels_path.exists():
                        z.writestr(name, rels_path.read_bytes())
                    else:
                        z.writestr(name, tpl.read(name))
                elif name.startswith('ppt/embeddings/Microsoft_Office_Excel_Binary_Worksheet') and name.endswith('.xlsb'):
                    # 跳过模板中的 .xlsb，避免与新生成的 .xlsx 冲突
                    continue
                else:
                    z.writestr(name, tpl.read(name))
            if 'docProps/app.xml' not in tpl.namelist():
                z.writestr('docProps/app.xml', APP_XML)
            # 打包嵌入式 .xlsx（若存在）
            for nm in embed_files:
                src = EMBED_DIR / nm
                if src.exists():
                    z.writestr(f'ppt/embeddings/{nm}', src.read_bytes())

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