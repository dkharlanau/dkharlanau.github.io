---
layout: default
title: "SAP S/4HANA API-Led Migration — Design, Restart and Cutover"
description: "Lead-level guide to API-led S/4HANA migration: when to use released APIs, object sequencing, idempotency, retries, throughput, delta loads, reconciliation, and cloud boundaries."
permalink: /labs/enterprise-context/migration/api-led-migration/
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
  - api
  - odata
  - integration
  - cutover
career_impact: mapped
career_skills:
  - integration-patterns
  - integration-recovery
  - delivery-release
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">SAP Enterprise</a></li><li><a href="/labs/enterprise-context/migration/">S/4HANA Migration</a></li><li aria-current="page">API-Led Migration</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Greenfield migration / API-led loading</p>
      <h1>An API can create the object.<br />That does not make it a migration strategy.</h1>
      <p>Use an API load when the released business interface fits the required target state, the volume fits the cutover window, and restart can be proved without duplicates. If Migration Cockpit already covers the initial-load object, it usually stays the simpler migration path.</p>
      <a class="research-canvas__button" href="#decision">Decide the path <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="API migration decision">
      <p>API load gate</p>
      <div class="research-canvas__signal-line"><span>1</span><strong>Semantics</strong><small>Can the API create the required state?</small></div>
      <div class="research-canvas__signal-line"><span>2</span><strong>Recovery</strong><small>Can the run restart safely?</small></div>
      <div class="research-canvas__signal-line"><span>3</span><strong>Window</strong><small>Can measured throughput fit cutover?</small></div>
      <em>Released interface first. Measured evidence before production.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <p><strong>Default:</strong> if SAP provides a migration object that fits the initial state, use Migration Cockpit unless there is a clear reason not to. It already gives migration-specific mapping, simulation, object processing and migration control.</p>
    <p><strong>Use an API deliberately.</strong> An API normally executes the productive business object. Depending on the object and operation, normal checks, derivations, pricing, workflow, accounting or other process behaviour can be triggered. Prove the actual side effects in the target release.</p>
    <p><strong>Never use direct table writes as a performance shortcut.</strong> More technical access in Private Cloud or on-premise does not remove the business-object boundary.</p>
  </section>

  <section class="research-canvas__inventory" id="decision" data-reveal>
    <header><p class="research-canvas__eyebrow">Decision tree</p><h2>Choose API loading only after the standard migration path is checked.</h2></header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/tooling/#staging"><span>MC</span><strong>Migration object fits the initial state</strong><small>Prefer Migration Cockpit. External sources can still be cleansed and transformed outside S/4 and loaded through SAP-defined staging tables.</small><i class="material-symbols-outlined" aria-hidden="true">table_view</i></a>
      <a href="#survives-go-live"><span>API</span><strong>The same flow must continue after go-live</strong><small>A released API becomes more attractive because migration engineering can evolve into a governed production integration instead of being thrown away.</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a>
      <a href="#contract"><span>GAP</span><strong>No suitable migration object</strong><small>Prove the gap, then test whether a released API can represent the complete required business state. “There is a POST method” is not enough.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="#examples"><span>DOC</span><strong>Open transaction must be recreated</strong><small>Use an API only when creating a normal target document is the intended business result. Do not assume that legacy status, document flow or partial processing can be reconstructed.</small><i class="material-symbols-outlined" aria-hidden="true">receipt_long</i></a>
      <a href="#stock"><span>STK</span><strong>Initial stock or financial opening</strong><small>Prefer migration content designed for opening state. Posting APIs can create valid postings, but they also create accounting and operational consequences that must be designed and reconciled.</small><i class="material-symbols-outlined" aria-hidden="true">inventory</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#history"><span>HIST</span><strong>Closed historical documents</strong><small>Do not recreate history through transactional APIs by default. Keep history in the agreed legacy, archive or data platform unless a supported target requirement justifies migration.</small><i class="material-symbols-outlined" aria-hidden="true">history</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="architecture" data-reveal>
    <header><p class="research-canvas__eyebrow">Reference architecture</p><h2>Separate source truth, API execution and proof.</h2><p>The loader should be restartable without asking the target system to remember your migration run.</p></header>
    <div class="research-route-list">
      <a href="#architecture"><span>01</span><strong>Source snapshot</strong><small>Freeze or timestamp the selected source population. Store source keys, extraction timestamp and control totals.</small><i class="material-symbols-outlined" aria-hidden="true">download</i></a>
      <a href="#architecture"><span>02</span><strong>Canonical migration layer</strong><small>Cleanse, map, split, merge and enrich data before it reaches the API adapter. Keep transformations versioned.</small><i class="material-symbols-outlined" aria-hidden="true">transform</i></a>
      <a href="#dependency"><span>03</span><strong>Dependency queue</strong><small>Release a record only when required target keys and prerequisite objects exist.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#execution-ledger"><span>04</span><strong>API adapter + execution ledger</strong><small>Record request identity, source key, target key, attempt, response class, timestamp and final state.</small><i class="material-symbols-outlined" aria-hidden="true">api</i></a>
      <a href="#reconciliation"><span>05</span><strong>Independent reconciliation</strong><small>Compare the target business state with source control totals and accepted business rules. API 2xx is transport evidence, not migration acceptance.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="contract" data-reveal>
    <header><p class="research-canvas__eyebrow">API contract review</p><h2>Read the interface as a business contract.</h2></header>
    <div class="research-route-list">
      <a href="#contract"><span>C</span><strong>Create semantics</strong><small>Which header, item and child entities can be created together? Which fields are derived by S/4? Which fields cannot be set at creation time?</small><i class="material-symbols-outlined" aria-hidden="true">add_box</i></a>
      <a href="#contract"><span>U</span><strong>Update semantics</strong><small>Can the fields required for delta loads be changed? Is the update deep or entity-by-entity? Does the API require ETags or another concurrency control?</small><i class="material-symbols-outlined" aria-hidden="true">edit</i></a>
      <a href="#contract"><span>ID</span><strong>Numbering and external identity</strong><small>Can the legacy key be supplied, or is the target key generated? Never design dependent loads before this is known.</small><i class="material-symbols-outlined" aria-hidden="true">key</i></a>
      <a href="#contract"><span>FX</span><strong>Side effects</strong><small>Check pricing, ATP, credit, workflow, output, tax, accounting, change documents and other logic relevant to the chosen business operation.</small><i class="material-symbols-outlined" aria-hidden="true">bolt</i></a>
      <a href="#performance"><span>VOL</span><strong>Batch and throughput rules</strong><small>Check batch support, changeset restrictions, payload size, parallelism and practical receiver capacity. Test with realistic business validation enabled.</small><i class="material-symbols-outlined" aria-hidden="true">speed</i></a>
      <a href="#recovery"><span>ERR</span><strong>Error and reversal model</strong><small>Know what a partial success looks like, what can be retried, and how an accepted but wrong object is corrected or reversed.</small><i class="material-symbols-outlined" aria-hidden="true">error</i></a>
      <a href="#public-cloud"><span>SEC</span><strong>Security and communication setup</strong><small>Confirm the released communication scenario, arrangement, authentication method and authorisations for the exact API and deployment model.</small><i class="material-symbols-outlined" aria-hidden="true">lock</i></a>
      <a href="#contract"><span>EXT</span><strong>Custom fields</strong><small>Confirm whether required custom fields are exposed and writable. Availability differs by API, entity and extension model.</small><i class="material-symbols-outlined" aria-hidden="true">extension</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="examples" data-reveal>
    <header><p class="research-canvas__eyebrow">Current API examples</p><h2>Useful APIs exist, but each one has its own migration shape.</h2><p>Examples below use current SAP S/4HANA Cloud Public Edition 2608 documentation. Re-check the target release before design freeze.</p></header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/85043858ea0f9244e10000000a4450e5.html" target="_blank" rel="noopener"><span>BP</span><strong>Business Partner — API_BUSINESS_PARTNER</strong><small>The OData API supports create, read, update and delete operations for Business Partner, Customer and Supplier data. SAP documents deep POST and batch processing. Treat BP role and organisational dependencies as part of the load contract.</small><i class="material-symbols-outlined" aria-hidden="true">badge</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/3a1c6785160b4a818bf125933891c008.html" target="_blank" rel="noopener"><span>MAT</span><strong>Product — OData V4, Version 2</strong><small>SAP documents Product Version 2 as a synchronous CRUD API. The current service supports external number ranges only, so numbering design must be checked before dependent loads.</small><i class="material-symbols-outlined" aria-hidden="true">category</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/ccf66cce781c4a9a988d2553da64ffa5.html" target="_blank" rel="noopener"><span>V2</span><strong>Product Master — API_PRODUCT_SRV</strong><small>The older A2X API still supports CRUD and batch. Current SAP guidance recommends Product Version 2 for most entities and keeps API_PRODUCT_SRV mainly for the documented text entities. Do not design a new loader from an old API name alone.</small><i class="material-symbols-outlined" aria-hidden="true">update</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/03c04db2a7434731b7fe21dca77440da/17f4a94ed364458ba96b399d43fd1779.html" target="_blank" rel="noopener"><span>SO</span><strong>Sales Order — API_SALES_ORDER_SRV</strong><small>The OData V2 API can create and change sales orders. SAP documents only one sales order per change set of a batch request, so the API contract directly affects throughput design.</small><i class="material-symbols-outlined" aria-hidden="true">shopping_cart</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/03c04db2a7434731b7fe21dca77440da/c09676370b0146ba976081e3da23a692.html" target="_blank" rel="noopener"><span>ETAG</span><strong>Sales Order concurrency</strong><small>SAP documents ETag handling for relevant Sales Order operations. A migration delta process must respect current target state instead of overwriting concurrent changes.</small><i class="material-symbols-outlined" aria-hidden="true">compare_arrows</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/bb9f1469daf04bd894ab2167f8132a1a/46dcde53d7964b768dcf75f97f4e3db9.html" target="_blank" rel="noopener"><span>PO</span><strong>Purchase Order — API_PURCHASEORDER_PROCESS_SRV</strong><small>The current OData API supports reading, creating and changing purchase-order data. Validate item category, schedule line, account assignment and process-side-effect requirements before using it as an open-PO loader.</small><i class="material-symbols-outlined" aria-hidden="true">shopping_bag</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="stock" data-reveal>
    <header><p class="research-canvas__eyebrow">Inventory boundary</p><h2>Reading stock and creating stock are different interfaces.</h2></header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/3f57e7df4a114edabffe8b2d581a59ed/f68f51a4dc2e46779877a10a301d9138.html" target="_blank" rel="noopener"><span>READ</span><strong>Material Stock API is read-only</strong><small>The current Material Stock API retrieves stock; create, update and delete operations are not supported. Do not infer a stock-load capability from the existence of a stock API.</small><i class="material-symbols-outlined" aria-hidden="true">visibility</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/3f57e7df4a114edabffe8b2d581a59ed/8bb0d08295044ee3af444b4f2a6e4457.html" target="_blank" rel="noopener"><span>POST</span><strong>Material Document API posts movements</strong><small>API_MATERIAL_DOCUMENT_SRV can create material documents. Using it for opening stock is a posting design, not a neutral copy operation. Movement type, valuation, batch or serial data and accounting reconciliation must be explicit.</small><i class="material-symbols-outlined" aria-hidden="true">swap_horiz</i></a>
      <a href="/labs/enterprise-context/migration/object-catalog/#balances"><span>MC</span><strong>Prefer the released stock migration object when it fits</strong><small>Migration content is designed for initial state and should be checked before engineering a posting-based alternative.</small><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="dependency" data-reveal>
    <header><p class="research-canvas__eyebrow">Dependency graph</p><h2>Parallelise inside a dependency level, not across broken prerequisites.</h2></header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/domain-playbooks/#wave-1"><span>1</span><strong>Identity and shared foundations</strong><small>Business Partners, finance masters and shared references establish keys used by later objects.</small><i class="material-symbols-outlined" aria-hidden="true">badge</i></a>
      <a href="/labs/enterprise-context/migration/domain-playbooks/#wave-2"><span>2</span><strong>Operational master data</strong><small>Products and their organisational views, purchasing relationships, production, quality and warehouse masters.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="/labs/enterprise-context/migration/domain-playbooks/#wave-3"><span>3</span><strong>Open commercial and operational documents</strong><small>Release API jobs only after customer, supplier, product, organisation, pricing and account-assignment prerequisites exist.</small><i class="material-symbols-outlined" aria-hidden="true">receipt_long</i></a>
      <a href="/labs/enterprise-context/migration/domain-playbooks/#wave-4"><span>4</span><strong>Stock and opening positions</strong><small>Load and reconcile inventory and financial opening under the agreed cutover sequence. Do not let a fast API stream bypass the financial dependency plan.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="execution-ledger" data-reveal>
    <header><p class="research-canvas__eyebrow">Run control</p><h2>The execution ledger is the restart contract.</h2></header>
    <div class="research-route-list">
      <a href="#execution-ledger"><span>KEY</span><strong>Stable request identity</strong><small>Use source system + object + source key + migration wave + mapping version as a stable identity. Do not use only a timestamp or row number.</small><i class="material-symbols-outlined" aria-hidden="true">fingerprint</i></a>
      <a href="#execution-ledger"><span>MAP</span><strong>Source-to-target key map</strong><small>Store the target key returned by S/4 immediately after successful creation. Dependent records must consume this governed cross-reference.</small><i class="material-symbols-outlined" aria-hidden="true">key</i></a>
      <a href="#execution-ledger"><span>STATE</span><strong>Explicit run states</strong><small>Prepared → ready → sent → accepted → reconciled. Keep rejected, retryable, uncertain and manually resolved as separate states.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="#recovery"><span>RESP</span><strong>Keep response evidence</strong><small>Store HTTP status, SAP message, returned key, correlation ID and attempt number without storing credentials or unnecessary sensitive payloads.</small><i class="material-symbols-outlined" aria-hidden="true">receipt</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="recovery" data-reveal>
    <header><p class="research-canvas__eyebrow">Retry and idempotency</p><h2>Do not retry a POST just because the client did not receive the answer.</h2></header>
    <div class="research-route-list">
      <a href="#recovery"><span>4XX</span><strong>Business or payload error</strong><small>Fix data or mapping first. Blind retry normally repeats the same failure.</small><i class="material-symbols-outlined" aria-hidden="true">build</i></a>
      <a href="#recovery"><span>429/5XX</span><strong>Capacity or temporary technical error</strong><small>Use controlled backoff and bounded retry where the API and platform semantics allow it. Reduce concurrency before increasing retry pressure.</small><i class="material-symbols-outlined" aria-hidden="true">schedule</i></a>
      <a href="#recovery"><span>?</span><strong>Unknown outcome after timeout</strong><small>Treat this as a separate state. Query by target key or another reliable business identifier before retrying a create request.</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
      <a href="#recovery"><span>DUP</span><strong>Do not assume a universal idempotency key</strong><small>Many business APIs do not give migration-level exactly-once semantics. Prevent duplicates with receiver capabilities where available plus your own request ledger and source-key checks.</small><i class="material-symbols-outlined" aria-hidden="true">content_copy</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="performance" data-reveal>
    <header><p class="research-canvas__eyebrow">Performance proof</p><h2>Estimate first. Measure before cutover sign-off.</h2></header>
    <div class="research-route-list">
      <a href="#performance"><span>1</span><strong>Define the population</strong><small>Count business objects, child entities and expected API calls. One source row is rarely one target request.</small><i class="material-symbols-outlined" aria-hidden="true">calculate</i></a>
      <a href="#performance"><span>2</span><strong>Measure p50 and p95 runtime</strong><small>Test realistic master data, validation, pricing and accounting. Empty test objects give false confidence.</small><i class="material-symbols-outlined" aria-hidden="true">timer</i></a>
      <a href="#performance"><span>3</span><strong>Find safe concurrency</strong><small>Increase parallelism until throughput stops improving or errors and receiver pressure rise. Use that measured level, not the maximum thread count of the loader.</small><i class="material-symbols-outlined" aria-hidden="true">speed</i></a>
      <a href="#performance"><span>4</span><strong>Include retries and reconciliation</strong><small>The cutover window is not only API execution. Reserve time for rejected records, uncertain outcomes, reconciliation and approved repair.</small><i class="material-symbols-outlined" aria-hidden="true">hourglass_bottom</i></a>
      <a href="#performance"><span>5</span><strong>Keep a fallback path</strong><small>If the API cannot meet the proven window, change the migration design before go-live: reduce scope, move baseline earlier, use a migration object, or change the cutover sequence.</small><i class="material-symbols-outlined" aria-hidden="true">alt_route</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="delta" data-reveal>
    <header><p class="research-canvas__eyebrow">Delta strategy</p><h2>A baseline without a delta rule is not a cutover plan.</h2></header>
    <div class="research-route-list">
      <a href="#delta"><span>T0</span><strong>Take a controlled baseline</strong><small>Record extraction timestamp and population rules. Baseline counts and sums become reconciliation evidence.</small><i class="material-symbols-outlined" aria-hidden="true">photo_camera</i></a>
      <a href="#delta"><span>Δ</span><strong>Capture post-baseline changes</strong><small>Use source timestamps, change pointers, CDC or another trusted source mechanism. The exact mechanism belongs to the source architecture, not the S/4 API.</small><i class="material-symbols-outlined" aria-hidden="true">change_history</i></a>
      <a href="#contract"><span>U</span><strong>Classify delta operations</strong><small>Create-new, update-existing and delete or cancel are different operations. Confirm that the target API supports the required change semantics.</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#delta"><span>GO</span><strong>Close the delta before release</strong><small>Freeze or control source changes, drain the delta queue, reconcile, then release business processing according to the cutover runbook.</small><i class="material-symbols-outlined" aria-hidden="true">lock_clock</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="reconciliation" data-reveal>
    <header><p class="research-canvas__eyebrow">Acceptance evidence</p><h2>Prove the business state, not request success.</h2></header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/cutover/#reconciliation"><span>CNT</span><strong>Population control</strong><small>Selected, excluded, sent, accepted, rejected and reconciled counts must add up by object and wave.</small><i class="material-symbols-outlined" aria-hidden="true">numbers</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#reconciliation"><span>KEY</span><strong>Identity control</strong><small>Every accepted source key has the expected target key and every dependent reference resolves.</small><i class="material-symbols-outlined" aria-hidden="true">key</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#reconciliation"><span>VAL</span><strong>Business totals</strong><small>Use quantities, values, currencies, dates, open quantities, stock types and other domain controls that can detect a valid-looking but wrong target state.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
      <a href="/labs/enterprise-context/migration/cutover/#go-no-go"><span>E2E</span><strong>Process proof</strong><small>Run representative sales, procurement, production, warehouse and finance scenarios against migrated data before go/no-go.</small><i class="material-symbols-outlined" aria-hidden="true">play_circle</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="public-cloud" data-reveal>
    <header><p class="research-canvas__eyebrow">Public Cloud</p><h2>Released API + communication scenario + communication arrangement.</h2></header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/03c04db2a7434731b7fe21dca77440da/ddb476591113422c98116a80d108e2cc.html" target="_blank" rel="noopener"><span>COM</span><strong>Check the communication scenario</strong><small>SAP documents that APIs normally belong to predefined communication scenarios. The arrangement enables the actual connection and services for the tenant.</small><i class="material-symbols-outlined" aria-hidden="true">settings_ethernet</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/f7399c7374d3475a96a56a0856b5f3ee.html" target="_blank" rel="noopener"><span>0008</span><strong>Business Partner example</strong><small>Business Partner integration is documented under SAP_COM_0008 and can use OData, SOAP and replication patterns. Choose the interface pattern from the business requirement, not only from the object name.</small><i class="material-symbols-outlined" aria-hidden="true">badge</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/7c85a9907ecf4b039f4cf574cc299d93/5d55fc2d126844039fc4084ef3e945c9.html" target="_blank" rel="noopener"><span>SCOPE</span><strong>Availability depends on scope and released interface</strong><small>Use the Public Interfaces view and SAP Business Accelerator Hub to confirm that the exact create or change operation is released for the target business scope.</small><i class="material-symbols-outlined" aria-hidden="true">verified_user</i></a>
      <a href="/labs/enterprise-context/migration/tooling/#cloud-integration"><span>CPI</span><strong>Integration Suite does not bypass the boundary</strong><small>Middleware can transform, route and buffer. The receiver still has to be a released S/4 interface for the required operation.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="survives-go-live" data-reveal>
    <header><p class="research-canvas__eyebrow">After go-live</p><h2>Decide whether the loader dies or becomes a product.</h2></header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/migration/cutover/#decommission"><span>END</span><strong>One-time migration loader</strong><small>Disable technical users, routes, staging data and schedules after the agreed support window. Preserve audit evidence and source-to-target mappings.</small><i class="material-symbols-outlined" aria-hidden="true">power_settings_new</i></a>
      <a href="/labs/enterprise-context/integration-operations/"><span>LIVE</span><strong>Recurring integration</strong><small>Move it into production ownership with monitoring, SLA, retry policy, change control, security review and support runbooks.</small><i class="material-symbols-outlined" aria-hidden="true">monitor_heart</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="assessment" data-reveal>
    <header><p class="research-canvas__eyebrow">Lead assessment</p><h2>Answer the API question in this order.</h2></header>
    <div class="research-route-list">
      <a href="#assessment"><span>1</span><strong>Start from target business state</strong><small>What must exist on day one, and what lifecycle status must it have?</small><i class="material-symbols-outlined" aria-hidden="true">flag</i></a>
      <a href="#decision"><span>2</span><strong>Check Migration Cockpit first</strong><small>If a released migration object fits, explain why a custom or API route is still justified.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="#contract"><span>3</span><strong>Prove API semantics</strong><small>Create and update support, numbering, side effects, custom fields, batch limits and security must fit the requirement.</small><i class="material-symbols-outlined" aria-hidden="true">api</i></a>
      <a href="#recovery"><span>4</span><strong>Design failure first</strong><small>Show how you prevent duplicates, classify uncertain outcomes and restart from the ledger.</small><i class="material-symbols-outlined" aria-hidden="true">restart_alt</i></a>
      <a href="#performance"><span>5</span><strong>Measure the window</strong><small>Do not promise throughput from theory. Use mock data, safe concurrency and end-to-end runtime evidence.</small><i class="material-symbols-outlined" aria-hidden="true">speed</i></a>
      <a href="#reconciliation"><span>6</span><strong>Finish with reconciliation</strong><small>The migration is complete when the business state is proved and accepted, not when the last API request returns success.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>