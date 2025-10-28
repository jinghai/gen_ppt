# LRTBH 图表重填充工程 · 总 README

本工程在 `charts/` 目录内实现对模板 PPT 的图表数据重填充与单页构建，保证样式与文本完全一致。按统一配置的时间范围（`update.start_date`/`update.end_date`）更新图表数据，超出范围的数据沿用模板原文。

## 目的与范围
- 使用已解压模板 `ppt/input/LRTBH-unzip`（内部 `ppt/charts`），解析每页图表并按统一配置更新数据。
- 所有代码与输出仅位于 `charts/` 内，按页/图表生成单页 PPT，最终合成完整 PPT。
- 不修改页面文本与样式，仅注入图表数据（字面值）。

## 核心要求（样式完全一致）
- 保留所有样式节点：`c:spPr`、`c:plotArea`、`c:legend`、`c:dLbls`、`c:numFmt`、`c:axId`、`c:majorGridlines/minorGridlines`、`c:marker`/`c:line`、配色方案与系列顺序。
- 不改动页面文本框：不修改 `p:txBody`/`a:t` 内容。
- 轴设定与刻度：保留 `min/max/majorUnit/tickLblPos`；如 p10 的日轴（20301–20331）按模板映射。
- 标签口径：百分比/值/小数位按模板保持；饼/环形的起始角度、间隙宽度、重叠、堆叠/簇状等不变。
- 仅替换数据为 `numLit/strLit`（必要时保留 `externalData` 引用），避免损坏样式关系。

## 统一配置
- `ppt/config.yaml` 集中管理：
  - 时间范围：`update.start_date: "YYYY-MM-DD"` 与 `update.end_date: "YYYY-MM-DD"`。
  - 数据源：`data_sources`（如 `sqlite: ppt/data/neticle-v5.sqlite`、`metrics_db: ppt/data/metrics_v5.db`）。
  - 项目根配置：
    - `project.template_root`: 模板解压根目录（默认 `ppt/input/LRTBH-unzip`）。
    - `project.output_root`: 输出根目录（默认 `ppt/output`）。
  - 渠道映射与筛选：`channels`、`filters`。
  - 填充策略：`fill_policy`（包含 `pre_aug`、`aug_update`、`axis_day_base`、`dedup` 等）。

## 目录约定（更新）
```
ppt/
  readme.md                  # 本文件：总说明与快速上手
  实现方案.md                # 详细方案、需求与进度跟踪
  config.yaml                # 统一配置（含 template_root/output_root）
  tools/                     # 通用脚本：parse/scaffold/fill/build/verify
  input/
    LRTBH-unzip/            # 模板已解压（推荐）
  charts/
    p10/                    # 页级目录示例（含 make_data.py/build.py/...）
  output/                   # 各单页与最终合成 PPT 输出
```

兼容的解压目录结构：
- 新结构（推荐）`ppt/input/`：`ppt/input/LRTBH-unzip/`，内部含 `ppt/charts/` 子目录。
- 旧结构（不推荐）`charts/`：`charts/L-RTBH-ppt-unzip/`，内部含 `charts/` 子目录；可用 `refresh_unzip.py --prune-legacy` 清理顶层旧镜像。

所有工具脚本会按 `ppt/config.yaml: project.template_root` 自动解析并兼容两种结构，无需手动修改路径。

## 快速上手（更新）
- 解析与索引（如有需要）：
  - `python ppt/tools/verify_unzip.py`（校验解压结构与配置）
- 生成脚手架（示例 p10）：
  - `python ppt/tools/scaffold_p10.py`（已按配置解析解压路径）
- 填充与构建（示例 p10）：
  - `python ppt/tools/fill_p10.py`（写入 chart_path.txt 指针，兼容两种结构）
  - `python ppt/charts/p10/build.py`（构建单页）
- 合成完整 PPT：
  - `python ppt/tools/build_all.py`（支持 `--skip-pages`、`--skip-compose`、`--skip-compose-original`）

## 数据填充与手工修订
- 每个图表目录保留 `data.csv`（查询快照）与 `final_data.csv`（最终填充文件）。
- `fill.py` 优先读取 `final_data.csv`，便于特殊情况下手动调整数据。
- 填充仅替换 `numLit/strLit` 的数据点与类别文本；保留样式与 `rels` 关系不变。

图表基础 XML 的定位通过各图表目录的 `chart_path.txt` 指针实现，脚本会按配置将其写为绝对路径（相对仓库），兼容 `ppt/charts` 与 `charts` 两种解压结构。

## 轻量校验摘要（推荐）
- 跳过逐页构建，仅验证合成与路径解析：
  - `python ppt/tools/build_all.py --skip-pages`
- 预期输出：
  - 终端打印 `Validation summary: {"total": 220, "matched": 220, "mismatched": 0}`。
  - 生成 `ppt/output/LRTBH-final-original.pptx` 与 `ppt/output/LRTBH-final.pptx`（如启用原版合成）。
- 快速预览输出目录：
  - 在 `ppt/output` 下启动本地服务：`python3 -m http.server 8000`。
  - 浏览 `http://localhost:8000/` 查看生成的文件。

## 进度与协作
- 详细需求、里程碑与执行清单见 `ppt/实现方案.md`；按页/图表持续推进与复盘。