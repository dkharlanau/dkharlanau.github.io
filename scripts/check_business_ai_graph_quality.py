#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "_data" / "labs" / "business_ai"

sys.path.insert(0, str(ROOT))
from scripts.check_business_ai_contract import ContractError, validate_graph_payload


RULES = {
    "BAI-GRAPH-001": ("error", "Duplicate stable ID", "Keep one stable ID for one concept and update references instead of creating aliases."),
    "BAI-GRAPH-002": ("error", "Broken process reference", "Point the cross-link to an existing Business AI process ID."),
    "BAI-GRAPH-003": ("error", "Broken process-stage reference", "Use the exact stage name from process_map.yml."),
    "BAI-GRAPH-004": ("error", "Broken canonical route", "Point the graph node to an existing public source page."),
    "BAI-GRAPH-005": ("error", "Missing enterprise boundary", "Record data, integration, authority, and control boundaries for the mapped process."),
    "BAI-GRAPH-006": ("error", "Invalid built graph", "Fix the generated node, edge, relationship, or contract mismatch."),
    "BAI-GRAPH-007": ("error", "Unreachable high-value node", "Connect the process, case, or enterprise context node through a typed relationship."),
    "BAI-GRAPH-008": ("error", "Insufficient SAP process coverage", "Keep explicit SAP context links for at least four priority process families."),
    "BAI-GAP-001": ("gap", "Missing explicit case review state", "Move the case through the evidence-review lifecycle; do not auto-promote it."),
    "BAI-GAP-002": ("gap", "Missing stable case process link", "Attach the case to one or more canonical EndToEndProcess IDs when the source supports the mapping."),
    "BAI-GAP-003": ("gap", "Missing case evidence source", "Add source IDs or keep the case outside reviewed evidence views."),
    "BAI-GAP-004": ("gap", "Missing case limitation", "Record what the public evidence does not establish."),
    "BAI-GAP-005": ("gap", "Metric lacks evidence source", "Link reported metrics to the evidence source that reports them."),
    "BAI-GAP-006": ("gap", "Platform or technology node is not connected", "Add supported technology-family relationships when the source model contains them."),
    "BAI-GAP-007": ("gap", "Process stage has no case coverage", "Research or map a case only when evidence supports this stage."),
    "BAI-GAP-008": ("gap", "Decision profile lacks control or failure test", "Add explicit control and failure-mode links before using the profile for high-impact decisions."),
    "BAI-GAP-009": ("gap", "Evidence review is stale", "Re-check the source set and update reviewed_at without changing evidence grade automatically."),
    "BAI-GAP-010": ("gap", "Weak evidence carries a strong-looking metric", "Keep the reported number, claim type, evidence grade, and limitation visible together."),
    "BAI-GAP-011": ("gap", "Projected case metadata", "Replace projection defaults with explicit canonical fields during case-schema upgrade."),
}


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def finding(rule_id: str, message: str, *, entity_id: str | None = None) -> dict[str, Any]:
    severity, title, remediation = RULES[rule_id]
    payload: dict[str, Any] = {
        "rule_id": rule_id,
        "severity": severity,
        "title": title,
        "message": message,
        "remediation": remediation,
    }
    if entity_id:
        payload["entity_id"] = entity_id
    return payload


def duplicate_findings(items: list[dict[str, Any]], label: str) -> list[dict[str, Any]]:
    ids = [str(item.get("id")) for item in items if item.get("id")]
    return [
        finding("BAI-GRAPH-001", f"Duplicate {label} ID: {item_id}.", entity_id=item_id)
        for item_id, count in Counter(ids).items()
        if count > 1
    ]


def route_exists(canonical_ref: str) -> bool:
    if not canonical_ref.startswith("/") or "://" in canonical_ref:
        return False
    clean = canonical_ref.split("#", 1)[0].split("?", 1)[0].strip("/")
    if not clean:
        return True
    path = ROOT / clean
    if path.is_file():
        return True
    if path.is_dir() and (path / "index.md").exists():
        return True
    if path.suffix:
        return path.exists()
    return path.with_suffix(".md").exists() or (path / "index.md").exists()


def all_catalog_records() -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    records = [
        load_yaml(DATA / "catalog.yml"),
        load_yaml(DATA / "expansion_2026_08_15.yml"),
        load_yaml(DATA / "expansion_2026_08_15_b.yml"),
    ]
    patterns: list[dict[str, Any]] = []
    cases: list[dict[str, Any]] = []
    sources: list[dict[str, Any]] = []
    for record in records:
        patterns.extend(record.get("patterns") or [])
        cases.extend(record.get("cases") or [])
        sources.extend(record.get("source_registry") or [])
    return patterns, cases, sources


def collect_source_findings(today: date | None = None) -> list[dict[str, Any]]:
    today = today or date.today()
    process_map = load_yaml(DATA / "process_map.yml")
    links = load_yaml(DATA / "enterprise_context_links.yml")
    technology = load_yaml(DATA / "technology_landscape.yml")
    assessment = load_yaml(DATA / "assessment_matrix.yml")
    catalog = load_yaml(DATA / "catalog.yml")
    patterns, cases, sources = all_catalog_records()

    findings: list[dict[str, Any]] = []
    processes = process_map.get("processes") or []
    process_by_id = {item.get("id"): item for item in processes if item.get("id")}

    findings.extend(duplicate_findings(processes, "process"))
    findings.extend(duplicate_findings(patterns, "pattern"))
    findings.extend(duplicate_findings(cases, "case"))
    findings.extend(duplicate_findings(sources, "evidence source"))
    findings.extend(duplicate_findings(links.get("process_links") or [], "enterprise context mapping"))

    mapped_processes: set[str] = set()
    required_boundary_fields = (
        "data_dependencies",
        "integration_boundaries",
        "authority_boundaries",
        "control_boundaries",
    )
    for mapping in links.get("process_links") or []:
        mapping_id = mapping.get("id") or "unknown-mapping"
        process_id = mapping.get("process_id")
        process = process_by_id.get(process_id)
        if not process:
            findings.append(finding("BAI-GRAPH-002", f"{mapping_id} points to unknown process {process_id!r}.", entity_id=mapping_id))
            continue
        mapped_processes.add(process_id)
        stages = set(process.get("stages") or [])
        for field in required_boundary_fields:
            if not mapping.get(field):
                findings.append(finding("BAI-GRAPH-005", f"{mapping_id} has no {field}.", entity_id=mapping_id))
        for page in mapping.get("context_pages") or []:
            page_id = page.get("id") or mapping_id
            canonical_ref = page.get("canonical_ref") or ""
            if not route_exists(canonical_ref):
                findings.append(finding("BAI-GRAPH-004", f"{page_id} points to missing route {canonical_ref!r}.", entity_id=page_id))
            for stage in page.get("stages") or []:
                if stage not in stages:
                    findings.append(finding("BAI-GRAPH-003", f"{page_id} points to unknown stage {stage!r} in {process_id}.", entity_id=page_id))

    if len(mapped_processes) < 4:
        findings.append(finding("BAI-GRAPH-008", f"Only {len(mapped_processes)} Business AI processes have SAP Enterprise context links."))

    case_process_stage_coverage: defaultdict[str, set[str]] = defaultdict(set)
    source_ids = {item.get("id") for item in sources if item.get("id")}
    for item in cases:
        case_id = item.get("id") or "unknown-case"
        if not item.get("review_state"):
            findings.append(finding("BAI-GAP-001", f"{case_id} has no explicit review_state.", entity_id=case_id))
        process_ids = item.get("process_ids") or []
        if not process_ids:
            findings.append(finding("BAI-GAP-002", f"{case_id} has no stable process_ids.", entity_id=case_id))
        else:
            for process_id in process_ids:
                if process_id not in process_by_id:
                    findings.append(finding("BAI-GRAPH-002", f"{case_id} references unknown process {process_id!r}.", entity_id=case_id))
                for stage in item.get("process_stages") or []:
                    case_process_stage_coverage[process_id].add(stage)
        item_source_ids = item.get("source_ids") or []
        if not item_source_ids:
            findings.append(finding("BAI-GAP-003", f"{case_id} has no evidence source IDs.", entity_id=case_id))
        for source_id in item_source_ids:
            if source_id not in source_ids:
                findings.append(finding("BAI-GRAPH-006", f"{case_id} references missing evidence source {source_id!r}.", entity_id=case_id))
        if not item.get("limits"):
            findings.append(finding("BAI-GAP-004", f"{case_id} has no explicit limitations.", entity_id=case_id))
        if item.get("reported_results") and not item_source_ids:
            findings.append(finding("BAI-GAP-005", f"{case_id} reports metrics without an evidence source.", entity_id=case_id))
        if item.get("evidence_grade") in {"C", "D"} and item.get("reported_results"):
            findings.append(finding("BAI-GAP-010", f"{case_id} has evidence grade {item.get('evidence_grade')} and reported metrics; keep claim type and limitations visible.", entity_id=case_id))

    for process in processes:
        process_id = process.get("id")
        if not process_id:
            continue
        covered = case_process_stage_coverage.get(process_id, set())
        missing = [stage for stage in process.get("stages") or [] if stage not in covered]
        if missing:
            findings.append(finding("BAI-GAP-007", f"{process_id} has {len(missing)} stage(s) without explicit case-stage coverage.", entity_id=process_id))

    for platform in technology.get("platforms") or []:
        if not platform.get("technology_family_ids"):
            findings.append(finding("BAI-GAP-006", f"{platform.get('id')} has no explicit technology_family_ids.", entity_id=platform.get("id")))

    for profile in assessment.get("decision_profiles") or []:
        profile_id = profile.get("id") or "unknown-decision-profile"
        if not profile.get("control_ids") or not profile.get("failure_pattern_ids"):
            findings.append(finding("BAI-GAP-008", f"{profile_id} does not yet link both controls and failure-mode tests.", entity_id=profile_id))

    reviewed_at = catalog.get("reviewed_at")
    if reviewed_at:
        reviewed = datetime.strptime(str(reviewed_at), "%Y-%m-%d").date()
        age = (today - reviewed).days
        if age > 180:
            findings.append(finding("BAI-GAP-009", f"Business AI catalog review is {age} days old."))

    return findings


def collect_graph_findings(graph: dict[str, Any], contract: dict[str, Any]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    try:
        validate_graph_payload(graph, contract)
    except ContractError as exc:
        return [finding("BAI-GRAPH-006", str(exc))]

    nodes = graph.get("nodes") or []
    edges = graph.get("edges") or []
    degree: Counter[str] = Counter()
    for edge in edges:
        degree[edge["from"]] += 1
        degree[edge["to"]] += 1

    for node in nodes:
        node_id = node.get("id")
        node_type = node.get("type")
        canonical_ref = node.get("canonical_ref")
        if not canonical_ref:
            findings.append(finding("BAI-GRAPH-004", f"{node_id} has no canonical_ref.", entity_id=node_id))
        if degree[node_id] == 0:
            if node_type in {"EndToEndProcess", "BusinessAICase", "EnterpriseContextPage"}:
                findings.append(finding("BAI-GRAPH-007", f"{node_id} ({node_type}) is unreachable.", entity_id=node_id))
            else:
                findings.append(finding("BAI-GAP-006", f"{node_id} ({node_type}) is currently unconnected.", entity_id=node_id))
        if node_type == "BusinessAICase" and node.get("projection_flags"):
            findings.append(finding("BAI-GAP-011", f"{node_id} uses projection defaults: {', '.join(node['projection_flags'])}.", entity_id=node_id))
    return findings


def build_report(site: Path | None = None, today: date | None = None) -> dict[str, Any]:
    findings = collect_source_findings(today=today)
    graph_path = None
    if site is not None:
        graph_path = site / "machine" / "business-ai" / "graph.json"
        if not graph_path.exists():
            findings.append(finding("BAI-GRAPH-006", f"Built graph is missing: {graph_path}."))
        else:
            try:
                graph = json.loads(graph_path.read_text(encoding="utf-8"))
                contract = load_yaml(DATA / "contract.yml")
                findings.extend(collect_graph_findings(graph, contract))
            except (OSError, json.JSONDecodeError) as exc:
                findings.append(finding("BAI-GRAPH-006", f"Cannot read built graph: {exc}."))

    errors = [item for item in findings if item["severity"] == "error"]
    gaps = [item for item in findings if item["severity"] == "gap"]
    by_rule = Counter(item["rule_id"] for item in findings)
    return {
        "schema": "business-ai-graph-quality@1",
        "generated_at": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "graph_path": str(graph_path) if graph_path else None,
        "summary": {
            "errors": len(errors),
            "coverage_gaps": len(gaps),
            "status": "fail" if errors else "pass_with_gaps" if gaps else "pass",
            "by_rule": dict(sorted(by_rule.items())),
        },
        "findings": findings,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Business AI graph integrity and evidence coverage.")
    parser.add_argument("--site", type=Path, help="Built Jekyll site root. When supplied, validate the generated graph JSON too.")
    parser.add_argument("--report", type=Path, help="Optional JSON report output path.")
    args = parser.parse_args(argv)

    try:
        report = build_report(site=args.site)
    except (OSError, yaml.YAMLError, ValueError) as exc:
        print(f"Business AI graph quality failed: {exc}", file=sys.stderr)
        return 1

    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    summary = report["summary"]
    print(json.dumps(summary, sort_keys=True))
    if summary["errors"]:
        for item in report["findings"]:
            if item["severity"] == "error":
                print(f"{item['rule_id']}: {item['message']}", file=sys.stderr)
        return 1
    print(f"Business AI graph quality passed with {summary['coverage_gaps']} advisory coverage gap(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
