---
layout: default
title: "Tool Roadmap — Portable Enterprise Tools"
description: "Canonical roadmap for product-level tools around mappings, processes, interfaces, reconciliation, transformation graphs, cutover, evidence, and enterprise data."
permalink: /labs/tool-roadmap/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-25
hide_global_cta: true
tags:
  - enterprise-tools
  - sap
  - mapping
  - process-modeling
  - integration
  - data
  - roadmap
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li aria-current="page">Tool Roadmap</li></ol>
</nav>

<style>
.tool-roadmap-page .tool-roadmap-table-scroll {
  width: 100%;
  margin-top: 1.6rem;
  overflow-x: auto;
  border-top: 1px solid var(--rc-ink);
  border-bottom: 1px solid var(--rc-line);
  -webkit-overflow-scrolling: touch;
  scrollbar-gutter: stable;
}
.tool-roadmap-page .tool-roadmap-table-scroll table {
  width: 100%;
  min-width: 54rem;
  margin: 0;
  border: 0;
  border-collapse: separate;
  border-spacing: 0;
  background: var(--rc-paper);
  font-size: .82rem;
}
.tool-roadmap-page #roadmap .tool-roadmap-table-scroll table { min-width: 118rem; }
.tool-roadmap-page .tool-roadmap-table-scroll :is(th, td) {
  padding: .82rem .9rem;
  border: 0;
  border-bottom: 1px solid var(--rc-line);
  color: var(--rc-soft);
  line-height: 1.45;
  text-align: left;
  vertical-align: top;
}
.tool-roadmap-page .tool-roadmap-table-scroll thead th {
  color: var(--rc-ink);
  background: color-mix(in srgb, var(--rc-paper) 92%, var(--rc-line));
  font-family: var(--ps-mono);
  font-size: .64rem;
  font-weight: 760;
  letter-spacing: .035em;
  text-transform: uppercase;
  white-space: nowrap;
}
.tool-roadmap-page .tool-roadmap-table-scroll tbody tr:hover td {
  background: color-mix(in srgb, var(--rc-signal) 4%, var(--rc-paper));
}
.tool-roadmap-page #roadmap .tool-roadmap-table-scroll :is(th, td):first-child {
  position: sticky;
  left: 0;
  z-index: 2;
  width: 3.2rem;
  min-width: 3.2rem;
  background: var(--rc-paper);
}
.tool-roadmap-page #roadmap .tool-roadmap-table-scroll :is(th, td):nth-child(2) {
  position: sticky;
  left: 3.2rem;
  z-index: 2;
  min-width: 13rem;
  background: var(--rc-paper);
}
.tool-roadmap-page #roadmap .tool-roadmap-table-scroll thead :is(th, td):first-child,
.tool-roadmap-page #roadmap .tool-roadmap-table-scroll thead :is(th, td):nth-child(2) {
  z-index: 3;
  background: color-mix(in srgb, var(--rc-paper) 92%, var(--rc-line));
}
.tool-roadmap-page #roadmap .tool-roadmap-table-scroll td:nth-child(3) { min-width: 19rem; }
.tool-roadmap-page #roadmap .tool-roadmap-table-scroll td:nth-child(4) { min-width: 20rem; }
.tool-roadmap-page #roadmap .tool-roadmap-table-scroll td:nth-child(5) { min-width: 18rem; }
.tool-roadmap-page #roadmap .tool-roadmap-table-scroll td:nth-child(10) { min-width: 12rem; }
.tool-roadmap-page #roadmap .tool-roadmap-table-scroll td:nth-child(13) { min-width: 20rem; }
.tool-roadmap-page .tool-roadmap-table-scroll code { white-space: nowrap; font-size: .78rem; }
.tool-roadmap-page .tool-roadmap-model {
  margin: 1.5rem 0;
  overflow-x: auto;
  border: 1px solid var(--rc-line);
  background: color-mix(in srgb, var(--rc-paper) 92%, var(--rc-line));
  padding: 1rem 1.1rem;
  color: var(--rc-ink);
  font-family: var(--ps-mono);
  font-size: .82rem;
  line-height: 1.45;
}
.tool-roadmap-page .research-canvas__inventory > h2 { margin-bottom: 1rem; }
.tool-roadmap-page .research-canvas__inventory > h3 { margin-top: 2.5rem; }
.tool-roadmap-page .research-canvas__inventory > p { max-width: 58rem; color: var(--rc-soft); line-height: 1.62; }
@media (max-width: 800px) {
  .tool-roadmap-page .tool-roadmap-table-scroll { margin-top: 1.2rem; }
  .tool-roadmap-page #roadmap .tool-roadmap-table-scroll table { min-width: 104rem; }
  .tool-roadmap-page .tool-roadmap-table-scroll :is(th, td) { padding: .72rem .75rem; }
}
</style>

<div class="research-canvas tool-roadmap-page">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Lab / Product roadmap</p>
      <h1>Build portable models<br />around enterprise change.</h1>
      <p>This roadmap focuses on tools that remain useful even when SAP products improve. The target is project knowledge that companies still own themselves: mappings, process variants, interfaces, cross-system relationships, reconciliation rules, change impact, cutover dependencies, decisions, tests, and evidence.</p>
      <a class="research-canvas__button" href="#roadmap">Open the roadmap <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Roadmap principles">
      <p>Selection rule</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Portable</strong><small>Git, files, open formats</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Cross-system</strong><small>Not owned by one ERP</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Compounding</strong><small>Each artifact strengthens the model</small></div>
      <em>Prefer tools that can export to SAP, Signavio, LeanIX, ALM, Jira, or agent systems rather than trying to replace them.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal aria-label="Product boundary">
    <span class="material-symbols-outlined" aria-hidden="true">account_tree</span>
    <p><strong>Product rule:</strong> a roadmap row must represent a product or durable capability family, not a single spreadsheet check.</p>
    <p><strong>SAP-proof rule:</strong> prioritize project-owned models and cross-system artifacts that SAP cannot fully own because they include non-SAP systems, business decisions, project context, local rules, and evidence.</p>
    <p><strong>Implementation rule:</strong> repository creation and product implementation are tracked separately. A repository may exist while the product remains unimplemented.</p>
    <p><strong>Naming rule:</strong> use literal engineering/category names. Avoid Doctor, Guard, Copilot, Assistant, Workbench, Explorer, Navigator, Studio, Smart, or AI-powered.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <h2>Strategic model</h2>
    <p>The strongest long-term direction is an <strong>Enterprise Transformation Model</strong>: an open, versionable representation of how processes, systems, data, mappings, interfaces, decisions, tests, changes, owners, and evidence relate to each other.</p>

<pre class="tool-roadmap-model">Process ── Step ── System
   │         │        │
   │         ├──── Data ── Mapping
   │         │        │       │
   │         └──── Interface ─┘
   │                  │
Decision ─────────── Test
   │                  │
   └──────── Change ──┘
              │
           Evidence</pre>

    <p>Individual products can share this model without becoming one monolithic application.</p>
    <h3>Product families and repository status</h3>
    <div class="tool-roadmap-table-scroll" role="region" aria-label="Product families" tabindex="0">
{% capture product_families_table %}
| Product family | Primary purpose | Repository | Repo created? | Implementation |
|---|---|---|:---:|---|
| **Mapping as Code** | Versionable source-to-target mappings, validation, lineage, tests and export | [mapping-as-code](https://github.com/dkharlanau/mapping-as-code) | **Yes** | Not started |
| **Transformation Graph** | Project-scoped visual graph across processes, systems, data, interfaces, mappings and tests | [transformation-graph](https://github.com/dkharlanau/transformation-graph) | **Yes** | Not started |
| **Interface as Code** | Versionable interface contracts with mapping, retry, monitoring, ownership and tests | [interface-as-code](https://github.com/dkharlanau/interface-as-code) | **Yes** | Not started |
| **Reconciliation as Code** | Repeatable cross-system reconciliation rules and evidence | [reconciliation-as-code](https://github.com/dkharlanau/reconciliation-as-code) | **Yes** | Not started |
| **Process as Code** | Structured process definitions with visual/BPMN/Markdown exports | [process-as-code](https://github.com/dkharlanau/process-as-code) | **Yes** | Not started |
| **Enterprise Change Graph** | Model-backed enterprise change impact and regression scope | [enterprise-change-graph](https://github.com/dkharlanau/enterprise-change-graph) | **Yes** | Not started |
| **Decision Tables as Code** | Versionable business decision tables, validation, tests and DMN export | [decision-tables-as-code](https://github.com/dkharlanau/decision-tables-as-code) | **Yes** | Not started |
| **Data Relationship Map** | Visualize cross-system business objects, IDs and relationships from files | [data-relationship-map](https://github.com/dkharlanau/data-relationship-map) | **Yes** | Not started |
| **Cutover Graph** | Dependency, wave, blocker, evidence and readiness model for cutover | [cutover-graph](https://github.com/dkharlanau/cutover-graph) | **Yes** | Not started |
| **Project Evidence Graph** | Trace requirements, decisions, mappings, tests, defects and evidence | [project-evidence-graph](https://github.com/dkharlanau/project-evidence-graph) | **Yes** | Not started |
| `dkharlanau.github.io` | Research, domain models, reference datasets, prototypes and interactive concepts | [dkharlanau.github.io](https://github.com/dkharlanau/dkharlanau.github.io) | **Yes** | Active foundation |
{% endcapture %}
{{ product_families_table | markdownify }}
    </div>
    <p><strong>Repository status checked on 2026-08-25.</strong> All ten planned product repositories exist and are public. At check time GitHub reported repository size <code>0</code> for all ten, so product implementation is still recorded as <code>Not started</code>.</p>
  </section>

  <section class="research-canvas__inventory" id="roadmap" data-reveal>
    <h2>Canonical product roadmap</h2>
    <p>The first two columns stay visible while the full roadmap scrolls horizontally. Repository creation and implementation remain separate status fields.</p>
    <div class="tool-roadmap-table-scroll" role="region" aria-label="Canonical product roadmap" tabindex="0">
{% capture product_roadmap_table %}
| # | Product | Business / consultant problem | First useful scope | Growth path | SAP-proof | Codex fit | Score | Status | Intended repo | Repo created? | Implementation | Comments |
|---:|---|---|---|---|:---:|:---:|---:|---|---|:---:|---|---|
| 1 | **Mapping as Code** | Mapping logic is scattered across Excel versions, comments, emails and project folders; changes are hard to review and test | Import Excel mapping → canonical YAML/JSON → validate coverage/conflicts → diff releases → visual source→rule→target lineage | Mapping contracts, value maps, generated tests, impact analysis, approvals, OpenLineage export, agent context | **5/5** | **5/5** | **100** | `NEXT` | [mapping-as-code](https://github.com/dkharlanau/mapping-as-code) | **Yes** | Not started | Public repo created; currently empty. RDP already provides mapping coverage, cardinality, normalization and exception concepts. |
| 2 | **Transformation Graph** | Project knowledge about processes, systems, data, interfaces, mappings, owners and tests is fragmented across many artifacts | Load structured CSV/Excel/YAML and build an interactive project graph with filters and dependency traversal | Change impact, architecture views, migration scope, ownership, test coverage, exports to other tools, graph API | **5/5** | **5/5** | **99** | `NEXT` | [transformation-graph](https://github.com/dkharlanau/transformation-graph) | **Yes** | Not started | Public repo created; currently empty. Site SAP Enterprise, RDP, Decision Design and machine-layer structures can seed the model. |
| 3 | **Interface as Code** | Interface specifications are split between mapping sheets, Confluence, diagrams, Jira, emails and operational notes | One versioned interface contract describing source/target, trigger, schema, mapping, retry, idempotency, monitoring, ownership and reconciliation | Generate interface specs, sequence/data-flow diagrams, test cases, runbook skeletons, change diffs, agent context | **5/5** | **5/5** | **98** | `NEXT` | [interface-as-code](https://github.com/dkharlanau/interface-as-code) | **Yes** | Not started | Public repo created; currently empty. Operational Templates already define many review dimensions. Start vendor-neutral; add SAP profiles later. |
| 4 | **Reconciliation as Code** | Every migration/cutover/project creates one-off Excel/Python reconciliation logic that is difficult to repeat or audit | YAML reconciliation spec + source/target files → coverage, field checks, control totals, exceptions and evidence report | Multi-system reconciliation, scheduled runs, signed manifests, historical runs, cutover evidence, CI quality gates | **5/5** | **5/5** | **97** | `NEXT` | [reconciliation-as-code](https://github.com/dkharlanau/reconciliation-as-code) | **Yes** | Not started | Public repo created; currently empty. RDP already describes reconciliation, control totals, evidence and exception policies. |
| 5 | **Process as Code** | Business processes are maintained as diagrams that are hard to diff, generate, reuse and connect to data/interfaces/tests | Structured YAML/Markdown/Excel process definition → visual process map + Mermaid/BPMN/Markdown export | Process variants, RACI, systems/data/interfaces per step, version diff, Signavio export, test skeletons | **4.5/5** | **5/5** | **96** | `QUEUE` | [process-as-code](https://github.com/dkharlanau/process-as-code) | **Yes** | Not started | Public repo created; currently empty. BPMN/Signavio should be export targets; Git-friendly text remains the source. |
| 6 | **Enterprise Change Graph** | Change impact is usually assessed manually and misses downstream process/data/interface/test dependencies | Select or define a change and calculate impacted graph nodes: processes, systems, data, mappings, interfaces, tests and owners | Regression scope, risk scoring, change history, release comparison, approval evidence, Jira/ALM export | **5/5** | **5/5** | **96** | `QUEUE` | [enterprise-change-graph](https://github.com/dkharlanau/enterprise-change-graph) | **Yes** | Not started | Public repo created; currently empty. Reuse Transformation Graph model rather than creating a second incompatible graph schema. |
| 7 | **Decision Tables as Code** | Business rules often live in Excel with overlapping conditions, missing combinations and no executable tests | Import decision table → canonical model → detect overlaps/gaps/conflicts → diff → generate test cases | DMN export, simulation, coverage analysis, rule lineage, approvals, connection to processes and interfaces | **5/5** | **5/5** | **94** | `QUEUE` | [decision-tables-as-code](https://github.com/dkharlanau/decision-tables-as-code) | **Yes** | Not started | Public repo created; currently empty. Keep it a rule specification/validation layer, not an SAP rule engine. |
| 8 | **Data Relationship Map** | Consultants need to understand how customer/material/vendor IDs and relationships line up across systems | Load 2–5 extracts/crosswalks → interactive object/ID relationship graph → missing/ambiguous/broken links | Semantic object profiles, master-data lineage, reconciliation, graph queries, reusable entity contracts | **5/5** | **5/5** | **94** | `QUEUE` | [data-relationship-map](https://github.com/dkharlanau/data-relationship-map) | **Yes** | Not started | Public repo created; currently empty. Natural home for cross-system ID registry and business-object relationship views. |
| 9 | **Cutover Graph** | Cutover plans are spreadsheet task lists with hidden dependencies, unclear critical paths and weak evidence | Tasks/objects/dependencies → DAG → waves → blockers → owners → readiness/evidence checkpoints | Scenario simulation, go/no-go, rollback dependencies, hypercare handoff, run history, sign-off evidence | **4.5/5** | **5/5** | **93** | `QUEUE` | [cutover-graph](https://github.com/dkharlanau/cutover-graph) | **Yes** | Not started | Public repo created; currently empty. Existing Cutover/Hypercare protocol can define evidence and control semantics. |
| 10 | **Project Evidence Graph** | Requirements, decisions, mappings, tests, defects and approvals lose their relationships over a long project | Import project artifacts/IDs and show requirement→decision→mapping→test→defect→evidence trace | Coverage gaps, stale decisions, audit trail, release evidence, AI context, ALM/Jira connectors | **5/5** | **4.5/5** | **92** | `QUEUE` | [project-evidence-graph](https://github.com/dkharlanau/project-evidence-graph) | **Yes** | Not started | Public repo created; currently empty. Potential traceability layer between Git, Jira/ALM, docs and structured artifacts. |
| 11 | **Consulting Artifact Compiler** | Consultants repeatedly recreate the same diagrams, mapping sheets, specs, test scopes and handover documents from overlapping facts | Take one structured project folder/model and generate Markdown, diagrams, mapping views, interface specs and test scope | Artifact templates, customer-specific profiles, build pipeline, versioned releases, publish packages, agent context | **5/5** | **5/5** | **92** | `CANDIDATE` | `consulting-artifact-compiler` | **No** | Not started | Meta-product over RDP, templates and the transformation model. Build after 2–3 canonical schemas stabilize. |
| 12 | **Process Variant Compare** | Global projects need to compare country/business-unit process variants without manually inspecting diagrams | Two structured process definitions → visual delta of steps, roles, systems, controls and data | Variant library, harmonization analysis, standard-vs-local scoring, Signavio/BPMN round-trip | **4.5/5** | **5/5** | **90** | `CANDIDATE` | [process-as-code](https://github.com/dkharlanau/process-as-code) | **Yes** | Not started | Planned feature of Process as Code; host repository now exists. |
| 13 | **Mapping Lineage & Impact** | A mapping change can silently affect interfaces, reconciliations and tests | Mapping change → downstream lineage → impacted targets, value maps, tests and consuming interfaces | Connect directly into Transformation Graph and Enterprise Change Graph | **5/5** | **5/5** | **90** | `CANDIDATE` | [mapping-as-code](https://github.com/dkharlanau/mapping-as-code) | **Yes** | Not started | Planned major capability of Mapping as Code; host repository now exists. |
| 14 | **Enterprise Data Contract** | File-based project data lacks explicit schema, identifiers, reference domains, ownership and quality expectations | Define portable contract for XLSX/CSV/project extracts with types, keys, references and rules | Validation, schema drift, fixture generation, mapping integration, reconciliation, data-product export | **5/5** | **5/5** | **89** | `CANDIDATE` | `enterprise-data-contract` | **No** | Not started | RDP already has source/output contracts and reusable validation blocks. Broader than Spreadsheet Contract. |
| 15 | **Cross-System Identifier Registry** | Crosswalks are copied between projects/files and become inconsistent; there is no explicit identity graph | Versioned identity mappings between legacy/MDG/S4/other systems with ambiguity and evidence tracking | Relationship graph, API, reconciliation integration, merge/split history, migration lineage | **5/5** | **5/5** | **89** | `CANDIDATE` | [data-relationship-map](https://github.com/dkharlanau/data-relationship-map) | **Yes** | Not started | Planned durable module of Data Relationship Map; host repository now exists. |
| 16 | **Test Scope as Code** | Regression scope is often derived manually from change descriptions, resulting in inconsistent coverage | Structured change/process/interface model → deterministic test scope and coverage matrix | Test contracts, ALM/Jira export, automated evidence linkage, coverage history | **4.5/5** | **5/5** | **88** | `CANDIDATE` | [enterprise-change-graph](https://github.com/dkharlanau/enterprise-change-graph) | **Yes** | Not started | Planned capability of Enterprise Change Graph. Avoid generic LLM-only test generation. |
| 17 | **Integration Contract Tests** | Teams need regression tests for payload semantics, not just connectivity | Interface contract + actual/expected payloads → schema, mapping and business assertion tests | IDoc/XML/JSON/API profiles, fixtures, replay, CI, compatibility matrix | **4.5/5** | **4.5/5** | **88** | `CANDIDATE` | [interface-as-code](https://github.com/dkharlanau/interface-as-code) | **Yes** | Not started | Planned capability of Interface as Code; IDoc can become one SAP-specific profile. |
| 18 | **Business Object Graph** | Functional consultants need a visual way to explain how business objects, organizational data and documents relate | Define object types/relationships from structured files → interactive object graph | SAP profiles, process overlays, master-data dependencies, migration scope, queryable graph | **5/5** | **5/5** | **87** | `CANDIDATE` | [transformation-graph](https://github.com/dkharlanau/transformation-graph) | **Yes** | Not started | Planned view of Transformation Graph rather than a separate product. |
| 19 | **Data Mapping Review Portal** | Business owners cannot meaningfully review giant technical mapping spreadsheets | Render mapping contracts as a focused web review: source, target, transformation, examples, unresolved decisions | Comments/approvals, release comparison, decision links, export back to mapping source | **5/5** | **4.5/5** | **87** | `CANDIDATE` | [mapping-as-code](https://github.com/dkharlanau/mapping-as-code) | **Yes** | Not started | Business-facing surface for Mapping as Code; host repository now exists. |
| 20 | **Transformation Scenario Sandbox** | Architecture/process alternatives are discussed in slides but their dependency consequences are hard to compare | Clone a transformation graph, modify systems/interfaces/process steps and compare impact | Scenario cost/risk overlays, migration waves, architectural options, decision records | **5/5** | **4/5** | **86** | `CANDIDATE` | [transformation-graph](https://github.com/dkharlanau/transformation-graph) | **Yes** | Not started | Planned advanced capability of Transformation Graph; host repository now exists. |
| 21 | **Operational Handover Package** | Project-to-AMS handover loses context between design, mapping, interface specs, controls and runbooks | Compile selected project model into operations package: interfaces, owners, monitoring, retries, known risks, runbooks | Automated refresh, support context packs, incident links, change history | **5/5** | **5/5** | **85** | `CANDIDATE` | `consulting-artifact-compiler` | **No** | Not started | Strong commercial/consulting utility; build after shared schemas stabilize. |
| 22 | **Data Exception Ledger** | Data migration and reconciliation exceptions are tracked in ad-hoc spreadsheets with poor lifecycle visibility | Standard exception records with source evidence, classification, owner, decision and resolution | Link exceptions to mappings, reconciliations, cutover, recurring patterns, dashboards | **5/5** | **5/5** | **85** | `CANDIDATE` | [reconciliation-as-code](https://github.com/dkharlanau/reconciliation-as-code) | **Yes** | Not started | Planned capability of Reconciliation as Code; host repository now exists. |
| 23 | **Enterprise Rule Catalog** | Important business rules are spread across mapping sheets, configuration notes, decisions and process docs | Versioned catalog linking rule → condition → outcome → owner → process → system → test | Decision-table execution, change impact, rule search, audit, exports | **5/5** | **4.5/5** | **84** | `CANDIDATE` | [decision-tables-as-code](https://github.com/dkharlanau/decision-tables-as-code) | **Yes** | Not started | Planned capability of Decision Tables as Code; host repository now exists. |
| 24 | **SAP Automotive Operations Model** | JIT/JIS knowledge is highly specialized and difficult to visualize as state, action and dependency models | Structured JIT/JIS actions/states/objects → interactive state/dependency model | Cancellation planning, incident diagnostics, process simulation, interface/test overlays | **4.5/5** | **4/5** | **84** | `CANDIDATE` | `dkharlanau.github.io` initially | **Yes — site repo** | Foundation exists | Strong niche differentiation. Keep as a domain profile over the general modeling tools before creating a separate repo. |
| 25 | **Agent Context Compiler** | Agents need small, scoped, machine-readable enterprise context rather than entire sites or document dumps | Select process/system/mapping/interface scope → compile compact JSON/Markdown context with provenance | MCP resources, skills, change-specific context packs, evaluation datasets | **5/5** | **5/5** | **83** | `CANDIDATE` | `dkharlanau.github.io` initially | **Yes — site repo** | Partial | Machine layer, llms exports, skills and manifests already exist. Stronger when backed by the transformation model. |
| 26 | **Project Model API** | Structured transformation artifacts need one stable machine interface for tools and agents | Read-only API over canonical process/mapping/interface/reconciliation/change entities | GraphQL/REST, MCP, tool integrations, local server, connectors | **5/5** | **4/5** | **82** | `BACKLOG` | future shared core | **No** | Not started | Infrastructure, not a first product. Build only after schemas are proven in real tools. |
| 27 | **SAP Migration File Validation** | Migration files can contain structural/data errors before load | Deterministic file validation for SAP Migration Cockpit templates | Template compare, correction checks, SAP-specific profiles | **2.5/5** | **5/5** | **69** | `BACKLOG` | future SAP profile | **No** | Not started | Intentionally demoted: SAP can improve this class of functionality. Better as a profile/module, not a flagship. |
| 28 | **SAP Incident Diagnostics** | Consultants need consistent evidence collection and diagnostic routing | Symptom → evidence checklist → likely layers → safe checks | Export/log ingestion, support context, incident patterns | **2.5/5** | **5/5** | **68** | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | Valuable content/tooling, but less defensible as a standalone product because SAP/ALM/AI support tooling will improve. |
| 29 | **SAP IDoc Analysis** | IDoc status and payload investigation is repetitive | IDoc semantic comparison/status normalization | Contract-test profile inside Interface as Code | **2/5** | **4/5** | **64** | `BACKLOG` | [interface-as-code](https://github.com/dkharlanau/interface-as-code) profile | **Yes** | Not started | Keep domain knowledge, but implement only as a profile of Interface as Code rather than a standalone bet. |
| 30 | **Generic SAP MCP Adapter** | Expose SAP APIs as agent tools | Narrow adapter for specific proven use cases | Broader tool surface if real demand appears | **1/5** | **3/5** | **45** | `PARKED` | future only | **No** | Not started | Commodity risk is high. Revisit only when another product has a concrete SAP action that needs MCP. |
{% endcapture %}
{{ product_roadmap_table | markdownify }}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <h2>What became features instead of products</h2>
    <p>The previous roadmap contained many useful ideas that should not disappear. They are now treated as capabilities inside stronger products:</p>
    <div class="tool-roadmap-table-scroll" role="region" aria-label="Ideas consolidated into products" tabindex="0">
{% capture product_features_table %}
| Previous idea | New home |
|---|---|
| Mapping Lint, Mapping Change Analysis, Reference Coverage, Mapping Lineage, Mapping Test Generation | **Mapping as Code** |
| Join Cardinality, ID Crosswalk, Schema Compare, Scope Reconciliation, Record Compare | **Reconciliation as Code / Data Relationship Map / Enterprise Data Contract** |
| IDoc Contract Tests, Interface Contract Review, Retry Analysis | **Interface as Code / Integration Contract Tests** |
| Cutover Dependencies, Cutover Readiness, Go/No-Go, Evidence Manifest | **Cutover Graph** |
| Change Impact, Regression Scope | **Enterprise Change Graph / Test Scope as Code** |
| Data Quality Rules, Identifier/Locale checks, Spreadsheet Contract | **Enterprise Data Contract** |
| SAP JIT Reference, JIT Diagnostics, Cancellation Analysis | **SAP Automotive Operations Model** |
| Agent Context Export, Knowledge API | **Agent Context Compiler / Project Model API** |
| RCA/Incident/Runbook templates | Supporting protocols on `dkharlanau.github.io`, not primary standalone products |
{% endcapture %}
{{ product_features_table | markdownify }}
    </div>
  </section>

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Execution order</p><h2>Build the model through useful products.</h2></div>
    <ol>
      <li><span>01</span><strong>Mapping</strong><p>Build Mapping as Code first: Excel import, canonical mapping schema, validation, diff and visual lineage.</p></li>
      <li><span>02</span><strong>Graph</strong><p>Build Transformation Graph around a small shared enterprise model and ingest mapping/process/interface artifacts.</p></li>
      <li><span>03</span><strong>Interfaces</strong><p>Add Interface as Code so mappings, contracts, operations and tests become connected rather than separate documents.</p></li>
      <li><span>04</span><strong>Reconcile</strong><p>Add Reconciliation as Code and evidence so the model proves what changed across systems instead of only documenting intent.</p></li>
      <li><span>05</span><strong>Expand</strong><p>Only then add Process as Code, Enterprise Change Graph, Cutover Graph and Project Evidence Graph as views over stable schemas.</p></li>
    </ol>
  </section>
</div>