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
    ("/labs/enterprise-context/production/", "Production Planning & Execution", ["FACT-PP-001", "FACT-PP-002"]),
    ("/labs/enterprise-context/quality-management/", "Quality Management", ["FACT-QM-001", "FACT-QM-002"]),
    ("/labs/enterprise-context/inventory-management/", "Inventory Management", ["FACT-IM-001", "FACT-IM-002"]),
    ("/labs/enterprise-context/finance-logistics/", "FI/CO Logistics Bridge", ["FACT-FIN-001", "FACT-FIN-002"]),
    ("/labs/enterprise-context/automotive-jit/", "Automotive JIT/JIS", ["FACT-AUTO-001", "FACT-AUTO-002"]),
    ("/labs/enterprise-context/transportation-management/", "Transportation Management", ["FACT-TM-001", "FACT-TM-002"]),
]

new_claims = [
    claim(
        "FACT-PP-001",
        "/labs/enterprise-context/production/",
        "A production version selects the alternative BOM together with the task list or master recipe and carries lot-size and validity restrictions. SAP uses production versions in planning and order creation to choose the suitable production technique.",
        ["SRC-SAP-PP-PRODUCTION-VERSION"],
        ["https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/bc6b9325fedd4344a84412b2195064fa/31c5bf53f106b44ce10000000a174cb4.html"],
        "SAP S/4HANA Production Planning",
        "SAP S/4HANA 2025 FPS01",
        "configuration_behavior",
    ),
    claim(
        "FACT-PP-002",
        "/labs/enterprise-context/production/",
        "Goods receipt for a manufacturing order posts the finished material to stock and reduces the expected receipt. The order is credited by the goods movement and the cost flow follows the order settlement rule, so physical completion and cost settlement are related but not the same checkpoint.",
        ["SRC-SAP-PP-GR", "SRC-SAP-PP-SETTLEMENT-RULE"],
        [
            "https://help.sap.com/docs/sap_s4hana_on-premise/f899ce30af9044299d573ea30b533f1c/b739c95360267614e10000000a174cb4.html",
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/34de0103497c4b80a7c7fbf6952ff971/5804b753128eb44ce10000000a174cb4.html",
        ],
        "SAP S/4HANA Production Orders and PP/DS integration",
        "SAP S/4HANA 2025 FPS01",
    ),
    claim(
        "FACT-QM-001",
        "/labs/enterprise-context/quality-management/",
        "The usage decision confirms completion of the inspection lot and records whether the inspected goods are accepted or rejected. It can also trigger follow-up actions, so it is a quality disposition decision rather than only a comment on results.",
        ["SRC-SAP-QM-USAGE-DECISION", "SRC-SAP-QM-LOT-COMPLETION"],
        [
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/2bc3ee8d1c83404e8cf62418640004f2/8d83b6535fe6b74ce10000000a174cb4.html",
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/2bc3ee8d1c83404e8cf62418640004f2/c164ba53422bb54ce10000000a174cb4.html",
        ],
        "SAP S/4HANA Quality Management",
        "SAP S/4HANA 2025 FPS01",
    ),
    claim(
        "FACT-QM-002",
        "/labs/enterprise-context/quality-management/",
        "For a stock-relevant inspection lot, stock can be posted during usage-decision processing and SAP creates the corresponding material-document postings. A non-stock-relevant lot cannot use the usage-decision stock-posting functions.",
        ["SRC-SAP-QM-LOT-COMPLETION", "SRC-SAP-QM-GR"],
        ["https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/2bc3ee8d1c83404e8cf62418640004f2/06edba53422bb54ce10000000a174cb4.html"],
        "SAP S/4HANA Quality Management and Inventory Management",
        "SAP S/4HANA 2025 FPS01",
    ),
    claim(
        "FACT-IM-001",
        "/labs/enterprise-context/inventory-management/",
        "A movement type defines the business purpose of a goods movement and controls important Inventory Management behavior such as quantity updates, stock and material valuation, consumption accounts, input fields, and some subsequent documents.",
        ["SRC-SAP-IM-MOVEMENT-TYPE"],
        ["https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/91b21005dded4984bcccf4a69ae1300c/1663bd534f22b44ce10000000a174cb4.html"],
        "SAP S/4HANA Inventory Management",
        "SAP S/4HANA 2025 FPS01",
        "configuration_behavior",
    ),
    claim(
        "FACT-IM-002",
        "/labs/enterprise-context/inventory-management/",
        "Physical inventory separates the count from the posting of differences. SAP supports posting differences after a recorded count or entering the count and posting the difference in one step, so a completed count alone does not prove that book stock was corrected.",
        ["SRC-SAP-IM-PHYSICAL-INVENTORY", "SRC-SAP-IM-INVENTORY-DIFFERENCE"],
        ["https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/91b21005dded4984bcccf4a69ae1300c/5161bd534f22b44ce10000000a174cb4.html"],
        "SAP S/4HANA Inventory Management and Physical Inventory",
        "SAP S/4HANA 2025 FPS01",
    ),
    claim(
        "FACT-FIN-001",
        "/labs/enterprise-context/finance-logistics/",
        "Goods receipt and invoice receipt for valuated procurement are linked through the GR/IR clearing account. The invoice posting clears the GR/IR amount against the vendor-side posting, so operational receipt and financial invoice completion are separate events that must reconcile.",
        ["SRC-SAP-FINLOG-GR-IR-POSTINGS", "SRC-SAP-FINLOG-PO-INVOICE"],
        ["https://help.sap.com/docs/SAP_S4HANA_ON-PREMI-SE/af9ef57f504840d2b81be8667206d485/825eb6531de6b64ce10000000a174cb4.html"],
        "SAP S/4HANA Sourcing and Procurement / Financial Accounting",
        "SAP S/4HANA 2025 FPS01",
    ),
    claim(
        "FACT-FIN-002",
        "/labs/enterprise-context/finance-logistics/",
        "Production-order settlement transfers actual order costs to one or more receiver cost objects according to the settlement rule. A settlement rule contains distribution rules that define receiver, share, and settlement type, so production completion does not by itself prove that controlling settlement is complete.",
        ["SRC-SAP-FINLOG-PRODUCTION-SETTLEMENT"],
        [
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/34de0103497c4b80a7c7fbf6952ff971/4904b753128eb44ce10000000a174cb4.html",
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/34de0103497c4b80a7c7fbf6952ff971/5804b753128eb44ce10000000a174cb4.html",
        ],
        "SAP S/4HANA Product Cost by Order",
        "SAP S/4HANA 2025 FPS01",
    ),
    claim(
        "FACT-AUTO-001",
        "/labs/enterprise-context/automotive-jit/",
        "In SAP S/4HANA 2025 FPS01, Next Generation JIT Supply to Customer supports end-to-end integration of sequenced JIS calls from the sales scheduling agreement through invoice, including EWM and TM integration.",
        ["SRC-SAP-AUTO-NG-E2E-JIS"],
        ["https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f5d3e1005efd4e86acf9a65abf428082/0fea9edeb6944f98aa8f368a2484009f.html?version=2025.001"],
        "SAP S/4HANA Next Generation Just-In-Time Supply to Customer",
        "SAP S/4HANA 2025 FPS01",
        "release_scope",
    ),
    claim(
        "FACT-AUTO-002",
        "/labs/enterprise-context/automotive-jit/",
        "In the nJIT supply-to-customer outbound process, an outbound delivery can be created from the S2C call. TM then creates freight units from that outbound delivery and transportation can continue with warehouse-driven or transport-driven execution.",
        ["SRC-SAP-AUTO-NG-DELIVERY", "SRC-SAP-AUTO-JIT-OUTBOUND"],
        [
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/1495ac28b1e249bfbd363b54435f4b04.html",
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/e2511f70a55f46cd997a9b0eff7d556d.html",
        ],
        "SAP S/4HANA nJIT, Logistics Execution, TM and EWM integration",
        "SAP S/4HANA 2025 FPS01",
    ),
    claim(
        "FACT-TM-001",
        "/labs/enterprise-context/transportation-management/",
        "TM creates freight units from transportation-demand documents such as order-based or delivery-based transportation requirements, orders, deliveries, and JIT calls. Freight orders are a result of transportation planning and become capacity and execution documents used for later carrier-related processing.",
        ["SRC-SAP-TM-FREIGHT-UNIT", "SRC-SAP-TM-FREIGHT-ORDER-MGMT"],
        [
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/2e86e6dc652b4f4aa4ac39c2d88595ca.html",
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/733c8b37b3f546a1b08750e8aeabb887/ff8bbbea9bd0421b9f833793d8d52b3d.html",
        ],
        "SAP S/4HANA Transportation Management",
        "SAP S/4HANA 2025 FPS01",
    ),
    claim(
        "FACT-TM-002",
        "/labs/enterprise-context/transportation-management/",
        "A freight settlement document represents freight-document costs from TM to MM. Posting it can create the service purchase order and service entry sheet that form the basis for carrier invoice verification, so freight execution and financial settlement are distinct completion layers.",
        ["SRC-SAP-TM-FREIGHT-SETTLEMENT", "SRC-SAP-TM-FSD"],
        [
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/7eb8bdf270d84b16ab8a755d09b11e81.html",
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/2f90ba3c7a8540e59f5ca0959d82e994.html",
        ],
        "SAP S/4HANA Transportation Management and Materials Management",
        "SAP S/4HANA 2025 FPS01",
    ),
]

routes = {item["route"]: item for item in review["routes"]}
for route, title, ids in new_routes:
    routes[route] = {
        "route": route,
        "title": title,
        "review_status": "primary_source_review_complete",
        "reviewed_at": "2026-08-16",
        "page_verified": False,
        "human_verification_required": True,
        "claim_ids": ids,
    }
claims = {item["id"]: item for item in review["claims"]}
for item in new_claims:
    claims[item["id"]] = item
review["routes"] = [routes[key] for key in sorted(routes)]
review["claims"] = [claims[key] for key in sorted(claims)]
review["version"] = "1.2.0"
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
text = text.replace('id="fact-routes">6</strong>', 'id="fact-routes">12</strong>', 1)
text = text.replace('id="fact-claims">23</strong>', 'id="fact-claims">35</strong>', 1)
text = text.replace('id="fact-supported">23</strong>', 'id="fact-supported">35</strong>', 1)
text = text.replace(
    "The first two batches cover integration recovery, billing, ATP, credit, warehouse execution, and deployment boundaries. These are areas where a small release or configuration assumption can change the answer.",
    "Three review batches now cover integration recovery, billing, ATP, credit, warehouse execution, deployment, production, quality, inventory, finance, automotive JIT/JIS, and transportation. The focus stays on claims that change a design or diagnostic decision.",
    1,
)
anchor = '      <a href="/labs/enterprise-context/deployment-models/"><span>3</span><strong>Deployment Models</strong><small>Public, Private, and on-premise operational and upgrade boundaries checked against the current SAP offering comparison.</small><i class="material-symbols-outlined" aria-hidden="true">cloud</i></a>'
extra = '''
      <a href="/labs/enterprise-context/production/"><span>2</span><strong>Production Planning & Execution</strong><small>Production version and manufacturing-order goods-receipt/cost-flow boundaries checked against SAP S/4HANA 2025 FPS01.</small><i class="material-symbols-outlined" aria-hidden="true">precision_manufacturing</i></a>
      <a href="/labs/enterprise-context/quality-management/"><span>2</span><strong>Quality Management</strong><small>Usage decision, inspection completion, and stock-relevant disposition checked against SAP S/4HANA 2025 FPS01.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="/labs/enterprise-context/inventory-management/"><span>2</span><strong>Inventory Management</strong><small>Movement-type control and physical-inventory difference posting checked against SAP S/4HANA 2025 FPS01.</small><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a>
      <a href="/labs/enterprise-context/finance-logistics/"><span>2</span><strong>FI/CO Logistics Bridge</strong><small>GR/IR clearing and production-order settlement boundaries checked against SAP S/4HANA 2025 FPS01.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
      <a href="/labs/enterprise-context/automotive-jit/"><span>2</span><strong>Automotive JIT/JIS</strong><small>2025 FPS01 nJIT end-to-end JIS integration and S2C delivery/TM flow checked against current SAP Help.</small><i class="material-symbols-outlined" aria-hidden="true">directions_car</i></a>
      <a href="/labs/enterprise-context/transportation-management/"><span>2</span><strong>Transportation Management</strong><small>Freight-unit/freight-order planning and TM-to-MM freight settlement checked against SAP S/4HANA 2025 FPS01.</small><i class="material-symbols-outlined" aria-hidden="true">local_shipping</i></a>'''
if extra.strip() not in text:
    if anchor not in text:
        raise SystemExit("Factual review card anchor not found")
    text = text.replace(anchor, anchor + extra, 1)
text = text.replace("Twenty-three reviewed claims across six release-sensitive SAP routes.", "Thirty-five reviewed claims across twelve release-sensitive SAP routes.", 1)
page_path.write_text(text, encoding="utf-8")

catalog_path = DATA / "catalog.json"
catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
catalog["version"] = "1.9.0"
marker = "Primary-source factual review across twelve core SAP assessment routes and thirty-five load-bearing claims"
if marker not in catalog["coverage"]["strong_now"]:
    catalog["coverage"]["strong_now"].append(marker)
catalog["coverage"]["next_practice_layers"] = [
    "create evidence-coverage summaries by assessment track and domain",
    "continue factual review for Pricing, Shipping, Procurement, MDG, Development, Tax, and other P0 evidence-debt routes",
    "connect real assessment feedback to review priority without converting feedback into factual truth",
    "extend graph-backed question generation only where factual evidence coverage is sufficient",
]
catalog_path.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

backlog_path = DATA / "backlog.json"
backlog = json.loads(backlog_path.read_text(encoding="utf-8"))
items = {item["id"]: item for item in backlog["items"]}
items["LOOP-020"] = {
    "id": "LOOP-020",
    "priority": "P1",
    "title": "Factual review batch three: core logistics execution and finance",
    "status": "done",
    "outputs": ["/labs/assessment/factual-review/", "/labs/assessment/data/factual-review.json"],
    "reviewed_routes": [route for route, _, _ in new_routes],
    "working_rule": "Review only load-bearing claims that change process ownership, diagnosis, execution, or financial completion. Keep source support separate from page verification.",
}
backlog["items"] = [items[key] for key in sorted(items)]
backlog["next_iteration_themes"] = [
    "create assessment-track evidence coverage and evidence-debt views",
    "continue factual review for remaining P0 enterprise routes",
    "connect feedback observations to review priority without changing factual truth",
    "use evidence coverage as a gate for future graph-backed question generation",
]
backlog_path.write_text(json.dumps(backlog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

assessment_path = ROOT / "labs/assessment/index.md"
assessment = assessment_path.read_text(encoding="utf-8")
assessment = assessment.replace(
    '<a href="/labs/assessment/data/factual-review.json"><span>23</span><strong>Factual Review Registry</strong><small>Twenty-three source-supported claims across six release-sensitive SAP routes; page verification remains unchanged.</small>',
    '<a href="/labs/assessment/data/factual-review.json"><span>35</span><strong>Factual Review Registry</strong><small>Thirty-five source-supported claims across twelve release-sensitive SAP routes; page verification remains unchanged.</small>',
    1,
)
assessment = assessment.replace(
    "LOOP-001 through LOOP-019 are complete; promotion priority now uses factual-review coverage.",
    "LOOP-001 through LOOP-020 are complete; twelve core SAP routes now have claim-level primary-source review.",
    1,
)
assessment_path.write_text(assessment, encoding="utf-8")

tests_path = ROOT / "tests/test_assessment_practice_layer.py"
tests = tests_path.read_text(encoding="utf-8")
tests = tests.replace(
    '("LOOP-010", "LOOP-011", "LOOP-012", "LOOP-013", "LOOP-014", "LOOP-015", "LOOP-016", "LOOP-017", "LOOP-018", "LOOP-019")',
    '("LOOP-010", "LOOP-011", "LOOP-012", "LOOP-013", "LOOP-014", "LOOP-015", "LOOP-016", "LOOP-017", "LOOP-018", "LOOP-019", "LOOP-020")',
    1,
)
tests = tests.replace('assert review["summary"]["routes_reviewed"] == 6', 'assert review["summary"]["routes_reviewed"] == 12', 1)
tests = tests.replace('assert review["summary"]["claims_reviewed"] == 23', 'assert review["summary"]["claims_reviewed"] == 35', 1)
tests = tests.replace('assert inventory["factual_review_counts"]["source_supported"] == len(reviewed_routes) == 6', 'assert inventory["factual_review_counts"]["source_supported"] == len(reviewed_routes) == 12', 1)
tests_path.write_text(tests, encoding="utf-8")

print(f"Factual review expanded to {review['summary']['routes_reviewed']} routes and {review['summary']['claims_reviewed']} claims.")
