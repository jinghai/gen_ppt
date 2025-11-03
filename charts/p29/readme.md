# P29 页面 - Lenovo France 媒体渠道声量份额分析

## 页面概述

P29页面用于分析Lenovo France在不同媒体渠道的声量份额（Share of Voice, SOV），通过堆叠柱状图和饼图展示品牌在各渠道的表现。

## 图表结构

### 1. 堆叠柱状图 - 渠道声量份额
- **X轴**: 6个目标渠道（Forum, Online News, Blog, X, Instagram, YouTube）
- **Y轴**: 声量份额百分比（0-100%）
- **数据层**: 按品牌堆叠，显示每个品牌在各渠道的份额
- **颜色**: 使用品牌专属颜色（config.yaml中定义）
- **数据标签**: 
  - 格式："0%"（整数百分比）
  - 颜色：Apple品牌使用黑色，其他品牌使用白色
  - 小于min_label_percent的标签可选择隐藏

### 2. 饼图 - 整体品牌声量份额
- **数据**: 所有渠道汇总的品牌声量份额
- **颜色**: 与堆叠柱状图保持一致的品牌颜色
- **数据标签**: 百分比格式，使用最大余数法确保总和为100%

## 数据处理流程

### 1. 数据提取 (`generate_excel.py`)
- **数据源**: 
  - Neticle数据库: `../../input/neticle-v4-08.sqlite`
  - Metrics数据库: `../../input/metrics-v4-08.db`
- **查询范围**: 2025年8月（UTC时间戳转换）
- **过滤条件**: 
  - 国家: France
  - 品牌: 基于keyword_label小写部分匹配
- **渠道映射**: 基于sourceName字段映射到6个目标渠道
- **SOV计算**: 
  - 渠道级别: 品牌提及数 / 渠道总提及数 × 100%
  - 整体级别: 品牌总提及数 / 全部总提及数 × 100%
  - 使用最大余数法确保百分比总和为100%

### 2. Excel生成
生成包含4个工作表的Excel文件：
- **Sheet1**: 堆叠柱状图数据（品牌×渠道矩阵）
- **Sheet2**: 饼图数据（品牌总份额）
- **Sheet3**: 原始提及数数据（调试用）
- **Sheet4**: 渠道映射统计（验证用）

### 3. PPT生成 (`fill_from_excel.py`)
- **模板读取**: 解压p29.pptx模板文件
- **数据嵌入**: 将Excel数据嵌入到PPT的图表数据源
- **样式应用**: 
  - 品牌颜色配置（16进制颜色码）
  - 数据标签格式化和颜色设置
  - bestFit字体大小调整
- **文件打包**: 重新打包为可编辑的PPT文件

## 渠道映射规则

基于sourceName字段（不区分大小写）映射：
- **Forum**: forum
- **Online News**: news, online news
- **Blog**: blog
- **X**: x, twitter
- **Instagram**: instagram
- **YouTube**: youtube
- **其他**: 未匹配的源归类为"Other"

## 文件结构

```
charts/p29/
├── config.yaml          # 配置文件
├── generate_excel.py    # 数据生成脚本
├── fill_from_excel.py   # PPT填充脚本
├── p29.pptx            # PPT模板（只读）
├── p29_data.xlsx       # 生成的数据文件
├── 需求.md              # 需求文档
├── readme.md           # 说明文档
├── tmp/                # 临时文件目录
│   ├── chart_data.json # 图表数据缓存
│   └── ppt_extracted/  # PPT解压文件
└── output/
    └── p29-final.pptx  # 最终输出文件
```

## 使用方法

### 一键构建
```bash
cd charts/p29
python generate_excel.py && python fill_from_excel.py
```

### 分步执行
```bash
# 1. 生成Excel数据文件
python generate_excel.py

# 2. 生成最终PPT文件
python fill_from_excel.py
```

## 输出文件

1. **p29_data.xlsx**: 包含图表数据的Excel文件
2. **output/p29-final.pptx**: 最终的PowerPoint演示文件

## 数据验证

- 每个渠道的品牌份额总和为100%（允许四舍五入误差）
- 整体品牌份额总和严格为100%（最大余数法保证）
- 支持空数据处理（total_mentions为0时SOV为0.0）
- 临时文件保留用于调试和验证

## 技术实现细节

### 数据库查询
- 使用pandas读取SQLite数据库
- 时间范围过滤基于UTC时间戳转换
- 品牌匹配使用小写部分字符串匹配
- 渠道映射基于sourceName字段

### SOV计算
- 渠道SOV = 品牌在该渠道的提及数 / 该渠道总提及数 × 100%
- 整体SOV = 品牌总提及数 / 全部品牌总提及数 × 100%
- 使用最大余数法处理四舍五入，确保总和为100%

### PPT数据嵌入
- 解压PPT文件到临时目录
- 修改chart/data.xlsx中的数据
- 更新图表样式和颜色配置
- 重新打包为完整的PPT文件

## 与多图表页面的区别

P29页面是单一数据源的双图表页面，相比多图表页面：
- **数据源**: 单一Neticle数据库查询
- **图表类型**: 固定的堆叠柱状图+饼图组合
- **数据处理**: 统一的SOV计算逻辑
- **配置复杂度**: 相对简单的渠道映射和品牌配置
- **输出格式**: 单一PPT文件，包含嵌入的Excel数据源
