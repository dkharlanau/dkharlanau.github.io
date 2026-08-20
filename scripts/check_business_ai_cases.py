#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "_data" / "labs" / "business_ai"
EXTENSIONS = (
    "expansion_2026_08_15.yml",
    "expansion_2026_08_15_b.yml",
    "expansion_2026_08_15_c.yml",
)


class CaseContractError(ValueError):
    pass


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def aggregate_cases():
    catalog = load_yaml(DATA / "catalog.yml")
    cases = list(catalog.get("cases", []))
    source_ids = {
        source.get("id")
        for source in catalog.get("source_registry", [])
        if isinstance(source, dict) and source.get("id")
    }
    for name in EXTENSIONS:
        extension = load_yaml(DATA / name)
        cases.extend(extension.get("cases", []))
        source_ids.update(
            source.get("id")
            for source in extension.get("source_registry", [])
            if isinstance(source, dict) and source.get("id")
        )
    return cases, source_ids


def infer_legacy_review_state(record: dict) -> str:
    source_ids = record.get("source_ids") or []
    pattern_ids = record.get("pattern_ids") or ([] if not record.get("pattern") else [record["pattern"]])
    if source_ids and pattern_ids and record.get("evidence_grade"):
        return "structured"
    if source_ids:
        return "sourced"
    return "candidate"


def normalize_case(record: dict) -> dict:
    normalized = dict(record)
    normalized.setdefault("case_kind", "unknown")
    if not normalized.get("review_state"):
        normalized["review_state"] = infer_legacy_review_state(normalized)
    normalized.setdefault("implementation_maturity", "unknown")

    if "pattern_ids" not in normalized and normalized.get("pattern"):
        normalized["pattern_ids"] = [normalized["pattern"]]
    normalized.setdefault("pattern_ids", [])

    if "process_label" not in normalized and normalized.get("process"):
        normalized["process_label"] = normalized["process"]
    if "metrics" not in normalized and "reported_metrics" in normalized:
        normalized["metrics"] = normalized.get("reported_metrics") or []
    normalized.setdefault("metrics", [])
    if "limitations" not in normalized and "limits" in normalized:
        normalized["limitations"] = normalized.get("limits") or []
    normalized.setdefault("limitations", [])
    if "consultant_interpretation" not in normalized and "consultant_note" in normalized:
        normalized["consultant_interpretation"] = normalized.get("consultant_note")
    if "implementation_summary" not in normalized and "implementation" in normalized:
        normalized["implementation_summary"] = normalized.get("implementation")

    normalized.setdefault("process_stage_ids", [])
    normalized.setdefault("source_ids", [])
    normalized.setdefault("source_types", [])
    normalized.setdefault("evidence_claims", [])
    normalized.setdefault("proof_gaps", [])
    normalized.setdefault("controls", [])
    normalized.setdefault("data_dependencies", [])
    normalized.setdefault("integration_boundaries", [])
    normalized.setdefault("systems_of_record", [])
    return normalized


def _has_value(value) -> bool:
    return value not in (None, "", [], {})


def _claim_levels(case: dict) -> set[str]:
    levels = set()
    for claim in case.get("evidence_claims", []):
        if isinstance(claim, dict) and claim.get("level"):
            levels.add(claim["level"])
    return levels


def validate_transition(from_state: str, to_state: str, contract: dict) -> None:
    lifecycle = contract["review_lifecycle"]
    allowed = lifecycle["transitions"].get(from_state)
    if allowed is None:
        raise CaseContractError(f"Unknown source review state: {from_state}")
    if to_state not in allowed:
        raise CaseContractError(
            f"Invalid review transition: {from_state} -> {to_state}"
        )


def validate_case(record: dict, contract: dict, known_source_ids: set[str]) -> dict:
    case = normalize_case(record)
    case_id = case.get("id", "<missing-id>")
    vocab = contract["vocabularies"]

    if not case.get("id") or not case.get("title"):
        raise CaseContractError(f"{case_id} is missing id or title")

    for field, vocabulary in (
        ("case_kind", "case_kind"),
        ("review_state", "review_state"),
        ("implementation_maturity", "implementation_maturity"),
        ("evidence_grade", "evidence_grade"),
        ("autonomy_level", "autonomy_level"),
        ("measurement_state", "measurement_state"),
        ("transferability", "transferability"),
    ):
        if field in case and case.get(field) not in (None, ""):
            if case[field] not in vocab[vocabulary]:
                raise CaseContractError(
                    f"{case_id} has invalid {field}: {case[field]!r}"
                )

    for source_type in case.get("source_types", []):
        if source_type not in vocab["source_type"]:
            raise CaseContractError(
                f"{case_id} has invalid source_type: {source_type!r}"
            )

    for source_id in case.get("source_ids", []):
        if source_id not in known_source_ids:
            raise CaseContractError(
                f"{case_id} references missing evidence source: {source_id}"
            )

    for claim in case.get("evidence_claims", []):
        if not isinstance(claim, dict):
            raise CaseContractError(f"{case_id} evidence claim must be a mapping")
        if not claim.get("statement") or not claim.get("level"):
            raise CaseContractError(
                f"{case_id} evidence claim requires statement and level"
            )
        level = claim["level"]
        if level not in vocab["evidence_level"]:
            raise CaseContractError(
                f"{case_id} evidence claim has invalid level: {level!r}"
            )
        if level == "runtime_proof" and not (
            claim.get("runtime_authorized") is True
            and claim.get("runtime_observed") is True
        ):
            raise CaseContractError(
                f"{case_id} runtime_proof requires authorized and observed runtime activity"
            )

    state = case["review_state"]
    gate = contract["review_lifecycle"]["gates"].get(state, {})
    schema_required = {
        field
        for field, definition in contract["case_schema"]["fields"].items()
        if state in definition.get("required_for", [])
    }
    required_fields = schema_required | set(gate.get("require", []))
    for field in sorted(required_fields):
        if not _has_value(case.get(field)):
            raise CaseContractError(
                f"{case_id} cannot be {state}: missing {field}"
            )

    blocked = set(gate.get("block_evidence_levels", []))
    blocked_present = blocked & _claim_levels(case)
    if blocked_present:
        raise CaseContractError(
            f"{case_id} cannot be {state}: blocked evidence levels {sorted(blocked_present)}"
        )

    if state in {"review_ready", "approved"}:
        for field in (
            "case_kind",
            "implementation_maturity",
            "measurement_state",
            "transferability",
        ):
            if case.get(field) == "unknown":
                raise CaseContractError(
                    f"{case_id} cannot be {state}: {field} is still unknown"
                )
        if not any(
            claim.get("level") == "source_fact"
            for claim in case.get("evidence_claims", [])
            if isinstance(claim, dict)
        ):
            raise CaseContractError(
                f"{case_id} cannot be {state}: no source_fact claim is recorded"
            )

    if state == "approved":
        human_review = case.get("human_review") or {}
        required_review = gate.get("human_review", {})
        if human_review.get("kind") != required_review.get("kind"):
            raise CaseContractError(
                f"{case_id} cannot be approved without a human review"
            )
        for field in required_review.get("require", []):
            if not _has_value(human_review.get(field)):
                raise CaseContractError(
                    f"{case_id} approved human review is missing {field}"
                )

    return case


def migration_gaps(case: dict, contract: dict) -> list[str]:
    normalized = normalize_case(case)
    review_ready = contract["review_lifecycle"]["gates"]["review_ready"]
    gaps = []
    for field in review_ready.get("require", []):
        if not _has_value(normalized.get(field)):
            gaps.append(field)
    for field in (
        "case_kind",
        "implementation_maturity",
        "measurement_state",
        "transferability",
    ):
        if normalized.get(field) == "unknown" and field not in gaps:
            gaps.append(field)
    if not normalized.get("evidence_claims") and "evidence_claims" not in gaps:
        gaps.append("evidence_claims")
    return gaps


def build_report():
    contract = load_yaml(DATA / "contract.yml")
    cases, source_ids = aggregate_cases()
    seen = set()
    state_counts = {state: 0 for state in contract["vocabularies"]["review_state"]}
    migration = []

    for raw_case in cases:
        case_id = raw_case.get("id")
        if case_id in seen:
            raise CaseContractError(f"Duplicate Business AI case id: {case_id}")
        seen.add(case_id)
        normalized = validate_case(raw_case, contract, source_ids)
        state_counts[normalized["review_state"]] += 1
        gaps = migration_gaps(raw_case, contract)
        if gaps:
            migration.append({"id": case_id, "missing_for_review_ready": gaps})

    return {
        "schema": "dkharlanau.business-ai.case-lifecycle",
        "contract_version": contract["contract"]["version"],
        "case_schema_version": contract["case_schema"]["version"],
        "case_count": len(cases),
        "review_state_counts": state_counts,
        "migration_gap_count": len(migration),
        "migration_gaps": migration,
        "agent_maximum_state": contract["review_lifecycle"]["agent_maximum_state"],
        "human_approval_state": contract["review_lifecycle"]["human_approval_state"],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Validate Business AI case schema, evidence claims, and review lifecycle."
    )
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        report = build_report()
    except (OSError, yaml.YAMLError, KeyError, CaseContractError) as exc:
        print(f"Business AI case contract failed: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(
            "Business AI case contract passed: "
            f"{report['case_count']} cases, "
            f"{report['migration_gap_count']} non-blocking review-ready migration gaps"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
