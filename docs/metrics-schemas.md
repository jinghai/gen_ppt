# Database Schema

本文档描述了 metrics 数据库中的表结构。

## 表结构

### brand_metrics_day
存储每日品牌指标数据。

| 字段名 | 数据类型 | 说明 |
|--------|----------|------|
| brandId | INTEGER | 品牌标识符 |
| date | DATE | 日期 |
| brand_mentions | INTEGER | 品牌提及数 |
| positive_mentions | INTEGER | 正面提及数 |
| negative_mentions | INTEGER | 负面提及数 |
| total_interactions | REAL | 总互动数 |
| sov | REAL | 声量份额 |
| sov_wider | REAL | 更广泛声量份额 |
| awareness | REAL | 品牌认知度 |
| brand_love | REAL | 品牌喜爱度 |
| brand_power | REAL | 品牌影响力 |
| bhi | REAL | 品牌健康指数 |
| consideration | REAL | 考虑度 |
| preference | REAL | 偏好度 |
| premium_index | REAL | 高端指数 |
| log_interactions | REAL | 对数互动量 |
| interaction_index | REAL | 互动指数 |
| coverage_rate | REAL | 覆盖率 |
| competition_coeff | REAL | 竞争系数 |

### brand_metrics_month
存储每月品牌指标数据。

| 字段名 | 数据类型 | 说明 |
|--------|----------|------|
| brandId | INTEGER | 品牌标识符 |
| year | INTEGER | 年份 |
| month | INTEGER | 月份 |
| brand_mentions | INTEGER | 品牌提及数 |
| positive_mentions | INTEGER | 正面提及数 |
| negative_mentions | INTEGER | 负面提及数 |
| total_interactions | REAL | 总互动数 |
| sov | REAL | 声量份额 |
| sov_wider | REAL | 更广泛声量份额 |
| awareness | REAL | 品牌认知度 |
| brand_love | REAL | 品牌喜爱度 |
| brand_power | REAL | 品牌影响力 |
| bhi | REAL | 品牌健康指数 |
| consideration | REAL | 考虑度 |
| preference | REAL | 偏好度 |
| premium_index | REAL | 高端指数 |
| log_interactions | REAL | 对数互动量 |
| interaction_index | REAL | 互动指数 |
| coverage_rate | REAL | 覆盖率 |
| competition_coeff | REAL | 竞争系数 |

### brand_metrics_week
存储每周品牌指标数据。

| 字段名 | 数据类型 | 说明 |
|--------|----------|------|
| brandId | INTEGER | 品牌标识符 |
| year | INTEGER | 年份 |
| week | INTEGER | 周数 |
| brand_mentions | INTEGER | 品牌提及数 |
| positive_mentions | INTEGER | 正面提及数 |
| negative_mentions | INTEGER | 负面提及数 |
| total_interactions | REAL | 总互动数 |
| sov | REAL | 声量份额 |
| sov_wider | REAL | 更广泛声量份额 |
| awareness | REAL | 品牌认知度 |
| brand_love | REAL | 品牌喜爱度 |
| brand_power | REAL | 品牌影响力 |
| bhi | REAL | 品牌健康指数 |
| consideration | REAL | 考虑度 |
| preference | REAL | 偏好度 |
| premium_index | REAL | 高端指数 |
| log_interactions | REAL | 对数互动量 |
| interaction_index | REAL | 互动指数 |
| coverage_rate | REAL | 覆盖率 |
| competition_coeff | REAL | 竞争系数 |

### brand_metrics_year
存储每年品牌指标数据。

| 字段名 | 数据类型 | 说明 |
|--------|----------|------|
| brandId | INTEGER | 品牌标识符 |
| year | INTEGER | 年份 |
| brand_mentions | INTEGER | 品牌提及数 |
| positive_mentions | INTEGER | 正面提及数 |
| negative_mentions | INTEGER | 负面提及数 |
| total_interactions | REAL | 总互动数 |
| sov | REAL | 声量份额 |
| sov_wider | REAL | 更广泛声量份额 |
| awareness | REAL | 品牌认知度 |
| brand_love | REAL | 品牌喜爱度 |
| brand_power | REAL | 品牌影响力 |
| bhi | REAL | 品牌健康指数 |
| consideration | REAL | 考虑度 |
| preference | REAL | 偏好度 |
| premium_index | REAL | 高端指数 |
| log_interactions | REAL | 对数互动量 |
| interaction_index | REAL | 互动指数 |
| coverage_rate | REAL | 覆盖率 |
| competition_coeff | REAL | 竞争系数 |

### subbrand_metrics_day
存储每日子品牌指标数据。

| 字段名 | 数据类型 | 说明 |
|--------|----------|------|
| brandId | INTEGER | 品牌标识符 |
| subbrandId | INTEGER | 子品牌标识符 |
| date | DATE | 日期 |
| brand_mentions | INTEGER | 品牌提及数 |
| positive_mentions | INTEGER | 正面提及数 |
| negative_mentions | INTEGER | 负面提及数 |
| total_interactions | REAL | 总互动数 |
| sov | REAL | 声量份额 |
| sov_wider | REAL | 更广泛声量份额 |
| awareness | REAL | 品牌认知度 |
| brand_love | REAL | 品牌喜爱度 |
| brand_power | REAL | 品牌影响力 |
| bhi | REAL | 品牌健康指数 |
| consideration | REAL | 考虑度 |
| preference | REAL | 偏好度 |
| premium_index | REAL | 高端指数 |
| log_interactions | REAL | 对数互动量 |
| interaction_index | REAL | 互动指数 |
| coverage_rate | REAL | 覆盖率 |
| competition_coeff | REAL | 竞争系数 |

### subbrand_metrics_month
存储每月子品牌指标数据。

| 字段名 | 数据类型 | 说明 |
|--------|----------|------|
| brandId | INTEGER | 品牌标识符 |
| subbrandId | INTEGER | 子品牌标识符 |
| year | INTEGER | 年份 |
| month | INTEGER | 月份 |
| brand_mentions | INTEGER | 品牌提及数 |
| positive_mentions | INTEGER | 正面提及数 |
| negative_mentions | INTEGER | 负面提及数 |
| total_interactions | REAL | 总互动数 |
| sov | REAL | 声量份额 |
| sov_wider | REAL | 更广泛声量份额 |
| awareness | REAL | 品牌认知度 |
| brand_love | REAL | 品牌喜爱度 |
| brand_power | REAL | 品牌影响力 |
| bhi | REAL | 品牌健康指数 |
| consideration | REAL | 考虑度 |
| preference | REAL | 偏好度 |
| premium_index | REAL | 高端指数 |
| log_interactions | REAL | 对数互动量 |
| interaction_index | REAL | 互动指数 |
| coverage_rate | REAL | 覆盖率 |
| competition_coeff | REAL | 竞争系数 |

### subbrand_metrics_week
存储每周子品牌指标数据。

| 字段名 | 数据类型 | 说明 |
|--------|----------|------|
| brandId | INTEGER | 品牌标识符 |
| subbrandId | INTEGER | 子品牌标识符 |
| year | INTEGER | 年份 |
| week | INTEGER | 周数 |
| brand_mentions | INTEGER | 品牌提及数 |
| positive_mentions | INTEGER | 正面提及数 |
| negative_mentions | INTEGER | 负面提及数 |
| total_interactions | REAL | 总互动数 |
| sov | REAL | 声量份额 |
| sov_wider | REAL | 更广泛声量份额 |
| awareness | REAL | 品牌认知度 |
| brand_love | REAL | 品牌喜爱度 |
| brand_power | REAL | 品牌影响力 |
| bhi | REAL | 品牌健康指数 |
| consideration | REAL | 考虑度 |
| preference | REAL | 偏好度 |
| premium_index | REAL | 高端指数 |
| log_interactions | REAL | 对数互动量 |
| interaction_index | REAL | 互动指数 |
| coverage_rate | REAL | 覆盖率 |
| competition_coeff | REAL | 竞争系数 |

### subbrand_metrics_year
存储每年子品牌指标数据。

| 字段名 | 数据类型 | 说明 |
|--------|----------|------|
| brandId | INTEGER | 品牌标识符 |
| subbrandId | INTEGER | 子品牌标识符 |
| year | INTEGER | 年份 |
| brand_mentions | INTEGER | 品牌提及数 |
| positive_mentions | INTEGER | 正面提及数 |
| negative_mentions | INTEGER | 负面提及数 |
| total_interactions | REAL | 总互动数 |
| sov | REAL | 声量份额 |
| sov_wider | REAL | 更广泛声量份额 |
| awareness | REAL | 品牌认知度 |
| brand_love | REAL | 品牌喜爱度 |
| brand_power | REAL | 品牌影响力 |
| bhi | REAL | 品牌健康指数 |
| consideration | REAL | 考虑度 |
| preference | REAL | 偏好度 |
| premium_index | REAL | 高端指数 |
| log_interactions | REAL | 对数互动量 |
| interaction_index | REAL | 互动指数 |
| coverage_rate | REAL | 覆盖率 |
| competition_coeff | REAL | 竞争系数 |