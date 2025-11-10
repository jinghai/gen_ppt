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
        - 写入折线/散点图数据到 `LineData`
        - 为散点图增加数值型 X 轴列（便于公式绑定）：X = axis_day_base + 序号
        注意：保持对现有模板的兼容，不移除原有 Date 列；列顺序为 [X, Date(如存在), Positive, Neutral, Negative]
        """
        # 创建嵌入对象目录
        embeddings_dir = extracted_dir / "ppt" / "embeddings"
        embeddings_dir.mkdir(parents=True, exist_ok=True)
        
        # 生成工作簿文件名
        workbook_file = embeddings_dir / "Microsoft_Excel_Worksheet1.xlsx"
        
        try:
            with pd.ExcelWriter(workbook_file, engine='openpyxl') as writer:
                # 写入饼图数据
                pie_df.to_excel(writer, sheet_name='PieData', index=False)
                
                # 写入折线/散点图数据：构造包含数值 X 轴的工作表
                # 中文注释：X 轴使用配置中的 axis_day_base 叠加每日序号，确保散点图的 xVal 为连续数值
                base = int(self.config.get('fill_policy', {}).get('axis_day_base', 20300))
                count = len(line_df)
                x_values = [base + i for i in range(count)]

                # 目标列顺序：X、Date(如存在)、各情绪列
                new_cols = {}
                new_cols['X'] = x_values
                if 'Date' in line_df.columns:
                    new_cols['Date'] = list(line_df['Date'])

                # 从配置读取折线/散点系列顺序，并逐列复制
                lines_order = list(self.config.get('charts', {}).get('line_chart', {}).get('lines', []))
                if not lines_order:
                    # 中文注释：严格错误策略——若未配置系列顺序则抛错
                    raise RuntimeError('缺少折线/散点系列顺序配置 charts.line_chart.lines')
                for col in lines_order:
                    if col not in line_df.columns:
                        raise RuntimeError(f'LineData 缺少必需列: {col}')
                    new_cols[col] = list(line_df[col])

                new_line_df = pd.DataFrame(new_cols)
                new_line_df.to_excel(writer, sheet_name='LineData', index=False)
                
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
            
        # 更新类别标签
        cat = ser.find('.//c:cat', namespaces)
        if cat is not None:
            str_ref = cat.find('.//c:strRef', namespaces)
            if str_ref is not None:
                # 更新标签数据
                str_cache = str_ref.find('.//c:strCache', namespaces)
                if str_cache is not None:
                    # 清除现有数据点
                    for pt in str_cache.findall('.//c:pt', namespaces):
                        str_cache.remove(pt)
                    
                    # 添加新数据点
                    for i, sentiment in enumerate(pie_df['Sentiment']):
                        pt = ET.SubElement(str_cache, '{http://schemas.openxmlformats.org/drawingml/2006/chart}pt')
                        pt.set('idx', str(i))
                        v = ET.SubElement(pt, '{http://schemas.openxmlformats.org/drawingml/2006/chart}v')
                        v.text = sentiment
                        
        # 更新数值数据
        val = ser.find('.//c:val', namespaces)
        if val is not None:
            num_ref = val.find('.//c:numRef', namespaces)
            if num_ref is not None:
                num_cache = num_ref.find('.//c:numCache', namespaces)
                if num_cache is not None:
                    # 清除现有数据点
                    for pt in num_cache.findall('.//c:pt', namespaces):
                        num_cache.remove(pt)
                    
                    # 添加新数据点
                    for i, percentage in enumerate(pie_df['Percentage']):
                        pt = ET.SubElement(num_cache, '{http://schemas.openxmlformats.org/drawingml/2006/chart}pt')
                        pt.set('idx', str(i))
                        v = ET.SubElement(pt, '{http://schemas.openxmlformats.org/drawingml/2006/chart}v')
                        v.text = str(percentage)
                        
    def _update_pie_chart_colors(self, ser, namespaces):
        """更新饼图颜色配置
        - 默认保留模板颜色，不覆盖；严格校验颜色节点存在。
        - 若 `fill_policy.use_config_colors` 为 true，则按配置覆盖颜色。
        - 若模板缺少期望的颜色节点，抛错，不做兜底。
        """
        use_cfg = bool(self.config.get('fill_policy', {}).get('use_config_colors', False))
        # 遍历数据点颜色
        dpts = ser.findall('.//c:dPt', namespaces)
        if not dpts:
            raise RuntimeError("模板饼图未包含 c:dPt 颜色节点，无法设置或校验颜色")
        a_ns = '{http://schemas.openxmlformats.org/drawingml/2006/main}'

        if not use_cfg:
            # 保留模板颜色：仅校验并记录
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
            return

        # 使用配置覆盖颜色
        try:
            pie_cfg = self.config['charts']['pie_chart']
            colors = pie_cfg.get('colors', {})
            sentiment_labels = pie_cfg.get('labels', ['Positive', 'Neutral', 'Negative'])
        except Exception as e:
            raise RuntimeError(f"读取饼图颜色配置失败: {e}")
        required_keys = ['positive', 'neutral', 'negative']
        for k in required_keys:
            if k not in colors:
                raise RuntimeError(f"饼图颜色缺失: {k}")
        color_map = {
            'Positive': colors['positive'].replace('#', ''),
            'Neutral': colors['neutral'].replace('#', ''),
            'Negative': colors['negative'].replace('#', '')
        }
        for dpt in dpts:
            idx_elem = dpt.find('.//c:idx', namespaces)
            if idx_elem is None:
                raise RuntimeError("模板饼图 dPt 缺少 c:idx 节点")
            idx = int(idx_elem.get('val'))
            if idx >= len(sentiment_labels):
                raise RuntimeError("饼图标签数量与模板 dPt 数量不一致")
            sentiment = sentiment_labels[idx]
            if sentiment not in color_map:
                raise RuntimeError(f"饼图标签未匹配到颜色: {sentiment}")
            sp_pr = dpt.find('.//c:spPr', namespaces)
            if sp_pr is None:
                raise RuntimeError("模板饼图缺少 c:spPr 节点，无法更新颜色")
            solid_fill = sp_pr.find(f'.//{a_ns}solidFill')
            if solid_fill is None:
                raise RuntimeError("模板饼图缺少 a:solidFill 节点")
            srgb_clr = solid_fill.find(f'.//{a_ns}srgbClr')
            if srgb_clr is None:
                # 若模板为 schemeClr，改为 srgbClr 以应用配置色值
                for el in list(solid_fill):
                    solid_fill.remove(el)
                srgb_clr = ET.SubElement(solid_fill, f'{a_ns}srgbClr')
            srgb_clr.set('val', color_map[sentiment])
            self.logger.info(f"应用配置饼图颜色: {sentiment} -> {color_map[sentiment]}")
                        
    def _update_line_chart_xml(self, root, line_df, namespaces):
        """更新折线图XML数据"""
        # 查找折线图
        line_chart = root.find('.//c:lineChart', namespaces)
        if line_chart is None:
            self.logger.warning("未找到折线图元素")
            return
            
        # 获取所有数据系列
        series_list = line_chart.findall('.//c:ser', namespaces)
        sentiment_labels = self.config['charts']['line_chart']['lines']
        
        for i, ser in enumerate(series_list):
            if i >= len(sentiment_labels):
                break
                
            sentiment = sentiment_labels[i]
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

        # 同步更新折线图系列颜色
        try:
            self._update_line_chart_colors(root, namespaces)
        except Exception as e:
            # 严格策略：颜色不一致应报告错误
            raise

    def _update_line_chart_colors(self, root, namespaces):
        """更新折线图系列颜色
        - 默认保留模板颜色，不覆盖；严格校验颜色节点存在。
        - 若 `fill_policy.use_config_colors` 为 true，则按配置覆盖颜色（与饼图一致）。
        """
        use_cfg = bool(self.config.get('fill_policy', {}).get('use_config_colors', False))
        line_chart = root.find('.//c:lineChart', namespaces)
        if line_chart is None:
            raise RuntimeError("未找到折线图元素以更新颜色")
        series_list = line_chart.findall('.//c:ser', namespaces)
        a_ns = '{http://schemas.openxmlformats.org/drawingml/2006/main}'

        if not use_cfg:
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
            return

        # 使用配置覆盖颜色
        pie_cfg = self.config['charts']['pie_chart']
        colors = pie_cfg.get('colors', {})
        for k in ['positive', 'neutral', 'negative']:
            if k not in colors:
                raise RuntimeError(f"折线颜色缺失: {k}")
        expected_order = ['positive', 'neutral', 'negative']
        for idx, ser in enumerate(series_list):
            if idx >= len(expected_order):
                break
            key = expected_order[idx]
            hex_val = colors[key].replace('#', '')
            sp_pr = ser.find('.//c:spPr', namespaces)
            if sp_pr is None:
                raise RuntimeError("模板折线系列缺少 c:spPr 节点，无法更新颜色")
            ln = sp_pr.find(f'.//{a_ns}ln')
            if ln is None:
                raise RuntimeError("模板折线系列缺少 a:ln 节点")
            solid_fill = ln.find(f'.//{a_ns}solidFill')
            if solid_fill is None:
                raise RuntimeError("模板折线系列缺少 a:solidFill 节点")
            srgb_clr = solid_fill.find(f'.//{a_ns}srgbClr')
            if srgb_clr is None:
                # 若模板为 schemeClr，改为 srgbClr 以应用配置色值
                for el in list(solid_fill):
                    solid_fill.remove(el)
                srgb_clr = ET.SubElement(solid_fill, f'{a_ns}srgbClr')
            srgb_clr.set('val', hex_val)
            self.logger.info(f"应用配置折线颜色: {key} -> {hex_val}")

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
        # X轴类别公式：假设第1列为日期/类别
        n = len(line_df) + 1
        x_col = self._excel_col_letter(0)
        for i, ser in enumerate(series_list):
            # 更新 X 轴公式
            cat_f = ser.find('.//c:cat/c:strRef/c:f', ns)
            if cat_f is None:
                raise RuntimeError("折线图缺少类别公式 c:cat/c:strRef/c:f")
            cat_f.text = f"LineData!${x_col}$2:${x_col}${n}"
            # 更新 Y 轴值公式：第 i+1 列（跳过日期列）
            y_col = self._excel_col_letter(i + 1)
            val_f = ser.find('.//c:val/c:numRef/c:f', ns)
            if val_f is None:
                raise RuntimeError("折线图缺少数值公式 c:val/c:numRef/c:f")
            val_f.text = f"LineData!${y_col}$2:${y_col}${n}"
        ET.ElementTree(root).write(chart_file, encoding='utf-8', xml_declaration=True)
        self.logger.info(f"折线图公式已更新到嵌入工作簿区域: {chart_file}")

    def _update_scatter_formulas(self, extracted_dir: Path, chart_base: str, line_df: pd.DataFrame):
        """将散点图的 xVal/yVal 公式绑定到嵌入工作簿 LineData
        - xVal 指向 X 数值轴列（A列）：LineData!$A$2:$A${n}
        - yVal 按配置顺序依次指向 Positive/Neutral/Negative（C/D/E 列）
        中文注释：此函数要求 _create_embedded_workbook 写入列顺序为 [X, Date(可选), Positive, Neutral, Negative]
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
        # 列字母映射：X(A), Positive(C), Neutral(D), Negative(E)
        # 若存在 Date 列，则 B 为 Date；yVal 从 C 开始按配置顺序对应
        x_col = 'A'
        # 从配置读取 y 系列的顺序
        lines_order = list(self.config.get('charts', {}).get('line_chart', {}).get('lines', []))
        if not lines_order:
            raise RuntimeError('缺少折线/散点系列顺序配置 charts.line_chart.lines')
        # 计算起始 y 列索引：X(A) -> 0, Date(B 可选) -> 1，y 从 2 开始
        y_start_idx = 2
        for i, ser in enumerate(series_list):
            if i >= len(lines_order):
                break
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
            # 准备X轴日索引
            base = int(self.config.get('fill_policy', {}).get('axis_day_base', 20300))
            x_values = [base + i for i in range(len(line_df['Date']))]
            sentiment_labels = self.config['charts']['line_chart']['lines']
            series_list = scatter_chart.findall('.//c:ser', namespaces)
            for i, ser in enumerate(series_list):
                if i >= len(sentiment_labels):
                    break
                sentiment = sentiment_labels[i]
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
                            for j, yv in enumerate(line_df[sentiment]):
                                pt = ET.SubElement(num_cache, '{http://schemas.openxmlformats.org/drawingml/2006/chart}pt')
                                pt.set('idx', str(j))
                                v = ET.SubElement(pt, '{http://schemas.openxmlformats.org/drawingml/2006/chart}v')
                                v.text = str(yv)
                            pt_count = num_cache.find('.//c:ptCount', namespaces)
                            if pt_count is not None:
                                pt_count.set('val', str(len(line_df[sentiment])))
                
                # 更新系列颜色
                self._update_scatter_chart_colors(ser, sentiment, namespaces)
            
            tree.write(chart_file, encoding='utf-8', xml_declaration=True)
            self.logger.info(f"散点图数据已更新: {chart_file}")
            return True
        except Exception as e:
            self.logger.error(f"更新散点图XML失败 {chart_file}: {e}")
            return False

    def _update_scatter_chart_colors(self, ser, sentiment, namespaces):
        """更新散点图系列颜色
        - 默认保留模板颜色，不覆盖；严格校验颜色节点存在。
        - 若 `fill_policy.use_config_colors` 为 true，则按配置覆盖颜色。
        """
        use_cfg = bool(self.config.get('fill_policy', {}).get('use_config_colors', False))
        a_ns = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
        sp_pr = ser.find('.//c:spPr', namespaces)
        if sp_pr is None:
            raise RuntimeError("模板散点系列缺少 c:spPr 节点")

        if not use_cfg:
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
            return

        # 使用配置覆盖颜色
        colors = self.config.get('sentiment', {}).get('colors', {})
        if sentiment not in ['Positive', 'Neutral', 'Negative']:
            raise RuntimeError(f"未知情绪标签: {sentiment}")
        mapping = {
            'Positive': colors.get('positive', '#4CAF50').replace('#', ''),
            'Neutral': colors.get('neutral', '#FFC107').replace('#', ''),
            'Negative': colors.get('negative', '#F44336').replace('#', '')
        }
        target = mapping[sentiment]
        # 清除并覆盖线条与填充颜色
        for el in list(sp_pr):
            sp_pr.remove(el)
        ln = ET.SubElement(sp_pr, f'{a_ns}ln')
        ln_solid = ET.SubElement(ln, f'{a_ns}solidFill')
        ET.SubElement(ln_solid, f'{a_ns}srgbClr', val=target)
        fill = ET.SubElement(sp_pr, f'{a_ns}solidFill')
        ET.SubElement(fill, f'{a_ns}srgbClr', val=target)
        self.logger.info(f"应用配置散点颜色: {sentiment} -> {target}")

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