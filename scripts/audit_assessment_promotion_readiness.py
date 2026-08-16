#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
ASSESSMENT_DATA = ROOT / "labs" / "assessment" / "data"
CATALOG_PATH = ASSESSMENT_DATA / "catalog.json"
OUTPUT_PATH = ASSESSMENT_DATA / "promotion-readiness.json"

PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|placeholder|lorem ipsum|coming soon)\b", re.IGNORECASE)
HTML_LABS_LINK_RE = re.compile(r'href=["\'](/labs/[^"\']*)["\']')
MD_LABS_LINK_RE = re.compile(r"\]\((/labs/[^)]+)\)")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    data = yaml.safe_load(raw) or {}
    if not isinstance(data, dict):
        data = {}
    return data, text[end + 5 :]


def page_sources() -> dict[str, dict[str, Any]]:
    routes: dict[str, dict[str, Any]] = {}
    for path in sorted((ROOT / "labs").rglob("*")):
        if path.suffix.lower() not in {".md", ".html"} or not path.is_file():
            continue
        frontmatter, body = parse_frontmatter(path)
        permalink = frontmatter.get("permalink")
        if not isinstance(permalink, str) or not permalink.startswith("/labs/"):
            continue
        routes[permalink] = {
            "path": path,
            "frontmatter": frontmatter,
            "body": body,
        }
    return routes


def collect_catalog_routes(value: Any, result: set[str]) -> None:
    if isinstance(value, str):
        if value.startswith("/labs/") and not value.startswith("/labs/assessment/data/"):
            if not re.search(r"\.(?:json|jsonl|ya?ml|txt)$", value):
                result.add(value)
        return
    if isinstance(value, dict):
        for item in value.values():
            collect_catalog_routes(item, result)
        return
    if isinstance(value, list):
        for item in value:
            collect_catalog_routes(item, result)


def all_catalog_routes() -> list[str]:
    catalog = load_json(CATALOG_PATH)
    result: set[str] = {"/labs/assessment/"}
    collect_catalog_routes(catalog, result)
    return sorted(result)


def boolish(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1"}
    return bool(value)


def internal_links(body: str) -> list[str]:
    return sorted(set(HTML_LABS_LINK_RE.findall(body) + MD_LABS_LINK_RE.findall(body)))


def machine_links(links: list[str]) -> list[str]:
    return [link for link in links if "/data/" in link or link.endswith((".json", ".jsonl", ".yml", ".yaml"))]


def structural_checks(frontmatter: dict[str, Any], body: str) -> dict[str, bool]:
    links = internal_links(body)
    tags = frontmatter.get("tags")
    tags_present = isinstance(tags, list) and len(tags) >= 1
    required_frontmatter = all(
        bool(frontmatter.get(key))
        for key in ("title", "description", "permalink", "last_modified_at")
    ) and tags_present
    return {
        "frontmatter_complete": required_frontmatter,
        "substantive_body": len(body.strip()) >= 1500,
        "internal_navigation": len(links) >= 2,
        "machine_readable_link": len(machine_links(links)) >= 1,
        "no_placeholder_markers": PLACEHOLDER_RE.search(body) is None,
    }


def readiness_state(frontmatter: dict[str, Any], checks: dict[str, bool]) -> str:
    status = str(frontmatter.get("status", "")).strip().lower()
    robots = str(frontmatter.get("robots", "")).strip().lower()
    sitemap = frontmatter.get("sitemap")
    draft_boundary = status == "draft" or "noindex" in robots or sitemap is False
    score = sum(checks.values())
    if not draft_boundary:
        return "public_or_indexable"
    if score >= 4:
        return "human_review_candidate"
    return "needs_structure"


def review_priority(frontmatter: dict[str, Any], checks: dict[str, bool], state: str) -> str:
    if state != "human_review_candidate":
        return "P2"
    score = sum(checks.values())
    verified = boolish(frontmatter.get("verified", False))
    if score == 5 and verified:
        return "P0"
    if score == 5:
        return "P1"
    return "P2"


def audit() -> dict[str, Any]:
    pages = page_sources()
    items: list[dict[str, Any]] = []
    for route in all_catalog_routes():
        page = pages.get(route)
        if page is None:
            items.append(
                {
                    "route": route,
                    "source_path": None,
                    "state": "missing_source",
                    "priority": "P2",
                    "structural_score": 0,
                    "checks": {},
                    "verified": False,
                    "status": None,
                    "robots": None,
                    "sitemap": None,
                    "body_characters": 0,
                    "internal_link_count": 0,
                    "machine_link_count": 0,
                }
            )
            continue

        path = page["path"]
        frontmatter = page["frontmatter"]
        body = page["body"]
        checks = structural_checks(frontmatter, body)
        links = internal_links(body)
        state = readiness_state(frontmatter, checks)
        items.append(
            {
                "route": route,
                "source_path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "state": state,
                "priority": review_priority(frontmatter, checks, state),
                "structural_score": sum(checks.values()),
                "checks": checks,
                "verified": boolish(frontmatter.get("verified", False)),
                "status": frontmatter.get("status"),
                "robots": frontmatter.get("robots"),
                "sitemap": frontmatter.get("sitemap"),
                "body_characters": len(body.strip()),
                "internal_link_count": len(links),
                "machine_link_count": len(machine_links(links)),
            }
        )

    state_order = {"human_review_candidate": 0, "needs_structure": 1, "public_or_indexable": 2, "missing_source": 3}
    priority_order = {"P0": 0, "P1": 1, "P2": 2}
    items.sort(key=lambda item: (state_order[item["state"]], priority_order[item["priority"]], -item["structural_score"], item["route"]))
    counts: dict[str, int] = {}
    for item in items:
        counts[item["state"]] = counts.get(item["state"], 0) + 1

    return {
        "id": "assessment-linked-lab-promotion-readiness",
        "version": "1.0.0",
        "updated_at": "2026-08-16",
        "policy": "/labs/assessment/data/promotion-readiness-policy.json",
        "scope_route_count": len(items),
        "counts": counts,
        "promotion_boundary": "This generated audit does not change status, verified, robots, or sitemap. Human review is required for promotion.",
        "items": items,
    }


def serialize(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit promotion readiness for Lab pages referenced by the assessment catalog.")
    parser.add_argument("--check", action="store_true", help="Verify committed readiness inventory is current.")
    args = parser.parse_args()

    payload = audit()
    rendered = serialize(payload)
    if args.check:
        if not OUTPUT_PATH.exists():
            print(f"Missing promotion readiness inventory: {OUTPUT_PATH.relative_to(ROOT)}")
            return 2
        if OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
            print(f"Stale promotion readiness inventory: {OUTPUT_PATH.relative_to(ROOT)}")
            return 2
        counts = payload["counts"]
        print(
            "Promotion readiness inventory is current: "
            f"{payload['scope_route_count']} routes, "
            f"{counts.get('human_review_candidate', 0)} human-review candidate(s), "
            f"{counts.get('needs_structure', 0)} needing structure."
        )
        return 0

    OUTPUT_PATH.write_text(rendered, encoding="utf-8")
    counts = payload["counts"]
    print(
        f"Generated {OUTPUT_PATH.relative_to(ROOT)}: "
        f"{payload['scope_route_count']} routes, "
        f"{counts.get('human_review_candidate', 0)} human-review candidate(s), "
        f"{counts.get('needs_structure', 0)} needing structure."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
