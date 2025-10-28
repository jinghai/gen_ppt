# P27页面 - 双图表品牌SOV与趋势分析

## 页面概述

P27页面是品牌声量份额(SOV)和趋势分析的双图表页面，包含2个图表（chart113.xml和chart114.xml），提供7个主要品牌的市场声量分布和Lenovo与其他品牌的日级趋势对比分析。

## 图表配置

### 替换图表列表
- **chart113.xml**: 品牌SOV分析图表
- **chart114.xml**: Lenovo vs Others趋势对比图表

### 配置参数
- **final_mode**: `updated` - 使用更新后的数据
- **axis_day_base**: `20300` - 日期轴基准值

## 数据源与字段映射

### 核心数据表
1. **brand_metrics_month**: 月度品牌指标聚合表
2. **brand_metrics_day**: 日度品牌指标明细表

### 关键字段映射
| 字段名 | 数据类型 | 业务含义 | 计算用途 | 原始数据源 |
|--------|----------|----------|----------|------------|
| brand_mentions | INTEGER | 品牌提及数 | SOV分子、趋势Y轴 | neticle-v5.sqlite/mentions_wide 聚合 |
| total_mentions | INTEGER | 总提及数 | SOV分母 | neticle-v5.sqlite/mentions_wide 聚合 |
| countryId | TEXT | 国家标识 | 数据聚合维度 | dict.sqlite/countries 表 |
| month | TEXT | 月份(YYYY-MM) | SOV时间筛选 | 计算字段 |
| day | TEXT | 日期(YYYY-MM-DD) | 趋势时间轴 | neticle-v5.sqlite/mentions_wide |
| brand | TEXT | 品牌名称 | 品牌筛选维度 | dict.sqlite/keywords 表 |

## 核心算法实现

### 1. SOV计算 (`make_sov`)
**功能**: 计算7个品牌的声量占比
```python
def make_sov(cfg: Config, conn: sqlite3.Connection) -> Tuple[List[str], List[float]]:
    month_label = _month_label(cfg.start_date)
    q = """
    SELECT countryId, month, brand, brand_mentions, total_mentions
    FROM brand_metrics_month
    WHERE month = ? AND brand IN (...)
    """
    # SOV = (brand_mentions / total_mentions) * 100
    sov = [round(v / float(denom) * 100.0, 1) for v in brand_mentions]
```

### 2. 趋势分析 (`make_trend_lenovo_vs_others`)
**功能**: 生成Lenovo与其他品牌的日级对比数据
```python
def make_trend_lenovo_vs_others(cfg: Config, conn: sqlite3.Connection):
    # 按日聚合品牌声量
    # Lenovo声量 vs Others合计声量
    # 生成时间序列数据点
```

### 3. 配置加载 (`_load_yaml_cfg`)
**功能**: 加载全局配置和页面特定设置
- 品牌列表: 从 `charts/config.yaml` 获取
- 数据库路径: 支持相对路径和绝对路径
- 时间范围: 由 `charts/config.yaml` 的 `update.start_date`/`update.end_date` 控制自然日范围（整月或跨月）

## 双图表处理策略

### 图表分布
- **1个SOV图表**: 提供品牌声量占比分析
- **1个趋势图表**: 专注于Lenovo与竞品的时间序列对比
- **精简高效**: 最小化图表数量，最大化信息密度

### 优化策略
```python
def main() -> int:
    # 处理2个图表
    # 复用数据库连接和配置对象
    # 快速处理，低资源消耗
    for chart_dir in sorted(chart_dirs):
        # 根据图表类型选择相应的数据生成函数
        if t in ('scatterChart', 'lineChart'):
            series = make_trend_lenovo_vs_others(cfg, conn)
        elif t in ('barChart','pieChart','areaChart','doughnutChart'):
            labels, values = make_sov(cfg, conn)
```

## 兜底机制

### 数据缺失处理
- 当数据库查询结果为空时，返回空列表
- 图表构建时会使用 `original_*.json` 缓存文件作为兜底
- 确保PPT始终有数据显示，保持完整性

### 路径探测机制
```python
REPO_ROOT = ROOT.parents[2]
# 自动探测项目根目录和配置文件位置
```

## 数据格式规范

### 类别图数据格式
```json
{
  "labels": ["Lenovo", "Dell", "Hp", "Asus", "Acer", "Apple", "Samsung"],
  "series": [{"name": null, "values": [25.3, 18.7, 15.2, 12.8, 10.5, 9.1, 8.4]}]
}
```

### 散点图数据格式
```json
{
  "scatter_series": [
    {
      "name": "Lenovo",
      "x": [20301, 20302, ...],
      "y": [1250, 1180, ...],
      "points": [[20301, 1250], [20302, 1180], ...]
    },
    {
      "name": "Others", 
      "x": [20301, 20302, ...],
      "y": [3850, 3920, ...],
      "points": [[20301, 3850], [20302, 3920], ...]
    }
  ]
}
```

## 主函数执行流程

### 图表类型识别
```python
def _chart_type(chart_xml: Path) -> str:
    # 解析XML，识别图表类型
    # 支持: scatterChart, lineChart, barChart, pieChart, areaChart, doughnutChart
```

### 数据生成与写入
```python
def main() -> int:
    # 1. 加载配置
    # 2. 连接数据库
    # 3. 遍历2个chart目录
    # 4. 根据图表类型生成相应数据
    # 5. 写入data.json和final_data.json
```

## 构建与测试

### 数据生成
```bash
cd charts/p27
python make_data.py
```

### 图表构建
```bash
python build.py
```

### 完整构建
```bash
cd charts/tools
python build_all.py --mode both
```

## 业务价值与应用

### 市场分析维度
- **核心品牌竞争格局**: 通过SOV图表提供品牌声量分布概览
- **关键趋势监控**: 专注于Lenovo与竞品的核心对比分析
- **精准洞察**: 双图表设计确保关键信息突出显示

### 决策支持功能
- **快速决策支持**: 基于核心声量数据快速制定营销策略
- **重点竞争态势评估**: 聚焦最重要的竞争对手分析
- **高效预警机制**: 通过关键图表快速发现品牌声量变化

### 高级分析能力
- **核心市场洞察**: 双图表支持最重要维度的深入分析
- **快速验证机制**: 两个图表相互验证，提高分析效率
- **趋势模式识别**: 精简图表数据支持快速趋势识别

## 技术实现特点

### 高效数据处理
- 使用pandas进行高效数据聚合
- SQL查询优化，支持快速数据处理
- 内存友好的数据结构设计
- 最小化数据库连接开销

### 轻量级容错机制
- 数据库连接异常处理
- 空数据集兜底策略
- 配置文件缺失容错
- 单个图表失败不影响另一个图表生成

### 标准化接口
- 统一的数据输出格式
- 标准化的配置加载机制
- 可复用的核心算法函数
- 模块化的图表类型处理

## 与其他页面的关系

### 数据一致性
- 与所有其他页面共享相同的数据源
- 统一的品牌列表和时间范围配置
- 一致的SOV计算逻辑

### 功能互补
- P27提供精简的双图表分析
- 与P8（7图表）、P21（4图表）、P22（5图表）、P23（16图表）、P24（28图表）、P25（28图表）、P26（2图表）形成完整的分析层次体系
- 支持快速概览和重点分析需求

### 架构价值
- 作为轻量级分析页面的标准实现
- 为快速分析和报告生成提供模板
- 验证系统在最小负载下的基础功能

## 特殊技术考虑

### 图表编号特点
- P27页面使用chart113和chart114，编号连续且较高
- 与P26页面（chart111-112）形成连续的双图表页面序列
- 这种设计便于批量管理和维护

### 性能优势
- 双图表设计确保最快的处理速度
- 最小的内存占用和资源消耗
- 适合频繁更新和实时分析场景

### 应用场景
- **快速报告**: 适合需要快速生成的简要分析报告
- **高频更新**: 支持高频率的数据更新和图表刷新
- **移动端展示**: 双图表设计适合移动设备的展示需求

## 与P26页面的对比

### 相似性
- 相同的双图表架构设计
- 一致的数据生成逻辑和算法实现
- 相同的配置参数和兜底机制

### 差异性
- **图表编号**: P27使用chart113-114，P26使用chart111-112
- **PPT位置**: 在最终PPT中可能处于不同的展示位置
- **业务用途**: 可能服务于不同的报告章节或分析维度

### 协同价值
- 两个页面可以提供相同分析的多重验证
- 支持A/B测试和对比分析需求
- 为不同的业务场景提供灵活的选择
