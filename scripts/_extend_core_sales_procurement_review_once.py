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
    ("/labs/enterprise-context/pricing/", "Sales Pricing", ["FACT-PRC-001", "FACT-PRC-002"]),
    ("/labs/enterprise-context/sales-order/", "Sales Order Decisions", ["FACT-SO-001", "FACT-SO-002"]),
    ("/labs/enterprise-context/shipping/", "Shipping and Scheduling", ["FACT-SHP-001", "FACT-SHP-002"]),
    ("/labs/enterprise-context/procurement/", "Procurement", ["FACT-PROC-001", "FACT-PROC-002"]),
    ("/labs/enterprise-context/mdg/interfaces/", "MDG Interfaces", ["FACT-MDGI-001", "FACT-MDGI-002"]),
]

new_claims = [
    claim(
        "FACT-PRC-001",
        "/labs/enterprise-context/pricing/",
        "SAP pricing uses the condition technique. A condition type can have an access sequence that searches condition tables in a defined order until a valid condition record is found; the pricing procedure then arranges the relevant condition types and calculation steps.",
        ["SRC-SAP-PRC-CONDITION-TECHNIQUE", "SRC-SAP-PRC-ACCESS-SEQUENCES", "SRC-SAP-PRC-PRICING-PROCEDURE"],
        [
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/c9b5e9de6e674fb99fff88d72c352291/d69fbe532789b44ce10000000a174cb4.html",
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/c9b5e9de6e674fb99fff88d72c352291/a2a1c1535fe6b74ce10000000a174cb4.html",
        ],
        "SAP S/4HANA Sales Pricing",
        "SAP S/4HANA 2025 FPS01",
        "configuration_behavior",
    ),
    claim(
        "FACT-PRC-002",
        "/labs/enterprise-context/pricing/",
        "Pricing procedure determination combines sales-area context with document and customer pricing indicators. Therefore a wrong procedure can be caused upstream by determination inputs even when the individual condition records themselves are correct.",
        ["SRC-SAP-PRC-PRICING-PROCEDURE", "SRC-SAP-SD-PRICING-PROCEDURE"],
        [
            "https://help.sap.com/docs/s4hana-best-practices/setting-up-sell-from-stock-bd9-e9718dcb7c964bb736ee48ffe4a2c207/set-pricing-procedure-determination",
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/c9b5e9de6e674fb99fff88d72c352291/d69fbe532789b44ce10000000a174cb4.html",
        ],
        "SAP S/4HANA Sales Pricing",
        "SAP S/4HANA 2025 / best-practice configuration checked 2026-08-16",
        "configuration_behavior",
    ),
    claim(
        "FACT-SO-001",
        "/labs/enterprise-context/sales-order/",
        "Sales document item category determination uses document and material context, including the sales document type and the material's item-category group, with additional controls such as usage or a higher-level item category where configured. The resulting item category controls important item behavior.",
        ["SRC-SAP-SD-ITEM-CATEGORY-DETERMINATION", "SRC-SAP-SD-DOCUMENT-CONTROL"],
        [
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/dc89c95360267214e10000000a174cb4.html",
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/c264b65334e6b54ce10000000a174cb4.html",
        ],
        "SAP S/4HANA Sales",
        "SAP S/4HANA 2025 FPS01",
        "configuration_behavior",
    ),
    claim(
        "FACT-SO-002",
        "/labs/enterprise-context/sales-order/",
        "Schedule line categories control delivery-relevant and requirements-related behavior at schedule-line level. Standard determination uses the sales item category together with MRP-related material context, so a schedule-line problem should be traced through item-category and material-planning inputs before changing the final order line.",
        ["SRC-SAP-SD-SCHEDULE-LINE-CATEGORY"],
        ["https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7340a09096454b7abf4379f926a21567/cb64b65334e6b54ce10000000a174cb4.html"],
        "SAP S/4HANA Sales",
        "SAP S/4HANA 2025 FPS01",
        "configuration_behavior",
    ),
    claim(
        "FACT-SHP-001",
        "/labs/enterprise-context/shipping/",
        "Shipping-point determination uses shipping condition, loading group, and delivering plant as key inputs. The shipping point is an organizational execution unit for deliveries and shipping activities, so an unexpected shipping point should be diagnosed from those inputs before changing the delivery.",
        ["SRC-SAP-SHP-POINTS", "SRC-SAP-SHP-LOADING-GROUP", "SRC-SAP-SD-DELIVERING-PLANT"],
        [
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/c7894a248ca14f74aca67f97528e5ad7/5d1bbf53d25ab64ce10000000a174cb4.html",
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/c7894a248ca14f74aca67f97528e5ad7/8fd7e5ec3c984728aadc19f6b9364988.html",
        ],
        "SAP S/4HANA Delivery Management",
        "SAP S/4HANA 2025 FPS01",
        "configuration_behavior",
    ),
    claim(
        "FACT-SHP-002",
        "/labs/enterprise-context/shipping/",
        "Classic route determination evaluates transportation-relevant origin, destination, shipping-condition, and material transportation-group context. Route and scheduling are related but separate decisions: the route can supply transit and transportation-lead-time data used by transportation and delivery scheduling.",
        ["SRC-SAP-SHP-ROUTE", "SRC-SAP-SHP-SCHEDULING"],
        [
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/c7894a248ca14f74aca67f97528e5ad7/601bbf53d25ab64ce10000000a174cb4.html",
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/9dbdba53422bb54ce10000000a174cb4.html",
        ],
        "SAP S/4HANA Sales and Delivery Management",
        "SAP S/4HANA 2025 FPS01",
        "configuration_behavior",
    ),
    claim(
        "FACT-PROC-001",
        "/labs/enterprise-context/procurement/",
        "Automatic source determination can evaluate maintained sources and source-control objects such as purchasing info records, outline agreements, source lists, and quota arrangements. A selected supplier is therefore the result of source-of-supply logic and master data, not merely the vendor entered on the final purchase order.",
        ["SRC-SAP-MM-SOURCE-DETERMINATION", "SRC-SAP-MM-SOURCE-LIST", "SRC-SAP-MM-QUOTA"],
        [
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/20e8b65334e6b54ce10000000a174cb4.html",
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/35e8b65334e6b54ce10000000a174cb4.html",
        ],
        "SAP S/4HANA Sourcing and Procurement",
        "SAP S/4HANA 2025 FPS01",
        "configuration_behavior",
    ),
    claim(
        "FACT-PROC-002",
        "/labs/enterprise-context/procurement/",
        "Purchase-order item category and account-assignment category solve different control problems. Item category shapes the procurement scenario and item processing, while account assignment determines which cost object or account receives the value when the purchase is not simply posted to valuated stock.",
        ["SRC-SAP-MM-PO-ITEM-CATEGORIES", "SRC-SAP-MM-ACCOUNT-ASSIGNMENT"],
        [
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/45e8b65334e6b54ce10000000a174cb4.html",
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/5ae8b65334e6b54ce10000000a174cb4.html",
        ],
        "SAP S/4HANA Sourcing and Procurement",
        "SAP S/4HANA 2025 FPS01",
        "configuration_behavior",
    ),
    claim(
        "FACT-MDGI-001",
        "/labs/enterprise-context/mdg/interfaces/",
        "The Data Replication Framework is used to define and execute replication from SAP S/4HANA or MDG to connected target systems. Replication models combine target systems with outbound implementations and can use filters, so successful governance and successful downstream distribution are separate responsibilities.",
        ["SRC-SAP-MDG-DRF"],
        ["https://help.sap.com/docs/sap_s4hana-on-premise/6d52de87aa0d4fb6a90924720a5b0549/0607694edd87437996a93e99d7ed3e28.html"],
        "SAP Master Data Governance / Data Replication Framework",
        "SAP S/4HANA 2025 FPS01 documentation checked 2026-08-16",
        "configuration_behavior",
    ),
    claim(
        "FACT-MDGI-002",
        "/labs/enterprise-context/mdg/interfaces/",
        "MDG separates governed staging and activation from replication to consuming systems. The data model and replication design therefore need an explicit active-data and downstream-distribution boundary; a completed change process alone does not prove that every target system can use the mastered object.",
        ["SRC-SAP-MDG-DATA-MODEL", "SRC-SAP-MDG-DRF"],
        [
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/22d76454004f2357e10000000a44176d.html",
            "https://help.sap.com/docs/sap_s4hana-on-premise/6d52de87aa0d4fb6a90924720a5b0549/0607694edd87437996a93e99d7ed3e28.html",
        ],
        "SAP Master Data Governance",
        "SAP S/4HANA 2025 FPS01 documentation checked 2026-08-16",
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
review["version"] = "1.5.0"
review["summary"] = {
    "routes_reviewed": len(review["routes"]),
    "claims_reviewed": len(review["claims"]),
    "source_supported": sum(1 for item in review["claims"] if item["status"] == "source_supported"),
    "source_conflict": sum(1 for item in review["claims"] if item["status"] == "source_conflict"),
    "human_verification_required": sum(1 for item in review["claims"] if item["human_verification_required"]),
}
review_path.write_text(json.dumps(review, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

page_path = ROOT / "labs/assessment/factual-review/index.html"
text = page_path.read_text(encoding="utf-8")
text = text.replace('id="fact-routes">16</strong>', 'id="fact-routes">21</strong>', 1)
text = text.replace('id="fact-claims">43</strong>', 'id="fact-claims">53</strong>', 1)
text = text.replace('id="fact-supported">43</strong>', 'id="fact-supported">53</strong>', 1)
text = text.replace(
    "The review now covers sixteen SAP routes, including the first AI/Data and development architecture batch. The focus stays on product facts that change design, ownership, recovery, or release decisions.",
    "The review now covers twenty-one SAP routes and fifty-three product-primary claims. The latest batch closes major Sales, Procurement, Shipping, and MDG replication evidence debt.",
    1,
)
anchor = '      <a href="/labs/enterprise-context/development/"><span>2</span><strong>SAP Development Architecture</strong><small>Public Edition 2608 developer extensibility and RAP managed/unmanaged behavior checked against current SAP Help.</small><i class="material-symbols-outlined" aria-hidden="true">code</i></a>'
extra = '''
      <a href="/labs/enterprise-context/pricing/"><span>2</span><strong>Sales Pricing</strong><small>Condition technique and pricing-procedure determination reviewed against SAP primary sources.</small><i class="material-symbols-outlined" aria-hidden="true">price_check</i></a>
      <a href="/labs/enterprise-context/sales-order/"><span>2</span><strong>Sales Order Decisions</strong><small>Item-category and schedule-line determination boundaries reviewed against SAP S/4HANA 2025 FPS01.</small><i class="material-symbols-outlined" aria-hidden="true">description</i></a>
      <a href="/labs/enterprise-context/shipping/"><span>2</span><strong>Shipping & Scheduling</strong><small>Shipping-point and route/scheduling determination inputs reviewed against SAP S/4HANA 2025 FPS01.</small><i class="material-symbols-outlined" aria-hidden="true">local_shipping</i></a>
      <a href="/labs/enterprise-context/procurement/"><span>2</span><strong>Procurement</strong><small>Source determination and PO item/account-assignment control reviewed against SAP S/4HANA 2025 FPS01.</small><i class="material-symbols-outlined" aria-hidden="true">shopping_cart</i></a>
      <a href="/labs/enterprise-context/mdg/interfaces/"><span>2</span><strong>MDG Interfaces</strong><small>DRF replication and governance-to-distribution boundaries reviewed against SAP primary sources.</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a>'''
if extra.strip() not in text:
    if anchor not in text:
        raise SystemExit("Factual review page anchor not found")
    text = text.replace(anchor, anchor + extra, 1)
text = text.replace("Forty-three reviewed claims across sixteen SAP product routes.", "Fifty-three reviewed claims across twenty-one SAP product routes.", 1)
page_path.write_text(text, encoding="utf-8")

catalog_path = DATA / "catalog.json"
catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
catalog["version"] = "2.3.0"
marker = "Product-primary review now covers Pricing, Sales Order, Shipping, Procurement, and MDG replication boundaries"
if marker not in catalog["coverage"]["strong_now"]:
    catalog["coverage"]["strong_now"].append(marker)
catalog["coverage"]["next_practice_layers"] = [
    "review the remaining profile-aware P0 routes from evidence-coverage.json, including Sales Processes, Sales Diagnostics, Logistics Capabilities, Data Governance, and integration subroutes",
    "add evidence-class coverage summaries by assessment track",
    "connect assessment feedback to practice priority while factual truth stays source-based",
    "use evidence coverage as a gate for question generation and page promotion",
]
catalog_path.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

backlog_path = DATA / "backlog.json"
backlog = json.loads(backlog_path.read_text(encoding="utf-8"))
items = {item["id"]: item for item in backlog["items"]}
items["LOOP-024"] = {
    "id": "LOOP-024",
    "priority": "P1",
    "title": "Core Sales, Procurement, Shipping, and MDG interface factual review",
    "status": "done",
    "outputs": ["/labs/assessment/factual-review/", "/labs/assessment/data/factual-review.json", "/labs/assessment/data/evidence-coverage.json"],
    "reviewed_routes": [route for route, _, _ in new_routes],
    "working_rule": "Close high-value P0 evidence debt on determination and replication decisions before adding more breadth.",
}
backlog["items"] = [items[key] for key in sorted(items)]
backlog["next_iteration_themes"] = [
    "continue the remaining P0 routes from the profile-aware evidence matrix",
    "add evidence-class coverage summaries by assessment track",
    "connect real feedback to practice priority without changing factual truth",
    "use evidence coverage as a gate for generated questions and publication review",
]
backlog_path.write_text(json.dumps(backlog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

assessment_path = ROOT / "labs/assessment/index.md"
assessment = assessment_path.read_text(encoding="utf-8")
assessment = assessment.replace(
    '<a href="/labs/assessment/data/factual-review.json"><span>43</span><strong>Factual Review Registry</strong><small>Forty-three source-supported product claims across sixteen SAP routes; page verification remains unchanged.</small>',
    '<a href="/labs/assessment/data/factual-review.json"><span>53</span><strong>Factual Review Registry</strong><small>Fifty-three source-supported product claims across twenty-one SAP routes; page verification remains unchanged.</small>',
    1,
)
assessment = assessment.replace(
    "LOOP-001 through LOOP-023 are complete; AI/Data and Integration product facts now have materially better source coverage.",
    "LOOP-001 through LOOP-024 are complete; core Sales, Procurement, Shipping, and MDG interface decisions now have primary-source coverage.",
    1,
)
assessment_path.write_text(assessment, encoding="utf-8")

tests_path = ROOT / "tests/test_assessment_practice_layer.py"
tests = tests_path.read_text(encoding="utf-8")
tests = tests.replace(
    '("LOOP-010", "LOOP-011", "LOOP-012", "LOOP-013", "LOOP-014", "LOOP-015", "LOOP-016", "LOOP-017", "LOOP-018", "LOOP-019", "LOOP-020", "LOOP-021", "LOOP-022", "LOOP-023")',
    '("LOOP-010", "LOOP-011", "LOOP-012", "LOOP-013", "LOOP-014", "LOOP-015", "LOOP-016", "LOOP-017", "LOOP-018", "LOOP-019", "LOOP-020", "LOOP-021", "LOOP-022", "LOOP-023", "LOOP-024")',
    1,
)
tests = tests.replace('assert review["summary"]["routes_reviewed"] == 16', 'assert review["summary"]["routes_reviewed"] == 21', 1)
tests = tests.replace('assert review["summary"]["claims_reviewed"] == 43', 'assert review["summary"]["claims_reviewed"] == 53', 1)
tests = tests.replace('assert inventory["factual_review_counts"]["source_supported"] == len(reviewed_routes) == 16', 'assert inventory["factual_review_counts"]["source_supported"] == len(reviewed_routes) == 21', 1)
tests = tests.replace('assert coverage["summary"]["unique_source_reviewed_routes"] >= 16', 'assert coverage["summary"]["unique_source_reviewed_routes"] >= 21', 1)
tests = tests.replace('assert coverage["summary"]["source_supported_claims"] >= 43', 'assert coverage["summary"]["source_supported_claims"] >= 53', 1)
tests_path.write_text(tests, encoding="utf-8")

print(f"Core factual review expanded to {review['summary']['routes_reviewed']} routes and {review['summary']['claims_reviewed']} claims.")
