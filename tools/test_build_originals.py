#!/usr/bin/env python3
"""
批量验证所有页面的 build_original.py：
- 自动发现 `charts/p*/build_original.py`
- 逐个以子进程运行，收集 stdout/stderr 与退出码
- 将完整日志汇总到项目根 `logs/build_original_tests.log`

使用说明：
  python3 tmp/test_build_originals.py

备注：遵循规则，不在工程内随意生成调试文件，此测试脚本放置于项目根的 tmp 目录。
"""

from __future__ import annotations

import sys
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CHARTS_DIR = ROOT / 'charts'
GLOBAL_LOG_DIR = ROOT / 'logs'
GLOBAL_LOG_FILE = GLOBAL_LOG_DIR / 'build_original_tests.log'


def log_global(msg: str) -> None:
    GLOBAL_LOG_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f'[{ts}] [test] {msg}'
    print(line)
    with GLOBAL_LOG_FILE.open('a', encoding='utf-8') as f:
        f.write(line + '\n')


def discover_pages() -> list[Path]:
    pages: list[Path] = []
    for d in sorted(CHARTS_DIR.iterdir()):
        if d.is_dir() and d.name.startswith('p') and (d / 'build_original.py').exists():
            pages.append(d)
    return pages


def run_page(page_dir: Path) -> bool:
    slide_no = page_dir.name[1:]
    log_global(f'Run build_original for p{slide_no}')
    cmd = [sys.executable, str(page_dir / 'build_original.py')]
    proc = subprocess.run(
        cmd,
        cwd=str(page_dir),
        text=True,
        capture_output=True,
    )
    if proc.stdout:
        log_global(f'[p{slide_no}] stdout:\n{proc.stdout.rstrip()}')
    if proc.stderr:
        log_global(f'[p{slide_no}] stderr:\n{proc.stderr.rstrip()}')
    log_global(f'[p{slide_no}] exit_code={proc.returncode}')
    return proc.returncode == 0


def main() -> None:
    GLOBAL_LOG_FILE.unlink(missing_ok=True)
    pages = discover_pages()
    if not pages:
        log_global('No pages with build_original.py found.')
        sys.exit(1)

    total = len(pages)
    ok = 0
    for d in pages:
        ok += 1 if run_page(d) else 0

    log_global(f'Summary: {ok}/{total} succeeded')
    if ok != total:
        sys.exit(2)


if __name__ == '__main__':
    main()