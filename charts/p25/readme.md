# P25页面 - 超高密度品牌SOV与趋势分析

## 页面概述

P25页面是品牌声量份额(SOV)和趋势分析的超高密度页面，包含28个图表（chart65.xml到chart92.xml），提供7个主要品牌的最全面市场声量分布和Lenovo与其他品牌的超详细多维度日级趋势对比分析。

## 图表配置

### 替换图表列表
- **chart93.xml**: 品牌SOV分析图表
- **chart92.xml**: 品牌SOV分析图表
- **chart95.xml**: 品牌SOV分析图表
- **chart94.xml**: 品牌SOV分析图表
- **chart97.xml**: 品牌SOV分析图表
- **chart96.xml**: 品牌SOV分析图表
- **chart89.xml**: 品牌SOV分析图表
- **chart88.xml**: 品牌SOV分析图表
- **chart91.xml**: Lenovo vs Others趋势对比图表
- **chart90.xml**: 品牌SOV分析图表
- **chart65.xml**: 品牌SOV分析图表
- **chart66.xml**: 品牌SOV分析图表
- **chart67.xml**: 品牌SOV分析图表
- **chart68.xml**: 品牌SOV分析图表
- **chart69.xml**: 品牌SOV分析图表
- **chart70.xml**: 品牌SOV分析图表
- **chart71.xml**: 品牌SOV分析图表
- **chart72.xml**: 品牌SOV分析图表
- **chart73.xml**: 品牌SOV分析图表
- **chart74.xml**: 品牌SOV分析图表
- **chart75.xml**: 品牌SOV分析图表
- **chart76.xml**: 品牌SOV分析图表
- **chart77.xml**: 品牌SOV分析图表
- **chart78.xml**: 品牌SOV分析图表
- **chart79.xml**: 品牌SOV分析图表
- **chart80.xml**: 品牌SOV分析图表
- **chart81.xml**: 品牌SOV分析图表
- **chart82.xml**: 品牌SOV分析图表

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

## 超高密度图表处理

### 图表分布策略
- **27个SOV图表**: 提供最全面的品牌声量占比分析
- **1个趋势图表**: 专注于Lenovo与竞品的时间序列对比
- **图表类型全覆盖**: 支持饼图、柱状图、面积图、环形图、散点图、折线图等所有类型

### 高性能优化策略
```python
def main() -> int:
    # 批量处理28个图表
    # 复用数据库连接和配置对象
    # 内存池管理，避免内存泄漏
    # 并行处理优化（如果需要）
    for chart_dir in sorted(chart_dirs):
        # 根据图表类型选择相应的数据生成函数
        if t in ('scatterChart', 'lineChart'):
            series = make_trend_lenovo_vs_others(cfg, conn)
        elif t in ('barChart','pieChart','areaChart','doughnutChart'):
            labels, values = make_sov(cfg, conn)
```

### 内存管理
- 分批处理图表，避免内存溢出
- 及时释放不需要的数据对象
- 使用生成器模式处理大数据集
- 优化SQL查询，减少内存占用

## 兜底机制

### 数据缺失处理
- 当数据库查询结果为空时，返回空列表
- 图表构建时会使用 `original_*.json` 缓存文件作为兜底
- 确保PPT始终有数据显示，保持完整性
- 单个图表失败不影响其他27个图表的生成

### 路径探测机制
```python
REPO_ROOT = ROOT.parents[2]
# 自动探测项目根目录和配置文件位置
```

### 错误恢复策略
- 图表级别的异常隔离
- 自动重试机制
- 详细的错误日志记录
- 优雅降级处理

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
    # 3. 遍历所有28个chart目录
    # 4. 根据图表类型生成相应数据
    # 5. 批量写入data.json和final_data.json
    # 6. 性能监控和错误处理
```

### 进度监控
- 实时显示处理进度（1/28, 2/28, ...）
- 估算剩余处理时间
- 内存使用情况监控
- 错误统计和报告

## 构建与测试

### 数据生成
```bash
cd charts/p25
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

### 性能测试
```bash
# 监控内存使用
time python make_data.py

# 验证所有图表数据完整性
python -c "
import json
from pathlib import Path
for i in range(28):
    chart_dir = Path(f'chart{65+i}')
    if chart_dir.exists():
        data_file = chart_dir / 'data.json'
        if data_file.exists():
            with open(data_file) as f:
                data = json.load(f)
                print(f'{chart_dir.name}: OK')
        else:
            print(f'{chart_dir.name}: MISSING')
"
```

## 业务价值与应用

### 市场分析维度
- **最全面品牌竞争格局**: 通过28个图表提供无死角的品牌声量分布分析
- **超细粒度市场份额监控**: SOV指标从所有可能维度反映品牌市场地位变化
- **最深度趋势变化追踪**: Lenovo与竞品的最全面相对表现分析

### 决策支持功能
- **超精细化营销策略优化**: 基于超高密度声量数据制定最精准营销策略
- **全景竞争态势评估**: 识别所有竞争对手和所有细分市场机会
- **多层次多维度预警机制**: 通过28个图表交叉验证及时发现任何品牌声量异常变化

### 高级分析能力
- **最细分市场洞察**: 28个图表支持最细粒度的深入分析
- **最强交叉验证机制**: 大量图表数据交叉验证，提供最高分析可靠性
- **复杂趋势模式识别**: 超大量图表数据支持最复杂趋势模式的识别和预测

### 企业级应用
- **高管决策仪表板**: 为高层管理提供最全面的市场情报
- **战略规划支持**: 支持长期战略规划和市场定位决策
- **风险预警系统**: 通过多维度监控及时发现市场风险

## 技术实现特点

### 超高性能数据处理
- 使用pandas进行超高效数据聚合
- SQL查询深度优化，支持超大数据量处理
- 内存友好的数据结构设计
- 批量处理深度优化，最小化数据库连接开销
- 可选并行处理支持

### 企业级容错机制
- 数据库连接异常处理和自动重连
- 空数据集兜底策略
- 配置文件缺失容错
- 单个图表失败不影响其他27个图表生成
- 详细的错误日志和监控

### 标准化接口
- 统一的数据输出格式
- 标准化的配置加载机制
- 可复用的核心算法函数
- 模块化的图表类型处理
- 可扩展的架构设计

### 监控与运维
- 实时性能监控
- 内存使用情况跟踪
- 处理进度可视化
- 错误统计和报告
- 自动化健康检查

## 与其他页面的关系

### 数据一致性
- 与所有其他页面共享相同的数据源
- 统一的品牌列表和时间范围配置
- 一致的SOV计算逻辑
- 标准化的数据格式

### 功能互补
- P25提供最高密度的图表分析（28个图表）
- 与P8（7图表）、P21（4图表）、P22（5图表）、P23（16图表）、P24（28图表）形成完整的分析层次体系
- 支持从概览到详细再到超详细再到极详细的完整分析需求

### 架构价值
- 作为超高密度分析页面的标准实现
- 为系统性能极限测试提供基准
- 验证系统在极高负载下的稳定性和性能
- 为未来更复杂页面提供技术参考和最佳实践

### 系统压力测试
- 验证数据库连接池的稳定性
- 测试内存管理的有效性
- 评估批量处理的性能极限
- 检验错误处理机制的完备性

## 特殊技术考虑

### 图表编号连续性
- P25页面的图表编号从chart65开始，与P24页面形成连续序列
- 这种设计确保了整个系统中图表编号的唯一性和连续性
- 便于全局图表管理和索引

### 数据一致性验证
- 与P24页面共享部分图表编号范围（chart65-chart82）
- 需要确保两个页面对相同编号图表的数据处理逻辑一致
- 实现跨页面的数据验证和校验机制

### 性能基准对比
- 作为P24页面的对照组，验证系统在相同负载下的稳定性
- 提供性能基准数据，用于系统优化和调优
- 支持A/B测试和性能回归测试
