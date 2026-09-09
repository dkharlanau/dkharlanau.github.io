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
      <p>SD, MM, PP, EWM, QM, FI and CO do not migrate independently. A sales order needs customers, products and pricing. A production order needs planning and production masters. Inventory must reconcile with valuation and accounting. These playbooks keep the dependencies visible.</p>
      <a class="research-canvas__button" href="#waves">Start with the waves <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Domain rule">
      <p>Migration logic</p>
      <div class="research-canvas__signal-line"><span>1</span><strong>Master</strong><small>Build the dependency</small></div>
      <div class="research-canvas__signal-line"><span>2</span><strong>Open</strong><small>Continue live business</small></div>
      <div class="research-canvas__signal-line"><span>3</span><strong>Prove</strong><small>Reconcile the outcome</small></div>
      <em>Module plans must converge into one business cutover.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_tree</span>
    <p><strong>Migration order is a dependency graph, not an SD/MM/FI calendar.</strong> The same object can be a prerequisite for several domains. Product, Business Partner, cost centre and profit centre are typical examples.</p>
    <p><strong>Every domain needs two owners.</strong> The functional migration lead owns the target business meaning. The business data owner approves the population, cleansing rules and reconciliation. A technical load team cannot make those decisions alone.</p>
  </section>

  <section class="research-canvas__inventory" id="waves" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Load waves</p>
      <h2>Build the target in dependency order.</h2>
      <p>The exact order changes by scope. Use SAP migration-object prerequisites to validate it for the target release.</p>
    </header>
    <div class="research-route-list">
      <a id="wave-0" href="#wave-0"><span>0</span><strong>Target configuration ready</strong><small>Organisational structures, currencies, ledgers, valuation, number ranges, document types, plants, sales areas, purchasing organisations, scope items and required extensions are usable before business data is loaded.</small><i class="material-symbols-outlined" aria-hidden="true">settings</i></a>
      <a id="wave-1" href="#wave-1"><span>1</span><strong>Identity and financial foundations</strong><small>Business Partners, customers, suppliers, banks, G/L accounts, cost centres, profit centres and other shared reference masters.</small><i class="material-symbols-outlined" aria-hidden="true">badge</i></a>
      <a id="wave-2" href="#wave-2"><span>2</span><strong>Operational master graph</strong><small>Products and organisational views, sales and purchasing masters, classification, BOMs, work centres, routings, production versions, quality and warehouse masters.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a id="wave-3" href="#wave-3"><span>3</span><strong>Open commitments</strong><small>Eligible sales contracts and orders, purchase contracts and orders, production or maintenance orders, and other in-flight business that must continue after go-live.</small><i class="material-symbols-outlined" aria-hidden="true">pending_actions</i></a>
      <a id="wave-4" href="#wave-4"><span>4</span><strong>Stock and financial opening position</strong><small>Inventory, AP/AR open items, G/L balances, asset values and other cutover balances in an agreed sequence. Quantity and value reconciliation happens here.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
      <a id="wave-5" href="#wave-5"><span>5</span><strong>Delta, interfaces and release</strong><small>Final deltas, recurring integrations, final reconciliation, business sign-off, go/no-go and controlled release to users.</small><i class="material-symbols-outlined" aria-hidden="true">rocket_launch</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="sales" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Sales / SD</p>
      <h2>Migrate the remaining customer promise.</h2>
      <p>The goal is not to reproduce every old sales document. It is to preserve the open commercial commitment that must continue in S/4.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/object-catalog/#foundation"><span>SD1</span><strong>Customer and Business Partner first</strong><small>Decide grouping, number ranges, roles, sales areas, company-code views, partner functions, addresses, tax data, credit-relevant design and legacy key mapping.</small><i class="material-symbols-outlined" aria-hidden="true">person</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#foundation"><span>SD2</span><strong>Product sales views and classification</strong><small>Sales organisation, distribution channel, units, item-category drivers, tax and availability-relevant attributes must match the new process design.</small><i class="material-symbols-outlined" aria-hidden="true">category</i></a>
      <a href="/labs/enterprise-context/pricing/"><span>SD3</span><strong>Pricing data follows the new pricing design</strong><small>Move condition records that are still required. Do not use migration as a reason to copy obsolete access sequences, condition types or customer-specific exceptions into a greenfield solution.</small><i class="material-symbols-outlined" aria-hidden="true">sell</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#open-business"><span>SD4</span><strong>Open sales documents</strong><small>Select only documents that can continue cleanly. Check follow-on documents, delivery status, billing status, rejection, blocks, schedule lines, quantities, contracts and returns against the supported migration object.</small><i class="material-symbols-outlined" aria-hidden="true">shopping_cart</i></a>
      <a href="#sales-partial"><span>SD5</span><strong>Partially executed chains need a business rule</strong><small>If part of an order was delivered or billed in legacy, the remaining open quantity may be migrated only when the supported object and business process allow it. Otherwise close, split or recreate the remaining commitment explicitly.</small><i class="material-symbols-outlined" aria-hidden="true">call_split</i></a>
      <a href="#sales-reconcile"><span>SD6</span><strong>Reconcile the promise</strong><small>Compare open order count, open quantity, requested and confirmed quantities where relevant, net value, contract remaining value, delivery blocks and a sample of customer/product/pricing relationships.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="sales-partial" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Sales decision</p>
      <h2>Do not rebuild historical document flow just to make a migrated order look old.</h2>
    </header>
    <div class="research-route-list">
      <a href="#sales-partial"><span>A</span><strong>No execution yet</strong><small>The cleanest case. Migrate the open document if the migration object supports the document type, item type, status and required fields.</small><i class="material-symbols-outlined" aria-hidden="true">check_circle</i></a>
      <a href="#sales-partial"><span>B</span><strong>Partially delivered</strong><small>Decide whether the remaining open quantity can be represented as a new target order without creating a false historical delivery chain. Reconcile remaining quantity and value, not the old document-flow appearance.</small><i class="material-symbols-outlined" aria-hidden="true">local_shipping</i></a>
      <a href="#sales-partial"><span>C</span><strong>Partially billed</strong><small>Separate the historical billed part from the remaining target obligation. Avoid recreating invoices only to reconstruct history unless a supported financial or legal requirement demands it.</small><i class="material-symbols-outlined" aria-hidden="true">receipt_long</i></a>
      <a href="#sales-partial"><span>D</span><strong>Complex follow-on flow</strong><small>For returns, intercompany, third-party, configurable products or industry-specific processes, confirm the exact migration object. If the chain cannot be represented safely, close or retain it in legacy and start a controlled target document.</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="sales-reconcile" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Sales proof</p>
      <h2>Target document creation is not enough.</h2>
    </header>
    <div class="research-route-list">
      <a href="#sales-reconcile"><span>COUNT</span><strong>Population</strong><small>Selected source documents = migrated target documents + approved exclusions + failed records still under resolution.</small><i class="material-symbols-outlined" aria-hidden="true">functions</i></a>
      <a href="#sales-reconcile"><span>QTY</span><strong>Open quantities</strong><small>Compare the remaining business quantity by customer, product and sales organisation. Include unit-of-measure conversion controls.</small><i class="material-symbols-outlined" aria-hidden="true">straighten</i></a>
      <a href="#sales-reconcile"><span>VAL</span><strong>Commercial value</strong><small>Compare expected net value and important pricing components. Differences caused by redesigned pricing must be approved, not hidden.</small><i class="material-symbols-outlined" aria-hidden="true">payments</i></a>
      <a href="#sales-reconcile"><span>FLOW</span><strong>Executable flow</strong><small>Sample migrated orders through ATP, delivery creation, picking/warehouse, goods issue, billing and accounting to prove that the migrated master and transaction data work together.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="procurement" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Procurement / MM</p>
      <h2>Migrate the open supplier commitment and the sourcing data needed to continue it.</h2>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/object-catalog/#foundation"><span>MM1</span><strong>Supplier and product foundations</strong><small>Supplier purchasing views, payment and company-code data, product purchasing/plant/valuation data and source-system key mapping must be stable first.</small><i class="material-symbols-outlined" aria-hidden="true">badge</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#domain-master"><span>MM2</span><strong>Source-of-supply masters</strong><small>Purchasing info records, source lists, contracts and related sourcing data move only when they are still valid in the new sourcing design.</small><i class="material-symbols-outlined" aria-hidden="true">request_quote</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#open-business"><span>MM3</span><strong>Open purchase orders</strong><small>Move the remaining open commitment, not the already received or invoiced history. Check item categories, service items, account assignment, subcontracting, consignment and other special processes against object restrictions.</small><i class="material-symbols-outlined" aria-hidden="true">shopping_bag</i></a>
      <a href="#procurement-grir"><span>MM4</span><strong>GR/IR boundary</strong><small>A purchase order can have history in legacy while an accounting open item remains. Decide how open goods receipt/invoice receipt exposure is represented and reconcile with Finance.</small><i class="material-symbols-outlined" aria-hidden="true">compare_arrows</i></a>
      <a href="#procurement-reconcile"><span>MM5</span><strong>Reconcile open commitment</strong><small>Compare open quantity, open value, supplier/product, delivery dates, account assignment, contract consumption and the financial GR/IR/open-item position.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="procurement-grir" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Procurement + Finance</p>
      <h2>A partially processed PO is a cross-domain decision.</h2>
    </header>
    <div class="research-route-list">
      <a href="#procurement-grir"><span>PO</span><strong>Remaining order quantity</strong><small>Represent only the part that still needs receipt or invoice processing in the target, using a supported migration object and an agreed business rule.</small><i class="material-symbols-outlined" aria-hidden="true">pending</i></a>
      <a href="#procurement-grir"><span>FI</span><strong>Historical accounting stays historical</strong><small>Do not create fake goods movements only to reproduce old PO history. Carry the required financial opening position through the approved finance migration method.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
      <a href="#procurement-grir"><span>GRIR</span><strong>Reconcile clearing exposure</strong><small>Finance and Procurement must agree the source GR/IR population, target open commitment and the treatment of unmatched receipts or invoices before go-live.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="procurement-reconcile" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Procurement proof</p>
      <h2>Prove both document continuity and accounting consistency.</h2>
    </header>
    <div class="research-route-list">
      <a href="#procurement-reconcile"><span>COUNT</span><strong>PO and contract population</strong><small>Source selected = migrated + approved exclusions + unresolved failures. Segment by document type and special process.</small><i class="material-symbols-outlined" aria-hidden="true">functions</i></a>
      <a href="#procurement-reconcile"><span>QTY</span><strong>Open quantity and value</strong><small>Compare remaining quantity and value by supplier, product, plant, purchasing organisation and account assignment.</small><i class="material-symbols-outlined" aria-hidden="true">inventory</i></a>
      <a href="#procurement-reconcile"><span>P2P</span><strong>Executable P2P test</strong><small>Receive, inspect where relevant, post invoice and account for a sample of migrated POs. A document that exists but cannot continue is a migration defect.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Inventory and warehouse</p>
      <h2>Stock is quantity, status, ownership, location and value.</h2>
      <p>“We loaded 10,000 materials” says almost nothing about inventory readiness.</p>
    </header>
    <div class="research-route-list">
      <a href="#inventory"><span>IM1</span><strong>Define the stock population</strong><small>Unrestricted, quality, blocked, special stock, batch, serialised stock, valuation type and storage location need explicit rules. Do not collapse stock categories for convenience.</small><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a>
      <a href="#inventory"><span>IM2</span><strong>Count close to cutover</strong><small>Use a controlled inventory freeze and, where practical, a physical count or strong source control to reduce the gap between extracted and real stock.</small><i class="material-symbols-outlined" aria-hidden="true">pin</i></a>
      <a href="#inventory"><span>IM3</span><strong>Reconcile quantity and value together</strong><small>Inventory Management quantity, material valuation and G/L inventory accounts must form one control set. Differences need a named owner and approved posting rule.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
      <a href="#ewm"><span>EWM</span><strong>Separate IM and EWM cutover</strong><small>Warehouse bins, warehouse product data, stock type, handling units and warehouse tasks are not the same layer as plant/storage-location inventory. Embedded or decentral EWM requires its own sequence.</small><i class="material-symbols-outlined" aria-hidden="true">warehouse</i></a>
      <a href="#inventory"><span>TEST</span><strong>Prove consumption and availability</strong><small>After load, test ATP, goods issue, goods receipt, transfer, picking and production staging on representative stock categories.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="ewm" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">EWM boundary</p>
      <h2>Do not load warehouse stock before the warehouse can own it.</h2>
    </header>
    <div class="research-route-list">
      <a href="#ewm"><span>1</span><strong>Warehouse structure ready</strong><small>Warehouse number, storage types, sections, activity areas, bins, resource and process configuration required by the target design.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#ewm"><span>2</span><strong>Warehouse product data ready</strong><small>Products must be extended with the warehouse attributes needed for putaway, picking, storage and handling.</small><i class="material-symbols-outlined" aria-hidden="true">category</i></a>
      <a href="#ewm"><span>3</span><strong>Stock and handling units aligned</strong><small>Decide whether physical stock is introduced through IM and distributed to EWM, loaded with an EWM-specific method, or handled by a combined cutover process for the selected deployment.</small><i class="material-symbols-outlined" aria-hidden="true">view_in_ar</i></a>
      <a href="#ewm"><span>4</span><strong>No open warehouse execution without a plan</strong><small>Old open warehouse tasks and waves are often better completed or cancelled in legacy. Start the target with a controlled physical state unless the exact process supports another method.</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="production" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Production / PP</p>
      <h2>Master graph first, open production second.</h2>
      <p>Production migration fails when teams treat BOM, routing and work centre as separate lists instead of one executable model.</p>
    </header>
    <div class="research-route-list">
      <a href="#production"><span>PP1</span><strong>Product and planning parameters</strong><small>MRP, procurement type, production scheduling, lot size, storage and valuation data must reflect the new target design.</small><i class="material-symbols-outlined" aria-hidden="true">category</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#production-master"><span>PP2</span><strong>BOM → work centre → routing → production version</strong><small>Sequence the production master graph and validate references, validity dates, units, capacity and costing relationships before open production orders.</small><i class="material-symbols-outlined" aria-hidden="true">precision_manufacturing</i></a>
      <a href="#quality"><span>PP3</span><strong>Quality dependencies</strong><small>Inspection setup, plans and characteristics can influence goods receipt and production release. Include QM in the production cutover rehearsal.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#open-business"><span>PP4</span><strong>Open production orders</strong><small>Move only orders that can continue safely in the target. Confirm supported statuses and how reservations, component quantities, confirmations and resulting target status are represented.</small><i class="material-symbols-outlined" aria-hidden="true">manufacturing</i></a>
      <a href="#production-wip"><span>PP5</span><strong>WIP is an accounting question too</strong><small>If work already happened in legacy, decide what remains operationally open and how WIP, variances, settlement and inventory values enter the target financial opening position.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
      <a href="#production"><span>TEST</span><strong>Prove a production cycle</strong><small>MRP or demand signal → planned/production order → staging → confirmation → goods movement → quality where relevant → settlement/accounting.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="production-wip" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Production + Finance</p>
      <h2>Do not reproduce shop-floor history by inventing target confirmations.</h2>
    </header>
    <div class="research-route-list">
      <a href="#production-wip"><span>CLOSE</span><strong>Close what can be closed</strong><small>Reduce open production before cutover. Fewer partially processed orders mean fewer reservation, WIP, variance and settlement decisions.</small><i class="material-symbols-outlined" aria-hidden="true">done_all</i></a>
      <a href="#production-wip"><span>OPEN</span><strong>Carry only the remaining operational work</strong><small>If an order must continue, migrate the supported target representation of remaining work. Keep historical confirmations and consumed history in the retained system unless explicitly required.</small><i class="material-symbols-outlined" aria-hidden="true">pending</i></a>
      <a href="#finance"><span>VALUE</span><strong>Finance owns the opening value rule</strong><small>Production and Finance must agree how inventory, WIP, variance and settlement positions are represented at the cutover key date.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="quality" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Quality / QM</p>
      <h2>Quality status can block otherwise correct stock and production.</h2>
    </header>
    <div class="research-route-list">
      <a href="#quality"><span>QM1</span><strong>Quality masters</strong><small>Inspection methods, master inspection characteristics, plans, catalogues and product inspection setup should be sequenced before processes that create inspection lots.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="#quality"><span>QM2</span><strong>Open quality work</strong><small>Decide whether existing inspection lots, notifications and blocked stock can be closed before cutover. If not, check the supported migration path and preserve the business status explicitly.</small><i class="material-symbols-outlined" aria-hidden="true">pending_actions</i></a>
      <a href="#inventory"><span>QM3</span><strong>Reconcile quality stock</strong><small>Quality inspection stock in the target must agree with Inventory Management and the physical cutover state.</small><i class="material-symbols-outlined" aria-hidden="true">inventory</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="finance" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Finance / FI</p>
      <h2>Define the opening balance architecture before the first mock load.</h2>
      <p>Finance cutover is a designed accounting transition. It is not the last technical load after logistics.</p>
    </header>
    <div class="research-route-list">
      <a href="#finance"><span>FI1</span><strong>Financial masters and dimensions</strong><small>G/L accounts, Business Partners, banks, cost centres, profit centres and required account-assignment masters must exist before transactional postings.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
      <a href="#finance"><span>FI2</span><strong>AP and AR open items</strong><small>Carry outstanding customer and supplier items with dates, currency, tax and payment attributes required for clearing and reporting. Reconcile aging and control accounts.</small><i class="material-symbols-outlined" aria-hidden="true">payments</i></a>
      <a href="#finance"><span>FI3</span><strong>G/L opening position</strong><small>Decide the migration key date, whether balances or selected line items are required, which periods are migrated and how current-year P&L/YTD requirements are represented.</small><i class="material-symbols-outlined" aria-hidden="true">calculate</i></a>
      <a href="#assets"><span>FI4</span><strong>Fixed assets</strong><small>Sequence asset master data and legacy values/postings according to the target Asset Accounting transfer date and object guidance.</small><i class="material-symbols-outlined" aria-hidden="true">apartment</i></a>
      <a href="#finance"><span>FI5</span><strong>Migration clearing accounts</strong><small>Use controlled clearing accounts where the migration method requires them. The cutover design defines which balances must be zero before business release.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
      <a href="#finance-proof"><span>FI6</span><strong>Trial balance is the gate</strong><small>Source closing position and target opening position must reconcile by company code, ledger, currency and agreed dimensions before go-live approval.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="controlling" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Controlling / CO</p>
      <h2>CO objects are dependencies, not a separate migration island.</h2>
    </header>
    <div class="research-route-list">
      <a href="#controlling"><span>CO1</span><strong>Cost centres and profit centres</strong><small>Validate hierarchy, validity, responsible owners, company-code relationships and the target reporting design before logistics and asset assignments reference them.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="#controlling"><span>CO2</span><strong>Internal orders and projects</strong><small>Move only structures and open commitments required by the target design. Close obsolete controlling objects instead of carrying them because they still exist in ECC.</small><i class="material-symbols-outlined" aria-hidden="true">workspaces</i></a>
      <a href="#production-wip"><span>CO3</span><strong>Production accounting</strong><small>WIP, variance and settlement rules must align with open production orders and the financial cutover position.</small><i class="material-symbols-outlined" aria-hidden="true">precision_manufacturing</i></a>
      <a href="#finance-proof"><span>CO4</span><strong>Reconcile by management dimensions</strong><small>Do not stop at company-code totals when the business needs profit-centre, cost-centre, project or segment reporting from day one.</small><i class="material-symbols-outlined" aria-hidden="true">analytics</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="assets" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Asset Accounting</p>
      <h2>Asset identity and asset value are two linked migration jobs.</h2>
    </header>
    <div class="research-route-list">
      <a href="#assets"><span>AA1</span><strong>Asset master data</strong><small>Asset class, company code, cost/profit assignments, locations, technical references and other attributes must match the target organisational model.</small><i class="material-symbols-outlined" aria-hidden="true">apartment</i></a>
      <a href="#assets"><span>AA2</span><strong>Legacy values or postings</strong><small>Coordinate acquisition value, accumulated depreciation, current-year depreciation and transfer date with the selected SAP migration object and fiscal-year strategy.</small><i class="material-symbols-outlined" aria-hidden="true">calculate</i></a>
      <a href="#finance-proof"><span>AA3</span><strong>Reconcile asset subledger to G/L</strong><small>Asset balances and related reconciliation accounts must agree before the finance cutover is approved.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="maintenance-projects" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Maintenance and projects</p>
      <h2>Technical objects and projects cross logistics and finance.</h2>
    </header>
    <div class="research-route-list">
      <a href="#maintenance-projects"><span>PM</span><strong>Functional locations and equipment</strong><small>Build the technical hierarchy, serialised relationships, classification and organisational assignments before plans and open maintenance orders.</small><i class="material-symbols-outlined" aria-hidden="true">engineering</i></a>
      <a href="#maintenance-projects"><span>PM</span><strong>Maintenance plans and open work</strong><small>Close completed work in legacy. Move only plans and supported open orders that must continue in S/4.</small><i class="material-symbols-outlined" aria-hidden="true">handyman</i></a>
      <a href="#maintenance-projects"><span>PS</span><strong>Projects and WBS</strong><small>Confirm project master, dates, status, responsible organisational units, profit/cost assignments and the treatment of open purchase commitments and financial balances.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="finance-proof" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Cross-domain reconciliation</p>
      <h2>Reconcile the business equations, not only each object.</h2>
    </header>
    <div class="research-route-list">
      <a href="#finance-proof"><span>STK</span><strong>Inventory quantity ↔ inventory value ↔ G/L</strong><small>Plant/storage/batch/special-stock quantities must agree with valuation and the related financial accounts after approved cutover postings.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
      <a href="#finance-proof"><span>AR</span><strong>Customer open items ↔ AR control account</strong><small>Open-item total, aging and currencies must reconcile to the G/L control position.</small><i class="material-symbols-outlined" aria-hidden="true">payments</i></a>
      <a href="#finance-proof"><span>AP</span><strong>Supplier open items ↔ AP control account</strong><small>Supplier balances and aging must reconcile to the financial opening position.</small><i class="material-symbols-outlined" aria-hidden="true">receipt</i></a>
      <a href="#finance-proof"><span>AA</span><strong>Asset values ↔ asset reconciliation accounts</strong><small>Asset acquisition and depreciation values must tie to the G/L according to the selected transfer strategy.</small><i class="material-symbols-outlined" aria-hidden="true">apartment</i></a>
      <a href="#procurement-grir"><span>GRIR</span><strong>Open procurement ↔ GR/IR exposure</strong><small>Purchasing and Finance agree the remaining receipts, invoices and clearing position.</small><i class="material-symbols-outlined" aria-hidden="true">compare_arrows</i></a>
      <a href="#production-wip"><span>WIP</span><strong>Open production ↔ WIP / settlement position</strong><small>Production and Finance agree what work remains operationally open and what value belongs in the opening balance.</small><i class="material-symbols-outlined" aria-hidden="true">manufacturing</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="ownership" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Ownership model</p>
      <h2>Every migration object needs a small accountable team.</h2>
    </header>
    <div class="research-route-list">
      <a href="#ownership"><span>BUS</span><strong>Business data owner</strong><small>Approves population, cleansing, business exceptions, reconciliation and final acceptance.</small><i class="material-symbols-outlined" aria-hidden="true">person_check</i></a>
      <a href="#ownership"><span>FUNC</span><strong>Functional migration lead</strong><small>Owns target semantics, migration-object fit, dependencies, mapping design, business validation and defect decision.</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      <a href="#ownership"><span>DATA</span><strong>Data engineering lead</strong><small>Owns extraction, transformation, source-to-target lineage, staging population, automation and technical data-quality checks.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="#ownership"><span>CTRL</span><strong>Cutover and control lead</strong><small>Owns run sequence, timing, freeze, checkpoints, evidence pack, go/no-go inputs and recovery coordination.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="#ownership"><span>SEC</span><strong>Security and platform owners</strong><small>Control temporary users, connections, privileges, secrets, migration environment access and decommissioning.</small><i class="material-symbols-outlined" aria-hidden="true">shield</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
