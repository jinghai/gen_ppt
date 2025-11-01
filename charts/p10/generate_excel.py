#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P10 数据生成脚本 - 从数据库提取法国Lenovo情感分析数据生成Excel
基于页面级配置，独立运行，不依赖全局配置
"""

import sqlite3
import pandas as pd
import yaml
import logging
import os
from datetime import datetime, timedelta
from pathlib import Path
import sys

class P10DataGenerator:
    """P10页面数据生成器"""
    
    def __init__(self, config_path="config.yaml"):
        """初始化数据生成器"""
        self.config_path = config_path
        self.config = self._load_config()
        self._setup_logging()
        self.logger = logging.getLogger(__name__)
        
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
        
    def _get_db_connection(self, db_type='neticle'):
        """获取数据库连接"""
        db_path = self.config['data_sources'][f'{db_type}_db']
        if not os.path.exists(db_path):
            raise FileNotFoundError(f"数据库文件不存在: {db_path}")
        return sqlite3.connect(db_path)
        
    def _convert_timestamp_to_date(self, timestamp_ms):
        """将毫秒时间戳转换为日期字符串"""
        try:
            # 转换毫秒时间戳为datetime对象
            dt = datetime.fromtimestamp(timestamp_ms / 1000)
            return dt.strftime('%Y-%m-%d')
        except Exception as e:
            self.logger.warning(f"时间戳转换失败: {timestamp_ms}, 错误: {e}")
            return None
            
    def extract_sentiment_data(self):
        """从数据库提取情感分析数据"""
        self.logger.info("开始提取情感分析数据...")
        
        # 构建SQL查询
        filters = self.config['filters']
        update_config = self.config['update']
        
        # 时间范围转换为毫秒时间戳
        start_date = datetime.strptime(update_config['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(update_config['end_date'], '%Y-%m-%d') + timedelta(days=1)  # 包含结束日期
        start_timestamp = int(start_date.timestamp() * 1000)
        end_timestamp = int(end_date.timestamp() * 1000)
        
        query = f"""
        SELECT 
            id,
            polarity,
            createdAtUtcMs,
            keyword_label,
            countryId
        FROM mentions_wide 
        WHERE countryId = {filters['countryId']}
          AND keyword_label LIKE '{filters['keyword_pattern']}'
          AND createdAtUtcMs >= {start_timestamp}
          AND createdAtUtcMs < {end_timestamp}
        ORDER BY createdAtUtcMs
        """
        
        try:
            conn = self._get_db_connection('neticle')
            df = pd.read_sql_query(query, conn)
            conn.close()
            
            self.logger.info(f"成功提取 {len(df)} 条记录")
            
            # 数据质量检查
            if len(df) < self.config['quality']['min_records']:
                self.logger.warning(f"数据量不足：{len(df)} < {self.config['quality']['min_records']}")
                
            return df
            
        except Exception as e:
            self.logger.error(f"数据提取失败: {e}")
            raise
            
    def process_sentiment_classification(self, df):
        """处理情感分类"""
        self.logger.info("开始处理情感分类...")
        
        sentiment_config = self.config['sentiment']
        
        # 添加日期列
        df['date'] = df['createdAtUtcMs'].apply(self._convert_timestamp_to_date)
        df = df.dropna(subset=['date'])  # 移除日期转换失败的记录
        
        # 情感分类
        def classify_sentiment(polarity):
            if polarity > 0:
                return 'Positive'
            elif polarity == 0:
                return 'Neutral'
            else:
                return 'Negative'
                
        df['sentiment'] = df['polarity'].apply(classify_sentiment)
        
        self.logger.info(f"情感分布: {df['sentiment'].value_counts().to_dict()}")
        return df
        
    def generate_pie_chart_data(self, df):
        """生成饼图数据"""
        self.logger.info("生成饼图数据...")
        
        # 计算情感分布
        sentiment_counts = df['sentiment'].value_counts()
        total_count = len(df)
        
        # 按配置顺序生成数据
        labels = self.config['charts']['pie_chart']['labels']
        pie_data = []
        
        for label in labels:
            count = sentiment_counts.get(label, 0)
            percentage = (count / total_count * 100) if total_count > 0 else 0
            pie_data.append({
                'Sentiment': label,
                'Count': count,
                'Percentage': round(percentage, 1)
            })
            
        pie_df = pd.DataFrame(pie_data)
        
        # 验证百分比总和
        if self.config['quality']['validate_percentages']:
            total_percentage = pie_df['Percentage'].sum()
            if abs(total_percentage - 100.0) > 0.1:
                self.logger.warning(f"百分比总和异常: {total_percentage}%")
                
        self.logger.info(f"饼图数据: {pie_df.to_dict('records')}")
        return pie_df
        
    def generate_line_chart_data(self, df):
        """生成折线图数据"""
        self.logger.info("生成折线图数据...")
        
        # 按日期和情感分组统计
        daily_sentiment = df.groupby(['date', 'sentiment']).size().unstack(fill_value=0)
        
        # 计算每日总数和百分比
        daily_sentiment['Total'] = daily_sentiment.sum(axis=1)
        
        # 生成完整日期范围
        start_date = datetime.strptime(self.config['update']['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(self.config['update']['end_date'], '%Y-%m-%d')
        date_range = pd.date_range(start=start_date, end=end_date, freq='D')
        date_strings = [d.strftime('%Y-%m-%d') for d in date_range]
        
        # 创建完整的数据框架
        labels = self.config['charts']['line_chart']['lines']
        line_data = []
        
        for date_str in date_strings:
            row_data = {'Date': date_str}
            
            if date_str in daily_sentiment.index:
                total = daily_sentiment.loc[date_str, 'Total']
                for label in labels:
                    count = daily_sentiment.loc[date_str, label] if label in daily_sentiment.columns else 0
                    percentage = (count / total * 100) if total > 0 else 0
                    row_data[label] = round(percentage, 1)
            else:
                # 缺失日期填充0
                for label in labels:
                    row_data[label] = 0.0
                    
            line_data.append(row_data)
            
        line_df = pd.DataFrame(line_data)
        
        # 检查缺失天数
        missing_days = len([d for d in date_strings if d not in daily_sentiment.index])
        if missing_days > self.config['quality']['max_missing_days']:
            self.logger.warning(f"缺失天数过多: {missing_days} > {self.config['quality']['max_missing_days']}")
            
        self.logger.info(f"折线图数据生成完成，共 {len(line_df)} 天")
        return line_df
        
    def save_to_excel(self, pie_df, line_df):
        """保存数据到Excel文件"""
        self.logger.info("保存数据到Excel文件...")
        
        output_file = self.config['output']['excel_file']
        
        try:
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                # 保存饼图数据
                pie_sheet = self.config['charts']['pie_chart']['sheet_name']
                pie_df.to_excel(writer, sheet_name=pie_sheet, index=False)
                
                # 保存折线图数据
                line_sheet = self.config['charts']['line_chart']['sheet_name']
                line_df.to_excel(writer, sheet_name=line_sheet, index=False)
                
                # 添加元数据工作表
                metadata = {
                    'Generated': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
                    'Config': [self.config_path],
                    'Data_Range': [f"{self.config['update']['start_date']} to {self.config['update']['end_date']}"],
                    'Country': [self.config['filters']['country_name']],
                    'Brand': [self.config['filters']['brand_key']],
                    'Total_Records': [len(pie_df) if not pie_df.empty else 0]
                }
                metadata_df = pd.DataFrame(metadata)
                metadata_df.to_excel(writer, sheet_name='Metadata', index=False)
                
            self.logger.info(f"Excel文件已保存: {output_file}")
            
        except Exception as e:
            self.logger.error(f"保存Excel文件失败: {e}")
            raise
            
    def run(self):
        """执行完整的数据生成流程"""
        try:
            self.logger.info("=== P10 数据生成开始 ===")
            
            # 1. 提取原始数据
            raw_df = self.extract_sentiment_data()
            
            # 2. 处理情感分类
            processed_df = self.process_sentiment_classification(raw_df)
            
            # 3. 生成饼图数据
            pie_df = self.generate_pie_chart_data(processed_df)
            
            # 4. 生成折线图数据
            line_df = self.generate_line_chart_data(processed_df)
            
            # 5. 保存到Excel
            self.save_to_excel(pie_df, line_df)
            
            self.logger.info("=== P10 数据生成完成 ===")
            return True
            
        except Exception as e:
            self.logger.error(f"数据生成失败: {e}")
            return False

def main():
    """主函数"""
    # 确保在正确的目录下运行
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # 创建输出目录
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # 运行数据生成器
    generator = P10DataGenerator()
    success = generator.run()
    
    if success:
        print("✅ P10 数据生成成功！")
        return 0
    else:
        print("❌ P10 数据生成失败！")
        return 1

if __name__ == "__main__":
    sys.exit(main())