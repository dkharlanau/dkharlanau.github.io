import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "products" / "manifest.json"


def load_manifest():
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


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
        "presentation-layer",
        "adjacent-execution-product",
        "adjacent-knowledge-product",
        "adjacent-interoperability-product",
    }
    for product in manifest["products"]:
        assert product["portfolio_role"] in allowed_roles
        assert product["owns"].strip()
        assert product["layer"] in manifest["layers"]
        assert product["id"] in manifest["layers"][product["layer"]]


def test_derived_products_declare_sources_and_visuals_are_not_business_truth():
    manifest = load_manifest()
    products = {product["id"]: product for product in manifest["products"]}

    for product in products.values():
        if product["portfolio_role"] == "derived-analysis":
            assert product.get("derived_from")
            assert all(source in products for source in product["derived_from"])

    assert products["visual-workbench"]["portfolio_role"] == "presentation-layer"
    assert "only" in products["visual-workbench"]["owns"].lower()


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
