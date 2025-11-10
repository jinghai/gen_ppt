#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P10 PPT填充脚本 - 从Excel数据填充PPT模板生成最终PPT
基于页面级配置，独立运行，支持完整的PPT数据嵌入
"""

import os
import sys
import yaml
import logging
import pandas as pd
from openpyxl import Workbook
import shutil
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

class P10PPTFiller:
    """P10 PPT填充器"""
    
    def __init__(self, config_path="config.yaml"):
        """初始化PPT填充器"""
        self.config_path = config_path
        self.config = self._load_config()
        self._setup_logging()
        self.logger = logging.getLogger(__name__)
        
        # 设置工作目录
        self.tmp_dir = Path(self.config['project']['tmp_dir'])
        self.output_dir = Path(self.config['project']['output_dir'])
        self.template_file = Path(self.config['project']['template_file'])
        
    def _load_config(self):
        """加载页面级配置文件"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"错误：无法加载配置文件 {self.config_path}: {e}")
            sys.exit(1)
            
    def _setup_logging(self):
        """设置日志配置"""
        log_config = self.config.get('logging', {})
        # 统一日志输出到 charts/p10/logs，并确保目录存在
        # 若配置提供绝对/相对路径，优先使用配置；否则默认 logs/build.log
        log_file = log_config.get('file', 'logs/build.log')
        log_path = Path(log_file)
        try:
            # 创建父目录（避免因目录不存在导致日志写入失败）
            if log_path.parent and str(log_path.parent) != '.':
                log_path.parent.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            # 严格报错：不做兜底，避免掩盖日志问题
            raise RuntimeError(f"创建日志目录失败: {log_path.parent} -> {e}")

        logging.basicConfig(
            level=getattr(logging, log_config.get('level', 'INFO')),
            format=log_config.get('format', '%(asctime)s - %(levelname)s - %(message)s'),
            handlers=[
                logging.FileHandler(str(log_path), encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        
    def _prepare_directories(self):
        """准备工作目录"""
        # 清理并创建临时目录
        if self.tmp_dir.exists():
            shutil.rmtree(self.tmp_dir)
        self.tmp_dir.mkdir(parents=True, exist_ok=True)
        
        # 创建输出目录
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.logger.info(f"工作目录已准备: {self.tmp_dir}")
        
    def _extract_ppt_template(self):
        """解压PPT模板到临时目录"""
        if not self.template_file.exists():
            raise FileNotFoundError(f"PPT模板文件不存在: {self.template_file}")
            
        extracted_dir = self.tmp_dir / "ppt_extracted"
        
        try:
            with zipfile.ZipFile(self.template_file, 'r') as zip_ref:
                zip_ref.extractall(extracted_dir)
            
            self.logger.info(f"PPT模板已解压到: {extracted_dir}")
            return extracted_dir
            
        except Exception as e:
            self.logger.error(f"解压PPT模板失败: {e}")
            raise
            
    def _load_excel_data(self):
        """加载Excel数据"""
        excel_file = Path(self.config['output']['excel_file'])
        if not excel_file.exists():
            raise FileNotFoundError(f"Excel数据文件不存在: {excel_file}")
            
        try:
            # 读取饼图数据
            pie_sheet = self.config['charts']['pie_chart']['sheet_name']
            pie_df = pd.read_excel(excel_file, sheet_name=pie_sheet)
            
            # 读取折线图数据
            line_sheet = self.config['charts']['line_chart']['sheet_name']
            line_df = pd.read_excel(excel_file, sheet_name=line_sheet)
            
            self.logger.info(f"Excel数据加载成功: 饼图 {len(pie_df)} 行, 折线图 {len(line_df)} 行")
            return pie_df, line_df
            
        except Exception as e:
            self.logger.error(f"加载Excel数据失败: {e}")
            raise
            
    def _create_embedded_workbook(self, pie_df, line_df, extracted_dir):
        """创建嵌入式工作簿文件
        - 写入饼图数据到 `PieData`
        - 写入折线/散点图数据到 `LineData`（系列顺序以模板为准，不依赖配置）
        - 为散点图增加数值型 X 轴列（便于公式绑定）：X = axis_day_base + 序号
        注意：保持对现有模板的兼容，不移除原有 Date 列；列顺序为 [X, Date(如存在), <模板系列顺序>]
        """
        # 创建嵌入对象目录
        embeddings_dir = extracted_dir / "ppt" / "embeddings"
        embeddings_dir.mkdir(parents=True, exist_ok=True)
        
        # 生成工作簿文件名
        workbook_file = embeddings_dir / "Microsoft_Excel_Worksheet1.xlsx"
        
        try:
            # 若存在旧文件，先删除以确保创建全新工作簿（避免继承隐藏工作表状态）
            if workbook_file.exists():
                workbook_file.unlink()
            # 解析模板图表文件以获取饼图类别顺序与折线/散点系列顺序
            replace_charts = list(self.config['output']['replace_charts'])
            chart_bases = [c.replace('.xml', '') for c in replace_charts]

            def _detect_type(base: str) -> str:
                    chart_xml = extracted_dir / 'ppt' / 'charts' / f'{base}.xml'
                    if not chart_xml.exists():
                        raise FileNotFoundError(f"图表XML不存在: {chart_xml}")
                    txt = chart_xml.read_text(encoding='utf-8')
                    if 'pieChart' in txt:
                        return 'pie'
                    if 'scatterChart' in txt:
                        return 'scatter'
                    if 'lineChart' in txt:
                        return 'line'
                    raise RuntimeError(f"无法识别图表类型: {chart_xml}")

            def _read_pie_labels(base: str) -> list:
                    chart_xml = extracted_dir / 'ppt' / 'charts' / f'{base}.xml'
                    tree = ET.parse(chart_xml)
                    root = tree.getroot()
                    ns = {'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart'}
                    ser = root.find('.//c:pieChart//c:ser', ns)
                    if ser is None:
                        raise RuntimeError('模板饼图缺少数据系列 c:ser')

                    # 优先：字符串引用的缓存
                    str_cache = ser.find('.//c:cat//c:strRef//c:strCache', ns)
                    if str_cache is not None:
                        labels = []
                        for pt in str_cache.findall('.//c:pt', ns):
                            v = pt.find('.//c:v', ns)
                            if v is None or not v.text:
                                raise RuntimeError('模板饼图类别点缺少值 c:v')
                            labels.append(v.text)
                        if not labels:
                            raise RuntimeError('模板饼图类别标签为空')
                        return labels

                    # 其次：字符串字面量
                    str_lit = ser.find('.//c:cat//c:strLit', ns)
                    if str_lit is not None:
                        labels = []
                        for pt in str_lit.findall('.//c:pt', ns):
                            v = pt.find('.//c:v', ns)
                            if v is None or v.text is None:
                                raise RuntimeError('模板饼图字面类别点缺少值 c:v')
                            labels.append(v.text)
                        if labels:
                            return labels

                    # 再次：数字引用或字面量（极少见），转为字符串
                    num_cache = ser.find('.//c:cat//c:numRef//c:numCache', ns)
                    if num_cache is not None:
                        labels = []
                        for pt in num_cache.findall('.//c:pt', ns):
                            v = pt.find('.//c:v', ns)
                            if v is None or v.text is None:
                                raise RuntimeError('模板饼图数值类别点缺少值 c:v')
                            labels.append(str(v.text))
                        if labels:
                            return labels
                    num_lit = ser.find('.//c:cat//c:numLit', ns)
                    if num_lit is not None:
                        labels = []
                        for pt in num_lit.findall('.//c:pt', ns):
                            v = pt.find('.//c:v', ns)
                            if v is None or v.text is None:
                                raise RuntimeError('模板饼图数值字面类别点缺少值 c:v')
                            labels.append(str(v.text))
                        if labels:
                            return labels

                    # 若上述均不存在，无法从模板解析类别顺序
                    # 尝试读取 dPt 上的文本（部分模板将自定义标签写在数据点上）
                    a_ns = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
                    dpt_nodes = ser.findall('.//c:dPt', ns)
                    if dpt_nodes:
                        indexed = []
                        for dpt in dpt_nodes:
                            idx_node = dpt.find('.//c:idx', ns)
                            if idx_node is None or not idx_node.get('val'):
                                # 若数据点缺少索引，严格报错
                                raise RuntimeError('模板饼图数据点缺少索引 c:idx')
                            idx = int(idx_node.get('val'))
                            # 寻找 dPt 文本
                            txt = None
                            # c:tx/c:rich 或 c:tx/c:strRef/c:strCache
                            tx_rich = dpt.find('.//c:tx//c:rich', ns)
                            if tx_rich is not None:
                                # 提取 a:t 文本（可能存在多个段落）
                                texts = []
                                for t in tx_rich.findall('.//a:t', a_ns):
                                    if t.text:
                                        texts.append(t.text)
                                if texts:
                                    txt = ''.join(texts)
                            if txt is None:
                                tx_cache = dpt.find('.//c:tx//c:strRef//c:strCache', ns)
                                if tx_cache is not None:
                                    pt = tx_cache.find('.//c:pt', ns)
                                    v = pt.find('.//c:v', ns) if pt is not None else None
                                    if v is not None and v.text:
                                        txt = v.text
                            indexed.append((idx, txt))
                        # 按 idx 排序，收集非空文本作为标签
                        indexed.sort(key=lambda x: x[0])
                        labels = [t for _, t in indexed if t]
                        if labels:
                            return labels

                    raise RuntimeError('模板饼图缺少类别定义（未找到 c:strRef/c:strCache、c:strLit、c:numRef/c:numCache 或 dPt 文本）')

            def _read_pie_labels_by_dpt_color(base: str) -> list:
                    """
                    当模板缺少 c:cat 时，按 dPt 颜色顺序识别标签并返回顺序列表。
                    中文注释：严格依据颜色映射识别，若颜色无法识别将报错，不做兜底。
                    """
                    chart_xml = extracted_dir / 'ppt' / 'charts' / f'{base}.xml'
                    tree = ET.parse(chart_xml)
                    root = tree.getroot()
                    ns = {
                        'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart',
                        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
                    }
                    ser = root.find('.//c:pieChart//c:ser', ns)
                    if ser is None:
                        raise RuntimeError('模板饼图缺少数据系列 c:ser')
                    dpts = ser.findall('.//c:dPt', ns)
                    if not dpts:
                        raise RuntimeError('模板饼图未包含 c:dPt 颜色节点，无法识别顺序')
                    # 颜色到标签的严格映射（与 _update_pie_chart_xml 保持一致）
                    color_to_label = {
                        '009FA9': 'Positive',  # 青色
                        '00AFA9': 'Positive',
                        '10B0AA': 'Positive',
                        'D81159': 'Negative',  # 品红
                        'F0005B': 'Negative',
                        'FEC000': 'Neutral',   # 黄色（饼图）
                        'FFBC42': 'Neutral',   # 黄色（折线/散点模板）
                    }
                    indexed = []
                    for dpt in dpts:
                        idx_elem = dpt.find('.//c:idx', ns)
                        if idx_elem is None or not idx_elem.get('val'):
                            raise RuntimeError('模板饼图在 dPt 上缺少索引 c:idx')
                        idx = int(idx_elem.get('val'))
                        srgb = dpt.find('.//a:srgbClr', ns)
                        color_hex = srgb.get('val') if srgb is not None else None
                        if not color_hex:
                            raise RuntimeError('模板饼图在 dPt 上缺少颜色 a:srgbClr@val')
                        label = color_to_label.get(color_hex.upper())
                        if not label:
                            raise RuntimeError(f'无法依据颜色映射识别标签: {color_hex}')
                        indexed.append((idx, label))
                    # 按 idx 排序后返回标签顺序
                    indexed.sort(key=lambda x: x[0])
                    return [lbl for _, lbl in indexed]

            def _read_series_labels(base: str, kind: str) -> list:
                    chart_xml = extracted_dir / 'ppt' / 'charts' / f'{base}.xml'
                    tree = ET.parse(chart_xml)
                    root = tree.getroot()
                    ns = {'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart'}
                    node = root.find('.//c:scatterChart', ns) if kind == 'scatter' else root.find('.//c:lineChart', ns)
                    if node is None:
                        raise RuntimeError(f"未找到 {kind} 图元素")
                    labels = []
                    for ser in node.findall('.//c:ser', ns):
                        tx_v = ser.find('.//c:tx//c:v', ns)
                        if tx_v is not None and tx_v.text:
                            labels.append(tx_v.text)
                            continue
                        str_cache = ser.find('.//c:tx//c:strRef//c:strCache', ns)
                        if str_cache is None:
                            raise RuntimeError('系列缺少名称 c:tx/c:v 或 c:tx/c:strRef/c:strCache')
                        pt = str_cache.find('.//c:pt', ns)
                        v = pt.find('.//c:v', ns) if pt is not None else None
                        if v is None or not v.text:
                            raise RuntimeError('系列名称缓存缺少值 c:v')
                        labels.append(v.text)
                    if not labels:
                        raise RuntimeError('模板未定义任何系列标签')
                    return labels

            pie_base = None
            series_base = None
            series_kind = None
            for base in chart_bases:
                t = _detect_type(base)
                if t == 'pie':
                    pie_base = base
                elif t == 'scatter' and series_base is None:
                    series_base = base
                    series_kind = 'scatter'
                elif t == 'line' and series_base is None:
                    series_base = base
                    series_kind = 'line'
            if pie_base is None:
                raise RuntimeError('未在 replace_charts 中发现饼图')
            if series_base is None:
                raise RuntimeError('未在 replace_charts 中发现散点或折线图用于确定系列顺序')

            # 尝试读取饼图类别标签；若模板仅包含公式但无缓存/字面量，则改为按 dPt 颜色顺序重排
            try:
                pie_labels = _read_pie_labels(pie_base)
            except RuntimeError as e:
                msg = str(e)
                if '模板饼图缺少类别' in msg:
                    # 按 dPt 颜色顺序解析标签
                    self.logger.info(f"模板饼图类别缺失，按 dPt 颜色顺序重排 PieData：{msg}")
                    pie_labels = _read_pie_labels_by_dpt_color(pie_base)
                else:
                    raise
            # 读取系列标签；若无法解析（如仅存在公式、无缓存），退化为按系列数量驱动
            try:
                series_labels = _read_series_labels(series_base, series_kind)
            except RuntimeError as e:
                msg = str(e)
                if '系列缺少名称' in msg or '未找到' in msg:
                    self.logger.info(f"模板{series_kind}图系列名称不可解析，按系列数量驱动：{msg}")
                    # 直接统计系列数量
                    chart_xml = extracted_dir / 'ppt' / 'charts' / f'{series_base}.xml'
                    t = ET.parse(chart_xml)
                    r = t.getroot()
                    ns = {'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart'}
                    node = r.find('.//c:scatterChart', ns) if series_kind == 'scatter' else r.find('.//c:lineChart', ns)
                    if node is None:
                        raise RuntimeError(f"未找到 {series_kind} 图元素以统计系列数量")
                    series_labels = [None] * len(node.findall('.//c:ser', ns))
                else:
                    raise

            # 写入饼图数据（按模板类别顺序重排）
            if 'Sentiment' not in pie_df.columns or 'Percentage' not in pie_df.columns:
                raise RuntimeError('PieData 缺少必需列 Sentiment/Percentage')
            if pie_labels is not None:
                # 中文注释：严格校验标签集合一致性，再按顺序重排以与模板 dPt 顺序对齐，避免编辑图表时 Excel 重新绑定导致颜色-数值错位。
                if sorted(list(pie_df['Sentiment'])) != sorted(pie_labels):
                    raise RuntimeError(f'PieData 情绪标签与模板不一致: {list(pie_df["Sentiment"]) } vs {pie_labels}')
                ordered_rows = []
                for lbl in pie_labels:
                    match = pie_df[pie_df['Sentiment'] == lbl]
                    if match.empty:
                        raise RuntimeError(f'PieData 缺少情绪标签: {lbl}')
                    ordered_rows.append(match.iloc[0])
                ordered_pie_df = pd.DataFrame(ordered_rows)
            else:
                # 正常情况不会进入此分支；保留以兼容极端模板（没有类别且无法识别颜色）。
                ordered_pie_df = pie_df.copy()

            # 统计所有相关图表的系列数量，确保 LineData 列覆盖最大系列数
            def _count_series(base: str, kind: str) -> int:
                chart_xml = extracted_dir / 'ppt' / 'charts' / f'{base}.xml'
                t = ET.parse(chart_xml)
                r = t.getroot()
                ns = {'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart'}
                node = r.find('.//c:scatterChart', ns) if kind == 'scatter' else r.find('.//c:lineChart', ns)
                if node is None:
                    return 0
                return len(node.findall('.//c:ser', ns))

            scatter_counts = []
            line_counts = []
            for base in chart_bases:
                t = _detect_type(base)
                if t == 'scatter':
                    scatter_counts.append(_count_series(base, 'scatter'))
                elif t == 'line':
                    line_counts.append(_count_series(base, 'line'))
            expected_series_count = max(scatter_counts + line_counts) if (scatter_counts or line_counts) else 0
            if expected_series_count == 0:
                raise RuntimeError('未能统计到任何折线或散点系列数量')
            self.logger.info(
                f"系列数量统计 -> scatter:{scatter_counts} line:{line_counts} 期望最大系列数:{expected_series_count}"
            )

            # 写入折线/散点图数据：构造包含数值 X 轴的工作表（系列顺序以模板为准）
            base = int(self.config.get('fill_policy', {}).get('axis_day_base', 20300))
            count = len(line_df)
            x_values = [base + i for i in range(count)]
            new_cols = {'X': x_values}
            if 'Date' in line_df.columns:
                new_cols['Date'] = list(line_df['Date'])
            # 根据系列标签或数量构造数值列
            value_cols = [c for c in line_df.columns if c != 'Date']
            self.logger.info(
                f"LineData 可用值列数:{len(value_cols)} 列名:{value_cols}"
            )
            if len(value_cols) < expected_series_count:
                raise RuntimeError(
                    f'LineData 列数量不足，期望系列数 {expected_series_count} 实际可用数值列 {len(value_cols)}'
                )
            # 若模板系列名称可解析，则必须与期望系列数一致，否则严格报错
            if all(lbl is not None for lbl in series_labels):
                if len(series_labels) != expected_series_count:
                    raise RuntimeError(
                        f'模板系列数量({len(series_labels)})与最大期望系列数({expected_series_count})不一致'
                    )
                for col in series_labels:
                    if col not in line_df.columns:
                        raise RuntimeError(f'LineData 缺少必需列: {col}（模板系列）')
                    new_cols[col] = list(line_df[col])
            else:
                # 按列顺序选取前 expected_series_count 个数值列
                for i in range(expected_series_count):
                    col = value_cols[i]
                    new_cols[col] = list(line_df[col])
            new_line_df = pd.DataFrame(new_cols)

            # 使用 openpyxl 直接写入，显式控制工作表可见性
            wb = Workbook()
            # 饼图数据表
            ws_pie = wb.active
            ws_pie.title = 'PieData'
            ws_pie.sheet_state = 'visible'
            # 写表头
            ws_pie.append(list(ordered_pie_df.columns))
            # 写数据行
            for row in ordered_pie_df.itertuples(index=False):
                ws_pie.append(list(row))

            # 折线/散点数据表
            ws_line = wb.create_sheet('LineData')
            ws_line.sheet_state = 'visible'
            ws_line.append(list(new_line_df.columns))
            for row in new_line_df.itertuples(index=False):
                ws_line.append(list(row))

            # 校验至少一个可见工作表
            if not any(w.sheet_state == 'visible' for w in wb.worksheets):
                raise RuntimeError('嵌入工作簿不包含可见工作表')

            # 将默认活动工作表设置为 LineData，便于在 PowerPoint 中编辑右侧图形时直接定位到对应数据
            try:
                wb.active = wb.worksheets.index(ws_line)
            except Exception as e:
                raise RuntimeError(f'设置工作簿活动表失败: {e}')

            # 保存工作簿
            wb.save(workbook_file)
                
            self.logger.info(f"嵌入式工作簿已创建: {workbook_file}")
            return workbook_file
            
        except Exception as e:
            self.logger.error(f"创建嵌入式工作簿失败: {e}")
            raise

    def _update_content_types(self, extracted_dir: Path, workbook_path: Path):
        """更新 [Content_Types].xml 以声明嵌入的 xlsx 工作簿
        - 添加 Default 映射：xlsx -> application/vnd.openxmlformats-officedocument.spreadsheetml.sheet（若缺失）
        - 移除 embeddings 下旧的 .xlsb 覆盖项（避免冲突）
        - 添加 embeddings/{workbook}.xlsx 的 Override 覆盖项（若缺失）
        严格错误策略：缺少 Content_Types.xml 时直接抛错。
        """
        ct_file = extracted_dir / '[Content_Types].xml'
        if not ct_file.exists():
            raise FileNotFoundError(f"缺少 Content_Types.xml: {ct_file}")

        try:
            tree = ET.parse(ct_file)
            root = tree.getroot()
            ns_ct = 'http://schemas.openxmlformats.org/package/2006/content-types'

            # 1) Default 映射检查/添加
            has_default_xlsx = any(
                (d.get('Extension') == 'xlsx')
                for d in root.findall(f'{{{ns_ct}}}Default')
            )
            if not has_default_xlsx:
                ET.SubElement(
                    root,
                    f'{{{ns_ct}}}Default',
                    Extension='xlsx',
                    ContentType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )

            # 2) 清理 embeddings 下旧 .xlsb 覆盖项
            for o in list(root.findall(f'{{{ns_ct}}}Override')):
                part = o.get('PartName') or ''
                if part.startswith('/ppt/embeddings/') and part.endswith('.xlsb'):
                    root.remove(o)

            # 3) 添加当前 xlsx 覆盖项（若不存在）
            target_part = f'/ppt/embeddings/{workbook_path.name}'
            has_xlsx_override = any(
                (o.get('PartName') == target_part)
                for o in root.findall(f'{{{ns_ct}}}Override')
            )
            if not has_xlsx_override:
                ET.SubElement(
                    root,
                    f'{{{ns_ct}}}Override',
                    PartName=target_part,
                    ContentType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )

            tree.write(ct_file, encoding='utf-8', xml_declaration=True)
            self.logger.info('Content_Types.xml 已更新')
        except Exception as e:
            self.logger.error(f'更新 Content_Types 失败: {e}')
            raise
            
    def _update_chart_data_xml(self, extracted_dir, chart_name, data_df, chart_type="pie"):
        """更新图表数据XML"""
        chart_file = extracted_dir / "ppt" / "charts" / f"{chart_name}.xml"
        
        if not chart_file.exists():
            self.logger.warning(f"图表文件不存在: {chart_file}")
            return False
            
        try:
            # 解析XML
            tree = ET.parse(chart_file)
            root = tree.getroot()
            
            # 定义命名空间
            namespaces = {
                'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart',
                'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'
            }
            
            if chart_type == "pie":
                self._update_pie_chart_xml(root, data_df, namespaces)
            elif chart_type == "line":
                self._update_line_chart_xml(root, data_df, namespaces)
                
            # 保存更新后的XML
            tree.write(chart_file, encoding='utf-8', xml_declaration=True)
            self.logger.info(f"图表数据已更新: {chart_file}")
            return True
            
        except Exception as e:
            self.logger.error(f"更新图表XML失败 {chart_file}: {e}")
            return False
            
    def _update_pie_chart_xml(self, root, pie_df, namespaces):
        """更新饼图XML数据"""
        # 查找饼图数据系列
        pie_chart = root.find('.//c:pieChart', namespaces)
        if pie_chart is None:
            self.logger.warning("未找到饼图元素")
            return
            
        # 查找数据系列
        ser = pie_chart.find('.//c:ser', namespaces)
        if ser is None:
            self.logger.warning("未找到饼图数据系列")
            return
            
        # 更新颜色配置
        self._update_pie_chart_colors(ser, namespaces)
            
        # 更新类别与数值（严格以模板 dPt 索引顺序为准，确保颜色与数据对应）
        cat = ser.find('.//c:cat', namespaces)
        cat_missing = cat is None
        dpts = ser.findall('.//c:dPt', namespaces)
        if not dpts:
            raise RuntimeError("模板饼图未包含 c:dPt 颜色节点，无法确定点顺序")
        # 收集 dPt 的索引顺序
        dpt_order = []
        for dpt in dpts:
            idx_elem = dpt.find('.//c:idx', namespaces)
            if idx_elem is None or not idx_elem.get('val'):
                raise RuntimeError('模板饼图数据点缺少索引 c:idx')
            dpt_order.append(int(idx_elem.get('val')))
        dpt_order_sorted = sorted(dpt_order)
        # 构建 idx->标签 的映射：优先使用 c:cat/c:strCache；若类别节点缺失，则从 dPt 文本读取
        idx_to_label = {}
        str_cache = None
        if not cat_missing:
            str_ref = cat.find('.//c:strRef', namespaces)
            if str_ref is None:
                raise RuntimeError('模板饼图缺少类别引用 c:cat/c:strRef')
            str_cache = str_ref.find('.//c:strCache', namespaces)
            if str_cache is None:
                raise RuntimeError('模板饼图缺少类别缓存 c:cat/c:strRef/c:strCache')
            for pt in str_cache.findall('.//c:pt', namespaces):
                idx_attr = pt.get('idx')
                v = pt.find('.//c:v', namespaces)
                if idx_attr is None or v is None or not v.text:
                    raise RuntimeError('模板饼图类别缓存点缺少 idx 或值 c:v')
                idx_to_label[int(idx_attr)] = v.text
        else:
            # 无 c:cat 时读取标签：优先 dPt 文本，其次按颜色映射识别标签
            color_to_label = {
                '009FA9': 'Positive',  # 绿色/青色
                '00AFA9': 'Positive',  # 容错近似
                '10B0AA': 'Positive',  # 容错近似
                'D81159': 'Negative',  # 品红
                'F0005B': 'Negative',  # 容错近似
                'FEC000': 'Neutral',   # 黄色（饼图）
                'FFBC42': 'Neutral',   # 黄色（折线图/散点模板）
            }
            for dpt in dpts:
                idx_elem = dpt.find('.//c:idx', namespaces)
                if idx_elem is None or not idx_elem.get('val'):
                    raise RuntimeError('模板饼图在 dPt 上缺少索引 c:idx')
                idx = int(idx_elem.get('val'))
                # 先尝试 dPt/tx 文本
                tx_text = None
                t_nodes = dpt.findall('.//c:tx//a:t', namespaces)
                if t_nodes:
                    tx_text = ''.join([t.text or '' for t in t_nodes]).strip()
                if tx_text:
                    idx_to_label[idx] = tx_text
                    continue
                # 再尝试按颜色识别标签
                srgb = dpt.find('.//a:srgbClr', namespaces)
                color_hex = srgb.get('val') if srgb is not None else None
                if not color_hex:
                    raise RuntimeError('模板饼图在 dPt 上缺少颜色 a:srgbClr@val，无法识别标签')
                mapped_label = color_to_label.get(color_hex.upper())
                if not mapped_label:
                    raise RuntimeError(f'无法依据颜色映射识别标签: {color_hex}')
                idx_to_label[idx] = mapped_label
        # 构造按 dPt 顺序的行
        ordered_rows = []
        ordered_labels = []
        for idx in dpt_order_sorted:
            lbl = idx_to_label.get(idx)
            if not lbl:
                raise RuntimeError(f'模板饼图在 idx={idx} 找不到类别标签')
            match = pie_df[pie_df['Sentiment'] == lbl]
            if match.empty:
                raise RuntimeError(f'PieData 缺少标签: {lbl}')
            ordered_rows.append(match.iloc[0])
            ordered_labels.append(lbl)
        # 用按颜色顺序重排后的数据替换
        pie_df = pd.DataFrame(ordered_rows)
        # 写回类别缓存（仅在存在 c:cat 时更新；若无 c:cat 则保留模板既有标签来源）
        if str_cache is not None:
            for pt in list(str_cache.findall('.//c:pt', namespaces)):
                str_cache.remove(pt)
            for idx, lbl in zip(dpt_order_sorted, ordered_labels):
                pt = ET.SubElement(str_cache, '{http://schemas.openxmlformats.org/drawingml/2006/chart}pt')
                pt.set('idx', str(idx))
                v = ET.SubElement(pt, '{http://schemas.openxmlformats.org/drawingml/2006/chart}v')
                v.text = lbl
                        
        # 更新数值数据
        val = ser.find('.//c:val', namespaces)
        if val is not None:
            num_ref = val.find('.//c:numRef', namespaces)
            if num_ref is not None:
                num_cache = num_ref.find('.//c:numCache', namespaces)
                if num_cache is not None:
                    # 清除现有数据点
                    for pt in list(num_cache.findall('.//c:pt', namespaces)):
                        num_cache.remove(pt)
                    # 添加新数据点（严格按 dPt 索引顺序写入，确保颜色对应）
                    for idx, percentage in zip(dpt_order_sorted, list(pie_df['Percentage'])):
                        pt = ET.SubElement(num_cache, '{http://schemas.openxmlformats.org/drawingml/2006/chart}pt')
                        pt.set('idx', str(idx))
                        v = ET.SubElement(pt, '{http://schemas.openxmlformats.org/drawingml/2006/chart}v')
                        v.text = str(percentage)
                        
    def _update_pie_chart_colors(self, ser, namespaces):
        """更新饼图颜色配置
        - 始终保留模板颜色并严格校验；不依赖也不覆盖为配置颜色。
        - 若模板缺少期望的颜色节点，抛错，不做兜底。
        """
        dpts = ser.findall('.//c:dPt', namespaces)
        if not dpts:
            raise RuntimeError("模板饼图未包含 c:dPt 颜色节点，无法校验颜色")
        a_ns = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
        for dpt in dpts:
            idx_elem = dpt.find('.//c:idx', namespaces)
            idx = idx_elem.get('val') if idx_elem is not None else '?'
            sp_pr = dpt.find('.//c:spPr', namespaces)
            if sp_pr is None:
                raise RuntimeError("模板饼图缺少 c:spPr 节点")
            solid_fill = sp_pr.find(f'.//{a_ns}solidFill')
            if solid_fill is None:
                raise RuntimeError("模板饼图缺少 a:solidFill 节点")
            srgb = solid_fill.find(f'.//{a_ns}srgbClr')
            scheme = solid_fill.find(f'.//{a_ns}schemeClr')
            val = srgb.get('val') if srgb is not None else scheme.get('val') if scheme is not None else None
            if val is None:
                raise RuntimeError("模板饼图颜色节点缺少 srgbClr/schemeClr")
            self.logger.info(f"保留模板饼图颜色: dPt[{idx}] -> {val}")
            # 保持模板颜色，不做任何覆盖
            # 若为 schemeClr，则保持 scheme 方案；若为 srgbClr 则保持具体色值
            # 本处不进行任何写入，以确保模板颜色严格保留。
                        
    def _update_line_chart_xml(self, root, line_df, namespaces):
        """更新折线图XML数据"""
        # 查找折线图
        line_chart = root.find('.//c:lineChart', namespaces)
        if line_chart is None:
            self.logger.warning("未找到折线图元素")
            return
            
        # 获取所有数据系列
        series_list = line_chart.findall('.//c:ser', namespaces)
        # 从模板读取系列标签顺序，作为数据-颜色的语义绑定依据
        tmpl_labels = []
        for ser in series_list:
            tx_v = ser.find('.//c:tx//c:v', namespaces)
            if tx_v is not None and tx_v.text:
                tmpl_labels.append(tx_v.text)
                continue
            str_cache = ser.find('.//c:tx//c:strRef//c:strCache', namespaces)
            if str_cache is None:
                raise RuntimeError('折线系列缺少名称 c:tx/c:v 或 c:tx/c:strRef/c:strCache')
            pt = str_cache.find('.//c:pt', namespaces)
            v = pt.find('.//c:v', namespaces) if pt is not None else None
            if v is None or not v.text:
                raise RuntimeError('折线系列名称缓存缺少值 c:v')
            tmpl_labels.append(v.text)

        for i, ser in enumerate(series_list):
            if i >= len(tmpl_labels):
                break
            sentiment = tmpl_labels[i]
            if sentiment not in line_df.columns:
                continue
                
            # 更新X轴数据（日期）
            cat = ser.find('.//c:cat', namespaces)
            if cat is not None:
                str_ref = cat.find('.//c:strRef', namespaces)
                if str_ref is not None:
                    str_cache = str_ref.find('.//c:strCache', namespaces)
                    if str_cache is not None:
                        # 清除现有数据点
                        for pt in str_cache.findall('.//c:pt', namespaces):
                            str_cache.remove(pt)
                        
                        # 添加日期数据点
                        for j, date in enumerate(line_df['Date']):
                            pt = ET.SubElement(str_cache, '{http://schemas.openxmlformats.org/drawingml/2006/chart}pt')
                            pt.set('idx', str(j))
                            v = ET.SubElement(pt, '{http://schemas.openxmlformats.org/drawingml/2006/chart}v')
                            v.text = str(date)
                        # 更新点计数
                        pt_count = str_cache.find('.//c:ptCount', namespaces)
                        if pt_count is not None:
                            pt_count.set('val', str(len(line_df['Date'])))
                            
            # 更新Y轴数据（百分比）
            val = ser.find('.//c:val', namespaces)
            if val is not None:
                num_ref = val.find('.//c:numRef', namespaces)
                if num_ref is not None:
                    num_cache = num_ref.find('.//c:numCache', namespaces)
                    if num_cache is not None:
                        # 清除现有数据点
                        for pt in num_cache.findall('.//c:pt', namespaces):
                            num_cache.remove(pt)
                        
                        # 添加百分比数据点
                        for j, percentage in enumerate(line_df[sentiment]):
                            pt = ET.SubElement(num_cache, '{http://schemas.openxmlformats.org/drawingml/2006/chart}pt')
                            pt.set('idx', str(j))
                            v = ET.SubElement(pt, '{http://schemas.openxmlformats.org/drawingml/2006/chart}v')
                            v.text = str(percentage)
                        # 更新点计数
                        pt_count = num_cache.find('.//c:ptCount', namespaces)
                        if pt_count is not None:
                            pt_count.set('val', str(len(line_df[sentiment])))

        # 同步更新折线图系列颜色（保留模板）
        self._update_line_chart_colors(root, namespaces)

    def _update_line_chart_colors(self, root, namespaces):
        """更新折线图系列颜色
        - 始终保留模板颜色并严格校验；不依赖也不覆盖为配置颜色。
        """
        line_chart = root.find('.//c:lineChart', namespaces)
        if line_chart is None:
            raise RuntimeError("未找到折线图元素以更新颜色")
        series_list = line_chart.findall('.//c:ser', namespaces)
        a_ns = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
        # 保留模板颜色：仅校验并记录
        for idx, ser in enumerate(series_list):
            sp_pr = ser.find('.//c:spPr', namespaces)
            if sp_pr is None:
                raise RuntimeError("模板折线系列缺少 c:spPr 节点")
            ln = sp_pr.find(f'.//{a_ns}ln')
            if ln is None:
                raise RuntimeError("模板折线系列缺少 a:ln 节点")
            solid_fill = ln.find(f'.//{a_ns}solidFill')
            if solid_fill is None:
                raise RuntimeError("模板折线系列缺少 a:solidFill 节点")
            srgb = solid_fill.find(f'.//{a_ns}srgbClr')
            scheme = solid_fill.find(f'.//{a_ns}schemeClr')
            val = srgb.get('val') if srgb is not None else scheme.get('val') if scheme is not None else None
            if val is None:
                raise RuntimeError("模板折线系列颜色节点缺少 srgbClr/schemeClr")
            self.logger.info(f"保留模板折线颜色: ser[{idx}] -> {val}")

    # ============================= 图表绑定修复（externalData 与公式） =============================
    def _excel_col_letter(self, idx: int) -> str:
        """将列索引(0基)转换为Excel列字母（A,B,...,Z,AA,...）"""
        if idx < 0:
            raise ValueError("列索引必须为非负")
        letters = []
        idx += 1
        while idx:
            idx, rem = divmod(idx - 1, 26)
            letters.append(chr(65 + rem))
        return ''.join(reversed(letters))

    def _get_workbook_rel_id(self, extracted_dir: Path, chart_base: str) -> str:
        """获取图表与嵌入工作簿的关系ID（rId），严格要求存在"""
        rels_file = extracted_dir / 'ppt' / 'charts' / '_rels' / f'{chart_base}.xml.rels'
        if not rels_file.exists():
            # 模板中可能使用 .rels 文件名不带 .xml（兼容处理，但仍按严格抛错）
            rels_file = extracted_dir / 'ppt' / 'charts' / '_rels' / f'{chart_base}.rels'
        if not rels_file.exists():
            raise FileNotFoundError(f"缺少图表关系文件: {rels_file}")
        tree = ET.parse(rels_file)
        root = tree.getroot()
        ns_pkg = 'http://schemas.openxmlformats.org/package/2006/relationships'
        for rel in root.findall(f'.//{{{ns_pkg}}}Relationship'):
            t = rel.get('Type', '')
            if t.endswith('/relationships/package'):
                rid = rel.get('Id')
                if not rid:
                    raise RuntimeError("关系文件存在 package 关系但缺少 Id")
                return rid
        raise RuntimeError("未找到指向嵌入工作簿的 package 关系")

    def _ensure_external_data(self, extracted_dir: Path, chart_base: str, rid: str):
        """确保图表XML存在 externalData 并启用 autoUpdate=1，r:id 指向嵌入工作簿"""
        chart_file = extracted_dir / 'ppt' / 'charts' / f'{chart_base}.xml'
        if not chart_file.exists():
            raise FileNotFoundError(f"图表XML不存在: {chart_file}")
        tree = ET.parse(chart_file)
        root = tree.getroot()
        ns_c = 'http://schemas.openxmlformats.org/drawingml/2006/chart'
        ns_r = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
        ext = root.find(f'.//{{{ns_c}}}externalData')
        if ext is None:
            # externalData 通常为 chartSpace 的直接子节点
            ext = ET.SubElement(root, f'{{{ns_c}}}externalData')
        ext.set(f'{{{ns_r}}}id', rid)
        # 设置 autoUpdate=1
        auto = ext.find(f'.//{{{ns_c}}}autoUpdate')
        if auto is None:
            auto = ET.SubElement(ext, f'{{{ns_c}}}autoUpdate')
        auto.set('val', '1')
        tree.write(chart_file, encoding='utf-8', xml_declaration=True)
        self.logger.info(f"externalData 已绑定并启用自动更新: {chart_file}")

    def _update_pie_formulas(self, extracted_dir: Path, chart_base: str, pie_df: pd.DataFrame):
        """将饼图的公式 c:f 指向嵌入工作簿 PieData 实际区域
        中文注释：部分模板可能不包含类别公式(c:cat/c:strRef/c:f)，此时仅更新数值公式确保绑定到嵌入工作簿，不做静默兜底。
        """
        chart_file = extracted_dir / 'ppt' / 'charts' / f'{chart_base}.xml'
        tree = ET.parse(chart_file)
        root = tree.getroot()
        ns = {'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart'}
        pie_chart = root.find('.//c:pieChart', ns)
        if pie_chart is None:
            raise RuntimeError("未找到饼图元素以更新公式")
        ser = pie_chart.find('.//c:ser', ns)
        if ser is None:
            raise RuntimeError("未找到饼图数据系列以更新公式")
        n = len(pie_df) + 1  # 含表头，第2行开始
        # 类别公式（可选）：若模板不存在类别公式则记录信息并跳过
        cat_f = ser.find('.//c:cat/c:strRef/c:f', ns)
        if cat_f is not None:
            cat_f.text = f"PieData!$A$2:$A${n}"
        else:
            self.logger.info("模板饼图无 c:cat/c:strRef/c:f，仅更新数值公式以绑定嵌入工作簿")
        # 数值公式
        val_f = ser.find('.//c:val/c:numRef/c:f', ns)
        if val_f is None:
            raise RuntimeError("饼图缺少数值公式 c:val/c:numRef/c:f")
        val_f.text = f"PieData!$B$2:$B${n}"
        ET.ElementTree(root).write(chart_file, encoding='utf-8', xml_declaration=True)
        self.logger.info(f"饼图公式已更新到嵌入工作簿区域: {chart_file}")

    def _update_line_formulas(self, extracted_dir: Path, chart_base: str, line_df: pd.DataFrame):
        """将折线图的公式 c:f 指向嵌入工作簿 LineData 实际区域"""
        chart_file = extracted_dir / 'ppt' / 'charts' / f'{chart_base}.xml'
        tree = ET.parse(chart_file)
        root = tree.getroot()
        ns = {'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart'}
        line_chart = root.find('.//c:lineChart', ns)
        if line_chart is None:
            raise RuntimeError("未找到折线图元素以更新公式")
        series_list = line_chart.findall('.//c:ser', ns)
        # X轴类别公式：若存在 Date 列则使用 Date，否则回退到 X 数值列
        n = len(line_df) + 1
        x_idx = 1 if 'Date' in line_df.columns else 0
        x_col = self._excel_col_letter(x_idx)
        for i, ser in enumerate(series_list):
            # 更新 X 轴公式
            cat_f = ser.find('.//c:cat/c:strRef/c:f', ns)
            if cat_f is None:
                raise RuntimeError("折线图缺少类别公式 c:cat/c:strRef/c:f")
            cat_f.text = f"LineData!${x_col}$2:${x_col}${n}"
            # 更新 Y 轴值公式：若存在 Date 列，则从第3列开始，否则从第2列开始
            y_col = self._excel_col_letter(i + (2 if 'Date' in line_df.columns else 1))
            val_f = ser.find('.//c:val/c:numRef/c:f', ns)
            if val_f is None:
                raise RuntimeError("折线图缺少数值公式 c:val/c:numRef/c:f")
            val_f.text = f"LineData!${y_col}$2:${y_col}${n}"
        ET.ElementTree(root).write(chart_file, encoding='utf-8', xml_declaration=True)
        self.logger.info(f"折线图公式已更新到嵌入工作簿区域: {chart_file}")

    def _update_scatter_formulas(self, extracted_dir: Path, chart_base: str, line_df: pd.DataFrame):
        """将散点图的 xVal/yVal 公式绑定到嵌入工作簿 LineData
        - xVal 指向 X 数值轴列（A列）：LineData!$A$2:$A${n}
        - yVal 按模板系列顺序依次指向对应列（保持与模板一致）
        中文注释：此函数要求 _create_embedded_workbook 写入列顺序为 [X, Date(可选), <模板系列>]
        """
        chart_file = extracted_dir / 'ppt' / 'charts' / f'{chart_base}.xml'
        if not chart_file.exists():
            raise FileNotFoundError(f"图表XML不存在: {chart_file}")
        tree = ET.parse(chart_file)
        root = tree.getroot()
        ns = {'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart'}
        scatter_chart = root.find('.//c:scatterChart', ns)
        if scatter_chart is None:
            raise RuntimeError("未找到散点图元素以更新公式")
        n = len(line_df) + 1
        series_list = scatter_chart.findall('.//c:ser', ns)
        # 列字母映射：X(A)。若存在 Date 列，则 B 为 Date；yVal 从 C 开始按模板顺序对应
        x_col = 'A'
        y_start_idx = 2 if 'Date' in line_df.columns else 1
        for i, ser in enumerate(series_list):
            y_idx = y_start_idx + i
            y_col = self._excel_col_letter(y_idx)
            # 更新 xVal 公式
            x_f = ser.find('.//c:xVal/c:numRef/c:f', ns)
            if x_f is None:
                raise RuntimeError("散点图缺少 xVal 公式 c:xVal/c:numRef/c:f")
            x_f.text = f"LineData!${x_col}$2:${x_col}${n}"
            # 更新 yVal 公式
            y_f = ser.find('.//c:yVal/c:numRef/c:f', ns)
            if y_f is None:
                raise RuntimeError("散点图缺少 yVal 公式 c:yVal/c:numRef/c:f")
            y_f.text = f"LineData!${y_col}$2:${y_col}${n}"
        ET.ElementTree(root).write(chart_file, encoding='utf-8', xml_declaration=True)
        self.logger.info(f"散点图公式已更新到嵌入工作簿区域: {chart_file}")

    def _update_scatter_chart_xml(self, extracted_dir, chart_name, line_df):
        """更新散点图(XML)为每日趋势百分比：X为日索引，Y为百分比"""
        chart_file = extracted_dir / "ppt" / "charts" / f"{chart_name}.xml"
        if not chart_file.exists():
            self.logger.warning(f"散点图文件不存在: {chart_file}")
            return False
        try:
            tree = ET.parse(chart_file)
            root = tree.getroot()
            namespaces = {
                'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart',
                'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'
            }
            scatter_chart = root.find('.//c:scatterChart', namespaces)
            if scatter_chart is None:
                self.logger.warning("未找到散点图元素")
                return False
            # 准备X轴日索引（与 _create_embedded_workbook 保持一致）。
            # 若不存在 Date 列，则严格按行数回退并保持与公式更新一致。
            base = int(self.config.get('fill_policy', {}).get('axis_day_base', 20300))
            length = len(line_df['Date']) if 'Date' in line_df.columns else len(line_df)
            x_values = [base + i for i in range(length)]
            series_list = scatter_chart.findall('.//c:ser', namespaces)
            # 按列索引绑定 Y：源数据 line_df 不含 X，因此若存在 Date，则 Y 从第2列开始，否则从第1列开始。
            y_start_idx = 1 if 'Date' in line_df.columns else 0
            value_cols = [c for c in line_df.columns if c != 'Date']
            if len(series_list) > len(value_cols):
                raise RuntimeError(
                    f"散点系列数({len(series_list)})超过 LineData 可用列({len(value_cols)})"
                )
            for i, ser in enumerate(series_list):
                y_idx = y_start_idx + i
                # 从源数据按列索引读取 Y 序列，类型严格校验为数值
                y_series = line_df.iloc[:, y_idx]
                try:
                    # 若非数值类型将触发异常，避免掩盖错误
                    _ = pd.to_numeric(y_series, errors='raise')
                except Exception:
                    raise TypeError(f"散点系列第{i+1}列数据非数值类型: {line_df.columns[y_idx]}")
                sentiment = line_df.columns[y_idx]
                # 更新X值
                xval = ser.find('.//c:xVal', namespaces)
                if xval is not None:
                    num_ref = xval.find('.//c:numRef', namespaces)
                    if num_ref is not None:
                        num_cache = num_ref.find('.//c:numCache', namespaces)
                        if num_cache is not None:
                            for pt in num_cache.findall('.//c:pt', namespaces):
                                num_cache.remove(pt)
                            for j, xv in enumerate(x_values):
                                pt = ET.SubElement(num_cache, '{http://schemas.openxmlformats.org/drawingml/2006/chart}pt')
                                pt.set('idx', str(j))
                                v = ET.SubElement(pt, '{http://schemas.openxmlformats.org/drawingml/2006/chart}v')
                                v.text = str(xv)
                            pt_count = num_cache.find('.//c:ptCount', namespaces)
                            if pt_count is not None:
                                pt_count.set('val', str(len(x_values)))
                # 更新Y值
                yval = ser.find('.//c:yVal', namespaces)
                if yval is not None:
                    num_ref = yval.find('.//c:numRef', namespaces)
                    if num_ref is not None:
                        num_cache = num_ref.find('.//c:numCache', namespaces)
                        if num_cache is not None:
                            for pt in num_cache.findall('.//c:pt', namespaces):
                                num_cache.remove(pt)
                            for j, yv in enumerate(y_series):
                                pt = ET.SubElement(num_cache, '{http://schemas.openxmlformats.org/drawingml/2006/chart}pt')
                                pt.set('idx', str(j))
                                v = ET.SubElement(pt, '{http://schemas.openxmlformats.org/drawingml/2006/chart}v')
                                v.text = str(yv)
                            pt_count = num_cache.find('.//c:ptCount', namespaces)
                            if pt_count is not None:
                                pt_count.set('val', str(len(y_series)))
                
                # 更新系列颜色（保留模板）
                self._update_scatter_chart_colors(ser, sentiment, namespaces)
            
            tree.write(chart_file, encoding='utf-8', xml_declaration=True)
            self.logger.info(f"散点图数据已更新: {chart_file}")
            return True
        except Exception as e:
            self.logger.error(f"更新散点图XML失败 {chart_file}: {e}")
            return False

    def _update_scatter_chart_colors(self, ser, sentiment, namespaces):
        """更新散点图系列颜色
        - 始终保留模板颜色并严格校验；不依赖也不覆盖为配置颜色。
        """
        a_ns = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
        sp_pr = ser.find('.//c:spPr', namespaces)
        if sp_pr is None:
            raise RuntimeError("模板散点系列缺少 c:spPr 节点")
        # 保留模板颜色：仅校验并记录
        ln = sp_pr.find(f'.//{a_ns}ln')
        solid_fill = sp_pr.find(f'.//{a_ns}solidFill')
        srgb_ln = ln.find(f'.//{a_ns}srgbClr') if ln is not None else None
        srgb_fill = solid_fill.find(f'.//{a_ns}srgbClr') if solid_fill is not None else None
        scheme_ln = ln.find(f'.//{a_ns}schemeClr') if ln is not None else None
        scheme_fill = solid_fill.find(f'.//{a_ns}schemeClr') if solid_fill is not None else None
        val_ln = srgb_ln.get('val') if srgb_ln is not None else scheme_ln.get('val') if scheme_ln is not None else None
        val_fill = srgb_fill.get('val') if srgb_fill is not None else scheme_fill.get('val') if scheme_fill is not None else None
        if val_ln is None and val_fill is None:
            raise RuntimeError("模板散点系列颜色节点缺失 srgbClr/schemeClr")
        self.logger.info(f"保留模板散点颜色: {sentiment} -> ln:{val_ln}, fill:{val_fill}")

    def _update_chart_rels(self, extracted_dir, workbook_path):
        """更新图表关系文件，指向新嵌入工作簿
        严格错误策略：若关系文件缺失则抛出 FileNotFoundError。
        """
        try:
            target = f"../embeddings/{Path(workbook_path).name}"
            rels_dir = extracted_dir / 'ppt' / 'charts' / '_rels'
            for chart_name in self.config['output']['replace_charts']:
                rels_file = rels_dir / f"{chart_name}.rels"
                if not rels_file.exists():
                    raise FileNotFoundError(f"未找到关系文件: {rels_file}")
                try:
                    tree = ET.parse(rels_file)
                    root = tree.getroot()
                    # OOXML package namespace
                    # 默认关系元素无需前缀
                    for rel in root.findall('.//{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
                        t = rel.get('Type', '')
                        if t.endswith('/relationships/package'):
                            rel.set('Target', target)
                    tree.write(rels_file, encoding='utf-8', xml_declaration=True)
                    self.logger.info(f"关系已更新: {rels_file} -> {target}")
                except Exception as e:
                    self.logger.error(f"更新关系失败 {rels_file}: {e}")
                    raise
            return True
        except Exception as e:
            self.logger.error(f"更新图表关系失败: {e}")
            return False
                            
    def _repackage_ppt(self, extracted_dir):
        """重新打包PPT文件"""
        output_file = self.output_dir / self.config['output']['final_ppt']
        
        try:
            with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
                for root, dirs, files in os.walk(extracted_dir):
                    for file in files:
                        file_path = Path(root) / file
                        arc_name = file_path.relative_to(extracted_dir)
                        zip_ref.write(file_path, arc_name)
                        
            self.logger.info(f"PPT文件已重新打包: {output_file}")
            return output_file
            
        except Exception as e:
            self.logger.error(f"重新打包PPT失败: {e}")
            raise
            
    def run(self):
        """执行完整的PPT填充流程"""
        try:
            self.logger.info("=== P10 PPT填充开始 ===")
            
            # 1. 准备工作目录
            self._prepare_directories()
            
            # 2. 解压PPT模板
            extracted_dir = self._extract_ppt_template()
            
            # 3. 加载Excel数据
            pie_df, line_df = self._load_excel_data()
            
            # 4. 创建嵌入式工作簿
            workbook_path = self._create_embedded_workbook(pie_df, line_df, extracted_dir)

            # 4.1 更新关系文件到新工作簿（保留外部数据引用）
            if self.config.get('fill_policy', {}).get('keep_external_data', True):
                self._update_chart_rels(extracted_dir, workbook_path)
                # 4.2 更新 Content_Types，声明新嵌入的 xlsx
                self._update_content_types(extracted_dir, workbook_path)

            # 4.3 为饼图/折线图/散点图绑定 externalData 并刷新公式引用到嵌入工作簿
            for chart_name in self.config['output']['replace_charts']:
                chart_base = chart_name.replace('.xml', '')
                chart_xml_path = extracted_dir / 'ppt' / 'charts' / f"{chart_base}.xml"
                if not chart_xml_path.exists():
                    raise FileNotFoundError(f"图表XML不存在: {chart_xml_path}")
                # 识别图表类型
                chart_type = None
                xml_text = chart_xml_path.read_text(encoding='utf-8')
                if 'pieChart' in xml_text:
                    chart_type = 'pie'
                elif 'lineChart' in xml_text:
                    chart_type = 'line'
                elif 'scatterChart' in xml_text:
                    chart_type = 'scatter'
                # 查找关系ID并绑定 externalData
                rid = self._get_workbook_rel_id(extracted_dir, chart_base)
                self._ensure_external_data(extracted_dir, chart_base, rid)
                # 更新公式绑定到嵌入工作簿
                if chart_type == 'pie':
                    self._update_pie_formulas(extracted_dir, chart_base, pie_df)
                elif chart_type == 'line':
                    self._update_line_formulas(extracted_dir, chart_base, line_df)
                elif chart_type == 'scatter':
                    self._update_scatter_formulas(extracted_dir, chart_base, line_df)
            
            # 5. 更新图表数据XML
            replace_charts = self.config['output']['replace_charts']
            for chart_name in replace_charts:
                chart_base = chart_name.replace('.xml', '')
                chart_xml_path = extracted_dir / 'ppt' / 'charts' / f"{chart_base}.xml"
                chart_type = None
                if chart_xml_path.exists():
                    try:
                        xml_text = chart_xml_path.read_text(encoding='utf-8')
                        if 'pieChart' in xml_text:
                            chart_type = 'pie'
                        elif 'lineChart' in xml_text:
                            chart_type = 'line'
                        elif 'scatterChart' in xml_text:
                            chart_type = 'scatter'
                    except Exception:
                        pass
                # 回退规则（模板约定）
                if chart_type is None:
                    if chart_base == 'chart1':
                        chart_type = 'pie'
                    elif chart_base == 'chart2':
                        chart_type = 'scatter'
                    else:
                        chart_type = 'line'
                # 按识别类型更新
                if chart_type == 'pie':
                    self._update_chart_data_xml(extracted_dir, chart_base, pie_df, 'pie')
                elif chart_type == 'line':
                    self._update_chart_data_xml(extracted_dir, chart_base, line_df, 'line')
                elif chart_type == 'scatter':
                    self._update_scatter_chart_xml(extracted_dir, chart_base, line_df)
                    
            # 6. 重新打包PPT
            final_ppt = self._repackage_ppt(extracted_dir)
            
            self.logger.info(f"=== P10 PPT填充完成: {final_ppt} ===")
            return True
            
        except Exception as e:
            self.logger.error(f"PPT填充失败: {e}")
            return False

def main():
    """主函数"""
    # 确保在正确的目录下运行
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # 运行PPT填充器
    filler = P10PPTFiller()
    success = filler.run()
    
    if success:
        print("✅ P10 PPT填充成功！")
        return 0
    else:
        print("❌ P10 PPT填充失败！")
        return 1

if __name__ == "__main__":
    sys.exit(main())