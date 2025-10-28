# P10 页面 - Sentiment breakdown（三分类）

## 页面概述

P10 页面呈现 Lenovo 在所选国家与周期内的情感分布与日级走势：
- 图表一（chart8）：当月情感分布饼图（Positive/Neutral/Negative）
- 图表二（chart9）：日级情感趋势折线（3 条序列：Positive、Neutral、Negative）

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
  - x 轴为连续数值：`axis_day_base + 序号`（来自 `fill_policy.axis_day_base`）。

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
