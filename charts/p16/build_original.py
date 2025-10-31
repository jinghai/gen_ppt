#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微模板构建原始单页 PPT：只用 template 资源；校验 .xlsb 嵌入；缺失即报错；统一日志。
"""
from __future__ import annotations
import zipfile
from pathlib import Path
from datetime import datetime
from typing import Set
from lxml import etree as ET

PAGE_DIR = Path(__file__).resolve().parent
SLIDE_NO = int(PAGE_DIR.name[1:])
TEMPLATE_DIR = PAGE_DIR / 'template'
EMBED_DIR = TEMPLATE_DIR / 'ppt' / 'embeddings'
CHARTS_DIR = TEMPLATE_DIR / 'ppt' / 'charts'
CHARTS_RELS_DIR = CHARTS_DIR / '_rels'
SLIDE_XML = TEMPLATE_DIR / 'ppt' / 'slides' / 'slide1.xml'
SLIDE_RELS = TEMPLATE_DIR / 'ppt' / 'slides' / '_rels' / 'slide1.xml.rels'
PRES_XML = TEMPLATE_DIR / 'ppt' / 'presentation.xml'
PRES_RELS = TEMPLATE_DIR / 'ppt' / '_rels' / 'presentation.xml.rels'
CONTENT_TYPES = TEMPLATE_DIR / '[Content_Types].xml'

OUT_PPTX = PAGE_DIR / 'output' / f'p{SLIDE_NO}-original.pptx'
LOG_DIR = PAGE_DIR / 'logs'
LOG_FILE = LOG_DIR / 'build_original.log'

def _log(msg: str) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f'[{ts}] {msg}\n'
    try:
        prev = LOG_FILE.read_text(encoding='utf-8') if LOG_FILE.exists() else ''
        LOG_FILE.write_text(prev + line, encoding='utf-8')
    except Exception:
        pass
    print(line, end='')

def _required_embeddings(charts_rels_dir: Path) -> Set[str]:
    req: Set[str] = set()
    if not charts_rels_dir.exists():
        raise FileNotFoundError(f'Rels directory missing: {charts_rels_dir}')
    for rel_file in sorted(charts_rels_dir.glob('chart*.xml.rels')):
        root = ET.parse(str(rel_file)).getroot()
        for rel in root.findall('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
            tgt = rel.get('Target') or ''
            if 'embeddings/' in tgt:
                req.add(Path(tgt).name)
    return req

def _resolve_rel_target(rel_file: Path, target: str) -> Path:
    base_dir = rel_file.parent.parent
    return (base_dir / Path(target)).resolve()

def _clean_slide1_rels_and_content_types() -> tuple[int, int]:
    removed_rels = 0
    removed_ct = 0

    if SLIDE_RELS.exists():
        try:
            root = ET.parse(str(SLIDE_RELS)).getroot()
            rel_tag = '{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'
            bad = []
            for rel in list(root.findall(rel_tag)):
                tgt = rel.get('Target') or ''
                cand = _resolve_rel_target(SLIDE_RELS, tgt)
                inside_tpl = (TEMPLATE_DIR in cand.parents) or (cand == TEMPLATE_DIR)
                if (not inside_tpl) or (not cand.exists()):
                    bad.append(rel)
            for r in bad:
                root.remove(r)
                removed_rels += 1
            if bad:
                ET.ElementTree(root).write(str(SLIDE_RELS), encoding='utf-8', xml_declaration=True)
        except Exception:
            pass

    if CONTENT_TYPES.exists():
        try:
            root = ET.parse(str(CONTENT_TYPES)).getroot()
            override_tag = '{http://schemas.openxmlformats.org/package/2006/content-types}Override'
            present = {f'/{p.relative_to(TEMPLATE_DIR).as_posix()}' for p in TEMPLATE_DIR.rglob('*') if p.is_file()}
            bad = []
            for ov in list(root.findall(override_tag)):
                part = ov.get('PartName') or ''
                if part and part not in present:
                    bad.append(ov)
            for ov in bad:
                root.remove(ov)
                removed_ct += 1
            if bad:
                ET.ElementTree(root).write(str(CONTENT_TYPES), encoding='utf-8', xml_declaration=True)
        except Exception:
            pass

    return removed_rels, removed_ct

def _validate_template() -> None:
    if not TEMPLATE_DIR.exists():
        raise FileNotFoundError(f'Micro-template missing: {TEMPLATE_DIR}')
    for p in [EMBED_DIR, CHARTS_DIR, CHARTS_RELS_DIR]:
        if not p.exists():
            raise FileNotFoundError(f'Micro-template subdir missing: {p}')
    for f in [SLIDE_XML, SLIDE_RELS, PRES_XML, PRES_RELS, CONTENT_TYPES]:
        if not f.exists():
            raise FileNotFoundError(f'Micro-template file missing: {f}')
    req = _required_embeddings(CHARTS_RELS_DIR)
    if not req:
        _log('No embeddings referenced by charts; continue.')
    for name in sorted(req):
        if not name.lower().endswith('.xlsb'):
            raise FileNotFoundError(f'Embedding not .xlsb: {name}')
        fp = EMBED_DIR / name
        if not fp.exists():
            raise FileNotFoundError(f'Embedding file missing: {fp}')

def _zip_template_dir(tpl_dir: Path, out_pptx: Path) -> None:
    out_pptx.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out_pptx, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for p in tpl_dir.rglob('*'):
            if p.is_dir():
                continue
            z.write(p, str(p.relative_to(tpl_dir)))

def main() -> int:
    _log(f'[p{SLIDE_NO}] build_original start')
    _validate_template()
    rel_rm, ct_rm = _clean_slide1_rels_and_content_types()
    if rel_rm or ct_rm:
        _log(f'Cleaned invalid refs: slide1.rels removed={rel_rm}, [Content_Types] removed={ct_rm}')
    _zip_template_dir(TEMPLATE_DIR, OUT_PPTX)
    _log(f'[p{SLIDE_NO}] build_original done: {OUT_PPTX}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())