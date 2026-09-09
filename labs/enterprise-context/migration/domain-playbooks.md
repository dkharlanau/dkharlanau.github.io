---
layout: default
title: "SAP S/4HANA Migration Domain Playbooks — SD, MM, PP, EWM, FI and CO"
description: "Practical greenfield migration playbooks for Sales, Procurement, Inventory, Production, Quality, Warehouse, Finance, Controlling and Asset Management."
permalink: /labs/enterprise-context/migration/domain-playbooks/
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
  - sales
  - procurement
  - production
  - finance
career_impact: mapped
career_skills:
  - logistics-p2p
  - logistics-production-quality
  - sales-o2c
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/migration/">S/4HANA Migration</a></li><li aria-current="page">Domain Playbooks</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Greenfield migration / Domain playbooks</p>
      <h1>One cutover,<br />many dependency chains.</h1>
      <p>SD, MM, PP, EWM, QM, FI and CO do not migrate independently. Orders depend on master data. Stock depends on valuation. Production depends on planning masters. Finance must prove the opening position across all of them.</p>
      <a class="research-canvas__button" href="#waves">Start with the waves <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Domain rule">
      <p>Migration logic</p>
      <div class="research-canvas__signal-line"><span>1</span><strong>Master</strong><small>Build dependencies</small></div>
      <div class="research-canvas__signal-line"><span>2</span><strong>Open</strong><small>Carry valid open state</small></div>
      <div class="research-canvas__signal-line"><span>3</span><strong>Prove</strong><small>Reconcile outcomes</small></div>
      <em>Module plans must converge into one business cutover.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <p><strong>Problem:</strong> module teams can produce individually correct load plans that fail as one cutover because shared master data, open-document state, stock valuation and financial opening balances depend on each other.</p>
    <p><strong>Current standard order rule.</strong> Migration Cockpit is for the initial operating state. Orders with follow-on documents in their document flow cannot be migrated through the standard migration content. SAP specifically requires partially delivered sales orders to be closed in the source and partially open purchase orders to be closed or cancelled.</p>
    <p><strong>Architectural consequence.</strong> If a commercial commitment remains after the legacy document is closed, create a controlled target document for the remaining business. Do not rebuild historical receipts, deliveries, invoices or confirmations only to imitate the old document flow.</p>
  </section>

  <section class="research-canvas__inventory" id="waves" data-reveal>
    <header><p class="research-canvas__eyebrow">Load waves</p><h2>Build the target in dependency order.</h2><p>Validate the final order against the migration-object prerequisites for the exact target release.</p></header>
    <div class="research-route-list">
      <a id="wave-0" href="#wave-0"><span>0</span><strong>Target configuration</strong><small>Organisational structures, currencies, ledgers, valuation, number ranges, document types, plants, sales areas, purchasing organisations, scope and required extensions are usable.</small><i class="material-symbols-outlined" aria-hidden="true">settings</i></a>
      <a id="wave-1" href="#wave-1"><span>1</span><strong>Shared foundations</strong><small>Business Partners, customers, suppliers, banks, G/L accounts, cost centres, profit centres and shared references.</small><i class="material-symbols-outlined" aria-hidden="true">badge</i></a>
      <a id="wave-2" href="#wave-2"><span>2</span><strong>Operational master graph</strong><small>Products and organisational views, sales and purchasing masters, classification, BOMs, work centres, routings, production versions, quality and warehouse masters.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a id="wave-3" href="#wave-3"><span>3</span><strong>Eligible open business</strong><small>Only supported open transactions without disqualifying follow-on flow, plus approved target recreation of remaining commitments where legacy chains must be closed.</small><i class="material-symbols-outlined" aria-hidden="true">pending_actions</i></a>
      <a id="wave-4" href="#wave-4"><span>4</span><strong>Stock and financial opening position</strong><small>Inventory, AP/AR open items, G/L balances, asset values and other cutover balances in the agreed financial sequence.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
      <a id="wave-5" href="#wave-5"><span>5</span><strong>Delta, integrations and release</strong><small>Final deltas, recurring interfaces, reconciliation, business sign-off, go/no-go and controlled release.</small><i class="material-symbols-outlined" aria-hidden="true">rocket_launch</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="sales" data-reveal>
    <header><p class="research-canvas__eyebrow">Sales / SD</p><h2>Migrate the customer promise, not its old document history.</h2></header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/object-catalog/#foundation"><span>SD1</span><strong>Customer and Business Partner</strong><small>Set grouping, numbering, roles, company-code and sales-area views, partner functions, addresses, tax data and source-to-target keys first.</small><i class="material-symbols-outlined" aria-hidden="true">person</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#foundation"><span>SD2</span><strong>Product sales views</strong><small>Sales organisation, distribution channel, units, tax and availability-relevant attributes must match the new process design.</small><i class="material-symbols-outlined" aria-hidden="true">category</i></a>
      <a href="/labs/enterprise-context/sales-processes/mechanisms/"><span>SD3</span><strong>Pricing follows the new design</strong><small>Migrate only condition records still needed. Do not use migration to copy obsolete condition technique or local exceptions into greenfield S/4.</small><i class="material-symbols-outlined" aria-hidden="true">sell</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#open-business"><span>SD4</span><strong>Open sales orders</strong><small>Use the released object only for eligible open orders. Orders with follow-on documents cannot be migrated through the standard content.</small><i class="material-symbols-outlined" aria-hidden="true">shopping_cart</i></a>
      <a href="#sales-partial"><span>SD5</span><strong>Partially delivered order</strong><small>Close it in the source. If business still has a remaining commitment, create a controlled target order for the remainder and keep the legacy chain as history.</small><i class="material-symbols-outlined" aria-hidden="true">call_split</i></a>
      <a href="#sales-reconcile"><span>SD6</span><strong>Prove the promise</strong><small>Reconcile selected/migrated/excluded records, open quantity and value, then run ATP → delivery → goods issue → billing on representative target orders.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="sales-partial" data-reveal>
    <header><p class="research-canvas__eyebrow">Sales decision</p><h2>Handle the remainder as new target business.</h2></header>
    <div class="research-route-list">
      <a href="#sales-partial"><span>A</span><strong>No follow-on flow</strong><small>If the order is otherwise eligible, use the released migration object and validate its exact document-type and field restrictions.</small><i class="material-symbols-outlined" aria-hidden="true">check_circle</i></a>
      <a href="#sales-partial"><span>B</span><strong>Delivery or billing already exists</strong><small>Close the source order as required. Retain the executed chain as history and create only the remaining commitment in the target when the business needs it.</small><i class="material-symbols-outlined" aria-hidden="true">history</i></a>
      <a href="#sales-partial"><span>C</span><strong>Complex scenarios</strong><small>Returns, intercompany, third-party and configurable products need an explicit cutover rule and target process test; do not assume the generic order object covers them.</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="sales-reconcile" data-reveal>
    <header><p class="research-canvas__eyebrow">Sales proof</p><h2>A created order is not yet a successful migration.</h2></header>
    <div class="research-route-list">
      <a href="#sales-reconcile"><span>COUNT</span><strong>Population</strong><small>Selected source = migrated + approved exclusions + commitments deliberately recreated in target + unresolved defects.</small><i class="material-symbols-outlined" aria-hidden="true">functions</i></a>
      <a href="#sales-reconcile"><span>QTY</span><strong>Open quantity</strong><small>Compare remaining business quantity by customer, product and sales organisation with unit conversions controlled.</small><i class="material-symbols-outlined" aria-hidden="true">straighten</i></a>
      <a href="#sales-reconcile"><span>VAL</span><strong>Commercial value</strong><small>Compare expected net value and key pricing components. Approved redesign differences must be visible.</small><i class="material-symbols-outlined" aria-hidden="true">payments</i></a>
      <a href="#sales-reconcile"><span>FLOW</span><strong>Executable flow</strong><small>Prove ATP, delivery, warehouse execution, PGI, billing and accounting on migrated or recreated target records.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="procurement" data-reveal>
    <header><p class="research-canvas__eyebrow">Procurement / MM</p><h2>Separate open commitment from historical receipt and invoice flow.</h2></header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/object-catalog/#foundation"><span>MM1</span><strong>Supplier and product</strong><small>Supplier purchasing/company-code views and product purchasing/plant/valuation data must be stable before purchasing documents.</small><i class="material-symbols-outlined" aria-hidden="true">badge</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#domain-master"><span>MM2</span><strong>Source-of-supply masters</strong><small>Migrate purchasing info records, source lists and contracts only when they remain valid in the new sourcing design.</small><i class="material-symbols-outlined" aria-hidden="true">request_quote</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#open-business"><span>MM3</span><strong>Open purchase orders</strong><small>Use standard migration only for eligible POs without follow-on documents. SAP requires partially open POs to be closed or cancelled in the source.</small><i class="material-symbols-outlined" aria-hidden="true">shopping_bag</i></a>
      <a href="#procurement-grir"><span>MM4</span><strong>Remaining commitment</strong><small>If purchasing activity must continue, recreate the required target PO and handle historical GR/IR, receipts and invoices through the agreed finance/history boundary.</small><i class="material-symbols-outlined" aria-hidden="true">compare_arrows</i></a>
      <a href="#procurement-reconcile"><span>MM5</span><strong>Prove P2P</strong><small>Reconcile remaining quantity/value and test receipt, quality where relevant, invoice posting and accounting.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="procurement-grir" data-reveal>
    <header><p class="research-canvas__eyebrow">Procurement + Finance</p><h2>GR/IR makes partial procurement a cross-domain cutover decision.</h2></header>
    <div class="research-route-list">
      <a href="#procurement-grir"><span>PO</span><strong>Operational remainder</strong><small>Create only the commitment that still needs target execution; do not recreate historical goods movements.</small><i class="material-symbols-outlined" aria-hidden="true">pending</i></a>
      <a href="#procurement-grir"><span>FI</span><strong>Financial opening position</strong><small>Finance defines the treatment of unmatched receipts, invoices, clearing exposure and migrated open items.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
      <a href="#procurement-grir"><span>CTRL</span><strong>One control equation</strong><small>Source remaining commitments + GR/IR/open-item position must explain the target PO population and target financial opening balance.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="procurement-reconcile" data-reveal>
    <header><p class="research-canvas__eyebrow">Procurement proof</p><h2>Prove document continuity and accounting consistency.</h2></header>
    <div class="research-route-list">
      <a href="#procurement-reconcile"><span>COUNT</span><strong>Population</strong><small>Selected source = migrated + approved exclusions + intentionally recreated commitments + unresolved failures.</small><i class="material-symbols-outlined" aria-hidden="true">functions</i></a>
      <a href="#procurement-reconcile"><span>QTY</span><strong>Quantity and value</strong><small>Compare by supplier, product, plant, purchasing organisation and account assignment.</small><i class="material-symbols-outlined" aria-hidden="true">inventory</i></a>
      <a href="#procurement-reconcile"><span>P2P</span><strong>Executable P2P</strong><small>A target PO must support the real next step: receipt, inspection, invoice and accounting.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Inventory and warehouse</p><h2>Stock is quantity, status, ownership, location and value.</h2></header>
    <div class="research-route-list">
      <a href="#inventory"><span>IM1</span><strong>Define the stock dimensions</strong><small>Unrestricted, quality, blocked, special stock, batch, serial, valuation type and storage location need explicit rules.</small><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a>
      <a href="#inventory"><span>IM2</span><strong>Freeze movements tightly</strong><small>Complete as many inbound, outbound, transfer and production movements as possible before the final snapshot.</small><i class="material-symbols-outlined" aria-hidden="true">pause_circle</i></a>
      <a href="#inventory"><span>IM3</span><strong>Reconcile quantity and value together</strong><small>Inventory quantity, material valuation and G/L inventory accounts form one control set.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
      <a href="#ewm"><span>EWM</span><strong>Separate IM and EWM cutover</strong><small>Bins, warehouse product data, HUs and warehouse execution are a different layer from plant/storage-location stock.</small><i class="material-symbols-outlined" aria-hidden="true">warehouse</i></a>
      <a href="#inventory"><span>TEST</span><strong>Use the stock</strong><small>Test ATP, goods issue, receipt, transfer, picking and production staging on representative stock categories.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="ewm" data-reveal>
    <header><p class="research-canvas__eyebrow">EWM boundary</p><h2>Load warehouse stock only after the warehouse can own it.</h2></header>
    <div class="research-route-list">
      <a href="#ewm"><span>1</span><strong>Structure ready</strong><small>Warehouse number, storage types, sections, activity areas, bins and process configuration.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#ewm"><span>2</span><strong>Warehouse product ready</strong><small>Products have the attributes needed for putaway, picking, storage and handling.</small><i class="material-symbols-outlined" aria-hidden="true">category</i></a>
      <a href="#ewm"><span>3</span><strong>Physical state aligned</strong><small>Define the selected deployment's method for IM stock, EWM stock, handling units and final physical reconciliation.</small><i class="material-symbols-outlined" aria-hidden="true">view_in_ar</i></a>
      <a href="#ewm"><span>4</span><strong>Close old execution where possible</strong><small>Complete or cancel old warehouse tasks and waves rather than carrying uncontrolled execution state across systems.</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="production" data-reveal>
    <header><p class="research-canvas__eyebrow">Production / PP</p><h2>Master graph first, open production second.</h2></header>
    <div class="research-route-list">
      <a href="#production"><span>PP1</span><strong>Planning-ready product</strong><small>MRP, procurement type, production scheduling, lot size, storage and valuation data reflect the target design.</small><i class="material-symbols-outlined" aria-hidden="true">category</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#production-master"><span>PP2</span><strong>BOM → work centre → routing → production version</strong><small>Treat these as one executable master graph and validate dates, units, capacity and costing relationships.</small><i class="material-symbols-outlined" aria-hidden="true">precision_manufacturing</i></a>
      <a href="#quality"><span>PP3</span><strong>Quality dependencies</strong><small>Inspection setup and plans can affect production release and goods receipt.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#open-business"><span>PP4</span><strong>Open production orders</strong><small>Confirm the exact object's status restrictions. As a general current rule, orders with follow-on documents cannot be migrated through standard Migration Cockpit content.</small><i class="material-symbols-outlined" aria-hidden="true">manufacturing</i></a>
      <a href="#production-wip"><span>PP5</span><strong>WIP is also Finance</strong><small>Operational remaining work and financial WIP/variance/settlement positions need one cutover design.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="production-wip" data-reveal>
    <header><p class="research-canvas__eyebrow">Production + Finance</p><h2>Do not invent target confirmations to reproduce history.</h2></header>
    <div class="research-route-list">
      <a href="#production-wip"><span>CLOSE</span><strong>Close what can be closed</strong><small>Reducing partially processed orders removes reservation, WIP, variance and settlement complexity.</small><i class="material-symbols-outlined" aria-hidden="true">done_all</i></a>
      <a href="#production-wip"><span>OPEN</span><strong>Carry only supportable remaining work</strong><small>If the standard object cannot migrate the execution state, start a controlled target order for remaining production rather than rebuilding consumed history.</small><i class="material-symbols-outlined" aria-hidden="true">pending</i></a>
      <a href="#finance"><span>VALUE</span><strong>Finance owns the value rule</strong><small>Agree how inventory, WIP, variance and settlement enter the target opening position.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="quality" data-reveal>
    <header><p class="research-canvas__eyebrow">Quality / QM</p><h2>Quality status can block otherwise correct stock and production.</h2></header>
    <div class="research-route-list">
      <a href="#quality"><span>QM1</span><strong>Quality masters</strong><small>Sequence methods, characteristics, plans, catalogues and product inspection setup before dependent processes.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="#quality"><span>QM2</span><strong>Open quality work</strong><small>Close existing inspection work where possible; otherwise verify the exact supported migration path and preserve the business state explicitly.</small><i class="material-symbols-outlined" aria-hidden="true">pending_actions</i></a>
      <a href="#inventory"><span>QM3</span><strong>Quality stock</strong><small>Quality inspection stock must reconcile with Inventory Management and the physical cutover state.</small><i class="material-symbols-outlined" aria-hidden="true">inventory</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="finance" data-reveal>
    <header><p class="research-canvas__eyebrow">Finance / FI</p><h2>Design the opening balance architecture before mock one.</h2></header>
    <div class="research-route-list">
      <a href="#finance"><span>FI1</span><strong>Financial foundations</strong><small>G/L accounts, Business Partners, banks, cost centres, profit centres and required account assignments exist first.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
      <a href="#finance"><span>FI2</span><strong>AP and AR open items</strong><small>Carry outstanding items with the dates, currencies, tax and payment attributes needed for clearing and reporting.</small><i class="material-symbols-outlined" aria-hidden="true">payments</i></a>
      <a href="#finance"><span>FI3</span><strong>G/L opening position</strong><small>Define migration key date, required balances/line items, periods, currencies and current-year reporting requirement.</small><i class="material-symbols-outlined" aria-hidden="true">calculate</i></a>
      <a href="#assets"><span>FI4</span><strong>Fixed assets</strong><small>Sequence asset master and legacy values/postings around the target Asset Accounting transfer date.</small><i class="material-symbols-outlined" aria-hidden="true">apartment</i></a>
      <a href="#finance-proof"><span>FI5</span><strong>Trial balance is the gate</strong><small>Source closing and target opening positions reconcile by company code, ledger, currency and agreed dimensions.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="controlling" data-reveal>
    <header><p class="research-canvas__eyebrow">Controlling / CO</p><h2>CO objects are shared dependencies, not an island.</h2></header>
    <div class="research-route-list">
      <a href="#controlling"><span>CO1</span><strong>Cost and profit centres</strong><small>Validate hierarchy, validity, owners and reporting design before logistics and asset assignments use them.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="#controlling"><span>CO2</span><strong>Orders and projects</strong><small>Carry only structures and open commitments required by the target; close obsolete controlling objects.</small><i class="material-symbols-outlined" aria-hidden="true">workspaces</i></a>
      <a href="#production-wip"><span>CO3</span><strong>Production accounting</strong><small>WIP, variance and settlement rules align with the production cutover and financial opening position.</small><i class="material-symbols-outlined" aria-hidden="true">precision_manufacturing</i></a>
      <a href="#finance-proof"><span>CO4</span><strong>Management reconciliation</strong><small>Reconcile required profit-centre, cost-centre, project and segment views, not only company-code totals.</small><i class="material-symbols-outlined" aria-hidden="true">analytics</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="assets" data-reveal>
    <header><p class="research-canvas__eyebrow">Asset Accounting</p><h2>Asset identity and value are linked migration jobs.</h2></header>
    <div class="research-route-list">
      <a href="#assets"><span>AA1</span><strong>Asset master</strong><small>Asset class, company code, cost/profit assignments, locations and technical references match the target organisation.</small><i class="material-symbols-outlined" aria-hidden="true">apartment</i></a>
      <a href="#assets"><span>AA2</span><strong>Legacy values/postings</strong><small>Coordinate acquisition value, accumulated depreciation, current-year depreciation and transfer date with the selected object.</small><i class="material-symbols-outlined" aria-hidden="true">calculate</i></a>
      <a href="#finance-proof"><span>AA3</span><strong>Subledger ↔ G/L</strong><small>Asset balances and reconciliation accounts agree before Finance accepts cutover.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="maintenance-projects" data-reveal>
    <header><p class="research-canvas__eyebrow">Maintenance and projects</p><h2>Technical objects and projects cross logistics and finance.</h2></header>
    <div class="research-route-list">
      <a href="#maintenance-projects"><span>PM</span><strong>Functional locations and equipment</strong><small>Build hierarchy, serial relationships, classification and organisational assignments before plans and open work.</small><i class="material-symbols-outlined" aria-hidden="true">engineering</i></a>
      <a href="#maintenance-projects"><span>PM</span><strong>Maintenance plans and open work</strong><small>Close completed legacy work and verify support before carrying any open order state.</small><i class="material-symbols-outlined" aria-hidden="true">handyman</i></a>
      <a href="#maintenance-projects"><span>PS</span><strong>Projects and WBS</strong><small>Coordinate project master, status, organisational assignments, open purchasing commitments and financial balances.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="finance-proof" data-reveal>
    <header><p class="research-canvas__eyebrow">Cross-domain reconciliation</p><h2>Reconcile business equations, not only objects.</h2></header>
    <div class="research-route-list">
      <a href="#finance-proof"><span>STK</span><strong>Inventory quantity ↔ value ↔ G/L</strong><small>Physical/logistics quantities, valuation and inventory accounts explain the same opening stock.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
      <a href="#finance-proof"><span>AR</span><strong>Customer open items ↔ AR</strong><small>Open-item totals and aging reconcile to the G/L control position.</small><i class="material-symbols-outlined" aria-hidden="true">payments</i></a>
      <a href="#finance-proof"><span>AP</span><strong>Supplier open items ↔ AP</strong><small>Supplier balances and aging reconcile to the financial opening position.</small><i class="material-symbols-outlined" aria-hidden="true">receipt</i></a>
      <a href="#finance-proof"><span>AA</span><strong>Asset values ↔ G/L</strong><small>Acquisition and depreciation values tie to asset reconciliation accounts.</small><i class="material-symbols-outlined" aria-hidden="true">apartment</i></a>
      <a href="#procurement-grir"><span>GRIR</span><strong>Procurement remainder ↔ GR/IR</strong><small>Target commitments and financial clearing exposure are explained together.</small><i class="material-symbols-outlined" aria-hidden="true">compare_arrows</i></a>
      <a href="#production-wip"><span>WIP</span><strong>Production remainder ↔ WIP</strong><small>Remaining operational work and financial WIP/settlement position agree.</small><i class="material-symbols-outlined" aria-hidden="true">manufacturing</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="ownership" data-reveal>
    <header><p class="research-canvas__eyebrow">Ownership model</p><h2>Every object needs accountable business and technical owners.</h2></header>
    <div class="research-route-list">
      <a href="#ownership"><span>BUS</span><strong>Business data owner</strong><small>Approves population, cleansing, exceptions, reconciliation and acceptance.</small><i class="material-symbols-outlined" aria-hidden="true">person_check</i></a>
      <a href="#ownership"><span>FUNC</span><strong>Functional migration lead</strong><small>Owns target meaning, object fit, dependencies, mappings and business validation.</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      <a href="#ownership"><span>DATA</span><strong>Data engineering lead</strong><small>Owns extraction, transformation, lineage, staging and automated quality controls.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="#ownership"><span>CTRL</span><strong>Cutover/control lead</strong><small>Owns sequence, freeze, timing, checkpoints, evidence and recovery coordination.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="#ownership"><span>SEC</span><strong>Security/platform owners</strong><small>Control temporary connections, roles, secrets and post-migration decommissioning.</small><i class="material-symbols-outlined" aria-hidden="true">shield</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
