#!/usr/bin/env python3
import json
import zipfile
from pathlib import Path
from typing import List, Dict, Any, Optional
from lxml import etree as ET
import click

NS = {
    'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
}


def _read_vals_from_cache(parent: ET._Element, path: str) -> List[Any]:
    el = parent.find(path, namespaces=NS)
    if el is None:
        return []
    cache = el.find('.//c:numCache', namespaces=NS)
    if cache is None:
        cache = el.find('.//c:numLit', namespaces=NS)
    if cache is None:
        # sometimes categories are strings
        cache = el.find('.//c:strCache', namespaces=NS)
        if cache is None:
            cache = el.find('.//c:strLit', namespaces=NS)
    if cache is None:
        return []
    pts = cache.findall('.//c:pt', namespaces=NS)
    if pts:
        pts_sorted = sorted(pts, key=lambda p: int(p.get('idx', '0')))
        values: List[Any] = []
        for p in pts_sorted:
            v = p.find('c:v', namespaces=NS)
            if v is not None and v.text is not None:
                txt = v.text
                try:
                    values.append(float(txt))
                except Exception:
                    values.append(txt)
        return values
    # fallback to direct v list
    values: List[Any] = []
    for v in cache.findall('.//c:v', namespaces=NS):
        if v.text is None:
            continue
        txt = v.text
        try:
            values.append(float(txt))
        except Exception:
            values.append(txt)
    return values


def _read_series_name(ser: ET._Element) -> Optional[str]:
    # Try c:tx -> c:strRef -> c:strCache -> c:pt -> c:v idx=0 OR c:tx -> c:v
    tx = ser.find('c:tx', namespaces=NS)
    if tx is None:
        return None
    v = tx.find('c:v', namespaces=NS)
    if v is not None and v.text:
        return v.text
    cache = tx.find('.//c:strCache', namespaces=NS)
    if cache is not None:
        pt0 = cache.find('.//c:pt[@idx="0"]/c:v', namespaces=NS)
        if pt0 is not None and pt0.text:
            return pt0.text
    return None


def parse_chart_xml(xml_bytes: bytes) -> Dict[str, Any]:
    root = ET.fromstring(xml_bytes)
    # chartSpace -> chart -> plotArea
    plot_area = root.find('.//c:plotArea', namespaces=NS)
    if plot_area is None:
        raise ValueError('chart xml missing c:plotArea')
    # detect chart types present
    types_order = ['barChart', 'lineChart', 'pieChart', 'doughnutChart', 'areaChart', 'scatterChart']
    chart_type = None
    for t in types_order:
        node = plot_area.find(f'c:{t}', namespaces=NS)
        if node is not None:
            chart_type = t
            break
    if chart_type is None:
        chart_type = 'unknown'
    result: Dict[str, Any] = {'chart_type': chart_type}
    # collect series
    sers = plot_area.findall('.//c:ser', namespaces=NS)
    if chart_type == 'scatterChart':
        series_list = []
        for ser in sers:
            name = _read_series_name(ser)
            xs = _read_vals_from_cache(ser, 'c:xVal')
            ys = _read_vals_from_cache(ser, 'c:yVal')
            points = []
            for i in range(max(len(xs), len(ys))):
                x = xs[i] if i < len(xs) else None
                y = ys[i] if i < len(ys) else None
                points.append([x, y])
            series_list.append({'name': name, 'x': xs, 'y': ys, 'points': points})
        result['scatter_series'] = series_list
        return result
    else:
        # non-scatter: categories + each series values
        # categories may sit under ser or under chart-level (but typical is under ser)
        # we prefer to read from the first ser's categories as the canonical labels
        labels: List[Any] = []
        if sers:
            labels = _read_vals_from_cache(sers[0], 'c:cat')
        series_vals = []
        for ser in sers:
            name = _read_series_name(ser)
            vals = _read_vals_from_cache(ser, 'c:val')
            series_vals.append({'name': name, 'values': vals})
        result['labels'] = labels
        result['series'] = series_vals
        return result


@click.command()
@click.option('--ppt', 'pptx_path', required=True, type=click.Path(exists=True, dir_okay=False, path_type=Path), help='原始模板 PPTX 文件路径')
@click.option('--chart', 'chart_name', required=True, type=str, help='图表文件名，如 chart8.xml')
@click.option('--out', 'out_dir', required=True, type=click.Path(path_type=Path), help='输出目录，用于写入原始数据 JSON')
def main(pptx_path: Path, chart_name: str, out_dir: Path):
    chart_path_in_zip = f'ppt/charts/{chart_name}'
    if not out_dir.exists():
        out_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(pptx_path, 'r') as z:
        try:
            xml_bytes = z.read(chart_path_in_zip)
        except KeyError:
            raise SystemExit(f'Chart not found in PPTX: {chart_path_in_zip}')
    parsed = parse_chart_xml(xml_bytes)
    # write meta
    (out_dir / 'original_meta.json').write_text(json.dumps({'chart': chart_name, **parsed}, ensure_ascii=False, indent=2))
    # scatter vs non-scatter
    if parsed.get('chart_type') == 'scatterChart':
        (out_dir / 'original_scatter.json').write_text(json.dumps(parsed['scatter_series'], ensure_ascii=False, indent=2))
    else:
        (out_dir / 'original_labels.json').write_text(json.dumps(parsed.get('labels', []), ensure_ascii=False, indent=2))
        (out_dir / 'original_series.json').write_text(json.dumps(parsed.get('series', []), ensure_ascii=False, indent=2))
    print(f'Extracted original data for {chart_name} -> {out_dir}')


if __name__ == '__main__':
    main()