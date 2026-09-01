from datetime import datetime, timezone

from scripts.google_search_pipeline import (
    analytics_totals,
    analytics_window,
    classify_index_status,
    classify_url_kind,
    compute_delta,
    merge_rolling_page_inventory,
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
    assert classify_url_kind("https://example.com/llms.txt") == "data"
    assert classify_url_kind("https://example.com/assets/app.js") == "data"
    assert classify_url_kind("https://example.com/assets/site.css") == "data"
    assert classify_url_kind("https://example.com/assets/icon.svg") == "data"
    assert classify_url_kind("https://example.com/labs/") == "page"


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
