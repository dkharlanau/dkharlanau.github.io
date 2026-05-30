#!/usr/bin/env python3
"""
Site Content Index Builder for dkharlanau.github.io

Indexes all markdown files from the site checkout.
Extracts YAML frontmatter and outputs deterministic JSONL index.

Usage:
    python3 scripts/build_site_index.py --output professional-radar/site-index/site_content_index.jsonl
    python3 scripts/build_site_index.py --output professional-radar/site-index/site_content_index.jsonl --validate
"""

import argparse
import json
import os
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


class DateTimeEncoder(json.JSONEncoder):
    """JSON encoder that handles datetime.date and datetime.datetime."""
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)


# Collections to index (relative to site root)
COLLECTIONS = {
    "_radar": "radar",
    "_news": "news",
    "_notes": "notes",
    "_blog": "blog",
    "atlas": "atlas",
    "services": "services",
    "ai": "ai",
    "datasets": "datasets",
}

# Fields to extract from frontmatter (with fallback logic)
INDEX_FIELDS = [
    "path",
    "permalink",
    "collection",
    "title",
    "slug",
    "date",
    "modified_at",
    "source",
    "source_url",
    "sap_area",
    "domain",
    "subdomain",
    "canonical_topic",
    "topics",
    "tags",
    "summary",
    "description",
    "excerpt",
    "author",
    "status",
    "confidence",
    "layout",
    "content_type",
]


def extract_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and body from markdown content."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not match:
        return {}, content
    try:
        frontmatter = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        frontmatter = {}
    body = match.group(2)
    return frontmatter, body


def normalize_value(value) -> any:
    """Normalize frontmatter values for JSON serialization."""
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, (list, tuple)):
        return [normalize_value(v) for v in value]
    if isinstance(value, dict):
        return {k: normalize_value(v) for k, v in value.items()}
    return value


def build_index(site_dir: Path) -> tuple[list[dict], list[str]]:
    """Build site content index from all markdown files."""
    records = []
    errors = []

    for dir_name, collection_name in COLLECTIONS.items():
        collection_dir = site_dir / dir_name
        if not collection_dir.exists():
            continue

        for md_file in collection_dir.rglob("*.md"):
            if md_file.name.startswith(".") or md_file.name == "README.md":
                continue

            try:
                content = md_file.read_text(encoding="utf-8")
                frontmatter, body = extract_frontmatter(content)

                if not frontmatter:
                    errors.append(f"No frontmatter: {md_file.relative_to(site_dir)}")
                    continue

                # Build record
                record = {"path": str(md_file.relative_to(site_dir))}

                # Extract collection
                record["collection"] = collection_name

                # Extract title
                title = frontmatter.get("title", "")
                if isinstance(title, str):
                    record["title"] = title.strip()
                else:
                    record["title"] = str(title) if title else ""

                # Extract slug from filename
                slug = md_file.stem
                record["slug"] = slug

                # Extract permalink
                permalink = frontmatter.get("permalink", "")
                if permalink:
                    record["permalink"] = permalink
                else:
                    # Derive from collection and slug
                    record["permalink"] = f"/{collection_name}/{slug}/"

                # Extract date
                date_val = frontmatter.get("date", "")
                if date_val:
                    record["date"] = str(date_val) if not isinstance(date_val, (datetime, date)) else date_val.isoformat()
                else:
                    record["date"] = ""

                # Extract modified_at
                modified = frontmatter.get("last_modified_at", frontmatter.get("modified_at", ""))
                if modified:
                    record["modified_at"] = str(modified) if not isinstance(modified, (datetime, date)) else modified.isoformat()
                else:
                    record["modified_at"] = ""

                # Extract source info
                record["source"] = frontmatter.get("source", "")
                record["source_url"] = frontmatter.get("source_url", "")

                # Extract SAP/area/domain info
                record["sap_area"] = frontmatter.get("sap_area", "")
                record["domain"] = frontmatter.get("domain", "")
                record["subdomain"] = frontmatter.get("subdomain", "")

                # Extract canonical topic
                record["canonical_topic"] = frontmatter.get("canonical_topic", "")

                # Extract topics/tags (normalize to list)
                topics = frontmatter.get("topics", frontmatter.get("tags", []))
                if isinstance(topics, str):
                    topics = [topics] if topics else []
                elif not isinstance(topics, list):
                    topics = []
                record["topics"] = topics
                record["tags"] = topics  # alias

                # Extract summary/description/excerpt
                record["summary"] = frontmatter.get("summary", "")
                record["description"] = frontmatter.get("description", "")
                record["excerpt"] = frontmatter.get("excerpt", "")

                # Extract author
                record["author"] = frontmatter.get("author", "")

                # Extract status
                record["status"] = frontmatter.get("status", "")

                # Extract confidence
                record["confidence"] = frontmatter.get("confidence", "")

                # Extract layout
                record["layout"] = frontmatter.get("layout", "")

                # Extract content type (from atlas)
                record["content_type"] = frontmatter.get("concept_type", "")

                # Add timestamps
                now = datetime.now(timezone.utc).isoformat()
                record["updated_at"] = now
                record["indexed_at"] = now

                # Normalize all values
                record = {k: normalize_value(v) for k, v in record.items()}

                records.append(record)

            except Exception as e:
                errors.append(f"Error processing {md_file.relative_to(site_dir)}: {e}")

    return records, errors


def validate_index(records: list[dict]) -> list[str]:
    """Validate index records for required fields."""
    errors = []
    for idx, record in enumerate(records):
        if not record.get("title"):
            errors.append(f"Record {idx}: empty title (path: {record.get('path', 'unknown')})")
        if not record.get("path"):
            errors.append(f"Record {idx}: empty path")
        if not record.get("collection"):
            errors.append(f"Record {idx}: empty collection (path: {record.get('path', 'unknown')})")
    return errors


def write_index(records: list[dict], output_path: Path) -> None:
    """Write index records as JSONL."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False, cls=DateTimeEncoder) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Build site content index")
    parser.add_argument("--site-dir", type=Path, default=Path("."), help="Site directory (default: current)")
    parser.add_argument("--output", type=Path, default=Path("professional-radar/site-index/site_content_index.jsonl"), help="Output JSONL file path")
    parser.add_argument("--validate", action="store_true", help="Validate index after building")
    args = parser.parse_args()

    print(f"Indexing site: {args.site_dir.resolve()}")
    print(f"Output: {args.output}")

    records, errors = build_index(args.site_dir)

    print(f"\nResults:")
    print(f"  Indexed: {len(records)}")
    print(f"  Errors: {len(errors)}")

    if errors:
        print(f"\nError files:")
        for error in errors[:10]:
            print(f"  - {error}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more")

    if args.validate:
        val_errors = validate_index(records)
        print(f"\nValidation:")
        print(f"  Records checked: {len(records)}")
        print(f"  Validation errors: {len(val_errors)}")
        if val_errors:
            for error in val_errors[:10]:
                print(f"  - {error}")
            if len(val_errors) > 10:
                print(f"  ... and {len(val_errors) - 10} more")

    # Summary by collection
    from collections import Counter
    collections = Counter(r.get("collection", "unknown") for r in records)
    print(f"\nBy collection:")
    for coll, count in sorted(collections.items()):
        print(f"  {coll}: {count}")

    write_index(records, args.output)
    print(f"\nIndex written: {args.output}")


if __name__ == "__main__":
    main()
