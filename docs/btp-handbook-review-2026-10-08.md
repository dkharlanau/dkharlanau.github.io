# BTP handbook editorial and implementation review

Review date: 2026-10-08. Canonical route: `/atlas/sap/sap-btp/`.

This record describes completed checks and remaining limits. It is not a human publication approval. The page remains `needs_verification`, `verified: false`, `noindex,follow`, with `sitemap: false`.

## Scope of the rewrite

The earlier page accumulated 45 lesson-shaped sections. The new composition has 18 chapters organized around decisions, with one synthetic external supplier-review case. The curriculum basis remains the supplied SAP Learning Business AI Platform 2610 and methodology extracts. Public SAP documentation adds qualifications where the course simplifies implementation, availability or licensing.

The new page contains six original monochrome SVG examples, 126 glossary entries, 24 native recall/case disclosures, and a local CAP teaching scaffold with 17 dependency-free domain-policy tests. These counts describe the material, not learner readiness.

## Review rounds

| Round | Question | Finding and change |
|---|---|---|
| Coverage | Could a reader design and cost the solution, not merely name products? | Added a full commercial-model and consumption chapter, service BOM versus SBOM distinction, stage/replica/runtime arithmetic, account mechanics and a practical development path. |
| Factual boundaries | Which statements could create a wrong delivery commitment? | Qualified free-plan transitions, entitlement versus authorization, managed-runtime responsibilities, CAP versus runtime language support, messaging QoS, identity offboarding, grounding and Data Retention Manager scope. |
| Architecture | Do all components have a responsibility and an explicit boundary? | Connected ERP ownership, external review, internal approval, integration, analytics, agent governance and recovery through the same case. Added counterexamples and alternatives. |
| Visual semantics | Does each line mean something precise? | Created a hierarchy, C4 container view, BPMN collaboration, UML sequence, typed relationship graph and methodology map. Each has a notation key and limitation. Fixed a C4 boundary label crossed by a connector and moved UML guard text away from lifelines. |
| Executable behavior | Can a small implementation fail safely in the taught cases? | Created a local scaffold with pure policy functions, CAP adapter, model, service definition, synthetic seed data and tests. All 17 policy tests passed. Generic HTTP permissions and database concurrency remain separate tests to perform. |
| Recall and transfer | Can the learner handle a changed condition? | Added worked-to-independent exercises, twelve challenge cases, an oral answer structure, an architecture artifact checklist and a searchable glossary. No guaranteed certification or fabricated project experience. |
| Rendering and regression | Does the authored composition remain readable and linkable? | Preserved all 45 previous chapter anchors, checked unique IDs and local references, parsed all six SVGs, tested focused browser layouts and added seven repository regression tests. |

## Coverage map

- Enterprise and solution roles; SAP EA Framework; RBA/RSA; capability, process and component distinctions -> chapters 1-3.
- Account hierarchy, environments, subscriptions, service instances, binding/key distinctions and multitenancy -> chapter 4.
- Trial, free tier, PAYG, CPEA/BTPEA, subscription terms, AI consumption and cost assumptions -> chapter 5.
- Clean core, three extension options, levels A-D, IDE/model/runtime/UX, Build, Joule Studio, mobile -> chapter 6.
- Integration Suite capabilities, event contracts, queues/topics, QoS, B2B, AIF, migration and recovery -> chapter 7.
- Identity, scopes, application/backend permissions, private connectivity and operational access controls -> chapter 8.
- Data vocabulary, products, HANA/Datasphere/SAC/MDG/MDI/BDC/BW/Databricks, semantics and source authority -> chapter 9.
- AI Core, Launchpad, generative AI hub, Joule patterns, RAG, models, MCP/A2A and evaluation -> chapter 10.
- Agent lifecycle, runtime enforcement, policy, organization and value -> chapter 11.
- CI/CD, transports, logs/audit, CIAS, scheduling, alerts, storage/retention, ALM and recovery -> chapter 12.
- Application Extension Methodology, DAAM, ISA-M and assessment request -> chapter 13.
- Original visual examples -> chapter 14; local development -> chapter 15; case practice -> chapter 16; glossary -> chapter 17; evidence -> chapter 18.

## Reuse and implementation choices

Read the existing UI catalog, registry, reader CSS and repository rules. Reused `research-canvas`, the Signavio reader, registered `study-table` and `page-faq` disclosure markup/CSS. Route-specific CSS is limited to handbook reading utilities, SVG scrolling, glossary filtering and source records; it does not introduce a second table skin.

Inspected `dkharlanau/visual-workbench` and `dkharlanau/process-as-code` READMEs. Their semantic modeling approach informed the separation of relationships from presentation. No sibling renderer was executed or copied. Small, static SVG teaching examples were chosen because the C4/BPMN/UML semantics and figure legends need explicit review; no new runtime graph library is needed. The plain relationship and methodology maps are not presented as formal BPMN or ArchiMate.

The canonical page is a short composer. Curated content resides in `_includes/btp-handbook/`. Existing deep anchors remain available. All essential content is server-rendered; JavaScript only filters the glossary and opens disclosures for printing.

## Executed checks

- Seven focused Python regression tests passed, including all previous anchors, source links, heading order, SVG parsing, example JSON and execution of the local policy scaffold.
- Seventeen Node.js domain-policy tests passed: acceptance/rejection, missing identity/role/request, assignment, evidence, repeated transitions and independent approval.
- JavaScript syntax checks passed for the glossary utility and scaffold.
- Focused Chromium preview checked at 320, 375, 768 and 1280 px: no document-level horizontal overflow. Wide figures/tables use explicit scroll containers.
- 200% CSS zoom in the focused desktop preview: no document-level horizontal overflow.
- Glossary search for `idempotency`: one matching entry; Clear restored all 126 entries. Native disclosure interaction worked.
- All six desktop figure screenshots were inspected; one mobile figure viewport was inspected. No copied SAP artwork or product icons were added.

## Explicit limits

The local browser fixture uses the live site's design-token values and shared component contracts. It is a focused preview, not the complete production Jekyll CSS cascade. A full local repository/Jekyll build could not be run because repository/network access from the working container was unavailable. GitHub repository access and publication use the connected GitHub tool.

CAP dependencies could not be installed in the isolated authoring runtime. CDS compilation, CAP HTTP authorization, database transaction/concurrency behavior, production identity integration, real ERP APIs and BTP deployment were not executed. The page and scaffold README state this. The policy tests prove only the pure rules they execute.

The previously observed repository CI failures involve older homepage/navigation/SEO expectations. They are not fixed or hidden by this content rewrite. Inspect the new commit's workflow results independently; structural checks are not proof of a successful Pages deployment.

The dedicated SAP certification page was checked on the review date: P_BTPA, one scenario-based assessment, two hours, 60% passing score. The candidate must verify the actual booking requirements. Course coverage and local exercise completion are not an official eligibility or readiness guarantee.
