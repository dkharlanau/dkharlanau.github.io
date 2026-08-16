#!/usr/bin/env python3
"""Apply one owner-approved Lab publication wave without bypassing quality gates.

The approval ledger owns the routes, search intents, review date, evidence mode, and
exact visible text replacements. Review replacements are applied first while pages are
still draft, the generated readiness inventory is refreshed, and only pages that then
pass the structural and evidence-policy gates are marked reviewed/verified.

Product-primary waves require source-supported factual review. Selective/heuristic waves
keep factual status separate: they are allowed only for explicitly public frameworks
whose evidence profile says primary-source debt is not the publication gate. This script
never opens robots or sitemap; the search promotion loop must still pass separately.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
APPROVALS = ROOT / "_data" / "labs" / "publication_reviews.yml"
READINESS = ROOT / "labs" / "assessment" / "data" / "promotion-readiness.json"
FACTUAL_REVIEW = ROOT / "labs" / "assessment" / "data" / "factual-review.json"
SEARCH_PUBLICATION_POLICY = ROOT / "_data" / "labs" / "search_publication_policy.yml"
READINESS_GENERATOR = ROOT / "scripts" / "audit_assessment_promotion_readiness.py"

PRODUCT_PRIMARY = "product_primary"
SELECTIVE_OR_HEURISTIC = "selective_or_heuristic"

STALE_REVIEW_MARKERS = (
    "human review still required",
    "page-level human review",
    "still needs page-level human review",
    "still requires page-level human review",
    "requires page-level human review",
    "remains draft until human review",
    "stays draft until human review",
    "<em>draft research",
    "<p>working model</p>",
    "<p>working inventory</p>",
)


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


def refresh_readiness() -> None:
    if not READINESS_GENERATOR.exists():
        raise RuntimeError(f"Readiness generator not found: {READINESS_GENERATOR}")
    subprocess.run([sys.executable, str(READINESS_GENERATOR)], cwd=ROOT, check=True)


def review_mode(wave: dict[str, Any]) -> str:
    mode = str(wave.get("review_mode") or PRODUCT_PRIMARY).strip().lower()
    if mode not in {PRODUCT_PRIMARY, SELECTIVE_OR_HEURISTIC}:
        raise RuntimeError(f"Unsupported review_mode: {mode}")
    return mode


def public_framework_routes() -> set[str]:
    if not SEARCH_PUBLICATION_POLICY.exists():
        return set()
    policy = load_yaml(SEARCH_PUBLICATION_POLICY)
    public = policy.get("public_frameworks") or {}
    return set(public) if isinstance(public, dict) else set()


def validate_evidence_gate(
    route: str,
    wave: dict[str, Any],
    item: dict[str, Any],
    public_frameworks: set[str],
) -> None:
    mode = review_mode(wave)
    factual = item.get("factual_review") or {}
    profile = item.get("evidence_profile") or {}
    factual_status = str(factual.get("status") or "not_reviewed")

    if factual_status in {"source_conflict", "release_scope_unclear"}:
        raise RuntimeError(f"{route}: factual status blocks publication: {factual_status}")

    if mode == PRODUCT_PRIMARY:
        required_status = str(wave.get("required_factual_status") or "source_supported")
        if item.get("priority") != "P1":
            raise RuntimeError(f"{route}: expected P1, got {item.get('priority')}")
        if factual_status != required_status:
            raise RuntimeError(f"{route}: factual status is {factual_status}")
        return

    if item.get("priority") != "P2":
        raise RuntimeError(f"{route}: selective/heuristic review expects P2, got {item.get('priority')}")
    if route not in public_frameworks:
        raise RuntimeError(f"{route}: selective/heuristic route is not an explicit public framework")
    source_debt = bool(profile.get("counts_as_source_review_debt", False))
    if source_debt and factual_status != "source_supported":
        raise RuntimeError(f"{route}: required primary-source review debt is still open")


def validate_wave(
    wave_id: str,
    wave: dict[str, Any],
    readiness: dict[str, dict[str, Any]],
    *,
    require_structure: bool = True,
    public_frameworks: set[str] | None = None,
) -> None:
    routes = wave.get("routes")
    if not isinstance(routes, dict) or not routes:
        raise RuntimeError(f"Publication wave has no routes: {wave_id}")

    min_score = int(wave.get("min_structural_score") or 5)
    review_date = str(wave.get("reviewed_at") or "").strip()
    if not review_date:
        raise RuntimeError(f"{wave_id}: reviewed_at is required")
    frameworks = public_frameworks if public_frameworks is not None else public_framework_routes()

    for route, cfg in routes.items():
        if not isinstance(cfg, dict):
            raise RuntimeError(f"{route}: route config must be a mapping")
        item = readiness.get(route)
        if not item:
            raise RuntimeError(f"No promotion-readiness item for {route}")
        if item.get("state") != "human_review_candidate":
            raise RuntimeError(f"{route}: expected human_review_candidate, got {item.get('state')}")
        validate_evidence_gate(route, wave, item, frameworks)
        if require_structure and int(item.get("structural_score") or 0) < min_score:
            raise RuntimeError(f"{route}: structural score below {min_score}")
        if item.get("verified") is not False or str(item.get("status") or "").lower() != "draft":
            raise RuntimeError(
                f"{route}: expected draft/unverified pre-state, got "
                f"status={item.get('status')} verified={item.get('verified')}"
            )
        expected_path = str(cfg.get("source_path") or "")
        if not expected_path:
            raise RuntimeError(f"{route}: source_path is required")
        if item.get("source_path") != expected_path:
            raise RuntimeError(f"{route}: source path drift: {item.get('source_path')} != {expected_path}")
        if not str(cfg.get("search_intent") or "").strip():
            raise RuntimeError(f"{route}: search_intent is required")


def configured_replacements(route: str, cfg: dict[str, Any]) -> list[tuple[str, str]]:
    raw = cfg.get("review_replacements") or []
    if not isinstance(raw, list):
        raise RuntimeError(f"{route}: review_replacements must be a list")
    replacements: list[tuple[str, str]] = []
    for idx, item in enumerate(raw, start=1):
        if not isinstance(item, dict):
            raise RuntimeError(f"{route}: replacement {idx} must be a mapping")
        old = str(item.get("from") or "")
        new = str(item.get("to") or "")
        if not old or not new:
            raise RuntimeError(f"{route}: replacement {idx} requires from/to text")
        replacements.append((old, new))
    return replacements


def apply_review_replacements(route: str, cfg: dict[str, Any]) -> str:
    path = ROOT / str(cfg["source_path"])
    text = path.read_text(encoding="utf-8")
    replacements = configured_replacements(route, cfg)
    for old, new in replacements:
        if old not in text:
            raise RuntimeError(f"{route}: expected review marker not found: {old[:100]}")
        text = text.replace(old, new, 1)
    if replacements:
        path.write_text(text, encoding="utf-8")
    return str(path.relative_to(ROOT)).replace("\\", "/")


def review_method_text(mode: str) -> str:
    if mode == PRODUCT_PRIMARY:
        return "primary sources + factual review + page-level editorial review"
    return "selective external evidence + page-level editorial review + authored heuristic boundary"


def finalize_page(
    route: str,
    cfg: dict[str, Any],
    wave_id: str,
    review_date: str,
    mode: str = PRODUCT_PRIMARY,
) -> str:
    path = ROOT / str(cfg["source_path"])
    text = path.read_text(encoding="utf-8")

    # Editorial state. Search visibility is intentionally left untouched here.
    text = set_frontmatter_scalar(text, "status", "reviewed")
    text = set_frontmatter_scalar(text, "verified", "true")
    text = set_frontmatter_scalar(text, "last_reviewed", review_date)
    text = set_frontmatter_scalar(text, "publication_wave", quoted(wave_id))
    text = set_frontmatter_scalar(text, "review_method", quoted(review_method_text(mode)))
    text = set_frontmatter_scalar(text, "evidence_review_mode", quoted(mode))
    text = set_frontmatter_scalar(text, "search_intent", quoted(str(cfg["search_intent"])))

    lowered = text.lower()
    for forbidden in STALE_REVIEW_MARKERS:
        if forbidden in lowered:
            raise RuntimeError(f"{route}: stale review language remains: {forbidden}")

    path.write_text(text, encoding="utf-8")
    return str(path.relative_to(ROOT)).replace("\\", "/")


def update_page(
    route: str,
    cfg: dict[str, Any],
    wave_id: str,
    review_date: str,
    mode: str = PRODUCT_PRIMARY,
) -> str:
    """Compatibility helper for unit tests and direct single-page review updates."""
    apply_review_replacements(route, cfg)
    return finalize_page(route, cfg, wave_id, review_date, mode)


def update_factual_review(routes: set[str], wave_id: str, review_date: str) -> None:
    payload = json.loads(FACTUAL_REVIEW.read_text(encoding="utf-8"))
    found: set[str] = set()
    for item in payload.get("routes", []):
        route = str(item.get("route") or "")
        if route not in routes:
            continue
        item["human_verification_required"] = False
        item["page_review_status"] = "reviewed"
        item["page_reviewed_at"] = review_date
        item["publication_wave"] = wave_id
        found.add(route)
    missing = routes - found
    if missing:
        raise RuntimeError(f"Missing factual-review route records: {sorted(missing)}")
    payload["updated_at"] = review_date
    FACTUAL_REVIEW.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wave", required=True, help="Wave id from _data/labs/publication_reviews.yml")
    args = parser.parse_args()

    approvals = load_yaml(APPROVALS)
    wave_id = args.wave.strip()
    wave = (approvals.get("waves") or {}).get(wave_id)
    if not isinstance(wave, dict):
        raise RuntimeError(f"Publication wave not found: {wave_id}")
    mode = review_mode(wave)
    frameworks = public_framework_routes()

    # Phase 1: prove the candidate/evidence pre-state without weakening the structure gate.
    readiness = readiness_index()
    validate_wave(
        wave_id,
        wave,
        readiness,
        require_structure=False,
        public_frameworks=frameworks,
    )

    # Phase 2: apply only exact, ledger-owned review edits while pages remain draft.
    for route, cfg in wave["routes"].items():
        apply_review_replacements(route, cfg)

    # Phase 3: regenerate structure facts from the reviewed source and enforce the full gate.
    refresh_readiness()
    readiness = readiness_index()
    validate_wave(
        wave_id,
        wave,
        readiness,
        require_structure=True,
        public_frameworks=frameworks,
    )

    # Phase 4: only now mark the page reviewed/verified. Search stays closed until promotion.
    changed: list[str] = []
    review_date = str(wave["reviewed_at"])
    for route, cfg in wave["routes"].items():
        changed.append(finalize_page(route, cfg, wave_id, review_date, mode))

    # Product-primary routes record completion in the claim registry. Selective/heuristic
    # routes intentionally leave factual status unchanged because editorial verification is a
    # separate axis and must not manufacture source-supported claims.
    if mode == PRODUCT_PRIMARY:
        update_factual_review(set(wave["routes"]), wave_id, review_date)
        changed.append(str(FACTUAL_REVIEW.relative_to(ROOT)))

    changed.append(str(READINESS.relative_to(ROOT)))

    print(f"Reviewed publication wave: {wave_id}")
    print(f"  Review mode: {mode}")
    if any(configured_replacements(route, cfg) for route, cfg in wave["routes"].items()):
        print("  Review edits applied before structural validation.")
    for path in changed:
        print(f"  - {path}")
    print("Search visibility remains closed until the promotion loop passes with --apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
