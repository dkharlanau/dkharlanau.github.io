---
layout: default
title: "SAP S/4HANA Greenfield Migration — Architecture and Data Load"
description: "A Lead-level guide to greenfield data migration into SAP S/4HANA: scope, sequencing, migration cockpit, cloud boundaries, cutover, reconciliation, and domain decisions."
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
      <p>A greenfield S/4HANA migration is a controlled rebuild of the data needed to operate the new solution. The architect decides what must exist on day one, what stays as history, how dependencies are sequenced, and how every loaded number is proved.</p>
      <a class="research-canvas__button" href="#migration-map">Open the migration map <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Migration scope">
      <p>Architect view</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Scope</strong><small>What moves and what does not</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Load</strong><small>Objects, tools, dependencies</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Prove</strong><small>Reconcile before go-live</small></div>
      <em>Research baseline: Public Cloud 2608 and S/4HANA 2025 FPS01 documentation.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">conversion_path</span>
    <p><strong>Greenfield is not “copy ECC into S/4”.</strong> Standard migration content is designed mainly for initial master data, open transactional data, balances, and inventory needed to start operations.</p>
    <p><strong>Closed history is a separate architecture decision.</strong> Keep it in the legacy system, an archive, a data platform, or another governed history solution unless a supported migration object and a real business need justify moving it.</p>
    <a href="/labs/enterprise-context/deployment-models/">Check deployment-model boundaries <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="migration-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Migration knowledge map</p>
      <h2>Six views for one cutover.</h2>
      <p>Use the pages together. Object knowledge without sequencing is incomplete. Tool knowledge without reconciliation is dangerous.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/object-catalog/"><span>01</span><strong>Migration Object Catalog</strong><small>What can usually be loaded across SD, MM, PP, QM, EWM, PM, PS, FI and CO; what is master, open transaction, balance, or reference data.</small><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a>
      <a href="/labs/enterprise-context/migration/tooling/"><span>02</span><strong>Tools and Technical Paths</strong><small>Migration Cockpit, staging tables, direct transfer, APIs, IDocs, Integration Suite, ETL tools, LTMOM, Public Cloud modeler, and custom engineering.</small><i class="material-symbols-outlined" aria-hidden="true">construction</i></a>
      <a href="/labs/enterprise-context/migration/domain-playbooks/"><span>03</span><strong>Domain Playbooks</strong><small>Practical load order and migration questions for Sales, Procurement, Inventory, Production, Finance, Controlling and adjacent logistics domains.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/labs/enterprise-context/migration/cutover/"><span>04</span><strong>Cutover and Reconciliation</strong><small>Mock loads, freeze and delta design, run control, error recovery, financial and logistics reconciliation, go/no-go evidence, and hypercare.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="/labs/enterprise-context/migration/lead-assessment/"><span>05</span><strong>Lead Assessment Drills</strong><small>Architecture questions that expose weak migration thinking: history, partial documents, internal numbering, stock versus value, rollback, cloud restrictions, and ownership.</small><i class="material-symbols-outlined" aria-hidden="true">psychology_alt</i></a>
      <a href="#architecture-model"><span>06</span><strong>Architecture Model</strong><small>The operating model on this page: scope layers, source paths, dependency gates, evidence, and deployment choices.</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="architecture-model" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Scope before extraction</p>
      <h2>Classify every requested dataset before anyone writes an ETL job.</h2>
      <p>The same word “migration” is often used for very different jobs. Separate them early.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/domain-playbooks/"><span>A</span><strong>Configuration and organisational design</strong><small>Company codes, plants, sales organisations, purchasing organisations, ledgers, valuation and process configuration normally belong to implementation and transport/configuration governance. Do not treat them as ordinary business-data loads.</small><i class="material-symbols-outlined" aria-hidden="true">settings</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#foundation"><span>B</span><strong>Foundation master data</strong><small>Business partners, customers, suppliers, products, units, banks, G/L accounts, cost and profit structures, and other objects that later transactions reference.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#domain-master"><span>C</span><strong>Domain master and planning data</strong><small>Purchasing info records, source lists, BOMs, work centres, routings, production versions, classification, quality, warehouse and maintenance structures.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#open-business"><span>D</span><strong>Open business transactions</strong><small>Open sales orders, contracts, purchase orders, production orders and other in-flight business that must continue after go-live. Eligibility is object-specific.</small><i class="material-symbols-outlined" aria-hidden="true">pending_actions</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#balances"><span>E</span><strong>Balances, stock and open items</strong><small>Inventory quantities and values, G/L balances, AP/AR open items, bank balances and fixed-asset values. These require business reconciliation, not only technical success.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#history"><span>F</span><strong>Closed history</strong><small>Closed orders, old deliveries, old invoices and long historical document chains are usually better retained outside the operational migration scope. Define access, retention and audit requirements separately.</small><i class="material-symbols-outlined" aria-hidden="true">history</i></a>
      <a href="/labs/enterprise-context/migration/tooling/#integration-after-go-live"><span>G</span><strong>Post-go-live replication and deltas</strong><small>Recurring interfaces are integration, not one-time migration. Design APIs, IDocs, events or middleware with monitoring, retries and ownership.</small><i class="material-symbols-outlined" aria-hidden="true">sync</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Source-system decision</p>
      <h2>Use direct transfer where it fits. Use staging as the neutral boundary.</h2>
      <p>Do not force every source through the same route.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/tooling/#direct-transfer"><span>ECC</span><strong>SAP ERP / supported SAP source</strong><small>Direct transfer can reduce extraction work when the exact source scenario and migration object are supported. Keep object selection, mappings, transformations and target validation explicit.</small><i class="material-symbols-outlined" aria-hidden="true">east</i></a>
      <a href="/labs/enterprise-context/migration/tooling/#staging"><span>EXT</span><strong>Non-SAP and mixed legacy sources</strong><small>Staging tables are usually the cleanest contract: extract and harmonise outside S/4, populate the SAP-defined structures, process mappings, simulate, migrate and reconcile.</small><i class="material-symbols-outlined" aria-hidden="true">table_view</i></a>
      <a href="/labs/enterprise-context/migration/tooling/#custom"><span>GAP</span><strong>No suitable migration object</strong><small>First prove that the gap is real. Then compare a released API, an SAP-supported interface, a modeler enhancement, or a controlled custom loader. Direct table writes are not a migration strategy.</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Deployment boundary</p>
      <h2>Public, Private and On-Premise share the migration problem, not the same freedom.</h2>
      <p>Always confirm the exact target release and active scope before freezing the design.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/tooling/#public-cloud"><span>PUB</span><strong>S/4HANA Cloud Public Edition</strong><small>Use released migration objects, Migrate Your Data, staging tables or supported direct transfer. Remote staging can use SAP HANA Cloud on BTP. Modeler enhancements are limited to migration objects and fields released by SAP.</small><i class="material-symbols-outlined" aria-hidden="true">cloud</i></a>
      <a href="/labs/enterprise-context/migration/tooling/#private-cloud"><span>PRV</span><strong>S/4HANA Cloud Private Edition</strong><small>Migration Cockpit remains central, with broader technical control. LTMOM supports migration-object modelling; recent 2025 features add direct-transfer selection and split options.</small><i class="material-symbols-outlined" aria-hidden="true">cloud_queue</i></a>
      <a href="/labs/enterprise-context/migration/tooling/#on-premise"><span>ONP</span><strong>S/4HANA On-Premise</strong><small>Similar Migration Cockpit and LTMOM capabilities to Private Edition, plus full customer system control. More freedom also creates more ways to build unsupported loaders, so governance matters more, not less.</small><i class="material-symbols-outlined" aria-hidden="true">dns</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Dependency model</p>
      <h2>Load by dependency, not by module plan.</h2>
      <p>A useful starting sequence is below. The final order must be proven against the migration-object prerequisites in the target release.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/domain-playbooks/#wave-0"><span>0</span><strong>Target configuration ready</strong><small>Organisational units, currencies, ledgers, valuation, number ranges, document types, plants, sales and purchasing structures, and required scope are usable.</small><i class="material-symbols-outlined" aria-hidden="true">check_circle</i></a>
      <a href="/labs/enterprise-context/migration/domain-playbooks/#wave-1"><span>1</span><strong>Identity and financial foundations</strong><small>Business partners, customers, suppliers, banks, G/L accounts, cost centres, profit centres and required reference masters.</small><i class="material-symbols-outlined" aria-hidden="true">badge</i></a>
      <a href="/labs/enterprise-context/migration/domain-playbooks/#wave-2"><span>2</span><strong>Products and operational masters</strong><small>Products and organisational extensions, classification, purchasing masters, BOM, work centre, routing, production version, quality and warehouse-related masters.</small><i class="material-symbols-outlined" aria-hidden="true">category</i></a>
      <a href="/labs/enterprise-context/migration/domain-playbooks/#wave-3"><span>3</span><strong>Open commercial and supply documents</strong><small>Eligible open contracts, sales orders, purchase orders, production orders and other continuing commitments.</small><i class="material-symbols-outlined" aria-hidden="true">receipt_long</i></a>
      <a href="/labs/enterprise-context/migration/domain-playbooks/#wave-4"><span>4</span><strong>Stock and financial cutover</strong><small>Inventory, AP/AR open items, G/L balances, asset master and asset postings in the agreed financial sequence. Reconcile quantity, value and clearing accounts together.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#delta"><span>5</span><strong>Delta, interfaces and business release</strong><small>Apply final deltas, start recurring integrations, complete reconciliation, approve go/no-go, and release the business only when evidence is signed.</small><i class="material-symbols-outlined" aria-hidden="true">rocket_launch</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead rules</p>
      <h2>Five rules prevent most migration design mistakes.</h2>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/cutover/"><span>1</span><strong>A successful load is not a successful migration</strong><small>Technical status proves processing. Business reconciliation proves that the target can operate with correct quantities, values, relationships and ownership.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/"><span>2</span><strong>Migration objects change by release</strong><small>Never design from an old spreadsheet of object names. Check the Available Migration Objects page, prerequisites, restrictions, scope items and migration approach for the target release.</small><i class="material-symbols-outlined" aria-hidden="true">update</i></a>
      <a href="/labs/enterprise-context/migration/tooling/#id-mapping"><span>3</span><strong>Legacy keys are part of the contract</strong><small>If target numbers change, keep source IDs as governed cross-references. Use them consistently in later migration objects so dependencies can be resolved and audited.</small><i class="material-symbols-outlined" aria-hidden="true">key</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#rehearsal"><span>4</span><strong>Every rehearsal must look more like production</strong><small>Same extraction logic, comparable volume, same mapping version, measured runtimes, real reconciliation and clear defect burn-down.</small><i class="material-symbols-outlined" aria-hidden="true">repeat</i></a>
      <a href="/labs/enterprise-context/migration/tooling/#engineering-kit"><span>5</span><strong>Put migration logic under engineering control</strong><small>Mappings, transformations, validation rules and reconciliation queries should be versioned, tested and promoted through controlled environments. Excel can be an input; it should not be the architecture.</small><i class="material-symbols-outlined" aria-hidden="true">terminal</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Official source map</p>
      <h2>Use SAP documentation as the release-level source of truth.</h2>
      <p>This Lab converts documentation into an architecture model. Exact object availability and restrictions must still be checked for the customer release and activated scope.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/S4_CE_DM" target="_blank" rel="noopener"><span>SAP</span><strong>Public Edition — Data Migration</strong><small>Migration Cockpit, staging tables, direct transfer, process and Public Cloud guidance.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>SAP</span><strong>Public Edition — Available Migration Objects</strong><small>Release-specific migration objects, prerequisites, restrictions, approach and validation guidance.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/S4_CE_DM_STATUS" target="_blank" rel="noopener"><span>SAP</span><strong>Public Edition — Data Migration Status</strong><small>Status, messages, audit data and reporting for the staging-table approach.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/S4_OP_DM" target="_blank" rel="noopener"><span>SAP</span><strong>S/4HANA / Private Edition — Data Migration</strong><small>Migration Cockpit guidance for SAP S/4HANA and Private Edition.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/S4_OP_MO" target="_blank" rel="noopener"><span>SAP</span><strong>S/4HANA / Private Edition — Available Migration Objects</strong><small>Object documentation and release-specific migration content for the broader S/4HANA stack.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
