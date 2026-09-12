---
layout: default
title: "SAP S/4HANA Migration Cutover — Rehearsal, Delta and Reconciliation"
description: "S/4HANA migration cutover playbook for mock loads, freeze and delta, recovery, reconciliation, go/no-go, hypercare, and decommissioning."
permalink: /labs/enterprise-context/migration/cutover/
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
  - cutover
  - reconciliation
  - hypercare
career_impact: mapped
career_skills:
  - delivery-release
  - integration-recovery
  - logistics-inventory
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/migration/">S/4HANA Migration</a></li><li aria-current="page">Cutover and Reconciliation</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Greenfield migration / Cutover</p>
      <h1>The load finishes<br />before cutover is approved.</h1>
      <p>A migration is ready when freeze, extraction, transformation, target loads, reconciliation, interfaces and business controls can run inside the cutover window with measured evidence. Production should be the most controlled rehearsal, not the first real run.</p>
      <a class="research-canvas__button" href="#rehearsal">Build the rehearsal loop <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Cutover gates">
      <p>Release gates</p>
      <div class="research-canvas__signal-line"><span>1</span><strong>Load</strong><small>Technical completion</small></div>
      <div class="research-canvas__signal-line"><span>2</span><strong>Tie</strong><small>Business reconciliation</small></div>
      <div class="research-canvas__signal-line"><span>3</span><strong>Release</strong><small>Signed go/no-go</small></div>
      <em>No business release on green technical status alone.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">timer</span>
    <p><strong>Cutover is an execution product.</strong> It has a versioned plan, prerequisites, owners, timings, checkpoints, evidence, stop conditions and recovery decisions.</p>
    <p><strong>Rollback is object-specific.</strong> Do not assume migrated masters, stock or accounting data can simply be deleted. Define the last safe stop point before production starts.</p>
  </section>

  <section class="research-canvas__inventory" id="rehearsal" data-reveal>
    <header><p class="research-canvas__eyebrow">Rehearsal loop</p><h2>Each mock must remove uncertainty.</h2></header>
    <div class="research-route-list">
      <a href="#rehearsal"><span>M0</span><strong>Object prototype</strong><small>Small data set: prove target semantics, mappings, legacy key handling, extensions and basic controls.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="#rehearsal"><span>M1</span><strong>Integrated mock</strong><small>Run dependent objects in sequence and test cross-object references and representative end-to-end processes.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#rehearsal"><span>M2</span><strong>Production-volume mock</strong><small>Measure extraction, transformation, staging, simulation, migration, post-processing and reconciliation with realistic volume.</small><i class="material-symbols-outlined" aria-hidden="true">speed</i></a>
      <a href="#rehearsal"><span>M3</span><strong>Full cutover rehearsal</strong><small>Use the real runbook, owners, freeze/delta model, interface sequence, evidence pack and go/no-go process.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="#rehearsal"><span>EXIT</span><strong>Readiness is an exit criterion</strong><small>Critical defects closed, mappings stable, runtime inside the window with contingency, reconciliation passed and recovery tested.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="freeze" data-reveal>
    <header><p class="research-canvas__eyebrow">Freeze</p><h2>Control the source before the load.</h2></header>
    <div class="research-route-list">
      <a href="#freeze"><span>FULL</span><strong>Full freeze</strong><small>Stop relevant business changes before final extraction. Simplest reconciliation, highest business outage.</small><i class="material-symbols-outlined" aria-hidden="true">pause_circle</i></a>
      <a href="#delta"><span>DELTA</span><strong>Snapshot plus delta</strong><small>Take a base extract earlier and capture controlled changes until final cut-off. Lower outage, more engineering risk.</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a>
      <a href="#freeze"><span>AREA</span><strong>Selective freeze</strong><small>Freeze only clean organisational/business boundaries when the source can enforce them reliably.</small><i class="material-symbols-outlined" aria-hidden="true">select_check_box</i></a>
      <a href="#inventory-freeze"><span>STOCK</span><strong>Stock freeze</strong><small>Goods movements need stricter control because late postings change physical quantity and accounting value.</small><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="delta" data-reveal>
    <header><p class="research-canvas__eyebrow">Delta design</p><h2>Define the delta per object.</h2></header>
    <div class="research-route-list">
      <a href="#delta"><span>KEY</span><strong>Change detection</strong><small>Define timestamp, change pointer, document-change source or extractor watermark and how inserts, updates and deletions are represented.</small><i class="material-symbols-outlined" aria-hidden="true">key</i></a>
      <a href="#delta"><span>ACT</span><strong>Delta action</strong><small>For each object decide create, supported update, staging replacement, cancellation/recreation, skip or route to production integration.</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      <a href="#delta"><span>LOCK</span><strong>Watermark ownership</strong><small>Do not advance the extraction watermark until the batch is accepted.</small><i class="material-symbols-outlined" aria-hidden="true">lock_clock</i></a>
      <a href="#delta"><span>DUP</span><strong>Duplicate control</strong><small>Use source key, run ID and target status so a retry cannot silently become a second creation.</small><i class="material-symbols-outlined" aria-hidden="true">content_copy</i></a>
      <a href="#delta"><span>END</span><strong>Final delta closes authority</strong><small>After the accepted final delta, stop source creation for that scope or route all new business to S/4.</small><i class="material-symbols-outlined" aria-hidden="true">check_circle</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="inventory-freeze" data-reveal>
    <header><p class="research-canvas__eyebrow">Inventory</p><h2>Stock needs a tighter clock than most master data.</h2></header>
    <div class="research-route-list">
      <a href="#inventory-freeze"><span>1</span><strong>Reduce movements</strong><small>Finish inbound, outbound, transfer and production postings where possible and drain posting queues.</small><i class="material-symbols-outlined" aria-hidden="true">move_down</i></a>
      <a href="#inventory-freeze"><span>2</span><strong>Take the exact snapshot</strong><small>Record product, plant, storage location, batch, stock status, special stock, valuation type and other target dimensions.</small><i class="material-symbols-outlined" aria-hidden="true">photo_camera</i></a>
      <a href="#inventory-freeze"><span>3</span><strong>Load and value</strong><small>Post initial stock using the agreed date, stock categories and valuation logic.</small><i class="material-symbols-outlined" aria-hidden="true">payments</i></a>
      <a href="#reconciliation"><span>4</span><strong>Reconcile physical, IM and G/L</strong><small>Quantity, value and accounting differences are separate defect classes.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
      <a href="#go-no-go"><span>5</span><strong>Release movements last</strong><small>Open business posting only after stock and financial controls pass.</small><i class="material-symbols-outlined" aria-hidden="true">play_circle</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="run-control" data-reveal>
    <header><p class="research-canvas__eyebrow">Run control</p><h2>Every step needs entry, exit, owner and evidence.</h2></header>
    <div class="research-route-list">
      <a href="#run-control"><span>ID</span><strong>Run identity</strong><small>Record run ID, migration project/object version, mapping version, source snapshot and staging/file batch.</small><i class="material-symbols-outlined" aria-hidden="true">tag</i></a>
      <a href="#run-control"><span>PRE</span><strong>Entry criteria</strong><small>Predecessors accepted, source extract complete, target ready, authorisations active and required interfaces controlled.</small><i class="material-symbols-outlined" aria-hidden="true">login</i></a>
      <a href="#run-control"><span>RUN</span><strong>Execution evidence</strong><small>Capture start/end, counts, errors, warnings, corrections and retries plus independent control totals.</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
      <a href="#run-control"><span>POST</span><strong>Exit criteria</strong><small>Technical processing complete, critical errors resolved, reconciliation passed and successor object cleared.</small><i class="material-symbols-outlined" aria-hidden="true">logout</i></a>
      <a href="#run-control"><span>STOP</span><strong>Stop condition</strong><small>Wrong snapshot, wrong mapping, systemic target error, control breach or runtime beyond the recovery point must stop the line.</small><i class="material-symbols-outlined" aria-hidden="true">stop_circle</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="performance" data-reveal>
    <header><p class="research-canvas__eyebrow">Performance</p><h2>Measure the whole path.</h2></header>
    <div class="research-route-list">
      <a href="#performance"><span>EXT</span><strong>Extraction</strong><small>Large source joins and late cleansing can consume the outage before SAP processing starts.</small><i class="material-symbols-outlined" aria-hidden="true">download</i></a>
      <a href="#performance"><span>TRN</span><strong>Transformation</strong><small>Profile mapping, deduplication, validation and staging generation with deterministic parallelism.</small><i class="material-symbols-outlined" aria-hidden="true">transform</i></a>
      <a href="#performance"><span>SAP</span><strong>Simulation and migration</strong><small>Measure every critical migration object with production-like volume and target capacity.</small><i class="material-symbols-outlined" aria-hidden="true">speed</i></a>
      <a href="#performance"><span>REC</span><strong>Reconciliation</strong><small>Protect time for business and finance controls; do not give the entire contingency window to loading.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="#performance"><span>BUF</span><strong>Contingency</strong><small>A plan that works only at the best measured runtime is not ready.</small><i class="material-symbols-outlined" aria-hidden="true">schedule</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="errors" data-reveal>
    <header><p class="research-canvas__eyebrow">Errors</p><h2>Classify before retry.</h2></header>
    <div class="research-route-list">
      <a href="#errors"><span>DATA</span><strong>Data defect</strong><small>Bad source value, duplicate, invalid reference, format or missing mapping. Fix the governed rule, not only one row.</small><i class="material-symbols-outlined" aria-hidden="true">data_alert</i></a>
      <a href="#errors"><span>CFG</span><strong>Configuration defect</strong><small>Missing organisation, account, number range, scope or process setting; fix through approved configuration governance.</small><i class="material-symbols-outlined" aria-hidden="true">settings</i></a>
      <a href="#errors"><span>DEP</span><strong>Dependency defect</strong><small>Predecessor master or key mapping is missing; fix the parent before retrying the child.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#errors"><span>TECH</span><strong>Technical transient</strong><small>Retry only after the target processing state is known and duplicate creation is controlled.</small><i class="material-symbols-outlined" aria-hidden="true">sync_problem</i></a>
      <a href="#errors"><span>BUS</span><strong>Business exception</strong><small>A technically valid record may still be out of scope; business owner approves exclude, recreate or manual treatment.</small><i class="material-symbols-outlined" aria-hidden="true">gavel</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="reconciliation" data-reveal>
    <header><p class="research-canvas__eyebrow">Reconciliation</p><h2>Use several proofs for the same business state.</h2></header>
    <div class="research-route-list">
      <a href="#reconciliation"><span>KEY</span><strong>Key-set</strong><small>Source selected = target migrated + approved exclusions/recreations + unresolved defects.</small><i class="material-symbols-outlined" aria-hidden="true">key</i></a>
      <a href="#reconciliation"><span>SUM</span><strong>Control totals</strong><small>Quantity, value, open amount, balance, acquisition value, depreciation and other object-specific sums.</small><i class="material-symbols-outlined" aria-hidden="true">functions</i></a>
      <a href="#reconciliation"><span>DIST</span><strong>Distribution</strong><small>Compare by company code, plant, sales organisation, customer, supplier, currency, stock status, aging bucket or asset class.</small><i class="material-symbols-outlined" aria-hidden="true">bar_chart</i></a>
      <a href="#reconciliation"><span>REF</span><strong>References</strong><small>Open transactions point to valid target masters and generated target IDs remain traceable to source keys.</small><i class="material-symbols-outlined" aria-hidden="true">link</i></a>
      <a href="#reconciliation"><span>PROC</span><strong>Process execution</strong><small>Representative migrated data can continue through O2C, P2P, production, warehouse and clearing processes.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="#financial-proof"><span>FIN</span><strong>Financial tie-out</strong><small>Trial balance, AR/AP, assets, inventory value and migration clearing accounts explain the approved opening position.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="financial-proof" data-reveal>
    <header><p class="research-canvas__eyebrow">Financial proof</p><h2>Finance signs the opening position.</h2></header>
    <div class="research-route-list">
      <a href="#financial-proof"><span>TB</span><strong>Trial balance</strong><small>Source close and target opening reconcile by company code, ledger, currency and agreed dimensions.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
      <a href="#financial-proof"><span>AR</span><strong>AR ↔ G/L</strong><small>Customer open items and aging reconcile to control accounts.</small><i class="material-symbols-outlined" aria-hidden="true">payments</i></a>
      <a href="#financial-proof"><span>AP</span><strong>AP ↔ G/L</strong><small>Supplier open items and aging reconcile to control accounts.</small><i class="material-symbols-outlined" aria-hidden="true">receipt</i></a>
      <a href="#financial-proof"><span>AA</span><strong>Assets ↔ G/L</strong><small>Asset acquisition/depreciation values reconcile to asset accounts.</small><i class="material-symbols-outlined" aria-hidden="true">apartment</i></a>
      <a href="#financial-proof"><span>INV</span><strong>Inventory ↔ G/L</strong><small>Loaded stock value and material valuation reconcile to inventory accounts.</small><i class="material-symbols-outlined" aria-hidden="true">inventory</i></a>
      <a href="#financial-proof"><span>CLR</span><strong>Migration clearing</strong><small>Every clearing account has an expected final state and zero-balance gates are explicit.</small><i class="material-symbols-outlined" aria-hidden="true">check_circle</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="go-no-go" data-reveal>
    <header><p class="research-canvas__eyebrow">Go / no-go</p><h2>Release the business on evidence.</h2></header>
    <div class="research-route-list">
      <a href="#go-no-go"><span>TECH</span><strong>Technical gate</strong><small>Critical jobs complete, target state known, interfaces ready, monitoring active and platform stable.</small><i class="material-symbols-outlined" aria-hidden="true">dns</i></a>
      <a href="#go-no-go"><span>DATA</span><strong>Data gate</strong><small>Object reconciliation passes thresholds, critical defects are closed and source-to-target lineage is complete.</small><i class="material-symbols-outlined" aria-hidden="true">dataset</i></a>
      <a href="#go-no-go"><span>FIN</span><strong>Finance gate</strong><small>Opening position and subledger/G/L controls are approved.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
      <a href="#go-no-go"><span>PROC</span><strong>Process gate</strong><small>Critical end-to-end smoke tests succeed on migrated data.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="#go-no-go"><span>LEAD</span><strong>Decision gate</strong><small>Residual risks, defects, workarounds and owners are visible to the named decision authority.</small><i class="material-symbols-outlined" aria-hidden="true">gavel</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="recovery" data-reveal>
    <header><p class="research-canvas__eyebrow">Recovery</p><h2>Define the last safe stop point before production starts.</h2></header>
    <div class="research-route-list">
      <a href="#recovery"><span>PRE</span><strong>Abort before release</strong><small>Keep legacy authoritative when a critical gate fails before target business use starts.</small><i class="material-symbols-outlined" aria-hidden="true">cancel</i></a>
      <a href="#recovery"><span>SYS</span><strong>Restore or rebuild</strong><small>Where the platform and operating contract support it, a pre-cutover restore/rebuild can provide a clean technical reset.</small><i class="material-symbols-outlined" aria-hidden="true">restore</i></a>
      <a href="#recovery"><span>OBJ</span><strong>Object correction</strong><small>After accepted creation, use supported correction/reversal paths; some masters cannot be deleted once referenced.</small><i class="material-symbols-outlined" aria-hidden="true">build</i></a>
      <a href="#recovery"><span>DUAL</span><strong>Avoid uncontrolled dual operation</strong><small>Do not let ECC and S/4 accept the same business scope without a designed coexistence model.</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="hypercare" data-reveal>
    <header><p class="research-canvas__eyebrow">Hypercare</p><h2>Keep migration traceability after day one.</h2></header>
    <div class="research-route-list">
      <a href="#hypercare"><span>XREF</span><strong>Key lookup</strong><small>Support can trace legacy customer, supplier, product, order or asset to its target identity.</small><i class="material-symbols-outlined" aria-hidden="true">key</i></a>
      <a href="#hypercare"><span>TAG</span><strong>Migration-origin evidence</strong><small>Keep run ID, mapping version and source snapshot so production and migration defects can be separated.</small><i class="material-symbols-outlined" aria-hidden="true">tag</i></a>
      <a href="#hypercare"><span>KPI</span><strong>Business outcomes</strong><small>Watch order failures, blocks, PO errors, stock differences, posting errors and integration backlog—not only row counts.</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
      <a href="#decommission"><span>EXIT</span><strong>Close deliberately</strong><small>Set criteria for retiring temporary tools, access, staging and migration support ownership.</small><i class="material-symbols-outlined" aria-hidden="true">flag</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="history" data-reveal>
    <header><p class="research-canvas__eyebrow">Historical data</p><h2>Retain history without turning S/4 into a legacy archive.</h2></header>
    <div class="research-route-list">
      <a href="#history"><span>LAW</span><strong>Retention first</strong><small>Define legal, tax, audit and business-access periods. Retention does not automatically require old transactions inside new S/4 operational tables.</small><i class="material-symbols-outlined" aria-hidden="true">policy</i></a>
      <a href="#history"><span>READ</span><strong>Read-only legacy</strong><small>Keep the old ERP under controlled read-only access where this meets audit and support needs.</small><i class="material-symbols-outlined" aria-hidden="true">visibility</i></a>
      <a href="#history"><span>ARCH</span><strong>Archive or data platform</strong><small>Preserve keys, lineage, authorisation and retention controls in the chosen history solution.</small><i class="material-symbols-outlined" aria-hidden="true">archive</i></a>
      <a href="#history"><span>LINK</span><strong>Make history searchable</strong><small>Users must be able to find old documents by legacy keys, business partner, product and date.</small><i class="material-symbols-outlined" aria-hidden="true">search</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="decommission" data-reveal>
    <header><p class="research-canvas__eyebrow">Closure</p><h2>Temporary migration access must end.</h2></header>
    <div class="research-route-list">
      <a href="#decommission"><span>ACC</span><strong>Remove temporary users</strong><small>Revoke broad migration roles after the approved support window.</small><i class="material-symbols-outlined" aria-hidden="true">person_remove</i></a>
      <a href="#decommission"><span>CONN</span><strong>Remove temporary connections</strong><small>Close source DB access, RFC destinations, staging credentials, API users and firewall rules no longer required.</small><i class="material-symbols-outlined" aria-hidden="true">link_off</i></a>
      <a href="#decommission"><span>DATA</span><strong>Apply staging retention</strong><small>Keep only the evidence required by project, audit and legal policy.</small><i class="material-symbols-outlined" aria-hidden="true">delete_sweep</i></a>
      <a href="#decommission"><span>DOC</span><strong>Archive the evidence pack</strong><small>Final mappings, control totals, key maps, load statistics, reconciliations, exceptions and approvals form the migration record.</small><i class="material-symbols-outlined" aria-hidden="true">folder</i></a>
      <a href="#decommission"><span>OWN</span><strong>Transfer surviving flows</strong><small>Anything that continues after go-live moves to a production integration owner.</small><i class="material-symbols-outlined" aria-hidden="true">handshake</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
