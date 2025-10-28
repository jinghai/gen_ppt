#!/usr/bin/env python3
import json
import sys
import argparse
from pathlib import Path
from typing import Dict, Any, List, Tuple

# 允许直接导入同目录下的解析工具
THIS_FILE = Path(__file__).resolve()
TOOLS_DIR = THIS_FILE.parent
CHARTS_DIR = TOOLS_DIR.parent / 'charts'

sys.path.append(str(TOOLS_DIR))
from extract_chart_cache import parse_chart_xml  # noqa: E402


def read_chart_xml_path(chart_dir: Path) -> Tuple[Path, str]:
    p = chart_dir / 'chart_path.txt'
    if not p.exists():
        raise FileNotFoundError(f"missing chart_path.txt in {chart_dir}")
    raw = p.read_text(encoding='utf-8').strip()
    xml_path = Path(raw)
    if not xml_path.exists():
        raise FileNotFoundError(f"chart xml not found: {xml_path}")
    chart_name = xml_path.name  # e.g. chart10.xml
    return xml_path, chart_name


def has_existing_original(chart_dir: Path) -> bool:
    direct = any((chart_dir / f).exists() for f in (
        'original_meta.json', 'original_labels.json', 'original_series.json', 'original_scatter.json'
    ))
    if direct:
        return True
    sub = chart_dir / 'original'
    if sub.exists() and sub.is_dir():
        if any((sub / f).exists() for f in (
            'original_meta.json', 'original_labels.json', 'original_series.json', 'original_scatter.json'
        )):
            return True
    return False


def write_original(chart_dir: Path, chart_name: str, parsed: Dict[str, Any]) -> List[str]:
    written: List[str] = []
    # 统一写在 chart 目录根部
    meta_path = chart_dir / 'original_meta.json'
    scatter_path = chart_dir / 'original_scatter.json'
    labels_path = chart_dir / 'original_labels.json'
    series_path = chart_dir / 'original_series.json'

    meta = {'chart': chart_name, **parsed}
    if not meta_path.exists():
        meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
        written.append(str(meta_path))

    if parsed.get('chart_type') == 'scatterChart':
        scatter = parsed.get('scatter_series', [])
        if not scatter_path.exists():
            scatter_path.write_text(json.dumps(scatter, ensure_ascii=False, indent=2), encoding='utf-8')
            written.append(str(scatter_path))
    else:
        labels = parsed.get('labels', [])
        series = parsed.get('series', [])
        if not labels_path.exists():
            labels_path.write_text(json.dumps(labels, ensure_ascii=False, indent=2), encoding='utf-8')
            written.append(str(labels_path))
        if not series_path.exists():
            series_path.write_text(json.dumps(series, ensure_ascii=False, indent=2), encoding='utf-8')
            written.append(str(series_path))

    return written


def process_page(page_dir: Path) -> Dict[str, Any]:
    res = {
        'page': page_dir.name,
        'charts_processed': 0,
        'charts_skipped_existing': 0,
        'charts_failed': 0,
        'files_written': [],
        'errors': [],
    }
    if not page_dir.exists():
        res['errors'].append(f"page not found: {page_dir}")
        return res
    # 遍历该页面的 chart* 子目录
    for child in sorted(page_dir.iterdir()):
        if not child.is_dir():
            continue
        if not child.name.startswith('chart'):
            continue
        try:
            if has_existing_original(child):
                res['charts_skipped_existing'] += 1
                continue
            xml_path, chart_name = read_chart_xml_path(child)
            xml_bytes = xml_path.read_bytes()
            parsed = parse_chart_xml(xml_bytes)
            written = write_original(child, chart_name, parsed)
            res['charts_processed'] += 1
            res['files_written'].extend(written)
        except Exception as e:
            res['charts_failed'] += 1
            res['errors'].append(f"{child.name}: {e}")
    return res


def main():
    parser = argparse.ArgumentParser(description='生成缺失的 original_* 原始缓存文件（基于 chart XML）')
    parser.add_argument('--pages', nargs='*', default=None, help='指定页面目录名（如 p14 p16 ...），未指定则处理全部 p*')
    parser.add_argument('--out-json', type=str, default=None, help='可选：将摘要写入指定 JSON 文件路径')
    args = parser.parse_args()

    pages_root = CHARTS_DIR
    if args.pages:
        page_dirs = [pages_root / p for p in args.pages]
    else:
        page_dirs = [d for d in pages_root.iterdir() if d.is_dir() and d.name.startswith('p')]

    summary = []
    for page_dir in page_dirs:
        res = process_page(page_dir)
        summary.append(res)

    if args.out_json:
        out_path = Path(args.out_json)
        if not out_path.parent.exists():
            out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f"Summary written -> {out_path}")
    else:
        print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()