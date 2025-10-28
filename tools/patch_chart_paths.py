import argparse
import os
from pathlib import Path
import yaml


def _resolve_repo_root(start: Path) -> Path:
    """Locate gen_ppt root: must contain config.yaml and input directory."""
    p = start
    for _ in range(8):
        if (p / 'config.yaml').exists() and (p / 'input').exists():
            return p
        if p.parent == p:
            break
        p = p.parent
    return start


def _resolve_unzip_charts_dir(repo_root: Path) -> Path:
    cfg_path = repo_root / 'config.yaml'
    try:
        cfg = yaml.safe_load(cfg_path.read_text(encoding='utf-8')) or {}
    except Exception:
        cfg = {}
    tr = (cfg.get('project') or {}).get('template_root', 'input/LRTBH-unzip')
    unz = Path(tr)
    if not unz.is_absolute():
        unz = repo_root / tr
    d = unz / 'ppt' / 'charts'
    return d if d.exists() else (unz / 'charts')


def patch_chart_paths(root_dir: Path, charts_dir: Path) -> int:
    """Rewrite all chart_path.txt files to point to actual charts_dir.

    Strategy:
    - For each chart_path.txt, derive chart XML basename from current content
      (fallback to directory name like 'chart123' -> 'chart123.xml').
    - Overwrite the file with absolute path: charts_dir / basename.

    Returns the number of files modified.
    """
    modified = 0
    for dirpath, _, filenames in os.walk(str(root_dir)):
        for name in filenames:
            if name != 'chart_path.txt':
                continue
            p = Path(dirpath) / name
            try:
                content = p.read_text(encoding='utf-8').strip()
            except Exception:
                continue
            # Derive chart xml name
            base = None
            if content:
                base = Path(content).name
            if not base or not base.startswith('chart') or not base.endswith('.xml'):
                # Fallback: use parent directory name
                parent = p.parent.name  # e.g., chart123
                if parent.startswith('chart'):
                    base = f"{parent.replace('/', '')}.xml"
                else:
                    # Best effort: keep original content
                    base = Path(content).name if content else None
            if not base:
                continue
            new_path = charts_dir / base
            new_text = str(new_path)
            if new_text != content:
                try:
                    p.write_text(new_text, encoding='utf-8')
                    modified += 1
                except Exception:
                    pass
    return modified


def main():
    parser = argparse.ArgumentParser(description='Patch chart_path.txt to actual charts dir from config')
    parser.add_argument('--root', default='charts', help='Root directory to scan (pages root)')
    parser.add_argument('--charts-dir', default=None, help='Override charts dir (absolute)')
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    repo_root = _resolve_repo_root(script_path.parents[1])
    charts_dir = Path(args.charts_dir) if args.charts_dir else _resolve_unzip_charts_dir(repo_root)
    root_dir = Path(args.root)
    if not root_dir.is_absolute():
        root_dir = repo_root / args.root
    count = patch_chart_paths(root_dir, charts_dir)
    print(f'Patched {count} files to charts_dir={charts_dir}')


if __name__ == '__main__':
    main()