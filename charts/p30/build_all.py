#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
import subprocess
import re

ROOT = Path(__file__).resolve().parent


def run_make_data():
    sys.path.append(str(ROOT))
    import make_data as make_data_mod  # type: ignore
    try:
        rc = make_data_mod.main()
        print('make_data.py finished with code', rc)
    except Exception as e:
        print('make_data.py failed:', e)


def run_fillers():
    for chart_dir in sorted([p for p in ROOT.iterdir() if p.is_dir() and re.match(r'^chart\d+$', p.name)]):
        try:
            subprocess.run([sys.executable, str(chart_dir / 'fill.py')], check=True)
        except Exception as e:
            print('filler failed for', chart_dir, e)


def main():
    ap = argparse.ArgumentParser(description='page build_all: run data generation and fill charts')
    ap.add_argument('--mode', choices=['modified','original','both'], default='both')
    args = ap.parse_args()
    run_make_data()
    run_fillers()
    print(ROOT.name, 'build_all done, mode =', args.mode)

if __name__ == '__main__':
    main()
