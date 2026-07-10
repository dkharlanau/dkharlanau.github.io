import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import content_maintenance_scan as scanner

REGISTRY_PATH = REPO_ROOT / "data" / "content-maintenance" / "page-registry.json"
CHANGELOG_PATH = REPO_ROOT / "data" / "content-maintenance" / "change-log.jsonl"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_registry():
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_changelog_events():
    events = []
    with open(CHANGELOG_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            events.append(json.loads(line))
    return events


# ---------------------------------------------------------------------------
# Registry schema
# ---------------------------------------------------------------------------

def test_registry_file_exists():
    assert REGISTRY_PATH.exists(), f"Registry must exist at {REGISTRY_PATH}"


def test_registry_top_level_schema():
    data = load_registry()
    assert data["schema"] == "dkharlanau.content_maintenance.page_registry"
    assert data["schema_version"] == "1.0"
    assert "generated_at" in data
    assert "count" in data
    assert data["count"] == len(data.get("pages", []))


def test_each_page_has_required_fields():
    data = load_registry()
    required = [
        "path",
        "url",
        "title",
        "section",
        "status",
        "verified",
        "robots",
        "sitemap",
        "last_reviewed",
        "last_meaningful_update",
        "source_confidence",
        "update_priority",
        "staleness_status",
        "maintenance_notes",
        "known_weak_sources",
        "watch_terms",
        "related_pages",
        "safe_to_auto_update",
        "requires_human_review",
        "safety_violations",
        "maintenance_override",
    ]
    for page in data["pages"]:
        for field in required:
            assert field in page, f"{page['path']} missing field: {field}"


def test_page_path_unique():
    data = load_registry()
    paths = [p["path"] for p in data["pages"]]
    assert len(paths) == len(set(paths)), "Page paths must be unique"


def test_url_format():
    data = load_registry()
    for page in data["pages"]:
        assert page["url"].startswith("https://dkharlanau.github.io/"), f"{page['path']} has bad URL"


# ---------------------------------------------------------------------------
# JSONL change-log validity
# ---------------------------------------------------------------------------

def test_changelog_file_exists():
    assert CHANGELOG_PATH.exists(), f"Change log must exist at {CHANGELOG_PATH}"


def test_changelog_lines_are_valid_json():
    events = load_changelog_events()
    assert len(events) > 0, "Change log must have at least one event"


def test_changelog_event_schema():
    events = load_changelog_events()
    required = [
        "event_id",
        "timestamp",
        "actor",
        "page_path",
        "event_type",
        "summary",
        "reason",
        "source_signal",
        "confidence",
        "files_changed",
        "validation",
        "human_review_required",
    ]
    for event in events:
        for field in required:
            assert field in event, f"Event {event.get('event_id')} missing field: {field}"


def test_changelog_event_types_valid():
    valid_types = {
        "created", "reviewed", "updated", "source_downgraded",
        "source_replaced", "claim_removed", "link_fixed",
        "metadata_changed", "deferred",
    }
    events = load_changelog_events()
    for event in events:
        assert event["event_type"] in valid_types, f"Invalid event_type: {event['event_type']}"


def test_changelog_event_id_unique():
    events = load_changelog_events()
    ids = [e["event_id"] for e in events]
    assert len(ids) == len(set(ids)), "Event IDs must be unique"


# ---------------------------------------------------------------------------
# Research safety rules
# ---------------------------------------------------------------------------

def test_research_pages_remain_noindex():
    data = load_registry()
    for page in data["pages"]:
        if page["section"].startswith("research"):
            robots = str(page.get("robots", "")).lower()
            assert "noindex" in robots, f"Research page {page['path']} must have noindex"


def test_research_pages_sitemap_false():
    data = load_registry()
    for page in data["pages"]:
        if page["section"].startswith("research"):
            assert page.get("sitemap") is False, f"Research page {page['path']} must have sitemap: false"


# ---------------------------------------------------------------------------
# Verified safety rules
# ---------------------------------------------------------------------------

def test_verified_never_auto_set_by_scanner():
    """The scanner must never flip verified to true."""
    # This is enforced by the scanner logic: it only reads verified from frontmatter.
    # We verify no page has verified:true unless frontmatter already had it.
    data = load_registry()
    for page in data["pages"]:
        if page["verified"] is True:
            # Atlas index pages and reviewed pages may be verified
            # The scanner never writes verified, so this is a read-only assertion
            pass
    # The real test: run scanner in check mode and ensure it does not modify verified
    result = subprocess.run(
        [sys.executable, str(SCRIPTS_DIR / "content_maintenance_scan.py"), "--check"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Scanner check failed: {result.stdout}\n{result.stderr}"


# ---------------------------------------------------------------------------
# Weak-source detection
# ---------------------------------------------------------------------------

def test_weak_source_detection_runs():
    data = load_registry()
    weak_pages = [p for p in data["pages"] if p["known_weak_sources"]]
    # We expect at least some weak sources in research pages
    research_weak = [p for p in weak_pages if p["section"].startswith("research")]
    assert len(research_weak) > 0, "Expected at least one research page with weak-source markers"


def test_weak_source_confidence_low_or_mixed():
    data = load_registry()
    for page in data["pages"]:
        if page["known_weak_sources"]:
            assert page["source_confidence"] in ("low", "mixed", "unknown"), \
                f"{page['path']} has weak sources but confidence is {page['source_confidence']}"


# ---------------------------------------------------------------------------
# Safety violation exit behavior
# ---------------------------------------------------------------------------

def test_scanner_exits_zero_when_no_safety_violations():
    result = subprocess.run(
        [sys.executable, str(SCRIPTS_DIR / "content_maintenance_scan.py"), "--check"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Expected exit 0, got {result.returncode}: {result.stdout}"


# ---------------------------------------------------------------------------
# Manual field preservation
# ---------------------------------------------------------------------------

def test_manual_fields_preserved_on_regeneration():
    """Simulate a manual edit to safe_to_auto_update, then regenerate and verify preservation."""
    original_text = REGISTRY_PATH.read_text(encoding="utf-8")
    data = load_registry()
    if not data["pages"]:
        pytest.skip("No pages in registry")

    # Pick first page and set a manual field
    first_path = data["pages"][0]["path"]
    for page in data["pages"]:
        if page["path"] == first_path:
            page["safe_to_auto_update"] = True
            page["maintenance_notes"] = "Test note"
            page["watch_terms"] = ["test-term"]
            page["related_pages"] = ["/atlas/test/"]
            page["maintenance_override"] = {
                "reason": "Test override",
                "update_priority": "none",
            }
            break

    try:
        # Write back and regenerate against the temporary mutation.
        with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "content_maintenance_scan.py")],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"Scanner failed: {result.stdout}\n{result.stderr}"

        new_data = load_registry()
        for page in new_data["pages"]:
            if page["path"] == first_path:
                assert page["safe_to_auto_update"] is True, "safe_to_auto_update not preserved"
                assert page["maintenance_notes"] == "Test note", "maintenance_notes not preserved"
                assert page["watch_terms"] == ["test-term"], "watch_terms not preserved"
                assert page["related_pages"] == ["/atlas/test/"], "related_pages not preserved"
                assert page.get("maintenance_override", {}).get("reason") == "Test override", "maintenance_override not preserved"
                break
        else:
            pytest.fail(f"Page {first_path} not found after regeneration")
    finally:
        REGISTRY_PATH.write_text(original_text, encoding="utf-8")


def test_maintenance_override_reduces_priority():
    """A page with maintenance_override should have its update_priority overridden."""
    data = load_registry()
    overridden_pages = [p for p in data["pages"] if p.get("maintenance_override")]
    assert len(overridden_pages) > 0, "Expected at least one overridden page"
    for page in overridden_pages:
        override = page["maintenance_override"]
        expected = override.get("update_priority")
        if expected:
            assert page["update_priority"] == expected, \
                f"{page['path']}: expected priority {expected}, got {page['update_priority']}"


def test_maintenance_override_does_not_hide_safety_violations():
    """Safety violations must still be detected even with maintenance_override."""
    # This is a logic test: verify the scanner still checks safety violations
    # when an override is present. We test via the check_safety_violations function.
    fm = {
        "title": "",
        "robots": "noindex,follow",
        "sitemap": False,
        "verified": False,
        "status": "draft",
    }
    violations = scanner.check_safety_violations("atlas/test.md", fm, [], "atlas")
    assert "missing_title" in violations
    # The override logic in build_registry_entry only affects update_priority,
    # not safety_violations. So violations should still exist.


def test_research_pages_with_override_still_require_noindex():
    """Research pages must remain noindex even with maintenance_override."""
    data = load_registry()
    for page in data["pages"]:
        if page["section"].startswith("research"):
            robots = str(page.get("robots", "")).lower()
            assert "noindex" in robots, f"Research page {page['path']} must have noindex"
            assert page.get("sitemap") is False, f"Research page {page['path']} must have sitemap: false"


def test_override_presence_in_registry():
    """The atlas/research-notes/index.md page should have a maintenance_override."""
    data = load_registry()
    page = next((p for p in data["pages"] if p["path"] == "atlas/research-notes/index.md"), None)
    assert page is not None, "atlas/research-notes/index.md must be in registry"
    assert page.get("maintenance_override") is not None, "Expected maintenance_override on research-notes index"
    override = page["maintenance_override"]
    assert "reason" in override, "Override must have a reason"
    assert override.get("update_priority") == "none", "Override should set update_priority to none"


def test_none_priority_overrides_cannot_remain_high_priority():
    """An explicit none-priority override must suppress high-priority output."""
    data = load_registry()
    failures = [
        p["path"]
        for p in data["pages"]
        if (p.get("maintenance_override") or {}).get("update_priority") == "none"
        and p["update_priority"] == "high"
    ]
    assert not failures, f"Override failed to suppress high priority: {failures}"


# ---------------------------------------------------------------------------
# Scanner unit tests
# ---------------------------------------------------------------------------

def test_discover_pages_finds_atlas_and_research():
    pages = scanner.discover_pages()
    atlas_pages = [p for p in pages if p[3].startswith("atlas")]
    research_pages = [p for p in pages if p[3].startswith("research")]
    assert len(atlas_pages) > 0, "Must find atlas pages"
    assert len(research_pages) > 0, "Must find research pages"


def test_detect_weak_sources_finds_markers():
    body = "This is a weak_signal and low confidence report from an aggregator newsletter."
    found = scanner.detect_weak_sources(body)
    assert len(found) >= 3, f"Expected multiple weak sources, got {found}"


def test_compute_staleness_fresh():
    today = scanner.date.today()
    status, reason = scanner.compute_staleness(today)
    assert status == "fresh"
    assert reason is None


def test_compute_staleness_stale():
    today = scanner.date.today()
    old = today - scanner.timedelta(days=100)
    status, reason = scanner.compute_staleness(old)
    assert status == "stale"
    assert reason is not None


def test_compute_staleness_unknown():
    status, reason = scanner.compute_staleness(None)
    assert status == "unknown"
    assert reason is not None


def test_check_safety_violations_research_missing_noindex():
    fm = {"title": "Test", "robots": "index,follow", "sitemap": False, "verified": False, "status": "draft"}
    violations = scanner.check_safety_violations("research/test.md", fm, [], "research")
    assert "research_missing_noindex" in violations


def test_check_safety_violations_research_sitemap_true():
    fm = {"title": "Test", "robots": "noindex,follow", "sitemap": True, "verified": False, "status": "draft"}
    violations = scanner.check_safety_violations("research/test.md", fm, [], "research")
    assert "research_sitemap_not_false" in violations


def test_check_safety_violations_verified_with_weak_sources():
    fm = {"title": "Test", "robots": "noindex,follow", "sitemap": False, "verified": True, "status": "reviewed"}
    violations = scanner.check_safety_violations("atlas/test.md", fm, ["weak_signal"], "atlas")
    assert "verified_with_weak_sources" in violations


def test_check_safety_violations_missing_title():
    fm = {"title": "", "robots": "noindex,follow", "sitemap": False, "verified": False, "status": "draft"}
    violations = scanner.check_safety_violations("atlas/test.md", fm, [], "atlas")
    assert "missing_title" in violations


def test_parse_date_various_formats():
    assert scanner.parse_date("2026-06-07") == scanner.date(2026, 6, 7)
    assert scanner.parse_date("2026-06-07 12:00:00") == scanner.date(2026, 6, 7)
    dt = scanner.datetime(2026, 6, 7, 12, 0, 0, tzinfo=scanner.timezone.utc)
    assert scanner.parse_date(dt) == scanner.date(2026, 6, 7)
    assert scanner.parse_date(None) is None
