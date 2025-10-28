#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import json
from pathlib import Path
import matplotlib.pyplot as plt


def _category_from_original(chart_dir: Path):
    out = {'labels': [], 'series': []}
    ol = chart_dir / 'original' / 'original_labels.json'
    os = chart_dir / 'original' / 'original_series.json'
    if not (ol.exists() and os.exists()):
        return out
    try:
        labels = json.loads(ol.read_text(encoding='utf-8'))
        series_raw = json.loads(os.read_text(encoding='utf-8'))
        series = []
        if series_raw:
            if isinstance(series_raw[0], dict):
                series = [{'name': s.get('name'), 'values': s.get('values', [])} for s in series_raw]
            elif isinstance(series_raw[0], (int, float)):
                series = [{'name': None, 'values': series_raw}]
            else:
                series = [{'name': None, 'values': s} for s in series_raw]
        return {'labels': labels or [], 'series': series}
    except Exception:
        return out


def _scatter_from_original(chart_dir: Path):
    orig_scatter = chart_dir / 'original' / 'original_scatter.json'
    if not orig_scatter.exists():
        return []
    try:
        data = json.loads(orig_scatter.read_text(encoding='utf-8'))
        out = []
        for s in data:
            name = s.get('name')
            x = s.get('x') or [p[0] for p in s.get('points', [])]
            y = s.get('y') or [p[1] for p in s.get('points', [])]
            out.append({'name': name, 'x': x, 'y': y})
        return out
    except Exception:
        return []


def generate_preview(chart_dir: Path):
    # 优先散点/线图预览
    scat = _scatter_from_original(chart_dir)
    if scat:
        fig, ax = plt.subplots()
        for i, s in enumerate(scat):
            ax.plot(s.get('x', []), s.get('y', []), marker='o', linestyle='-', label=s.get('name') or f'Series {i}')
        ax.grid(True)
        plt.title(f'{chart_dir.name} Original Preview')
        plt.xlabel('X')
        plt.ylabel('Y')
        if any(s.get('name') for s in scat):
            plt.legend()
        plt.savefig(chart_dir / 'preview_original.png', dpi=120)
        plt.close(fig)
        return True

    # 类别图（饼图/柱状等）
    cat = _category_from_original(chart_dir)
    labels = cat.get('labels')
    series = cat.get('series')
    if series:
        sizes = series[0]['values']
        if not labels or len(labels) != len(sizes):
            labels = [f'Slice {i+1}' for i in range(len(sizes))]
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        plt.title(f'{chart_dir.name} Original Preview')
        plt.savefig(chart_dir / 'preview_original.png', dpi=100)
        plt.close(fig)
        return True
    return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate preview image from original_* cache files')
    parser.add_argument('--chart_dir', required=True, help='Path to chart directory, e.g., charts/charts/p13/chart10')
    args = parser.parse_args()
    chart_dir = Path(args.chart_dir)
    ok = generate_preview(chart_dir)
    if ok:
        print('Preview generated:', chart_dir / 'preview_original.png')
    else:
        print('No original_* data found for preview in', chart_dir)