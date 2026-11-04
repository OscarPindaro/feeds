#!/usr/bin/env python3
"""Drop feeds from feeds-llm.opml that no longer answer with a real feed.

Usage: python3 refresh.py [--dry-run]

A feed is kept only if it returns HTTP 200 and the body contains at least one
<item> or <entry>. Everything else — dead domains, 404s, HTML soft-404s — is
removed. Categories and ordering are preserved.
"""

import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

PATH = "feeds-llm.opml"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"


def fetch(url: str) -> bool:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": UA, "Accept": "application/rss+xml, application/xml, text/xml, */*"},
    )
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            if r.status != 200:
                return False
            body = r.read(200_000).decode("utf-8", "replace")
    except Exception:
        return False
    return "<item" in body or "<entry" in body


def alive(url: str) -> bool:
    # A single failure is usually rate limiting, not a dead feed: several hosts
    # (github.blog, martinfowler.com) reject bursts and answer fine seconds later.
    for attempt, delay in enumerate((0, 3, 8)):
        if attempt:
            time.sleep(delay)
        if fetch(url):
            return True
    return False


def main() -> int:
    dry = "--dry-run" in sys.argv
    tree = ET.parse(PATH)
    root = tree.getroot()
    body = root.find("body")
    if body is None:
        print("no <body> in", PATH)
        return 1

    urls = [o.get("xmlUrl") for o in body.iter("outline") if o.get("xmlUrl")]
    with ThreadPoolExecutor(max_workers=8) as ex:
        results = list(ex.map(alive, urls))

    dead = [u for u, ok in zip(urls, results) if not ok]
    print(f"{len(urls) - len(dead)}/{len(urls)} alive, {len(dead)} dead")
    for u in dead:
        print("  -", u)

    if dry or not dead:
        return 0

    if len(dead) > len(urls) // 5:
        print("refusing to rewrite: more than 20% failed, that looks like a network problem")
        return 1

    for group in body:
        for outline in list(group):
            if outline.get("xmlUrl") in dead:
                group.remove(outline)

    ET.indent(tree, space="  ")
    tree.write(PATH, encoding="UTF-8", xml_declaration=True)
    print(f"rewrote {PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
