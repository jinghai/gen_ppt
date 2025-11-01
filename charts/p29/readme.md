# P29页面 - 联想法国市场媒体渠道声量份额分析

## 页面概述

P29页面展示联想法国市场在各媒体渠道的声量份额分析，包含左侧堆叠柱状图（各渠道品牌SOV）和右侧饼图（品牌总体SOV），为法国市场的媒体渠道策略提供数据支持。

## 图表结构

### 左侧堆叠柱状图 - 各渠道品牌声量份额
- **X轴**: 6个媒体渠道（Online News, Forum, Blog, X, Instagram, YouTube）
- **Y轴**: 声量份额百分比（0-100%）
- **系列**: 7个品牌（Lenovo, Dell, HP, ASUS, Acer, Apple, Samsung）
- **数据来源**: neticle数据库mentions_wide表

### 右侧饼图 - 品牌总体声量份额
- **数据**: 各品牌在所有渠道的总体声量占比
- **标签**: 品牌名称 + 百分比
- **数据来源**: 聚合所有渠道的品牌提及数

## 数据处理流程

### 1. 数据提取 (`generate_excel.py`)
**功能**: 从neticle数据库提取法国市场数据并生成Excel文件
- **输入**: neticle-v5.sqlite数据库
- **筛选条件**: 
  - 国家: 法国 (countryId = 39)
  - 时间: 2025年8月 (start_date: 2025-07-31 22:00:00, end_date: 2025-08-31 21:59:08)
  - 品牌: Lenovo, Dell, HP, ASUS, Acer, Apple, Samsung
- **输出**: `p29_data.xlsx` (包含4个工作表：Sheet1、渠道SOV数据、品牌总体SOV、原始统计)

### 2. PPT生成 (`fill_from_excel.py`)
**功能**: 基于Excel数据和PPT模板生成最终演示文稿
- **输入**: `p29_data.xlsx` + `p29.pptx`模板
- **处理**: 更新图表数据、嵌入Excel数据源、应用Excel样式增强
- **输出**: `p29-final.pptx` (可在PowerPoint中编辑的最终文件)

#### Excel样式增强功能
- **字体颜色自动对比**: 根据背景色亮度自动选择黑色或白色字体，确保可读性
  - 使用W3C亮度计算公式: `(R*299 + G*587 + B*114) / 1000`
  - 亮度 > 128 使用黑色字体，否则使用白色字体
- **品牌底色映射**: 单元格背景色与config.yaml中的brand_colors配置保持一致
- **字体加粗**: 重要数据使用加粗字体突出显示

## 渠道映射规则

### 源渠道 → 目标渠道
| 源渠道 (sources.name) | 目标渠道 | 说明 |
|---------------------|---------|------|
| article | Online News | 在线新闻文章 |
| frontpage | Online News | 新闻首页 |
| forum | Forum | 论坛讨论 |
| blog | Blog | 博客文章 |
| twitter | X | Twitter/X平台 |
| instagram | Instagram | Instagram平台 |
| video | YouTube | 视频平台 |
| facebook | (排除) | 不包含在分析中 |
| linkedin | (排除) | 不包含在分析中 |
| tiktok | (排除) | 不包含在分析中 |
| googleplus | (排除) | 不包含在分析中 |

## 文件结构

### 核心文件
- `generate_excel.py`: 数据提取和Excel生成脚本
- `fill_from_excel.py`: PPT生成脚本  
- `p29_data.xlsx`: 中间数据文件（供人工检验）
- `p29-final.pptx`: 最终PPT输出文件
- `需求.md`: 详细需求文档

### 配置文件
- `config.yaml`: 全局配置（品牌、时间、数据库路径等）
- `chart115/data.json`: 图表数据文件
- `chart115/final_data.json`: 最终图表数据

### 模板文件
- `template/p29.pptx`: PPT模板（不可修改）

## 使用说明

### 一键构建（推荐）
```bash
# 进入P29目录
cd charts/p29

# 执行一键构建脚本
python build.py
```

该脚本将自动完成以下步骤：
1. 执行数据提取和Excel生成（`generate_excel.py`）
2. 执行PPT生成（`fill_from_excel.py`）
3. 验证输出文件

### 分步执行
如需分步执行或调试，可以单独运行：

#### 步骤1: 生成Excel数据文件
```bash
cd /Users/jinghai/coder/gen_ppt/charts/p29
python generate_excel.py
```
- 输出: `p29_data.xlsx` (包含3个工作表)
- 可手动检验和修改数据

#### 步骤2: 生成最终PPT
```bash
python fill_from_excel.py
```
- 输入: `p29_data.xlsx` + `template/p29.pptx`
- 输出: `p29-final.pptx` (可在PowerPoint中编辑)

### 输出文件
- **Excel数据文件**: `p29_data.xlsx` - 包含4个工作表（Sheet1、渠道SOV数据、品牌总体SOV、原始统计）
  - **Sheet1**: 主要数据展示，包含品牌颜色映射和字体对比优化
  - **渠道SOV数据**: 各渠道内品牌声量份额数据
  - **品牌总体SOV**: 品牌整体声量份额数据  
  - **原始统计**: 原始提及数统计数据
- **最终PPT文件**: `output/p29-final.pptx` - 包含左右两个图表的完整PPT

### 数据验证
- **原始数据**: 44条记录 (各渠道各品牌的提及数)
- **渠道SOV数据**: 42条记录 (6个渠道 × 7个品牌)
- **品牌总体SOV**: 7条记录 (7个品牌的总体占比)
- **Excel样式**: 自动应用品牌颜色和字体对比优化

### 注意事项
- 模板文件 `template/p29.pptx` 不可修改
- 生成的PPT文件可在PowerPoint中正常编辑
- Excel文件支持人工检验和数据调整
- 所有时间均为UTC时间戳格式

## 技术实现细节

### 数据库查询逻辑
```sql
-- 提取法国市场2025年8月数据
SELECT m.*, s.name as source_name, k.keyword_label as brand
FROM mentions_wide m
JOIN sources s ON m.sourceId = s.id  
JOIN keywords k ON m.keywordId = k.id
WHERE m.countryId = 39 
  AND m.date >= 1722459600000  -- 2025-07-31 22:00:00 UTC
  AND m.date <= 1725145148000  -- 2025-08-31 21:59:08 UTC
  AND k.keyword_label IN ('Lenovo-FR-V5', 'Dell-FR-V5', ...)
```

### SOV计算公式
```python
# 渠道内品牌SOV
channel_sov = (brand_mentions_in_channel / total_mentions_in_channel) * 100

# 品牌总体SOV  
brand_sov = (brand_total_mentions / all_brands_total_mentions) * 100
```

### PPT数据嵌入
- 使用python-pptx库更新图表数据
- 保持原始PPT格式和样式
- 支持PowerPoint原生编辑功能
- Excel数据源包含品牌颜色映射和字体优化

## 与多图表页面的对比

### 优势
- **加载速度**: 最快的数据加载和图表渲染速度
- **资源效率**: 最低的内存和CPU占用
- **维护成本**: 最简单的代码结构和维护需求
- **用户体验**: 最直观的信息展示，无认知负担

### 适用场景
- **高层汇报**: 适合向高层管理者展示核心竞争态势
- **移动查看**: 在移动设备上查看关键指标
- **快速决策**: 需要基于核心数据快速做出决策
- **系统监控**: 作为监控系统的核心指标展示

### 局限性
- **信息深度**: 无法提供趋势分析和时间序列洞察
- **对比维度**: 缺少多维度的对比分析能力
- **详细程度**: 不适合需要详细分析的业务场景
