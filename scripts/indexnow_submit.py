#!/usr/bin/env python3
"""Submit indexable canonical URLs to IndexNow.

Usage:
    INDEXNOW_KEY=your-key python3 scripts/indexnow_submit.py [--dry-run]
    INDEXNOW_KEY=your-key python3 scripts/indexnow_submit.py --urls /about/ /services/

Rules:
- Key must come from INDEXNOW_KEY env var or .env.local file.
- Dry-run mode prints URLs without submitting.
- Only submits indexable canonical URLs (no noindex, no draft, no research).
- Never submits unverified Atlas or research pages.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path


BASE_URL = "https://dkharlanau.github.io"
INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"
REPO_ROOT = Path(__file__).resolve().parent.parent
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

CORE_URLS = {
    f"{BASE_URL}/",
    f"{BASE_URL}/about/",
    f"{BASE_URL}/ai/",
    f"{BASE_URL}/services/",
    f"{BASE_URL}/datasets/",
    f"{BASE_URL}/notes/",
    f"{BASE_URL}/blog/",
    f"{BASE_URL}/atlas/",
    f"{BASE_URL}/robots.txt",
    f"{BASE_URL}/llms.txt",
    f"{BASE_URL}/LLM.txt",
    f"{BASE_URL}/sitemap.xml",
    f"{BASE_URL}/sitemap-pages.xml",
    f"{BASE_URL}/sitemap-data.xml",
    f"{BASE_URL}/sitemap-atlas.xml",
}


def load_key() -> str:
    """Load IndexNow key from env or .env.local."""
    key = os.environ.get("INDEXNOW_KEY", "").strip()
    if key:
        return key
    env_local = REPO_ROOT / ".env.local"
    if env_local.exists():
        for line in env_local.read_text(encoding="utf-8").splitlines():
            if line.startswith("INDEXNOW_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return ""


def file_permalink(path: Path) -> str | None:
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return None
    for line in match.group(1).splitlines():
        if line.startswith("permalink:"):
            value = line.split(":", 1)[1].strip().strip('"').strip("'")
            if value:
                return value if value.startswith("/") else f"/{value}"
    return None


def is_indexable(path: str, abs_path: Path) -> bool:
    """Check if a markdown file is indexable based on frontmatter."""
    if not abs_path.exists():
        return False
    text = abs_path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return True  # No frontmatter = assume indexable
    fm_text = match.group(1)
    robots = ""
    sitemap_val = ""
    verified = ""
    status = ""
    for line in fm_text.splitlines():
        if line.startswith("robots:"):
            robots = line.split(":", 1)[1].strip().strip('"').strip("'")
        elif line.startswith("sitemap:"):
            sitemap_val = line.split(":", 1)[1].strip().strip('"').strip("'")
        elif line.startswith("verified:"):
            verified = line.split(":", 1)[1].strip().strip('"').strip("'")
        elif line.startswith("status:"):
            status = line.split(":", 1)[1].strip().strip('"').strip("'")
    if "noindex" in robots:
        return False
    if sitemap_val == "false":
        return False
    if path.startswith("research/"):
        return False
    if path.startswith("atlas/"):
        if verified != "true" or status != "reviewed":
            return False
    return True


def public_url_for_path(path: str) -> set[str]:
    urls: set[str] = set()
    clean = path.strip()
    if not clean or clean.startswith(("vendor/", ".git/", "_site/", "scripts/", "tests/", "docs/")):
        return urls

    abs_path = REPO_ROOT / clean

    if clean in {"robots.txt", "llms.txt", "LLM.txt"}:
        urls.add(f"{BASE_URL}/{clean}")
        return urls

    if clean.startswith(".well-known/"):
        urls.add(f"{BASE_URL}/{clean}")
        return urls

    if clean.endswith(".md"):
        if not is_indexable(clean, abs_path):
            return urls
        permalink = file_permalink(abs_path)
        if permalink:
            urls.add(f"{BASE_URL}{permalink}")
        return urls

    if clean.startswith(("ai/", "datasets/", "atlas/")) and clean.endswith((".json", ".yml", ".xml", ".txt")):
        urls.add(f"{BASE_URL}/{clean}")
        return urls

    if clean.startswith(("assets/", "_data/", "_includes/", "_layouts/")) or clean == "_config.yml":
        urls.update(CORE_URLS)
        return urls

    return urls


def discover_indexable_urls() -> set[str]:
    """Walk the repo and discover all indexable canonical URLs."""
    urls: set[str] = set()
    for root, dirs, files in os.walk(REPO_ROOT):
        # Skip non-public dirs
        dirs[:] = [d for d in dirs if d not in {
            "_site", ".git", "vendor", "node_modules",
            "Kimi_Agent_SAP Atlas Expansion", "scripts", "tests",
        } and not d.startswith("Basic_LinkedInDataExport_")]
        for f in files:
            if f.endswith(".md") or f.endswith((".json", ".yml", ".xml", ".txt")):
                rel = Path(root).relative_to(REPO_ROOT).as_posix()
                if rel == ".":
                    rel_path = f
                else:
                    rel_path = f"{rel}/{f}"
                urls.update(public_url_for_path(rel_path))
    return urls


def submit(urls: list[str], key: str, dry_run: bool) -> None:
    if dry_run:
        print("[DRY RUN] Would submit the following URLs to IndexNow:")
        for url in urls:
            print(f"  - {url}")
        return

    payload = {
        "host": "dkharlanau.github.io",
        "key": key,
        "keyLocation": f"{BASE_URL}/{key}.txt",
        "urlList": urls,
    }
    request = urllib.request.Request(
        INDEXNOW_ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read().decode("utf-8", errors="replace")
            print(f"IndexNow response: {response.status}")
            if body:
                print(body)
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        print(f"IndexNow HTTP error: {exc.code}\n{detail}", file=sys.stderr)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Print URLs without submitting")
    parser.add_argument("--urls", nargs="*", help="Explicit relative paths or URLs to submit")
    parser.add_argument("--all", action="store_true", help="Submit all indexable URLs discovered in repo")
    args = parser.parse_args()

    key = load_key()
    if not key:
        print("ERROR: INDEXNOW_KEY not set. Export it or add to .env.local", file=sys.stderr)
        return 1

    urls: set[str] = set()

    if args.urls:
        for u in args.urls:
            if u.startswith("http"):
                urls.add(u)
            else:
                urls.update(public_url_for_path(u))
    elif args.all:
        urls = discover_indexable_urls()
    else:
        urls.update(CORE_URLS)

    if not urls:
        print("No URLs to submit.")
        return 0

    ordered = sorted(urls)
    print(f"Submitting {len(ordered)} URL(s) to IndexNow")
    for url in ordered:
        print(f"  - {url}")

    submit(ordered, key, args.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
