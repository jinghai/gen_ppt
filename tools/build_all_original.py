#!/usr/bin/env python3
import json
import zipfile
import hashlib
from io import BytesIO
from pathlib import Path
import yaml
import logging
import warnings
from typing import Dict, Any, List, Optional
from lxml import etree as ET
import sys
import subprocess
import re

# 工程根目录与路径（gen_ppt 根）
ROOT = Path(__file__).resolve().parents[1]

def _load_proj_cfg() -> dict:
    try:
        cfg = yaml.safe_load((ROOT / 'config.yaml').read_text(encoding='utf-8')) or {}
    except Exception:
        cfg = {}
    return cfg.get('project') or {}

_proj = _load_proj_cfg()
TEMPLATE_PPT = (ROOT / (_proj.get('original_ppt') or 'input/LRTBH.pptx'))

def _resolve_unz_root() -> Path:
    tr = _proj.get('template_root', 'input/LRTBH-unzip')
    p = Path(tr)
    if not p.is_absolute():
        p = ROOT / tr
    return p

def _charts_dir(unz: Path) -> Path:
    d = unz / 'ppt' / 'charts'
    return d if d.exists() else unz / 'charts'

UNZIP_ROOT = _resolve_unz_root()
OUT_PATH = ROOT / (_proj.get('output_root') or 'output') / 'LRTBH-final-original.pptx'
REPORT_JSON = ROOT / (_proj.get('output_root') or 'output') / 'original_rebuild_validate.json'
REPORT_MD = ROOT / (_proj.get('output_root') or 'output') / 'original_rebuild_validate.md'

NS = {
    'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
}


def _get_logger(log_file: Optional[Path] = None, level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger('build_all_original')
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
    # 将 Python warnings 重定向到日志（文件与控制台）
    warnings.simplefilter('default')
    logging.captureWarnings(True)
    wlog = logging.getLogger('py.warnings')
    wlog.setLevel(level)
    wlog.addHandler(ch)
    if log_file is not None:
        wlog.addHandler(fh)
    return logger


def _replace_num_cache(parent: ET._Element, path: str, values: List[Any]):
    el = parent.find(path, namespaces=NS)
    if el is None:
        return
    num_ref = el.find('c:numRef', namespaces=NS)
    if num_ref is not None:
        cache = num_ref.find('c:numCache', namespaces=NS)
        if cache is None:
            cache = ET.SubElement(num_ref, f'{{{NS["c"]}}}numCache')
    else:
        cache = el.find('c:numLit', namespaces=NS)
        if cache is None:
            cache = ET.SubElement(el, f'{{{NS["c"]}}}numLit')
    # clear points
    for pt in list(cache.findall('c:pt', namespaces=NS)):
        cache.remove(pt)
    cnt = cache.find('c:ptCount', namespaces=NS)
    if cnt is None:
        cnt = ET.SubElement(cache, f'{{{NS["c"]}}}ptCount')
    cnt.set('val', str(len(values)))
    for i, v in enumerate(values):
        pt = ET.SubElement(cache, f'{{{NS["c"]}}}pt')
        pt.set('idx', str(i))
        ve = ET.SubElement(pt, f'{{{NS["c"]}}}v')
        ve.text = str(v)


def _replace_str_lit(parent: ET._Element, path: str, labels: List[str]):
    el = parent.find(path, namespaces=NS)
    if el is None:
        return
    str_ref = el.find('c:strRef', namespaces=NS)
    if str_ref is not None:
        cache = str_ref.find('c:strCache', namespaces=NS)
        if cache is None:
            cache = ET.SubElement(str_ref, f'{{{NS["c"]}}}strCache')
    else:
        cache = el.find('c:strLit', namespaces=NS)
        if cache is None:
            cache = ET.SubElement(el, f'{{{NS["c"]}}}strLit')
    for pt in list(cache.findall('c:pt', namespaces=NS)):
        cache.remove(pt)
    cnt = cache.find('c:ptCount', namespaces=NS)
    if cnt is None:
        cnt = ET.SubElement(cache, f'{{{NS["c"]}}}ptCount')
    cnt.set('val', str(len(labels)))
    for i, v in enumerate(labels):
        pt = ET.SubElement(cache, f'{{{NS["c"]}}}pt')
        pt.set('idx', str(i))
        ve = ET.SubElement(pt, f'{{{NS["c"]}}}v')
        ve.text = str(v)


def _parse_chart_type(plot_area: ET._Element) -> str:
    types_order = ['barChart', 'lineChart', 'pieChart', 'doughnutChart', 'areaChart', 'scatterChart']
    for t in types_order:
        if plot_area.find(f'c:{t}', namespaces=NS) is not None:
            return t
    return 'unknown'


def _load_original_for_chart_dir(chart_dir: Path) -> Optional[Dict[str, Any]]:
    # 支持 chart_dir 与 chart_dir/original 两种布局
    orig_dir = chart_dir / 'original'
    cand = lambda fname: [
        chart_dir / fname,
        orig_dir / fname,
    ]
    scatter_fp = next((p for p in cand('original_scatter.json') if p.exists()), None)
    labels_fp = next((p for p in cand('original_labels.json') if p.exists()), None)
    series_fp = next((p for p in cand('original_series.json') if p.exists()), None)

    if scatter_fp is not None:
        data = json.loads(scatter_fp.read_text(encoding='utf-8'))
        return {'chart_type': 'scatterChart', 'scatter_series': data}
    if labels_fp is not None and series_fp is not None:
        labels = json.loads(labels_fp.read_text(encoding='utf-8'))
        series = json.loads(series_fp.read_text(encoding='utf-8'))
        return {'chart_type': 'categorical', 'labels': labels, 'series': series}
    return None


def _build_chart_xml_bytes(chart_name: str, original_data: Dict[str, Any]) -> Optional[bytes]:
    # 优先使用 nested ppt/charts，若不存在则回退顶层 charts
    base_xml_candidates = [_charts_dir(UNZIP_ROOT) / chart_name]
    base_xml = next((p for p in base_xml_candidates if p.exists()), None)
    if not base_xml.exists():
        return None
    tree = ET.parse(str(base_xml))
    root = tree.getroot()
    plot_area = root.find('.//c:plotArea', namespaces=NS)
    if plot_area is None:
        return None
    chart_type = _parse_chart_type(plot_area)

    if original_data.get('chart_type') == 'scatterChart' or chart_type == 'scatterChart':
        ser_els = plot_area.find('c:scatterChart', namespaces=NS).findall('c:ser', namespaces=NS)
        series_list = original_data.get('scatter_series') or []
        for idx, ser in enumerate(ser_els):
            src = series_list[idx] if idx < len(series_list) else {'x': [], 'y': []}
            _replace_num_cache(ser, 'c:yVal', src.get('y', []))
            _replace_num_cache(ser, 'c:xVal', src.get('x', []))
    else:
        # 类别型图表：写 cat 与各系列 val
        target = None
        for t in ['barChart','lineChart','pieChart','doughnutChart','areaChart']:
            el = plot_area.find(f'c:{t}', namespaces=NS)
            if el is not None:
                target = el
                break
        if target is None:
            return None
        labels = original_data.get('labels') or []
        series = original_data.get('series') or []
        ser_els = target.findall('c:ser', namespaces=NS)
        for idx, ser in enumerate(ser_els):
            # 类别写在 ser 层级，parse_chart_xml 会从第一个 ser 的 c:cat 读取 labels
            _replace_str_lit(ser, 'c:cat', labels)
            values = series[idx] if idx < len(series) else []
            # 支持 {"name": ..., "values": [...] } 或直接列表
            if isinstance(values, dict):
                values = values.get('values', [])
            _replace_num_cache(ser, 'c:val', values)
    # 输出到内存
    bio = BytesIO()
    tree.write(bio, encoding='utf-8', xml_declaration=True)
    return bio.getvalue()


def _read_chart_name(chart_path_txt: Path) -> Optional[str]:
    if not chart_path_txt.exists():
        return None
    line = chart_path_txt.read_text(encoding='utf-8').strip()
    if not line:
        return None
    return Path(line).name  # e.g., chart209.xml


def _collect_rebuild_targets() -> Dict[str, Dict[str, Any]]:
    targets: Dict[str, Dict[str, Any]] = {}
    for chart_path_txt in (ROOT / 'charts').rglob('chart_path.txt'):
        chart_dir = chart_path_txt.parent
        chart_name = _read_chart_name(chart_path_txt)
        if not chart_name:
            continue
        orig = _load_original_for_chart_dir(chart_dir)
        if orig is None:
            continue
        targets[chart_name] = orig
    return targets


def _compose_ppt_from_template(template: Path, out_path: Path, chart_bytes_map: Dict[str, bytes]):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(template, 'r') as zin, zipfile.ZipFile(out_path, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            name = item.filename
            if name.startswith('ppt/charts/chart') and name.split('/')[-1] in chart_bytes_map:
                data = chart_bytes_map[name.split('/')[-1]]
                zout.writestr(name, data)
            else:
                zout.writestr(item, zin.read(name))


def _md5(fp: Path) -> str:
    h = hashlib.md5()
    with fp.open('rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


def _validate_against_original(out_ppt: Path, template: Path, chart_names: List[str]) -> Dict[str, Any]:
    from extract_chart_cache import parse_chart_xml  # 复用解析
    diffs = []
    with zipfile.ZipFile(out_ppt, 'r') as znew, zipfile.ZipFile(template, 'r') as zorig:
        for cn in chart_names:
            path = f'ppt/charts/{cn}'
            try:
                new_xml = znew.read(path)
                orig_xml = zorig.read(path)
            except KeyError:
                diffs.append({'chart': cn, 'error': 'missing in zip'})
                continue
            new_data = parse_chart_xml(new_xml)
            orig_data = parse_chart_xml(orig_xml)
            ok = True
            detail: Dict[str, Any] = {'chart': cn, 'ok': True}
            if new_data.get('chart_type') == 'scatterChart':
                ns = new_data.get('scatter_series', [])
                os = orig_data.get('scatter_series', [])
                if len(ns) != len(os):
                    ok = False
                else:
                    for i in range(len(ns)):
                        if ns[i].get('x') != os[i].get('x') or ns[i].get('y') != os[i].get('y'):
                            ok = False
                            break
                detail['type'] = 'scatter'
            else:
                nl = new_data.get('labels', [])
                ol = orig_data.get('labels', [])
                if nl != ol:
                    ok = False
                nser = new_data.get('series', [])
                oser = orig_data.get('series', [])
                if len(nser) != len(oser):
                    ok = False
                else:
                    for i in range(len(nser)):
                        if nser[i].get('values') != oser[i].get('values'):
                            ok = False
                            break
                detail['type'] = 'categorical'
            detail['ok'] = ok
            if not ok:
                detail['new'] = new_data
                detail['orig'] = orig_data
            diffs.append(detail)
    summary = {
        'total': len(chart_names),
        'matched': sum(1 for d in diffs if d.get('ok')),
        'mismatched': sum(1 for d in diffs if not d.get('ok')),
        'charts': diffs,
    }
    return summary


def _iter_pages(filter_pages: Optional[List[str]] = None) -> List[Path]:
    base = ROOT / 'charts'
    if not base.exists():
        return []
    if filter_pages:
        candidates = [base / p for p in filter_pages]
    else:
        candidates = [p for p in base.iterdir() if p.is_dir() and re.match(r'^p\d+$', p.name)]
    pages = [p for p in candidates if p.exists() and p.is_dir()]
    return sorted(pages, key=lambda x: x.name)


def run_page_build_originals(pages: Optional[List[str]] = None, logger: Optional[logging.Logger] = None) -> Dict[str, int]:
    """调用 charts 下各页面的 build_original.py（若存在）。

    返回统计：总页面数、尝试执行数、成功数、失败数。
    """
    logger = logger or _get_logger(None)
    page_dirs = _iter_pages(pages)
    total = len(page_dirs)
    executed = 0
    succeeded = 0
    failed = 0
    for page in page_dirs:
        script = page / 'build_original.py'
        if not script.exists():
            logger.debug('skip (no build_original.py): %s', page)
            continue
        executed += 1
        cmd = [sys.executable, str(script)]
        try:
            logger.info('running build_original.py for %s', page.name)
            subprocess.run(cmd, cwd=str(page), check=True)
            succeeded += 1
        except Exception as e:
            failed += 1
            logger.warning('build_original.py failed for %s: %s', page.name, e)
    return {'total': total, 'executed': executed, 'succeeded': succeeded, 'failed': failed}


def build_and_validate(out_path: Path, strict: bool = False, logger: Optional[logging.Logger] = None):
    logger = logger or _get_logger(None)
    if not TEMPLATE_PPT.exists():
        raise FileNotFoundError(TEMPLATE_PPT)
    if not UNZIP_ROOT.exists():
        raise FileNotFoundError(UNZIP_ROOT)
    logger.info(f'Template PPT: {TEMPLATE_PPT}')
    logger.info(f'Unzip root: {UNZIP_ROOT}')
    targets = _collect_rebuild_targets()
    if not targets:
        logger.info('No charts with original_* found. Copying template only.')
        out_path.parent.mkdir(parents=True, exist_ok=True)
        # 直接复制模板
        with TEMPLATE_PPT.open('rb') as fsrc, out_path.open('wb') as fdst:
            fdst.write(fsrc.read())
        return
    # 生成每个 chart 的 XML
    chart_bytes_map: Dict[str, bytes] = {}
    for cn, data in targets.items():
        b = _build_chart_xml_bytes(cn, data)
        if b is not None:
            chart_bytes_map[cn] = b
    logger.info(f'Prepared {len(chart_bytes_map)} charts for replacement')
    # 合成新 PPT
    _compose_ppt_from_template(TEMPLATE_PPT, out_path, chart_bytes_map)
    logger.info(f'Generated PPT: {out_path} (md5={_md5(out_path)})')
    # 校验：解析并比对新旧图表数据
    summary = _validate_against_original(out_path, TEMPLATE_PPT, list(chart_bytes_map.keys()))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    logger.info(f'Wrote JSON report: {REPORT_JSON}')
    # 生成 MD 摘要
    md_lines = [
        f'# 原始版重建校验报告',
        f'- 模板 md5: {_md5(TEMPLATE_PPT)}',
        f'- 新稿 md5: {_md5(out_path)}',
        f'- 参与校验图表数: {summary["total"]}',
        f'- 完全一致: {summary["matched"]}',
        f'- 不一致: {summary["mismatched"]}',
    ]
    if summary['mismatched']:
        md_lines.append('\n## 差异详单（截断）')
        for d in summary['charts'][:30]:
            if not d.get('ok'):
                md_lines.append(f'- {d["chart"]}: type={d.get("type")} 不一致')
    REPORT_MD.write_text('\n'.join(md_lines), encoding='utf-8')
    logger.info('Validation summary: ' + json.dumps({k: summary[k] for k in ['total','matched','mismatched']}, ensure_ascii=False))
    if strict and summary['mismatched'] > 0:
        raise SystemExit(2)


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser(description='使用 original_* 重建原始版 PPT，并校验与模板一致性；按需可运行逐页构建')
    ap.add_argument('--out', type=Path, default=OUT_PATH, help='输出 PPTX 路径')
    # 默认开启严格模式，发现不一致时退出码为 2；可用 --no-strict 关闭
    ap.add_argument('--strict', dest='strict', action='store_true', default=True, help='若存在不一致则退出码为 2（默认开启）')
    ap.add_argument('--no-strict', dest='strict', action='store_false', help='关闭严格模式（存在不一致时不改变退出码）')
    ap.add_argument('--pages', nargs='*', default=None, help='仅运行指定页面（如 p10 p12）；与 --build-pages 搭配使用或单独提供也会触发逐页构建')
    # 默认不跑逐页构建；仅在明确指定时才执行
    ap.add_argument('--build-pages', action='store_true', help='启用逐页 build_original.py 执行（默认跳过）')
    default_log = ROOT / 'logs' / 'build_all_original.log'
    ap.add_argument('--log-file', type=Path, default=default_log, help='日志输出文件路径')
    ap.add_argument('--log-level', default='INFO', choices=['DEBUG','INFO','WARNING','ERROR','CRITICAL'], help='日志级别')
    args = ap.parse_args()
    logger = _get_logger(args.log_file, getattr(logging, args.log_level.upper(), logging.INFO))
    logger.info('Starting build_all_original with logging to %s', args.log_file)
    # 触发逐页构建的条件：显式 --build-pages 或提供了 --pages（表示希望跑指定页面）
    should_build_pages = bool(args.build_pages or (args.pages and len(args.pages) > 0))
    if should_build_pages:
        stats = run_page_build_originals(args.pages, logger=logger)
        logger.info('Per-page build_original summary: total=%d executed=%d succeeded=%d failed=%d',
                    stats['total'], stats['executed'], stats['succeeded'], stats['failed'])
    build_and_validate(args.out, strict=args.strict, logger=logger)