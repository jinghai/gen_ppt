#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从当前页面的微模板（template 目录）构建原始单页 PPT：

- 仅使用微模板内的资源（ppt/*），不回退或访问全局 UNZ；
- 解析 chart*.xml.rels 收集 embeddings 的引用，要求全部为旧数据 .xlsb；
- 缺失或扩展名不符合则立即报错（Fail Fast）；
- 将微模板完整打包为 output/pXX-original.pptx；
- 统一日志输出到 pXX/logs/build_original.log（同时打印到控制台）。

遵循 MVP 原则，避免过度设计：只做必要的校验与打包。
依赖：lxml>=5.2（解析 XML）
"""

from __future__ import annotations
import zipfile
from pathlib import Path
from datetime import datetime
from typing import Set
from lxml import etree as ET


def _page_dir() -> Path:
    return Path(__file__).resolve().parent


def _slide_no_from_dir(page_dir: Path) -> int:
    name = page_dir.name
    if not name.startswith('p'):
        raise ValueError(f'Invalid page dir name: {name}')
    return int(name[1:])


PAGE_DIR = _page_dir()
SLIDE_NO = _slide_no_from_dir(PAGE_DIR)
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
    """同时写入页面日志文件与控制台。"""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f'[{ts}] {msg}\n'
    try:
        prev = LOG_FILE.read_text(encoding='utf-8') if LOG_FILE.exists() else ''
        LOG_FILE.write_text(prev + line, encoding='utf-8')
    except Exception:
        # 容忍并发写入或编码异常，保证控制台输出即可
        pass
    print(line, end='')


def _required_embeddings(charts_rels_dir: Path) -> Set[str]:
    """从 chart*.xml.rels 收集被引用的 embeddings 文件名。"""
    required: Set[str] = set()
    if not charts_rels_dir.exists():
        raise FileNotFoundError(f'Rels directory missing: {charts_rels_dir}')
    for rel_file in sorted(charts_rels_dir.glob('chart*.xml.rels')):
        try:
            root = ET.parse(str(rel_file)).getroot()
            for rel in root.findall('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
                tgt = rel.get('Target') or ''
                if 'embeddings/' in tgt:
                    required.add(Path(tgt).name)
        except Exception as e:
            raise RuntimeError(f'Parse rels failed: {rel_file}: {e}')
    return required


def _resolve_rel_target(rel_file: Path, target: str) -> Path:
    """相对 `slide1.xml.rels` 解析关系 Target，得到模板内绝对路径。"""
    base_dir = rel_file.parent.parent
    return (base_dir / Path(target)).resolve()


def _clean_slide1_rels_and_content_types() -> tuple[int, int]:
    """清理无效关系与内容类型覆盖，提升原始 PPTX 的可打开性。"""
    removed_rels = 0
    removed_ct = 0

    # 关系清理
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

    # 内容类型清理
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
    """基本存在性与 embeddings 合规性校验。"""
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
            raise FileNotFoundError(f'Embedding not .xlsb: {name} (must use old .xlsb data)')
        fp = EMBED_DIR / name
        if not fp.exists():
            raise FileNotFoundError(f'Embedding file missing: {fp}')


def _zip_template_dir(tpl_dir: Path, out_pptx: Path) -> None:
    """将微模板目录完整压缩为 PPTX。"""
    out_pptx.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out_pptx, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for p in tpl_dir.rglob('*'):
            if p.is_dir():
                continue
            rel = p.relative_to(tpl_dir)
            z.write(p, str(rel))


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