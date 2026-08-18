#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "_data" / "labs" / "business_ai"
EXTENSIONS = (
    "expansion_2026_08_15.yml",
    "expansion_2026_08_15_b.yml",
    "expansion_2026_08_15_c.yml",
)


class GraphIntegrityError(ValueError):
    pass


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def records_by_id(records, label):
    result = {}
    for record in records or []:
        record_id = record.get("id") if isinstance(record, dict) else None
        if not record_id:
            raise GraphIntegrityError(f"{label} record is missing id")
        if record_id in result:
            raise GraphIntegrityError(f"Duplicate {label} id: {record_id}")
        result[record_id] = record
    return result


def require_refs(owner, field, values, known_ids, target_label):
    for value in values or []:
        if value not in known_ids:
            raise GraphIntegrityError(
                f"{owner} field {field} references missing {target_label}: {value}"
            )


def aggregate_catalog(catalog, extensions):
    patterns = list(catalog.get("patterns", []))
    cases = list(catalog.get("cases", []))
    sources = list(catalog.get("source_registry", []))
    for extension in extensions:
        patterns.extend(extension.get("patterns", []))
        cases.extend(extension.get("cases", []))
        sources.extend(extension.get("source_registry", []))
    return patterns, cases, sources


def validate_structure(contract, domain_map, process_map, catalog, extensions, scenarios, matrix, technologies):
    patterns, cases, sources = aggregate_catalog(catalog, extensions)
    sources.extend(scenarios.get("source_registry", []))

    domains = records_by_id(domain_map.get("domains", []), "domain")
    processes = records_by_id(process_map.get("processes", []), "process")
    pattern_map = records_by_id(patterns, "pattern")
    case_map = records_by_id(cases, "case")
    source_map = records_by_id(sources, "source")
    scenario_map = records_by_id(scenarios.get("scenarios", []), "scenario")
    failure_map = records_by_id(scenarios.get("failure_patterns", []), "failure pattern")
    profile_map = records_by_id(matrix.get("profiles", []), "decision profile")
    technology_map = records_by_id(technologies.get("families", []), "technology family")

    allowed_grades = set(contract["vocabularies"]["evidence_grade"])
    allowed_autonomy = set(contract["vocabularies"]["autonomy_level"])

    for process_id, process in processes.items():
        require_refs(process_id, "domains", process.get("domains"), domains, "domain")
        require_refs(process_id, "pattern_ids", process.get("pattern_ids"), pattern_map, "pattern")
        require_refs(
            process_id,
            "technology_families",
            process.get("technology_families"),
            technology_map,
            "technology family",
        )

    for domain_id, domain in domains.items():
        require_refs(domain_id, "case_ids", domain.get("case_ids"), case_map, "case")

    for case_id, case in case_map.items():
        pattern_id = case.get("pattern")
        if pattern_id and pattern_id not in pattern_map:
            raise GraphIntegrityError(
                f"{case_id} field pattern references missing pattern: {pattern_id}"
            )
        grade = case.get("evidence_grade")
        if grade not in allowed_grades:
            raise GraphIntegrityError(
                f"{case_id} has invalid evidence_grade: {grade!r}"
            )
        require_refs(case_id, "source_ids", case.get("source_ids"), source_map, "source")

    for profile_id, profile in profile_map.items():
        require_refs(profile_id, "pattern_ids", profile.get("pattern_ids"), pattern_map, "pattern")
        require_refs(
            profile_id,
            "failure_pattern_ids",
            profile.get("failure_pattern_ids"),
            failure_map,
            "failure pattern",
        )
        require_refs(
            profile_id,
            "scenario_ids",
            profile.get("scenario_ids"),
            scenario_map,
            "scenario",
        )
        autonomy = profile.get("recommended_autonomy")
        if autonomy not in allowed_autonomy:
            raise GraphIntegrityError(
                f"{profile_id} has invalid recommended_autonomy: {autonomy!r}"
            )

    return {
        "domains": domains,
        "processes": processes,
        "patterns": pattern_map,
        "cases": case_map,
        "sources": source_map,
        "scenarios": scenario_map,
        "failure_patterns": failure_map,
        "decision_profiles": profile_map,
        "technology_families": technology_map,
    }


def coverage_gaps(indexes, catalog, domain_map, process_map, matrix, reviewed_at, stale_after_days=180):
    gaps = []

    for domain in domain_map.get("domains", []):
        if not domain.get("case_ids"):
            gaps.append({
                "kind": "domain-case-coverage",
                "id": domain["id"],
                "reason": "Domain has no linked public case yet.",
            })

    for process in process_map.get("processes", []):
        if any(not isinstance(stage, dict) or not stage.get("id") for stage in process.get("stages", [])):
            gaps.append({
                "kind": "stable-stage-id",
                "id": process["id"],
                "reason": "Legacy process stages do not yet carry stable graph IDs.",
            })
        if not process.get("control_points"):
            gaps.append({
                "kind": "process-control-coverage",
                "id": process["id"],
                "reason": "Process has no explicit control points.",
            })

    for case_id, case in indexes["cases"].items():
        if not case.get("source_ids"):
            gaps.append({
                "kind": "case-source-coverage",
                "id": case_id,
                "reason": "Case has no source IDs.",
            })
        if not case.get("limits"):
            gaps.append({
                "kind": "case-limitation-coverage",
                "id": case_id,
                "reason": "Case has no explicit limitations.",
            })
        if case.get("evidence_grade") == "D":
            gaps.append({
                "kind": "weak-evidence",
                "id": case_id,
                "reason": "Grade D is marketing-level evidence and must not be presented as implementation proof.",
            })

    for profile in matrix.get("profiles", []):
        if not profile.get("required_controls"):
            gaps.append({
                "kind": "decision-control-coverage",
                "id": profile["id"],
                "reason": "Decision profile has no required controls.",
            })
        if not profile.get("failure_pattern_ids"):
            gaps.append({
                "kind": "counter-evidence-coverage",
                "id": profile["id"],
                "reason": "Decision profile has no linked failure pattern.",
            })

    if reviewed_at:
        parsed = datetime.strptime(str(reviewed_at), "%Y-%m-%d").date()
        age = (date.today() - parsed).days
        if age > stale_after_days:
            gaps.append({
                "kind": "source-freshness",
                "id": "business-ai-catalog",
                "reason": f"Catalog review is {age} days old; freshness review is due.",
            })

    return gaps


def build_report():
    contract = load_yaml(DATA / "contract.yml")
    domain_map = load_yaml(DATA / "domain_map.yml")
    process_map = load_yaml(DATA / "process_map.yml")
    catalog = load_yaml(DATA / "catalog.yml")
    extensions = [load_yaml(DATA / name) for name in EXTENSIONS]
    scenarios = load_yaml(DATA / "scenario_library.yml")
    matrix = load_yaml(DATA / "assessment_matrix.yml")
    technologies = load_yaml(DATA / "technology_landscape.yml")

    indexes = validate_structure(
        contract,
        domain_map,
        process_map,
        catalog,
        extensions,
        scenarios,
        matrix,
        technologies,
    )
    gaps = coverage_gaps(
        indexes,
        catalog,
        domain_map,
        process_map,
        matrix,
        catalog.get("reviewed_at"),
    )
    return {
        "schema": "dkharlanau.business-ai.graph-integrity",
        "contract_version": contract["contract"]["version"],
        "structural_errors": 0,
        "counts": {key: len(value) for key, value in indexes.items()},
        "coverage_gap_count": len(gaps),
        "coverage_gaps": gaps,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate Business AI graph references and report strategic coverage gaps.")
    parser.add_argument("--json", action="store_true", help="Print the report as JSON.")
    args = parser.parse_args(argv)
    try:
        report = build_report()
    except (OSError, yaml.YAMLError, GraphIntegrityError, KeyError, ValueError) as exc:
        print(f"Business AI graph integrity failed: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(
            "Business AI graph integrity passed: "
            f"{sum(report['counts'].values())} indexed records, "
            f"{report['coverage_gap_count']} non-blocking coverage gaps"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
