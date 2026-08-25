---
layout: default
title: "Tool Roadmap — SAP, Data, Integration and Operations"
description: "Canonical roadmap for practical SAP and enterprise tools: priorities, implementation fit, repository placement, and delivery status."
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
  </section>

  <section class="research-canvas__inventory" data-reveal markdown="1">
## Delivery model

| Home | Intended scope | Repo created? |
|---|---|:---:|
| `sap-migration-tools` | SAP migration validation, templates, errors, mapping tasks, correction files and CSV packs | **No** |
| `mapping-lint` | Mapping validation, coverage, changes, lineage and generated tests | **No** |
| `enterprise-data-utils` | Join cardinality, crosswalks, reconciliation, schema/file analysis and anonymization | **No** |
| `idoc-contract-tests` | IDoc semantic comparison, assertions, status analysis and test fixtures | **No** |
| `dkharlanau.github.io` | Diagnostic, operational, architecture, automotive and AI decision tools that primarily use existing site knowledge | **Yes** |

**Status:** `NEXT` = build next; `QUEUE` = strong follow-up; `CANDIDATE` = keep and validate; `BACKLOG` = useful but not current focus; `PARKED` = weak fit now; `REJECTED` = deliberately do not build.
  </section>

  <section class="research-canvas__inventory" id="roadmap" data-reveal markdown="1">
## Canonical roadmap

| # | Tool | Concrete task | Codex fit | Score | Status | Intended home | Repo created? |
|---:|---|---|:---:|---:|---|---|:---:|
| 1 | **SAP Migration Validator** | Validate Migration Cockpit XML/CSV structure, fields, types, lengths and references before load | 5/5 | 97 | `NEXT` | `sap-migration-tools` | **No** |
| 2 | **Mapping Lint** | Find mapping gaps, conflicts, duplicates, missing defaults and unresolved rows | 5/5 | 96 | `NEXT` | `mapping-lint` | **No** |
| 3 | **Join Cardinality** | Predict row multiplication, data loss and unsafe key cardinality before joining files | 5/5 | 95 | `NEXT` | `enterprise-data-utils` | **No** |
| 4 | **SAP Migration Error Analysis** | Normalize migration messages, group root patterns, rank affected records and remediation work | 4/5 | 95 | `QUEUE` | `sap-migration-tools` | **No** |
| 5 | **ID Crosswalk** | Build and validate cross-system identifier relationships from two or more files | 5/5 | 94 | `QUEUE` | `enterprise-data-utils` | **No** |
| 6 | **SAP Data Validation** | Inspect Excel/CSV exports for type drift, blanks, duplicates, identifiers, locale errors and suspicious conversions | 5/5 | 94 | `QUEUE` | `enterprise-data-utils` | **No** |
| 7 | **SAP Migration Template Compare** | Compare two Migration Cockpit templates and report structural or field-level changes | 5/5 | 93 | `QUEUE` | `sap-migration-tools` | **No** |
| 8 | **SAP Mapping Validation** | Validate downloaded SAP mapping-task workbooks for coverage, collisions and type/length issues | 4.5/5 | 92 | `QUEUE` | `sap-migration-tools` | **No** |
| 9 | **Mapping Change Analysis** | Compare mapping releases and identify breaking changes and affected targets | 5/5 | 92 | `QUEUE` | `mapping-lint` | **No** |
| 10 | **Reference Coverage** | Measure lookup/reference coverage, unmapped values, frequency and unused reference entries | 5/5 | 92 | `QUEUE` | `mapping-lint` | **No** |
| 11 | **Cutover Dependencies** | Turn object dependencies into load waves, ordering constraints, blockers and cycle detection | 5/5 | 91 | `QUEUE` | `enterprise-data-utils` | **No** |
| 12 | **IDoc Contract Tests** | Compare actual and expected IDocs using SAP-aware assertions rather than generic XML diff | 4/5 | 91 | `QUEUE` | `idoc-contract-tests` | **No** |
| 13 | **Mapping Test Generation** | Convert mapping specifications into executable validation cases and assertions | 5/5 | 90 | `CANDIDATE` | `mapping-lint` | **No** |
| 14 | **Data Reconciliation** | Compare source/target or before/after files by business key and control totals | 5/5 | 90 | `CANDIDATE` | `enterprise-data-utils` | **No** |
| 15 | **SAP Correction Compare** | Verify intended and unexpected changes in correction files before reload | 4.5/5 | 89 | `CANDIDATE` | `sap-migration-tools` | **No** |
| 16 | **SAP JIT Cancellation Analysis** | Determine safe cancellation/unwind sequencing for JIT/JIS process states | 4/5 | 89 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** |
| 17 | **Schema Compare** | Detect added, removed or changed columns, inferred types and formats between exports | 5/5 | 88 | `CANDIDATE` | `enterprise-data-utils` | **No** |
| 18 | **SAP Partner Validation** | Detect self-links, missing partners, cycles and inconsistent partner relationships | 4/5 | 88 | `CANDIDATE` | `enterprise-data-utils` | **No** |
| 19 | **SAP Migration CSV Validation** | Validate Migration Cockpit CSV packages, filenames, structure, references and formats | 4.5/5 | 87 | `CANDIDATE` | `sap-migration-tools` | **No** |
| 20 | **SAP Data Anonymize** | Produce structurally equivalent, relationship-preserving test fixtures from private SAP exports | 5/5 | 87 | `CANDIDATE` | `enterprise-data-utils` | **No** |
| 21 | **SAP Record Compare** | Compare two SAP/ALV exports by business records instead of spreadsheet cell positions | 5/5 | 87 | `CANDIDATE` | `enterprise-data-utils` | **No** |
| 22 | **Scope Reconciliation** | Compare expected scope with an actual extract and report missing, unexpected and duplicate objects | 5/5 | 87 | `CANDIDATE` | `enterprise-data-utils` | **No** |
| 23 | **Interface Contract Review** | Review an interface definition for schema, mapping, retry, monitoring, ownership and reconciliation gaps | 5/5 | 87 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** |
| 24 | **SAP JIT Reference** | Search JIT/JIS actions, objects, prerequisites, dependencies and standard references | 4/5 | 87 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** |
| 25 | **SAP JIT Diagnostics** | Trace a JIT/JIS production symptom through evidence, process state and likely failed layer | 4/5 | 87 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** |
| 26 | **Integration Failure Analysis** | Isolate API, IDoc, RFC, file or event failures by layer, retry risk and ownership boundary | 5/5 | 86 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** |
| 27 | **Change Impact** | Turn a proposed SAP/enterprise change into dependency, risk and regression-test scope | 5/5 | 86 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** |
| 28 | **SAP Diagnostics Index** | Route a symptom or business object to the relevant Atlas diagnostic path and required evidence | 5/5 | 86 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** |
| 29 | **Incident Patterns** | Cluster incident exports into recurring symptoms and problem candidates | 4.5/5 | 85 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** |
| 30 | **SAP Incident Analysis** | Structure incident evidence, hypotheses, checks, unsafe actions and escalation boundaries | 5/5 | 85 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** |
| 31 | **Cutover Readiness** | Review cutover plans for data, interfaces, authorizations, jobs, monitoring, rollback and exit gaps | 5/5 | 85 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** |
| 32 | **Mapping Lineage** | Visualize source → transformation → target relationships from mapping specifications | 5/5 | 84 | `CANDIDATE` | `mapping-lint` | **No** |
| 33 | **Object Deduplication** | Rank duplicate business-object candidates and explain the matching evidence | 4/5 | 84 | `CANDIDATE` | `enterprise-data-utils` | **No** |
| 34 | **Retry Analysis** | Review retry and reprocessing safety, idempotency and duplicate scenarios | 5/5 | 84 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** |
| 35 | **Agent Context Export** | Export selected site knowledge as compact JSON/Markdown context for ChatGPT, Claude or Codex | 5/5 | 84 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** |
| 36 | **IDoc Status Analysis** | Analyze IDoc/AIF-style exports for status distribution, dominant errors and stuck patterns | 4/5 | 83 | `CANDIDATE` | `idoc-contract-tests` | **No** |
| 37 | **AI Use-Case Review** | Classify a use case as deterministic, AI-assisted or human-led and define autonomy/control boundaries | 5/5 | 83 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** |
| 38 | **SAP Export Profile** | Paste or upload an SAP export for immediate structural and value profiling | 5/5 | 82 | `CANDIDATE` | `enterprise-data-utils` | **No** |
| 39 | **Data Manifest** | Record file hash, schema, row counts and reconciliation controls as repeatable evidence | 5/5 | 82 | `CANDIDATE` | `enterprise-data-utils` | **No** |
| 40 | **SAP BP Replication** | Trace BP replication through eligibility, source, mapping, channel, target and key mapping | 5/5 | 81 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** |
| 41 | **Root Cause Review** | Check RCA quality against evidence, causal explanation, corrective action and recurrence controls | 5/5 | 81 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** |
| 42 | **Knowledge API** | Expose curated site datasets and reviewed knowledge through normalized machine endpoints | 4/5 | 81 | `CANDIDATE` | `dkharlanau.github.io` | **Yes — site repo** |
| 43 | **SAP ID Validation** | Detect leading-zero loss, numeric conversion, scientific notation and identifier corruption | 5/5 | 81 | `BACKLOG` | `enterprise-data-utils` | **No** |
| 44 | **Data Quality Rules** | Define and review structured DQ rules including ownership, enforcement and remediation | 5/5 | 80 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** |
| 45 | **Architecture Tradeoffs** | Compare architecture options by contradictions, assumptions, reversibility and experiments | 5/5 | 80 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** |
| 46 | **Locale Validation** | Detect decimal, date and separator problems in spreadsheets and CSV files | 5/5 | 80 | `BACKLOG` | `enterprise-data-utils` | **No** |
| 47 | **SAP RFC Queue Diagnostics** | Structure qRFC/tRFC investigation and recovery order with safe intervention boundaries | 4/5 | 79 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** |
| 48 | **SAP AMS Review** | Assess AMS operating maturity, waste and improvement backlog | 5/5 | 79 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** |
| 49 | **Incident Evidence** | Review support tickets/escalations for missing evidence and weak diagnostic completeness | 5/5 | 79 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** |
| 50 | **Runbook Review** | Build or review runbooks for stop conditions, rollback, evidence, ownership and validation | 5/5 | 78 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** |
| 51 | **SAP Text Validation** | Validate long-text exports for duplicates, line problems, control characters and length issues | 5/5 | 78 | `BACKLOG` | `enterprise-data-utils` | **No** |
| 52 | **SAP Output Diagnostics** | Trace output/message failures through determination, recipient, processing and delivery | 5/5 | 78 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** |
| 53 | **Spreadsheet Contract** | Apply a reusable schema/rule contract to arbitrary spreadsheets | 5/5 | 77 | `BACKLOG` | `enterprise-data-utils` | **No** |
| 54 | **Requirement Review** | Review requirements for ambiguity, scope, ownership, testability and acceptance criteria | 5/5 | 76 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** |
| 55 | **Enterprise Test Data** | Generate synthetic enterprise datasets with relationships and deliberate quality failures | 5/5 | 76 | `BACKLOG` | `enterprise-data-utils` | **No** |
| 56 | **Knowledge Export** | Turn reviewed site knowledge into checklists and structured operational artifacts | 5/5 | 75 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** |
| 57 | **SAP Context Search** | Search SAP terms together with related processes, objects, risks, datasets and diagnostic pages | 5/5 | 74 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** |
| 58 | **SAP Lead Cases** | Generate and assess SAP Lead scenarios for explanation, diagnosis, design and challenge practice | 5/5 | 73 | `BACKLOG` | `dkharlanau.github.io` | **Yes — site repo** |
| 59 | **SAP MCP Adapter** | Expose SAP APIs as generic MCP capabilities | 3/5 | 58 | `PARKED` | future repo | **No** |
| 60 | **SAP Operations Agent** | Generic SAP support/operations agent over systems and documents | 3/5 | 50 | `PARKED` | future only if a narrow use case proves value | **No** |
| 61 | **SAP Migration XML Split** | Split migration XML files | 5/5 | 42 | `REJECTED` | do not build; existing SAP solution covers the core need | **N/A** |
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