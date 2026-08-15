from pathlib import Path

import yaml


ROOT = Path("labs/enterprise-context")
CONTRACT = Path("_data/labs/enterprise_context/agent_contracts/sales.yml")


HUMAN_VIEWS = {
    ROOT / "sales-processes" / "index.html": "/labs/enterprise-context/sales-processes/",
    ROOT / "sales-diagnostics" / "index.html": "/labs/enterprise-context/sales-diagnostics/",
    ROOT / "sales-analytics" / "index.html": "/labs/enterprise-context/sales-analytics/",
}


def test_sales_human_views_have_stable_routes():
    for path, route in HUMAN_VIEWS.items():
        assert path.exists(), f"Missing Sales human view: {path}"
        body = path.read_text(encoding="utf-8")
        assert f"permalink: {route}" in body


def test_sales_agent_router_exposes_analytics_endpoint():
    contract = yaml.safe_load(CONTRACT.read_text(encoding="utf-8"))
    endpoints = {item["primary_endpoint"] for item in contract["namespaces"]}

    assert "/labs/enterprise-context/data/sales-process-atlas.json" in endpoints
    assert "/labs/enterprise-context/data/sales-diagnostic-casebook.json" in endpoints
    assert "/labs/enterprise-context/data/sales-process-kpis.json" in endpoints
