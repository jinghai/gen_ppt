#!/usr/bin/env python3
import json
from pathlib import Path
import sys

# 依赖通用填充函数：兼容 charts/p10 与 charts/charts/p10
TOOL_CANDIDATES = [
    Path(__file__).resolve().parents[3] / 'tools',  # charts/tools
    Path(__file__).resolve().parents[2] / 'tools',  # charts/charts/tools (不存在则跳过)
]
for tc in TOOL_CANDIDATES:
    if tc.exists():
        sys.path.append(str(tc))
from fill_chart_xml import fill_chart  # type: ignore

ROOT = Path(__file__).resolve().parents[0]



def load_final_json(fp: Path):
    """读取 JSON：支持 {labels:[...], series:[{values:[...]}, ...]} 或简写 list[list] """
    try:
        data = json.loads(fp.read_text(encoding='utf-8'))
    except Exception:
        return [], []
    labels = []
    series = []
    if isinstance(data, dict):
        labels = data.get('labels') or []
        sr = data.get('series') or []
        if sr:
            if isinstance(sr[0], dict):
                series = [s.get('values', []) for s in sr]
            elif isinstance(sr[0], (int, float)):
                series = [sr]
            else:
                series = sr
    elif isinstance(data, list):
        # 简写：仅系列
        if data and isinstance(data[0], (int, float)):
            series = [data]
        else:
            series = data
    return labels, series


def main():
    chart_path = Path((ROOT / 'chart_path.txt').read_text(encoding='utf-8').strip())
    # 仅支持 JSON：final_data.json > data.json
    final_json = ROOT / 'final_data.json'
    data_json = ROOT / 'data.json'
    if final_json.exists():
        labels, series = load_final_json(final_json)
        src_desc = final_json
    elif data_json.exists():
        labels, series = load_final_json(data_json)
        src_desc = data_json
    else:
        raise FileNotFoundError('缺少数据：final_data.json 或 data.json')

    fill_chart(chart_path, series, labels)
    print('filled chart8 from', src_desc)

if __name__ == '__main__':
    main()