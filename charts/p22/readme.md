# P22页面 - 品牌SOV与趋势分析

## 页面概述

P22页面是品牌声量份额(SOV)和趋势分析的重要页面，包含5个图表（chart34.xml到chart38.xml），提供7个主要品牌的市场声量分布和Lenovo与其他品牌的日级趋势对比分析。

## 图表配置

### 替换图表列表
- **chart34.xml**: 品牌SOV分析图表
- **chart35.xml**: 品牌SOV分析图表  
- **chart36.xml**: 品牌SOV分析图表
- **chart37.xml**: 品牌SOV分析图表
- **chart38.xml**: Lenovo vs Others趋势对比图表

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
    # 3. 遍历所有chart目录
    # 4. 根据图表类型生成相应数据
    # 5. 写入data.json和final_data.json
```

## 构建与测试

### 数据生成
```bash
cd charts/p22
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
- **品牌竞争格局**: 通过5个图表全面展示品牌声量分布
- **市场份额监控**: SOV指标反映品牌市场地位变化
- **趋势变化追踪**: Lenovo与竞品的相对表现分析

### 决策支持功能
- **营销策略优化**: 基于声量数据调整品牌投入重点
- **竞争态势评估**: 识别主要竞争对手和市场机会
- **预警机制**: 及时发现品牌声量异常变化

## 技术实现特点

### 高性能数据处理
- 使用pandas进行高效数据聚合
- SQL查询优化，支持大数据量处理
- 内存友好的数据结构设计

### 容错机制
- 数据库连接异常处理
- 空数据集兜底策略
- 配置文件缺失容错

### 标准化接口
- 统一的数据输出格式
- 标准化的配置加载机制
- 可复用的核心算法函数

## 与其他页面的关系

### 数据一致性
- 与P8、P10、P12、P13、P21等页面共享相同的数据源
- 统一的品牌列表和时间范围配置
- 一致的SOV计算逻辑

### 功能互补
- P22提供中等密度的图表分析（5个图表）
- 与P21（4图表）、P23（16图表）形成不同粒度的分析层次
- 支持从概览到详细的渐进式分析需求
