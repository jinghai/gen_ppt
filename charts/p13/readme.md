# P13（Engagement breakdown – France）

本页生成法国市场的 Engagement breakdown，严格以 `p13.pptx` 为模板，不对模板做程序性修改。生成的 PPT 可在编辑器内直接编辑嵌入的数据表。

## 使用方法
1. 确认数据与配置：
   - 已知数据位于 `input` 目录（详见 `p13/需求.md`）。
   - 页面级配置：`charts/p13/config.yaml`。
2. 一键构建：
   - 在仓库根目录执行：
     - `python charts/p13/build.py`
   - 构建过程：先生成 Excel，再填充模板，最后打包输出 `charts/p13/output/p13-final.pptx`。
3. 手动分步（可选）：
   - 只生成 Excel：`python charts/p13/generate_excel.py`
   - 用 Excel 填充：`python charts/p13/fill_from_excel.py`

## 生成的数据（Excel）
`charts/p13/output/p13_data.xlsx` 供人工校验与修改，包含：
- `MetaData`：国家/品牌/时间范围及度量选项。
- `PieData`：`sentiment,value,color`（饼图占比）。
- `LineData`：`date,sentiment,value,color`（按日折线/散点）。

修改 Excel 后再次运行填充脚本即可更新 PPT。

## 图表与颜色
- 默认颜色映射：Positive `#2ECC71`、Negative `#E74C3C`、Neutral `#F1C40F`。
- 系列顺序固定：Positive → Negative → Neutral。
- 脚本同时更新图表数据缓存和系列颜色，确保打开 PPT 即显示新数据。

## 模板与临时目录
- 模板：`charts/p13/p13.pptx`（不可被程序修改）。
- 页面级临时目录：`charts/p13/tmp`（自动创建与清理）。
- 最终打包将嵌入 `Microsoft_Excel_Worksheet1.xlsx`，编辑器可直接“编辑数据”。

## 法国市场过滤与时间范围
- 默认过滤 `country='FR'`/`market='France'`，品牌为 `Lenovo`，时间范围指向 `2025-08`，可在 `config.yaml` 调整。

## 常见问题
- 输出为空/颜色不符：检查 `output/p13_data.xlsx` 是否存在与列名是否正确；颜色是否为有效十六进制。
- 模板更新了文字或标签：无需改动代码；构建会复用模板原文并仅替换图表数据与嵌入表。
- 大型 DB 不便打开：脚本仅做聚合查询，避免整体加载；如需额外过滤，请在 `config.yaml` 指定。
