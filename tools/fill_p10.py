#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path
import yaml

REPO = Path(__file__).resolve().parents[1]
P10 = REPO / 'charts' / 'p10'

def _resolve_unz_root() -> Path:
    try:
        cfg = yaml.safe_load((REPO / 'config.yaml').read_text(encoding='utf-8')) or {}
    except Exception:
        cfg = {}
    tr = (cfg.get('project') or {}).get('template_root', 'input/LRTBH-unzip')
    p = Path(tr)
    if not p.is_absolute():
        p = REPO / tr
    return p

def _charts_dir(unz: Path) -> Path:
    d = unz / 'ppt' / 'charts'
    return d if d.exists() else unz / 'charts'

CHARTS_DIR = _charts_dir(_resolve_unz_root())

CHARTS = [
    ('chart8','chart8.xml'),
    ('chart9','chart9.xml'),
]

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=str(REPO))
    if r.returncode != 0:
        raise RuntimeError(r.stderr)
    return r.stdout


def main():
    for name, chart_xml in CHARTS:
        d = P10 / name
        labels = d / 'labels.json'
        series = d / 'series.json'
        chart_path = CHARTS_DIR / chart_xml
        if not chart_path.exists():
            raise FileNotFoundError(chart_path)
        cmd = [
            'python3','tools/fill_chart_xml.py',
            '--chart', str(chart_path),
            '--series_json', str(series),
            '--labels_json', str(labels)
        ]
        out = run(cmd)
        print(out)
    print('p10 filled successfully')

if __name__ == '__main__':
    main()