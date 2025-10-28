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
    """读取 JSON：支持 list[ {name,x,y,points} ] 或 {scatter_series: [...]} """
    try:
        data = json.loads(fp.read_text(encoding='utf-8'))
    except Exception:
        return []
    series = []
    if isinstance(data, dict) and 'scatter_series' in data:
        arr = data.get('scatter_series') or []
        for s in arr:
            y = s.get('y') or [p[1] for p in (s.get('points') or [])]
            series.append(y)
    elif isinstance(data, list):
        for s in data:
            if isinstance(s, dict):
                y = s.get('y') or [p[1] for p in (s.get('points') or [])]
                series.append(y)
            elif isinstance(s, (int, float)):
                # 单系列简写：list[float]
                series = [data]
                break
    return series




def main():
    chart_path = Path((ROOT / 'chart_path.txt').read_text(encoding='utf-8').strip())
    # 仅支持 JSON：final_data.json > data.json
    final_json = ROOT / 'final_data.json'
    data_json = ROOT / 'data.json'
    if final_json.exists():
        series = load_final_json(final_json)
        src_desc = final_json
    elif data_json.exists():
        series = load_final_json(data_json)
        src_desc = data_json
    else:
        raise FileNotFoundError('缺少数据：final_data.json 或 data.json')
    labels = None  # 散点不使用 labels
    fill_chart(chart_path, series, labels)
    print('filled chart9 from', src_desc)

if __name__ == '__main__':
    main()