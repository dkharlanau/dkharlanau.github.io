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
FACTUAL_REVIEW_PATH = ASSESSMENT_DATA / "factual-review.json"
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
        routes[permalink] = {"path": path, "frontmatter": frontmatter, "body": body}
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


def factual_review_index() -> dict[str, dict[str, Any]]:
    if not FACTUAL_REVIEW_PATH.exists():
        return {}
    payload = load_json(FACTUAL_REVIEW_PATH)
    claims = payload.get("claims", [])
    routes = payload.get("routes", [])
    claims_by_id = {str(item.get("id")): item for item in claims if item.get("id")}
    result: dict[str, dict[str, Any]] = {}
    for route in routes:
        route_id = str(route.get("route", ""))
        if not route_id:
            continue
        route_claims = [claims_by_id[item] for item in route.get("claim_ids", []) if item in claims_by_id]
        conflicts = [item for item in route_claims if item.get("status") == "source_conflict"]
        unclear = [item for item in route_claims if item.get("status") == "release_scope_unclear"]
        supported = [item for item in route_claims if item.get("status") == "source_supported"]
        if conflicts:
            status = "source_conflict"
        elif unclear:
            status = "release_scope_unclear"
        elif route_claims and len(supported) == len(route_claims):
            status = "source_supported"
        else:
            status = "needs_source_review"
        result[route_id] = {
            "status": status,
            "claim_count": len(route_claims),
            "source_supported_count": len(supported),
            "source_conflict_count": len(conflicts),
            "release_scope_unclear_count": len(unclear),
            "reviewed_at": route.get("reviewed_at"),
            "human_verification_required": bool(route.get("human_verification_required", True)),
        }
    return result


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
    required_frontmatter = all(bool(frontmatter.get(key)) for key in ("title", "description", "permalink", "last_modified_at")) and tags_present
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


def evidence_applicable(route: str) -> bool:
    return route.startswith("/labs/enterprise-context/") or route in {"/labs/ai-ready/", "/labs/business-ai/"}


def review_priority(route: str, checks: dict[str, bool], state: str, factual: dict[str, Any]) -> tuple[str, str]:
    if state != "human_review_candidate":
        return "P2", "Structure or publication state must be resolved before promotion review."
    score = sum(checks.values())
    if evidence_applicable(route):
        factual_status = factual.get("status", "not_reviewed")
        if factual_status in {"source_conflict", "release_scope_unclear"}:
            return "P0", "Evidence has a conflict or unclear release scope that needs resolution."
        if factual_status in {"not_reviewed", "needs_source_review"}:
            return "P0", "Structure is mature but load-bearing factual claims have not completed primary-source review."
        if factual_status == "source_supported":
            return "P1", "Primary-source review exists; human page-level verification is the next gate."
    if score == 5:
        return "P2", "Assessment or authoring route is structurally mature; factual SAP review is not the primary gate."
    return "P2", "Structural review remains the next action."


def audit() -> dict[str, Any]:
    pages = page_sources()
    factual_index = factual_review_index()
    items: list[dict[str, Any]] = []
    for route in all_catalog_routes():
        factual = factual_index.get(
            route,
            {
                "status": "not_reviewed",
                "claim_count": 0,
                "source_supported_count": 0,
                "source_conflict_count": 0,
                "release_scope_unclear_count": 0,
                "reviewed_at": None,
                "human_verification_required": True,
            },
        )
        page = pages.get(route)
        if page is None:
            items.append(
                {
                    "route": route,
                    "source_path": None,
                    "state": "missing_source",
                    "priority": "P2",
                    "review_reason": "Catalog route cannot be resolved to a Lab source file.",
                    "structural_score": 0,
                    "checks": {},
                    "factual_review": factual,
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
        priority, review_reason = review_priority(route, checks, state, factual)
        items.append(
            {
                "route": route,
                "source_path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "state": state,
                "priority": priority,
                "review_reason": review_reason,
                "structural_score": sum(checks.values()),
                "checks": checks,
                "factual_review": factual,
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
    factual_order = {"source_conflict": 0, "release_scope_unclear": 1, "not_reviewed": 2, "needs_source_review": 3, "source_supported": 4}
    items.sort(
        key=lambda item: (
            state_order[item["state"]],
            priority_order[item["priority"]],
            factual_order.get(item["factual_review"]["status"], 9),
            -item["structural_score"],
            item["route"],
        )
    )
    counts: dict[str, int] = {}
    factual_counts: dict[str, int] = {}
    priority_counts: dict[str, int] = {}
    for item in items:
        counts[item["state"]] = counts.get(item["state"], 0) + 1
        factual_status = item["factual_review"]["status"]
        factual_counts[factual_status] = factual_counts.get(factual_status, 0) + 1
        priority_counts[item["priority"]] = priority_counts.get(item["priority"], 0) + 1

    return {
        "id": "assessment-linked-lab-promotion-readiness",
        "version": "1.1.0",
        "updated_at": "2026-08-16",
        "policy": "/labs/assessment/data/promotion-readiness-policy.json",
        "factual_review_registry": "/labs/assessment/data/factual-review.json",
        "scope_route_count": len(items),
        "counts": counts,
        "factual_review_counts": factual_counts,
        "priority_counts": priority_counts,
        "promotion_boundary": "This generated audit does not change status, verified, robots, or sitemap. Human review is required for promotion.",
        "items": items,
    }


def serialize(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit evidence-aware promotion readiness for Lab pages referenced by the assessment catalog.")
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
            f"{payload['factual_review_counts'].get('source_supported', 0)} source-reviewed route(s)."
        )
        return 0

    OUTPUT_PATH.write_text(rendered, encoding="utf-8")
    counts = payload["counts"]
    print(
        f"Generated {OUTPUT_PATH.relative_to(ROOT)}: "
        f"{payload['scope_route_count']} routes, "
        f"{counts.get('human_review_candidate', 0)} human-review candidate(s), "
        f"{payload['factual_review_counts'].get('source_supported', 0)} source-reviewed route(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
