#!/usr/bin/env python3
"""Fetch CCTV XinWenLianBo (新闻联播) transcripts from official website.

Zero-dependency Python script using only stdlib (urllib + re).
Fetches from tv.cctv.com/lm/xwlb/day/YYYYMMDD.shtml

Usage: python3 fetch_xwlb.py [YYYYMMDD] [output_dir]
"""

import os
import re
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timedelta

BASE_URL = "https://tv.cctv.com/lm/xwlb"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def fetch_page(url):
    """Fetch a page with proper headers and return HTML content."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except (urllib.error.HTTPError, urllib.error.URLError, OSError) as e:
        print(f"  [WARN] Failed to fetch {url}: {e}", file=sys.stderr)
        return None

def extract_article_urls(html):
    """Extract individual article URLs from the day page."""
    pattern = r'href="(https://tv\.cctv\.com/\d{4}/\d{2}/\d{2}/[A-Za-z0-9]+\.shtml)"'
    urls = re.findall(pattern, html)
    return list(dict.fromkeys(urls))

def extract_title(html):
    """Extract the title from an article page."""
    match = re.search(r'<title>([^<]+)</title>', html)
    if match:
        return match.group(1).strip()
    match = re.search(r'<h[12][^>]*>([^<]+)</h[12]>', html)
    if match:
        return match.group(1).strip()
    return "未知标题"

def extract_content(html):
    """Extract the article body content from CCTV article page."""
    # Strategy 1: Extract from content_area div
    match = re.search(r'id="content_area"[^>]*>(.+?)</div>\s*(?:<!--|<script)', html, re.DOTALL)
    if not match:
        match = re.search(r'class="content_area"[^>]*>(.+?)</div>\s*(?:<!--|<script)', html, re.DOTALL)
    if not match:
        match = re.search(r'id="content_area"[^>]*>(.+?)</div>', html, re.DOTALL)
    
    if match:
        content = match.group(1)
        content = re.sub(r'<[^>]+>', ' ', content)
        content = re.sub(r'&nbsp;', ' ', content)
        content = re.sub(r'&amp;', '&', content)
        content = re.sub(r'&lt;', '<', content)
        content = re.sub(r'&gt;', '>', content)
        content = re.sub(r'\s+', ' ', content).strip()
        if len(content) > 30:
            return content
    
    # Strategy 2: Look for markers and capture
    markers = ['央视网消息', '本台消息', '记者', '央视网讯']
    for marker in markers:
        idx = html.find(marker)
        if idx >= 0:
            chunk = html[idx:idx+5000]
            chunk = re.sub(r'<[^>]+>', ' ', chunk)
            chunk = re.sub(r'\s+', ' ', chunk).strip()
            for ender in ['编辑：', '责任编辑：', '分享：']:
                eidx = chunk.find(ender, 50)
                if eidx > 0:
                    chunk = chunk[:eidx]
                    break
            if len(chunk) > 30:
                return chunk
    
    return None

def fetch_article(url):
    """Fetch a single article and extract title + content."""
    html = fetch_page(url)
    if not html:
        return None
    title = extract_title(html)
    content = extract_content(html)
    return {"title": title, "url": url, "content": content}

def main():
    if len(sys.argv) > 1:
        date_str = sys.argv[1]
    else:
        date_str = datetime.now().strftime("%Y%m%d")

    if len(sys.argv) > 2:
        output_dir = sys.argv[2]
    else:
        output_dir = os.environ.get("XWLB_OUT", "./data/xwlb")

    os.makedirs(output_dir, exist_ok=True)
    url = f"{BASE_URL}/day/{date_str}.shtml"
    print(f"[INFO] Fetching XWLB for {date_str} from {url}", file=sys.stderr)

    html = fetch_page(url)
    if not html:
        print(f"[ERROR] Failed to fetch day page for {date_str}", file=sys.stderr)
        sys.exit(1)

    article_urls = extract_article_urls(html)
    print(f"[INFO] Found {len(article_urls)} article URLs", file=sys.stderr)

    results = []
    for i, url in enumerate(article_urls):
        print(f"[{i+1}/{len(article_urls)}] Fetching {url}", file=sys.stderr)
        article = fetch_article(url)
        if article:
            results.append(article)
        if i < len(article_urls) - 1:
            time.sleep(1)

    date_formatted = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
    lines = [f"# 新闻联播 {date_formatted}\n"]
    for i, article in enumerate(results, 1):
        lines.append(f"## {i}. {article['title']}\n")
        if article['content']:
            lines.append(f"{article['content']}\n")
        else:
            lines.append(f"[仅标题] 文字稿暂未上线或需单独抓取。\n")
        lines.append(f"原文链接: {article['url']}\n")
        lines.append("---\n")

    output_path = os.path.join(output_dir, f"{date_str}.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[DONE] {len(results)} articles saved to {output_path}", file=sys.stderr)
    print(output_path)

if __name__ == "__main__":
    main()
