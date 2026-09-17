# Data Sources

> Omni News v1.0.0 — 完整数据源清单 (82个源)

---

## 📊 总览

| 类别 | 数量 | 状态 |
|------|------|------|
| 社交媒体/热榜 | 23 | 9✅ 11⚠️ 3❌ |
| 国内权威新闻 | 15 | 15✅ |
| 国际新闻源 | 21 | 19✅ 2⚠️ |
| AI/Builder | 15 | 15✅ |
| 实用工具 | 8 | 6✅ 2⚠️ |
| **总计** | **82** | **64✅ / 15⚠️ / 3❌** |

**图例**: ✅ 实测可用 | ⚠️ 文档声明/待验证 | ❌ 间接覆盖

---

## 🔥 社交媒体 / 热榜 (23个平台)

| # | 平台 | 状态 | 来源 | 说明 |
|---|------|------|------|------|
| 1 | **微博** | ✅ | Hotspot API + 60s API + DailyHotApi | 实时热搜 |
| 2 | **知乎** | ✅ | Hotspot API + 60s API + DailyHotApi | 话题榜 |
| 3 | **腾讯早报** | ✅ | Hotspot API | 每日早报 |
| 4 | **雪球** | ✅ | web_fetch | 个股讨论 |
| 5 | **HackerNews** | ✅ | Firebase API | 技术热帖 |
| 6 | **ProductHunt** | ✅ | RSS | 产品发布 |
| 7 | **抖音** | ✅ | 60s API(实测50条) | 实时热点 |
| 8 | **B站** | ✅ | 60s API(实测50条) | 热门视频 |
| 9 | **今日头条** | ✅ | 60s API(实测50条) | 热搜榜 |
| 10 | **猫眼票房** | ✅ | 60s API(实测) | 电影票房 |
| 11 | **百度热搜** | ⚠️ | DailyHotApi + 60s API | 实时热搜 |
| 12 | **小红书** | ⚠️ | 间接覆盖 | 60s API公共实例404 |
| 13 | **快手** | ⚠️ | DailyHotApi | 短视频热点 |
| 14 | **贴吧** | ⚠️ | DailyHotApi | 论坛话题 |
| 15 | **虎扑** | ⚠️ | DailyHotApi | 体育社区 |
| 16 | **懂车帝** | ⚠️ | 60s API | 汽车资讯 |
| 17 | **IT之家** | ⚠️ | DailyHotApi | 科技资讯 |
| 18 | **豆瓣** | ⚠️ | 60s API + DailyHotApi | 影视/书评 |
| 19 | **地震速报** | ⚠️ | DailyHotApi | 中国地震台 |
| 20 | **气象预警** | ⚠️ | DailyHotApi | 中央气象台 |
| 21 | **X/Twitter** | ⚠️ | web_search + Follow Builders | 间接覆盖 |
| 22 | **YouTube** | ⚠️ | Follow Builders + web_search | 间接覆盖 |
| 23 | **Reddit** | ⚠️ | InBrief + web_search | 间接覆盖 |

---

## 🇨🇳 国内权威新闻 (15个源)

| # | 源 | 方式 | 类别 |
|---|-----|------|------|
| 1 | CCTV 新闻联播 | Python脚本 | 综合官方 |
| 2 | 人民网 | web_fetch | 综合官方 |
| 3 | 中国新闻网 | web_fetch | 综合官方 |
| 4 | 新浪新闻 | web_fetch | 综合门户 |
| 5 | 新浪财经 7×24 | web_fetch | 财经 |
| 6 | 财联社电报 | browser | 财经 |
| 7 | AIHOT | web_fetch | AI聚合 |
| 8 | 澎湃新闻 | web_fetch | 深度报道 |
| 9 | 36氪 | RSS + 首页 | 科技创投 |
| 10 | IT之家 | web_fetch | 科技 |
| 11 | 量子位 | web_fetch | AI |
| 12 | 机器之心 | web_fetch | AI |
| 13 | 新华网 | RSS | 综合 |
| 14 | 央视 | RSS | 综合 |
| 15 | 腾讯新闻 | DailyHotApi | 门户 |

---

## 🌍 国际新闻源 (21个)

| # | 源 | 方式 | 类别 |
|---|-----|------|------|
| 1 | BBC | RSS | 综合 |
| 2 | Reuters | RSS | 综合 |
| 3 | AP | RSS | 综合 |
| 4 | The Guardian | RSS | 综合 |
| 5 | Al Jazeera | RSS | 综合 |
| 6 | NPR | RSS | 综合 |
| 7 | DW | RSS | 综合 |
| 8 | 南华早报 | RSS | 亚洲 |
| 9 | TechCrunch | RSS | 科技 |
| 10 | The Verge | RSS | 科技 |
| 11 | New Atlas | RSS | 科技 |
| 12 | WallstreetCN | API | 财经 |
| 13 | Yahoo Finance | API | 财经 |
| 14 | The Hear | API | 20国头条 |
| 15 | NewsMCP | API | ⚠️ 已关闭 |
| 16 | OpenAI Blog | web_fetch | AI |
| 17 | Anthropic News | web_fetch | AI |
| 18 | Microsoft Source | RSS | 科技 |
| 19 | NVIDIA Blog | RSS | AI/芯片 |
| 20 | 华尔街见闻 | TrendRadar | 财经 |
| 21 | 凤凰网 | TrendRadar | 门户 |

---

## 🤖 AI / Builder 动态 (15个信源)

| # | 源 | 方式 | 说明 |
|---|-----|------|------|
| 1-26 | Follow Builders | GitHub | 26位AI Builder |
| 27-32 | Follow Builders | GitHub | 6个YouTube播客 |
| 33 | Anthropic Engineering | 博客 | 技术博客 |
| 34 | Claude Blog | 博客 | 产品更新 |
| 35 | InBrief.info | API | 100 AI信源 |
| 36 | AI News Digest | GitHub | 60+信源 |
| 37 | GitHub Trending | web_fetch | AI仓库 |
| 38 | OpenAI | 官方 | 模型/产品 |
| 39 | Anthropic | 官方 | 模型/产品 |
| 40 | Microsoft | 官方 | Azure/AI |
| 41 | NVIDIA | 官方 | GPU/AI |

---

## 🛠️ 实用工具 (8个)

| # | 工具 | 用途 | 状态 |
|---|------|------|------|
| 1 | SnowNLP | 中文情感分析 | ✅ |
| 2 | PaddleNLP | 预训练情感模型 | ✅ |
| 3 | BettaFish | 多Agent舆情方法论 | ✅ |
| 4 | 天气查询 | 实时天气+预报 | ✅ |
| 5 | 汇率查询 | 货币汇率 | ✅ |
| 6 | 历史上的今天 | 每日历史 | ⚠️ |
| 7 | Epic免费游戏 | 每周免费 | ✅ |
| 8 | 翻译 | 109种语言 | ✅ |

---

## API 端点详情

### 60s API (60s.viki.moe)

| 端点 | 说明 | 状态 |
|------|------|------|
| `/v2/weibo` | 微博热搜 | ✅ 实测可用 |
| `/v2/zhihu` | 知乎话题 | ✅ 实测可用(30条) |
| `/v2/douyin` | 抖音热点 | ✅ 实测可用(50条) |
| `/v2/bilibili` | B站热门 | ✅ 实测可用(50条) |
| `/v2/toutiao` | 头条热搜 | ✅ 实测可用(50条) |
| `/v2/maoyan` | 猫眼票房 | ✅ 实测可用 |
| `/v2/60s` | 每天60秒读世界 | ✅ 实测可用(15条) |
| `/v2/xiaohongshu` | 小红书 | ❌ 404 |
| `/v2/baidu` | 百度 | ❌ null |
| `/v2/ithome` | IT之家 | ❌ 404 |

### WallstreetCN API

| 端点 | 说明 |
|------|------|
| `/apiv1/content/information-flow` | 最新信息流 |
| `/apiv1/content/carousel/information-flow` | 头条信息流 |
| `/apiv1/content/articles/hot` | 热文 |
| `/apiv1/search/article` | 搜索 |

### The Hear API

| 端点 | 说明 |
|------|------|
| `/api/country-view/{country}` | 国家头条 |
| `/api/country-view/{country}?at=...` | 历史快照 |

### NewsMCP API (已关闭)

| 端点 | 说明 |
|------|------|
| `/v1/news/?topics=...&hours=24` | 新闻聚合 |
| `/v1/news/{event_id}/` | 事件详情 |

---

## 自部署服务

| 服务 | Docker命令 | 端口 |
|------|-----------|------|
| 60s API | `docker run -d --restart always --name 60s -p 4399:4399 vikiboss/60s:latest` | 4399 |
| DailyHotApi | `docker pull imsyy/dailyhot-api:latest && docker run --restart always -p 6688:6688 -d imsyy/dailyhot-api` | 6688 |
| TrendSonar | `docker-compose up -d` | 8000 |

---

## 方法论来源

| 项目 | Stars | 提取内容 |
|------|-------|---------|
| vikiboss/60s | 5.8k | 零Key设计+CDN加速 |
| imsyy/DailyHotApi | 4.1k | 40+平台聚合+双模式 |
| 666ghj/BettaFish | 42.2k | 多Agent协作+情感微调 |
| aicezam/trendsonar | - | 去重流水线+多模型路由 |
| cclank/news-aggregator-skill | - | 杂志排版+Deep Fetch |
| dukeblue1994-glitch/chronicle | - | MinHash LSH + HDBSCAN |

---

## 付费源（已排除但记录）

| 源 | 费用 | 替代方案 |
|----|------|---------|
| X 官方 API | $200/月起 | twikit + web_search |
| tianapi | 天聚数行API Key | web_search |
| google-news-api | 50次免费后$25/2500次 | NewsMCP + The Hear |
| jisu-news | 聚数付费 | web_search |
| ifind-finance-data | iFind付费 | WallstreetCN |
| caixin-news | 财新付费墙 | web_search |

---

## 数据质量评分

| 维度 | 评分 | 说明 |
|------|------|------|
| 时效性 | ⭐⭐⭐⭐ | 大部分源实时更新 |
| 覆盖面 | ⭐⭐⭐⭐⭐ | 82源覆盖23平台 |
| 准确性 | ⭐⭐⭐⭐ | 多源交叉验证 |
| 结构化 | ⭐⭐⭐ | 部分源为HTML需解析 |
| 稳定性 | ⭐⭐⭐ | 公共API偶尔不可用 |
| 成本 | ⭐⭐⭐⭐⭐ | 完全免费 |
