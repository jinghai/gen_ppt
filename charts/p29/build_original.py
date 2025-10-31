"""
构建原始 PPT（仅本页），基于完整的 PowerPoint 模板。

策略与约束（MVP，避免过度设计）：
- 使用与 build.py 相同的完整 PowerPoint 模板（input/LRTBH.pptx），确保包含所有必需的结构元素。
- 从完整模板中提取当前页面的内容，替换到模板中。
- 严格校验 `ppt/embeddings` 中的嵌入数据类型，仅允许 `.xlsb`。
- 输出日志到当前页面 `logs/build_original.log`，并在控制台同步打印。
- 生成完整可用的 `pXX-original.pptx`（XX 为页码）。

该实现兼顾可读性与稳健性，满足当前需求并便于后续扩展。
"""

from __future__ import annotations

import zipfile
from datetime import datetime
from pathlib import Path
import xml.etree.ElementTree as ET
import yaml
import shutil
import tempfile


def _page_dir() -> Path:
    return Path(__file__).resolve().parent


def _slide_no_from_dir(page_dir: Path) -> int:
    name = page_dir.name
    if not name.startswith('p'):
        raise ValueError(f'Invalid page dir name: {name}')
    return int(name[1:])


def _resolve_tpl() -> Path:
    """解析完整的 PowerPoint 模板路径，与 build.py 保持一致"""
    base = Path(__file__).resolve().parents[2]
    try:
        cfg = yaml.safe_load((base / 'config.yaml').read_text(encoding='utf-8')) or {}
    except Exception:
        cfg = {}
    op = (cfg.get('project') or {}).get('original_ppt', 'input/LRTBH.pptx')
    p = Path(op)
    if not p.is_absolute():
        p = base / op
    return p


PAGE_DIR = _page_dir()
SLIDE_NO = _slide_no_from_dir(PAGE_DIR)
TEMPLATE_DIR = PAGE_DIR / 'template'
EMBED_DIR = TEMPLATE_DIR / 'ppt' / 'embeddings'
SLIDES_DIR = TEMPLATE_DIR / 'ppt' / 'slides'
PRES_DIR = TEMPLATE_DIR / 'ppt'
CHARTS_DIR = TEMPLATE_DIR / 'ppt' / 'charts'
CHARTS_RELS_DIR = CHARTS_DIR / '_rels'

# 使用完整的 PowerPoint 模板
TPL = _resolve_tpl()

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


def build() -> None:
    """基于完整 PowerPoint 模板构建原始 PPTX（单页）。"""
    log('Start build_original')
    
    # 检查完整模板是否存在
    if not TPL.exists():
        raise FileNotFoundError(f'Template not found: {TPL}')
    
    # 检查页面特定内容是否存在
    assert_micro_template_integrity()
    
    OUT_PPTX.parent.mkdir(parents=True, exist_ok=True)
    
    # 使用临时目录处理模板
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # 解压完整模板到临时目录
        with zipfile.ZipFile(TPL, 'r') as template_zip:
            template_zip.extractall(temp_path)
        
        log(f'Extracted template from {TPL}')
        
        # 替换页面特定的内容
        _replace_page_content(temp_path)
        
        # 重新打包为 PPTX
        with zipfile.ZipFile(OUT_PPTX, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            for p in sorted(temp_path.rglob('*')):
                if p.is_file():
                    arc = p.relative_to(temp_path)
                    z.write(p, arcname=str(arc))
        
        log(f'Wrote {OUT_PPTX}')


def _replace_page_content(temp_path: Path) -> None:
    """替换模板中的页面特定内容"""
    
    # 1. 替换 slide1.xml
    slide_src = SLIDES_DIR / 'slide1.xml'
    slide_dst = temp_path / 'ppt' / 'slides' / 'slide1.xml'
    if slide_src.exists() and slide_dst.exists():
        shutil.copy2(slide_src, slide_dst)
        log('Replaced slide1.xml')
    
    # 2. 替换 slide1.xml.rels
    slide_rels_src = SLIDES_DIR / '_rels' / 'slide1.xml.rels'
    slide_rels_dst = temp_path / 'ppt' / 'slides' / '_rels' / 'slide1.xml.rels'
    if slide_rels_src.exists() and slide_rels_dst.exists():
        shutil.copy2(slide_rels_src, slide_rels_dst)
        log('Replaced slide1.xml.rels')
    
    # 3. 替换图表文件
    if CHARTS_DIR.exists():
        charts_dst = temp_path / 'ppt' / 'charts'
        if charts_dst.exists():
            # 清空现有图表目录
            shutil.rmtree(charts_dst)
        # 复制新的图表目录
        shutil.copytree(CHARTS_DIR, charts_dst)
        log('Replaced charts directory')
    
    # 4. 替换嵌入文件
    if EMBED_DIR.exists():
        embed_dst = temp_path / 'ppt' / 'embeddings'
        if embed_dst.exists():
            # 清空现有嵌入目录
            shutil.rmtree(embed_dst)
        # 复制新的嵌入目录
        shutil.copytree(EMBED_DIR, embed_dst)
        log('Replaced embeddings directory')
    
    # 5. 替换媒体文件（如果存在）
    media_src = TEMPLATE_DIR / 'ppt' / 'media'
    if media_src.exists():
        media_dst = temp_path / 'ppt' / 'media'
        if media_dst.exists():
            # 清空现有媒体目录
            shutil.rmtree(media_dst)
        # 复制新的媒体目录
        shutil.copytree(media_src, media_dst)
        log('Replaced media directory')

    # 6. 过滤演示文稿的关系与幻灯片列表，仅保留 slide1
    keep_rid = _filter_presentation_rels(temp_path)
    _filter_presentation_xml(temp_path, keep_rid)
    _filter_content_types(temp_path)
    _normalize_app_xml_slides_count(temp_path)


def _filter_presentation_rels(temp_path: Path) -> str:
    """仅保留指向 slide1.xml 的关系，返回其 rId。

    - 文件：ppt/_rels/presentation.xml.rels
    - 规则：保留非 slide 类型的关系；slide 类型只保留 Target 为 slides/slide1.xml 的项。
    """
    rels_path = temp_path / 'ppt' / '_rels' / 'presentation.xml.rels'
    if not rels_path.exists():
        return ''

    ET.register_namespace('', 'http://schemas.openxmlformats.org/package/2006/relationships')
    tree = ET.parse(rels_path)
    root = tree.getroot()
    REL_TAG = '{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'

    keep_rid = ''
    to_remove = []
    for rel in list(root.findall(REL_TAG)):
        typ = rel.get('Type') or ''
        tgt = rel.get('Target') or ''
        if typ.endswith('/slide'):
            if tgt.replace('\\', '/') == 'slides/slide1.xml':
                keep_rid = rel.get('Id') or keep_rid
            else:
                to_remove.append(rel)
    for rel in to_remove:
        root.remove(rel)

    tree.write(rels_path, encoding='utf-8', xml_declaration=True)
    if not keep_rid:
        log('WARN: slide1 relationship not found; other slides removed but rId is empty')
    else:
        log(f'Filtered presentation.rels, keep slide rId={keep_rid}')
    return keep_rid


def _filter_presentation_xml(temp_path: Path, keep_rid: str) -> None:
    """在 presentation.xml 中仅保留 sldIdLst 里引用 keep_rid 的项。"""
    pres_xml = temp_path / 'ppt' / 'presentation.xml'
    if not pres_xml.exists():
        return

    ET.register_namespace('r', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships')
    ET.register_namespace('p', 'http://schemas.openxmlformats.org/presentationml/2006/main')
    tree = ET.parse(pres_xml)
    root = tree.getroot()
    P_NS = 'http://schemas.openxmlformats.org/presentationml/2006/main'
    R_NS = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'

    sldIdLst = root.find(f'{{{P_NS}}}sldIdLst')
    if sldIdLst is not None:
        to_remove = []
        for sldId in list(sldIdLst.findall(f'{{{P_NS}}}sldId')):
            rid = sldId.get(f'{{{R_NS}}}id')
            if keep_rid and rid == keep_rid:
                continue
            # 删除非 keep_rid 的元素
            to_remove.append(sldId)
        for s in to_remove:
            sldIdLst.remove(s)

    tree.write(pres_xml, encoding='utf-8', xml_declaration=True)
    log(f'Filtered presentation.xml, kept {1 if keep_rid else 0} slide entries')


def _filter_content_types(temp_path: Path) -> None:
    """在 [Content_Types].xml 中只保留 slide1 的 Override。"""
    ct_path = temp_path / '[Content_Types].xml'
    if not ct_path.exists():
        return
    tree = ET.parse(ct_path)
    root = tree.getroot()
    OV_TAG = '{http://schemas.openxmlformats.org/package/2006/content-types}Override'
    to_remove = []
    for ov in list(root.findall(OV_TAG)):
        part = ov.get('PartName') or ''
        if part.startswith('/ppt/slides/slide') and part != '/ppt/slides/slide1.xml':
            to_remove.append(ov)
    for ov in to_remove:
        root.remove(ov)
    tree.write(ct_path, encoding='utf-8', xml_declaration=True)
    if to_remove:
        log(f'Filtered [Content_Types].xml, removed {len(to_remove)} slide overrides')


def _normalize_app_xml_slides_count(temp_path: Path) -> None:
    """将 docProps/app.xml 的 <Slides> 设为 1。"""
    app_xml = temp_path / 'docProps' / 'app.xml'
    if not app_xml.exists():
        return
    tree = ET.parse(app_xml)
    root = tree.getroot()
    TAG = '{http://schemas.openxmlformats.org/officeDocument/2006/extended-properties}Slides'
    slides_el = root.find(TAG)
    if slides_el is None:
        # 如果不存在，尽量在根下插入一个，避免破坏结构
        slides_el = ET.Element(TAG)
        root.append(slides_el)
    slides_el.text = '1'
    tree.write(app_xml, encoding='utf-8', xml_declaration=True)
    log('Normalized docProps/app.xml Slides=1')


def main() -> None:
    try:
        build()
    except Exception as e:
        log(f'ERROR: {e!r}')
        raise


if __name__ == '__main__':
    main()