#!/usr/bin/env python3
# 增加文件日志输出：stdout/stderr 同步写入本页 logs/build.log（不改变原有功能）
import sys, atexit
from datetime import datetime
from pathlib import Path as _PathForLogging

def _init_file_logging():
    """初始化文件日志到 charts/p10/logs/build.log，并保留控制台输出。"""
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

    sys.stdout = _Tee(sys.__stdout__, fh)
    sys.stderr = _Tee(sys.__stderr__, fh)
    print(f"[log] start {datetime.utcnow().isoformat()}Z")

    def _close():
        print(f"[log] end {datetime.utcnow().isoformat()}Z")
        try:
            fh.flush(); fh.close()
        except Exception:
            pass
    atexit.register(_close)

_init_file_logging()
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
# 标准化输出目录至 page 目录下：charts/p10/output/p10.pptx
OUT_PPTX = Path(__file__).resolve().parent / 'output' / 'p10.pptx'
APP_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Office PowerPoint</Application>
</Properties>
'''

UNZIP = _resolve(_proj.get('template_root', 'input/LRTBH-unzip'))

# 页面本地微模板目录（如存在则优先使用，以读取已填充的 chart XML）
PAGE_DIR = Path(__file__).resolve().parent
PAGE_TEMPLATE = PAGE_DIR / 'template'

def _pref(*parts: str) -> Path:
    nested = UNZIP / 'ppt'
    cand = nested.joinpath(*parts)
    return cand if cand.exists() else UNZIP.joinpath(*parts)

SLIDE_SRC = _pref('slides', f'slide{SLIDE_NO}.xml')
SLIDE_RELS_SRC = _pref('slides', '_rels', f'slide{SLIDE_NO}.xml.rels')
THEME_SRC = _pref('theme', 'theme1.xml')

def _charts_dir() -> Path:
    # 严格使用页面微模板 charts/p10/template/ppt/charts；缺失则报错
    d = PAGE_TEMPLATE / 'ppt' / 'charts'
    if not d.exists():
        raise FileNotFoundError(f'Page micro-template charts missing: {d}')
    return d

CHARTS_DIR = _charts_dir()
CHARTS_RELS_DIR = CHARTS_DIR / '_rels'
# embeddings/media：若页面模板存在则优先其位置，否则仍指向 UNZIP
def _pref_page(*parts: str) -> Path:
    cand = PAGE_TEMPLATE / 'ppt'
    cand = cand.joinpath(*parts)
    if not cand.exists():
        raise FileNotFoundError(f'Page micro-template missing: {cand}')
    return cand

EMBED_DIR = _pref_page('embeddings')
MEDIA_DIR = _pref_page('media')


def _read(p: Path) -> str:
    return p.read_text(encoding='utf-8')


def build():
    # 确保输出目录存在（charts/p10/output）
    OUT_PPTX.parent.mkdir(parents=True, exist_ok=True)
    # 使用完整模板复制并仅保留第10页，同时替换 chart8/9（如有）
    with zipfile.ZipFile(TEMPLATE_PPT, 'r') as tpl:
        pres_rels_bytes = tpl.read('ppt/_rels/presentation.xml.rels')
        pres_xml_bytes = tpl.read('ppt/presentation.xml')
        ct_bytes = tpl.read('[Content_Types].xml')
        # 严格策略下不使用模板回退；缺失将报错

    if not (CHARTS_DIR / 'chart8.xml').exists():
        raise FileNotFoundError(f'Missing chart: {CHARTS_DIR / "chart8.xml"}')
    if not (CHARTS_DIR / 'chart9.xml').exists():
        raise FileNotFoundError(f'Missing chart: {CHARTS_DIR / "chart9.xml"}')
    if not CHARTS_RELS_DIR.exists():
        raise FileNotFoundError(f'Missing chart rels directory: {CHARTS_RELS_DIR}')
    if not (CHARTS_RELS_DIR / 'chart8.xml.rels').exists():
        raise FileNotFoundError(f'Missing rels: {CHARTS_RELS_DIR / "chart8.xml.rels"}')
    if not (CHARTS_RELS_DIR / 'chart9.xml.rels').exists():
        raise FileNotFoundError(f'Missing rels: {CHARTS_RELS_DIR / "chart9.xml.rels"}')
    chart8_bytes = (CHARTS_DIR / 'chart8.xml').read_bytes()
    chart9_bytes = (CHARTS_DIR / 'chart9.xml').read_bytes()
    chart8_rels_bytes = (CHARTS_RELS_DIR / 'chart8.xml.rels').read_bytes()
    chart9_rels_bytes = (CHARTS_RELS_DIR / 'chart9.xml.rels').read_bytes()

    # 收集页面模板中的 embeddings（优先使用页面模板位置）
    embed_files = []
    if EMBED_DIR.exists():
        for p in sorted(EMBED_DIR.glob('*')):
            # 仅新增写入 xlsx，避免与模板内已存在的 xlsb 重复
            if p.suffix.lower() == '.xlsx':
                embed_files.append(p)

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
    def filter_content_types(ct_bytes: bytes, embed_files: list):
        ct = ET.fromstring(ct_bytes)
        ns_ct = 'http://schemas.openxmlformats.org/package/2006/content-types'
        for o in list(ct.findall('{%s}Override' % ns_ct)):
            part = o.get('PartName') or ''
            if part.startswith('/ppt/slides/slide'):
                ct.remove(o)
        ET.SubElement(ct, '{%s}Override' % ns_ct, PartName='/ppt/slides/slide1.xml', ContentType='application/vnd.openxmlformats-officedocument.presentationml.slide+xml')
        ET.SubElement(ct, '{%s}Override' % ns_ct, PartName='/docProps/app.xml', ContentType='application/vnd.openxmlformats-officedocument.extended-properties+xml')
        # 为新增的嵌入式工作簿添加覆盖项
        ext_ct = {
            '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            '.xlsb': 'application/vnd.ms-excel.sheet.binary.macroEnabled.12',
        }
        for ef in embed_files:
            part_name = f'/ppt/embeddings/{ef.name}'
            content_type = ext_ct.get(ef.suffix.lower())
            if content_type:
                ET.SubElement(ct, '{%s}Override' % ns_ct, PartName=part_name, ContentType=content_type)
        return ET.tostring(ct, xml_declaration=True, encoding='UTF-8', standalone="yes")

    new_pres_rels_xml, slide_rel_id = filter_pres_rels(pres_rels_bytes)
    new_pres_xml = filter_pres_xml(pres_xml_bytes, slide_rel_id)
    new_ct_xml = filter_content_types(ct_bytes, embed_files)

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
            # 写入/覆盖 embeddings（来自页面微模板）
            for ef in embed_files:
                z.writestr(f'ppt/embeddings/{ef.name}', ef.read_bytes())
            if 'docProps/app.xml' not in tpl.namelist():
                z.writestr('docProps/app.xml', APP_XML)

    print('Built', OUT_PPTX)

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


if __name__ == '__main__':
    run_make_data()
    run_fillers()
    build()
    # 收集页面模板中的 embeddings（优先使用页面模板位置）
    embed_files = []
    if EMBED_DIR.exists():
        for p in sorted(EMBED_DIR.glob('*')):
            if p.suffix.lower() in ('.xlsx', '.xlsb'):
                embed_files.append(p)