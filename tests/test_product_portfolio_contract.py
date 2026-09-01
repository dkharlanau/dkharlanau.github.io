import json
import hashlib
from pathlib import Path
import subprocess
import sys
from urllib.parse import urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "products" / "manifest.json"
INTEROPERABILITY = ROOT / "products" / "interoperability.json"
TRUST_BOUNDARIES = ROOT / "products" / "trust-boundaries.json"
JEKYLL_PROJECTION = ROOT / "_data" / "public_portfolio.yml"

EXPECTED_PUBLIC_REPOSITORIES = {
    "agent-ready-web-profile",
    "ai-cv-builder",
    "cutover-graph",
    "data-relationship-map",
    "decision-tables-as-code",
    "dkharlanau-datasets",
    "enterprise-architecture-composer",
    "enterprise-change-graph",
    "interface-as-code",
    "mapping-as-code",
    "process-as-code",
    "project-evidence-graph",
    "reconciliation-as-code",
    "sap-agentic-operations",
    "signal-to-insight",
    "transformation-graph",
    "visual-workbench",
}


def load_manifest():
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def load_interoperability():
    return json.loads(INTEROPERABILITY.read_text(encoding="utf-8"))


def load_trust_boundaries():
    return json.loads(TRUST_BOUNDARIES.read_text(encoding="utf-8"))


def load_jekyll_projection():
    return yaml.safe_load(JEKYLL_PROJECTION.read_text(encoding="utf-8"))


def test_portfolio_manifest_has_problem_first_entrypoints_and_unique_products():
    manifest = load_manifest()
    assert manifest["schema_version"] == "1.3"
    products = manifest["products"]
    ids = [product["id"] for product in products]
    assert len(ids) == len(set(ids))
    assert set(ids) == EXPECTED_PUBLIC_REPOSITORIES

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
        "architecture-composer",
        "adjacent-profile-product",
        "adjacent-evidence-product",
    }
    for product in manifest["products"]:
        assert product["portfolio_role"] in allowed_roles
        assert product["title"].strip()
        assert product["summary"].strip()
        assert product["owns"].strip()
        assert product["layer"] in manifest["layers"]
        assert product["id"] in manifest["layers"][product["layer"]]


def test_reader_map_classifies_all_17_projects_without_equal_card_priority():
    manifest = load_manifest()
    reader_map = manifest["reader_map"]
    tracks = {track["id"]: track for track in reader_map["tracks"]}

    assert reader_map["repository_count"] == 17
    assert set(tracks) == {
        "enterprise-design",
        "transformation-assurance",
        "sap-practical-ai",
    }
    assert tracks["enterprise-design"]["primary_projects"] == [
        "enterprise-architecture-composer",
        "visual-workbench",
    ]
    assert tracks["transformation-assurance"]["primary_projects"] == [
        "project-evidence-graph"
    ]
    assert tracks["sap-practical-ai"]["primary_projects"] == [
        "sap-agentic-operations",
        "signal-to-insight",
    ]

    classified = []
    primary = []
    for track in tracks.values():
        classified.extend(track["primary_projects"])
        classified.extend(track["supporting_projects"])
        primary.extend(track["primary_projects"])

    assert len(classified) == len(set(classified)) == 17
    assert set(classified) == EXPECTED_PUBLIC_REPOSITORIES
    assert len(primary) == 5
    assert "not evidence of external adoption" in reader_map["boundaries"]["adoption"]
    assert "not implied" in reader_map["boundaries"]["compatibility"]

    reference_case = reader_map["reference_case"]
    assert reference_case["id"] == "enterprise-change-evidence-pack"
    assert reference_case["status"] == "synthetic-reproducible-demonstration"
    assert reference_case["human_url"].endswith(
        "/machine/portfolio/enterprise-change-evidence-pack/"
    )
    assert reference_case["machine_url"].endswith(
        "/products/reference-cases/enterprise-change-evidence-pack/manifest.json"
    )
    assert "does not prove external adoption" in reference_case["boundary"]

    actions = {action["id"]: action for action in reader_map["actions"]}
    assert set(actions) == {"run", "propose", "collaborate"}
    assert actions["run"]["href"] == "/machine/portfolio/enterprise-change-evidence-pack/"
    assert "portfolio-integration.yml" in actions["propose"]["href"]
    assert actions["collaborate"]["href"].startswith("https://www.linkedin.com/")


def test_jekyll_portfolio_data_is_a_checked_projection_of_the_canonical_manifest():
    manifest = load_manifest()
    projection = load_jekyll_projection()
    projection_meta = projection["projection"]

    assert projection_meta["canonical_source"] == "/products/manifest.json"
    assert projection_meta["canonical_schema_version"] == manifest["schema_version"]
    assert projection_meta["canonical_sha256"] == hashlib.sha256(MANIFEST.read_bytes()).hexdigest()

    reader_map = manifest["reader_map"]
    assert projection["observed_at"] == reader_map["observed_at"]
    assert projection["scope"]["repository_count"] == reader_map["repository_count"]
    assert projection["scope"]["selection"] == reader_map["selection"]
    assert projection["boundaries"] == reader_map["boundaries"]
    assert projection["reference_case"] == reader_map["reference_case"]
    assert projection["actions"] == reader_map["actions"]
    assert projection["homepage"] == reader_map["homepage"]
    assert projection["tracks"] == reader_map["tracks"]

    manifest_products = {product["id"]: product for product in manifest["products"]}
    projected_products = {product["id"]: product for product in projection["projects"]}
    assert set(projected_products) == set(manifest_products) == EXPECTED_PUBLIC_REPOSITORIES
    for project_id, projected in projected_products.items():
        canonical = manifest_products[project_id]
        assert projected["title"] == canonical["title"]
        assert projected["description"] == canonical["summary"]
        assert projected["repository_url"] == canonical["repository"]
        assert projected["public_url"] == canonical["page"]

        track = next(
            item for item in reader_map["tracks"]
            if project_id in item["primary_projects"] + item["supporting_projects"]
        )
        expected_role = "primary" if project_id in track["primary_projects"] else "supporting"
        assert projected["track_id"] == track["id"]
        assert projected["role"] == expected_role


def test_public_portfolio_projection_generator_check_passes():
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_public_portfolio.py"), "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "projection is current" in result.stdout


def test_public_project_map_uses_the_projection_and_preserves_verification_boundary():
    page = (ROOT / "machine" / "portfolio" / "index.md").read_text(encoding="utf-8")
    endpoint = (ROOT / "ai" / "public-portfolio.json").read_text(encoding="utf-8")
    machine = (ROOT / "machine" / "index.md").read_text(encoding="utf-8")
    agent_tools = (ROOT / "agent-tools" / "index.md").read_text(encoding="utf-8")
    ai_hub = (ROOT / "ai" / "index.md").read_text(encoding="utf-8")

    assert "{% assign portfolio = site.data.public_portfolio %}" in page
    assert 'status: needs_verification' in page
    assert 'verified: false' in page
    assert 'robots: noindex,follow' in page
    assert 'sitemap: false' in page
    assert 'ai_sidecar: /ai/public-portfolio.json' in page
    assert 'where: "role", "primary"' in page
    assert 'where: "role", "supporting"' in page
    assert "portfolio-track__primary--single" in page
    assert "not a compatibility claim" in page
    assert "Open public entry" in page
    assert "portfolio.reference_case" in page
    assert "portfolio.actions" in page
    assert "project.public_action" not in page

    assert "{{ site.data.public_portfolio | jsonify }}" in endpoint
    assert "/machine/portfolio/" in machine
    assert "/ai/public-portfolio.json" in machine
    assert "/machine/portfolio/" in agent_tools
    assert "/ai/public-portfolio.json" in ai_hub

    legacy_products = (ROOT / "products" / "index.html").read_text(encoding="utf-8")
    assert 'rel="canonical" href="https://dkharlanau.github.io/machine/portfolio/"' in legacy_products
    assert 'http-equiv="refresh"' not in legacy_products
    assert "The maintained reader map lives" in legacy_products
    assert "/products/manifest.json" in legacy_products

    issue_form = yaml.safe_load(
        (ROOT / ".github" / "ISSUE_TEMPLATE" / "portfolio-integration.yml").read_text(
            encoding="utf-8"
        )
    )
    assert issue_form["name"] == "Portfolio integration proposal"
    fields = {
        item["id"]: item
        for item in issue_form["body"]
        if isinstance(item, dict) and item.get("id")
    }
    assert set(fields) == {
        "producer",
        "consumer",
        "decision",
        "artifact",
        "fixture",
        "verification",
        "boundaries",
    }
    assert fields["boundaries"]["type"] == "checkboxes"


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


def test_portfolio_trust_contract_separates_identity_integrity_authority_and_assurance():
    contract = load_trust_boundaries()
    assert contract["schema_version"] == "0.1"
    assert contract["scope"] == "portfolio-cross-repository-artifacts"

    assert set(contract["separate_states"]) == {
        "identity",
        "structural_validity",
        "content_integrity",
        "provenance",
        "authorization",
        "assurance",
    }

    defaults = contract["default_posture"]
    assert defaults["cross_repository_input_trusted_by_default"] is False
    assert defaults["upstream_artifact_can_expand_consumer_authority"] is False
    assert defaults["embedded_or_referenced_code_executes_by_default"] is False
    assert defaults["secrets_are_portable_artifact_content"] is False

    integrity = contract["integrity"]
    assert integrity["sha256_proves_content_identity"] is True
    assert integrity["sha256_implies_authorization"] is False
    assert integrity["sha256_implies_business_approval"] is False
    assert integrity["sha256_implies_positive_assurance"] is False


def test_portfolio_trust_contract_fails_closed_and_keeps_public_private_data_boundary():
    contract = load_trust_boundaries()
    consumer = contract["consumer_requirements"]
    assert consumer["validate_supported_contracts_only"] is True
    assert consumer["fail_closed_on_required_missing_binding"] is True
    assert consumer["fail_closed_on_required_ambiguous_binding"] is True
    assert consumer["fail_closed_on_integrity_pin_mismatch"] is True
    assert consumer["execute_upstream_scripts_by_reference"] is False

    data = contract["data_boundary"]
    assert data["enterprise_data_local_private_by_default"] is True
    assert data["public_examples_synthetic_or_redacted"] is True
    assert data["public_projection_may_copy_raw_enterprise_evidence_by_default"] is False

    secrets = contract["secrets"]
    assert secrets["credentials_are_runtime_inputs"] is True
    assert secrets["portable_evidence_may_persist_passwords_tokens_or_private_keys"] is False

    assert "automatic trust between repositories owned by the same account" in contract["non_goals"]
