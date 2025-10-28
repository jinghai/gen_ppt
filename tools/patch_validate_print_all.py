#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2] / 'charts' / 'charts'

# 更稳健的两行匹配：第一行是 print(' 或 print("，第二行是 '.join(VAR))，保留原变量名
LINE1 = re.compile(r"^\s*print\(\s*['\"]\s*$")
LINE2 = re.compile(r"^\s*['\"]\.join\(([A-Za-z_][A-Za-z0-9_]*)\)\)\s*$")

patched_files = []
warn_files = []

for pdir in sorted([d for d in ROOT.iterdir() if d.is_dir() and d.name.startswith('p')]):
    fp = pdir / 'validate.py'
    if not fp.exists():
        continue
    txt = fp.read_text(encoding='utf-8')
    lines = txt.splitlines()
    changed = False

    for i in range(len(lines) - 1):
        li = lines[i]
        lj = lines[i+1]
        m1 = LINE1.match(li)
        m2 = LINE2.match(lj)
        if m1 and m2:
            var = m2.group(1)
            indent = li[:len(li) - len(li.lstrip())]
            lines[i] = indent + f"print('\\n'.join({var}))"
            lines[i+1] = ''
            changed = True
            break

    if changed:
        fp.write_text('\n'.join([l for l in lines if l != '']), encoding='utf-8')

    after = fp.read_text(encoding='utf-8')
    # 视为成功：包含 print('\n'.join( 或 print("\n".join(
    if re.search(r"print\(\s*['\"]\\n['\"]\.join\(", after):
        patched_files.append(str(fp))
    else:
        warn_files.append(str(fp))

print('patched_ok:', len(patched_files))
for f in patched_files:
    print('  ', f)
print('patch_warnings:', len(warn_files))
for f in warn_files:
    print('  ', f)