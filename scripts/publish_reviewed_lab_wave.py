#!/usr/bin/env python3
"""Apply an owner-approved Lab publication wave without bypassing quality gates.

This script does not open robots or sitemap by itself. It marks the approved pages as
reviewed/verified, records the page-level review in the factual-review registry, and
updates visible review language. `lab_search_promotion_loop.py --apply` must still pass
before a route becomes indexable.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
APPROVALS = ROOT / "_data" / "labs" / "publication_reviews.yml"
READINESS = ROOT / "labs" / "assessment" / "data" / "promotion-readiness.json"
FACTUAL_REVIEW = ROOT / "labs" / "assessment" / "data" / "factual-review.json"
WAVE_ID = "logistics-search-wave-01"
REVIEW_DATE = "2026-08-16"

VISIBLE_REPLACEMENTS: dict[str, list[tuple[str, str]]] = {
    "/labs/enterprise-context/sales-order/": [
        ("<p>Working map</p>", "<p>Reviewed map</p>"),
        ("<em>Draft research · no client data · human review still required</em>", "<em>Reviewed model · source-tracked · no client data</em>"),
        (
            "the assessment factual-review layer currently confirms two load-bearing controls on this route: item-category determination and schedule-line-category behavior. The wider decision map keeps its own source registry, but the page still requires end-to-end human review before any verification or publication decision.",
            "the assessment factual-review layer confirms the load-bearing item-category and schedule-line controls on this route. The wider decision map was reviewed against its SAP source registry; authored diagnostic heuristics remain separated from documented product behavior.",
        ),
    ],
    "/labs/enterprise-context/pricing/": [
        ("<p>Working model</p>", "<p>Reviewed model</p>"),
        ("<em>Draft research · practical reasoning · no client data</em>", "<em>Reviewed model · source-tracked · no client data</em>"),
        (
            "claim-level review currently confirms the condition-technique search model and pricing-procedure determination inputs. The wider page includes extensions, billing parity, and practitioner heuristics from its source registry, but it still needs page-level human review before any verification or publication decision.",
            "claim-level review confirms the condition-technique search model and pricing-procedure determination inputs. Extensions and billing behavior were reviewed against the source registry; practitioner heuristics remain explicitly identified as authored reasoning.",
        ),
    ],
    "/labs/enterprise-context/atp/": [
        ("<p>Working model</p>", "<p>Reviewed model</p>"),
        ("<em>Draft research · practical reasoning · no client data</em>", "<em>Reviewed model · source-tracked · no client data</em>"),
        (
            "claim-level review currently confirms the advanced ATP simulation API scope, Supply Protection behavior, and the complementary PAL/Supply Protection model. The wider page also covers classic ATP controls, BOP, alternatives, and integrations, so page-level human review is still required.",
            "claim-level review confirms the advanced ATP simulation API scope, Supply Protection behavior, and the complementary PAL/Supply Protection model. Classic ATP controls, BOP, alternatives, and integration boundaries were reviewed against the route source registry; authored diagnostic framing remains explicitly separate.",
        ),
    ],
    "/labs/enterprise-context/shipping/": [
        ("<p>Working model</p>", "<p>Reviewed model</p>"),
        ("<em>Draft research · practical reasoning · no client data</em>", "<em>Reviewed model · source-tracked · no client data</em>"),
        (
            "claim-level review currently confirms the shipping-point input model and the classic route-determination context, including the role of route data in scheduling. The wider execution and EWM/TM boundary still requires page-level human review.",
            "claim-level review confirms the shipping-point input model and the classic route-determination context, including the role of route data in scheduling. The wider execution and EWM/TM boundary was reviewed as an authored integration model and remains separated from release-specific SAP behavior.",
        ),
    ],
    "/labs/enterprise-context/procurement/": [
        ("<p>Working model</p>", "<p>Reviewed model</p>"),
        ("<em>Draft research · practical reasoning · no client data</em>", "<em>Reviewed model · source-tracked · no client data</em>"),
        (
            "claim-level review currently confirms source-of-supply behavior and the distinction between item category and account-assignment category. The end-to-end map covers more decisions and integrations, so page-level human review is still required before any verification or publication decision.",
            "claim-level review confirms source-of-supply behavior and the distinction between item category and account-assignment category. The end-to-end map was reviewed against its SAP source registry; cross-process diagnostic framing remains authored reasoning.",
        ),
    ],
    "/labs/enterprise-context/ewm/": [
        ("<p>Working model</p>", "<p>Reviewed model</p>"),
        (
            "claim-level review currently confirms warehouse-task semantics, warehouse-order grouping, and wave-to-task/order behavior. The ownership model above is an authored diagnostic frame; deployment, production, QM, automation, and cross-system completion still require page-level human review.",
            "claim-level review confirms warehouse-task semantics, warehouse-order grouping, and wave-to-task/order behavior. Deployment, production, QM, automation, and cross-system boundaries were reviewed against the route source registry; the ownership model remains an authored diagnostic frame.",
        ),
    ],
    "/labs/enterprise-context/integrations/": [
        ("<p>Research status</p>", "<p>Reviewed architecture</p>"),
        (
            "reviewed SAP product claims support selected platform and interface behavior. The architecture stack, selection sequence, and design heuristics are authored reasoning and remain subject to page-level human review.",
            "reviewed product documentation supports the named platform and interface behavior. The architecture stack, selection sequence, and design heuristics were reviewed as authored reasoning and are intentionally kept separate from vendor product facts.",
        ),
    ],
    "/labs/enterprise-context/automotive-jit/": [
        ("<p>Working model</p>", "<p>Reviewed model</p>"),
    ],
}


def load_yaml(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(payload, dict):
        raise RuntimeError(f"Expected mapping in {path}")
    return payload


def set_frontmatter_scalar(text: str, key: str, value: str) -> str:
    if not text.startswith("---\n"):
        raise RuntimeError("Missing YAML front matter")
    end = text.find("\n---", 4)
    if end < 0:
        raise RuntimeError("Missing YAML front matter terminator")
    front, rest = text[:end], text[end:]
    line = f"{key}: {value}"
    pattern = re.compile(rf"(?m)^{re.escape(key)}\s*:\s*.*$")
    if pattern.search(front):
        front = pattern.sub(line, front, count=1)
    else:
        front += "\n" + line
    return front + rest


def quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def readiness_index() -> dict[str, dict[str, Any]]:
    payload = json.loads(READINESS.read_text(encoding="utf-8"))
    return {str(item["route"]): item for item in payload.get("items", []) if item.get("route")}


def validate_wave(wave: dict[str, Any], readiness: dict[str, dict[str, Any]]) -> None:
    required_status = str(wave.get("required_factual_status") or "source_supported")
    min_score = int(wave.get("min_structural_score") or 5)
    for route, cfg in wave["routes"].items():
        item = readiness.get(route)
        if not item:
            raise RuntimeError(f"No promotion-readiness item for {route}")
        factual = item.get("factual_review") or {}
        if item.get("priority") != "P1":
            raise RuntimeError(f"{route}: expected P1, got {item.get('priority')}")
        if factual.get("status") != required_status:
            raise RuntimeError(f"{route}: factual status is {factual.get('status')}")
        if int(item.get("structural_score") or 0) < min_score:
            raise RuntimeError(f"{route}: structural score below {min_score}")
        expected_path = str(cfg.get("source_path") or "")
        if item.get("source_path") != expected_path:
            raise RuntimeError(f"{route}: source path drift: {item.get('source_path')} != {expected_path}")


def update_page(route: str, cfg: dict[str, Any]) -> str:
    path = ROOT / str(cfg["source_path"])
    text = path.read_text(encoding="utf-8")

    # Editorial state. Search visibility is intentionally left untouched here.
    text = set_frontmatter_scalar(text, "status", "reviewed")
    text = set_frontmatter_scalar(text, "verified", "true")
    text = set_frontmatter_scalar(text, "last_reviewed", REVIEW_DATE)
    text = set_frontmatter_scalar(text, "publication_wave", quoted(WAVE_ID))
    text = set_frontmatter_scalar(text, "review_method", quoted("primary sources + factual review + page-level editorial review"))
    text = set_frontmatter_scalar(text, "search_intent", quoted(str(cfg["search_intent"])))

    for old, new in VISIBLE_REPLACEMENTS.get(route, []):
        if old not in text:
            raise RuntimeError(f"{route}: expected review marker not found: {old[:90]}")
        text = text.replace(old, new, 1)

    # A reviewed page in this wave must not still tell the reader that human review is pending.
    lowered = text.lower()
    for forbidden in ("human review still required", "page-level human review", "still needs page-level human review"):
        if forbidden in lowered:
            raise RuntimeError(f"{route}: stale pending-review language remains: {forbidden}")

    path.write_text(text, encoding="utf-8")
    return str(path.relative_to(ROOT)).replace("\\", "/")


def update_factual_review(routes: set[str]) -> None:
    payload = json.loads(FACTUAL_REVIEW.read_text(encoding="utf-8"))
    found: set[str] = set()
    for item in payload.get("routes", []):
        route = str(item.get("route") or "")
        if route not in routes:
            continue
        item["human_verification_required"] = False
        item["page_review_status"] = "reviewed"
        item["page_reviewed_at"] = REVIEW_DATE
        item["publication_wave"] = WAVE_ID
        found.add(route)
    missing = routes - found
    if missing:
        raise RuntimeError(f"Missing factual-review route records: {sorted(missing)}")
    payload["updated_at"] = REVIEW_DATE
    FACTUAL_REVIEW.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    approvals = load_yaml(APPROVALS)
    wave = (approvals.get("waves") or {}).get(WAVE_ID)
    if not isinstance(wave, dict) or not isinstance(wave.get("routes"), dict):
        raise RuntimeError(f"Publication wave not found: {WAVE_ID}")

    readiness = readiness_index()
    validate_wave(wave, readiness)

    changed: list[str] = []
    for route, cfg in wave["routes"].items():
        changed.append(update_page(route, cfg))
    update_factual_review(set(wave["routes"]))
    changed.append(str(FACTUAL_REVIEW.relative_to(ROOT)))

    print(f"Reviewed publication wave: {WAVE_ID}")
    for path in changed:
        print(f"  - {path}")
    print("Search visibility remains closed until the promotion loop passes with --apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
