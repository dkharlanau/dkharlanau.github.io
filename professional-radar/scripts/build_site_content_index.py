#!/usr/bin/env python3
"""
build_site_content_index.py

Deterministic site-content index for dkharlanau.github.io.
Runs against local Jekyll source files — no build output required.

Content areas:
  _radar/   → collection: radar
  _news/    → collection: news (deduplicated against _radar mirrors)
  _notes/   → collection: notes
  _blog/    → collection: blog
  atlas/    → area: atlas

Output: JSONL with one record per source file.

Usage:
  python build_site_content_index.py
  python build_site_content_index.py --output /path/to/index.jsonl
  python build_site_content_index.py --check
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT = REPO_ROOT / "professional-radar" / "site-index" / "site_content_index.jsonl"

CONTENT_AREAS = {
    "_radar": {"collection": "radar", "permalink_prefix": "/radar/"},
    "_news": {"collection": "news", "permalink_prefix": "/news/"},
    "_notes": {"collection": "notes", "permalink_prefix": "/notes/"},
    "_blog": {"collection": "blog", "permalink_prefix": "/blog/"},
    "atlas": {"collection": "atlas", "permalink_prefix": "/atlas/"},
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def sha256(text: str) -> str:
    """Deterministic SHA-256 of normalized UTF-8 text."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def parse_frontmatter(raw: str) -> tuple:
    """Extract YAML frontmatter and remaining body from a markdown file."""
    if raw.startswith("---"):
        parts = raw.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1].strip()
            body = parts[2].strip()
            return _yaml_to_dict(fm_text), body
    return {}, raw


def _yaml_to_dict(text: str) -> dict[str, Any]:
    """Minimal YAML parser sufficient for the site's frontmatter keys."""
    result: dict[str, Any] = {}
    key: str | None = None
    buffer: list[str] = []
    indent_stack: list[int] = []
    list_stack: list[list[Any]] = []
    current_list: list[Any] | None = None

    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()
        if not stripped or stripped.startswith("#"):
            i += 1
            continue

        indent = len(line) - len(stripped)

        # List item
        if stripped.startswith("- "):
            value = stripped[2:].strip()
            # If we're inside a nested dict context, this list item belongs to that dict
            if current_list is not None:
                # Parse inline key: value if present
                if ": " in value and not value.startswith('"') and not value.startswith("'"):
                    k, v = value.split(": ", 1)
                    current_list.append({k.strip(): _parse_yaml_value(v.strip())})
                else:
                    current_list.append(_parse_yaml_value(value))
            else:
                if key is None:
                    i += 1
                    continue
                if not isinstance(result.get(key), list):
                    result[key] = []
                current_list = result[key]
                current_list.append(_parse_yaml_value(value))
            i += 1
            continue

        # Reset list tracking on non-list, non-indented line
        if current_list is not None and indent == 0 and not stripped.startswith("-"):
            current_list = None

        # Key: value
        if ":" in stripped:
            colon_idx = stripped.index(":")
            key = stripped[:colon_idx].strip()
            rest = stripped[colon_idx + 1 :].strip()
            if rest:
                result[key] = _parse_yaml_value(rest)
            else:
                # Might be a nested dict or list starting next line
                result[key] = {}
            i += 1
            continue

        i += 1

    return result


def _parse_yaml_value(value: str) -> Any:
    """Parse a simple YAML scalar value."""
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    if value.lower() in ("true", "yes"):
        return True
    if value.lower() in ("false", "no"):
        return False
    if value in ("null", "~", ""):
        return None
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        pass
    return value


def extract_headings(body: str) -> list[str]:
    """Extract H2 and H3 headings from markdown body."""
    headings = []
    for line in body.splitlines():
        match = re.match(r"^(#{2,3})\s+(.+)$", line.strip())
        if match:
            level = len(match.group(1))
            text = match.group(2).strip()
            # Strip inline markdown like bold/italic
            text = re.sub(r"\*\*?|\_\_?", "", text)
            headings.append(text)
    return headings


def infer_permalink(path: Path, collection: str, frontmatter: dict) -> Optional[str]:
    """Infer Jekyll permalink from frontmatter or collection defaults."""
    if "permalink" in frontmatter:
        return frontmatter["permalink"]

    slug = path.stem
    cfg = CONTENT_AREAS.get(f"_{collection}") if collection != "atlas" else CONTENT_AREAS.get("atlas")
    if cfg:
        prefix = cfg["permalink_prefix"]
        if collection == "atlas":
            # atlas files are in subdirectories; index.md is the dir index
            rel = path.relative_to(REPO_ROOT / "atlas")
            if slug == "index":
                return f"/atlas/{rel.parent}/" if str(rel.parent) != "." else "/atlas/"
            return f"/atlas/{rel.parent}/{slug}/" if str(rel.parent) != "." else f"/atlas/{slug}/"
        return f"{prefix}{slug}/"
    return None


def canonical_topic_from(frontmatter: dict, collection: str, headings: list[str]) -> Optional[str]:
    """Infer a canonical topic from available metadata."""
    topics = frontmatter.get("topics", [])
    if topics:
        return topics[0] if isinstance(topics, list) else topics
    tags = frontmatter.get("tags", [])
    if tags:
        return tags[0] if isinstance(tags, list) else tags
    if "sap_area" in frontmatter:
        return frontmatter["sap_area"]
    if "business_process" in frontmatter:
        return frontmatter["business_process"]
    if headings:
        return headings[0]
    return None


def audience_from(frontmatter: dict, collection: str) -> Optional[str]:
    """Infer audience from collection or metadata."""
    if collection in ("radar", "news"):
        return "professional_radar"
    if collection == "notes":
        return "technical_leadership"
    if collection == "blog":
        return "general"
    if collection == "atlas":
        return "sap_practitioner"
    return None


def description_from(frontmatter: dict, body: str) -> Optional[str]:
    """Return description or excerpt from frontmatter, or first paragraph of body."""
    for key in ("description", "excerpt", "summary", "subtitle"):
        if key in frontmatter:
            val = frontmatter[key]
            if val and str(val).strip():
                return str(val).strip()
    # First non-empty paragraph of body
    for para in body.split("\n\n"):
        para = para.strip()
        if para and not para.startswith("<") and not para.startswith("{%"):
            # Strip markdown inline formatting
            clean = re.sub(r"\*\*?|\_\_?", "", para).strip()
            if clean:
                return clean[:300]
    return None


# ---------------------------------------------------------------------------
# Indexer
# ---------------------------------------------------------------------------


def index_file(path: Path, collection: str) -> Optional[dict[str, Any]]:
    """Return an index record for a single markdown file, or None if invalid."""
    raw = path.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(raw)

    if not frontmatter:
        return None  # Skip files without frontmatter

    permalink = infer_permalink(path, collection, frontmatter)
    headings = extract_headings(body)
    description = description_from(frontmatter, body)
    topics = frontmatter.get("topics", [])
    if not isinstance(topics, list):
        topics = [topics] if topics else []
    tags = frontmatter.get("tags", [])
    if not isinstance(tags, list):
        tags = [tags] if tags else []

    date_raw = frontmatter.get("date") or frontmatter.get("last_modified_at")
    date_str = None
    if date_raw:
        if isinstance(date_raw, datetime):
            date_str = date_raw.strftime("%Y-%m-%d")
        else:
            date_str = str(date_raw)[:10]

    # Normalize content for hashing (strip frontmatter, normalize whitespace)
    normalized_body = re.sub(r"\s+", " ", body).strip()
    content_hash = sha256(normalized_body)

    record = {
        "path": str(path.relative_to(REPO_ROOT)),
        "collection_or_area": collection,
        "permalink": permalink,
        "title": frontmatter.get("title"),
        "description": description,
        "headings": headings,
        "topics": topics,
        "tags": tags,
        "canonical_topic": canonical_topic_from(frontmatter, collection, headings),
        "sap_area": frontmatter.get("sap_area"),
        "business_process": frontmatter.get("business_process"),
        "audience": audience_from(frontmatter, collection),
        "source_url": frontmatter.get("source_url"),
        "date": date_str,
        "date_checked": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "confidence": frontmatter.get("confidence"),
        "content_hash": content_hash,
    }

    # Prune None values for compactness, but keep empty lists for array fields
    record = {k: v for k, v in record.items() if v is not None}
    return record


def build_index() -> list[dict[str, Any]]:
    """Walk all content areas and build a deterministic index."""
    records: list[dict[str, Any]] = []
    seen_hashes: set[str] = set()

    for area_dir, cfg in CONTENT_AREAS.items():
        collection = cfg["collection"]
        area_path = REPO_ROOT / area_dir
        if not area_path.exists():
            continue

        # Find all .md files, sorted for determinism
        md_files = sorted(area_path.rglob("*.md"), key=lambda p: str(p))

        for md_file in md_files:
            record = index_file(md_file, collection)
            if not record:
                continue

            # Deduplicate radar/news mirrors by content hash
            ch = record.get("content_hash")
            if ch in seen_hashes:
                continue
            seen_hashes.add(ch)

            records.append(record)

    # Sort records by path for deterministic output
    records.sort(key=lambda r: r["path"])
    return records


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def write_jsonl(records: list[dict[str, Any]], output_path: Path) -> None:
    """Write records as JSONL with deterministic key ordering."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def smoke_test(records: list[dict[str, Any]]) -> bool:
    """Run basic smoke tests."""
    errors = []

    # 1. Non-empty
    if not records:
        errors.append("Index is empty.")

    # 2. Contains atlas
    atlas_count = sum(1 for r in records if r.get("collection_or_area") == "atlas")
    if atlas_count == 0:
        errors.append("No atlas records found.")
    print(f"  atlas records: {atlas_count}")

    # 3. Contains radar
    radar_count = sum(1 for r in records if r.get("collection_or_area") == "radar")
    if radar_count == 0:
        errors.append("No radar records found.")
    print(f"  radar records: {radar_count}")

    # 4. Deduplication: total radar + news should be <= distinct files in those dirs
    # More practically: if radar and news have identical files, news should be deduplicated
    news_count = sum(1 for r in records if r.get("collection_or_area") == "news")
    print(f"  news records: {news_count} (deduplicated)")
    radar_files = len(list((REPO_ROOT / "_radar").rglob("*.md"))) if (REPO_ROOT / "_radar").exists() else 0
    news_files = len(list((REPO_ROOT / "_news").rglob("*.md"))) if (REPO_ROOT / "_news").exists() else 0
    if radar_files > 0 and news_files > 0 and radar_count + news_count >= radar_files + news_files:
        errors.append("Deduplication may not be working (radar+news count >= raw file count).")

    # 5. Every record has required fields
    for r in records:
        for key in ("path", "collection_or_area", "content_hash"):
            if key not in r:
                errors.append(f"Record missing '{key}': {r.get('path')}")

    if errors:
        print("SMOKE TEST FAILED:")
        for e in errors:
            print(f"  - {e}")
        return False

    print("SMOKE TEST PASSED")
    return True


def stability_test(output_path: Path) -> bool:
    """Run twice and compare hashes for stability."""
    records1 = build_index()
    write_jsonl(records1, output_path)
    hash1 = sha256(output_path.read_text(encoding="utf-8"))

    records2 = build_index()
    write_jsonl(records2, output_path)
    hash2 = sha256(output_path.read_text(encoding="utf-8"))

    if hash1 == hash2:
        print(f"STABILITY TEST PASSED (hash: {hash1[:16]}...)")
        return True
    else:
        print("STABILITY TEST FAILED: output differs between runs")
        print(f"  run 1: {hash1}")
        print(f"  run 2: {hash2}")
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Build deterministic site-content index")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Output JSONL path")
    parser.add_argument("--check", action="store_true", help="Run smoke + stability tests")
    args = parser.parse_args()

    print("Building site-content index ...")
    records = build_index()
    print(f"  total records: {len(records)}")

    write_jsonl(records, args.output)
    print(f"  written to: {args.output}")

    ok = smoke_test(records)

    if args.check:
        ok = stability_test(args.output) and ok

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
