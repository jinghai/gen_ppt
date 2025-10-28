# P23页面 - 高密度品牌SOV与趋势分析

## 页面概述

P23页面是品牌声量份额(SOV)和趋势分析的高密度页面，包含16个图表（chart39.xml到chart54.xml），提供7个主要品牌的全方位市场声量分布和Lenovo与其他品牌的多维度日级趋势对比分析。

## 图表配置

### 替换图表列表
- **chart49.xml**: 品牌SOV分析图表
- **chart51.xml**: 品牌SOV分析图表  
- **chart50.xml**: 品牌SOV分析图表
- **chart53.xml**: 品牌SOV分析图表
- **chart52.xml**: 品牌SOV分析图表
- **chart39.xml**: 品牌SOV分析图表
- **chart54.xml**: 品牌SOV分析图表
- **chart40.xml**: 品牌SOV分析图表
- **chart42.xml**: 品牌SOV分析图表
- **chart41.xml**: 品牌SOV分析图表
- **chart44.xml**: 品牌SOV分析图表
- **chart43.xml**: 品牌SOV分析图表
- **chart46.xml**: 品牌SOV分析图表
- **chart45.xml**: 品牌SOV分析图表
- **chart48.xml**: 品牌SOV分析图表
- **chart47.xml**: Lenovo vs Others趋势对比图表

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

## 高密度图表处理

### 图表分布策略
- **15个SOV图表**: 提供多角度品牌声量占比分析
- **1个趋势图表**: 专注于Lenovo与竞品的时间序列对比
- **图表类型多样化**: 支持饼图、柱状图、面积图、环形图等多种展示形式

### 性能优化
```python
def main() -> int:
    # 批量处理16个图表
    # 复用数据库连接和配置对象
    # 优化内存使用，避免重复计算
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

### 批量数据生成与写入
```python
def main() -> int:
    # 1. 加载配置
    # 2. 连接数据库
    # 3. 遍历所有16个chart目录
    # 4. 根据图表类型生成相应数据
    # 5. 批量写入data.json和final_data.json
```

## 构建与测试

### 数据生成
```bash
cd charts/p23
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
- **全方位品牌竞争格局**: 通过16个图表提供最详细的品牌声量分布分析
- **多角度市场份额监控**: SOV指标从不同维度反映品牌市场地位变化
- **深度趋势变化追踪**: Lenovo与竞品的全面相对表现分析

### 决策支持功能
- **精细化营销策略优化**: 基于高密度声量数据制定精准营销策略
- **全面竞争态势评估**: 识别所有主要竞争对手和细分市场机会
- **多层次预警机制**: 通过多图表交叉验证及时发现品牌声量异常变化

### 高级分析能力
- **细分市场洞察**: 16个图表支持不同细分维度的深入分析
- **交叉验证机制**: 多图表数据一致性验证，提高分析可靠性
- **趋势模式识别**: 大量图表数据支持复杂趋势模式的识别

## 技术实现特点

### 高性能数据处理
- 使用pandas进行高效数据聚合
- SQL查询优化，支持大数据量处理
- 内存友好的数据结构设计
- 批量处理优化，减少数据库连接开销

### 容错机制
- 数据库连接异常处理
- 空数据集兜底策略
- 配置文件缺失容错
- 单个图表失败不影响其他图表生成

### 标准化接口
- 统一的数据输出格式
- 标准化的配置加载机制
- 可复用的核心算法函数
- 模块化的图表类型处理

## 与其他页面的关系

### 数据一致性
- 与P8、P10、P12、P13、P21、P22等页面共享相同的数据源
- 统一的品牌列表和时间范围配置
- 一致的SOV计算逻辑

### 功能互补
- P23提供最高密度的图表分析（16个图表）
- 与P21（4图表）、P22（5图表）、P24（28图表）形成完整的分析层次体系
- 支持从概览到详细再到超详细的渐进式分析需求

### 架构价值
- 作为高密度分析页面的标准实现
- 为其他复杂页面提供技术参考
- 验证系统在高负载下的稳定性和性能
