#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
校验并自动修复 charts/charts/p*/chart*/ 下的 original_* 原始缓存数据：
- 读取每个 chart 的 chart_path.txt 指向的原始 chart*.xml；
- 解析 XML（复用 extract_chart_cache.parse_chart_xml）得到真实 labels/series 或 scatter_series；
- 和现有 original_* 进行逐项对比（含浮点容差），若不一致则重写 original_* 文件；
- 再次校验，确保通过；
- 输出 JSON/Markdown 报告；

用法：
  python charts/tools/validate_and_fix_original.py [--pages p14 p16 ...] [--dry-run] [--strict]
"""
import argparse
import json
import sys
import zipfile
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[2]
TOOLS_DIR = ROOT / 'ppt' / 'tools'
PAGES_DIR = ROOT / 'ppt' / 'charts'
OUTPUT_DIR = ROOT / 'ppt' / 'output'
REPORT_JSON = OUTPUT_DIR / 'original_fix_validate.json'
REPORT_MD = OUTPUT_DIR / 'original_fix_validate.md'
TEMPLATE_PPT = ROOT / 'ppt' / 'input' / 'LRTBH.pptx'

sys.path.append(str(TOOLS_DIR))
from extract_chart_cache import parse_chart_xml  # type: ignore


def _eq(a: Any, b: Any, tol: float = 1e-9) -> bool:
    """与 ensure_page_scripts.py 保持一致：数值允许极小误差，其余严格等值"""
    try:
        af = float(a)
        bf = float(b)
        return abs(af - bf) <= tol
    except Exception:
        return a == b


def _read_chart_xml_path(chart_dir: Path) -> Tuple[Path, str]:
    p = chart_dir / 'chart_path.txt'
    if not p.exists():
        raise FileNotFoundError(f"missing chart_path.txt in {chart_dir}")
    raw = p.read_text(encoding='utf-8').strip()
    xml_path = Path(raw)
    chart_name = xml_path.name  # e.g. chart10.xml
    return xml_path, chart_name


def _original_file(chart_dir: Path, name: str) -> Path:
    sub = chart_dir / 'original' / name
    if sub.exists():
        return sub
    return chart_dir / name


def _read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return None


def _compare(parsed: Dict[str, Any], chart_dir: Path) -> Tuple[bool, List[str]]:
    errs: List[str] = []
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
                continue
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


def _rewrite_original(chart_dir: Path, chart_name: str, parsed: Dict[str, Any]) -> List[str]:
    """无条件重写 original_*（根目录与 original/ 子目录都写入）。"""
    written: List[str] = []
    # root paths
    root_meta = chart_dir / 'original_meta.json'
    root_scatter = chart_dir / 'original_scatter.json'
    root_labels = chart_dir / 'original_labels.json'
    root_series = chart_dir / 'original_series.json'
    # subdir paths
    subdir = chart_dir / 'original'
    subdir.mkdir(exist_ok=True)
    sub_meta = subdir / 'original_meta.json'
    sub_scatter = subdir / 'original_scatter.json'
    sub_labels = subdir / 'original_labels.json'
    sub_series = subdir / 'original_series.json'

    meta = {'chart': chart_name, **parsed}
    txt_meta = json.dumps(meta, ensure_ascii=False, indent=2)
    root_meta.write_text(txt_meta, encoding='utf-8'); written.append(str(root_meta))
    sub_meta.write_text(txt_meta, encoding='utf-8'); written.append(str(sub_meta))

    if parsed.get('chart_type') == 'scatterChart':
        scatter = parsed.get('scatter_series', [])
        txt_sc = json.dumps(scatter, ensure_ascii=False, indent=2)
        root_scatter.write_text(txt_sc, encoding='utf-8'); written.append(str(root_scatter))
        sub_scatter.write_text(txt_sc, encoding='utf-8'); written.append(str(sub_scatter))
        # 清理类别文件以防误用
        if root_labels.exists(): root_labels.unlink()
        if root_series.exists(): root_series.unlink()
        if sub_labels.exists(): sub_labels.unlink()
        if sub_series.exists(): sub_series.unlink()
    else:
        labels = parsed.get('labels', [])
        series = parsed.get('series', [])
        txt_lbl = json.dumps(labels, ensure_ascii=False, indent=2)
        txt_ser = json.dumps(series, ensure_ascii=False, indent=2)
        root_labels.write_text(txt_lbl, encoding='utf-8'); written.append(str(root_labels))
        root_series.write_text(txt_ser, encoding='utf-8'); written.append(str(root_series))
        sub_labels.write_text(txt_lbl, encoding='utf-8'); written.append(str(sub_labels))
        sub_series.write_text(txt_ser, encoding='utf-8'); written.append(str(sub_series))
        # 清理散点文件以防误用
        if root_scatter.exists(): root_scatter.unlink()
        if sub_scatter.exists(): sub_scatter.unlink()
    return written


def validate_and_fix_chart(chart_dir: Path, dry_run: bool = False) -> Dict[str, Any]:
    res: Dict[str, Any] = {
        'chart_dir': str(chart_dir),
        'chart': chart_dir.name,
        'page': chart_dir.parent.name,
        'chart_name': None,
        'ok_before': False,
        'fixed': False,
        'ok_after': False,
        'errors_before': [],
        'errors_after': [],
        'written': [],
    }
    _, chart_name = _read_chart_xml_path(chart_dir)
    # 从模板 PPTX 的 zip 中读取真实 XML，避免使用可能过期的 UNZIP 版本
    with zipfile.ZipFile(TEMPLATE_PPT, 'r') as z:
        try:
            xml_bytes = z.read(f'ppt/charts/{chart_name}')
        except KeyError:
            raise FileNotFoundError(f'Chart not found in template: {chart_name}')
    parsed = parse_chart_xml(xml_bytes)
    res['chart_name'] = chart_name
    ok_before, errs_before = _compare(parsed, chart_dir)
    res['ok_before'] = ok_before
    res['errors_before'] = errs_before
    if not ok_before and not dry_run:
        res['written'] = _rewrite_original(chart_dir, chart_name, parsed)
        res['fixed'] = True
        # re-compare
        ok_after, errs_after = _compare(parsed, chart_dir)
        res['ok_after'] = ok_after
        res['errors_after'] = errs_after
    else:
        res['ok_after'] = ok_before
        res['errors_after'] = errs_before
    return res


def iter_charts(pages: List[str] = None) -> List[Path]:
    charts: List[Path] = []
    if pages:
        page_dirs = [PAGES_DIR / p for p in pages]
    else:
        page_dirs = [d for d in PAGES_DIR.iterdir() if d.is_dir() and d.name.startswith('p')]
    for page in sorted(page_dirs, key=lambda x: x.name):
        for child in sorted(page.iterdir(), key=lambda x: x.name):
            if child.is_dir() and child.name.startswith('chart'):
                charts.append(child)
    return charts


def main():
    ap = argparse.ArgumentParser(description='校验并自动修复 original_*，确保与原始模板 chart*.xml 一致')
    ap.add_argument('--pages', nargs='*', default=None, help='指定页面目录（如 p14 p16 ...），不指定则处理全部 p*')
    ap.add_argument('--dry-run', action='store_true', help='仅校验，不写入修复')
    ap.add_argument('--strict', action='store_true', help='若修复后仍存在不一致则退出码为 2')
    ap.add_argument('--out-json', type=Path, default=REPORT_JSON, help='校验/修复报告 JSON 输出路径')
    ap.add_argument('--out-md', type=Path, default=REPORT_MD, help='校验/修复报告 Markdown 输出路径')
    args = ap.parse_args()

    charts = iter_charts(args.pages)
    summary: List[Dict[str, Any]] = []
    ok_total = 0
    fixed_total = 0
    fail_total = 0
    for c in charts:
        try:
            r = validate_and_fix_chart(c, dry_run=args.dry_run)
            summary.append(r)
            if r['ok_after']:
                ok_total += 1
                if r['fixed']:
                    fixed_total += 1
            else:
                fail_total += 1
        except Exception as e:
            summary.append({'chart_dir': str(c), 'chart': c.name, 'page': c.parent.name, 'error': str(e)})
            fail_total += 1

    # 写报告 JSON
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    report = {
        'total': len(charts),
        'ok': ok_total,
        'fixed': fixed_total,
        'fail': fail_total,
        'items': summary,
    }
    args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')

    # 写报告 MD
    lines = [
        '# original_* 校验与自动修复报告',
        f'- 总图表: {len(charts)}',
        f'- 修复后通过: {ok_total}',
        f'- 其中修复成功: {fixed_total}',
        f'- 修复后仍失败: {fail_total}',
        '',
        '## 明细',
    ]
    for r in summary:
        if 'error' in r:
            lines.append(f"- {r['page']}/{r['chart']}: ERROR {r['error']}")
            continue
        status = 'OK' if r['ok_after'] else ('FIXED' if r['fixed'] else 'MISMATCH')
        before = '; '.join(r['errors_before']) if r['errors_before'] else 'None'
        after = '; '.join(r['errors_after']) if r['errors_after'] else 'None'
        lines.append(f"- {r['page']}/{r['chart']} ({r['chart_name']}): {status}; before=[{before}] after=[{after}]")
    args.out_md.write_text('\n'.join(lines), encoding='utf-8')

    print(f"[done] 校验/修复完成：OK={ok_total} FIXED={fixed_total} FAIL={fail_total} -> {args.out_json}")
    if args.strict and fail_total > 0:
        sys.exit(2)


if __name__ == '__main__':
    main()