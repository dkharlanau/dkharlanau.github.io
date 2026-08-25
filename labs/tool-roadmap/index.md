---
layout: default
title: "Tool Roadmap — SAP, Data, Integration and Operations"
description: "Canonical roadmap for practical SAP and enterprise tools: priorities, implementation fit, repository placement, delivery status, and implementation notes."
permalink: /labs/tool-roadmap/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-25
hide_global_cta: true
tags:
  - sap
  - tools
  - data-quality
  - integration
  - migration
  - roadmap
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li aria-current="page">Tool Roadmap</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Lab / Tool roadmap</p>
      <h1>Build small tools<br />around real enterprise work.</h1>
      <p>This is the canonical backlog for public tool development. The priority is deterministic software that solves a concrete file, mapping, migration, integration, or operational task without requiring a private SAP landscape.</p>
      <a class="research-canvas__button" href="#roadmap">Open the roadmap <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Roadmap rules">
      <p>Selection rule</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Concrete</strong><small>One observable problem</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Testable</strong><small>Deterministic where possible</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Portable</strong><small>No SAP access required</small></div>
      <em>ChatGPT and Codex should help build the tool, not become the tool by default.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal aria-label="Naming and product boundary">
    <span class="material-symbols-outlined" aria-hidden="true">terminal</span>
    <p><strong>Naming rule:</strong> use literal engineering names such as validate, compare, reconcile, lint, profile, trace, and analyze. Avoid product-name filler such as Doctor, Guard, Copilot, Assistant, Explorer, Navigator, Studio, or AI-powered.</p>
    <p><strong>Repository rule:</strong> do not create one repository per row. Related capabilities should share a small number of strong repositories and a reusable deterministic core.</p>
    <p><strong>Repository status:</strong> checked against the GitHub repositories owned by <code>dkharlanau</code> on 2026-08-25. “Yes — site repo” means the intended host repository already exists; it does not mean that the tool itself is implemented.</p>
    <p><strong>Implementation:</strong> <code>Not started</code> means no tool implementation exists; <code>Foundation exists</code> means reusable site data, rules, templates or domain content already exist; <code>Partial</code> means a meaningful part of the actual capability already exists; <code>Implemented</code> is reserved for a usable tested tool.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal markdown="1">
## Delivery model

| Home | Intended scope | Repo created? | Implementation |
|---|---|:---:|---|
| `sap-migration-tools` | SAP migration validation, templates, errors, mapping tasks, correction files and CSV packs | **No** | Not started |
| `mapping-lint` | Mapping validation, coverage, changes, lineage and generated tests | **No** | Not started; RDP primitives can be reused |
| `enterprise-data-utils` | Join cardinality, crosswalks, reconciliation, schema/file analysis and anonymization | **No** | Not started; RDP already defines several core blocks |
| `idoc-contract-tests` | IDoc semantic comparison, assertions, status analysis and test fixtures | **No** | Not started; Atlas diagnostics provide domain context |
| `dkharlanau.github.io` | Diagnostic, operational, architecture, automotive and AI decision tools that primarily use existing site knowledge | **Yes** | Foundation exists; several underlying datasets, protocols and labs already exist |

**Status:** `NEXT` = build next; `QUEUE` = strong follow-up; `CANDIDATE` = keep and validate; `BACKLOG` = useful but not current focus; `PARKED` = weak fit now; `REJECTED` = deliberately do not build.
  </section>

  <section class="research-canvas__inventory" id="roadmap" data-reveal markdown="1">
## Canonical roadmap

| # | Tool | Concrete task | Codex fit | Score | Status | Intended home | Repo created? | Implementation | Comments |
|---:|---|---|:---:|---:|---|---|:---:|---|---|
| 1 | **SAP Migration Validator** | Validate Migration Cockpit XML/CSV structure, fields, types, lengths and references before load | 5/5 | 97 | `NEXT` | `sap-migration-tools` | **No** | Not started | Best first SAP tool. Need public/synthetic Migration Cockpit fixtures and deterministic validation rules. |
| 2 | **Mapping Lint** | Find mapping gaps, conflicts, duplicates, missing defaults and unresolved rows | 5/5 | 96 | `NEXT` | `mapping-lint` | **No** | Foundation exists | RDP already contains mapping coverage, cardinality, normalization and exception concepts. Strong standalone repo. |
| 3 | **Join Cardinality** | Predict row multiplication, data loss and unsafe key cardinality before joining files | 5/5 | 95 | `NEXT` | `enterprise-data-utils` | **No** | Foundation exists | RDP already defines cardinality validation. Very small MVP and easy to test exhaustively. |
| 4 | **SAP Migration Error Analysis** | Normalize migration messages, group root patterns, rank affected records and remediation work | 4/5 | 95 | `QUEUE` | `sap-migration-tools` | **No** | Not started | Needs realistic exported migration messages. Normalize dynamic variables before grouping. |
| 5 | **ID Crosswalk** | Build and validate cross-system identifier relationships from two or more files | 5/5 | 94 | `QUEUE` | `enterprise-data-utils` | **No** | Foundation exists | Exact matching first; ambiguous/fuzzy candidates must remain separate from accepted mappings. |
| 6 | **SAP Data Validation** | Inspect Excel/CSV exports for type drift, blanks, duplicates, identifiers, locale errors and suspicious conversions | 5/5 | 94 | `QUEUE` | `enterprise-data-utils` | **No** | Foundation exists | RDP already has cleaners, locale parsers, validators and SAP identifier normalization concepts. |
| 7 | **SAP Migration Template Compare** | Compare two Migration Cockpit templates and report structural or field-level changes | 5/5 | 93 | `QUEUE` | `sap-migration-tools` | **No** | Not started | Excellent low-data MVP: two templates in, structural change report out. |
| 8 | **SAP Mapping Validation** | Validate downloaded SAP mapping-task workbooks for coverage, collisions and type/length issues | 4.5/5 | 92 | `QUEUE` | `sap-migration-tools` | **No** | Not started | Requires a few representative SAP mapping-task files to lock down workbook semantics. |
| 9 | **Mapping Change Analysis** | Compare mapping releases and identify breaking changes and affected targets | 5/5 | 92 | `QUEUE` | `mapping-lint` | **No** | Foundation exists | Natural second command after Mapping Lint; reuse the same parser and canonical mapping model. |
| 10 | **Reference Coverage** | Measure lookup/reference coverage, unmapped values, frequency and unused reference entries | 5/5 | 92 | `QUEUE` | `mapping-lint` | **No** | Foundation exists | RDP already defines mapping coverage. Add frequency/impact ranking for practical use. |
| 11 | **Cutover Dependencies** | Turn object dependencies into load waves, ordering constraints, blockers and cycle detection | 5/5 | 91 | `QUEUE` | `enterprise-data-utils` | **No** | Not started | Graph/topological-sort problem; strong deterministic tool with almost no SAP dependency. |
| 12 | **IDoc Contract Tests** | Compare actual and expected IDocs using SAP-aware assertions rather than generic XML diff | 4/5 | 91 | `QUEUE` | `idoc-contract-tests` | **No** | Foundation exists | Atlas has IDoc diagnostics; implementation still needs realistic IDoc fixtures and segment matching rules. |
| 13 | **Mapping Test Generation** | Convert mapping specifications into executable validation cases and assertions | 5/5 | 90 | `CANDIDATE` | `mapping-lint` | **No** | Not started | Build only after a stable canonical mapping model exists. |
| 14 | **Data Reconciliation** | Compare source/target or before/after files by business key and control totals | 5/5 | 90 | `CANDIDATE` | `enterprise-data-utils` | **No** | Foundation exists | RDP already describes monthly reconciliation and control-total patterns. |
| 15 | **SAP Correction Compare** | Verify intended and unexpected changes in correction files before reload | 4.5/5 | 89 | `CANDIDATE` | `sap-migration-tools` | **No** | Not started | Reuse Migration Cockpit parser from #1; needs correction-file fixtures. |
| 16 | **SAP JIT Cancellation Analysis** | Determine safe cancellation/unwind sequencing for JIT/JIS process states | 4/5 | 89 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | Automotive JIT knowledge already exists; needs explicit state/action model and careful functional QA. |
| 17 | **Schema Compare** | Detect added, removed or changed columns, inferred types and formats between exports | 5/5 | 88 | `CANDIDATE` | `enterprise-data-utils` | **No** | Foundation exists | Generic but useful building block; should be a module, not its own repo. |
| 18 | **SAP Partner Validation** | Detect self-links, missing partners, cycles and inconsistent partner relationships | 4/5 | 88 | `CANDIDATE` | `enterprise-data-utils` | **No** | Not started | Needs explicit KNVP-like input contract and conservative rules to avoid false positives. |
| 19 | **SAP Migration CSV Validation** | Validate Migration Cockpit CSV packages, filenames, structure, references and formats | 4.5/5 | 87 | `CANDIDATE` | `sap-migration-tools` | **No** | Not started | Extension of #1 after XML/template rules are stable. |
| 20 | **SAP Data Anonymize** | Produce structurally equivalent, relationship-preserving test fixtures from private SAP exports | 5/5 | 87 | `CANDIDATE` | `enterprise-data-utils` | **No** | Not started | Strategically valuable because it can create safe fixtures for the other public tools. |
| 21 | **SAP Record Compare** | Compare two SAP/ALV exports by business records instead of spreadsheet cell positions | 5/5 | 87 | `CANDIDATE` | `enterprise-data-utils` | **No** | Foundation exists | Reuse canonicalization and key selection. Differentiate through SAP/business-key semantics. |
| 22 | **Scope Reconciliation** | Compare expected scope with an actual extract and report missing, unexpected and duplicate objects | 5/5 | 87 | `CANDIDATE` | `enterprise-data-utils` | **No** | Foundation exists | Thin specialization of reconciliation; likely a command/module rather than standalone product. |
| 23 | **Interface Contract Review** | Review an interface definition for schema, mapping, retry, monitoring, ownership and reconciliation gaps | 5/5 | 87 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | Operational Templates and integration material already define many review dimensions. |
| 24 | **SAP JIT Reference** | Search JIT/JIS actions, objects, prerequisites, dependencies and standard references | 4/5 | 87 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | Best as an interactive view over the automotive-JIT dataset, not a separate repo. |
| 25 | **SAP JIT Diagnostics** | Trace a JIT/JIS production symptom through evidence, process state and likely failed layer | 4/5 | 87 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | Combine automotive knowledge with the Atlas diagnostic pattern. Domain QA is the main work. |
| 26 | **Integration Failure Analysis** | Isolate API, IDoc, RFC, file or event failures by layer, retry risk and ownership boundary | 5/5 | 86 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | Integration Failure Analysis template already provides the core reasoning protocol. |
| 27 | **Change Impact** | Turn a proposed SAP/enterprise change into dependency, risk and regression-test scope | 5/5 | 86 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | Change Impact Review template already exists; build structured input/output and reusable evidence links. |
| 28 | **SAP Diagnostics Index** | Route a symptom or business object to the relevant Atlas diagnostic path and required evidence | 5/5 | 86 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** | Partial | Atlas already has a large diagnostic corpus and interactive pathfinder; next step is stronger routing/search. |
| 29 | **Incident Patterns** | Cluster incident exports into recurring symptoms and problem candidates | 4.5/5 | 85 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | Needs a CSV input contract and transparent clustering; avoid opaque LLM-only grouping. |
| 30 | **SAP Incident Analysis** | Structure incident evidence, hypotheses, checks, unsafe actions and escalation boundaries | 5/5 | 85 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | Incident Triage protocol and Atlas diagnostics already provide most of the decision structure. |
| 31 | **Cutover Readiness** | Review cutover plans for data, interfaces, authorizations, jobs, monitoring, rollback and exit gaps | 5/5 | 85 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | Cutover/Hypercare protocol exists; needs scored checklist and evidence model. |
| 32 | **Mapping Lineage** | Visualize source → transformation → target relationships from mapping specifications | 5/5 | 84 | `CANDIDATE` | `mapping-lint` | **No** | Not started | Visualization should sit on the canonical mapping model built for #2. |
| 33 | **Object Deduplication** | Rank duplicate business-object candidates and explain the matching evidence | 4/5 | 84 | `CANDIDATE` | `enterprise-data-utils` | **No** | Foundation exists | RDP matcher concepts help; accepted duplicates must never be inferred silently from fuzzy scores. |
| 34 | **Retry Analysis** | Review retry and reprocessing safety, idempotency and duplicate scenarios | 5/5 | 84 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | Integration Failure template already asks about idempotency, duplicates and retry risk. |
| 35 | **Agent Context Export** | Export selected site knowledge as compact JSON/Markdown context for ChatGPT, Claude or Codex | 5/5 | 84 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** | Partial | Machine layer, llms exports, Agent Skills and manifests already exist; need user-selectable context packaging. |
| 36 | **IDoc Status Analysis** | Analyze IDoc/AIF-style exports for status distribution, dominant errors and stuck patterns | 4/5 | 83 | `CANDIDATE` | `idoc-contract-tests` | **No** | Foundation exists | Atlas diagnostics provide semantics; needs standardized export fixtures and normalization. |
| 37 | **AI Use-Case Review** | Classify a use case as deterministic, AI-assisted or human-led and define autonomy/control boundaries | 5/5 | 83 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | Decision Design and Business AI already contain decision/control concepts. Keep scoring explicit and explainable. |
| 38 | **SAP Export Profile** | Paste or upload an SAP export for immediate structural and value profiling | 5/5 | 82 | `CANDIDATE` | `enterprise-data-utils` | **No** | Foundation exists | Very small browser-local feature using the same parsing core as Data Validation. |
| 39 | **Data Manifest** | Record file hash, schema, row counts and reconciliation controls as repeatable evidence | 5/5 | 82 | `CANDIDATE` | `enterprise-data-utils` | **No** | Foundation exists | Fits RDP evidence/contract model. Useful support primitive rather than headline product. |
| 40 | **SAP BP Replication** | Trace BP replication through eligibility, source, mapping, channel, target and key mapping | 5/5 | 81 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | Atlas already has BP/customer replication and key-mapping diagnostics. Convert them into guided flow. |
| 41 | **Root Cause Review** | Check RCA quality against evidence, causal explanation, corrective action and recurrence controls | 5/5 | 81 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | RCA protocol already exists. Tool should review structure/evidence rather than invent a root cause. |
| 42 | **Knowledge API** | Expose curated site datasets and reviewed knowledge through normalized machine endpoints | 4/5 | 81 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** | Partial | Static JSON/YAML, manifests, llms exports and machine routes already exist; normalize and document a stable facade. |
| 43 | **SAP ID Validation** | Detect leading-zero loss, numeric conversion, scientific notation and identifier corruption | 5/5 | 81 | `BACKLOG` | `enterprise-data-utils` | **No** | Foundation exists | SAP identifier normalization is already an RDP block concept; include inside Data Validation. |
| 44 | **Data Quality Rules** | Define and review structured DQ rules including ownership, enforcement and remediation | 5/5 | 80 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | RDP and data-quality Atlas material already cover rules and governance. |
| 45 | **Architecture Tradeoffs** | Compare architecture options by contradictions, assumptions, reversibility and experiments | 5/5 | 80 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | TRIZ and Decision Design are already substantial frameworks; build as a structured application over them. |
| 46 | **Locale Validation** | Detect decimal, date and separator problems in spreadsheets and CSV files | 5/5 | 80 | `BACKLOG` | `enterprise-data-utils` | **No** | Foundation exists | RDP already names locale-specific date and decimal parsers. Module of SAP Data Validation. |
| 47 | **SAP RFC Queue Diagnostics** | Structure qRFC/tRFC investigation and recovery order with safe intervention boundaries | 4/5 | 79 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | Use Atlas/integration protocols; needs careful SAP-specific review of recovery boundaries. |
| 48 | **SAP AMS Review** | Assess AMS operating maturity, waste and improvement backlog | 5/5 | 79 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | Existing AMS/operations material can seed dimensions; value depends on a credible scoring model. |
| 49 | **Incident Evidence** | Review support tickets/escalations for missing evidence and weak diagnostic completeness | 5/5 | 79 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | Incident protocol already defines expected evidence; good deterministic checklist with optional text extraction. |
| 50 | **Runbook Review** | Build or review runbooks for stop conditions, rollback, evidence, ownership and validation | 5/5 | 78 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | Runbook template already exists; build coverage review before any generative builder. |
| 51 | **SAP Text Validation** | Validate long-text exports for duplicates, line problems, control characters and length issues | 5/5 | 78 | `BACKLOG` | `enterprise-data-utils` | **No** | Not started | Straightforward module when a few realistic text-export fixtures are available. |
| 52 | **SAP Output Diagnostics** | Trace output/message failures through determination, recipient, processing and delivery | 5/5 | 78 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | Atlas already contains output/integration diagnostics patterns; convert to guided checks. |
| 53 | **Spreadsheet Contract** | Apply a reusable schema/rule contract to arbitrary spreadsheets | 5/5 | 77 | `BACKLOG` | `enterprise-data-utils` | **No** | Foundation exists | Technically easy but generic/competitive. Build only if the SAP/data tools need a shared external contract format. |
| 54 | **Requirement Review** | Review requirements for ambiguity, scope, ownership, testability and acceptance criteria | 5/5 | 76 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** | Foundation exists | Business-analysis and assessment content can seed rules; weaker search differentiation than data tools. |
| 55 | **Enterprise Test Data** | Generate synthetic enterprise datasets with relationships and deliberate quality failures | 5/5 | 76 | `BACKLOG` | `enterprise-data-utils` | **No** | Not started | Useful mainly as fixture infrastructure for the higher-priority tools. |
| 56 | **Knowledge Export** | Turn reviewed site knowledge into checklists and structured operational artifacts | 5/5 | 75 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** | Partial | Agent Skills, machine exports and operational templates already exist; add controlled output schemas. |
| 57 | **SAP Context Search** | Search SAP terms together with related processes, objects, risks, datasets and diagnostic pages | 5/5 | 74 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** | Partial | Site already has search and structured manifests. Improve semantic relationships before adding AI search. |
| 58 | **SAP Lead Cases** | Generate and assess SAP Lead scenarios for explanation, diagnosis, design and challenge practice | 5/5 | 73 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** | Partial | Interview Readiness and SAP Lead Assessment already implement much of this product direction. |
| 59 | **SAP MCP Adapter** | Expose SAP APIs as generic MCP capabilities | 3/5 | 58 | `PARKED` | future repo | **No** | Not started | Requires real SAP APIs, authentication and narrow use cases; poor current fit. |
| 60 | **SAP Operations Agent** | Generic SAP support/operations agent over systems and documents | 3/5 | 50 | `PARKED` | future only if a narrow use case proves value | **No** | Foundation exists | Related knowledge and `sap-agentic-operations` repo exist, but a generic agent is intentionally not a current build target. |
| 61 | **SAP Migration XML Split** | Split migration XML files | 5/5 | 42 | `REJECTED` | do not build; existing SAP solution covers the core need | **N/A** | Rejected | Core need is already covered elsewhere; no reason to spend brand or maintenance effort here. |
  </section>

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Execution order</p><h2>Prove value before expanding the family.</h2></div>
    <ol>
      <li><span>01</span><strong>Validate</strong><p>Build one deterministic utility with realistic fixtures and automated tests.</p></li>
      <li><span>02</span><strong>Use</strong><p>Run it on a real or safely anonymized work artifact and record whether it removes manual effort.</p></li>
      <li><span>03</span><strong>Publish</strong><p>Add a focused README, browser demo where appropriate, examples, tests, package/CLI surface, and one strong problem page.</p></li>
      <li><span>04</span><strong>Expand</strong><p>Only add the next capability when it shares primitives, users, or search intent with the proven tool.</p></li>
    </ol>
  </section>
</div>