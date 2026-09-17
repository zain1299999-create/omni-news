# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-09-17

### Added
- **十层采集引擎**: 新闻联播直采 + 国内权威媒体 + 社交媒体 + 国际财经 + 国际RSS + AI/Builder + 搜索引擎 + 60s API + DailyHotApi + TrendRadar
- **情感分析层**: SnowNLP + PaddleNLP + BettaFish 方法论
- **82个免费源**: 零API Key依赖，覆盖23个社交平台
- **多格式输出**: Markdown / HTML / 图片 / PDF / RSS
- **智能去重**: 4阶段流水线（精确→语义→AI核验→事件聚类）
- **场景化早报**: 财经/科技/吃瓜/AI/国际/联播/Builder/舆情 8套模板
- **事件聚合展示**: 多源对比表 + 情感分布 + 趋势 + 时间轴
- **个性化关键词追踪**: 精确匹配 + 语义匹配 + 权重调整
- **Deep Fetch 深度穿透**: Playwright绕过Cloudflare + LLM防降智过滤
- **多模型路由策略**: 按任务复杂度分配主/备模型
- **信源健康监控**: 成功率/响应时间/内容质量三维评分
- **杂志级排版原则**: 7条视觉规则 + emoji锚点 + 可信度分级

### 引擎详情
- **引擎1**: 新闻联播直采 (tv.cctv.com, Python脚本)
- **引擎2**: 国内权威媒体 (新浪/人民网/澎湃/36kr/IT之家等14源)
- **引擎3**: 社交媒体热点 (微博/知乎/雪球 via Hotspot API)
- **引擎4**: 国际财经 (WallstreetCN + Yahoo Finance + The Hear 20国)
- **引擎5**: 国际新闻RSS (BBC/Reuters/Guardian/TechCrunch等21源)
- **引擎6**: AI/Builder动态 (Follow Builders 26人 + InBrief 100源)
- **引擎7**: 搜索引擎交叉验证 (bocha + baidu 双引擎)
- **引擎8**: 60s API (微博/知乎/抖音/B站/头条/猫眼/豆瓣/IT之家/贴吧/懂车帝/快手)
- **引擎9**: DailyHotApi (40+平台JSON+RSS双模式)
- **引擎10**: TrendRadar (11平台智能监控+关键词过滤+多渠道推送)

### 社交媒体覆盖（23个平台）
- ✅ 直接覆盖: 微博/知乎/抖音/B站/今日头条/猫眼票房/雪球/HackerNews/ProductHunt
- ⚠️ 文档可用: 小红书/快手/贴吧/虎扑/懂车帝/IT之家/豆瓣/地震速报/气象预警
- ⚠️ 间接覆盖: X/Twitter/YouTube/Reddit

### 方法论来源
- TrendSonar: 多阶段去重+专题追踪+流式报告+智能体问答
- cclank/news-aggregator-skill: 杂志排版+场景化模板+OPML订阅+Deep Fetch
- chronicle: MinHash LSH + HDBSCAN + 时间线生成
- BettaFish: 多Agent协作+论坛辩论+情感微调
- 60s API: 零Key设计+CDN加速+多运行时
- DailyHotApi: 40+平台聚合+JSON+RSS双模式
- NewsMCP: 事件聚类+影响评分+12话题×30地区
- Follow Builders: 中央Feed模式+Remix摘要
- AI News Digest: 5道QA Gate+9层信源系统

### 文件结构
- `skills/omni-news/SKILL.md` — 核心技能文件 (1296行)
- `scripts/fetch_xwlb.py` — 新闻联播直采脚本
- `docs/ARCHITECTURE.md` — 架构详解
- `docs/SOURCES.md` — 数据源清单
- `examples/daily_news_2026-09-17.md` — 样例日报

---

## [Unreleased]

### Planned
- 自动 Cron 定时运行
- Web UI 仪表盘
- 邮件/Slack/Telegram 推送
- 更多国际源（日本/韩国/东南亚）
- 视频新闻聚合（YouTube/B站/抖音）
- 实时 WebSocket 推送
