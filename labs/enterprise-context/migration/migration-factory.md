---
layout: default
title: "SAP S/4HANA Migration Factory — Governance, Mock Cycles and Ownership"
description: "Lead-level operating model for an S/4HANA migration factory: environments, object squads, mock cycles, defect control, design freeze, evidence, cutover ownership and handover."
permalink: /labs/enterprise-context/migration/migration-factory/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-09
hide_global_cta: true
tags:
  - sap
  - s4hana
  - migration
  - governance
  - testing
  - cutover
career_impact: mapped
career_skills:
  - delivery-release
  - lead-decision
  - integration-recovery
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">SAP Enterprise</a></li><li><a href="/labs/enterprise-context/migration/">S/4HANA Migration</a></li><li aria-current="page">Migration Factory</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Greenfield migration / Operating model</p>
      <h1>Build a migration factory<br />that learns every cycle.</h1>
      <p>The factory is not a room full of loaders. It is the operating model that turns source ownership, mapping, target configuration, object dependencies, test cycles, defect decisions and reconciliation into one repeatable production run.</p>
      <a class="research-canvas__button" href="#factory-model">Build the operating model <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Factory loop">
      <p>Factory loop</p>
      <div class="research-canvas__signal-line"><span>1</span><strong>Run</strong><small>Production-like cycle</small></div>
      <div class="research-canvas__signal-line"><span>2</span><strong>Learn</strong><small>Defect + timing evidence</small></div>
      <div class="research-canvas__signal-line"><span>3</span><strong>Freeze</strong><small>Stable cutover baseline</small></div>
      <em>Every mock must reduce uncertainty.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">groups</span>
    <p><strong>Migration ownership is cross-functional.</strong> Data teams can prepare and load records, but source owners explain legacy meaning, functional teams own target semantics, Finance signs financial opening, business owners accept operational state, and the migration Lead owns the integrated execution model.</p>
    <p><strong>One cutover needs one control model.</strong> Separate SD, MM, PP and FI trackers are useful locally, but the programme also needs one dependency graph, one object register, one defect classification and one go/no-go evidence pack.</p>
  </section>

  <section class="research-canvas__inventory" id="factory-model" data-reveal>
    <header><p class="research-canvas__eyebrow">Operating model</p><h2>Organise by load contract and dependency, not only by module.</h2></header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/design-register/"><span>REG</span><strong>Object register</strong><small>Every object has scope, target contract, owner, predecessors, mapping version, volume, delta, reconciliation and fallback.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="#roles"><span>OWN</span><strong>Named ownership</strong><small>Source, target functional, technical load, reconciliation, business acceptance and cutover decision roles are explicit.</small><i class="material-symbols-outlined" aria-hidden="true">person</i></a>
      <a href="/labs/enterprise-context/migration/domain-playbooks/#waves"><span>DEP</span><strong>Dependency board</strong><small>Objects are released by predecessor readiness instead of independent module calendars.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#cycles"><span>RUN</span><strong>Mock-cycle cadence</strong><small>Each cycle has frozen inputs, versioned logic, entry criteria, measured runtime, reconciliation and a defined learning objective.</small><i class="material-symbols-outlined" aria-hidden="true">repeat</i></a>
      <a href="#defects"><span>DEF</span><strong>Defect control</strong><small>Classify the cause once, fix the governing rule, rerun affected scope and prove that the defect does not return.</small><i class="material-symbols-outlined" aria-hidden="true">bug_report</i></a>
      <a href="#freeze"><span>FRZ</span><strong>Design freeze</strong><small>Freeze only after release contract, mappings, dependency, volume, delta and acceptance proof have converged.</small><i class="material-symbols-outlined" aria-hidden="true">lock</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="roles" data-reveal>
    <header><p class="research-canvas__eyebrow">Ownership</p><h2>A RACI is useful only when it answers real cutover questions.</h2></header>
    <div class="research-route-list">
      <a href="#roles"><span>SRC</span><strong>Source owner</strong><small>Explains source semantics, validates population rules, owns source remediation and signs the closing source control total.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="#roles"><span>FUNC</span><strong>Target functional owner</strong><small>Owns target business meaning, configuration prerequisites, mapping decisions, expected derivations and process validation.</small><i class="material-symbols-outlined" aria-hidden="true">settings</i></a>
      <a href="#roles"><span>ENG</span><strong>Migration engineering</strong><small>Owns extraction, transformation, staging or API execution, version control, automation, run logs and repeatability.</small><i class="material-symbols-outlined" aria-hidden="true">terminal</i></a>
      <a href="#roles"><span>FIN</span><strong>Finance control owner</strong><small>Owns subledger-to-G/L, inventory valuation, migration clearing and financial opening acceptance where the object has accounting impact.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
      <a href="#roles"><span>BUS</span><strong>Business acceptance owner</strong><small>Signs the operational outcome: the migrated object can support the day-one business process.</small><i class="material-symbols-outlined" aria-hidden="true">verified_user</i></a>
      <a href="#roles"><span>LEAD</span><strong>Migration Lead</strong><small>Owns integrated scope, dependency sequence, run model, unresolved risk, cutover evidence and escalation to the go/no-go authority.</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="environments" data-reveal>
    <header><p class="research-canvas__eyebrow">Environment strategy</p><h2>Test the migration design in the same lifecycle used for production.</h2></header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/cd29e96c4def4037a9f62820d72fd4ee.html" target="_blank" rel="noopener"><span>PUB</span><strong>Public Edition: project lifecycle matters</strong><small>Current 2608 guidance describes creating the migration project in the development system, transporting it to test for test migration, and then transporting the successful project to production.</small><i class="material-symbols-outlined" aria-hidden="true">cloud</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/29193bf0ebdd4583930b2176cb993268/c67e14ff693e423aae2b96d9f3b0fc91.html" target="_blank" rel="noopener"><span>ONP</span><strong>S/4HANA / Private: test-cycle project discipline</strong><small>Current S/4HANA 2025 guidance describes test migration in a production-like test system and typically creating a new migration project for each new test transfer with the corrections learned from the previous run.</small><i class="material-symbols-outlined" aria-hidden="true">dns</i></a>
      <a href="#environments"><span>DATA</span><strong>Keep test data representative</strong><small>Use realistic key distributions, document size, custom fields, currencies, organisational scope and known exception classes. Tiny clean samples are not volume proof.</small><i class="material-symbols-outlined" aria-hidden="true">dataset</i></a>
      <a href="#environments"><span>CFG</span><strong>Control configuration drift</strong><small>A migration mock against different number ranges, valuation, document types or organisational settings can pass and still teach the wrong lesson.</small><i class="material-symbols-outlined" aria-hidden="true">difference</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="cycles" data-reveal>
    <header><p class="research-canvas__eyebrow">Mock cycles</p><h2>Each cycle has a question to answer.</h2></header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/cutover/#rehearsal"><span>M0</span><strong>Object prototype</strong><small>Question: can the target state be represented with the selected migration object or API, including keys and extensions?</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#rehearsal"><span>M1</span><strong>Integrated dependency run</strong><small>Question: do predecessors, generated target keys and cross-domain references work in the real sequence?</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#performance"><span>M2</span><strong>Production-volume run</strong><small>Question: does extraction → transformation → load → post-processing → reconciliation fit the window with contingency?</small><i class="material-symbols-outlined" aria-hidden="true">speed</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#delta"><span>M3</span><strong>Delta rehearsal</strong><small>Question: can the baseline and final changes close without duplicates, missed changes or unclear source/target authority?</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#go-no-go"><span>M4</span><strong>Full cutover rehearsal</strong><small>Question: can the real people, controls, timings, interfaces, reconciliation and decision gates execute as one runbook?</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="defects" data-reveal>
    <header><p class="research-canvas__eyebrow">Defect burn-down</p><h2>Track causes, not only failed rows.</h2></header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/cutover/#errors"><span>DATA</span><strong>Source data</strong><small>Invalid or missing source values, duplicates or inconsistent relationships. Decide whether to remediate source or transform deliberately.</small><i class="material-symbols-outlined" aria-hidden="true">data_alert</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#errors"><span>MAP</span><strong>Mapping or transformation</strong><small>A governing rule is wrong or incomplete. Correct the versioned rule and rerun all records affected by it.</small><i class="material-symbols-outlined" aria-hidden="true">transform</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#errors"><span>CFG</span><strong>Target configuration</strong><small>Missing organisation, account, scope, number range or process setup. Fix through the implementation configuration path.</small><i class="material-symbols-outlined" aria-hidden="true">settings</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#errors"><span>DEP</span><strong>Dependency</strong><small>Parent object or target key is missing. Do not patch child data to hide a broken load sequence.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/labs/enterprise-context/migration/api-led-migration/#recovery"><span>TECH</span><strong>Execution or interface</strong><small>Transient error, throttling, timeout or uncertain API result needs a restart rule that protects against duplicates.</small><i class="material-symbols-outlined" aria-hidden="true">sync_problem</i></a>
      <a href="#defects"><span>SCOPE</span><strong>Business exception</strong><small>The source record may be valid but out of agreed target scope. Route it to an explicit business decision instead of calling it a technical defect.</small><i class="material-symbols-outlined" aria-hidden="true">gavel</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="metrics" data-reveal>
    <header><p class="research-canvas__eyebrow">Factory metrics</p><h2>Measure convergence, not activity.</h2></header>
    <div class="research-route-list">
      <a href="#metrics"><span>FP</span><strong>First-pass acceptance</strong><small>Share of selected instances accepted without repair. Use by object and defect class; do not hide recurring mapping defects behind final 100% success.</small><i class="material-symbols-outlined" aria-hidden="true">check_circle</i></a>
      <a href="#metrics"><span>REC</span><strong>Reconciliation pass rate</strong><small>How many object controls pass without unexplained differences: key-set, quantity, value, finance and process proof.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
      <a href="#metrics"><span>RUN</span><strong>Runtime trend</strong><small>Track the same production-like workload across cycles. Runtime improvement is useful only if scope and control quality remain comparable.</small><i class="material-symbols-outlined" aria-hidden="true">timer</i></a>
      <a href="#metrics"><span>DEF</span><strong>Repeat-defect rate</strong><small>A defect that returns after it was marked fixed is evidence that the governing rule or regression control is weak.</small><i class="material-symbols-outlined" aria-hidden="true">replay</i></a>
      <a href="#metrics"><span>OPEN</span><strong>Critical unresolved exceptions</strong><small>Count by business impact and owner, not only severity labels. A small number can still block a dependency wave or financial sign-off.</small><i class="material-symbols-outlined" aria-hidden="true">priority_high</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="freeze" data-reveal>
    <header><p class="research-canvas__eyebrow">Design freeze</p><h2>Freeze a proved baseline, not a calendar date.</h2></header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/design-register/#gates"><span>OBJ</span><strong>Object contracts accepted</strong><small>Exact release, scope, dependencies, mappings, volume, delta, reconciliation and fallback are signed or have visible residual risk.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
      <a href="#freeze"><span>CHG</span><strong>Change control starts</strong><small>After freeze, a mapping, selection rule, object version or configuration change needs impact analysis and targeted regression.</small><i class="material-symbols-outlined" aria-hidden="true">change_circle</i></a>
      <a href="#freeze"><span>BASE</span><strong>Production baseline identified</strong><small>The cutover run points to known versions of transformations, Migration Cockpit project/content, API adapter, reconciliation queries and runbook.</small><i class="material-symbols-outlined" aria-hidden="true">label</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#recovery"><span>STOP</span><strong>Recovery decisions frozen</strong><small>Last safe stop points, fallback paths and authority decisions are agreed before production data starts moving.</small><i class="material-symbols-outlined" aria-hidden="true">stop_circle</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="evidence" data-reveal>
    <header><p class="research-canvas__eyebrow">Evidence retention</p><h2>SAP logs help operate the run. Your programme still needs its own evidence pack.</h2></header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/160335a19109485e9d96f5824f71de3d.html" target="_blank" rel="noopener"><span>180D</span><strong>Public Edition migration messages are retained for 180 days</strong><small>Current 2608 guidance states that migration messages are permanently deleted after the retention period. Do not make long-term audit evidence depend only on the live migration project messages.</small><i class="material-symbols-outlined" aria-hidden="true">history</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#decommission"><span>PACK</span><strong>Archive the migration record</strong><small>Keep final source controls, mapping versions, target keys, load statistics, reconciliation results, approved exceptions, sign-offs and relevant run evidence under project retention rules.</small><i class="material-symbols-outlined" aria-hidden="true">folder</i></a>
      <a href="/labs/enterprise-context/migration/api-led-migration/#execution-ledger"><span>API</span><strong>Keep API execution lineage</strong><small>For API-led loads, preserve request identity, source key, target key, response class and final reconciled state without retaining credentials or unnecessary sensitive payloads.</small><i class="material-symbols-outlined" aria-hidden="true">receipt_long</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="daily" data-reveal>
    <header><p class="research-canvas__eyebrow">Cutover control room</p><h2>During cutover, report decisions and blockers, not presentation slides.</h2></header>
    <div class="research-route-list">
      <a href="#daily"><span>STAT</span><strong>Object state</strong><small>Not started, running, blocked, technically complete, reconciled, accepted. Keep “complete” separate from “accepted”.</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
      <a href="#daily"><span>PATH</span><strong>Critical path</strong><small>Which blocked object delays stock, open transactions, financial opening or business release?</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="#daily"><span>TIME</span><strong>Forecast vs recovery point</strong><small>Use measured runtime to forecast completion and compare it with the last safe stop point, not only the planned finish time.</small><i class="material-symbols-outlined" aria-hidden="true">schedule</i></a>
      <a href="#daily"><span>DEC</span><strong>Open decisions</strong><small>Every exception above threshold has an owner, decision deadline and impact on go/no-go.</small><i class="material-symbols-outlined" aria-hidden="true">gavel</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#go-no-go"><span>GO</span><strong>Evidence gates</strong><small>Technical, data, finance, process and decision gates stay visible until business release.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="assessment" data-reveal>
    <header><p class="research-canvas__eyebrow">Lead assessment</p><h2>Explain the factory in one minute.</h2></header>
    <div class="research-route-list">
      <a href="#assessment"><span>1</span><strong>One object register</strong><small>Every object has a verified target contract, owner, dependency, volume, delta, recovery and acceptance proof.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="#assessment"><span>2</span><strong>Mocks answer questions</strong><small>Prototype semantics, then dependencies, volume, delta and full cutover. Each cycle closes a specific uncertainty.</small><i class="material-symbols-outlined" aria-hidden="true">repeat</i></a>
      <a href="#assessment"><span>3</span><strong>Defects fix rules</strong><small>Classify root cause and change the governing mapping, source, configuration or dependency rule instead of repeatedly repairing rows.</small><i class="material-symbols-outlined" aria-hidden="true">bug_report</i></a>
      <a href="#assessment"><span>4</span><strong>Freeze on evidence</strong><small>Only a production-like, reconciled and recoverable baseline becomes the cutover version.</small><i class="material-symbols-outlined" aria-hidden="true">lock</i></a>
      <a href="#assessment"><span>5</span><strong>Release on business proof</strong><small>The factory is successful when the target state is accepted and executable, not when loaders finish.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>