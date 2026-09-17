#!/usr/bin/env python3
"""
Auto Update - 根据扫描结果自动更新SKILL.md
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def update_skill_md(scan_results, skill_path):
    """更新SKILL.md添加新源"""
    if not Path(skill_path).exists():
        print(f"❌ SKILL.md not found: {skill_path}")
        return False
    
    content = Path(skill_path).read_text(encoding="utf-8")
    projects = scan_results.get("new_projects", [])
    
    if not projects:
        print("ℹ️ No new projects to add")
        return False
    
    # 只添加评分最高的前5个
    top_projects = [p for p in projects if p["score"] >= 3][:5]
    
    if not top_projects:
        print("ℹ️ No projects meet the quality threshold")
        return False
    
    # 在文档末尾添加新发现
    new_section = "\n\n---\n\n## 🧬 自动进化发现 ({})\n\n".format(datetime.now().strftime('%Y-%m-%d'))
    new_section += "以下项目由自动进化扫描发现，经人工审核后可纳入采集引擎。\n\n"
    
    for p in top_projects:
        new_section += f"### {p['name']}\n"
        if p.get("description"):
            new_section += f"{p['description']}\n\n"
        new_section += f"- URL: {p['url']}\n"
        new_section += f"- ⭐{p['stars']} | 评分: {p['score']}\n"
        if p.get("language"):
            new_section += f"- 语言: {p['language']}\n"
        if p.get("topics"):
            new_section += f"- 标签: {', '.join(p['topics'])}\n"
        new_section += "- 状态: ⏳ 待审核\n\n"
    
    content += new_section
    
    Path(skill_path).write_text(content, encoding="utf-8")
    print(f"✅ Updated SKILL.md with {len(top_projects)} new projects")
    return True


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan-results", required=True)
    parser.add_argument("--skill-path", default="skills/omni-news/SKILL.md")
    args = parser.parse_args()
    
    scan_results = load_json(args.scan_results)
    update_skill_md(scan_results, args.skill_path)


if __name__ == "__main__":
    main()
