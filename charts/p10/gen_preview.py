#!/usr/bin/env python3
import json
import sys
from pathlib import Path
import matplotlib.pyplot as plt

P10 = Path(__file__).resolve().parents[0]


def _category_from_original(chart_dir: Path):
    out = {'labels': [], 'series': []}
    ol = chart_dir / 'original_labels.json'
    os = chart_dir / 'original_series.json'
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
    orig_scatter = chart_dir / 'original_scatter.json'
    if not orig_scatter.exists():
        return []
    try:
        data = json.loads(orig_scatter.read_text(encoding='utf-8'))
        out = []
        for s in data:
            name = s.get('name')
            x = s.get('x') or [p[0] for p in s.get('points', [])]
            y = s.get('y') or [p[1] for p in s.get('points', [])]
            out.append({'name': name, 'x': x, 'y': y, 'points': [[x[i] if i < len(x) else None, y[i] if i < len(y) else None] for i in range(max(len(x or []), len(y or [])))]})
        return out
    except Exception:
        return []


def generate_chart8_preview(chart_dir: Path):
    data = _category_from_original(chart_dir)
    labels = data.get('labels')
    series = data.get('series')
    if not series:
        return
    sizes = series[0]['values']
    if not labels or len(labels) != len(sizes):
        labels = [f'Slice {i+1}' for i in range(len(sizes))]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    plt.title(f'{chart_dir.name} Original Data Preview')
    plt.savefig(chart_dir / 'preview_original.png', dpi=100)
    plt.close(fig)


def generate_chart9_preview(chart_dir: Path):
    data = _scatter_from_original(chart_dir)
    if not data:
        return
    fig, ax = plt.subplots()
    for i, s in enumerate(data):
        ax.plot(s.get('x', []), s.get('y', []), marker='o', linestyle='-', label=s.get('name') or f'Series {i}')
    ax.grid(True)
    plt.title(f'{chart_dir.name} Original Data Preview')
    plt.xlabel('X-Value')
    plt.ylabel('Y-Value')
    if any(s.get('name') for s in data):
        plt.legend()
    plt.savefig(chart_dir / 'preview_original.png', dpi=120)
    plt.close(fig)


def main():
    c8_dir = P10 / 'chart8'
    generate_chart8_preview(c8_dir)
    print(f'Generated preview for chart8 at {c8_dir / "preview_original.png"}')

    c9_dir = P10 / 'chart9'
    generate_chart9_preview(c9_dir)
    print(f'Generated preview for chart9 at {c9_dir / "preview_original.png"}')


if __name__ == '__main__':
    main()