# P16 项目使用说明

## 项目概述
- 生成法国联想品牌的声量份额页面：主趋势 + 渠道分解。
- 流程分为两步：先生成 `p16_data.xlsx`，再填充 `p16-final.pptx`。
- 原则：严格报错、不兜底；禁止使用 HTTP 预览或下载；仅在页面根 `tmp` 目录生成临时文件。

## 项目结构
```
charts/p16/
├── config.yaml            # 页面级配置
├── generate_excel.py      # 生成 Excel（解压模板到 tmp，读取模板与数据库数据）
├── fill_from_excel.py     # 填充 PPT（使用 tmp/ppt 内容，更新图表与标签）
├── p16.pptx               # 模板文件
├── p16_data.xlsx          # 生成的 Excel（位于页面根）
├── output/                # 输出目录（最终 PPT）
├── tmp/                   # 临时解压目录（保留用于排查）
└── p16-图表解释.md        # 页面视觉与数据含义说明
```

## 依赖安装（严格管理包依赖）
- Python 3.9+
- 安装：
```bash
pip install pandas openpyxl lxml pyyaml pyxlsb
```
> 注：`pyxlsb` 仅在模板图表链接到嵌入工作簿 `.xlsb` 时需要；缺失时会明确报错。

## 快速开始
1) 生成 Excel 并解压模板到 `tmp`：
```bash
python generate_excel.py
```
输出：页面根 `./p16_data.xlsx`；并在 `./tmp` 下解压出 `ppt/charts`、`ppt/embeddings` 等。

2) 填充 PPT（需要 `tmp/ppt` 已存在）：
```bash
python fill_from_excel.py
```
输出：`./output/p16-final.pptx`。`tmp` 目录将保留用于排查。

## 配置说明（与实现一致）
```yaml
project:
  template_ppt: ./p16.pptx
  output_dir: ./output
  tmp_dir: ./tmp
  final_ppt: ./output/p16-final.pptx

data_sources:
  neticle_db: ../../input/neticle-v5-08-etl.sqlite
  metrics_db: ../../input/metrics-v4-08.db

filters:
  country_name: "France"
  country_id: 39
  brand_name: "lenovo"
  target_month: "2025-08"

# 渠道映射：将 sources.name 归并为目标渠道（以 channel_map 为准）
# 规则：大小写不敏感的精确字符串匹配；未匹配归为 Other。
channel_map:
  Forum: ["forum", "forum aggregator"]
  Online News: [
    "article", "frontpage",
    "article aggregator", "frontpage aggregator",
    "comment", "comment article"
  ]
  Blog: ["blog", "blog aggregator", "comment blog"]
  X: ["twitter", "tweet", "retweet", "quoted tweet", "twitter reply"]
  Instagram: ["instagram", "instagram post", "instagram comment", "instagram reply"]
  # YouTube（合并通用视频标签）
  YouTube: ["youtube video", "video yt comment", "video yt reply", "video", "video aggregator"]

chart_mapping:
  chart1: {file: chart1.xml, type: main_trend}
  chart2..chart7: {type: channel_breakdown}

label_mode:
  auto_labels: true
  auto_label_settings: {font_size: 10, position: outside_end}
```

## 数据与图表策略
- 主趋势：覆盖 `numCache/strCache` 并写入嵌入工作簿；启用 `externalData.autoUpdate=1` 与百分比 `0%` 格式；标签位置为上方。
- 渠道分解：同主趋势；移除数值轴固定 `min/max`，由数据自动缩放到小数比例。
- 标签策略：
  - 删除所有手工百分比标签节点（`slide1.xml` 中文本匹配 `\d+%` 的形状）后，再启用自动标签，避免重复。
  - 统一图表级与系列级标签：显示数值（百分比）、禁用类别/系列名与引导线、位置上方。
- 内容类型声明：更新 `[Content_Types].xml`，为 `ppt/embeddings/*.xlsx` 添加 `<Override>`，确保首次打开即识别为工作簿。

## 常见错误（严格报错，不兜底）
- 缺少 `tmp/ppt/charts` 或 `tmp/ppt/embeddings`：请先运行 `generate_excel.py`，或检查模板是否存在。
- `p16_data.xlsx` 不存在或表缺失：检查第 1 步是否执行成功；日志会给出具体原因。
- 嵌入工作簿读取失败或缺少 `pyxlsb`：安装依赖或检查模板是否链接到 `.xlsb`。
- 月份标签无法识别：确保配置 `target_month` 有效，或修正模板类别标签（支持 `May '25`、`Aug 2025` 等常见格式）。
- 所有输出均为模板值（未覆盖任何 computed）：脚本将报错，请检查品牌与月份过滤是否匹配数据库。

## 目录与文件规范
- 临时文件仅在页面根 `tmp` 目录；不得随处生成临时文件。
- Excel 输出位于页面根：`./p16_data.xlsx`（相对路径时忽略子目录）。
- 最终 PPT 位于 `./output/p16-final.pptx`。

## 验收清单
- `summary` 工作表中 `computed条数 > 0`。
- 打开 `p16-final.pptx` 即显示最新数据与自动标签；页面不再出现手工百分比标签。
- 日志仅包含明确的错误与信息级提示，无兜底或静默忽略。
