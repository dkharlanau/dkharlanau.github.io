---
layout: default
title: "Atlas Backlog Publishing Map"
description: "Controlled publishing pipeline for promoting backlog material into Atlas review candidates."
permalink: /docs/atlas-backlog-publishing-map/
robots: noindex,follow
sitemap: false
---

# Atlas Backlog Publishing Map

*Generated: 2026-06-05*
*Status: living document — updated as batches progress*

## 1. Backlog Inventory Summary

| Source | Files | Markdown | Public/Private | Suitable for Atlas |
|---|---|---|---|---|
| `_notes/` | 7 | 7 | Public | 3 (after rewrite) |
| `_blog/` | 1 | 1 | Public | 0 (general systems, not SAP) |
| `_news/` | 3 | 3 | Public | 0 (time-bound signals) |
| `_radar/` | 5 | 5 | Public | 0 (time-bound signals) |
| `docs/` | 22 | 22 | Public | 0 (planning artifacts) |
| `datasets/` | ~100 | ~10 (index files) | Public | 0 (data feeds) |
| `professional-radar/` | 8 | 1 | Public | 0 (tooling/config) |
| `Kimi_Agent_SAP Atlas Expansion/` | 4 | 4 | Excluded | 0 (planning files) |
| Private source (`kb-drafts/`) | 753 | 753 | Private | 33 (already promoted); 672 merge candidates; 35 keep private; 13 archive |

**Total backlog inspected:** 803 files across all sources.

---

## 2. Classification Taxonomy

### By Action

| Action | Count | Sources |
|---|---|---|
| `promote_now` | 0 | — |
| `promote_after_cleanup` | 3 | `_notes/ai_ml.md`, `_notes/consulting_principles.md`, `_notes/tools_mini_apps.md` |
| `needs_fact_review` | 0 | — |
| `needs_rewrite_from_marketing_to_knowledge` | 3 | `_notes/ams.md`, `_notes/process_audit.md`, `_notes/composable_erp.md` (already have Atlas equivalents) |
| `merge_with_existing_atlas` | 3 | `_notes/ams.md` → `sap-ams-operating-model`, `_notes/process_audit.md` → `sap-process-audit`, `_notes/composable_erp.md` → `composable-erp-for-sap-operations` |
| `keep_as_note` | 2 | `_blog/the-system-that-waits.md`, `_notes/system-architecture.md` |
| `keep_as_radar_signal` | 8 | `_news/*`, `_radar/*` |
| `keep_private` | 70 | `docs/*`, `professional-radar/*`, excluded workspace, private-source planning files |
| `discard_or_archive` | 13 | Private-source thin/duplicate candidates (per ATLAS_EDITORIAL_REGISTER) |

### By Domain

| Domain | Public Candidates | Private Candidates |
|---|---|---|
| SAP AMS | 1 | 20+ |
| SAP SD / Order to Cash | 0 | 24+ |
| SAP MM / Procurement / P2P | 0 | 40+ |
| Master Data / Data Quality | 0 | 15+ |
| Integrations / IDoc / AIF / API | 1 | 25+ |
| AI Operations | 1 | 20+ |
| Agentic Workflows | 0 | 15+ |
| Process Diagnostics | 1 | 20+ |
| Operational Memory | 0 | 10+ |
| Vendor / Architecture / Lock-in | 1 | 10+ |
| General productivity / not Atlas | 2 | 50+ |

---

## 3. Top 30 Atlas Candidates

### Immediate batch (Batch 1 — merged)
1. ✅ AI-ML Sidecars for SAP (`_notes/ai_ml.md` → `atlas/ai-operations/ai-ml-sidecars-for-sap`)
2. ✅ Mini Apps for SAP Operations (`_notes/tools_mini_apps.md` → `atlas/automation/mini-apps-for-sap-operations`)
3. ✅ IDoc and AIF Integration Diagnostics (`_notes/ams.md` IDoc content → `atlas/diagnostics/idoc-aif-integration-diagnostics`)
4. ✅ SAP Clean Core Strategy (news/general knowledge → `atlas/concepts/sap-clean-core-strategy`)
5. ✅ SAP MM Procurement Overview (general SAP knowledge → `atlas/sap/sap-mm-procurement-overview`)
6. ✅ Consulting Principles for SAP Programmes (`_notes/consulting_principles.md` → `atlas/concepts/consulting-principles-for-sap`)

### Batch 2 (merged)
7. ✅ SAP Credit Management Diagnostics (private source → `atlas/diagnostics/sap-credit-management-diagnostics`)
8. ✅ SAP Delivery Block Analysis (private source → `atlas/diagnostics/sap-delivery-block-analysis`)
9. ✅ SAP Billing Block Analysis (private source → `atlas/diagnostics/sap-billing-block-analysis`)
10. ✅ SAP Incompletion Procedure Diagnostics (private source → `atlas/diagnostics/sap-incompletion-procedure-diagnostics`)
11. ✅ SAP Pricing Condition Technique (private source → `atlas/sap/sap-pricing-condition-technique`)
12. ✅ SAP Account Determination Diagnostics (private source → `atlas/sap/sap-account-determination-diagnostics`)

### Deferred to Batch 3 (next PR)
13. SAP Invoice Verification Patterns (private source → needs fact review)
14. SAP Movement Types and Inventory (private source → needs fact review)
15. SAP Stock Transfer and In-Transit (private source → needs fact review)
16. SAP Three-Way Match Diagnostics (private source → needs fact review)
17. SAP Procurement KPIs (private source → needs rewrite)
18. SAP GR/IR Clearing Deep-Dive (already exists as `gr-ir-clearing-explained` — consider expansion)
19. SAP MM Sourcing / Info Records / Source List (private source → needs fact review)
20. SAP Purchase Order Creation Diagnostics (private source → needs fact review)

### Deferred to Batch 4 (later)
21. SAP Integration Suite Event Mesh (private source → needs fact review)
22. SAP Ariba Integration Context (private source → needs fact review)
23. SAP Business Network Context (private source → needs fact review)
24. SAP EWM Integration Overview (private source → needs fact review)
25. SAP TM Integration Overview (private source → needs fact review)
26. SAP IBP Integration Overview (private source → needs fact review)
27. SAP MDG Governance Patterns (private source → needs rewrite)
28. Master Data Replication Patterns (private source → needs rewrite)
29. SAP Business Partner Governance (private source → needs fact review)
30. SAP Customer/Vendor Master Diagnostics (private source → needs fact review)

---

## 4. Duplicates / Merge Candidates

| Backlog Source | Existing Atlas Page | Action |
|---|---|---|
| `_notes/ams.md` | `atlas/automation/sap-ams-operating-model.md` | Keep _notes/ as public service page; Atlas page is the knowledge version |
| `_notes/process_audit.md` | `atlas/diagnostics/sap-process-audit.md` | Keep _notes/ as public service page; Atlas page is the knowledge version |
| `_notes/composable_erp.md` | `atlas/concepts/composable-erp-for-sap-operations.md` | Keep _notes/ as public service page; Atlas page is the knowledge version |

---

## 5. Risky / Private Candidates

| Candidate | Risk | Why Deferred |
|---|---|---|
| Private-source SAP diagnostic deep-dives | High | System-dependent claims need verification against public SAP docs |
| Private-source configuration guides | High | May contain landscape-specific assumptions |
| Private-source industry-specific procurement | Medium | Needs generalization before public release |
| `_notes/system-architecture.md` | Low | Not SAP knowledge — site architecture note |
| `_blog/the-system-that-waits.md` | Low | General systems design, not SAP-specific |

---

## 6. Service / Marketing Material Needing Conversion

| Source | Current Tone | Target Section | Conversion Needed |
|---|---|---|---|
| `_notes/ai_ml.md` | Service page ("Blueprint for SAP AI sidecars") | `atlas/ai-operations/` | Remove "I" language, remove CTA, convert to pattern description |
| `_notes/consulting_principles.md` | Service page ("How I run SAP programmes") | `atlas/concepts/` | Remove "I" language, generalize to principles |
| `_notes/tools_mini_apps.md` | Service page ("What I build", "Request a prototype") | `atlas/automation/` | Remove service offerings, convert to pattern catalog |

---

## 7. Recommended Publishing Batches

### Batch 1 (merged): 6 pages
- **Theme:** SAP operations knowledge — AI sidecars, mini apps, integration diagnostics, clean core, procurement overview, consulting principles
- **Source:** Public `_notes/` rewritten as knowledge
- **Status:** `needs_verification`
- **Robots:** `noindex,follow`
- **Sitemap:** `false`

### Batch 2 (merged): 6 pages
- **Theme:** SAP diagnostics deep-dives — credit management, delivery blocks, billing blocks, incompletion procedure, pricing condition technique, account determination
- **Source:** Private source used for topic discovery only; all pages rewritten from scratch as conservative diagnostic frames
- **Status:** `needs_verification`
- **Robots:** `noindex,follow`
- **Sitemap:** `false`

### Batch 3 (next PR): 6–8 pages
- **Theme:** Procurement and inventory — invoice verification, movement types, stock transfer, three-way match, sourcing, purchase order creation
- **Source:** Private source rewritten and verified
- **Status:** `needs_verification`
- **Robots:** `noindex,follow`
- **Sitemap:** `false`

### Batch 4 (later): 6–8 pages
- **Theme:** Integration and master data — Event Mesh, Ariba, EWM, TM, IBP, MDG, business partner governance, replication
- **Source:** Private source rewritten and verified
- **Status:** `needs_verification`
- **Robots:** `noindex,follow`
- **Sitemap:** `false`

---

## 8. Recommended Verification Batches

| Batch | Pages | Verification Approach |
|---|---|---|
| V1 | Batch 1 (6 pages) | Cross-check against public SAP docs, remove landscape-specific claims |
| V2 | Batch 2 (diagnostics) | Verify against SAP Help Portal, SAP Notes, release-independent docs |
| V3 | Batch 3 (procurement) | Verify against SAP MM docs, public configuration guides |
| V4 | Batch 4 (integration) | Verify against SAP Integration Suite docs, BTP docs |

---

## 9. Recommended Indexing Batches

| Batch | Pages | Indexing Criteria |
|---|---|---|
| I1 | Already verified (14 pages) | Already indexed or ready |
| I2 | Batch 1 after 2-week review | Conservative, no system-specific claims |
| I3 | Batch 2 after 4-week review | Verified against public docs |
| I4 | Batch 3+ after 6-week review | Full verification complete |

---

## 10. Current Atlas Counts

- **Total Atlas pages:** 38
- **Verified:** 14
- **Unverified:** 24
- **Related edges:** 110
- **Broken links:** 0

### After Batch 1
- **Total Atlas pages:** 32 (+6)
- **Verified:** 18 (unchanged)
- **Unverified:** 14 (+6)
- **Related edges:** ~80 (+12 estimated)
- **Broken links:** 0 (target)

### After Batch 2
- **Total Atlas pages:** 38 (+6)
- **Verified:** 14 (unchanged)
- **Unverified:** 24 (+6)
- **Related edges:** 110 (+18)
- **Broken links:** 0

---

*This map is updated after each batch. Last updated: 2026-06-05.*
