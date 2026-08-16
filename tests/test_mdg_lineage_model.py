from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
TOPICS = ROOT / "_data" / "labs" / "enterprise_context" / "topics"
SOURCES = ROOT / "_data" / "labs" / "enterprise_context" / "sources" / "mdg_lineage_runtime_registry.yml"


def load_yaml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_mdg_lineage_has_end_to_end_dimensions_and_evidence():
    data = load_yaml(TOPICS / "mdg_lineage.yml")
    dimensions = {item["id"] for item in data["lineage_dimensions"]}
    assert dimensions == {
        "LIN-MDG-PROVENANCE",
        "LIN-MDG-GOVERNANCE",
        "LIN-MDG-TRANSFORMATION",
        "LIN-MDG-ACTIVATION",
        "LIN-MDG-DISTRIBUTION",
        "LIN-MDG-CONSUMPTION",
    }
    stages = {item["stage"] for item in data["audit_evidence"]}
    assert {"Request", "Rule processing", "Workflow", "Activation", "Replication", "Identity", "Consumption"} <= stages
    assert data["provenance_states"]["vocabulary_status"].startswith("Lab semantic vocabulary")


def test_mdg_runtime_covers_request_to_business_proof():
    data = load_yaml(TOPICS / "mdg_build_runtime.yml")
    chain = data["runtime_chain"]
    assert len(chain) == 12
    assert chain[0]["id"] == "MDG-RUN-SOURCE"
    assert chain[-1]["id"] == "MDG-RUN-PROVE"
    assert len(data["design_time_layers"]) == 12


def test_mdg_model_engineering_covers_cross_layer_change_impact():
    data = load_yaml(TOPICS / "mdg_data_model_engineering.yml")
    changes = {item["change"] for item in data["field_impact_matrix"]}
    assert "Add attribute" in changes
    assert "Add dependent entity" in changes
    assert "Change key or relationship" in changes


def test_mdg_source_refs_are_backed_by_primary_registry():
    registry = load_yaml(SOURCES)
    source_ids = {item["id"] for item in registry["sources"]}
    for filename in ["mdg_lineage.yml", "mdg_build_runtime.yml", "mdg_data_model_engineering.yml"]:
        topic = load_yaml(TOPICS / filename)
        for source_id in topic.get("source_refs", []):
            assert source_id in source_ids
    assert all(item["publisher"] == "SAP" for item in registry["sources"])
