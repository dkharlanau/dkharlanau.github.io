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
    "BAI-GRAPH-001": ("error", "Duplicate stable ID", "Keep one stable ID for one concept."),
    "BAI-GRAPH-002": ("error", "Broken process reference", "Use an existing Business AI process ID."),
    "BAI-GRAPH-003": ("error", "Broken stage reference", "Use the exact stage from process_map.yml."),
    "BAI-GRAPH-004": ("error", "Broken canonical route", "Point to an existing public source page."),
    "BAI-GRAPH-005": ("error", "Missing enterprise boundary", "Record data, integration, authority, and control boundaries."),
    "BAI-GRAPH-006": ("error", "Invalid built graph", "Fix node, edge, relationship, or contract mismatch."),
    "BAI-GRAPH-007": ("error", "Unreachable high-value node", "Connect the node with a typed relationship."),
    "BAI-GRAPH-008": ("error", "Insufficient SAP process coverage", "Map at least four priority process families."),
    "BAI-GAP-001": ("gap", "Missing explicit case review state", "Move the case through review; do not auto-promote it."),
    "BAI-GAP-002": ("gap", "Missing stable case process link", "Add canonical process_ids when evidence supports the mapping."),
    "BAI-GAP-003": ("gap", "Missing case evidence source", "Add source IDs or keep the gap explicit."),
    "BAI-GAP-004": ("gap", "Missing case limitation", "Record what the evidence does not establish."),
    "BAI-GAP-005": ("gap", "Metric lacks evidence source", "Link the metric to the source that reports it."),
    "BAI-GAP-006": ("gap", "Unconnected secondary node", "Add a supported relationship when the source model contains one."),
    "BAI-GAP-007": ("gap", "Process stage has no case coverage", "Research or map evidence for this stage."),
    "BAI-GAP-008": ("gap", "Decision profile lacks control or failure test", "Add both before high-impact reuse."),
    "BAI-GAP-009": ("gap", "Evidence review is stale", "Re-check sources; never auto-promote evidence."),
    "BAI-GAP-010": ("gap", "Weak evidence carries a strong-looking metric", "Keep grade, claim type, metric, and limitation together."),
    "BAI-GAP-011": ("gap", "Projected case metadata", "Replace projection defaults with explicit canonical fields."),
}


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def make_finding(rule_id: str, message: str, entity_id: str | None = None) -> dict[str, Any]:
    severity, title, remediation = RULES[rule_id]
    result: dict[str, Any] = {
        "rule_id": rule_id,
        "severity": severity,
        "title": title,
        "message": message,
        "remediation": remediation,
    }
    if entity_id:
        result["entity_id"] = entity_id
    return result


def duplicate_findings(items: list[dict[str, Any]], label: str) -> list[dict[str, Any]]:
    counts = Counter(item.get("id") for item in items if item.get("id"))
    return [
        make_finding("BAI-GRAPH-001", f"Duplicate {label} ID: {item_id}.", str(item_id))
        for item_id, count in counts.items()
        if count > 1
    ]


def route_exists(canonical_ref: str) -> bool:
    if not canonical_ref.startswith("/") or "://" in canonical_ref:
        return False
    clean = canonical_ref.split("#", 1)[0].split("?", 1)[0].strip("/")
    if not clean:
        return True
    path = ROOT / clean
    candidates = [
        path,
        path.with_suffix(".md"),
        path.with_suffix(".html"),
        path / "index.md",
        path / "index.html",
    ]
    return any(candidate.is_file() for candidate in candidates)


def catalog_records() -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    datasets = [
        load_yaml(DATA / "catalog.yml"),
        load_yaml(DATA / "expansion_2026_08_15.yml"),
        load_yaml(DATA / "expansion_2026_08_15_b.yml"),
    ]
    patterns: list[dict[str, Any]] = []
    cases: list[dict[str, Any]] = []
    sources: list[dict[str, Any]] = []
    for dataset in datasets:
        patterns.extend(dataset.get("patterns") or [])
        cases.extend(dataset.get("cases") or [])
        sources.extend(dataset.get("source_registry") or [])
    return patterns, cases, sources


def collect_source_findings(today: date | None = None) -> list[dict[str, Any]]:
    today = today or date.today()
    process_map = load_yaml(DATA / "process_map.yml")
    link_map = load_yaml(DATA / "enterprise_context_links.yml")
    technology = load_yaml(DATA / "technology_landscape.yml")
    assessment = load_yaml(DATA / "assessment_matrix.yml")
    catalog = load_yaml(DATA / "catalog.yml")
    patterns, cases, sources = catalog_records()

    findings: list[dict[str, Any]] = []
    processes = process_map.get("processes") or []
    process_by_id = {item["id"]: item for item in processes if item.get("id")}
    source_ids = {item["id"] for item in sources if item.get("id")}

    for items, label in (
        (processes, "process"),
        (patterns, "pattern"),
        (cases, "case"),
        (sources, "evidence source"),
        (link_map.get("process_links") or [], "enterprise mapping"),
    ):
        findings.extend(duplicate_findings(items, label))

    mapped_processes: set[str] = set()
    for mapping in link_map.get("process_links") or []:
        mapping_id = mapping.get("id") or "unknown-mapping"
        process_id = mapping.get("process_id")
        process = process_by_id.get(process_id)
        if not process:
            findings.append(make_finding("BAI-GRAPH-002", f"{mapping_id} points to unknown process {process_id!r}.", mapping_id))
            continue
        mapped_processes.add(process_id)
        stage_names = set(process.get("stages") or [])
        for field in ("data_dependencies", "integration_boundaries", "authority_boundaries", "control_boundaries"):
            if not mapping.get(field):
                findings.append(make_finding("BAI-GRAPH-005", f"{mapping_id} has no {field}.", mapping_id))
        for page in mapping.get("context_pages") or []:
            page_id = page.get("id") or mapping_id
            ref = page.get("canonical_ref") or ""
            if not route_exists(ref):
                findings.append(make_finding("BAI-GRAPH-004", f"{page_id} points to missing route {ref!r}.", page_id))
            for stage in page.get("stages") or []:
                if stage not in stage_names:
                    findings.append(make_finding("BAI-GRAPH-003", f"{page_id} points to unknown stage {stage!r} in {process_id}.", page_id))

    if len(mapped_processes) < 4:
        findings.append(make_finding("BAI-GRAPH-008", f"Only {len(mapped_processes)} Business AI processes have SAP context links."))

    stage_coverage: defaultdict[str, set[str]] = defaultdict(set)
    for item in cases:
        case_id = item.get("id") or "unknown-case"
        if not item.get("review_state"):
            findings.append(make_finding("BAI-GAP-001", f"{case_id} has no explicit review_state.", case_id))
        process_ids = item.get("process_ids") or []
        if not process_ids:
            findings.append(make_finding("BAI-GAP-002", f"{case_id} has no stable process_ids.", case_id))
        for process_id in process_ids:
            if process_id not in process_by_id:
                findings.append(make_finding("BAI-GRAPH-002", f"{case_id} references unknown process {process_id!r}.", case_id))
            stage_coverage[process_id].update(item.get("process_stages") or [])
        case_sources = item.get("source_ids") or []
        if not case_sources:
            findings.append(make_finding("BAI-GAP-003", f"{case_id} has no evidence source IDs.", case_id))
        for source_id in case_sources:
            if source_id not in source_ids:
                findings.append(make_finding("BAI-GRAPH-006", f"{case_id} references missing evidence source {source_id!r}.", case_id))
        if not item.get("limits"):
            findings.append(make_finding("BAI-GAP-004", f"{case_id} has no explicit limitations.", case_id))
        if item.get("reported_results") and not case_sources:
            findings.append(make_finding("BAI-GAP-005", f"{case_id} reports metrics without evidence sources.", case_id))
        if item.get("evidence_grade") in {"C", "D"} and item.get("reported_results"):
            findings.append(make_finding("BAI-GAP-010", f"{case_id} has grade {item.get('evidence_grade')} and reported metrics.", case_id))

    for process in processes:
        process_id = process.get("id")
        if not process_id:
            continue
        missing = [stage for stage in process.get("stages") or [] if stage not in stage_coverage.get(process_id, set())]
        if missing:
            findings.append(make_finding("BAI-GAP-007", f"{process_id} has {len(missing)} stage(s) without explicit case-stage coverage.", process_id))

    for platform in technology.get("platforms") or []:
        if not platform.get("technology_family_ids"):
            findings.append(make_finding("BAI-GAP-006", f"{platform.get('id')} has no explicit technology_family_ids.", platform.get("id")))

    for profile in assessment.get("decision_profiles") or []:
        profile_id = profile.get("id") or "unknown-decision-profile"
        if not profile.get("control_ids") or not profile.get("failure_pattern_ids"):
            findings.append(make_finding("BAI-GAP-008", f"{profile_id} does not link both controls and failure tests.", profile_id))

    reviewed_at = catalog.get("reviewed_at")
    if reviewed_at:
        reviewed = datetime.strptime(str(reviewed_at), "%Y-%m-%d").date()
        age = (today - reviewed).days
        if age > 180:
            findings.append(make_finding("BAI-GAP-009", f"Catalog review is {age} days old."))

    return findings


def collect_graph_findings(graph: dict[str, Any], contract: dict[str, Any]) -> list[dict[str, Any]]:
    try:
        validate_graph_payload(graph, contract)
    except ContractError as exc:
        return [make_finding("BAI-GRAPH-006", str(exc))]

    findings: list[dict[str, Any]] = []
    degree: Counter[str] = Counter()
    for edge in graph.get("edges") or []:
        degree[edge["from"]] += 1
        degree[edge["to"]] += 1

    for node in graph.get("nodes") or []:
        node_id = node.get("id")
        node_type = node.get("type")
        if not node.get("canonical_ref"):
            findings.append(make_finding("BAI-GRAPH-004", f"{node_id} has no canonical_ref.", node_id))
        if degree[node_id] == 0:
            rule = "BAI-GRAPH-007" if node_type in {"EndToEndProcess", "BusinessAICase", "EnterpriseContextPage"} else "BAI-GAP-006"
            findings.append(make_finding(rule, f"{node_id} ({node_type}) is unconnected.", node_id))
        if node_type == "BusinessAICase" and node.get("projection_flags"):
            flags = ", ".join(node["projection_flags"])
            findings.append(make_finding("BAI-GAP-011", f"{node_id} uses projection defaults: {flags}.", node_id))
    return findings


def build_report(site: Path | None = None, today: date | None = None) -> dict[str, Any]:
    findings = collect_source_findings(today=today)
    graph_path: Path | None = None
    if site is not None:
        graph_path = site / "machine" / "business-ai" / "graph.json"
        if not graph_path.exists():
            findings.append(make_finding("BAI-GRAPH-006", f"Built graph is missing: {graph_path}."))
        else:
            try:
                graph = json.loads(graph_path.read_text(encoding="utf-8"))
                findings.extend(collect_graph_findings(graph, load_yaml(DATA / "contract.yml")))
            except (OSError, json.JSONDecodeError) as exc:
                findings.append(make_finding("BAI-GRAPH-006", f"Cannot read built graph: {exc}."))

    errors = [item for item in findings if item["severity"] == "error"]
    gaps = [item for item in findings if item["severity"] == "gap"]
    by_rule = Counter(item["rule_id"] for item in findings)
    return {
        "schema": "business-ai-graph-quality@1",
        "generated_at": datetime.now().astimezone().replace(microsecond=0).isoformat(),
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
    parser.add_argument("--site", type=Path, help="Built Jekyll site root; validates generated graph JSON too.")
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
