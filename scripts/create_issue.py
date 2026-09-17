#!/usr/bin/env python3
"""
Create Issue - 根据扫描结果创建GitHub Issue
"""

import json
import os
import sys
from datetime import datetime


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def format_project_issue(project, index):
    """格式化单个项目为Issue段落"""
    lines = []
    lines.append(f"### {index}. [{project['name']}]({project['url']}) ⭐{project['stars']}")
    
    if project.get("description"):
        lines.append(f"> {project['description']}")
    
    lines.append(f"- **评分**: {project['score']}")
    lines.append(f"- **语言**: {project.get('language', 'N/A')}")
    lines.append(f"- **标签**: {', '.join(project.get('topics', []))}")
    lines.append(f"- **质量标记**: {', '.join(project.get('reasons', []))}")
    lines.append(f"- **发现方式**: 搜索 `{project.get('query', 'N/A')}`")
    
    if project.get("homepage"):
        lines.append(f"- **官网**: {project['homepage']}")
    
    lines.append(f"- [ ] 评估是否纳入")
    lines.append(f"- [ ] 检查是否需要API Key")
    lines.append(f"- [ ] 测试端点可用性")
    
    return "\n".join(lines)


def create_issue_body(scan_results, health_results=None):
    """创建Issue正文"""
    projects = scan_results.get("new_projects", [])
    
    lines = []
    lines.append(f"# 🧬 自动进化报告 - {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")
    lines.append("## 📊 扫描摘要")
    lines.append("")
    lines.append(f"- **扫描模式**: {scan_results.get('mode', 'normal')}")
    lines.append(f"- **搜索查询数**: {scan_results.get('search_queries_used', 0)}")
    lines.append(f"- **发现新项目**: {len(projects)}")
    lines.append(f"- **扫描时间**: {scan_results.get('scan_time', 'N/A')}")
    lines.append("")
    
    # 健康检查结果
    if health_results:
        lines.append("## 💓 数据源健康")
        lines.append("")
        lines.append(f"- **健康率**: {health_results.get('healthy_pct', 0)}%")
        lines.append(f"- **健康端点**: {health_results.get('healthy_count', 0)}/{health_results.get('total_endpoints', 0)}")
        
        unhealthy = health_results.get("unhealthy", [])
        if unhealthy:
            lines.append(f"- **不健康端点**: {len(unhealthy)}")
            for u in unhealthy:
                lines.append(f"  - ❌ {u['name']}: {u.get('error', u['status'])}")
        lines.append("")
    
    # 新项目详情
    if projects:
        lines.append(f"## 🆕 发现 {len(projects)} 个新项目")
        lines.append("")
        lines.append("---")
        
        for i, p in enumerate(projects, 1):
            lines.append(format_project_issue(p, i))
            lines.append("")
            lines.append("---")
    else:
        lines.append("## ✅ 未发现新项目")
        lines.append("")
        lines.append("本次扫描未发现符合质量阈值的新数据源。")
    
    lines.append("")
    lines.append("## 🤖 下一步")
    lines.append("")
    lines.append("1. 审核上述新项目")
    lines.append("2. 测试可用性")
    lines.append("3. 更新 SKILL.md")
    lines.append("4. 关闭此 Issue")
    lines.append("")
    lines.append("---")
    lines.append("*此 Issue 由 GitHub Actions 自动创建*")
    
    return "\n".join(lines)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan-results", required=True)
    parser.add_argument("--health-results", default=None)
    parser.add_argument("--issue-title", default=None)
    args = parser.parse_args()
    
    scan_results = load_json(args.scan_results)
    health_results = load_json(args.health_results) if args.health_results else None
    
    body = create_issue_body(scan_results, health_results)
    
    # 输出到文件（GitHub Actions 会读取并创建Issue）
    with open("issue_body.md", "w", encoding="utf-8") as f:
        f.write(body)
    
    title = args.issue_title or f"🧬 自动进化报告 - {datetime.now().strftime('%Y-%m-%d')}"
    
    print(f"📝 Issue 标题: {title}")
    print(f"📄 Issue 正文: {len(body)} 字符")
    print(f"📊 新项目数: {len(scan_results.get('new_projects', []))}")
    
    # 输出供后续步骤使用
    with open(os.environ.get("GITHUB_ENV", "/dev/null"), "a") as f:
        f.write(f"ISSUE_TITLE={title}\n")


if __name__ == "__main__":
    main()
