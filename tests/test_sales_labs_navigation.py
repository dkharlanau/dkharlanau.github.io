from pathlib import Path


LABS_INDEX = Path("labs/index.md")


REQUIRED_SALES_ROUTES = {
    "/labs/enterprise-context/sales-processes/": "SAP Sales Process Atlas",
    "/labs/enterprise-context/sales-diagnostics/": "SAP Sales Diagnostic Casebook",
    "/labs/enterprise-context/data/sales-agent-index.json": "Sales Agent Routing Index",
}


def test_labs_index_exposes_sales_human_and_agent_routes():
    body = LABS_INDEX.read_text(encoding="utf-8")

    for route, label in REQUIRED_SALES_ROUTES.items():
        assert route in body, f"Missing Sales route on Labs index: {route}"
        assert label in body, f"Missing Sales route label on Labs index: {label}"
