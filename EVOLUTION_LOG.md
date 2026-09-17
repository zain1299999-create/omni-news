# 🧬 进化日志

> 自动记录每次扫描发现的新技术和项目。

此日志由 GitHub Actions 自动更新。每天 UTC 02:00 扫描 GitHub 寻找新闻相关的新项目。

---

## 如何参与自动进化

### 自动触发（推荐）
仓库已配置 GitHub Actions 定时工作流，每天自动：
1. 扫描 GitHub 发现新项目
2. 检查现有数据源健康状态
3. 创建 Issue 追踪新发现
4. 更新进化日志

### 手动触发
1. 进入 Actions → Auto Evolve → Run workflow
2. 选择搜索深度: quick/normal/deep
3. 可选勾选"自动创建PR"

### 审核流程
1. Issue 被创建后，审核新项目
2. 测试可用性
3. 合并 PR 更新 SKILL.md
4. 关闭 Issue
