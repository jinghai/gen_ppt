#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
遍历 charts/charts 下所有页面的 chart* 目录，
根据 original_* 缓存批量生成 preview_original.png 预览图。
"""
from __future__ import annotations
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
PAGES_ROOT = ROOT / 'charts' / 'charts'

sys.path.append(str(ROOT / 'charts' / 'tools'))
from gen_preview_chart import generate_preview  # type: ignore


def iter_chart_dirs():
    for page in sorted([p for p in PAGES_ROOT.iterdir() if p.is_dir() and p.name.startswith('p')]):
        for chart in sorted([c for c in page.iterdir() if c.is_dir() and c.name.startswith('chart')]):
            yield chart


def main():
    total = 0
    ok = 0
    skipped = 0
    for chart_dir in iter_chart_dirs():
        total += 1
        # 已存在则跳过
        if (chart_dir / 'preview_original.png').exists():
            skipped += 1
            continue
        try:
            if generate_preview(chart_dir):
                ok += 1
        except Exception as e:
            print('preview failed:', chart_dir, e)
    print(f"Preview summary: total={total}, generated={ok}, skipped_existing={skipped}")


if __name__ == '__main__':
    main()