#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

# 允许相对导入工具
TOOLS = Path(__file__).resolve().parents[2] / 'tools'
sys.path.append(str(TOOLS))
from extract_chart_cache import parse_chart_xml  # type: ignore

P10 = Path(__file__).resolve().parents[0]


def _eq(a: Any, b: Any, tol: float = 1e-9) -> bool:
    try:
        af = float(a)
        bf = float(b)
        return abs(af - bf) <= tol
    except Exception:
        return a == b


def _read(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return None


def _load_chart_xml_bytes(chart_path_txt: Path) -> bytes:
    """从原始模板 PPTX 的 zip 中读取 chart*.xml，而不是使用 chart_path.txt 指向的工作区副本。
    这样可以避免预览/填充修改后的 UNZIPPED 内容影响“原始缓存 vs 模板”的一致性校验。
    """
    raw = chart_path_txt.read_text(encoding='utf-8').strip()
    chart_name = Path(raw).name  # e.g. chart8.xml
    # 优先从全局配置读取 original_ppt 路径
    cfg = None
    try:
        import yaml  # 延迟导入，避免运行环境不装时失败
        root = Path(__file__).resolve().parents[3]
        config = root / 'ppt' / 'config.yaml'
        if config.exists():
            cfg = yaml.safe_load(config.read_text(encoding='utf-8')) or {}
    except Exception:
        cfg = None
    original_ppt = None
    if cfg:
        p = (cfg.get('project') or {}).get('original_ppt')
        if p:
            pp = Path(p)
            original_ppt = pp if pp.is_absolute() else root / p
    if not original_ppt:
        original_ppt = Path(__file__).resolve().parents[3] / 'ppt' / 'input' / 'LRTBH.pptx'

    import zipfile
    with zipfile.ZipFile(original_ppt, 'r') as z:
        return z.read(f'ppt/charts/{chart_name}')


def validate_original_vs_template(chart_dir: Path) -> Tuple[bool, List[str]]:
    """验证 original_* 与模板 chart*.xml 的解析结果完全一致"""
    errs: List[str] = []
    # parse current xml
    xml_bytes = _load_chart_xml_bytes(chart_dir / 'chart_path.txt')
    parsed = parse_chart_xml(xml_bytes)
    ctype = parsed.get('chart_type')
    if ctype == 'scatterChart':
        orig_scatter = _read(chart_dir / 'original_scatter.json') or []
        parsed_scatter = parsed.get('scatter_series') or []
        if len(orig_scatter) != len(parsed_scatter):
            errs.append('scatter series length mismatch')
        # compare series
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
        orig_labels = _read(chart_dir / 'original_labels.json') or []
        orig_series = _read(chart_dir / 'original_series.json') or []
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
        # 仅系列时，用第一系列长度
        s0 = data_json[0] if data_json else []
        return len(s0)
    return 0


def validate_counts(chart_dir: Path) -> Tuple[bool, List[str]]:
    """验证 data 与 final_data 的数据量与原始一致，不少数据"""
    errs: List[str] = []
    meta = _read(chart_dir / 'original_meta.json') or {}
    ctype = meta.get('chart_type')
    if ctype == 'scatterChart':
        orig = _read(chart_dir / 'original_scatter.json')
        base = _count_scatter_y(orig)
        djson = _read(chart_dir / 'data.json')
        fjson = _read(chart_dir / 'final_data.json')
        dlen = _count_scatter_y(djson)
        flen = _count_scatter_y(fjson)
        if dlen < base:
            errs.append(f'data.json y length {dlen} < original {base}')
        if flen < base:
            errs.append(f'final_data.json y length {flen} < original {base}')
    else:
        orig_lbls = _read(chart_dir / 'original_labels.json') or []
        base = len(orig_lbls)
        djson = _read(chart_dir / 'data.json')
        fjson = _read(chart_dir / 'final_data.json')
        dlen = _count_category_len(djson)
        flen = _count_category_len(fjson)
        if dlen < base:
            errs.append(f'data.json labels length {dlen} < original {base}')
        if flen < base:
            errs.append(f'final_data.json labels length {flen} < original {base}')
    return (len(errs) == 0), errs


def main():
    all_ok = True
    messages: List[str] = []
    for name in ['chart8', 'chart9']:
        d = P10 / name
        ok1, errs1 = validate_original_vs_template(d)
        ok2, errs2 = validate_counts(d)
        if ok1 and ok2:
            messages.append(f'{name}: OK')
        else:
            all_ok = False
            if not ok1:
                messages.append(f'{name}: 原始与模板不一致 -> ' + '; '.join(errs1))
            if not ok2:
                messages.append(f'{name}: 数据量校验失败 -> ' + '; '.join(errs2))
    print('\n'.join(messages))
    if not all_ok:
        sys.exit(1)


if __name__ == '__main__':
    main()