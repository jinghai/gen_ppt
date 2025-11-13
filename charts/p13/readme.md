# P13（Engagement breakdown – France）

本页生成法国市场的 Engagement breakdown，严格以 `p13.pptx` 为模板，不对模板做程序性修改。生成的 PPT 可在编辑器内直接编辑嵌入的数据表。

## 使用方法
1. 确认数据与配置：
   - 已知数据位于 `input` 目录（详见 `p13/需求.md`）。
   - 页面级配置：`charts/p13/config.yaml`。
2. 生成 Excel：
   - `python charts/p13/generate_excel.py`
3. 填充模板并打包 PPT：
   - `python charts/p13/fill_from_excel.py`

## 生成的数据（Excel）
`charts/p13/p13_data.xlsx` 供人工校验与修改，包含：
- `MetaData`：国家/品牌/时间范围及总参与度。
- `PieData`：`Sentiment, Percentage`（按参与度加权的月度占比）。
- `LineData`：`Date, Positive, Neutral, Negative`（IndexGlobal：对所有天×情绪的参与度取全局最大值归一化为 0-100 指数；列顺序固定）。
- 审计表：
  - `AuditDay`：每日参与度原值与百分比（可核对趋势指数来源的原值；指数不再是当日占比）。
- `AuditRow`：示例原始行与派生参与度（最多 200 行），含 `PostId` 与 `Channel`（若宽表存在）。
  - PostId 候选：`postId/post_id/mentionId/id/postID`；Channel 候选：`channel/source/platform/network/site`。
  - `AuditMonth`：当月各情绪参与度与占比（核对 PieData）。

修改 Excel 后再次运行填充脚本即可更新 PPT。

## 图表与颜色
- 默认颜色映射（按模板）：Positive `#009FA9`、Neutral `#FFBC42`、Negative `#D81159`。
- 系列顺序固定：Positive → Neutral → Negative。
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
