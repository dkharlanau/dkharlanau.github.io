from scripts.google_search_pipeline import (
    classify_index_status,
    classify_url_kind,
    compute_delta,
    parse_sitemap_document,
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
