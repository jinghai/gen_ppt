# P31页面 - 10图表品牌SOV与趋势分析

## 页面概述

P31页面是品牌声量份额(SOV)与趋势分析的10图表页面，包含10个图表（chart169.xml到chart175.xml等），提供中等密度的品牌竞争格局分析，在简洁性和信息丰富度之间取得平衡。

## 图表配置

### 替换图表列表
- **chart169.xml**: 品牌SOV分析图表
- **chart170.xml**: 品牌SOV分析图表
- **chart171.xml**: 品牌SOV分析图表
- **chart172.xml**: 品牌SOV分析图表
- **chart173.xml**: 品牌SOV分析图表
- **chart174.xml**: 品牌SOV分析图表
- **chart175.xml**: 品牌SOV分析图表
- **chart176.xml**: 品牌SOV分析图表
- **chart177.xml**: 品牌SOV分析图表
- **chart178.xml**: 品牌SOV分析图表

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

### 扩展指标字段
| 字段名 | 数据类型 | 业务含义 | 计算公式 |
|--------|----------|----------|----------|
| sov | REAL | 声量占比 | (brand_mentions / total_mentions) × 100% |
| awareness | REAL | 品牌知名度 | 预计算指标 |
| consideration | REAL | 品牌考虑度 | 预计算指标 |
| preference | REAL | 品牌偏好度 | 预计算指标 |
| bhi | REAL | 品牌健康指数 | (awareness×0.3 + consideration×0.4 + preference×0.3) |

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
**功能**: 生成Lenovo vs Others的日级对比数据
```python
def make_trend_lenovo_vs_others(cfg: Config, conn: sqlite3.Connection) -> List[Dict]:
    # 查询日级数据
    # 计算Lenovo声量和Others合计声量
    # 生成时间序列数据点
    return [
        {"name": "Lenovo", "type": "scatter", "data": lenovo_points},
        {"name": "Others", "type": "scatter", "data": others_points}
    ]
```

### 3. 配置加载 (`_load_yaml_cfg`)
**功能**: 加载全局配置和页面特定设置
- 品牌列表: 从 `charts/config.yaml` 获取
- 数据库路径: 支持相对路径和绝对路径
- 时间范围: 由 `charts/config.yaml` 的 `update.start_date`/`update.end_date` 控制自然日范围（整月或跨月）

## 10图表处理策略

### 图表分布特点
- **中等密度**: 10个图表提供适中的信息密度
- **平衡设计**: 在简洁性和详细程度之间取得平衡
- **多维分析**: 支持SOV和趋势的多角度分析

### 处理优化
```python
def main() -> int:
    # 遍历10个chart目录
    for chart_dir in sorted(ROOT.glob('chart*')):
        if chart_dir.is_dir():
            t = _chart_type(chart_dir / f'{chart_dir.name}.xml')
            if t in ('barChart','pieChart','areaChart','doughnutChart'):
                # 生成SOV数据
                labels, values = make_sov(cfg, conn)
                write_cat_json(chart_dir, labels, values)
            elif t in ('scatterChart','lineChart'):
                # 生成趋势数据
                data = make_trend_lenovo_vs_others(cfg, conn)
                write_scatter_json(chart_dir, data)
```

## 兜底机制

### 数据缺失处理
- 当数据库查询结果为空时，返回空列表
- 图表构建时会使用 `original_*.json` 缓存文件作为兜底
- 确保10个图表始终有数据显示，保持PPT完整性

### 缓存文件结构
每个chart目录包含：
- `original_series.json`: 类别图表数据缓存
- `original_scatter.json`: 散点图表数据缓存
- `original_line.json`: 折线图表数据缓存

## 数据格式规范

### 类别图数据格式 (SOV)
```json
{
  "labels": ["Lenovo", "Dell", "Hp", "Asus", "Acer", "Apple", "Samsung"],
  "series": [{"name": null, "values": [25.3, 18.7, 15.2, 12.8, 10.5, 9.1, 8.4]}]
}
```

### 散点/折线图数据格式 (趋势)
```json
[
  {
    "name": "Lenovo",
    "type": "scatter",
    "data": [
      {"x": 20301.0, "y": 1250},
      {"x": 20302.0, "y": 1180}
    ]
  },
  {
    "name": "Others",
    "type": "scatter", 
    "data": [
      {"x": 20301.0, "y": 6890},
      {"x": 20302.0, "y": 7120}
    ]
  }
]
```

## 主函数执行流程

### 图表类型识别
```python
def _chart_type(chart_xml: Path) -> str:
    # 解析XML，识别图表类型
    # 支持: barChart, pieChart, areaChart, doughnutChart, scatterChart, lineChart
```

### 数据生成与写入
```python
def main() -> int:
    # 1. 加载配置
    # 2. 连接数据库
    # 3. 遍历10个chart目录
    # 4. 根据图表类型生成相应数据
    # 5. 写入data.json和final_data.json
```

## 构建与测试

### 数据生成
```bash
cd charts/p31
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
- **中等密度监控**: 10个图表提供适中的市场视角
- **多维度SOV分析**: 不同角度的声量占比分析
- **竞争态势评估**: Lenovo与竞品的对比分析
- **趋势变化追踪**: 基于时间序列的趋势分析

### 决策支持功能
- **战术规划**: 基于中等密度数据制定战术策略
- **营销优化**: 识别营销投入的关键时机
- **品牌监控**: 监控品牌健康状况和市场地位
- **竞争分析**: 分析竞品动态和市场变化

### 高级分析能力
- **平衡视角**: 在详细程度和可读性之间取得平衡
- **多角度洞察**: 通过10个图表提供多维度分析
- **趋势预测**: 基于历史数据预测品牌发展趋势

## 技术实现特点

### 中等复杂度处理
- 处理10个图表的数据生成和管理
- 平衡的SQL查询复杂度
- 适中的内存和CPU占用
- 合理的数据生成时间

### 模块化架构
- 支持SOV和趋势两种主要分析类型
- 标准化的图表类型处理
- 可扩展的数据处理流程
- 统一的错误处理机制

### 标准化接口
- 与其他页面保持一致的数据输出格式
- 标准化的配置加载机制
- 可复用的核心算法
- 模块化的图表类型处理

## 与其他页面的关系

### 数据一致性
- 与所有其他页面共享相同的数据源
- 统一的品牌列表和时间范围配置
- 一致的SOV计算逻辑和趋势分析方法

### 功能互补
- P31提供中等密度的SOV与趋势分析
- 与P8（7图表）、P21（4图表）、P22（5图表）、P23（16图表）、P24（28图表）、P25（28图表）、P26（2图表）、P27（2图表）、P29（1图表）、P30（1图表）形成完整的分析层次体系
- 在简洁性和详细程度之间提供平衡选择

### 架构价值
- 作为中等复杂度分析页面的标准实现
- 为平衡型分析需求提供模板
- 验证系统在中等规模场景下的处理能力

## 特殊技术考虑

### 图表编号特点
- P31页面使用chart169-chart178，编号连续且较高
- 10图表设计表示其在PPT中的重要地位
- 便于与其他密度级别的页面进行区分

### 性能平衡
- 10图表设计在性能和功能之间取得平衡
- 适中的资源消耗和系统负载
- 支持定期更新和实时监控需求
- 兼容多种部署环境

### 应用场景
- **中层管理**: 适合中层管理者的详细分析需求
- **业务分析**: 支持业务分析师的深度分析工作
- **定期报告**: 适合定期业务报告的标准格式
- **跨部门协作**: 平衡的信息密度便于跨部门沟通

## 与其他密度级别页面的对比

### 与单图表页面（P29、P30）对比
**优势**:
- **信息丰富度**: 10个图表提供更全面的分析视角
- **多维分析**: 支持SOV和趋势的综合分析
- **业务价值**: 更高的业务洞察价值

**劣势**:
- **复杂度**: 相对更高的处理复杂度
- **资源消耗**: 更多的内存和CPU占用

### 与高密度页面（P23、P24、P25）对比
**优势**:
- **可读性**: 更好的图表可读性和理解性
- **维护性**: 更简单的维护和调试
- **性能**: 更优的处理性能

**劣势**:
- **信息密度**: 相对较低的信息密度
- **分析深度**: 有限的深度分析能力

### 最佳适用场景
- **标准业务报告**: 适合大多数业务报告需求
- **中层决策支持**: 为中层管理者提供决策支持
- **平衡型分析**: 在简洁性和详细程度之间需要平衡的场景
- **跨职能协作**: 需要跨职能团队协作的分析项目

## 技术架构优势

### 扩展性
- 支持新增图表类型和分析维度
- 配置驱动的图表参数管理
- 标准化的数据接口设计

### 可维护性
- 清晰的代码结构和模块划分
- 统一的错误处理和日志记录
- 完善的文档和注释

### 可靠性
- 多层兜底机制确保数据可用性
- 完善的异常处理和恢复机制
- 数据一致性检查和验证
