"""
构建原始 PPT（仅本页），基于页面微模板。

策略与约束（MVP，避免过度设计）：
- 只使用页面 `template/` 目录下的微模板，不做 UNZ 回退或跨页面依赖。
- 严格校验 `ppt/embeddings` 中的嵌入数据类型，仅允许 `.xlsb`。
- 需要存在关键文件：`slide1.xml`、`presentation.xml(.rels)`、`[Content_Types].xml`、`ppt/charts/_rels/`。
- 输出日志到当前页面 `logs/build_original.log`，并在控制台同步打印。
- 直接将微模板目录打包为 `pXX-original.pptx`（XX 为页码），不进行冗余的 XML 过滤（微模板已是单页）。

该实现兼顾可读性与稳健性，满足当前需求并便于后续扩展。
"""

from __future__ import annotations

import zipfile
from datetime import datetime
from pathlib import Path
import xml.etree.ElementTree as ET


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
SLIDES_DIR = TEMPLATE_DIR / 'ppt' / 'slides'
PRES_DIR = TEMPLATE_DIR / 'ppt'
CHARTS_DIR = TEMPLATE_DIR / 'ppt' / 'charts'
CHARTS_RELS_DIR = CHARTS_DIR / '_rels'

OUT_PPTX = PAGE_DIR / 'output' / f'p{SLIDE_NO}-original.pptx'
LOG_DIR = PAGE_DIR / 'logs'
LOG_FILE = LOG_DIR / 'build_original.log'


def log(msg: str) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f'[{ts}] [p{SLIDE_NO}] {msg}'
    print(line)
    with LOG_FILE.open('a', encoding='utf-8') as f:
        f.write(line + '\n')


def assert_micro_template_integrity() -> None:
    """校验微模板的关键结构与约束。"""
    if not TEMPLATE_DIR.exists():
        raise FileNotFoundError(f'Micro template missing: {TEMPLATE_DIR}')

    required_files = [
        SLIDES_DIR / 'slide1.xml',
        PRES_DIR / 'presentation.xml',
        PRES_DIR / '_rels' / 'presentation.xml.rels',
        TEMPLATE_DIR / '[Content_Types].xml',
    ]
    for p in required_files:
        if not p.exists():
            raise FileNotFoundError(f'Required file missing: {p}')

    if not EMBED_DIR.exists():
        raise FileNotFoundError(f'Embeddings directory missing: {EMBED_DIR}')
    bad = [p for p in EMBED_DIR.iterdir() if p.is_file() and p.suffix.lower() != '.xlsb']
    if bad:
        raise ValueError(f'Only .xlsb allowed in embeddings, found: {", ".join(b.name for b in bad)}')

    if not CHARTS_RELS_DIR.exists():
        raise FileNotFoundError(f'Charts rels directory missing: {CHARTS_RELS_DIR}')


def _resolve_rel_target(rel_file: Path, target: str) -> Path:
    """将 Relationship 的 Target 相对路径解析为微模板内的绝对文件路径。

    - 关系文件位于形如 `.../_rels/xxx.rels`，其基准目录是对应部件所在目录（如 `ppt/slides`）。
    - 返回值为解析后的实际文件路径（绝对路径）。
    """
    base_dir = rel_file.parent.parent  # e.g. ppt/slides
    cand = (base_dir / Path(target)).resolve()
    return cand


def _clean_slide1_rels_and_content_types() -> tuple[int, int]:
    """清理微模板中的无效关系与内容类型声明。

    执行两项清理（最小改动，MVP）：
    1) slide1.xml.rels：移除指向不存在目标（如缺失的 notesSlides/notesMaster）。
    2) [Content_Types].xml：移除 Override 中引用的 PartName 在微模板中不存在的项。

    返回 (removed_rels, removed_ct_overrides) 二元组，便于日志记录。
    """
    removed_rels = 0
    removed_ct = 0

    # 1) 关系清理：仅针对 slide1 的关系文件
    slide_rels = TEMPLATE_DIR / 'ppt' / 'slides' / '_rels' / 'slide1.xml.rels'
    if slide_rels.exists():
        try:
            ET.register_namespace('', 'http://schemas.openxmlformats.org/package/2006/relationships')
            tree = ET.parse(slide_rels)
            root = tree.getroot()
            rel_tag = '{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'
            to_remove = []
            for rel in list(root.findall(rel_tag)):
                tgt = rel.get('Target') or ''
                # 解析目标并验证是否存在于微模板内
                cand = _resolve_rel_target(slide_rels, tgt)
                # 仅当目标确实位于 TEMPLATE_DIR 内且存在才保留
                try:
                    inside_tpl = (TEMPLATE_DIR in cand.parents) or (cand == TEMPLATE_DIR)
                except Exception:
                    inside_tpl = False
                if not inside_tpl or not cand.exists():
                    to_remove.append(rel)
            for rel in to_remove:
                root.remove(rel)
                removed_rels += 1
            if to_remove:
                tree.write(slide_rels, encoding='utf-8', xml_declaration=True)
        except Exception:
            # 解析失败不阻断打包（MVP策略），仅忽略清理以保证稳健性
            pass

    # 2) 内容类型清理：删除不存在的 Override PartName
    ct_path = TEMPLATE_DIR / '[Content_Types].xml'
    if ct_path.exists():
        try:
            tree = ET.parse(ct_path)
            root = tree.getroot()
            override_tag = '{http://schemas.openxmlformats.org/package/2006/content-types}Override'
            # 收集微模板内实际存在的文件（用于判断 PartName 是否有效）
            present = {f'/{p.relative_to(TEMPLATE_DIR).as_posix()}' for p in TEMPLATE_DIR.rglob('*') if p.is_file()}
            to_remove = []
            for ov in list(root.findall(override_tag)):
                part = ov.get('PartName') or ''
                if part and part not in present:
                    to_remove.append(ov)
            for ov in to_remove:
                root.remove(ov)
                removed_ct += 1
            if to_remove:
                tree.write(ct_path, encoding='utf-8', xml_declaration=True)
        except Exception:
            # 解析失败不阻断打包（MVP策略）
            pass

    return removed_rels, removed_ct


def build() -> None:
    """将微模板完整打包为原始 PPTX（单页）。"""
    log('Start build_original')
    assert_micro_template_integrity()
    # 在打包前执行关系与内容类型清理，避免无效引用导致 PPTX 不可打开
    rel_rm, ct_rm = _clean_slide1_rels_and_content_types()
    if rel_rm or ct_rm:
        log(f'Cleaned invalid refs: slide1.rels removed={rel_rm}, [Content_Types] removed={ct_rm}')
    OUT_PPTX.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(OUT_PPTX, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for p in sorted(TEMPLATE_DIR.rglob('*')):
            if p.is_file():
                arc = p.relative_to(TEMPLATE_DIR)
                z.write(p, arcname=str(arc))
    log(f'Wrote {OUT_PPTX}')


def main() -> None:
    try:
        build()
    except Exception as e:
        log(f'ERROR: {e!r}')
        raise


if __name__ == '__main__':
    main()