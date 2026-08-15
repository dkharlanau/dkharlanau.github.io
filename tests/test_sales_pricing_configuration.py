from pathlib import Path

import yaml


ROOT = Path("_data/labs/enterprise_context")
GRAPH_PATH = ROOT / "graphs" / "pricing_configuration.yml"
SOURCE_ROOT = ROOT / "sources"
PAGE_PATH = Path("labs/enterprise-context/pricing/configuration/index.html")
ENDPOINT_PATH = Path("labs/enterprise-context/data/pricing-configuration.json")


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def walk(value):
    if isinstance(value, dict):
        yield value
        for nested in value.values():
            yield from walk(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from walk(nested)


def all_source_ids() -> set[str]:
    ids: set[str] = set()
    for pattern in ("*.yml", "*.yaml", "*.json"):
        for path in SOURCE_ROOT.glob(pattern):
            data = load_yaml(path)
            if not isinstance(data, dict):
                continue
            for source in data.get("sources", []):
                if isinstance(source, dict) and isinstance(source.get("id"), str):
                    ids.add(source["id"])
    return ids


def test_pricing_configuration_sequence_is_ordered_and_source_tracked():
    graph = load_yaml(GRAPH_PATH)
    sequence = graph["configuration_sequence"]

    assert [item["order"] for item in sequence] == list(range(1, 11))
    assert len({item["id"] for item in sequence}) == len(sequence)

    known_sources = all_source_ids()
    referenced = set()
    for node in walk(graph):
        refs = node.get("source_refs")
        if isinstance(refs, list):
            referenced.update(ref for ref in refs if isinstance(ref, str))

    assert referenced
    assert not sorted(referenced - known_sources), f"Unknown pricing configuration source refs: {sorted(referenced - known_sources)}"


def test_pricing_configuration_separates_ownership_layers():
    graph = load_yaml(GRAPH_PATH)
    layers = {item["layer"] for item in graph["ownership_model"]}

    assert {
        "Customizing",
        "Pricing master data",
        "Business/master/document data",
        "Extension logic",
        "Copy / billing repricing",
    } == layers


def test_pricing_configuration_keeps_type_and_procedure_controls_distinct():
    graph = load_yaml(GRAPH_PATH)

    type_controls = {item["control"] for item in graph["condition_type_checklist"]}
    assert {
        "Condition class / business role",
        "Calculation type",
        "Rate source and access sequence",
        "Plus/minus and manual policy",
        "Header/item/group behavior",
        "Scale behavior",
    } <= type_controls

    row_controls = {item["control"] for item in graph["procedure_row_checklist"]}
    assert {
        "Step / counter",
        "Requirement",
        "From / To",
        "Subtotal",
        "Alternative base",
        "Alternative calculation",
    } <= row_controls


def test_pricing_configuration_has_boundary_test_matrix_and_guardrails():
    graph = load_yaml(GRAPH_PATH)
    dimensions = {item["dimension"] for item in graph["project_test_matrix"]}

    assert {
        "Base calculation",
        "Scales",
        "Quantity / UoM",
        "Currency",
        "Group conditions",
        "Competing conditions",
        "Free Goods",
        "Document lifecycle",
        "Extension",
    } == dimensions
    assert len(graph["extension_guardrails"]) >= 8
    assert len(graph["lead_failure_cases"]) >= 6


def test_pricing_configuration_human_and_machine_views_exist():
    assert PAGE_PATH.exists()
    assert ENDPOINT_PATH.exists()

    page = PAGE_PATH.read_text(encoding="utf-8")
    assert "/labs/enterprise-context/pricing/anatomy/" in page
    assert "/labs/enterprise-context/data/pricing-configuration.json" in page
    assert "Problem:" in page
    assert "Context:" in page
