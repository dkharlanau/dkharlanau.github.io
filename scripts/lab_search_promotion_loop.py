#!/usr/bin/env python3
"""Rank Lab pages for search publication and safely promote reviewed pages.

The loop combines three independent signals:
- factual readiness from labs/assessment/data/promotion-readiness.json
- search-intent ownership from _data/labs/search_intents.yml
- source-level search quality (metadata, body, links, evidence, H1, freshness)

It never marks a draft page verified. With --apply, only pages already marked
status=reviewed and verified=true can be changed from noindex to indexable.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from search_discoverability_inventory import PageRecord, build_records, parse_frontmatter


HTML_TAG_RE = re.compile(r"<[^>]+>", re.DOTALL)
LIQUID_TAG_RE = re.compile(r"{%.*?%}|{{.*?}}", re.DOTALL)
HTML_LINK_RE = re.compile(r'href=["\']([^"\']+)["\']', re.IGNORECASE)
MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HTML_H1_RE = re.compile(r"<h1\b", re.IGNORECASE)
MD_H1_RE = re.compile(r"^#\s+", re.MULTILINE)
URL_RE = re.compile(r"https?://[^\s\]\[()<>{}\"']+")
SOURCE_DATA_RE = re.compile(r"site\.data\.labs\.enterprise_context\.sources\.([A-Za-z0-9_]+)")
DRAFT_MARKERS = ("TODO", "FIXME", "TBD", "lorem ipsum")


@dataclass
class PromotionCandidate:
    route: str
    source_path: str
    title: str
    search_intent: str
    publication_state: str
    assessment_priority: str
    factual_status: str
    human_verification_required: bool
    score: int
    word_count: int
    internal_links: int
    external_links: int
    evidence_urls: int
    h1_count: int
    reasons: list[str]


def load_search_intents(repo: Path) -> dict[str, dict]:
    path = repo / "_data" / "labs" / "search_intents.yml"
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    routes = data.get("routes") if isinstance(data, dict) else {}
    return routes if isinstance(routes, dict) else {}


def load_assessment_readiness(repo: Path) -> dict[str, dict]:
    path = repo / "labs" / "assessment" / "data" / "promotion-readiness.json"
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {
        str(item.get("route")): item
        for item in payload.get("items", [])
        if item.get("route")
    }


def read_source(repo: Path, record: PageRecord) -> tuple[str, dict, str]:
    path = repo / record.source_path
    text = path.read_text(encoding="utf-8", errors="ignore")
    fm = parse_frontmatter(path) or {}
    end = text.find("\n---", 4)
    body = text[end + 4 :] if end >= 0 else text
    return text, fm, body


def text_word_count(body: str) -> int:
    plain = LIQUID_TAG_RE.sub(" ", body)
    plain = HTML_TAG_RE.sub(" ", plain)
    return len(re.findall(r"\b[A-Za-z0-9][A-Za-z0-9+./_-]*\b", plain))


def link_counts(body: str) -> tuple[int, int]:
    links = HTML_LINK_RE.findall(body) + MD_LINK_RE.findall(body)
    internal = 0
    external = 0
    for link in links:
        value = link.strip()
        if not value or value.startswith("#"):
            continue
        if value.startswith("/"):
            internal += 1
        elif value.startswith("http://") or value.startswith("https://"):
            external += 1
    return internal, external


def h1_count(body: str) -> int:
    return len(HTML_H1_RE.findall(body)) + len(MD_H1_RE.findall(body))


def recursive_urls(value: Any) -> set[str]:
    urls: set[str] = set()
    if isinstance(value, dict):
        for item in value.values():
            urls.update(recursive_urls(item))
    elif isinstance(value, list):
        for item in value:
            urls.update(recursive_urls(item))
    elif isinstance(value, str):
        urls.update(URL_RE.findall(value))
    return urls


def evidence_urls(repo: Path, body: str) -> set[str]:
    urls = set(URL_RE.findall(body))
    for name in SOURCE_DATA_RE.findall(body):
        path = repo / "_data" / "labs" / "enterprise_context" / "sources" / f"{name}.yml"
        if not path.exists():
            continue
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError:
            continue
        urls.update(recursive_urls(data))
    return urls


def quality_score(
    repo: Path,
    record: PageRecord,
    intents: dict[str, dict],
    readiness: dict[str, dict],
) -> PromotionCandidate:
    _text, fm, body = read_source(repo, record)
    words = text_word_count(body)
    internal, external = link_counts(body)
    h1s = h1_count(body)
    evidence = evidence_urls(repo, body)
    score = 0
    reasons: list[str] = []

    intent_entry = intents.get(record.route) or {}
    explicit_intent = str(fm.get("search_intent") or intent_entry.get("primary") or "").strip()
    search_intent = explicit_intent or record.search_intent or record.title

    assessment = readiness.get(record.route) or {}
    factual = assessment.get("factual_review") or {}
    assessment_priority = str(assessment.get("priority") or "")
    factual_status = str(factual.get("status") or "not_reviewed")
    human_required = bool(factual.get("human_verification_required", False))

    title_len = len(record.title)
    if 30 <= title_len <= 80:
        score += 7
    elif record.title:
        score += 4
        reasons.append("title length should be reviewed")
    else:
        reasons.append("missing title")

    desc_len = len(record.description)
    if 90 <= desc_len <= 180:
        score += 10
    elif record.description:
        score += 5
        reasons.append("description length should be reviewed")
    else:
        reasons.append("missing description")

    if explicit_intent:
        score += 5
    else:
        reasons.append("search intent is inferred from title")

    if words >= 900:
        score += 18
    elif words >= 500:
        score += 14
    elif words >= 250:
        score += 8
    else:
        reasons.append("thin source body")

    if h1s == 1:
        score += 7
    else:
        reasons.append(f"expected one H1, found {h1s}")

    if internal >= 8:
        score += 15
    elif internal >= 4:
        score += 11
    elif internal >= 2:
        score += 6
    else:
        reasons.append("weak internal-link coverage")

    evidence_count = len(evidence)
    if evidence_count >= 6:
        score += 23
    elif evidence_count >= 3:
        score += 18
    elif evidence_count >= 1:
        score += 9
    else:
        reasons.append("no resolvable evidence URLs")

    if fm.get("last_modified_at") or fm.get("last_reviewed") or fm.get("updated"):
        score += 5
    else:
        reasons.append("missing review/update date")

    if fm.get("tags"):
        score += 5
    else:
        reasons.append("missing topic tags")

    if ".json" in body or fm.get("enterprise_context_graph"):
        score += 5

    if any(marker.lower() in body.lower() for marker in DRAFT_MARKERS):
        score = max(0, score - 15)
        reasons.append("contains draft placeholder marker")

    score = min(score, 100)

    if record.classification == "REVIEW_TO_INDEX":
        state = "READY_TO_PROMOTE" if score >= 70 else "PROMOTE_BLOCKED"
    elif record.classification == "KEEP_NOINDEX":
        if factual_status == "source_supported" and assessment_priority == "P1" and score >= 70:
            state = "HUMAN_VERIFY_NEXT"
        elif score >= 80:
            state = "REVIEW_NEXT"
        elif score >= 65:
            state = "REVIEW_LATER"
        else:
            state = "WORKING"
    else:
        state = record.classification

    if factual_status == "source_supported":
        reasons.append("load-bearing reviewed claims are source-supported")
    elif assessment_priority == "P0":
        reasons.append("assessment evidence review has a P0 blocker")

    return PromotionCandidate(
        route=record.route,
        source_path=record.source_path,
        title=record.title,
        search_intent=search_intent,
        publication_state=state,
        assessment_priority=assessment_priority,
        factual_status=factual_status,
        human_verification_required=human_required,
        score=score,
        word_count=words,
        internal_links=internal,
        external_links=external,
        evidence_urls=evidence_count,
        h1_count=h1s,
        reasons=reasons,
    )


def replace_frontmatter_scalar(text: str, key: str, value: str) -> str:
    end = text.find("\n---", 4)
    if end < 0:
        raise ValueError("missing front matter terminator")
    front = text[:end]
    rest = text[end:]
    pattern = re.compile(rf"(?m)^{re.escape(key)}\s*:\s*.*$")
    replacement = f"{key}: {value}"
    if pattern.search(front):
        front = pattern.sub(replacement, front, count=1)
    else:
        front = front + "\n" + replacement
    return front + rest


def apply_promotions(repo: Path, candidates: list[PromotionCandidate]) -> list[str]:
    changed: list[str] = []
    for candidate in candidates:
        if candidate.publication_state != "READY_TO_PROMOTE":
            continue
        path = repo / candidate.source_path
        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(path) or {}
        if fm.get("verified") is not True or str(fm.get("status") or "").lower() != "reviewed":
            raise RuntimeError(f"refusing to promote unreviewed page: {candidate.source_path}")
        text = replace_frontmatter_scalar(text, "robots", "index,follow")
        text = replace_frontmatter_scalar(text, "sitemap", "true")
        path.write_text(text, encoding="utf-8")
        changed.append(candidate.source_path)
    return changed


def write_reports(repo: Path, candidates: list[PromotionCandidate], output_dir: str) -> None:
    out = repo / output_dir
    out.mkdir(parents=True, exist_ok=True)
    csv_path = out / "lab-promotion-queue.csv"
    md_path = out / "lab-promotion-queue.md"

    fields = [
        "route", "source_path", "publication_state", "assessment_priority", "factual_status",
        "human_verification_required", "score", "title", "search_intent", "word_count",
        "internal_links", "external_links", "evidence_urls", "h1_count", "reasons",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for candidate in candidates:
            row = candidate.__dict__.copy()
            row["reasons"] = "; ".join(candidate.reasons)
            writer.writerow({field: row.get(field, "") for field in fields})

    lines = [
        "# Lab Search Promotion Queue",
        "",
        "The score prioritizes review. It does not replace human verification.",
        "",
        "| State | Assessment | Facts | Score | Route | Evidence | Links | Search intent |",
        "|---|---|---|---:|---|---:|---:|---|",
    ]
    for candidate in candidates:
        lines.append(
            f"| {candidate.publication_state} | {candidate.assessment_priority or '—'} | "
            f"{candidate.factual_status} | {candidate.score} | `{candidate.route}` | "
            f"{candidate.evidence_urls} | {candidate.internal_links} | {candidate.search_intent or candidate.title} |"
        )
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-dir", default=".")
    parser.add_argument("--output-dir", default="reports/seo")
    parser.add_argument("--apply", action="store_true", help="Promote only READY_TO_PROMOTE pages")
    args = parser.parse_args()

    repo = Path(args.repo_dir).resolve()
    intents = load_search_intents(repo)
    readiness = load_assessment_readiness(repo)
    records = [record for record in build_records(repo) if record.route.startswith("/labs/")]
    candidates = [quality_score(repo, record, intents, readiness) for record in records]
    state_order = {
        "READY_TO_PROMOTE": 0,
        "HUMAN_VERIFY_NEXT": 1,
        "PROMOTE_BLOCKED": 2,
        "REVIEW_NEXT": 3,
        "REVIEW_LATER": 4,
        "WORKING": 5,
    }
    candidates.sort(key=lambda item: (state_order.get(item.publication_state, 9), -item.score, item.route))
    write_reports(repo, candidates, args.output_dir)

    ready = [item for item in candidates if item.publication_state == "READY_TO_PROMOTE"]
    human_next = [item for item in candidates if item.publication_state == "HUMAN_VERIFY_NEXT"]
    print(f"Lab promotion loop: {len(candidates)} routes")
    print(f"  Ready to promote: {len(ready)}")
    print(f"  Human verify next: {len(human_next)}")
    for item in candidates[:25]:
        print(
            f"  {item.score:3d} {item.publication_state:18s} "
            f"{item.assessment_priority or '-':2s} {item.factual_status:18s} {item.route}"
        )

    if args.apply:
        changed = apply_promotions(repo, candidates)
        print(f"  Promoted: {len(changed)}")
        for path in changed:
            print(f"  - {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
