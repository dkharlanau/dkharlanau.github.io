#!/usr/bin/env python3
"""
Atlas Artifact Generator for dkharlanau.github.io

Regenerates the static Atlas discovery layer:
  - atlas/manifest.json        — machine-readable index of all Atlas pages
  - llms-full.txt              — full-text concatenation of verified Atlas pages
  - ai/rag/related.json        — related-content graph from frontmatter
  - ai/atlas-compact-index.json — compact signal-matching index
  - ai/verified-pages.json     — site-wide inventory of reviewed, verified, indexable pages

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

CHECK_MODE_TIMESTAMP = "CHECK_MODE"


def discover_atlas_articles():
    """Dynamically discover public Atlas article pages under atlas/.

    Inclusion rules (all must be true):
      - path matches atlas/**/*.md
      - frontmatter has permalink starting with /atlas/
      - frontmatter has atlas_section
      - frontmatter has status
      - frontmatter has verified
      - not a section/index page (path does not end with /index.md)
      - not marked sitemap: false unless atlas_include: true is present

    Returns a sorted list of relative POSIX paths.
    """
    articles = []
    for md_path in sorted(ATLAS_DIR.rglob("*.md")):
        rel_path = md_path.relative_to(REPO_DIR).as_posix()

        # Exclude section/index pages by path pattern
        if rel_path.endswith("/index.md") or rel_path == "atlas/index.md":
            continue

        fm, _ = parse_frontmatter(md_path)
        if not fm:
            continue

        # Required frontmatter signals
        permalink = fm.get("permalink", "")
        if not permalink or not permalink.startswith("/atlas/"):
            continue
        if "atlas_section" not in fm:
            continue
        if "status" not in fm:
            continue
        if "verified" not in fm:
            continue

        # Exclude noindex/sitemap:false pages unless explicitly included
        # OR unless they have all required article frontmatter (article pages
        # may set sitemap:false while still belonging to the Atlas manifest).
        sitemap = fm.get("sitemap", True)
        atlas_include = fm.get("atlas_include", False)
        has_article_signals = all(k in fm for k in ("atlas_section", "status", "verified"))
        if sitemap is False and not atlas_include and not has_article_signals:
            continue

        articles.append(rel_path)

    return sorted(articles)


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


def extract_headings(body, max_headings=12):
    """Extract compact markdown/HTML headings for matching."""
    headings = []
    for line in body.splitlines():
        stripped = line.strip()
        md_match = re.match(r"^#{2,4}\s+(.+)$", stripped)
        html_match = re.match(r"^<h([2-4])[^>]*>(.*?)</h\1>$", stripped, re.I)
        text = ""
        if md_match:
            text = md_match.group(1)
        elif html_match:
            text = html_match.group(2)
        if text:
            clean = strip_jekyll_and_html(text)
            clean = re.sub(r"\s+", " ", clean).strip()
            if clean and clean not in headings:
                headings.append(clean)
        if len(headings) >= max_headings:
            break
    return headings


def _keyword_terms(*values):
    terms = []
    for value in values:
        if not value:
            continue
        if isinstance(value, list):
            candidates = value
        else:
            candidates = [value]
        for candidate in candidates:
            text = str(candidate).strip()
            if not text:
                continue
            normalized = re.sub(r"\s+", " ", text.lower())
            if normalized not in terms:
                terms.append(normalized)
    return terms


def _token_terms(text):
    tokens = re.findall(r"[a-z0-9][a-z0-9+-]{2,}", text.lower())
    stopwords = {
        "the", "and", "for", "with", "from", "that", "this", "how", "when",
        "where", "what", "why", "into", "page", "sap",
    }
    result = []
    for token in tokens:
        if token in stopwords:
            continue
        if token not in result:
            result.append(token)
    return result


def _matching_terms(fm, headings):
    phrase_terms = _keyword_terms(
        fm.get("title", ""),
        fm.get("description", ""),
        fm.get("domain", ""),
        fm.get("subdomain", ""),
        fm.get("concept_type", ""),
        fm.get("sap_area", ""),
        fm.get("business_process", ""),
        fm.get("tags", []) or [],
        headings,
    )
    token_text = " ".join(phrase_terms)
    token_terms = _token_terms(token_text)
    combined = []
    for term in phrase_terms + token_terms:
        if term and term not in combined:
            combined.append(term)
    return combined[:80]


def _sap_domain_keywords(fm):
    return _keyword_terms(
        fm.get("domain", ""),
        fm.get("subdomain", ""),
        fm.get("sap_area", ""),
        fm.get("business_process", ""),
        fm.get("tags", []) or [],
    )[:40]


def build_permalink_map():
    """Build a map of permalink -> file info for the whole site."""
    all_pages = {}
    for root, dirs, files in os.walk(REPO_DIR):
        # Skip generated and dependency dirs
        dirs[:] = [d for d in dirs if d not in {
            "_site", ".git", "vendor", "node_modules", 
            "Kimi_Agent_SAP Atlas Expansion",
        } and not d.startswith("Basic_LinkedInDataExport_") and not d.startswith("Basic_LinkInDataExport_")]
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


def generate_compact_signal_index(atlas_files, check_mode=False):
    """Generate ai/atlas-compact-index.json for signal-to-page matching."""
    entries = []
    for rel_path in atlas_files:
        abs_path = REPO_DIR / rel_path
        fm, body = parse_frontmatter(abs_path)
        headings = extract_headings(body)
        entry = {
            "path": rel_path,
            "url": fm.get("permalink", ""),
            "title": fm.get("title", ""),
            "description": fm.get("description", ""),
            "atlas_section": fm.get("atlas_section", ""),
            "domain": fm.get("domain", ""),
            "subdomain": fm.get("subdomain", ""),
            "concept_type": fm.get("concept_type", ""),
            "sap_area": fm.get("sap_area", ""),
            "business_process": fm.get("business_process", ""),
            "status": fm.get("status", ""),
            "verified": bool(fm.get("verified", False)),
            "last_reviewed": serialize_value(fm.get("last_reviewed", "")),
            "tags": fm.get("tags", []) or [],
            "headings": headings,
            "sap_domain_keywords": _sap_domain_keywords(fm),
            "matching_terms": _matching_terms(fm, headings),
        }
        entries.append(entry)

    index = {
        "schema": "dkharlanau.atlas.compact_signal_index",
        "schema_version": "1.0",
        "generated_at": _now(check_mode),
        "canonical_url": "https://dkharlanau.github.io/ai/atlas-compact-index.json",
        "description": (
            "Compact public Atlas index for matching enriched professional "
            "signals to existing Atlas pages. Built from public frontmatter "
            "and headings only; no private notes, draft paths, or full body text."
        ),
        "source": "scripts/generate_atlas_artifacts.py",
        "count": len(entries),
        "entries": entries,
        "fallback": {
            "decision": "needs_research",
            "reason": (
                "If no candidate clears the matcher threshold, do not update "
                "or create a page automatically."
            ),
        },
    }

    if not check_mode:
        out_path = REPO_DIR / "ai" / "atlas-compact-index.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(index, f, indent=2, ensure_ascii=False, cls=DateTimeEncoder)

    return index


def _now(check_mode):
    """Return current timestamp or deterministic placeholder in check mode."""
    if check_mode:
        return CHECK_MODE_TIMESTAMP
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _derive_page_type(rel_path):
    """Derive a high-level page type from the source path."""
    parts = rel_path.split("/")
    if not parts:
        return "page"
    return parts[0]


def _derive_section(rel_path, fm):
    """Derive a section label from frontmatter or source path."""
    if fm.get("atlas_section"):
        return fm["atlas_section"]
    parts = rel_path.split("/")
    if len(parts) >= 2:
        return parts[1]
    return ""


def _is_indexable(fm):
    """Return True if frontmatter signals the page should be indexed."""
    robots = str(fm.get("robots", "")).lower()
    if "noindex" in robots:
        return False
    if fm.get("sitemap") is False:
        return False
    return True


def generate_verified_inventory(all_pages, check_mode=False):
    """Generate ai/verified-pages.json — site-wide verified, indexable pages.

    Includes any page with verified=true and status=reviewed that is not
    marked noindex or sitemap=false. Source file paths are excluded.
    """
    entries = []
    for permalink, info in all_pages.items():
        rel_path = info["file"]
        fm = info["fm"]

        # Skip template and excluded paths
        if rel_path.startswith("docs/templates/"):
            continue
        if not fm.get("verified"):
            continue
        if fm.get("status") != "reviewed":
            continue
        if not _is_indexable(fm):
            continue

        page_type = _derive_page_type(rel_path)
        section = _derive_section(rel_path, fm)

        entry = {
            "url": permalink,
            "title": fm.get("title", ""),
            "description": fm.get("description", ""),
            "type": page_type,
            "section": section,
            "status": fm.get("status", ""),
            "verified": bool(fm.get("verified")),
            "last_reviewed": serialize_value(fm.get("last_reviewed", "")),
            "last_modified_at": serialize_value(fm.get("last_modified_at", "")),
            "author": fm.get("author", ""),
            "tags": fm.get("tags", []) or [],
        }
        entries.append(entry)

    entries.sort(key=lambda e: (e["type"], e["section"], e["url"]))

    inventory = {
        "schema": "dkharlanau.site.verified_pages",
        "schema_version": "1.0",
        "generated_at": _now(check_mode),
        "canonical_url": "https://dkharlanau.github.io/ai/verified-pages.json",
        "description": (
            "Machine-readable inventory of all reviewed and verified indexable "
            "pages across the public site. Intended for AI agents and search "
            "crawlers that need to know which pages are trustworthy and "
            "retrieval-ready."
        ),
        "source": "scripts/generate_atlas_artifacts.py",
        "count": len(entries),
        "collections": sorted({e["type"] for e in entries}),
        "entries": entries,
    }

    if not check_mode:
        out_path = REPO_DIR / "ai" / "verified-pages.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(inventory, f, indent=2, ensure_ascii=False, cls=DateTimeEncoder)

    return inventory


def generate_manifest(all_pages, atlas_files, check_mode=False):
    """Generate atlas/manifest.json. Returns dict. Writes to disk unless check_mode."""
    entries = []
    for rel_path in atlas_files:
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
        "generated_at": _now(check_mode),
        "canonical_url": "https://dkharlanau.github.io/atlas/manifest.json",
        "count": len(entries),
        "verified_count": sum(1 for e in entries if e["verified"]),
        "unverified_count": sum(1 for e in entries if not e["verified"]),
        "sections": sorted({e["atlas_section"] for e in entries}),
        "entries": entries,
    }

    if not check_mode:
        out_path = REPO_DIR / "atlas" / "manifest.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False, cls=DateTimeEncoder)

    return manifest


def generate_llms_full(all_pages, atlas_files, check_mode=False):
    """Generate llms-full.txt with verified pages only. Returns text. Writes to disk unless check_mode."""
    lines = []
    lines.append("Atlas Full-Text Manifest")
    lines.append("=" * 50)
    lines.append(f"Generated: {_now(check_mode)}")
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
    for rel_path in atlas_files:
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
        lines.append("\n".join(line.rstrip() for line in clean_body.splitlines()))
        lines.append("")
        lines.append("=" * 50)
        lines.append("")

    lines.append(f"END OF MANIFEST — {verified_count} verified pages included")

    text = "\n".join(lines)

    if not check_mode:
        out_path = REPO_DIR / "llms-full.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)

    return text


def generate_related(all_pages, atlas_files, check_mode=False):
    """Generate ai/rag/related.json from frontmatter related links. Returns (edges, broken_links, dict). Writes to disk unless check_mode."""
    edges = []
    broken_links = []

    for rel_path in atlas_files:
        abs_path = REPO_DIR / rel_path
        fm, _ = parse_frontmatter(abs_path)
        permalink = fm.get("permalink", "")
        title = fm.get("title", "")
        section = fm.get("atlas_section", "")
        tags = fm.get("tags", []) or []
        related = fm.get("related", []) or []

        for link in related:
            target = all_pages.get(link)
            edge_base = {
                "source_url": permalink,
                "source_title": title,
                "source_section": section,
                "source_status": fm.get("status", ""),
                "source_verified": bool(fm.get("verified", False)),
                "source_tags": tags,
            }
            if target:
                edges.append({
                    **edge_base,
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
                        **edge_base,
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
        "generated_at": _now(check_mode),
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

    if not check_mode:
        out_dir = REPO_DIR / "ai" / "rag"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "related.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(related_json, f, indent=2, ensure_ascii=False, cls=DateTimeEncoder)

    return edges, broken_links, related_json


def _normalize_timestamp_in_json(text):
    """Replace generated_at timestamp with CHECK_MODE placeholder for comparison."""
    return re.sub(
        r'"generated_at":\s*"[^"]+"',
        f'"generated_at": "{CHECK_MODE_TIMESTAMP}"',
        text,
    )


def _normalize_timestamp_in_llms(text):
    """Replace Generated: timestamp with CHECK_MODE placeholder for comparison."""
    return re.sub(
        r'^Generated:\s*\S+',
        f'Generated: {CHECK_MODE_TIMESTAMP}',
        text,
        flags=re.MULTILINE,
    )


def _load_json_file(path):
    """Load and return JSON file contents as string."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _load_text_file(path):
    """Load and return text file contents as string."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def run_check(all_pages, atlas_files):
    """Validate existing artifacts against regenerated content. Returns list of issues."""
    issues = []

    # --- manifest.json ---
    print("\n[CHECK 1/6] manifest.json")
    manifest_generated = generate_manifest(all_pages, atlas_files, check_mode=True)
    manifest_path = REPO_DIR / "atlas" / "manifest.json"
    if not manifest_path.exists():
        issues.append("manifest.json: file missing")
    else:
        try:
            manifest_committed_text = _load_json_file(manifest_path)
            manifest_committed = json.loads(manifest_committed_text)
        except json.JSONDecodeError as e:
            issues.append(f"manifest.json: invalid JSON — {e}")
            manifest_committed = {}

        if manifest_committed:
            # Normalize timestamps
            gen_norm = json.loads(_normalize_timestamp_in_json(json.dumps(manifest_generated, indent=2, ensure_ascii=False, cls=DateTimeEncoder)))
            com_norm = json.loads(_normalize_timestamp_in_json(manifest_committed_text))
            if gen_norm != com_norm:
                issues.append("manifest.json: stale — committed file differs from source")
            else:
                print("  ✓ manifest.json is up to date")

        # Semantic checks — compare committed against generated expectations
        expected_count = manifest_generated.get("count")
        expected_verified = manifest_generated.get("verified_count")
        expected_unverified = manifest_generated.get("unverified_count")
        if manifest_committed.get("count") != expected_count:
            issues.append(f"manifest.json: expected {expected_count} entries, found {manifest_committed.get('count')}")
        if manifest_committed.get("verified_count") != expected_verified:
            issues.append(f"manifest.json: expected {expected_verified} verified, found {manifest_committed.get('verified_count')}")
        if manifest_committed.get("unverified_count") != expected_unverified:
            issues.append(f"manifest.json: expected {expected_unverified} unverified, found {manifest_committed.get('unverified_count')}")

    # --- llms-full.txt ---
    print("\n[CHECK 2/6] llms-full.txt")
    llms_generated = generate_llms_full(all_pages, atlas_files, check_mode=True)
    llms_path = REPO_DIR / "llms-full.txt"
    if not llms_path.exists():
        issues.append("llms-full.txt: file missing")
    else:
        llms_committed = _load_text_file(llms_path)
        gen_norm = _normalize_timestamp_in_llms(llms_generated)
        com_norm = _normalize_timestamp_in_llms(llms_committed)
        if gen_norm != com_norm:
            issues.append("llms-full.txt: stale — committed file differs from source")
        else:
            print("  ✓ llms-full.txt is up to date")

    # Semantic checks on committed file
    if llms_path.exists():
        # Verify only reviewed+verified pages included (exact line match)
        llms_pages = set(llms_committed.splitlines())
        for rel_path in atlas_files:
            abs_path = REPO_DIR / rel_path
            fm, _ = parse_frontmatter(abs_path)
            title = fm.get("title", "")
            page_line = f"PAGE: {title}"
            if fm.get("status") == "reviewed" and fm.get("verified"):
                if page_line not in llms_pages:
                    issues.append(f"llms-full.txt: missing verified page '{title}'")
            else:
                if page_line in llms_pages:
                    issues.append(f"llms-full.txt: unverified page '{title}' should not be included")

        # Private path leak check
        leak_patterns = ["source_files", "private-source", "kb-drafts", "/Users/", ".env"]
        for pattern in leak_patterns:
            if pattern in llms_committed:
                issues.append(f"llms-full.txt: private leak — contains '{pattern}'")

        # LinkedIn export name check
        if "Basic_LinkedInDataExport" in llms_committed or "Basic_LinkInDataExport" in llms_committed:
            issues.append("llms-full.txt: contains LinkedIn export reference")

    # --- related.json ---
    print("\n[CHECK 3/6] related.json")
    edges, broken_links, related_generated = generate_related(all_pages, atlas_files, check_mode=True)
    related_path = REPO_DIR / "ai" / "rag" / "related.json"
    if not related_path.exists():
        issues.append("related.json: file missing")
    else:
        try:
            related_committed_text = _load_json_file(related_path)
            related_committed = json.loads(related_committed_text)
        except json.JSONDecodeError as e:
            issues.append(f"related.json: invalid JSON — {e}")
            related_committed = {}

        if related_committed:
            gen_norm = json.loads(_normalize_timestamp_in_json(json.dumps(related_generated, indent=2, ensure_ascii=False, cls=DateTimeEncoder)))
            com_norm = json.loads(_normalize_timestamp_in_json(related_committed_text))
            if gen_norm != com_norm:
                issues.append("related.json: stale — committed file differs from source")
            else:
                print("  ✓ related.json is up to date")

        # Semantic checks — compare committed against generated expectations
        expected_edges = len(edges)
        if related_committed.get("count") != expected_edges:
            issues.append(f"related.json: expected {expected_edges} edges, found {related_committed.get('count')}")
        if related_committed.get("broken_link_count") != 0:
            issues.append(f"related.json: expected 0 broken links, found {related_committed.get('broken_link_count')}")
        if related_committed.get("warnings"):
            issues.append(f"related.json: warnings array not empty")

        # Private path leak check
        for pattern in leak_patterns:
            if pattern in related_committed_text:
                issues.append(f"related.json: private leak — contains '{pattern}'")

    # --- compact signal index ---
    print("\n[CHECK 4/6] atlas-compact-index.json")
    compact_generated = generate_compact_signal_index(atlas_files, check_mode=True)
    compact_path = REPO_DIR / "ai" / "atlas-compact-index.json"
    compact_committed = {}
    compact_committed_text = ""
    if not compact_path.exists():
        issues.append("atlas-compact-index.json: file missing")
    else:
        try:
            compact_committed_text = _load_json_file(compact_path)
            compact_committed = json.loads(compact_committed_text)
        except json.JSONDecodeError as e:
            issues.append(f"atlas-compact-index.json: invalid JSON — {e}")

        if compact_committed:
            gen_norm = json.loads(_normalize_timestamp_in_json(json.dumps(compact_generated, indent=2, ensure_ascii=False, cls=DateTimeEncoder)))
            com_norm = json.loads(_normalize_timestamp_in_json(compact_committed_text))
            if gen_norm != com_norm:
                issues.append("atlas-compact-index.json: stale — committed file differs from source")
            else:
                print("  ✓ atlas-compact-index.json is up to date")

        if compact_committed.get("count") != len(atlas_files):
            issues.append(f"atlas-compact-index.json: expected {len(atlas_files)} entries, found {compact_committed.get('count')}")
        for entry in compact_committed.get("entries", []):
            path = entry.get("path", "")
            if not path or not (REPO_DIR / path).exists():
                issues.append(f"atlas-compact-index.json: entry path missing: {path}")
            if not entry.get("url", "").startswith("/atlas/"):
                issues.append(f"atlas-compact-index.json: invalid Atlas URL for {path}")
            if not entry.get("matching_terms"):
                issues.append(f"atlas-compact-index.json: missing matching_terms for {path}")

        for pattern in leak_patterns:
            if pattern in compact_committed_text:
                issues.append(f"atlas-compact-index.json: private leak — contains '{pattern}'")

    # --- verified-pages.json ---
    print("\n[CHECK 5/7] verified-pages.json")
    inventory_generated = generate_verified_inventory(all_pages, check_mode=True)
    inventory_path = REPO_DIR / "ai" / "verified-pages.json"
    inventory_committed = {}
    inventory_committed_text = ""
    if not inventory_path.exists():
        issues.append("verified-pages.json: file missing")
    else:
        try:
            inventory_committed_text = _load_json_file(inventory_path)
            inventory_committed = json.loads(inventory_committed_text)
        except json.JSONDecodeError as e:
            issues.append(f"verified-pages.json: invalid JSON — {e}")

        if inventory_committed:
            gen_norm = json.loads(_normalize_timestamp_in_json(json.dumps(inventory_generated, indent=2, ensure_ascii=False, cls=DateTimeEncoder)))
            com_norm = json.loads(_normalize_timestamp_in_json(inventory_committed_text))
            if gen_norm != com_norm:
                issues.append("verified-pages.json: stale — committed file differs from source")
            else:
                print("  ✓ verified-pages.json is up to date")

        expected_inventory_count = len(inventory_generated.get("entries", []))
        if inventory_committed.get("count") != expected_inventory_count:
            issues.append(f"verified-pages.json: expected {expected_inventory_count} entries, found {inventory_committed.get('count')}")

        for entry in inventory_committed.get("entries", []):
            if not entry.get("url", "").startswith("/"):
                issues.append(f"verified-pages.json: invalid URL {entry.get('url')}")
            if not entry.get("title"):
                issues.append(f"verified-pages.json: missing title for {entry.get('url')}")
            if not entry.get("type"):
                issues.append(f"verified-pages.json: missing type for {entry.get('url')}")

        for pattern in leak_patterns:
            if pattern in inventory_committed_text:
                issues.append(f"verified-pages.json: private leak — contains '{pattern}'")

    # --- Cross-validate manifest vs related ---
    print("\n[CHECK 6/7] Cross-validation")
    if manifest_committed and related_committed:
        manifest_urls = {e["url"] for e in manifest_committed.get("entries", [])}
        related_sources = {e["source_url"] for e in related_committed.get("edges", [])}
        related_targets = {e["target_url"] for e in related_committed.get("edges", [])}
        # All related sources must be in manifest
        orphan_sources = related_sources - manifest_urls
        if orphan_sources:
            issues.append(f"related.json: sources not in manifest: {orphan_sources}")
        else:
            print("  ✓ All related sources present in manifest")

    # --- Frontmatter tag consistency ---
    print("\n[CHECK 7/7] Frontmatter tag consistency")
    tag_issues = []
    for rel_path in atlas_files:
        abs_path = REPO_DIR / rel_path
        fm, _ = parse_frontmatter(abs_path)
        tags = fm.get("tags", []) or []
        if not tags:
            tag_issues.append(f"{rel_path}: no tags")
        for tag in tags:
            if not re.match(r'^[a-z0-9-]+$', tag):
                tag_issues.append(f"{rel_path}: invalid tag '{tag}'")
    if tag_issues:
        issues.extend(tag_issues)
    else:
        print(f"  ✓ All {len(atlas_files)} articles have valid tags")

    return issues


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

    # Discover Atlas articles dynamically
    atlas_files = discover_atlas_articles()
    print(f"Atlas articles discovered: {len(atlas_files)}")

    if args.check:
        print("\n[CHECK MODE] Validating existing artifacts...")
        issues = run_check(all_pages, atlas_files)
        print("\n" + "=" * 40)
        if issues:
            print(f"CHECK FAILED — {len(issues)} issue(s):")
            for issue in issues:
                print(f"  ✗ {issue}")
            sys.exit(1)
        else:
            print("CHECK PASSED — all artifacts are up to date and valid.")
            sys.exit(0)

    # Generate manifest
    print("\n[1/5] Generating atlas/manifest.json ...")
    manifest = generate_manifest(all_pages, atlas_files)
    print(f"  Entries: {manifest['count']}")
    print(f"  Verified: {manifest['verified_count']}")
    print(f"  Unverified: {manifest['unverified_count']}")

    # Generate llms-full.txt
    print("\n[2/5] Generating llms-full.txt ...")
    verified_count = generate_llms_full(all_pages, atlas_files)
    print(f"  Verified pages included: {verified_count}")

    # Generate related.json
    print("\n[3/5] Generating ai/rag/related.json ...")
    edges, broken, _ = generate_related(all_pages, atlas_files)
    print(f"  Edges: {len(edges)}")
    print(f"  Broken links: {len(broken)}")
    if broken:
        for bl in broken:
            print(f"    BROKEN: {bl['source_url']} -> {bl['target_url']}")

    # Generate compact signal index
    print("\n[4/5] Generating ai/atlas-compact-index.json ...")
    compact_index = generate_compact_signal_index(atlas_files)
    print(f"  Entries: {compact_index['count']}")

    # Generate verified page inventory
    print("\n[5/5] Generating ai/verified-pages.json ...")
    inventory = generate_verified_inventory(all_pages)
    print(f"  Verified pages: {inventory['count']}")
    print(f"  Collections: {', '.join(inventory['collections'])}")

    print("\n" + "=" * 40)
    print("All artifacts generated successfully.")
    print("Run 'git diff' to review changes before committing.")


if __name__ == "__main__":
    main()
