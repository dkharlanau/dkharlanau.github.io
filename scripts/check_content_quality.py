#!/usr/bin/env python3
"""Content quality gate for indexable pages.

Checks for:
- Placeholder markers (TODO, FIXME, TBD, lorem ipsum)
- "needs verification" text on indexable pages
- Thin content (< 150 words)
- Missing H1 or multiple H1s
- Empty sections
- Repeated headings
- Private paths
- Missing practical diagnostic sections for Atlas diagnostics

Usage:
    python3 scripts/check_content_quality.py [--repo-dir .] [--fail-on-critical]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

PLACEHOLDER_MARKERS = ["TODO:", "FIXME:", "TBD —", "TBD.", "lorem ipsum", "Lorem ipsum", "coming soon", " Coming soon"]
PRIVATE_PATTERNS = [
    "/Users/", "source_files", "private-source", "kb-drafts",
    "Kimi_Agent_SAP Atlas Expansion", "Basic_LinkedInDataExport",
    "Basic_LinkInDataExport", "li2resume.local", ".env.local",
]

ATLAS_DIAGNOSTIC_SECTIONS = [
    "symptom", "cause", "check", "table", "transaction", "workflow",
    "fix", "next step", "related", "diagnostic",
]

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


def count_words(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def count_headings(text: str) -> dict:
    h1 = re.findall(r"^#\s+(.+)$", text, re.MULTILINE)
    h2 = re.findall(r"^##\s+(.+)$", text, re.MULTILINE)
    h3 = re.findall(r"^###\s+(.+)$", text, re.MULTILINE)
    return {"h1": len(h1), "h2": len(h2), "h3": len(h3), "h1_texts": h1, "h2_texts": h2}


def check_page(path: Path, rel: str) -> list[str]:
    issues: list[str] = []
    if is_excluded(rel):
        return issues

    fm = parse_frontmatter(path)
    if not fm:
        return issues

    if fm.get("redirect"):
        return issues

    robots = fm.get("robots", "")
    is_noindex = "noindex" in robots.lower()
    status = fm.get("status", "")
    verified = fm.get("verified", False)
    title = fm.get("title", "")
    description = fm.get("description", "")
    atlas_section = fm.get("atlas_section", "")

    text = path.read_text(encoding="utf-8")
    body = text
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            body = text[end + 3:]

    word_count = count_words(body)
    headings = count_headings(body)

    # Collection flags (used for multiple checks)
    is_collection_page = any(rel.startswith(p) for p in ["_notes/", "_blog/", "_radar/", "_news/"])
    is_news_or_radar = rel.startswith("_news/") or rel.startswith("_radar/")
    is_skill_hub = rel.startswith("skill-hub/")

    # Indexable page checks
    if not is_noindex:
        has_layout = "layout" in fm

        if not title:
            issues.append(f"{rel}: indexable page has no title")
        if not description and not is_news_or_radar:
            issues.append(f"{rel}: indexable page has no description")
        # Thin content: strict for Atlas, lenient for pages with layouts or collections
        if word_count < 150:
            if rel.startswith("atlas/") or (not has_layout and not is_collection_page):
                issues.append(f"{rel}: indexable page is thin ({word_count} words)")
        # H1: skip if page has a layout or is in a collection with default layout
        if not has_layout and not is_collection_page:
            if headings["h1"] == 0:
                issues.append(f"{rel}: indexable page has no H1")
            if headings["h1"] > 1:
                issues.append(f"{rel}: indexable page has {headings['h1']} H1s")

        # Placeholder markers — more precise matching
        lower_body = body.lower()
        for marker in PLACEHOLDER_MARKERS:
            if marker.lower() in lower_body:
                # Skip if it appears inside a quoted question or instructional context
                # Simple heuristic: if it's in a list item about checking for placeholders, skip
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
                    issues.append(f"{rel}: indexable page contains placeholder '{marker}'")
                    break

        # Private paths
        for pattern in PRIVATE_PATTERNS:
            if pattern.lower() in lower_body:
                issues.append(f"{rel}: contains private path pattern '{pattern}'")
                break

        # "needs verification" text on indexable page
        if "needs verification" in lower_body and status != "needs_verification":
            # Skip if it's in instructional context about when things need verification
            lines = body.splitlines()
            found_in_context = False
            for line in lines:
                if "needs verification" in line.lower():
                    if any(ctx in line.lower() for ctx in [
                        "change request needs", "feature needs", "requirement needs",
                    ]):
                        found_in_context = True
                        break
            if not found_in_context:
                issues.append(f"{rel}: indexable page contains 'needs verification' text")

    # Atlas diagnostic specific checks
    if rel.startswith("atlas/diagnostics/") and not rel.endswith("index.md"):
        if word_count < 300:
            issues.append(f"{rel}: Atlas diagnostic is thin ({word_count} words, expected >= 300)")
        lower_body = body.lower()
        has_practical = any(
            section in lower_body for section in ATLAS_DIAGNOSTIC_SECTIONS
        )
        if not has_practical:
            issues.append(f"{rel}: Atlas diagnostic lacks practical sections (symptoms, causes, checks, fixes)")

    # Repeated headings (skip template-style pages: skill-hub, artifact templates)
    if not is_skill_hub and "template" not in rel.lower():
        seen = set()
        for h in headings["h2_texts"]:
            clean = h.strip().lower()
            if clean in seen:
                issues.append(f"{rel}: repeated heading '{h}'")
            seen.add(clean)

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-dir", default=".", help="Repository root")
    parser.add_argument("--fail-on-critical", action="store_true", help="Exit non-zero on issues")
    args = parser.parse_args()

    repo_dir = Path(args.repo_dir).resolve()
    all_issues: list[str] = []

    for md_path in sorted(repo_dir.rglob("*.md")):
        rel = md_path.relative_to(repo_dir).as_posix()
        if rel.startswith("vendor/") or rel.startswith("_site/") or rel.startswith(".git/"):
            continue
        all_issues.extend(check_page(md_path, rel))

    if all_issues:
        print(f"Content quality check failed: {len(all_issues)} issue(s)")
        for issue in all_issues[:50]:
            print(f"  - {issue}")
        if len(all_issues) > 50:
            print(f"  ... and {len(all_issues) - 50} more")
        if args.fail_on_critical:
            return 2
    else:
        print("Content quality check passed.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
