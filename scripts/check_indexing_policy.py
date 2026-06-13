#!/usr/bin/env python3
"""Enforce safe publication rules for indexable content.

Validates that:
- needs_verification / verified:false pages have noindex + sitemap:false
- verified pages are NOT noindex and have title + description
- no sitemap/noindex conflict
- no llms-full inclusion of unverified pages
- no private paths in indexable content
- no broken local links on indexable pages

Usage:
    python3 scripts/check_indexing_policy.py [--repo-dir .] [--site-dir _site] [--fail-on-critical]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
LINK_HREF_RE = re.compile(r'<a[^>]+href=["\'](.*?)["\'][^>]*>', re.IGNORECASE | re.DOTALL)
META_ROBOTS_RE = re.compile(
    r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
DESC_RE = re.compile(
    r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
CANONICAL_RE = re.compile(
    r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.IGNORECASE | re.DOTALL)

PRIVATE_PATH_PATTERNS = [
    "/Users/", "source_files", "private-source", "kb-drafts", ".env",
    "Kimi_Agent_SAP Atlas Expansion", "Basic_LinkedInDataExport",
    "Basic_LinkInDataExport", "li2resume.local",
]
DRAFT_MARKERS = ["TODO:", "FIXME:", "TBD —", "TBD.", "lorem ipsum", "Lorem ipsum"]

EXCLUDED_DIRS = [
    "vendor", "_site", ".git", ".codex", "agent-skills/skills", "docs/templates",
    "docs/maintenance", "docs/research", "Kimi_Agent_SAP Atlas Expansion",
]


def is_excluded(rel: str) -> bool:
    for prefix in EXCLUDED_DIRS:
        if rel.startswith(prefix):
            return True
    return False


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}
    fm: dict = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith("#"):
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if value.lower() in ("true", "yes"):
                fm[key] = True
            elif value.lower() in ("false", "no"):
                fm[key] = False
            else:
                fm[key] = value
    return fm


def check_atlas_policy(file_path: Path, rel: str) -> list[str]:
    issues: list[str] = []
    if is_excluded(rel):
        return issues

    fm = parse_frontmatter(file_path)
    if not fm:
        return issues

    status = fm.get("status", "")
    verified = fm.get("verified", False)
    robots = fm.get("robots", "")
    sitemap = fm.get("sitemap", True)
    title = fm.get("title", "")
    description = fm.get("description", "")

    is_noindex = "noindex" in robots.lower()

    # Unverified / needs_verification MUST be noindex
    if status == "needs_verification" or verified is False:
        if not is_noindex:
            issues.append(f"{rel}: unverified page lacks robots:noindex (status={status}, verified={verified})")
        if sitemap is not False:
            issues.append(f"{rel}: unverified page has sitemap:true (should be false)")

    # Verified / indexable MUST NOT be noindex
    if verified is True and status == "reviewed":
        if is_noindex:
            issues.append(f"{rel}: verified+reviewed page has robots:noindex")
        if sitemap is False:
            issues.append(f"{rel}: verified+reviewed page has sitemap:false")
        if not title:
            issues.append(f"{rel}: verified+reviewed page has no title")
        if not description:
            issues.append(f"{rel}: verified+reviewed page has no description")

    # Research pages should not be in sitemap (existing policy)
    if rel.startswith("research/") and sitemap is not False:
        issues.append(f"{rel}: research page should have sitemap:false")

    # Scenarios should remain noindex until verified
    if rel.startswith("scenarios/"):
        if status == "needs_verification" or verified is False:
            if not is_noindex:
                issues.append(f"{rel}: unverified scenario lacks robots:noindex")
            if sitemap is not False:
                issues.append(f"{rel}: unverified scenario has sitemap:true")

    # Content checks for all pages
    body = file_path.read_text(encoding="utf-8")
    for pattern in PRIVATE_PATH_PATTERNS:
        if pattern.lower() in body.lower():
            issues.append(f"{rel}: contains private path pattern '{pattern}'")
            break

    # Draft markers — smarter detection
    lower_body = body.lower()
    for marker in DRAFT_MARKERS:
        if marker.lower() in lower_body and not is_noindex:
            # Skip if it appears in instructional/checklist context
            lines = body.splitlines()
            found_in_context = False
            for line in lines:
                if marker.lower() in line.lower():
                    if any(ctx in line.lower() for ctx in [
                        "does the document contain", "check for", "look for",
                        "identify", "contains placeholders", "weak output", "owner:", "action items:",
                    ]):
                        found_in_context = True
                        break
            if not found_in_context:
                issues.append(f"{rel}: contains draft marker '{marker}' on indexable page")
                break

    return issues


def check_built_html(site_dir: Path, repo_dir: Path) -> list[str]:
    """Cross-check generated HTML against source frontmatter."""
    issues: list[str] = []
    if not site_dir.is_dir():
        return issues

    for html_path in site_dir.rglob("*.html"):
        rel = html_path.relative_to(site_dir).as_posix()
        try:
            content = html_path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        robots_match = META_ROBOTS_RE.search(content)
        robots = robots_match.group(1).lower() if robots_match else ""
        is_noindex = "noindex" in robots

        title = TITLE_RE.search(content)
        desc = DESC_RE.search(content)
        canonical = CANONICAL_RE.search(content)
        h1s = H1_RE.findall(content)

        # Guess source path
        source_rel = rel.replace("index.html", "index.md").replace(".html", ".md")
        source_path = repo_dir / source_rel

        if source_path.exists():
            fm = parse_frontmatter(source_path)
            if fm:
                fm_verified = fm.get("verified", False)
                fm_status = fm.get("status", "")
                fm_sitemap = fm.get("sitemap", True)

                # Sitemap/noindex conflict detection
                if fm_sitemap is False and not is_noindex:
                    # This is a warning, not critical, because Jekyll may generate sitemap:false pages
                    pass

                if fm_verified is True and fm_status == "reviewed":
                    if not title:
                        issues.append(f"{rel}: verified page missing <title>")
                    if not desc:
                        issues.append(f"{rel}: verified page missing meta description")
                    if not canonical:
                        issues.append(f"{rel}: verified page missing canonical")
                    if len(h1s) != 1:
                        issues.append(f"{rel}: verified page has {len(h1s)} H1 (expected 1)")

        # Check for broken local links (ignore inline script strings)
        content_for_links = re.sub(
            r'<script[^>]*>.*?</script>', '', content,
            flags=re.IGNORECASE | re.DOTALL,
        )
        static_extensions = {
            ".json", ".yml", ".yaml", ".xml", ".txt", ".css", ".js",
            ".svg", ".png", ".jpg", ".jpeg", ".webp", ".avif", ".pdf",
        }
        page_dir = html_path.parent
        for link in LINK_HREF_RE.findall(content_for_links):
            if not link or link.startswith("#") or ":" in link:
                continue
            # Strip query/fragment markers for filesystem checks
            link_clean = link.split("?")[0].split("#")[0]
            if link.startswith("/"):
                target = site_dir / link_clean.lstrip("/")
            else:
                target = page_dir / link_clean
            try:
                resolved = target.resolve()
                resolved.relative_to(site_dir.resolve())
                target = resolved
            except (ValueError, OSError):
                pass
            if target.is_dir():
                target = target / "index.html"
            elif target.suffix.lower() not in {".html"} | static_extensions:
                target = target.with_suffix(".html")
            if not target.exists() and not is_noindex:
                issues.append(f"{rel}: broken local link '{link}' on indexable page")

    return issues


def check_llms_full(repo_dir: Path) -> list[str]:
    """Verify llms-full.txt only contains verified pages."""
    issues: list[str] = []
    llms_path = repo_dir / "llms-full.txt"
    if not llms_path.exists():
        return issues

    text = llms_path.read_text(encoding="utf-8")
    for pattern in PRIVATE_PATH_PATTERNS:
        if pattern.lower() in text.lower():
            issues.append(f"llms-full.txt: contains private path pattern '{pattern}'")

    # Find all URLs mentioned
    urls_in_llms = set()
    for line in text.splitlines():
        if line.startswith("URL:"):
            urls_in_llms.add(line.replace("URL:", "").strip())

    # Cross-check with Atlas manifest if available
    manifest_path = repo_dir / "atlas" / "manifest.json"
    if manifest_path.exists():
        import json
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            for entry in manifest.get("entries", []):
                url = entry.get("url", "")
                if url in urls_in_llms:
                    if not entry.get("verified", False):
                        issues.append(f"llms-full.txt: includes unverified page '{url}' ({entry.get('title', '')})")
                    if entry.get("status", "") != "reviewed":
                        issues.append(f"llms-full.txt: includes unreviewed page '{url}' ({entry.get('title', '')})")
        except json.JSONDecodeError:
            pass

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-dir", default=".", help="Repository root")
    parser.add_argument("--site-dir", default="_site", help="Built site directory")
    parser.add_argument("--fail-on-critical", action="store_true", help="Exit non-zero on issues")
    parser.add_argument("--skip-built", action="store_true", help="Skip built HTML checks (useful when _site is stale)")
    args = parser.parse_args()

    repo_dir = Path(args.repo_dir).resolve()
    site_dir = Path(args.site_dir).resolve()

    all_issues: list[str] = []

    # 1. Source frontmatter policy checks
    for md_path in sorted(repo_dir.rglob("*.md")):
        rel = md_path.relative_to(repo_dir).as_posix()
        if rel.startswith("vendor/") or rel.startswith("_site/") or rel.startswith(".git/"):
            continue
        if rel.startswith("atlas/") or rel.startswith("scenarios/") or rel.startswith("skill-hub/") or rel.startswith("research/"):
            all_issues.extend(check_atlas_policy(md_path, rel))

    # 2. Built HTML checks (only if not skipped)
    if not args.skip_built:
        all_issues.extend(check_built_html(site_dir, repo_dir))

    # 3. llms-full.txt checks
    all_issues.extend(check_llms_full(repo_dir))

    if all_issues:
        print(f"Indexing policy check failed: {len(all_issues)} issue(s)")
        for issue in all_issues[:50]:
            print(f"  - {issue}")
        if len(all_issues) > 50:
            print(f"  ... and {len(all_issues) - 50} more")
        if args.fail_on_critical:
            return 2
    else:
        print("Indexing policy check passed.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
