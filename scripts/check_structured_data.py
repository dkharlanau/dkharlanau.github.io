#!/usr/bin/env python3
"""Validate JSON-LD structured data in a built Jekyll site.

Checks:
- All <script type="application/ld+json"> blocks parse as JSON.
- No duplicate @id values within a single HTML page.
- No JSON-LD on pages whose robots meta contains noindex.
- No empty required fields for known types.
- No invalid ISO dates.
- No localhost or private-path leaks inside JSON-LD.
- Type-specific required fields:
  - Article: headline, author.name, publisher.name, url
  - BreadcrumbList: itemListElement with >= 2 items, each with name/position
  - Dataset: name, description, distribution (non-empty)
  - Event: name, startDate, location
  - Course: name, description, provider
  - Person/Organization: name

Usage:
    python3 scripts/check_structured_data.py [_site]
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parents[1]

SCRIPT_RE = re.compile(
    r'<script\s+type=["\']application/ld\+json["\']\s*>(.*?)</script>',
    re.IGNORECASE | re.DOTALL,
)
ROBOTS_RE = re.compile(
    r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)

PRIVATE_PATTERNS = [
    "/Users/",
    ".env",
    "source_files",
    "private-source",
    "kb-drafts",
    "Kimi_Agent_SAP Atlas Expansion",
    "Basic_LinkedInDataExport",
    "li2resume.local",
]

LOCALHOST_PATTERNS = ["localhost", "127.0.0.1", "0.0.0.0"]

DATE_FIELDS = {
    "datePublished",
    "dateModified",
    "dateCreated",
    "startDate",
    "endDate",
    "previousStartDate",
    "validFrom",
}


def collect_top_level_ids(obj: object, ids: list[str]) -> None:
    """Record @id values that identify top-level nodes in a JSON-LD block.

    Nested reference objects (e.g. {"@id": "..."} used as property values)
    intentionally reuse IDs and are ignored here; only duplicate top-level
    entities are problematic.
    """
    if isinstance(obj, dict):
        top_id = obj.get("@id")
        if isinstance(top_id, str):
            ids.append(top_id)
        # If this is a graph container, collect IDs of its named graph nodes.
        graph = obj.get("@graph")
        if isinstance(graph, list):
            for item in graph:
                if isinstance(item, dict):
                    item_id = item.get("@id")
                    if isinstance(item_id, str):
                        ids.append(item_id)
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, dict):
                item_id = item.get("@id")
                if isinstance(item_id, str):
                    ids.append(item_id)


def iter_items(obj: object):
    if isinstance(obj, dict):
        yield obj
        for value in obj.values():
            yield from iter_items(value)
    elif isinstance(obj, list):
        for item in obj:
            yield from iter_items(item)


def is_valid_date(value: str) -> bool:
    if not isinstance(value, str):
        return False
    s = value.strip()
    if not s:
        return False
    # Allow open-ended ISO intervals like "2013-12-19/.."
    if ".." in s:
        s = s.replace("/..", "").replace("../", "")
    # Allow interval separator
    if "/" in s:
        parts = s.split("/")
        return all(is_valid_date_part(p) for p in parts if p)
    return is_valid_date_part(s)


def is_valid_date_part(value: str) -> bool:
    try:
        datetime.fromisoformat(value)
        return True
    except ValueError:
        pass
    # Allow year-only or year-month
    for fmt in ("%Y", "%Y-%m"):
        try:
            datetime.strptime(value, fmt)
            return True
        except ValueError:
            pass
    return False


def is_absolute_https(url: str) -> bool:
    return isinstance(url, str) and url.startswith("https://")


def has_private_path(text: str) -> bool:
    lower = text.lower()
    return any(pattern.lower() in lower for pattern in PRIVATE_PATTERNS)


def has_localhost(text: str) -> bool:
    lower = text.lower()
    return any(pattern.lower() in lower for pattern in LOCALHOST_PATTERNS)


def validate_item(item: dict, errors: list[str], file_label: str) -> None:
    if not isinstance(item, dict):
        return

    item_type = item.get("@type")
    if not isinstance(item_type, str):
        return

    # Generic checks for string values inside this item
    for key, value in item.items():
        if isinstance(value, str):
            if key in DATE_FIELDS and not is_valid_date(value):
                errors.append(f"{file_label}: invalid date '{key}={value}'")
            if has_private_path(value):
                errors.append(f"{file_label}: private path in '{key}={value}'")
            if has_localhost(value):
                errors.append(f"{file_label}: localhost in '{key}={value}'")
            if key in {"url", "contentUrl", "item", "sameAs", "image", "mainEntityOfPage"} and value:
                parsed = urlparse(value)
                if parsed.scheme and parsed.scheme not in {"https", "http"}:
                    errors.append(f"{file_label}: non-HTTP(S) URL '{key}={value}'")

    # Type-specific checks
    if item_type in {"Article", "NewsArticle", "BlogPosting"}:
        if not item.get("headline"):
            errors.append(f"{file_label}: Article missing headline")
        author = item.get("author")
        if isinstance(author, dict) and not author.get("name"):
            errors.append(f"{file_label}: Article author missing name")
        publisher = item.get("publisher")
        if isinstance(publisher, dict) and not publisher.get("name"):
            errors.append(f"{file_label}: Article publisher missing name")
        if not item.get("url"):
            errors.append(f"{file_label}: Article missing url")

    elif item_type == "BreadcrumbList":
        elements = item.get("itemListElement")
        if not isinstance(elements, list) or len(elements) < 2:
            errors.append(f"{file_label}: BreadcrumbList needs >= 2 items")
        else:
            for idx, element in enumerate(elements, start=1):
                if not isinstance(element, dict):
                    errors.append(f"{file_label}: BreadcrumbList item {idx} is not an object")
                    continue
                if not element.get("name"):
                    errors.append(f"{file_label}: BreadcrumbList item {idx} missing name")
                if element.get("position") is None:
                    errors.append(f"{file_label}: BreadcrumbList item {idx} missing position")

    elif item_type == "Dataset":
        if not item.get("name"):
            errors.append(f"{file_label}: Dataset missing name")
        if not item.get("description"):
            errors.append(f"{file_label}: Dataset missing description")
        distribution = item.get("distribution")
        if not isinstance(distribution, list) or len(distribution) == 0:
            errors.append(f"{file_label}: Dataset missing distribution")

    elif item_type == "Event":
        if not item.get("name"):
            errors.append(f"{file_label}: Event missing name")
        if not item.get("startDate"):
            errors.append(f"{file_label}: Event missing startDate")
        if not item.get("location"):
            errors.append(f"{file_label}: Event missing location")

    elif item_type == "Course":
        if not item.get("name"):
            errors.append(f"{file_label}: Course missing name")
        if not item.get("description"):
            errors.append(f"{file_label}: Course missing description")
        if not item.get("provider"):
            errors.append(f"{file_label}: Course missing provider")

    elif item_type in {"Person", "Organization"}:
        # A bare reference (e.g. {"@type": "Person", "@id": "..."}) is valid.
        # Only descriptive nodes that lack both a name and an identifier are wrong.
        if not item.get("name") and "@id" not in item:
            errors.append(f"{file_label}: {item_type} missing name")


RICH_RESULT_TYPES = {
    "Article",
    "NewsArticle",
    "BlogPosting",
    "BreadcrumbList",
    "Dataset",
    "Event",
    "Course",
    "ItemList",
    "ProfilePage",
    "Organization",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate JSON-LD structured data in a built site.")
    parser.add_argument("root", nargs="?", default="_site", help="Built site root (default: _site)")
    args = parser.parse_args()

    site_dir = Path(args.root)
    if not site_dir.is_dir():
        print(f"Missing directory: {site_dir}. Build the site before running.")
        return 1

    errors: list[str] = []
    html_files = sorted(site_dir.rglob("*.html"))

    for html_path in html_files:
        rel = html_path.relative_to(site_dir).as_posix()
        content = html_path.read_text(encoding="utf-8", errors="ignore")

        robots_match = ROBOTS_RE.search(content)
        robots = robots_match.group(1).lower() if robots_match else ""
        is_noindex = "noindex" in robots

        blocks = SCRIPT_RE.findall(content)
        if not blocks:
            continue

        if is_noindex:
            errors.append(f"{rel}: JSON-LD found on noindex page")
            continue

        page_ids: list[str] = []
        for block_index, block in enumerate(blocks, start=1):
            block_label = f"{rel} block {block_index}"
            try:
                data = json.loads(html.unescape(block))
            except json.JSONDecodeError as exc:
                errors.append(f"{block_label}: invalid JSON ({exc})")
                continue

            collect_top_level_ids(data, page_ids)

            for item in iter_items(data):
                validate_item(item, errors, block_label)

        seen = set()
        for item_id in page_ids:
            if item_id in seen:
                errors.append(f"{rel}: duplicate @id '{item_id}'")
            seen.add(item_id)

    if errors:
        print(f"Structured data check failed for {len(errors)} issue(s):")
        for item in errors[:200]:
            print(f"- {item}")
        if len(errors) > 200:
            print(f"... and {len(errors) - 200} more")
        return 2

    print(f"Structured data check passed for {len(html_files)} HTML files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
