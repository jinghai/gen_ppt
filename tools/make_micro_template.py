#!/usr/bin/env python3
import argparse
import shutil
import zipfile
from pathlib import Path
from typing import Set, Tuple, List
from lxml import etree as ET
import yaml


def _find_repo_root(start: Path) -> Path:
    root = start
    while root.parent != root:
        if (root / 'config.yaml').exists() and (root / 'input').exists():
            return root
        root = root.parent
    # fallback: gen_ppt directory
    return start


def _load_cfg(repo_root: Path) -> dict:
    try:
        return yaml.safe_load((repo_root / 'config.yaml').read_text(encoding='utf-8')) or {}
    except Exception:
        return {}


def _resolve(root: Path, p: str) -> Path:
    q = Path(p)
    return q if q.is_absolute() else (root / q)


def _read_text(p: Path) -> str:
    return p.read_text(encoding='utf-8')


def _collect_from_slide(unz_root: Path, slide_no: int) -> Tuple[Set[str], Set[str], str, str, Set[str], Set[str]]:
    """
    From UNZIPPED ppt tree, collect assets referenced by a specific slide:
    - charts (names)
    - images (names)
    - slideLayout path (relative under ppt/)
    - slideMaster path (relative under ppt/)
    - embeddings (names)
    - image extensions
    """
    ppt = unz_root / 'ppt'
    slides_rels = ppt / 'slides' / '_rels' / f'slide{slide_no}.xml.rels'
    charts: Set[str] = set()
    images: Set[str] = set()
    embeddings: Set[str] = set()
    img_exts: Set[str] = set()
    slide_layout_rel_target: str = ''
    slide_master_rel_target: str = ''

    if slides_rels.exists():
        rel_root = ET.fromstring(slides_rels.read_bytes())
        for rel in rel_root.findall('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
            typ = rel.get('Type') or ''
            tgt = rel.get('Target') or ''
            if typ.endswith('/chart'):
                charts.add(Path(tgt).name)
                # check chart rels for embeddings
                chart_rel = ppt / 'charts' / '_rels' / f"{Path(tgt).name}.rels"
                if chart_rel.exists():
                    mm = ET.fromstring(chart_rel.read_bytes())
                    for crel in mm.findall('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
                        ctyp = crel.get('Type') or ''
                        ctgt = crel.get('Target') or ''
                        if ctyp.endswith('/oleObject') or ('embeddings/' in ctgt):
                            name = Path(ctgt).name
                            embeddings.add(name)
            elif typ.endswith('/image'):
                name = Path(tgt).name
                images.add(name)
                ext = Path(name).suffix[1:].lower()
                if ext:
                    img_exts.add(ext)
            elif typ.endswith('/slideLayout'):
                slide_layout_rel_target = tgt  # e.g., 'slideLayouts/slideLayout12.xml'
            # notesSlide ignored

    # resolve slide master from slide layout rels
    if slide_layout_rel_target:
        layout_rels = ppt / 'slideLayouts' / '_rels' / f"{Path(slide_layout_rel_target).name}.rels"
        if layout_rels.exists():
            lr_root = ET.fromstring(layout_rels.read_bytes())
            for rel in lr_root.findall('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
                typ = rel.get('Type') or ''
                tgt = rel.get('Target') or ''
                if typ.endswith('/slideMaster'):
                    slide_master_rel_target = tgt  # e.g., '../slideMasters/slideMaster3.xml'
                    break

    return charts, images, slide_layout_rel_target, slide_master_rel_target, embeddings, img_exts


def _build_content_types(slide_no: int, charts: Set[str], embeddings: Set[str], img_exts: Set[str], has_theme: bool, layout_name: str, master_name: str) -> str:
    defaults = [
        '  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
        '  <Default Extension="xml" ContentType="application/xml"/>'
    ]
    for ext in sorted(img_exts):
        mime = 'image/jpeg' if ext in ('jpg', 'jpeg') else f'image/{ext}'
        defaults.append(f'  <Default Extension="{ext}" ContentType="{mime}"/>')
    # common spreadsheet embeddings
    defaults.append('  <Default Extension="xlsx" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"/>')

    overrides = [
        '  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>',
        '  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>',
        '  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>',
        f'  <Override PartName="/ppt/slides/slide1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
    ]
    if has_theme:
        overrides.append('  <Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>')
    if layout_name:
        overrides.append(f'  <Override PartName="/ppt/slideLayouts/{layout_name}" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>')
    if master_name:
        overrides.append(f'  <Override PartName="/ppt/slideMasters/{master_name}" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>')
    for c in sorted(charts):
        overrides.append(f'  <Override PartName="/ppt/charts/{c}" ContentType="application/vnd.openxmlformats-officedocument.drawingml.chart+xml"/>')
    for emb in sorted(embeddings):
        # best-effort: treat as spreadsheet unless .bin or .xlsb
        ext = Path(emb).suffix.lower()
        if ext == '.xlsb':
            ct = 'application/vnd.ms-excel.sheet.binary.macroEnabled.12'
        elif ext == '.bin':
            ct = 'application/vnd.ms-office.oleObject'
        else:
            ct = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        overrides.append(f'  <Override PartName="/ppt/embeddings/{emb}" ContentType="{ct}"/>')

    xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">\n'
        + '\n'.join(defaults) + '\n'
        + '\n'.join(overrides) + '\n'
        + '</Types>'
    )
    return xml


def _build_presentation(slide_no: int, has_theme: bool) -> Tuple[str, str, str, str]:
    pres_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">\n'
        '  <p:sldIdLst>\n'
        '    <p:sldId id="256" r:id="rId1"/>\n'
        '  </p:sldIdLst>\n'
        '  <p:defaultTextStyle/>\n'
        '</p:presentation>'
    )
    pres_rels_lines = [
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide1.xml"/>'
    ]
    if has_theme:
        pres_rels_lines.append('<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="theme/theme1.xml"/>')
    pres_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        + ''.join(pres_rels_lines) + '</Relationships>'
    )
    rels_top = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">\n'
        '  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>\n'
        '  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>\n'
        '  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>\n'
        '</Relationships>'
    )
    core_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n'
        '  <dc:title>Micro template</dc:title>\n'
        '</cp:coreProperties>'
    )
    app_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">\n'
        '  <Application>Microsoft Office PowerPoint</Application>\n'
        '</Properties>'
    )
    return pres_xml, pres_rels, rels_top, core_xml + '\n' + app_xml


def make_micro_template_for_page(page_dir: Path, repo_root: Path, unz_root: Path) -> None:
    page_name = page_dir.name
    if not page_name.startswith('p'):
        raise ValueError(f'Invalid page dir: {page_dir}')
    slide_no = int(page_name[1:])
    tpl_dir = page_dir / 'template'
    if tpl_dir.exists():
        shutil.rmtree(str(tpl_dir))
    # ensure base structure
    (tpl_dir / 'ppt' / 'slides' / '_rels').mkdir(parents=True, exist_ok=True)
    (tpl_dir / 'ppt' / 'charts' / '_rels').mkdir(parents=True, exist_ok=True)
    (tpl_dir / 'ppt' / 'media').mkdir(parents=True, exist_ok=True)
    (tpl_dir / 'ppt' / 'embeddings').mkdir(parents=True, exist_ok=True)
    (tpl_dir / 'ppt' / 'slideLayouts' / '_rels').mkdir(parents=True, exist_ok=True)
    (tpl_dir / 'ppt' / 'slideMasters' / '_rels').mkdir(parents=True, exist_ok=True)
    (tpl_dir / 'ppt' / 'theme').mkdir(parents=True, exist_ok=True)
    (tpl_dir / 'ppt' / '_rels').mkdir(parents=True, exist_ok=True)
    (tpl_dir / '_rels').mkdir(parents=True, exist_ok=True)
    (tpl_dir / 'docProps').mkdir(parents=True, exist_ok=True)

    ppt = unz_root / 'ppt'

    # copy slide xml and rels (renamed to slide1)
    src_slide = ppt / 'slides' / f'slide{slide_no}.xml'
    src_slide_rels = ppt / 'slides' / '_rels' / f'slide{slide_no}.xml.rels'
    if not src_slide.exists():
        raise FileNotFoundError(f'slide{slide_no}.xml not found in UNZIPPED root: {ppt}')
    (tpl_dir / 'ppt' / 'slides' / 'slide1.xml').write_text(_read_text(src_slide), encoding='utf-8')
    if src_slide_rels.exists():
        (tpl_dir / 'ppt' / 'slides' / '_rels' / 'slide1.xml.rels').write_bytes(src_slide_rels.read_bytes())

    # collect refs
    charts, images, layout_tgt, master_tgt, embeddings, img_exts = _collect_from_slide(unz_root, slide_no)

    # copy charts and rels
    charts_dir = ppt / 'charts'
    charts_rels_dir = charts_dir / '_rels'
    for c in sorted(charts):
        cp = charts_dir / c
        if cp.exists():
            (tpl_dir / 'ppt' / 'charts' / c).write_bytes(cp.read_bytes())
        cr = charts_rels_dir / f'{c}.rels'
        if cr.exists():
            (tpl_dir / 'ppt' / 'charts' / '_rels' / f'{c}.rels').write_bytes(cr.read_bytes())

    # copy embeddings
    emb_dir = ppt / 'embeddings'
    for emb in sorted(embeddings):
        ep = emb_dir / emb
        if ep.exists():
            (tpl_dir / 'ppt' / 'embeddings' / emb).write_bytes(ep.read_bytes())

    # copy images
    media_dir = ppt / 'media'
    for img in sorted(images):
        ip = media_dir / img
        if ip.exists():
            (tpl_dir / 'ppt' / 'media' / img).write_bytes(ip.read_bytes())

    # copy slideLayout and slideMaster (+theme)
    has_theme = False
    layout_name = ''
    master_name = ''
    if layout_tgt:
        layout_name = Path(layout_tgt).name
        layout_xml = ppt / 'slideLayouts' / layout_name
        layout_rels = ppt / 'slideLayouts' / '_rels' / f'{layout_name}.rels'
        if layout_xml.exists():
            (tpl_dir / 'ppt' / 'slideLayouts' / layout_name).write_bytes(layout_xml.read_bytes())
        if layout_rels.exists():
            (tpl_dir / 'ppt' / 'slideLayouts' / '_rels' / f'{layout_name}.rels').write_bytes(layout_rels.read_bytes())
    if master_tgt:
        # master_tgt may be '../slideMasters/slideMaster#.xml'
        master_name = Path(master_tgt).name
        master_xml = ppt / 'slideMasters' / master_name
        master_rels = ppt / 'slideMasters' / '_rels' / f'{master_name}.rels'
        if master_xml.exists():
            (tpl_dir / 'ppt' / 'slideMasters' / master_name).write_bytes(master_xml.read_bytes())
        if master_rels.exists():
            (tpl_dir / 'ppt' / 'slideMasters' / '_rels' / f'{master_name}.rels').write_bytes(master_rels.read_bytes())
            # parse theme from master rels
            mr_root = ET.fromstring(master_rels.read_bytes())
            for rel in mr_root.findall('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
                typ = rel.get('Type') or ''
                tgt = rel.get('Target') or ''
                if typ.endswith('/theme'):
                    theme_xml = ppt / 'theme' / Path(tgt).name
                    if theme_xml.exists():
                        (tpl_dir / 'ppt' / 'theme' / 'theme1.xml').write_bytes(theme_xml.read_bytes())
                        has_theme = True
                    break

    # build presentation.xml, rels, content types and docProps
    pres_xml, pres_rels, rels_top, docprops_xml = _build_presentation(slide_no, has_theme)
    (tpl_dir / 'ppt' / 'presentation.xml').write_text(pres_xml, encoding='utf-8')
    (tpl_dir / 'ppt' / '_rels' / 'presentation.xml.rels').write_text(pres_rels, encoding='utf-8')
    (tpl_dir / '_rels' / '.rels').write_text(rels_top, encoding='utf-8')
    # split docProps xml into core/app
    # We stored both in one string; write separately for clarity
    core_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n'
        '  <dc:title>Micro template</dc:title>\n'
        '</cp:coreProperties>'
    )
    app_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">\n'
        '  <Application>Microsoft Office PowerPoint</Application>\n'
        '</Properties>'
    )
    (tpl_dir / 'docProps' / 'core.xml').write_text(core_xml, encoding='utf-8')
    (tpl_dir / 'docProps' / 'app.xml').write_text(app_xml, encoding='utf-8')

    ct_xml = _build_content_types(slide_no, charts, embeddings, img_exts, has_theme, layout_name, master_name)
    (tpl_dir / '[Content_Types].xml').write_text(ct_xml, encoding='utf-8')

    print(f'[micro-template] built {tpl_dir} for {page_dir.name} (charts={len(charts)}, images={len(images)}, embeddings={len(embeddings)})')


def _zip_template_dir(tpl_dir: Path, out_pptx: Path) -> None:
    # zip the template directory structure into a valid pptx file
    out_pptx.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out_pptx, 'w', zipfile.ZIP_DEFLATED) as z:
        for p in tpl_dir.rglob('*'):
            if p.is_dir():
                continue
            rel = p.relative_to(tpl_dir)
            z.write(p, str(rel))


def main():
    ap = argparse.ArgumentParser(description='生成试点页微模板到 charts/pXX/template')
    ap.add_argument('--pages', nargs='*', help='指定页面（如 p8 p10 p24），不传则默认全部发现 charts/pXX')
    ap.add_argument('--zip-preview', action='store_true', help='同时打包 zip 预览到 charts/pXX/output/pXX.template.pptx')
    args = ap.parse_args()

    repo_root = _find_repo_root(Path(__file__).resolve().parent)
    cfg = _load_cfg(repo_root)
    tr = (cfg.get('project') or {}).get('template_root', 'input/LRTBH-unzip')
    unz_root = _resolve(repo_root, tr)
    # 支持两种结构：ppt/charts 或顶层 charts
    if not (unz_root / 'ppt').exists() and (unz_root / 'charts').exists():
        # 允许传入 charts 根，向上推到包含 ppt 的根
        # 若为 charts 目录，则其父应为模板解压根
        unz_root = unz_root.parent

    charts_root = repo_root / 'charts'
    page_dirs: List[Path] = []
    if args.pages:
        for name in args.pages:
            p = charts_root / name
            if p.exists() and p.is_dir() and p.name.startswith('p'):
                page_dirs.append(p)
    else:
        for p in sorted(charts_root.glob('p*')):
            if p.is_dir():
                page_dirs.append(p)

    if not page_dirs:
        print('[micro-template] 未发现页面目录，退出。')
        return

    for pd in page_dirs:
        try:
            make_micro_template_for_page(pd, repo_root, unz_root)
            if args.zip_preview:
                out_dir = pd / 'output'
                out_dir.mkdir(parents=True, exist_ok=True)
                out_pptx = out_dir / f"{pd.name}.template.pptx"
                _zip_template_dir(pd / 'template', out_pptx)
                print(f"[micro-template] 预览已打包: {out_pptx}")
        except Exception as e:
            print(f"[micro-template] 构建 {pd.name} 失败: {e}")

if __name__ == '__main__':
    main()