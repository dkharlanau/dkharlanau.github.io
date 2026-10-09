# BTP handbook: second architecture and exam-preparation review

Review date: 2026-10-09. Canonical route: `/atlas/sap/sap-btp/`.

This is an editorial and implementation review, not human publication approval or proof of certification readiness. The page remains `needs_verification`, `verified: false`, `noindex,follow`, `sitemap: false`.

## Scope and source boundary

Re-read the complete 18-chapter handbook, including the glossary, six diagrams, methods and development exercise. Retained sections that already answered their architectural question. Added a separate exam-orientation chapter rather than another long series of lesson summaries. The composition now has 19 primary handbook chapters and two expandable supplementary review chapters, 140 unique glossary terms and 34 native disclosures, including the two supplementary containers.

The supplied SAP Learning 2610 extracts remain the curriculum basis. Current SAP documentation supplements them for product prerequisites, commercial restrictions, communication setup and resilience. Original priorities, design matrices, numerical requirements and oral scenarios are explicitly teaching exercises, not official exam weights or customer results.

The public certification page now identifies **C_BAIPA**, SAP Certified - Solution Architect - SAP Business AI Platform, with one scenario-based activity, two hours and a 60% passing score. This corrects the previous handbook's P_BTPA reference. The earlier review record is historical, not the current exam authority. No private enrollment, entitlement, available attempt or customer agreement was inspected.

## Completed review rounds

| Round | Gap identified | Change |
|---|---|---|
| Exam orientation | Reading order did not distinguish essential decisions from specialist implementation depth. | Added a diagnostic reading route, essential-skill matrix, actual-enrollment boundary and current certification source. |
| Architecture choices | A product list could be mistaken for a mandatory stack. | Added required responsibilities versus conditional products, hard-constraint gates, alternatives and revisit triggers. |
| Commercial dependencies | Generic licensing cautions were insufficient for concrete choices. | Added subscription/consumption coexistence restrictions, classic Joule prerequisites, AI Core plan/deployment dependencies, model metering and task/API plan checks. |
| Interfaces and security | Readers needed to trace real callers and separate configuration on each side. | Added five paths, ERP communication artifacts, 202/412 meanings, delta polling, token validation and tenant/object checks. |
| Operating quality | Availability and scalability were mostly qualitative. | Added measurable illustrative NFRs, receiver limits, bounded queues, circuit breakers, configuration recovery and multi-region limitations. |
| Development evidence | Policy tests did not teach recovery after a remotely committed write. | Added a dependency-free simulated receiver/client drill with explicit idempotency and lookup contracts. |
| Recall and transfer | Existing cases needed adversarial follow-up. | Added two original oral rehearsals with four follow-up constraints and a concrete self-check without a readiness percentage. |
| Rendering and regression | New dense matrices and glossary entries could damage reading. | Preserved existing components and diagrams; verified links, headings, term ordering, mobile overflow, search and native disclosures. |

## Executed checks

- Existing supplier-review pure policy suite: **17 passed**, rerun locally from the supplied exercise.
- New recovery simulator: **11 passed**. Cases include normal confirmation, lost response after commit, blocking blind retry, reconciliation, duplicate input, conflicting payload, tenant-scoped keys, invalid input and delayed receipt visibility.
- New focused Python regression suite: **11 passed**, including all 45 legacy anchors, new topic targets, unique IDs, heading order, six parseable accessible SVGs, 140 sorted unique terms, valid example JSON and evidence boundaries. One regression executes the recovery simulator; these are not independent production test counts.
- Seven source-only checks from the reconciled architecture-review suite also passed. Its separate 18-test recovery-contract simulator was preserved but not rerun locally during this completion review.
- Focused Chromium preview: widths 320, 375, 768 and 1280 pixels had no document-level horizontal overflow. A 200% zoom check also passed.
- Glossary search for JWT returned the intended entry; clearing restored all 140 terms. Native disclosure interaction worked. No browser JavaScript errors were reported.
- Mobile table text remained 17px and wide tables used their explicit horizontal scroll region. Desktop and mobile reading screenshots were inspected.
- Refreshed the self-contained HTML reader and local practice ZIP. No source font files or private data are included.

## Reuse and delivery boundaries

No new renderer, diagram library or shared CSS component was introduced. The six original monochrome SVGs, registered study tables, reader layout and native question disclosures were retained. Existing deep links remain valid. Changes are limited to the handbook composer/includes, the new simulator, focused tests and this review record.

The simulator is an in-memory model of a receiver that explicitly supports deduplication and lookup. It is not an SAP API and does not prove database durability, cross-process locking, actual tenant isolation or a distributed transaction. Its approver string is audit data, not authentication. Real receiver capabilities must be verified separately.

CAP dependency installation, CDS compilation, CAP HTTP permissions, database concurrency, real identity integration, ERP communication arrangements and BTP deployment were not executed. No paid resources were provisioned. A passing local suite does not imply that these untested layers work.

The browser check uses the offline/focused rendering of the handbook, not the complete production Jekyll CSS cascade. Full local Jekyll/network-dependent validation was unavailable. GitHub CI and Pages deployment must be checked separately. Previously observed unrelated homepage/navigation/SEO regression failures were not changed or hidden.

Product documentation and example tests do not replace the selected exam's technical readiness and resource-use instructions, a signed license agreement, human publication review or real implementation experience.

## Reconciliation with concurrent work

Before publication, the branch advanced from `0153f5a` to `a4678fa`. The concurrent exam briefing, decision workbench, two-file recovery-contract example, its tests, review log and four source anchors are preserved. The briefing and workbench remain reachable as expandable supplementary material rather than duplicating the primary reading route. Equivalent certification corrections in the main practice/source records are retained. This completion review is stored separately from the concurrent review log.

The existing architecture-review tests are updated for the intentionally expanded 21 rendered sections and 140 terms. The canonical certification URL is checked in the expanded page instead of requiring repeated raw URLs in every include. No safety check or recovery test is removed.
