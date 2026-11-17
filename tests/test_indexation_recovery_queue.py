from scripts.indexation_recovery_queue import (
    LiveCheck,
    build_markdown,
    build_recovery,
    recovery_action,
)


def good(url: str) -> LiveCheck:
    return LiveCheck(url, 200, "index,follow", url, True, True, "")


def bad(url: str) -> LiveCheck:
    return LiveCheck(url, 200, "noindex,follow", url, True, False, "rendered robots contains noindex")


def config():
    return {
        "site_url": "https://example.com",
        "manual_request_limit": 2,
        "candidate_statuses": [
            "unknown",
            "not_inspected",
            "crawled_not_indexed",
        ],
        "status_scores": {
            "unknown": 600,
            "not_inspected": 550,
            "crawled_not_indexed": 400,
        },
        "tier_scores": {"P0": 300, "P1": 200, "P2": 100},
        "current_inspection_bonus": 20,
        "prefix_rules": [{"prefix": "/atlas/", "score": 80}],
        "priority_routes": [
            {"path": "/service/", "tier": "P0", "focus": "ams", "reason": "Commercial route."},
            {"path": "/atlas/problem/", "tier": "P0", "focus": "integration", "reason": "Problem route."},
            {"path": "/crawled/", "tier": "P1", "focus": "ams", "reason": "Already crawled."},
            {"path": "/missing/", "tier": "P2", "focus": "learning", "reason": "Configured route."},
        ],
    }


def test_unknown_live_indexable_enters_manual_queue():
    report = {
        "generated_at": "2026-09-16T10:00:00Z",
        "urls": [
            {
                "url": "https://example.com/service/",
                "kind": "page",
                "status": "unknown",
                "priority": "P0",
                "inspection_source": "current",
            }
        ],
    }
    cfg = config()
    cfg["priority_routes"] = cfg["priority_routes"][:1]
    recovery = build_recovery(report, cfg, live_checker=good)
    assert recovery["summary"]["manual_request_candidates"] == 1
    assert recovery["manual_request_queue"][0]["action"] == "REQUEST_INDEXING"


def test_crawled_not_indexed_never_bypasses_quality_review():
    assert recovery_action("crawled_not_indexed", good("https://example.com/crawled/")) == (
        "QUALITY_REVIEW_THEN_REQUEST"
    )


def test_live_noindex_blocks_request_indexing():
    assert recovery_action("unknown", bad("https://example.com/service/")) == "FIX_TECHNICAL_GATE"


def test_priority_corpus_tracks_missing_and_indexed_routes():
    report = {
        "generated_at": "2026-09-16T10:00:00Z",
        "urls": [
            {
                "url": "https://example.com/service/",
                "kind": "page",
                "status": "indexed",
                "priority": "OK",
                "inspection_source": "current",
            },
            {
                "url": "https://example.com/atlas/problem/",
                "kind": "page",
                "status": "unknown",
                "priority": "P0",
                "inspection_source": "previous",
            },
            {
                "url": "https://example.com/crawled/",
                "kind": "page",
                "status": "crawled_not_indexed",
                "priority": "P1",
                "inspection_source": "current",
            },
        ],
    }
    recovery = build_recovery(report, config(), live_checker=good)
    summary = recovery["summary"]
    assert summary["configured_priority_routes"] == 4
    assert summary["present_priority_routes"] == 3
    assert summary["missing_priority_routes"] == 1
    assert summary["indexed_priority_routes"] == 1
    assert summary["priority_indexed_pct"] == 25.0
    assert recovery["missing_priority_routes"][0]["url"] == "https://example.com/missing/"


def test_manual_queue_is_capped_and_ranked_by_business_tier():
    cfg = config()
    cfg["manual_request_limit"] = 1
    cfg["priority_routes"] = cfg["priority_routes"][:2]
    report = {
        "generated_at": "2026-09-16T10:00:00Z",
        "urls": [
            {
                "url": "https://example.com/service/",
                "kind": "page",
                "status": "unknown",
                "priority": "P0",
                "inspection_source": "current",
            },
            {
                "url": "https://example.com/atlas/problem/",
                "kind": "page",
                "status": "unknown",
                "priority": "P0",
                "inspection_source": "current",
            },
        ],
    }
    recovery = build_recovery(report, cfg, live_checker=good)
    assert recovery["summary"]["manual_request_candidates"] == 2
    assert recovery["summary"]["manual_queue_size"] == 1
    assert recovery["manual_request_queue"][0]["url"] == "https://example.com/atlas/problem/"


def test_recovery_preserves_actual_inspection_times_in_json_and_markdown():
    cfg = config()
    cfg["priority_routes"] = cfg["priority_routes"][:2]
    report = {
        "generated_at": "2026-11-17T12:20:00Z",
        "urls": [
            {"url": "https://example.com/service/", "kind": "page", "status": "unknown",
             "inspection_source": "previous", "stale": True, "inspected_at": "2026-11-15T09:00:00Z"},
            {"url": "https://example.com/atlas/problem/", "kind": "page", "status": "unknown",
             "inspection_source": "previous", "stale": True, "inspected_at": None},
        ],
    }
    recovery = build_recovery(report, cfg, live_checker=good)
    by_url = {row["url"]: row for row in recovery["priority_corpus"]}
    assert by_url["https://example.com/service/"]["inspected_at"] == "2026-11-15T09:00:00Z"
    assert by_url["https://example.com/atlas/problem/"]["inspected_at"] is None
    markdown = build_markdown(recovery)
    assert markdown.count("2026-11-15T09:00:00Z") == 2
    assert markdown.count("| unknown | unknown |") == 2
    assert "source report date is not the inspection date" in markdown
