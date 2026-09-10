# Two-focus product strategy

Decision date: 2026-09-10. Owner direction: two audience outcomes, one SAP knowledge base. This supersedes the old six-area model as homepage positioning, not as physical storage architecture. Read together with AGENTS.md, PROJECT_MAP.md and ARCHITECTURE.md.

## Decision

The site has two primary customer journeys:

1. **Learn SAP through practice**: topic refresh, interview preparation, assessment rehearsal and focused practice packs.
2. **Improve SAP AMS**: reduce avoidable repeat work through evidence-led diagnosis, bounded technical/process improvements and controlled continuous improvement.

Knowledge, Labs, frameworks, datasets, AI tooling and the profile support those journeys. They are infrastructure and evidence, not six equal homepage offers. Keep the existing logo. Do not put the author's name in a giant hero. Preserve established deep URLs and public knowledge; do not mass-move or delete content to simplify the menu.

Working positioning: **SAP learning and AMS optimization.** Supporting idea: **Build stronger SAP skills. Make support work better.** “Next-generation AMS” describes the commercial method: support should systematically reduce the reasons support is needed. It is not a substitute for naming the buyer's problem.

## Product architecture

English primary navigation: **Learn / Improve AMS / Library / About / Search**. English entry points only are changed in phase 1; existing localized home templates and translations remain intact until reviewed localization work is done.

The physical repository still has the established six product areas. `learning/` is an audience and practice-pack packaging layer over existing canonical knowledge and Labs, not a seventh independent knowledge base. The content-quality policy now recognizes `learning/index.md` as a landing page and `learning/packs/` as `learning_pack` content so future publication follows the same review, indexing and retrieval controls as the rest of the site.

| Route | Product job | Source of truth |
|---|---|---|
| `/` | Two-goal audience router | `index.md`, `_includes/sections/home-focus.html` |
| `/learn/` | Learning entry point | `learning/index.md` |
| `/learn/packs/bp-mdg-replication/` | Original synthetic practice product | `learning/packs/bp-mdg-replication.md` |
| `/labs/interview-readiness/` | Interview preparation and browser-local progress | Existing Lab source |
| `/labs/assessment/` | Assessment practice and attempt history | Existing Lab source |
| `/services/sap-ams-consulting/` | Canonical AMS commercial pillar | Existing service path, rewritten in place |
| Existing specialist services | Integration, master-data and process depth | Existing service sources |
| `/knowledge/`, `/labs/`, `/frameworks/`, `/machine/` | Supporting knowledge and infrastructure | Existing canonical products |

Do not create competing “next-gen AMS” pillar URLs. The wider `/services/` route remains a compatibility and depth catalogue. Technical explanations stay in Atlas/Labs; learning packs link to them rather than copying them.

## Shared reasoning method

The two journeys share a method but not a commercial promise:

**Problem → Evidence → Decision → Change → Verify**

For learning, the method becomes a case that the learner must solve before reading the review. For AMS, it becomes a bounded diagnostic or improvement with ownership, recovery and acceptance criteria. A training case is never customer evidence.

## Learning product

### Value proposition

Do not compete by producing another broad SAP textbook. The product is applied reasoning under incomplete evidence: distinguish facts from hypotheses, select discriminating checks, explain trade-offs, define a safe action and verify the business result.

Topic refresh, interview practice and assessment practice are different jobs:

- **Refresh:** understand process, data, integration and constraints using canonical knowledge.
- **Interview:** explain a decision and a real project role clearly.
- **Assessment:** commit to a decision under constraints and review the reasoning.
- **Practice pack:** combine a small system map, original cases, worked review, counterexamples and a reusable decision aid.

### Implemented pilot: BP / MDG Replication — Evidence to Recovery

The current free pilot is version 0.2.0 and contains five synthetic cases:

1. **Selection gap** — intended objects do not all appear in supplied outbound evidence.
2. **Application gap** — transport succeeds while target business state remains unresolved.
3. **Blank semantics** — clear, empty and omitted values cannot be assumed equivalent.
4. **Concurrent change** — timestamps support chronology but do not define field authority.
5. **Recovery design** — different exception classes require different evidence and recovery decisions.

The pack uses the reusable response shape **Facts → Unknowns → Hypotheses → Discriminating checks → Decision → Owner → Verification**. It includes a five-dimension self-review rubric and a reusable replication decision worksheet.

All counts, values and circumstances are invented. The pack is `needs_verification`, `verified: false`, `noindex,follow`, `sitemap: false` and must remain outside retrieval/index promotion until human review. It collects no answers and does not write to Interview Readiness or Assessment progress. There is no validated pass threshold.

### Pack quality contract

A future pack should contain:

- one explicit outcome and prerequisite boundary;
- a small explanatory system or decision map;
- progressively harder original cases;
- an attempt before the worked reasoning is visible;
- counterexamples and recovery/safety boundaries;
- a rubric that distinguishes recall from evidence and judgment;
- a reusable worksheet or checklist;
- applicability, provenance, limitations and review status.

The useful artifact is the improved second attempt, not a decorative PDF or an inflated score.

### Commercial ladder

Hypothesis to test: **free pilot → complete single-user pack → optional human review → team-use version with explicit licensing.**

No checkout, paid download, pricing, private-file fulfillment or certification claim is implemented. Public repository URLs are not access control. Payment, tax, merchant eligibility, private storage and support burden must be validated before a paid offer is activated.

## Commercial product: next-generation SAP AMS

Position as an improvement capability working with the client's internal team and existing provider, not as an invented 24/7 outsourcing company.

### Offer 1 — Repeat-work diagnostic

Representative sanitized evidence, recovery effort, business volume and current ownership are used to produce a repeat-pattern register, evidence gaps, baseline and ranked prevention backlog. The buyer decision is which problem is worth fixing first, including the option not to automate.

### Offer 2 — Reliability improvement

One prioritized pattern becomes an explicit design, implementation responsibility map, tests, controlled rollout/recovery plan, runbook and acceptance evidence. Development and platform work are scoped; they are not implied as unlimited delivery.

### Offer 3 — Continuous-improvement cycle

An owned backlog and baseline become a recurring review of recurrence, manual effort, control coverage, knowledge transfer and observed results. Continue, revise or stop an intervention according to demonstrated benefit and risk.

Relevant depth includes BP/MDG and replication, integration recovery/reconciliation, O2C exceptions, runbooks and operational memory. AI is a bounded assistive mechanism, not a third business line or an autonomous production owner.

### Implemented buyer-facing example

The AMS pillar now contains an **illustrative diagnostic output** for a synthetic BP-replication incident class. It demonstrates the deliverable structure without inventing a customer result:

- business outcome;
- repeat pattern;
- evidence gap;
- recovery boundary;
- candidate control;
- acceptance measure;
- guardrails.

The example deliberately recommends exception partitioning and intended-versus-target reconciliation before automated recovery. It is a comprehension artifact for a buyer, not evidence that a client achieved a particular saving.

## Measurement and economics

Learning funnel hypothesis: relevant visit → practice start → completed attempt/self-review → improved second attempt → return or explicit request for more. A link click is not a completed exercise. External practitioner observation should record confusion, corrections, usefulness and willingness to pay without collecting client data.

Commercial funnel hypothesis: problem-page visit → diagnostic artifact inspection → scoped problem conversation → accepted diagnostic → accepted improvement. Track actual counts and denominators only when available.

AMS outcome definitions:

- repeat incidence for an agreed pattern per comparable business-volume denominator;
- manual recovery and verification labor, separate from elapsed waiting time;
- median and tail recovery time with start/end and severity mix defined;
- unresolved business exceptions after the agreed observation window;
- reopens, escaped change defects, unexpected overwrites/duplicates and SLA regressions as guardrails.

Released internal capacity and cash savings are different outcomes. Net recurring operating benefit must account for recurring tooling, maintenance and review; one-off implementation cost stays separate for payback analysis. Do not double count the same avoided hour. A before/after reduction caused by lower business volume is not automatically an improvement.

No unsupported percentage savings, customer outcomes, service-level commitments or external-validation badges.

## Search intent ownership

These are hypotheses to validate, not keyword-volume claims.

| Search / reader intent | Owning destination | Content job |
|---|---|---|
| SAP MDG / BP interview and replication scenarios | Learning pack + canonical references | Applied cases with reasoning, limits and sources |
| SAP Lead assessment preparation | Assessment + learning route | Show what the learner must actually decide |
| SAP AMS optimization / recurring SAP incidents | AMS service pillar | Name the problem, scope, output, evidence and next action |
| SAP integration reliability | Existing integration service | One bounded diagnostic and evidence chain |
| SAP master-data stability / replication | Existing master-data service | Scope, traceability, target-state acceptance |

One intent should have one preferred destination. Informational content remains useful without buying. Add contextual CTAs rather than turning every page into sales copy. Use the existing indexing and AI-artifact generators; never manufacture review status to gain visibility.

## Visual and editorial contract

Keep the current logo, type system and global theme. The two-focus design is intentionally scoped under `.focus-page`; no global CSS reset, animation framework or external runtime is introduced.

Use restrained bright accents to distinguish Learn and AMS, moderate-weight headings and generous reading space. Visuals must explain something: an evidence chain, decision sequence, exception class, system boundary or recovery state. Avoid decorative robot art, generic network diagrams and large hero clutter.

The implemented UI primitives are semantic HTML/CSS rather than raster illustrations: evidence/process strips, case navigation, proof cards, diagnostic sheets and mobile/print layouts. Generated image assets can be added later only when they improve comprehension and pass visual review.

Learning pages follow **outcome → map → attempt → review → transfer**. Commercial pages follow **problem → fit → deliverables → method → diagnostic example → measurement → evidence → scoped contact**.

## Execution and validation gates

### P0 — current Deep Run

Implemented in the candidate branch:

- two-goal English homepage and navigation;
- `/learn/` product entry point;
- five-case BP/MDG free pilot pack;
- buyer-facing synthetic AMS diagnostic example;
- scoped visual system for the two journeys;
- learning content-model integration with the quality pipeline.

Required before merge: exact-SHA Python tests, deterministic state materialization, Jekyll build, rendered checks, visual smoke, content-quality changed-content gate, links, SEO, indexing, sitemap, accessibility, AI endpoints, Atlas artifact freshness and assessment readiness. A successful source test or build must not be described as complete validation when later gates did not run.

New learning content remains unverified/noindex after merge until a separate human technical review. Broad authorization to edit does not constitute that review.

### P1 — evidence from humans, not more inventory

Have independent practitioners attempt the pilot without guidance. Record whether they complete the cases, where the wording or evidence model fails, what changes between first and second attempt, and whether they explicitly want the full product. Reuse #329 for assessment-generation work and #380 for broader visual-quality work rather than creating parallel queues.

Show the synthetic diagnostic deliverable to potential buyers or AMS leads. Test whether they understand the scope, output and next decision without a verbal explanation. Reuse #331 for evidence-to-service alignment and #392 for reviewed diagnostic-to-workflow links.

### P1 — localization and catalogue alignment

Apply the reviewed two-goal hierarchy to existing locales without replacing translated content with English. Reconcile the wider services catalogue after checking inbound links and intent ownership. Do not remove established deep URLs.

### P2 — monetization and automation

Only after learning and buyer evidence: evaluate payment/fulfillment eligibility, versioned private paid assets, licensing, support burden and a small pilot. Reuse privacy-safe measurement principles from #387. Connector distribution is not a prerequisite for either first product.

Reversal conditions: readers cannot distinguish the two paths; practitioners do not improve after using the pack; buyers cannot recognize a bounded deliverable; or packaging/fulfillment cost exceeds demonstrated demand. Change the wedge rather than generate more pages.

## Safety and repository boundaries

Everything committed here is public. Do not publish client names, ticket identifiers, private source material, credentials, raw logs or internal paths. Training and diagnostic samples must remain synthetic. Do not weaken existing CI, indexing or verification gates.

Do not dispatch Repository State Sync on a candidate branch: the inspected workflow pushes generated state to `main`. Use the normal PR CI path for candidate verification.

## Sources and repository evidence

Public SAP references used by the current pilot/service were checked on 2026-09-10 and are linked from the relevant pages, including SAP Help for Business Partner replication using ALE and SOA, SAP Cloud ALM operations APIs and SAP Automation Pilot.

Repository evidence: AGENTS.md, PROJECT_MAP.md, ARCHITECTURE.md, homepage/header sources, service sources, quality pipeline, CI, Repository State Sync and existing issues including #329, #331, #380, #387 and #392.

Execution caveat carried from the foundation run: AGENTS.md references editorial/template paths that were unavailable at their documented locations. Do not claim those sources were read until their paths are repaired or replaced.
