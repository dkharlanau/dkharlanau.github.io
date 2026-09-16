#!/usr/bin/env python3
"""Build a focused Google indexation recovery queue from Search Console output.

This does not submit URLs to Google and does not redefine publication eligibility.
It consumes google-indexing.json, overlays an explicit business-priority corpus,
checks live rendered technical signals, and produces a short Search Console queue.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

DEFAULT_USER_AGENT = "DKH-Indexation-Recovery/1.0 (+https://dkharlanau.github.io/)"
REQUESTABLE_ACTIONS = {"REQUEST_INDEXING"}


@dataclass(frozen=True)
class LiveCheck:
    url: str
    http_status: int | None
    robots: str
    canonical: str
    canonical_self: bool | None
    indexable: bool
    error: str = ""

    def as_dict(self) -> dict[str, Any]:
        return {
            "url": self.url,
            "http_status": self.http_status,
            "robots": self.robots,
            "canonical": self.canonical,
            "canonical_self": self.canonical_self,
            "indexable": self.indexable,
            "error": self.error,
        }


class _HeadParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.robots_values: list[str] = []
        self.canonical = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {str(key).lower(): (value or "") for key, value in attrs}
        if tag.lower() == "meta" and values.get("name", "").lower() in {"robots", "googlebot"}:
            if values.get("content"):
                self.robots_values.append(values["content"])
        if tag.lower() == "link" and "canonical" in values.get("rel", "").lower().split():
            if values.get("href") and not self.canonical:
                self.canonical = values["href"]


def _normalize_url(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path or "/"
    if not Path(path).suffix and not path.endswith("/"):
        path += "/"
    return parsed._replace(path=path, query="", fragment="").geturl()


def _same_canonical(url: str, canonical: str) -> bool:
    if not canonical:
        return False
    return _normalize_url(url) == _normalize_url(urljoin(url, canonical))


def fetch_live_check(url: str, *, timeout: int = 20) -> LiveCheck:
    request = Request(
        url,
        headers={
            "User-Agent": DEFAULT_USER_AGENT,
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            status = int(getattr(response, "status", response.getcode()))
            content_type = str(response.headers.get("Content-Type") or "")
            x_robots = str(response.headers.get("X-Robots-Tag") or "")
            body = response.read(2_000_000).decode(
                response.headers.get_content_charset() or "utf-8",
                errors="replace",
            )
    except HTTPError as exc:
        return LiveCheck(url, int(exc.code), "", "", None, False, f"HTTP {exc.code}")
    except (URLError, TimeoutError, OSError) as exc:
        return LiveCheck(url, None, "", "", None, False, str(exc))

    if status != 200:
        return LiveCheck(url, status, x_robots, "", None, False, f"HTTP {status}")
    if "html" not in content_type.lower():
        return LiveCheck(
            url,
            status,
            x_robots,
            "",
            None,
            False,
            f"unexpected content type: {content_type or 'unknown'}",
        )

    parser = _HeadParser()
    parser.feed(body)
    robots_values = [x_robots, *parser.robots_values]
    robots = ", ".join(value for value in robots_values if value).strip()
    noindex = "noindex" in robots.lower()
    canonical = urljoin(url, parser.canonical) if parser.canonical else ""
    canonical_self = _same_canonical(url, canonical) if canonical else False
    indexable = bool(status == 200 and not noindex and canonical_self)
    error = ""
    if noindex:
        error = "rendered robots contains noindex"
    elif not canonical:
        error = "missing rendered canonical"
    elif not canonical_self:
        error = "rendered canonical is not self-referential"

    return LiveCheck(url, status, robots, canonical, canonical_self, indexable, error)


def load_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _priority_map(config: dict[str, Any]) -> dict[str, dict[str, Any]]:
    base = str(config.get("site_url") or "").rstrip("/")
    result: dict[str, dict[str, Any]] = {}
    for entry in config.get("priority_routes") or []:
        path = str(entry.get("path") or "").strip()
        if not path.startswith("/"):
            raise ValueError(f"Priority route must start with '/': {path!r}")
        url = f"{base}{path}" if base else path
        result[_normalize_url(url)] = dict(entry)
    return result


def recovery_action(status: str, live: LiveCheck | None) -> str:
    if live is not None and not live.indexable:
        return "FIX_TECHNICAL_GATE"
    if status == "unknown":
        return "REQUEST_INDEXING"
    if status == "not_inspected":
        return "INSPECT_FIRST"
    if status == "discovered_not_indexed":
        return "STRENGTHEN_DISCOVERY"
    if status == "crawled_not_indexed":
        return "QUALITY_REVIEW_THEN_REQUEST"
    if status in {"blocked", "fetch_error"}:
        return "FIX_TECHNICAL_GATE"
    if status in {"needs_review", "inspection_error"}:
        return "REVIEW_FIRST"
    return "NO_ACTION"


def _status_score(config: dict[str, Any], status: str) -> int:
    return int((config.get("status_scores") or {}).get(status, 0))


def _tier_score(config: dict[str, Any], tier: str) -> int:
    return int((config.get("tier_scores") or {}).get(tier, 0))


def _prefix_score(config: dict[str, Any], path: str) -> int:
    score = 0
    for rule in config.get("prefix_rules") or []:
        prefix = str(rule.get("prefix") or "")
        if prefix and path.startswith(prefix):
            score = max(score, int(rule.get("score") or 0))
    return score


def build_recovery(
    report: dict[str, Any],
    config: dict[str, Any],
    *,
    live_checker: Callable[[str], LiveCheck] | None = fetch_live_check,
) -> dict[str, Any]:
    priority_map = _priority_map(config)
    page_items = {
        _normalize_url(str(item.get("url"))): item
        for item in report.get("urls") or []
        if item.get("kind") == "page" and item.get("url")
    }
    candidate_statuses = set(config.get("candidate_statuses") or [])
    manual_limit = max(0, int(config.get("manual_request_limit") or 0))

    corpus: list[dict[str, Any]] = []
    missing: list[dict[str, Any]] = []
    candidates: list[dict[str, Any]] = []

    for url, meta in priority_map.items():
        item = page_items.get(url)
        if item is None:
            missing.append(
                {
                    "url": url,
                    "path": meta.get("path", ""),
                    "tier": meta.get("tier", "P2"),
                    "focus": meta.get("focus", ""),
                    "reason": meta.get("reason", ""),
                }
            )
            continue

        status = str(item.get("status") or "needs_review")
        parsed_path = urlparse(url).path or "/"
        live = live_checker(url) if live_checker is not None else None
        action = recovery_action(status, live)
        tier = str(meta.get("tier") or "P2")
        score = (
            _status_score(config, status)
            + _tier_score(config, tier)
            + _prefix_score(config, parsed_path)
        )
        if item.get("inspection_source") == "current":
            score += int(config.get("current_inspection_bonus") or 0)

        row = {
            "url": url,
            "path": meta.get("path", parsed_path),
            "tier": tier,
            "focus": meta.get("focus", ""),
            "reason": meta.get("reason", ""),
            "status": status,
            "gsc_priority": item.get("priority", ""),
            "inspection_source": item.get("inspection_source", ""),
            "stale": bool(item.get("stale", False)),
            "last_crawl_time": item.get("last_crawl_time"),
            "user_canonical": item.get("user_canonical"),
            "google_canonical": item.get("google_canonical"),
            "action": action,
            "score": score,
            "live_check": live.as_dict() if live is not None else None,
        }
        corpus.append(row)
        if status in candidate_statuses and action != "NO_ACTION":
            candidates.append(row)

    candidates.sort(key=lambda item: (-int(item["score"]), str(item["url"])))
    requestable = [row for row in candidates if row["action"] in REQUESTABLE_ACTIONS]
    manual_queue = requestable[:manual_limit]

    status_counts = Counter(str(row["status"]) for row in corpus)
    action_counts = Counter(str(row["action"]) for row in corpus)
    configured_count = len(priority_map)
    indexed_count = status_counts.get("indexed", 0)

    return {
        "generated_from": report.get("generated_at"),
        "site_url": config.get("site_url"),
        "manual_request_limit": manual_limit,
        "summary": {
            "configured_priority_routes": configured_count,
            "present_priority_routes": len(corpus),
            "missing_priority_routes": len(missing),
            "indexed_priority_routes": indexed_count,
            "priority_indexed_pct": (
                round(indexed_count / configured_count * 100, 1) if configured_count else 0.0
            ),
            "recovery_candidates": len(candidates),
            "manual_request_candidates": len(requestable),
            "manual_queue_size": len(manual_queue),
            "status_counts": dict(sorted(status_counts.items())),
            "action_counts": dict(sorted(action_counts.items())),
        },
        "manual_request_queue": manual_queue,
        "recovery_candidates": candidates,
        "priority_corpus": sorted(corpus, key=lambda item: (item["tier"], item["url"])),
        "missing_priority_routes": missing,
    }


def build_markdown(recovery: dict[str, Any]) -> str:
    summary = recovery["summary"]
    lines = [
        "# Google Indexation Recovery Queue",
        "",
        f"Source report: `{recovery.get('generated_from') or 'unknown'}`",
        "",
        "This report does **not** submit URLs to Google. It narrows the site's already "
        "indexable/search-tracked corpus to business-priority pages, checks the live "
        "rendered technical gate, and produces a short Search Console operator queue.",
        "",
        "## Priority corpus KPI",
        "",
        f"- Configured priority routes: **{summary['configured_priority_routes']}**",
        f"- Present in Google Search inventory: **{summary['present_priority_routes']}**",
        f"- Indexed priority routes: **{summary['indexed_priority_routes']}** "
        f"(**{summary['priority_indexed_pct']:.1f}%**)",
        f"- Recovery candidates: **{summary['recovery_candidates']}**",
        f"- Manual Request Indexing candidates: **{summary['manual_request_candidates']}**",
        f"- Manual queue size (capped): **{summary['manual_queue_size']}**",
        "",
        "## Manual Search Console queue",
        "",
        "Only `unknown` URLs that pass the live HTTP/robots/self-canonical gate appear "
        "here. In Search Console, run **Test live URL** first; use **Request indexing** "
        "only when the live test remains indexable.",
        "",
    ]

    queue = recovery.get("manual_request_queue") or []
    if queue:
        lines.extend(
            [
                "| Rank | Tier | Focus | Status | URL | Reason |",
                "| ---: | --- | --- | --- | --- | --- |",
            ]
        )
        for rank, row in enumerate(queue, start=1):
            url = str(row["url"]).replace("|", "%7C")
            reason = str(row.get("reason") or "").replace("|", "\\|")
            focus = str(row.get("focus") or "").replace("|", "\\|")
            lines.append(
                f"| {rank} | {row['tier']} | {focus} | {row['status']} | "
                f"[{url}]({url}) | {reason} |"
            )
    else:
        lines.append("No URL currently qualifies for the manual Request Indexing queue.")

    lines.extend(
        [
            "",
            "## Recovery actions",
            "",
            "| Action | Count | Meaning |",
            "| --- | ---: | --- |",
        ]
    )
    meanings = {
        "REQUEST_INDEXING": "Live technical gate passed; run Test live URL, then request indexing.",
        "INSPECT_FIRST": "No reliable GSC inspection status yet; inspect before deciding.",
        "STRENGTHEN_DISCOVERY": "Google knows the URL but has not crawled it; improve internal discovery first.",
        "QUALITY_REVIEW_THEN_REQUEST": "Google crawled the page but did not select it; improve value/signals before another request.",
        "FIX_TECHNICAL_GATE": "HTTP, robots, canonical, block, or fetch issue must be fixed first.",
        "REVIEW_FIRST": "Inspection data is ambiguous or errored; review before requesting.",
        "NO_ACTION": "Already indexed or no recovery action is needed.",
    }
    for action, count in sorted((summary.get("action_counts") or {}).items()):
        lines.append(f"| {action} | {count} | {meanings.get(action, '')} |")

    lines.extend(
        [
            "",
            "## Full priority corpus",
            "",
            "| Tier | Focus | Status | Action | Live gate | URL |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in recovery.get("priority_corpus") or []:
        live = row.get("live_check") or {}
        live_gate = "pass" if live.get("indexable") else "fail"
        if row.get("live_check") is None:
            live_gate = "not checked"
        url = str(row["url"]).replace("|", "%7C")
        lines.append(
            f"| {row['tier']} | {row.get('focus','')} | {row['status']} | "
            f"{row['action']} | {live_gate} | [{url}]({url}) |"
        )

    missing = recovery.get("missing_priority_routes") or []
    if missing:
        lines.extend(["", "## Missing configured priority routes", ""])
        for row in missing:
            lines.append(f"- `{row['url']}` — configured but absent from the Search pipeline inventory.")

    lines.extend(
        [
            "",
            "## Operating rule",
            "",
            "Do not use Request Indexing as a substitute for content quality or internal "
            "discovery. `Crawled - currently not indexed`, technical failures, and ambiguous "
            "inspection states stay out of the manual request queue until their underlying "
            "issue is addressed.",
        ]
    )
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", required=True, help="google-indexing.json produced by the Google Search pipeline.")
    parser.add_argument(
        "--config",
        default="config/indexation-recovery.json",
        help="Business-priority recovery configuration.",
    )
    parser.add_argument(
        "--output-dir",
        default="reports/seo/google-search",
        help="Output directory for recovery JSON and Markdown.",
    )
    parser.add_argument(
        "--skip-live-checks",
        action="store_true",
        help="Build the queue without fetching live rendered pages.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = load_json(args.report)
    config = load_json(args.config)
    recovery = build_recovery(
        report,
        config,
        live_checker=None if args.skip_live_checks else fetch_live_check,
    )

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "indexation-recovery.json"
    markdown_path = output_dir / "indexation-recovery.md"
    json_path.write_text(
        json.dumps(recovery, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    markdown_path.write_text(build_markdown(recovery), encoding="utf-8")
    print(f"Wrote {json_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
