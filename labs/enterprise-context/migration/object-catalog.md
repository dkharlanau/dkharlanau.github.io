---
layout: default
title: "SAP S/4HANA Migration Object Catalog — Greenfield Load Scope"
description: "A practical catalog of S/4HANA migration object families for Sales, Procurement, Inventory, Production, Quality, EWM, Finance, Controlling and Asset Management."
permalink: /labs/enterprise-context/migration/object-catalog/
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
  - migration-cockpit
  - master-data
  - logistics
career_impact: mapped
career_skills:
  - logistics-master-data
  - sales-o2c
  - logistics-p2p
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/migration/">S/4HANA Migration</a></li><li aria-current="page">Object Catalog</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Greenfield migration / Object catalog</p>
      <h1>Ask what the business needs,<br />then find the migration object.</h1>
      <p>This catalog is an architecture map, not a frozen SAP object list. SAP changes migration content by release, deployment model, scope item and country. Use the catalog to define the migration scope, then confirm every object in the target system documentation.</p>
      <a class="research-canvas__button" href="#foundation">Start with foundations <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Catalog rule">
      <p>Object decision</p>
      <div class="research-canvas__signal-line"><span>1</span><strong>Need</strong><small>Day-1 business state</small></div>
      <div class="research-canvas__signal-line"><span>2</span><strong>Object</strong><small>Released migration content</small></div>
      <div class="research-canvas__signal-line"><span>3</span><strong>Proof</strong><small>Business validation</small></div>
      <em>Always check exact target release.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">warning</span>
    <p><strong>Do not promise “all ECC data”.</strong> Migration Cockpit objects are built for specific business objects and specific initial-load purposes. A migration object can create data and can have strict limits on updates, document status, follow-on documents, countries, extensions and prerequisites.</p>
    <p><strong>Object names below are families and common examples.</strong> Use <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener">Available Migration Objects for Public Edition</a> or <a href="https://help.sap.com/S4_OP_MO" target="_blank" rel="noopener">Available Migration Objects for S/4HANA / Private Edition</a> before design freeze.</p>
  </section>

  <section class="research-canvas__inventory" id="release-watchlist" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">2608 release watchlist</p>
      <h2>The object name is not enough. Read its scope, prerequisites and post-processing.</h2>
      <p>These current Public Edition examples show why the migration register must store release-level restrictions instead of only an object name.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/da48c42d19e6484a90795feb509d2fc4.html" target="_blank" rel="noopener"><span>SD</span><strong>Open sales order: staging, custom fields, released extra fields</strong><small>The 2608 object SLS_ORDER_2 uses staging tables, supports custom fields for sales document header/item, and supports selected additional standard fields through the Public Cloud Migration Object Modeler. It still represents open initial state, not historical document flow.</small><i class="material-symbols-outlined" aria-hidden="true">shopping_cart</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/bcac78c2e4454b0a8f1409a06e447b2f.html" target="_blank" rel="noopener"><span>PP</span><strong>Production order: Created or Released only</strong><small>The 2608 object PP_PRODNORD supports source orders in Created or Released status. After migration, the target production orders have status Created. Product and production version are mandatory prerequisites.</small><i class="material-symbols-outlined" aria-hidden="true">manufacturing</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/846562085c054f16ae13d851557cc086.html" target="_blank" rel="noopener"><span>PM</span><strong>Maintenance order: internal numbering only</strong><small>The current PM_MAINTORD2 migration object does not support external number ranges. If legacy order numbers matter for lookup or audit, keep a governed cross-reference instead of assuming number preservation.</small><i class="material-symbols-outlined" aria-hidden="true">handyman</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/3fb24f963798441da2867718ca6f711f.html" target="_blank" rel="noopener"><span>MM</span><strong>Purchase contract: item-category limits matter</strong><small>The current object does not support external services, creation of configurations, and several item categories including third-party, enhanced limits, consignment and subcontracting. A generic “contract migration” line in a plan is therefore too broad.</small><i class="material-symbols-outlined" aria-hidden="true">contract</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/9c62e3f7092744d49021051301263e85.html" target="_blank" rel="noopener"><span>MAT</span><strong>Product extension: new organisational levels, not updates</strong><small>PROD_EXT_2 can extend an existing product to new plants, valuation areas, distribution chains or storage locations. It does not update existing organisational levels. Valuation data is also a prerequisite for stock loading when S/4 must calculate stock value.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/c633ded541d44facae2a4938fd3c2e3c.html" target="_blank" rel="noopener"><span>AR</span><strong>Receivables: open items are a posting design</strong><small>OPEN_ITEM_AR is transactional staging content. Currency precision and target posting rules can create differences, so reconcile amounts by currency and do not treat FI migration as a row-count exercise.</small><i class="material-symbols-outlined" aria-hidden="true">payments</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/444fa56a65a84453bbf5e306d754a3b3.html" target="_blank" rel="noopener"><span>PS</span><strong>Enterprise project: hierarchy plus CO prerequisites</strong><small>The current object can include WBS and milestones. Cost centre and profit centre are mandatory prerequisites, showing why project migration belongs in the cross-domain dependency graph.</small><i class="material-symbols-outlined" aria-hidden="true">workspaces</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/56bc815302c447fd84ce683df838dafa.html" target="_blank" rel="noopener"><span>PP</span><strong>Routing: migration can require post-load validation</strong><small>The 2608 Routing object supports selected additional standard fields through the modeler. SAP also documents follow-on validation and cost simulation, so “loaded successfully” is not the end of the object run.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="foundation" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Foundation</p>
      <h2>Load the identities that later documents reference.</h2>
      <p>These objects sit low in the dependency graph. Wrong numbering or missing organisational extensions will surface later as hundreds of “transaction” errors.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/16b8c81e2269493a8b8b44b3407de195.html" target="_blank" rel="noopener"><span>BP</span><strong>Supplier / Business Partner</strong><small>General, company-code and purchasing-organisation views. Decide number ranges, roles, addresses, tax data, bank data and partner cross-references before dependent purchasing documents.</small><i class="material-symbols-outlined" aria-hidden="true">badge</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>BP</span><strong>Customer / Business Partner</strong><small>General, company-code and sales-area views. In S/4HANA the Business Partner model is central, so customer migration is also a CVI and identity design topic.</small><i class="material-symbols-outlined" aria-hidden="true">person</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/f86dc2eb1f8b48c880a7607213104b27/289644d401a844878ce84670517dfa98.html" target="_blank" rel="noopener"><span>MAT</span><strong>Product</strong><small>Core product master plus relevant plant, sales, purchasing, valuation, UoM and storage data. If internal numbering is used, keep the legacy number because later objects can reuse the ID mapping.</small><i class="material-symbols-outlined" aria-hidden="true">category</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/9c62e3f7092744d49021051301263e85.html" target="_blank" rel="noopener"><span>EXT</span><strong>Product — new organisational levels</strong><small>Use when an existing product must be extended to new plants, valuation areas, distribution chains or storage locations. It is not a general update tool for existing organisational data.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>FIN</span><strong>G/L account and financial masters</strong><small>Chart/company-code financial master data required by postings. Confirm which masters are configuration, which are migration objects, and which must already exist.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>CO</span><strong>Cost centre and profit centre</strong><small>Controlling dimensions referenced by products, assets, projects, purchase account assignments and financial postings. Hierarchy and validity design matter.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>REF</span><strong>Banks, exchange/reference data and dependent masters</strong><small>Check the released object list and target configuration. Some reference data is loaded, some is configured, and some is already delivered by SAP.</small><i class="material-symbols-outlined" aria-hidden="true">currency_exchange</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="domain-master" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Sales and procurement masters</p>
      <h2>Commercial documents depend on more than customer, supplier and product.</h2>
      <p>Pricing and sourcing failures often look like order-load defects but start in missing master relationships.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>SD</span><strong>Pricing condition records</strong><small>Where a released migration object exists, migrate the condition records needed for the new pricing design. Do not copy old condition technique blindly if greenfield pricing was redesigned.</small><i class="material-symbols-outlined" aria-hidden="true">sell</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>SD</span><strong>Customer-product / sales master relationships</strong><small>Customer-material information and other sales master relationships can be relevant to order creation. Confirm exact object availability and scope.</small><i class="material-symbols-outlined" aria-hidden="true">link</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>MM</span><strong>Purchasing info records</strong><small>Supplier-product purchasing conditions and data. Sequence after supplier and product and before open purchasing documents that need the relationship.</small><i class="material-symbols-outlined" aria-hidden="true">request_quote</i></a>
      <a href="https://help.sap.com/S4_OP_MO" target="_blank" rel="noopener"><span>MM</span><strong>Source lists and source-of-supply data</strong><small>Used where source determination must continue after go-live. Treat dates, plants, suppliers and product references as dependency-sensitive keys.</small><i class="material-symbols-outlined" aria-hidden="true">list_alt</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/3fb24f963798441da2867718ca6f711f.html" target="_blank" rel="noopener"><span>MM</span><strong>Purchasing contracts</strong><small>Open outline agreements can be part of day-one procurement. Restrictions exist for item categories and service scenarios, so inspect the object documentation.</small><i class="material-symbols-outlined" aria-hidden="true">contract</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>SD</span><strong>Sales contracts</strong><small>Continuing customer commitments can be loaded when supported. Decide whether old validity, release status and consumed quantities still make business sense in the new solution.</small><i class="material-symbols-outlined" aria-hidden="true">description</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="production-master" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Production and engineering</p>
      <h2>Build the production graph before open production orders.</h2>
      <p>A production order references a chain of master data. The exact chain depends on the process and target scope.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>PP</span><strong>Bill of Material</strong><small>Material components and structure used by production and engineering. Confirm change-number, alternative BOM and variant requirements.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>PP</span><strong>Work centre / resource</strong><small>Capacity and costing-relevant production resource. Cost centres and activity types may be prerequisites.</small><i class="material-symbols-outlined" aria-hidden="true">precision_manufacturing</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/56bc815302c447fd84ce683df838dafa.html" target="_blank" rel="noopener"><span>PP</span><strong>Routing / recipe / task-list family</strong><small>Operations, sequences, work centres and control data. For QM or maintenance task lists, use the object designed for that business purpose.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>PP</span><strong>Production version</strong><small>Links product, BOM and routing for production selection. It is often a gate before production-order migration.</small><i class="material-symbols-outlined" aria-hidden="true">join_inner</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>PP</span><strong>Production supply area and planning masters</strong><small>Supply and planning structures can be required by product and production execution. Check the activated manufacturing scope.</small><i class="material-symbols-outlined" aria-hidden="true">factory</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>CLASS</span><strong>Characteristics, classes and classification</strong><small>Shared foundation for configurable products, batches, equipment and other classified objects. Load reusable classification structures before assignments that reference them.</small><i class="material-symbols-outlined" aria-hidden="true">tune</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="quality-warehouse" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Quality, warehouse and asset operations</p>
      <h2>Adjacent logistics domains create hidden prerequisites.</h2>
      <p>Even when the migration lead sits in SD/MM, warehouse, quality and maintenance data can block end-to-end execution on day one.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>QM</span><strong>Inspection methods and characteristics</strong><small>Quality master data used by plans and inspection processing. Sequence reusable methods and characteristics before plans that reference them.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/cbb6d3e190d84558b7b3ddb90495801c.html" target="_blank" rel="noopener"><span>QM</span><strong>Inspection plans and quality master data</strong><small>Confirm task-list type, product, plant and catalogue dependencies. Quality setup can also be part of product organisational data.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>EWM</span><strong>Warehouse product data</strong><small>Warehouse-relevant product attributes can be part of product migration or extensions. Confirm warehouse-specific migration content for the selected EWM deployment and release.</small><i class="material-symbols-outlined" aria-hidden="true">warehouse</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>EWM</span><strong>Warehouse structures and stock-related data</strong><small>Bins, fixed-bin assignments and warehouse stock require an EWM-specific cutover design. Do not assume Inventory Management stock and EWM stock are the same load.</small><i class="material-symbols-outlined" aria-hidden="true">view_in_ar</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>PM</span><strong>Equipment and functional locations</strong><small>Technical objects can carry classification, serialisation, location and maintenance relationships that need their own sequence.</small><i class="material-symbols-outlined" aria-hidden="true">build</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/b97c17855d78480ead0cebb32c4a346f.html" target="_blank" rel="noopener"><span>PM</span><strong>Maintenance plans, task lists and open maintenance orders</strong><small>Operational maintenance continuity may require both master and open transaction data. Check prerequisites and status restrictions for each object.</small><i class="material-symbols-outlined" aria-hidden="true">engineering</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/444fa56a65a84453bbf5e306d754a3b3.html" target="_blank" rel="noopener"><span>PS</span><strong>Projects / WBS / enterprise project data</strong><small>Projects often reference company code, plant, profit centre, cost centre and business partners. Separate project master structures from open financial and logistics commitments.</small><i class="material-symbols-outlined" aria-hidden="true">workspaces</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="open-business" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Open business</p>
      <h2>Migrate only the transaction state that can continue cleanly.</h2>
      <p>Open does not automatically mean migratable. Follow-on documents, partial delivery, partial invoice, approval status and document category can change the answer.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/da48c42d19e6484a90795feb509d2fc4.html" target="_blank" rel="noopener"><span>SD</span><strong>Open sales orders</strong><small>Typical object content includes header, item, partners, schedule lines, texts and conditions where supported. Public Cloud documentation explicitly limits the object by scenario; partially executed chains may need to be closed or redesigned.</small><i class="material-symbols-outlined" aria-hidden="true">shopping_cart</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>SD</span><strong>Open sales contracts and other released sales documents</strong><small>Use only where the target release provides a migration object and the remaining commitment can continue without recreating historical follow-on flow.</small><i class="material-symbols-outlined" aria-hidden="true">contract_edit</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>MM</span><strong>Open purchase orders</strong><small>Only the remaining open business should move. Delivered or invoiced portions and unsupported item categories require a business rule: close, cancel, split, recreate or retain in legacy.</small><i class="material-symbols-outlined" aria-hidden="true">shopping_bag</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/bcac78c2e4454b0a8f1409a06e447b2f.html" target="_blank" rel="noopener"><span>PP</span><strong>Open production orders</strong><small>For Public Edition 2608, Created and Released source status are supported and migrated orders are created in target status Created. Reconcile reservations, components, quantities and execution state with the production cutover plan.</small><i class="material-symbols-outlined" aria-hidden="true">manufacturing</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/846562085c054f16ae13d851557cc086.html" target="_blank" rel="noopener"><span>PM</span><strong>Open maintenance orders</strong><small>Move only work that must continue in S/4 and only with the supported predecessor masters and status model. The current Public Edition object supports internal numbering only.</small><i class="material-symbols-outlined" aria-hidden="true">handyman</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="balances" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Balances, stock and finance</p>
      <h2>This is where technical migration becomes accounting.</h2>
      <p>Quantities and values must tell the same story. A green technical log cannot approve financial cutover.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>STK</span><strong>Material inventory balance</strong><small>Initial stock by supported stock categories and special-stock cases. Product valuation data is a prerequisite when the system must calculate stock values.</small><i class="material-symbols-outlined" aria-hidden="true">inventory</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/c633ded541d44facae2a4938fd3c2e3c.html" target="_blank" rel="noopener"><span>AR</span><strong>Accounts Receivable open items</strong><small>Customer open receivables at cutover. Reconcile count, currency, amount, due-date logic, tax and migration clearing accounts.</small><i class="material-symbols-outlined" aria-hidden="true">payments</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/3178ae18e33b49fa9fb440352a2cdcfa.html" target="_blank" rel="noopener"><span>AP</span><strong>Accounts Payable open items</strong><small>Supplier liabilities that remain open after go-live. Close as much noise as possible before extraction and define how partial payments, special G/L and local requirements are handled.</small><i class="material-symbols-outlined" aria-hidden="true">receipt</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>GL</span><strong>G/L balances and open/line items</strong><small>Load the financial opening position required by the target design. Historical account balances can be a separate supported requirement from historical operational documents.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance_wallet</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>AA</span><strong>Fixed asset master data</strong><small>Asset identity, assignments and depreciation-related master data. Cost centres, profit centres and other account assignments must be ready.</small><i class="material-symbols-outlined" aria-hidden="true">apartment</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/3c0dddd9424549fe9c46db30780c128c.html" target="_blank" rel="noopener"><span>AA</span><strong>Fixed asset postings / legacy values</strong><small>Coordinate with asset master migration and the Asset Accounting legacy-transfer date. Public Cloud documentation separates master data and posting/value steps for current objects.</small><i class="material-symbols-outlined" aria-hidden="true">calculate</i></a>
      <a href="https://help.sap.com/S4_CE_MO" target="_blank" rel="noopener"><span>BANK</span><strong>Bank and cash opening position</strong><small>Decide what is a master, what is a balance and what stays as bank-statement history. The target opening balance must reconcile to the financial cutover model.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="not-migration" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Do not force into Migration Cockpit</p>
      <h2>Some requested data belongs to another solution path.</h2>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/cutover/#history"><span>HIST</span><strong>Closed operational history</strong><small>Old completed orders, deliveries, invoices and document flow usually belong to legacy retention, archive or analytics rather than operational initial load.</small><i class="material-symbols-outlined" aria-hidden="true">history</i></a>
      <a href="/labs/enterprise-context/migration/tooling/#integration-after-go-live"><span>RUN</span><strong>Recurring replication</strong><small>If data must continue arriving after go-live, design an integration with monitoring and recovery. Do not keep a migration loader as a shadow production interface.</small><i class="material-symbols-outlined" aria-hidden="true">sync</i></a>
      <a href="/labs/enterprise-context/migration/tooling/#custom"><span>UPD</span><strong>Mass updates of existing target records</strong><small>Migration objects are not general-purpose mass-maintenance tools. Use released mass-maintenance apps, APIs or governed application functions when the business needs updates after initial migration.</small><i class="material-symbols-outlined" aria-hidden="true">edit_note</i></a>
      <a href="/labs/enterprise-context/migration/domain-playbooks/#wave-0"><span>CFG</span><strong>Target configuration</strong><small>Organisational and process configuration follows implementation and transport/configuration governance. A migration project can depend on it without being responsible for creating it.</small><i class="material-symbols-outlined" aria-hidden="true">settings</i></a>
      <a href="/labs/enterprise-context/migration/tooling/#custom"><span>DB</span><strong>Direct table writes</strong><small>A table may look familiar from ECC while the S/4 business object, validations or persistence model has changed. Use supported business interfaces and migration content.</small><i class="material-symbols-outlined" aria-hidden="true">block</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Object readiness card</p>
      <h2>Freeze one card for every migration object.</h2>
      <p>This prevents the common problem where “Customer is ready” means something different to extraction, functional, test and business teams.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/cutover/"><span>1</span><strong>Scope and owner</strong><small>Business purpose, target release, migration approach, business owner, data owner, technical owner, record volume and cutover criticality.</small><i class="material-symbols-outlined" aria-hidden="true">assignment</i></a>
      <a href="/labs/enterprise-context/migration/tooling/#id-mapping"><span>2</span><strong>Keys and mapping</strong><small>Source key, target key, internal/external numbering, value mappings, fixed values, code conversion and cross-reference storage.</small><i class="material-symbols-outlined" aria-hidden="true">key</i></a>
      <a href="/labs/enterprise-context/migration/domain-playbooks/"><span>3</span><strong>Dependencies</strong><small>Configuration prerequisites, predecessor migration objects, required master relationships, ordering constraints and post-processing.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/labs/enterprise-context/migration/tooling/#custom"><span>4</span><strong>Extensions and gaps</strong><small>Custom fields, modeler enhancement, unsupported source data, target API capability and the decision for each gap.</small><i class="material-symbols-outlined" aria-hidden="true">extension</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#reconciliation"><span>5</span><strong>Acceptance evidence</strong><small>Record count, control totals, business samples, target reports, rejected-record threshold, financial tie-out and sign-off owner.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
