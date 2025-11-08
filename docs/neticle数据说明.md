
## mentions_wide
### 结构
| 序号 | 字段名 | 类型 | 说明 |
| --- | --- | --- | --- |
| 1 | id | TEXT | 主键，唯一标识（关键字ID-提及ID） |
| 2 | author | NUMERIC | 作者 |
| 3 | countryId | NUMERIC | 国家 ID |
| 4 | countryName | NUMERIC | 国家显示名 |
| 5 | createdAtUtcMs | NUMERIC | 创建时间（UTC 毫秒） |
| 6 | discoveredAtUtcMs | NUMERIC | 发现时间（UTC 毫秒） |
| 7 | keywordId | NUMERIC | 关键词 ID |
| 8 | keyword_ianaLanguages | NUMERIC | 关键词语言数组 |
| 9 | keyword_ianaTimeZone | NUMERIC | 关键词时区 |
| 10 | keyword_label | NUMERIC | 关键词显示名 |
| 11 | polarity | NUMERIC | 情感倾向（-3~+3） |
| 12 | reach | NUMERIC | 覆盖度 |
| 13 | sourceId | NUMERIC | 来源 ID |
| 14 | sourceName | NUMERIC | 来源显示名 |
| 15 | sourceLabel | NUMERIC | 来源显示名（标签） |
| 16 | sumComments | NUMERIC | 评论数 |
| 17 | sumInteractions | NUMERIC | 互动总数 |
| 18 | sumLikes | NUMERIC | 点赞数 |
| 19 | sumShares | NUMERIC | 分享数 |
| 20 | textOriginal | NUMERIC | 原文 |
| 21 | title | NUMERIC | 标题/渠道标题 |
| 22 | aspectId | NUMERIC | 方面/主题 ID |
| 23 | attributeLabelIds | NUMERIC | 属性标签 ID 列表 |
| 24 | brandLabelIds | NUMERIC | 品牌标签 ID 列表 |
| 25 | cityId | NUMERIC | 城市 ID |
| 26 | cityLabel | NUMERIC | 城市显示名 |
| 27 | cityCountryId | NUMERIC | 城市所属国家 ID |
| 28 | contentLength | NUMERIC | 内容长度（字符数） |
| 29 | domain | NUMERIC | 域名 |
| 30 | emotionLabelIds | NUMERIC | 情感标签 ID 列表 |
| 31 | engagementRate | NUMERIC | 互动率 |
| 32 | facebookDetails | NUMERIC | Facebook 明细（JSON/聚合） |
| 33 | facebookDetails_angry | NUMERIC | Facebook angry 反应数 |
| 34 | facebookDetails_care | NUMERIC | Facebook care 反应数 |
| 35 | facebookDetails_comment | NUMERIC | Facebook 评论数 |
| 36 | facebookDetails_fan | NUMERIC | Facebook 粉丝数 |
| 37 | facebookDetails_haha | NUMERIC | Facebook haha 反应数 |
| 38 | facebookDetails_like | NUMERIC | Facebook 点赞数 |
| 39 | facebookDetails_love | NUMERIC | Facebook love 反应数 |
| 40 | facebookDetails_reply | NUMERIC | Facebook 回复数 |
| 41 | facebookDetails_sad | NUMERIC | Facebook sad 反应数 |
| 42 | facebookDetails_share | NUMERIC | Facebook 分享数 |
| 43 | facebookDetails_wow | NUMERIC | Facebook wow 反应数 |
| 44 | genderId | NUMERIC | 性别 ID |
| 45 | genderLabel | NUMERIC | 性别显示名 |
| 46 | genderName | NUMERIC | 性别内部名 |
| 47 | hash | NUMERIC | 内容哈希 |
| 48 | imageAttachments | NUMERIC | 图片附件列表 |
| 49 | importance | NUMERIC | 重要度 |
| 50 | instagramDetails | NUMERIC | Instagram 明细（JSON/聚合） |
| 51 | instagramDetails_comment | NUMERIC | Instagram 评论数 |
| 52 | instagramDetails_follower | NUMERIC | Instagram 粉丝数 |
| 53 | instagramDetails_like | NUMERIC | Instagram 点赞数 |
| 54 | instagramDetails_score | NUMERIC | Instagram 评分/得分 |
| 55 | instagramDetails_view | NUMERIC | Instagram 浏览数 |
| 56 | isMarked | NUMERIC | 是否人工标记 |
| 57 | languageId | NUMERIC | 语言 ID |
| 58 | languageLabel | NUMERIC | 语言显示名 |
| 59 | languageIsoCode2 | NUMERIC | 语言 ISO 代码 |
| 60 | latitude | NUMERIC | 纬度 |
| 61 | linkedinDetails | NUMERIC | LinkedIn 明细（JSON/聚合） |
| 62 | linkedinDetails_celebrate | NUMERIC | LinkedIn celebrate 反应数 |
| 63 | linkedinDetails_comment | NUMERIC | LinkedIn 评论数 |
| 64 | linkedinDetails_curious | NUMERIC | LinkedIn curious 反应数 |
| 65 | linkedinDetails_follower | NUMERIC | LinkedIn 粉丝数 |
| 66 | linkedinDetails_funny | NUMERIC | LinkedIn funny 反应数 |
| 67 | linkedinDetails_insightful | NUMERIC | LinkedIn insightful 反应数 |
| 68 | linkedinDetails_like | NUMERIC | LinkedIn 点赞数 |
| 69 | linkedinDetails_love | NUMERIC | LinkedIn love 反应数 |
| 70 | linkedinDetails_share | NUMERIC | LinkedIn 分享数 |
| 71 | linkedinDetails_support | NUMERIC | LinkedIn support 反应数 |
| 72 | linkedinDetails_view | NUMERIC | LinkedIn 浏览数 |
| 73 | locationLabelIds | NUMERIC | 地理标签 ID 列表 |
| 74 | longitude | NUMERIC | 经度 |
| 75 | note | NUMERIC | 备注 |
| 76 | organizationLabelIds | NUMERIC | 组织标签 ID 列表 |
| 77 | ownChannelId | NUMERIC | 自有渠道 ID |
| 78 | ownChannelType | NUMERIC | 自有渠道类型 |
| 79 | ownChannelKeywordId | NUMERIC | 自有渠道关键词 ID |
| 80 | ownChannelProfileId | NUMERIC | 自有渠道配置文件 ID |
| 81 | ownChannelClientId | NUMERIC | 自有渠道客户 ID |
| 82 | ownChannelCountryId | NUMERIC | 自有渠道国家 ID |
| 83 | personLabelIds | NUMERIC | 人物标签 ID 列表 |
| 84 | pinterestDetails | NUMERIC | Pinterest 明细（JSON/聚合） |
| 85 | pinterestDetails_comment | NUMERIC | Pinterest 评论数 |
| 86 | pinterestDetails_like | NUMERIC | Pinterest 点赞数 |
| 87 | regionId | NUMERIC | 区域 ID |
| 88 | regionLabel | NUMERIC | 区域显示名 |
| 89 | regionCountryId | NUMERIC | 区域所属国家 ID |
| 90 | relatedDiscussionUrl | NUMERIC | 相关讨论链接 |
| 91 | relatedUrl | NUMERIC | 相关链接 |
| 92 | relevantTextFormatted | NUMERIC | 相关片段（格式化） |
| 93 | relevantTextOriginal | NUMERIC | 相关片段（原文） |
| 94 | reviewDetails | NUMERIC | 评测明细（JSON/聚合） |
| 95 | subSourceId | NUMERIC | 子来源 ID |
| 96 | sumDislikes | NUMERIC | 不喜欢/踩数 |
| 97 | sumFollowers | NUMERIC | 粉丝总数 |
| 98 | sumReactions | NUMERIC | 反应总数 |
| 99 | textFormatted | NUMERIC | 原文（格式化） |
| 100 | threadId | NUMERIC | 线程 ID |
| 101 | threadMetrics | NUMERIC | 线程统计（JSON） |
| 102 | thumbnailUrl | NUMERIC | 缩略图链接 |
| 103 | tiktokDetails | NUMERIC | TikTok 明细（JSON/聚合） |
| 104 | tiktokDetails_follower | NUMERIC | TikTok 粉丝数 |
| 105 | tiktokDetails_like | NUMERIC | TikTok 点赞数 |
| 106 | tiktokDetails_share | NUMERIC | TikTok 分享数 |
| 107 | tiktokDetails_view | NUMERIC | TikTok 浏览数 |
| 108 | topicLabelIds | NUMERIC | 主题标签 ID 列表 |
| 109 | translatedTextFormatted | NUMERIC | 译文（格式化） |
| 110 | translatedTitle | NUMERIC | 标题译文 |
| 111 | twitterDetails | NUMERIC | X/Twitter 明细（JSON/聚合） |
| 112 | twitterDetails_comment | NUMERIC | X/Twitter 评论数 |
| 113 | twitterDetails_follower | NUMERIC | X/Twitter 粉丝数 |
| 114 | twitterDetails_like | NUMERIC | X/Twitter 点赞数 |
| 115 | twitterDetails_quote | NUMERIC | X/Twitter 引用数 |
| 116 | twitterDetails_reply | NUMERIC | X/Twitter 回复数 |
| 117 | twitterDetails_retweet | NUMERIC | X/Twitter 转推数 |
| 118 | url | NUMERIC | 原文链接 |
| 119 | urlAttachments | NUMERIC | 链接附件列表 |
| 120 | videoAttachments | NUMERIC | 视频附件列表 |
| 121 | youtubeDetails | NUMERIC | YouTube 明细（JSON/聚合） |
| 122 | youtubeDetails_comment | NUMERIC | YouTube 评论数 |
| 123 | youtubeDetails_dislike | NUMERIC | YouTube 踩数 |
| 124 | youtubeDetails_like | NUMERIC | YouTube 点赞数 |
| 125 | youtubeDetails_subscribe | NUMERIC | YouTube 订阅数 |
| 126 | youtubeDetails_view | NUMERIC | YouTube 浏览数 |
| 127 | sourceCode | NUMERIC | 来源代码（枚举） |
| 128 | parentSourceId | NUMERIC | 上级来源 ID |
| 129 | parentSourceCode | NUMERIC | 上级来源代码 |
| 130 | sourceIsGroup | NUMERIC | 是否为分组来源 |
| 131 | sourceIsEnabled | NUMERIC | 来源是否启用 |
| 132 | sourceOrder | NUMERIC | 来源显示顺序 |
| 133 | sourceColor | NUMERIC | 来源颜色 |
| 134 | sourceCountryId | NUMERIC | 来源国家 ID |
| 135 | subSourceName | NUMERIC | 子来源内部名 |
| 136 | subSourceLabel | NUMERIC | 子来源显示名 |
| 137 | subSourceCode | NUMERIC | 子来源代码 |
| 138 | subSourceIsGroup | NUMERIC | 子来源是否分组 |
| 139 | subSourceParentSourceId | NUMERIC | 子来源上级来源 ID |
| 140 | subSourceParentSourceCode | NUMERIC | 子来源上级来源代码 |
| 141 | subSourceCountryId | NUMERIC | 子来源国家 ID |
| 142 | countryLabel | NUMERIC | 国家显示名（字典） |
| 143 | countryIsoCode2 | NUMERIC | 国家 ISO 代码 |
| 144 | countryNeticleCode | NUMERIC | 国家内部代号 |
| 145 | countryIanaTimeZone | NUMERIC | 国家时区 |
| 146 | countryIanaLanguages | NUMERIC | 国家语言数组 |
| 147 | languageNeticleCode | NUMERIC | 语言内部代号 |
| 148 | cityRegionId | NUMERIC | 城市所属区域 ID |
| 149 | cityRegionLabel | NUMERIC | 城市所属区域显示名 |
| 150 | aspectLabel | NUMERIC | 方面/主题显示名 |
| 151 | aspectGroupId | NUMERIC | 方面所属分组 ID |
| 152 | ownChannelLabel | NUMERIC | 自有渠道显示名 |
| 153 | ownChannelName | NUMERIC | 自有渠道内部名 |
| 154 | attributeLabelNames | NUMERIC | 属性标签名称列表 |
| 155 | brandLabelNames | NUMERIC | 品牌标签名称列表 |
| 156 | emotionLabelNames | NUMERIC | 情感标签名称列表 |
| 157 | locationLabelNames | NUMERIC | 地理标签名称列表 |
| 158 | organizationLabelNames | NUMERIC | 组织标签名称列表 |
| 159 | personLabelNames | NUMERIC | 人物标签名称列表 |
| 160 | topicLabelNames | NUMERIC | 主题标签名称列表 |
| 161 | attributeLabelCount | NUMERIC | 属性标签计数 |
| 162 | brandLabelCount | NUMERIC | 品牌标签计数 |
| 163 | emotionLabelCount | NUMERIC | 情感标签计数 |
| 164 | locationLabelCount | NUMERIC | 地理标签计数 |
| 165 | organizationLabelCount | NUMERIC | 组织标签计数 |
| 166 | personLabelCount | NUMERIC | 人物标签计数 |
| 167 | topicLabelCount | NUMERIC | 主题标签计数 |
