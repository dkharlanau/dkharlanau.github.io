from pathlib import Path

import yaml


MANIFEST_PATH = Path("_data/labs/enterprise_context/manifest.yml")


EXPECTED_HUMAN_VIEWS = {
    "sales_process_atlas": "/labs/enterprise-context/sales-processes/",
    "sales_process_coverage": "/labs/enterprise-context/sales-processes/coverage/",
    "sales_control_plane": "/labs/enterprise-context/sales-processes/control-plane/",
    "sales_mechanisms": "/labs/enterprise-context/sales-processes/mechanisms/",
    "sales_integrations": "/labs/enterprise-context/sales-processes/integrations/",
    "sales_master_data": "/labs/enterprise-context/sales-processes/master-data/",
    "sales_diagnostic_casebook": "/labs/enterprise-context/sales-diagnostics/",
}

EXPECTED_MACHINE_ENDPOINTS = {
    "sales_process_atlas": "/labs/enterprise-context/data/sales-process-atlas.json",
    "sales_process_coverage": "/labs/enterprise-context/data/sales-process-coverage.json",
    "sales_process_sources": "/labs/enterprise-context/data/sales-process-sources.json",
    "sales_mechanisms": "/labs/enterprise-context/data/sales-mechanisms.json",
    "sales_control_plane": "/labs/enterprise-context/data/sales-control-plane.json",
    "sales_return_claims_control_plane": "/labs/enterprise-context/data/sales-return-claims-control-plane.json",
    "sales_order_integration_map": "/labs/enterprise-context/data/sales-order-integration-map.json",
    "sales_diagnostic_casebook": "/labs/enterprise-context/data/sales-diagnostic-casebook.json",
}


def load_manifest():
    return yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8"))


def url_to_repo_path(url: str) -> Path:
    relative = url.removeprefix("/labs/enterprise-context/")
    if relative.startswith("data/"):
        return Path("labs/enterprise-context") / relative
    return Path("labs/enterprise-context") / relative / "index.html"


def test_sales_human_views_are_registered_and_exist():
    manifest = load_manifest()
    views = manifest["human_views"]

    for key, url in EXPECTED_HUMAN_VIEWS.items():
        assert views.get(key) == url
        assert url_to_repo_path(url).exists(), f"Missing human view for {key}: {url}"


def test_sales_machine_endpoints_are_registered_and_exist():
    manifest = load_manifest()
    endpoints = manifest["machine_endpoints"]

    for key, url in EXPECTED_MACHINE_ENDPOINTS.items():
        assert endpoints.get(key) == url
        assert url_to_repo_path(url).exists(), f"Missing machine endpoint for {key}: {url}"


def test_sales_diagnostic_casebook_is_a_registered_deep_dive():
    manifest = load_manifest()
    deep_dives = {item["id"]: item for item in manifest["deep_dives"]}

    casebook = deep_dives["DEEP-SD-DIAGNOSTIC-CASEBOOK"]
    assert casebook["parent_topic"] == "TOPIC-O2C-SALES-ORDER-CREATION"
    assert casebook["page_url"] == "/labs/enterprise-context/sales-diagnostics/"
    assert casebook["graph_ref"] == "GRAPH-SD-SALES-DIAGNOSTIC-CASEBOOK"
