<div align="center">

# 📰 Omni News

**多平台全方位新闻信息平台**

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/zain1299999-create/omni-news/releases/tag/v1.0.0)
[![Auto Evolve](https://img.shields.io/badge/auto--evolve-enabled-success.svg)](.github/workflows/evolve.yml)
[![Health Check](https://img.shields.io/badge/health--check-daily-brightgreen.svg)](.github/workflows/evolve.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Sources](https://img.shields.io/badge/sources-82-brightgreen.svg)](docs/SOURCES.md)
[![Platforms](https://img.shields.io/badge/platforms-23-orange.svg)](docs/SOURCES.md)
[![Engines](https://img.shields.io/badge/engines-10-red.svg)](docs/ARCHITECTURE.md)

*聚合82个免费源 · 10层采集引擎 · 情感分析层 · 社交媒体18平台全覆盖*

[English](README.md) · [中文](README.md)

</div>

---

## ✨ 特色

- **十层采集引擎**: 新闻联播直采 + 国内权威媒体 + 社交媒体 + 国际财经 + 国际RSS + AI/Builder + 搜索引擎 + 60s API + DailyHotApi + TrendRadar
- **情感分析层**: SnowNLP + PaddleNLP + BettaFish 方法论
- **82个免费源**: 零API Key依赖，覆盖23个社交平台
- **🧬 自动进化**: 基于GitHub Actions的定时扫描引擎，每天自动发现新技术和新数据源
- **多格式输出**: Markdown / HTML / 图片 / PDF / RSS
- **智能去重**: 4阶段流水线（精确→语义→AI核验→事件聚类）
- **场景化早报**: 财经/科技/吃瓜/AI/国际/联播/Builder/舆情 8套模板

---

## 🚀 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/zain1299999-create/omni-news.git
cd omni-news

# 安装依赖（可选，用于情感分析）
pip install snownlp paddlenlp sentence-transformers
```

### 使用

作为 QwenPaw 技能使用：

```bash
# 将技能复制到 QwenPaw 工作区
cp -r skills/omni-news ~/.qwenpaw/workspaces/default/skills/
cp -r scripts ~/.qwenpaw/workspaces/default/skills/omni-news/

# 重启 QwenPaw 后即可通过关键词触发
# 触发词: 新闻、日报、早报、快讯、头条、联播、财经、AI动态、舆情
```

### 命令行使用

```bash
# 采集新闻联播
python scripts/fetch_xwlb.py

# 生成日报（全部引擎）
# 在 QwenPaw 中输入: "今天有什么新闻"
```

---

## 📊 引擎架构

```
┌────────────────────────────────────────────────────────────┐
│                      用户请求                               │
└──────────────────────────┬─────────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────────┐
│  引擎1: 新闻联播直采 (tv.cctv.com)                          │
│  引擎2: 国内权威媒体 (新浪/人民网/澎湃/36kr/IT之家等)        │
│  引擎3: 社交媒体热点 (微博/知乎/雪球 via Hotspot API)       │
│  引擎4: 国际财经 (WallstreetCN + Yahoo Finance + The Hear)  │
│  引擎5: 国际新闻RSS (BBC/Reuters/Guardian/TechCrunch等21源) │
│  引擎6: AI/Builder动态 (Follow Builders + InBrief)          │
│  引擎7: 搜索引擎交叉 (bocha + baidu)                       │
│  引擎8: 60s API (微博/知乎/抖音/B站/头条/猫眼)              │
│  引擎9: DailyHotApi (40+平台聚合)                          │
│  引擎10: TrendRadar (11平台监控+推送)                      │
│  情感层: 中文情感分析 (BERT+多模型)                        │
└──────────────────────────┬─────────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────────┐
│  处理层: 去重→信源分级→可信度标注→情感分析→影响分析       │
└──────────────────────────┬─────────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────────┐
│  输出层: 结构化Markdown报告 + 存档 + 趋势图表              │
└────────────────────────────────────────────────────────────┘
```

---

## 🧬 自动进化系统

> 新闻平台不是静态的——它会自动寻找新技术并进化。

### 工作原理

```
每天 UTC 02:00 (北京时间 10:00)
        │
        ▼
┌──────────────────────┐
│  🔍 扫描GitHub       │  搜索25+关键词（新闻聚合/RSS/情感分析/金融数据/社交媒体）
│  发现新项目          │  质量评估: Stars + 活跃度 + 文档 + License
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  💓 健康检查         │  验证现有82个数据源的可用性
│  现有源状态          │  检测降级/失效的端点
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  📝 自动创建Issue    │  新发现的项目自动记录到GitHub Issues
│  追踪新发现          │  包含项目描述、评分、可用性评估
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  🔄 可选自动PR       │  高评分项目可自动创建PR更新SKILL.md
│  更新采集引擎        │  人工审核后合并
└──────────────────────┘
```

### 参与方式

1. **自动**: 每天10:00自动运行，查看 [Issues](https://github.com/zain1299999-create/omni-news/issues) 了解新发现
2. **手动**: Actions → Auto Evolve → Run workflow
3. **审核**: 测试新源可用性 → 合并PR → 关闭Issue

### 进化日志

查看 [EVOLUTION_LOG.md](EVOLUTION_LOG.md) 了解历次扫描发现。

---

## 📁 项目结构

```
omni-news/
├── 📄 README.md               # 项目说明
├── 📄 LICENSE                 # MIT 许可证
├── 📄 CHANGELOG.md            # 版本变更记录
├── 📄 .gitignore              # Git 忽略规则
│
├── 📁 skills/                 # QwenPaw 技能
│   └── 📁 omni-news/
│       └── 📄 SKILL.md        # 核心技能文件 (1296行)
│
├── 📁 scripts/                # 脚本
│   └── 📄 fetch_xwlb.py       # 新闻联播直采脚本
│
├── 📁 docs/                   # 文档
│   ├── 📄 ARCHITECTURE.md     # 架构详解
│   └── 📄 SOURCES.md          # 数据源清单
│
└── 📁 examples/               # 示例输出
    └── 📄 daily_news_2026-09-17.md  # 样例日报
```

---

## 🌐 数据源覆盖

### 社交媒体 / 热榜（23个平台）

| 平台 | 状态 | 来源 |
|------|------|------|
| 微博 | ✅ | Hotspot API + 60s API |
| 知乎 | ✅ | Hotspot API + 60s API |
| 抖音 | ✅ | 60s API |
| B站 | ✅ | 60s API |
| 今日头条 | ✅ | 60s API |
| 猫眼票房 | ✅ | 60s API |
| 小红书 | ⚠️ | 间接覆盖 |
| 快手 | ⚠️ | DailyHotApi |
| 贴吧/虎扑/懂车帝 | ⚠️ | DailyHotApi |
| X/Twitter | ⚠️ | 间接覆盖 |

### 国内新闻（15个源）
CCTV新闻联播 · 人民网 · 中国新闻网 · 新浪新闻 · 新浪财经7×24 · 财联社 · AIHOT · 澎湃新闻 · 36氪 · IT之家 · 量子位 · 机器之心 · 新华网RSS · 央视RSS · 腾讯新闻

### 国际新闻（21个源）
BBC · Reuters · AP · Guardian · Al Jazeera · NPR · DW · 南华早报 · TechCrunch · The Verge · New Atlas · WallstreetCN · Yahoo Finance · The Hear(20国) · NewsMCP · OpenAI · Anthropic · Microsoft · NVIDIA · HackerNews · ProductHunt

### AI/Builder（15个信源）
Follow Builders(26人) · Follow Builders(6播客) · Anthropic Engineering · Claude Blog · InBrief.info(100源) · AI News Digest(60+源) · GitHub Trending

---

## 📈 采集统计

| 指标 | 数值 |
|------|------|
| 总数据源 | **82** |
| 采集引擎 | **10** |
| 社交平台 | **23** |
| 实测可用端点 | **45岁以上** |
| 采集成功率 | **75%** |
| 情感分析模型 | **3** |
| 输出格式 | **5** |

---

## 🔧 配置

### 环境变量（可选）

```bash
# 60s API 自部署（公共实例有限额）
export SIXTYS_API_URL="http://localhost:4399"

# DailyHotApi 自部署
export DAILYHOT_API_URL="http://localhost:6688"

# 情感分析模型选择
export SENTIMENT_MODEL="snownlp"  # snownlp | paddlenlp | bettafish
```

### Cron 定时运行

```bash
# 早报 08:30
# 午报 12:00
# 晚报 20:30（新闻联播上线后）
# 舆情 10:00 / 16:00
```

---

## 🤝 贡献

欢迎贡献！请查看 [ARCHITECTURE.md](docs/ARCHITECTURE.md) 了解架构设计。

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送分支 (`git push origin feature/amazing-feature`)
5. 开启 Pull Request

---

## 📜 版本历史

- **v1.0.0** (2026-09-17): 初始版本
  - 10层采集引擎 + 情感分析层
  - 82个免费源，23个社交平台
  - 多格式输出（Markdown/HTML/图片/PDF/RSS）
  - 场景化早报（8套模板）
  - 智能去重与事件聚类

详见 [CHANGELOG.md](CHANGELOG.md)

---

## 📄 许可证

[MIT](LICENSE) © 2026 Zain

---

## 🙏 致谢

感谢以下开源项目提供的方法论和灵感：

- [60s API](https://github.com/vikiboss/60s) - 零Key实时热搜
- [DailyHotApi](https://github.com/imsyy/DailyHotApi) - 40+平台聚合
- [TrendRadar](https://github.com/sansan0/TrendRadar) - 智能监控推送
- [BettaFish](https://github.com/666ghj/BettaFish) - 多Agent舆情分析
- [TrendSonar](https://github.com/aicezam/trendsonar) - 新闻聚合平台
- [NewsMCP](https://newsmcp.io) - 事件聚合API
- [Follow Builders](https://github.com/zarazhangrui/follow-builders) - AI Builder追踪
- [InBrief.info](https://github.com/frankzch/ai-news-skill) - AI新闻聚合
- [AI News Digest](https://github.com/chengjialu8888/AI_News_Digest) - AI新闻摘要

---

<div align="center">

⭐ **如果这个项目对你有帮助，请给个 Star!** ⭐

[报告 Bug](https://github.com/zain1299999-create/omni-news/issues) · [功能请求](https://github.com/zain1299999-create/omni-news/issues) · [讨论](https://github.com/zain1299999-create/omni-news/discussions)

</div>
