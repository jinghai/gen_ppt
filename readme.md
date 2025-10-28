# LRTBH 图表重填充工程 · 总 README

本工程在 `charts/` 目录内实现对模板 PPT 的图表数据重填充与单页构建，保证样式与文本完全一致。通过统一配置（`config.yaml`）指定时间范围与数据源更新图表数据，超出范围的数据沿用模板原文。

说明：本仓库采用根路径结构（`input/`、`charts/`、`tools/`、`output/`），不使用历史文档中的 `ppt/` 前缀路径；如遇到旧文档中的 `ppt/...`，以本 README 为准。

## 目录结构
```
.
├── charts/                 # 按页组织，每页包含 build.py 及多个 chart 子目录
│   ├── p10/
│   │   ├── build.py
│   │   ├── chart8/
│   │   └── chart9/
│   └── ...
├── config.yaml             # 统一配置（模板根、输出根、时间范围、数据源等）
├── input/
│   ├── LRTBH-unzip/        # 模板 PPT 解压目录（内部应含 ppt/charts 等）
│   └── LRTBH.pptx          # 模板 PPT 原文件（可选，通常不入库）
├── logs/                   # 运行日志（建议不入库）
├── output/                 # 单页与最终合成 PPT 输出（建议不入库）
├── tools/                  # 通用工具脚本
│   ├── build_all.py        # 批量构建与（可选）合成
│   ├── check_pptx.py       # 辅助检查/验证
│   └── fill_p10.py         # 示例填充脚本（p10）
├── readme.md               # 本文件
├── requirements.txt        # 依赖定义
├── 图表实现模式.md
└── 实现方案.md
```

## 环境要求
- Python 3.10+（推荐 3.11）
- macOS（已在此环境下开发/使用）

### 建立虚拟环境
```
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip setuptools wheel
pip install -r requirements.txt
```
退出：`deactivate`

## 配置（config.yaml）
- 时间范围：
  - `update.start_date: "YYYY-MM-DD"`
  - `update.end_date: "YYYY-MM-DD"`
- 数据源：`data_sources`（例如 sqlite 路径、指标库等）
- 项目根配置：
  - `project.template_root`: 模板解压根目录（默认 `input/LRTBH-unzip`）
  - `project.output_root`: 输出根目录（默认 `output`）
- 其他：`channels`、`filters`、`fill_policy`（如 `pre_aug`、`aug_update`、`axis_day_base`、`dedup` 等）

## 快速上手
1) 准备模板
- 将模板原文件放置于 `input/LRTBH.pptx`（可选）。
- 解压模板到 `input/LRTBH-unzip/`（内部应包含 `ppt/charts` 等子目录）。

2) 创建并激活虚拟环境、安装依赖
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3) 构建单页示例（以 p10 为例）
- 如需先生成/更新数据或图表路径指针，可执行：
```
python tools/fill_p10.py
```
- 构建 p10：
```
python charts/p10/build.py
```
- 生成产物位于 `output/`（例如 `output/p10.pptx`）。

4) 批量构建与合成
```
python tools/build_all.py
```
- 查看参数：
```
python tools/build_all.py -h
```

## 数据填充与修订约定
- 每个图表目录可保留 `data.csv`（查询快照）与 `final_data.csv`（最终填充数据）。
- 构建/填充脚本优先读取 `final_data.csv`，便于在特殊情况下手工修订数据。
- 仅替换图表数据的 `numLit/strLit`，不变更样式与关系（rels）。
- 图表基础 XML 的定位可通过各图表目录的 `chart_path.txt` 指针实现；若脚本可依据 `config.yaml` 自动解析路径，可不提交该文件。

## 校验与排查
- 基本校验：执行 `python tools/build_all.py`，确认输出是否生成且可打开。
- 依赖校验：`pip check`、`python -c 'import lxml,click,pandas,yaml'` 等快速导入测试。
- 输出预览：在 `output/` 目录下启动本地服务 `python3 -m http.server 8000`，浏览 `http://localhost:8000/` 查看生成文件。

## 版本管理建议
- 强烈建议在 `.gitignore` 中排除：`output/`、`logs/`、`input/LRTBH-unzip/`、`input/LRTBH.pptx`、`.venv/`、`__pycache__/`、`*.pyc`、`.DS_Store`、`.pytest_cache/`、`.mypy_cache/`、`.idea/`、`.vscode/` 等。
- `charts/**/` 中的中间产物按是否可重算进行选择性提交：`final_data.csv`（如为手工修订且构建必需）建议入库；`data.csv` 通常可不入库。

## 现状与一致性说明
- 本仓库包含工具脚本：`tools/build_all.py`、`tools/fill_p10.py`、`tools/check_pptx.py`。
- 旧文档中提到的 `verify_unzip.py`、`scaffold_p10.py` 在当前仓库中未包含。如需这类能力，可在现有 `tools` 基础上补充，或以本 README 提供的等价流程替代。