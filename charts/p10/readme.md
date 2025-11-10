# P10 页面 - Lenovo法国市场情感分析

## 项目概述

P10页面专门用于分析Lenovo品牌在法国市场的情感表现，通过饼图和折线图展示2025年8月7日至28日期间的情感分布和趋势变化。

## 功能特性

### 📊 数据可视化
- **饼图**: 展示整体情感分布（积极、中性、消极）
- **折线图**: 展示每日情感趋势变化

### 🎯 数据来源
- **数据库**: neticle-v5-08.sqlite
- **数据表**: mentions_wide
- **关键字段**: 
  - `polarity`: 情感极性值
  - `createdAtUtcMs`: 时间戳
  - `countryIsoCode2`: 国家代码
  - `keyword_label`: 关键词标签

### 🎨 颜色说明
- **统一颜色方案**: 确保所有图表元素颜色一致性
- **情感颜色映射**（来源于模板，不可配置覆盖）:
  - Positive（积极）: `#009FA9` (蓝绿色，模板)
  - Neutral（中性）: `#FFBC42` (琥珀黄，模板)
  - Negative（消极）: `#D81159` (洋红红，模板)
- **应用范围**: 饼图填充、折线图线条、图例标识
- **颜色来源策略**: 严格保留模板系列颜色，不读取或覆盖配置。

### 🔍 筛选条件
- **地区**: 法国 (`countryIsoCode2='fr'`)
- **品牌**: Lenovo (`keyword_label LIKE '%lenovo%'`)
- **时间范围**: 2025年8月7日-28日

### 📊 情感分类规则（与 p13 阀值统一）
- **Positive（积极）**: polarity ≥ 0.05
- **Neutral（中性）**: -0.05 < polarity < 0.05
- **Negative（消极）**: polarity ≤ -0.05

## 项目结构

```
p10/
├── build.py              # 主构建脚本（一键执行）
├── generate_excel.py     # 数据提取和Excel生成
├── fill_from_excel.py    # PPT模板填充（包含颜色处理，保留模板颜色）
├── config.yaml          # 页面级配置文件
├── 需求.md              # 详细需求文档
├── p10-图表解释.md      # 图表详细解释文档
├── readme.md            # 本文档
├── p10_data.xlsx        # 生成的Excel数据文件
├── logs/                # 日志目录
│   └── build.log        # 构建日志
└── output/              # 输出目录
    └── p10-final.pptx   # 最终生成的PPT文件
```

## 快速开始

### 1. 环境要求

确保已安装以下Python包：
```bash
pip install pandas openpyxl pyyaml lxml
```

### 2. 一键构建

```bash
cd charts/p10
python build.py
```

### 3. 分步执行（可选）

如需分步执行，可以单独运行：

```bash
# 1. 生成Excel数据
python generate_excel.py

# 2. 填充PPT模板
python fill_from_excel.py
```

## 配置说明

### 主要配置项

- **数据源路径**: `data_sources.neticle`
- **时间范围**: `time_range.start_date` / `end_date`
- **筛选条件**: `filters.country` / `brand`
- **情感分类**: `sentiment.thresholds`
- **图表设置**: `charts.pie` / `line`

### 情感分类规则

```yaml
sentiment:
  thresholds:
    positive_min: 0.05      # 积极情感最小阀值（≥ 划为积极）
    negative_max: -0.05     # 消极情感最大阀值（≤ 划为消极）
```

### 颜色策略（模板优先）

- 默认且唯一策略：保留模板中定义的系列颜色，脚本不写入任何颜色节点，不支持通过配置覆盖颜色。
- 若模板缺少对应颜色节点（如 `a:ln/a:solidFill/a:srgbClr`），脚本将报错，不做兜底处理。

## 输出文件

### Excel文件 (`p10_data.xlsx`)
- **Sheet1 - 饼图数据**: 情感分类统计
- **Sheet2 - 折线图数据**: 每日情感趋势
- **Sheet3 - 元数据**: 数据质量和统计信息

### PPT文件 (`output/p10-final.pptx`)
- 基于模板生成的最终演示文稿
- 包含嵌入的Excel数据和图表

### 编辑图表数据（PowerPoint 中）
- 在 PPT 中右键图表选择“编辑数据”，会打开嵌入的 Excel 工作簿。
- 默认活动工作表为 `LineData`（右侧折线/散点图数据）。
- 编辑右侧图表：在 `LineData` 表中修改列 `A`（日期），`C/D/E`（Positive/Negative/Neutral 的百分比），图形会即时刷新。
- 编辑左侧饼图：请切换到 `PieData` 工作表，修改 `Sentiment/Percentage`，图形会即时刷新。
- 若 Excel 未自动刷新，请确认 PPT 的图表“外部数据自动更新”已启用（脚本已写入 `autoUpdate=1`）。

## 数据质量控制

### 自动检查项
- ✅ 数据完整性验证
- ✅ 时间范围校验
- ✅ 情感分类准确性
- ✅ 颜色配置一致性验证
- ✅ 输出文件大小检查

### 质量指标
- **数据覆盖率**: 确保每日都有数据
- **情感分布**: 验证三类情感都有数据
- **异常值检测**: 识别极端polarity值

## 日志和调试

### 日志文件
- **位置**: `logs/build.log`
- **级别**: INFO（可在config.yaml中调整）
- **内容**: 完整的执行过程和错误信息

### 常见问题

1. **数据库连接失败**
   - 检查数据库文件路径是否正确
   - 确认文件权限

2. **Excel生成失败**
   - 检查磁盘空间
   - 确认openpyxl库已安装

3. **PPT填充失败**
   - 检查模板文件是否存在
   - 确认lxml库已安装
   - 验证颜色配置格式正确性

## 性能指标

- **数据提取**: ~0.5秒（5557条记录）
- **Excel生成**: ~0.2秒
- **PPT填充**: ~0.3秒
- **总耗时**: <1秒

## 版本信息

- **创建日期**: 2024-11-01
- **版本**: 1.0.0
- **Python要求**: 3.7+
- **依赖库**: pandas, openpyxl, pyyaml, lxml

## 维护说明

### 定期检查
- 数据库文件更新
- 配置参数调整
- 模板文件维护

### 扩展建议
- 支持更多时间范围
- 增加其他品牌分析
- 添加更多可视化图表
- 支持自定义颜色主题
- 增加交互式图表功能

---

**注意**: 本页面遵循MVP原则，专注核心功能实现，避免过度设计。如需扩展功能，请参考需求文档进行规划。

## 数据源与字段

核心来自 metrics_v5 聚合库：
1. `brand_metrics_month`（月度）：`positive_mentions`、`neutral_mentions`、`negative_mentions`
2. `brand_metrics_day`（日度）：`positive_mentions`、`neutral_mentions`、`negative_mentions`

过滤条件（来自 `gen_ppt/config.yaml` 的 filters 配置）：
- `countryId`：目标国家（示例 39=France）
- `brand_key`：目标品牌（示例 Lenovo）。内部以 `LOWER(brand)=lower(brand_key)` 匹配
- 时间范围：`update.start_date` ~ `update.end_date`

说明：早期文档的 SOV 与“Lenovo vs Others”实现已替换为“三分类情感”实现；涉及的字段切换为正中负三列。

## 计算与映射

- chart8（饼图）：
  - 分母 `denom = pos + neu + neg`；各类值除以 `denom` 后乘 100，保留 1 位小数。
- chart9（折线）：
  - 默认“每日占比”：对 `brand_metrics_day` 每天计算
    - `p_t = positive_mentions(t)`，`n_t = neutral_mentions(t)`，`ng_t = negative_mentions(t)`
    - `denom_t = p_t + n_t + ng_t`
    - `pos%_t = 100 * p_t / denom_t`（`denom_t=0` 时记 0），`neu%_t`、`neg%_t` 同理；保留 1 位小数。
  - 可选“平滑占比（滑窗）”：在 `charts/p10/config.yaml` 启用
    - `chart9.smooth_percent: true`
    - `chart9.smooth_window: 7`（天）
    - 计算方式为“窗口滚动求和后再求占比”：
      - `P_t = sum_{i=t-w+1..t} p_i`（窗口外视为 0，`min_periods=1`）
      - `N_t、NG_t` 同理，`DEN_t = P_t + N_t + NG_t`
      - `pos%_t = 100 * P_t / DEN_t`（`DEN_t=0` 时记 0），其余同理；保留 1 位小数。
- 折线图类别轴：若存在 `Date` 列则使用 `Date`；否则使用数值 `X`（`axis_day_base + 序号`）。
- 散点图 `xVal`：使用连续数值 `X`（`axis_day_base + 序号`）。
- 嵌入工作簿列顺序：严格按模板系列顺序排列；折线/散点公式按该顺序绑定。

## 缺失数据兜底

- 任一数据源缺失或分母为 0 时，退回使用 `original_*` 缓存（`chart8/original_series.json`、`chart9/original_scatter.json`）。
- 产出 `data.json` 与 `final_data.json`，填充脚本优先读取 `final_data.json`。

## 产出 JSON 结构

- chart8：`{ "labels": ["Positive","Neutral","Negative"], "series": [ {"name": null, "values": [..] } ] }`
- chart9：`{ "scatter_series": [ {"name":"Positive","x":[..],"y":[..]}, {"name":"Neutral",..}, {"name":"Negative",..} ] }`

## 配置项（p10/config.yaml）

```
output:
  replace_charts: ["chart8.xml","chart9.xml"]
  final_mode: updated
fill_policy:
  axis_day_base: 20300
chart9:
  smooth_percent: false   # 是否启用 7 日（可调）滑窗的“平滑占比”
  smooth_window: 7        # 窗口大小（天），仅在 smooth_percent=true 时生效
```

## 构建与预览

推荐一次性构建并生成预览：

```
python gen_ppt/charts/p10/build_all.py --mode both
```

它将执行：
- 运行 `make_data.py` 生成数据 JSON
- 调用 `chart8/fill.py`、`chart9/fill.py` 更新模板 XML
- 生成 `output/p10.pptx`（单页版）与 `output/LRTBH-final-*.pptx` 合并稿（取决于全局配置）
- 基于 `original_*` 生成 `preview_original.png` 便捷对比图

## 对齐与校验

- 字段对齐：三分类字段在 `brand_metrics_day/month` 中命名为 `positive_mentions`、`neutral_mentions`、`negative_mentions`。
- 验证：`gen_ppt/tools/build_all.py` 会对替换的 chart xml 做简易变更检测，便于发现未生效的替换。
