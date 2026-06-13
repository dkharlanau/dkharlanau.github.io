# Hub Architecture Plan — SEO Visibility Swarm

**Date:** 2026-06-13  
**Branch:** `feat/seo-visibility-swarm`  
**Site:** https://dkharlanau.github.io  
**Author:** Dzmitryi Kharlanau  
**Atlas status:** 189 pages total (14 verified content pages + 8 verified index pages = 22 verified; 175 unverified/noindex)  
**Skill Hub status:** ~82 pages (all 11 sub-indexes verified; leaf pages unverified by default)  
**Scenarios status:** 12 pages (all unverified/noindex)  
**Research status:** ~40 pages (all noindex)  

---

## Executive Summary

Google struggles to understand the site because most deep content (Atlas diagnostics, Scenarios, Research) is `noindex`. The verified, indexable surface is thin: 22 Atlas pages, 11 Skill Hub sub-indexes, Services pages, and a few Datasets. Without hub pages, crawlers see disconnected islands.

**Strategy:** Create 5 narrow, verified hub pages that act as topical entry points. Each hub links only to verified/public destinations and explicitly acknowledges noindex content without linking to it as if it were indexable.

**Safety rule:** No hub page may be created without human review and verification. Agents may not mark pages `verified: true`.

---

## Hub Design Principles

1. **Link only to verified or naturally indexable pages.** Do not link to unverified Atlas diagnostics, Scenarios, or Research as if they are indexable.
2. **Each hub must survive on its own evidence.** If all linked destinations were removed, the hub should still be a credible, standalone page.
3. **Hubs are not sitemaps.** They are editorial, topical entry points with narrative flow and clear search intent mapping.
4. **Schema markup required.** `ItemList` or `CollectionPage` with `BreadcrumbList`.
5. **All hubs are Level 2 (verified, indexable).** They must pass `sitemap: true`, `robots: index,follow`, `status: reviewed`, `verified: true`.
6. **Acknowledge noindex content.** If a hub references unverified diagnostics, it must use a disclaimer like: *“Additional diagnostic deep-dives are maintained in the Atlas diagnostics collection and are currently under review.”* — without linking them as indexable destinations.

---

## Hub 1: `/sap-ams-diagnostics/`

**Target URL:** `https://dkharlanau.github.io/sap-ams-diagnostics/`  
**H1:** SAP AMS Diagnostics — Order-to-Cash, Delivery, and Master Data Support  
**SEO Title:** SAP AMS Diagnostics | O2C, Delivery Blocks, Credit, Pricing, BP — Dzmitryi Kharlanau  
**Meta Description:** Practical SAP AMS diagnostics for order-to-cash friction, delivery blocks, billing errors, credit management, pricing, account determination, and business partner replication. Structured support knowledge for SAP consultants and operations teams.  

**Primary Search Intent:** *Informational* — “SAP delivery block diagnostics,” “SAP billing block troubleshooting,” “SAP credit management support”  
**Secondary Search Intents:** *Navigational* (consultant looking for the Atlas), *Transactional* (hiring an SAP AMS consultant)

**Pages to Link To (verified/public):**
| Destination | Why |
|-------------|-----|
| `/atlas/diagnostics/` | Verified diagnostics index |
| `/atlas/concepts/order-to-cash/` | Verified O2C concept |
| `/atlas/maps/order-to-cash-map/` | Verified O2C process map |
| `/atlas/ai-operations/ai-agent-for-sap-support/` | Verified AI support concept |
| `/atlas/ai-operations/ai-ready-process-documentation/` | Verified documentation concept |
| `/atlas/automation/operational-memory-for-sap-ams/` | Verified operational memory |
| `/skill-hub/sap-ams/` | Verified skill group index |
| `/services/sap-ams-consulting/` | Indexable service page |
| `/services/sap-o2c-process-audit/` | Indexable service page |
| `/datasets/ams/` | Indexable dataset index |
| `/about/` | Canonical profile |

**Required Verified Pages Before Launch:**
- `/atlas/diagnostics/index.md` (already verified)
- `/atlas/concepts/order-to-cash.md` (already verified)
- `/atlas/maps/order-to-cash-map.md` (already verified)
- Hub page itself must be human-reviewed and marked `verified: true, status: reviewed`

**Pages That Must Remain Noindex:**
- All individual diagnostic pages: `sap-delivery-block-analysis.md`, `sap-delivery-processing-diagnostics.md`, `sap-credit-management-diagnostics.md`, `sap-incompletion-procedure-diagnostics.md`, `sap-billing-block-analysis.md`, `sap-account-assignment-diagnostics.md`, `sap-invoice-split-analysis.md`, `sap-business-partner-replication-diagnostics.md`, `sap-customer-master-replication-diagnostics.md`, `sap-cvi-synchronization-diagnostics.md`, `sap-key-mapping-diagnostics.md`, `sap-inbound-processing-diagnostics.md`, `sap-outbound-processing-diagnostics.md`, `sap-idoc-status-diagnostics.md`, `sap-ale-distribution-model-diagnostics.md`, `sap-interface-monitoring-diagnostics.md`, `idoc-aif-integration-diagnostics.md`, `sap-qrfc-trfc-diagnostics.md`, `sap-rfc-destination-diagnostics.md`, `sap-output-message-control-diagnostics.md`, `sap-background-job-diagnostics.md`, `sap-organizational-data-diagnostics.md`, `sap-number-range-diagnostics.md`, `sap-process-audit.md`, `sap-master-data-duplicate-diagnostics.md`, `sap-material-master-extension-diagnostics.md`, `sap-batch-determination-diagnostics.md`, `sap-material-document-diagnostics.md`, `sap-reservation-diagnostics.md`, `sap-purchasing-info-record-diagnostics.md`, `sap-physical-inventory-diagnostics.md`, `sap-movement-types-diagnostics.md`, `sap-mrp-exception-diagnostics.md`, `sap-purchase-requisition-diagnostics.md`, `sap-purchase-order-creation-diagnostics.md`, `sap-purchase-order-diagnostics.md`, `sap-consignment-procurement-diagnostics.md`, `sap-goods-receipt-diagnostics.md`, `sap-invoice-verification-diagnostics.md`, `sap-release-strategy-diagnostics.md`, `sap-returns-processing-diagnostics.md`, `sap-retail-replenishment-diagnostics.md`, `sap-retail-assortment-listing-diagnostics.md`, `pos-sales-not-reflected-in-sap.md`, `sap-customer-vendor-master-diagnostics.md`, `sap-mdg-to-s4-replication-diagnostics.md`, `sap-integration-error-handling-diagnostics.md`
- All Scenarios pages
- All Research pages

**Schema Type:** `CollectionPage` (main), `BreadcrumbList`, `ItemList` of linked entries, `Person` (author)  
**Risk Notes:** This hub is the broadest and overlaps with Hub 3 (BP/MDG) and Hub 4 (IDoc/Interface). Keep Hub 1 focused on *business process friction* (O2C, delivery, billing, credit) rather than technical integration plumbing. If the overlap causes internal cannibalization, merge Hub 1 and Hub 3 into a single `/sap-ams-diagnostics/` hub and drop Hub 3.

---

## Hub 2: `/sap-mm-procurement-diagnostics/`

**Target URL:** `https://dkharlanau.github.io/sap-mm-procurement-diagnostics/`  
**H1:** SAP MM Procurement Diagnostics — Purchase-to-Pay, Invoice Verification, and Stock Management  
**SEO Title:** SAP MM Procurement Diagnostics | P2P, Invoice Verification, GR, Stock — Dzmitryi Kharlanau  
**Meta Description:** Practical SAP MM procurement diagnostics for purchase-to-pay friction, invoice verification delays, goods receipt issues, stock transfers, movement types, and release strategy. Structured support knowledge for SAP operations teams.  

**Primary Search Intent:** *Informational* — “SAP invoice verification troubleshooting,” “SAP GR IR differences,” “SAP purchase order release strategy”  
**Secondary Search Intents:** *Navigational* (Atlas), *Transactional* (consulting)

**Pages to Link To (verified/public):**
| Destination | Why |
|-------------|-----|
| `/atlas/maps/procure-to-pay-map/` | Verified P2P map |
| `/atlas/concepts/order-to-cash/` | Verified concept (boundary context) |
| `/atlas/concepts/sap-atp-is-not-inventory/` | Verified inventory concept |
| `/atlas/concepts/sap-stock-exists-not-promisable/` | Verified stock concept |
| `/atlas/concepts/store-receiving-sap-retail/` | Verified retail concept |
| `/atlas/data-quality/sap-master-data-quality/` | Verified data quality |
| `/atlas/data-quality/master-data-governance-failure-modes/` | Verified governance |
| `/skill-hub/dama-dmbok/` | Verified data skill group |
| `/skill-hub/sap-ams/` | Verified AMS skill group |
| `/services/sap-o2c-process-audit/` | Indexable service |
| `/datasets/ams/` | Indexable dataset |
| `/about/` | Canonical profile |

**Required Verified Pages Before Launch:**
- `/atlas/maps/procure-to-pay-map.md` (already verified)
- `/atlas/data-quality/sap-master-data-quality.md` (already verified)
- `/atlas/data-quality/master-data-governance-failure-modes.md` (already verified)
- Hub page itself must be human-reviewed

**Pages That Must Remain Noindex:**
- All unverified MM diagnostics: `sap-invoice-verification-diagnostics.md`, `sap-goods-receipt-diagnostics.md`, `sap-purchase-order-diagnostics.md`, `sap-purchase-order-creation-diagnostics.md`, `sap-purchase-requisition-diagnostics.md`, `sap-release-strategy-diagnostics.md`, `sap-movement-types-diagnostics.md`, `sap-material-master-extension-diagnostics.md`, `sap-material-document-diagnostics.md`, `sap-physical-inventory-diagnostics.md`, `sap-reservation-diagnostics.md`, `sap-purchasing-info-record-diagnostics.md`, `sap-consignment-procurement-diagnostics.md`, `sap-returns-processing-diagnostics.md`, `sap-retail-replenishment-diagnostics.md`, `sap-retail-assortment-listing-diagnostics.md`, `sap-mrp-exception-diagnostics.md`, `sap-batch-determination-diagnostics.md`, `sap-spool-output-diagnostics.md`
- All Scenarios (e.g., `invoice-verification-three-way-match-delays.md`, `vendor-supplier-master-data-procurement-issues.md`)

**Schema Type:** `CollectionPage`, `BreadcrumbList`, `ItemList`  
**Risk Notes:** Fewer verified pages than Hub 1. The hub must rely heavily on the P2P map and data-quality verified pages to provide substance. If the P2P map is too thin, this hub will look like a thin doorway. Consider delaying until 2–3 additional MM diagnostics are verified.

---

## Hub 3: `/sap-mdg-bp-replication-diagnostics/`

**Target URL:** `https://dkharlanau.github.io/sap-mdg-bp-replication-diagnostics/`  
**H1:** SAP MDG and BP Replication Diagnostics — Master Data, CVI, and Key Mapping  
**SEO Title:** SAP MDG BP Replication Diagnostics | CVI, Key Mapping, Vendor/Customer — Dzmitryi Kharlanau  
**Meta Description:** Practical SAP MDG and business partner replication diagnostics for CVI synchronization, key mapping, vendor/customer master data, and governance failure modes. Structured support knowledge for SAP operations teams.  

**Primary Search Intent:** *Informational* — “SAP BP replication error,” “SAP CVI synchronization troubleshooting,” “SAP MDG key mapping”  
**Secondary Search Intents:** *Navigational* (Atlas), *Transactional* (consulting)

**Pages to Link To (verified/public):**
| Destination | Why |
|-------------|-----|
| `/atlas/data-quality/sap-master-data-quality/` | Verified data quality |
| `/atlas/data-quality/master-data-governance-failure-modes/` | Verified governance |
| `/atlas/data-quality/` | Verified data quality index |
| `/atlas/sap/` | Verified SAP index |
| `/skill-hub/dama-dmbok/` | Verified data skill group |
| `/skill-hub/sap-ams/` | Verified AMS skill group |
| `/services/sap-integration-architecture/` | Indexable service |
| `/datasets/ams/` | Indexable dataset |
| `/about/` | Canonical profile |

**Required Verified Pages Before Launch:**
- `/atlas/data-quality/sap-master-data-quality.md` (already verified)
- `/atlas/data-quality/master-data-governance-failure-modes.md` (already verified)
- Hub page itself must be human-reviewed
- **Recommendation:** Verify at least one of `sap-business-partner-replication-diagnostics.md`, `sap-cvi-synchronization-diagnostics.md`, or `sap-key-mapping-diagnostics.md` before launching this hub, otherwise it will be too thin.

**Pages That Must Remain Noindex:**
- All unverified BP/MDG diagnostics: `sap-business-partner-replication-diagnostics.md`, `sap-customer-master-replication-diagnostics.md`, `sap-cvi-synchronization-diagnostics.md`, `sap-key-mapping-diagnostics.md`, `sap-mdg-to-s4-replication-diagnostics.md`, `sap-customer-vendor-master-diagnostics.md`, `sap-bp-relationship-diagnostics.md`, `sap-master-data-duplicate-diagnostics.md`
- Scenarios: `bp-customer-replication-downstream-impact.md`, `mdg-change-request-activation-delays.md`, `duplicate-master-data-support-cost.md`, `master-data-issues-blocking-sales-orders.md`

**Schema Type:** `CollectionPage`, `BreadcrumbList`, `ItemList`  
**Risk Notes:** This is the thinnest hub in terms of verified backing content. There is no verified BP-specific diagnostic page yet. Launching without at least one verified BP/MDG diagnostic risks creating a low-quality doorway page. **Strong recommendation:** delay until 1–2 BP diagnostics are verified, or merge this content into Hub 1.

---

## Hub 4: `/sap-idoc-interface-diagnostics/`

**Target URL:** `https://dkharlanau.github.io/sap-idoc-interface-diagnostics/`  
**H1:** SAP IDoc and Interface Diagnostics — ALE, Status, qRFC, and Monitoring  
**SEO Title:** SAP IDoc Interface Diagnostics | ALE, qRFC, Status, Monitoring — Dzmitryi Kharlanau  
**Meta Description:** Practical SAP IDoc and interface diagnostics for ALE distribution models, IDoc status codes, qRFC queues, inbound/outbound processing, and integration monitoring. Structured support knowledge for SAP operations teams.  

**Primary Search Intent:** *Informational* — “SAP IDoc status 51 troubleshooting,” “SAP qRFC queue stuck,” “SAP ALE distribution model error”  
**Secondary Search Intents:** *Navigational* (Atlas), *Transactional* (consulting)

**Pages to Link To (verified/public):**
| Destination | Why |
|-------------|-----|
| `/atlas/diagnostics/` | Verified diagnostics index |
| `/atlas/concepts/sap-integration-architecture/` | **Note: currently unverified.** If not verified before launch, omit. |
| `/atlas/automation/rule-based-automation-vs-ai/` | Verified automation concept |
| `/skill-hub/integration-architecture/` | Verified integration skill group |
| `/skill-hub/sap-ams/` | Verified AMS skill group |
| `/services/sap-integration-architecture/` | Indexable service |
| `/datasets/ams/` | Indexable dataset |
| `/about/` | Canonical profile |

**Required Verified Pages Before Launch:**
- `/atlas/diagnostics/index.md` (already verified)
- `/skill-hub/integration-architecture/index.md` (already verified)
- Hub page itself must be human-reviewed
- **Recommendation:** Verify `sap-idoc-status-diagnostics.md` or `sap-qrfc-trfc-diagnostics.md` before launch, or rely on the diagnostics index as the only deep link.

**Pages That Must Remain Noindex:**
- All unverified interface diagnostics: `sap-idoc-status-diagnostics.md`, `sap-inbound-processing-diagnostics.md`, `sap-outbound-processing-diagnostics.md`, `sap-ale-distribution-model-diagnostics.md`, `sap-interface-monitoring-diagnostics.md`, `idoc-aif-integration-diagnostics.md`, `sap-qrfc-trfc-diagnostics.md`, `sap-rfc-destination-diagnostics.md`, `sap-integration-error-handling-diagnostics.md`, `sap-output-message-control-diagnostics.md`
- Scenarios: `idoc-api-integration-failures-ownership.md`, `integration-monitoring-gaps-sap-middleware.md`

**Schema Type:** `CollectionPage`, `BreadcrumbList`, `ItemList`  
**Risk Notes:** Similar to Hub 3, this hub lacks verified deep content. The IDoc status diagnostics page is particularly valuable but currently unverified. Consider merging this hub into Hub 1 as a subsection, or delay until `sap-idoc-status-diagnostics.md` is verified.

---

## Hub 5: `/ai-assisted-sap-support/`

**Target URL:** `https://dkharlanau.github.io/ai-assisted-sap-support/`  
**H1:** AI-Assisted SAP Support — Operational Memory, Incident Triage, and Knowledge Capture  
**SEO Title:** AI-Assisted SAP Support | Incident Triage, Knowledge Capture, Automation — Dzmitryi Kharlanau  
**Meta Description:** Practical AI-assisted SAP support workflows for incident triage, operational memory, knowledge capture, side-by-side automation, and clean-core AI governance. Structured guidance for SAP AMS teams and AI agents.  

**Primary Search Intent:** *Informational* — “AI assisted SAP support,” “SAP AMS incident triage automation,” “operational memory for SAP support”  
**Secondary Search Intents:** *Navigational* (Skill Hub), *Transactional* (consulting), *Commercial* (AI enablement services)

**Pages to Link To (verified/public):**
| Destination | Why |
|-------------|-----|
| `/atlas/ai-operations/` | Verified AI operations index |
| `/atlas/ai-operations/ai-agent-for-sap-support/` | Verified AI agent concept |
| `/atlas/ai-operations/ai-ready-process-documentation/` | Verified documentation |
| `/atlas/ai-operations/authorization-aware-ai-for-sap/` | Verified governance |
| `/atlas/automation/operational-memory-for-sap-ams/` | Verified operational memory |
| `/atlas/automation/agent-assisted-development-workflows/` | Verified dev workflows |
| `/atlas/automation/rule-based-automation-vs-ai/` | Verified automation strategy |
| `/skill-hub/ai-assisted-analysis/` | Verified AI skill group |
| `/skill-hub/sap-ams/` | Verified AMS skill group |
| `/services/sap-ai-ml-enablement/` | Indexable service |
| `/datasets/ai-business-signals/` | Indexable dataset |
| `/about/` | Canonical profile |
| `/ai/` | Machine-readable AI endpoint index |

**Required Verified Pages Before Launch:**
- All 4 verified `ai-operations/` pages (already verified)
- All 3 verified `automation/` pages (already verified)
- `/skill-hub/ai-assisted-analysis/index.md` (already verified)
- Hub page itself must be human-reviewed

**Pages That Must Remain Noindex:**
- All unverified AI/automation pages in `atlas/ai-operations/` and `atlas/automation/` (if any added later)
- All Research pages (e.g., `ai-agents-for-ams-incident-triage.md`, `mcp-and-enterprise-tool-use.md`, `knowledge-graphs-for-support-memory.md`)
- Scenarios: `ai-ready-support-knowledge-layer-sap-ams.md`, `repeated-sap-ams-incidents-knowledge-loss.md`
- Unverified Skill Hub leaf pages (most skill pages are unverified)

**Schema Type:** `CollectionPage`, `BreadcrumbList`, `ItemList`, `Service` (link to consulting service)  
**Risk Notes:** This is the strongest hub because it has the most verified backing content. It is also the most aligned with the owner’s current positioning. **Launch this hub first.**

---

## Risk and Dependency Matrix

| Hub | Verified Backing Pages | Overlap Risk | Doorway Risk | Recommended Priority |
|-----|------------------------|--------------|--------------|----------------------|
| 1 — SAP AMS Diagnostics | Medium-High | Overlaps with 3, 4 | Low if focused on O2C | **2** |
| 2 — MM Procurement | Low-Medium | Isolated | Medium — thin content | **4** (delay) |
| 3 — MDG/BP Replication | Low | Overlaps with 1 | High — very thin | **5** (delay or merge) |
| 4 — IDoc/Interface | Low | Overlaps with 1 | High — very thin | **5** (delay or merge) |
| 5 — AI-Assisted SAP Support | High | Isolated | Low | **1** (launch first) |

**Overlap Mitigation:** If Hubs 3 and 4 are delayed, fold their topics into Hub 1 as subsections with clear anchors. For example, Hub 1 could have an “Integration and IDoc” section and a “Master Data and BP” section that name the noindex diagnostics without linking them as indexable destinations.

---

## Launch Sequencing

1. **Phase 1 (immediate):** Hub 5 — AI-Assisted SAP Support. Highest verified content density, lowest risk, strongest alignment with current positioning.
2. **Phase 2 (after 2–3 additional diagnostics verified):** Hub 1 — SAP AMS Diagnostics. Requires `sap-delivery-block-analysis.md` or `sap-billing-block-analysis.md` verified, or the hub remains too broad.
3. **Phase 3 (after P2P/GR content verified):** Hub 2 — MM Procurement. Requires at least `sap-invoice-verification-diagnostics.md` or `sap-goods-receipt-diagnostics.md` verified.
4. **Phase 4 (after BP/IDoc content verified):** Hubs 3 and 4, or merge them into Hub 1.

---

## Noindex Content Disclosure Policy

Every hub must include a standard disclosure near the bottom:

> **Atlas diagnostics deep-dives.** This hub references a larger collection of SAP diagnostic pages maintained in the [Atlas diagnostics](/atlas/diagnostics/) index. Individual diagnostic pages are released for indexing only after independent review. Until then, they remain accessible for operational use but are not promoted to search engines.

This keeps the site honest, aligns with the verification policy, and signals quality control to Google.

---

## Schema Template (for all hubs)

```json
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "{H1}",
  "description": "{meta description}",
  "url": "https://dkharlanau.github.io{path}/",
  "author": {
    "@type": "Person",
    "@id": "https://dkharlanau.github.io/#dkharlanau",
    "name": "Dzmitryi Kharlanau",
    "url": "https://dkharlanau.github.io/about/"
  },
  "isPartOf": {
    "@type": "WebSite",
    "name": "Dzmitryi Kharlanau — SAP AMS Consultant",
    "url": "https://dkharlanau.github.io"
  },
  "mainEntity": {
    "@type": "ItemList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "...",
        "url": "..."
      }
    ]
  },
  "breadcrumb": {
    "@type": "BreadcrumbList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://dkharlanau.github.io/" },
      { "@type": "ListItem", "position": 2, "name": "{Hub Name}", "item": "https://dkharlanau.github.io{path}/" }
    ]
  }
}
```

---

## Sitemap Impact

Each hub, once verified, will appear in:
- `sitemap-pages.xml` (as a `site.page` with `verified: true, status: reviewed`)
- `llms-full.txt` (generated by `scripts/generate_atlas_artifacts.py`)
- Section sitemaps if added to `_config.yml` or generator logic

Before creating a hub, update `scripts/generate_atlas_artifacts.py` or confirm that non-Atlas verified pages are included in `llms-full.txt`. Currently the generator may only scan `atlas/`, `scenarios/`, and `skill-hub/`. A root-level hub like `/sap-ams-diagnostics/` may need explicit inclusion logic.

---

## Summary Checklist

- [ ] Hub 5 designed and human-reviewed
- [ ] Hub 5 page created with `verified: true, status: reviewed, robots: index,follow, sitemap: true`
- [ ] Hub 5 schema markup validated
- [ ] `bundle exec jekyll build` passes
- [ ] `python3 scripts/check_seo.py _site` passes
- [ ] `python3 scripts/check_links.py _site` passes
- [ ] Hub 1–4 planned but not created until backing diagnostics verified
- [ ] README updated if new major sections added (see `github-proof-loop-2026-06-13.md`)
