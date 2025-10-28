# P14页面 - 品牌SOV与趋势分析

## 页面概述

P14页面包含5个图表，遵循标准的品牌声量份额(SOV)和趋势分析模式。

## 图表配置

### 主要图表类型
- **类别图**: 7品牌SOV分析（饼图/柱状图/面积图/环形图）
- **趋势图**: Lenovo vs Others 日级对比（散点图/折线图）

## 数据源与字段

### 核心数据表
1. **brand_metrics_month**: 月度品牌指标聚合表
2. **brand_metrics_day**: 日度品牌指标明细表

### 关键字段
- brand_mentions: 品牌提及数
- total_mentions: 总提及数  
- countryId: 国家标识
- month/day: 时间维度
- brand: 品牌名称

## 计算公式

### SOV计算
SOV = (品牌提及数 / 总提及数) * 100

### 趋势分析
- Lenovo声量 vs 其他品牌合计声量
- 按日级数据生成时间序列

## 缺失数据处理

- 使用 original_*.json 缓存文件作为兜底
- 确保图表始终有数据显示
- 保持PPT完整性

## 构建命令

cd charts/P14
python make_data.py
python build.py

## 业务价值

- **市场份额分析**: 品牌声量占比
- **竞争态势监控**: 相对市场地位
- **趋势变化追踪**: 时间序列分析
- **策略决策支持**: 数据驱动洞察
