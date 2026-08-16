#!/usr/bin/env python3
"""Classify remaining P2 Lab candidates for search publication.

P2 does not mean low quality. In the assessment readiness model it usually means that
primary-source debt is not the main gate. This triage keeps public authored frameworks
separate from practice tools and internal assessment/control pages.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
READINESS_PATH = ROOT / "labs" / "assessment" / "data" / "promotion-readiness.json"
CATALOG_PATH = ROOT / "labs" / "assessment" / "data" / "catalog.json"
POLICY_PATH = ROOT / "_data" / "labs" / "search_publication_policy.yml"

PUBLIC_REVIEW_NEXT = "PUBLIC_REVIEW_NEXT"
KEEP_PRACTICE_NOINDEX = "KEEP_PRACTICE_NOINDEX"
KEEP_INTERNAL_NOINDEX = "KEEP_INTERNAL_NOINDEX"
NEEDS_POLICY_DECISION = "NEEDS_POLICY_DECISION"
POLICY_ERROR = "POLICY_ERROR"


def load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise RuntimeError(f"Expected mapping in {path}")
    return payload


def load_yaml(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(payload, dict):
        raise RuntimeError(f"Expected mapping in {path}")
    return payload


def catalog_route_set(catalog: dict[str, Any], key: str) -> set[str]:
    routes: set[str] = set()
    values = catalog.get(key) or []
    if not isinstance(values, list):
        return routes
    for item in values:
        if not isinstance(item, dict):
            continue
        route = item.get("route")
        if isinstance(route, str) and route.startswith("/labs/"):
            routes.add(route)
    return routes


def classify_item(
    item: dict[str, Any],
    public_frameworks: dict[str, Any],
    practice_routes: set[str],
    authoring_routes: set[str],
) -> tuple[str, str, str]:
    route = str(item.get("route") or "")
    factual = item.get("factual_review") or {}
    profile = item.get("evidence_profile") or {}

    if route in public_frameworks:
        policy_entry = public_frameworks.get(route) or {}
        search_intent = str(policy_entry.get("search_intent") or "").strip()
        if not search_intent:
            return POLICY_ERROR, "Public framework is missing a search intent.", ""
        has_source_debt = bool(profile.get("counts_as_source_review_debt", False))
        factual_status = str(factual.get("status") or "not_reviewed")
        if has_source_debt and factual_status != "source_supported":
            return (
                POLICY_ERROR,
                "Public framework still has required primary-source review debt.",
                search_intent,
            )
        return (
            PUBLIC_REVIEW_NEXT,
            str(policy_entry.get("reason") or "Public authored framework."),
            search_intent,
        )

    if route in practice_routes:
        return (
            KEEP_PRACTICE_NOINDEX,
            "Assessment practice route. Useful to users inside the Lab, but external search is not its main job.",
            "",
        )

    if route in authoring_routes or route.startswith("/labs/assessment/"):
        return (
            KEEP_INTERNAL_NOINDEX,
            "Assessment authoring or control-plane route. Keep it crawlable from the Lab but out of external search.",
            "",
        )

    return (
        NEEDS_POLICY_DECISION,
        "P2 candidate is outside the current public, practice and internal policy groups.",
        "",
    )


def build_triage(root: Path = ROOT) -> dict[str, Any]:
    readiness = load_json(root / "labs" / "assessment" / "data" / "promotion-readiness.json")
    catalog = load_json(root / "labs" / "assessment" / "data" / "catalog.json")
    policy = load_yaml(root / "_data" / "labs" / "search_publication_policy.yml")

    public_frameworks = policy.get("public_frameworks") or {}
    if not isinstance(public_frameworks, dict):
        raise RuntimeError("public_frameworks must be a mapping")

    practice_routes = catalog_route_set(catalog, "practice_modes")
    authoring_routes = catalog_route_set(catalog, "authoring_tools")

    rows: list[dict[str, Any]] = []
    for item in readiness.get("items", []):
        if item.get("state") != "human_review_candidate" or item.get("priority") != "P2":
            continue
        decision, reason, search_intent = classify_item(
            item, public_frameworks, practice_routes, authoring_routes
        )
        factual = item.get("factual_review") or {}
        profile = item.get("evidence_profile") or {}
        rows.append(
            {
                "route": item.get("route"),
                "source_path": item.get("source_path"),
                "decision": decision,
                "structural_score": item.get("structural_score"),
                "factual_status": factual.get("status"),
                "external_review_mode": profile.get("external_review_mode"),
                "source_review_debt": bool(profile.get("counts_as_source_review_debt", False)),
                "search_intent": search_intent,
                "reason": reason,
            }
        )

    order = {
        PUBLIC_REVIEW_NEXT: 0,
        KEEP_PRACTICE_NOINDEX: 1,
        KEEP_INTERNAL_NOINDEX: 2,
        POLICY_ERROR: 3,
        NEEDS_POLICY_DECISION: 4,
    }
    rows.sort(key=lambda row: (order.get(str(row["decision"]), 9), str(row["route"])))

    counts: dict[str, int] = {}
    for row in rows:
        decision = str(row["decision"])
        counts[decision] = counts.get(decision, 0) + 1

    policy_routes = set(public_frameworks)
    readiness_routes = {str(row.get("route")) for row in readiness.get("items", [])}
    orphan_public_policy = sorted(policy_routes - readiness_routes)

    return {
        "version": policy.get("version", 1),
        "updated_at": str(policy.get("updated_at") or ""),
        "candidate_count": len(rows),
        "counts": counts,
        "practice_route_count": len(practice_routes),
        "authoring_route_count": len(authoring_routes),
        "orphan_public_policy_routes": orphan_public_policy,
        "rows": rows,
    }


def write_reports(payload: dict[str, Any], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / "lab-p2-publication-triage.csv"
    md_path = output_dir / "lab-p2-publication-triage.md"
    json_path = output_dir / "lab-p2-publication-triage.json"

    fields = [
        "route",
        "source_path",
        "decision",
        "structural_score",
        "factual_status",
        "external_review_mode",
        "source_review_debt",
        "search_intent",
        "reason",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in payload["rows"]:
            writer.writerow({field: row.get(field, "") for field in fields})

    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Lab P2 Search Publication Triage",
        "",
        "P2 is a policy class, not a quality score. Public authored frameworks, practice tools, and internal review pages have different search jobs.",
        "",
        f"- Remaining P2 candidates: **{payload['candidate_count']}**",
        f"- Public review next: **{payload['counts'].get(PUBLIC_REVIEW_NEXT, 0)}**",
        f"- Practice routes kept noindex: **{payload['counts'].get(KEEP_PRACTICE_NOINDEX, 0)}**",
        f"- Internal routes kept noindex: **{payload['counts'].get(KEEP_INTERNAL_NOINDEX, 0)}**",
        f"- Policy errors: **{payload['counts'].get(POLICY_ERROR, 0)}**",
        f"- Unclassified: **{payload['counts'].get(NEEDS_POLICY_DECISION, 0)}**",
        "",
        "| Decision | Route | Structure | Facts | Source debt | Search intent / reason |",
        "|---|---|---:|---|---|---|",
    ]
    for row in payload["rows"]:
        detail = row.get("search_intent") or row.get("reason") or ""
        lines.append(
            f"| {row['decision']} | `{row['route']}` | {row['structural_score']} | "
            f"{row['factual_status']} | {str(row['source_review_debt']).lower()} | {detail} |"
        )
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-dir", default=".")
    parser.add_argument("--output-dir", default="reports/seo")
    parser.add_argument("--fail-on-unclassified", action="store_true")
    args = parser.parse_args()

    root = Path(args.repo_dir).resolve()
    payload = build_triage(root)
    write_reports(payload, root / args.output_dir)

    print(f"Lab P2 publication triage: {payload['candidate_count']} candidate(s)")
    for key in (
        PUBLIC_REVIEW_NEXT,
        KEEP_PRACTICE_NOINDEX,
        KEEP_INTERNAL_NOINDEX,
        POLICY_ERROR,
        NEEDS_POLICY_DECISION,
    ):
        print(f"  {key}: {payload['counts'].get(key, 0)}")
    for row in payload["rows"]:
        if row["decision"] in {PUBLIC_REVIEW_NEXT, POLICY_ERROR, NEEDS_POLICY_DECISION}:
            print(f"  - {row['decision']:24s} {row['route']}")

    bad = payload["counts"].get(POLICY_ERROR, 0) + payload["counts"].get(NEEDS_POLICY_DECISION, 0)
    if args.fail_on_unclassified and bad:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
