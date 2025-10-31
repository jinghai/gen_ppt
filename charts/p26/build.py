#!/usr/bin/env python3
# 文件日志：stdout/stderr 双写入 logs/build.log（不中断控制台打印）
import sys, atexit
from datetime import datetime
from pathlib import Path as _PathForLogging

def _init_file_logging():
    page_dir = _PathForLogging(__file__).resolve().parent
    logs_dir = page_dir / 'logs'
    logs_dir.mkdir(parents=True, exist_ok=True)
    fh = open(logs_dir / 'build.log', 'a', encoding='utf-8')
    class _Tee:
        def __init__(self, *streams): self.streams = streams
        def write(self, data):
            for s in self.streams:
                try: s.write(data); s.flush()
                except Exception: pass
        def flush(self):
            for s in self.streams:
                try: s.flush()
                except Exception: pass
    sys.stdout = _Tee(sys.__stdout__, fh)
    sys.stderr = _Tee(sys.__stderr__, fh)
    print(f"[log] start {datetime.utcnow().isoformat()}Z")
    def _close():
        print(f"[log] end {datetime.utcnow().isoformat()}Z")
        try: fh.flush(); fh.close()
        except Exception: pass
    atexit.register(_close)

_init_file_logging()
import zipfile
from pathlib import Path
import yaml
from lxml import etree as ET
from typing import Optional

SLIDE_NO = 26
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
    # 已废弃：不再支持回退到全局模板解压目录（UNZ）。
    # 为保持向后兼容，仍保留函数但不使用其返回值。
    try:
        cfg = yaml.safe_load((BASE / 'config.yaml').read_text(encoding='utf-8')) or {}
    except Exception:
        cfg = {}
    tr = (cfg.get('project') or {}).get('template_root')
    p = Path(tr) if tr else BASE / 'template'
    if not p.is_absolute():
        p = BASE / p
    return p

# 标准化输出目录至 page 目录下：charts/p26/output/p26.pptx
OUT = Path(__file__).resolve().parent / 'output' / f'p{SLIDE_NO}.pptx'

# 嵌入工作簿目录：严格使用页面微模板；缺失则报错
PAGE_DIR = Path(__file__).resolve().parent
EMBED_DIR = PAGE_DIR / 'template' / 'ppt' / 'embeddings'
if not EMBED_DIR.exists():
    raise FileNotFoundError(f"Page micro-template embeddings missing: {EMBED_DIR}")

# 图表与关系目录：严格使用页面微模板；缺失则报错
CHARTS_DIR = PAGE_DIR / 'template' / 'ppt' / 'charts'
CHARTS_RELS_DIR = CHARTS_DIR / '_rels'
if not CHARTS_DIR.exists():
    raise FileNotFoundError(f"Page micro-template charts missing: {CHARTS_DIR}")
if not CHARTS_RELS_DIR.exists():
    raise FileNotFoundError(f"Chart rels directory missing: {CHARTS_RELS_DIR}")

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


def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)

    # 读取模板中的 presentation 关系、结构与内容类型
    with zipfile.ZipFile(TPL, 'r') as tpl:
        pres_rels_bytes = tpl.read('ppt/_rels/presentation.xml.rels')
        pres_xml_bytes = tpl.read('ppt/presentation.xml')
        ct_bytes = tpl.read('[Content_Types].xml')

    # 预加载页面微模板中的图表及关系（严格策略：必须存在）
    charts_fallback = {}
    for chart_file in CHARTS_DIR.glob('chart*.xml'):
        charts_fallback[chart_file.name] = chart_file.read_bytes()
    for rels_file in CHARTS_RELS_DIR.glob('chart*.xml.rels'):
        charts_fallback[f'rels:{rels_file.name}'] = rels_file.read_bytes()

    # 过滤 presentation.xml.rels，仅保留指向指定slide的关系（重定向到 slide1）以及非 slide 的其他关系
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

    # 过滤 Content_Types：移除全部 slide 覆盖项后添加 slide1，并追加嵌入 xlsx 覆盖项
    def filter_content_types(ct_bytes: bytes, embed_files: list[str]):
        ct = ET.fromstring(ct_bytes)
        ns_ct = 'http://schemas.openxmlformats.org/package/2006/content-types'
        for o in list(ct.findall('{%s}Override' % ns_ct)):
            part = o.get('PartName') or ''
            if part.startswith('/ppt/slides/slide'):
                ct.remove(o)
        ET.SubElement(ct, '{%s}Override' % ns_ct, PartName='/ppt/slides/slide1.xml', ContentType='application/vnd.openxmlformats-officedocument.presentationml.slide+xml')
        # 确保存在 docProps/app.xml 覆盖项
        has_app = any((o.get('PartName') == '/docProps/app.xml') for o in ct.findall('{%s}Override' % ns_ct))
        if not has_app:
            ET.SubElement(ct, '{%s}Override' % ns_ct, PartName='/docProps/app.xml', ContentType='application/vnd.openxmlformats-officedocument.extended-properties+xml')
        # 添加嵌入式 xlsx 覆盖项
        for nm in embed_files:
            ET.SubElement(ct, '{%s}Override' % ns_ct, PartName=f'/ppt/embeddings/{nm}', ContentType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        return ET.tostring(ct, xml_declaration=True, encoding='UTF-8', standalone="yes")

    # 生成新文件：复制模板的所有项，删除除指定slide之外的其它幻灯片及其 rels，替换 presentation 与 Content_Types；并重命名指定slide→slide1
    with zipfile.ZipFile(TPL, 'r') as tpl:
        new_pres_rels_xml, slide_rel_id = filter_pres_rels(pres_rels_bytes)
        new_pres_xml = filter_pres_xml(pres_xml_bytes, slide_rel_id)
        # 收集嵌入式 xlsx（跳过 xlsb）
        embed_files = []
        try:
            if EMBED_DIR.exists():
                for f in EMBED_DIR.glob('Microsoft_Office_Excel_Binary_Worksheet*.xlsx'):
                    embed_files.append(f.name)
        except Exception:
            embed_files = []
        new_ct_xml = filter_content_types(ct_bytes, embed_files)
        
        # 读取指定slide的关系文件以获取图表信息
        slide_rels_bytes = None
        try:
            slide_rels_bytes = tpl.read(f'ppt/slides/_rels/slide{SLIDE_NO}.xml.rels')
        except KeyError:
            pass
        # 严格校验：依据 slide 关系确认所用图表必须存在于页面微模板
        if slide_rels_bytes:
            rel_root = ET.fromstring(slide_rels_bytes)
            used_charts = set()
            used_rels = set()
            for rel in rel_root.findall('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
                typ = rel.get('Type') or ''
                tgt = rel.get('Target') or ''
                if typ.endswith('/chart') and '../charts/' in tgt:
                    nm = tgt.split('../charts/')[-1]
                    used_charts.add(nm)
                    used_rels.add(f'{nm}.rels')
            missing = [nm for nm in used_charts if nm not in charts_fallback]
            missing_rels = [nm for nm in used_rels if f'rels:{nm}' not in charts_fallback]
            if missing or missing_rels:
                raise FileNotFoundError(
                    f"Page micro-template charts/rels missing: charts={missing}, rels={missing_rels}"
                )
        
        with zipfile.ZipFile(OUT, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            for name in tpl.namelist():
                # 去除非指定页的幻灯片
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
                elif name.startswith('ppt/charts/chart') and name.endswith('.xml'):
                    # 使用回退图表数据（如果有）
                    chart_name = name.split('/')[-1]
                    fallback_data = charts_fallback.get(chart_name)
                    z.writestr(name, fallback_data if fallback_data is not None else tpl.read(name))
                elif name.startswith('ppt/charts/_rels/chart') and name.endswith('.xml.rels'):
                    # 使用回退关系数据（如果有）
                    rels_name = name.split('/')[-1]
                    fallback_data = charts_fallback.get(f'rels:{rels_name}')
                    z.writestr(name, fallback_data if fallback_data is not None else tpl.read(name))
                elif name.startswith('ppt/embeddings/Microsoft_Office_Excel_Binary_Worksheet') and name.endswith('.xlsb'):
                    # 跳过模板中的 xlsb，避免与新生成的 xlsx 冲突
                    continue
                else:
                    z.writestr(name, tpl.read(name))
            # Write docProps/app.xml if it doesn't exist
            if 'docProps/app.xml' not in tpl.namelist():
                z.writestr('docProps/app.xml', APP_XML)
            # 打包嵌入式 xlsx（若存在）
            for nm in embed_files:
                src = EMBED_DIR / nm
                if src.exists():
                    z.writestr(f'ppt/embeddings/{nm}', src.read_bytes())
    print(f'Built {OUT}')


if __name__ == '__main__':
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
        chart_dirs = sorted([d for d in page_dir.iterdir() if d.is_dir() and re.match(r'^chart\\d+$', d.name)])
        for d in chart_dirs:
            fill = d / 'fill.py'
            if fill.exists():
                print(f'[p{SLIDE_NO}] run {fill.name} in {d.name}')
                subprocess.run([sys.executable, str(fill)], check=True, cwd=str(d))
            else:
                print(f'[p{SLIDE_NO}] skip {d.name}/fill.py (not found)')

    run_make_data()
    run_fillers()
    build()
