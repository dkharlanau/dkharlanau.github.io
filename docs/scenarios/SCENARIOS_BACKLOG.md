# Scenarios Backlog

## Purpose

This file tracks the SAP Process & Integration Scenarios section: created pages, deferred topics, future Atlas dependencies, and promotion candidates.

## Section positioning

- **Atlas** explains *how* to diagnose SAP issues (technical diagnostics, configuration, objects).
- **Scenarios** explains *why* those issues matter to business workflows, process cost, and support operations.

Scenarios pages connect business pain → SAP process context → master data / configuration / integration root causes → operational cost drivers → diagnostic workflow → solution patterns → AI/automation opportunities → related Atlas diagnostics.

---

## Created scenarios (flagship v1)

| # | Scenario title | File | Cluster | Related Atlas pages | Status |
|---|----------------|------|---------|---------------------|--------|
| 1 | Why customer master data issues block sales orders | `scenarios/master-data-issues-blocking-sales-orders.md` | Master Data Pain | `/atlas/diagnostics/sap-sales-order-block-diagnosis/`, `/atlas/diagnostics/sap-customer-master-replication-diagnostics/`, `/atlas/diagnostics/sap-incompletion-procedure-diagnostics/`, `/atlas/data-quality/sap-master-data-quality/`, `/atlas/concepts/order-to-cash/` | needs_verification |
| 2 | How BP replication failures break downstream SAP processes | `scenarios/bp-customer-replication-downstream-impact.md` | Master Data Pain | `/atlas/diagnostics/sap-business-partner-replication-diagnostics/`, `/atlas/diagnostics/sap-customer-master-replication-diagnostics/`, `/atlas/diagnostics/sap-key-mapping-diagnostics/`, `/atlas/diagnostics/sap-cvi-synchronization-diagnostics/`, `/atlas/diagnostics/sap-mdg-to-s4-replication-diagnostics/`, `/atlas/data-quality/sap-master-data-replication-patterns/` | needs_verification |
| 3 | Why vendor master data issues disrupt procurement | `scenarios/vendor-supplier-master-data-procurement-issues.md` | Master Data Pain | `/atlas/diagnostics/sap-vendor-master-replication-diagnostics/`, `/atlas/diagnostics/sap-purchase-order-creation-diagnostics/`, `/atlas/diagnostics/sap-source-determination-diagnostics/`, `/atlas/data-quality/sap-master-data-quality/`, `/atlas/sap/sap-mm-procurement-overview/` | needs_verification |
| 4 | Why invoice verification delays increase procurement support cost | `scenarios/invoice-verification-three-way-match-delays.md` | Process Execution Pain | `/atlas/diagnostics/sap-invoice-verification-diagnostics/`, `/atlas/diagnostics/sap-three-way-match-diagnostics/`, `/atlas/diagnostics/sap-goods-receipt-diagnostics/`, `/atlas/sap/gr-ir-clearing-explained/`, `/atlas/sap/sap-mm-procurement-overview/` | needs_verification |
| 5 | How delivery and billing block delays stall order-to-cash | `scenarios/delivery-billing-block-order-to-cash-delays.md` | Process Execution Pain | `/atlas/diagnostics/sap-delivery-block-analysis/`, `/atlas/diagnostics/sap-billing-block-analysis/`, `/atlas/diagnostics/sap-credit-management-diagnostics/`, `/atlas/diagnostics/sap-incompletion-procedure-diagnostics/`, `/atlas/concepts/order-to-cash/` | needs_verification |
| 6 | Why pricing and account determination errors cause billing failures | `scenarios/pricing-account-determination-billing-failures.md` | Process Execution Pain | `/atlas/sap/sap-pricing-condition-technique/`, `/atlas/sap/sap-pricing-procedure-debugging/`, `/atlas/diagnostics/sap-account-assignment-diagnostics/`, `/atlas/diagnostics/sap-billing-block-analysis/`, `/atlas/diagnostics/sap-invoice-split-analysis/` | needs_verification |
| 7 | How IDoc and API integration failures create unclear ownership | `scenarios/idoc-api-integration-failures-ownership.md` | Integration & Monitoring Pain | `/atlas/diagnostics/idoc-aif-integration-diagnostics/`, `/atlas/diagnostics/sap-idoc-status-diagnostics/`, `/atlas/diagnostics/sap-inbound-processing-diagnostics/`, `/atlas/diagnostics/sap-outbound-processing-diagnostics/`, `/atlas/diagnostics/sap-qrfc-trfc-diagnostics/`, `/atlas/concepts/integration-ownership-model/` | needs_verification |
| 8 | Why MDG change request delays stall master data activation | `scenarios/mdg-change-request-activation-delays.md` | Master Data Pain | `/atlas/data-quality/sap-mdg-governance-patterns/`, `/atlas/diagnostics/sap-business-partner-replication-diagnostics/`, `/atlas/diagnostics/sap-mdg-to-s4-replication-diagnostics/`, `/atlas/data-quality/master-data-governance-failure-modes/`, `/atlas/sap/sap-mdg/` | needs_verification |
| 9 | How duplicate master data drives hidden support cost | `scenarios/duplicate-master-data-support-cost.md` | Master Data Pain | `/atlas/diagnostics/sap-master-data-duplicate-diagnostics/`, `/atlas/diagnostics/sap-key-mapping-diagnostics/`, `/atlas/diagnostics/sap-number-range-diagnostics/`, `/atlas/data-quality/sap-master-data-quality/`, `/atlas/data-quality/master-data-governance-failure-modes/` | needs_verification |
| 10 | Why repeated SAP AMS incidents signal knowledge loss | `scenarios/repeated-sap-ams-incidents-knowledge-loss.md` | Support Cost & AMS Pain | `/atlas/automation/operational-memory-for-sap-ams/`, `/atlas/ai-operations/ai-agent-for-sap-support/`, `/atlas/diagnostics/sap-process-audit/`, `/atlas/concepts/consulting-principles-for-sap/` | needs_verification |
| 11 | How integration monitoring gaps create repeated incidents | `scenarios/integration-monitoring-gaps-sap-middleware.md` | Integration & Monitoring Pain | `/atlas/diagnostics/sap-interface-monitoring-diagnostics/`, `/atlas/diagnostics/sap-integration-error-handling-diagnostics/`, `/atlas/sap/sap-integration-suite/`, `/atlas/concepts/integration-ownership-model/`, `/atlas/maps/integration-monitoring-reliability-map/` | needs_verification |
| 12 | Building an AI-ready support knowledge layer for SAP AMS | `scenarios/ai-ready-support-knowledge-layer-sap-ams.md` | Technology Shift Scenarios | `/atlas/ai-operations/ai-agent-for-sap-support/`, `/atlas/ai-operations/ai-ready-process-documentation/`, `/atlas/automation/operational-memory-for-sap-ams/`, `/atlas/concepts/knowledge-graph-for-sap-operations/`, `/atlas/sap/rag/` | needs_verification |

---

## Deferred scenarios

| # | Scenario title | Reason for deferral | Future trigger |
|---|----------------|---------------------|----------------|
| 13 | Goods receipt and inventory posting failures | Partial overlap with existing GR diagnostic; better as a scenario after GR scenario backlog is cleared | When inventory posting pain is validated with operational cost data |
| 14 | Source-to-pay delays caused by supplier/purchasing data issues | Overlaps with scenarios 3 and 4; needs distinct angle on sourcing-specific pain | When sourcing/negotiation phase pain is clearly separable from procurement execution |
| 15 | Order-to-cash exception management across SAP, CRM, e-commerce, and WMS | High complexity, requires multi-system context; defer until CRM/e-commerce Atlas pages exist | When Atlas has CRM/e-commerce diagnostic coverage |
| 16 | Key mapping and CVI synchronization failures | Partial overlap with scenario 2; could be merged or promoted as standalone if CVI pain is validated | When CVI-specific ticket volume justifies separate scenario |
| 17 | Handover gaps between SAP AMS, integration teams, and business process owners | Organizational/process ownership pain; valuable but less SAP-object-centric; defer for v2 | When organizational pain is validated with case patterns |

---

## Future Atlas pages needed

Some scenarios reference Atlas pages that do not yet exist or are thin. These are noted as future candidates, not broken links.

| Atlas topic | Gap | Scenario dependency |
|-------------|-----|---------------------|
| SAP CRM sales order diagnostics | Does not exist | Scenario 15 |
| SAP e-commerce order integration diagnostics | Does not exist | Scenario 15 |
| SAP WMS integration diagnostics | Does not exist | Scenario 15 |
| SAP CVI deep-dive diagnostics | Thin | Scenario 2, 16 |
| SAP organizational data governance | Thin | Scenario 8, 17 |

---

## Future verification tasks

- Verify scenario claims against public SAP Help Portal documentation
- Cross-check cost driver estimates with public AMS benchmarking sources
- Validate AI/automation opportunity claims against real workflow patterns (not vendor marketing)
- Review related Atlas links for continued accuracy

## Candidates for Level 2 / index promotion

Scenarios may be promoted from `needs_verification` to `reviewed` and from `noindex` to `index` when:

1. All factual claims are verified against public SAP documentation or credible sources
2. Related Atlas links are confirmed valid
3. Cost driver estimates are backed by operational data or public benchmarks
4. No private corpus content is present
5. Page has been reviewed for style consistency

Promotion order (suggested):
1. Scenario 5 (delivery/billing blocks) — strong Atlas link coverage
2. Scenario 2 (BP replication) — high search value, good link coverage
3. Scenario 4 (invoice verification) — practical procurement pain
4. Scenario 10 (repeated AMS incidents) — differentiator content

---

## Safety confirmations

- All scenario pages created with `status: needs_verification`, `verified: false`, `robots: noindex,follow`, `sitemap: false`
- No private corpus content copied into scenario pages
- No private file paths exposed
- No client names, internal incidents, tickets, screenshots, or proprietary details exposed
- Scenarios pages excluded from `llms-full.txt` by virtue of unverified status
- Source research uses public-safe information only

---

*Backlog maintained as part of the Scenarios section. Last updated: 2026-06-09*
