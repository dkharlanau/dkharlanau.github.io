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
    ("/labs/enterprise-context/business-ai/", "SAP Business AI", ["FACT-BAI-001", "FACT-BAI-002"]),
    ("/labs/enterprise-context/mdg/", "Master Data Governance", ["FACT-MDG-001", "FACT-MDG-002"]),
    ("/labs/enterprise-context/integrations/", "Integration Architecture", ["FACT-INT-001", "FACT-INT-002"]),
    ("/labs/enterprise-context/development/", "SAP Development Architecture", ["FACT-DEV-001", "FACT-DEV-002"]),
]
new_claims = [
    claim(
        "FACT-BAI-001",
        "/labs/enterprise-context/business-ai/",
        "Joule brings AI assistants and agents into a common SAP experience. SAP describes it as embedded into work across SAP and non-SAP systems, with a conversational UI, contextual business information, access controls, governance, analytics, and extensibility mechanisms.",
        ["SRC-SAP-JOULE-HELP"],
        ["https://help.sap.com/docs/JOULE/3fdd7b321eb24d1b9d40605dce822e84?locale=en-US"],
        "SAP Joule",
        "Cloud service documentation checked 2026-08-16",
    ),
    claim(
        "FACT-BAI-002",
        "/labs/enterprise-context/business-ai/",
        "SAP AI Core is a service on SAP BTP for standardized execution and lifecycle management of AI assets. The generative AI hub is a capability of SAP AI Core and SAP AI Launchpad for governed access to and orchestration of generative AI models; it extends rather than replaces the AI Core runtime foundation.",
        ["SRC-SAP-AI-CORE", "SRC-SAP-GENAI-HUB"],
        [
            "https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/sap-ai-core-overview?locale=en-us",
            "https://help.sap.com/docs/sap-ai-core/generative-ai/generative-ai-hub",
        ],
        "SAP AI Core and generative AI hub",
        "Cloud service documentation checked 2026-08-16",
    ),
    claim(
        "FACT-MDG-001",
        "/labs/enterprise-context/mdg/",
        "SAP MDG on SAP S/4HANA 2025 FPS01 offers classic mode and cloud-ready mode. Classic mode covers a broad set of central-governance, consolidation, data-quality, and master-data domains, while cloud-ready mode currently supports the Business Partner domain and uses a cloud-ready extensibility approach.",
        ["SRC-SAP-MDG-S4-OVERVIEW", "SRC-SAP-MDG-CLASSIC", "SRC-SAP-MDG-CLOUD-READY"],
        [
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/be72563dbbef459c8d953b7e3b0f99dc.html",
            "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/744b92a39ff34188a4c50563e62f8c10.html",
        ],
        "SAP Master Data Governance on SAP S/4HANA",
        "SAP S/4HANA 2025 FPS01",
        "release_scope",
    ),
    claim(
        "FACT-MDG-002",
        "/labs/enterprise-context/mdg/",
        "Switching on cloud-ready mode enables its apps but disables classic-mode consolidation and mass-processing apps and related functions. Processes created in classic mode can continue in cloud-ready mode, while processes created in cloud-ready mode cannot be continued after switching back to classic mode.",
        ["SRC-SAP-MDG-CLOUD-READY-SWITCH"],
        ["https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/34085136212d495aa7718063a34c5485.html"],
        "SAP Master Data Governance cloud-ready mode",
        "SAP S/4HANA 2025 FPS01",
        "configuration_behavior",
    ),
    claim(
        "FACT-INT-001",
        "/labs/enterprise-context/integrations/",
        "SAP Integration Suite is an integration platform on SAP BTP for cloud, on-premise, and hybrid scenarios. Its current capability landscape includes process integration with Cloud Integration, API management or composition, business events, B2B integration, third-party connectivity, migration assessment, and customer-managed edge execution options.",
        ["SRC-SAP-INTEGRATION-SUITE", "SRC-SAP-INTEGRATION-CONNECTIVITY"],
        ["https://help.sap.com/docs/SAP_INTEGRATION_SUITE/51ab953548be4459bfe8539ecaeee98d/what-is-sap-integration-suite"],
        "SAP Integration Suite",
        "Cloud service documentation checked 2026-08-16",
    ),
    claim(
        "FACT-INT-002",
        "/labs/enterprise-context/integrations/",
        "SAP Event Mesh supports asynchronous publish-and-consume business events and decoupled communication across applications. Advanced Event Mesh adds distributed event streaming, event management, monitoring, and event-broker capabilities for larger event-driven landscapes.",
        ["SRC-SAP-EVENT-MESH", "SRC-SAP-INTEGRATION-SUITE-EVENT-MESH", "SRC-SAP-ADVANCED-EVENT-MESH"],
        [
            "https://help.sap.com/docs/SAP_EM/bf82e6b26456494cbdd197057c09979f/what-is-sap-event-mesh",
            "https://help.sap.com/docs/sap-integration-suite/advanced-event-mesh",
        ],
        "SAP Event Mesh and SAP Integration Suite, Advanced Event Mesh",
        "Cloud service documentation checked 2026-08-16",
    ),
    claim(
        "FACT-DEV-001",
        "/labs/enterprise-context/development/",
        "Developer extensibility in SAP S/4HANA Cloud Public Edition 2608 is available in a three-system landscape and uses a cloud-optimized ABAP subset, released SAP APIs and objects, and predefined extension points. RAP and ADT are part of this developer-extensibility model.",
        ["SRC-SAP-S4-PUBLIC-DEVELOPER-2608", "SRC-SAP-ADT-ECLIPSE-2608"],
        ["https://help.sap.com/docs/SAP_S4HANA_CLOUD/6aa39f1ac05441e5a23f484f31e477e7/e1059ff581854a699f15734049f14293.html"],
        "SAP S/4HANA Cloud Public Edition developer extensibility",
        "2608 Latest documentation checked 2026-08-16",
        "release_scope",
    ),
    claim(
        "FACT-DEV-002",
        "/labs/enterprise-context/development/",
        "RAP business objects use CDS view entities as the data-model basis. In managed implementation, the RAP provider supplies standard transactional behavior and buffering; in unmanaged implementation, the developer implements the transactional behavior and buffer, which supports reuse of existing business logic.",
        ["SRC-SAP-RAP-IMPLEMENTATION-TYPES"],
        ["https://help.sap.com/docs/ABAP_PLATFORM_NEW/fc4c71aa50014fd1b43721701471913d/e11757cf7e664121b9f583e7ca0eeb39.html"],
        "ABAP RESTful Application Programming Model",
        "ABAP Platform 2025 FPS01",
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
review["version"] = "1.4.0"
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
text = text.replace('id="fact-routes">12</strong>', 'id="fact-routes">16</strong>', 1)
text = text.replace('id="fact-claims">35</strong>', 'id="fact-claims">43</strong>', 1)
text = text.replace('id="fact-supported">35</strong>', 'id="fact-supported">43</strong>', 1)
text = text.replace(
    "Three review batches now cover integration recovery, billing, ATP, credit, warehouse execution, deployment, production, quality, inventory, finance, automotive JIT/JIS, and transportation. The focus stays on claims that change a design or diagnostic decision.",
    "The review now covers sixteen SAP routes, including the first AI/Data and development architecture batch. The focus stays on product facts that change design, ownership, recovery, or release decisions.",
    1,
)
anchor = '      <a href="/labs/enterprise-context/transportation-management/"><span>2</span><strong>Transportation Management</strong><small>Freight-unit/freight-order planning and TM-to-MM freight settlement checked against SAP S/4HANA 2025 FPS01.</small><i class="material-symbols-outlined" aria-hidden="true">local_shipping</i></a>'
extra = '''
      <a href="/labs/enterprise-context/business-ai/"><span>2</span><strong>SAP Business AI</strong><small>Joule and SAP AI Core / generative AI hub boundaries checked against current SAP Help.</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
      <a href="/labs/enterprise-context/mdg/"><span>2</span><strong>Master Data Governance</strong><small>Classic vs cloud-ready mode and switching restrictions checked against SAP S/4HANA 2025 FPS01.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/labs/enterprise-context/integrations/"><span>2</span><strong>Integration Architecture</strong><small>Integration Suite capability boundaries and Event Mesh / Advanced Event Mesh roles checked against current SAP Help.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="/labs/enterprise-context/development/"><span>2</span><strong>SAP Development Architecture</strong><small>Public Edition 2608 developer extensibility and RAP managed/unmanaged behavior checked against current SAP Help.</small><i class="material-symbols-outlined" aria-hidden="true">code</i></a>'''
if extra.strip() not in text:
    if anchor not in text:
        raise SystemExit("Factual review page anchor not found")
    text = text.replace(anchor, anchor + extra, 1)
text = text.replace("Thirty-five reviewed claims across twelve release-sensitive SAP routes.", "Forty-three reviewed claims across sixteen SAP product routes.", 1)
page_path.write_text(text, encoding="utf-8")

catalog_path = DATA / "catalog.json"
catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
catalog["version"] = "2.2.0"
marker = "Product-primary factual review covers SAP Business AI, MDG, Integration architecture, and Development in addition to core logistics"
if marker not in catalog["coverage"]["strong_now"]:
    catalog["coverage"]["strong_now"].append(marker)
catalog["coverage"]["next_practice_layers"] = [
    "review mixed-evidence Data Governance with SAP product sources plus appropriate standards or explicit author heuristics",
    "continue profile-aware P0 routes such as Pricing, Procurement, Shipping, Sales Order, and MDG interfaces",
    "add evidence-class coverage summaries to show product facts versus standards or research",
    "use evidence coverage as a gate for future graph-backed question generation",
]
catalog_path.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

backlog_path = DATA / "backlog.json"
backlog = json.loads(backlog_path.read_text(encoding="utf-8"))
items = {item["id"]: item for item in backlog["items"]}
items["LOOP-023"] = {
    "id": "LOOP-023",
    "priority": "P1",
    "title": "AI/Data and Integration product-primary factual review",
    "status": "done",
    "outputs": ["/labs/assessment/factual-review/", "/labs/assessment/data/factual-review.json", "/labs/assessment/data/evidence-coverage.json"],
    "reviewed_routes": [route for route, _, _ in new_routes],
    "working_rule": "Improve assessment balance by reviewing load-bearing SAP product facts in AI/Data and Integration, while keeping generic architecture heuristics in their own evidence class.",
}
backlog["items"] = [items[key] for key in sorted(items)]
backlog["next_iteration_themes"] = [
    "review mixed-evidence Data Governance without pretending consultant heuristics are SAP product facts",
    "continue the highest profile-aware P0 evidence debt after coverage recalculation",
    "add evidence-class coverage summaries by track",
    "use evidence class and coverage as quality gates for generated assessment questions",
]
backlog_path.write_text(json.dumps(backlog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

assessment_path = ROOT / "labs/assessment/index.md"
assessment = assessment_path.read_text(encoding="utf-8")
assessment = assessment.replace(
    '<a href="/labs/assessment/data/factual-review.json"><span>35</span><strong>Factual Review Registry</strong><small>Thirty-five source-supported claims across twelve release-sensitive SAP routes; page verification remains unchanged.</small>',
    '<a href="/labs/assessment/data/factual-review.json"><span>43</span><strong>Factual Review Registry</strong><small>Forty-three source-supported product claims across sixteen SAP routes; page verification remains unchanged.</small>',
    1,
)
assessment = assessment.replace(
    "LOOP-001 through LOOP-022 are complete; evidence debt now respects the evidence class expected by each route.",
    "LOOP-001 through LOOP-023 are complete; AI/Data and Integration product facts now have materially better source coverage.",
    1,
)
assessment_path.write_text(assessment, encoding="utf-8")

tests_path = ROOT / "tests/test_assessment_practice_layer.py"
tests = tests_path.read_text(encoding="utf-8")
tests = tests.replace(
    '("LOOP-010", "LOOP-011", "LOOP-012", "LOOP-013", "LOOP-014", "LOOP-015", "LOOP-016", "LOOP-017", "LOOP-018", "LOOP-019", "LOOP-020", "LOOP-021", "LOOP-022")',
    '("LOOP-010", "LOOP-011", "LOOP-012", "LOOP-013", "LOOP-014", "LOOP-015", "LOOP-016", "LOOP-017", "LOOP-018", "LOOP-019", "LOOP-020", "LOOP-021", "LOOP-022", "LOOP-023")',
    1,
)
tests = tests.replace('assert review["summary"]["routes_reviewed"] == 12', 'assert review["summary"]["routes_reviewed"] == 16', 1)
tests = tests.replace('assert review["summary"]["claims_reviewed"] == 35', 'assert review["summary"]["claims_reviewed"] == 43', 1)
tests = tests.replace('assert inventory["factual_review_counts"]["source_supported"] == len(reviewed_routes) == 12', 'assert inventory["factual_review_counts"]["source_supported"] == len(reviewed_routes) == 16', 1)
tests = tests.replace('assert coverage["summary"]["unique_source_reviewed_routes"] >= 12', 'assert coverage["summary"]["unique_source_reviewed_routes"] >= 16', 1)
tests = tests.replace('assert coverage["summary"]["source_supported_claims"] >= 35', 'assert coverage["summary"]["source_supported_claims"] >= 43', 1)
tests_path.write_text(tests, encoding="utf-8")

print(f"Factual review expanded to {review['summary']['routes_reviewed']} routes and {review['summary']['claims_reviewed']} claims.")
