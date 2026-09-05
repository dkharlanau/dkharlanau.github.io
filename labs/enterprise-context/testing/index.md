---
layout: default
title: "SAP Testing Strategy for S/4HANA Delivery"
description: "A practical SAP testing playbook for component, integration, regression, UAT, authorization, performance, and post-deployment checks."
permalink: /labs/enterprise-context/testing/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-03
last_reviewed: 2026-09-03
publication_wave: "sap-delivery-review-2026-09"
review_method: "current SAP primary sources + practitioner boundary review for PTF + page-level factual review"
structured_data:
  type: TechArticle
primary_topic: "sap-testing"
hide_global_cta: true
career_impact: mapped
career_skills:
  - delivery-testing
  - delivery-lifecycle
tags:
  - sap
  - s4hana
  - testing
  - regression-testing
  - test-automation
  - abap-unit
  - ptf
  - cloud-alm
  - tricentis
  - logistics
  - integration
search_intent: "SAP S/4HANA testing strategy ABAP Unit PTF Cloud ALM Test Automation Tool Tricentis regression end to end logistics"
semantic_links:
  - type: "related_topic"
    title: "SAP Development Architecture"
    url: "/labs/enterprise-context/development/"
  - type: "related_topic"
    title: "SAP Integration Architecture"
    url: "/labs/enterprise-context/integrations/"
  - type: "related_topic"
    title: "SAP Integration Operations"
    url: "/labs/enterprise-context/integration-operations/"
  - type: "related_topic"
    title: "SAP Performance and Technical Operations"
    url: "/labs/enterprise-context/performance/"
  - type: "related_topic"
    title: "Sales Processes"
    url: "/labs/enterprise-context/sales-processes/"
  - type: "related_topic"
    title: "Procurement"
    url: "/labs/enterprise-context/procurement/"
  - type: "prerequisite"
    title: "SAP S/4HANA Deployment Models"
    url: "/labs/enterprise-context/deployment-models/"
source_links:
  - title: "SAP ABAP Cloud — Test"
    url: "https://help.sap.com/docs/abap-cloud/abap-cloud/test?locale=en-US"
  - title: "SAP ABAP Cloud — Develop Tests"
    url: "https://help.sap.com/docs/abap-cloud/abap-cloud/developing-automated-tests"
  - title: "SAPUI5 Testing Tutorial"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/468a97775123488ab3345a0c48cadd8f/291c9121e6044ab381e0b51716f97f52.html"
  - title: "SAP Cloud ALM — Test Execution Concepts"
    url: "https://help.sap.com/docs/cloud-alm/applicationhelp/test-execution-concepts"
  - title: "SAP Cloud ALM — Manual Test Cases"
    url: "https://help.sap.com/docs/cloud-alm/applicationhelp/manual-test-cases"
  - title: "SAP Cloud ALM — Integrating Test Automation Providers"
    url: "https://help.sap.com/docs/cloud-alm/setup-administration/integrating-test-automation-providers"
  - title: "Tricentis Test Automation for SAP Integrated with SAP Cloud ALM"
    url: "https://help.sap.com/docs/cloud-alm/setup-administration/tricentis-test-automation-for-sap"
  - title: "SAP S/4HANA Cloud Public Edition — Test Automation Tool FAQ"
    url: "https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/acaf51440ec84e409895cd8cde9486cb.html"
  - title: "SAP eCATT Tutorial"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/c6663103e6ad47dcb8bb830d85137077/496d2715e0221ec6e10000000a42189b.html"
  - title: "SAP eCATT — Test Data Editor"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/c6663103e6ad47dcb8bb830d85137077/49708b9f81463e90e10000000a42189c.html"
  - title: "SAP Learning — Explaining the Test Strategy"
    url: "https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-public-edition/explaining-the-test-strategy_d4b6f563-e5bb-41b5-b7e2-ec899edb756f"
  - title: "LeverX — SAP Process Test Framework (PTF): A Practical Guide to End-to-End Testing for ABAP Developers"
    url: "https://career.leverx.com/blog/sap-process-test-framework-ptf-a-practical-guide-to-end-to-end-testing-for-abap-developers"
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">SAP Enterprise</a></li><li aria-current="page">Testing</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">SAP Enterprise / Testing</p>
      <h1>Test the business risk, not only the screen.</h1>
      <p>A useful SAP test proves that the business process still works after a change: the document is correct, follow-on documents are created, postings are right, integrations finish, authorizations behave as expected, failures can be recovered, and the result can be explained.</p>
      <a class="research-canvas__button" href="#test-stack">Build the test stack <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Testing playbook scope">
      <p>Testing layers</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Fast</strong><small>Code and component checks</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Flow</strong><small>Process and integration regression</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Release</strong><small>E2E, UAT and production smoke</small></div>
      <em>Source-checked against SAP Help and current SAP learning content. PTF details are also informed by recent practitioner material and must be checked against the target release.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <p><strong>Testing is not a phase after development.</strong> It starts when the change and its risks are understood. A pricing change, BAdI, interface mapping, authorization role and warehouse configuration need different test evidence.</p>
    <p><strong>Do not automate everything.</strong> Automate stable, repeatable and valuable checks. Keep human testing for new behavior, usability, business judgment and cases where the process changes faster than the script can be maintained.</p>
    <p><strong>Source boundary:</strong> ABAP Cloud, SAPUI5, SAP Cloud ALM, Tricentis, eCATT, and Public Edition Test Automation Tool statements are checked against SAP sources. The PTF section is deliberately practitioner-informed and release-dependent; it is not presented as a universal capability for every S/4HANA landscape.</p>
  </section>

  <section class="research-canvas__inventory" id="test-stack" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Test stack</p>
      <h2>Use several layers. One tool cannot prove an SAP process.</h2>
      <p>The lower layers should fail quickly and explain the defect precisely. The upper layers prove that the complete business outcome still works.</p>
    </header>
    <div class="research-route-list">
      <a href="#developer-tests"><span>L0</span><strong>Static quality gate</strong><small>ATC checks code quality, syntax, standards and many performance or correctness risks before runtime. It is a quality gate, not an end-to-end functional test.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="#developer-tests"><span>L1</span><strong>Unit and isolated component tests</strong><small>ABAP Unit, test doubles, CDS/RAP test support, QUnit and similar checks prove small units quickly and deterministically.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="#ptf"><span>L2</span><strong>Backend process regression</strong><small>Use API-level or backend process tests when the risk sits in document lifecycle, determinations, status changes and follow-on processing. PTF can fit here when it is available in the target landscape.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#tool-map"><span>L3</span><strong>UI and business-process automation</strong><small>SAPUI5 OPA5 tests, S/4HANA Cloud Test Automation Tool, Tricentis and other providers cover UI behavior or complete browser-based process flows.</small><i class="material-symbols-outlined" aria-hidden="true">web</i></a>
      <a href="#test-management"><span>L4</span><strong>Managed E2E, regression and UAT</strong><small>Test plans, traceability, owners, evidence and defects are managed as a release activity. SAP Cloud ALM can orchestrate manual and automated test cases.</small><i class="material-symbols-outlined" aria-hidden="true">assignment_turned_in</i></a>
      <a href="#non-functional"><span>L5</span><strong>Non-functional and operational tests</strong><small>Authorization, performance, volume, batch, recovery, queue behavior, monitoring and post-deployment smoke tests prove that the process can run in real operations.</small><i class="material-symbols-outlined" aria-hidden="true">monitor_heart</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="design" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Test design</p>
      <h2>A good test case is a small proof with clear evidence.</h2>
      <p>Do not start by recording clicks. Start with the business rule or failure that the test must prove.</p>
    </header>
    <div class="research-route-list">
      <a href="#design"><span>01</span><strong>State the risk</strong><small>Example: “A sales-order pricing enhancement must not change the approved price for standard customers.” The risk tells you what to assert.</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      <a href="#test-data"><span>02</span><strong>Define preconditions and data</strong><small>Name the customer, supplier, material, plant, sales area, purchasing organization, stock, role, dates and prerequisite documents. A test without controlled data is difficult to reproduce.</small><i class="material-symbols-outlined" aria-hidden="true">dataset</i></a>
      <a href="#design"><span>03</span><strong>Execute one meaningful action chain</strong><small>Keep steps business-readable. Separate setup from the action under test so a failed prerequisite does not look like a product defect.</small><i class="material-symbols-outlined" aria-hidden="true">play_arrow</i></a>
      <a href="#design"><span>04</span><strong>Assert business outcomes</strong><small>Check the values that matter: status, quantity, price, schedule line, document flow, stock, accounting impact, output, delivery block or invoice result.</small><i class="material-symbols-outlined" aria-hidden="true">done_all</i></a>
      <a href="#integrations"><span>05</span><strong>Assert technical outcomes where needed</strong><small>For integrations, also prove message status, correlation ID, target document, retry result and absence of duplicate processing. For performance, compare an agreed baseline.</small><i class="material-symbols-outlined" aria-hidden="true">manage_search</i></a>
      <a href="#negative-tests"><span>06</span><strong>Add a failure path</strong><small>Happy-path-only regression is weak. Test blocked credit, missing master data, duplicate messages, invalid quantities, authorization denial, timeout or another realistic failure.</small><i class="material-symbols-outlined" aria-hidden="true">error</i></a>
      <a href="#release-gates"><span>07</span><strong>Keep evidence and ownership</strong><small>Record who ran the test, the build or transport level, test data, result, defect link and key evidence. A screenshot alone is not enough when the real result is in accounting or an interface.</small><i class="material-symbols-outlined" aria-hidden="true">receipt_long</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="coverage" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Coverage model</p>
      <h2>Think in risks and variants, not in transaction-code counts.</h2>
      <p>For every critical process, combine the dimensions below. This produces a smaller and stronger regression suite than copying hundreds of historical scripts.</p>
    </header>
    <div class="research-route-list">
      <a href="#negative-tests"><span>+</span><strong>Positive path</strong><small>The main business scenario completes with the expected documents, postings and outputs.</small><i class="material-symbols-outlined" aria-hidden="true">check_circle</i></a>
      <a href="#negative-tests"><span>−</span><strong>Negative path</strong><small>A business rule rejects or blocks the process correctly and gives an actionable result.</small><i class="material-symbols-outlined" aria-hidden="true">block</i></a>
      <a href="#test-data"><span>↔</span><strong>Boundary and variant</strong><small>Test important organizational units, countries, currencies, units of measure, quantities, dates, tax or pricing variants without creating a combinatorial explosion.</small><i class="material-symbols-outlined" aria-hidden="true">tune</i></a>
      <a href="#integrations"><span>R</span><strong>Recovery path</strong><small>Prove what happens after a temporary failure: retry, reprocessing, queue restart or manual correction must not create a duplicate business result.</small><i class="material-symbols-outlined" aria-hidden="true">restart_alt</i></a>
      <a href="#non-functional"><span>NF</span><strong>Operational boundary</strong><small>Roles, volume, background jobs, interfaces and response time can break a technically correct configuration when the process reaches production scale.</small><i class="material-symbols-outlined" aria-hidden="true">speed</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="sales-regression" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Logistics example / Order to Cash</p>
      <h2>Do not stop after the sales order is saved.</h2>
      <p>A practical O2C regression chain follows the business document flow and validates the controls around it.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/sales-order/"><span>01</span><strong>Sales order</strong><small>Validate partner and material determination, pricing, tax, schedule lines, ATP confirmation, credit or delivery blocks, incompletion and the important custom logic.</small><i class="material-symbols-outlined" aria-hidden="true">shopping_cart</i></a>
      <a href="/labs/enterprise-context/shipping/"><span>02</span><strong>Delivery and goods issue</strong><small>Validate delivery relevance, quantities, batches or serials where relevant, picking status, PGI, stock impact and document flow.</small><i class="material-symbols-outlined" aria-hidden="true">local_shipping</i></a>
      <a href="/labs/enterprise-context/billing/"><span>03</span><strong>Billing and accounting</strong><small>Validate billing relevance, quantities, pricing transfer, taxes, accounting document, revenue or account determination, and any billing blocks.</small><i class="material-symbols-outlined" aria-hidden="true">request_quote</i></a>
      <a href="#integrations"><span>04</span><strong>Outputs and integrations</strong><small>Check EDI/API/event/output results, downstream document creation, acknowledgements and operational monitoring where the process crosses system boundaries.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="#negative-tests"><span>05</span><strong>Failure variants</strong><small>Include at least the failures that matter for the change: no stock, credit block, incomplete master data, pricing error, output failure, rejected interface or duplicate inbound request.</small><i class="material-symbols-outlined" aria-hidden="true">report_problem</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="procurement-regression" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Logistics example / Procure to Pay</p>
      <h2>Test the purchasing document and the financial consequence.</h2>
      <p>P2P defects often appear only when goods movement, invoice verification or account determination is reached.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/procurement/"><span>01</span><strong>Requirement and purchase order</strong><small>Validate source, supplier, material, account assignment, price, tax, delivery date, release or approval behavior and output.</small><i class="material-symbols-outlined" aria-hidden="true">description</i></a>
      <a href="/labs/enterprise-context/inventory-management/"><span>02</span><strong>Goods receipt</strong><small>Validate movement, stock type, quantity, valuation, material document, accounting document and follow-on effects such as quality inspection where relevant.</small><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a>
      <a href="/labs/enterprise-context/finance-logistics/"><span>03</span><strong>Invoice verification</strong><small>Validate three-way-match behavior, tolerance or block logic, tax, GR/IR impact and the resulting FI postings.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
      <a href="#integrations"><span>04</span><strong>Supplier and external-system integration</strong><small>Validate outbound PO, confirmations, ASN, invoice or other messages, including duplicate handling and reprocessing.</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a>
      <a href="#negative-tests"><span>05</span><strong>Failure variants</strong><small>Test invalid account assignment, quantity or price variance, missing master data, blocked supplier, rejected invoice, duplicate message and temporary integration failure where they are in scope.</small><i class="material-symbols-outlined" aria-hidden="true">report_problem</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="integrations" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Integration testing</p>
      <h2>“The message was sent” is not an end-to-end result.</h2>
      <p>An integration test should prove transport, mapping, business processing and recovery. The final assertion is usually a business object or state, not a green middleware icon.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/integrations/"><span>01</span><strong>Contract and mapping</strong><small>Validate required fields, code/value mapping, units, currencies, dates, schema/API version and semantic meaning. A technically valid payload can still be a wrong business payload.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/labs/enterprise-context/integration-operations/"><span>02</span><strong>Correlation and observability</strong><small>Keep message ID, business key, timestamp, source and target result. The test must be diagnosable from both ends.</small><i class="material-symbols-outlined" aria-hidden="true">travel_explore</i></a>
      <a href="#negative-tests"><span>03</span><strong>Idempotency and duplicate handling</strong><small>Send the same business request twice where the architecture promises idempotency. Confirm that the system does not create two orders, invoices or postings.</small><i class="material-symbols-outlined" aria-hidden="true">content_copy</i></a>
      <a href="#negative-tests"><span>04</span><strong>Retry and reprocessing</strong><small>Simulate a temporary target or mapping failure. Then recover it through the approved mechanism and prove that the final state is correct.</small><i class="material-symbols-outlined" aria-hidden="true">restart_alt</i></a>
      <a href="#negative-tests"><span>05</span><strong>Ordering and partial failure</strong><small>For queued or dependent messages, test sequence assumptions and what happens if one step fails after an earlier step has committed.</small><i class="material-symbols-outlined" aria-hidden="true">low_priority</i></a>
      <a href="/labs/enterprise-context/performance/"><span>06</span><strong>Volume and operational backlog</strong><small>A single-message test does not prove throughput. For critical high-volume interfaces, include realistic batches and verify queue or processing behavior.</small><i class="material-symbols-outlined" aria-hidden="true">speed</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="negative-tests" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Negative and recovery testing</p>
      <h2>Prove that the system fails safely.</h2>
      <p>A Lead should ask what the process does when the happy path is impossible. The failure behavior is part of the design.</p>
    </header>
    <div class="research-route-list">
      <a href="#negative-tests"><span>BIZ</span><strong>Business-rule rejection</strong><small>Insufficient stock, blocked customer or supplier, tolerance breach, missing mandatory data, invalid status transition or conflicting document state.</small><i class="material-symbols-outlined" aria-hidden="true">gavel</i></a>
      <a href="#integrations"><span>INT</span><strong>Technical dependency failure</strong><small>Timeout, authentication failure, unavailable endpoint, malformed payload, mapping error, queue stop or rejected acknowledgement.</small><i class="material-symbols-outlined" aria-hidden="true">cloud_off</i></a>
      <a href="#test-management"><span>SEC</span><strong>Authorization denial</strong><small>A user without the business role must be blocked at the correct boundary without exposing data or allowing a partial posting.</small><i class="material-symbols-outlined" aria-hidden="true">shield_lock</i></a>
      <a href="#negative-tests"><span>REC</span><strong>Recovery after failure</strong><small>After the root cause is corrected, retry or reprocess once and verify final consistency. Recovery testing is where duplicate and partial-posting defects are often found.</small><i class="material-symbols-outlined" aria-hidden="true">settings_backup_restore</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="developer-tests" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Developer tests</p>
      <h2>Push defects down to the cheapest layer.</h2>
      <p>ABAP Cloud provides ABAP Unit, ATC and test-double support for isolated tests. SAPUI5 provides QUnit, OPA5 and mock-server patterns for UI development.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/abap-cloud/abap-cloud/developing-automated-tests" target="_blank" rel="noopener"><span>AU</span><strong>ABAP Unit</strong><small>Use for methods, classes, CDS/RAP-related logic and other small components. Keep tests fast, deterministic and close to the code they protect.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/abap-cloud/abap-development-tools-user-guide/add-test-doubles" target="_blank" rel="noopener"><span>TD</span><strong>Test doubles and seams</strong><small>Replace external dependencies so the test proves the unit itself. SAP provides test-double support for interfaces and several data-access scenarios; use test seams carefully for hard-to-isolate legacy dependencies.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/abap-cloud/abap-cloud/test?locale=en-US" target="_blank" rel="noopener"><span>ATC</span><strong>ABAP Test Cockpit</strong><small>Run static quality checks early and as a transport or pipeline gate where the landscape supports it. ATC complements functional tests; it does not replace them.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/468a97775123488ab3345a0c48cadd8f/291c9121e6044ab381e0b51716f97f52.html" target="_blank" rel="noopener"><span>UI5</span><strong>QUnit and OPA5</strong><small>Use QUnit for JavaScript units and OPA5 for SAPUI5 integration scenarios. Keep these below the full cross-system E2E layer.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="ptf" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Process Test Framework / PTF</p>
      <h2>A useful backend regression pattern when the real risk is the document lifecycle.</h2>
      <p>Recent practitioner material describes SAP Process Test Framework as a backend-oriented way to run multi-step business processes without driving the full UI. That makes it interesting for document-heavy logistics regression. Treat availability and exact configuration as release-dependent and verify them in the target system.</p>
    </header>
    <div class="research-route-list">
      <a href="https://career.leverx.com/blog/sap-process-test-framework-ptf-a-practical-guide-to-end-to-end-testing-for-abap-developers" target="_blank" rel="noopener"><span>Fit</span><strong>Where PTF adds value</strong><small>Use it between ABAP Unit and UI E2E when a test must create real business documents, call business actions, follow statuses and validate follow-on results repeatedly.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="#ptf"><span>Script</span><strong>Model the business sequence</strong><small>A script should read like a process: create or change an object, pass the generated document to the next action, then validate the few business fields that prove the outcome.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#ptf"><span>Ref</span><strong>Pass document IDs through reference steps</strong><small>Do not hard-code a purchase order, delivery or freight document when the test itself creates it. Feed generated keys to the next step so the run stays repeatable.</small><i class="material-symbols-outlined" aria-hidden="true">link</i></a>
      <a href="#test-data"><span>TDC</span><strong>Separate data from the script</strong><small>Practitioner examples use reusable Test Data Containers and SECATT-based maintenance in classic ABAP contexts. Keep input and expected values outside the action logic where possible.</small><i class="material-symbols-outlined" aria-hidden="true">dataset</i></a>
      <a href="#ptf"><span>Check</span><strong>Assert only what matters</strong><small>Do not compare an entire business object if the test protects three critical outcomes. Broad checks create fragile tests that fail after harmless changes.</small><i class="material-symbols-outlined" aria-hidden="true">checklist</i></a>
      <a href="#ptf"><span>Debug</span><strong>Keep failures diagnosable</strong><small>Backend process tests can leave created business documents for analysis. Use that evidence to locate the failing action instead of only reporting “script failed”. Plan cleanup or dedicated test data so the landscape remains usable.</small><i class="material-symbols-outlined" aria-hidden="true">bug_report</i></a>
    </div>
    <p><strong>Implementation note:</strong> practitioner examples for custom classic business objects describe registering PTF business objects and actions, including transactions such as PTFBO and PTFBOA, and building action logic around PTF base classes. Do not copy those steps blindly into RAP or a different S/4HANA release; confirm the supported framework and APIs first.</p>
  </section>

  <section class="research-canvas__inventory" id="test-data" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Test data</p>
      <h2>Stable automation starts with data ownership.</h2>
      <p>Many “flaky tests” are actually uncontrolled master data, stock, dates, number ranges, roles or prerequisite documents.</p>
    </header>
    <div class="research-route-list">
      <a href="#test-data"><span>01</span><strong>Create named test-data packs</strong><small>Define reusable customers, suppliers, materials, plants, organizations, accounts and users for important process variants. Document what may be changed and what must stay stable.</small><i class="material-symbols-outlined" aria-hidden="true">inventory</i></a>
      <a href="#test-data"><span>02</span><strong>Parameterize volatile values</strong><small>Dates, quantities, external references and expected calculated values should be variants or generated values where possible, not copied literals from one successful run.</small><i class="material-symbols-outlined" aria-hidden="true">variables</i></a>
      <a href="#test-data"><span>03</span><strong>Design reset and cleanup</strong><small>Some SAP documents cannot simply be deleted. Use reversals, dedicated ranges, fresh generated business keys or isolated data so repeated tests do not corrupt their own prerequisites.</small><i class="material-symbols-outlined" aria-hidden="true">cleaning_services</i></a>
      <a href="#test-data"><span>04</span><strong>Protect production data</strong><small>Do not solve test realism by copying uncontrolled personal or sensitive production data. Use approved masking, synthetic data or governed refresh procedures.</small><i class="material-symbols-outlined" aria-hidden="true">privacy_tip</i></a>
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/c6663103e6ad47dcb8bb830d85137077/49708b9f81463e90e10000000a42189c.html" target="_blank" rel="noopener"><span>eCATT</span><strong>Test Data Containers</strong><small>Classic eCATT separates parameters and variants from scripts through Test Data Containers. This is a useful design principle even when another automation tool owns the test.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="tool-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Tool selection</p>
      <h2>Choose the lowest layer that can prove the risk.</h2>
      <p>Do not choose a tool because it is fashionable or already licensed. Choose it because it gives fast, maintainable evidence for the failure you are trying to prevent.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/abap-cloud/abap-cloud/test?locale=en-US" target="_blank" rel="noopener"><span>ABAP</span><strong>ABAP Unit + ATC</strong><small>Best first choice for custom ABAP logic and code-quality gates. Add test doubles when dependencies would make the unit test unstable.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="#ptf"><span>PTF</span><strong>Process Test Framework</strong><small>Consider for backend business-process regression in supported landscapes, especially when real SAP document creation and follow-on processing are the main risk.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/acaf51440ec84e409895cd8cde9486cb.html" target="_blank" rel="noopener"><span>PE</span><strong>S/4HANA Cloud Public Edition Test Automation Tool</strong><small>Use standard or custom test processes, test plans, scheduled execution and post-upgrade regression for Public Edition business processes. Check current release documentation for supported scope.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/cloud-alm/setup-administration/tricentis-test-automation-for-sap" target="_blank" rel="noopener"><span>TTA</span><strong>Tricentis Test Automation for SAP</strong><small>Use for automated functional E2E browser-based testing when broad UI/process coverage and Cloud ALM orchestration fit the project.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/c6663103e6ad47dcb8bb830d85137077/496d2715e0221ec6e10000000a42189b.html" target="_blank" rel="noopener"><span>eCATT</span><strong>eCATT</strong><small>Still relevant in classic ABAP landscapes for reusable automated tests, remote-system scripts and Test Workbench scenarios. Do not make it the default for a new cloud-first program without a clear reason.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/468a97775123488ab3345a0c48cadd8f/291c9121e6044ab381e0b51716f97f52.html" target="_blank" rel="noopener"><span>UI5</span><strong>QUnit + OPA5</strong><small>Use inside SAPUI5 development for JavaScript unit and UI integration tests. They reduce the number of defects that need an expensive full E2E run.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="test-management" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Test management</p>
      <h2>Cloud ALM manages the testing process; the automation provider executes the automated test.</h2>
      <p>This distinction is useful in architecture discussions. SAP Cloud ALM can prepare test cases, connect them to requirements or solution processes, organize test plans, execute manual cases, trigger automated cases, monitor progress and support defect follow-up.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/cloud-alm/applicationhelp/manual-test-cases" target="_blank" rel="noopener"><span>MAN</span><strong>Manual test cases</strong><small>Use structured activities and actions with instructions and expected results. Manual testing is appropriate for UAT, new behavior, usability and scenarios that are not worth automating.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/cloud-alm/applicationhelp/test-execution-concepts" target="_blank" rel="noopener"><span>AUTO</span><strong>Automated test cases</strong><small>Cloud ALM starts the run, while the automation provider performs the test and stores detailed execution results. Keep provider ownership clear in support and architecture diagrams.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/cloud-alm/setup-administration/integrating-test-automation-providers" target="_blank" rel="noopener"><span>API</span><strong>Automation providers</strong><small>Cloud ALM can integrate SAP and third-party providers through the supported test-automation integration model. This lets one release plan contain both manual and automated evidence.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="#release-gates"><span>Lead</span><strong>Traceability matters more than test count</strong><small>A Lead should be able to answer which requirements and risks are covered, which critical tests failed, who owns the defects and what blocks release.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="automation" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Automation strategy</p>
      <h2>Automate the regression you want to run often.</h2>
      <p>The goal is not a high automation percentage. The goal is fast confidence after every relevant change or upgrade.</p>
    </header>
    <div class="research-route-list">
      <a href="#automation"><span>YES</span><strong>Automate stable, frequent, high-risk flows</strong><small>Good candidates have clear expected results, controlled data, repeated execution and enough business impact to justify maintenance.</small><i class="material-symbols-outlined" aria-hidden="true">bolt</i></a>
      <a href="#automation"><span>NO</span><strong>Do not automate unstable design too early</strong><small>If the UI, process or rules change every sprint, the script becomes another product to maintain. First stabilize the contract you are testing.</small><i class="material-symbols-outlined" aria-hidden="true">construction</i></a>
      <a href="#automation"><span>Mix</span><strong>Keep a small release smoke suite</strong><small>Critical login, order, purchasing, posting, interface and background-process checks should finish quickly enough to run after imports and deployment.</small><i class="material-symbols-outlined" aria-hidden="true">rocket_launch</i></a>
      <a href="#automation"><span>ROI</span><strong>Measure maintenance cost too</strong><small>A test that saves ten minutes but needs two hours of repair every release is not automatically valuable. Prefer resilient business-level selectors, APIs and reusable data.</small><i class="material-symbols-outlined" aria-hidden="true">calculate</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="non-functional" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Non-functional testing</p>
      <h2>Functional correctness is necessary, not sufficient.</h2>
      <p>For business-critical SAP processes, include the operating constraints that can fail only under realistic users, volume or timing.</p>
    </header>
    <div class="research-route-list">
      <a href="#non-functional"><span>AUTH</span><strong>Roles and authorizations</strong><small>Test allowed and denied personas, organizational restrictions and sensitive actions. Include the real business role, not only an administrator.</small><i class="material-symbols-outlined" aria-hidden="true">admin_panel_settings</i></a>
      <a href="/labs/enterprise-context/performance/"><span>PERF</span><strong>Performance and volume</strong><small>Define a baseline for critical actions and high-volume jobs or interfaces. Diagnose response time by layer instead of treating “slow” as one defect type.</small><i class="material-symbols-outlined" aria-hidden="true">speed</i></a>
      <a href="/labs/enterprise-context/integration-operations/"><span>OPS</span><strong>Batch, queues and recovery</strong><small>Validate scheduling dependencies, retry behavior, queue backlogs, failed updates and operational monitoring for flows that continue after the user leaves the screen.</small><i class="material-symbols-outlined" aria-hidden="true">settings_suggest</i></a>
      <a href="#release-gates"><span>DEP</span><strong>Post-deployment smoke</strong><small>After production deployment, verify a small set of safe critical checks plus jobs, interfaces and monitoring signals. Do not discover a broken destination only when the first business order arrives.</small><i class="material-symbols-outlined" aria-hidden="true">health_and_safety</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="release-gates" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Release gates</p>
      <h2>Define what must be true before the change moves forward.</h2>
      <p>The exact gate depends on project risk, but the sequence below is a useful default for SAP changes.</p>
    </header>
    <div class="research-route-list">
      <a href="#developer-tests"><span>DEV</span><strong>Before transport</strong><small>ATC and relevant unit/component tests pass. Developer evidence explains the changed logic and important negative case.</small><i class="material-symbols-outlined" aria-hidden="true">code</i></a>
      <a href="#coverage"><span>Q</span><strong>After import to test quality system</strong><small>Run smoke tests plus the impacted component and configuration scenarios with controlled data.</small><i class="material-symbols-outlined" aria-hidden="true">move_up</i></a>
      <a href="#integrations"><span>SIT</span><strong>System and integration test</strong><small>Critical cross-component and cross-system flows pass, including recovery for the changed interfaces or asynchronous steps.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="#automation"><span>REG</span><strong>Risk-based regression</strong><small>Run the stable regression pack selected from change impact. Do not rerun every historical test without understanding relevance.</small><i class="material-symbols-outlined" aria-hidden="true">history</i></a>
      <a href="#test-management"><span>UAT</span><strong>Business acceptance</strong><small>Business owners validate process intent, important variants and usability with realistic roles. UAT confirms fitness for business use; it should not be the first place technical defects are found.</small><i class="material-symbols-outlined" aria-hidden="true">groups</i></a>
      <a href="#release-gates"><span>GO</span><strong>Go-live decision</strong><small>Critical tests are passed, release-blocking defects are resolved or formally accepted, monitoring and rollback/recovery are ready, owners are known, and the production smoke plan is prepared.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="defects" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Defect triage</p>
      <h2>A failed test should narrow the search.</h2>
      <p>Record enough evidence to reproduce the problem before changing configuration or code.</p>
    </header>
    <div class="research-route-list">
      <a href="#defects"><span>01</span><strong>Capture the business key</strong><small>Document number, message ID, user, timestamp, system/client, test-data variant and transport/build level are more useful than a screenshot of the error popup.</small><i class="material-symbols-outlined" aria-hidden="true">key</i></a>
      <a href="#defects"><span>02</span><strong>Find the failing layer</strong><small>Classify the defect first: master data, configuration, custom code, integration, authorization, background processing or performance. Then open the right diagnostic tool.</small><i class="material-symbols-outlined" aria-hidden="true">layers</i></a>
      <a href="/labs/enterprise-context/integration-operations/"><span>03</span><strong>Follow the asynchronous path</strong><small>For IDoc/RFC/queue/event/API flows, do not stop at the sending system. Follow processing until the final business result or exact failed step.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="/labs/enterprise-context/performance/"><span>04</span><strong>Use evidence before intervention</strong><small>Do not delete locks, queues, updates or documents just to make the test green. Preserve enough evidence to identify the root cause and avoid duplicates.</small><i class="material-symbols-outlined" aria-hidden="true">troubleshoot</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="anti-patterns" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Common testing mistakes</p>
      <h2>What usually creates false confidence.</h2>
      <p>These patterns make a test suite large without making a release safer.</p>
    </header>
    <div class="research-route-list">
      <a href="#anti-patterns"><span>01</span><strong>Testing only that the screen saves</strong><small>The process can save successfully and still produce wrong pricing, stock, accounting, output or follow-on documents.</small><i class="material-symbols-outlined" aria-hidden="true">visibility_off</i></a>
      <a href="#anti-patterns"><span>02</span><strong>Using UAT as the first real integration test</strong><small>Business users should validate business acceptance, not discover missing RFC destinations, broken mappings or basic code defects.</small><i class="material-symbols-outlined" aria-hidden="true">person_alert</i></a>
      <a href="#anti-patterns"><span>03</span><strong>Automating every click</strong><small>UI-heavy scripts are expensive when the real contract can be proven by a lower, more stable layer.</small><i class="material-symbols-outlined" aria-hidden="true">ads_click</i></a>
      <a href="#anti-patterns"><span>04</span><strong>Reusing dirty data</strong><small>A test that depends on yesterday’s stock, open delivery, changed customer or expired role is not a reliable regression test.</small><i class="material-symbols-outlined" aria-hidden="true">data_alert</i></a>
      <a href="#anti-patterns"><span>05</span><strong>Checking everything</strong><small>Exact comparison of every field makes automation fragile. Assert the fields, statuses, postings and messages that represent the business contract.</small><i class="material-symbols-outlined" aria-hidden="true">select_check_box</i></a>
      <a href="#anti-patterns"><span>06</span><strong>Ignoring recovery</strong><small>If the production support team must reprocess messages, restart queues or reverse documents, that recovery path deserves a test before go-live.</small><i class="material-symbols-outlined" aria-hidden="true">build_circle</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="lead-answer" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead assessment</p>
      <h2>A strong answer starts with risk and finishes with release evidence.</h2>
      <p>If an assessor asks “How would you organize SAP testing?”, the structure below is more useful than naming ten tools.</p>
    </header>
    <div class="research-route-list">
      <a href="#lead-answer"><span>1</span><strong>Start from change impact</strong><small>Identify affected business processes, integrations, roles, data and financial or operational consequences.</small><i class="material-symbols-outlined" aria-hidden="true">manage_search</i></a>
      <a href="#test-stack"><span>2</span><strong>Push coverage down the stack</strong><small>Use ATC and unit tests for code, backend/component tests for rules and document lifecycles, and fewer expensive E2E tests for the complete process.</small><i class="material-symbols-outlined" aria-hidden="true">vertical_align_bottom</i></a>
      <a href="#test-data"><span>3</span><strong>Own test data and expected results</strong><small>Make tests repeatable across environments and releases. Separate prerequisites, actions and assertions.</small><i class="material-symbols-outlined" aria-hidden="true">dataset</i></a>
      <a href="#negative-tests"><span>4</span><strong>Test failure and recovery</strong><small>Cover important negative cases, authorization boundaries, retries and duplicate protection, not only the main positive flow.</small><i class="material-symbols-outlined" aria-hidden="true">restart_alt</i></a>
      <a href="#automation"><span>5</span><strong>Automate the stable regression core</strong><small>Choose the tool by layer and deployment model. Public Edition, classic ABAP and browser-based cross-system testing can require different solutions.</small><i class="material-symbols-outlined" aria-hidden="true">smart_toy</i></a>
      <a href="#release-gates"><span>6</span><strong>Define the release gate</strong><small>Know what must pass, which defects block release, who owns acceptance, what evidence is retained and what smoke checks run after deployment.</small><i class="material-symbols-outlined" aria-hidden="true">verified_user</i></a>
    </div>
    <p><strong>Short version:</strong> I design SAP testing as a risk-based stack. Fast developer checks protect local logic; process and integration tests protect business rules and document flows; a smaller E2E regression pack proves the critical business journey. I control test data, include negative and recovery cases, automate stable high-value scenarios, keep traceability in the test-management layer, and define clear release and post-deployment gates.</p>
  </section>

  <section class="research-canvas__inventory" id="deployment" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Deployment model</p>
      <h2>The strategy stays consistent; the available tools change.</h2>
      <p>Always check the target edition and release before designing automation around a transaction or framework.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/deployment-models/"><span>PE</span><strong>S/4HANA Cloud Public Edition</strong><small>Prefer released extensibility and test capabilities. The Test Automation Tool supports standard/custom business-process test plans and regression scenarios; Cloud ALM can orchestrate supported automation providers.</small><i class="material-symbols-outlined" aria-hidden="true">cloud</i></a>
      <a href="/labs/enterprise-context/deployment-models/"><span>PR</span><strong>S/4HANA Cloud Private Edition</strong><small>You may have more classic ABAP and third-party automation options, but still choose clean, maintainable interfaces and upgrade-safe tests instead of relying on fragile GUI scripting.</small><i class="material-symbols-outlined" aria-hidden="true">cloud_sync</i></a>
      <a href="/labs/enterprise-context/deployment-models/"><span>OP</span><strong>On-premise / classic ABAP landscapes</strong><small>ABAP Unit, ATC, eCATT and other classic tools may be part of the landscape. Do not assume a framework seen in one release is available or recommended in another.</small><i class="material-symbols-outlined" aria-hidden="true">dns</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
