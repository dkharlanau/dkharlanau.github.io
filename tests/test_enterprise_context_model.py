from pathlib import Path

import yaml

from scripts.validate_enterprise_context import validate


ROOT = Path("_data/labs/enterprise_context")


def write_yaml(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")


def minimal_root(tmp_path: Path) -> Path:
    root = tmp_path / "enterprise_context"
    write_yaml(
        root / "schema.yml",
        {
            "statuses": ["researching", "source_verified"],
            "evidence_types": ["documented_fact", "expert_heuristic"],
            "node_types": [
                {"id": "process", "prefix": "PROC"},
                {"id": "application_component", "prefix": "APP"},
            ],
            "edge_types": ["integrates_with", "precedes"],
        },
    )
    write_yaml(root / "manifest.yml", {"id": "lab-enterprise-context"})
    write_yaml(root / "model_contract.yml", {"version": "1.0.0"})
    write_yaml(
        root / "sources" / "registry.yml",
        {
            "sources": [
                {
                    "id": "SRC-ONE",
                    "publisher": "Example",
                    "source_type": "official_help",
                    "title": "Example source",
                    "accessed_at": "2026-08-14",
                    "status": "source_verified",
                }
            ]
        },
    )
    return root


def topic_payload() -> dict:
    return {
        "id": "TOPIC-TEST",
        "type": "research_topic",
        "title": "Test topic",
        "summary": "Fixture topic",
        "domain": "Test",
        "status": "researching",
        "created_at": "2026-08-14",
        "updated_at": "2026-08-14",
        "tags": ["test"],
        "entities": [
            {"id": "PROC-TEST-ONE", "type": "process", "title": "One"},
            {"id": "APP-TEST-TWO", "type": "application_component", "title": "Two"},
        ],
        "relations": [
            {
                "from": "PROC-TEST-ONE",
                "type": "integrates_with",
                "to": "APP-TEST-TWO",
                "evidence_type": "documented_fact",
                "confidence": "high",
                "source_refs": ["SRC-ONE"],
            }
        ],
        "source_refs": ["SRC-ONE"],
    }


def test_repository_enterprise_context_has_no_integrity_errors():
    report = validate(ROOT)
    assert not report.errors, "\n".join(finding.render() for finding in report.errors)


def test_validator_accepts_resolved_graph(tmp_path):
    root = minimal_root(tmp_path)
    write_yaml(root / "topics" / "topic.yml", topic_payload())

    report = validate(root)

    assert not report.errors
    assert report.topic_count == 1
    assert report.entity_count == 2
    assert report.relation_count == 1
    assert report.source_count == 1


def test_validator_rejects_unknown_relation_endpoint(tmp_path):
    root = minimal_root(tmp_path)
    topic = topic_payload()
    topic["relations"][0]["to"] = "APP-MISSING"
    write_yaml(root / "topics" / "topic.yml", topic)

    report = validate(root)

    assert any(item.code == "unresolved_relation_endpoint" for item in report.errors)


def test_validator_rejects_unknown_source_reference(tmp_path):
    root = minimal_root(tmp_path)
    topic = topic_payload()
    topic["source_refs"] = ["SRC-NOT-REGISTERED"]
    write_yaml(root / "topics" / "topic.yml", topic)

    report = validate(root)

    assert any(item.code == "unknown_source_ref" for item in report.errors)


def test_validator_rejects_duplicate_relation_in_same_topic(tmp_path):
    root = minimal_root(tmp_path)
    topic = topic_payload()
    topic["relations"].append(dict(topic["relations"][0]))
    write_yaml(root / "topics" / "topic.yml", topic)

    report = validate(root)

    assert any(item.code == "duplicate_relation" for item in report.errors)


def test_validator_rejects_conflicting_entity_type(tmp_path):
    root = minimal_root(tmp_path)
    topic = topic_payload()
    topic["entities"].append({"id": "PROC-TEST-ONE", "type": "application_component", "title": "Conflict"})
    write_yaml(root / "topics" / "topic.yml", topic)

    report = validate(root)

    assert any(item.code == "conflicting_entity_type" for item in report.errors)
