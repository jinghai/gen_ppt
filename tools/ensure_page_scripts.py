#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为指定页面（如 p8..p31）创建缺失的通用脚本：
- build.py：占位说明（后续若有单页打包需求再实现）
- build_original.py：调用 generate_original_cache.py 生成原始缓存
- gen_preview.py：离线批量生成 preview_original.png（每个 chart* 目录）
- validate.py：对比 original_* 与模板 chart.xml 解析一致性，并校验数据量不小于原始
"""
import argparse
import re
from pathlib import Path

# 项目根目录定位：tools/ensure_page_scripts.py 的上一级即为项目根
ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / 'tools'
PAGES_DIR = ROOT / 'charts'

BUILD_PY_TMPL = """#!/usr/bin/env python3
print("[info] build stub: implement slide-specific packaging after template is complete")
"""

BUILD_ORIGINAL_TMPL = """#!/usr/bin/env python3
import zipfile
from pathlib import Path
from typing import Optional
from lxml import etree as ET
import yaml

THIS_DIR = Path(__file__).resolve().parent
SLIDE_NO = int(THIS_DIR.name[1:])
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
"""

GEN_PREVIEW_TMPL = """#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1] / 'tools'
sys.path.append(str(TOOLS))
from gen_preview_chart import generate_preview  # type: ignore

PAGE = Path(__file__).resolve().parent


def main():
    charts = [c for c in PAGE.iterdir() if c.is_dir() and re.match(r'^chart\\d+$', c.name)]
    ok = 0
    for c in charts:
        if generate_preview(c):
            ok += 1
    print(f'[done] previews generated: {ok}/{len(charts)} in {PAGE}')


if __name__ == '__main__':
    main()
"""

VALIDATE_TMPL = """#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

TOOLS = Path(__file__).resolve().parents[1] / 'tools'
sys.path.append(str(TOOLS))
from extract_chart_cache import parse_chart_xml  # type: ignore

PAGE = Path(__file__).resolve().parent


def _eq(a: Any, b: Any, tol: float = 1e-9) -> bool:
    try:
        af = float(a)
        bf = float(b)
        return abs(af - bf) <= tol
    except Exception:
        return a == b


def _read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return None


def _read_chart_xml_bytes(chart_dir: Path) -> bytes:
    p = chart_dir / 'chart_path.txt'
    xml_path = Path(p.read_text(encoding='utf-8').strip())
    return xml_path.read_bytes()


def _original_file(chart_dir: Path, name: str) -> Path:
    sub = chart_dir / 'original' / name
    if sub.exists():
        return sub
    root = chart_dir / name
    return root


def validate_original_vs_template(chart_dir: Path) -> Tuple[bool, List[str]]:
    errs: List[str] = []
    xml_bytes = _read_chart_xml_bytes(chart_dir)
    parsed = parse_chart_xml(xml_bytes)
    ctype = parsed.get('chart_type')
    if ctype == 'scatterChart':
        orig_scatter = _read_json(_original_file(chart_dir, 'original_scatter.json')) or []
        parsed_scatter = parsed.get('scatter_series') or []
        if len(orig_scatter) != len(parsed_scatter):
            errs.append('scatter series length mismatch')
        for i in range(min(len(orig_scatter), len(parsed_scatter))):
            os = orig_scatter[i]
            ps = parsed_scatter[i]
            ox, oy = os.get('x', []), os.get('y', [])
            px, py = ps.get('x', []), ps.get('y', [])
            if len(ox) != len(px) or len(oy) != len(py):
                errs.append(f'scatter[{i}] x/y length mismatch')
            else:
                for j in range(len(ox)):
                    if not _eq(ox[j], px[j]) or not _eq(oy[j], py[j]):
                        errs.append(f'scatter[{i}] point {j} mismatch')
                        break
    else:
        orig_labels = _read_json(_original_file(chart_dir, 'original_labels.json')) or []
        orig_series = _read_json(_original_file(chart_dir, 'original_series.json')) or []
        plabels = parsed.get('labels') or []
        pseries = parsed.get('series') or []
        if len(orig_labels) != len(plabels):
            errs.append('labels length mismatch')
        else:
            for j in range(len(orig_labels)):
                if not _eq(orig_labels[j], plabels[j]):
                    errs.append(f'label[{j}] mismatch')
                    break
        if len(orig_series) != len(pseries):
            errs.append('series count mismatch')
        else:
            for si in range(len(orig_series)):
                ov = orig_series[si]['values'] if isinstance(orig_series[si], dict) else (orig_series[si] or [])
                pv = pseries[si]['values'] if isinstance(pseries[si], dict) else (pseries[si] or [])
                if len(ov) != len(pv):
                    errs.append(f'series[{si}] length mismatch')
                    break
                for j in range(len(ov)):
                    if not _eq(ov[j], pv[j]):
                        errs.append(f'series[{si}][{j}] value mismatch')
                        break
    return (len(errs) == 0), errs


def _count_scatter_y(series_json: Any) -> int:
    if isinstance(series_json, dict) and 'scatter_series' in series_json:
        arr = series_json.get('scatter_series') or []
        if not arr:
            return 0
        return len(arr[0].get('y') or [])
    if isinstance(series_json, list):
        if not series_json:
            return 0
        s0 = series_json[0]
        if isinstance(s0, dict):
            return len(s0.get('y') or [])
        if isinstance(s0, list):
            return len(s0)
    return 0


def _count_category_len(data_json: Any) -> int:
    if isinstance(data_json, dict):
        lbls = data_json.get('labels') or []
        return len(lbls)
    if isinstance(data_json, list):
        s0 = data_json[0] if data_json else []
        return len(s0)
    return 0


def validate_counts(chart_dir: Path) -> Tuple[bool, List[str]]:
    errs: List[str] = []
    meta = _read_json(_original_file(chart_dir, 'original_meta.json')) or {}
    ctype = meta.get('chart_type')
    if ctype == 'scatterChart':
        orig = _read_json(_original_file(chart_dir, 'original_scatter.json'))
        base = _count_scatter_y(orig)
        djson = _read_json(chart_dir / 'data.json')
        fjson = _read_json(chart_dir / 'final_data.json')
        dlen = _count_scatter_y(djson)
        flen = _count_scatter_y(fjson)
        if dlen < base:
            errs.append(f'data.json y length {dlen} < original {base}')
        if flen < base:
            errs.append(f'final_data.json y length {flen} < original {base}')
    else:
        orig_lbls = _read_json(_original_file(chart_dir, 'original_labels.json')) or []
        base = len(orig_lbls)
        djson = _read_json(chart_dir / 'data.json')
        fjson = _read_json(chart_dir / 'final_data.json')
        dlen = _count_category_len(djson)
        flen = _count_category_len(fjson)
        if dlen < base:
            errs.append(f'data.json labels length {dlen} < original {base}')
        if flen < base:
            errs.append(f'final_data.json labels length {flen} < original {base}')
    return (len(errs) == 0), errs


def main():
    import re as _re
    charts = [c for c in PAGE.iterdir() if c.is_dir() and _re.match(r'^chart\d+$', c.name)]
    all_ok = True
    msgs: List[str] = []
    for c in charts:
        ok1, e1 = validate_original_vs_template(c)
        ok2, e2 = validate_counts(c)
        if ok1 and ok2:
            msgs.append(f'{c.name}: OK')
        else:
            all_ok = False
            if not ok1:
                msgs.append(f'{c.name}: 原始与模板不一致 -> ' + '; '.join(e1))
            if not ok2:
                msgs.append(f'{c.name}: 数据量校验失败 -> ' + '; '.join(e2))
    print('\n'.join(msgs))
    if not all_ok:
        sys.exit(1)


if __name__ == '__main__':
    PAGE = Path(__file__).resolve().parent
    main()
"""


REQUIRED = {
    'build.py': BUILD_PY_TMPL,
    'build_original.py': BUILD_ORIGINAL_TMPL,
    'gen_preview.py': GEN_PREVIEW_TMPL,
    'validate.py': VALIDATE_TMPL,
}


def ensure_page(page_dir: Path) -> int:
    created = 0
    for fn, content in REQUIRED.items():
        fp = page_dir / fn
        if not fp.exists():
            fp.write_text(content, encoding='utf-8')
            created += 1
    return created


def main():
    ap = argparse.ArgumentParser(description='Ensure missing page scripts exist with generic implementations')
    ap.add_argument('--pages', nargs='*', default=None, help='pages like p8 p10 ...; default all p*')
    args = ap.parse_args()
    if args.pages:
        pages = [PAGES_DIR / p for p in args.pages]
    else:
        import re as _re
        pages = [p for p in PAGES_DIR.iterdir() if p.is_dir() and _re.match(r'^p\d+$', p.name)]
    total = 0
    for p in pages:
        total += ensure_page(p)
    print('Created files:', total)


if __name__ == '__main__':
    main()