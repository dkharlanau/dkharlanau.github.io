#!/usr/bin/env python3
"""Audit generated HTML for indexability, metadata, and SEO quality.

Produces:
  - reports/seo/indexability-audit-YYYY-MM-DD.csv
  - reports/seo/indexability-audit-YYYY-MM-DD.md

Usage:
    python3 scripts/audit_indexability.py [--site-dir _site] [--fail-on-critical]
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

# --- Regex patterns ---------------------------------------------------------
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
META_DESC_RE = re.compile(
    r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
META_DESC_RE_ALT = re.compile(
    r'<meta[^>]+content=["\'](.*?)["\'][^>]+name=["\']description["\']',
    re.IGNORECASE | re.DOTALL,
)
ROBOTS_RE = re.compile(
    r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
CANONICAL_RE = re.compile(
    r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
OG_TITLE_RE = re.compile(
    r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
OG_DESC_RE = re.compile(
    r'<meta[^>]+property=["\']og:description["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
OG_IMAGE_RE = re.compile(
    r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
TWITTER_CARD_RE = re.compile(
    r'<meta[^>]+name=["\']twitter:card["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.IGNORECASE | re.DOTALL)
H2_RE = re.compile(r"<h2[^>]*>(.*?)</h2>", re.IGNORECASE | re.DOTALL)
IMG_RE = re.compile(r"<img[^>]*>", re.IGNORECASE | re.DOTALL)
IMG_ALT_RE = re.compile(r'alt=["\'](.*?)["\']', re.IGNORECASE | re.DOTALL)
IMG_SRC_RE = re.compile(r'src=["\'](.*?)["\']', re.IGNORECASE | re.DOTALL)
A_HREF_RE = re.compile(r'<a[^>]+href=["\'](.*?)["\'][^>]*>', re.IGNORECASE | re.DOTALL)
JSONLD_RE = re.compile(
    r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.IGNORECASE | re.DOTALL,
)
LINK_REL_RE = re.compile(
    r'<link[^>]+rel=["\']([^"\']*)["\'][^>]*>',
    re.IGNORECASE | re.DOTALL,
)

# --- Draft / private markers --------------------------------------------------
DRAFT_MARKERS = ["TODO", "FIXME", "TBD", "lorem ipsum", "lorem ipsum"]
PRIVATE_PATH_PATTERNS = [
    "/Users/", "source_files", "private-source", "kb-drafts", ".env",
    "Kimi_Agent_SAP Atlas Expansion", "Basic_LinkedInDataExport",
    "Basic_LinkInDataExport", "li2resume.local",
]


def pick(pattern: re.Pattern, text: str) -> str:
    match = pattern.search(text)
    if not match:
        return ""
    return html.unescape(match.group(1)).strip()


def pick_all(pattern: re.Pattern, text: str) -> list[str]:
    return [html.unescape(m.group(1)).strip() for m in pattern.finditer(text)]


def strip_html_tags(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text)


def word_count(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def load_sitemap_urls(site_dir: Path) -> set[str]:
    urls: set[str] = set()
    sitemap_files = sorted(site_dir.glob("sitemap*.xml"))
    for sitemap_path in sitemap_files:
        try:
            content = sitemap_path.read_text(encoding="utf-8")
            for loc in re.findall(r"<loc>(.*?)</loc>", content, re.IGNORECASE | re.DOTALL):
                urls.add(loc.strip())
        except Exception:
            continue
    return urls


def load_llms_full_pages(repo_dir: Path) -> set[str]:
    """Extract page URLs from llms-full.txt if present."""
    llms_path = repo_dir / "llms-full.txt"
    if not llms_path.exists():
        return set()
    urls: set[str] = set()
    try:
        text = llms_path.read_text(encoding="utf-8")
        for line in text.splitlines():
            if line.startswith("URL:"):
                urls.add(line.replace("URL:", "").strip())
    except Exception:
        pass
    return urls


def detect_jsonld_types(text: str) -> list[str]:
    types: list[str] = []
    for block in JSONLD_RE.findall(text):
        try:
            data = json.loads(block.strip())
            if isinstance(data, dict):
                t = data.get("@type", "")
                if isinstance(t, str):
                    types.append(t)
                elif isinstance(t, list):
                    types.extend(t)
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        t = item.get("@type", "")
                        if isinstance(t, str):
                            types.append(t)
                        elif isinstance(t, list):
                            types.extend(t)
        except json.JSONDecodeError:
            types.append("[invalid-json]")
    return types


def classify_page(row: dict) -> str:
    reasons: list[str] = []

    is_noindex = "noindex" in row["robots"].lower()
    is_unverified = row["source_verified"] == "false" or row["source_status"] != "reviewed"
    is_sitemap = row["sitemap_included"] == "yes"
    is_llms = row["llms_included"] == "yes"

    # Critical: sitemap/noindex conflict
    if is_sitemap and is_noindex:
        reasons.append("sitemap_noindex_conflict")

    # Critical: llms includes unverified
    if is_llms and is_unverified:
        reasons.append("unverified_but_indexable")

    # Critical: indexable but unverified
    if not is_noindex and is_unverified:
        reasons.append("unverified_but_indexable")

    # Missing title
    if not row["title"]:
        reasons.append("missing_title")

    # Missing description
    if not row["meta_description"]:
        reasons.append("missing_description")

    # Missing canonical
    if not row["canonical"]:
        reasons.append("missing_canonical")

    # Missing H1
    h1_count = int(row["h1_count"])
    if h1_count == 0:
        reasons.append("missing_h1")
    elif h1_count > 1:
        reasons.append("duplicate_h1")

    # Thin content
    if int(row["word_count"]) < 150 and not is_noindex:
        reasons.append("thin_content")

    # Missing OG
    if not row["og_title"] or not row["og_description"]:
        reasons.append("missing_og_metadata")

    # Broken links
    if int(row["broken_local_links"]) > 0:
        reasons.append("broken_local_links")

    # Image alt issues
    if int(row["images_missing_alt"]) > 0:
        reasons.append("image_alt_issues")

    # Schema missing
    if not row["jsonld_types"]:
        reasons.append("schema_missing_recommended")

    # Private paths
    body = row.get("_body", "")
    for pattern in PRIVATE_PATH_PATTERNS:
        if pattern.lower() in body.lower():
            reasons.append("private_paths_exposed")
            break

    # Draft markers
    lower_body = body.lower()
    for marker in DRAFT_MARKERS:
        if marker.lower() in lower_body:
            reasons.append("draft_markers")
            break

    if not reasons:
        if is_noindex:
            return "noindex_candidate"
        return "indexable_ok"

    return ", ".join(reasons)


def extract_source_frontmatter_info(source_path: Path) -> dict:
    """Try to read source .md file and extract frontmatter signals."""
    result = {
        "source_status": "",
        "source_verified": "",
        "source_robots": "",
        "source_sitemap": "",
    }
    if not source_path.exists():
        return result
    try:
        text = source_path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            return result
        end = text.find("---", 3)
        if end == -1:
            return result
        fm = text[3:end].strip()
        for line in fm.splitlines():
            if line.startswith("status:"):
                result["source_status"] = line.split(":", 1)[1].strip().strip('"').strip("'")
            elif line.startswith("verified:"):
                result["source_verified"] = line.split(":", 1)[1].strip().strip('"').strip("'")
            elif line.startswith("robots:"):
                result["source_robots"] = line.split(":", 1)[1].strip().strip('"').strip("'")
            elif line.startswith("sitemap:"):
                result["source_sitemap"] = line.split(":", 1)[1].strip().strip('"').strip("'")
    except Exception:
        pass
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", default="_site", help="Built site directory")
    parser.add_argument("--repo-dir", default=".", help="Repository root")
    parser.add_argument("--fail-on-critical", action="store_true", help="Exit non-zero on critical issues")
    args = parser.parse_args()

    site_dir = Path(args.site_dir).resolve()
    repo_dir = Path(args.repo_dir).resolve()
    if not site_dir.is_dir():
        print(f"Missing site directory: {site_dir}", file=sys.stderr)
        return 1

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    csv_path = repo_dir / "reports" / "seo" / f"indexability-audit-{today}.csv"
    md_path = repo_dir / "reports" / "seo" / f"indexability-audit-{today}.md"
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    sitemap_urls = load_sitemap_urls(site_dir)
    llms_urls = load_llms_full_pages(repo_dir)

    html_files = sorted(site_dir.rglob("*.html"))
    rows: list[dict] = []
    critical_issues: list[str] = []
    all_titles: dict[str, list[str]] = {}
    all_canonicals: dict[str, list[str]] = {}

    for file_path in html_files:
        rel = file_path.relative_to(site_dir).as_posix()
        try:
            content = file_path.read_text(encoding="utf-8", errors="ignore")
        except Exception as exc:
            print(f"Warning: cannot read {rel}: {exc}", file=sys.stderr)
            continue

        title = pick(TITLE_RE, content)
        meta_desc = pick(META_DESC_RE, content) or pick(META_DESC_RE_ALT, content)
        robots = pick(ROBOTS_RE, content)
        canonical = pick(CANONICAL_RE, content)
        og_title = pick(OG_TITLE_RE, content)
        og_desc = pick(OG_DESC_RE, content)
        og_image = pick(OG_IMAGE_RE, content)
        twitter_card = pick(TWITTER_CARD_RE, content)
        h1_list = pick_all(H1_RE, content)
        h2_list = pick_all(H2_RE, content)
        images = IMG_RE.findall(content)
        images_missing_alt = sum(1 for img in images if not IMG_ALT_RE.search(img))
        links = A_HREF_RE.findall(content)
        internal_links = 0
        external_links = 0
        broken_local = 0
        for link in links:
            parsed = urlparse(link)
            if parsed.scheme in ("http", "https", "mailto", "tel", "data", "javascript"):
                external_links += 1
            elif link.startswith("#"):
                continue
            else:
                internal_links += 1
                local_path = link.lstrip("/")
                if local_path:
                    target = site_dir / local_path
                    if target.is_dir():
                        target = target / "index.html"
                    elif not str(target).endswith(".html"):
                        target = target.with_suffix(".html")
                    if not target.exists():
                        broken_local += 1

        # JSON-LD
        jsonld_types = detect_jsonld_types(content)

        # URL reconstruction
        url = canonical
        if not url:
            url = f"https://dkharlanau.github.io/{rel.replace('index.html', '').replace('.html', '')}"

        # Source file guess
        source_rel = rel.replace("index.html", "index.md").replace(".html", ".md")
        source_path = repo_dir / source_rel
        fm_info = extract_source_frontmatter_info(source_path)

        sitemap_included = "yes" if url in sitemap_urls else "no"
        llms_included = "yes" if url in llms_urls else "no"

        # Track duplicates
        if title:
            all_titles.setdefault(title, []).append(rel)
        if canonical:
            all_canonicals.setdefault(canonical, []).append(rel)

        body_text = strip_html_tags(content)
        wc = word_count(body_text)

        row = {
            "source_path": source_rel if source_path.exists() else "",
            "output_path": rel,
            "url": url,
            "title": title,
            "title_length": len(title),
            "meta_description": meta_desc,
            "description_length": len(meta_desc),
            "canonical": canonical,
            "robots": robots,
            "h1_count": len(h1_list),
            "h1_text": " | ".join(h1_list)[:200],
            "h2_count": len(h2_list),
            "word_count": wc,
            "internal_links": internal_links,
            "external_links": external_links,
            "broken_local_links": broken_local,
            "image_count": len(images),
            "images_missing_alt": images_missing_alt,
            "jsonld_types": ", ".join(jsonld_types),
            "og_title": og_title,
            "og_description": og_desc,
            "og_image": og_image,
            "twitter_card": twitter_card,
            "sitemap_included": sitemap_included,
            "llms_included": llms_included,
            "source_status": fm_info["source_status"],
            "source_verified": fm_info["source_verified"],
            "source_robots": fm_info["source_robots"],
            "source_sitemap": fm_info["source_sitemap"],
            "_body": content,
        }
        row["classification"] = classify_page(row)
        rows.append(row)

    # Detect duplicates across pages
    for title, paths in all_titles.items():
        if len(paths) > 1:
            for row in rows:
                if row["title"] == title and row["classification"] == "indexable_ok":
                    row["classification"] = "duplicate_title"
                    critical_issues.append(f"Duplicate title '{title}' on {', '.join(paths)}")

    for canonical, paths in all_canonicals.items():
        if len(paths) > 1:
            for row in rows:
                if row["canonical"] == canonical and "duplicate_canonical" not in row["classification"]:
                    row["classification"] += ", duplicate_canonical" if row["classification"] != "indexable_ok" else "duplicate_canonical"
                    critical_issues.append(f"Duplicate canonical '{canonical}' on {', '.join(paths)}")

    # --- CSV output -----------------------------------------------------------
    fieldnames = [
        "output_path", "url", "title", "title_length", "meta_description",
        "description_length", "canonical", "robots", "h1_count", "h2_count",
        "word_count", "internal_links", "external_links", "broken_local_links",
        "image_count", "images_missing_alt", "jsonld_types", "og_title",
        "og_description", "og_image", "twitter_card", "sitemap_included",
        "llms_included", "source_status", "source_verified", "classification",
    ]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})

    # --- Markdown report ------------------------------------------------------
    md_lines = [
        f"# Indexability Audit Report",
        f"",
        f"**Date:** {today}",
        f"**Site directory:** `{site_dir}`",
        f"**Pages scanned:** {len(rows)}",
        f"",
        f"## Summary",
        f"",
    ]

    classifications: dict[str, int] = {}
    for row in rows:
        c = row["classification"]
        classifications[c] = classifications.get(c, 0) + 1

    for cls, count in sorted(classifications.items(), key=lambda x: -x[1]):
        md_lines.append(f"- **{cls}:** {count}")

    md_lines.extend([
        "",
        "## Critical Issues",
        "",
    ])
    if critical_issues:
        for issue in critical_issues:
            md_lines.append(f"- {issue}")
    else:
        md_lines.append("No critical issues detected.")

    md_lines.extend([
        "",
        "## Pages with Issues (indexable or flagged)",
        "",
        "| Path | Classification | Title | Description | Canonical | Robots | H1 | Words | Broken Links |",
        "|------|---------------|-------|-------------|-----------|--------|-----|-------|--------------|",
    ])

    for row in rows:
        if row["classification"] != "indexable_ok" or row["broken_local_links"] != "0":
            md_lines.append(
                f"| {row['output_path']} | {row['classification']} | {row['title'][:40]} | "
                f"{'yes' if row['meta_description'] else 'no'} | "
                f"{'yes' if row['canonical'] else 'no'} | {row['robots'][:20]} | "
                f"{row['h1_count']} | {row['word_count']} | {row['broken_local_links']} |"
            )

    md_lines.extend([
        "",
        "## Verified + Indexable Pages",
        "",
    ])
    for row in rows:
        if row["classification"] == "indexable_ok" and "noindex" not in row["robots"].lower():
            md_lines.append(f"- `{row['output_path']}` — {row['title']}")

    md_lines.extend([
        "",
        "## Noindex Pages",
        "",
    ])
    for row in rows:
        if "noindex" in row["robots"].lower():
            md_lines.append(f"- `{row['output_path']}` — {row['title']}")

    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    print(f"Audit complete: {len(rows)} pages scanned")
    print(f"  CSV: {csv_path}")
    print(f"  MD:  {md_path}")
    if critical_issues:
        print(f"  Critical issues: {len(critical_issues)}")
        for issue in critical_issues[:10]:
            print(f"    - {issue}")
        if len(critical_issues) > 10:
            print(f"    ... and {len(critical_issues) - 10} more")
        if args.fail_on_critical:
            return 2
    else:
        print("  No critical issues")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
