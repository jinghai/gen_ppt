# P30页面 - 单图表品牌SOV分析

## 页面概述

P30页面是品牌声量份额(SOV)分析的单图表页面，包含1个图表（chart131.xml），专注于7个主要品牌的市场声量分布分析，提供最精简的品牌竞争格局洞察。

## 图表配置

### 替换图表列表
- **chart131.xml**: 品牌SOV分析图表

### 配置参数
- **final_mode**: `updated` - 使用更新后的数据
- **axis_day_base**: `20300` - 日期轴基准值

## 数据源与字段映射

### 核心数据表
1. **brand_metrics_month**: 月度品牌指标聚合表

### 关键字段映射
| 字段名 | 数据类型 | 业务含义 | 计算用途 | 原始数据源 |
|--------|----------|----------|----------|------------|
| brand_mentions | INTEGER | 品牌提及数 | SOV分子 | neticle-v5.sqlite/mentions_wide 聚合 |
| total_mentions | INTEGER | 总提及数 | SOV分母 | neticle-v5.sqlite/mentions_wide 聚合 |
| countryId | TEXT | 国家标识 | 数据聚合维度 | dict.sqlite/countries 表 |
| month | TEXT | 月份(YYYY-MM) | SOV时间筛选 | 计算字段 |
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

### 2. 配置加载 (`_load_yaml_cfg`)
**功能**: 加载全局配置和页面特定设置
- 品牌列表: 从 `charts/config.yaml` 获取
- 数据库路径: 支持相对路径和绝对路径
- 时间范围: 由 `charts/config.yaml` 的 `update.start_date`/`update.end_date` 控制自然日范围（整月或跨月）

## 单图表处理策略

### 图表特点
- **专注性**: 仅包含1个SOV分析图表
- **高效性**: 最小的数据处理开销
- **精准性**: 专注于核心品牌竞争格局分析

### 优化策略
```python
def main() -> int:
    # 处理1个图表
    # 最小化资源消耗
    # 快速生成核心分析结果
    chart_dir = ROOT / 'chart131'
    if chart_dir.exists():
        t = _chart_type(chart_dir / 'chart131.xml')
        if t in ('barChart','pieChart','areaChart','doughnutChart'):
            labels, values = make_sov(cfg, conn)
            write_cat_json(chart_dir, labels, values)
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

## 主函数执行流程

### 图表类型识别
```python
def _chart_type(chart_xml: Path) -> str:
    # 解析XML，识别图表类型
    # 支持: barChart, pieChart, areaChart, doughnutChart
```

### 数据生成与写入
```python
def main() -> int:
    # 1. 加载配置
    # 2. 连接数据库
    # 3. 处理单个chart目录
    # 4. 生成SOV数据
    # 5. 写入data.json和final_data.json
```

## 构建与测试

### 数据生成
```bash
cd charts/p30
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
- **核心竞争格局**: 通过单一SOV图表提供最直观的品牌声量分布
- **快速洞察**: 专注于最重要的市场份额信息
- **简洁展示**: 适合高层汇报和快速决策场景

### 决策支持功能
- **即时分析**: 基于单一图表快速了解品牌竞争态势
- **核心指标监控**: 专注于SOV这一关键市场指标
- **高效沟通**: 简化的图表设计便于跨部门沟通

### 高级分析能力
- **精准定位**: 单图表设计确保关键信息不被稀释
- **快速响应**: 最小的数据处理时间支持实时分析需求
- **核心价值提取**: 从复杂数据中提取最核心的竞争信息

## 技术实现特点

### 极简数据处理
- 仅处理SOV计算，无需趋势分析
- 最小的SQL查询复杂度
- 极低的内存和CPU占用
- 最快的数据生成速度

### 轻量级架构
- 单一图表处理逻辑
- 简化的错误处理机制
- 最小的依赖关系
- 高度优化的执行路径

### 标准化接口
- 与其他页面保持一致的数据输出格式
- 标准化的配置加载机制
- 可复用的核心SOV算法
- 模块化的图表类型处理

## 与其他页面的关系

### 数据一致性
- 与所有其他页面共享相同的数据源
- 统一的品牌列表和时间范围配置
- 一致的SOV计算逻辑

### 功能互补
- P30提供最精简的SOV分析
- 与P8（7图表）、P21（4图表）、P22（5图表）、P23（16图表）、P24（28图表）、P25（28图表）、P26（2图表）、P27（2图表）、P29（1图表）形成完整的分析层次体系
- 支持快速概览和核心洞察需求

### 架构价值
- 作为最小化分析页面的标准实现
- 为快速分析和核心指标监控提供模板
- 验证系统在最轻量级场景下的基础功能

## 特殊技术考虑

### 图表编号特点
- P30页面使用chart131，编号相对较高
- 单图表设计可能表示其在PPT中的特殊用途
- 便于与多图表页面进行区分和管理

### 性能优势
- 单图表设计确保最优的处理性能
- 最小的资源消耗和系统负载
- 适合高频更新和实时监控场景
- 支持移动端和低配置环境

### 应用场景
- **执行摘要**: 适合放置在报告的执行摘要部分
- **仪表板**: 作为监控仪表板的核心指标展示
- **移动端**: 单图表设计完美适配移动设备
- **快速汇报**: 支持快速的口头汇报和讨论

## 与多图表页面的对比

### 优势
- **加载速度**: 最快的数据加载和图表渲染速度
- **资源效率**: 最低的内存和CPU占用
- **维护成本**: 最简单的代码结构和维护需求
- **用户体验**: 最直观的信息展示，无认知负担

### 适用场景
- **高层汇报**: 适合向高层管理者展示核心竞争态势
- **移动查看**: 在移动设备上查看关键指标
- **快速决策**: 需要基于核心数据快速做出决策
- **系统监控**: 作为监控系统的核心指标展示

### 局限性
- **信息深度**: 无法提供趋势分析和时间序列洞察
- **对比维度**: 缺少多维度的对比分析能力
- **详细程度**: 不适合需要详细分析的业务场景

## 与P29页面的对比

### 相似性
- 都是单图表SOV分析页面
- 相同的数据处理逻辑和算法实现
- 一致的性能优势和应用场景

### 差异性
- **图表编号**: P30使用chart131，P29使用chart115
- **PPT位置**: 可能在PPT中承担不同的展示角色
- **业务用途**: 可能针对不同的业务场景或受众群体

### 技术价值
- 验证单图表页面设计的可复用性
- 提供多个轻量级分析入口
- 支持不同业务场景的个性化需求
