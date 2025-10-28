#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from lxml import etree
import yaml

NS = {
  'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart',
  'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
  'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
}

def replace_num_cache(val_el, values):
    # 通用数值填充，适配 numRef/numLit 两种缓存形式
    if val_el is None:
        return
    num_ref = val_el.find('c:numRef', namespaces=NS)
    if num_ref is not None:
        num_cache = num_ref.find('c:numCache', namespaces=NS)
        if num_cache is None:
            num_cache = etree.SubElement(num_ref, f'{{{NS["c"]}}}numCache')
        for pt in num_cache.findall('c:pt', namespaces=NS):
            num_cache.remove(pt)
        cnt = num_cache.find('c:ptCount', namespaces=NS)
        if cnt is None:
            cnt = etree.SubElement(num_cache, f'{{{NS["c"]}}}ptCount')
        cnt.set('val', str(len(values)))
        for i, v in enumerate(values):
            pt = etree.SubElement(num_cache, f'{{{NS["c"]}}}pt')
            pt.set('idx', str(i))
            f = etree.SubElement(pt, f'{{{NS["c"]}}}v')
            f.text = str(v)
    else:
        num_lit = val_el.find('c:numLit', namespaces=NS)
        if num_lit is None:
            num_lit = etree.SubElement(val_el, f'{{{NS["c"]}}}numLit')
        for pt in num_lit.findall('c:pt', namespaces=NS):
            num_lit.remove(pt)
        cnt = num_lit.find('c:ptCount', namespaces=NS)
        if cnt is None:
            cnt = etree.SubElement(num_lit, f'{{{NS["c"]}}}ptCount')
        cnt.set('val', str(len(values)))
        for i, v in enumerate(values):
            pt = etree.SubElement(num_lit, f'{{{NS["c"]}}}pt')
            pt.set('idx', str(i))
            f = etree.SubElement(pt, f'{{{NS["c"]}}}v')
            f.text = str(v)

def replace_str_lit(cat_el, labels):
    str_ref = cat_el.find('c:strRef', namespaces=NS)
    if str_ref is not None:
        str_cache = str_ref.find('c:strCache', namespaces=NS)
        if str_cache is None:
            str_cache = etree.SubElement(str_ref, f'{{{NS["c"]}}}strCache')
        for pt in str_cache.findall('c:pt', namespaces=NS):
            str_cache.remove(pt)
        cnt = str_cache.find('c:ptCount', namespaces=NS)
        if cnt is None:
            cnt = etree.SubElement(str_cache, f'{{{NS["c"]}}}ptCount')
        cnt.set('val', str(len(labels)))
        for i, v in enumerate(labels):
            pt = etree.SubElement(str_cache, f'{{{NS["c"]}}}pt')
            pt.set('idx', str(i))
            f = etree.SubElement(pt, f'{{{NS["c"]}}}v')
            f.text = str(v)
    else:
        str_lit = cat_el.find('c:strLit', namespaces=NS)
        if str_lit is None:
            str_lit = etree.SubElement(cat_el, f'{{{NS["c"]}}}strLit')
        for pt in str_lit.findall('c:pt', namespaces=NS):
            str_lit.remove(pt)
        cnt = str_lit.find('c:ptCount', namespaces=NS)
        if cnt is None:
            cnt = etree.SubElement(str_lit, f'{{{NS["c"]}}}ptCount')
        cnt.set('val', str(len(labels)))
        for i, v in enumerate(labels):
            pt = etree.SubElement(str_lit, f'{{{NS["c"]}}}pt')
            pt.set('idx', str(i))
            f = etree.SubElement(pt, f'{{{NS["c"]}}}v')
            f.text = str(v)


def _parse_num_cache(val_el):
    if val_el is None:
        return []
    num_ref = val_el.find('c:numRef', namespaces=NS)
    pts = []
    if num_ref is not None:
        num_cache = num_ref.find('c:numCache', namespaces=NS)
        if num_cache is not None:
            pts = num_cache.findall('c:pt', namespaces=NS)
    else:
        num_lit = val_el.find('c:numLit', namespaces=NS)
        if num_lit is not None:
            pts = num_lit.findall('c:pt', namespaces=NS)
    values = []
    for pt in pts:
        v_el = pt.find('c:v', namespaces=NS)
        txt = v_el.text if v_el is not None else ''
        try:
            values.append(float(txt))
        except (TypeError, ValueError):
            values.append(txt)
    return values


def _parse_str_cache(cat_el):
    if cat_el is None:
        return []
    str_ref = cat_el.find('c:strRef', namespaces=NS)
    pts = []
    if str_ref is not None:
        str_cache = str_ref.find('c:strCache', namespaces=NS)
        if str_cache is not None:
            pts = str_cache.findall('c:pt', namespaces=NS)
    else:
        str_lit = cat_el.find('c:strLit', namespaces=NS)
        if str_lit is not None:
            pts = str_lit.findall('c:pt', namespaces=NS)
    labels = []
    for pt in pts:
        v_el = pt.find('c:v', namespaces=NS)
        labels.append(v_el.text if v_el is not None else '')
    return labels


def _load_config():
    root = Path(__file__).resolve().parents[1]
    cfg = {}
    gp = root / 'config.yaml'
    if gp.exists():
        try:
            cfg = yaml.safe_load(gp.read_text(encoding='utf-8')) or {}
        except Exception:
            cfg = {}
    # 叠加 p10 局部配置（支持新旧目录）
    p10_candidates = [
        root / 'charts' / 'p10' / 'config.yaml',  # charts/charts/p10
        root / 'p10' / 'config.yaml',             # charts/p10
    ]
    for p10p in p10_candidates:
        if p10p.exists():
            try:
                local_cfg = yaml.safe_load(p10p.read_text(encoding='utf-8')) or {}
                if isinstance(local_cfg.get('fill_policy'), dict):
                    base = cfg.get('fill_policy', {}) or {}
                    merged = {**base, **local_cfg['fill_policy']}
                    cfg['fill_policy'] = merged
            except Exception:
                pass
            break
    return cfg


def _get(cfg, keys, default=None):
    cur = cfg
    for k in keys:
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    return cur if cur is not None else default


def fill_chart(chart_xml_path: Path, series_data: list, category_labels: list):
    tree = etree.parse(str(chart_xml_path))
    root = tree.getroot()
    plot = root.find('c:chart/c:plotArea', namespaces=NS)
    if plot is None:
        raise RuntimeError('No plotArea found')
    chart_types = ['lineChart','barChart','pieChart','scatterChart','areaChart','doughnutChart']
    target_chart = None
    for t in chart_types:
        el = plot.find(f'c:{t}', namespaces=NS)
        if el is not None:
            target_chart = el
            break
    if target_chart is None:
        raise RuntimeError('Unsupported chart type')

    cfg = _load_config()
    keep_original = bool(_get(cfg, ['fill_policy','keep_original_for_missing'], False))
    axis_base = int(_get(cfg, ['fill_policy','axis_day_base'], 20300))

    # scatterChart: 使用 xVal/yVal，支持“缺失数据回退到原始图表”
    if target_chart.tag.endswith('scatterChart'):
        series_els = target_chart.findall('c:ser', namespaces=NS)
        for idx, ser in enumerate(series_els):
            new_y = series_data[idx] if (series_data and idx < len(series_data)) else []
            y_el = ser.find('c:yVal', namespaces=NS)
            x_el = ser.find('c:xVal', namespaces=NS)
            if keep_original:
                orig_y = _parse_num_cache(y_el)
                orig_x = _parse_num_cache(x_el)
                final_len = max(len(orig_y), len(new_y))
                final_y = [
                    new_y[i] if i < len(new_y) else (orig_y[i] if i < len(orig_y) else '')
                    for i in range(final_len)
                ]
                final_x = []
                for i in range(final_len):
                    if i < len(new_y):
                        final_x.append(axis_base + 1 + i)
                    else:
                        final_x.append(orig_x[i] if i < len(orig_x) else (axis_base + 1 + i))
            else:
                final_y = new_y
                final_x = [axis_base + 1 + i for i in range(len(new_y))]
            replace_num_cache(y_el, final_y)
            if x_el is not None:
                replace_num_cache(x_el, final_x)
    else:
        # 类别型图表：按标签对齐，缺失标签用原始缓存补齐
        cat_el = target_chart.find('c:cat', namespaces=NS)
        orig_labels = _parse_str_cache(cat_el) if cat_el is not None else []
        series_els = target_chart.findall('c:ser', namespaces=NS)
        n_series = len(series_els)

        if keep_original:
            # 原始映射：label -> [s0,s1,...]
            orig_series_vals = [
                _parse_num_cache(ser.find('c:val', namespaces=NS)) for ser in series_els
            ]
            orig_map = {}
            for i, lbl in enumerate(orig_labels):
                orig_map[lbl] = [
                    (sv[i] if i < len(sv) else '') for sv in orig_series_vals
                ]
            # 新映射
            new_map = {}
            if category_labels is not None and series_data:
                for i, lbl in enumerate(category_labels):
                    new_map[lbl] = [
                        (series_data[s_idx][i] if s_idx < len(series_data) and i < len(series_data[s_idx]) else '')
                        for s_idx in range(n_series)
                    ]
            # 最终标签：以原始顺序为主，追加新出现的标签
            final_labels = list(orig_labels)
            if category_labels:
                for lbl in category_labels:
                    if lbl not in final_labels:
                        final_labels.append(lbl)
            # 组装最终系列数据
            final_series = [[ ] for _ in range(n_series)]
            for lbl in final_labels:
                src = new_map[lbl] if lbl in new_map else orig_map.get(lbl, ['']*n_series)
                for s_idx in range(n_series):
                    final_series[s_idx].append(src[s_idx])
            # 写入
            if cat_el is not None:
                replace_str_lit(cat_el, final_labels)
            for idx, ser in enumerate(series_els):
                val_el = ser.find('c:val', namespaces=NS)
                values = final_series[idx] if idx < len(final_series) else []
                replace_num_cache(val_el, values)
        else:
            # 原有行为：完全用新 labels 和 series 覆盖
            if cat_el is not None and category_labels is not None:
                replace_str_lit(cat_el, category_labels)
            for idx, ser in enumerate(series_els):
                values = series_data[idx] if (series_data and idx < len(series_data)) else []
                val_el = ser.find('c:val', namespaces=NS)
                replace_num_cache(val_el, values)

    tree.write(str(chart_xml_path), encoding='utf-8', xml_declaration=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--chart', required=True, help='chart*.xml 路径')
    ap.add_argument('--series_json', required=True, help='系列数据 JSON 文件路径')
    ap.add_argument('--labels_json', required=False, help='分类标签 JSON 文件路径')
    args = ap.parse_args()
    chart = Path(args.chart)
    series = json.loads(Path(args.series_json).read_text(encoding='utf-8'))
    labels = None
    if args.labels_json:
        labels = json.loads(Path(args.labels_json).read_text(encoding='utf-8'))
    fill_chart(chart, series, labels)
    print(f'filled: {chart}')

if __name__ == '__main__':
    main()