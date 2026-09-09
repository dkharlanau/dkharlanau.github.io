---
layout: default
title: "SAP S/4HANA Greenfield Migration — Architecture and Data Load"
description: "Lead-level greenfield S/4HANA migration architecture: scope, sequencing, Migration Cockpit, API-led loading, migration factory, cutover, and reconciliation."
permalink: /labs/enterprise-context/migration/
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
  - greenfield
  - data-migration
  - logistics
career_impact: mapped
career_skills:
  - integration-deployment
  - logistics-master-data
  - delivery-release
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">SAP Enterprise</a></li><li aria-current="page">S/4HANA Migration</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">SAP Enterprise / Greenfield migration</p>
      <h1>Move the business state,<br />not the old database.</h1>
      <p>A greenfield migration rebuilds the data needed to run the new S/4HANA solution. The Lead decides what must exist on day one, what remains as history, how dependencies are sequenced, and how every important quantity and value is proved.</p>
      <a class="research-canvas__button" href="#migration-map">Open the migration map <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Migration scope">
      <p>Architect view</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Scope</strong><small>What moves and what does not</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Load</strong><small>Objects, tools, dependencies</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Prove</strong><small>Reconcile before release</small></div>
      <em>Baseline: Public Cloud 2608 and S/4HANA 2025 documentation.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">conversion_path</span>
    <p><strong>Greenfield is not “copy ECC into S/4”.</strong> Standard migration is focused on the initial operating state: master data, eligible open business, inventory, open items and balances.</p>
    <p><strong>Closed operational history is a separate decision.</strong> Keep it in a governed legacy system, archive or data platform unless an explicit business, legal and supported target requirement justifies another path.</p>
    <a href="/labs/enterprise-context/deployment-models/">Check deployment-model boundaries <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="migration-map" data-reveal>
    <header><p class="research-canvas__eyebrow">Knowledge map</p><h2>Nine views for one cutover.</h2><p>Object knowledge without sequencing is incomplete. Tool knowledge without reconciliation is unsafe.</p></header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/object-catalog/"><span>01</span><strong>Migration Object Catalog</strong><small>Master data, open business, balances and object families across SD, MM, PP, QM, EWM, PM, PS, FI and CO.</small><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a>
      <a href="/labs/enterprise-context/migration/tooling/"><span>02</span><strong>Tools and Technical Paths</strong><small>Migration Cockpit, staging, direct transfer, APIs, IDocs, ETL, LTMOM, Public Cloud modeler and custom engineering.</small><i class="material-symbols-outlined" aria-hidden="true">construction</i></a>
      <a href="/labs/enterprise-context/migration/api-led-migration/"><span>03</span><strong>API-Led Migration</strong><small>When a released API is justified, plus dependency queues, source-to-target keys, retry safety, throughput proof, delta strategy and reconciliation.</small><i class="material-symbols-outlined" aria-hidden="true">api</i></a>
      <a href="/labs/enterprise-context/migration/design-register/"><span>04</span><strong>Migration Design Register</strong><small>One object-level contract for release, method, dependencies, numbering, volume, delta, reconciliation, ownership, fallback and evidence.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="/labs/enterprise-context/migration/migration-factory/"><span>05</span><strong>Migration Factory</strong><small>Ownership, environments, mock cycles, defect burn-down, convergence metrics, design freeze, evidence retention and cutover control.</small><i class="material-symbols-outlined" aria-hidden="true">factory</i></a>
      <a href="/labs/enterprise-context/migration/domain-playbooks/"><span>06</span><strong>Domain Playbooks</strong><small>Sales, Procurement, Inventory, EWM, Production, Quality, Finance, Controlling, Assets and cross-domain dependencies.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/labs/enterprise-context/migration/cutover/"><span>07</span><strong>Cutover and Reconciliation</strong><small>Mocks, freeze, deltas, run control, recovery, financial proof, go/no-go, hypercare and decommissioning.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="/labs/enterprise-context/migration/lead-assessment/"><span>08</span><strong>Lead Assessment Drills</strong><small>Architecture questions on history, partial documents, numbering, API recovery, throughput, stock/value, rollback, cloud restrictions and ownership.</small><i class="material-symbols-outlined" aria-hidden="true">psychology_alt</i></a>
      <a href="#architecture-model"><span>09</span><strong>Architecture Model</strong><small>Scope classes, source paths, dependency gates, evidence and deployment choices.</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="architecture-model" data-reveal>
    <header><p class="research-canvas__eyebrow">Scope first</p><h2>Classify every requested dataset before extraction starts.</h2></header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/domain-playbooks/#wave-0"><span>A</span><strong>Configuration</strong><small>Company codes, plants, sales and purchasing structures, ledgers, valuation, process configuration and scope belong to implementation/configuration governance.</small><i class="material-symbols-outlined" aria-hidden="true">settings</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#foundation"><span>B</span><strong>Foundation master data</strong><small>Business Partners, customers, suppliers, products, banks, G/L accounts, cost/profit structures and common references.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#domain-master"><span>C</span><strong>Domain and planning master data</strong><small>Purchasing masters, classification, BOMs, work centres, routings, production versions, quality, warehouse and maintenance structures.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#open-business"><span>D</span><strong>Eligible open business</strong><small>Open contracts and orders only where the released migration object supports the current state. Follow-on document flow is a critical restriction.</small><i class="material-symbols-outlined" aria-hidden="true">pending_actions</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#balances"><span>E</span><strong>Stock, open items and balances</strong><small>Inventory quantities/values, AP/AR, G/L balances, assets and other opening positions require business and financial reconciliation.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#history"><span>F</span><strong>Closed history</strong><small>Retain it through the agreed history architecture instead of rebuilding old operational document chains in S/4.</small><i class="material-symbols-outlined" aria-hidden="true">history</i></a>
      <a href="/labs/enterprise-context/migration/tooling/#integration-after-go-live"><span>G</span><strong>Recurring flows</strong><small>If the data continues after go-live, treat it as production integration with monitoring, retry, ownership and change governance.</small><i class="material-symbols-outlined" aria-hidden="true">sync</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Source path</p><h2>Use direct transfer where supported. Use staging as the neutral boundary.</h2></header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/tooling/#direct-transfer"><span>SAP</span><strong>Supported SAP source</strong><small>Direct transfer can reduce custom extraction. It does not remove scope, mapping, prerequisite, simulation or reconciliation work.</small><i class="material-symbols-outlined" aria-hidden="true">east</i></a>
      <a href="/labs/enterprise-context/migration/tooling/#staging"><span>EXT</span><strong>External or mixed legacy sources</strong><small>Extract and harmonise outside S/4, populate the SAP staging contract, process mappings, simulate, migrate and reconcile.</small><i class="material-symbols-outlined" aria-hidden="true">table_view</i></a>
      <a href="/labs/enterprise-context/migration/api-led-migration/#decision"><span>GAP</span><strong>No suitable migration object</strong><small>Prove the gap, then compare a released API/interface, modeler enhancement or a controlled custom loader. Never write directly to application tables.</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Deployment boundary</p><h2>Same migration problem, different technical freedom.</h2></header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/tooling/#public-cloud"><span>PUB</span><strong>S/4HANA Cloud Public Edition</strong><small>Use released migration objects and supported migration approaches. Public Cloud 2608 documents staging-table migration and direct transfer from SAP systems; modeler changes are limited to SAP-released content.</small><i class="material-symbols-outlined" aria-hidden="true">cloud</i></a>
      <a href="/labs/enterprise-context/migration/tooling/#private-cloud"><span>PRV</span><strong>S/4HANA Cloud Private Edition</strong><small>Migration Cockpit remains central with broader technical control and LTMOM modelling.</small><i class="material-symbols-outlined" aria-hidden="true">cloud_queue</i></a>
      <a href="/labs/enterprise-context/migration/tooling/#on-premise"><span>ONP</span><strong>S/4HANA On-Premise</strong><small>Similar Migration Cockpit/LTMOM capabilities plus full system control. More freedom increases the need for clean-core governance.</small><i class="material-symbols-outlined" aria-hidden="true">dns</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Dependency model</p><h2>Load by dependency, not by module calendar.</h2></header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/domain-playbooks/#wave-0"><span>0</span><strong>Configuration ready</strong><small>Target organisations, ledgers, valuation, number ranges, scope and process settings are usable.</small><i class="material-symbols-outlined" aria-hidden="true">settings</i></a>
      <a href="/labs/enterprise-context/migration/domain-playbooks/#wave-1"><span>1</span><strong>Shared foundations</strong><small>Business Partners, financial masters and common reference objects.</small><i class="material-symbols-outlined" aria-hidden="true">badge</i></a>
      <a href="/labs/enterprise-context/migration/domain-playbooks/#wave-2"><span>2</span><strong>Operational masters</strong><small>Products, purchasing/sales masters, production, quality, warehouse and maintenance dependencies.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="/labs/enterprise-context/migration/domain-playbooks/#wave-3"><span>3</span><strong>Eligible open business</strong><small>Open transactions that can be represented safely under the current migration-object restrictions.</small><i class="material-symbols-outlined" aria-hidden="true">receipt_long</i></a>
      <a href="/labs/enterprise-context/migration/domain-playbooks/#wave-4"><span>4</span><strong>Stock and financial opening</strong><small>Inventory, AP/AR, G/L, assets and related cross-domain reconciliation.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#delta"><span>5</span><strong>Final delta and release</strong><small>Final changes, production integrations, reconciliation, go/no-go and controlled business release.</small><i class="material-symbols-outlined" aria-hidden="true">rocket_launch</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Lead rules</p><h2>Five rules keep the programme under control.</h2></header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/cutover/#reconciliation"><span>1</span><strong>Technical success is not business acceptance</strong><small>Prove quantities, values, references and executable processes.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/"><span>2</span><strong>Object availability is release-specific</strong><small>Check the current Available Migration Objects documentation, prerequisites and restrictions before design freeze.</small><i class="material-symbols-outlined" aria-hidden="true">update</i></a>
      <a href="/labs/enterprise-context/migration/tooling/#id-mapping"><span>3</span><strong>Legacy keys are governed data</strong><small>Keep source-to-target identity even when S/4 generates internal numbers.</small><i class="material-symbols-outlined" aria-hidden="true">key</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#rehearsal"><span>4</span><strong>Rehearsals must converge on production</strong><small>Same logic, realistic volume, measured runtime, real reconciliation and controlled defect burn-down.</small><i class="material-symbols-outlined" aria-hidden="true">repeat</i></a>
      <a href="/labs/enterprise-context/migration/tooling/#engineering-kit"><span>5</span><strong>Version migration logic like software</strong><small>Mappings, transformations, validations, reconciliation queries and runbooks belong under engineering control.</small><i class="material-symbols-outlined" aria-hidden="true">terminal</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Official source map</p><h2>Use SAP Help as the release-level source of truth.</h2></header>
    <div class="research-route-list">
      <a href="https://help.sap.com/S4_CE_DM" target="_blank" rel="noopener"><span>SAP</span><strong>Public Edition — Data Migration</strong><small>Migration process, staging tables and direct transfer.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>SAP</span><strong>Public Edition — Available Migration Objects</strong><small>Object-specific prerequisites, restrictions and migration approach.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/S4_CE_DM_STATUS" target="_blank" rel="noopener"><span>SAP</span><strong>Public Edition — Data Migration Status</strong><small>Status and audit support for the staging-table approach.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/S4_OP_DM" target="_blank" rel="noopener"><span>SAP</span><strong>S/4HANA / Private Edition — Data Migration</strong><small>Migration Cockpit guidance for the broader S/4HANA stack.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/S4_OP_MO" target="_blank" rel="noopener"><span>SAP</span><strong>S/4HANA / Private Edition — Available Migration Objects</strong><small>Release-specific migration content and object documentation.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>