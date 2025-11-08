# P16 项目 - 法国联想市场数据分析

## 项目概述

P16用于生成法国联想品牌的市场声量分析报告，包括主趋势图与渠道分解图。项目从离线数据库提取数据，生成Excel，并自动填充到PPT模板中；同时启用图表缓存自动刷新与自动数据标签，避免手工编辑。

## 项目结构

```
charts/p16/
├── config.yaml           # 项目配置（精简版，仅保留必要项）
├── generate_excel.py     # 数据提取与Excel生成
├── fill_from_excel.py    # PPT模板填充（自动刷新缓存与数据标签）
├── build.py              # 主构建脚本
├── output/               # 输出目录
│   ├── p16_data.xlsx     # 生成的Excel数据
│   └── p16-final.pptx    # 最终PPT文件
├── tmp/                  # 模板解包与重打包临时目录
└── README.md             # 项目文档
```

## 配置说明

### config.yaml 主要配置项（精简版）

```yaml
# 项目路径
project:
  template_ppt: ./p16.pptx
  output_dir: ./output
  tmp_dir: ./tmp
  final_ppt: ./output/p16-final.pptx

# 数据源
data_sources:
  neticle_db: ../../input/neticle-v4-08.sqlite
  metrics_db: ../../input/metrics-v4-08.db

# 过滤条件（法国联想）
filters:
  country_name: "France"
  country_id: 39
  brand_name: "lenovo"
  target_month: "2025-08"

# 渠道映射（示例）
channels:
  Forum:
    - forum
    - forum_aggregator
  Online News:
    - article
    - frontpage
    - article_aggregator
    - frontpage_aggregator
    - comment
    - comment_article
  Blog:
    - blog
    - blog_aggregator
    - comment_blog
  X:
    - twitter
    - twitter_reply
    - twitter_retweet
    - twitter_quoted
  Instagram:
    - instagram
    - instagram_post
    - instagram_comment
    - instagram_reply
  YouTube:
    - youtube
    - video

# 图表映射
chart_mapping:
  chart1:
    file: chart1.xml
    type: main_trend
    description: "主趋势图 - 联想声量份额趋势"
  chart2:
    file: chart2.xml
    type: channel_breakdown
    description: "Forum渠道分解图"
  chart3:
    file: chart3.xml
    type: channel_breakdown
    description: "Online News渠道分解图"
  chart4:
    file: chart4.xml
    type: channel_breakdown
    description: "Blog渠道分解图"
  chart5:
    file: chart5.xml
    type: channel_breakdown
    description: "Instagram渠道分解图"
  chart6:
    file: chart6.xml
    type: channel_breakdown
    description: "YouTube渠道分解图"
  chart7:
    file: chart7.xml
    type: channel_breakdown
    description: "X渠道分解图"
```

> 说明：已移除旧版`time_ranges`、`replace_charts`、`final_mode`、`fill_policy`等未使用配置项；统一通过`filters.target_month`控制目标月份。

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

执行后会在`tmp/`目录展开PPT并更新`ppt/charts/*.xml`：
- 写入`numRef/numCache`以刷新图表缓存，避免“打开不变、编辑才变”。
- 设置`externalData/autoUpdate=1`，引用Excel时自动刷新。
- 启用自动数据标签（显示数值、位置`top`），去除人工文本标签。

## 输出文件

### 1. p16_data.xlsx
包含三个工作表：
- **main_trend**: 主趋势数据（月份、SOV百分比）
- **channel_breakdown**: 渠道分解数据（月份、渠道、SOV百分比）
- **summary**: 数据摘要信息

### 2. p16-final.pptx
基于模板生成的最终PPT，包含自动刷新后的图表与数据标签。

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
- **缺失处理**: 未映射的渠道将被过滤掉

## 依赖要求

```python
pandas>=1.5.0
openpyxl>=3.0.0
python>=3.9（内置sqlite3、zipfile、xml.etree.ElementTree）
```

## 常见问题

1. **数据库连接失败**：检查数据库文件路径是否正确且可读。
2. **图表文件未找到**：确保PPT模板包含对应图表；脚本会继续处理其他部分。
3. **配置文件错误**：确认YAML语法正确、必需项已设置。

## 扩展指南
- 添加新渠道：在`config.yaml`的`channels`部分添加映射
- 添加新图表：在`chart_mapping`中添加新的图表配置
- 更新月份：调整`filters.target_month`

## 提交与推送

### 推送到 GitHub（origin）
```bash
./push.sh "chore: 更新说明或变更内容"
```

### 同时推送到 GitHub 与 Gitee（双远程）
```bash
./push_both.sh "chore: 双远程同步"
```

前置要求：
- 已配置 GitHub 远程：`git remote add origin <github仓库地址>`
- 已配置 Gitee 远程：`git remote add gitee <gitee仓库地址>`

脚本行为说明：
- 两个脚本都会在有变更时自动 `git add -A` 并 `git commit -m "消息"`，无变更则跳过提交。
- `push_both.sh` 会严格校验两个远程是否已配置，未配置时直接报错退出，不进行兜底处理。