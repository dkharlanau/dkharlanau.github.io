#!/usr/bin/env python3
"""Check that analytics is present once in built HTML and absent elsewhere."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


GA4_SRC_RE = re.compile(
    r"https://www\.googletagmanager\.com/gtag/js\?id=(G-[A-Z0-9]+)"
)
GA4_CONFIG_RE = re.compile(r"gtag\(\s*['\"]config['\"]\s*,\s*['\"](G-[A-Z0-9]+)['\"]")
GTM_RE = re.compile(r"\bGTM-[A-Z0-9]+\b")
NON_HTML_SUFFIXES = {".xml", ".json", ".txt"}
NAMED_NON_HTML = {"robots.txt", "llms.txt", "llms-full.txt"}


@dataclass(frozen=True)
class AnalyticsFinding:
    path: str
    reason: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def ga4_ids(content: str) -> tuple[list[str], list[str]]:
    return GA4_SRC_RE.findall(content), GA4_CONFIG_RE.findall(content)


def gtm_ids(content: str) -> list[str]:
    # Deduplicate each ID on a page, but keep multiple container IDs visible.
    return sorted(set(GTM_RE.findall(content)))


def classify_html(content: str) -> tuple[str, str | None]:
    src_ids, config_ids = ga4_ids(content)
    containers = gtm_ids(content)

    unique_ga4 = set(src_ids) | set(config_ids)
    has_ga4 = bool(src_ids or config_ids)
    has_gtm = bool(containers)

    if has_ga4 and has_gtm:
        return "duplicate", "contains both GA4 and GTM markers"
    if has_gtm:
        if len(containers) == 1 and len(GTM_RE.findall(content)) == 1:
            return "tagged", None
        return "duplicate", "contains duplicate or multiple GTM markers"
    if has_ga4:
        if len(unique_ga4) != 1:
            return "duplicate", "contains multiple GA4 measurement IDs"
        measurement_id = next(iter(unique_ga4))
        src_count = src_ids.count(measurement_id)
        config_count = config_ids.count(measurement_id)
        if src_count == 1 and config_count == 1:
            return "tagged", None
        if src_count == 0 or config_count == 0:
            return "missing", "incomplete GA4 snippet"
        return "duplicate", "contains duplicate GA4 script or config markers"
    return "missing", "analytics marker missing"


def should_scan_non_html(path: Path) -> bool:
    return path.suffix.lower() in NON_HTML_SUFFIXES or path.name in NAMED_NON_HTML


def has_analytics_marker(content: str) -> bool:
    return bool(GA4_SRC_RE.search(content) or GA4_CONFIG_RE.search(content) or GTM_RE.search(content))


def check_site(site_dir: Path) -> tuple[int, dict[str, int], list[AnalyticsFinding]]:
    html_files = sorted(site_dir.rglob("*.html"))
    findings: list[AnalyticsFinding] = []
    tagged = 0
    missing = 0
    duplicate = 0

    for path in html_files:
        rel = path.relative_to(site_dir).as_posix()
        status, reason = classify_html(read_text(path))
        if status == "tagged":
            tagged += 1
        elif status == "missing":
            missing += 1
            findings.append(AnalyticsFinding(rel, reason or "analytics marker missing"))
        else:
            duplicate += 1
            findings.append(AnalyticsFinding(rel, reason or "duplicate analytics marker"))

    non_html_with_analytics = 0
    for path in sorted(p for p in site_dir.rglob("*") if p.is_file() and should_scan_non_html(p)):
        content = read_text(path)
        if has_analytics_marker(content):
            non_html_with_analytics += 1
            findings.append(
                AnalyticsFinding(
                    path.relative_to(site_dir).as_posix(),
                    "non-HTML file contains analytics marker",
                )
            )

    summary = {
        "total_html_pages": len(html_files),
        "tagged_html_pages": tagged,
        "missing_html_pages": missing,
        "duplicate_tag_pages": duplicate,
        "non_html_files_with_analytics": non_html_with_analytics,
    }
    exit_code = 0 if not findings else 2
    return exit_code, summary, findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check GA4/GTM analytics coverage in a built Jekyll site."
    )
    parser.add_argument("--site-dir", default="_site", help="Built site directory.")
    args = parser.parse_args(argv)

    site_dir = Path(args.site_dir)
    if not site_dir.is_dir():
        print(f"Missing directory: {site_dir}. Build the site before running.")
        return 1

    exit_code, summary, findings = check_site(site_dir)
    print(f"Total HTML pages: {summary['total_html_pages']}")
    print(f"Tagged HTML pages: {summary['tagged_html_pages']}")
    print(f"Missing HTML pages: {summary['missing_html_pages']}")
    print(f"Duplicate-tag pages: {summary['duplicate_tag_pages']}")
    print(f"Non-HTML files with analytics snippets: {summary['non_html_files_with_analytics']}")

    if findings:
        print("Analytics coverage failures:")
        for finding in findings[:300]:
            print(f"- {finding.path}: {finding.reason}")
        if len(findings) > 300:
            print(f"... and {len(findings) - 300} more")

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
