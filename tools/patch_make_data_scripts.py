#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量修正 charts/charts/*/make_data.py 中的两个问题：
1) 错误的 chart_name 构造（使用 "chartX.xml" 而非 "X.xml"）
2) metrics_db 路径为相对路径时未按仓库根解析

用法：直接运行，无需参数。
"""
from __future__ import annotations
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PAGES_ROOT = REPO / 'charts' / 'charts'

FIXES = [
    (
        # 修复 chart_name 构造
        "chart_name = chart_dir.name.replace('chart','') + '.xml'",
        "chart_name = chart_dir.name + '.xml'",
    ),
    (
        # 修复 metrics_db 路径解析（保持兼容现有变量与逻辑）
        "output_db = Path(((base_cfg.get('data_sources') or {}).get('metrics_db') or METRICS_DB_DEFAULT))",
        (
            "raw_db = ((base_cfg.get('data_sources') or {}).get('metrics_db') or METRICS_DB_DEFAULT)\n"
            "    output_db = (raw_db if isinstance(raw_db, Path) else Path(raw_db))\n"
            "    if not output_db.is_absolute():\n"
            "        output_db = (REPO_ROOT / output_db)\n"
        ),
    ),
]


def patch_file(fp: Path) -> bool:
    txt = fp.read_text(encoding='utf-8')
    changed = False
    for old, new in FIXES:
        if old in txt and new not in txt:
            txt = txt.replace(old, new)
            changed = True
    if changed:
        fp.write_text(txt, encoding='utf-8')
    return changed


def main():
    if not PAGES_ROOT.exists():
        raise FileNotFoundError(PAGES_ROOT)
    changed_files = []
    for page in sorted([p for p in PAGES_ROOT.iterdir() if p.is_dir() and p.name.startswith('p')]):
        fp = page / 'make_data.py'
        if fp.exists():
            if patch_file(fp):
                changed_files.append(fp)
    print('Patched make_data.py files:', len(changed_files))
    for f in changed_files[:10]:
        print('-', f)


if __name__ == '__main__':
    main()