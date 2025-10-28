#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为指定页面（如 p8..p31）创建缺失的通用脚本：
- build.py：占位说明（后续若有单页打包需求再实现）
- build_original.py：调用 generate_original_cache.py 生成原始缓存
- gen_preview.py：离线批量生成 preview_original.png（每个 chart* 目录）
- validate.py：对比 original_* 与模板 chart.xml 解析一致性，并校验数据量不小于原始
"""
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / 'charts' / 'tools'
PAGES_DIR = ROOT / 'charts' / 'charts'

BUILD_PY_TMPL = """#!/usr/bin/env python3
print("[info] build stub: implement slide-specific packaging after template is complete")
"""

BUILD_ORIGINAL_TMPL = """#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
TOOLS = THIS_DIR.parents[1] / 'tools'

if __name__ == '__main__':
    # 仅生成/补齐当前页面的 original_* 原始缓存（已存在则跳过）
    cmd = [sys.executable, str(TOOLS / 'generate_original_cache.py'), '--pages', THIS_DIR.name]
    subprocess.run(cmd, check=True)
    # 将根目录 original_* 同步到 original/ 子目录（缺失时复制）
    subprocess.run([sys.executable, str(TOOLS / 'sync_original_subdir.py'), '--pages', THIS_DIR.name], check=True)
    print('[done] original_* ensured for', THIS_DIR)
"""

GEN_PREVIEW_TMPL = """#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1] / 'tools'
sys.path.append(str(TOOLS))
from gen_preview_chart import generate_preview  # type: ignore

PAGE = Path(__file__).resolve().parent


def main():
    charts = [c for c in PAGE.iterdir() if c.is_dir() and re.match(r'^chart\\d+$', c.name)]
    ok = 0
    for c in charts:
        if generate_preview(c):
            ok += 1
    print(f'[done] previews generated: {ok}/{len(charts)} in {PAGE}')


if __name__ == '__main__':
    main()
"""

VALIDATE_TMPL = """#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

TOOLS = Path(__file__).resolve().parents[1] / 'tools'
sys.path.append(str(TOOLS))
from extract_chart_cache import parse_chart_xml  # type: ignore

PAGE = Path(__file__).resolve().parent


def _eq(a: Any, b: Any, tol: float = 1e-9) -> bool:
    try:
        af = float(a)
        bf = float(b)
        return abs(af - bf) <= tol
    except Exception:
        return a == b


def _read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return None


def _read_chart_xml_bytes(chart_dir: Path) -> bytes:
    p = chart_dir / 'chart_path.txt'
    xml_path = Path(p.read_text(encoding='utf-8').strip())
    return xml_path.read_bytes()


def _original_file(chart_dir: Path, name: str) -> Path:
    sub = chart_dir / 'original' / name
    if sub.exists():
        return sub
    root = chart_dir / name
    return root


def validate_original_vs_template(chart_dir: Path) -> Tuple[bool, List[str]]:
    errs: List[str] = []
    xml_bytes = _read_chart_xml_bytes(chart_dir)
    parsed = parse_chart_xml(xml_bytes)
    ctype = parsed.get('chart_type')
    if ctype == 'scatterChart':
        orig_scatter = _read_json(_original_file(chart_dir, 'original_scatter.json')) or []
        parsed_scatter = parsed.get('scatter_series') or []
        if len(orig_scatter) != len(parsed_scatter):
            errs.append('scatter series length mismatch')
        for i in range(min(len(orig_scatter), len(parsed_scatter))):
            os = orig_scatter[i]
            ps = parsed_scatter[i]
            ox, oy = os.get('x', []), os.get('y', [])
            px, py = ps.get('x', []), ps.get('y', [])
            if len(ox) != len(px) or len(oy) != len(py):
                errs.append(f'scatter[{i}] x/y length mismatch')
            else:
                for j in range(len(ox)):
                    if not _eq(ox[j], px[j]) or not _eq(oy[j], py[j]):
                        errs.append(f'scatter[{i}] point {j} mismatch')
                        break
    else:
        orig_labels = _read_json(_original_file(chart_dir, 'original_labels.json')) or []
        orig_series = _read_json(_original_file(chart_dir, 'original_series.json')) or []
        plabels = parsed.get('labels') or []
        pseries = parsed.get('series') or []
        if len(orig_labels) != len(plabels):
            errs.append('labels length mismatch')
        else:
            for j in range(len(orig_labels)):
                if not _eq(orig_labels[j], plabels[j]):
                    errs.append(f'label[{j}] mismatch')
                    break
        if len(orig_series) != len(pseries):
            errs.append('series count mismatch')
        else:
            for si in range(len(orig_series)):
                ov = orig_series[si]['values'] if isinstance(orig_series[si], dict) else (orig_series[si] or [])
                pv = pseries[si]['values'] if isinstance(pseries[si], dict) else (pseries[si] or [])
                if len(ov) != len(pv):
                    errs.append(f'series[{si}] length mismatch')
                    break
                for j in range(len(ov)):
                    if not _eq(ov[j], pv[j]):
                        errs.append(f'series[{si}][{j}] value mismatch')
                        break
    return (len(errs) == 0), errs


def _count_scatter_y(series_json: Any) -> int:
    if isinstance(series_json, dict) and 'scatter_series' in series_json:
        arr = series_json.get('scatter_series') or []
        if not arr:
            return 0
        return len(arr[0].get('y') or [])
    if isinstance(series_json, list):
        if not series_json:
            return 0
        s0 = series_json[0]
        if isinstance(s0, dict):
            return len(s0.get('y') or [])
        if isinstance(s0, list):
            return len(s0)
    return 0


def _count_category_len(data_json: Any) -> int:
    if isinstance(data_json, dict):
        lbls = data_json.get('labels') or []
        return len(lbls)
    if isinstance(data_json, list):
        s0 = data_json[0] if data_json else []
        return len(s0)
    return 0


def validate_counts(chart_dir: Path) -> Tuple[bool, List[str]]:
    errs: List[str] = []
    meta = _read_json(_original_file(chart_dir, 'original_meta.json')) or {}
    ctype = meta.get('chart_type')
    if ctype == 'scatterChart':
        orig = _read_json(_original_file(chart_dir, 'original_scatter.json'))
        base = _count_scatter_y(orig)
        djson = _read_json(chart_dir / 'data.json')
        fjson = _read_json(chart_dir / 'final_data.json')
        dlen = _count_scatter_y(djson)
        flen = _count_scatter_y(fjson)
        if dlen < base:
            errs.append(f'data.json y length {dlen} < original {base}')
        if flen < base:
            errs.append(f'final_data.json y length {flen} < original {base}')
    else:
        orig_lbls = _read_json(_original_file(chart_dir, 'original_labels.json')) or []
        base = len(orig_lbls)
        djson = _read_json(chart_dir / 'data.json')
        fjson = _read_json(chart_dir / 'final_data.json')
        dlen = _count_category_len(djson)
        flen = _count_category_len(fjson)
        if dlen < base:
            errs.append(f'data.json labels length {dlen} < original {base}')
        if flen < base:
            errs.append(f'final_data.json labels length {flen} < original {base}')
    return (len(errs) == 0), errs


def main():
    import re as _re
    charts = [c for c in PAGE.iterdir() if c.is_dir() and _re.match(r'^chart\d+$', c.name)]
    all_ok = True
    msgs: List[str] = []
    for c in charts:
        ok1, e1 = validate_original_vs_template(c)
        ok2, e2 = validate_counts(c)
        if ok1 and ok2:
            msgs.append(f'{c.name}: OK')
        else:
            all_ok = False
            if not ok1:
                msgs.append(f'{c.name}: 原始与模板不一致 -> ' + '; '.join(e1))
            if not ok2:
                msgs.append(f'{c.name}: 数据量校验失败 -> ' + '; '.join(e2))
    print('\n'.join(msgs))
    if not all_ok:
        sys.exit(1)


if __name__ == '__main__':
    PAGE = Path(__file__).resolve().parent
    main()
"""


REQUIRED = {
    'build.py': BUILD_PY_TMPL,
    'build_original.py': BUILD_ORIGINAL_TMPL,
    'gen_preview.py': GEN_PREVIEW_TMPL,
    'validate.py': VALIDATE_TMPL,
}


def ensure_page(page_dir: Path) -> int:
    created = 0
    for fn, content in REQUIRED.items():
        fp = page_dir / fn
        if not fp.exists():
            fp.write_text(content, encoding='utf-8')
            created += 1
    return created


def main():
    ap = argparse.ArgumentParser(description='Ensure missing page scripts exist with generic implementations')
    ap.add_argument('--pages', nargs='*', default=None, help='pages like p8 p10 ...; default all p*')
    args = ap.parse_args()
    if args.pages:
        pages = [PAGES_DIR / p for p in args.pages]
    else:
        import re as _re
        pages = [p for p in PAGES_DIR.iterdir() if p.is_dir() and _re.match(r'^p\d+$', p.name)]
    total = 0
    for p in pages:
        total += ensure_page(p)
    print('Created files:', total)


if __name__ == '__main__':
    main()