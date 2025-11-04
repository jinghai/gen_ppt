# P16 项目 - 法国联想市场数据分析

## 项目概述

P16项目专门用于生成法国联想品牌的市场声量分析报告，包括主趋势图表和渠道分解图表。项目从多个数据源提取数据，生成Excel数据文件，并自动填充到PowerPoint模板中。

## 项目结构

```
charts/p16/
├── config.yaml           # 项目配置文件
├── generate_excel.py     # 数据提取和Excel生成脚本
├── fill_from_excel.py    # PPT模板填充脚本
├── build.py             # 主构建脚本
├── output/              # 输出目录
│   ├── p16_data.xlsx    # 生成的Excel数据文件
│   └── p16-final.pptx   # 最终PPT文件
├── tmp/                 # 临时文件目录
└── README.md           # 项目文档
```

## 数据源

### 1. metrics-v4-08.db
- **表**: `brand_metrics_month`
- **用途**: 提供月度品牌指标数据
- **关键字段**: `countryId`, `brandId`, `month`, `sov`

### 2. neticle-v4-08.sqlite
- **表**: `mentions_wide`
- **用途**: 提供原始提及数据，用于渠道分解分析
- **关键字段**: `countryId`, `brandId`, `sourceLabel`, `month`, `mentions`

## 配置说明

### config.yaml 主要配置项

```yaml
project:
  name: "p16"
  description: "法国联想市场数据分析"

data_sources:
  neticle_db: "../../data/neticle-v4-08.sqlite"
  metrics_db: "../../data/metrics-v4-08.db"

filters:
  country: "France"
  country_id: 39
  brand: "lenovo"
  brand_id: 1

channels:
  Forum: ["forum"]
  Online News: ["article", "frontpage"]
  Blog: ["blog"]
  X: ["twitter"]
  Instagram: ["instagram"]
  YouTube: ["video"]

chart_mapping:
  main_trend:
    file: "chart23"
    type: "line"
    description: "主趋势图表"
  forum:
    file: "chart22"
    type: "line"
    description: "论坛渠道趋势"
  # ... 其他图表映射

time_ranges:
  main_trend:
    start_month: "2025-03"
    end_month: "2025-08"
  channel_breakdown:
    start_month: "2025-05"
    end_month: "2025-08"
```

## 使用方法

### 1. 构建完整报告
```bash
python build.py build
```

### 2. 清理临时文件
```bash
python build.py clean
```

### 3. 查看帮助
```bash
python build.py help
```

### 4. 单独运行组件

#### 生成Excel数据文件
```bash
python generate_excel.py
```

#### 填充PPT模板
```bash
python fill_from_excel.py
```

## 输出文件

### 1. p16_data.xlsx
包含三个工作表：
- **main_trend**: 主趋势数据（月份、SOV百分比）
- **channel_breakdown**: 渠道分解数据（月份、渠道、SOV百分比）
- **summary**: 数据摘要信息

### 2. p16-final.pptx
基于模板生成的最终PowerPoint演示文稿，包含更新的图表数据。

## 数据计算逻辑

### SOV (Share of Voice) 计算
```
SOV = (品牌提及数 / 总提及数) × 100%
```

### 渠道SOV计算
1. 根据`sourceLabel`映射到对应渠道
2. 按渠道聚合提及数
3. 计算每个渠道的SOV百分比

### 数据填充策略
- **真实数据**: 从数据库中提取的实际数据
- **模板数据**: 当数据库中缺少数据时，使用配置文件中的模板值
- **缺失处理**: 未映射的渠道将被过滤掉

### 图表显示策略
- 默认禁用自动数据标签（不显示数值标签），以保证视觉简洁
- 保留`numCache`百分比格式（`0%`），并开启`externalData.autoUpdate=1`，确保打开PPT时自动刷新嵌入数据

## 依赖要求

```python
pandas>=1.5.0
sqlite3 (内置)
openpyxl>=3.0.0
zipfile (内置)
xml.etree.ElementTree (内置)
```

## 错误处理

### 常见问题及解决方案

1. **数据库连接失败**
   - 检查数据库文件路径是否正确
   - 确认数据库文件存在且可读

2. **图表文件未找到**
   - 这是正常现象，脚本会继续处理其他部分
   - 确保PPT模板包含正确的图表文件

3. **配置文件错误**
   - 检查YAML语法是否正确
   - 确认所有必需的配置项都已设置

## 开发说明

### 代码结构
- **generate_excel.py**: 数据提取和Excel生成逻辑
- **fill_from_excel.py**: PPT模板处理和数据填充
- **build.py**: 主控制脚本，整合所有流程

### 扩展指南
1. 添加新渠道：在`config.yaml`的`channels`部分添加映射
2. 修改时间范围：更新`time_ranges`配置
3. 添加新图表：在`chart_mapping`中添加新的图表配置

## 版本历史

- **v1.0**: 初始版本，支持基本的数据提取和PPT生成
- **v1.1**: 优化渠道映射逻辑，改进错误处理
- **v1.2**: 添加数据验证和清理功能

## 联系信息

如有问题或建议，请联系开发团队。
