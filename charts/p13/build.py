#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
P13 一键构建脚本
- 执行 generate_excel.py 生成 PieData/LineData 到页面 output；
- 执行 fill_from_excel.py 解压模板、嵌入工作簿、更新图表并打包输出；
- 保持页面级 tmp 目录，不改动模板文件。
"""

import subprocess
import sys
from pathlib import Path


def main():
    page_dir = Path(__file__).resolve().parent
    gen = page_dir / 'generate_excel.py'
    fill = page_dir / 'fill_from_excel.py'

    if not gen.exists():
        print('[p13] 缺少 generate_excel.py')
        sys.exit(1)
    if not fill.exists():
        print('[p13] 缺少 fill_from_excel.py')
        sys.exit(1)

    print('[p13] 生成 Excel 数据...')
    subprocess.run([sys.executable, str(gen)], check=True, cwd=str(page_dir))

    print('[p13] 填充模板并打包...')
    subprocess.run([sys.executable, str(fill)], check=True, cwd=str(page_dir))

    print('[p13] 构建完成。')


if __name__ == '__main__':
    main()
