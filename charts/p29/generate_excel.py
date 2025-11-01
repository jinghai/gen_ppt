#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P29页面Excel数据生成器
根据数据库数据生成Excel文件，供人工检验和修改
"""

import sqlite3
import pandas as pd
import yaml
from pathlib import Path
from datetime import datetime, timedelta, timezone
from collections import defaultdict
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils.dataframe import dataframe_to_rows

# 项目路径配置
ROOT = Path(__file__).resolve().parent

def load_config():
    """加载页面级配置文件"""
    config_path = ROOT / 'config.yaml'
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config

def get_database_paths(config):
    """获取数据库路径（相对于P29目录）"""
    neticle_db = ROOT / config['data_sources']['neticle_db']
    metrics_db = ROOT / config['data_sources']['metrics_db']
    return neticle_db, metrics_db

def to_utc_ms(date_str):
    """将日期字符串转换为UTC毫秒时间戳"""
    dt = datetime.strptime(date_str, '%Y-%m-%d').replace(tzinfo=timezone.utc)
    return int(dt.timestamp() * 1000)

def extract_channel_data(config):
    """从neticle数据库提取渠道数据"""
    neticle_db, _ = get_database_paths(config)
    
    # 配置参数
    country_id = config['filters']['countryId']
    start_date = config['update']['start_date']
    end_date = config['update']['end_date']
    brands = config['filters']['brands']
    # 使用配置中的展示名做标准化映射，确保后续聚合与展示一致
    brands_display = config['filters']['brands_display']
    # 构建品牌归一化映射：如 'hp' -> 'HP', 'asus' -> 'ASUS'
    brand_norm_map = {b.lower(): d for b, d in zip(brands, brands_display)}
    channel_mapping = config['channels']
    
    # 时间范围转换
    start_ms = to_utc_ms(start_date)
    end_ms = to_utc_ms((datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d'))
    
    # 创建渠道映射字典
    source_to_channel = {}
    for channel, sources in channel_mapping.items():
        for source in sources:
            source_to_channel[source.lower()] = channel
    
    # 查询数据
    with sqlite3.connect(neticle_db) as conn:
        # 获取所有相关数据
        sql = """
        SELECT 
            m.sourceName,
            m.keyword_label,
            COUNT(*) as mention_count,
            SUM(m.sumInteractions) as total_interactions,
            AVG(m.polarity) as avg_sentiment
        FROM mentions_wide m
        WHERE m.countryId = ?
          AND m.createdAtUtcMs >= ? 
          AND m.createdAtUtcMs < ?
          AND m.keyword_label IS NOT NULL
        GROUP BY m.sourceName, m.keyword_label
        ORDER BY m.sourceName, m.keyword_label
        """
        
        df = pd.read_sql_query(sql, conn, params=[country_id, start_ms, end_ms])
    
    # 数据处理
    processed_data = []
    
    for _, row in df.iterrows():
        source_name = row['sourceName'].lower() if row['sourceName'] else ''
        channel = source_to_channel.get(source_name, 'Other')
        
        # 提取并归一化品牌名称
        keyword_label = row['keyword_label']
        brand = None
        for b in brands:
            if keyword_label and b.lower() in keyword_label.lower():
                # 使用映射后的展示名，避免大小写不一致造成聚合漏算
                brand = brand_norm_map.get(b.lower(), b.title())
                break
        
        if brand and channel != 'Other':
            processed_data.append({
                'Channel': channel,
                'Brand': brand,
                'Source': row['sourceName'],
                'Mention_Count': row['mention_count'],
                'Total_Interactions': row['total_interactions'] or 0,
                'Avg_Sentiment': round(row['avg_sentiment'] or 0, 2)
            })
    
    return pd.DataFrame(processed_data)

def calculate_channel_sov(df, config):
    """计算各渠道内的品牌声量份额"""
    brands_display = config['filters']['brands_display']
    channels = config['fill_policy']['channel_order']
    
    # 按渠道和品牌聚合数据
    channel_brand_data = df.groupby(['Channel', 'Brand'])['Mention_Count'].sum().reset_index()
    
    # 计算每个渠道内的SOV
    sov_data = []
    
    for channel in channels:
        channel_data = channel_brand_data[channel_brand_data['Channel'] == channel]
        total_mentions = channel_data['Mention_Count'].sum()
        
        for brand in brands_display:
            brand_mentions = channel_data[channel_data['Brand'] == brand]['Mention_Count'].sum()
            sov = round((brand_mentions / total_mentions * 100), 1) if total_mentions > 0 else 0.0
            
            sov_data.append({
                'Channel': channel,
                'Brand': brand,
                'Mentions': brand_mentions,
                'Total_Channel_Mentions': total_mentions,
                'SOV_Percentage': sov
            })
    
    return pd.DataFrame(sov_data)

def calculate_brand_total_sov(df, config):
    """计算品牌总体声量份额（饼图数据）"""
    brands_display = config['filters']['brands_display']
    
    # 按品牌聚合总提及数
    brand_totals = df.groupby('Brand')['Mention_Count'].sum().reset_index()
    total_mentions = brand_totals['Mention_Count'].sum()
    
    pie_data = []
    for brand in brands_display:
        brand_mentions = brand_totals[brand_totals['Brand'] == brand]['Mention_Count'].sum()
        percentage = round((brand_mentions / total_mentions * 100), 1) if total_mentions > 0 else 0.0
        
        pie_data.append({
            'Brand': brand,
            'Total_Mentions': brand_mentions,
            'Percentage': percentage
        })
    
    return pd.DataFrame(pie_data)

def style_worksheet(ws, title):
    """设置工作表样式"""
    # 标题样式
    title_font = Font(name='Arial', size=14, bold=True, color='FFFFFF')
    title_fill = PatternFill(start_color='366092', end_color='366092', fill_type='solid')
    
    # 表头样式
    header_font = Font(name='Arial', size=11, bold=True, color='FFFFFF')
    header_fill = PatternFill(start_color='4F81BD', end_color='4F81BD', fill_type='solid')
    
    # 数据样式
    data_font = Font(name='Arial', size=10)
    
    # 边框样式
    thin_border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    
    # 设置标题
    ws['A1'] = title
    ws['A1'].font = title_font
    ws['A1'].fill = title_fill
    ws['A1'].alignment = Alignment(horizontal='center', vertical='center')
    
    # 合并标题单元格
    if ws.max_column > 1:
        ws.merge_cells(f'A1:{chr(64 + ws.max_column)}1')
    
    # 设置表头样式
    for cell in ws[2]:
        if cell.value:
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = Alignment(horizontal='center', vertical='center')
            cell.border = thin_border
    
    # 设置数据样式
    for row in ws.iter_rows(min_row=3, max_row=ws.max_row):
        for cell in row:
            if cell.value is not None:
                cell.font = data_font
                cell.border = thin_border
                if isinstance(cell.value, (int, float)):
                    cell.alignment = Alignment(horizontal='right', vertical='center')
                else:
                    cell.alignment = Alignment(horizontal='left', vertical='center')
    
    # 自动调整列宽
    for col_num in range(1, ws.max_column + 1):
        max_length = 0
        column_letter = openpyxl.utils.get_column_letter(col_num)
        
        for row_num in range(1, ws.max_row + 1):
            cell = ws.cell(row=row_num, column=col_num)
            try:
                if cell.value and len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        
        adjusted_width = min(max_length + 2, 30)
        ws.column_dimensions[column_letter].width = adjusted_width

def create_excel_file(config):
    """创建Excel文件"""
    print("正在提取数据...")
    
    # 提取原始数据
    raw_data = extract_channel_data(config)
    
    if raw_data.empty:
        print("警告：未找到符合条件的数据")
        return
    
    print(f"提取到 {len(raw_data)} 条原始数据记录")
    
    # 计算SOV数据
    sov_data = calculate_channel_sov(raw_data, config)
    pie_data = calculate_brand_total_sov(raw_data, config)
    
    # 创建Excel文件
    output_path = ROOT / 'p29_data.xlsx'
    
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        # 写入各个工作表
        raw_data.to_excel(writer, sheet_name='原始数据', index=False, startrow=1)
        sov_data.to_excel(writer, sheet_name='渠道SOV数据', index=False, startrow=1)
        pie_data.to_excel(writer, sheet_name='品牌总体SOV', index=False, startrow=1)
        
        # 获取工作簿对象
        workbook = writer.book
        
        # 设置样式
        style_worksheet(workbook['原始数据'], 'P29 - 原始提及数据')
        style_worksheet(workbook['渠道SOV数据'], 'P29 - 各渠道品牌声量份额')
        style_worksheet(workbook['品牌总体SOV'], 'P29 - 品牌总体声量份额（饼图）')
    
    print(f"Excel文件已生成：{output_path}")
    print(f"- 原始数据：{len(raw_data)} 条记录")
    print(f"- 渠道SOV数据：{len(sov_data)} 条记录")
    print(f"- 品牌总体SOV：{len(pie_data)} 条记录")
    
    return output_path

def main():
    """主函数"""
    try:
        print("开始生成P29页面Excel数据文件...")
        
        # 加载配置
        config = load_config()
        
        # 创建Excel文件
        excel_path = create_excel_file(config)
        
        if excel_path:
            print(f"\n✅ Excel数据文件生成成功：{excel_path}")
            print("\n📋 文件包含以下工作表：")
            print("  1. 原始数据 - 从数据库提取的原始提及数据")
            print("  2. 渠道SOV数据 - 各渠道内品牌声量份额（用于左侧堆叠柱状图）")
            print("  3. 品牌总体SOV - 品牌总体声量份额（用于右侧饼图）")
            print("\n💡 您可以在Excel中检验和修改数据，然后使用fill_from_excel.py脚本将数据填充到PPT中")
        else:
            print("❌ Excel文件生成失败")
            return 1
            
    except Exception as e:
        print(f"❌ 生成Excel文件时发生错误：{e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())