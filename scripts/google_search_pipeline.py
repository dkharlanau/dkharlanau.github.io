#!/usr/bin/env python3
"""Submit the site sitemap to Google Search Console and audit search visibility.

This tool uses Search Console APIs, not the Google Indexing API. It can:
- discover URLs from a sitemap index,
- submit the sitemap to Search Console,
- inspect page indexing status,
- read Search Analytics performance,
- keep a rolling URL status inventory,
- build JSON and Markdown reports,
- compare the current run with a previous report.

Without credentials it can still validate the live sitemap and write a setup
report. Use --require-credentials when a production run must fail until the
Search Console connection is configured.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import time
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen

WEBMASTERS_SCOPE = "https://www.googleapis.com/auth/webmasters"
INSPECTION_ENDPOINT = "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect"
SITEMAP_API_ROOT = "https://www.googleapis.com/webmasters/v3"
DATA_EXTENSIONS = {
    ".json",
    ".yml",
    ".yaml",
    ".xml",
    ".txt",
    ".csv",
    ".css",
    ".js",
    ".map",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".ico",
    ".woff",
    ".woff2",
    ".ttf",
}
DEFAULT_USER_AGENT = "DKH-Google-Search-Pipeline/2.0 (+https://dkharlanau.github.io/)"

PRIORITY_ORDER = {"P0": 0, "P1": 1, "P2": 2, "REVIEW": 3, "OK": 4, "SKIP": 5, "ERROR": 6}
STATUS_RANK = {
    "unknown": 0,
    "blocked": 0,
    "fetch_error": 0,
    "crawled_not_indexed": 1,
    "discovered_not_indexed": 2,
    "inspection_error": 3,
    "needs_review": 4,
    "not_inspected": 5,
    "indexed": 20,
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def local_name(tag: str) -> str:
    return tag.split("}", 1)[-1]


def fetch_text(url: str, *, timeout: int = 30, attempts: int = 6, delay: float = 10.0) -> str:
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            request = Request(
                url,
                headers={
                    "User-Agent": DEFAULT_USER_AGENT,
                    "Accept": "application/xml,text/xml,*/*",
                },
            )
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
        return (
            "P1",
            "crawled_not_indexed",
            "Review content quality and canonical signals; request indexing manually if the page is important.",
        )

    if "discovered" in coverage_lc and "not indexed" in coverage_lc:
        return (
            "P2",
            "discovered_not_indexed",
            "Strengthen internal links and wait for Google to crawl the page.",
        )

    if "blocked" in indexing_state.lower() or "blocked" in robots_state.lower():
        return "P0", "blocked", "Fix robots or noindex rules before requesting indexing."

    if fetch_state and fetch_state not in {"SUCCESSFUL", "PAGE_FETCH_STATE_UNSPECIFIED"}:
        return "P0", "fetch_error", "Fix the page fetch problem and then resubmit the sitemap."

    if "unknown to google" in coverage_lc or (
        verdict in {"NEUTRAL", "VERDICT_UNSPECIFIED", ""} and not last_crawl
    ):
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


def query_search_analytics(
    session,
    site_url: str,
    *,
    start_date: str,
    end_date: str,
    dimensions: list[str] | None = None,
    row_limit: int = 250,
) -> dict[str, Any]:
    endpoint = (
        f"{SITEMAP_API_ROOT}/sites/{quote(site_url, safe='')}"
        "/searchAnalytics/query"
    )
    payload: dict[str, Any] = {
        "startDate": start_date,
        "endDate": end_date,
        "dataState": "final",
        "rowLimit": row_limit,
    }
    if dimensions:
        payload["dimensions"] = dimensions

    response = session.post(endpoint, json=payload, timeout=30)
    if response.status_code != 200:
        raise RuntimeError(
            f"Search Analytics failed ({response.status_code}): {response.text[:500]}"
        )
    return response.json()


def analytics_window(days: int, *, now: datetime | None = None) -> tuple[str, str]:
    if days < 1:
        raise ValueError("days must be at least 1")
    current = now or datetime.now(timezone.utc)
    # Search Console final data usually lags behind real time. Ending two days
    # ago makes scheduled comparisons more stable.
    end = current.date() - timedelta(days=2)
    start = end - timedelta(days=days - 1)
    return start.isoformat(), end.isoformat()


def analytics_totals(payload: dict[str, Any]) -> dict[str, float]:
    rows = payload.get("rows") or []
    if not rows:
        return {"clicks": 0.0, "impressions": 0.0, "ctr": 0.0, "position": 0.0}
    row = rows[0]
    return {
        "clicks": float(row.get("clicks") or 0.0),
        "impressions": float(row.get("impressions") or 0.0),
        "ctr": float(row.get("ctr") or 0.0),
        "position": float(row.get("position") or 0.0),
    }


def analytics_rows(payload: dict[str, Any]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for row in payload.get("rows") or []:
        keys = row.get("keys") or []
        result.append(
            {
                "key": str(keys[0]) if keys else "",
                "clicks": float(row.get("clicks") or 0.0),
                "impressions": float(row.get("impressions") or 0.0),
                "ctr": float(row.get("ctr") or 0.0),
                "position": float(row.get("position") or 0.0),
            }
        )
    return result


def collect_search_analytics(session, site_url: str) -> dict[str, Any]:
    start_7, end_7 = analytics_window(7)
    start_28, end_28 = analytics_window(28)

    seven = query_search_analytics(
        session,
        site_url,
        start_date=start_7,
        end_date=end_7,
        row_limit=1,
    )
    twenty_eight = query_search_analytics(
        session,
        site_url,
        start_date=start_28,
        end_date=end_28,
        row_limit=1,
    )
    top_pages = query_search_analytics(
        session,
        site_url,
        start_date=start_28,
        end_date=end_28,
        dimensions=["page"],
        row_limit=25,
    )
    top_queries = query_search_analytics(
        session,
        site_url,
        start_date=start_28,
        end_date=end_28,
        dimensions=["query"],
        row_limit=25,
    )

    return {
        "status": "available",
        "data_through": end_28,
        "windows": {
            "7d": {
                "start_date": start_7,
                "end_date": end_7,
                **analytics_totals(seven),
            },
            "28d": {
                "start_date": start_28,
                "end_date": end_28,
                **analytics_totals(twenty_eight),
            },
        },
        "top_pages_28d": analytics_rows(top_pages),
        "top_queries_28d": analytics_rows(top_queries),
    }


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
    return {
        key: int(current_counts.get(key, 0)) - int(previous_counts.get(key, 0))
        for key in sorted(keys)
    }


def parse_report_time(report: dict[str, Any] | None) -> datetime | None:
    if not report:
        return None
    raw = str(report.get("generated_at") or "")
    if not raw:
        return None
    try:
        return datetime.fromisoformat(raw.replace("Z", "+00:00")).astimezone(timezone.utc)
    except ValueError:
        return None


def previous_report_age_hours(
    report: dict[str, Any] | None,
    *,
    now: datetime | None = None,
) -> float | None:
    if not report or report.get("setup_required"):
        return None

    raw = str(report.get("last_inspection_at") or "")
    inspected_at: datetime | None = None
    if raw:
        try:
            inspected_at = datetime.fromisoformat(raw.replace("Z", "+00:00")).astimezone(timezone.utc)
        except ValueError:
            inspected_at = None

    if inspected_at is None:
        inspected_pages = int(report.get("summary", {}).get("inspected_pages") or 0)
        if inspected_pages <= 0:
            return None
        inspected_at = parse_report_time(report)

    if inspected_at is None:
        return None
    current = now or datetime.now(timezone.utc)
    return max(0.0, (current - inspected_at).total_seconds() / 3600.0)


def _stable_order(seed: str, url: str) -> str:
    return hashlib.sha256(f"{seed}|{url}".encode("utf-8")).hexdigest()


def select_entries_for_inspection(
    entries: list[dict[str, str]],
    previous: dict[str, Any] | None,
    *,
    max_inspections: int,
    mode: str,
    seed: str,
) -> list[dict[str, str]]:
    if max_inspections <= 0:
        return []

    previous_items = {
        str(item.get("url")): item
        for item in (previous or {}).get("urls", [])
        if item.get("kind") == "page" and item.get("url")
    }

    if mode == "all":
        ordered = sorted(entries, key=lambda item: item["url"])
    elif mode == "rotate":
        ordered = sorted(entries, key=lambda item: _stable_order(seed, item["url"]))
    elif mode == "priority":
        def key(item: dict[str, str]) -> tuple[int, str]:
            old = previous_items.get(item["url"])
            if old is None:
                rank = -1
            else:
                rank = STATUS_RANK.get(str(old.get("status") or "needs_review"), 10)
            return rank, _stable_order(seed, item["url"])

        ordered = sorted(entries, key=key)
    else:
        raise ValueError(f"Unsupported inspection mode: {mode}")

    return ordered[:max_inspections]


def _previous_page_items(previous: dict[str, Any] | None) -> dict[str, dict[str, Any]]:
    if not previous:
        return {}
    return {
        str(item.get("url")): dict(item)
        for item in previous.get("urls", [])
        if item.get("kind") == "page" and item.get("url")
    }


def merge_rolling_page_inventory(
    page_entries: list[dict[str, str]],
    current_items: list[dict[str, Any]],
    previous: dict[str, Any] | None,
) -> list[dict[str, Any]]:
    current_by_url = {item["url"]: item for item in current_items}
    previous_by_url = _previous_page_items(previous)
    merged: list[dict[str, Any]] = []

    for entry in page_entries:
        url = entry["url"]
        if url in current_by_url:
            item = dict(current_by_url[url])
            item["inspection_source"] = "current"
            item["stale"] = False
            merged.append(item)
            continue

        if url in previous_by_url:
            item = dict(previous_by_url[url])
            item["lastmod"] = entry.get("lastmod", "")
            item["kind"] = "page"
            item["inspection_source"] = "previous"
            item["stale"] = True
            merged.append(item)
            continue

        merged.append(
            {
                "url": url,
                "lastmod": entry.get("lastmod", ""),
                "kind": "page",
                "priority": "REVIEW",
                "status": "not_inspected",
                "recommended_action": "Pending a scheduled URL Inspection pass.",
                "inspection_source": "none",
                "stale": True,
            }
        )

    return merged


def _fmt_number(value: float) -> str:
    if value >= 1000:
        return f"{value:,.0f}"
    if value.is_integer():
        return f"{value:.0f}"
    return f"{value:.1f}"


def build_markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    submission = report["sitemap_submission"]
    analytics = report.get("search_analytics") or {}
    lines = [
        "# Google Search indexing report",
        "",
        f"Generated: `{report['generated_at']}`",
        "",
        f"- Property: `{report['site_url']}`",
        f"- Sitemap: `{report['sitemap_url']}`",
        f"- Sitemap API: **{submission.get('status', 'unknown')}**",
        f"- Sitemap URLs discovered: **{summary['sitemap_urls']}**",
        f"- Page URLs inspected this run: **{summary['inspected_pages']}**",
        f"- Page URLs tracked: **{summary.get('tracked_page_urls', 0)}**",
        f"- Data URLs skipped: **{summary['skipped_data_urls']}**",
    ]

    if summary.get("inspection_skipped_reason"):
        lines.append(f"- Inspection note: {summary['inspection_skipped_reason']}")

    lines.extend(
        [
            "",
            "## Search performance",
            "",
        ]
    )

    if analytics.get("status") == "available":
        lines.extend(
            [
                "| Window | Clicks | Impressions | CTR | Avg. position |",
                "| --- | ---: | ---: | ---: | ---: |",
            ]
        )
        for label in ("7d", "28d"):
            item = analytics.get("windows", {}).get(label, {})
            clicks = _fmt_number(float(item.get("clicks") or 0.0))
            impressions = _fmt_number(float(item.get("impressions") or 0.0))
            ctr = float(item.get("ctr") or 0.0) * 100
            position = float(item.get("position") or 0.0)
            lines.append(
                f"| {label} | {clicks} | {impressions} | {ctr:.1f}% | {position:.1f} |"
            )

        top_queries = analytics.get("top_queries_28d") or []
        if top_queries:
            lines.extend(
                [
                    "",
                    "### Top queries, 28 days",
                    "",
                    "| Query | Clicks | Impressions | Position |",
                    "| --- | ---: | ---: | ---: |",
                ]
            )
            for row in top_queries[:10]:
                key = str(row.get("key") or "").replace("|", "\\|")
                lines.append(
                    f"| {key} | {_fmt_number(float(row.get('clicks') or 0.0))} | "
                    f"{_fmt_number(float(row.get('impressions') or 0.0))} | "
                    f"{float(row.get('position') or 0.0):.1f} |"
                )
    elif analytics.get("status") == "error":
        lines.append(f"Search Analytics error: `{analytics.get('error', 'unknown error')}`")
    else:
        lines.append("Search Analytics is not available until Search Console credentials are configured.")

    lines.extend(
        [
            "",
            "## Indexing status",
            "",
            "| Status | Count | Change |",
            "| --- | ---: | ---: |",
        ]
    )

    counts = summary["status_counts"]
    delta = summary["status_delta"]
    for status in [
        "indexed",
        "unknown",
        "crawled_not_indexed",
        "discovered_not_indexed",
        "blocked",
        "fetch_error",
        "needs_review",
        "not_inspected",
        "inspection_error",
    ]:
        if status in counts or status in delta:
            change = delta.get(status, 0)
            sign = "+" if change > 0 else ""
            lines.append(f"| {status} | {counts.get(status, 0)} | {sign}{change} |")

    queue = [
        item
        for item in report["urls"]
        if item.get("kind") == "page" and item.get("priority") not in {"OK", "SKIP"}
    ]
    queue.sort(
        key=lambda item: (
            PRIORITY_ORDER.get(item.get("priority", "ERROR"), 99),
            item["url"],
        )
    )

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
            lines.append(
                f"\nOnly the first 75 of {len(queue)} queue items are shown here. "
                "The JSON report has all items."
            )

    if report.get("setup_required"):
        lines.extend(
            [
                "",
                "## Setup required",
                "",
                "Google API credentials are not configured yet. The sitemap was parsed, "
                "but no API submission, URL inspection, or Search Analytics request was sent.",
                "Add the service account JSON to the GitHub secret "
                "`GOOGLE_SEARCH_CONSOLE_SERVICE_ACCOUNT` and add that service account to "
                "the Search Console property.",
            ]
        )

    if report.get("fatal_error"):
        lines.extend(["", "## Fatal error", "", f"`{report['fatal_error']}`"])

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
                "priority": "SKIP" if kind == "data" else "REVIEW",
                "status": "data_url_skipped" if kind == "data" else "not_inspected",
                "recommended_action": (
                    "No URL Inspection request is sent for data endpoints by default."
                    if kind == "data"
                    else "Configure Search Console API credentials."
                ),
                "inspection_source": "none",
                "stale": True,
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
        "search_analytics": {"status": "not_configured"},
        "last_inspection_at": None,
        "summary": {},
        "urls": [],
    }

    if not args.credentials:
        report["urls"] = build_setup_only_items(entries)
        status_counts = dict(
            Counter(
                item["status"]
                for item in report["urls"]
                if item["kind"] == "page"
            )
        )
        report["summary"] = {
            "sitemap_urls": len(entries),
            "inspected_pages": 0,
            "tracked_page_urls": sum(
                1 for item in report["urls"] if item["kind"] == "page"
            ),
            "inspected_data_urls": 0,
            "skipped_data_urls": sum(
                1 for item in report["urls"] if item["kind"] == "data"
            ),
            "inspection_errors": 0,
            "inspection_mode": args.inspection_mode,
            "inspection_skipped_reason": "credentials are not configured",
            "status_counts": status_counts,
            "status_delta": compute_delta(status_counts, previous),
        }
        return report, 3 if args.require_credentials else 0

    session = create_authorized_session(args.credentials)
    report["sitemap_submission"] = submit_sitemap(session, args.site_url, args.sitemap_url)

    try:
        report["search_analytics"] = collect_search_analytics(session, args.site_url)
    except Exception as exc:
        report["search_analytics"] = {"status": "error", "error": str(exc)}

    page_entries_all = [
        entry for entry in entries if classify_url_kind(entry["url"]) == "page"
    ]
    data_entries_all = [
        entry for entry in entries if classify_url_kind(entry["url"]) == "data"
    ]
    inspectable_entries = list(page_entries_all)
    if args.include_data:
        inspectable_entries.extend(data_entries_all)

    skipped_reason = ""
    previous_age = previous_report_age_hours(previous)
    if (
        args.min_inspection_interval_hours > 0
        and previous_age is not None
        and previous_age < args.min_inspection_interval_hours
    ):
        selected_entries: list[dict[str, str]] = []
        skipped_reason = (
            f"cooldown active: previous report is {previous_age:.1f}h old; "
            f"minimum interval is {args.min_inspection_interval_hours:.1f}h"
        )
    else:
        selected_entries = select_entries_for_inspection(
            inspectable_entries,
            previous,
            max_inspections=args.max_inspections,
            mode=args.inspection_mode,
            seed=args.selection_seed or datetime.now(timezone.utc).date().isoformat(),
        )

    current_items: list[dict[str, Any]] = []
    inspection_errors = 0

    for index, entry in enumerate(selected_entries):
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
                "recommended_action": (
                    "Check API permissions, quota, and the Search Console property."
                ),
                "error": str(exc),
            }
        current_items.append(item)

        if args.request_delay and index < len(selected_entries) - 1:
            time.sleep(args.request_delay)

    current_page_items = [
        item for item in current_items if item.get("kind") == "page"
    ]
    current_data_by_url = {
        item["url"]: item
        for item in current_items
        if item.get("kind") == "data"
    }

    page_items = merge_rolling_page_inventory(
        page_entries_all,
        current_page_items,
        previous,
    )

    data_items: list[dict[str, Any]] = []
    for entry in data_entries_all:
        current_data = current_data_by_url.get(entry["url"])
        if current_data is not None:
            item = dict(current_data)
            item["inspection_source"] = "current"
            item["stale"] = False
            data_items.append(item)
        else:
            data_items.append(
                {
                    "url": entry["url"],
                    "lastmod": entry.get("lastmod", ""),
                    "kind": "data",
                    "priority": "SKIP",
                    "status": "data_url_skipped",
                    "recommended_action": (
                        "No URL Inspection request is sent for data endpoints by default."
                    ),
                    "inspection_source": "none",
                    "stale": False,
                }
            )

    items = page_items + data_items
    if selected_entries:
        report["last_inspection_at"] = report["generated_at"]
    elif previous:
        report["last_inspection_at"] = previous.get("last_inspection_at")

    status_counts = dict(
        Counter(item["status"] for item in page_items if item["kind"] == "page")
    )
    report["urls"] = items
    report["summary"] = {
        "sitemap_urls": len(entries),
        "inspected_pages": sum(
            1 for item in current_items if item.get("kind") == "page"
        ),
        "inspected_data_urls": sum(
            1 for item in current_items if item.get("kind") == "data"
        ),
        "tracked_page_urls": len(page_items),
        "skipped_data_urls": sum(
            1 for item in data_items if item.get("status") == "data_url_skipped"
        ),
        "inspection_errors": inspection_errors,
        "inspection_mode": args.inspection_mode,
        "inspection_skipped_reason": skipped_reason,
        "previous_report_age_hours": previous_age,
        "status_counts": status_counts,
        "status_delta": compute_delta(status_counts, previous),
    }

    if selected_entries and inspection_errors == len(selected_entries):
        return report, 2
    return report, 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--site-url",
        required=True,
        help="Exact Search Console property, including trailing slash for URL-prefix properties.",
    )
    parser.add_argument(
        "--sitemap-url",
        required=True,
        help="Public sitemap or sitemap index URL.",
    )
    parser.add_argument(
        "--credentials",
        default=os.getenv("GOOGLE_APPLICATION_CREDENTIALS"),
        help="Service account JSON file.",
    )
    parser.add_argument(
        "--require-credentials",
        action="store_true",
        help="Fail production runs when Search Console credentials are missing.",
    )
    parser.add_argument(
        "--previous-report",
        help="Previous JSON report used for rolling status and deltas.",
    )
    parser.add_argument(
        "--output-dir",
        default="reports/seo/google-search",
        help="Directory for JSON and Markdown reports.",
    )
    parser.add_argument(
        "--max-inspections",
        type=int,
        default=100,
        help="Maximum URL Inspection API calls per run. Zero disables inspections.",
    )
    parser.add_argument(
        "--inspection-mode",
        choices=("priority", "rotate", "all"),
        default="priority",
        help="How to select URLs when the inspection budget is smaller than the sitemap.",
    )
    parser.add_argument(
        "--selection-seed",
        default="",
        help="Stable seed for rotation. Defaults to the current UTC date.",
    )
    parser.add_argument(
        "--min-inspection-interval-hours",
        type=float,
        default=0.0,
        help="Skip URL Inspection when the previous report is newer than this interval.",
    )
    parser.add_argument(
        "--max-sitemap-depth",
        type=int,
        default=4,
        help="Maximum sitemap index nesting depth.",
    )
    parser.add_argument(
        "--request-delay",
        type=float,
        default=0.15,
        help="Delay between URL Inspection calls in seconds.",
    )
    parser.add_argument(
        "--include-data",
        action="store_true",
        help="Also inspect JSON/YAML/XML/TXT/CSV sitemap URLs.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.max_inspections < 0:
        raise SystemExit("--max-inspections must be zero or greater")
    if args.min_inspection_interval_hours < 0:
        raise SystemExit("--min-inspection-interval-hours must be zero or greater")

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
            "search_analytics": {"status": "error", "error": str(exc)},
            "last_inspection_at": None,
            "summary": {
                "sitemap_urls": 0,
                "inspected_pages": 0,
                "tracked_page_urls": 0,
                "inspected_data_urls": 0,
                "skipped_data_urls": 0,
                "inspection_errors": 0,
                "inspection_mode": args.inspection_mode,
                "inspection_skipped_reason": "",
                "status_counts": {},
                "status_delta": {},
            },
            "urls": [],
            "fatal_error": str(exc),
        }
        exit_code = 1

    json_path = output_dir / "google-indexing.json"
    markdown_path = output_dir / "google-indexing.md"
    json_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    markdown_path.write_text(build_markdown(report), encoding="utf-8")

    print(f"Wrote {json_path}")
    print(f"Wrote {markdown_path}")
    if report.get("fatal_error"):
        print(f"ERROR: {report['fatal_error']}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
