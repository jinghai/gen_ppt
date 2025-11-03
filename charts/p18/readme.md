# P18页面 - Lenovo Net Lovers（法国）

## 页面说明
- **模板**：`charts/p18/p18.pptx`（不可修改模板本体，页面级脚本仅替换数据）
- **输出**：`charts/p18/output/p18-final.pptx`（单页，可在 PPT 编辑器内查看和修改内嵌数据）
- **附图解释**：`charts/p18/p18-图表解释.md`（仅描述结构与数据对应）
- **详细需求**：`charts/p18/需求.md`

## 指标与定义（摘要）
- **Lovers%**：法国市场、Lenovo 相关提及中，情感为正面（sentiment > 0）的占比
- **Neutral%**：法国市场、Lenovo 相关提及中，情感为中性（sentiment = 0）的占比  
- **Haters%**：法国市场、Lenovo 相关提及中，情感为负面（sentiment < 0）的占比
- **Net Lovers%** = Lovers% - Haters%
- **Ranking**：当月法国市场中，多品牌的 Net Lovers% 排序，Lenovo 的名次

## 配置参数（config.yaml）
```yaml
# 数据源配置
data_sources:
  neticle_db: "input/neticle-v4-08.sqlite"
  neticle_table: "mentions_wide"
  date_column: "date"
  country_column: "countryId"
  sentiment_column: "sentiment"
  country_id: 39  # 法国

# 品牌过滤配置
filters:
  keyword_like: "%lenovo%"  # Lenovo品牌的LIKE模式

# 情感阈值配置
sentiment_thresholds:
  lovers_min: 0.1
  neutral_min: -0.1
  neutral_max: 0.1
  haters_max: -0.1

# 排名品牌配置
ranking:
  brands: ["lenovo","dell","hp","asus","acer","apple","samsung"]  # 参与排名的品牌列表
```

## 数据来源与查询规则
- **主数据源**：`input/neticle-v4-08.sqlite` 宽表 `mentions_wide`
- **严格品牌匹配**：仅使用 `keyword_label` 字段进行品牌识别
  - Lenovo：`keyword_label LIKE '%lenovo%'`
  - 其他品牌：`keyword_label LIKE '%{brand.lower()}%'`
- **国家过滤**：`countryId = 39`（法国）
- **错误处理**：如果 `keyword_label` 字段不存在，立即报错，不允许回退

## 使用方法
### 一键构建
```bash
# 在项目根目录执行
python charts/p18/build.py
```

### 分步执行
```bash
# 1. 生成Excel数据文件
python charts/p18/generate_excel.py

# 2. 填充PPT图表数据
python charts/p18/fill_from_excel.py
```

## 生成物
- **汇总数据**：`charts/p18/p18_data.xlsx`（便于人工检验/修订）
- **页面嵌入**：`charts/p18/tmp/ppt/embeddings/Microsoft_Office_Excel_Binary_Worksheet{1..4}.xlsx`
- **页面图表 XML**：`charts/p18/tmp/ppt/charts/chart{1..4}.xml` 与 `_rels/chartX.xml.rels`
- **最终输出**：`charts/p18/output/p18-final.pptx`

## 计算逻辑
### 时间范围（自动发现）
- **MainTrend**: 最近6个月的数据
- **Ranking**: 最近4个月的数据  
- **Lovers/Neutral/Haters**: 最近4个月的数据
- **月份自动发现**：基于数据库中实际存在的数据月份

### 数据计算流程
1. **模板数据提取**：从 `p18.pptx` 提取现有图表数据和月份标签
2. **数据库连接**：连接SQLite数据库，验证表结构
3. **月份发现**：自动发现数据库中可用的月份数据
4. **品牌数据查询**：
   ```sql
   SELECT strftime('%Y-%m', date) as month,
          SUM(CASE WHEN sentiment > 0.1 THEN 1 ELSE 0 END) as lovers,
          SUM(CASE WHEN sentiment BETWEEN -0.1 AND 0.1 THEN 1 ELSE 0 END) as neutral,
          SUM(CASE WHEN sentiment < -0.1 THEN 1 ELSE 0 END) as haters,
          COUNT(*) as total
   FROM mentions_wide 
   WHERE countryId = 39 AND keyword_label LIKE '%lenovo%'
   GROUP BY month
   ```
5. **百分比计算**：
   - Lovers% = (lovers / total) × 100
   - Neutral% = (neutral / total) × 100
   - Haters% = (haters / total) × 100
   - Net Lovers% = Lovers% - Haters%
6. **排名计算**：对所有配置品牌计算Net Lovers%并排序

### 严格模式特性
- **无回退策略**：数据库连接失败或查询无结果时直接报错
- **字段验证**：`keyword_label` 字段缺失时立即终止
- **国家验证**：`countryId` 字段缺失时立即终止
- **数据完整性**：确保所有必需数据都能正确获取

## 技术架构
### 核心文件
- **`config.yaml`**：配置参数（数据源、过滤条件、阈值等）
- **`generate_excel.py`**：数据库查询与Excel生成（758行）
- **`fill_from_excel.py`**：PPT图表数据填充（305行）
- **`build.py`**：完整构建流程（约100行）

### 关键函数
#### generate_excel.py
- `_get_available_brand_columns()`: 检查数据库表结构
- `_brand_where_and_params()`: 生成品牌过滤SQL条件
- `_query_monthly_sentiment()`: 查询月度情感数据
- `discover_months()`: 自动发现可用月份
- `extract_template_data()`: 提取模板数据

#### fill_from_excel.py
- `read_ranking_values()`: 读取排名数据
- `read_main_trend_values()`: 读取趋势数据
- `update_ranking_texts()`: 更新排名文本
- `update_percentage_texts()`: 更新百分比文本

### 数据流
1. **配置加载** → 读取 `config.yaml` 获取所有参数
2. **模板解析** → 提取PPT模板中的图表结构和数据
3. **数据库查询** → 严格按配置条件查询实际数据
4. **数据计算** → 计算情感百分比和品牌排名
5. **Excel生成** → 生成汇总Excel和4个嵌入文件
6. **PPT更新** → 更新图表XML和关系文件
7. **文件打包** → 生成最终PPT文件

### 错误处理策略
- **立即失败原则**：遇到关键错误立即终止，不允许兜底
- **字段验证**：严格验证数据库表结构
- **数据完整性**：确保所有计算都基于真实数据
- **详细日志**：记录所有关键操作和错误信息

## 依赖管理
### Python包依赖
- **标准库**：`sqlite3`, `json`, `os`, `shutil`, `zipfile`, `xml.etree.ElementTree`
- **第三方库**：`openpyxl`, `yaml`

### 安装命令
```bash
pip install openpyxl pyyaml
```

## 临时文件管理
- **临时目录**：`charts/p18/tmp/`（页面级隔离）
- **自动清理**：构建开始时自动清理临时文件
- **调试文件**：如需调试文件，统一放在项目根目录的 `tmp/` 下

## 关键实现点
- **模板兼容性**：保持模板颜色与系列顺序一致
- **Excel集成**：设置 `externalData/autoUpdate=1`，确保PPT打开时显示最新数据
- **页面隔离**：所有临时文件限制在 `charts/p18/tmp/` 目录内
- **严格验证**：所有数据操作都进行严格验证，确保数据准确性
- **配置驱动**：所有参数通过 `config.yaml` 配置，便于维护和调整

## 注意事项
- **禁止HTTP操作**：不允许使用HTTP预览或下载
- **MVP原则**：避免过度设计，专注核心功能
- **完善注释**：代码包含详细注释，便于维护
- **严格模式**：不允许任何兜底掩盖错误，确保数据可靠性
- **品牌匹配**：严格使用 `keyword_label` 字段，不允许回退到其他字段
