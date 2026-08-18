#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONTRACT = ROOT / "_data" / "labs" / "business_ai" / "contract.yml"
DEFAULT_FIXTURE = ROOT / "tests" / "fixtures" / "business_ai_graph_valid.yml"


class ContractError(ValueError):
    pass


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractError(message)


def validate_contract(contract: dict) -> None:
    _require(isinstance(contract, dict), "Contract must be a mapping.")
    meta = contract.get("contract")
    _require(isinstance(meta, dict), "Missing contract metadata.")
    _require(meta.get("id") == "business-ai-graph", "Unexpected contract id.")
    _require(bool(meta.get("version")), "Contract version is required.")

    source = contract.get("source_of_truth", {})
    datasets = source.get("datasets", {})
    _require(
        source.get("contract") == "_data/labs/business_ai/contract.yml",
        "Contract must identify itself as the source of truth.",
    )
    _require(isinstance(datasets, dict) and datasets, "Canonical datasets are required.")

    source_paths = {
        item.get("path") for item in datasets.values() if isinstance(item, dict)
    }
    outputs = contract.get("generated_outputs", [])
    _require(isinstance(outputs, list) and outputs, "Generated outputs must be declared.")
    _require(
        not (source_paths & set(outputs)),
        "A generated output cannot also be a canonical source.",
    )
    for source_path in source_paths:
        _require(
            (ROOT / source_path).exists(),
            f"Canonical dataset does not exist: {source_path}.",
        )

    vocabularies = contract.get("vocabularies", {})
    required_vocabularies = {
        "case_kind",
        "evidence_grade",
        "source_confidence",
        "review_state",
        "autonomy_level",
        "outcome_state",
        "evidence_level",
    }
    _require(
        required_vocabularies <= set(vocabularies),
        "Required controlled vocabularies are missing.",
    )
    for name, values in vocabularies.items():
        _require(
            isinstance(values, list) and values,
            f"Vocabulary {name} must be a non-empty list.",
        )
        _require(
            len(values) == len(set(values)),
            f"Vocabulary {name} contains duplicates.",
        )

    entity_types = contract.get("entity_types", [])
    _require(isinstance(entity_types, list) and entity_types, "Entity types are required.")
    _require(
        len(entity_types) == len(set(entity_types)),
        "Entity types must be unique.",
    )
    allowed_entities = set(entity_types)

    relationship_types = contract.get("relationship_types", [])
    _require(
        isinstance(relationship_types, list) and relationship_types,
        "Relationship types are required.",
    )
    relationship_ids = []
    for relation in relationship_types:
        _require(isinstance(relation, dict), "Each relationship type must be a mapping.")
        relation_id = relation.get("id")
        relationship_ids.append(relation_id)
        _require(
            relation.get("from") in allowed_entities,
            f"Relationship {relation_id} has an unknown source type.",
        )
        _require(
            relation.get("to") in allowed_entities,
            f"Relationship {relation_id} has an unknown target type.",
        )
    _require(
        len(relationship_ids) == len(set(relationship_ids)),
        "Relationship type IDs must be unique.",
    )

    field_vocabularies = contract.get("field_vocabularies", {})
    for field, vocabulary in field_vocabularies.items():
        _require(
            vocabulary in vocabularies,
            f"Field {field} points to unknown vocabulary {vocabulary}.",
        )


def validate_graph_payload(payload: dict, contract: dict) -> None:
    validate_contract(contract)
    _require(isinstance(payload, dict), "Graph payload must be a mapping.")
    _require(
        payload.get("contract_version") == contract["contract"]["version"],
        "Graph contract_version does not match the canonical contract.",
    )

    id_pattern = re.compile(contract["id_policy"]["entity_pattern"])
    relationship_id_pattern = re.compile(contract["id_policy"]["relationship_pattern"])
    entity_types = set(contract["entity_types"])
    vocabularies = contract["vocabularies"]
    field_vocabularies = contract["field_vocabularies"]
    required_fields = contract.get("required_fields_by_entity", {})

    nodes = payload.get("nodes", [])
    _require(isinstance(nodes, list), "nodes must be a list.")
    node_by_id = {}
    for node in nodes:
        _require(isinstance(node, dict), "Each node must be a mapping.")
        node_id = node.get("id", "")
        node_type = node.get("type")
        _require(bool(id_pattern.fullmatch(node_id)), f"Invalid node id: {node_id!r}.")
        _require(node_id not in node_by_id, f"Duplicate node id: {node_id}.")
        _require(
            node_type in entity_types,
            f"Node {node_id} has unknown type {node_type}.",
        )
        for field in required_fields.get(node_type, []):
            _require(
                node.get(field) not in (None, ""),
                f"Node {node_id} is missing required field {field}.",
            )
        for field, vocabulary_name in field_vocabularies.items():
            if field in node:
                _require(
                    node[field] in vocabularies[vocabulary_name],
                    f"Node {node_id} has invalid {field}: {node[field]!r}.",
                )
        node_by_id[node_id] = node

    relationships = {
        item["id"]: item for item in contract["relationship_types"]
    }
    edges = payload.get("edges", [])
    _require(isinstance(edges, list), "edges must be a list.")
    edge_ids = set()
    for edge in edges:
        _require(isinstance(edge, dict), "Each edge must be a mapping.")
        edge_id = edge.get("id", "")
        relation_id = edge.get("type")
        source_id = edge.get("from")
        target_id = edge.get("to")
        _require(
            bool(relationship_id_pattern.fullmatch(edge_id)),
            f"Invalid edge id: {edge_id!r}.",
        )
        _require(edge_id not in edge_ids, f"Duplicate edge id: {edge_id}.")
        _require(
            relation_id in relationships,
            f"Edge {edge_id} has unknown relationship type {relation_id}.",
        )
        _require(
            source_id in node_by_id,
            f"Edge {edge_id} references missing source node {source_id}.",
        )
        _require(
            target_id in node_by_id,
            f"Edge {edge_id} references missing target node {target_id}.",
        )
        relation = relationships[relation_id]
        _require(
            node_by_id[source_id]["type"] == relation["from"],
            f"Edge {edge_id} source type does not match {relation_id}.",
        )
        _require(
            node_by_id[target_id]["type"] == relation["to"],
            f"Edge {edge_id} target type does not match {relation_id}.",
        )
        edge_ids.add(edge_id)


def validate_source_alignment(contract: dict, catalog: dict, assessment: dict) -> None:
    validate_contract(contract)

    _require(
        set(catalog.get("evidence_grades", {}))
        == set(contract["vocabularies"]["evidence_grade"]),
        "Catalog evidence grades differ from the canonical contract.",
    )
    for case in catalog.get("cases", []):
        grade = case.get("evidence_grade")
        _require(
            grade in contract["vocabularies"]["evidence_grade"],
            f"Catalog case {case.get('id')} has invalid evidence grade {grade!r}.",
        )

    autonomy_ids = {
        item.get("id") for item in assessment.get("autonomy_levels", [])
    }
    _require(
        autonomy_ids == set(contract["vocabularies"]["autonomy_level"]),
        "Assessment autonomy levels differ from the canonical contract.",
    )


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate the canonical Business AI data and graph contract."
    )
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--graph", type=Path, default=DEFAULT_FIXTURE)
    args = parser.parse_args(argv)

    try:
        contract = load_yaml(args.contract)
        graph = load_yaml(args.graph)
        catalog = load_yaml(ROOT / "_data" / "labs" / "business_ai" / "catalog.yml")
        assessment = load_yaml(
            ROOT / "_data" / "labs" / "business_ai" / "assessment_matrix.yml"
        )
        validate_graph_payload(graph, contract)
        validate_source_alignment(contract, catalog, assessment)
    except (OSError, yaml.YAMLError, ContractError) as exc:
        print(f"Business AI contract failed: {exc}", file=sys.stderr)
        return 1

    print("Business AI contract passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
