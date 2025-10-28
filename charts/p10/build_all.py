#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
import subprocess

# 统一运行本页的两种构建：修改版（build.py）与原始版（build_original.py）
ROOT = Path(__file__).resolve().parent


# 新增：先生成真实数据 JSON
def run_make_data():
    sys.path.insert(0, str(ROOT))
    import make_data as make_data_mod  # type: ignore
    try:
        rc = make_data_mod.main()
        print('make_data.py finished with code', rc)
    except Exception as e:
        print('make_data.py failed:', e)


# 新增：填充 chart8/chart9 的 XML
def run_fillers():
    try:
        subprocess.run([sys.executable, str(ROOT / 'chart8' / 'fill.py')], check=True)
        subprocess.run([sys.executable, str(ROOT / 'chart9' / 'fill.py')], check=True)
    except Exception as e:
        print('fillers failed:', e)


def run_modified():
    sys.path.insert(0, str(ROOT))
    import build as build_mod  # type: ignore
    build_mod.build()


def run_original():
    sys.path.insert(0, str(ROOT))
    import build_original as build_org  # type: ignore
    build_org.build()


# 新增：生成原始数据预览图片
def run_preview():
    sys.path.insert(0, str(ROOT))
    import gen_preview as preview_mod  # type: ignore
    try:
        preview_mod.main()
    except Exception as e:
        print('gen_preview.py failed:', e)


def main():
    ap = argparse.ArgumentParser(description='p10 build_all: run data generation, builds and preview')
    ap.add_argument('--mode', choices=['modified','original','both'], default='both', help='which build(s) to run')
    args = ap.parse_args()

    # 先生成数据 JSON（data/final）
    run_make_data()

    # 生成填充：更新 chart8/chart9 的 XML
    run_fillers()

    if args.mode in ('modified','both'):
        run_modified()
    if args.mode in ('original','both'):
        run_original()

    # 生成预览图片（使用 original_*）
    run_preview()

    print('p10 build_all done, mode =', args.mode)


if __name__ == '__main__':
    main()