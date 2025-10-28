#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2] / 'charts' / 'charts'

PATTERN = re.compile(r"^(\s*)TOOLS\s*=\s*Path\(__file__\)\.resolve\(\)\.parents\[(\d+)\]\s*/\s*'tools'\s*$")

patched = []
unchanged = []

for pdir in sorted([d for d in ROOT.iterdir() if d.is_dir() and d.name.startswith('p')]):
    fp = pdir / 'validate.py'
    if not fp.exists():
        continue
    txt = fp.read_text(encoding='utf-8')
    lines = txt.splitlines()
    changed = False
    for i, line in enumerate(lines):
        m = PATTERN.match(line)
        if m:
            indent = m.group(1)
            idx = int(m.group(2))
            if idx != 2:
                lines[i] = indent + "TOOLS = Path(__file__).resolve().parents[2] / 'tools'"
                changed = True
            break
    if changed:
        fp.write_text('\n'.join(lines), encoding='utf-8')
        patched.append(str(fp))
    else:
        unchanged.append(str(fp))

print('tools_path_patched:', len(patched))
for f in patched:
    print('  ', f)
print('tools_path_unchanged:', len(unchanged))
for f in unchanged:
    print('  ', f)