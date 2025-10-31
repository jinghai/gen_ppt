#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P29页面PPT数据填充器
从Excel文件读取数据并填充到PPT模板中
"""

import json
import pandas as pd
import yaml
from pathlib import Path
import shutil
import zipfile
import tempfile
from lxml import etree
import openpyxl

# 项目路径配置
ROOT = Path(__file__).resolve().parent

def load_config():
    """加载页面级配置文件"""
    config_path = ROOT / 'config.yaml'
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config

def read_excel_data(excel_path):
    """从Excel文件读取数据"""
    if not excel_path.exists():
        raise FileNotFoundError(f"Excel文件不存在：{excel_path}")
    
    # 读取各个工作表，跳过标题行
    sov_data = pd.read_excel(excel_path, sheet_name='渠道SOV数据', skiprows=1)
    pie_data = pd.read_excel(excel_path, sheet_name='品牌总体SOV', skiprows=1)
    
    return sov_data, pie_data

def prepare_chart_data(sov_data, pie_data, config):
    """准备图表数据格式"""
    channels = config['fill_policy']['channel_order']
    brands_display = config['filters']['brands_display']
    
    # 准备左侧堆叠柱状图数据
    chart_labels = channels
    chart_series = []
    
    for brand in brands_display:
        brand_data = sov_data[sov_data['Brand'] == brand]
        values = []
        
        for channel in channels:
            channel_data = brand_data[brand_data['Channel'] == channel]
            if not channel_data.empty:
                values.append(float(channel_data['SOV_Percentage'].iloc[0]))
            else:
                values.append(0.0)
        
        chart_series.append({
            'name': brand,
            'values': values
        })
    
    # 准备右侧饼图数据
    pie_labels = []
    pie_values = []
    
    for _, row in pie_data.iterrows():
        if row['Percentage'] > 0:  # 只包含有数据的品牌
            pie_labels.append(row['Brand'])
            pie_values.append(float(row['Percentage']))
    
    return {
        'bar_chart': {
            'labels': chart_labels,
            'series': chart_series
        },
        'pie_chart': {
            'labels': pie_labels,
            'values': pie_values
        }
    }

def update_chart_data_json(chart_data):
    """准备图表数据（不再依赖chart115目录）"""
    # 写入堆叠柱状图数据
    bar_data = {
        'labels': chart_data['bar_chart']['labels'],
        'series': chart_data['bar_chart']['series']
    }
    
    # 创建临时目录保存数据（如果需要的话）
    temp_dir = ROOT / 'tmp'
    temp_dir.mkdir(exist_ok=True)
    
    # 可选：保存数据到临时文件用于调试
    temp_data_path = temp_dir / 'chart_data.json'
    with open(temp_data_path, 'w', encoding='utf-8') as f:
        json.dump(bar_data, f, ensure_ascii=False, indent=2)
    
    print(f"图表数据已准备完成，临时保存到：{temp_data_path}")
    return bar_data

def extract_ppt_template():
    """解压PPT模板到临时目录"""
    template_ppt = ROOT / 'p29.pptx'
    if not template_ppt.exists():
        raise FileNotFoundError(f"PPT模板不存在：{template_ppt}")
    
    # 创建临时目录
    temp_dir = ROOT / 'tmp'
    temp_dir.mkdir(exist_ok=True)
    
    # 解压PPT
    extract_dir = temp_dir / 'ppt_extracted'
    if extract_dir.exists():
        shutil.rmtree(extract_dir)
    
    with zipfile.ZipFile(template_ppt, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    
    print(f"PPT模板已解压到：{extract_dir}")
    return extract_dir

def update_embedded_excel(extract_dir, chart_data):
    """更新嵌入的Excel文件"""
    # 查找嵌入的Excel文件
    embeddings_dir = extract_dir / 'ppt' / 'embeddings'
    if not embeddings_dir.exists():
        print("警告：未找到embeddings目录")
        return
    
    # 查找.xlsb或.xlsx文件
    excel_files = list(embeddings_dir.glob('*.xlsx')) + list(embeddings_dir.glob('*.xlsb'))
    if not excel_files:
        print("警告：未找到嵌入的Excel文件")
        return
    
    # 使用第一个Excel文件
    original_excel_file = excel_files[0]
    print(f"找到嵌入的Excel文件：{original_excel_file}")
    
    # 如果是.xlsb文件，我们需要创建一个新的.xlsx文件来替换它
    if original_excel_file.suffix.lower() == '.xlsb':
        new_excel_file = embeddings_dir / 'Workbook1.xlsx'
        print(f"将.xlsb文件替换为.xlsx文件：{new_excel_file}")
        
        # 更新关系文件中的引用
        chart_rels_file = extract_dir / 'ppt' / 'charts' / '_rels' / 'chart1.xml.rels'
        if chart_rels_file.exists():
            with open(chart_rels_file, 'r', encoding='utf-8') as f:
                rels_content = f.read()
            
            # 替换.xlsb为.xlsx
            rels_content = rels_content.replace('Workbook1.xlsb', 'Workbook1.xlsx')
            
            with open(chart_rels_file, 'w', encoding='utf-8') as f:
                f.write(rels_content)
            print("已更新图表关系文件中的引用")
        
        # 删除原始.xlsb文件
        original_excel_file.unlink()
        excel_file = new_excel_file
    else:
        excel_file = original_excel_file
    
    try:
        # 创建新的Excel工作簿
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = 'Sheet1'
        
        # 写入新的堆叠柱状图数据
        channels = chart_data['bar_chart']['labels']
        series_data = chart_data['bar_chart']['series']
        
        # 写入表头：第一列是渠道，其余列是品牌
        ws.cell(row=1, column=1, value='Channel')
        for col_idx, series in enumerate(series_data):
            ws.cell(row=1, column=col_idx + 2, value=series['name'])
        
        # 写入数据
        for row_idx, channel in enumerate(channels):
            ws.cell(row=row_idx + 2, column=1, value=channel)
            
            for col_idx, series in enumerate(series_data):
                value = series['values'][row_idx]
                ws.cell(row=row_idx + 2, column=col_idx + 2, value=value)
        
        # 保存Excel文件
        wb.save(excel_file)
        print(f"已更新嵌入的Excel文件：{excel_file}")
        
        # 显示更新后的数据预览
        print("更新后的数据预览：")
        print(f"渠道数量: {len(channels)}")
        print(f"品牌数量: {len(series_data)}")
        print("前几行数据：")
        for i, channel in enumerate(channels[:3]):
            row_data = [channel] + [series['values'][i] for series in series_data]
            print(f"  {row_data}")
        
    except Exception as e:
        print(f"更新嵌入Excel文件时出错：{e}")
        import traceback
        traceback.print_exc()

def repack_ppt(extract_dir, output_path):
    """重新打包PPT文件"""
    print(f"正在重新打包PPT到：{output_path}")
    
    # 确保输出目录存在
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # 创建新的ZIP文件
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
        for file_path in extract_dir.rglob('*'):
            if file_path.is_file():
                # 计算相对路径
                arcname = file_path.relative_to(extract_dir)
                zip_ref.write(file_path, arcname)
    
    print(f"PPT文件已生成：{output_path}")

def main():
    """主函数"""
    try:
        print("开始从Excel数据生成PPT...")
        
        # 清理之前的临时文件
        temp_dir = ROOT / 'tmp'
        if temp_dir.exists():
            shutil.rmtree(temp_dir)
            print("已清理之前的临时文件")
        
        # 加载配置
        config = load_config()
        
        # 检查Excel文件
        excel_path = ROOT / 'p29_data.xlsx'
        if not excel_path.exists():
            print(f"❌ Excel数据文件不存在：{excel_path}")
            print("请先运行 generate_excel.py 生成Excel数据文件")
            return 1
        
        # 读取Excel数据
        print("正在读取Excel数据...")
        sov_data, pie_data = read_excel_data(excel_path)
        
        # 准备图表数据
        print("正在准备图表数据...")
        chart_data = prepare_chart_data(sov_data, pie_data, config)
        
        # 更新JSON数据文件
        print("正在更新图表数据文件...")
        update_chart_data_json(chart_data)
        
        # 解压PPT模板
        print("正在解压PPT模板...")
        extract_dir = extract_ppt_template()
        
        # 更新嵌入的Excel文件
        print("正在更新嵌入的Excel数据...")
        update_embedded_excel(extract_dir, chart_data)
        
        # 重新打包PPT
        output_dir = ROOT / 'output'
        output_path = output_dir / 'p29-final.pptx'
        repack_ppt(extract_dir, output_path)
        
        print(f"\n✅ PPT文件生成成功：{output_path}")
        print("\n📊 生成的PPT包含：")
        print("  - 左侧：各渠道品牌声量份额堆叠柱状图")
        print("  - 右侧：品牌总体声量份额饼图")
        print("  - 嵌入的Excel数据已更新，可在PowerPoint中编辑")
        
        # 保留临时文件用于调试
        temp_dir = ROOT / 'tmp'
        if temp_dir.exists():
            print(f"临时文件已保留在：{temp_dir}")
            print("  - chart_data.json: 图表数据")
            print("  - ppt_extracted/: 解压的PPT内容")
        
        return 0
        
    except Exception as e:
        print(f"❌ 生成PPT时发生错误：{e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    exit(main())