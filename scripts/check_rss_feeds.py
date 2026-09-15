#!/usr/bin/env python3
"""Validate source-backed RSS/Atom feeds in the rendered Jekyll artifact."""

from __future__ import annotations

import argparse
from datetime import date, datetime
from email.utils import parsedate_to_datetime
from pathlib import Path
import xml.etree.ElementTree as ET

import yaml

from lib.content_model import discover_pages

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://dkharlanau.github.io"
ATOM_NS = "http://www.w3.org/2005/Atom"


def fail(message: str) -> None:
    raise SystemExit(f"RSS contract failed: {message}")


def as_date(value: object, label: str) -> date:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    text = str(value or "").strip()[:10]
    try:
        return date.fromisoformat(text)
    except ValueError:
        fail(f"invalid {label}: {value!r}")


def read_xml(path: Path) -> ET.Element:
    if not path.is_file():
        fail(f"missing rendered feed: {path}")
    try:
        return ET.parse(path).getroot()
    except ET.ParseError as exc:
        fail(f"invalid XML in {path}: {exc}")


def text(node: ET.Element | None) -> str:
    return "" if node is None or node.text is None else node.text.strip()


def validate_templates() -> None:
    for rel in ("feed.xml", "rss.xml", "blog/feed.xml"):
        source = (ROOT / rel).read_text(encoding="utf-8")
        if "site.time" in source:
            fail(f"{rel} depends on the Jekyll build clock")


def eligible_blog_urls() -> set[str]:
    pages, parse_errors = discover_pages(ROOT)
    if parse_errors:
        failed = ", ".join(item["path"] for item in parse_errors[:5])
        fail(f"front matter parse errors block feed validation: {failed}")
    return {
        page.canonical_url
        for page in pages
        if page.collection == "blog" and page.retrieval_eligible and page.date_published
    }


def validate_rss(site_dir: Path, trusted_blogs: set[str]) -> tuple[int, int]:
    root = read_xml(site_dir / "rss.xml")
    if root.tag != "rss" or root.attrib.get("version") != "2.0":
        fail("_site/rss.xml is not RSS 2.0")
    channel = root.find("channel")
    if channel is None:
        fail("RSS channel is missing")

    self_links = [
        node
        for node in channel.findall(f"{{{ATOM_NS}}}link")
        if node.attrib.get("rel") == "self"
    ]
    if not any(
        node.attrib.get("href") == f"{BASE_URL}/rss.xml"
        and node.attrib.get("type") == "application/rss+xml"
        for node in self_links
    ):
        fail("RSS self-discovery link is missing or incorrect")

    items = channel.findall("item")
    if not items:
        fail("RSS contains no source-backed items")

    changelog = yaml.safe_load((ROOT / "_data/changelog.yml").read_text(encoding="utf-8")) or {}
    changelog_entries = changelog.get("entries") or []
    item_by_title = {text(item.find("title")): item for item in items}

    for entry in changelog_entries:
        title = str(entry.get("title") or "").strip()
        summary = str(entry.get("summary") or "").strip()
        if not title or not summary:
            fail("every changelog RSS source entry needs title and summary")
        item = item_by_title.get(title)
        if item is None:
            fail(f"changelog entry missing from RSS: {title}")
        if text(item.find("link")) != f"{BASE_URL}/changelog/":
            fail(f"changelog item links to the wrong page: {title}")
        guid = item.find("guid")
        if guid is None or guid.attrib.get("isPermaLink") != "false" or ":changelog/" not in text(guid):
            fail(f"changelog item has no stable non-permalink GUID: {title}")
        try:
            rendered_date = parsedate_to_datetime(text(item.find("pubDate"))).date()
        except (TypeError, ValueError) as exc:
            fail(f"invalid RSS pubDate for changelog entry {title}: {exc}")
        if rendered_date != as_date(entry.get("date"), f"changelog date for {title}"):
            fail(f"RSS pubDate does not match changelog source date: {title}")
        if text(item.find("description")) != summary:
            fail(f"RSS description does not match changelog source summary: {title}")

    blog_items = 0
    for item in items:
        link = text(item.find("link"))
        if not link.startswith(f"{BASE_URL}/blog/"):
            continue
        blog_items += 1
        if link not in trusted_blogs:
            fail(f"unreviewed, unverified, or non-indexable blog leaked into RSS: {link}")
        guid = item.find("guid")
        if guid is None or guid.attrib.get("isPermaLink") != "true" or text(guid) != link:
            fail(f"blog RSS item has an unstable GUID: {link}")

    return len(items), blog_items


def atom_entry_urls(root: ET.Element) -> set[str]:
    urls: set[str] = set()
    for entry in root.findall(f"{{{ATOM_NS}}}entry"):
        for link in entry.findall(f"{{{ATOM_NS}}}link"):
            href = link.attrib.get("href", "")
            if link.attrib.get("rel") == "alternate" and href.startswith(f"{BASE_URL}/blog/"):
                urls.add(href)
    return urls


def validate_atom(site_dir: Path, trusted_blogs: set[str]) -> tuple[int, int]:
    root_feed = read_xml(site_dir / "feed.xml")
    blog_feed = read_xml(site_dir / "blog/feed.xml")
    expected_tag = f"{{{ATOM_NS}}}feed"
    if root_feed.tag != expected_tag:
        fail("_site/feed.xml is not an Atom feed")
    if blog_feed.tag != expected_tag:
        fail("_site/blog/feed.xml is not an Atom feed")
    if not text(root_feed.find(f"{{{ATOM_NS}}}updated")):
        fail("primary Atom feed has no source-backed updated timestamp")
    if not text(blog_feed.find(f"{{{ATOM_NS}}}updated")):
        fail("blog Atom feed has no source-backed updated timestamp")

    root_blog_urls = atom_entry_urls(root_feed)
    blog_urls = atom_entry_urls(blog_feed)
    for url in root_blog_urls | blog_urls:
        if url not in trusted_blogs:
            fail(f"untrusted blog leaked into Atom feed: {url}")
    return len(root_feed.findall(f"{{{ATOM_NS}}}entry")), len(blog_feed.findall(f"{{{ATOM_NS}}}entry"))


def validate_discovery(site_dir: Path) -> None:
    index = (site_dir / "index.html").read_text(encoding="utf-8")
    expected = f'href="{BASE_URL}/rss.xml"'
    if 'rel="alternate" type="application/rss+xml"' not in index or expected not in index:
        fail("homepage is missing RSS autodiscovery from the shared template")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-dir", default="_site")
    args = parser.parse_args()
    site_dir = (ROOT / args.site_dir).resolve()

    validate_templates()
    trusted_blogs = eligible_blog_urls()
    rss_items, rss_blog_items = validate_rss(site_dir, trusted_blogs)
    atom_items, blog_atom_items = validate_atom(site_dir, trusted_blogs)
    validate_discovery(site_dir)
    print(
        "RSS/Atom contract passed: "
        f"rss_items={rss_items}, rss_blog_items={rss_blog_items}, "
        f"root_atom_entries={atom_items}, blog_atom_entries={blog_atom_items}."
    )


if __name__ == "__main__":
    main()
