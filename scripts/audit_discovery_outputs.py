#!/usr/bin/env python3
"""Post-build discovery audit for _site output.

Validates sitemaps, robots.txt, llms files, and JSON-LD structured data
against the Search and AI Discovery Trust Contract.

Usage:
    python3 scripts/audit_discovery_outputs.py _site

Exit codes:
    0 — no blocking violations
    non-zero — safety or discovery violations found
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


BASE_URL = "https://dkharlanau.github.io"
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"

# Patterns that must never appear in sitemap URLs
PRIVATE_PATH_PATTERNS = [
    "/private/",
    "/draft/",
    "/admin/",
    "WorkOS_Vault",
    "/.git/",
    ".git/",
]

# Fake schema.org fields that are unsupported without visible source justification
FAKE_SCHEMA_FIELDS = [
    "aggregateRating",
    "review",
    "offers",
    "price",
    "ratingValue",
]

FRONT_MATTER_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
JSON_LD_RE = re.compile(
    r'<script\s+type=["\']application/ld\+json["\']\s*>(.*?)</script>',
    re.IGNORECASE | re.DOTALL,
)


def _warn(msg: str) -> None:
    print(f"  [WARN] {msg}")


def _violation(msg: str) -> None:
    print(f"  [VIOLATION] {msg}")


def _known(msg: str) -> None:
    print(f"  [KNOWN] {msg}")


def _new_violation(msg: str) -> None:
    print(f"  [NEW VIOLATION] {msg}")


def load_baseline(baseline_path: Path) -> list[dict]:
    """Load baseline entries from JSON file."""
    if not baseline_path.exists():
        return []
    try:
        data = json.loads(baseline_path.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return data
    except (json.JSONDecodeError, OSError):
        pass
    return []


def match_baseline(violation: str, baseline: list[dict]) -> dict | None:
    """Return matching baseline entry for a violation, or None."""
    for entry in baseline:
        pattern = entry.get("pattern", "")
        if pattern and pattern in violation:
            return entry
    return None


def _known(msg: str) -> None:
    print(f"  [KNOWN] {msg}")


def _new_violation(msg: str) -> None:
    print(f"  [NEW VIOLATION] {msg}")


def parse_simple_frontmatter(text: str) -> dict:
    """Extract scalar frontmatter fields without a YAML parser."""
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}
    fm_text = match.group(1)
    result: dict = {}
    for raw_line in fm_text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        # Keep first occurrence; lists are ignored for the fields we care about.
        if key not in result:
            result[key] = val
    return result


def build_source_url_map(source_root: Path) -> dict[str, dict]:
    """Map canonical URL path (e.g. /atlas/foo/) -> frontmatter dict."""
    url_map: dict[str, dict] = {}
    for md_path in source_root.rglob("*.md"):
        rel = md_path.relative_to(source_root).as_posix()
        # Skip generated / non-content directories
        if rel.startswith(("_site/", ".git/", "vendor/", "node_modules/")):
            continue
        text = md_path.read_text(encoding="utf-8")
        fm = parse_simple_frontmatter(text)
        permalink = fm.get("permalink", "")
        if not permalink:
            # Derive Jekyll default permalink from collection + slug when possible.
            # This is best-effort; explicit permalinks are preferred.
            if rel.startswith("_notes/"):
                slug = md_path.stem.replace("_", "-")
                permalink = f"/notes/{slug}/"
            elif rel.startswith("_blog/"):
                slug = md_path.stem.replace("_", "-")
                permalink = f"/blog/{slug}/"
            elif rel.startswith("_radar/"):
                slug = md_path.stem.replace("_", "-")
                permalink = f"/radar/{slug}/"
            elif rel.startswith("_news/"):
                slug = md_path.stem.replace("_", "-")
                permalink = f"/news/{slug}/"
            elif rel.startswith("atlas/") and md_path.name == "index.md":
                permalink = "/" + rel.replace("/index.md", "/")
            elif rel.startswith("atlas/"):
                slug = md_path.stem.replace("_", "-")
                section = rel.split("/")[1] if "/" in rel else ""
                permalink = f"/atlas/{section}/{slug}/"
            else:
                # Skip files we cannot map reliably
                continue
        url_map[permalink] = fm
    return url_map


def get_url_path(url: str) -> str:
    if url.startswith(BASE_URL):
        return url[len(BASE_URL):]
    return url


def is_noindex_page(fm: dict) -> bool:
    robots = str(fm.get("robots", "")).lower()
    return "noindex" in robots


def is_sitemap_false(fm: dict) -> bool:
    sitemap = fm.get("sitemap", "")
    # YAML false can be parsed as empty string by our simple parser,
    # but explicit "false" string is common in Jekyll frontmatter.
    return sitemap in ("false", "False", "FALSE", False, "no", "No")


def is_unverified_atlas(fm: dict) -> bool:
    verified = fm.get("verified", "")
    status = fm.get("status", "")
    # If either field is missing or not matching reviewed state, treat as unverified
    return not (str(verified).lower() == "true" and str(status).lower() == "reviewed")


def audit_sitemaps(site_root: Path, source_root: Path, violations: list, warnings: list) -> tuple[int, list[str]]:
    """Validate sitemap.xml and all referenced section sitemaps.

    Returns (url_count, list_of_sitemap_files_checked).
    """
    sitemap_index_path = site_root / "sitemap.xml"
    checked_files: list[str] = []
    total_urls = 0

    if not sitemap_index_path.exists():
        violations.append("sitemap.xml missing in _site")
        return 0, checked_files

    # Validate XML
    try:
        tree = ET.parse(sitemap_index_path)
    except ET.ParseError as e:
        violations.append(f"sitemap.xml is not valid XML: {e}")
        return 0, checked_files

    root = tree.getroot()
    if root.tag != f"{{{SITEMAP_NS}}}sitemapindex":
        violations.append("sitemap.xml root is not <sitemapindex>")

    # Build source URL map once
    url_map = build_source_url_map(source_root)

    # Discover referenced sitemaps
    referenced: list[str] = []
    for sitemap_elem in root.findall(f"{{{SITEMAP_NS}}}sitemap"):
        loc = sitemap_elem.find(f"{{{SITEMAP_NS}}}loc")
        if loc is not None and loc.text:
            referenced.append(loc.text)

    # Also check for ai/sitemap.xml which is deprecated and must NOT be referenced
    deprecated_ai_sitemap = f"{BASE_URL}/ai/sitemap.xml"
    if deprecated_ai_sitemap in referenced:
        violations.append("deprecated ai/sitemap.xml is referenced in sitemap index")

    # Validate each referenced sitemap exists and is valid XML
    section_sitemaps: list[Path] = []
    for ref_url in referenced:
        path_part = get_url_path(ref_url)
        file_path = site_root / path_part.lstrip("/")
        checked_files.append(str(file_path.relative_to(site_root)))
        if not file_path.exists():
            violations.append(f"sitemap index references missing file: {ref_url}")
            continue
        try:
            sub_tree = ET.parse(file_path)
        except ET.ParseError as e:
            violations.append(f"{path_part} is not valid XML: {e}")
            continue
        section_sitemaps.append(file_path)

    # Audit every URL in every section sitemap
    for sitemap_file in section_sitemaps:
        sub_tree = ET.parse(sitemap_file)
        sub_root = sub_tree.getroot()
        is_atlas_sitemap = sitemap_file.name == "sitemap-atlas.xml"

        for url_elem in sub_root.findall(f"{{{SITEMAP_NS}}}url"):
            loc = url_elem.find(f"{{{SITEMAP_NS}}}loc")
            if loc is None or not loc.text:
                warnings.append(f"{sitemap_file.name}: empty <loc> element")
                continue
            url = loc.text.strip()
            total_urls += 1

            # Canonical URL check
            if not url.startswith(f"{BASE_URL}/"):
                violations.append(f"non-canonical URL in {sitemap_file.name}: {url}")

            # Research exclusion
            if "/research/" in url:
                violations.append(f"research URL in {sitemap_file.name}: {url}")

            # Private path exclusion
            for pattern in PRIVATE_PATH_PATTERNS:
                if pattern in url:
                    violations.append(f"private path leak in {sitemap_file.name}: {url} (pattern: {pattern})")

            # Cross-reference with source frontmatter for deeper checks
            url_path = get_url_path(url)
            fm = url_map.get(url_path, {})
            if not fm:
                # Try without trailing slash for index pages
                fm = url_map.get(url_path.rstrip("/") + "/", {})
            if not fm:
                # Some URLs like /LLM.txt or /datasets/manifest.json don't have markdown sources
                # Only warn for HTML-like paths that we expect to map
                if url_path.endswith(("/", ".html")):
                    warnings.append(f"cannot map URL to source frontmatter: {url}")
                continue

            if is_noindex_page(fm):
                violations.append(f"noindex page in {sitemap_file.name}: {url}")

            if is_sitemap_false(fm):
                violations.append(f"sitemap:false page in {sitemap_file.name}: {url}")

            if is_atlas_sitemap:
                if "/atlas/" not in url_path:
                    violations.append(f"non-atlas URL in sitemap-atlas.xml: {url}")
                elif is_unverified_atlas(fm):
                    violations.append(f"unverified Atlas page in sitemap-atlas.xml: {url}")

    return total_urls, checked_files


def audit_robots_txt(site_root: Path, violations: list, warnings: list) -> dict:
    """Validate robots.txt policy and sitemap references."""
    robots_path = site_root / "robots.txt"
    if not robots_path.exists():
        violations.append("robots.txt missing in _site")
        return {}

    text = robots_path.read_text(encoding="utf-8")
    summary: dict = {}

    # Sitemap lines
    sitemap_lines = [line for line in text.splitlines() if line.strip().lower().startswith("sitemap:")]
    if not sitemap_lines:
        violations.append("robots.txt missing Sitemap: lines")
    else:
        for line in sitemap_lines:
            url = line.split(":", 1)[1].strip()
            if not url.startswith("https://dkharlanau.github.io/"):
                violations.append(f"robots.txt Sitemap line is not canonical: {url}")
        summary["sitemap_lines"] = len(sitemap_lines)

    # OAI-SearchBot Allow
    oai_match = re.search(
        r"User-agent:\s*OAI-SearchBot\s*\n(.*?)(?=\nUser-agent:|\Z)",
        text,
        re.IGNORECASE | re.DOTALL,
    )
    if not oai_match:
        violations.append("robots.txt missing OAI-SearchBot policy")
    else:
        block = oai_match.group(1)
        if "Allow: /" not in block:
            violations.append("robots.txt does not Allow: / for OAI-SearchBot")
        summary["oai_searchbot"] = "Allow"

    # GPTBot explicit policy
    gpt_match = re.search(
        r"User-agent:\s*GPTBot\s*\n(.*?)(?=\nUser-agent:|\Z)",
        text,
        re.IGNORECASE | re.DOTALL,
    )
    if not gpt_match:
        violations.append("robots.txt missing explicit GPTBot policy")
    else:
        block = gpt_match.group(1)
        if "Disallow: /" not in block:
            violations.append("robots.txt does not Disallow: / for GPTBot")
        summary["gptbot"] = "Disallow"

    # Content-Signal (informational)
    if "Content-Signal:" not in text:
        warnings.append("robots.txt missing Content-Signal header")

    return summary


def audit_llms_files(site_root: Path, violations: list, warnings: list) -> None:
    """Check llms.txt and llms-full.txt for private/noindex/research leaks."""
    for name in ("llms.txt", "llms-full.txt"):
        path = site_root / name
        if not path.exists():
            violations.append(f"{name} missing in _site")
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in PRIVATE_PATH_PATTERNS:
            if pattern in text:
                violations.append(f"{name} contains private path pattern: {pattern}")
        if "/research/" in text:
            violations.append(f"{name} contains research path: /research/")
        # Heuristic: noindex or draft markers
        if "noindex" in text.lower():
            warnings.append(f"{name} contains 'noindex' text — verify it is policy text, not a leaked page")
        if "draft" in text.lower():
            warnings.append(f"{name} contains 'draft' text — verify it is not leaked draft content")


def audit_json_ld(site_root: Path, violations: list, warnings: list) -> int:
    """Validate JSON-LD blocks in all built HTML files."""
    html_files = sorted(site_root.rglob("*.html"))
    blocks_checked = 0
    for file_path in html_files:
        content = file_path.read_text(encoding="utf-8", errors="ignore")
        blocks = JSON_LD_RE.findall(content)
        for block in blocks:
            blocks_checked += 1
            # Strip leading/trailing whitespace and newlines
            json_text = block.strip()
            if not json_text:
                warnings.append(f"{file_path.relative_to(site_root)}: empty JSON-LD block")
                continue
            try:
                data = json.loads(json_text)
            except json.JSONDecodeError as e:
                violations.append(
                    f"invalid JSON-LD in {file_path.relative_to(site_root)}: {e}"
                )
                continue

            # Check for unsupported fake schema fields
            json_str = json_text.lower()
            for field in FAKE_SCHEMA_FIELDS:
                if field.lower() in json_str:
                    violations.append(
                        f"unsupported fake field '{field}' in JSON-LD at {file_path.relative_to(site_root)}"
                    )
    return blocks_checked


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Audit built _site discovery outputs.")
    parser.add_argument("site_root", nargs="?", default="_site", help="Built site root")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail on ALL violations (default behavior)",
    )
    parser.add_argument(
        "--warn-only",
        action="store_true",
        help="Report violations but exit 0; separate known baseline violations from new ones",
    )
    parser.add_argument(
        "--baseline",
        type=str,
        default="data/seo/discovery-audit-baseline.json",
        help="Path to baseline JSON file (default: data/seo/discovery-audit-baseline.json)",
    )
    args = parser.parse_args(argv)

    site_root = Path(args.site_root).resolve()
    if not site_root.is_dir():
        print(f"ERROR: directory not found: {site_root}")
        return 2

    # Source root is the parent of _site (repo root)
    source_root = site_root.parent

    violations: list[str] = []
    warnings: list[str] = []

    print("=" * 60)
    print("Discovery Output Audit")
    print(f"Site root: {site_root}")
    if args.warn_only:
        print("Mode: WARN-ONLY (violations reported but will not block)")
    elif args.strict:
        print("Mode: STRICT (all violations are blocking)")
    print("=" * 60)

    # 1. Sitemaps
    print("\n[1] Sitemap audit")
    url_count, sitemap_files = audit_sitemaps(site_root, source_root, violations, warnings)
    print(f"  Sitemap files checked: {len(sitemap_files)}")
    for sf in sitemap_files:
        print(f"    - {sf}")
    print(f"  Total sitemap URLs: {url_count}")

    # 2. robots.txt
    print("\n[2] robots.txt audit")
    robots_summary = audit_robots_txt(site_root, violations, warnings)
    for k, v in robots_summary.items():
        print(f"  {k}: {v}")

    # 3. LLMs files
    print("\n[3] LLMs files audit")
    audit_llms_files(site_root, violations, warnings)

    # 4. JSON-LD
    print("\n[4] JSON-LD structured data audit")
    json_ld_count = audit_json_ld(site_root, violations, warnings)
    print(f"  JSON-LD blocks checked: {json_ld_count}")

    # Load baseline and classify violations
    baseline_path = source_root / args.baseline
    baseline = load_baseline(baseline_path)
    known: list[tuple[str, dict]] = []
    new_violations: list[str] = []
    for v in violations:
        entry = match_baseline(v, baseline)
        if entry:
            known.append((v, entry))
        else:
            new_violations.append(v)

    # Summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"  Warnings:           {len(warnings)}")
    print(f"  Total violations:     {len(violations)}")
    if baseline:
        print(f"  Known/baselined:      {len(known)}")
        print(f"  New violations:       {len(new_violations)}")

    if warnings:
        print("\n  Warnings:")
        for w in warnings:
            _warn(w)

    if known:
        print("\n  Known violations (baselined):")
        for v, entry in known:
            _known(f"[{entry.get('id', 'unknown')}] {v}")

    if new_violations:
        print("\n  New violations:")
        for v in new_violations:
            _new_violation(v)

    # Determine exit behavior
    if args.warn_only:
        # In warn-only mode, we exit 0 even if there are violations,
        # but we still fail if there are NEW violations that are not baselined.
        if new_violations:
            print(f"\nAudit found {len(new_violations)} NEW violation(s) not in baseline.")
            return 1
        if violations:
            print(f"\nAudit found {len(violations)} known violation(s) — all baselined. Exiting 0.")
        else:
            print("\nAudit PASSED — no violations.")
        return 0

    # Strict / default mode: any violation is blocking
    if violations:
        print(f"\nAudit FAILED with {len(violations)} violation(s).")
        return 1

    print("\nAudit PASSED — no blocking violations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
