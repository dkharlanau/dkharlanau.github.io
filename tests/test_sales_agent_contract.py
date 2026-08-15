from pathlib import Path

import yaml


ROOT = Path("_data/labs/enterprise_context")
CONTRACT_PATH = ROOT / "agent_contracts" / "sales.yml"
MANIFEST_PATH = ROOT / "manifest.yml"
ENDPOINT_PATH = Path("labs/enterprise-context/data/sales-agent-index.json")


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def endpoint_to_repo_path(url: str) -> Path:
    prefix = "/labs/enterprise-context/"
    assert url.startswith(prefix)
    return Path("labs/enterprise-context") / url.removeprefix(prefix)


def test_sales_agent_contract_has_stable_namespaces():
    contract = load_yaml(CONTRACT_PATH)
    namespaces = contract["namespaces"]
    prefixes = [item["prefix"] for item in namespaces]

    assert contract["id"] == "AGENT-CONTRACT-SD-SALES"
    assert len(prefixes) == len(set(prefixes))
    assert {"SD.", "MEC.SD.", "ORC.SD.", "INT.SD.", "EVT.SD.", "SDC."}.issubset(prefixes)

    for item in namespaces:
        assert endpoint_to_repo_path(item["primary_endpoint"]).exists()


def test_sales_agent_routing_starts_from_real_endpoints():
    contract = load_yaml(CONTRACT_PATH)

    assert len(contract["routing_rules"]) >= 7
    for rule in contract["routing_rules"]:
        assert rule["intent"]
        assert rule["reason"]
        assert endpoint_to_repo_path(rule["start_with"]).exists()


def test_sales_agent_contract_protects_negative_semantics():
    contract = load_yaml(CONTRACT_PATH)
    semantics = contract["negative_semantics"]

    assert "not reviewed" in semantics["process_mechanism_map"]
    assert "does not automatically mean" in semantics["scope_items"]
    assert "does not prove" in semantics["diagnostic_casebook"]
    assert any("absent relation" in item for item in contract["answer_policy"])
    assert any("evidence is missing" in item for item in contract["answer_policy"])


def test_sales_agent_index_is_registered_in_manifest():
    manifest = load_yaml(MANIFEST_PATH)
    endpoint = manifest["machine_endpoints"]["sales_agent_index"]

    assert endpoint == "/labs/enterprise-context/data/sales-agent-index.json"
    assert ENDPOINT_PATH.exists()

    body = ENDPOINT_PATH.read_text(encoding="utf-8")
    assert "site.data.labs.enterprise_context.agent_contracts.sales" in body
    assert '"process_mechanism_coverage"' in body
    assert '"diagnostic_casebook_meta"' in body
