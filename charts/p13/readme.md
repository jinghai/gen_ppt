# P13 页面 - Engagement breakdown（情感分布 + 日级走势）

## 页面概述

第 13 页可视化“Engagement breakdown”：
- 图表一（chart10，饼图）：情感分布（Positive / Neutral / Negative），展示当月占比。
- 图表二（chart11，散点/折线）：日级情感走势（三条序列：Positive、Neutral、Negative），Y 轴为 0–100（百分比）。
- 页面下方包含“PEAKS EXPLANATION”说明文本（非程序生成，来自模板），举例说明某日 Neutral 峰值（如 26/08/25 与 Lenovo 产品讨论）与 28/08/25 负面波动的语境。

说明：X 轴日期范围由全局 `config.yaml` 的 `update.start_date` ~ `update.end_date` 控制（例如 2025-08-01 至 2025-08-31）；模板中的坐标轴显示可能仅覆盖其中的一个可视区间。

## 配置要点

- 本页局部配置文件：`charts/p13/config.yaml`
  - `output.replace_charts`: `['chart10.xml','chart11.xml']`
  - `output.final_mode`: `updated`
  - `fill_policy.axis_day_base`: `20300`（可覆盖全局同名配置）
- 月度饼图（chart10）取 `update.start_date` 所在月份（例如 `2025-08`）。
- 日级趋势（chart11）采用 `update.start_date ~ update.end_date` 的完整日期窗。
- 输出文件：`output/p13.pptx`。
- 填充脚本根据 `chart_path.txt` 中的 XML 基名与根配置自动解析实际 XML 路径，无需在 chart 目录内放置 XML 文件。

## 数据源与字段

来自聚合指标库 `metrics_v5.db`：
1. `brand_metrics_month`（月度）：`positive_mentions`、`neutral_mentions`、`negative_mentions`
2. `brand_metrics_day`（日度）：`positive_mentions`、`neutral_mentions`、`negative_mentions`

过滤条件（来自 `gen_ppt/config.yaml` → `filters`）：
- `countryId`：目标国家（示例 39=France）
- `brand_key`：目标品牌（示例 Lenovo，内部以 `LOWER(brand)=lower(brand_key)` 匹配）
- 时间范围：`update.start_date` ~ `update.end_date`

备注：本页不使用 Neticle 原始库，所有图表来自指标聚合库（`metrics_v5.db`）。

## 计算与映射

- 图表一（chart10，饼图：当月情感分布）
  - 取目标品牌在目标国家与目标月份的三类提及计数：`p=positive_mentions`，`n=neutral_mentions`，`ng=negative_mentions`。
  - 分母 `denom = p + n + ng`；各类占比按 `value/denom*100` 计算后，做“合计归一到 100.0%”校正（见下）。
  - 标签顺序固定为：`['Positive','Neutral','Negative']`。

- 图表二（chart11，散点/折线：日级情感走势）
  - 对每一天计算 `p_t`、`n_t`、`ng_t`，再得 `denom_t = p_t + n_t + ng_t`。
  - 当日占比：
    - `pos_pct(t) = p_t / denom_t * 100`（若 `denom_t=0` 则为 0）
    - `neu_pct(t) = n_t / denom_t * 100`
    - `neg_pct(t) = ng_t / denom_t * 100`
 - 对每一天的三项百分比应用“合计归一到 100.0%”校正。
  - X 轴数值映射：`x[i] = axis_day_base + i + 1`，`axis_day_base` 来自 `config.yaml` 的 `fill_policy.axis_day_base`（默认 20300），以对齐模板数轴。

归一化规则：先按 1 位小数四舍五入，若三项之和与 100.0 存在 0.1 的舍入偏差，则将残差加到三项中数值最大的那一项（再保留 1 位），并裁剪到 [0,100]，确保每一天及当月饼图的百分比严格和为 100.0%。

### Engagement 指标口径（Lenovo）

- 定义
  - Engagement 总量（Engagement volume）：日度表 `brand_metrics_day` 的 `total_interactions` 之和。
  - 每条互动率 IPM（Interactions per Mention）：`total_interactions / total_mentions`。
- 过滤条件：`LOWER(brand)=lower(brand_key)`、`countryId=config.country_id`、`day in [start_date, end_date]`。
- 输出位置：以上指标以附加字段 `metrics` 的形式写入 `chart10/final_data.json` 与 `chart11/final_data.json`，结构如下：
  - `engagement_total_month`：窗口期互动总量（整数）。
  - `ipm_month`：窗口期 IPM（四位小数）。
  - `by_day.date`：窗口内全体日期数组。
  - `by_day.engagement`：按日 `total_interactions`。
  - `by_day.ipm`：按日 IPM。
- 说明：图表仍按“情感百分比”渲染；`metrics` 供页脚注释或其他页面二次使用，填充脚本会忽略未知字段，不影响图表填充。

## 缺失数据处理

- 若数据库缺失或查询为空：
  - chart10 回退到 `chart10/original_series.json` 推断值；
  - chart11 回退到 `chart11/original_scatter.json`；
- 始终生成 `data.json` 与 `final_data.json`，确保填充流程不中断。

## 构建与填充

- 生成数据：`python charts/p13/make_data.py`
- 填充 XML 并构建单页：`python charts/p13/build.py`
- 预览图表原始态：查看 `chart10/preview_original.png`、`chart11/preview_original.png`
 - 预览最终 PPT：浏览器打开 `http://localhost:8000/output/p13.pptx`（先在工程根目录运行 `python -m http.server 8000`）

## 业务含义

- 情感结构：量化正/中/负情绪在总体互动中的占比。
- 情感走势：跟踪每天的情感百分比波动与峰值成因。
- 决策支持：结合文本“PEAKS EXPLANATION”辅助定位话题与异动。
