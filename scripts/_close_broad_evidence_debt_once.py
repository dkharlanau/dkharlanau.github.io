#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs/assessment/data"


def claim(cid, route, text, refs, urls, product, release, claim_type="documented_behavior"):
    return {
        "id": cid,
        "route": route,
        "claim": text,
        "claim_type": claim_type,
        "evidence_class": "sap_product_primary",
        "status": "source_supported",
        "source_refs": refs,
        "official_evidence": urls,
        "product_scope": product,
        "release_scope": release,
        "reviewed_at": "2026-08-16",
        "human_verification_required": True,
    }


review_path = DATA / "factual-review.json"
review = json.loads(review_path.read_text(encoding="utf-8"))
new_routes = [
    ("/labs/enterprise-context/sales-processes/", "Sales Process Atlas", ["FACT-SPROC-001", "FACT-SPROC-002"]),
    ("/labs/enterprise-context/sales-processes/integrations/", "Sales Process Integrations", ["FACT-SPINT-001", "FACT-SPINT-002"]),
    ("/labs/enterprise-context/transportation-management/integrations/", "TM Integrations", ["FACT-TMINT-001", "FACT-TMINT-002"]),
    ("/labs/enterprise-context/logistics-capabilities/", "Cross-Process Logistics Capabilities", ["FACT-LOGCAP-001", "FACT-LOGCAP-002"]),
    ("/labs/enterprise-context/data-governance/", "Data Governance", ["FACT-DG-001", "FACT-DG-002"]),
]
new_claims = [
    claim(
        "FACT-SPROC-001",
        "/labs/enterprise-context/sales-processes/",
        "A standard sell-from-stock flow connects sales order, outbound delivery, picking and goods issue, and delivery-related billing. Billing transfers accounting-relevant data into Financial Accounting, so commercial, physical, and financial completion are separate checkpoints in one end-to-end process.",
        ["SRC-SAP-ASSESS-SELL-FROM-STOCK"],
        ["https://help.sap.com/docs/SAP_S4HANA_CLOUD/89d896ca9cd64318b1667df5ec00e4b2/60e3856c92004daf8a71f5017fd2b9a8.html"],
        "SAP S/4HANA Cloud Public Edition Sales",
        "2608 Latest",
    ),
    claim(
        "FACT-SPROC-002",
        "/labs/enterprise-context/sales-processes/",
        "In the sales-order outbound-delivery scenario, the sales order item is the root for subsequent logistics process steps. Outbound delivery, picking, packing, goods issue, and billing expose different process statuses; posting goods issue is the final delivery-processing step and delivery-related billing uses the delivery as its main reference.",
        ["SRC-SAP-ASSESS-SALES-PROCESS-FLOW"],
        ["https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/25a41481f62e469ba0e61015a0d39d20/610fb16c6f8341e0a0725eeb3abb00ed.html"],
        "SAP S/4HANA Logistics / Sales",
        "2025 FPS01",
    ),
    claim(
        "FACT-SPINT-001",
        "/labs/enterprise-context/sales-processes/integrations/",
        "The Sales Order A2X OData V2 API is a synchronous inbound service for external applications and supports creating, reading, updating, and deleting sales orders. An API endpoint is therefore a command/query contract, not the same thing as asynchronous business-event publication.",
        ["SRC-SAP-ASSESS-SALES-ORDER-API"],
        ["https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/19d48293097f4a2589433856b034dfa5/00d244581efca007e10000000a441470.html"],
        "SAP S/4HANA APIs for Sales",
        "2025 FPS01",
    ),
    claim(
        "FACT-SPINT-002",
        "/labs/enterprise-context/sales-processes/integrations/",
        "The Sales Order business object publishes events for creation, change, deletion, and overall-processing-status change. These events carry business identifiers and status context, so event-driven consumers should use the event as a notification contract rather than assume it contains the full mutable sales-order state.",
        ["SRC-SAP-ASSESS-SALES-ORDER-EVENTS"],
        ["https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/19d48293097f4a2589433856b034dfa5/78168e21723f4d58a631e3790a7f96b4.html"],
        "SAP S/4HANA APIs for Sales",
        "2025 FPS01",
    ),
    claim(
        "FACT-TMINT-001",
        "/labs/enterprise-context/transportation-management/integrations/",
        "In an external-planning scenario, transportation requirements can be sent as freight units or consignment orders and planning results returned as freight orders or freight bookings. SAP documents TransportationOrderGenericRequest_Out and _In as the communication APIs for this exchange.",
        ["SRC-SAP-ASSESS-TM-EXTERNAL-PLANNING"],
        ["https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/6e825c862de14cec93e7a3ca5c3d3a17.html"],
        "SAP S/4HANA Transportation Management",
        "2025 FPS01",
    ),
    claim(
        "FACT-TMINT-002",
        "/labs/enterprise-context/transportation-management/integrations/",
        "The Freight Order A2X API can create, update, and cancel freight orders and can assign or unassign freight units, report events, and calculate charges. SAP also warns not to use this API to update freight orders during the planning and subcontracting phase of SAP_COM_0414 because later external-planning replication can overwrite those updates.",
        ["SRC-SAP-ASSESS-TM-FREIGHT-ORDER-API"],
        ["https://help.sap.com/docs/SAP_S4HANA_CLOUD/588780cab2774a7ab9fffca3a7f919fe/4ca2bf7c61f541e290f948cfd9b785e5.html"],
        "SAP S/4HANA Cloud Transportation Management",
        "Current documentation checked 2026-08-16",
    ),
    claim(
        "FACT-LOGCAP-001",
        "/labs/enterprise-context/logistics-capabilities/",
        "Batch management preserves lot identity across logistics processes. SAP shows batch determination, availability and usability checks in Sales and batch assignment or determination in Production, so batch is a cross-process material identity rather than a warehouse-only attribute.",
        ["SRC-SAP-ASSESS-BATCH-MANAGEMENT"],
        ["https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/4eb099dbc8a6435c9b36a854a7e05522/c7feb753128eb44ce10000000a174cb4.html"],
        "SAP S/4HANA Logistics - Batch Management",
        "2025 FPS01",
    ),
    claim(
        "FACT-LOGCAP-002",
        "/labs/enterprise-context/logistics-capabilities/",
        "A handling unit is a uniquely identified packaging unit that carries the packed materials and can carry batch and serial-number information through the supply chain. Serial numbers identify individual material instances and can be assigned to HU items, so HU identity and serial identity solve different traceability problems even when they travel together.",
        ["SRC-SAP-ASSESS-HANDLING-UNIT", "SRC-SAP-ASSESS-SERIAL-HU"],
        [
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/1dad2180e6f34b75ac77afce5cb5eda1/5b2f169885e111db2b24000f20dac9ef.html",
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/25a41481f62e469ba0e61015a0d39d20/c328b753128eb44ce10000000a174cb4-233.html",
        ],
        "SAP S/4HANA Logistics - Handling Unit and Serial Number Management",
        "2025 FPS01 documentation checked 2026-08-16",
    ),
    claim(
        "FACT-DG-001",
        "/labs/enterprise-context/data-governance/",
        "SAP MDG Data Quality Management supports derivation rules, validation rules, data-quality KPIs, scheduled evaluations, monitoring, drilldown, and correction for product and business-partner master data. These are implementation mechanisms for governed data quality; they do not define the enterprise ownership model by themselves.",
        ["SRC-SAP-ASSESS-MDG-DQM"],
        ["https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/03f3f2e3d99a47b39fc106e52304e665.html"],
        "SAP Master Data Governance, Data Quality Management",
        "SAP S/4HANA 2025 FPS01",
    ),
    claim(
        "FACT-DG-002",
        "/labs/enterprise-context/data-governance/",
        "MDG validation rules are managed in a central rule repository and can be used for data-quality evaluations and checks in change requests, consolidation, and other MDG processes. The rule implementation can therefore support preventive and detective controls, while ownership and acceptance thresholds remain governance decisions.",
        ["SRC-SAP-ASSESS-MDG-VALIDATION-RULES"],
        ["https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/61e6c725c1bf4332aadbf1b9e040b9c5.html"],
        "SAP Master Data Governance",
        "SAP S/4HANA 2025 FPS01",
        "configuration_behavior",
    ),
]

routes = {item["route"]: item for item in review["routes"]}
for route, title, ids in new_routes:
    routes[route] = {"route": route, "title": title, "review_status": "primary_source_review_complete", "reviewed_at": "2026-08-16", "page_verified": False, "human_verification_required": True, "claim_ids": ids}
claims = {item["id"]: item for item in review["claims"]}
for item in new_claims:
    claims[item["id"]] = item
review["routes"] = [routes[key] for key in sorted(routes)]
review["claims"] = [claims[key] for key in sorted(claims)]
review["version"] = "1.6.0"
review["summary"] = {
    "routes_reviewed": len(review["routes"]),
    "claims_reviewed": len(review["claims"]),
    "source_supported": sum(1 for item in review["claims"] if item["status"] == "source_supported"),
    "source_conflict": sum(1 for item in review["claims"] if item["status"] == "source_conflict"),
    "human_verification_required": sum(1 for item in review["claims"] if item["human_verification_required"]),
}
review_path.write_text(json.dumps(review, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

profile_path = DATA / "evidence-profile.json"
profile = json.loads(profile_path.read_text(encoding="utf-8"))
profile["version"] = "1.1.0"
profile["route_overrides"]["/labs/enterprise-context/sales-diagnostics/"] = {
    "expected_evidence_classes": ["sap_product_primary", "author_heuristic"],
    "external_review_mode": "selective_for_named_product_claims",
    "counts_as_source_review_debt": False,
    "reason": "The page is explicitly an authored diagnostic casebook. SAP sources anchor product behavior and release-sensitive limits; hypothesis trees and diagnostic habits are author guidance rather than product facts."
}
profile_path.write_text(json.dumps(profile, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

page_path = ROOT / "labs/assessment/factual-review/index.html"
text = page_path.read_text(encoding="utf-8")
text = text.replace('id="fact-routes">21</strong>', 'id="fact-routes">26</strong>', 1)
text = text.replace('id="fact-claims">53</strong>', 'id="fact-claims">63</strong>', 1)
text = text.replace('id="fact-supported">53</strong>', 'id="fact-supported">63</strong>', 1)
text = text.replace(
    "The review now covers twenty-one SAP routes and fifty-three product-primary claims. The latest batch closes major Sales, Procurement, Shipping, and MDG replication evidence debt.",
    "The broad evidence pass now covers twenty-six SAP routes and sixty-three product-primary claims. Required assessment routes have claim-level source support; authored or mixed routes keep their evidence-class boundaries explicit.",
    1,
)
anchor = '      <a href="/labs/enterprise-context/mdg/interfaces/"><span>2</span><strong>MDG Interfaces</strong><small>DRF replication and governance-to-distribution boundaries reviewed against SAP primary sources.</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a>'
extra = '''
      <a href="/labs/enterprise-context/sales-processes/"><span>2</span><strong>Sales Process Atlas</strong><small>Sell-from-stock and sales-order-to-delivery process boundaries reviewed against SAP primary sources.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="/labs/enterprise-context/sales-processes/integrations/"><span>2</span><strong>Sales Process Integrations</strong><small>Sales Order A2X and business-event contracts reviewed against SAP S/4HANA 2025 FPS01.</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a>
      <a href="/labs/enterprise-context/transportation-management/integrations/"><span>2</span><strong>TM Integrations</strong><small>External planning and Freight Order API ownership boundaries reviewed against SAP primary sources.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="/labs/enterprise-context/logistics-capabilities/"><span>2</span><strong>Logistics Capabilities</strong><small>Batch, handling-unit, and serial identity boundaries reviewed against SAP S/4HANA 2025 FPS01.</small><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a>
      <a href="/labs/enterprise-context/data-governance/"><span>2</span><strong>Data Governance</strong><small>MDG data-quality and validation-rule mechanisms reviewed while governance ownership remains explicit author guidance.</small><i class="material-symbols-outlined" aria-hidden="true">policy</i></a>'''
if extra.strip() not in text:
    if anchor not in text:
        raise SystemExit("Factual review page anchor not found")
    text = text.replace(anchor, anchor + extra, 1)
text = text.replace("Fifty-three reviewed claims across twenty-one SAP product routes.", "Sixty-three reviewed claims across twenty-six SAP product routes.", 1)
page_path.write_text(text, encoding="utf-8")

catalog_path = DATA / "catalog.json"
catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
catalog["version"] = "2.4.0"
marker = "Broad required evidence coverage is complete; authored diagnostics and generic AI frameworks use selective evidence profiles instead of forced SAP-product verification"
if marker not in catalog["coverage"]["strong_now"]:
    catalog["coverage"]["strong_now"].append(marker)
catalog["coverage"]["next_practice_layers"] = [
    "move from broad evidence debt to page-level human review of source-supported P1 routes",
    "add standards or primary-research evidence only where selective AI and governance routes make externally checkable claims",
    "connect real assessment feedback to practice and review priority without changing factual truth",
    "use evidence-class coverage as a gate for generated questions and any future publication recommendation",
]
catalog_path.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

backlog_path = DATA / "backlog.json"
backlog = json.loads(backlog_path.read_text(encoding="utf-8"))
items = {item["id"]: item for item in backlog["items"]}
items["LOOP-025"] = {
    "id": "LOOP-025",
    "priority": "P1",
    "title": "Close broad required evidence debt",
    "status": "done",
    "outputs": [
        "/labs/assessment/data/factual-review.json",
        "/labs/assessment/data/evidence-profile.json",
        "/labs/assessment/data/evidence-coverage.json",
        "_data/labs/enterprise_context/sources/assessment_review_loop025.yml"
    ],
    "reviewed_routes": [route for route, _, _ in new_routes],
    "profiled_routes": ["/labs/enterprise-context/sales-diagnostics/"],
    "working_rule": "Complete source review where product evidence is a required gate, and explicitly classify authored diagnostic reasoning instead of forcing it into a product-fact model."
}
backlog["items"] = [items[key] for key in sorted(items)]
backlog["next_iteration_themes"] = [
    "start page-level human review on source-supported P1 routes without auto-publishing",
    "prioritize human review by assessment importance, release sensitivity, and feedback signals",
    "add standards or original research to selective routes only when an external claim actually needs it",
    "use evidence-class completeness as a quality gate for question generation and publication recommendations",
]
backlog_path.write_text(json.dumps(backlog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

assessment_path = ROOT / "labs/assessment/index.md"
assessment = assessment_path.read_text(encoding="utf-8")
assessment = assessment.replace(
    '<a href="/labs/assessment/data/factual-review.json"><span>53</span><strong>Factual Review Registry</strong><small>Fifty-three source-supported product claims across twenty-one SAP routes; page verification remains unchanged.</small>',
    '<a href="/labs/assessment/data/factual-review.json"><span>63</span><strong>Factual Review Registry</strong><small>Sixty-three source-supported product claims across twenty-six SAP routes; page verification remains unchanged.</small>',
    1,
)
assessment = assessment.replace(
    "LOOP-001 through LOOP-024 are complete; core Sales, Procurement, Shipping, and MDG interface decisions now have primary-source coverage.",
    "LOOP-001 through LOOP-025 are complete; broad required evidence debt is closed and the next gate is page-level human review.",
    1,
)
assessment_path.write_text(assessment, encoding="utf-8")

tests_path = ROOT / "tests/test_assessment_practice_layer.py"
tests = tests_path.read_text(encoding="utf-8")
tests = tests.replace(
    '("LOOP-010", "LOOP-011", "LOOP-012", "LOOP-013", "LOOP-014", "LOOP-015", "LOOP-016", "LOOP-017", "LOOP-018", "LOOP-019", "LOOP-020", "LOOP-021", "LOOP-022", "LOOP-023", "LOOP-024")',
    '("LOOP-010", "LOOP-011", "LOOP-012", "LOOP-013", "LOOP-014", "LOOP-015", "LOOP-016", "LOOP-017", "LOOP-018", "LOOP-019", "LOOP-020", "LOOP-021", "LOOP-022", "LOOP-023", "LOOP-024", "LOOP-025")',
    1,
)
tests = tests.replace('assert review["summary"]["routes_reviewed"] == 21', 'assert review["summary"]["routes_reviewed"] == 26', 1)
tests = tests.replace('assert review["summary"]["claims_reviewed"] == 53', 'assert review["summary"]["claims_reviewed"] == 63', 1)
tests = tests.replace('assert inventory["factual_review_counts"]["source_supported"] == len(reviewed_routes) == 21', 'assert inventory["factual_review_counts"]["source_supported"] == len(reviewed_routes) == 26', 1)
tests = tests.replace('assert coverage["summary"]["unique_source_reviewed_routes"] >= 21', 'assert coverage["summary"]["unique_source_reviewed_routes"] == coverage["summary"]["unique_externally_review_required_routes"] == 26', 1)
tests = tests.replace('assert coverage["summary"]["source_supported_claims"] >= 53', 'assert coverage["summary"]["source_supported_claims"] >= 63', 1)
tests = tests.replace('assert coverage["summary"]["unique_selective_or_heuristic_routes"] >= 2', 'assert coverage["summary"]["unique_selective_or_heuristic_routes"] >= 3', 1)
completion_test = '''

def test_broad_required_evidence_debt_is_closed_without_forcing_authored_diagnostics() -> None:
    coverage = load_json("evidence-coverage.json")
    profile = load_json("evidence-profile.json")
    readiness = load_json("promotion-readiness.json")
    by_route = {item["route"]: item for item in readiness["items"]}

    assert coverage["summary"]["coverage_percent"] == 100.0
    assert coverage["summary"]["unique_p0_evidence_debt_routes"] == 0
    assert coverage["next_focus"] == []
    assert profile["route_overrides"]["/labs/enterprise-context/sales-diagnostics/"]["counts_as_source_review_debt"] is False
    assert by_route["/labs/enterprise-context/sales-diagnostics/"]["priority"] == "P2"
    assert by_route["/labs/enterprise-context/data-governance/"]["factual_review"]["status"] == "source_supported"
'''
if "test_broad_required_evidence_debt_is_closed_without_forcing_authored_diagnostics" not in tests:
    tests = tests.rstrip() + completion_test + "\n"
tests_path.write_text(tests, encoding="utf-8")

print(f"Broad required evidence debt closed at {review['summary']['routes_reviewed']} reviewed routes and {review['summary']['claims_reviewed']} claims.")
