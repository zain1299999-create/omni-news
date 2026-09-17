#!/usr/bin/env python3
"""
Update Evolution Log - 更新进化日志
"""

import json
import os
from datetime import datetime
from pathlib import Path


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def update_log(scan_results, date_str):
    """更新EVOLUTION_LOG.md"""
    log_path = Path("EVOLUTION_LOG.md")
    
    projects = scan_results.get("new_projects", [])
    
    lines = []
    lines.append(f"## {date_str}")
    lines.append("")
    lines.append(f"**扫描模式**: {scan_results.get('mode', 'normal')} | **发现新项目**: {len(projects)}")
    lines.append("")
    
    if projects:
        lines.append("| # | 项目 | Stars | 评分 | 描述 |")
        lines.append("|---|------|-------|------|------|")
        for i, p in enumerate(projects[:10], 1):
            desc = (p.get("description") or "")[:50]
            lines.append(f"| {i} | [{p['name']}]({p['url']}) | ⭐{p['stars']} | {p['score']} | {desc} |")
    else:
        lines.append("_未发现新项目_")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    
    new_content = "\n".join(lines)
    
    # 读取现有内容
    if log_path.exists():
        existing = log_path.read_text(encoding="utf-8")
    else:
        existing = "# 🧬 进化日志\n\n> 自动记录每次扫描发现的新技术和项目。\n\n"
    
    # 插入到标题之后
    if "# 🧬 进化日志" in existing:
        parts = existing.split("\n\n", 1)
        content = parts[0] + "\n\n" + new_content + (parts[1] if len(parts) > 1 else "")
    else:
        content = new_content + existing
    
    log_path.write_text(content, encoding="utf-8")
    print(f"✅ Updated EVOLUTION_LOG.md")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan-results", required=True)
    parser.add_argument("--date", required=True)
    args = parser.parse_args()
    
    scan_results = load_json(args.scan_results)
    update_log(scan_results, args.date)
