# 输出指标库字段说明

## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | TEXT | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | INTEGER | intent_posts / intent_total |
| `preference` | 偏好度 | INTEGER | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | INTEGER | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | TEXT | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | INTEGER | intent_posts / intent_total |
| `preference` | 偏好度 | INTEGER | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | INTEGER | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | TEXT | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | INTEGER | intent_posts / intent_total |
| `preference` | 偏好度 | INTEGER | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | INTEGER | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | TEXT | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | INTEGER | intent_posts / intent_total |
| `preference` | 偏好度 | INTEGER | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | INTEGER | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | TEXT | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | INTEGER | intent_posts / intent_total |
| `preference` | 偏好度 | INTEGER | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | INTEGER | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | TEXT | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | INTEGER | intent_posts / intent_total |
| `preference` | 偏好度 | INTEGER | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | INTEGER | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | TEXT | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | INTEGER | intent_posts / intent_total |
| `preference` | 偏好度 | INTEGER | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | INTEGER | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | TEXT | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | INTEGER | intent_posts / intent_total |
| `preference` | 偏好度 | INTEGER | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | INTEGER | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | TEXT | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | INTEGER | intent_posts / intent_total |
| `preference` | 偏好度 | INTEGER | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | INTEGER | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | TEXT | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | INTEGER | intent_posts / intent_total |
| `preference` | 偏好度 | INTEGER | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | INTEGER | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | TEXT | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | INTEGER | intent_posts / intent_total |
| `preference` | 偏好度 | INTEGER | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | INTEGER | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | TEXT | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | INTEGER | intent_posts / intent_total |
| `preference` | 偏好度 | INTEGER | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | INTEGER | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | TEXT | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | INTEGER | intent_posts / intent_total |
| `preference` | 偏好度 | INTEGER | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | INTEGER | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_day

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `day` | 日期 | TEXT | 日期标签 YYYY-MM-DD |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_week

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `week` | 周 | TEXT | 周标签 YYYY-WNN |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_month

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `month` | 月份 | TEXT | 月份标签 YYYY-MM |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_quarter

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `quarter` | 季度 | TEXT | 季度标签 YYYY-QN |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## brand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `brand` | 品牌 | TEXT | 品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
## subbrand_metrics_year

| 字段名 | 中文名 | 数据类型 | 说明 |
|---|---|---|---|
| `countryName` | 国家名 | TEXT | 源 mentions_wide.countryName |
| `countryId` | 国家ID | INTEGER | 国家标识（Neticle） |
| `year` | 年份 | TEXT | 年份标签 YYYY |
| `subbrand` | 子品牌 | TEXT | 子品牌名称（关键词分组映射） |
| `sov` | 声量比 | REAL | brand_mentions / total_mentions |
| `awareness` | 认知度 | REAL | brand_authors / total_authors |
| `consideration` | 考虑度 | REAL | intent_posts / intent_total |
| `preference` | 偏好度 | REAL | prefer_posts / prefer_total |
| `brand_love` | 好感度 | REAL | positive_mentions / brand_mentions |
| `bhi` | 健康度 | REAL | 加权综合(awareness, consideration, preference, brand_love) |
| `brand_power` | 品牌力 | REAL | interaction_index * coverage_rate * competition_coeff |
| `premium_index` | 高端指数 | REAL | premium_posts / premium_total |
| `intent_posts` | 购买意向帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `prefer_posts` | 偏好帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `premium_posts` | 高端帖子数 | INTEGER | 命中文本关键词的帖子数（品牌） |
| `brand_mentions` | 品牌及数 | INTEGER | 品牌提及计数 |
| `positive_mentions` | 正向提及 | INTEGER | polarity 超过正阈值计数 |
| `negative_mentions` | 负向提及 | INTEGER | polarity 低于负阈值计数 |
| `neutral_mentions` | 中性提及 | INTEGER | polarity 等于 0 的计数 |
| `total_interactions` | 总互动 | INTEGER | sumInteractions 合计 |
| `brand_authors` | 唯一作者 | INTEGER | 品牌范围内 DISTINCT author 数 |
| `total_mentions` | 总提及 | INTEGER | 当期所有提及计数 |
| `total_authors` | 总唯一作者 | INTEGER | 当期所有提及的唯一作者数 |
| `source_count` | 品牌来源数 | INTEGER | 品牌覆盖到的 DISTINCT sourceId 数 |
| `total_sources` | 总来源数 | INTEGER | 全局来源总数（字典库或回退 DISTINCT sourceId） |
| `interaction_benchmark` | 互动基准 | REAL | 同期 log_interactions 的 75% 分位 |
| `coverage_benchmark` | 覆盖基准 | REAL | 同期 coverage_rate 的均值 |
| `competition_benchmark` | 竞争基准 | REAL | 同期 TOP3 interaction_index 的均值 |
| `log_interactions` | 互动对数 | REAL | log10(total_interactions + 1) |
