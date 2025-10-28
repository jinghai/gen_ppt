#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys
from typing import List, Dict

# 扩展为扫描 ppt/charts 与 ppt/charts/charts 下的所有 p* 目录
ROOT = Path(__file__).resolve().parents[2] / 'ppt' / 'charts'


def find_validate_scripts() -> List[Path]:
    bases = [ROOT, ROOT / 'charts']
    scripts: List[Path] = []
    for base in bases:
        if not base.exists():
            continue
        for v in base.rglob('validate.py'):
            # 仅收集页面目录（p*）下的 validate.py
            if v.parent.name.startswith('p'):
                scripts.append(v)
    # 去重并排序
    uniq: Dict[str, Path] = {str(p): p for p in scripts}
    return [uniq[k] for k in sorted(uniq.keys())]


def run_validate(script: Path) -> Dict[str, str]:
    proc = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
    name = script.parent.name
    ok = proc.returncode == 0
    output = (proc.stdout or '').strip()
    error = (proc.stderr or '').strip()
    status = 'PASS' if ok else 'FAIL'
    reason = output if output else error
    return {
        'dir': name,
        'path': str(script),
        'status': status,
        'reason': reason,
    }


def main():
    scripts = find_validate_scripts()
    if not scripts:
        print('No validate scripts found under ppt/charts/* or ppt/charts/charts/*')
        sys.exit(1)
    results = [run_validate(s) for s in scripts]
    all_ok = True
    for r in results:
        print(f"{r['dir']}: {r['status']}" + (f" -> {r['reason']}" if r['status'] == 'FAIL' else ''))
        if r['status'] != 'PASS':
            all_ok = False
    if not all_ok:
        sys.exit(1)


if __name__ == '__main__':
    main()