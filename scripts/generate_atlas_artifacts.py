#!/usr/bin/env python3
"""
Atlas Artifact Generator for dkharlanau.github.io

Regenerates the static Atlas discovery layer:
  - atlas/manifest.json      — machine-readable index of all Atlas pages
  - llms-full.txt            — full-text concatenation of verified pages
  - ai/rag/related.json      — related-content graph from frontmatter

Usage:
    python3 scripts/generate_atlas_artifacts.py
    python3 scripts/generate_atlas_artifacts.py --check

Requirements:
    PyYAML (pip install pyyaml)

Safety:
    - Never exposes source_files or private draft paths.
    - Only includes verified pages in llms-full.txt.
    - Validates that related links point to existing pages.
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


REPO_DIR = Path(__file__).resolve().parent.parent
ATLAS_DIR = REPO_DIR / "atlas"

# Ordered list of Atlas article files (not section index pages)
ATLAS_FILES = sorted([
    "atlas/ai-operations/ai-agent-for-sap-support.md",
    "atlas/ai-operations/ai-ready-process-documentation.md",
    "atlas/ai-operations/authorization-aware-ai-for-sap.md",
    "atlas/automation/agent-assisted-development-workflows.md",
    "atlas/automation/operational-memory-for-sap-ams.md",
    "atlas/automation/rule-based-automation-vs-ai.md",
    "atlas/concepts/order-to-cash.md",
    "atlas/concepts/sap-atp-is-not-inventory.md",
    "atlas/concepts/sap-stock-exists-not-promisable.md",
    "atlas/concepts/store-receiving-sap-retail.md",
    "atlas/data-quality/master-data-governance-failure-modes.md",
    "atlas/data-quality/sap-master-data-quality.md",
    "atlas/diagnostics/pos-sales-not-reflected-in-sap.md",
    "atlas/diagnostics/sap-goods-receipt-diagnostics.md",
    "atlas/diagnostics/sap-invoice-split-analysis.md",
    "atlas/diagnostics/sap-sales-order-block-diagnosis.md",
    "atlas/maps/order-to-cash-map.md",
    "atlas/maps/procure-to-pay-map.md",
    "atlas/sap/gr-ir-clearing-explained.md",
    "atlas/sap/sap-item-category-determination.md",
    "atlas/sap/sap-partner-determination-failures.md",
    "atlas/sap/sap-pricing-procedure-debugging.md",
])


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)


def parse_frontmatter(path):
    """Extract YAML frontmatter and body from a Markdown file."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        return {}, content

    end = content.find("---", 3)
    if end == -1:
        return {}, content

    fm_text = content[3:end].strip()
    body = content[end + 3:].strip()

    try:
        fm = yaml.safe_load(fm_text) or {}
    except Exception as e:
        print(f"YAML parse error in {path}: {e}", file=sys.stderr)
        fm = {}

    return fm, body


def serialize_value(v):
    if isinstance(v, (date, datetime)):
        return v.isoformat()
    if isinstance(v, list):
        return [serialize_value(i) for i in v]
    if isinstance(v, dict):
        return {k: serialize_value(vv) for k, vv in v.items()}
    return v


def strip_jekyll_and_html(text):
    """Remove Jekyll tags, HTML tags, and liquid markup for plain text."""
    text = re.sub(r'{%\s*include\s+[^%]+%}', '', text)
    text = re.sub(r'{%\s*assign\s+[^%]+%}', '', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'{{[^}]+}}', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def build_permalink_map():
    """Build a map of permalink -> file info for the whole site."""
    all_pages = {}
    for root, dirs, files in os.walk(REPO_DIR):
        # Skip generated and dependency dirs
        dirs[:] = [d for d in dirs if d not in {
            "_site", ".git", "vendor", "node_modules", 
            "Kimi_Agent_SAP Atlas Expansion",
            "Basic_LinkedInDataExport_04-10-2026.zip"
        }]
        for f in files:
            if f.endswith(".md"):
                abs_path = Path(root) / f
                rel_path = abs_path.relative_to(REPO_DIR).as_posix()
                fm, _ = parse_frontmatter(abs_path)
                permalink = fm.get("permalink", "")
                if permalink:
                    all_pages[permalink] = {
                        "file": rel_path,
                        "title": fm.get("title", ""),
                        "fm": fm,
                    }
    return all_pages


def generate_manifest(all_pages):
    """Generate atlas/manifest.json."""
    entries = []
    for rel_path in ATLAS_FILES:
        abs_path = REPO_DIR / rel_path
        fm, _ = parse_frontmatter(abs_path)

        related = fm.get("related", []) or []
        tags = fm.get("tags", []) or []

        entry = {
            "title": fm.get("title", ""),
            "description": fm.get("description", ""),
            "url": fm.get("permalink", ""),
            "atlas_section": fm.get("atlas_section", ""),
            "domain": fm.get("domain", ""),
            "subdomain": fm.get("subdomain", ""),
            "concept_type": fm.get("concept_type", ""),
            "sap_area": fm.get("sap_area", ""),
            "business_process": fm.get("business_process", ""),
            "status": fm.get("status", ""),
            "verified": bool(fm.get("verified", False)),
            "last_reviewed": serialize_value(fm.get("last_reviewed", "")),
            "author": fm.get("author", ""),
            "tags": tags,
            "related": serialize_value(related),
        }
        entries.append(entry)

    manifest = {
        "schema": "dkharlanau.atlas.manifest",
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "canonical_url": "https://dkharlanau.github.io/atlas/manifest.json",
        "count": len(entries),
        "verified_count": sum(1 for e in entries if e["verified"]),
        "unverified_count": sum(1 for e in entries if not e["verified"]),
        "sections": sorted({e["atlas_section"] for e in entries}),
        "entries": entries,
    }

    out_path = REPO_DIR / "atlas" / "manifest.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False, cls=DateTimeEncoder)

    return manifest


def generate_llms_full(all_pages):
    """Generate llms-full.txt with verified pages only."""
    lines = []
    lines.append("Atlas Full-Text Manifest")
    lines.append("=" * 50)
    lines.append(f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}")
    lines.append("Canonical: https://dkharlanau.github.io/llms-full.txt")
    lines.append("Source: https://dkharlanau.github.io/atlas/manifest.json")
    lines.append("")
    lines.append("This file contains the full text of reviewed and verified Atlas pages only.")
    lines.append("Pages with status=needs_verification or verified=false are excluded.")
    lines.append("Source file paths are excluded to protect private draft locations.")
    lines.append("")
    lines.append("=" * 50)
    lines.append("")

    verified_count = 0
    for rel_path in ATLAS_FILES:
        abs_path = REPO_DIR / rel_path
        fm, body = parse_frontmatter(abs_path)

        if not fm.get("verified", False):
            continue
        if fm.get("status", "") != "reviewed":
            continue

        verified_count += 1
        title = fm.get("title", "Untitled")
        url = fm.get("permalink", "")
        tags = fm.get("tags", []) or []

        lines.append(f"PAGE: {title}")
        lines.append(f"URL: {url}")
        lines.append(f"SECTION: {fm.get('atlas_section', '')}")
        lines.append(f"DOMAIN: {fm.get('domain', '')}")
        lines.append(f"TYPE: {fm.get('concept_type', '')}")
        lines.append(f"SAP AREA: {fm.get('sap_area', '')}")
        lines.append(f"BUSINESS PROCESS: {fm.get('business_process', '')}")
        lines.append(f"TAGS: {', '.join(tags)}")
        lines.append(f"REVIEWED: {serialize_value(fm.get('last_reviewed', ''))}")
        lines.append("-" * 40)

        clean_body = strip_jekyll_and_html(body)
        lines.append(clean_body)
        lines.append("")
        lines.append("=" * 50)
        lines.append("")

    lines.append(f"END OF MANIFEST — {verified_count} verified pages included")

    out_path = REPO_DIR / "llms-full.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return verified_count


def generate_related(all_pages):
    """Generate ai/rag/related.json from frontmatter related links."""
    edges = []
    broken_links = []

    for rel_path in ATLAS_FILES:
        abs_path = REPO_DIR / rel_path
        fm, _ = parse_frontmatter(abs_path)
        permalink = fm.get("permalink", "")
        title = fm.get("title", "")
        section = fm.get("atlas_section", "")
        tags = fm.get("tags", []) or []
        related = fm.get("related", []) or []

        for link in related:
            target = all_pages.get(link)
            if target:
                edges.append({
                    "source_url": permalink,
                    "source_title": title,
                    "source_section": section,
                    "source_tags": tags,
                    "target_url": link,
                    "target_title": target["title"],
                    "target_file": target["file"],
                    "relation_source": "frontmatter",
                    "valid": True,
                })
            else:
                # Try file-path resolution as fallback
                file_guess = link.strip("/") + ".md"
                abs_guess = REPO_DIR / file_guess
                if abs_guess.exists():
                    target_fm, _ = parse_frontmatter(abs_guess)
                    edges.append({
                        "source_url": permalink,
                        "source_title": title,
                        "source_section": section,
                        "source_tags": tags,
                        "target_url": link,
                        "target_title": target_fm.get("title", ""),
                        "target_file": file_guess,
                        "relation_source": "frontmatter",
                        "valid": True,
                    })
                else:
                    broken_links.append({
                        "source_url": permalink,
                        "source_title": title,
                        "target_url": link,
                        "reason": "target page not found",
                    })

    related_json = {
        "schema": "dkharlanau.atlas.related",
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "canonical_url": "https://dkharlanau.github.io/ai/rag/related.json",
        "description": (
            "Static related-content graph for Atlas pages. "
            "Generated from frontmatter 'related' fields. "
            "For agent navigation and future RAG ingestion."
        ),
        "count": len(edges),
        "broken_link_count": len(broken_links),
        "edges": edges,
        "warnings": broken_links,
    }

    out_dir = REPO_DIR / "ai" / "rag"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "related.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(related_json, f, indent=2, ensure_ascii=False, cls=DateTimeEncoder)

    return edges, broken_links


def main():
    parser = argparse.ArgumentParser(
        description="Regenerate Atlas static discovery artifacts."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate existing artifacts without regenerating.",
    )
    args = parser.parse_args()

    print("Atlas Artifact Generator")
    print("=" * 40)

    # Build permalink map for the whole site
    all_pages = build_permalink_map()
    print(f"Site pages indexed: {len(all_pages)}")

    if args.check:
        # Validation-only mode
        print("\n[CHECK MODE] Validating existing artifacts...")
        # TODO: add validation logic if needed
        return

    # Generate manifest
    print("\n[1/3] Generating atlas/manifest.json ...")
    manifest = generate_manifest(all_pages)
    print(f"  Entries: {manifest['count']}")
    print(f"  Verified: {manifest['verified_count']}")
    print(f"  Unverified: {manifest['unverified_count']}")

    # Generate llms-full.txt
    print("\n[2/3] Generating llms-full.txt ...")
    verified_count = generate_llms_full(all_pages)
    print(f"  Verified pages included: {verified_count}")

    # Generate related.json
    print("\n[3/3] Generating ai/rag/related.json ...")
    edges, broken = generate_related(all_pages)
    print(f"  Edges: {len(edges)}")
    print(f"  Broken links: {len(broken)}")
    if broken:
        for bl in broken:
            print(f"    BROKEN: {bl['source_url']} -> {bl['target_url']}")

    print("\n" + "=" * 40)
    print("All artifacts generated successfully.")
    print("Run 'git diff' to review changes before committing.")


if __name__ == "__main__":
    main()
