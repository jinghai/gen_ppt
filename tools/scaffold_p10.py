#!/usr/bin/env python3
import json
from pathlib import Path
import yaml


def _find_root(start: Path) -> Path:
    p = start
    while p.parent != p:
        if (p / 'config.yaml').exists() and (p / 'input').exists():
            return p
        p = p.parent
    return start

TOOLS_DIR = Path(__file__).resolve().parent
ROOT = _find_root(TOOLS_DIR)
OUT = ROOT / 'charts' / 'p10'

P10_CHARTS = ['chart8.xml', 'chart9.xml']

SCAFFOLD = {
    'chart8.xml': {
        'labels': ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        'series': [[10,12,13,9,8,7,11]]
    },
    'chart9.xml': {
        'labels': ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        'series': [[30,28,26,25,27,29,30]]
    }
}

def _resolve_unz_root() -> Path:
    try:
        cfg = yaml.safe_load((ROOT / 'config.yaml').read_text(encoding='utf-8')) or {}
    except Exception:
        cfg = {}
    tr = (cfg.get('project') or {}).get('template_root', 'input/LRTBH-unzip')
    p = Path(tr)
    if not p.is_absolute():
        p = ROOT / tr
    return p

def _charts_dir(unz: Path) -> Path:
    d = unz / 'ppt' / 'charts'
    return d if d.exists() else unz / 'charts'

def main():
    charts_root = _charts_dir(_resolve_unz_root())
    OUT.mkdir(parents=True, exist_ok=True)
    for c in P10_CHARTS:
        chart_path = charts_root / c
        dest_dir = OUT / c.replace('.xml','')
        dest_dir.mkdir(parents=True, exist_ok=True)
        # write placeholders
        (dest_dir / 'labels.json').write_text(json.dumps(SCAFFOLD[c]['labels'], ensure_ascii=False, indent=2), encoding='utf-8')
        (dest_dir / 'series.json').write_text(json.dumps(SCAFFOLD[c]['series'], ensure_ascii=False, indent=2), encoding='utf-8')
        # write pointers：仅写入 chart 名称，路径解析走统一逻辑
        (dest_dir / 'chart_path.txt').write_text(c, encoding='utf-8')
    print('scaffolded p10 charts at', OUT)

if __name__ == '__main__':
    main()