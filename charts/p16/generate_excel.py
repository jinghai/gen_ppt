#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P16 数据生成脚本 - 联想法国市场声量份额趋势

实现目标（严格按需求）：
- 先从模板中抽取数据（优先嵌入 xlsx，其次 chartXML）；模板数据抽取失败直接报错；
- 再计算数据库数据，用能计算到的月份覆盖模板数据；不可计算的月份保留模板值；
- 在 Excel 中为每条记录增加 `source` 字段，标注 `template` 或 `computed`；
- 若所有输出均为模板值（没有任何 computed），直接抛错提示检查品牌与月份配置；
- 使用页面级 tmp 目录并在每次运行前清空已解压旧数据；不在随地生成代码文件。
"""

import os
import sys
import sqlite3
import zipfile
import shutil
import logging
from datetime import datetime
from typing import List, Tuple, Dict, Optional

import pandas as pd
import yaml
from lxml import etree as ET
import re

# 尝试导入 pyxlsb 以读取嵌入的 xlsb（若模板链接到外部工作簿）
try:
    from pyxlsb import open_workbook
except Exception:
    open_workbook = None  # 在需要读取嵌入工作簿时严格校验

# 设置日志（严格报错，不做静默兜底）
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class P16DataGenerator:
    """P16 数据生成器

    职责：
    - 解压模板到页面 tmp 目录并读取图表数据；
    - 从数据库计算主趋势与渠道分解数据；
    - 以模板为基线，计算值覆盖并标注来源；
    - 生成 Excel 文件供填充脚本使用；
    - 失败场景直接抛错（不兜底）。
    """

    def __init__(self, config_path: str = 'config.yaml'):
        self.config_path = config_path
        self.config = self._load_config()
        self._setup_paths()

    def _load_config(self) -> dict:
        """加载配置文件，失败直接抛错。"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            raise RuntimeError(f'加载配置文件失败: {e}')

    def _setup_paths(self) -> None:
        """设置路径并标准化为绝对路径。"""
        self.page_dir = os.path.dirname(os.path.abspath(__file__))

        # 数据库路径
        metrics_db = self.config['data_sources']['metrics_db']
        neticle_db = self.config['data_sources']['neticle_db']
        self.metrics_db = metrics_db if os.path.isabs(metrics_db) else os.path.abspath(os.path.join(self.page_dir, metrics_db))
        self.neticle_db = neticle_db if os.path.isabs(neticle_db) else os.path.abspath(os.path.join(self.page_dir, neticle_db))

        # 模板PPT路径与页面级 tmp 目录
        template_ppt = self.config['project']['template_ppt']
        self.template_ppt = template_ppt if os.path.isabs(template_ppt) else os.path.abspath(os.path.join(self.page_dir, template_ppt))

        tmp_dir_cfg = self.config['project']['tmp_dir']
        self.tmp_dir = tmp_dir_cfg if os.path.isabs(tmp_dir_cfg) else os.path.abspath(os.path.join(self.page_dir, tmp_dir_cfg))

        # 输出 Excel 路径（遵循配置；若相对路径则落于页面目录）
        output_dir = self.config['project']['output_dir']
        output_dir_abs = output_dir if os.path.isabs(output_dir) else os.path.abspath(os.path.join(self.page_dir, output_dir))
        os.makedirs(output_dir_abs, exist_ok=True)

        excel_file = self.config['output']['excel_file']
        # Excel统一输出到页面目录根（相对路径情况下忽略子目录）
        if os.path.isabs(excel_file):
            self.excel_file = excel_file
        else:
            self.excel_file = os.path.abspath(os.path.join(self.page_dir, os.path.basename(excel_file)))

    # -------------------- 模板抽取与解析 --------------------
    def _clean_tmp(self) -> None:
        """清空页面级 tmp 下已解压的旧数据，避免污染。"""
        # 解压根目录改为 tmp（不再使用 tmp/ppt）
        extract_dir = self.tmp_dir
        if os.path.exists(extract_dir):
            shutil.rmtree(extract_dir)

    def _extract_template(self) -> str:
        """解压模板 PPT 到页面级 tmp 目录，返回解压根目录。失败直接抛错。"""
        if not os.path.exists(self.template_ppt):
            raise FileNotFoundError(f'模板文件不存在: {self.template_ppt}')
        os.makedirs(self.tmp_dir, exist_ok=True)
        # 解压根目录为 tmp（其中将包含 ppt/charts 与 ppt/embeddings 等子目录）
        extract_root = self.tmp_dir
        with zipfile.ZipFile(self.template_ppt, 'r') as z:
            z.extractall(extract_root)
        logger.info(f'模板已解压到: {extract_root}')
        return extract_root

    def _parse_chart_xml(self, chart_xml_path: str) -> Tuple[List[str], List[float]]:
        """解析 chart XML 的类别与数值缓存（numCache/strCache）。

        返回: (categories, values)
        - categories: 字符串标签（如 "May '25"）；可能为空（部分模板隐藏类别轴）。
        - values: 浮点数列表；若无法解析数值，抛出异常。
        """
        ns = {'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart'}
        try:
            tree = ET.parse(chart_xml_path)
            root = tree.getroot()
            # 取第一个系列 c:ser
            ser = root.find('.//c:chart/c:plotArea//c:ser', namespaces=ns)
            if ser is None:
                raise RuntimeError(f'未找到系列数据: {chart_xml_path}')

            # 类别优先读取 strCache
            categories = [
                (v.text or '').strip()
                for v in ser.findall('.//c:cat//c:strRef//c:strCache//c:pt/c:v', namespaces=ns)
            ]
            if not categories:
                categories = [
                    (v.text or '').strip()
                    for v in ser.findall('.//c:cat//c:numRef//c:numCache//c:pt/c:v', namespaces=ns)
                ]

            # 数值读取 numCache
            values_raw = [
                (v.text or '').strip()
                for v in ser.findall('.//c:val//c:numRef//c:numCache//c:pt/c:v', namespaces=ns)
            ]
            if not values_raw:
                # 某些图表可能使用直接数值缓存（无 numRef）
                values_raw = [
                    (v.text or '').strip()
                    for v in ser.findall('.//c:val//c:numLit//c:pt/c:v', namespaces=ns)
                ]

            # 若 XML 中未取到数值，尝试读取嵌入工作簿（c:externalData）
            if not values_raw:
                # 读取 numRef 的公式以定位范围
                f_node = ser.find('.//c:val//c:numRef//c:f', namespaces=ns)
                rel_id_node = root.find('.//c:chart/c:externalData', namespaces=ns)
                if f_node is not None and rel_id_node is not None:
                    rel_id = rel_id_node.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
                    if not open_workbook:
                        raise RuntimeError('模板图表链接到嵌入工作簿，但当前环境缺少 pyxlsb 依赖，无法读取数值')
                    values_raw = self._read_values_from_embedded_workbook(chart_xml_path, rel_id, f_node.text)

            # 转浮点
            values = []
            for x in values_raw:
                try:
                    values.append(float(x))
                except Exception:
                    raise RuntimeError(f'数值无法解析为浮点: {x} @ {chart_xml_path}')

            # 若类别为空但数值存在，允许返回空类别（某些模板隐藏轴标签），由上层决定推断逻辑
            if categories:
                # 对齐长度（若长度不一致，按更短者截断，避免越界）
                n = min(len(categories), len(values))
                return categories[:n], values[:n]
            else:
                return [], values
        except Exception as e:
            raise RuntimeError(f'解析图表XML失败: {chart_xml_path} - {e}')

    def _read_values_from_embedded_workbook(self, chart_xml_path: str, rel_id: str, formula: str) -> List[str]:
        """读取嵌入 xlsb 的数值，依据 chart XML 的 numRef 公式。

        formula 示例："Sheet1!$A$1:$F$1"。返回字符串列表（后续转换为浮点）。
        若无法读取或定位，抛异常。
        """
        # chart1.xml 的关系文件位于 charts/_rels/chart1.xml.rels
        chart_dir = os.path.dirname(chart_xml_path)
        rels_path = os.path.join(chart_dir, '_rels', os.path.basename(chart_xml_path) + '.rels')
        if not os.path.exists(rels_path):
            raise RuntimeError(f'缺少关系文件: {rels_path}')

        # 解析 .rels 获取嵌入工作簿相对路径
        try:
            rels_tree = ET.parse(rels_path)
            rels_root = rels_tree.getroot()
            rel_ns = {'r': 'http://schemas.openxmlformats.org/package/2006/relationships'}
            # 不使用命名空间查找，直接遍历
            target_path = None
            for rel in rels_root:
                rid = rel.get('Id') or rel.get('ID')
                if rid == rel_id:
                    target_path = rel.get('Target')
                    break
            if not target_path:
                raise RuntimeError(f'未找到 externalData 的关系目标: rel_id={rel_id}')
        except Exception as e:
            raise RuntimeError(f'解析关系文件失败: {rels_path} - {e}')

        # 解析公式，提取工作表名与范围
        m = re.match(r"([^!]+)!\$(?P<col1>[A-Z]+)\$(?P<row1>\d+):\$(?P<col2>[A-Z]+)\$(?P<row2>\d+)", formula or '')
        if not m:
            raise RuntimeError(f'无法识别数值公式范围: {formula}')
        sheet_name = m.group(1)
        col1, row1 = m.group('col1'), int(m.group('row1'))
        col2, row2 = m.group('col2'), int(m.group('row2'))

        # 列字母转索引（A=1）
        def col_to_idx(col: str) -> int:
            idx = 0
            for ch in col:
                idx = idx * 26 + (ord(ch) - ord('A') + 1)
            return idx
        c1, c2 = col_to_idx(col1), col_to_idx(col2)

        # 计算嵌入工作簿绝对路径
        # target 是相对到 charts 目录的路径，如 ../embeddings/Workbook1.xlsb
        wb_path = os.path.abspath(os.path.join(chart_dir, target_path))
        if not os.path.exists(wb_path):
            raise RuntimeError(f'嵌入工作簿不存在: {wb_path}')
        if not open_workbook:
            raise RuntimeError('当前环境缺少 pyxlsb，无法读取嵌入工作簿')

        # 读取指定范围的单元格数值
        values: List[str] = []
        try:
            with open_workbook(wb_path) as wb:
                with wb.get_sheet(sheet_name) as sh:
                    # 仅支持单行或单列范围
                    if row1 == row2:
                        # 单行：遍历该行的所有单元格
                        for i, row in enumerate(sh.rows(), start=1):
                            if i == row1:
                                # 收集该行的数值（按列索引过滤）
                                for cell in row:
                                    # pyxlsb 的 cell 没有显式列索引，逐个收集后按数量截断
                                    if cell.v is not None:
                                        values.append(str(cell.v))
                                # 按列范围截断
                                width = c2 - c1 + 1
                                values = values[:width]
                                break
                    elif c1 == c2:
                        # 单列：遍历所有行，收集该列的数值
                        col_values = []
                        for row in sh.rows():
                            for cell in row:
                                if cell.v is not None:
                                    col_values.append(str(cell.v))
                        height = row2 - row1 + 1
                        values = col_values[:height]
                    else:
                        raise RuntimeError(f'暂不支持二维区域读取: {formula}')
        except Exception as e:
            raise RuntimeError(f'读取嵌入工作簿失败: {wb_path} - {e}')

        if not values:
            raise RuntimeError(f'嵌入工作簿返回空值: {wb_path} {formula}')
        return values

    def _infer_months_from_config(self, count: int) -> List[str]:
        """当模板未提供类别标签时，根据配置的 target_month 推断最近 count 个月（含）。"""
        target = self.config.get('filters', {}).get('target_month')
        if not target:
            raise RuntimeError('模板缺少类别标签，且配置未提供 target_month，无法推断月份')
        try:
            end = datetime.strptime(target, '%Y-%m')
        except Exception:
            raise RuntimeError(f'target_month 配置不合法: {target}')
        months: List[str] = []
        # 生成从 end 往前的 count 个月（含 end）
        y, m = end.year, end.month
        for i in range(count):
            mm = m - (count - 1 - i)
            yy = y
            while mm <= 0:
                mm += 12
                yy -= 1
            months.append(f'{yy}-{mm:02d}')
        return months

    def _normalize_month_display(self, label: str) -> str:
        """将模板中的月份显示（如 "May '25"）转换为 YYYY-MM。无法解析则抛错。"""
        label = (label or '').strip()
        # 常见格式：%b '%y
        try:
            dt = datetime.strptime(label, "%b '%y")
            return dt.strftime('%Y-%m')
        except Exception:
            # 尝试更长格式：%B '%y 或 %b %Y
            for fmt in ["%B '%y", '%b %Y', '%B %Y']:
                try:
                    dt = datetime.strptime(label, fmt)
                    return dt.strftime('%Y-%m')
                except Exception:
                    continue
        raise RuntimeError(f'无法识别的月份标签: {label}')

    def extract_template_main_trend(self, charts_dir: str) -> pd.DataFrame:
        """从模板 chart1.xml 读取主趋势数据（月份 + 值）。"""
        chart_file = self.config['chart_mapping']['chart1']['file']
        chart_path = os.path.join(charts_dir, chart_file)
        if not os.path.exists(chart_path):
            raise FileNotFoundError(f'主趋势图表文件缺失: {chart_path}')
        categories, values = self._parse_chart_xml(chart_path)

        # 若模板类别缺失，根据 target_month 推断最近 N 个月
        if categories:
            months = [self._normalize_month_display(c) for c in categories]
        else:
            months = self._infer_months_from_config(len(values))
        df = pd.DataFrame({
            'month': months,
            'month_display': [self.format_month_display(m) for m in months],
            'sov_percent': values,
            'source': ['template'] * len(months),
        })
        if df.empty:
            raise RuntimeError('主趋势模板数据为空')
        return df

    def extract_template_channel_breakdown(self, charts_dir: str) -> pd.DataFrame:
        """从模板 chart2..7.xml 读取渠道分解数据（月份 + 渠道 + 值）。"""
        mappings: Dict[str, dict] = self.config.get('chart_mapping', {})
        rows = []
        for chart_id, info in mappings.items():
            if info.get('type') != 'channel_breakdown':
                continue
            chart_file = info['file']
            chart_path = os.path.join(charts_dir, chart_file)
            if not os.path.exists(chart_path):
                raise FileNotFoundError(f'渠道图表文件缺失: {chart_path}')

            # 频道名从描述里提取（如 “Forum渠道分解图” -> “Forum”）
            desc = info.get('description', '')
            channel_name = desc.replace('渠道分解图', '').strip() or chart_id

            categories, values = self._parse_chart_xml(chart_path)
            if categories:
                months = [self._normalize_month_display(c) for c in categories]
            else:
                months = self._infer_months_from_config(len(values))
            for m, v in zip(months, values):
                rows.append({
                    'month': m,
                    'month_display': self.format_month_display(m),
                    'channel': channel_name,
                    'sov_percent': v,
                    'source': 'template'
                })

        df = pd.DataFrame(rows)
        if df.empty:
            raise RuntimeError('渠道模板数据为空')
        return df

    # -------------------- 数据库计算 --------------------
    def compute_main_trend(self) -> pd.DataFrame:
        """从 metrics 数据库计算主趋势（月份 -> SOV%）。失败直接抛错。"""
        logger.info('提取主趋势数据库数据...')
        try:
            conn = sqlite3.connect(self.metrics_db)
        except Exception as e:
            raise RuntimeError(f'连接 metrics 数据库失败: {e}')

        try:
            query = (
                """
                -- 仅计算目标月份，并在数据库侧统一保留一位小数
                SELECT month, ROUND(sov * 100, 1) AS sov_percent
                FROM brand_metrics_month
                WHERE countryName = ? AND brand = ? AND month = ?
                ORDER BY month
                """
            )
            df = pd.read_sql_query(
                query,
                conn,
                # 参数顺序严格对应 SQL：countryName, brand, month
                params=[
                    self.config['filters']['country_name'],
                    self.config['filters']['brand_name'],
                    self.config['filters']['target_month']
                ]
            )
            conn.close()
        except Exception as e:
            conn.close()
            raise RuntimeError(f'查询 metrics 数据库失败: {e}')

        # 规范化显示
        if not df.empty:
            df['month_display'] = df['month'].apply(self.format_month_display)
        return df

    def compute_channel_breakdown(self) -> pd.DataFrame:
        """从 neticle 数据库计算渠道分解（月份 + 渠道 -> SOV%）。失败直接抛错。"""
        logger.info('提取渠道分解数据库数据...')
        try:
            conn = sqlite3.connect(self.neticle_db)
        except Exception as e:
            raise RuntimeError(f'连接 neticle 数据库失败: {e}')

        try:
            query = (
                """
                SELECT 
                    strftime('%Y-%m', datetime(createdAtUtcMs/1000, 'unixepoch')) AS month,
                    sourceLabel,
                    keyword_label,
                    COUNT(*) AS mention_count
                FROM mentions_wide
                WHERE countryId = ?
                  AND strftime('%Y-%m', datetime(createdAtUtcMs/1000, 'unixepoch')) = ?
                GROUP BY month, sourceLabel, keyword_label
                """
            )
            # 仅保留目标月份的原始提及数据，避免计算到非目标月份（如 7 月）
            df = pd.read_sql_query(
                query,
                conn,
                params=[self.config['filters']['country_id'], self.config['filters']['target_month']]
            )
            conn.close()
        except Exception as e:
            conn.close()
            raise RuntimeError(f'查询 neticle 数据库失败: {e}')

        if df.empty:
            # 空数据不兜底，返回空 DataFrame，后续用模板覆盖但整体无 computed 会抛错
            return pd.DataFrame()

        # 渠道映射
        channel_mapping = self.config['channels']
        def map_channel(src: str) -> str:
            for ch, sources in channel_mapping.items():
                if src in sources:
                    return ch
            return None

        df['channel'] = df['sourceLabel'].apply(map_channel)
        df = df[df['channel'].notna()]
        if df.empty:
            return pd.DataFrame()

        # 品牌识别（lenovo）
        df['is_lenovo'] = df['keyword_label'].str.lower().str.contains('lenovo', na=False)

        # 按月份与渠道计算 SOV%
        rows = []
        for (month, channel), g in df.groupby(['month', 'channel']):
            total_mentions = g['mention_count'].sum()
            lenovo_mentions = g[g['is_lenovo']]['mention_count'].sum()
            # 计算 SOV%，并统一保留一位小数；无总量时保持为 None（不兜底）
            sov_percent = (lenovo_mentions / total_mentions * 100) if total_mentions > 0 else None
            if sov_percent is not None:
                sov_percent = round(sov_percent, 1)
            rows.append({
                'month': month,
                'month_display': self.format_month_display(month),
                'channel': channel,
                'sov_percent': sov_percent
            })

        return pd.DataFrame(rows)

    # -------------------- 覆盖策略 --------------------
    def overlay_main_trend(self, template_df: pd.DataFrame, computed_df: pd.DataFrame) -> Tuple[pd.DataFrame, int]:
        """以模板为基线，计算值覆盖主趋势；返回覆盖后的DF及computed计数。"""
        if template_df.empty:
            raise RuntimeError('主趋势模板为空，无法覆盖')

        df = template_df.copy()
        if computed_df is None or computed_df.empty:
            return df, 0

        computed_map = {row['month']: row['sov_percent'] for _, row in computed_df.iterrows()}
        computed_count = 0
        for idx, row in df.iterrows():
            month = row['month']
            if month in computed_map and pd.notna(computed_map[month]):
                df.at[idx, 'sov_percent'] = float(computed_map[month])
                df.at[idx, 'source'] = 'computed'
                computed_count += 1
        return df, computed_count

    def overlay_channel_breakdown(self, template_df: pd.DataFrame, computed_df: pd.DataFrame) -> Tuple[pd.DataFrame, int]:
        """以模板为基线，计算值覆盖渠道分解；返回覆盖后的DF及computed计数。"""
        if template_df.empty:
            raise RuntimeError('渠道模板为空，无法覆盖')

        df = template_df.copy()
        if computed_df is None or computed_df.empty:
            return df, 0

        # 建立 (month, channel) -> sov 映射
        computed_map = {}
        for _, row in computed_df.iterrows():
            key = (row['month'], row['channel'])
            val = row['sov_percent']
            computed_map[key] = val

        computed_count = 0
        for idx, row in df.iterrows():
            key = (row['month'], row['channel'])
            if key in computed_map and pd.notna(computed_map[key]):
                df.at[idx, 'sov_percent'] = float(computed_map[key])
                df.at[idx, 'source'] = 'computed'
                computed_count += 1
        return df, computed_count

    # -------------------- 工具方法 --------------------
    def format_month_display(self, month_str: str) -> str:
        """将 YYYY-MM 格式化为 "Mon 'yy" 显示。"""
        try:
            date_obj = datetime.strptime(month_str, '%Y-%m')
            return date_obj.strftime("%b '%y")
        except Exception:
            return month_str

    # -------------------- 主流程 --------------------
    def generate_excel(self) -> None:
        """生成 Excel 文件。失败直接抛错，不返回布尔。"""
        logger.info('开始生成 Excel 文件...')

        # 1) 清理并解压模板
        self._clean_tmp()
        extract_root = self._extract_template()

        # 兼容两种结构：tmp/ppt/ppt/charts 与 tmp/ppt/charts
        charts_dir = os.path.join(extract_root, 'ppt', 'charts')
        if not os.path.exists(charts_dir):
            charts_dir = os.path.join(extract_root, 'charts')
        if not os.path.exists(charts_dir):
            raise FileNotFoundError(f'图表目录不存在: {charts_dir}')

        # 2) 读取模板数据
        template_main = self.extract_template_main_trend(charts_dir)
        template_channel = self.extract_template_channel_breakdown(charts_dir)

        # 3) 计算数据库数据
        computed_main = self.compute_main_trend()
        computed_channel = self.compute_channel_breakdown()

        # 4) 覆盖并统计 computed 条数
        final_main, count_main = self.overlay_main_trend(template_main, computed_main)
        final_channel, count_channel = self.overlay_channel_breakdown(template_channel, computed_channel)

        total_computed = count_main + count_channel
        if total_computed == 0:
            raise RuntimeError('所有输出均为模板值（未覆盖任何 computed）。请检查品牌匹配与月份配置。')

        # 5) 写 Excel（包含 source 列与摘要）
        os.makedirs(os.path.dirname(self.excel_file), exist_ok=True)
        with pd.ExcelWriter(self.excel_file, engine='openpyxl') as writer:
            final_main.to_excel(writer, sheet_name='main_trend', index=False)
            final_channel.to_excel(writer, sheet_name='channel_breakdown', index=False)

            summary_data = {
                '项': ['主趋势数据点数', '渠道分解数据点数', 'computed条数', '生成时间', '数据源说明'],
                '值': [
                    len(final_main),
                    len(final_channel),
                    total_computed,
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    '以模板为基线，数据库计算覆盖；source=template/computed'
                ]
            }
            pd.DataFrame(summary_data).to_excel(writer, sheet_name='summary', index=False)

        logger.info(f'Excel 文件生成成功: {self.excel_file}')


def main() -> int:
    """入口函数：失败直接抛错并返回非零退出码。"""
    logger.info('=== P16 数据生成开始 ===')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    try:
        generator = P16DataGenerator()
        generator.generate_excel()
        logger.info('=== P16 数据生成完成 ===')
        return 0
    except Exception as e:
        logger.error(f'=== P16 数据生成失败: {e}')
        return 1


if __name__ == '__main__':
    sys.exit(main())
