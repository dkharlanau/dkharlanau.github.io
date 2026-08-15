from pathlib import Path

import yaml


ROOT = Path("_data/labs/enterprise_context")
GRAPH_PATH = ROOT / "graphs" / "pricing_anatomy.yml"
SOURCE_ROOT = ROOT / "sources"
PAGE_PATH = Path("labs/enterprise-context/pricing/anatomy/index.html")
GRAPH_ENDPOINT = Path("labs/enterprise-context/data/pricing-anatomy.json")
SOURCE_ENDPOINT = Path("labs/enterprise-context/data/pricing-anatomy-sources.json")


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


def test_pricing_anatomy_ids_are_unique_and_sources_resolve():
    graph = load_yaml(GRAPH_PATH)
    sources = all_source_ids()

    ids = []
    source_refs = []
    for node in walk(graph):
        node_id = node.get("id")
        if isinstance(node_id, str):
            ids.append(node_id)
        refs = node.get("source_refs")
        if isinstance(refs, list):
            source_refs.extend(ref for ref in refs if isinstance(ref, str))

    assert len(ids) == len(set(ids)), "Pricing anatomy IDs must be unique"
    assert source_refs, "Pricing anatomy must remain source-tracked"
    missing = sorted(set(source_refs) - sources)
    assert not missing, f"Unknown pricing anatomy source refs: {missing}"


def test_pricing_anatomy_keeps_core_condition_dimensions():
    graph = load_yaml(GRAPH_PATH)

    families = {item["id"] for item in graph["condition_families"]}
    assert {
        "PRCA-FAM-BASE",
        "PRCA-FAM-DISCOUNT",
        "PRCA-FAM-SURCHARGE",
        "PRCA-FAM-GROUP",
        "PRCA-FAM-MANUAL",
        "PRCA-FAM-FREE",
    } <= families

    bases = {item["id"] for item in graph["base_models"]}
    assert {
        "PRCA-BASE-QTY",
        "PRCA-BASE-VALUE",
        "PRCA-BASE-SUBTOTAL",
        "PRCA-BASE-GROUP",
        "PRCA-BASE-FORMULA",
    } <= bases

    scales = {item["id"] for item in graph["scale_models"]}
    assert {
        "PRCA-SCALE-FROM",
        "PRCA-SCALE-TO",
        "PRCA-SCALE-GRAD",
        "PRCA-SCALE-GROUP",
    } <= scales


def test_free_goods_and_formula_roles_do_not_collapse_into_generic_pricing():
    graph = load_yaml(GRAPH_PATH)

    free_goods_variants = {item["id"] for item in graph["free_goods_model"]["variants"]}
    assert free_goods_variants == {"PRCA-FG-INCLUSIVE", "PRCA-FG-EXCLUSIVE"}

    fits = {item["best_fit"] for item in graph["formula_decision_table"]}
    assert "Requirement" in fits
    assert "Alternative condition base" in fits
    assert "Alternative calculation / condition amount logic" in fits
    assert "Group condition / group key logic" in fits


def test_pricing_anatomy_has_practitioner_patterns_and_diagnostics():
    graph = load_yaml(GRAPH_PATH)

    assert len(graph["extension_patterns"]) >= 7
    assert len(graph["practitioner_patterns"]) >= 8
    assert len(graph["failure_drills"]) >= 8
    assert len(graph["assessment_drills"]) >= 6

    for pattern in graph["practitioner_patterns"]:
        assert pattern.get("scenario")
        assert pattern.get("preferred_shape")
        assert pattern.get("trap")


def test_pricing_anatomy_human_and_machine_views_exist():
    assert PAGE_PATH.exists()
    assert GRAPH_ENDPOINT.exists()
    assert SOURCE_ENDPOINT.exists()

    page = PAGE_PATH.read_text(encoding="utf-8")
    assert "/labs/enterprise-context/data/pricing-anatomy.json" in page
    assert "/labs/enterprise-context/data/pricing-anatomy-sources.json" in page
    assert "Synthetic patterns" in page or "synthetic patterns" in page
