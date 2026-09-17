#!/usr/bin/env python3
"""
Health Checker - 检查现有数据源的可用性
验证API端点是否可达，RSS源是否有更新
"""

import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: requests not installed")
    sys.exit(1)

# 要检查的关键端点
HEALTH_ENDPOINTS = [
    {"name": "60s API weibo", "url": "https://60s.viki.moe/v2/weibo", "type": "json"},
    {"name": "60s API douyin", "url": "https://60s.viki.moe/v2/douyin", "type": "json"},
    {"name": "60s API zhihu", "url": "https://60s.viki.moe/v2/zhihu", "type": "json"},
    {"name": "60s API toutiao", "url": "https://60s.viki.moe/v2/toutiao", "type": "json"},
    {"name": "60s API bilibili", "url": "https://60s.viki.moe/v2/bilibili", "type": "json"},
    {"name": "60s API maoyan", "url": "https://60s.viki.moe/v2/maoyan", "type": "json"},
    {"name": "WallstreetCN", "url": "https://api-one-wscn.awtmt.com/apiv1/content/information-flow?channel=global&accept=article&limit=5", "type": "json"},
    {"name": "The Hear US", "url": "https://www.thehear.org/api/country-view/us", "type": "json"},
    {"name": "HackerNews", "url": "https://hacker-news.firebaseio.com/v0/topstories.json", "type": "json"},
    {"name": "36kr RSS", "url": "https://36kr.com/feed", "type": "xml"},
    {"name": "BBC RSS", "url": "http://feeds.bbci.co.uk/news/world/rss.xml", "type": "xml"},
    {"name": "Reuters RSS", "url": "https://feeds.reuters.com/Reuters/worldNews", "type": "xml"},
]

def check_endpoint(endpoint):
    """检查单个端点"""
    name = endpoint["name"]
    url = endpoint["url"]
    expected_type = endpoint.get("type", "json")
    
    result = {
        "name": name,
        "url": url,
        "status": "unknown",
        "response_time_ms": 0,
        "items_count": 0,
        "error": None,
    }
    
    try:
        start = time.time()
        resp = requests.get(url, timeout=15, headers={"User-Agent": "OmniNews-HealthCheck/1.0"})
        elapsed = (time.time() - start) * 1000
        result["response_time_ms"] = round(elapsed, 0)
        
        if resp.status_code == 200:
            content_type = resp.headers.get("content-type", "")
            
            if expected_type == "json" and "json" in content_type:
                try:
                    data = resp.json()
                    if isinstance(data, dict) and "data" in data:
                        items = data["data"]
                        if isinstance(items, list):
                            result["items_count"] = len(items)
                        elif isinstance(items, dict) and "list" in items:
                            result["items_count"] = len(items["list"])
                        elif isinstance(items, dict) and "items" in items:
                            result["items_count"] = len(items["items"])
                    elif isinstance(data, list):
                        result["items_count"] = len(data)
                    result["status"] = "healthy"
                except:
                    result["status"] = "degraded"
            elif expected_type == "xml" and ("xml" in content_type or "rss" in content_type):
                text = resp.text
                items = re.findall(r'<item[^>]*>', text, re.IGNORECASE)
                result["items_count"] = len(items)
                result["status"] = "healthy" if items else "degraded"
            else:
                result["status"] = "healthy"
            
            # 响应时间过长
            if elapsed > 10000:
                result["status"] = "slow"
                
        elif resp.status_code == 404:
            result["status"] = "not_found"
            result["error"] = f"HTTP 404"
        elif resp.status_code == 429:
            result["status"] = "rate_limited"
            result["error"] = f"HTTP 429"
        elif resp.status_code >= 500:
            result["status"] = "server_error"
            result["error"] = f"HTTP {resp.status_code}"
        else:
            result["status"] = "error"
            result["error"] = f"HTTP {resp.status_code}"
            
    except requests.exceptions.Timeout:
        result["status"] = "timeout"
        result["error"] = "Connection timeout"
    except requests.exceptions.ConnectionError:
        result["status"] = "connection_error"
        result["error"] = "Connection failed"
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)[:100]
    
    return result


def main():
    print("💓 Omni News Health Checker")
    print(f"📅 {datetime.now().isoformat()}")
    print(f"🔍 检查 {len(HEALTH_ENDPOINTS)} 个端点\n")
    
    results = []
    for ep in HEALTH_ENDPOINTS:
        r = check_endpoint(ep)
        results.append(r)
        
        status_icon = {
            "healthy": "✅",
            "degraded": "⚠️",
            "slow": "🐌",
            "not_found": "❌",
            "rate_limited": "🚫",
            "server_error": "🔥",
            "connection_error": "🔌",
            "timeout": "⏱️",
        }.get(r["status"], "❓")
        
        print(f"  {status_icon} {r['name']}: {r['status']} ({r['response_time_ms']}ms, {r['items_count']} items)")
    
    # 统计
    healthy = sum(1 for r in results if r["status"] == "healthy")
    unhealthy = [r for r in results if r["status"] not in ("healthy", "slow")]
    
    print(f"\n{'=' * 40}")
    print(f"✅ 健康: {healthy}/{len(results)}")
    print(f"❌ 不健康: {len(unhealthy)}/{len(results)}")
    
    output = {
        "check_time": datetime.now().isoformat(),
        "total_endpoints": len(results),
        "healthy_count": healthy,
        "unhealthy_count": len(unhealthy),
        "healthy_pct": round(healthy / len(results) * 100, 1) if results else 0,
        "results": results,
        "unhealthy": unhealthy,
    }
    
    with open("health_results.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"\n📄 结果已保存: health_results.json")


if __name__ == "__main__":
    main()
