# P18页面 - Lenovo Net Lovers（法国）

## 页面说明
- 模板：`charts/p18/p18.pptx`（不可修改模板本体，页面级脚本仅替换数据）
- 输出：`charts/p18/output/p18-final.pptx`（单页，可在 PPT 编辑器内查看和修改内嵌数据）
- 附图解释：`charts/p18/p18-图表解释.md`（仅描述结构与数据对应）
- 详细需求：`charts/p18/需求.md`

## 配置参数（config.yaml）
```yaml
# 数据源配置（路径相对页面目录解析，建议使用绝对路径）
data_sources:
  neticle_db: "input/neticle-v4-08.sqlite"
  neticle_table: "mentions_wide"
  date_column: "createdAtUtcMs"         # 日期字段；支持文本/epoch(ms)
  country_column: "countryId" # 国家字段，仅此字段

# 品牌过滤配置
filters:
  country_id: 39                # 法国
  country_name: "France"
  brand_key: "Lenovo"          # 主品牌（大小写不敏感）
  keyword_like: "%lenovo%"     # Lenovo 的 LIKE 模式

# 情感阈值配置（按代码使用）
sentiment:
  thresholds:
    column: "polarity"         # 情感列名
    positive_min: 0.33
    negative_max: -0.33

# 月份配置（可选）
months:
  main: ["2025-07","2025-08","2025-09","2025-10","2025-11","2025-12"]
  split: ["2025-09","2025-10","2025-11","2025-12"]
  auto_discover: false          # 为 true 时自动从库中发现月份

# 排名品牌配置
ranking:
  brands: ["lenovo","dell","hp","asus","acer","apple","samsung"]
```

## 数据来源与查询规则（按代码实现）
- 主数据源：`mentions_wide`（SQLite）
- 品牌匹配：严格使用 `keyword_label` 字段（不回退其他列）
  - Lenovo：`LOWER(keyword_label) LIKE LOWER(:keyword_like)`（来自 `filters.keyword_like`）
  - 其他品牌：`LOWER(keyword_label) LIKE LOWER('%{brand.lower()}%')`
- 国家过滤：`countryId = :country`（来自 `filters.country_id`）
- 情感分桶：使用 `sentiment.thresholds` 中的阈值与列名
  - Positive：`polarity > :positive_min`
  - Neutral：`:negative_max <= polarity <= :positive_min`
  - Negative：`polarity < :negative_max`
- 日期匹配：支持文本日期与 epoch(ms) 两类存储；按月聚合

## 使用方法
### 分步执行（推荐）
```bash
# 1) 生成页面级 Excel 数据与嵌入 xlsx
python charts/p18/generate_excel.py

# 2) 用 Excel 数据填充图表并打包输出
python charts/p18/fill_from_excel.py
```

### 一键构建
```bash
python charts/p18/build.py
```
- 说明：`build.py` 仅委托到页面级 `fill_from_excel.py`，不自动生成数据。
- 前置要求：需已存在 `charts/p18/p18_data.xlsx` 与 `charts/p18/tmp/ppt` 解压结构及嵌入 xlsx，否则会报错。

## 生成物
- 汇总数据：`charts/p18/p18_data.xlsx`（便于人工检验/修订）
- 页面嵌入：`charts/p18/tmp/ppt/ppt/embeddings/Microsoft_Office_Excel_Binary_Worksheet{1..4}.xlsx`
- 页面图表 XML：`charts/p18/tmp/ppt/ppt/charts/chart{1..4}.xml` 与 `_rels/chartX.xml.rels`
- 最终输出：`charts/p18/output/p18-final.pptx`

## 计算逻辑（概要）
- 时间范围：
  - MainTrend：最近 6 个月
  - Lovers/Neutral/Haters：最近 4 个月
  - 月份可选自动发现，按严格过滤生成并排序，取末段
- 数据计算：
  - 按月聚合 Positive/Neutral/Negative/Total
  - 百分比：`round(100 * count / total)`
  - Net Lovers%：`Lovers% - Haters%`
- 排名计算：
  - 对配置品牌计算当月 Net Lovers%，排序得到 Lenovo 的名次

## 严格模式与错误处理
- 关键缺失直接失败：
  - 模板解压或嵌入/图表 XML 缺失 → 报错
  - `keyword_label` / `countryId` 缺失 → 报错
  - `p18_data.xlsx` 缺失或工作表缺失 → 报错
- 模板数据提取：若任一图表基础数据为空，直接抛错（不兜底默认值）。
- 计算覆盖：若某月份无计算结果，保留模板值，并在 Excel `Source` 行标注为 `template`（用于人工检验）。

## 依赖管理
- 第三方：`openpyxl`, `pyyaml`
- 安装命令：`pip install openpyxl pyyaml`

## 临时文件管理
- 页面级临时目录：`charts/p18/tmp/`（统一使用 `tmp/ppt` 结构）
- 调试文件：如需调试，统一放在项目根目录 `tmp/` 下（避免随地生成）

## 注意事项
- 禁止 HTTP 预览或下载；所有文件本地读写
- MVP 原则：避免过度设计，专注核心功能
- 注释完善：脚本内含详尽注释，便于维护
- 严格模式：不允许兜底掩盖错误；遇到缺失立即报错
