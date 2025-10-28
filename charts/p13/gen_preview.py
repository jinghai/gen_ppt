#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1] / 'tools'
sys.path.append(str(TOOLS))
from gen_preview_chart import generate_preview  # type: ignore

PAGE = Path(__file__).resolve().parent


def main():
    charts = [c for c in PAGE.iterdir() if c.is_dir() and re.match(r'^chart\d+$', c.name)]
    ok = 0
    for c in charts:
        if generate_preview(c):
            ok += 1
    print(f'[done] previews generated: {ok}/{len(charts)} in {PAGE}')


if __name__ == '__main__':
    main()
