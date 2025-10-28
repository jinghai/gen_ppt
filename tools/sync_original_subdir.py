#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将 chart 根目录下的 original_* 同步到 original/ 子目录（仅在子目录缺失时复制），
以兼容工具脚本读取 original/ 路径。
支持指定页面列表（p8 p10 ...）。
"""
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAGES_DIR = ROOT / 'charts' / 'charts'

FILES = ['original_meta.json','original_labels.json','original_series.json','original_scatter.json']


def sync_page(page_dir: Path) -> int:
    count = 0
    charts = sorted([c for c in page_dir.iterdir() if c.is_dir() and re.match(r'^chart\d+$', c.name)])
    for chart in charts:
        subdir = chart / 'original'
        subdir.mkdir(exist_ok=True)
        for fn in FILES:
            src = chart / fn
            dst = subdir / fn
            if src.exists() and not dst.exists():
                dst.write_bytes(src.read_bytes())
                count += 1
    return count


def main():
    ap = argparse.ArgumentParser(description='Sync root original_* into original/ subdir when missing')
    ap.add_argument('--pages', nargs='*', default=None, help='pages like p8 p10 ...; default all p*')
    args = ap.parse_args()
    if args.pages:
        pages = [PAGES_DIR / p for p in args.pages]
    else:
        import re as _re
        pages = [p for p in PAGES_DIR.iterdir() if p.is_dir() and _re.match(r'^p\d+$', p.name)]
    total = 0
    for p in pages:
        total += sync_page(p)
    print('Synced files:', total)


if __name__ == '__main__':
    main()