#!/usr/bin/env python3
"""
Evolution Scanner - 扫描GitHub发现新闻相关的新项目
搜索关键词、评估质量、对比现有源，输出新发现
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: requests not installed. Run: pip install requests")
    sys.exit(1)

# === 搜索关键词 ===
SEARCH_QUERIES = [
    # 新闻聚合
    "news aggregator RSS",
    "news aggregator Chinese",
    "news API free",
    "newsfeed API",
    "headline API",
    
    # 社交媒体
    "weibo API",
    "zhihu API",
    "douyin API",
    "xiaohongshu scraper",
    "twitter alternative API",
    "reddit API wrapper",
    
    # RSS/内容聚合
    "RSS feed generator",
    "RSS parser Python",
    "full text RSS",
    "RSSHub alternative",
    
    # 情感分析
    "sentiment analysis Chinese NLP",
    "Chinese text classification",
    "news sentiment analysis",
    "opinion mining Chinese",
    
    # 金融数据
    "stock market API free",
    "financial news API",
    "crypto news API",
    "forex API free",
    
    # AI/科技
    "AI news aggregator",
    "tech news API",
    "HackerNews API",
    "ProductHunt API",
    
    # 数据源
    "public API list",
    "free API collection",
    "open data news",
    
    # 新闻分析
    "news clustering",
    "topic detection news",
    "news summarization",
    "fake news detection",
]

# === 质量评估阈值 ===
QUALITY_THRESHOLDS = {
    "min_stars": 50,
    "min_recent_commits_days": 90,  # 90天内有提交
    "max_issues_ratio": 0.3,  # issue关闭率
}

# === 现有源（从SKILL.md提取）===
EXISTING_SOURCES = set()

def load_existing_sources():
    """从SKILL.md加载现有数据源"""
    skill_path = Path(__file__).parent.parent / "skills" / "omni-news" / "SKILL.md"
    if not skill_path.exists():
        return
    
    content = skill_path.read_text(encoding="utf-8")
    
    # 提取所有URL
    urls = re.findall(r'https?://[^\s\)\"\'>]+', content)
    for url in urls:
        # 提取域名作为源标识
        domain = re.sub(r'https?://(www\.)?', '', url).split('/')[0]
        EXISTING_SOURCES.add(domain.lower())
    
    # 提取所有项目名称 (from 致谢部分)
    projects = re.findall(r'\[([^\]]+)\]\(https?://github\.com/[^)]+\)', content)
    for p in projects:
        EXISTING_SOURCES.add(p.lower())


def search_github(query, sort="stars", order="desc", per_page=30):
    """搜索GitHub项目"""
    url = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": sort,
        "order": order,
        "per_page": per_page,
    }
    
    headers = {}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"
    
    try:
        resp = requests.get(url, params=params, headers=headers, timeout=15)
        if resp.status_code == 200:
            return resp.json().get("items", [])
        elif resp.status_code == 403:
            print(f"  ⚠️ API限流: {query}")
            return []
        else:
            print(f"  ❌ 搜索失败 ({resp.status_code}): {query}")
            return []
    except Exception as e:
        print(f"  ❌ 搜索异常: {e}")
        return []


def evaluate_project(project):
    """评估项目质量"""
    score = 0
    reasons = []
    
    stars = project.get("stargazers_count", 0)
    if stars >= 1000:
        score += 3
        reasons.append(f"⭐{stars}")
    elif stars >= 500:
        score += 2
        reasons.append(f"⭐{stars}")
    elif stars >= 100:
        score += 1
        reasons.append(f"⭐{stars}")
    elif stars >= QUALITY_THRESHOLDS["min_stars"]:
        score += 0.5
        reasons.append(f"⭐{stars}")
    else:
        return 0, []  # 太少star，跳过
    
    # 检查最近更新
    updated = project.get("updated_at", "")
    if updated:
        try:
            update_date = datetime.fromisoformat(updated.replace("Z", "+00:00"))
            days_ago = (datetime.now(update_date.tzinfo) - update_date).days
            if days_ago <= 30:
                score += 2
                reasons.append("🟢活跃")
            elif days_ago <= 90:
                score += 1
                reasons.append("🟡近期")
            elif days_ago <= 365:
                score += 0.5
                reasons.append("⚪一年")
            else:
                return 0, []  # 太久没更新
        except:
            pass
    
    # 检查是否有描述
    desc = project.get("description", "")
    if desc and len(desc) > 20:
        score += 0.5
        reasons.append("📝有描述")
    
    # 检查license
    if project.get("license"):
        score += 0.5
        reasons.append("📜有许可")
    
    # 检查topics
    topics = project.get("topics", [])
    if topics:
        score += 0.5
        reasons.append(f"🏷️{len(topics)}标签")
    
    return score, reasons


def is_new_source(project):
    """检查是否是新的数据源（不在现有源中）"""
    repo_name = project.get("full_name", "").lower()
    desc = (project.get("description") or "").lower()
    homepage = (project.get("homepage") or "").lower()
    
    # 检查是否已存在
    for source in EXISTING_SOURCES:
        if source in repo_name or source in desc or source in homepage:
            return False
    
    return True


def scan_all(mode="normal"):
    """执行全量扫描"""
    load_existing_sources()
    print(f"📊 已加载 {len(EXISTING_SOURCES)} 个现有源")
    
    # 根据模式确定搜索范围
    if mode == "quick":
        queries = SEARCH_QUERIES[:8]
    elif mode == "deep":
        queries = SEARCH_QUERIES
    else:
        queries = SEARCH_QUERIES[:15]
    
    print(f"🔍 搜索模式: {mode}, 查询数: {len(queries)}")
    
    all_projects = {}
    seen_repos = set()
    
    for i, query in enumerate(queries):
        print(f"\n[{i+1}/{len(queries)}] 搜索: {query}")
        projects = search_github(query)
        
        for proj in projects:
            repo_name = proj.get("full_name", "")
            if repo_name in seen_repos:
                continue
            seen_repos.add(repo_name)
            
            # 评估质量
            score, reasons = evaluate_project(proj)
            if score < 2:  # 最低质量分
                continue
            
            # 检查是否是新源
            if not is_new_source(proj):
                continue
            
            all_projects[repo_name] = {
                "name": repo_name,
                "description": proj.get("description", ""),
                "url": proj.get("html_url", ""),
                "stars": proj.get("stargazers_count", 0),
                "language": proj.get("language", ""),
                "topics": proj.get("topics", []),
                "updated_at": proj.get("updated_at", ""),
                "homepage": proj.get("homepage", ""),
                "score": score,
                "reasons": reasons,
                "query": query,
            }
        
        # 避免API限流
        time.sleep(1)
    
    # 按分数排序
    sorted_projects = sorted(
        all_projects.values(),
        key=lambda x: x["score"],
        reverse=True
    )
    
    return sorted_projects


def main():
    parser = argparse.ArgumentParser(description="Evolution Scanner")
    parser.add_argument("--mode", default="normal", choices=["quick", "normal", "deep"])
    parser.add_argument("--output", default="scan_results.json")
    parser.add_argument("--min-score", type=float, default=2.0)
    args = parser.parse_args()
    
    print("=" * 60)
    print("🧬 Omni News Evolution Scanner")
    print(f"📅 时间: {datetime.now().isoformat()}")
    print(f"🔧 模式: {args.mode}")
    print("=" * 60)
    
    projects = scan_all(args.mode)
    
    # 过滤低分项目
    projects = [p for p in projects if p["score"] >= args.min_score]
    
    # 生成摘要
    summary = f"扫描完成: 发现 {len(projects)} 个新项目"
    if projects:
        top = projects[0]
        summary += f" | 最佳: {top['name']} (⭐{top['stars']}, 评分{top['score']})"
    
    # 输出结果
    result = {
        "scan_time": datetime.now().isoformat(),
        "mode": args.mode,
        "total_scanned": len(projects),
        "summary": summary,
        "new_projects": projects[:20],  # 最多保留20个
        "search_queries_used": len(SEARCH_QUERIES[:15]),
    }
    
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"\n{'=' * 60}")
    print(f"✅ {summary}")
    print(f"📄 结果已保存: {args.output}")
    
    if projects:
        print(f"\n🏆 TOP 10 新项目:")
        for i, p in enumerate(projects[:10]):
            print(f"  {i+1}. {p['name']} ⭐{p['stars']} (评分:{p['score']})")
            if p['description']:
                print(f"     {p['description'][:80]}")


if __name__ == "__main__":
    main()
