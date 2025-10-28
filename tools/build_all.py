#!/usr/bin/env python3
import zipfile
import shutil
from pathlib import Path
import yaml
import subprocess
import sys
import argparse
import re
import logging
from typing import List, Optional, Dict, Any

# 找到 gen_ppt 根目录（需同时包含 config.yaml 与 input 目录）
ROOT = Path(__file__).resolve().parent
while ROOT.parent != ROOT:
    if (ROOT / 'config.yaml').exists() and (ROOT / 'input').exists():
        break
    ROOT = ROOT.parent
else:
    ROOT = Path(__file__).resolve().parents[1]

CONFIG = ROOT / 'config.yaml'
P10_CONFIG_CANDIDATES = [
    ROOT / 'charts' / 'p10' / 'config.yaml',
]

# 从配置读取公共路径，提供合理的回退
try:
    _cfg = yaml.safe_load(CONFIG.read_text(encoding='utf-8')) or {}
except Exception:
    _cfg = {}
_proj = _cfg.get('project') or {}

def _resolve(p: str) -> Path:
    rp = Path(p)
    return rp if rp.is_absolute() else ROOT / p

DEFAULT_TEMPLATE_PPT = _resolve(_proj.get('original_ppt', 'input/LRTBH.pptx'))
UNZIPPED = _resolve(_proj.get('template_root', 'input/LRTBH-unzip'))
_out_root = _proj.get('output_root', 'output')
OUT_DEFAULT = _resolve(_out_root) / 'LRTBH-final.pptx'
ORIG_OUT_DEFAULT = _resolve(_out_root) / 'LRTBH-final-original.pptx'

# REPLACE_MAP 由配置驱动

def path_in_unzipped(*parts: str) -> Path:
    """优先返回 UNZIPPED/ppt/... 子树中的路径，若不存在则回退至 UNZIPPED 顶层。"""
    nested = UNZIPPED / 'ppt'
    candidate = nested.joinpath(*parts)
    if candidate.exists():
        return candidate
    return UNZIPPED.joinpath(*parts)


def collect_page_replace_charts() -> list:
    pages_roots = [ROOT / 'charts']
    names = []
    for pr in pages_roots:
        if not pr.exists():
            continue
        for p in pr.iterdir():
            if not p.is_dir() or not p.name.startswith('p'):
                continue
            cfg = p / 'config.yaml'
            if cfg.exists():
                try:
                    data = yaml.safe_load(cfg.read_text(encoding='utf-8')) or {}
                except Exception:
                    data = {}
                charts = (data.get('output') or {}).get('replace_charts') or []
                for c in charts:
                    if c not in names:
                        names.append(c)
    return names


def load_out_path_and_mode():
    charts_override = None
    mode_override = None
    # check p10 config in new unified path first, then fallback
    for p10_cfg in P10_CONFIG_CANDIDATES:
        if p10_cfg.exists():
            try:
                p10 = yaml.safe_load(p10_cfg.read_text(encoding='utf-8')) or {}
            except Exception:
                p10 = {}
            charts_override = p10.get('output', {}).get('replace_charts', charts_override)
            mode_override = p10.get('output', {}).get('final_mode', mode_override)
            break
    if CONFIG.exists():
        cfg = yaml.safe_load(CONFIG.read_text(encoding='utf-8')) or {}
        out = cfg.get('output', {}).get('final_ppt')
        mode = cfg.get('output', {}).get('final_mode', 'updated')
        charts = cfg.get('output', {}).get('replace_charts', [])
        # p10 overrides
        if charts_override:
            charts = charts_override
        if mode_override:
            mode = mode_override
        # aggregate from pages
        page_charts = collect_page_replace_charts()
        if page_charts:
            charts = list(dict.fromkeys(charts + [c for c in page_charts if c not in charts]))
        return (ROOT / out if out else OUT_DEFAULT), mode, charts
    # defaults when no global config
    charts = charts_override or ['chart8.xml','chart9.xml']
    mode = mode_override or 'updated'
    # merge with per-page configs if present
    page_charts = collect_page_replace_charts()
    for c in page_charts:
        if c not in charts:
            charts.append(c)
    return OUT_DEFAULT, mode, charts


def compose_final(template: Path, out_path: Path, mode: str, charts: list):
    if not template.exists():
        raise FileNotFoundError(template)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(template, 'r') as zin, zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as zout:
        names = set(zin.namelist())
        for name in zin.namelist():
            if mode == 'updated' and name.startswith('ppt/charts/') and Path(name).name in charts:
                src = path_in_unzipped('charts', Path(name).name)
                if src.exists():
                    zout.writestr(name, src.read_bytes())
                else:
                    zout.writestr(name, zin.read(name))
            else:
                zout.writestr(name, zin.read(name))
        # 同步 chart 关系：优先使用 UNZIPPED 的 rels，否则保留模板
        for chart_name in charts:
            rel_name = f'ppt/charts/_rels/{chart_name}.rels'
            src_rels = path_in_unzipped('charts', '_rels', f'{chart_name}.rels')
            if src_rels.exists():
                zout.writestr(rel_name, src_rels.read_bytes())
            elif rel_name in names:
                zout.writestr(rel_name, zin.read(rel_name))

    print('Composed', out_path, 'mode=', mode, 'charts=', charts)


def _validate_replaced_charts(out_ppt: Path, template: Path, chart_names: List[str]) -> Dict[str, Any]:
    """对最终合成稿中被替换的图表进行轻量校验：确认这些图表"数据已发生变化"。
    逻辑：解析 out_ppt 与 template 的 chart*.xml，若数据完全相同，则视为未变更（潜在问题）。
    返回 {'total':N,'changed':A,'unchanged':B,'charts':[...]} 的摘要。
    """
    from extract_chart_cache import parse_chart_xml  # 复用解析工具
    summary: Dict[str, Any] = {
        'total': 0,
        'changed': 0,
        'unchanged': 0,
        'charts': [],
    }
    if not chart_names:
        return summary
    if not out_ppt.exists() or not template.exists():
        return summary
    try:
        with zipfile.ZipFile(out_ppt, 'r') as znew, zipfile.ZipFile(template, 'r') as zorig:
            for cn in chart_names:
                path = f'ppt/charts/{cn}'
                detail: Dict[str, Any] = {'chart': cn, 'ok': True}
                try:
                    new_xml = znew.read(path)
                    orig_xml = zorig.read(path)
                except KeyError:
                    detail['ok'] = False
                    detail['error'] = 'missing chart in zip'
                    summary['charts'].append(detail)
                    continue
                new_data = parse_chart_xml(new_xml)
                orig_data = parse_chart_xml(orig_xml)
                changed = False
                if new_data.get('chart_type') == 'scatterChart':
                    ns = new_data.get('scatter_series', [])
                    os = orig_data.get('scatter_series', [])
                    # 发生变化：任意系列的 x/y 不同 或 系列数量不同
                    if len(ns) != len(os):
                        changed = True
                    else:
                        for i in range(len(ns)):
                            if ns[i].get('x') != os[i].get('x') or ns[i].get('y') != os[i].get('y'):
                                changed = True
                                break
                    detail['type'] = 'scatter'
                else:
                    nl = new_data.get('labels', [])
                    ol = orig_data.get('labels', [])
                    if nl != ol:
                        changed = True
                    nser = new_data.get('series', [])
                    oser = orig_data.get('series', [])
                    if len(nser) != len(oser):
                        changed = True
                    else:
                        for i in range(len(nser)):
                            if nser[i].get('values') != oser[i].get('values'):
                                changed = True
                                break
                    detail['type'] = 'categorical'
                detail['changed'] = changed
                summary['charts'].append(detail)
    except Exception as e:
        # 保守处理：不影响构建流程，仅记录错误
        return {'total': 0, 'matched': 0, 'mismatched': 0, 'error': str(e), 'charts': []}
    summary['total'] = len(chart_names)
    summary['changed'] = sum(1 for d in summary['charts'] if d.get('changed'))
    summary['unchanged'] = sum(1 for d in summary['charts'] if not d.get('changed'))
    return summary


def _read_text(p: Path) -> str:
    return p.read_text(encoding='utf-8')


def _is_readable_zip(p: Path) -> bool:
    if not p or not p.exists():
        return False
    try:
        with zipfile.ZipFile(p, 'r') as z:
            names = z.namelist()
            # 至少包含顶层关系与 presentation 相关内容才视为可用
            return any(n.startswith('ppt/slides/') for n in names) and ('[Content_Types].xml' in names)
    except Exception:
        return False


def compose_without_template(out_path: Path):
    """当原始模板缺失或损坏时，直接从 UNZIPPED 构造一个可打开的 PPTX。
    - 枚举 slides/slide*.xml，构造 presentation.xml 与其关系；
    - 过滤每页 slide rels 中的 slideLayout/notesSlide 关系，保留 chart/image；
    - 复制 charts 及其 rels，收集并复制 embeddings；
    - 复制 media 和 theme1.xml（若存在）；
    - 动态生成 [Content_Types].xml 覆盖项。
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)

    slides_dir = path_in_unzipped('slides')
    charts_dir = path_in_unzipped('charts')
    charts_rels_dir = charts_dir / '_rels'
    media_dir = path_in_unzipped('media')
    theme_path = path_in_unzipped('theme', 'theme1.xml')
    embed_dir = path_in_unzipped('embeddings')
    rels_dir = slides_dir / '_rels'

    if not slides_dir.exists():
        raise FileNotFoundError(f"missing slides dir: {slides_dir}")
    slide_files = sorted([p for p in slides_dir.glob('slide*.xml')], key=lambda p: int(p.stem.replace('slide','')))
    if not slide_files:
        raise FileNotFoundError(f"no slides in {slides_dir}")

    slide_nums = [int(p.stem.replace('slide','')) for p in slide_files]

    # 解析每页的 rels，保留 chart/image，收集 chart 与 image/embeddings
    per_slide_rels = {}
    charts_to_copy = set()
    images_to_copy = set()
    embeddings_to_copy = set()
    for snum in slide_nums:
        rel_path = rels_dir / f'slide{snum}.xml.rels'
        keep_rels = []
        if rel_path.exists():
            txt = _read_text(rel_path)
            for m in re.finditer(r'<Relationship[^>]+Id="([^"]+)"[^>]+Type="([^"]+)"[^>]+Target="([^"]+)"', txt):
                rid, typ, tgt = m.group(1), m.group(2), m.group(3)
                if typ.endswith('/chart'):
                    keep_rels.append((rid, typ, tgt))
                    charts_to_copy.add(Path(tgt).name)
                    # 查 chart rels 的嵌入
                    chart_rel = charts_rels_dir / f"{Path(tgt).name}.rels"
                    if chart_rel.exists():
                        cr_txt = _read_text(chart_rel)
                        mm = re.search(r'Target="\./\./embeddings/([^"]+)"', cr_txt)
                        if mm:
                            embeddings_to_copy.add(mm.group(1))
                elif typ.endswith('/image'):
                    keep_rels.append((rid, typ, tgt))
                    images_to_copy.add(Path(tgt).name)
                elif typ.endswith('/slideLayout') or typ.endswith('/notesSlide'):
                    # 跳过指向缺失的布局/备注，避免无效引用
                    continue
                else:
                    # 其他类型忽略
                    continue
        per_slide_rels[snum] = keep_rels

    # Content-Types 默认项（rels/xml + 动态图片扩展）
    img_exts = {Path(n).suffix[1:].lower() for n in images_to_copy if Path(n).suffix}
    defaults = [
        '  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
        '  <Default Extension="xml" ContentType="application/xml"/>'
    ]
    for ext in sorted(img_exts):
        mime = 'image/jpeg' if ext in ('jpg','jpeg') else f'image/{ext}'
        defaults.append(f'  <Default Extension="{ext}" ContentType="{mime}"/>')

    # 固定覆盖项 + 所有 slide + theme
    overrides_fixed = [
        '  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>',
        '  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>',
        '  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>'
    ]
    slide_overrides = [
        f'  <Override PartName="/ppt/slides/slide{s}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
        for s in slide_nums
    ]
    theme_overrides = []
    if theme_path.exists():
        theme_overrides.append('  <Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>')
    chart_overrides = [
        f'  <Override PartName="/ppt/charts/{c}" ContentType="application/vnd.openxmlformats-officedocument.drawingml.chart+xml"/>'
        for c in sorted(charts_to_copy)
    ]
    embed_overrides = []
    for emb in sorted(embeddings_to_copy):
        ext = Path(emb).suffix.lower()
        if ext == '.xlsb':
            ct = 'application/vnd.ms-excel.sheet.binary.macroEnabled.12'
        elif ext == '.xlsx':
            ct = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        elif ext == '.bin':
            ct = 'application/vnd.ms-office.oleObject'
        else:
            ct = 'application/octet-stream'
        embed_overrides.append(f'  <Override PartName="/ppt/embeddings/{emb}" ContentType="{ct}"/>')

    ct_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">\n'
        + '\n'.join(defaults) + '\n'
        + '\n'.join(overrides_fixed) + '\n'
        + '\n'.join(slide_overrides) + '\n'
        + '\n'.join(theme_overrides) + '\n'
        + '\n'.join(chart_overrides) + '\n'
        + '\n'.join(embed_overrides) + '\n'
        + '</Types>'
    )

    # 构造 presentation.xml 与其 rels
    pres_sld_ids = []
    pres_rels_lines = []
    for idx, snum in enumerate(slide_nums, start=1):
        pres_sld_ids.append(f'    <p:sldId id="{255+idx}" r:id="rId{idx}"/>')
        pres_rels_lines.append(f'<Relationship Id="rId{idx}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{snum}.xml"/>')
    r_theme_id = None
    if theme_path.exists():
        r_theme_id = f'rId{len(slide_nums)+1}'
        pres_rels_lines.append(f'<Relationship Id="{r_theme_id}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="theme/theme1.xml"/>')
    pres_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">\n'
        '  <p:sldIdLst>\n' + '\n'.join(pres_sld_ids) + '\n  </p:sldIdLst>\n'
        '  <p:defaultTextStyle/>\n'
        '</p:presentation>'
    )
    pres_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        + ''.join(pres_rels_lines) + '</Relationships>'
    )

    # 顶层 _rels/.rels 与 docProps
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
        '  <dc:title>Composed without original template</dc:title>\n'
        '</cp:coreProperties>'
    )
    app_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">\n'
        '  <Application>Microsoft Office PowerPoint</Application>\n'
        '</Properties>'
    )

    # 写入 ZIP
    with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('[Content_Types].xml', ct_xml)
        z.writestr('_rels/.rels', rels_top)
        z.writestr('docProps/core.xml', core_xml)
        z.writestr('docProps/app.xml', app_xml)
        z.writestr('ppt/presentation.xml', pres_xml)
        z.writestr('ppt/_rels/presentation.xml.rels', pres_rels)

        # slides 与其过滤后的 rels
        for snum in slide_nums:
            src = slides_dir / f'slide{snum}.xml'
            z.writestr(f'ppt/slides/slide{snum}.xml', _read_text(src))
            rels_triplets = per_slide_rels.get(snum) or []
            rels_lines = [f'<Relationship Id="{rid}" Type="{typ}" Target="{tgt}"/>' for rid, typ, tgt in rels_triplets]
            slide_rels_xml = (
                '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
                '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                + ''.join(rels_lines) + '</Relationships>'
            )
            z.writestr(f'ppt/slides/_rels/slide{snum}.xml.rels', slide_rels_xml)

        # theme
        if theme_path.exists():
            z.writestr('ppt/theme/theme1.xml', _read_text(theme_path))

        # charts 与其 rels
        for c in sorted(charts_to_copy):
            cp = charts_dir / c
            if cp.exists():
                z.writestr(f'ppt/charts/{c}', cp.read_bytes())
            crp = charts_rels_dir / f'{c}.rels'
            if crp.exists():
                z.writestr(f'ppt/charts/_rels/{c}.rels', crp.read_bytes())

        # embeddings
        for emb in sorted(embeddings_to_copy):
            ep = embed_dir / emb
            if ep.exists():
                z.writestr(f'ppt/embeddings/{emb}', ep.read_bytes())

        # images
        for img in sorted(images_to_copy):
            ip = media_dir / img
            if ip.exists():
                z.writestr(f'ppt/media/{img}', ip.read_bytes())

    print('Composed without template:', out_path)


def discover_page_builders() -> List[Path]:
    roots = [ROOT / 'charts']
    candidates = []
    for pages_root in roots:
        if not pages_root.exists():
            continue
        for p in pages_root.iterdir():
            if p.is_dir() and p.name.startswith('p') and (p / 'build_all.py').exists():
                candidates.append(p / 'build_all.py')
    # dedupe and sort by page name
    uniq = {}
    for c in candidates:
        uniq[c.parent.name] = c
    return [uniq[k] for k in sorted(uniq.keys())]


def run_page_builders(pages: Optional[List[str]], mode: str):
    builders = discover_page_builders()
    if pages:
        name_set = set(pages)
        builders = [b for b in builders if b.parent.name in name_set]
    for b in builders:
        print('Running page builder:', b)
        subprocess.run([sys.executable, str(b), '--mode', mode], check=True)

def load_original_ppt() -> Path:
    if CONFIG.exists():
        try:
            cfg = yaml.safe_load(CONFIG.read_text(encoding='utf-8')) or {}
            val = (cfg.get('project') or {}).get('original_ppt')
            if val:
                p = Path(val)
                return p if p.is_absolute() else ROOT / val
        except Exception:
            pass
    return DEFAULT_TEMPLATE_PPT

def is_unzip_complete(dest_root: Path, required_charts: list) -> bool:
    charts_dir = dest_root / 'ppt' / 'charts'
    slides_rels = dest_root / 'ppt' / 'slides' / '_rels'
    if not charts_dir.exists() or not slides_rels.exists():
        return False
    if required_charts:
        for c in required_charts:
            if not (charts_dir / c).exists():
                return False
    return True

def ensure_unzipped(template: Path, dest_root: Path, required_charts: list):
    if template is None or not template.exists():
        # 无模板则跳过（可能后续仅跑单页构建）
        return
    if is_unzip_complete(dest_root, required_charts):
        return
    dest_root.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(template, 'r') as z:
        allowed_prefixes = (
            'ppt/charts/', 'ppt/charts/_rels/',
            'ppt/slides/', 'ppt/slides/_rels/',
            'ppt/theme/', 'ppt/embeddings/', 'ppt/media/'
        )
        for name in z.namelist():
            if not any(name.startswith(p) for p in allowed_prefixes):
                continue
            if name.endswith('/'):
                continue
            rel = name[len('ppt/'):]
            out = dest_root / 'ppt' / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(z.read(name))
    print('Unzipped selected ppt/* from', template, 'to', dest_root)


def compose_original(template: Path, out_path: Path):
    # 通过调用原始版重建脚本生成 LRTBH-final-original，而不是直接拷贝模板
    if not template.exists():
        raise FileNotFoundError(template)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    script = ROOT / 'tools' / 'build_all_original.py'
    if not script.exists():
        raise FileNotFoundError(script)
    # 显式传递输出路径，保持与全局配置一致
    subprocess.run([sys.executable, str(script), '--out', str(out_path)], check=True)
    print('Generated original via build_all_original:', out_path)


def _get_logger(log_file: Optional[Path] = None, level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger('build_all')
    if logger.handlers:
        return logger
    logger.setLevel(level)
    fmt = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(fmt)
    logger.addHandler(ch)
    if log_file is not None:
        try:
            log_file.parent.mkdir(parents=True, exist_ok=True)
        except Exception:
            pass
        fh = logging.FileHandler(str(log_file), encoding='utf-8')
        fh.setLevel(level)
        fh.setFormatter(fmt)
        logger.addHandler(fh)
    return logger


def main():
    ap = argparse.ArgumentParser(description='Compose final PPT and/or run per-page builders')
    ap.add_argument('--mode', choices=['modified','original','both'], default='both', help='which single-page builds to run')
    ap.add_argument('--pages', nargs='*', help='specific pages to run, e.g. p10')
    ap.add_argument('--skip-pages', action='store_true', help='skip running per-page build_all.py')
    ap.add_argument('--skip-compose', action='store_true', help='skip composing final PPT')
    ap.add_argument('--skip-compose-original', action='store_true', help='skip composing original PPT copy')
    default_log = ROOT / 'logs' / 'build_all.log'
    ap.add_argument('--log-file', type=Path, default=default_log, help='日志输出文件路径')
    ap.add_argument('--log-level', default='INFO', choices=['DEBUG','INFO','WARNING','ERROR','CRITICAL'], help='日志级别')
    args = ap.parse_args()

    logger = _get_logger(args.log_file, getattr(logging, args.log_level.upper(), logging.INFO))
    logger.info('Starting build_all with mode=%s pages=%s', args.mode, args.pages)

    # 加载配置的原始 PPT 路径与需要替换的图表列表，并确保解压可用
    out_path, mode, charts = load_out_path_and_mode()
    template_ppt = load_original_ppt()
    ensure_unzipped(template_ppt, UNZIPPED, charts)
    logger.info('Template PPT: %s', template_ppt)
    logger.info('UNZIPPED root: %s', UNZIPPED)
    logger.info('Out path: %s, mode: %s, charts to replace: %d', out_path, mode, len(charts))

    if not args.skip_pages:
        logger.info('Running per-page builders...')
        run_page_builders(args.pages, args.mode)

    if not args.skip_compose:
        if _is_readable_zip(template_ppt):
            compose_final(template_ppt, out_path, mode, charts)
            # 轻量一致性校验（仅针对被替换的图表）
            if charts:
                summary = _validate_replaced_charts(out_path, template_ppt, charts)
                print('Final validation summary (changed vs unchanged):', {
                    'total': summary.get('total'),
                    'changed': summary.get('changed'),
                    'unchanged': summary.get('unchanged'),
                })
                logger.info('Final validation summary: total=%s changed=%s unchanged=%s', summary.get('total'), summary.get('changed'), summary.get('unchanged'))
        else:
            print('[warn] original template not readable, composing from UNZIPPED fallback')
            logger.warning('Original template not readable, composing from UNZIPPED fallback')
            compose_without_template(out_path)
    # 同步生成一份原始 PPT 拷贝，便于比对和审阅
    if not args.skip_compose_original:
        if _is_readable_zip(template_ppt):
            compose_original(template_ppt, ORIG_OUT_DEFAULT)
            logger.info('Generated original copy via build_all_original: %s', ORIG_OUT_DEFAULT)
        else:
            print('[warn] skip composing original copy due to unreadable template')
            logger.warning('Skip composing original copy due to unreadable template')


if __name__ == '__main__':
    main()