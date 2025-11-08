# Database Schema

本文档描述了 neticle 数据库中的表结构。

## 表结构

### mentions_wide
存储带有额外分析字段的丰富提及数据。

| 字段名 | 数据类型 | 说明 |
|--------|----------|------|
| id | TEXT | 主键 |
| author | NUMERIC | 作者标识符 |
| countryId | NUMERIC | 国家标识符 |
| countryName | NUMERIC | 国家名称 |
| createdAtUtcMs | NUMERIC | 创建时间（UTC毫秒） |
| discoveredAtUtcMs | NUMERIC | 发现时间（UTC毫秒） |
| keywordId | NUMERIC | 关键词标识符 |
| keyword_ianaLanguages | NUMERIC | 关键词IANA语言 |
| keyword_ianaTimeZone | NUMERIC | 关键词IANA时区 |
| keyword_label | NUMERIC | 关键词标签 |
| polarity | NUMERIC | 情感极性 |
| reach | NUMERIC | 覆盖范围 |
| sourceId | NUMERIC | 数据源标识符 |
| sourceName | NUMERIC | 数据源名称 |
| sourceLabel | NUMERIC | 数据源标签 |
| sumComments | NUMERIC | 总评论数 |
| sumInteractions | NUMERIC | 总互动数 |
| sumLikes | NUMERIC | 总点赞数 |
| sumShares | NUMERIC | 总分享数 |
| textOriginal | NUMERIC | 原始文本内容 |
| title | NUMERIC | 标题 |
| aspectId | NUMERIC | 方面标识符 |
| attributeLabelIds | NUMERIC | 属性标签标识符 |
| brandLabelIds | NUMERIC | 品牌标签标识符 |
| cityId | NUMERIC | 城市标识符 |
| cityLabel | NUMERIC | 城市标签 |
| cityCountryId | NUMERIC | 城市所属国家标识符 |
| contentLength | NUMERIC | 内容长度 |
| domain | NUMERIC | 域名 |
| emotionLabelIds | NUMERIC | 情感标签标识符 |
| engagementRate | NUMERIC | 互动率 |
| facebookDetails | NUMERIC | Facebook详情 |
| facebookDetails_angry | NUMERIC | Facebook愤怒数 |
| facebookDetails_care | NUMERIC | Facebook关心数 |
| facebookDetails_comment | NUMERIC | Facebook评论数 |
| facebookDetails_fan | NUMERIC | Facebook粉丝数 |
| facebookDetails_haha | NUMERIC | Facebook搞笑数 |
| facebookDetails_like | NUMERIC | Facebook点赞数 |
| facebookDetails_love | NUMERIC | Facebook爱心数 |
| facebookDetails_reply | NUMERIC | Facebook回复数 |
| facebookDetails_sad | NUMERIC | Facebook难过数 |
| facebookDetails_share | NUMERIC | Facebook分享数 |
| facebookDetails_wow | NUMERIC | Facebook惊讶数 |
| genderId | NUMERIC | 性别标识符 |
| genderLabel | NUMERIC | 性别标签 |
| genderName | NUMERIC | 性别名称 |
| hash | NUMERIC | 哈希值 |
| imageAttachments | NUMERIC | 图片附件 |
| importance | NUMERIC | 重要性评分 |
| instagramDetails | NUMERIC | Instagram详情 |
| instagramDetails_comment | NUMERIC | Instagram评论数 |
| instagramDetails_follower | NUMERIC | Instagram粉丝数 |
| instagramDetails_like | NUMERIC | Instagram点赞数 |
| instagramDetails_score | NUMERIC | Instagram评分 |
| instagramDetails_view | NUMERIC | Instagram观看数 |
| isMarked | NUMERIC | 是否标记 |
| languageId | NUMERIC | 语言标识符 |
| languageLabel | NUMERIC | 语言标签 |
| languageIsoCode2 | NUMERIC | 语言ISO代码 |
| latitude | NUMERIC | 纬度 |
| linkedinDetails | NUMERIC | LinkedIn详情 |
| linkedinDetails_celebrate | NUMERIC | LinkedIn庆祝数 |
| linkedinDetails_comment | NUMERIC | LinkedIn评论数 |
| linkedinDetails_curious | NUMERIC | LinkedIn好奇数 |
| linkedinDetails_follower | NUMERIC | LinkedIn粉丝数 |
| linkedinDetails_funny | NUMERIC | LinkedIn搞笑数 |
| linkedinDetails_insightful | NUMERIC | LinkedIn洞察数 |
| linkedinDetails_like | NUMERIC | LinkedIn点赞数 |
| linkedinDetails_love | NUMERIC | LinkedIn爱心数 |
| linkedinDetails_share | NUMERIC | LinkedIn分享数 |
| linkedinDetails_support | NUMERIC | LinkedIn支持数 |
| linkedinDetails_view | NUMERIC | LinkedIn观看数 |
| locationLabelIds | NUMERIC | 位置标签标识符 |
| longitude | NUMERIC | 经度 |
| note | NUMERIC | 备注 |
| organizationLabelIds | NUMERIC | 组织标签标识符 |
| ownChannelId | NUMERIC | 自有频道标识符 |
| ownChannelType | NUMERIC | 自有频道类型 |
| ownChannelKeywordId | NUMERIC | 自有频道关键词标识符 |
| ownChannelProfileId | NUMERIC | 自有频道档案标识符 |
| ownChannelClientId | NUMERIC | 自有频道客户端标识符 |
| ownChannelCountryId | NUMERIC | 自有频道国家标识符 |
| personLabelIds | NUMERIC | 人物标签标识符 |
| pinterestDetails | NUMERIC | Pinterest详情 |
| pinterestDetails_comment | NUMERIC | Pinterest评论数 |
| pinterestDetails_like | NUMERIC | Pinterest点赞数 |
| regionId | NUMERIC | 区域标识符 |
| regionLabel | NUMERIC | 区域标签 |
| regionCountryId | NUMERIC | 区域所属国家标识符 |
| relatedDiscussionUrl | NUMERIC | 相关讨论URL |
| relatedUrl | NUMERIC | 相关URL |
| relevantTextFormatted | NUMERIC | 相关格式化文本 |
| relevantTextOriginal | NUMERIC | 相关原始文本 |
| reviewDetails | NUMERIC | 评论详情 |
| subSourceId | NUMERIC | 子数据源标识符 |
| sumDislikes | NUMERIC | 总点踩数 |
| sumFollowers | NUMERIC | 总粉丝数 |
| sumReactions | NUMERIC | 总反应数 |
| textFormatted | NUMERIC | 格式化文本内容 |
| threadId | NUMERIC | 线程标识符 |
| thumbnailUrl | NUMERIC | 缩略图URL |
| tiktokDetails | NUMERIC | TikTok详情 |
| tiktokDetails_follower | NUMERIC | TikTok粉丝数 |
| tiktokDetails_like | NUMERIC | TikTok点赞数 |
| tiktokDetails_share | NUMERIC | TikTok分享数 |
| tiktokDetails_view | NUMERIC | TikTok观看数 |
| topicLabelIds | NUMERIC | 主题标签标识符 |
| translatedTextFormatted | NUMERIC | 翻译后格式化文本 |
| translatedTitle | NUMERIC | 翻译后标题 |
| twitterDetails | NUMERIC | Twitter详情 |
| twitterDetails_comment | NUMERIC | Twitter评论数 |
| twitterDetails_follower | NUMERIC | Twitter粉丝数 |
| twitterDetails_like | NUMERIC | Twitter点赞数 |
| twitterDetails_quote | NUMERIC | Twitter引用数 |
| twitterDetails_reply | NUMERIC | Twitter回复数 |
| twitterDetails_retweet | NUMERIC | Twitter转推数 |
| url | NUMERIC | URL地址 |
| urlAttachments | NUMERIC | URL附件 |
| videoAttachments | NUMERIC | 视频附件 |
| youtubeDetails | NUMERIC | YouTube详情 |
| youtubeDetails_comment | NUMERIC | YouTube评论数 |
| youtubeDetails_dislike | NUMERIC | YouTube点踩数 |
| youtubeDetails_like | NUMERIC | YouTube点赞数 |
| youtubeDetails_subscribe | NUMERIC | YouTube订阅数 |
| youtubeDetails_view | NUMERIC | YouTube观看数 |
| sourceCode | NUMERIC | 数据源代码 |
| parentSourceId | NUMERIC | 父数据源标识符 |
| parentSourceCode | NUMERIC | 父数据源代码 |
| sourceIsGroup | NUMERIC | 数据源是否为组 |
| sourceIsEnabled | NUMERIC | 数据源是否启用 |
| sourceOrder | NUMERIC | 数据源排序 |
| sourceColor | NUMERIC | 数据源颜色 |
| sourceCountryId | NUMERIC | 数据源国家标识符 |
| subSourceName | NUMERIC | 子数据源名称 |
| subSourceLabel | NUMERIC | 子数据源标签 |
| subSourceCode | NUMERIC | 子数据源代码 |
| subSourceIsGroup | NUMERIC | 子数据源是否为组 |
| subSourceParentSourceId | NUMERIC | 子数据源父标识符 |
| subSourceParentSourceCode | NUMERIC | 子数据源父代码 |
| subSourceCountryId | NUMERIC | 子数据源国家标识符 |
| countryLabel | NUMERIC | 国家标签 |
| countryIsoCode2 | NUMERIC | 国家ISO代码 |
| countryNeticleCode | NUMERIC | 国家Neticle代码 |
| countryIanaTimeZone | NUMERIC | 国家IANA时区 |
| countryIanaLanguages | NUMERIC | 国家IANA语言 |
| languageNeticleCode | NUMERIC | 语言Neticle代码 |
| cityRegionId | NUMERIC | 城市区域标识符 |
| cityRegionLabel | NUMERIC | 城市区域标签 |
| aspectLabel | NUMERIC | 方面标签 |
| aspectGroupId | NUMERIC | 方面组标识符 |
| ownChannelLabel | NUMERIC | 自有频道标签 |
| ownChannelName | NUMERIC | 自有频道名称 |
| attributeLabelNames | NUMERIC | 属性标签名称 |
| brandLabelNames | NUMERIC | 品牌标签名称 |
| emotionLabelNames | NUMERIC | 情感标签名称 |
| locationLabelNames | NUMERIC | 位置标签名称 |
| organizationLabelNames | NUMERIC | 组织标签名称 |
| personLabelNames | NUMERIC | 人物标签名称 |
| topicLabelNames | NUMERIC | 主题标签名称 |
| attributeLabelCount | NUMERIC | 属性标签数量 |
| brandLabelCount | NUMERIC | 品牌标签数量 |
| emotionLabelCount | NUMERIC | 情感标签数量 |
| locationLabelCount | NUMERIC | 位置标签数量 |
| organizationLabelCount | NUMERIC | 组织标签数量 |
| personLabelCount | NUMERIC | 人物标签数量 |
| topicLabelCount | NUMERIC | 主题标签数量 |

## 索引

- idx_wide_createdAtUtcMs: 创建时间索引
- idx_wide_countryId: 国家标识符索引
- idx_wide_sourceId: 数据源标识符索引
- idx_wide_author: 作者索引
- idx_wide_polarity: 情感极性索引
- idx_wide_keywordId: 关键词标识符索引
- idx_wide_countryId_createdAtUtcMs: 国家标识符和创建时间复合索引
- idx_wide_sourceId_createdAtUtcMs: 数据源标识符和创建时间复合索引
- idx_wide_keywordId_createdAtUtcMs: 关键词标识符和创建时间复合索引

