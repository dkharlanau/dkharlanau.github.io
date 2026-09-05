---
layout: default
title: "SAP DRF — Data Replication Framework"
description: "A practical SAP DRF guide to replication models, filters, outbound processing, monitoring, and safe recovery."
permalink: /labs/enterprise-context/integrations/drf/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-03
last_reviewed: 2026-09-03
publication_wave: "sap-integration-review-2026-09"
review_method: "current SAP primary sources + deployment-boundary review + page-level factual review"
search_intent: "SAP DRF Data Replication Framework configuration DRFIMG DRFOUT DRFLOG filters direct pooled output troubleshooting"
structured_data:
  type: TechArticle
primary_topic: "sap-integration"
hide_global_cta: true
career_impact: mapped
career_skills:
  - integration-patterns
  - integration-recovery
  - logistics-mdg
tags:
  - sap
  - sap-s4hana
  - drf
  - data-replication-framework
  - master-data
  - integration
  - mdg
  - troubleshooting
semantic_links:
  - type: "part_of"
    title: "SAP Integration Architecture — Logistics, Events and Data Distribution"
    url: "/labs/enterprise-context/integrations/"
  - type: "integrates_with"
    title: "Integration Operations & Recovery — Enterprise Context Lab"
    url: "/labs/enterprise-context/integration-operations/"
  - type: "related_topic"
    title: "MDG and Data Governance"
    url: "/labs/enterprise-context/mdg/"
source_links:
  - title: "Data Replication Framework — SAP S/4HANA Cloud Public Edition 2608"
    url: "https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/88e3f5577c84bc12e10000000a4450e5.html"
  - title: "Data Replication Framework Configuration"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/22ccb1d573f84837a0850bd039543b50/7030f4dc2b3b4d77a87000cf6829a363.html"
  - title: "Data Replication Framework - DRF"
    url: "https://help.sap.com/docs/SUPPORT_CONTENT/carab/3362176074.html"
  - title: "Filter Concept"
    url: "https://help.sap.com/docs/latest/2de74e75ac4240c68ff125a948205aee/68c049fa0a434e26b1bc3c249f64bf91.html"
  - title: "Defining the Business System"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/2de74e75ac4240c68ff125a948205aee/418df7b7a1004e6eb56b4c9e49b058e1.html"
  - title: "Replicating Locations from SAP S/4HANA via DRF"
    url: "https://help.sap.com/docs/SAP_LBN_GTT_OPTION/98d177f964dc42f8916622380de9d0c3/4ba91045409b47dbbfcf109f5429b4fc.html"
  - title: "Define Replication Models and Outbound Implementations"
    url: "https://help.sap.com/docs/sap-digital-manufacturing/integration-guide/define-replication-models-and-outbound-implementations"
# ai-discovery-managed:start
primary_topic: "sap-integration"
ai_sidecar: "/ai/pages/labs--enterprise-context--integrations--drf.json"
entity_mentions:
  - "sap-s4hana"
  - "sap-mdg"
semantic_links:
  - type: "parent_context"
    title: "SAP Integration Architecture — Logistics, Events and Data Distribution"
    url: "/labs/enterprise-context/integrations/"
  - type: "related_topic"
    title: "SAP MDG Interface Contracts — Enterprise Context Lab"
    url: "/labs/enterprise-context/mdg/interfaces/"
  - type: "related_topic"
    title: "SAP AIF — Configuration, Monitoring and Safe Reprocessing"
    url: "/labs/enterprise-context/aif/"
  - type: "related_topic"
    title: "SAP Business Partner — CVI, Configuration, Guardrails and Extensions"
    url: "/labs/enterprise-context/business-partner/"
  - type: "integrates_with"
    title: "SAP Sales Integration Map — IDocs, APIs, Events and Handoffs"
    url: "/labs/enterprise-context/sales-processes/integrations/"
  - type: "integrates_with"
    title: "Integration Operations & Recovery — Enterprise Context Lab"
    url: "/labs/enterprise-context/integration-operations/"
# ai-discovery-managed:end
---
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/labs/">Labs</a></li>
    <li><a href="/labs/enterprise-context/">SAP Enterprise</a></li>
    <li><a href="/labs/enterprise-context/integrations/">Integrations</a></li>
    <li aria-current="page">DRF</li>
  </ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">SAP Enterprise / Integration / Master Data Replication</p>
      <h1>SAP DRF.<br />The control plane for outbound replication.</h1>
      <p>Data Replication Framework decides which business objects leave the source system, which target receives them, which outbound implementation does the work, and how the replication is started. The important part is not memorizing DRFOUT. It is understanding the chain.</p>
      <a class="research-canvas__button" href="#mental-model">Build the mental model <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="DRF memory model">
      <p>Four transactions to remember</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>DRFIMG</strong><small>Configuration</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>DRFF</strong><small>Filter criteria</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>DRFOUT</strong><small>Execute replication</small></div>
      <div class="research-canvas__signal-line"><span>04</span><strong>DRFLOG</strong><small>Historical logs</small></div>
      <em>Model → implementation → target → filter → run → prove.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_tree</span>
    <p><strong>DRF is not middleware.</strong> It is the source-side replication framework. It controls selection and outbound processing. SAP Integration Suite, web services, IDocs, RFC-based communication, or another transport can still be part of the path, depending on the delivered outbound implementation.</p>
    <p><strong>Lead rule:</strong> never say “DRF sends data through technology X” as a universal statement. First check the business object and the outbound implementation.</p>
    <p><strong>Deployment boundary:</strong> DRF is also available in SAP S/4HANA Cloud Public Edition, but the classic DRFIMG, DRFF, DRFOUT, and DRFLOG transaction workflow described here applies mainly to classic ABAP, on-premise/private-edition, and documented product-specific scenarios. In Public Edition, use the delivered replication apps and configuration available for the tenant release instead of assuming classic transaction access.</p>
  </section>

  <section class="research-canvas__inventory" id="mental-model" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Mental model</p>
      <h2>DRF answers six questions.</h2>
      <p>If one answer is missing, replication is usually incomplete or impossible to support.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>1. What?</h3><p>The business object: business partner, product, location, hierarchy, project data, or another DRF-enabled object.</p></div>
      <div><h3>2. Which instances?</h3><p>Filters decide which object instances are transfer-relevant when the scenario supports filtering.</p></div>
      <div><h3>3. How?</h3><p>The outbound implementation defines the replication logic and interface behavior for the business object.</p></div>
      <div><h3>4. Where?</h3><p>The replication model links the outbound implementation to one or more target business systems.</p></div>
      <div><h3>5. When?</h3><p>Initialization, changes, manual execution, direct output, or pooled output may be available. Support is implementation-specific.</p></div>
      <div><h3>6. Did it work?</h3><p>DRF logs prove framework processing. Receiver monitoring and business reconciliation prove the final result.</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Architecture</p>
      <h2>Read the chain from object to business result.</h2>
      <p>This is the diagram to keep in your head during design and troubleshooting.</p>
    </header>
    <div class="ecg-memory-grid">
      <article class="ecg-memory-card"><span>01</span><strong>Business object</strong><h3>Source data</h3><p>A supported object exists or changes in S/4HANA or MDG.</p></article>
      <article class="ecg-memory-card"><span>02</span><strong>Selection</strong><h3>Filter scope</h3><p>DRF decides whether the instance belongs to the replication scope.</p></article>
      <article class="ecg-memory-card"><span>03</span><strong>Replication model</strong><h3>Scenario container</h3><p>The model groups outbound implementations and target assignments.</p></article>
      <article class="ecg-memory-card"><span>04</span><strong>Outbound implementation</strong><h3>Technical behavior</h3><p>This is where object-specific replication logic and supported modes matter.</p></article>
      <article class="ecg-memory-card"><span>05</span><strong>Business system</strong><h3>Target identity</h3><p>Technical settings tell DRF which receiver path belongs to the target.</p></article>
      <article class="ecg-memory-card"><span>06</span><strong>Transport</strong><h3>Interface path</h3><p>Service, IDoc, RFC-related path, middleware, or another implementation-specific channel.</p></article>
      <article class="ecg-memory-card"><span>07</span><strong>Receiver</strong><h3>Application processing</h3><p>The target validates and commits the replicated business object.</p></article>
      <article class="ecg-memory-card"><span>08</span><strong>Reconciliation</strong><h3>Business proof</h3><p>Confirm that the expected target object and business state really exist.</p></article>
    </div>
    <p class="ecg-caption"><strong>Debug in the same order:</strong> selection → DRF processing → transport → receiver → reconciliation.</p>
  </section>

  <section class="research-canvas__inventory" id="objects" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Core objects</p>
      <h2>Four terms you must not mix.</h2>
    </header>
    <div class="ecg-input-grid">
      <article><span>MODEL</span><h3>Replication Model</h3><p>The scenario container. It assigns outbound implementations and target systems and must be active before normal use.</p></article>
      <article><span>OUT</span><h3>Outbound Implementation</h3><p>Object-specific replication behavior. It determines what is technically supported: interface, parameters, filtering behavior, and replication modes.</p></article>
      <article><span>TARGET</span><h3>Business System</h3><p>The logical receiver known to DRF. Technical settings can include destination and business-object-specific communication settings.</p></article>
      <article><span>FILTER</span><h3>Filter Criteria</h3><p>Rules that reduce the data scope. They are not a replacement for business ownership of the replication scope.</p></article>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">difference</span>
    <p><strong>Replication mode ≠ output mode.</strong> In DRFOUT, common replication modes include <strong>Initialization</strong>, <strong>Changes</strong>, and <strong>Manual</strong>, where supported. In business-system settings, some objects support <strong>Direct Output</strong> or <strong>Pooled Output</strong>.</p>
    <p>Direct output can send supported changes immediately. Pooled output collects changes for later mass processing. Do not assume every outbound implementation supports every option.</p>
  </section>

  <section class="research-canvas__inventory" id="setup" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Configuration</p>
      <h2>Set up DRF from the receiver backwards.</h2>
      <p>The exact IMG nodes vary by scenario and release, but the dependency chain stays stable. Use SAP documentation for the concrete business object before copying technical values.</p>
    </header>
    <div class="ecg-determination-list">
      <article class="ecg-determination-detail"><header><div><span>00</span><small>before customizing</small></div><h3>Check that the scenario is actually DRF-enabled</h3><p class="ecg-question">Which business object, outbound implementation, interface, and replication modes does SAP deliver for this integration?</p></header><div class="ecg-decision-columns"><div><h4>Check</h4><ul><li>Business object type</li><li>Delivered outbound implementation</li><li>Supported replication and output modes</li></ul></div><div><h4>Avoid</h4><p>Designing a generic “DRF solution” before checking object support.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>01</span><small>DRFIMG</small></div><h3>Define the target business system</h3><p class="ecg-question">How does DRF identify and reach the receiver?</p></header><div class="ecg-decision-columns"><div><h4>Configure</h4><ul><li>Business system identity</li><li>Required destination or technical settings</li><li>Business object assignment where required</li><li>Communication channel where required</li></ul></div><div><h4>Lead check</h4><p>Confirm the receiver identity and transport path with the integration team before building the model.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>02</span><small>DRFIMG</small></div><h3>Create the replication model</h3><p class="ecg-question">What logical replication scenario are we defining?</p></header><div class="ecg-decision-columns"><div><h4>Maintain</h4><ul><li>Model name and description</li><li>Log retention if available</li><li>Data-model setting if the scenario requires it</li></ul></div><div><h4>Design rule</h4><p>Name models by business purpose and target, not by a random project code only.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>03</span><small>DRFIMG</small></div><h3>Assign the outbound implementation</h3><p class="ecg-question">Which delivered or custom implementation performs the replication?</p></header><div class="ecg-decision-columns"><div><h4>Maintain</h4><ul><li>Outbound implementation</li><li>Sequence if the scenario uses it</li><li>Required outbound parameters</li></ul></div><div><h4>Important</h4><p>Parameters such as package size appear in several SAP scenarios, but values are implementation-specific. Do not copy them blindly.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>04</span><small>DRFIMG</small></div><h3>Assign the target system</h3><p class="ecg-question">Where should this outbound implementation send data?</p></header><div class="ecg-decision-columns"><div><h4>Maintain</h4><ul><li>Target business system</li><li>Target-specific outbound parameters</li><li>Language or additional settings when supported</li></ul></div><div><h4>Failure pattern</h4><p>A correct model with the wrong target assignment can look like a data problem while it is really configuration.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>05</span><small>DRFF</small></div><h3>Define filters carefully</h3><p class="ecg-question">Which object instances are allowed into the replication scope?</p></header><div class="ecg-decision-columns"><div><h4>Use filters for</h4><ul><li>Organizational scope</li><li>Object attributes</li><li>Controlled rollout</li><li>Reducing initial-load risk</li></ul></div><div><h4>Boundary</h4><p>Filter concepts and Manual-mode behavior can differ by implementation. Verify the object-specific documentation.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>06</span><small>activate</small></div><h3>Activate the replication model</h3><p class="ecg-question">Is the configuration ready to be used?</p></header><div class="ecg-decision-columns"><div><h4>Before activation</h4><ul><li>Receiver checked</li><li>Outbound implementation checked</li><li>Scope checked</li><li>Volume understood</li></ul></div><div><h4>Lead check</h4><p>Treat activation as a release decision when direct output can create immediate traffic.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>07</span><small>DRFOUT</small></div><h3>Run a controlled first replication</h3><p class="ecg-question">Can we prove one small end-to-end case before volume arrives?</p></header><div class="ecg-decision-columns"><div><h4>Start narrow</h4><ul><li>One object or a small filter scope</li><li>Known target</li><li>Known expected result</li><li>Receiver monitoring ready</li></ul></div><div><h4>Then</h4><p>Only after the small case reconciles should you move to initialization or a wider productive scope.</p></div></div></article>
    </div>
  </section>

  <section class="research-canvas__inventory" id="modes" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Execution model</p>
      <h2>Choose the mode from the business need.</h2>
      <p>The names look simple. The implementation support is not universal.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Initialization</h3><p>Use for an initial or full transfer when the outbound implementation supports it. The main risk is uncontrolled volume.</p></div>
      <div><h3>Changes</h3><p>Use for changed objects when the implementation maintains the required change information and supports this mode.</p></div>
      <div><h3>Manual</h3><p>Use for controlled selection or reprocessing scenarios when supported. Filter rules can be implementation-specific.</p></div>
      <div><h3>Direct Output</h3><p>For supported business objects, changes can be sent when the object is saved. DRFOUT is not the normal trigger for those changes.</p></div>
      <div><h3>Pooled Output</h3><p>Changes are collected and later sent in a mass process. The change run must be executed or scheduled.</p></div>
      <div><h3>Scheduled run</h3><p>Useful for repeatable pooled or batch replication. Schedule only after volume, locking, recovery, and monitoring are understood.</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="runbook" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">How to use it</p>
      <h2>DRFOUT is an execution step, not the whole process.</h2>
      <p>For a controlled run, use the same sequence every time.</p>
    </header>
    <div class="research-route-list">
      <a href="#monitoring"><span>1</span><strong>Select the replication model</strong><small>Confirm that this is the intended business scenario and target.</small><i class="material-symbols-outlined" aria-hidden="true">filter_1</i></a>
      <a href="#monitoring"><span>2</span><strong>Check the outbound implementation</strong><small>Especially when the model contains several implementations.</small><i class="material-symbols-outlined" aria-hidden="true">filter_2</i></a>
      <a href="#monitoring"><span>3</span><strong>Select a supported replication mode</strong><small>Initialization, Changes, or Manual only when the implementation supports it.</small><i class="material-symbols-outlined" aria-hidden="true">filter_3</i></a>
      <a href="#monitoring"><span>4</span><strong>Control the scope</strong><small>Use the relevant model filter or manual selection rules for the concrete implementation.</small><i class="material-symbols-outlined" aria-hidden="true">filter_4</i></a>
      <a href="#monitoring"><span>5</span><strong>Execute and read the DRF result</strong><small>Do not stop at “green”. Record selected object count, generated messages, target, and errors.</small><i class="material-symbols-outlined" aria-hidden="true">filter_5</i></a>
      <a href="#monitoring"><span>6</span><strong>Follow the message outside DRF</strong><small>Use the monitor for the actual interface technology and middleware path.</small><i class="material-symbols-outlined" aria-hidden="true">filter_6</i></a>
      <a href="#monitoring"><span>7</span><strong>Reconcile the receiver</strong><small>Prove that the expected business object exists with the expected scope and state.</small><i class="material-symbols-outlined" aria-hidden="true">done_all</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="monitoring" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Monitoring</p>
      <h2>Use DRFLOG, then keep walking.</h2>
      <p>DRFLOG gives historical replication logs. DRFOUT also shows the result of the current execution. Neither one proves that the final business process is correct.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Layer 1 · Selection</h3><ul><li>Was the object selected?</li><li>Did the filter include it?</li><li>Was the correct replication mode used?</li><li>Did a Changes run actually have a change to process?</li></ul></div>
      <div><h3>Layer 2 · DRF processing</h3><ul><li>Correct model?</li><li>Correct outbound implementation?</li><li>Correct target?</li><li>Generation or framework error?</li></ul></div>
      <div><h3>Layer 3 · Transport</h3><ul><li>Service or message created?</li><li>Middleware received it?</li><li>Queue or IDoc involved?</li><li>Connectivity or authentication error?</li></ul></div>
      <div><h3>Layer 4 · Receiver</h3><ul><li>Did the target process and commit?</li><li>Validation error?</li><li>Key mapping issue?</li><li>Duplicate or ordering problem?</li></ul></div>
      <div><h3>Layer 5 · Business result</h3><ul><li>Object exists once?</li><li>Correct status and attributes?</li><li>Expected downstream process works?</li><li>Reconciliation complete?</li></ul></div>
    </div>
    <p class="ecg-caption"><strong>Tool boundary:</strong> if the outbound implementation uses IDoc, queues, SOAP, or Integration Suite, use the monitor for that technology after DRF. DRFLOG is only one part of the evidence chain.</p>
  </section>

  <section class="research-canvas__inventory" id="troubleshooting" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Troubleshooting</p>
      <h2>Start from the first missing evidence.</h2>
      <p>This avoids the usual support pattern: open five transactions, restart something, and hope.</p>
    </header>
    <div class="research-route-list">
      <a href="#mistakes"><span>A</span><strong>Zero objects selected</strong><small>Check model, mode, filter, business-object support, and whether a relevant change exists. Do not start with middleware.</small><i class="material-symbols-outlined" aria-hidden="true">search</i></a>
      <a href="#mistakes"><span>B</span><strong>Objects selected, no outbound message</strong><small>Check outbound implementation, target assignment, technical settings, required parameters, and implementation log.</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      <a href="#mistakes"><span>C</span><strong>Message created, transport failed</strong><small>Move to the actual interface monitor: connectivity, authentication, queue, web service, IDoc, or middleware evidence.</small><i class="material-symbols-outlined" aria-hidden="true">sync_problem</i></a>
      <a href="#mistakes"><span>D</span><strong>Transport green, receiver rejected</strong><small>Check payload semantics, mandatory data, key mapping, validation, sequence, and receiver application log.</small><i class="material-symbols-outlined" aria-hidden="true">report</i></a>
      <a href="#mistakes"><span>E</span><strong>Receiver green, business state wrong</strong><small>Reconcile the target object and dependent process. This is no longer a transport-only incident.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="mistakes" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Common mistakes</p>
      <h2>DRF failures are often configuration assumptions.</h2>
    </header>
    <div class="ecg-input-grid">
      <article><span>!</span><h3>Inactive model</h3><p>The model looks complete in Customizing but is not active.</p></article>
      <article><span>!</span><h3>Filter removes the object</h3><p>The interface is healthy because there is nothing to send.</p></article>
      <article><span>!</span><h3>Wrong target</h3><p>The model or outbound implementation points to another business system.</p></article>
      <article><span>!</span><h3>Delta assumed, not verified</h3><p>“Changes” or direct output is discussed as if every object supports the same mechanism.</p></article>
      <article><span>!</span><h3>Pooled output never scheduled</h3><p>Changes are collected, but no regular change run sends them.</p></article>
      <article><span>!</span><h3>Direct output chosen without support</h3><p>Direct output is business-object-dependent. Check SAP support for the concrete object.</p></article>
      <article><span>!</span><h3>Initial load is too broad</h3><p>A technically valid initialization creates unnecessary volume and operational risk.</p></article>
      <article><span>!</span><h3>DRFF behavior assumed in Manual mode</h3><p>Filter handling can be implementation-specific. Confirm it before relying on a manual resend procedure.</p></article>
      <article><span>!</span><h3>Green DRF log closes the incident</h3><p>Framework success is not receiver commit and not business reconciliation.</p></article>
    </div>
  </section>

  <section class="research-canvas__inventory" id="boundaries" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Technology boundaries</p>
      <h2>Know what DRF does not replace.</h2>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>DRF vs IDoc</h3><p>DRF controls a replication scenario. IDoc is a message technology that some scenarios can use. They are different layers.</p></div>
      <div><h3>DRF vs Integration Suite</h3><p>DRF controls source-side replication. Integration Suite can mediate, route, transform, monitor, and connect systems after the source creates the outbound interaction.</p></div>
      <div><h3>DRF vs MDG</h3><p>MDG governs master data creation and change. DRF distributes data. Governance and distribution solve different problems and often work together.</p></div>
      <div><h3>DRF vs API</h3><p>An API defines an application contract. DRF can invoke delivered service-based replication, but it is not a general replacement for every transactional API integration.</p></div>
      <div><h3>DRF vs event architecture</h3><p>Direct output can be event-triggered for supported objects, but that does not make DRF a general enterprise event broker.</p></div>
      <div><h3>DRF vs data migration</h3><p>DRF is for replication between operating systems. It is not automatically the right tool for one-time transformation-heavy migration programs.</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="case" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Worked example</p>
      <h2>Business Partner replication to a cloud receiver.</h2>
      <p>This is a learning example based on SAP-documented service scenarios. Exact implementation IDs and parameters must always be checked for the target product and release.</p>
    </header>
    <div class="research-route-list">
      <a href="#assessment"><span>1</span><strong>Receiver</strong><small>Create the business system and required technical communication settings for the cloud target.</small><i class="material-symbols-outlined" aria-hidden="true">dns</i></a>
      <a href="#assessment"><span>2</span><strong>Model</strong><small>Create a replication model for Business Partner distribution.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#assessment"><span>3</span><strong>Outbound implementation</strong><small>In specific SAP service scenarios, documentation uses outbound implementation 986_3 for BP/relationship replication via services. Treat this as a scenario value, not a universal BP setting.</small><i class="material-symbols-outlined" aria-hidden="true">settings</i></a>
      <a href="#assessment"><span>4</span><strong>Target and parameters</strong><small>Assign the target business system and only the outbound parameters required by the documented scenario.</small><i class="material-symbols-outlined" aria-hidden="true">tune</i></a>
      <a href="#assessment"><span>5</span><strong>Scope</strong><small>Apply a narrow filter or manual selection when the implementation supports it.</small><i class="material-symbols-outlined" aria-hidden="true">filter_alt</i></a>
      <a href="#assessment"><span>6</span><strong>Activation and test</strong><small>Activate the model, replicate a known BP, trace the service path, and prove the BP in the receiver.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">lightbulb</span>
    <p><strong>Lead-level shortcut:</strong> when someone says “DRF is not working”, translate it into a precise missing fact: not selected, not generated, not transported, not accepted, or not reconciled.</p>
  </section>

  <section class="research-canvas__inventory" id="assessment" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead assessment</p>
      <h2>Questions that expose whether you understand DRF.</h2>
    </header>
    <div class="research-route-list">
      <a href="#answer"><span>Q</span><strong>What is a replication model?</strong><small>A logical DRF scenario that groups outbound implementations and their target-system assignments. I also treat activation, scope, and ownership as part of the operational design.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#answer"><span>Q</span><strong>Replication model vs outbound implementation?</strong><small>The model organizes the scenario. The outbound implementation contains the object-specific technical replication behavior. Mixing these two leads to weak troubleshooting.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#answer"><span>Q</span><strong>Why did initialization work but delta did not?</strong><small>I first verify that the outbound implementation supports the selected Changes or output mode, then check change recording, filters, scheduling, and target configuration. I do not assume delta works identically for every object.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#answer"><span>Q</span><strong>When is DRFOUT not the trigger?</strong><small>For supported Direct Output scenarios, changes can be sent when the business object is saved. DRFOUT is still relevant for other modes and scenarios.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#answer"><span>Q</span><strong>How do you troubleshoot DRF?</strong><small>I split the path into selection, DRF processing, transport, receiver commit, and business reconciliation. I stop at the first missing evidence.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#answer"><span>Q</span><strong>DRF or Integration Suite?</strong><small>Usually that is the wrong either-or question. DRF can control source-side replication while Integration Suite handles mediation and connectivity. The architecture depends on the delivered interface and business need.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#answer"><span>Q</span><strong>What is the biggest production risk?</strong><small>Uncontrolled scope and weak recovery. A full load can create volume quickly, while a green DRF log can hide a receiver or reconciliation problem.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="answer" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">30-second answer</p>
      <h2>How I would explain DRF in an interview.</h2>
    </header>
    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">record_voice_over</span>
      <p><strong>“DRF is SAP’s source-side framework for controlled outbound replication of supported business objects. I use the replication model to define the scenario, the outbound implementation to define object-specific replication behavior, the business-system assignment to define the receiver, and filters to control scope. For execution I check which replication and output modes the implementation really supports. In production I troubleshoot from selection to DRF processing, transport, receiver commit, and final business reconciliation. A green DRF log alone is not completion.”</strong></p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="sources" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Primary sources</p>
      <h2>SAP documentation used to verify the framework behavior.</h2>
      <p>The explanations, troubleshooting model, and assessment framing are independently written. Concrete technical values remain scenario- and release-specific.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/88e3f5577c84bc12e10000000a4450e5.html" target="_blank" rel="noopener"><span>2608</span><strong>Data Replication Framework — SAP S/4HANA Cloud Public Edition</strong><small>Current Public Edition DRF feature set and app-based operating boundary.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/22ccb1d573f84837a0850bd039543b50/7030f4dc2b3b4d77a87000cf6829a363.html" target="_blank" rel="noopener"><span>SAP</span><strong>Data Replication Framework Configuration</strong><small>Business systems, replication models, outbound implementations, target assignment, activation.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SUPPORT_CONTENT/carab/3362176074.html" target="_blank" rel="noopener"><span>SAP</span><strong>Data Replication Framework - DRF</strong><small>DRFIMG, DRFF, DRFOUT, and DRFLOG transaction overview.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/latest/2de74e75ac4240c68ff125a948205aee/68c049fa0a434e26b1bc3c249f64bf91.html" target="_blank" rel="noopener"><span>SAP</span><strong>Filter Concept</strong><small>Transfer relevance and DRF filtering concepts.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/2de74e75ac4240c68ff125a948205aee/418df7b7a1004e6eb56b4c9e49b058e1.html" target="_blank" rel="noopener"><span>SAP</span><strong>Defining the Business System</strong><small>Business-system technical settings and Direct/Pooled Output behavior for supported objects.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_LBN_GTT_OPTION/98d177f964dc42f8916622380de9d0c3/4ba91045409b47dbbfcf109f5429b4fc.html" target="_blank" rel="noopener"><span>SAP</span><strong>Replicating Locations via DRF</strong><small>Concrete example of DRFIMG, DRFF, DRFOUT, Initialization, Changes, and Manual usage.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/sap-digital-manufacturing/integration-guide/define-replication-models-and-outbound-implementations" target="_blank" rel="noopener"><span>SAP</span><strong>Define Replication Models and Outbound Implementations</strong><small>Concrete example showing how outbound implementations represent object-specific replication behavior.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
