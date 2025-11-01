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
        logging.basicConfig(
            level=getattr(logging, log_config.get('level', 'INFO')),
            format=log_config.get('format', '%(asctime)s - %(levelname)s - %(message)s'),
            handlers=[
                logging.FileHandler(log_config.get('file', 'p10_build.log'), encoding='utf-8'),
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
        """创建嵌入式工作簿文件"""
        # 创建嵌入对象目录
        embeddings_dir = extracted_dir / "ppt" / "embeddings"
        embeddings_dir.mkdir(parents=True, exist_ok=True)
        
        # 生成工作簿文件名
        workbook_file = embeddings_dir / "Microsoft_Excel_Worksheet1.xlsx"
        
        try:
            with pd.ExcelWriter(workbook_file, engine='openpyxl') as writer:
                # 写入饼图数据
                pie_df.to_excel(writer, sheet_name='PieData', index=False)
                
                # 写入折线图数据  
                line_df.to_excel(writer, sheet_name='LineData', index=False)
                
            self.logger.info(f"嵌入式工作簿已创建: {workbook_file}")
            return workbook_file
            
        except Exception as e:
            self.logger.error(f"创建嵌入式工作簿失败: {e}")
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
        """更新饼图颜色配置"""
        # 获取配置中的颜色映射
        colors = self.config.get('sentiment', {}).get('colors', {})
        sentiment_labels = self.config.get('sentiment', {}).get('labels', ['Positive', 'Neutral', 'Negative'])
        
        # 颜色映射：去掉#号
        color_map = {
            'Positive': colors.get('positive', '#4CAF50').replace('#', ''),
            'Neutral': colors.get('neutral', '#FFC107').replace('#', ''),
            'Negative': colors.get('negative', '#F44336').replace('#', '')
        }
        
        # 查找所有数据点格式
        dpts = ser.findall('.//c:dPt', namespaces)
        
        for dpt in dpts:
            idx_elem = dpt.find('.//c:idx', namespaces)
            if idx_elem is not None:
                idx = int(idx_elem.get('val'))
                if idx < len(sentiment_labels):
                    sentiment = sentiment_labels[idx]
                    if sentiment in color_map:
                        # 查找或创建spPr元素
                        sp_pr = dpt.find('.//c:spPr', namespaces)
                        if sp_pr is not None:
                            # 查找solidFill元素
                            solid_fill = sp_pr.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}solidFill', namespaces)
                            if solid_fill is not None:
                                # 查找srgbClr元素
                                srgb_clr = solid_fill.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}srgbClr', namespaces)
                                if srgb_clr is not None:
                                    # 更新颜色值
                                    srgb_clr.set('val', color_map[sentiment])
                                    self.logger.info(f"更新饼图颜色: {sentiment} -> {color_map[sentiment]}")
                        
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
        """更新散点图系列颜色"""
        # 从配置文件获取颜色映射
        colors = self.config.get('sentiment', {}).get('colors', {})
        color_mapping = {
            'Positive': colors.get('positive', '#4CAF50').replace('#', ''),
            'Neutral': colors.get('neutral', '#FFC107').replace('#', ''),
            'Negative': colors.get('negative', '#F44336').replace('#', '')
        }
        
        if sentiment not in color_mapping:
            return
            
        target_color = color_mapping[sentiment]
        
        # 查找或创建spPr元素
        sp_pr = ser.find('.//c:spPr', namespaces)
        if sp_pr is None:
            sp_pr = ET.SubElement(ser, '{http://schemas.openxmlformats.org/drawingml/2006/chart}spPr')
        
        # 清空spPr元素的所有子元素，然后重新添加需要的元素
        sp_pr.clear()
        
        # 添加线条样式（如果需要）
        ln = ET.SubElement(sp_pr, '{http://schemas.openxmlformats.org/drawingml/2006/main}ln')
        ln_solid_fill = ET.SubElement(ln, '{http://schemas.openxmlformats.org/drawingml/2006/main}solidFill')
        ln_srgb_clr = ET.SubElement(ln_solid_fill, '{http://schemas.openxmlformats.org/drawingml/2006/main}srgbClr')
        ln_srgb_clr.set('val', target_color)
        
        # 添加填充颜色
        solid_fill = ET.SubElement(sp_pr, '{http://schemas.openxmlformats.org/drawingml/2006/main}solidFill')
        srgb_clr = ET.SubElement(solid_fill, '{http://schemas.openxmlformats.org/drawingml/2006/main}srgbClr')
        srgb_clr.set('val', target_color)
        
        self.logger.info(f"更新散点图颜色: {sentiment} -> {target_color}")

    def _update_chart_rels(self, extracted_dir, workbook_path):
        """更新图表关系文件，指向新嵌入工作簿"""
        try:
            target = f"../embeddings/{Path(workbook_path).name}"
            rels_dir = extracted_dir / 'ppt' / 'charts' / '_rels'
            for chart_name in self.config['output']['replace_charts']:
                rels_file = rels_dir / f"{chart_name}.rels"
                if not rels_file.exists():
                    self.logger.warning(f"未找到关系文件: {rels_file}")
                    continue
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
                    self.logger.warning(f"更新关系失败 {rels_file}: {e}")
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