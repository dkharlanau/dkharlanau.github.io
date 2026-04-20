#!/usr/bin/env python3
"""Submit changed public URLs to IndexNow after repository updates."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path


BASE_URL = "https://dkharlanau.github.io"
INDEXNOW_KEY = "31ff0ffa67bc49f3bca0a4a719e30fa2"
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
    f"{BASE_URL}/robots.txt",
    f"{BASE_URL}/llms.txt",
    f"{BASE_URL}/LLM.txt",
    f"{BASE_URL}/sitemap.xml",
    f"{BASE_URL}/sitemap-pages.xml",
    f"{BASE_URL}/sitemap-data.xml",
    f"{BASE_URL}/ai/sitemap.xml",
}


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=REPO_ROOT, text=True).strip()


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


def dataset_view_url(path: str) -> str | None:
    if not path.startswith("datasets/") or not path.endswith(".json"):
        return None
    rel = path[len("datasets/") :]
    parts = rel.split("/")
    if len(parts) != 2:
        return None
    collection, filename = parts
    stem = filename[:-5]
    return f"{BASE_URL}/datasets/view/{collection}/{stem}/"


def public_url_for_path(path: str) -> set[str]:
    urls: set[str] = set()
    clean = path.strip()
    if not clean or clean.startswith(("vendor/", ".git/", "_site/")):
        return urls

    abs_path = REPO_ROOT / clean

    if clean in {"robots.txt", "llms.txt", "LLM.txt"}:
        urls.add(f"{BASE_URL}/{clean}")
        return urls

    if clean.startswith(".well-known/"):
        urls.add(f"{BASE_URL}/{clean}")
        return urls

    if clean.endswith(".md"):
        permalink = file_permalink(abs_path)
        if permalink:
            urls.add(f"{BASE_URL}{permalink}")
        return urls

    if clean.startswith(("ai/", "datasets/")) and clean.endswith((".json", ".yml", ".xml", ".txt")):
        urls.add(f"{BASE_URL}/{clean}")
        view_url = dataset_view_url(clean)
        if view_url:
            urls.add(view_url)
        return urls

    if clean.startswith(("assets/", "_data/", "_includes/", "_layouts/")) or clean == "_config.yml":
        urls.update(CORE_URLS)
        return urls

    return urls


def changed_files() -> list[str]:
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    before = ""
    after = ""
    if event_path and Path(event_path).exists():
        payload = json.loads(Path(event_path).read_text(encoding="utf-8"))
        before = payload.get("before", "") or ""
        after = payload.get("after", "") or ""

    if before and set(before) != {"0"} and after:
        diff_range = [before, after]
    else:
        diff_range = ["HEAD~1", "HEAD"]

    try:
        output = git("diff", "--name-only", *diff_range)
    except subprocess.CalledProcessError:
        output = git("ls-files")
    return [line for line in output.splitlines() if line]


def submit(urls: list[str]) -> None:
    if os.environ.get("INDEXNOW_DRY_RUN") == "1":
        print("IndexNow dry run enabled; skipping network request.")
        return

    payload = {
        "host": "dkharlanau.github.io",
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
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
    urls = set()
    for path in changed_files():
        urls.update(public_url_for_path(path))

    if not urls:
        urls.update(CORE_URLS)

    ordered_urls = sorted(urls)
    print(f"Submitting {len(ordered_urls)} URL(s) to IndexNow")
    for url in ordered_urls:
        print(url)

    submit(ordered_urls)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
