---
layout: default
title: "SAP S/4HANA Migration Cutover — Rehearsal, Delta and Reconciliation"
description: "A Lead-level cutover playbook for S/4HANA data migration: mock loads, freeze and delta, run control, recovery, reconciliation, go/no-go, hypercare and decommissioning."
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
      <h1>The load finishes<br />before the cutover is approved.</h1>
      <p>A migration is ready when source freeze, extraction, transformation, target loads, reconciliation, interfaces and business controls can be executed inside the cutover window with measured evidence. The final weekend should be the most controlled rehearsal, not the first real run.</p>
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
    <p><strong>Cutover is an execution product.</strong> It has a versioned plan, prerequisites, owners, timings, checkpoints, entry and exit criteria, recovery decisions and evidence.</p>
    <p><strong>Rollback is object-specific.</strong> You cannot assume that migrated Business Partners, products, accounting documents or stock can simply be deleted. The safest recovery strategy is designed before production: abort before release, restore/rebuild where technically supported, correct controlled errors, or execute an approved business reversal path.</p>
  </section>

  <section class="research-canvas__inventory" id="rehearsal" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Rehearsal loop</p>
      <h2>Each mock must remove uncertainty.</h2>
      <p>There is no magic number of mock loads. Stop counting cycles and start measuring readiness.</p>
    </header>
    <div class="research-route-list">
      <a href="#rehearsal"><span>M0</span><strong>Object prototype</strong><small>Small data set. Prove the migration object, target semantics, mapping approach, legacy key handling, custom fields and basic reconciliation.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="#rehearsal"><span>M1</span><strong>Integrated mock</strong><small>Run multiple dependent objects in target sequence. Prove cross-object references, error handling and basic end-to-end process execution.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#rehearsal"><span>M2</span><strong>Production-volume rehearsal</strong><small>Use realistic volume and parallelism. Measure extraction, transformation, staging, simulation, migration, post-processing and reconciliation.</small><i class="material-symbols-outlined" aria-hidden="true">speed</i></a>
      <a href="#rehearsal"><span>M3</span><strong>Full cutover rehearsal</strong><small>Use the cutover runbook, real owner model, freeze/delta logic, interface sequence, evidence pack and go/no-go meeting. The sequence should be executable without tribal knowledge.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="#rehearsal"><span>EXIT</span><strong>Ready means stable</strong><small>Critical defects closed, mappings frozen, runtime inside the window with contingency, reconciliation thresholds met, recovery decisions tested and owners trained.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="freeze" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Freeze strategy</p>
      <h2>Control the source before you control the load.</h2>
    </header>
    <div class="research-route-list">
      <a href="#freeze"><span>FULL</span><strong>Full business freeze</strong><small>Stop relevant business postings before final extraction. Simple to reconcile, expensive for the business. Use where outage is acceptable and delta complexity is high.</small><i class="material-symbols-outlined" aria-hidden="true">pause_circle</i></a>
      <a href="#delta"><span>DELTA</span><strong>Snapshot plus delta</strong><small>Take an earlier base extraction, keep the source operating, then capture changes since the snapshot. Better outage, more engineering and reconciliation complexity.</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a>
      <a href="#freeze"><span>AREA</span><strong>Selective freeze</strong><small>Freeze only chosen company codes, plants, sales organisations or business activities while other areas continue. Useful only when organisational boundaries are clean enough to control.</small><i class="material-symbols-outlined" aria-hidden="true">select_check_box</i></a>
      <a href="#inventory-freeze"><span>STOCK</span><strong>Physical stock freeze</strong><small>Goods movements need stricter control than ordinary master changes because every late movement can change both quantity and accounting value.</small><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="delta" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Delta design</p>
      <h2>A delta must be defined per object.</h2>
      <p>“We will take the delta on Friday” is not a design.</p>
    </header>
    <div class="research-route-list">
      <a href="#delta"><span>KEY</span><strong>Change detection</strong><small>Define the source timestamp, change pointer, document-change table, extractor watermark or other reliable mechanism. Know how inserts, updates and deletions are represented.</small><i class="material-symbols-outlined" aria-hidden="true">key</i></a>
      <a href="#delta"><span>TYPE</span><strong>Delta action</strong><small>For each object decide create, replace staging row, supported update, cancellation/recreation, skip or route to a separate production integration.</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      <a href="#delta"><span>LOCK</span><strong>Watermark ownership</strong><small>Record the exact extraction cut-off and do not advance it until the batch is accepted. This prevents silent data gaps after a retry.</small><i class="material-symbols-outlined" aria-hidden="true">lock_clock</i></a>
      <a href="#delta"><span>DUP</span><strong>Duplicate control</strong><small>Every rerunnable step needs a source business key, run ID and target status so the team can distinguish retry from duplicate creation.</small><i class="material-symbols-outlined" aria-hidden="true">content_copy</i></a>
      <a href="#delta"><span>END</span><strong>Final delta closes the source</strong><small>After the final accepted delta, the source population is frozen for the migrated business scope or all new transactions are routed to the target.</small><i class="material-symbols-outlined" aria-hidden="true">check_circle</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="inventory-freeze" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Inventory cutover</p>
      <h2>Stock needs a tighter clock than most master data.</h2>
    </header>
    <div class="research-route-list">
      <a href="#inventory-freeze"><span>1</span><strong>Reduce movements</strong><small>Complete inbound, outbound, transfer and production movements before the freeze where possible. Close queues and interface backlogs that could post late stock changes.</small><i class="material-symbols-outlined" aria-hidden="true">move_down</i></a>
      <a href="#inventory-freeze"><span>2</span><strong>Take the source stock snapshot</strong><small>Record quantity by the exact dimensions required by the target: product, plant, storage location, batch, special stock, stock status, valuation type and other relevant keys.</small><i class="material-symbols-outlined" aria-hidden="true">photo_camera</i></a>
      <a href="#inventory-freeze"><span>3</span><strong>Load and value</strong><small>Post the target initial stock with the agreed posting date and valuation logic. Keep the finance team in the same checkpoint.</small><i class="material-symbols-outlined" aria-hidden="true">payments</i></a>
      <a href="#reconciliation"><span>4</span><strong>Reconcile physical, inventory and G/L</strong><small>Quantity differences, value differences and accounting differences are different defect classes. Do not hide one with an adjustment in another layer.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
      <a href="#go-no-go"><span>5</span><strong>Release movements last</strong><small>Allow new goods movements only after stock controls and the related financial checks pass.</small><i class="material-symbols-outlined" aria-hidden="true">play_circle</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="run-control" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Run control</p>
      <h2>Every step has an owner, start gate, end gate and evidence.</h2>
    </header>
    <div class="research-route-list">
      <a href="#run-control"><span>ID</span><strong>Run ID and object version</strong><small>Record cutover run, migration project, object version, mapping version, source snapshot and file or staging batch. Never rely on file names like final_v7_real.csv.</small><i class="material-symbols-outlined" aria-hidden="true">tag</i></a>
      <a href="#run-control"><span>PRE</span><strong>Entry criteria</strong><small>Predecessor objects accepted, source extract complete, mapping version frozen, target configuration open, authorisations active and required interfaces stopped.</small><i class="material-symbols-outlined" aria-hidden="true">login</i></a>
      <a href="#run-control"><span>RUN</span><strong>Execution evidence</strong><small>Start/end time, record count, successful records, errors, warnings, corrections, retry count and operator. Capture SAP migration status plus independent control totals.</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
      <a href="#run-control"><span>POST</span><strong>Exit criteria</strong><small>Technical load complete, critical errors resolved, reconciliation within threshold, target sample approved and successor object cleared to start.</small><i class="material-symbols-outlined" aria-hidden="true">logout</i></a>
      <a href="#run-control"><span>STOP</span><strong>Stop condition</strong><small>Define when the team stops rather than burns the contingency window: wrong source snapshot, wrong mapping version, systemic target error, reconciliation breach or runtime beyond the recovery point.</small><i class="material-symbols-outlined" aria-hidden="true">stop_circle</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="performance" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Performance</p>
      <h2>Measure the whole migration path.</h2>
    </header>
    <div class="research-route-list">
      <a href="#performance"><span>EXT</span><strong>Extraction runtime</strong><small>Measure source query and file generation time. Large source joins and late cleansing can consume the outage before SAP processing starts.</small><i class="material-symbols-outlined" aria-hidden="true">download</i></a>
      <a href="#performance"><span>TRN</span><strong>Transformation runtime</strong><small>Profile mapping, deduplication, validation and staging generation. Parallelise only where dependencies and deterministic results are controlled.</small><i class="material-symbols-outlined" aria-hidden="true">transform</i></a>
      <a href="#performance"><span>SAP</span><strong>Simulation and migration runtime</strong><small>Measure each migration object with production-like volume. Package size, parallel jobs and target-system capacity can materially change the window.</small><i class="material-symbols-outlined" aria-hidden="true">speed</i></a>
      <a href="#performance"><span>REC</span><strong>Reconciliation runtime</strong><small>Do not give all contingency to the load. Business reconciliation, finance checks and sampling need protected time before release.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="#performance"><span>BUF</span><strong>Contingency is designed capacity</strong><small>Keep time for a controlled retry or correction. A plan that works only at the best measured runtime is not ready.</small><i class="material-symbols-outlined" aria-hidden="true">schedule</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="errors" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Error and retry model</p>
      <h2>Recover records without losing the batch story.</h2>
    </header>
    <div class="research-route-list">
      <a href="#errors"><span>DATA</span><strong>Data defect</strong><small>Bad or missing source value, invalid reference, duplicate, bad format or missing mapping. Correct the governed source/transformation rule, not only the one rejected row.</small><i class="material-symbols-outlined" aria-hidden="true">data_alert</i></a>
      <a href="#errors"><span>CFG</span><strong>Target configuration defect</strong><small>Required organisational unit, account, number range, scope or process setting is missing. Fix the target only through the approved implementation/configuration path.</small><i class="material-symbols-outlined" aria-hidden="true">settings</i></a>
      <a href="#errors"><span>DEP</span><strong>Dependency defect</strong><small>Predecessor master or key mapping is missing. Do not retry the child object until the predecessor is accepted.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#errors"><span>TECH</span><strong>Technical transient</strong><small>Timeout, connection issue, job failure or temporary platform problem. Retry only when the target processing state is known and duplicate creation is controlled.</small><i class="material-symbols-outlined" aria-hidden="true">sync_problem</i></a>
      <a href="#errors"><span>BUS</span><strong>Business exception</strong><small>Record is technically valid but no longer belongs in scope. Business owner approves exclusion, manual treatment or redesign and the reconciliation pack records the decision.</small><i class="material-symbols-outlined" aria-hidden="true">gavel</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="reconciliation" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Reconciliation matrix</p>
      <h2>Use several proofs for the same business state.</h2>
      <p>Counts are necessary. Counts alone are weak.</p>
    </header>
    <div class="research-route-list">
      <a href="#reconciliation"><span>KEY</span><strong>Key-set reconciliation</strong><small>Which source business keys should exist in target? Compare source selected, migrated, excluded and unresolved populations.</small><i class="material-symbols-outlined" aria-hidden="true">key</i></a>
      <a href="#reconciliation"><span>SUM</span><strong>Control totals</strong><small>Quantity, value, open amount, balance, acquisition value, depreciation, remaining contract value and other object-specific sums.</small><i class="material-symbols-outlined" aria-hidden="true">functions</i></a>
      <a href="#reconciliation"><span>DIST</span><strong>Distribution checks</strong><small>Compare by company code, plant, sales organisation, supplier, customer, currency, stock status, aging bucket, asset class and other meaningful dimensions.</small><i class="material-symbols-outlined" aria-hidden="true">bar_chart</i></a>
      <a href="#reconciliation"><span>REF</span><strong>Referential checks</strong><small>Every open document references a valid target master. Every internal target number has a traceable source key where the project needs it.</small><i class="material-symbols-outlined" aria-hidden="true">link</i></a>
      <a href="#reconciliation"><span>PROC</span><strong>Process execution checks</strong><small>Representative migrated records can continue through the target process: order-to-cash, procure-to-pay, production, warehouse and finance clearing.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="#financial-proof"><span>FIN</span><strong>Financial tie-out</strong><small>Trial balance, AP, AR, assets, inventory value and migration clearing accounts reconcile to the approved source closing position.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="financial-proof" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Financial proof</p>
      <h2>Finance signs the opening position, not the loader.</h2>
    </header>
    <div class="research-route-list">
      <a href="#financial-proof"><span>TB</span><strong>Trial balance</strong><small>Source close and target opening reconcile by company code, ledger, currency and agreed reporting dimensions.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
      <a href="#financial-proof"><span>AR</span><strong>AR subledger ↔ G/L</strong><small>Customer open items, aging and control-account balances agree.</small><i class="material-symbols-outlined" aria-hidden="true">payments</i></a>
      <a href="#financial-proof"><span>AP</span><strong>AP subledger ↔ G/L</strong><small>Supplier open items, aging and control-account balances agree.</small><i class="material-symbols-outlined" aria-hidden="true">receipt</i></a>
      <a href="#financial-proof"><span>AA</span><strong>Asset subledger ↔ G/L</strong><small>Asset acquisition and depreciation values tie to the related reconciliation accounts.</small><i class="material-symbols-outlined" aria-hidden="true">apartment</i></a>
      <a href="#financial-proof"><span>INV</span><strong>Inventory valuation ↔ G/L</strong><small>Loaded stock value and material valuation agree with inventory accounts after approved cutover postings.</small><i class="material-symbols-outlined" aria-hidden="true">inventory</i></a>
      <a href="#financial-proof"><span>CLR</span><strong>Migration clearing accounts</strong><small>Any migration clearing account has an expected final state. Accounts expected to be zero are explicitly checked before release.</small><i class="material-symbols-outlined" aria-hidden="true">check_circle</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="go-no-go" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Go / no-go</p>
      <h2>Release the business on evidence.</h2>
    </header>
    <div class="research-route-list">
      <a href="#go-no-go"><span>TECH</span><strong>Technical gate</strong><small>Critical migration jobs complete, no unknown processing state, integrations ready, monitoring active and platform stable.</small><i class="material-symbols-outlined" aria-hidden="true">dns</i></a>
      <a href="#go-no-go"><span>DATA</span><strong>Data gate</strong><small>Object-level reconciliation within approved thresholds, critical defects closed and source-to-target lineage complete.</small><i class="material-symbols-outlined" aria-hidden="true">dataset</i></a>
      <a href="#go-no-go"><span>FIN</span><strong>Finance gate</strong><small>Opening position approved, subledgers reconcile and required clearing controls pass.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
      <a href="#go-no-go"><span>PROC</span><strong>Business process gate</strong><small>Critical E2E smoke tests succeed on migrated data and key roles can execute day-one operations.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="#go-no-go"><span>LEAD</span><strong>Decision gate</strong><small>Open risks, residual defects, workarounds, owners and business impact are visible. The decision authority signs go, conditional go or no-go.</small><i class="material-symbols-outlined" aria-hidden="true">gavel</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="recovery" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Recovery and rollback</p>
      <h2>Define the recovery point before production migration starts.</h2>
    </header>
    <div class="research-route-list">
      <a href="#recovery"><span>PRE</span><strong>Abort before business release</strong><small>The simplest decision. Keep the legacy business state authoritative when a critical migration or reconciliation gate fails before users are released.</small><i class="material-symbols-outlined" aria-hidden="true">cancel</i></a>
      <a href="#recovery"><span>SYS</span><strong>System restore or rebuild</strong><small>Where the platform and project support it, a pre-cutover restore/rebuild can be the cleanest technical reset. Feasibility and timing depend on deployment model and operational contract.</small><i class="material-symbols-outlined" aria-hidden="true">restore</i></a>
      <a href="#recovery"><span>OBJ</span><strong>Object-level correction</strong><small>For accepted but wrong records, use the supported business correction or reversal path. Some migrated masters cannot be deleted once referenced.</small><i class="material-symbols-outlined" aria-hidden="true">build</i></a>
      <a href="#recovery"><span>DUAL</span><strong>Avoid uncontrolled dual operation</strong><small>Do not let both ECC and S/4 accept the same business scope without an explicit coexistence architecture. Reconciliation becomes harder every minute.</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      <a href="#recovery"><span>RPO</span><strong>Recovery point is a business decision</strong><small>Define the last moment when the organisation can safely abandon the target cutover and resume legacy processing without losing accepted transactions.</small><i class="material-symbols-outlined" aria-hidden="true">schedule</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="hypercare" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Hypercare</p>
      <h2>Keep migration traceability after day one.</h2>
    </header>
    <div class="research-route-list">
      <a href="#hypercare"><span>XREF</span><strong>Source-to-target key lookup</strong><small>Support teams can trace a legacy customer, product, order or asset to its target identity without asking the migration team.</small><i class="material-symbols-outlined" aria-hidden="true">key</i></a>
      <a href="#hypercare"><span>TAG</span><strong>Migration-origin evidence</strong><small>Keep run IDs, mapping versions and approved source snapshots so a production defect can be separated from a migration defect.</small><i class="material-symbols-outlined" aria-hidden="true">tag</i></a>
      <a href="#hypercare"><span>KPI</span><strong>Watch business outcomes</strong><small>Order failures, delivery blocks, PO errors, stock differences, posting errors, interface backlog and clearing exceptions are more useful than only counting migrated rows.</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
      <a href="#decommission"><span>EXIT</span><strong>Close migration deliberately</strong><small>Define when temporary tools, access, staging data and support ownership can be retired.</small><i class="material-symbols-outlined" aria-hidden="true">flag</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="history" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Historical data</p>
      <h2>Retain history without turning S/4 into a legacy archive.</h2>
    </header>
    <div class="research-route-list">
      <a href="#history"><span>LAW</span><strong>Retention requirement</strong><small>Start with legal, tax, audit and business-access periods. The retention requirement does not automatically require historical transactional data inside the new S/4 operational tables.</small><i class="material-symbols-outlined" aria-hidden="true">policy</i></a>
      <a href="#history"><span>READ</span><strong>Read-only legacy access</strong><small>Keep the old ERP available in a controlled read-only mode where this meets retention, audit and support needs.</small><i class="material-symbols-outlined" aria-hidden="true">visibility</i></a>
      <a href="#history"><span>ARCH</span><strong>Archive or data platform</strong><small>Move retained history into an approved archive or analytics/data platform with preserved keys, lineage, authorisation and retention controls.</small><i class="material-symbols-outlined" aria-hidden="true">archive</i></a>
      <a href="#history"><span>LINK</span><strong>Make history discoverable</strong><small>Users need a simple way to find old documents from legacy numbers, customers, suppliers, products and dates. A retention solution nobody can search is not complete.</small><i class="material-symbols-outlined" aria-hidden="true">search</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="decommission" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Migration closure</p>
      <h2>Temporary migration access must have an end date.</h2>
    </header>
    <div class="research-route-list">
      <a href="#decommission"><span>ACC</span><strong>Remove temporary users and broad roles</strong><small>Migration often needs unusual access. Revoke it after the approved support window.</small><i class="material-symbols-outlined" aria-hidden="true">person_remove</i></a>
      <a href="#decommission"><span>CONN</span><strong>Remove temporary connections</strong><small>Close source database connections, RFC destinations, staging credentials, API users and firewall rules that are no longer needed.</small><i class="material-symbols-outlined" aria-hidden="true">link_off</i></a>
      <a href="#decommission"><span>DATA</span><strong>Apply staging retention</strong><small>Keep only the migration evidence required by the project, audit and legal policy. Do not leave customer data in temporary buckets indefinitely.</small><i class="material-symbols-outlined" aria-hidden="true">delete_sweep</i></a>
      <a href="#decommission"><span>DOC</span><strong>Archive the evidence pack</strong><small>Final mappings, source snapshots or hashes, load statistics, reconciliations, approvals, exceptions, key mapping and support handover form the migration record.</small><i class="material-symbols-outlined" aria-hidden="true">folder</i></a>
      <a href="#decommission"><span>OWN</span><strong>Transfer surviving interfaces</strong><small>Any load path that continues after go-live moves to a production integration owner with monitoring, support and change governance.</small><i class="material-symbols-outlined" aria-hidden="true">handshake</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
