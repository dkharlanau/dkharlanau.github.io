#!/usr/bin/env python3
"""Audit search-intent ownership for Lab promotion candidates.

Primary-source-supported P1 routes should have one explicit primary search intent.
The audit also detects exact duplicates and high token overlap that may indicate
search cannibalization. It does not claim query volume or ranking potential.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import yaml


STOP = {
    "sap", "s4hana", "s", "4hana", "and", "with", "from", "to", "the", "a", "an",
    "for", "of", "vs", "in", "on", "process", "architecture",
}


def load_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else {}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def tokens(text: str) -> set[str]:
    values = re.findall(r"[a-z0-9]+", text.lower())
    return {value for value in values if value not in STOP and len(value) > 1}


def overlap(left: str, right: str) -> float:
    a, b = tokens(left), tokens(right)
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def audit(repo: Path) -> dict:
    registry_path = repo / "_data" / "labs" / "search_intents.yml"
    readiness_path = repo / "labs" / "assessment" / "data" / "promotion-readiness.json"
    registry = load_yaml(registry_path)
    routes = registry.get("routes") or {}
    readiness = load_json(readiness_path)

    p1 = {
        item["route"]: item
        for item in readiness.get("items", [])
        if item.get("priority") == "P1"
    }

    missing = sorted(route for route in p1 if route not in routes)
    orphan = sorted(route for route in routes if route not in {item.get("route") for item in readiness.get("items", [])})

    exact: dict[str, list[str]] = {}
    for route, item in routes.items():
        primary = str((item or {}).get("primary") or "").strip().lower()
        exact.setdefault(primary, []).append(route)
    exact_duplicates = [value for key, value in exact.items() if key and len(value) > 1]

    near_duplicates: list[dict] = []
    route_items = sorted((route, str((item or {}).get("primary") or "")) for route, item in routes.items())
    for idx, (left_route, left_intent) in enumerate(route_items):
        for right_route, right_intent in route_items[idx + 1 :]:
            score = overlap(left_intent, right_intent)
            if score >= 0.58:
                near_duplicates.append({
                    "left": left_route,
                    "right": right_route,
                    "overlap": round(score, 3),
                    "left_intent": left_intent,
                    "right_intent": right_intent,
                })

    return {
        "version": registry.get("version", 1),
        "updated_at": registry.get("updated_at"),
        "p1_route_count": len(p1),
        "mapped_route_count": len(routes),
        "missing_p1_routes": missing,
        "orphan_registry_routes": orphan,
        "exact_duplicate_groups": exact_duplicates,
        "near_duplicate_pairs": sorted(near_duplicates, key=lambda item: -item["overlap"]),
        "routes": routes,
    }


def write_report(repo: Path, payload: dict, output_dir: str) -> None:
    out = repo / output_dir
    out.mkdir(parents=True, exist_ok=True)
    (out / "lab-search-intents.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    lines = [
        "# Lab Search Intent Audit",
        "",
        "Intent ownership is a content-design rule, not a search-volume claim.",
        "",
        f"- P1 promotion candidates: **{payload['p1_route_count']}**",
        f"- Routes with explicit intents: **{payload['mapped_route_count']}**",
        f"- Missing P1 intents: **{len(payload['missing_p1_routes'])}**",
        f"- Exact duplicate groups: **{len(payload['exact_duplicate_groups'])}**",
        f"- High-overlap pairs: **{len(payload['near_duplicate_pairs'])}**",
        "",
        "## Missing P1 routes",
        "",
    ]
    if payload["missing_p1_routes"]:
        lines.extend(f"- `{route}`" for route in payload["missing_p1_routes"])
    else:
        lines.append("No missing P1 intent mappings.")

    lines.extend(["", "## Potential cannibalization", ""])
    if payload["near_duplicate_pairs"]:
        for item in payload["near_duplicate_pairs"]:
            lines.append(
                f"- **{item['overlap']:.2f}** `{item['left']}` ↔ `{item['right']}`"
            )
            lines.append(f"  - {item['left_intent']}")
            lines.append(f"  - {item['right_intent']}")
    else:
        lines.append("No high-overlap intent pairs detected.")

    lines.extend(["", "## Intent ownership", ""])
    for route, item in sorted(payload["routes"].items()):
        lines.append(f"- `{route}` → {item.get('primary', '')}")

    (out / "lab-search-intents.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-dir", default=".")
    parser.add_argument("--output-dir", default="reports/seo")
    parser.add_argument("--fail-on-missing-p1", action="store_true")
    args = parser.parse_args()

    repo = Path(args.repo_dir).resolve()
    payload = audit(repo)
    write_report(repo, payload, args.output_dir)

    print(f"Lab search intent audit: {payload['mapped_route_count']} mapped routes")
    print(f"  P1 candidates: {payload['p1_route_count']}")
    print(f"  Missing P1: {len(payload['missing_p1_routes'])}")
    print(f"  High-overlap pairs: {len(payload['near_duplicate_pairs'])}")
    for route in payload["missing_p1_routes"][:20]:
        print(f"  - missing: {route}")

    if args.fail_on_missing_p1 and payload["missing_p1_routes"]:
        return 2
    if payload["exact_duplicate_groups"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
