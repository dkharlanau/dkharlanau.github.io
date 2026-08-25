#!/usr/bin/env python3
"""Submit the site sitemap to Google Search Console and audit sitemap URLs.

This tool uses the Search Console API, not the Google Indexing API. It can:
- discover URLs from a sitemap index,
- submit the sitemap to Search Console,
- inspect page indexing status,
- build JSON and Markdown reports,
- compare the current run with a previous report.

Without credentials it still validates the live sitemap and writes a setup report.
"""

from __future__ import annotations

import argparse
import json
import os
import time
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen

WEBMASTERS_SCOPE = "https://www.googleapis.com/auth/webmasters"
INSPECTION_ENDPOINT = "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect"
SITEMAP_API_ROOT = "https://www.googleapis.com/webmasters/v3"
DATA_EXTENSIONS = {".json", ".yml", ".yaml", ".xml", ".txt", ".csv"}
DEFAULT_USER_AGENT = "DKH-Google-Search-Pipeline/1.0 (+https://dkharlanau.github.io/)"

PRIORITY_ORDER = {"P0": 0, "P1": 1, "P2": 2, "REVIEW": 3, "OK": 4, "SKIP": 5, "ERROR": 6}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def local_name(tag: str) -> str:
    return tag.split("}", 1)[-1]


def fetch_text(url: str, *, timeout: int = 30, attempts: int = 6, delay: float = 10.0) -> str:
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            request = Request(url, headers={"User-Agent": DEFAULT_USER_AGENT, "Accept": "application/xml,text/xml,*/*"})
            with urlopen(request, timeout=timeout) as response:
                charset = response.headers.get_content_charset() or "utf-8"
                return response.read().decode(charset, errors="replace")
        except Exception as exc:  # network errors vary by runtime
            last_error = exc
            if attempt < attempts:
                time.sleep(delay)
    raise RuntimeError(f"Could not fetch {url} after {attempts} attempts: {last_error}")


def parse_sitemap_document(xml_text: str) -> tuple[str, list[dict[str, str]]]:
    root = ET.fromstring(xml_text.lstrip())
    root_name = local_name(root.tag)

    if root_name == "sitemapindex":
        entries: list[dict[str, str]] = []
        for child in root:
            if local_name(child.tag) != "sitemap":
                continue
            loc = ""
            lastmod = ""
            for item in child:
                name = local_name(item.tag)
                if name == "loc" and item.text:
                    loc = item.text.strip()
                elif name == "lastmod" and item.text:
                    lastmod = item.text.strip()
            if loc:
                entries.append({"url": loc, "lastmod": lastmod})
        return "sitemapindex", entries

    if root_name == "urlset":
        entries = []
        for child in root:
            if local_name(child.tag) != "url":
                continue
            loc = ""
            lastmod = ""
            for item in child:
                name = local_name(item.tag)
                if name == "loc" and item.text:
                    loc = item.text.strip()
                elif name == "lastmod" and item.text:
                    lastmod = item.text.strip()
            if loc:
                entries.append({"url": loc, "lastmod": lastmod})
        return "urlset", entries

    raise ValueError(f"Unsupported sitemap root element: {root_name}")


def same_origin(url_a: str, url_b: str) -> bool:
    a = urlparse(url_a)
    b = urlparse(url_b)
    return (a.scheme, a.netloc) == (b.scheme, b.netloc)


def collect_sitemap_urls(
    sitemap_url: str,
    *,
    max_depth: int = 4,
    fetcher=fetch_text,
) -> tuple[list[dict[str, str]], list[str]]:
    seen_sitemaps: set[str] = set()
    pages: dict[str, dict[str, str]] = {}
    sitemap_sources: list[str] = []

    def visit(url: str, depth: int) -> None:
        if url in seen_sitemaps:
            return
        if depth > max_depth:
            raise RuntimeError(f"Sitemap nesting is deeper than {max_depth}: {url}")
        if not same_origin(sitemap_url, url):
            raise RuntimeError(f"Cross-origin sitemap is not allowed: {url}")

        seen_sitemaps.add(url)
        sitemap_sources.append(url)
        kind, entries = parse_sitemap_document(fetcher(url))

        if kind == "sitemapindex":
            for entry in entries:
                visit(entry["url"], depth + 1)
            return

        for entry in entries:
            page_url = entry["url"]
            if not same_origin(sitemap_url, page_url):
                continue
            pages.setdefault(page_url, entry)

    visit(sitemap_url, 0)
    return list(pages.values()), sitemap_sources


def classify_url_kind(url: str) -> str:
    suffix = Path(urlparse(url).path).suffix.lower()
    return "data" if suffix in DATA_EXTENSIONS else "page"


def classify_index_status(index_status: dict[str, Any]) -> tuple[str, str, str]:
    verdict = str(index_status.get("verdict") or "").upper()
    coverage = str(index_status.get("coverageState") or "")
    coverage_lc = coverage.lower()
    indexing_state = str(index_status.get("indexingState") or "").upper()
    robots_state = str(index_status.get("robotsTxtState") or "").upper()
    fetch_state = str(index_status.get("pageFetchState") or "").upper()
    last_crawl = str(index_status.get("lastCrawlTime") or "")

    if verdict == "PASS" or ("indexed" in coverage_lc and "not indexed" not in coverage_lc):
        return "OK", "indexed", "No action."

    if "crawled" in coverage_lc and "not indexed" in coverage_lc:
        return "P1", "crawled_not_indexed", "Review content quality and canonical signals; request indexing manually if the page is important."

    if "discovered" in coverage_lc and "not indexed" in coverage_lc:
        return "P2", "discovered_not_indexed", "Strengthen internal links and wait for Google to crawl the page."

    if "blocked" in indexing_state.lower() or "blocked" in robots_state.lower():
        return "P0", "blocked", "Fix robots or noindex rules before requesting indexing."

    if fetch_state and fetch_state not in {"SUCCESSFUL", "PAGE_FETCH_STATE_UNSPECIFIED"}:
        return "P0", "fetch_error", "Fix the page fetch problem and then resubmit the sitemap."

    if "unknown to google" in coverage_lc or (verdict in {"NEUTRAL", "VERDICT_UNSPECIFIED", ""} and not last_crawl):
        return "P0", "unknown", "Check internal links; request indexing manually for priority pages."

    return "REVIEW", "needs_review", "Review the Search Console details for this URL."


def create_authorized_session(credentials_file: str):
    try:
        from google.auth.transport.requests import AuthorizedSession
        from google.oauth2 import service_account
    except ImportError as exc:
        raise RuntimeError(
            "Google authentication libraries are missing. Install: pip install 'google-auth[requests]'"
        ) from exc

    credentials = service_account.Credentials.from_service_account_file(
        credentials_file,
        scopes=[WEBMASTERS_SCOPE],
    )
    return AuthorizedSession(credentials)


def submit_sitemap(session, site_url: str, sitemap_url: str) -> dict[str, Any]:
    endpoint = (
        f"{SITEMAP_API_ROOT}/sites/{quote(site_url, safe='')}"
        f"/sitemaps/{quote(sitemap_url, safe='')}"
    )
    response = session.put(endpoint, timeout=30)
    if response.status_code not in {200, 204}:
        raise RuntimeError(
            f"Search Console sitemap submit failed ({response.status_code}): {response.text[:500]}"
        )
    return {"status": "submitted", "http_status": response.status_code}


def inspect_url(session, site_url: str, page_url: str) -> dict[str, Any]:
    response = session.post(
        INSPECTION_ENDPOINT,
        json={
            "inspectionUrl": page_url,
            "siteUrl": site_url,
            "languageCode": "en-US",
        },
        timeout=30,
    )
    if response.status_code != 200:
        raise RuntimeError(
            f"URL Inspection failed ({response.status_code}) for {page_url}: {response.text[:500]}"
        )
    return response.json()


def load_previous_report(path: str | None) -> dict[str, Any] | None:
    if not path:
        return None
    report_path = Path(path)
    if not report_path.exists():
        return None
    try:
        return json.loads(report_path.read_text(encoding="utf-8"))
    except Exception:
        return None


def compute_delta(current_counts: dict[str, int], previous: dict[str, Any] | None) -> dict[str, int]:
    previous_counts = {}
    if previous:
        previous_counts = previous.get("summary", {}).get("status_counts", {}) or {}
    keys = set(current_counts) | set(previous_counts)
    return {key: int(current_counts.get(key, 0)) - int(previous_counts.get(key, 0)) for key in sorted(keys)}


def build_markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    submission = report["sitemap_submission"]
    lines = [
        "# Google Search indexing report",
        "",
        f"Generated: `{report['generated_at']}`",
        "",
        f"- Property: `{report['site_url']}`",
        f"- Sitemap: `{report['sitemap_url']}`",
        f"- Sitemap API: **{submission.get('status', 'unknown')}**",
        f"- Sitemap URLs discovered: **{summary['sitemap_urls']}**",
        f"- Page URLs inspected: **{summary['inspected_pages']}**",
        f"- Data URLs skipped: **{summary['skipped_data_urls']}**",
        "",
        "## Indexing status",
        "",
        "| Status | Count | Change |",
        "| --- | ---: | ---: |",
    ]

    counts = summary["status_counts"]
    delta = summary["status_delta"]
    for status in ["indexed", "unknown", "crawled_not_indexed", "discovered_not_indexed", "blocked", "fetch_error", "needs_review", "inspection_error"]:
        if status in counts or status in delta:
            change = delta.get(status, 0)
            sign = "+" if change > 0 else ""
            lines.append(f"| {status} | {counts.get(status, 0)} | {sign}{change} |")

    queue = [
        item
        for item in report["urls"]
        if item.get("kind") == "page" and item.get("priority") not in {"OK", "SKIP"}
    ]
    queue.sort(key=lambda item: (PRIORITY_ORDER.get(item.get("priority", "ERROR"), 99), item["url"]))

    lines.extend(["", "## Priority queue", ""])
    if not queue:
        lines.append("No page needs manual review in this run.")
    else:
        lines.extend(
            [
                "| Priority | Status | URL | Recommended action |",
                "| --- | --- | --- | --- |",
            ]
        )
        for item in queue[:75]:
            url = item["url"].replace("|", "%7C")
            action = str(item.get("recommended_action") or "").replace("|", "\\|")
            lines.append(
                f"| {item.get('priority', 'REVIEW')} | {item.get('status', 'needs_review')} | "
                f"[{url}]({url}) | {action} |"
            )
        if len(queue) > 75:
            lines.append(f"\nOnly the first 75 of {len(queue)} queue items are shown here. The JSON report has all items.")

    if report.get("setup_required"):
        lines.extend(
            [
                "",
                "## Setup required",
                "",
                "Google API credentials are not configured yet. The sitemap was parsed, but no API submission or URL inspection was sent.",
                "Add the service account JSON to the GitHub secret `GOOGLE_SEARCH_CONSOLE_SERVICE_ACCOUNT` and add that service account to the Search Console property.",
            ]
        )

    return "\n".join(lines) + "\n"


def build_setup_only_items(entries: list[dict[str, str]]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for entry in entries:
        kind = classify_url_kind(entry["url"])
        items.append(
            {
                "url": entry["url"],
                "lastmod": entry.get("lastmod", ""),
                "kind": kind,
                "priority": "SKIP",
                "status": "not_inspected",
                "recommended_action": "Configure Search Console API credentials.",
            }
        )
    return items


def run(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    entries, sitemap_sources = collect_sitemap_urls(
        args.sitemap_url,
        max_depth=args.max_sitemap_depth,
    )
    previous = load_previous_report(args.previous_report)

    report: dict[str, Any] = {
        "generated_at": utc_now(),
        "site_url": args.site_url,
        "sitemap_url": args.sitemap_url,
        "sitemap_sources": sitemap_sources,
        "setup_required": not bool(args.credentials),
        "sitemap_submission": {"status": "not_configured"},
        "summary": {},
        "urls": [],
    }

    if not args.credentials:
        report["urls"] = build_setup_only_items(entries)
        status_counts = {"not_inspected": sum(1 for item in report["urls"] if item["kind"] == "page")}
        report["summary"] = {
            "sitemap_urls": len(entries),
            "inspected_pages": 0,
            "skipped_data_urls": sum(1 for item in report["urls"] if item["kind"] == "data"),
            "inspection_errors": 0,
            "status_counts": status_counts,
            "status_delta": compute_delta(status_counts, previous),
        }
        return report, 0

    session = create_authorized_session(args.credentials)
    report["sitemap_submission"] = submit_sitemap(session, args.site_url, args.sitemap_url)

    page_entries = [entry for entry in entries if classify_url_kind(entry["url"]) == "page"]
    data_entries = [entry for entry in entries if classify_url_kind(entry["url"]) == "data"]
    if args.include_data:
        page_entries.extend(data_entries)
        data_entries = []

    page_entries = page_entries[: args.max_inspections]
    items: list[dict[str, Any]] = []
    inspection_errors = 0

    for index, entry in enumerate(page_entries):
        page_url = entry["url"]
        kind = classify_url_kind(page_url)
        try:
            response = inspect_url(session, args.site_url, page_url)
            inspection = response.get("inspectionResult", {})
            index_status = inspection.get("indexStatusResult", {}) or {}
            priority, status, action = classify_index_status(index_status)
            item = {
                "url": page_url,
                "lastmod": entry.get("lastmod", ""),
                "kind": kind,
                "priority": priority,
                "status": status,
                "recommended_action": action,
                "verdict": index_status.get("verdict"),
                "coverage_state": index_status.get("coverageState"),
                "robots_txt_state": index_status.get("robotsTxtState"),
                "indexing_state": index_status.get("indexingState"),
                "page_fetch_state": index_status.get("pageFetchState"),
                "last_crawl_time": index_status.get("lastCrawlTime"),
                "google_canonical": index_status.get("googleCanonical"),
                "user_canonical": index_status.get("userCanonical"),
                "crawled_as": index_status.get("crawledAs"),
                "sitemaps": index_status.get("sitemap") or [],
                "referring_urls": index_status.get("referringUrls") or [],
            }
        except Exception as exc:
            inspection_errors += 1
            item = {
                "url": page_url,
                "lastmod": entry.get("lastmod", ""),
                "kind": kind,
                "priority": "ERROR",
                "status": "inspection_error",
                "recommended_action": "Check API permissions, quota, and the Search Console property.",
                "error": str(exc),
            }
        items.append(item)

        if args.request_delay and index < len(page_entries) - 1:
            time.sleep(args.request_delay)

    for entry in data_entries:
        items.append(
            {
                "url": entry["url"],
                "lastmod": entry.get("lastmod", ""),
                "kind": "data",
                "priority": "SKIP",
                "status": "data_url_skipped",
                "recommended_action": "No URL Inspection request is sent for data endpoints by default.",
            }
        )

    status_counts = dict(Counter(item["status"] for item in items if item["kind"] == "page"))
    report["urls"] = items
    report["summary"] = {
        "sitemap_urls": len(entries),
        "inspected_pages": len(page_entries),
        "skipped_data_urls": len(data_entries),
        "inspection_errors": inspection_errors,
        "status_counts": status_counts,
        "status_delta": compute_delta(status_counts, previous),
    }

    if page_entries and inspection_errors == len(page_entries):
        return report, 2
    return report, 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-url", required=True, help="Exact Search Console property, including trailing slash for URL-prefix properties.")
    parser.add_argument("--sitemap-url", required=True, help="Public sitemap or sitemap index URL.")
    parser.add_argument("--credentials", default=os.getenv("GOOGLE_APPLICATION_CREDENTIALS"), help="Service account JSON file.")
    parser.add_argument("--previous-report", help="Previous JSON report used to calculate status deltas.")
    parser.add_argument("--output-dir", default="reports/seo/google-search", help="Directory for JSON and Markdown reports.")
    parser.add_argument("--max-inspections", type=int, default=1900, help="Maximum URL Inspection API calls per run.")
    parser.add_argument("--max-sitemap-depth", type=int, default=4, help="Maximum sitemap index nesting depth.")
    parser.add_argument("--request-delay", type=float, default=0.15, help="Delay between URL Inspection calls in seconds.")
    parser.add_argument("--include-data", action="store_true", help="Also inspect JSON/YAML/XML/TXT/CSV sitemap URLs.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.max_inspections < 1:
        raise SystemExit("--max-inspections must be at least 1")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        report, exit_code = run(args)
    except Exception as exc:
        report = {
            "generated_at": utc_now(),
            "site_url": args.site_url,
            "sitemap_url": args.sitemap_url,
            "setup_required": not bool(args.credentials),
            "sitemap_submission": {"status": "fatal_error"},
            "summary": {
                "sitemap_urls": 0,
                "inspected_pages": 0,
                "skipped_data_urls": 0,
                "inspection_errors": 0,
                "status_counts": {},
                "status_delta": {},
            },
            "urls": [],
            "fatal_error": str(exc),
        }
        exit_code = 1

    json_path = output_dir / "google-indexing.json"
    markdown_path = output_dir / "google-indexing.md"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    markdown_path.write_text(build_markdown(report), encoding="utf-8")

    print(f"Wrote {json_path}")
    print(f"Wrote {markdown_path}")
    if report.get("fatal_error"):
        print(f"ERROR: {report['fatal_error']}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
