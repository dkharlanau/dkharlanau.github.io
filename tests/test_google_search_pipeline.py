from datetime import datetime, timezone
import json
from types import SimpleNamespace

import pytest

from scripts import google_search_pipeline as pipeline

from scripts.google_search_pipeline import (
    analytics_totals,
    analytics_window,
    classify_index_status,
    classify_url_kind,
    compute_delta,
    merge_rolling_page_inventory,
    load_monitor_urls,
    parse_sitemap_document,
    previous_report_age_hours,
    select_entries_for_inspection,
)


def test_parse_sitemap_index():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
      <sitemap>
        <loc>https://example.com/sitemap-pages.xml</loc>
        <lastmod>2026-08-25T00:00:00Z</lastmod>
      </sitemap>
    </sitemapindex>
    """
    kind, entries = parse_sitemap_document(xml)
    assert kind == "sitemapindex"
    assert entries == [
        {
            "url": "https://example.com/sitemap-pages.xml",
            "lastmod": "2026-08-25T00:00:00Z",
        }
    ]


def test_parse_urlset():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
      <url>
        <loc>https://example.com/labs/</loc>
        <lastmod>2026-08-24</lastmod>
      </url>
      <url><loc>https://example.com/about/</loc></url>
    </urlset>
    """
    kind, entries = parse_sitemap_document(xml)
    assert kind == "urlset"
    assert entries[0]["url"] == "https://example.com/labs/"
    assert entries[0]["lastmod"] == "2026-08-24"
    assert entries[1]["lastmod"] == ""


def test_data_endpoints_are_not_page_urls():
    assert classify_url_kind("https://example.com/ai/resume.json") == "data"
    assert classify_url_kind("https://example.com/ai/entity-graph.jsonld") == "data"
    assert classify_url_kind("https://example.com/ai/entity-graph.JSONLD?version=1") == "data"
    assert classify_url_kind("https://example.com/llms.txt") == "data"
    assert classify_url_kind("https://example.com/assets/app.js") == "data"
    assert classify_url_kind("https://example.com/assets/site.css") == "data"
    assert classify_url_kind("https://example.com/assets/icon.svg") == "data"
    assert classify_url_kind("https://example.com/labs/") == "page"


def test_setup_inventory_excludes_jsonld_from_page_inspections():
    entries = [
        {"url": "https://example.com/ai/entity-graph.jsonld", "lastmod": ""},
        {"url": "https://example.com/atlas/example/", "lastmod": ""},
    ]
    rows = pipeline.build_setup_only_items(entries)
    assert [(row["kind"], row["status"]) for row in rows] == [
        ("data", "data_url_skipped"),
        ("page", "not_inspected"),
    ]


def test_indexed_status_is_ok():
    priority, status, action = classify_index_status(
        {
            "verdict": "PASS",
            "coverageState": "Submitted and indexed",
            "lastCrawlTime": "2026-08-24T12:00:00Z",
        }
    )
    assert priority == "OK"
    assert status == "indexed"
    assert action == "No action."


def test_crawled_not_indexed_is_p1():
    priority, status, _ = classify_index_status(
        {
            "verdict": "NEUTRAL",
            "coverageState": "Crawled - currently not indexed",
            "lastCrawlTime": "2026-08-24T12:00:00Z",
        }
    )
    assert priority == "P1"
    assert status == "crawled_not_indexed"


def test_discovered_not_indexed_is_p2():
    priority, status, _ = classify_index_status(
        {
            "verdict": "NEUTRAL",
            "coverageState": "Discovered - currently not indexed",
        }
    )
    assert priority == "P2"
    assert status == "discovered_not_indexed"


def test_unknown_url_is_p0():
    priority, status, _ = classify_index_status(
        {
            "verdict": "NEUTRAL",
            "coverageState": "URL is unknown to Google",
        }
    )
    assert priority == "P0"
    assert status == "unknown"


def test_delta_uses_previous_report():
    previous = {
        "summary": {
            "status_counts": {
                "indexed": 10,
                "unknown": 4,
            }
        }
    }
    delta = compute_delta({"indexed": 12, "unknown": 1}, previous)
    assert delta == {"indexed": 2, "unknown": -3}


def test_priority_selection_prefers_new_and_problem_urls():
    entries = [
        {"url": "https://example.com/indexed/", "lastmod": ""},
        {"url": "https://example.com/problem/", "lastmod": ""},
        {"url": "https://example.com/new/", "lastmod": ""},
    ]
    previous = {
        "urls": [
            {
                "url": "https://example.com/indexed/",
                "kind": "page",
                "status": "indexed",
            },
            {
                "url": "https://example.com/problem/",
                "kind": "page",
                "status": "crawled_not_indexed",
            },
        ]
    }
    selected = select_entries_for_inspection(
        entries,
        previous,
        max_inspections=2,
        mode="priority",
        seed="2026-08-25",
    )
    urls = {item["url"] for item in selected}
    assert "https://example.com/new/" in urls
    assert "https://example.com/problem/" in urls
    assert "https://example.com/indexed/" not in urls


def test_rotation_is_stable_for_same_seed():
    entries = [
        {"url": f"https://example.com/{letter}/", "lastmod": ""}
        for letter in "abcdef"
    ]
    first = select_entries_for_inspection(
        entries,
        None,
        max_inspections=4,
        mode="rotate",
        seed="2026-08-25",
    )
    second = select_entries_for_inspection(
        entries,
        None,
        max_inspections=4,
        mode="rotate",
        seed="2026-08-25",
    )
    assert first == second


def test_monitored_urls_are_selected_first_within_existing_budget():
    entries = [{"url": f"https://example.com/{letter}/", "lastmod": ""} for letter in "abcdef"]
    monitored = ["https://example.com/e/", "https://example.com/b/"]
    selected = select_entries_for_inspection(entries, None, max_inspections=4, mode="rotate",
                                             seed="2026-11-17", monitor_urls=monitored)
    assert [item["url"] for item in selected[:2]] == monitored
    assert len({item["url"] for item in selected}) == 4
    limited = select_entries_for_inspection(entries, None, max_inspections=1, mode="all",
                                            seed="unused", monitor_urls=monitored)
    assert [item["url"] for item in limited] == monitored[:1]


def test_monitor_file_rejects_missing_duplicate_or_foreign_urls(tmp_path):
    path = tmp_path / "monitor.json"
    entries = [{"url": "https://example.com/a/", "lastmod": ""}]
    for urls in (["https://example.com/a/", "https://example.com/a/"],
                 ["https://other.example/a/"], ["https://example.com/missing/"]):
        path.write_text(json.dumps({"urls": urls}), encoding="utf-8")
        with pytest.raises(ValueError):
            load_monitor_urls(str(path), "https://example.com/", entries)
    path.write_text(json.dumps({"urls": ["https://example.com/a/"]}), encoding="utf-8")
    assert load_monitor_urls(str(path), "https://example.com/", entries) == ["https://example.com/a/"]


def test_previous_report_age_hours():
    previous = {
        "generated_at": "2026-08-25T06:00:00Z",
        "summary": {"inspected_pages": 10},
    }
    age = previous_report_age_hours(
        previous,
        now=datetime(2026, 8, 25, 9, 30, tzinfo=timezone.utc),
    )
    assert age == 3.5


def test_analytics_window_ends_two_days_behind():
    start, end = analytics_window(
        7,
        now=datetime(2026, 8, 25, 9, 30, tzinfo=timezone.utc),
    )
    assert start == "2026-08-17"
    assert end == "2026-08-23"


def test_analytics_totals_handles_empty_and_values():
    assert analytics_totals({}) == {
        "clicks": 0.0,
        "impressions": 0.0,
        "ctr": 0.0,
        "position": 0.0,
    }
    totals = analytics_totals(
        {
            "rows": [
                {
                    "clicks": 3,
                    "impressions": 120,
                    "ctr": 0.025,
                    "position": 8.4,
                }
            ]
        }
    )
    assert totals["clicks"] == 3.0
    assert totals["impressions"] == 120.0
    assert totals["ctr"] == 0.025
    assert totals["position"] == 8.4


def test_rolling_inventory_keeps_uninspected_previous_status():
    entries = [
        {"url": "https://example.com/a/", "lastmod": "2026-08-25"},
        {"url": "https://example.com/b/", "lastmod": "2026-08-25"},
        {"url": "https://example.com/c/", "lastmod": "2026-08-25"},
    ]
    current = [
        {
            "url": "https://example.com/a/",
            "lastmod": "2026-08-25",
            "kind": "page",
            "priority": "OK",
            "status": "indexed",
            "recommended_action": "No action.",
        }
    ]
    previous = {
        "urls": [
            {
                "url": "https://example.com/b/",
                "kind": "page",
                "priority": "P1",
                "status": "crawled_not_indexed",
                "recommended_action": "Review.",
            }
        ]
    }
    merged = merge_rolling_page_inventory(entries, current, previous)
    by_url = {item["url"]: item for item in merged}
    assert by_url["https://example.com/a/"]["inspection_source"] == "current"
    assert by_url["https://example.com/b/"]["status"] == "crawled_not_indexed"
    assert by_url["https://example.com/b/"]["inspection_source"] == "previous"
    assert by_url["https://example.com/c/"]["status"] == "not_inspected"


def test_rolling_inventory_preserves_url_inspection_times_without_guessing():
    entries = [{"url": f"https://example.com/{letter}/", "lastmod": ""} for letter in "abcd"]
    current = [{"url": "https://example.com/a/", "kind": "page", "status": "indexed",
                "inspected_at": "2026-11-17T12:00:05Z"}]
    previous = {"generated_at": "2026-11-16T14:00:00Z", "urls": [
        {"url": "https://example.com/b/", "kind": "page", "status": "unknown",
         "inspected_at": "2026-11-15T12:30:00Z"},
        {"url": "https://example.com/c/", "kind": "page", "status": "indexed",
         "last_crawl_time": "2026-11-14T10:00:00Z"},
    ]}
    first = merge_rolling_page_inventory(entries, current, previous)
    by_url = {item["url"]: item for item in first}
    assert by_url["https://example.com/a/"]["inspected_at"] == "2026-11-17T12:00:05Z"
    assert by_url["https://example.com/b/"]["inspected_at"] == "2026-11-15T12:30:00Z"
    assert by_url["https://example.com/c/"]["inspected_at"] is None
    assert by_url["https://example.com/d/"]["inspected_at"] is None
    assert by_url["https://example.com/b/"]["stale"] is True
    second = merge_rolling_page_inventory(entries, [], {"urls": first})
    assert {row["url"]: row["inspected_at"] for row in second} == {
        url: row["inspected_at"] for url, row in by_url.items()
    }


def test_run_dates_successful_inspections_but_not_failed_results(monkeypatch):
    entries = [{"url": f"https://example.com/{name}/", "lastmod": ""} for name in ("ok", "error")]
    monkeypatch.setattr(pipeline, "collect_sitemap_urls", lambda *a, **kw: (entries, []))
    monkeypatch.setattr(pipeline, "load_previous_report", lambda path: None)
    monkeypatch.setattr(pipeline, "create_authorized_session", lambda credentials: object())
    monkeypatch.setattr(pipeline, "submit_sitemap", lambda *a: {"status": "submitted"})
    monkeypatch.setattr(pipeline, "collect_search_analytics", lambda *a: {"status": "available"})
    timestamps = iter(["2026-11-17T12:00:00Z", "2026-11-17T12:00:01Z",
                       "2026-11-17T12:00:02Z", "2026-11-17T12:00:03Z"])
    monkeypatch.setattr(pipeline, "utc_now", lambda: next(timestamps))

    def inspect(session, site, url):
        if url.endswith("/error/"):
            raise RuntimeError("quota exceeded")
        return {"inspectionResult": {"indexStatusResult": {"verdict": "PASS"}}}

    monkeypatch.setattr(pipeline, "inspect_url", inspect)
    args = SimpleNamespace(sitemap_url="https://example.com/sitemap.xml", max_sitemap_depth=4,
                           previous_report=None, site_url="https://example.com/", credentials="set",
                           require_credentials=True, include_data=False, min_inspection_interval_hours=0,
                           max_inspections=2, inspection_mode="all", selection_seed="", request_delay=0)
    report, exit_code = pipeline.run(args)
    rows = {item["url"]: item for item in report["urls"]}
    assert exit_code == 0
    assert rows["https://example.com/error/"]["inspection_attempted_at"] == "2026-11-17T12:00:01Z"
    assert rows["https://example.com/error/"]["inspected_at"] is None
    assert rows["https://example.com/ok/"]["inspection_attempted_at"] == "2026-11-17T12:00:02Z"
    assert rows["https://example.com/ok/"]["inspected_at"] == "2026-11-17T12:00:03Z"
