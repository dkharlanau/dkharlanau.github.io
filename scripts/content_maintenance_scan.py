#!/usr/bin/env python3
"""
Content Maintenance Scanner for Atlas and Research pages.

Scans Atlas and Research markdown files, reads frontmatter, and generates:
  - data/content-maintenance/page-registry.json
  - data/content-maintenance/change-log.jsonl

Usage:
    python3 scripts/content_maintenance_scan.py
    python3 scripts/content_maintenance_scan.py --check

Requirements:
    PyYAML (pip install pyyaml)

Safety:
    - Never sets verified: true.
    - Never relaxes noindex/sitemap rules for research pages.
    - Never exposes private paths or private notes.
    - Preserves manual fields in the registry on regeneration.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import uuid
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


REPO_DIR = Path(__file__).resolve().parent.parent
ATLAS_DIR = REPO_DIR / "atlas"
RESEARCH_DIR = REPO_DIR / "research"
MAINTENANCE_DIR = REPO_DIR / "data" / "content-maintenance"
REGISTRY_PATH = MAINTENANCE_DIR / "page-registry.json"
CHANGELOG_PATH = MAINTENANCE_DIR / "change-log.jsonl"

# Staleness thresholds
FRESH_DAYS = 30
WATCH_DAYS = 90

WEAK_SOURCE_PATTERNS = [
    re.compile(r"\bweak[_\s]?signal\b", re.IGNORECASE),
    re.compile(r"\blow\s+confidence\b", re.IGNORECASE),
    re.compile(r"\baggregator\b", re.IGNORECASE),
    re.compile(r"\bmarket\s+report\b", re.IGNORECASE),
    re.compile(r"\bnewsletter\b", re.IGNORECASE),
    re.compile(r"\bfuture[-\s]?dated\b", re.IGNORECASE),
    re.compile(r"\bverify\s+against\s+official\s+docs\b", re.IGNORECASE),
    re.compile(r"\bunverified\b", re.IGNORECASE),
    re.compile(r"\bspeculation\b", re.IGNORECASE),
    re.compile(r"\brumor\b", re.IGNORECASE),
]


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
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


def parse_date(value: Any) -> date | None:
    """Parse a date from various frontmatter formats."""
    if value is None:
        return None
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, str):
        for fmt in ("%Y-%m-%d", "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S%z"):
            try:
                return datetime.strptime(value, fmt).date()
            except ValueError:
                continue
    return None


def detect_weak_sources(body: str) -> list[str]:
    """Scan page body for weak-source markers."""
    found: list[str] = []
    for pattern in WEAK_SOURCE_PATTERNS:
        if pattern.search(body):
            found.append(pattern.pattern)
    return found


def compute_staleness(last_date: date | None) -> tuple[str, str | None]:
    """Compute staleness status and reason."""
    if last_date is None:
        return "unknown", "No review date found"
    today = date.today()
    delta = (today - last_date).days
    if delta < 0:
        return "unknown", f"Date is in the future ({last_date.isoformat()})"
    if delta <= FRESH_DAYS:
        return "fresh", None
    if delta <= WATCH_DAYS:
        return "watch", f"Last reviewed {delta} days ago"
    return "stale", f"Last reviewed {delta} days ago"


def compute_source_confidence(fm: dict[str, Any], weak_sources: list[str]) -> str:
    """Compute source confidence from frontmatter and weak-source detection."""
    evidence_level = fm.get("evidence_level", "unknown")
    if weak_sources:
        if evidence_level in ("high", "medium"):
            return "mixed"
        return "low"
    if evidence_level in ("high", "medium", "low"):
        return evidence_level
    verified = fm.get("verified", False)
    if verified is True:
        return "high"
    status = fm.get("status", "")
    if status in ("reviewed", "published"):
        return "medium"
    if status in ("draft", "needs_verification", "skeleton"):
        return "unknown"
    return "unknown"


def compute_update_priority(
    staleness: str,
    weak_sources: list[str],
    safety_violations: list[str],
    fm: dict[str, Any],
) -> str:
    """Compute update priority."""
    if safety_violations:
        return "high"
    if staleness == "stale":
        return "high"
    if weak_sources:
        if staleness == "watch":
            return "high"
        return "medium"
    if staleness == "watch":
        return "medium"
    return "none"


def check_safety_violations(
    rel_path: str,
    fm: dict[str, Any],
    weak_sources: list[str],
    section: str,
) -> list[str]:
    """Check for safety violations."""
    violations: list[str] = []
    title = fm.get("title", "")
    robots = str(fm.get("robots", "")).lower()
    sitemap = fm.get("sitemap", True)
    verified = fm.get("verified", False)
    status = str(fm.get("status", "")).lower()

    if not title:
        violations.append("missing_title")

    if section == "research":
        if "noindex" not in robots:
            violations.append("research_missing_noindex")
        if sitemap is not False:
            violations.append("research_sitemap_not_false")

    if verified is True and weak_sources:
        violations.append("verified_with_weak_sources")

    if sitemap is True and (status in ("draft", "needs_verification", "skeleton") or verified is False):
        violations.append("sitemap_true_on_unverified")

    return violations


def build_registry_entry(
    rel_path: str,
    url: str,
    fm: dict[str, Any],
    body: str,
    section: str,
    existing: dict[str, Any] | None,
) -> dict[str, Any]:
    """Build a single registry entry."""
    title = fm.get("title", "")
    status = fm.get("status", "")
    verified = fm.get("verified", False)
    robots = str(fm.get("robots", ""))
    sitemap = fm.get("sitemap", True)

    last_reviewed = parse_date(fm.get("last_reviewed"))
    last_meaningful_update = parse_date(fm.get("updated")) or parse_date(fm.get("last_modified_at")) or parse_date(fm.get("date"))

    weak_sources = detect_weak_sources(body)
    safety_violations = check_safety_violations(rel_path, fm, weak_sources, section)
    staleness, staleness_reason = compute_staleness(last_reviewed or last_meaningful_update)
    source_confidence = compute_source_confidence(fm, weak_sources)
    update_priority = compute_update_priority(staleness, weak_sources, safety_violations, fm)

    # Preserve manual fields from existing registry if present
    safe_to_auto_update = False
    requires_human_review = True
    maintenance_notes = ""
    known_weak_sources: list[str] = []
    watch_terms: list[str] = []
    related_pages: list[str] = []

    if existing:
        safe_to_auto_update = existing.get("safe_to_auto_update", False)
        requires_human_review = existing.get("requires_human_review", True)
        maintenance_notes = existing.get("maintenance_notes", "")
        known_weak_sources = existing.get("known_weak_sources", [])
        watch_terms = existing.get("watch_terms", [])
        related_pages = existing.get("related_pages", [])

    # Merge detected weak sources with known ones
    all_weak = list(set(weak_sources + known_weak_sources))

    entry: dict[str, Any] = {
        "path": rel_path,
        "url": url,
        "title": title,
        "section": section,
        "status": status,
        "verified": verified,
        "robots": robots,
        "sitemap": sitemap,
        "last_reviewed": last_reviewed.isoformat() if last_reviewed else None,
        "last_meaningful_update": last_meaningful_update.isoformat() if last_meaningful_update else None,
        "source_confidence": source_confidence,
        "update_priority": update_priority,
        "staleness_status": staleness,
        "staleness_reason": staleness_reason,
        "maintenance_notes": maintenance_notes,
        "known_weak_sources": all_weak,
        "watch_terms": watch_terms,
        "related_pages": related_pages,
        "safe_to_auto_update": safe_to_auto_update,
        "requires_human_review": requires_human_review,
        "safety_violations": safety_violations,
    }

    return entry


def discover_pages() -> list[tuple[str, Path, str, str]]:
    """Discover all Atlas and Research markdown pages.

    Returns list of (rel_path, path, url, section).
    """
    pages: list[tuple[str, Path, str, str]] = []

    for md_path in sorted(ATLAS_DIR.rglob("*.md")):
        rel_path = md_path.relative_to(REPO_DIR).as_posix()
        fm, _ = parse_frontmatter(md_path)
        if not fm:
            continue
        permalink = fm.get("permalink", "")
        if not permalink:
            # Derive from path for index pages or fallback
            if rel_path.endswith(".md"):
                permalink = "/" + rel_path.replace(".md", "/")
        url = f"https://dkharlanau.github.io{permalink}"
        section = "atlas"
        # Sub-section classification
        if "atlas_section" in fm:
            sub = fm["atlas_section"]
            if sub in ("sap", "concepts", "diagnostics", "maps", "ai-operations", "automation", "data-quality"):
                section = f"atlas/{sub}"
        pages.append((rel_path, md_path, url, section))

    for md_path in sorted(RESEARCH_DIR.rglob("*.md")):
        rel_path = md_path.relative_to(REPO_DIR).as_posix()
        fm, _ = parse_frontmatter(md_path)
        if not fm:
            continue
        permalink = fm.get("permalink", "")
        if not permalink:
            if rel_path.endswith(".md"):
                permalink = "/" + rel_path.replace(".md", "/")
        url = f"https://dkharlanau.github.io{permalink}"
        section = "research"
        # Sub-section classification
        parent_dir = md_path.parent.name
        if parent_dir in ("briefs", "comparisons", "watchlists", "sources"):
            section = f"research/{parent_dir}"
        pages.append((rel_path, md_path, url, section))

    return pages


def load_existing_registry() -> dict[str, dict[str, Any]]:
    """Load existing registry as a dict keyed by path."""
    if not REGISTRY_PATH.exists():
        return {}
    try:
        with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        entries = data.get("pages", [])
        return {e["path"]: e for e in entries}
    except Exception as e:
        print(f"Warning: could not load existing registry: {e}", file=sys.stderr)
        return {}


def load_existing_changelog_event_ids() -> set[str]:
    """Load existing event IDs from change log."""
    if not CHANGELOG_PATH.exists():
        return set()
    event_ids: set[str] = set()
    try:
        with open(CHANGELOG_PATH, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    event = json.loads(line)
                    event_ids.add(event.get("event_id", ""))
                except json.JSONDecodeError:
                    continue
    except Exception as e:
        print(f"Warning: could not load existing changelog: {e}", file=sys.stderr)
    return event_ids


def generate_initial_changelog_events(
    pages: list[tuple[str, Path, str, str]],
    existing_event_ids: set[str],
) -> list[dict[str, Any]]:
    """Generate initial metadata_changed events for pages not yet in the log."""
    events: list[dict[str, Any]] = []
    now = datetime.now(timezone.utc).isoformat()
    for rel_path, _, _, section in pages:
        event_id = f"init-{rel_path.replace('/', '-')}"
        if event_id in existing_event_ids:
            continue
        events.append({
            "event_id": event_id,
            "timestamp": now,
            "actor": "script",
            "page_path": rel_path,
            "event_type": "metadata_changed",
            "summary": "Initial maintenance registry entry generated from current repository state",
            "reason": "Scanner bootstrap: no prior maintenance history exists for this page",
            "source_signal": "repository_scan",
            "confidence": "high",
            "files_changed": [rel_path],
            "validation": "frontmatter_parsed",
            "human_review_required": section.startswith("research"),
        })
    return events


def run_scan(check_mode: bool = False) -> int:
    """Run the maintenance scan. Returns exit code."""
    pages = discover_pages()
    existing_registry = load_existing_registry()
    existing_event_ids = load_existing_changelog_event_ids()

    registry_entries: list[dict[str, Any]] = []
    safety_violations_total = 0
    stale_count = 0
    watch_count = 0
    weak_source_count = 0
    high_priority_count = 0

    for rel_path, md_path, url, section in pages:
        fm, body = parse_frontmatter(md_path)
        existing = existing_registry.get(rel_path)
        entry = build_registry_entry(rel_path, url, fm, body, section, existing)
        registry_entries.append(entry)

        if entry["safety_violations"]:
            safety_violations_total += len(entry["safety_violations"])
        if entry["staleness_status"] == "stale":
            stale_count += 1
        if entry["staleness_status"] == "watch":
            watch_count += 1
        if entry["known_weak_sources"]:
            weak_source_count += 1
        if entry["update_priority"] == "high":
            high_priority_count += 1

    # Sort entries for stability
    registry_entries.sort(key=lambda e: e["path"])

    registry = {
        "schema": "dkharlanau.content_maintenance.page_registry",
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "count": len(registry_entries),
        "pages": registry_entries,
    }

    new_events = generate_initial_changelog_events(pages, existing_event_ids)

    if not check_mode:
        MAINTENANCE_DIR.mkdir(parents=True, exist_ok=True)
        with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
            json.dump(registry, f, indent=2, ensure_ascii=False)
            f.write("\n")

        with open(CHANGELOG_PATH, "a", encoding="utf-8") as f:
            for event in new_events:
                f.write(json.dumps(event, ensure_ascii=False) + "\n")

    # Print report
    print("=" * 60)
    print("Content Maintenance Scan Report")
    print("=" * 60)
    print(f"Total pages scanned:      {len(registry_entries)}")
    print(f"High priority updates:    {high_priority_count}")
    print(f"Stale pages:              {stale_count}")
    print(f"Watch pages:              {watch_count}")
    print(f"Weak-source pages:        {weak_source_count}")
    print(f"Safety violations:        {safety_violations_total}")
    print(f"New changelog events:     {len(new_events)}")
    print("-" * 60)

    if safety_violations_total > 0:
        print("SAFETY VIOLATIONS DETECTED:")
        for entry in registry_entries:
            if entry["safety_violations"]:
                print(f"  {entry['path']}: {', '.join(entry['safety_violations'])}")
        print("-" * 60)

    if check_mode:
        print("Check mode: no files written.")

    # Exit non-zero only for safety violations
    return 1 if safety_violations_total > 0 else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Run in check mode without writing files")
    args = parser.parse_args()
    return run_scan(check_mode=args.check)


if __name__ == "__main__":
    sys.exit(main())
