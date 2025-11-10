#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
P13 PPT 填充脚本

功能：
- 读取页面级配置 charts/p13/config.yaml；
- 从 output/p13_data.xlsx 读取 PieData 与 LineData；
- 解压 charts/p13/p13.pptx 到页面级 tmp 目录；
- 在解压目录下创建嵌入式工作簿 ppt/embeddings/Microsoft_Excel_Worksheet1.xlsx；
- 更新图表 XML（chart10 饼图、chart11 折线或散点）数据缓存与系列颜色；
- 更新图表关系文件指向嵌入工作簿，更新 Content_Types 覆盖项；
- 重新打包为 charts/p13/output/p13-final.pptx。

注意：不修改模板文件本身；所有中间文件仅使用页面级 tmp；遵循色彩与顺序映射。
"""

import os
import sys
import shutil
import zipfile
import logging
import yaml
import pandas as pd
import xml.etree.ElementTree as ET
from pathlib import Path


class P13PPTFiller:
    def __init__(self, config_path: str = 'config.yaml'):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.cfg = yaml.safe_load(f)

        self.page_dir = Path(__file__).resolve().parent
        self.project = self.cfg.get('project', {})
        self.charts = self.cfg.get('charts', {})
        self.output_cfg = self.cfg.get('output', {})
        self.fill_policy = self.cfg.get('fill_policy', {})
        self.sentiment_cfg = self.cfg.get('sentiment', {})

        # 路径
        self.tmp_dir = self.page_dir / self.project.get('tmp_dir', 'tmp')
        self.output_dir = self.page_dir / self.project.get('output_dir', 'output')
        self.template_file = self.page_dir / self.project.get('template_file', 'p13.pptx')
        # Excel 数据文件改为放置在页面目录，而非 output 子目录。
        # 若配置未提供 excel_file_name，则使用默认文件名 'p13_data.xlsx'。
        # 不做兜底到 output，避免掩盖生成路径错误；缺失时直接报错。
        self.excel_path = self.page_dir / self.output_cfg.get('excel_file_name', 'p13_data.xlsx')
        self.final_pptx = self.output_dir / self.output_cfg.get('final_pptx_name', 'p13-final.pptx')
        self.embedded_name = self.fill_policy.get('embedded_workbook_name', 'Microsoft_Excel_Worksheet1.xlsx')

        # 日轴基准
        self.axis_day_base = int(self.fill_policy.get('axis_day_base', 20300))

        # 颜色映射
        colors = self.sentiment_cfg.get('colors', {})
        # 颜色严格与模板对齐：Positive=009FA9, Neutral=FFBC42, Negative=D81159
        # 若配置缺失则使用模板色值作为默认，不做兜底为其它颜色。
        self.color_map = {
            'Positive': colors.get('Positive', '#009FA9').replace('#', ''),
            'Neutral': colors.get('Neutral', '#FFBC42').replace('#', ''),
            'Negative': colors.get('Negative', '#D81159').replace('#', ''),
        }

        # 日序列顺序
        self.line_order = [
            self.charts.get('line', {}).get('positive_column', 'Positive'),
            self.charts.get('line', {}).get('neutral_column', 'Neutral'),
            self.charts.get('line', {}).get('negative_column', 'Negative'),
        ]

        # 日日期列名
        self.date_col = self.charts.get('line', {}).get('date_column', 'Date')

        # 日序列可能同时支持折线或散点两种模板

        # 日志
        log_cfg = self.cfg.get('logging', {})
        log_file = Path(log_cfg.get('file', str(self.page_dir / 'logs' / 'build.log')))
        # 在初始化日志之前，确保日志目录存在；不做静默兜底，目录创建失败将抛出异常
        if log_file.parent and not log_file.parent.exists():
            log_file.parent.mkdir(parents=True, exist_ok=True)

        logging.basicConfig(
            level=getattr(logging, log_cfg.get('level', 'INFO')),
            format=log_cfg.get('format', '%(asctime)s - %(levelname)s - %(message)s'),
            handlers=[
                logging.FileHandler(str(log_file), encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    # -------------------- 基本工具 --------------------
    def _prepare_dirs(self):
        if self.tmp_dir.exists():
            shutil.rmtree(self.tmp_dir)
        self.tmp_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def _extract_template(self) -> Path:
        if not self.template_file.exists():
            raise FileNotFoundError(f"模板不存在: {self.template_file}")
        extracted = self.tmp_dir / 'ppt_extracted'
        with zipfile.ZipFile(self.template_file, 'r') as z:
            z.extractall(extracted)
        self.logger.info(f"模板已解压: {extracted}")
        return extracted

    def _load_excel(self):
        if not self.excel_path.exists():
            raise FileNotFoundError(f"Excel 不存在: {self.excel_path}")
        pie_sheet = self.charts.get('pie', {}).get('sheet_name', 'PieData')
        line_sheet = self.charts.get('line', {}).get('sheet_name', 'LineData')
        pie_df = pd.read_excel(self.excel_path, sheet_name=pie_sheet)
        line_df = pd.read_excel(self.excel_path, sheet_name=line_sheet)
        self.logger.info(f"Excel 加载成功: Pie={len(pie_df)} 行, Line={len(line_df)} 行")
        return pie_df, line_df

    def _create_embedded_workbook(self, extracted_dir: Path, pie_df, line_df) -> Path:
        """
        创建嵌入式工作簿，并以图表可绑定的结构写入。

        设计思路：
        - 为饼图写入 Sheet `PieData`（列：Sentiment、Percentage），保留表头；
        - 为折线/散点写入 Sheet `LineData`，首列增加数值型日轴列 `X`（axis_day_base + 序号），
          其后依次为 `Date`、三条情绪列（按照 line_order 排序，若列不存在将报错）。
        这样我们可以在图表 XML 中以公式（c:f）绑定到这些单元格区域，实现 PPT 内编辑表格即可刷新图表。
        """
        embeddings_dir = extracted_dir / 'ppt' / 'embeddings'
        embeddings_dir.mkdir(parents=True, exist_ok=True)
        workbook_file = embeddings_dir / self.embedded_name

        # 构造 LineData 的绑定友好结构
        date_col = self.date_col
        if date_col not in line_df.columns:
            raise ValueError(f"LineData 缺少日期列: {date_col}")
        n = len(line_df[date_col])
        x_vals = [self.axis_day_base + i for i in range(n)]
        ordered_cols = []
        for s in self.line_order:
            if s not in line_df.columns:
                raise ValueError(f"LineData 缺少情绪列: {s}")
            ordered_cols.append(s)
        line_out = pd.DataFrame({'X': x_vals, date_col: list(line_df[date_col])})
        for s in ordered_cols:
            line_out[s] = list(line_df[s])

        with pd.ExcelWriter(workbook_file, engine='openpyxl') as writer:
            pie_df.to_excel(writer, sheet_name=self.charts.get('pie', {}).get('sheet_name', 'PieData'), index=False)
            line_out.to_excel(writer, sheet_name=self.charts.get('line', {}).get('sheet_name', 'LineData'), index=False)
        self.logger.info(f"嵌入式工作簿已写入: {workbook_file}")
        return workbook_file

    # -------------------- 图表更新 --------------------
    def _update_pie_chart_xml(self, chart_file: Path, pie_df):
        if not chart_file.exists():
            self.logger.warning(f"缺少图表文件: {chart_file}")
            return False
        try:
            tree = ET.parse(chart_file)
            root = tree.getroot()
            ns = {'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart',
                  'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
            pie = root.find('.//c:pieChart', ns)
            if pie is None:
                self.logger.warning("未找到 pieChart 元素")
                return False
            ser = pie.find('.//c:ser', ns)
            if ser is None:
                self.logger.warning("未找到饼图数据系列 ser")
                return False

            # 更新类别标签
            cat = ser.find('.//c:cat', ns)
            if cat is not None:
                str_ref = cat.find('.//c:strRef', ns)
                if str_ref is not None:
                    str_cache = str_ref.find('.//c:strCache', ns)
                    if str_cache is not None:
                        for pt in list(str_cache.findall('.//c:pt', ns)):
                            str_cache.remove(pt)
                        for i, lab in enumerate(list(pie_df['Sentiment'])):
                            ptn = ET.SubElement(str_cache, '{http://schemas.openxmlformats.org/drawingml/2006/chart}pt')
                            ptn.set('idx', str(i))
                            v = ET.SubElement(ptn, '{http://schemas.openxmlformats.org/drawingml/2006/chart}v')
                            v.text = str(lab)
                        pc = str_cache.find('.//c:ptCount', ns)
                        if pc is not None:
                            pc.set('val', str(len(pie_df['Sentiment'])))

            # 更新数值
            val = ser.find('.//c:val', ns)
            if val is not None:
                num_ref = val.find('.//c:numRef', ns)
                if num_ref is not None:
                    num_cache = num_ref.find('.//c:numCache', ns)
                    if num_cache is not None:
                        for pt in list(num_cache.findall('.//c:pt', ns)):
                            num_cache.remove(pt)
                        for i, perc in enumerate(list(pie_df['Percentage'])):
                            ptn = ET.SubElement(num_cache, '{http://schemas.openxmlformats.org/drawingml/2006/chart}pt')
                            ptn.set('idx', str(i))
                            v = ET.SubElement(ptn, '{http://schemas.openxmlformats.org/drawingml/2006/chart}v')
                            v.text = str(perc)
                        pc = num_cache.find('.//c:ptCount', ns)
                        if pc is not None:
                            pc.set('val', str(len(pie_df['Percentage'])))

            # 更新扇区颜色（按数据点索引）
            dpts = ser.findall('.//c:dPt', ns)
            for dpt in dpts:
                idx_e = dpt.find('.//c:idx', ns)
                if idx_e is None:
                    continue
                idx = int(idx_e.get('val')) if idx_e.get('val') else 0
                # 按 Sentiment 顺序定位颜色
                sentiment_list = list(pie_df['Sentiment'])
                if idx >= len(sentiment_list):
                    continue
                senti = sentiment_list[idx]
                color_hex = self.color_map.get(senti)
                if not color_hex:
                    continue
                spPr = dpt.find('.//c:spPr', ns)
                if spPr is None:
                    spPr = ET.SubElement(dpt, '{http://schemas.openxmlformats.org/drawingml/2006/chart}spPr')
                # 清空后重建 solidFill
                for ch in list(spPr):
                    spPr.remove(ch)
                solid = ET.SubElement(spPr, '{http://schemas.openxmlformats.org/drawingml/2006/main}solidFill')
                rgb = ET.SubElement(solid, '{http://schemas.openxmlformats.org/drawingml/2006/main}srgbClr')
                rgb.set('val', color_hex)

            # 统一标签显示：启用百分比、关闭数值/系列名/类别名；取消手动定位，改为最佳适配
            dLbls_ser = ser.find('.//c:dLbls', ns)
            if dLbls_ser is None:
                dLbls_ser = ET.SubElement(ser, '{http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls')
            # 移除所有点级 dLbl（含 delete 与 manualLayout），避免覆盖全局设置
            for d in list(dLbls_ser.findall('c:dLbl', ns)):
                dLbls_ser.remove(d)
            # 设置显示选项
            def _set_flag(name: str, val: str):
                el = dLbls_ser.find(f'c:{name}', ns)
                if el is None:
                    el = ET.SubElement(dLbls_ser, f'{{http://schemas.openxmlformats.org/drawingml/2006/chart}}{name}')
                el.set('val', val)
            _set_flag('showLegendKey', '0')
            _set_flag('showVal', '0')
            _set_flag('showCatName', '0')
            _set_flag('showSerName', '0')
            _set_flag('showPercent', '1')
            _set_flag('showBubbleSize', '0')
            # 标签位置：最佳适配，尽量落在扇形内
            pos = dLbls_ser.find('c:dLblPos', ns)
            if pos is None:
                pos = ET.SubElement(dLbls_ser, '{http://schemas.openxmlformats.org/drawingml/2006/chart}dLblPos')
            pos.set('val', 'bestFit')
            # 关闭引导线，避免标签在外部时出现牵引线影响视觉
            _set_flag('showLeaderLines', '0')

            # 同步更新图表级 dLbls（作为默认设置），确保与系列一致
            dLbls_chart = pie.find('c:dLbls', ns)
            if dLbls_chart is None:
                dLbls_chart = ET.SubElement(pie, '{http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls')
            for d in list(dLbls_chart.findall('c:dLbl', ns)):
                dLbls_chart.remove(d)
            def _set_chart_flag(name: str, val: str):
                el = dLbls_chart.find(f'c:{name}', ns)
                if el is None:
                    el = ET.SubElement(dLbls_chart, f'{{http://schemas.openxmlformats.org/drawingml/2006/chart}}{name}')
                el.set('val', val)
            _set_chart_flag('showLegendKey', '0')
            _set_chart_flag('showVal', '0')
            _set_chart_flag('showCatName', '0')
            _set_chart_flag('showSerName', '0')
            _set_chart_flag('showPercent', '1')
            _set_chart_flag('showBubbleSize', '0')
            _set_chart_flag('showLeaderLines', '0')

            tree.write(chart_file, encoding='utf-8', xml_declaration=True)
            self.logger.info(f"饼图 XML 已更新: {chart_file}")
            return True
        except Exception as e:
            self.logger.error(f"更新饼图失败 {chart_file}: {e}")
            return False

    def _update_line_chart_xml(self, chart_file: Path, line_df):
        if not chart_file.exists():
            self.logger.warning(f"缺少图表文件: {chart_file}")
            return False
        try:
            tree = ET.parse(chart_file)
            root = tree.getroot()
            ns = {'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart',
                  'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}

            # 优先尝试 lineChart
            line_chart = root.find('.//c:lineChart', ns)
            if line_chart is not None:
                series_list = line_chart.findall('.//c:ser', ns)
                for i, ser in enumerate(series_list):
                    if i >= len(self.line_order):
                        break
                    sentiment = self.line_order[i]
                    if sentiment not in line_df.columns:
                        continue
                    # 更新 X 轴日期
                    cat = ser.find('.//c:cat', ns)
                    if cat is not None:
                        str_ref = cat.find('.//c:strRef', ns)
                        if str_ref is not None:
                            str_cache = str_ref.find('.//c:strCache', ns)
                            if str_cache is not None:
                                for pt in list(str_cache.findall('.//c:pt', ns)):
                                    str_cache.remove(pt)
                                for j, d in enumerate(list(line_df[self.date_col])):
                                    ptn = ET.SubElement(str_cache, '{http://schemas.openxmlformats.org/drawingml/2006/chart}pt')
                                    ptn.set('idx', str(j))
                                    v = ET.SubElement(ptn, '{http://schemas.openxmlformats.org/drawingml/2006/chart}v')
                                    v.text = str(d)
                                pc = str_cache.find('.//c:ptCount', ns)
                                if pc is not None:
                                    pc.set('val', str(len(line_df[self.date_col])))
                    # 更新 Y 轴百分比
                    val = ser.find('.//c:val', ns)
                    if val is not None:
                        num_ref = val.find('.//c:numRef', ns)
                        if num_ref is not None:
                            num_cache = num_ref.find('.//c:numCache', ns)
                            if num_cache is not None:
                                for pt in list(num_cache.findall('.//c:pt', ns)):
                                    num_cache.remove(pt)
                                for j, y in enumerate(list(line_df[sentiment])):
                                    ptn = ET.SubElement(num_cache, '{http://schemas.openxmlformats.org/drawingml/2006/chart}pt')
                                    ptn.set('idx', str(j))
                                    v = ET.SubElement(ptn, '{http://schemas.openxmlformats.org/drawingml/2006/chart}v')
                                    v.text = str(y)
                                pc = num_cache.find('.//c:ptCount', ns)
                                if pc is not None:
                                    pc.set('val', str(len(line_df[sentiment])))

                    # 更新系列颜色
                    spPr = ser.find('.//c:spPr', ns)
                    if spPr is None:
                        spPr = ET.SubElement(ser, '{http://schemas.openxmlformats.org/drawingml/2006/chart}spPr')
                    for ch in list(spPr):
                        spPr.remove(ch)
                    ln = ET.SubElement(spPr, '{http://schemas.openxmlformats.org/drawingml/2006/main}ln')
                    ln_sf = ET.SubElement(ln, '{http://schemas.openxmlformats.org/drawingml/2006/main}solidFill')
                    ln_rgb = ET.SubElement(ln_sf, '{http://schemas.openxmlformats.org/drawingml/2006/main}srgbClr')
                    ln_rgb.set('val', self.color_map.get(sentiment, '000000'))
                    sf = ET.SubElement(spPr, '{http://schemas.openxmlformats.org/drawingml/2006/main}solidFill')
                    rgb = ET.SubElement(sf, '{http://schemas.openxmlformats.org/drawingml/2006/main}srgbClr')
                    rgb.set('val', self.color_map.get(sentiment, '000000'))

                tree.write(chart_file, encoding='utf-8', xml_declaration=True)
                self.logger.info(f"折线图 XML 已更新: {chart_file}")
                return True

            # 其次尝试 scatterChart（若模板为散点）
            scatter_chart = root.find('.//c:scatterChart', ns)
            if scatter_chart is not None:
                series_list = scatter_chart.findall('.//c:ser', ns)
                # 构造 X 值（轴基准 + 序号）
                x_vals = [self.axis_day_base + i for i in range(len(line_df[self.date_col]))]
                for i, ser in enumerate(series_list):
                    if i >= len(self.line_order):
                        break
                    sentiment = self.line_order[i]
                    if sentiment not in line_df.columns:
                        continue
                    # 更新 xVal
                    xval = ser.find('.//c:xVal', ns)
                    if xval is not None:
                        num_ref = xval.find('.//c:numRef', ns)
                        if num_ref is not None:
                            num_cache = num_ref.find('.//c:numCache', ns)
                            if num_cache is not None:
                                for pt in list(num_cache.findall('.//c:pt', ns)):
                                    num_cache.remove(pt)
                                for j, xv in enumerate(x_vals):
                                    ptn = ET.SubElement(num_cache, '{http://schemas.openxmlformats.org/drawingml/2006/chart}pt')
                                    ptn.set('idx', str(j))
                                    v = ET.SubElement(ptn, '{http://schemas.openxmlformats.org/drawingml/2006/chart}v')
                                    v.text = str(xv)
                                pc = num_cache.find('.//c:ptCount', ns)
                                if pc is not None:
                                    pc.set('val', str(len(x_vals)))
                    # 更新 yVal
                    yval = ser.find('.//c:yVal', ns)
                    if yval is not None:
                        num_ref = yval.find('.//c:numRef', ns)
                        if num_ref is not None:
                            num_cache = num_ref.find('.//c:numCache', ns)
                            if num_cache is not None:
                                for pt in list(num_cache.findall('.//c:pt', ns)):
                                    num_cache.remove(pt)
                                for j, y in enumerate(list(line_df[sentiment])):
                                    ptn = ET.SubElement(num_cache, '{http://schemas.openxmlformats.org/drawingml/2006/chart}pt')
                                    ptn.set('idx', str(j))
                                    v = ET.SubElement(ptn, '{http://schemas.openxmlformats.org/drawingml/2006/chart}v')
                                    v.text = str(y)
                                pc = num_cache.find('.//c:ptCount', ns)
                                if pc is not None:
                                    pc.set('val', str(len(line_df[sentiment])))

                    # 系列颜色
                    spPr = ser.find('.//c:spPr', ns)
                    if spPr is None:
                        spPr = ET.SubElement(ser, '{http://schemas.openxmlformats.org/drawingml/2006/chart}spPr')
                    for ch in list(spPr):
                        spPr.remove(ch)
                    ln = ET.SubElement(spPr, '{http://schemas.openxmlformats.org/drawingml/2006/main}ln')
                    ln_sf = ET.SubElement(ln, '{http://schemas.openxmlformats.org/drawingml/2006/main}solidFill')
                    ln_rgb = ET.SubElement(ln_sf, '{http://schemas.openxmlformats.org/drawingml/2006/main}srgbClr')
                    ln_rgb.set('val', self.color_map.get(sentiment, '000000'))
                    sf = ET.SubElement(spPr, '{http://schemas.openxmlformats.org/drawingml/2006/main}solidFill')
                    rgb = ET.SubElement(sf, '{http://schemas.openxmlformats.org/drawingml/2006/main}srgbClr')
                    rgb.set('val', self.color_map.get(sentiment, '000000'))

                tree.write(chart_file, encoding='utf-8', xml_declaration=True)
                self.logger.info(f"散点图 XML 已更新: {chart_file}")
                return True

            self.logger.warning("未找到 lineChart 或 scatterChart 元素")
            return False
        except Exception as e:
            self.logger.error(f"更新折线/散点失败 {chart_file}: {e}")
            return False

    # -------------------- externalData 与公式绑定 --------------------
    def _get_workbook_rel_id(self, rels_file: Path) -> str:
        """读取某个图表的关系文件，返回嵌入工作簿的 rId（关系类型为 package）。"""
        if not rels_file.exists():
            raise FileNotFoundError(f"缺少关系文件: {rels_file}")
        tree = ET.parse(rels_file)
        root = tree.getroot()
        for rel in root.findall('.//{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
            typ = rel.get('Type', '')
            if typ.endswith('/relationships/package'):
                rid = rel.get('Id')
                if not rid:
                    raise ValueError(f"关系文件缺少 Id: {rels_file}")
                return rid
        raise ValueError(f"未找到指向工作簿的关系（package）: {rels_file}")

    def _ensure_external_data(self, chart_file: Path, rel_id: str):
        """确保 chart.xml 中存在 externalData 并指向给定 rId；同时开启 autoUpdate。"""
        if not chart_file.exists():
            raise FileNotFoundError(f"缺少图表文件: {chart_file}")
        tree = ET.parse(chart_file)
        root = tree.getroot()
        ns_c = 'http://schemas.openxmlformats.org/drawingml/2006/chart'
        ns_r = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
        ext = root.find(f'.//{{{ns_c}}}externalData')
        if ext is None:
            # externalData 必须是 chartSpace 的直接子元素
            ext = ET.SubElement(root, f'{{{ns_c}}}externalData')
        ext.set(f'{{{ns_r}}}id', rel_id)
        auto = ext.find(f'{{{ns_c}}}autoUpdate')
        if auto is None:
            auto = ET.SubElement(ext, f'{{{ns_c}}}autoUpdate')
        auto.set('val', '1')
        tree.write(chart_file, encoding='utf-8', xml_declaration=True)
        self.logger.info(f"externalData 已绑定: {chart_file} -> {rel_id}")

    def _update_pie_formulas(self, chart_file: Path, pie_rows: int, sheet_name: str = 'PieData'):
        """
        将饼图的数值与类别公式（c:f）绑定到嵌入工作簿的 PieData 区域：
        - 值：B2:B{N+1}（Percentage）
        - 类别：A2:A{N+1}（Sentiment）
        如果模板中不存在 c:cat/strRef，则仅更新数值公式。
        """
        tree = ET.parse(chart_file)
        root = tree.getroot()
        ns = {'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart'}
        pie = root.find('.//c:pieChart', ns)
        if pie is None:
            raise ValueError("模板不包含饼图（pieChart）")
        ser = pie.find('.//c:ser', ns)
        if ser is None:
            raise ValueError("饼图缺少数据系列 ser")
        # 值公式
        val = ser.find('.//c:val/c:numRef', ns)
        if val is None:
            raise ValueError("饼图缺少数值引用（c:val/c:numRef）")
        f_el = val.find('c:f', ns)
        if f_el is None:
            f_el = ET.SubElement(val, '{http://schemas.openxmlformats.org/drawingml/2006/chart}f')
        f_el.text = f"{sheet_name}!$B$2:$B${pie_rows + 1}"
        # 类别公式（若有）
        cat = ser.find('.//c:cat/c:strRef', ns)
        if cat is not None:
            f_cat = cat.find('c:f', ns)
            if f_cat is None:
                f_cat = ET.SubElement(cat, '{http://schemas.openxmlformats.org/drawingml/2006/chart}f')
            f_cat.text = f"{sheet_name}!$A$2:$A${pie_rows + 1}"
        tree.write(chart_file, encoding='utf-8', xml_declaration=True)
        self.logger.info(f"饼图公式已绑定到 {sheet_name}")

    def _update_line_formulas(self, chart_file: Path, line_rows: int, sheet_name: str = 'LineData'):
        """
        绑定折线或散点图的系列公式到嵌入工作簿的 LineData：
        - 统一使用列方向：
          X（数值日轴）= A2:A{N+1}；Date（字符串）= B2:B{N+1}；
          各情绪列依次为 C/D/E2:E{N+1}（按 self.line_order 对应）。
        - 若检测到 lineChart：cat 使用 B 列；val 使用 C/D/E。
        - 若检测到 scatterChart：xVal 使用 A 列；yVal 使用 C/D/E。
        """
        tree = ET.parse(chart_file)
        root = tree.getroot()
        ns = {'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart'}

        line_chart = root.find('.//c:lineChart', ns)
        scatter_chart = root.find('.//c:scatterChart', ns)
        if line_chart is None and scatter_chart is None:
            raise ValueError("模板不包含 lineChart 或 scatterChart")

        def _range(col_letter: str) -> str:
            return f"{sheet_name}!${col_letter}$2:${col_letter}${line_rows + 1}"

        if line_chart is not None:
            series_list = line_chart.findall('.//c:ser', ns)
            for i, ser in enumerate(series_list):
                if i >= len(self.line_order):
                    break
                # X 轴为日期（字符串）列 B
                cat_ref = ser.find('.//c:cat/c:strRef', ns)
                if cat_ref is None:
                    cat = ser.find('.//c:cat', ns)
                    if cat is None:
                        cat = ET.SubElement(ser, '{http://schemas.openxmlformats.org/drawingml/2006/chart}cat')
                    cat_ref = ET.SubElement(cat, '{http://schemas.openxmlformats.org/drawingml/2006/chart}strRef')
                f_cat = cat_ref.find('c:f', ns)
                if f_cat is None:
                    f_cat = ET.SubElement(cat_ref, '{http://schemas.openxmlformats.org/drawingml/2006/chart}f')
                f_cat.text = _range('B')

                # Y 轴为对应情绪列 C/D/E
                val_ref = ser.find('.//c:val/c:numRef', ns)
                if val_ref is None:
                    val_el = ser.find('.//c:val', ns)
                    if val_el is None:
                        val_el = ET.SubElement(ser, '{http://schemas.openxmlformats.org/drawingml/2006/chart}val')
                    val_ref = ET.SubElement(val_el, '{http://schemas.openxmlformats.org/drawingml/2006/chart}numRef')
                f_val = val_ref.find('c:f', ns)
                if f_val is None:
                    f_val = ET.SubElement(val_ref, '{http://schemas.openxmlformats.org/drawingml/2006/chart}f')
                col = chr(ord('C') + i)  # C/D/E...
                f_val.text = _range(col)

            tree.write(chart_file, encoding='utf-8', xml_declaration=True)
            self.logger.info("折线图公式已绑定到 LineData")
            return

        # scatterChart
        series_list = scatter_chart.findall('.//c:ser', ns)
        for i, ser in enumerate(series_list):
            if i >= len(self.line_order):
                break
            # xVal 使用 A 列（数值日轴）
            x_ref = ser.find('.//c:xVal/c:numRef', ns)
            if x_ref is None:
                x_el = ser.find('.//c:xVal', ns)
                if x_el is None:
                    x_el = ET.SubElement(ser, '{http://schemas.openxmlformats.org/drawingml/2006/chart}xVal')
                x_ref = ET.SubElement(x_el, '{http://schemas.openxmlformats.org/drawingml/2006/chart}numRef')
            f_x = x_ref.find('c:f', ns)
            if f_x is None:
                f_x = ET.SubElement(x_ref, '{http://schemas.openxmlformats.org/drawingml/2006/chart}f')
            f_x.text = _range('A')

            # yVal 使用对应情绪列 C/D/E
            y_ref = ser.find('.//c:yVal/c:numRef', ns)
            if y_ref is None:
                y_el = ser.find('.//c:yVal', ns)
                if y_el is None:
                    y_el = ET.SubElement(ser, '{http://schemas.openxmlformats.org/drawingml/2006/chart}yVal')
                y_ref = ET.SubElement(y_el, '{http://schemas.openxmlformats.org/drawingml/2006/chart}numRef')
            f_y = y_ref.find('c:f', ns)
            if f_y is None:
                f_y = ET.SubElement(y_ref, '{http://schemas.openxmlformats.org/drawingml/2006/chart}f')
            col = chr(ord('C') + i)
            f_y.text = _range(col)

        tree.write(chart_file, encoding='utf-8', xml_declaration=True)
        self.logger.info("散点图公式已绑定到 LineData")

    # -------------------- 关系与内容类型 --------------------
    def _update_chart_rels(self, extracted_dir: Path, workbook_path: Path):
        target = f"../embeddings/{workbook_path.name}"
        rels_dir = extracted_dir / 'ppt' / 'charts' / '_rels'
        for chart in self.output_cfg.get('replace_charts', ['chart10.xml', 'chart11.xml']):
            rels_file = rels_dir / f"{chart}.rels"
            if not rels_file.exists():
                self.logger.warning(f"缺少关系文件: {rels_file}")
                continue
            try:
                tree = ET.parse(rels_file)
                root = tree.getroot()
                for rel in root.findall('.//{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
                    typ = rel.get('Type', '')
                    if typ.endswith('/relationships/package'):
                        rel.set('Target', target)
                tree.write(rels_file, encoding='utf-8', xml_declaration=True)
                self.logger.info(f"更新关系: {rels_file} -> {target}")
            except Exception as e:
                self.logger.warning(f"更新关系失败 {rels_file}: {e}")

    def _update_content_types(self, extracted_dir: Path, workbook_path: Path):
        ct_file = extracted_dir / '[Content_Types].xml'
        if not ct_file.exists():
            self.logger.warning("缺少 Content_Types.xml，跳过更新")
            return
        try:
            tree = ET.parse(ct_file)
            root = tree.getroot()
            ns = 'http://schemas.openxmlformats.org/package/2006/content-types'
            # 移除模板中的 xlsb 覆盖，避免冲突
            for ov in list(root.findall(f'{{{ns}}}Override')):
                part = ov.get('PartName', '')
                if part.startswith('/ppt/embeddings/') and part.endswith('.xlsb'):
                    root.remove(ov)
            # 添加我们的 xlsx 覆盖项（若不存在）
            part_name = f'/ppt/embeddings/{workbook_path.name}'
            exists = False
            for ov in root.findall(f'{{{ns}}}Override'):
                if ov.get('PartName', '') == part_name:
                    exists = True
                    break
            if not exists:
                ET.SubElement(root, f'{{{ns}}}Override', PartName=part_name, ContentType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            tree.write(ct_file, encoding='utf-8', xml_declaration=True)
            self.logger.info("Content_Types.xml 已更新")
        except Exception as e:
            self.logger.warning(f"更新 Content_Types 失败: {e}")

    # -------------------- 打包 --------------------
    def _repackage(self, extracted_dir: Path):
        with zipfile.ZipFile(self.final_pptx, 'w', zipfile.ZIP_DEFLATED) as z:
            for root, dirs, files in os.walk(extracted_dir):
                for f in files:
                    p = Path(root) / f
                    z.write(p, p.relative_to(extracted_dir))
        self.logger.info(f"已生成: {self.final_pptx}")

    # -------------------- 主流程 --------------------
    def run(self):
        self.logger.info("=== P13 填充开始 ===")
        self._prepare_dirs()
        extracted_dir = self._extract_template()
        pie_df, line_df = self._load_excel()
        workbook_path = self._create_embedded_workbook(extracted_dir, pie_df, line_df)

        # 更新关系与类型
        if self.fill_policy.get('keep_external_data', True):
            self._update_chart_rels(extracted_dir, workbook_path)
        self._update_content_types(extracted_dir, workbook_path)

        # 更新图表 XML（缓存 + 公式 + externalData）
        charts_dir = extracted_dir / 'ppt' / 'charts'
        pie_chart = charts_dir / self.charts.get('pie', {}).get('chart_file', 'chart10.xml')
        line_chart = charts_dir / self.charts.get('line', {}).get('chart_file', 'chart11.xml')
        self._update_pie_chart_xml(pie_chart, pie_df)
        self._update_line_chart_xml(line_chart, line_df)

        # 绑定公式与 externalData 指向嵌入工作簿
        rels_dir = charts_dir / '_rels'
        pie_rid = self._get_workbook_rel_id(rels_dir / f"{pie_chart.name}.rels")
        line_rid = self._get_workbook_rel_id(rels_dir / f"{line_chart.name}.rels")
        self._ensure_external_data(pie_chart, pie_rid)
        self._ensure_external_data(line_chart, line_rid)
        # 公式绑定（使 PPT 编辑嵌入工作簿时可刷新图表）
        self._update_pie_formulas(pie_chart, pie_rows=len(pie_df), sheet_name=self.charts.get('pie', {}).get('sheet_name', 'PieData'))
        self._update_line_formulas(line_chart, line_rows=len(line_df[self.date_col]), sheet_name=self.charts.get('line', {}).get('sheet_name', 'LineData'))

        # 打包
        self._repackage(extracted_dir)


def main():
    filler = P13PPTFiller(Path(__file__).resolve().parent / 'config.yaml')
    filler.run()


if __name__ == '__main__':
    main()