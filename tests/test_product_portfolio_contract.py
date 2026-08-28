import json
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "products" / "manifest.json"
INTEROPERABILITY = ROOT / "products" / "interoperability.json"


def load_manifest():
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def load_interoperability():
    return json.loads(INTEROPERABILITY.read_text(encoding="utf-8"))


def test_portfolio_manifest_has_problem_first_entrypoints_and_unique_products():
    manifest = load_manifest()
    assert manifest["schema_version"] == "1.2"
    products = manifest["products"]
    ids = [product["id"] for product in products]
    assert len(ids) == len(set(ids))
    assert "agent-ready-web-profile" in ids

    entrypoints = manifest["entrypoints"]
    assert len(entrypoints) >= 8
    assert all(item["product"] in ids for item in entrypoints)
    assert len({item["problem"] for item in entrypoints}) == len(entrypoints)


def test_every_product_declares_a_bounded_semantic_owner():
    manifest = load_manifest()
    allowed_roles = {
        "authoritative-contract",
        "bounded-analysis",
        "derived-analysis",
        "evidence-producer",
        "evidence-aware-execution",
        "assurance-graph",
        "visual-modeling-layer",
        "adjacent-execution-product",
        "adjacent-knowledge-product",
        "adjacent-interoperability-product",
    }
    for product in manifest["products"]:
        assert product["portfolio_role"] in allowed_roles
        assert product["owns"].strip()
        assert product["layer"] in manifest["layers"]
        assert product["id"] in manifest["layers"][product["layer"]]


def test_derived_products_declare_sources_and_visuals_do_not_take_imported_domain_ownership():
    manifest = load_manifest()
    products = {product["id"]: product for product in manifest["products"]}

    for product in products.values():
        if product["portfolio_role"] == "derived-analysis":
            assert product.get("derived_from")
            assert all(source in products for source in product["derived_from"])

    visual = products["visual-workbench"]
    assert visual["portfolio_role"] == "visual-modeling-layer"
    assert "visual semantic model" in visual["owns"].lower()
    assert "imported domain semantics remain upstream" in visual["owns"].lower()
    assert set(visual["consumes"]) >= {"process-as-code", "mapping-as-code", "interface-as-code"}


def test_cross_repo_ownership_direction_is_explicit():
    manifest = load_manifest()
    products = {product["id"]: product for product in manifest["products"]}

    assert products["mapping-as-code"]["portfolio_role"] == "authoritative-contract"
    assert "mapping-as-code" in products["reconciliation-as-code"]["consumes"]
    assert "reconciliation-as-code" in products["cutover-graph"]["consumes"]
    assert "cutover-graph" in products["project-evidence-graph"]["consumes"]

    rules = manifest["architecture"]
    assert "one owning product" in rules["source_of_truth_rule"]
    assert "deterministically regenerable" in rules["projection_rule"]
    assert "universal writable enterprise graph" in rules["graph_rule"]
    assert "not a network URL or trust assertion" in rules["reference_scheme"]


def test_interoperability_contract_keeps_identity_separate_from_trust():
    contract = load_interoperability()
    assert contract["schema_version"] == "0.1"
    assert contract["scheme"] == "eac"
    assert contract["syntax"]["network_dereference"] is False
    semantics = contract["semantics"]
    assert semantics["identity_only"] is True
    assert semantics["producer_owns_kind_and_local_id"] is True
    assert semantics["uri_presence_implies_existence"] is False
    assert semantics["uri_presence_implies_trust"] is False
    assert semantics["uri_presence_implies_positive_assurance"] is False
    assert semantics["consumer_must_use_explicit_binding_for_resolution"] is True

    provenance = set(contract["evidence_binding"]["recommended_provenance"])
    assert {"status", "document_sha256", "configuration_sha256", "observed_at"} <= provenance


def test_interoperability_examples_are_logical_eac_references_with_producer_ownership():
    contract = load_interoperability()
    examples = contract["implemented_examples"]
    assert len(examples) >= 3
    for example in examples:
        parts = urlsplit(example["reference"])
        assert parts.scheme == "eac"
        assert parts.netloc == "dkharlanau"
        segments = [segment for segment in parts.path.split("/") if segment]
        assert len(segments) >= 3
        assert segments[0] == example["producer"]
        assert segments[1] == example["kind"]

    current_consumers = {item["repository"] for item in contract["current_consumers"]}
    assert {"cutover-graph", "project-evidence-graph"} <= current_consumers
    assert "global network resolver" in contract["non_goals"]
    assert "automatic trust from a syntactically valid URI" in contract["non_goals"]
