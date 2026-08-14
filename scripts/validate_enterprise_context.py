#!/usr/bin/env python3
"""Validate structural integrity of the Enterprise Context Lab graph."""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

import yaml


DEFAULT_ROOT = Path("_data/labs/enterprise_context")
TOPIC_REQUIRED = {"id", "type", "title", "summary", "domain", "status", "created_at", "updated_at"}
SOURCE_REQUIRED = {"id", "publisher", "source_type", "title", "accessed_at", "status"}
RELATION_REQUIRED = {"from", "type", "to", "evidence_type", "confidence"}
CONFIDENCE_LEVELS = {"low", "medium", "high"}


@dataclass
class Finding:
    severity: str
    code: str
    message: str
    path: Path

    def render(self) -> str:
        return f"{self.severity.upper():7} {self.code:30} {self.path}: {self.message}"


@dataclass
class Report:
    findings: list[Finding] = field(default_factory=list)
    topic_count: int = 0
    source_count: int = 0
    entity_count: int = 0
    relation_count: int = 0

    def add(self, severity: str, code: str, message: str, path: Path) -> None:
        self.findings.append(Finding(severity, code, message, path))

    @property
    def errors(self) -> list[Finding]:
        return [item for item in self.findings if item.severity == "error"]

    @property
    def warnings(self) -> list[Finding]:
        return [item for item in self.findings if item.severity == "warning"]


def load_yaml(path: Path, report: Report) -> Any:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return yaml.safe_load(handle)
    except (OSError, yaml.YAMLError) as exc:
        report.add("error", "invalid_yaml", str(exc), path)
        return None


def walk(value: Any) -> Iterable[dict[str, Any]]:
    if isinstance(value, dict):
        yield value
        for nested in value.values():
            yield from walk(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from walk(nested)


def iter_relations(value: Any) -> Iterable[dict[str, Any]]:
    for node in walk(value):
        relations = node.get("relations")
        if isinstance(relations, list):
            for relation in relations:
                if isinstance(relation, dict):
                    yield relation


def iter_source_refs(value: Any) -> Iterable[str]:
    for node in walk(value):
        refs = node.get("source_refs")
        if isinstance(refs, list):
            for ref in refs:
                if isinstance(ref, str):
                    yield ref


def schema_vocab(schema: dict[str, Any]) -> tuple[dict[str, str], set[str], set[str], set[str]]:
    node_prefixes = {
        item["id"]: item["prefix"]
        for item in schema.get("node_types", [])
        if isinstance(item, dict) and item.get("id") and item.get("prefix")
    }
    edge_types = {item for item in schema.get("edge_types", []) if isinstance(item, str)}
    evidence_types = {item for item in schema.get("evidence_types", []) if isinstance(item, str)}
    statuses = {item for item in schema.get("statuses", []) if isinstance(item, str)}
    return node_prefixes, edge_types, evidence_types, statuses


def validate(root: Path = DEFAULT_ROOT) -> Report:
    report = Report()
    schema_path = root / "schema.yml"
    manifest_path = root / "manifest.yml"
    contract_path = root / "model_contract.yml"

    for required_path in (schema_path, manifest_path, contract_path):
        if not required_path.exists():
            report.add("error", "missing_core_file", "Required Lab control file is missing.", required_path)

    schema = load_yaml(schema_path, report) if schema_path.exists() else {}
    if not isinstance(schema, dict):
        report.add("error", "invalid_schema", "schema.yml must contain a mapping.", schema_path)
        schema = {}

    node_prefixes, edge_types, evidence_types, statuses = schema_vocab(schema)

    topic_docs: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted((root / "topics").glob("*.yml")):
        data = load_yaml(path, report)
        if not isinstance(data, dict):
            if data is not None:
                report.add("error", "invalid_topic_root", "Topic root must be a mapping.", path)
            continue
        report.topic_count += 1
        topic_docs.append((path, data))
        missing = sorted(TOPIC_REQUIRED - set(data))
        if missing:
            report.add("error", "missing_topic_fields", f"Missing: {', '.join(missing)}", path)
        if data.get("type") != "research_topic":
            report.add("warning", "unexpected_topic_type", f"Expected research_topic, got {data.get('type')!r}.", path)
        if not data.get("tags"):
            report.add("warning", "topic_without_tags", "Topic has no tags.", path)
        status = data.get("status")
        if status and statuses and status not in statuses:
            report.add("error", "unknown_topic_status", f"Unknown status {status!r}.", path)

    sources_by_id: dict[str, tuple[Path, dict[str, Any]]] = {}
    for path in sorted((root / "sources").glob("*.yml")):
        data = load_yaml(path, report)
        if not isinstance(data, dict):
            if data is not None:
                report.add("error", "invalid_source_root", "Source registry root must be a mapping.", path)
            continue
        sources = data.get("sources", [])
        if not isinstance(sources, list):
            report.add("error", "invalid_sources_collection", "Top-level sources must be a list.", path)
            continue
        for source in sources:
            if not isinstance(source, dict):
                report.add("error", "invalid_source_record", "Source entry must be a mapping.", path)
                continue
            source_id = source.get("id")
            missing = sorted(SOURCE_REQUIRED - set(source))
            if missing:
                report.add("error", "missing_source_fields", f"{source_id or '<unknown>'}: missing {', '.join(missing)}", path)
            if not isinstance(source_id, str) or not source_id:
                report.add("error", "missing_source_id", "Source entry has no valid id.", path)
                continue
            report.source_count += 1
            if source_id in sources_by_id:
                first_path, first_source = sources_by_id[source_id]
                if first_source != source:
                    report.add("error", "duplicate_source_id", f"{source_id} also appears in {first_path} with different metadata.", path)
                else:
                    report.add("warning", "repeated_source_id", f"{source_id} duplicates an identical record from {first_path}.", path)
            else:
                sources_by_id[source_id] = (path, source)

    entity_occurrences: dict[str, list[tuple[Path, dict[str, Any]]]] = defaultdict(list)
    for path, data in topic_docs:
        for node in walk(data):
            entity_type = node.get("type")
            entity_id = node.get("id")
            if entity_type in node_prefixes and isinstance(entity_id, str):
                entity_occurrences[entity_id].append((path, node))
                expected_prefix = f"{node_prefixes[entity_type]}-"
                if not entity_id.startswith(expected_prefix):
                    report.add(
                        "warning",
                        "id_prefix_mismatch",
                        f"{entity_id} is type {entity_type}; expected prefix {expected_prefix}",
                        path,
                    )

    report.entity_count = len(entity_occurrences)
    for entity_id, occurrences in sorted(entity_occurrences.items()):
        types = {node.get("type") for _, node in occurrences}
        if len(types) > 1:
            locations = ", ".join(str(path) for path, _ in occurrences)
            report.add("error", "conflicting_entity_type", f"{entity_id} has types {sorted(types)} across {locations}.", occurrences[0][0])

    known_entities = set(entity_occurrences)
    known_sources = set(sources_by_id)

    for path, data in topic_docs:
        seen_triples: set[tuple[str, str, str]] = set()
        for relation in iter_relations(data):
            report.relation_count += 1
            missing = sorted(RELATION_REQUIRED - set(relation))
            if missing:
                report.add("error", "missing_relation_fields", f"Missing: {', '.join(missing)}", path)
                continue

            source = relation.get("from")
            edge_type = relation.get("type")
            target = relation.get("to")
            evidence_type = relation.get("evidence_type")
            confidence = relation.get("confidence")

            if edge_types and edge_type not in edge_types:
                report.add("error", "unknown_edge_type", f"Unknown relation type {edge_type!r}.", path)
            if source not in known_entities:
                report.add("error", "unresolved_relation_endpoint", f"Unknown from endpoint {source!r}.", path)
            if target not in known_entities:
                report.add("error", "unresolved_relation_endpoint", f"Unknown to endpoint {target!r}.", path)
            if evidence_types and evidence_type not in evidence_types:
                report.add("error", "unknown_evidence_type", f"Unknown evidence type {evidence_type!r}.", path)
            if confidence not in CONFIDENCE_LEVELS:
                report.add("error", "unknown_confidence", f"Unknown confidence {confidence!r}.", path)

            triple = (str(source), str(edge_type), str(target))
            if triple in seen_triples:
                report.add("error", "duplicate_relation", f"Duplicate relation {source} -[{edge_type}]-> {target}.", path)
            seen_triples.add(triple)

            if source == target and not relation.get("rationale"):
                report.add("warning", "self_relation_without_rationale", f"Self relation for {source} has no rationale.", path)
            if evidence_type == "documented_fact" and not relation.get("source_refs"):
                report.add("warning", "documented_relation_without_source", f"{source} -[{edge_type}]-> {target} has no source_refs.", path)

        for source_ref in sorted(set(iter_source_refs(data))):
            if source_ref not in known_sources:
                report.add("error", "unknown_source_ref", f"Unknown source reference {source_ref}.", path)

    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT, help="Enterprise Context data root")
    parser.add_argument("--strict-warnings", action="store_true", help="Treat warnings as failures")
    args = parser.parse_args()

    report = validate(args.root)
    for finding in report.findings:
        print(finding.render())

    print(
        "\nEnterprise Context: "
        f"{report.topic_count} topics, {report.entity_count} entities, "
        f"{report.relation_count} relations, {report.source_count} source records; "
        f"{len(report.errors)} errors, {len(report.warnings)} warnings."
    )

    if report.errors or (args.strict_warnings and report.warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
