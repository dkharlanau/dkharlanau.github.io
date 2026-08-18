#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "_data" / "labs" / "business_ai"
EXTENSIONS = (
    "expansion_2026_08_15.yml",
    "expansion_2026_08_15_b.yml",
    "expansion_2026_08_15_c.yml",
)


class PortfolioError(ValueError):
    pass


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def by_id(records, label):
    result = {}
    for record in records or []:
        record_id = record.get("id") if isinstance(record, dict) else None
        if not record_id:
            raise PortfolioError(f"{label} record is missing id")
        if record_id in result:
            raise PortfolioError(f"Duplicate {label} id: {record_id}")
        result[record_id] = record
    return result


def aggregate_catalog():
    catalog = load_yaml(DATA / "catalog.yml")
    patterns = list(catalog.get("patterns", []))
    cases = list(catalog.get("cases", []))
    sources = list(catalog.get("source_registry", []))
    for name in EXTENSIONS:
        extension = load_yaml(DATA / name)
        patterns.extend(extension.get("patterns", []))
        cases.extend(extension.get("cases", []))
        sources.extend(extension.get("source_registry", []))
    return catalog, patterns, cases, sources


def has_metrics(record):
    return bool(record.get("metrics") or record.get("reported_metrics"))


def has_limitations(record):
    return bool(record.get("limitations") or record.get("limits"))


def normalized_maturity(record):
    return record.get("implementation_maturity") or "unknown"


def normalized_autonomy(record):
    return record.get("autonomy_level") or "unknown"


def validate_failure_intelligence(
    failure_data,
    scenarios,
    failure_patterns,
    patterns,
    stages,
    technologies,
    profiles,
):
    evidence_kinds = set(failure_data.get("evidence_kinds", {}))
    cause_categories = set(failure_data.get("cause_categories", []))
    observed = by_id(failure_data.get("observed_records", []), "observed failure")
    risks = by_id(failure_data.get("plausible_risks", []), "plausible risk")
    overlap = set(observed) & set(risks)
    if overlap:
        raise PortfolioError(f"Failure and risk IDs overlap: {sorted(overlap)}")

    for record_id, record in observed.items():
        kind = record.get("evidence_kind")
        if kind not in evidence_kinds or kind == "plausible_risk":
            raise PortfolioError(f"{record_id} has invalid observed evidence kind: {kind}")
        scenario_id = record.get("scenario_id")
        if scenario_id not in scenarios:
            raise PortfolioError(f"{record_id} references missing scenario: {scenario_id}")
        scenario = scenarios[scenario_id]
        if not scenario.get("source_ids"):
            raise PortfolioError(f"{record_id} observed scenario has no source evidence")
        for field, values, known, label in (
            ("failure_pattern_ids", record.get("failure_pattern_ids"), failure_patterns, "failure pattern"),
            ("pattern_ids", record.get("pattern_ids"), patterns, "pattern"),
            ("process_stage_ids", record.get("process_stage_ids"), stages, "process stage"),
            ("technology_family_ids", record.get("technology_family_ids"), technologies, "technology family"),
            ("decision_profile_ids", record.get("decision_profile_ids"), profiles, "decision profile"),
        ):
            for value in values or []:
                if value not in known:
                    raise PortfolioError(
                        f"{record_id} field {field} references missing {label}: {value}"
                    )
        for category in record.get("cause_categories", []):
            if category not in cause_categories:
                raise PortfolioError(
                    f"{record_id} has unknown cause category: {category}"
                )
        if not record.get("control_lessons"):
            raise PortfolioError(f"{record_id} is missing control lessons")
        if not record.get("interpretation_boundary"):
            raise PortfolioError(f"{record_id} is missing interpretation boundary")

    for record_id, record in risks.items():
        if record.get("evidence_kind") != "plausible_risk":
            raise PortfolioError(f"{record_id} must use plausible_risk evidence kind")
        if record.get("scenario_id"):
            raise PortfolioError(
                f"{record_id} plausible risk cannot claim an observed scenario"
            )
        for field, values, known, label in (
            ("failure_pattern_ids", record.get("failure_pattern_ids"), failure_patterns, "failure pattern"),
            ("pattern_ids", record.get("pattern_ids"), patterns, "pattern"),
            ("process_stage_ids", record.get("process_stage_ids"), stages, "process stage"),
            ("technology_family_ids", record.get("technology_family_ids"), technologies, "technology family"),
        ):
            for value in values or []:
                if value not in known:
                    raise PortfolioError(
                        f"{record_id} field {field} references missing {label}: {value}"
                    )
        for category in record.get("cause_categories", []):
            if category not in cause_categories:
                raise PortfolioError(
                    f"{record_id} has unknown cause category: {category}"
                )
        for required in ("statement", "basis", "controls"):
            if not record.get(required):
                raise PortfolioError(f"{record_id} is missing {required}")

    return observed, risks


def build_domain_coverage(domains, cases, strong_grades):
    result = []
    for domain in domains.values():
        linked = [cases[item] for item in domain.get("case_ids", []) if item in cases]
        result.append(
            {
                "id": domain["id"],
                "title": domain.get("title"),
                "linked_case_count": len(linked),
                "strong_evidence_count": sum(
                    1 for case in linked if case.get("evidence_grade") in strong_grades
                ),
                "metric_case_count": sum(1 for case in linked if has_metrics(case)),
                "limitation_case_count": sum(
                    1 for case in linked if has_limitations(case)
                ),
                "case_ids": [case["id"] for case in linked],
            }
        )
    return result


def build_pattern_coverage(patterns, cases, observed, risks, strong_grades):
    case_by_pattern = defaultdict(list)
    for case in cases.values():
        pattern_ids = case.get("pattern_ids") or ([] if not case.get("pattern") else [case["pattern"]])
        for pattern_id in pattern_ids:
            case_by_pattern[pattern_id].append(case)
    observed_by_pattern = Counter()
    risk_by_pattern = Counter()
    for record in observed.values():
        observed_by_pattern.update(record.get("pattern_ids", []))
    for record in risks.values():
        risk_by_pattern.update(record.get("pattern_ids", []))

    result = []
    for pattern in patterns.values():
        linked = case_by_pattern.get(pattern["id"], [])
        result.append(
            {
                "id": pattern["id"],
                "title": pattern.get("title"),
                "linked_case_count": len(linked),
                "strong_evidence_count": sum(
                    1 for case in linked if case.get("evidence_grade") in strong_grades
                ),
                "observed_negative_count": observed_by_pattern[pattern["id"]],
                "plausible_risk_count": risk_by_pattern[pattern["id"]],
            }
        )
    return result


def build_industry_coverage(cases, strong_grades):
    totals = Counter()
    strong = Counter()
    measured = Counter()
    for case in cases.values():
        industry = case.get("industry") or "Unknown"
        totals[industry] += 1
        if case.get("evidence_grade") in strong_grades:
            strong[industry] += 1
        if has_metrics(case):
            measured[industry] += 1
    return [
        {
            "industry": industry,
            "case_count": totals[industry],
            "strong_evidence_count": strong[industry],
            "metric_case_count": measured[industry],
        }
        for industry in sorted(totals)
    ]


def build_process_coverage(processes, stages, sap_links, observed):
    stage_count = Counter(stage.get("process_id") for stage in stages.values())
    observed_by_process = Counter()
    for record in observed.values():
        process_ids = {
            stages[stage_id].get("process_id")
            for stage_id in record.get("process_stage_ids", [])
            if stage_id in stages
        }
        observed_by_process.update(item for item in process_ids if item)

    control_link_count = Counter()
    for link in sap_links.get("stage_links", []):
        stage = stages.get(link.get("stage_id"))
        if stage and stage.get("process_id"):
            control_link_count[stage["process_id"]] += 1

    return [
        {
            "id": process["id"],
            "title": process.get("title"),
            "legacy_stage_count": len(process.get("stages", [])),
            "stable_stage_count": stage_count[process["id"]],
            "pattern_count": len(process.get("pattern_ids", [])),
            "technology_family_count": len(process.get("technology_families", [])),
            "process_control_point_count": len(process.get("control_points", [])),
            "sap_authority_control_link_count": control_link_count[process["id"]],
            "observed_negative_count": observed_by_process[process["id"]],
        }
        for process in processes.values()
    ]


def gap_factor(count, target):
    if target <= 0:
        return 0.0
    if count <= 0:
        return 1.0
    if count < target:
        return 0.5
    return 0.0


def build_priorities(model, domains, cases, stages, sap_links, observed, strong_grades):
    weights = model["priority_model"]["weights"]
    stage_process = {
        stage_id: stage.get("process_id") for stage_id, stage in stages.items()
    }
    observed_process = Counter()
    for record in observed.values():
        process_ids = {
            stage_process.get(stage_id)
            for stage_id in record.get("process_stage_ids", [])
            if stage_process.get(stage_id)
        }
        observed_process.update(process_ids)

    stage_link_process = Counter()
    for link in sap_links.get("stage_links", []):
        process_id = stage_process.get(link.get("stage_id"))
        if process_id:
            stage_link_process[process_id] += 1
    domain_link_count = Counter(
        link.get("domain_id") for link in sap_links.get("domain_links", [])
    )
    stable_stage_count = Counter(stage_process.values())

    priorities = []
    for item in model.get("strategic_slices", []):
        linked_case_ids = set()
        for domain_id in item.get("domain_ids", []):
            domain = domains.get(domain_id, {})
            linked_case_ids.update(domain.get("case_ids", []))
        linked_cases = [cases[case_id] for case_id in linked_case_ids if case_id in cases]
        strong_evidence_count = sum(
            1 for case in linked_cases if case.get("evidence_grade") in strong_grades
        )
        control_links = sum(
            stage_link_process[process_id] for process_id in item.get("process_ids", [])
        ) + sum(domain_link_count[domain_id] for domain_id in item.get("domain_ids", []))
        stable_stages = sum(
            stable_stage_count[process_id] for process_id in item.get("process_ids", [])
        )
        negative_count = sum(
            observed_process[process_id] for process_id in item.get("process_ids", [])
        )

        strong_target = max(int(item.get("target_strong_evidence", 0)), 1)
        evidence_gap = 1.0 - min(strong_evidence_count / strong_target, 1.0)
        control_gap = gap_factor(control_links, int(item.get("target_control_links", 0)))
        machine_gap = gap_factor(stable_stages, int(item.get("target_stable_stages", 0)))
        if negative_count <= 0:
            negative_gap = 1.0
        elif negative_count == 1:
            negative_gap = 0.5
        else:
            negative_gap = 0.0
        strategic = float(item.get("strategic_relevance", 0.0))

        factors = {
            "strategic_relevance": strategic,
            "strong_evidence_gap": round(evidence_gap, 4),
            "control_gap": control_gap,
            "negative_evidence_gap": negative_gap,
            "machine_readiness_gap": machine_gap,
        }
        score = round(
            sum(float(weights[name]) * value for name, value in factors.items()),
            2,
        )
        reasons = []
        if evidence_gap > 0:
            reasons.append(
                f"{strong_evidence_count}/{strong_target} target strong-evidence cases"
            )
        if control_gap > 0:
            reasons.append(
                f"{control_links}/{item.get('target_control_links', 0)} target authority/control links"
            )
        if negative_gap > 0:
            reasons.append(f"{negative_count} source-backed negative records linked")
        if machine_gap > 0:
            reasons.append(
                f"{stable_stages}/{item.get('target_stable_stages', 0)} target stable stages"
            )
        priorities.append(
            {
                "id": item["id"],
                "title": item["title"],
                "score": score,
                "factors": factors,
                "linked_case_count": len(linked_cases),
                "strong_evidence_count": strong_evidence_count,
                "authority_control_link_count": control_links,
                "observed_negative_count": negative_count,
                "stable_stage_count": stable_stages,
                "reasons": reasons,
            }
        )

    priorities.sort(key=lambda row: (-row["score"], row["id"]))
    for rank, row in enumerate(priorities, 1):
        row["rank"] = rank
    return priorities


def build_decision_evidence(profiles, observed):
    observed_by_failure = defaultdict(list)
    for record in observed.values():
        for failure_id in record.get("failure_pattern_ids", []):
            observed_by_failure[failure_id].append(record["id"])
    result = []
    for profile in profiles.values():
        failure_ids = profile.get("failure_pattern_ids", [])
        challenging = sorted(
            {
                record_id
                for failure_id in failure_ids
                for record_id in observed_by_failure.get(failure_id, [])
            }
        )
        result.append(
            {
                "id": profile["id"],
                "supporting_scenario_ids": profile.get("scenario_ids", []),
                "challenging_failure_pattern_ids": failure_ids,
                "challenging_observed_record_ids": challenging,
            }
        )
    return result


def build_report():
    contract = load_yaml(DATA / "contract.yml")
    coverage_model = load_yaml(DATA / "coverage_model.yml")
    failure_data = load_yaml(DATA / "failure_intelligence.yml")
    domain_map = load_yaml(DATA / "domain_map.yml")
    process_map = load_yaml(DATA / "process_map.yml")
    scenario_data = load_yaml(DATA / "scenario_library.yml")
    matrix = load_yaml(DATA / "assessment_matrix.yml")
    technologies_data = load_yaml(DATA / "technology_landscape.yml")
    sap_links = load_yaml(DATA / "sap_process_links.yml")
    catalog, pattern_records, case_records, _ = aggregate_catalog()

    domains = by_id(domain_map.get("domains", []), "domain")
    processes = by_id(process_map.get("processes", []), "process")
    patterns = by_id(pattern_records, "pattern")
    cases = by_id(case_records, "case")
    scenarios = by_id(scenario_data.get("scenarios", []), "scenario")
    failure_patterns = by_id(
        scenario_data.get("failure_patterns", []), "failure pattern"
    )
    stages = by_id(sap_links.get("process_stages", []), "process stage")
    technologies = by_id(technologies_data.get("families", []), "technology family")
    profiles = by_id(matrix.get("profiles", []), "decision profile")

    observed, risks = validate_failure_intelligence(
        failure_data,
        scenarios,
        failure_patterns,
        patterns,
        stages,
        technologies,
        profiles,
    )

    strong_grades = set(coverage_model["strong_evidence_rule"]["grades"])
    strong_statuses = set(coverage_model["strong_case_rule"]["statuses"])
    evidence_grades = Counter(case.get("evidence_grade") or "unknown" for case in cases.values())
    maturity = Counter(normalized_maturity(case) for case in cases.values())
    autonomy = Counter(normalized_autonomy(case) for case in cases.values())
    decision_autonomy = Counter(
        profile.get("recommended_autonomy") or "unknown" for profile in profiles.values()
    )
    scenario_grades = Counter(
        scenario.get("evidence_grade") or "unknown" for scenario in scenarios.values()
    )
    scenario_status = Counter(
        scenario.get("status") or "unknown" for scenario in scenarios.values()
    )

    priorities = build_priorities(
        coverage_model,
        domains,
        cases,
        stages,
        sap_links,
        observed,
        strong_grades,
    )

    return {
        "schema": "dkharlanau.business-ai.portfolio-coverage",
        "coverage_model_version": coverage_model["schema_version"],
        "contract_version": contract["contract"]["version"],
        "reviewed_at": catalog.get("reviewed_at"),
        "snapshot_key": f"{contract['contract']['version']}+{catalog.get('reviewed_at')}",
        "summary": {
            "catalog_case_count": len(cases),
            "scenario_count": len(scenarios),
            "strong_case_count": sum(
                1 for scenario in scenarios.values() if scenario.get("status") in strong_statuses
            ),
            "strong_scenario_evidence_count": sum(
                1 for scenario in scenarios.values() if scenario.get("evidence_grade") in strong_grades
            ),
            "strong_catalog_evidence_count": sum(
                1 for case in cases.values() if case.get("evidence_grade") in strong_grades
            ),
            "catalog_metric_case_count": sum(1 for case in cases.values() if has_metrics(case)),
            "catalog_limitation_case_count": sum(
                1 for case in cases.values() if has_limitations(case)
            ),
            "observed_negative_count": len(observed),
            "plausible_risk_count": len(risks),
            "case_control_count": sum(1 for case in cases.values() if case.get("controls")),
            "process_control_count": sum(
                1 for process in processes.values() if process.get("control_points")
            ),
            "decision_profile_control_count": sum(
                1 for profile in profiles.values() if profile.get("required_controls")
            ),
        },
        "dimensions": {
            "domains": build_domain_coverage(domains, cases, strong_grades),
            "processes": build_process_coverage(processes, stages, sap_links, observed),
            "patterns": build_pattern_coverage(
                patterns, cases, observed, risks, strong_grades
            ),
            "industries": build_industry_coverage(cases, strong_grades),
            "evidence_grades": dict(sorted(evidence_grades.items())),
            "scenario_evidence_grades": dict(sorted(scenario_grades.items())),
            "scenario_status": dict(sorted(scenario_status.items())),
            "implementation_maturity": dict(sorted(maturity.items())),
            "case_autonomy": dict(sorted(autonomy.items())),
            "decision_profile_autonomy": dict(sorted(decision_autonomy.items())),
        },
        "research_priorities": priorities,
        "negative_evidence": {
            "observed_records": list(observed.values()),
            "plausible_risks": list(risks.values()),
            "decision_evidence": build_decision_evidence(profiles, observed),
        },
        "trend_contract": coverage_model.get("trend_contract", {}),
        "method": {
            "strong_case_rule": coverage_model.get("strong_case_rule"),
            "strong_evidence_rule": coverage_model.get("strong_evidence_rule"),
            "negative_evidence_rule": coverage_model.get("negative_evidence_rule"),
            "measurement_rule": coverage_model.get("measurement_rule"),
            "control_rule": coverage_model.get("control_rule"),
            "priority_model": coverage_model.get("priority_model"),
        },
    }


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Analyze Business AI portfolio coverage, evidence gaps, and negative evidence."
    )
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        report = build_report()
    except (OSError, yaml.YAMLError, KeyError, PortfolioError) as exc:
        print(f"Business AI portfolio analysis failed: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        top = report["research_priorities"][0] if report["research_priorities"] else None
        print(
            "Business AI portfolio analysis passed: "
            f"{report['summary']['catalog_case_count']} catalog cases, "
            f"{report['summary']['observed_negative_count']} observed negative records, "
            f"top research priority {top['id'] if top else 'none'}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
