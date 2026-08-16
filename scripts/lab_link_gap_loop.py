#!/usr/bin/env python3
"""Find internal-link gaps between Lab search-intent routes.

The loop uses existing source links, route hierarchy, tags and explicit search intents.
It produces contextual link suggestions but never edits article prose automatically.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path

import yaml

from search_discoverability_inventory import build_records, parse_frontmatter


HTML_LINK_RE = re.compile(r'href=["\'](/labs/[^"\'#?]+/?)["\']', re.IGNORECASE)
MD_LINK_RE = re.compile(r"\[[^\]]+\]\((/labs/[^)#?]+/?)(?:#[^)]+)?\)")
WORD_RE = re.compile(r"[a-z0-9]+")
STOP = {"sap", "and", "with", "the", "for", "from", "process", "architecture", "integration", "s4hana"}


def load_registry(repo: Path) -> dict:
    path = repo / "_data" / "labs" / "search_intents.yml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return (data or {}).get("routes", {}) if isinstance(data, dict) else {}


def source_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    end = text.find("\n---", 4)
    return text[end + 4 :] if text.startswith("---\n") and end >= 0 else text


def local_links(body: str) -> set[str]:
    return set(HTML_LINK_RE.findall(body) + MD_LINK_RE.findall(body))


def tokens(text: str) -> set[str]:
    return {word for word in WORD_RE.findall(text.lower()) if word not in STOP and len(word) > 1}


def jaccard(left: set[str], right: set[str]) -> float:
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def parent(route: str) -> str:
    parts = [item for item in route.split("/") if item]
    if len(parts) <= 2:
        return "/labs/"
    return "/" + "/".join(parts[:-1]) + "/"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-dir", default=".")
    parser.add_argument("--output-dir", default="reports/seo")
    args = parser.parse_args()

    repo = Path(args.repo_dir).resolve()
    registry = load_registry(repo)
    records = {record.route: record for record in build_records(repo) if record.route in registry}

    meta: dict[str, dict] = {}
    inbound: dict[str, set[str]] = defaultdict(set)
    for route, record in records.items():
        path = repo / record.source_path
        fm = parse_frontmatter(path) or {}
        body = source_body(path)
        links = local_links(body)
        for target in links:
            if target in registry:
                inbound[target].add(route)
        meta[route] = {
            "path": record.source_path,
            "title": record.title,
            "intent": str((registry.get(route) or {}).get("primary") or record.title),
            "tags": {str(tag).lower() for tag in (fm.get("tags") or [])},
            "links": links,
        }

    rows: list[dict] = []
    for route, item in sorted(meta.items()):
        candidates: list[tuple[float, str]] = []
        for other_route, other in meta.items():
            if other_route == route or other_route in item["links"]:
                continue
            intent_score = jaccard(tokens(item["intent"]), tokens(other["intent"]))
            tag_score = jaccard(item["tags"], other["tags"])
            hierarchy_bonus = 0.18 if parent(route) == parent(other_route) else 0.0
            score = (0.58 * intent_score) + (0.32 * tag_score) + hierarchy_bonus
            if score >= 0.12:
                candidates.append((score, other_route))
        candidates.sort(key=lambda value: (-value[0], value[1]))
        suggestions = [target for _score, target in candidates[:4]]
        existing_mapped = sorted(target for target in item["links"] if target in registry)
        rows.append({
            "route": route,
            "source_path": item["path"],
            "inbound_count": len(inbound[route]),
            "outbound_mapped_count": len(existing_mapped),
            "existing_mapped_links": " | ".join(existing_mapped),
            "suggested_links": " | ".join(suggestions),
            "priority": "HIGH" if len(inbound[route]) == 0 or len(existing_mapped) < 2 else "NORMAL",
        })

    out = repo / args.output_dir
    out.mkdir(parents=True, exist_ok=True)
    csv_path = out / "lab-link-gaps.csv"
    md_path = out / "lab-link-gaps.md"
    fields = [
        "route", "source_path", "priority", "inbound_count", "outbound_mapped_count",
        "existing_mapped_links", "suggested_links",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    high = [row for row in rows if row["priority"] == "HIGH"]
    lines = [
        "# Lab Internal Link Gap Queue",
        "",
        "Suggestions use search intent, topic tags and route hierarchy. They are review hints, not automatic prose edits.",
        "",
        f"- Intent-mapped routes: **{len(rows)}**",
        f"- High-priority link gaps: **{len(high)}**",
        "",
        "| Priority | Route | Inbound | Mapped outbound | Suggested related routes |",
        "|---|---|---:|---:|---|",
    ]
    for row in sorted(rows, key=lambda value: (value["priority"] != "HIGH", value["inbound_count"], value["route"])):
        lines.append(
            f"| {row['priority']} | `{row['route']}` | {row['inbound_count']} | "
            f"{row['outbound_mapped_count']} | {row['suggested_links'] or '—'} |"
        )
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Lab link-gap loop: {len(rows)} routes")
    print(f"  High priority: {len(high)}")
    for row in high[:20]:
        print(f"  - {row['route']}: inbound={row['inbound_count']}, outbound={row['outbound_mapped_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
