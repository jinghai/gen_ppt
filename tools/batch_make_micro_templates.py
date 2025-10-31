#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量为 charts 下的每个页面生成微模板，并为每个页面中涉及到的嵌入对象（embeddings）生成对应的 .xlsx 文件（新数据快照，输出到页面级目录）：

- 微模板使用原始模板的样式与关系，保证生成的 PPT 样式一模一样；
- embeddings 目录只保留原始 .xlsb 作为旧数据；若微模板中的关系或嵌入文件出现 .xlsx/.bin 等非 .xlsb，则尝试从 input/LRTBH-unzip 中查找对应 .xlsb 并修正关系为 .xlsb；
- 额外生成的新数据快照 .xlsx 输出到 charts/pXX/xlsx_snapshots 目录，避免污染模板的 embeddings 目录；

设计说明：
- 先调用 tools/make_micro_template.py 为目标页面生成微模板目录 charts/pXX/template；
- 解析微模板中的 chart*.xml.rels，定位每个图表使用的嵌入对象文件名（如 oleObject1.bin、worksheet1.xlsb 或 embedding3.xlsx）；
- 读取 charts/pXX/chartN/ 下的 final_data.json（优先）或 data.json，按图表类型（bar/pie/area/doughnut -> 分类；line/scatter -> 趋势/散点）生成 .xlsx；
- 一个嵌入对象对应一个工作簿（Workbook），其中每个引用该嵌入的图表生成一个 Sheet；
- 新数据命名规则：若旧文件扩展为 .xlsx，则新数据命名为 "{basename}__new.xlsx"；否则命名为 "{basename}.xlsx"；上述 .xlsx 始终写入页面级目录 xlsx_snapshots 下。

注意：不会修改 chart*.xml.rels 的引用目标，新增的 .xlsx 仅作为数据快照随微模板打包保留；这能满足“样式一模一样”的要求，并让旧/新数据在 embeddings 目录中并存，便于后续流程使用。

更新：为满足 build_original 的严格校验（embeddings 目录仅允许 .xlsb），本脚本在生成微模板后会：
- 检查并修正图表关系(.rels)中指向 embeddings 的目标文件扩展为 .xlsb；
- 从 /input/LRTBH-unzip/ppt/embeddings 中查找并复制缺失的 .xlsb；
- 将微模板中的非 .xlsb 嵌入文件移至页面目录 charts/pXX/embeddings_backup 备份。

命令行参数：
- --pages p8 p10 ... 指定页面；缺省则遍历 charts/pXX 全部页面
- --skip-make-data 跳过执行每页的 make_data.py；默认执行（若存在）
- --zip-preview 同时将微模板目录打包为 charts/pXX/output/pXX.template.pptx（默认不打包）

依赖：requirements.txt 已包含 lxml 与 openpyxl；本脚本仅复用这些依赖。
"""

from __future__ import annotations
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from lxml import etree as ET
from openpyxl import Workbook
import shutil


# 路径辅助：将 tools 目录加入 sys.path，便于导入同目录脚本
TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

# 尝试导入 make_micro_template；若缺失则提供轻量级 _find_repo_root 回退，并在主流程中跳过微模板生成，仅做 .xlsb 强制与快照生成
HAVE_MAKE_MICRO = True
try:
    from make_micro_template import make_micro_template_for_page, _find_repo_root  # type: ignore
except Exception:
    HAVE_MAKE_MICRO = False
    def _find_repo_root(start: Path) -> Path:
        """回退：从当前目录向上寻找包含 charts/ 与 config.yaml 的仓库根。"""
        cur = start
        for _ in range(6):
            if (cur / 'charts').exists() and (cur / 'config.yaml').exists():
                return cur
            cur = cur.parent
        # 兜底：返回上两级
        return start.parent.parent


def _detect_chart_type(chart_xml_path: Path) -> str:
    """根据 chart*.xml 内容检测图表类型。
    返回值之一：barChart/pieChart/areaChart/doughnutChart/lineChart/scatterChart/unknown。
    约定：若同时存在多种节点，按常见优先序返回第一个匹配。
    """
    if not chart_xml_path.exists():
        return 'unknown'
    try:
        root = ET.fromstring(chart_xml_path.read_bytes())
    except Exception:
        return 'unknown'
    ns = {
        'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart'
    }
    # 常见类型按优先序检查
    if root.findall('.//c:barChart', ns):
        return 'barChart'
    if root.findall('.//c:pieChart', ns):
        # doughnut 在 Office XML 仍然是 pieChart 的一类，这里区分不强制
        return 'pieChart'
    if root.findall('.//c:areaChart', ns):
        return 'areaChart'
    if root.findall('.//c:lineChart', ns):
        return 'lineChart'
    if root.findall('.//c:scatterChart', ns):
        return 'scatterChart'
    # 非标准命名尝试（某些脚本约定）
    txt = chart_xml_path.read_text(encoding='utf-8', errors='ignore')
    if 'doughnutChart' in txt:
        return 'doughnutChart'
    return 'unknown'


def _resolve_chart_xml_name(chart_dir: Path) -> Optional[str]:
    """从 chartN 目录解析其实际 XML 文件名：优先 chart_path.txt，否则回退为 chartN.xml。"""
    name = None
    p = chart_dir / 'chart_path.txt'
    if p.exists():
        try:
            raw = p.read_text(encoding='utf-8').strip()
            if raw:
                name = Path(raw).name
        except Exception:
            name = None
    if not name:
        name = f"{chart_dir.name}.xml"
    return name


def _chart_to_embed_name(tpl_dir: Path, chart_xml_name: str) -> Optional[str]:
    """读取微模板中的 chart*.xml.rels，返回该图表引用的 embeddings 文件名（如 oleObject1.bin / worksheet1.xlsb / embedding3.xlsx）。
    若无嵌入引用则返回 None。
    """
    rels = tpl_dir / 'ppt' / 'charts' / '_rels' / f'{chart_xml_name}.rels'
    if not rels.exists():
        return None
    try:
        root = ET.fromstring(rels.read_bytes())
    except Exception:
        return None
    for rel in root.findall('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
        typ = rel.get('Type') or ''
        tgt = rel.get('Target') or ''
        # 两种方式：Type 为 oleObject 或 Target 指向 ../embeddings/
        if typ.endswith('/oleObject') or ('embeddings/' in tgt):
            return Path(tgt).name
    return None


def _new_embed_xlsx_name(old_embed_name: str) -> str:
    """给出旧嵌入文件名，返回新数据 .xlsx 的命名：
    - 若旧文件扩展为 .xlsx，则返回 "{stem}__new.xlsx" 以避免覆盖；
    - 其他扩展（.xlsb/.bin/...）返回 "{stem}.xlsx"。
    """
    stem = Path(old_embed_name).stem
    ext = Path(old_embed_name).suffix.lower()
    if ext == '.xlsx':
        return f'{stem}__new.xlsx'
    return f'{stem}.xlsx'


def _load_chart_json(chart_dir: Path) -> Tuple[str, Dict[str, object]]:
    """加载图表数据 JSON：优先 final_data.json，其次 data.json。
    返回 (来源文件名, 数据对象)。若均不存在，返回 ('', {})。
    """
    f1 = chart_dir / 'final_data.json'
    f2 = chart_dir / 'data.json'
    src = ''
    obj: Dict[str, object] = {}
    try:
        if f1.exists():
            src = 'final_data.json'
            obj = json.loads(f1.read_text(encoding='utf-8'))
        elif f2.exists():
            src = 'data.json'
            obj = json.loads(f2.read_text(encoding='utf-8'))
    except Exception:
        src = ''
        obj = {}
    return src, obj


def _enforce_xlsb_embeddings(page_dir: Path, unzipped_root: Path, repo_root: Path) -> int:
    """在生成微模板后，强制将 embeddings 的引用与文件统一为 .xlsb：
    - 解析 charts/pXX/template/ppt/charts/_rels 下的每个 .rels；
    - 若关系目标为 ../embeddings/*.xlsx 或 *.bin，则尝试在 unzipped_root/ppt/embeddings 中查找同 stem 的 .xlsb；
    - 找到则复制至微模板 embeddings，并将 .rels 的 Target 修正为 .xlsb；
    - 若目标已为 .xlsb 但文件缺失，则同样从 unzipped_root 复制；
    - 将微模板中非 .xlsb 的 embeddings 文件移动到 charts/pXX/embeddings_backup；
    返回已修正的关系条数。
    """
    tpl_dir = page_dir / 'template'
    charts_rels = tpl_dir / 'ppt' / 'charts' / '_rels'
    embeds_dir = tpl_dir / 'ppt' / 'embeddings'
    unz_embeds_dir = unzipped_root / 'ppt' / 'embeddings'
    if not charts_rels.exists() or not embeds_dir.exists():
        print(f'[{page_dir.name}] 微模板未生成或结构不完整，跳过 .xlsb 强制检查：{tpl_dir}')
        return 0

    changed = 0
    missing_log = repo_root / 'logs' / 'batch_missing_xlsb.log'
    missing_log.parent.mkdir(parents=True, exist_ok=True)

    # 逐个 .rels 修正 Target 指向 .xlsb，并复制缺失文件
    for rels_path in sorted(charts_rels.glob('*.rels')):
        try:
            tree = ET.parse(str(rels_path))
            root = tree.getroot()
        except Exception as e:
            print(f'[{page_dir.name}] 解析 .rels 失败：{rels_path.name} -> {e}')
            continue
        updated = False
        referenced_after: List[str] = []
        for rel in root.findall('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
            tgt = rel.get('Target') or ''
            if 'embeddings/' not in tgt:
                continue
            old_name = Path(tgt).name
            stem = Path(old_name).stem
            ext = Path(old_name).suffix.lower()
            # 目标应为 .xlsb
            new_name = f'{stem}.xlsb'
            src_xlsb = unz_embeds_dir / new_name
            dest_xlsb = embeds_dir / new_name

            if ext == '.xlsb':
                # 仅保证文件存在
                if not dest_xlsb.exists():
                    if src_xlsb.exists():
                        try:
                            shutil.copy2(str(src_xlsb), str(dest_xlsb))
                            print(f'[{page_dir.name}] 补齐缺失 .xlsb：{new_name}')
                        except Exception as e:
                            print(f'[{page_dir.name}] 复制 .xlsb 失败：{src_xlsb} -> {e}')
                    else:
                        with missing_log.open('a', encoding='utf-8') as fp:
                            fp.write(f'{page_dir.name}: 缺失 .xlsb {new_name}（未在 {unz_embeds_dir} 找到）\n')
                        print(f'[{page_dir.name}] 缺失 .xlsb：{new_name}（未找到来源）')
                referenced_after.append(new_name)
                continue

            # 不是 .xlsb：尝试从 unzipped_root 查找同 stem 的 .xlsb 并修正关系
            if src_xlsb.exists():
                try:
                    shutil.copy2(str(src_xlsb), str(dest_xlsb))
                    rel.set('Target', f'../embeddings/{new_name}')
                    updated = True
                    print(f'[{page_dir.name}] 修正关系 -> .xlsb：{rels_path.name} : {old_name} -> {new_name}')
                    referenced_after.append(new_name)
                except Exception as e:
                    print(f'[{page_dir.name}] 修正关系复制失败：{src_xlsb} -> {e}')
            else:
                # 回退：按 stem 搜索任何 .xlsb
                alt = None
                for cand in unz_embeds_dir.glob('*.xlsb'):
                    if cand.stem == stem:
                        alt = cand
                        break
                if alt:
                    try:
                        shutil.copy2(str(alt), str(dest_xlsb))
                        rel.set('Target', f'../embeddings/{alt.name}')
                        updated = True
                        print(f'[{page_dir.name}] 修正关系(回退) -> .xlsb：{rels_path.name} : {old_name} -> {alt.name}')
                        referenced_after.append(alt.name)
                    except Exception as e:
                        print(f'[{page_dir.name}] 修正关系复制失败(回退)：{alt} -> {e}')
                else:
                    with missing_log.open('a', encoding='utf-8') as fp:
                        fp.write(f'{page_dir.name}: 无法为 {old_name} 找到对应 .xlsb（来源 {unz_embeds_dir}）\n')
                    print(f'[{page_dir.name}] 未找到 {old_name} 的 .xlsb 对应，关系未修正')
                    # 保留原始引用，避免破坏微模板；记录引用的非 .xlsb 名称
                    referenced_after.append(old_name)

        if updated:
            try:
                tree.write(str(rels_path), xml_declaration=True, encoding='utf-8')
                changed += 1
            except Exception as e:
                print(f'[{page_dir.name}] 写回 .rels 失败：{rels_path.name} -> {e}')

        # 将 embeddings 目录中未被引用的非 .xlsb 文件移到备份目录
        try:
            backup_dir = page_dir / 'embeddings_backup'
            backup_dir.mkdir(parents=True, exist_ok=True)
            ref_set = set(referenced_after)
            for f in sorted(embeds_dir.glob('*')):
                if f.is_file() and f.suffix.lower() != '.xlsb' and f.name not in ref_set:
                    dest = backup_dir / f.name
                    try:
                        shutil.move(str(f), str(dest))
                        print(f'[{page_dir.name}] 备份未引用的非 .xlsb：{f.name} -> {dest}')
                    except Exception as e:
                        print(f'[{page_dir.name}] 备份未引用的非 .xlsb 失败：{f.name} -> {e}')
        except Exception as e:
            print(f'[{page_dir.name}] 备份非 .xlsb 时出错：{e}')

    return changed


def _write_sheet_for_category(ws, labels: List[str], series: List[Dict[str, object]], title: str):
    """将分类图数据写入单个 Sheet：
    - 首行：Label + 每个系列名（若无名称则使用 Series{i}）
    - 后续每行：labels[i] + 各系列的 values[i]
    """
    ws.title = title[:31]  # Excel sheet 名最长 31
    header = ['Label']
    # 系列名
    names: List[str] = []
    for i, s in enumerate(series):
        n = s.get('name')
        if isinstance(n, str) and n:
            names.append(n)
        else:
            names.append(f'Series{i+1}')
    header.extend(names)
    ws.append(header)
    # 逐行写入
    # 允许 series[i]['values'] 缺失或长度不同，按索引安全取值
    max_len = len(labels)
    values_list: List[List[Optional[float]]] = []
    for s in series:
        vals = s.get('values') or []
        if not isinstance(vals, list):
            vals = []
        values_list.append(vals)  # type: ignore
    for idx in range(max_len):
        row = [labels[idx] if idx < len(labels) else '']
        for vals in values_list:
            v = vals[idx] if idx < len(vals) else None
            row.append(v)
        ws.append(row)


def _write_sheet_for_scatter(ws, series: List[Dict[str, object]], title: str):
    """将散点/趋势数据写入单个 Sheet：
    - 首行：Index + Series1..N（若 series[i] 存在 name 则替换列名）；
    - 后续每行：索引 + 各序列的 y 值；
    - 若提供 points=[(x,y),...] 则取 y 值；如提供 y=[...] 列表则直接使用。
    """
    ws.title = title[:31]
    names: List[str] = []
    values_list: List[List[Optional[float]]] = []
    for i, s in enumerate(series):
        n = s.get('name')
        if isinstance(n, str) and n:
            names.append(n)
        else:
            names.append(f'Series{i+1}')
        # 统一取 y 列；若无 y，则从 points 中提取第二维
        ys = s.get('y')
        if isinstance(ys, list):
            vals = ys
        else:
            pts = s.get('points') or []
            vals = [p[1] for p in pts if isinstance(p, (list, tuple)) and len(p) >= 2]
        values_list.append(vals)  # type: ignore
    header = ['Index'] + names
    ws.append(header)
    max_len = max((len(vs) for vs in values_list), default=0)
    for idx in range(max_len):
        row = [idx + 1]
        for vals in values_list:
            v = vals[idx] if idx < len(vals) else None
            row.append(v)
        ws.append(row)


def _ensure_make_data(page_dir: Path) -> None:
    """若页面有 make_data.py 则执行之，生成最新 JSON 数据。"""
    script = page_dir / 'make_data.py'
    if script.exists():
        print(f'[{page_dir.name}] run make_data.py')
        subprocess.run([sys.executable, str(script)], check=True, cwd=str(page_dir))
    else:
        print(f'[{page_dir.name}] skip make_data.py (not found)')


def _collect_chart_dirs(page_dir: Path) -> List[Path]:
    """枚举 charts/pXX 下的 chartN 目录。"""
    chart_dirs: List[Path] = []
    for p in sorted(page_dir.iterdir(), key=lambda x: x.name):
        if p.is_dir() and re.match(r'^chart\d+$', p.name):
            chart_dirs.append(p)
    return chart_dirs


def _generate_xlsx_for_page(page_dir: Path) -> int:
    """为单个页面生成 .xlsx 新数据快照，输出到页面目录 xlsx_snapshots。
    - 返回生成的 .xlsx 文件个数。
    """
    tpl_dir = page_dir / 'template'
    charts_root = tpl_dir / 'ppt' / 'charts'
    snapshots_root = page_dir / 'xlsx_snapshots'
    if not charts_root.exists():
        print(f'[{page_dir.name}] 微模板未生成或结构不完整，跳过 xlsx：{tpl_dir}')
        return 0
    snapshots_root.mkdir(parents=True, exist_ok=True)

    chart_dirs = _collect_chart_dirs(page_dir)
    # 每个嵌入一个工作簿
    wb_map: Dict[str, Workbook] = {}
    # 统计每个嵌入下已写入的 sheet 个数，构造 sheet 名
    sheet_count: Dict[str, int] = {}

    for cdir in chart_dirs:
        chart_xml_name = _resolve_chart_xml_name(cdir)
        if not chart_xml_name:
            print(f'[{page_dir.name}] 未解析 chart XML 名：{cdir}')
            continue
        chart_xml_path = charts_root / chart_xml_name
        chart_type = _detect_chart_type(chart_xml_path)
        embed_name = _chart_to_embed_name(tpl_dir, chart_xml_name) or f'{Path(chart_xml_name).stem}.bin'
        new_xlsx_name = _new_embed_xlsx_name(embed_name)
        wb = wb_map.get(new_xlsx_name)
        if wb is None:
            wb = Workbook()
            # openpyxl 默认有一个空 sheet，后续按需替换
            wb_map[new_xlsx_name] = wb
            sheet_count[new_xlsx_name] = 0

        # 加载 JSON
        src_name, obj = _load_chart_json(cdir)
        # 构造 sheet 名：chartN 或 chartN(final)
        idx = sheet_count[new_xlsx_name]
        sheet_title = f'{cdir.name}'
        if src_name == 'final_data.json':
            sheet_title = f'{cdir.name}-final'
        if idx == 0:
            ws = wb.active
            # 重命名首个默认 Sheet
            ws.title = sheet_title[:31]
        else:
            ws = wb.create_sheet(title=sheet_title[:31])
        sheet_count[new_xlsx_name] = idx + 1

        # 写入不同图类型数据
        if chart_type in ('barChart', 'pieChart', 'areaChart', 'doughnutChart'):
            labels = []
            series = []
            if isinstance(obj, dict):
                labels = obj.get('labels') or []  # type: ignore
                series = obj.get('series') or []  # type: ignore
            if not isinstance(labels, list):
                labels = []
            if not isinstance(series, list):
                series = []
            _write_sheet_for_category(ws, labels, series, ws.title)
        elif chart_type in ('lineChart', 'scatterChart'):
            ser = []
            if isinstance(obj, dict):
                # 兼容多形：scatter_series 字段或直接数组
                arr = obj.get('scatter_series')
                if isinstance(arr, list):
                    ser = arr  # type: ignore
                elif 'series' in obj and isinstance(obj.get('series'), list):
                    # 少数约定也可能用 series 表示趋势序列
                    ser = obj.get('series')  # type: ignore
            _write_sheet_for_scatter(ws, ser, ws.title)
        else:
            # 未知类型：尽量写入原始对象的 JSON 文本供人工查看
            ws.title = (ws.title or cdir.name)[:31]
            ws.append(['raw_json'])
            ws.append([json.dumps(obj, ensure_ascii=False)])

    # 保存所有工作簿
    count = 0
    for new_name, wb in wb_map.items():
        out_path = snapshots_root / new_name
        wb.save(str(out_path))
        count += 1
        print(f'[{page_dir.name}] 快照写入：{out_path}')
    return count


def _zip_template_dir(tpl_dir: Path, out_pptx: Path) -> None:
    """将微模板目录打包为 pptx 文件（用于离线预览）。"""
    import zipfile
    out_pptx.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out_pptx, 'w') as z:
        for p in tpl_dir.rglob('*'):
            if p.is_dir():
                continue
            z.write(p, str(p.relative_to(tpl_dir)))


def main() -> int:
    ap = argparse.ArgumentParser(description='批量生成页面微模板并写入 embeddings 的 .xlsx（新数据快照）')
    ap.add_argument('--pages', nargs='*', help='指定页面（如 p8 p10 p24），缺省为 charts/pXX 全量')
    ap.add_argument('--skip-make-data', action='store_true', help='跳过执行每页 make_data.py（默认执行）')
    ap.add_argument('--zip-preview', action='store_true', help='打包 charts/pXX/template 为 charts/pXX/output/pXX.template.pptx')
    args = ap.parse_args()

    repo_root = _find_repo_root(Path(__file__).resolve().parent)
    charts_root = repo_root / 'charts'

    # 收集页面目录
    pages: List[Path] = []
    if args.pages:
        for n in args.pages:
            p = charts_root / n
            if p.exists() and p.is_dir() and p.name.startswith('p'):
                pages.append(p)
    else:
        for p in sorted(charts_root.glob('p*')):
            if p.is_dir():
                pages.append(p)

    if not pages:
        print('[batch-micro-template] 未发现页面目录，退出。')
        return 1

    total_tpl = 0
    total_xlsx = 0
    for pd in pages:
        try:
            if not args.skip_make_data:
                _ensure_make_data(pd)
        except Exception as e:
            # make_data 非致命错误，继续后续流程
            print(f'[{pd.name}] make_data 执行失败：{e}')

        if HAVE_MAKE_MICRO:
            try:
                # 生成微模板（严格按 UNZIPPED 的样式与关系）
                unz_root = None  # 由 make_micro_template 内部解析 config.yaml 决定
                make_micro_template_for_page(pd, repo_root, repo_root / "input/LRTBH-unzip")
                total_tpl += 1
            except Exception as e:
                print(f'[{pd.name}] 微模板生成失败：{e}')
                # 即便生成失败，仍尝试进行 .xlsb 修正与快照（若已有模板目录）
        else:
            print(f'[{pd.name}] 微模板生成工具缺失，跳过生成，仅尝试 .xlsb 修正与快照')

        try:
            # 生成后强制统一为 .xlsb 嵌入，并修正关系
            fixed = _enforce_xlsb_embeddings(pd, repo_root / "input/LRTBH-unzip", repo_root)
            if fixed > 0:
                print(f'[{pd.name}] 已修正 {fixed} 个关系为 .xlsb，并补齐缺失嵌入')
        except Exception as e:
            print(f'[{pd.name}] .xlsb 强制修正失败：{e}')

        try:
            # 写入 embeddings 的 .xlsx（新数据快照）
            count = _generate_xlsx_for_page(pd)
            total_xlsx += count
        except Exception as e:
            print(f'[{pd.name}] 生成 xlsx 失败：{e}')

        if args.zip_preview:
            try:
                out_dir = pd / 'output'
                out_dir.mkdir(parents=True, exist_ok=True)
                out_pptx = out_dir / f'{pd.name}.template.pptx'
                _zip_template_dir(pd / 'template', out_pptx)
                print(f'[{pd.name}] 预览已打包：{out_pptx}')
            except Exception as e:
                print(f'[{pd.name}] 打包预览失败：{e}')

    print(f'[batch-micro-template] 完成：微模板 {total_tpl} 页，生成 xlsx {total_xlsx} 个。')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())