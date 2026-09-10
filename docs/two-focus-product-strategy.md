# Two-focus product strategy

Decision date: 2026-09-10. Owner direction: two audience outcomes, one SAP knowledge base. This supersedes the six-area model as homepage positioning, not as physical storage architecture. Read together with AGENTS.md, PROJECT_MAP.md and ARCHITECTURE.md.

## Decision

The site has two primary customer journeys:

1. **Learn SAP through practice**: independent study, interview preparation, assessment rehearsal and eventually paid learning packs.
2. **Improve SAP AMS**: reduce avoidable repeat work through evidence-led diagnosis, scoped technical/process improvements and controlled continuous improvement.

Knowledge, Labs, frameworks, datasets, AI tooling and the profile support those journeys. They are not six equal offers. Keep the existing logo. Do not put the author's name in a giant hero. Preserve established deep URLs and public knowledge; do not mass-move or delete content to simplify the menu.

Working positioning: **SAP learning and AMS optimization.** Supporting idea: **Build stronger SAP skills. Make support work better.** “Next-generation AMS” describes the method on the commercial pillar; it is not a substitute for naming the buyer's problem.

## Audiences and conversion boundaries

| Audience | Immediate job | Useful next action | Commercial hypothesis |
|---|---|---|---|
| Practising SAP consultant | Explain and defend a decision | Attempt a case, review, repeat | A bounded specialist pack may be worth paying for |
| Candidate preparing for a Lead assessment | Show cross-domain judgment | Complete a timed case and evidence-based self-review | Guided review may have more value than more reading |
| AMS/service owner | Identify expensive recurring work | Define one incident class and inspect a diagnostic output | A fixed-scope diagnostic is easier to assess than a full provider replacement |
| Internal SAP team or AMS delivery lead | Improve an existing operation | Implement and measure one prevention/control change | A recurring improvement engagement follows demonstrated value |

These are hypotheses, not validated customer research. No traffic, conversion, willingness-to-pay or revenue measurement was supplied for this decision. Do not claim market validation, keyword volumes or ROI.

## Content architecture and migration

English primary navigation: **Learn / Improve AMS / Library / About / Search**. Home presents only two primary choices. Frameworks and machine resources remain reachable from the secondary library area.

| Route | Role | Source |
|---|---|---|
| `/` | Two-goal audience router | `index.md`, `_includes/sections/home-focus.html` |
| `/learn/` | Learning entry point, not a second topic database | `learning/index.md` |
| `/learn/packs/bp-mdg-replication/` | First original synthetic practice preview | `learning/packs/bp-mdg-replication.md` |
| `/labs/interview-readiness/` | Existing interview preparation and local progress | Existing Lab source; unchanged |
| `/labs/assessment/` | Existing case assessment and attempt history | Existing Lab source; unchanged |
| `/services/sap-ams-consulting/` | Canonical AMS commercial pillar | Existing service path, rewritten in place |
| Existing specialist service routes | Data, integration and process depth | Retained; linked from the AMS pillar |
| `/knowledge/`, `/labs/`, `/frameworks/`, `/machine/` | Supporting reference/discovery infrastructure | Retained |

The new `learning/` source directory holds audience routing and original practice packaging only. It is justified by a distinct reader task, not an additional subject domain. Technical explanations remain canonical in existing Labs/Atlas. `_data/learning_packs.yml` holds catalogue metadata, not duplicated answers or an alternative progress engine.

Phase 1 changes English entry points only. Existing localized home templates and translations are preserved. Phase 2 must apply the same hierarchy and reviewed translations to the existing locales, keep language metadata and canonical/hreflang behavior intact, and clearly label English-only destinations. Do not silently replace translated text with English or report locale parity before testing it.

The full `/services/` catalogue remains as a compatibility/depth route; it is not the primary commercial entry from the new English header. A later consolidation may simplify it after checking inbound links and query ownership. Do not create competing “next-gen AMS” pillar URLs.

## Learning offer: sell practice, not a prettier content dump

Initial sequence:

1. BP / MDG replication and controlled mass-change reasoning.
2. SAP Lead interview and assessment decision practice.
3. AMS incident diagnosis and prevention.

Do not launch three paid packs at once. The implemented first preview contains **one** synthetic case; the full packs below are proposed scope, not available inventory.

A proposed full pack should include:
- one explicit outcome and prerequisite boundary;
- a concise explanation linked to canonical topic material;
- a useful system/decision map;
- a small set of progressively harder original cases;
- practice prompts followed by worked reasoning and counterexamples;
- a manual rubric that distinguishes recall from evidence, trade-offs and safety;
- a reusable checklist or worksheet;
- release/version applicability, provenance, limitations and review date.

Proposed flagship BP / MDG pack cases: selection/filter gaps; transport versus application success; mapping/identity ambiguity; update versus overwrite/blank semantics; concurrent changes and recovery scope; end-to-end reconciliation and business sign-off. Do not ship operational commands as universal fixes. Any release-specific technical content needs primary references and practitioner review.

The current preview uses a fictional 12/10/8-object case, collapsible review, a four-dimension 0–2 rubric and print rules. It collects no answers and does not write to existing Lab progress models. The print view is an exercise sheet, not a professionally typeset PDF product. No checkout, paid download, license change or certification claim is implemented.

A commercial progression to test: free sample → complete single-user pack → optional human review → team-use version with explicit licensing. Pricing is deliberately not published before feedback, fulfillment cost and payment feasibility are established. Public site content is not secret inventory; paid files cannot be protected by obscure URLs in this public repository. Future paid delivery needs an eligible provider/private storage and access control. Do not choose or activate payment, tax or merchant arrangements without checking actual eligibility and owner authorization.

## Commercial offer: improve the current support model

Position as a scoped improvement capability working with the client's internal team and existing provider, not as an invented 24/7 outsourcing company.

**Repeat-work diagnostic:** representative sanitized evidence → repeat-pattern register, ownership gaps, baseline, ranked prevention backlog → choose the next intervention.

**Reliability improvement:** one prioritized problem → explicit design, implementation responsibilities, checks, controlled rollout/recovery and runbook → accept or reject the change against a defined outcome.

**Continuous-improvement cycle:** owned backlog and baseline → regular review of recurrence, manual effort, controls and knowledge transfer → continue, revise or stop.

Relevant technical depth: BP/MDG and replication; integration recovery and reconciliation; order-to-cash exceptions; runbooks and operational memory. AI is a bounded assistive mechanism, not a third business line. Cloud ALM, Integration Suite, AIF, IDoc or CI/CD are selected according to the actual landscape, not added to every page for keyword coverage.

Continuous improvement and CI/CD are different concepts. The former is the operating loop; the latter can help control engineering changes. Keep approvals, authorization, secrets and production actions outside the public site. Existing monitoring capability is not authorization to write.

## Measurement and economic boundaries

Learning funnel hypothesis: relevant visit → practice start → completed attempt/self-review → return or explicit request for the complete pack. A link click is not a completed exercise. Start with a lightweight external-practitioner observation protocol before adding analytics; retain failed and abandoned attempts. Use no pasted answer text, personal case history or client material as analytics.

Commercial funnel hypothesis: relevant problem-page visit → artifact inspection → scoped problem conversation → accepted diagnostic → accepted improvement. Track actual counts and denominators when available; do not invent them.

AMS outcome definitions:
- repeat incidence for an agreed pattern per comparable business-volume denominator;
- manual recovery/verification labor, separate from elapsed wait time;
- median and tail recovery time with severity mix and timestamps defined;
- unresolved business exceptions after the agreed window;
- reopened incidents, escaped change defects and SLA regressions as guardrails.

Economic model: net recurring operating benefit = comparable avoided labor cost minus additional recurring tooling, maintenance and review cost. Keep one-off implementation cost separate for payback analysis. Avoid double counting incident handling and the same automation hours. Released internal capacity is not necessarily lower cash spend. Use matched workload and disclose changes in volume/mix; a before/after comparison alone is not causal proof.

No unsupported percentage savings, customer outcomes, service-level commitments or external-validation badges.

## Search intent ownership

These are initial query families to validate, not measured keyword opportunities:

| Intent | Owning destination | Content job |
|---|---|---|
| SAP MDG / BP interview questions, DRF interview scenarios | Learning pack and existing topic references | Original applied question with reasoning, limits and sources |
| SAP Lead assessment preparation | Existing assessment + learning route | Show an actual exercise and what it assesses |
| SAP AMS optimization / reduce recurring SAP incidents | Existing AMS service pillar | Name buyer problem, input, output, boundaries and next action |
| SAP integration reliability assessment | Existing integration service | Describe one bounded diagnostic and supporting evidence |
| SAP master-data stability / replication assessment | Existing master-data service | Explain scope, traceability and acceptance |

One intent, one preferred destination. Informational pages remain useful without buying. Add only a relevant contextual CTA, not a sitewide sales block. Use existing indexing and AI-artifact generators; never manufacture review status to gain visibility. New learning pages remain `verified: false`, `noindex,follow`, `sitemap: false` until human review.

SAP's current certification materials emphasize practical, scenario/system-based assessment. This supports the relevance of applied practice but does not prove demand for this specific paid product. Do not imply SAP endorsement or reproduce live exam content.

## Visual and editorial contract

Reuse the current brand, logo, type family and site primitives. The added `site-focus.css` is scoped to `.focus-page`; no global style reset, external dependency, animation framework or new navigation runtime. Keep a readable 60–75-character text measure, moderate-weight headings, visible focus and a single-column mobile layout.

A pack visual must explain something: system boundaries, object/message chronology, decision points or failure/recovery states. Avoid robot stock art, decorative network graphs and large unrelated illustrations. Future pack covers may have a consistent accent and one meaningful diagram, but do not substitute illustrations for an exercise or claim visual approval without screenshots. This batch adds no generated image assets.

A study page follows outcome → case → attempt → review → rubric → next practice. A service page follows problem → fit → deliverables → method → measurement → evidence → scoped contact. Keep the audiences separate; do not turn every learning page into a consulting advert.

## Execution queue and exit criteria

### P0 — integration and review of this foundation
- Inspect the exact candidate diff and preserve concurrent work.
- Run source/unit checks, deterministic state generation, Jekyll build, links, SEO/indexing, structured data, accessibility and visual smoke on the final SHA.
- Inspect homepage, learning hub, sample pack and AMS pillar at mobile and desktop widths, plus shared-header regressions on profile/library/localized pages.
- Complete human technical review of the new preview before index promotion. Broad permission to edit is not evidence of a human content review.
- Keep a candidate off main if required checks are incomplete or failing. No workflow or deployment gate is weakened.

### P1 — prove one full learning pack
Have a small independent practitioner group attempt the preview unaided; record completion, misunderstood steps, corrections, usefulness and explicit willingness to pay. This is a proposed research protocol, not completed research. Revise before expanding the case set. Reuse #329 for assessment-generation work and #380 for system-level visual quality; do not duplicate those queues.

### P1 — prove one commercial diagnostic
Prepare one synthetic, clearly labeled diagnostic deliverable using the same method as the service offer, then test comprehension with a potential buyer or AMS lead. Do not treat a consultant training exercise as buyer validation. Reuse #331 for evidence-to-service alignment and #392 for reviewed diagnostic-to-workflow links.

### P1 — localization and service catalogue alignment
Apply the reviewed two-goal hierarchy to existing locales; route untranslated material transparently. Reconcile the wider services catalogue and machine-facing positioning through their canonical sources and generators. Do not remove old routes.

### P2 — monetization and automation
Only after product and buyer evidence: assess payment eligibility/fulfillment, versioned private paid assets, licensing, support burden and a small pilot. For privacy-safe usage measurement reuse the principles in #387. Connector distribution remains in #386/#385; it is not a prerequisite for the first learning pack or AMS diagnostic.

Reversal conditions: readers cannot distinguish the two paths; the preview does not help them complete a real practice task; buyers cannot recognize a bounded deliverable; or packaging costs exceed demonstrated demand. Simplify or change the chosen wedge rather than generate more pages.

## Sources checked 2026-09-10

- SAP Certification practical exams: https://learning.sap.com/helpcenter/certification-support/certification-practical-exam
- SAP Learning Q2 2026 release notes: https://learning.sap.com/release-notes/q2-2026
- SAP Cloud ALM operations APIs: https://support.sap.com/en/alm/sap-cloud-alm/operations/expert-portal/calm-apis-for-operations.html
- SAP Automation Pilot: https://www.sap.com/products/technology-platform/automation-pilot.html
- SAP BP replication using ALE: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/287a3851fd167062e10000000a44538d.html
- SAP BP replication using SOA: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/74b0b157c81944ffaac6ebc07245b9dc/5efcb922c8e9408095bf900611f6cfdd.html

Repository evidence: AGENTS.md, PROJECT_MAP.md, ARCHITECTURE.md, homepage/header sources, existing AMS service, CI, Repository State Sync, open issues #329/#331/#380/#384–#387/#391–#392 and the inspected dkharlanau/prompts Deep Run contract.

Execution caveat: AGENTS.md points to `docs/content/author-editorial-profile.md`, `docs/templates/README.md` and `docs/site-content-design-contract.md`; these exact reads returned 404 during this run. Follow the available editorial/safety rules in AGENTS.md and resolve the stale references before expanding article production. Do not silently claim those documents were read.

Do not dispatch Repository State Sync on a candidate branch: its inspected workflow pushes to `HEAD:main`. Use the existing PR validation path for candidate verification. Repository source remains public even when the candidate has not been deployed.
