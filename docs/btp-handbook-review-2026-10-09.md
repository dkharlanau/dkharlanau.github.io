# BTP handbook: architecture and exam-target review

Review date: 2026-10-09. Route: `/atlas/sap/sap-btp/`.
This is an editorial/implementation review record, not human publication approval.

## Main correction

The target is **C_BAIPA — SAP Certified – Solution Architect – SAP Business AI Platform**.
The current dedicated SAP page lists one scenario-based activity, two hours and a
60% pass score. The prior handbook's P_BTPA reference did not match this target.
Corrected the practice chapter, source register and new exam briefing. The older
2026-10-08 review document is a historical record, not the current exam reference.

Sources:
- https://learning.sap.com/certifications/sap-certified-solution-architect-sap-business-ai-platform
- https://learning.sap.com/helpcenter/certification-support/scenario-based-assessment-faqs
- https://learning.sap.com/helpcenter/certification-support/certification-practical-exam

## Review rounds and resulting changes

| Review lens | Finding | Implemented change |
|---|---|---|
| Curriculum and priorities | Broad product coverage did not tell a candidate what to explain first. | Added an essential/conditional skill map and a suggested revision route. This is not an official exam weighting. |
| Scope and trade-offs | Product descriptions did not make minimal composition sufficiently concrete. | Added required capabilities versus optional products, three initial alternatives and hard gates before scoring. |
| Integration | Readers needed to trace real boundaries rather than name middleware. | Added six request paths, a scoped SAP_COM_0008 example, communication setup and ETag/CSRF/idempotency distinctions. |
| Commercial constraints | The generic cost chapter needed plan-dependent examples. | Added consumption-flavor restrictions, AI Core extended-plan prerequisites, MCP/Task Center checks, dated promotion caution and synthetic usage arithmetic. |
| Operations and quality | RTO/RPO were defined, but acceptance criteria needed examples. | Added measurable workload, consistency, recovery, isolation, fallback and ownership requirements. Explicitly marked all proposed targets as synthetic. |
| Practical evidence | Lost-response recovery was explained but not executable. | Added a dependency-free fake-receiver exercise with 18 passing tests. It does not claim real ERP idempotency or production durability. |
| Readability and regressions | Avoid another pile of loosely connected lessons. | Kept the original chapters; added two focused sections, preserved all prior anchors, 126 glossary entries and six diagrams. |

## Scope and source handling

The supplied SAP Learning extracts remain the curriculum basis. The added decision
matrices, quality targets and recovery exercise are original teaching material.
Product documentation supplies the specific implementation/commercial qualifications.
The updated page has 20 chapters. No new CSS framework, diagram engine, icon set,
learning-score widget or commercial positioning was introduced.

Existing handbook source was recovered from the attached standalone reading edition
and verified against GitHub blob hashes before editing. The live composer and changed
includes were read/checked through the connected GitHub tool. The live branch was
checked before creating the commit. Unrelated homepage and SEO issues were not changed.

## Executed validation

- Eight focused Python regression tests passed: current certification reference,
  20 sections, legacy anchors, unique IDs, heading hierarchy, retained review status,
  six parseable accessible SVGs, glossary count and the new Node test suite.
- Eighteen recovery-contract tests passed on Node.js 22: valid confirmation,
  absent/expired/self approval, scope and payload checks, duplicate/concurrent
  submissions, lost reply after commit, unavailable lookup, business rejection,
  tenant-qualified keys and untrusted receipts.
- The prior attached CAP lab's 17 dependency-free policy tests passed again.
- System Chromium checked the standalone preview at 320, 375, 768 and 1280 pixels:
  no document-level horizontal overflow; glossary filtering and native disclosures
  worked. A 200% CSS zoom check also had no document-level overflow.
- Desktop workbench and mobile entry screenshots were inspected. No new diagram
  artwork was added; the existing BPMN/C4 examples were also visually reviewed.

## Important limits

The new receiver and ledger are in-memory teaching objects, not a production adapter,
validated SAP API, database transaction system or durable distributed service. Approval
fixtures are test data, not signed credentials; production code must load and enforce
trusted approval evidence itself. Single-process concurrency checks do not establish
multi-instance/database correctness. Recovery requires a supported real receiver
contract, authenticated scope and durable state.

CAP dependencies, CAP HTTP/database integration, actual ERP APIs, production identity,
BTP deployment and charged services were not executed. The browser checks use the
self-contained reading edition, not a full production Jekyll CSS cascade. Full-repository
CI and Pages deployment must be checked separately. No blocked network or package
installation is presented as a passed test.

The page remains `needs_verification`, `verified: false`, `noindex,follow` and
`sitemap: false`. No exam pass, official syllabus completeness, product availability
or five years of project experience is implied by the content or test counts.
