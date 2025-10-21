#!/usr/bin/env python3
"""
Generate a fully static sitemap.xml by inspecting source content.

The script walks Markdown/HTML pages (with front matter), the `_notes`
collection, and selected machine-readable assets (under `ai/` plus `LLM.txt`),
then emits an XML sitemap at the project root. Run this after making content
changes or rebuilding the site.

Requires `PyYAML` (`python3 -m pip install --user PyYAML`).

Example:
    python bin/build_static_sitemap.py
"""
from __future__ import annotations

import datetime as dt
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_FILE = ROOT / "sitemap-static.xml"
CONFIG_FILE = ROOT / "_config.yml"


def load_site_config() -> Dict[str, Any]:
    if not CONFIG_FILE.exists():
        raise FileNotFoundError(f"Cannot find config file at {CONFIG_FILE}")
    with CONFIG_FILE.open("r", encoding="utf-8") as fp:
        return yaml.safe_load(fp)


def parse_front_matter(path: Path) -> Tuple[Dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    text = text.lstrip("\ufeff")  # strip BOM if present
    if not text.startswith("---"):
        return {}, text
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
    if not match:
        return {}, text
    front_matter_raw, content = match.groups()
    data = yaml.safe_load(front_matter_raw) or {}
    return data, content


def to_iso_timestamp(path: Path) -> str:
    timestamp = dt.datetime.fromtimestamp(path.stat().st_mtime, tz=dt.timezone.utc)
    return timestamp.isoformat()


def ensure_path(url_path: str) -> str:
    if not url_path.startswith("/"):
        url_path = "/" + url_path
    url_path = re.sub(r"//+", "/", url_path)
    if not Path(url_path).suffix and not url_path.endswith("/"):
        url_path += "/"
    return url_path


def collect_standard_pages() -> Iterable[Tuple[str, Path]]:
    """Collect Markdown/HTML/XML pages outside special directories."""
    ignored_dirs = {
        "_site",
        "assets",
        "vendor",
        "bin",
        "_notes",
        "_layouts",
        "_includes",
        "_data",
        "_sass",
        "ai",
    }
    for path in ROOT.rglob("*"):
        if path.is_dir():
            continue
        if path.suffix not in {".md", ".html", ".xml"}:
            continue
        relative = path.relative_to(ROOT)
        if relative.parts and relative.parts[0] in ignored_dirs:
            continue
        relative_str = str(relative)
        if relative_str in {
            "sitemap.xml",
            "sitemap-pages.xml",
            "sitemap-data.xml",
            "sitemap-static.xml",
        }:
            continue
        data, _ = parse_front_matter(path)
        if not data:
            continue
        if data.get("sitemap") is False:
            continue
        url = data.get("permalink")
        if not url:
            if path.name in {"index.md", "index.html"}:
                parent = "/" + "/".join(relative.parent.parts)
                url = parent if parent != "/" else "/"
            else:
                url = "/" + "/".join(relative.with_suffix("").parts)
        yield ensure_path(url), path


def slugify(value: str) -> str:
    value = value.lower()
    value = value.replace("_", "-").replace(" ", "-")
    value = re.sub(r"[^a-z0-9\\-]+", "", value)
    value = re.sub(r"-{2,}", "-", value)
    return value.strip("-")


def collect_notes() -> Iterable[Tuple[str, Path]]:
    notes_dir = ROOT / "_notes"
    if not notes_dir.exists():
        return []
    notes: List[Tuple[str, Path]] = []
    for path in notes_dir.glob("*.md"):
        data, _ = parse_front_matter(path)
        if data.get("sitemap") is False:
            continue
        slug = data.get("slug") or slugify(path.stem)
        notes.append((ensure_path(f"/notes/{slug}/"), path))
    return notes


def collect_ai_assets() -> Iterable[Tuple[str, Path]]:
    ai_dir = ROOT / "ai"
    if not ai_dir.exists():
        return []
    assets: List[Tuple[str, Path]] = []
    for path in ai_dir.rglob("*"):
        if path.is_dir():
            continue
        if path.suffix.lower() not in {".json", ".yml", ".yaml"}:
            continue
        relative = path.relative_to(ROOT)
        assets.append((ensure_path("/" + "/".join(relative.parts)), path))
    txt_file = ROOT / "LLM.txt"
    if txt_file.exists():
        assets.append(("/LLM.txt", txt_file))
    return assets


def build_url(base_url: str, base_path: str, path: str) -> str:
    if base_path and not base_path.startswith("/"):
        base_path = "/" + base_path
    base = base_url.rstrip("/")
    combined = base + base_path
    return combined.rstrip("/") + path


def generate_sitemap() -> None:
    config = load_site_config()
    site_url = config.get("url", "https://example.com")
    baseurl = config.get("baseurl", "")

    entries: Dict[str, str] = {}

    for url_path, source_path in (
        list(collect_standard_pages())
        + list(collect_notes())
        + list(collect_ai_assets())
    ):
        entries[url_path] = to_iso_timestamp(source_path)

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]

    for url_path in sorted(entries.keys()):
        full_url = build_url(site_url, baseurl, url_path)
        lastmod = entries[url_path]
        xml_lines.append("  <url>")
        xml_lines.append(f"    <loc>{full_url}</loc>")
        xml_lines.append(f"    <lastmod>{lastmod}</lastmod>")
        xml_lines.append("  </url>")

    xml_lines.append("</urlset>")

    OUTPUT_FILE.write_text("\n".join(xml_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    generate_sitemap()
