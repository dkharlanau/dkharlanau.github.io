---
layout: default
title: "SAP Integration Architecture — Logistics, Events and Data Distribution"
description: "A practical decision map for SAP logistics integration: APIs, IDocs, events, queues, Kafka, files, B2B, Event Mesh, TIBCO, and data distribution."
permalink: /labs/enterprise-context/integrations/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-29
hide_global_cta: true
tags:
  - sap
  - integration
  - logistics
  - event-driven-architecture
  - master-data
last_reviewed: 2026-09-29
publication_wave: "logistics-search-wave-01"
review_method: "SAP primary sources + 2026-09-29 logistics integration review + page-level editorial review"
search_intent: "SAP integration architecture with IDoc, API, events, Event Mesh and Kafka"
# ai-discovery-managed:start
structured_data:
  type: TechArticle
primary_topic: "sap-integration"
ai_sidecar: "/ai/pages/labs--enterprise-context--integrations.json"
semantic_links:
  - type: "used_by"
    title: "SAP Sales Integration Map — IDocs, APIs, Events and Handoffs"
    url: "/labs/enterprise-context/sales-processes/integrations/"
  - type: "integrates_with"
    title: "Integration Operations & Recovery — Enterprise Context Lab"
    url: "/labs/enterprise-context/integration-operations/"
  - type: "integrates_with"
    title: "SAP Development Architecture — RAP, CAP, ABAP Cloud and Clean Core"
    url: "/labs/enterprise-context/development/"
  - type: "deep_dive"
    title: "SAP DRF — Data Replication Framework"
    url: "/labs/enterprise-context/integrations/drf/"
  - type: "deep_dive"
    title: "SAP Data Migration and Controlled Bulk Loading"
    url: "/labs/enterprise-context/integrations/data-migration/"
  - type: "related_topic"
    title: "SAP Decision Cards — Enterprise Context Lab"
    url: "/labs/enterprise-context/decisions/"
source_links:
  - title: "What Is SAP Integration Suite?"
    url: "https://help.sap.com/docs/integration-suite/sap-integration-suite/decide-on-integration-technology"
  - title: "Connectivity Options"
    url: "https://help.sap.com/docs/integration-suite/sap-integration-suite/connectivity-options"
  - title: "Understanding the Basic Concepts"
    url: "https://help.sap.com/docs/integration-suite/sap-integration-suite/understanding-basic-concepts-a81309fbdc4446b98e138a328bf1776c"
  - title: "Trading Partner Management"
    url: "https://help.sap.com/docs/SAP_INTEGRATION_SUITE/sap-integration-suite/trading-partner-management"
  - title: "IDoc Adapter"
    url: "https://help.sap.com/docs/integration-suite/sap-integration-suite/idoc-adapter"
  - title: "Kafka Adapter"
    url: "https://help.sap.com/docs/SAP_INTEGRATION_SUITE/sap-integration-suite/kafka-adapter"
  - title: "What Is SAP Event Mesh?"
    url: "https://help.sap.com/docs/SAP_EM/bf82e6b26456494cbdd197057c09979f/what-is-sap-event-mesh"
  - title: "Event Mesh"
    url: "https://help.sap.com/docs/SAP_INTEGRATION_SUITE/sap-integration-suite/event-mesh"
  - title: "What Is SAP Integration Suite, Advanced Event Mesh?"
    url: "https://help.sap.com/docs/sap-integration-suite/advanced-event-mesh"
  - title: "Event Mesh Bridge"
    url: "https://help.sap.com/docs/integration-suite/sap-integration-suite/event-mesh-bridge"
  - title: "Synchronization of Master Data"
    url: "https://help.sap.com/docs/master-data-integration/sap-master-data-integration-prod/synchronization-of-master-data"
  - title: "Integration Models"
    url: "https://help.sap.com/docs/master-data-integration/sap-master-data-integration-prod/integration-models"
# ai-discovery-managed:end
---
{% assign topic = site.data.labs.enterprise_context.topics.integration_architecture_landscape %}
{% assign language = site.data.labs.enterprise_context.topics.integration_architecture_language %}
{% assign registry = site.data.labs.enterprise_context.sources.integration_registry %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li aria-current="page">Integrations</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise Context Lab / Integration Architecture</p>
      <h1>{{ topic.title }}</h1>
      <p>{{ topic.summary }}</p>
      <a class="research-canvas__button" href="#architecture-stack">Start with the architecture language <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Research status">
      <p>Reviewed architecture</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ topic.interface_types | size }}</strong><small>Interface patterns</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ topic.platforms | size }}</strong><small>Platform views</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ language.terms | size }}</strong><small>Architecture terms</small></div>
      <div class="research-canvas__signal-line"><span>04</span><strong>{{ topic.maturity.gates_complete }}/{{ topic.maturity.gates_total }}</strong><small>Maturity gates</small></div>
      <em>Primary sources reviewed together {{ topic.reviewed_together_at }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">hub</span>
    <p><strong>Problem:</strong> integration discussions often mix business meaning, protocols, brokers, middleware, and products in one sentence.</p>
    <p><strong>Working rule.</strong> First define the business meaning and interaction. Then define the contract, transport, mediation, broker or stream, application owner, and recovery model.</p>
    <a href="/labs/enterprise-context/data/topics.json">Open machine-readable topic data <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
  </section>

  <section class="research-canvas__inventory" id="lead-answer-frame" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead answer frame</p>
      <h2>Explain the dependency before the platform.</h2>
      <p>For an assessment answer, move through the design in a fixed order. A technology name is useful only after the business interaction and failure model are clear.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>01 · Business interaction</h3><p>What business object or event crosses the boundary, who owns it, and does the sender need an immediate answer?</p></div>
      <div><h3>02 · Contract and semantics</h3><p>Define identity, version, required fields, idempotency expectation, ordering need, and what a successful receiver state means.</p></div>
      <div><h3>03 · Delivery pattern</h3><p>Choose synchronous request, asynchronous command, event, queue, stream, file, or B2B exchange from the dependency and operating model.</p></div>
      <div><h3>04 · Platform fit</h3><p>Only now select the SAP or non-SAP runtime, broker, mediation layer, or streaming platform that fits the contract.</p></div>
      <div><h3>05 · Recovery</h3><p>Explain retries, duplicates, replay, ordering, monitoring, dead-letter or error handling, and the owner of recovery.</p></div>
      <div><h3>06 · Business proof</h3><p>Close with reconciliation in the receiving business object. A green transport status is not proof of business completion.</p></div>
    </div>
    <p class="ecg-caption"><strong>Evidence boundary:</strong> reviewed product documentation supports the named platform and interface behavior. The architecture stack, selection sequence, and design heuristics were reviewed as authored reasoning and are intentionally kept separate from vendor product facts.</p>
    <a href="/labs/enterprise-context/integration-operations/">Continue into runtime recovery and reconciliation <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>



  <section class="research-canvas__inventory" id="logistics-integration-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Logistics integration architecture</p>
      <h2>A warehouse interface is a state contract, not an adapter list.</h2>
      <p>Logistics integration crosses delivery ownership, physical execution, stock posting, transport, master data, and recovery. SOAP, REST, IDoc, or events describe only part of that design. Start by deciding which system owns each business state.</p>
    </header>

    <div class="ecg-decision-columns">
      <div>
        <h3>Embedded EWM</h3>
        <p>EWM and the surrounding S/4HANA applications share one system boundary. Warehouse execution is still a separate business responsibility, but many handoffs are local integration rather than a remote-system contract.</p>
      </div>
      <div>
        <h3>Decentralized SAP EWM</h3>
        <p>Warehouse execution runs in a separate SAP EWM system. Delivery, stock, master-data, and status synchronization now cross a technical boundary and need explicit monitoring and reconciliation.</p>
      </div>
      <div>
        <h3>External 3PL WMS</h3>
        <p>The warehouse is operated in a non-SAP execution system. S/4HANA should exchange business intent and confirmations while the 3PL keeps its internal picking, packing, staging, and automation logic behind its boundary.</p>
      </div>
      <div>
        <h3>SAP Logistics Management</h3>
        <p>This is a separate SAP cloud logistics product on SAP BTP. It has its own release-specific integration setup. Do not treat its integration guide as a generic recipe for every third-party WMS.</p>
      </div>
      <div>
        <h3>TM, carrier, and network integration</h3>
        <p>Transportation adds another owner. A warehouse can finish loading while carrier commitment, transport execution, events, or freight settlement are still incomplete.</p>
      </div>
    </div>

    <p class="ecg-caption"><strong>Memory hook:</strong> first identify the execution owner and the enterprise posting owner. Then define the business messages between them. Choose the protocol last.</p>

    <div class="research-route-list">
      <a href="/labs/enterprise-context/ewm/"><span>EWM</span><strong>Warehouse execution model</strong><small>Warehouse requests, tasks, orders, embedded versus decentralized boundaries, and physical execution.</small><i class="material-symbols-outlined" aria-hidden="true">warehouse</i></a>
      <a href="/labs/enterprise-context/ewm/integrations/"><span>INT</span><strong>EWM integration architecture</strong><small>S/4HANA, TM, production, quality, MES, automation, and EWM-specific integration contracts.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="/labs/enterprise-context/transportation-management/integrations/"><span>TM</span><strong>Transportation integration contracts</strong><small>ERP demand, APIs, B2B messages, execution events, and carrier-facing integration.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="/labs/enterprise-context/integration-operations/"><span>OPS</span><strong>Integration operations and recovery</strong><small>Retries, duplicate control, message monitoring, recovery ownership, and business reconciliation.</small><i class="material-symbols-outlined" aria-hidden="true">monitor_heart</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="warehouse-business-contract" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">3PL and WMS contract</p>
      <h2>Define the business state that crosses the boundary.</h2>
      <p>The useful contract is not “send a delivery”. It is a conversation: request execution, report progress when needed, confirm the physical result, and support correction when the result must be reversed.</p>
    </header>

    <div class="ecg-decision-columns">
      <div>
        <h3>Outbound</h3>
        <p><strong>Intent:</strong> S/4HANA creates the delivery and asks the warehouse to execute it.</p>
        <p><strong>Return state:</strong> the warehouse can report updates, split information, and the final shipping result. S/4HANA then continues with the enterprise document and posting flow.</p>
      </div>
      <div>
        <h3>Inbound</h3>
        <p><strong>Intent:</strong> a purchase or supply process creates inbound warehouse demand.</p>
        <p><strong>Return state:</strong> the warehouse confirms the physical receipt. The enterprise system converts that confirmation into the appropriate stock and accounting state.</p>
      </div>
      <div>
        <h3>Stock transfer</h3>
        <p><strong>Intent:</strong> stock must move between enterprise locations or warehouse-controlled locations.</p>
        <p><strong>Return state:</strong> shipment and receipt confirmations must preserve quantities, identities, and document correlation across both ends of the movement.</p>
      </div>
      <div>
        <h3>Reversal and correction</h3>
        <p><strong>Intent:</strong> undo or correct a result that already changed business state.</p>
        <p><strong>Return state:</strong> use an explicit reversal or compensation path. Do not overwrite history and hope that stock, delivery, and accounting become consistent again.</p>
      </div>
    </div>

    <p>SAP's Public Edition 1ZQ material illustrates the same separation clearly: the outbound delivery is sent by Web Services to a third-party WMS, the WMS performs its internal warehouse work as a black box, and confirmations return to SAP for the follow-on business process. The procurement flow follows the same idea for inbound deliveries and goods receipt.</p>
    <p class="ecg-caption"><strong>Lead rule:</strong> a technical acknowledgement proves transport. It does not prove that picking, goods issue, goods receipt, stock, billing readiness, or financial posting reached the intended business state.</p>
  </section>

  <section class="research-canvas__inventory" id="logistics-protocol-choice" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Protocol choice</p>
      <h2>REST versus SOAP is usually not the first decision.</h2>
      <p>A partner may expose REST while an SAP standard business contract is SOAP-based. That creates an adaptation problem, but the adapter must preserve the business semantics rather than only convert JSON to XML.</p>
    </header>

    <div class="ecg-decision-columns">
      <div><h3>Contract</h3><p>Which command, confirmation, update, cancellation, or event is being exchanged? What does success mean to the business?</p></div>
      <div><h3>Identity</h3><p>Which delivery, item, handling unit, batch, serial number, stock-transfer document, or external reference correlates both systems?</p></div>
      <div><h3>Reliability</h3><p>What happens after timeout, duplicate delivery, retry, out-of-order message, partial execution, or receiver downtime?</p></div>
      <div><h3>Mediation</h3><p>Use an integration layer when mapping, protocol conversion, routing, security policy, decoupling, or central monitoring justify it. Do not put transformation logic into the S/4HANA core by default simply because PCE allows custom ABAP.</p></div>
    </div>

    <p>When middleware converts REST to SOAP or SOAP to REST, define correlation IDs, idempotency behavior, retry ownership, error categories, and replay rules before building mappings. Otherwise the interface may be technically connected and still be impossible to operate safely.</p>
  </section>

  <section class="research-canvas__inventory" id="logistics-deployment-boundary" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Deployment and release boundary</p>
      <h2>Do not memorize one setup path for every S/4HANA landscape.</h2>
      <p>The original business pattern can stay similar while the configuration model changes by product, deployment, and release. This is where many 3PL discussions become misleading.</p>
    </header>

    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Logistics integration deployment boundary">
      <table class="study-table__table">
        <thead>
          <tr><th>Context</th><th>What the current SAP material shows</th><th>Architecture consequence</th></tr>
        </thead>
        <tbody>
          <tr>
            <th>S/4HANA Cloud Public Edition + third-party WMS</th>
            <td>Scope item 1ZQ documents asynchronous Web Services exchanges for outbound and inbound warehouse processes. The third-party WMS can remain a black box behind the contract.</td>
            <td>Start from the released scope and communication model for the target Public Edition release. Do not project PCE transactions into Public Cloud.</td>
          </tr>
          <tr>
            <th>S/4HANA Cloud Public Edition 2608 + SAP Logistics Management</th>
            <td>SAP introduced scope item 83S for integration with SAP Logistics Management on SAP BTP.</td>
            <td>83S is a product-specific SAP Logistics Management path. It is not proof that an arbitrary non-SAP 3PL supports the same setup.</td>
          </tr>
          <tr>
            <th>S/4HANA Cloud Private Edition + SAP Logistics Management</th>
            <td>The current integration guide uses SAP Integration Suite and SOA Manager for SOAP integration. SAP also lists SPRO for third-party warehouse configuration and AIF/SRT tools for monitoring.</td>
            <td>PCE gives more technical freedom, but the supported product integration still has a defined service and routing model. Follow that model before inventing a custom adapter.</td>
          </tr>
          <tr>
            <th>S/4HANA Cloud Private Edition + arbitrary non-SAP 3PL</th>
            <td>The exact partner contract is outside the SAP Logistics Management product guide and must be verified against released S/4HANA services and the 3PL API.</td>
            <td>Do not copy 1ZQ, 83S, or a Logistics Management setup by analogy. Design the adaptation and operating model from the two real contracts.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p class="ecg-caption"><strong>Important:</strong> a scope item, a communication scenario, an IMG activity, a SOAP consumer configuration, and an Integration Suite flow are different configuration layers. They can belong to one solution, but they are not interchangeable.</p>
  </section>

  <section class="research-canvas__inventory" id="logistics-configuration-layers" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Configuration model</p>
      <h2>Separate process relevance, service routing, mediation, and operations.</h2>
      <p>This is a safer way to read a long configuration guide. Every step should answer one of these questions.</p>
    </header>

    <div class="ecg-decision-columns">
      <div><h3>1 · Business and SPRO configuration</h3><p>Which warehouse, storage location, delivery, or stock movement is externally executed? Which document or state change should start distribution?</p></div>
      <div><h3>2 · Service configuration</h3><p>Which provider or consumer service is active? Which receiver, endpoint, authentication method, and business context select the destination?</p></div>
      <div><h3>3 · Middleware</h3><p>Where are mapping, routing, protocol conversion, security policy, throttling, and technical retry handled?</p></div>
      <div><h3>4 · Partner execution</h3><p>What does the 3PL do after receiving the request, and which intermediate or final states can it return?</p></div>
      <div><h3>5 · Operations</h3><p>Where do we monitor transport, application processing, retries, and business reconciliation? Who owns each recovery action?</p></div>
    </div>

    <p>A warehouse number can appear in business configuration, receiver determination, middleware routing, and monitoring. That does not make those settings one configuration object. Keep the layers separate when troubleshooting.</p>
  </section>

  <section class="research-canvas__inventory" id="logistics-failure-model" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Failure model</p>
      <h2>Find the first wrong business state.</h2>
      <p>Start with the document flow and message correlation. Then move down to transport or configuration only where the evidence points.</p>
    </header>

    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="3PL logistics integration failure model">
      <table class="study-table__table">
        <thead><tr><th>Symptom</th><th>Likely boundary</th><th>First proof</th></tr></thead>
        <tbody>
          <tr><td>Delivery exists but no outbound warehouse message is created</td><td>Process relevance, trigger, or receiver determination</td><td>Prove warehouse relevance, distribution condition, receiver, and message creation before checking the network.</td></tr>
          <tr><td>Message was created but the 3PL did not receive it</td><td>Endpoint, authentication, transport, middleware, or routing</td><td>Trace the same correlation ID through the SAP runtime and middleware.</td></tr>
          <tr><td>3PL received the request but rejects it</td><td>Contract, mapping, reference data, or master-data synchronization</td><td>Compare the rejected business fields and identifiers with the receiving contract.</td></tr>
          <tr><td>Warehouse execution finished but S/4HANA is not updated</td><td>Inbound confirmation, correlation, validation, or posting</td><td>Prove that the confirmation arrived, was accepted, and changed the intended SAP business object.</td></tr>
          <tr><td>The same confirmation is processed twice</td><td>Idempotency and replay design</td><td>Check the business key, duplicate-detection rule, retry history, and whether the receiver can safely reprocess.</td></tr>
          <tr><td>All messages are green but stock or delivery status is wrong</td><td>Business reconciliation</td><td>Compare warehouse truth, S/4HANA stock, delivery status, goods movement, and document flow. Transport success is not enough.</td></tr>
          <tr><td>A reversal is stuck after the original movement succeeded</td><td>Compensation flow</td><td>Trace the reversal as its own business conversation; do not assume the original success path can simply run backwards.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="logistics-lead-answer" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Assessment answer</p>
      <h2>Explain a 3PL integration from ownership to recovery.</h2>
      <p>A Lead-level answer should make the architecture visible before naming transactions.</p>
    </header>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">record_voice_over</span>
      <p><strong>60–90 second frame:</strong> “I first separate enterprise ownership from warehouse execution. I define which system owns the delivery, physical warehouse work, stock posting, transport state, and final confirmation. Then I define the business messages and their success criteria. Only after that do I choose SOAP, REST, IDoc, or events. For Public Edition I check the released scope and communication model for that release. For PCE I verify the released services and SOA or middleware setup for the chosen warehouse product. If a non-SAP 3PL exposes a different contract, I normally adapt at the integration layer instead of putting protocol conversion into the core. Finally I design idempotency, retries, monitoring, reversals, and business reconciliation, because a green message is not proof that the logistics process is complete.”</p>
    </div>

    <div class="ecg-decision-columns">
      <div><h3>Trap: “REST is more modern, so use REST.”</h3><p>The protocol does not decide whether the contract fits the process. Start with business semantics, coupling, reliability, and recovery.</p></div>
      <div><h3>Trap: “PCE allows ABAP, so build an adapter.”</h3><p>Technical freedom is not a reason to add lifecycle debt to the core. Check standard services and mediation first.</p></div>
      <div><h3>Trap: “AIF will monitor everything.”</h3><p>Use the monitor that owns the runtime, then connect technical evidence to business reconciliation. Different interfaces can use different monitoring tools.</p></div>
      <div><h3>Trap: “External WMS and decentralized EWM are the same pattern.”</h3><p>They may exchange similar logistics states, but product ownership, master data, supported contracts, and operational tooling are different.</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="logistics-integration-sources" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Current SAP evidence</p>
      <h2>Use the target product and release as the configuration source of truth.</h2>
      <p>The architecture model above is independently written. These SAP pages support the release-sensitive product facts used in the logistics section.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/s4hana-cloud-best-practices/logistics-with-third-party-warehouse-management-1zq-br/sales-process" target="_blank" rel="noopener"><span>SAP</span><strong>1ZQ · Sales Process</strong><small>Public Edition third-party WMS flow: outbound delivery, split, and confirmation Web Services messages.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/s4hana-cloud-best-practices/logistics-with-third-party-warehouse-management-1zq-ch/procurement-process" target="_blank" rel="noopener"><span>SAP</span><strong>1ZQ · Procurement Process</strong><small>Public Edition inbound flow and goods-receipt confirmation from a third-party warehouse.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_LOGISTICS_MANAGEMENT/ff6700aed66c43c48fe5351d55db2381/f19bb3e09dbd4f8c99406e1f01cf37f5.html" target="_blank" rel="noopener"><span>SAP</span><strong>PCE configuration transactions for SAP Logistics Management</strong><small>SPRO, SOAMANAGER, SE80, AIF, OData, and SOAP monitoring responsibilities.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_LOGISTICS_MANAGEMENT/ff6700aed66c43c48fe5351d55db2381/22afde33045a4c0786df97d628d9a98a.html" target="_blank" rel="noopener"><span>SAP</span><strong>Connect S/4HANA Cloud Private Edition to SAP Integration Suite</strong><small>Current SAP Logistics Management integration guide entry point for PCE SOAP setup through SOA Manager.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_LOGISTICS_MANAGEMENT/ff6700aed66c43c48fe5351d55db2381/6488c68e6af341aab1cbd478e4bd9a36.html?locale=en-US" target="_blank" rel="noopener"><span>SAP</span><strong>Connect SAP Integration Suite to SAP Logistics Management</strong><small>Product-specific integration package and iFlow configuration for PCE integration.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/01adb27f56d44d3db2f1f2e40cedc016.html?locale=en-US" target="_blank" rel="noopener"><span>SAP</span><strong>Public Edition 2608 · SAP Logistics Management integration (83S)</strong><small>Release boundary for the new SAP Logistics Management scope item.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="isa-m" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Integration strategy / ISA-M</p>
      <h2>{{ topic.integration_strategy.title }}</h2>
      <p>{{ topic.integration_strategy.summary }}</p>
    </header>
    <div class="research-route-list">
      {% for phase in topic.integration_strategy.phases %}
      <a href="#integration-lifecycle"><span>{{ phase.order }}</span><strong>{{ phase.title }}</strong><small>{{ phase.outcome }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
      {% endfor %}
    </div>
    <div class="ecg-decision-columns">
      {% for item in topic.integration_strategy.decision_levels %}
      <div><h3>{{ item.level }}</h3><p><strong>Owner:</strong> {{ item.owner }}</p><p>{{ item.question }}</p></div>
      {% endfor %}
    </div>
    <p class="ecg-caption"><strong>Lead rule:</strong> {{ topic.integration_strategy.lead_rule }}</p>
  </section>

  <section class="research-canvas__inventory" id="requirements-to-strategy" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Implementation flow</p>
      <h2>Do not freeze the interface list in Discover.</h2>
      <p>The first list of integrations is only a baseline. Fit-to-Standard is where process experts can expose missing dependencies and clarify what each interface must actually achieve.</p>
    </header>
    <div class="ecg-decision-columns">
      {% for item in topic.integration_strategy.project_flow %}
      <div><h3>{{ item.stage }}</h3><p>{{ item.action }}</p></div>
      {% endfor %}
    </div>
    <div class="ecg-decision-columns">
      <div><h3>ISA-M</h3><p>{{ topic.integration_strategy.boundary.methodology }}</p></div>
      <div><h3>Integration Assessment</h3><p>{{ topic.integration_strategy.boundary.capability }}</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="integration-lifecycle" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Delivery lifecycle</p>
      <h2>{{ topic.integration_delivery_lifecycle.title }}</h2>
      <p>{{ topic.integration_delivery_lifecycle.summary }}</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.integration_delivery_lifecycle.stages %}
      <a href="#platform-map"><span>{{ item.order }}</span><strong>{{ item.title }}</strong><small><b>{{ item.tools }}</b> · {{ item.purpose }}</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      {% endfor %}
    </div>
    <p class="ecg-caption"><strong>Operational boundary:</strong> a successful middleware message is not the same as a completed business process. Monitoring must lead to business reconciliation where the process risk requires it.</p>
  </section>

  <section class="research-canvas__inventory" id="architecture-stack" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Architecture language</p>
      <h2>Eight layers. Do not mix them.</h2>
      <p>This is the mental model I use before choosing a product. If the first answer is “Kafka”, “CPI”, or “TIBCO”, the discussion started too low in the stack.</p>
    </header>
    <div class="research-route-list">
      {% for item in language.architecture_stack %}
      <a href="#terminology"><span>{{ item.order }}</span><strong>{{ item.layer }}</strong><small>{{ item.question }} <b>Examples:</b> {{ item.examples | join: ", " }}. <b>Lead rule:</b> {{ item.lead_rule }}</small><i class="material-symbols-outlined" aria-hidden="true">layers</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="selection-questions" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Design sequence</p>
      <h2>Twelve questions before middleware.</h2>
      <p>These questions expose coupling, ownership, reliability, and semantics before anyone starts comparing adapters.</p>
    </header>
    <div class="research-route-list">
      {% for question in language.selection_questions %}
      <a href="#integration-rules"><span>?</span><strong>{{ question }}</strong><small>Answer this with a business object and a failure scenario, not only a technology name.</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="terminology" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Terminology</p>
      <h2>One language for integration architecture.</h2>
      <p>A message is not automatically an event. A broker is not an integration runtime. A topic does not mean exactly the same thing in JMS and Kafka. Naming things correctly removes a surprising amount of architecture fog.</p>
    </header>
    <div class="research-route-list">
      {% for item in language.terms %}
      <a href="#not-the-same"><span>TERM</span><strong>{{ item.term }}</strong><small><b>{{ item.category }}</b> · {{ item.definition }} <b>Architect view:</b> {{ item.architect_view }} <b>Example:</b> {{ item.example }}</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="not-the-same" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Do not confuse</p>
      <h2>Similar words, different architecture decisions.</h2>
      <p>Most terminology errors are harmless until someone uses them to select a platform. Then they become invoices.</p>
    </header>
    <div class="research-route-list">
      {% for pair in language.not_the_same %}
      <a href="#walkthroughs"><span>≠</span><strong>{{ pair.left }} ≠ {{ pair.right }}</strong><small>{{ pair.distinction }}</small><i class="material-symbols-outlined" aria-hidden="true">difference</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="walkthroughs" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Read the stack end to end</p>
      <h2>Four examples using the same language.</h2>
      <p>The point is not memorizing diagrams. The point is being able to explain every layer of a design consistently.</p>
    </header>
    <div class="research-route-list">
      {% for item in language.walkthroughs %}
      <a href="#interface-patterns"><span>FLOW</span><strong>{{ item.title }}</strong><small>{{ item.business_need }} <b>Path:</b> {{ item.flow }} <b>Meaning:</b> {{ item.language.business_meaning }} · <b>Interaction:</b> {{ item.language.interaction }} · <b>Contract:</b> {{ item.language.contract }} · <b>Transport:</b> {{ item.language.transport }} · <b>Reliability:</b> {{ item.language.reliability }} <b>Architect take:</b> {{ item.architect_take }}</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="integration-rules" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Memory hooks</p>
      <h2>Ten rules before middleware.</h2>
      <p>I use these rules to keep the discussion on coupling, reliability, and business ownership instead of adapter names.</p>
    </header>
    <div class="research-route-list">
      {% for principle in topic.architecture_principles %}
      <a href="#interface-patterns"><span>{{ forloop.index }}</span><strong>{{ principle }}</strong><small>Use this as a design check, then validate the concrete interface contract.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="interface-patterns" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Interface patterns</p>
      <h2>Choose the message meaning first.</h2>
      <p>REST, IDoc, Kafka, JMS, and SFTP are not different spellings of the same thing. Each creates a different dependency between sender and receiver.</p>
    </header>
    <div class="research-route-list">
      {% for interface in topic.interface_types %}
      <a href="#decision-guide"><span>INT</span><strong>{{ interface.title }}</strong><small><b>{{ interface.message_meaning }}</b> · {{ interface.best_for }} <b>Lead rule:</b> {{ interface.lead_rule }}</small><i class="material-symbols-outlined" aria-hidden="true">compare_arrows</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="platform-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Platform map</p>
      <h2>Do not put every middleware product in one bucket.</h2>
      <p>Integration runtimes, brokers, and event-streaming platforms solve different parts of the problem. A mature landscape often uses more than one on purpose.</p>
    </header>
    <div class="research-route-list">
      {% for platform in topic.platforms %}
      <a href="/labs/enterprise-context/data/topics.json"><span>PLT</span><strong>{{ platform.title }}</strong><small><b>{{ platform.platform_type }}</b> · {{ platform.remember }} Best fit: {{ platform.best_fit[0] }} Trade-off: {{ platform.trade_offs[0] }}</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      {% endfor %}
    </div>
  </section>


  <section class="research-canvas__inventory" id="suite-capabilities" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">SAP Integration Suite</p>
      <h2>Capabilities solve different parts of the integration problem.</h2>
      <p>We do not select “Integration Suite” as one large box. We select the capabilities that match the interaction, contract, and operating model.</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.sap_integration_suite_capabilities %}
      <a href="#decision-guide"><span>CAP</span><strong>{{ item.title }}</strong><small><b>{{ item.role }}</b> · {{ item.remember }}</small><i class="material-symbols-outlined" aria-hidden="true">extension</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="decision-guide" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Decision guide</p>
      <h2>Start from the dependency you need.</h2>
      <p>The first question is not “Kafka or Event Mesh?” It is “What must the sender know about the receiver, and when?”</p>
    </header>
    <div class="research-route-list">
      {% for decision in topic.decision_guide %}
      <a href="#reliability"><span>→</span><strong>{{ decision.need }}</strong><small><b>{{ decision.primary_pattern }}</b> · {{ decision.preferred_stack }}. {{ decision.why }} <b>Avoid:</b> {{ decision.avoid }}</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="logistics-patterns" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Logistics</p>
      <h2>Apply the same rules to real process boundaries.</h2>
      <p>Sales, purchasing, warehouse, and transportation need different latency and reliability choices, but the design logic stays consistent.</p>
    </header>
    <div class="research-route-list">
      {% for pattern in topic.logistics_patterns %}
      <a href="/labs/enterprise-context/data/topics.json"><span>LOG</span><strong>{{ pattern.title }}</strong><small>{{ pattern.path }} <b>First Lead check:</b> {{ pattern.lead_focus[0] }}</small><i class="material-symbols-outlined" aria-hidden="true">local_shipping</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="master-data" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Data distribution</p>
      <h2>{{ topic.data_distribution.title }}</h2>
      <p>{{ topic.data_distribution.principle }} Governance, replication, synchronization, and protocol mediation are separate jobs.</p>
    </header>
    <div class="research-route-list">
      {% for responsibility in topic.data_distribution.responsibilities %}
      <a href="/labs/enterprise-context/data/topics.json"><span>MD</span><strong>{{ responsibility.title }}</strong><small><b>{{ responsibility.owner_options | join: " / " }}</b> · {{ responsibility.job }} {{ responsibility.rule }}</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Master-data patterns</p>
      <h2>Distribute deliberately, then reconcile.</h2>
      <p>A successful outbound message is not proof that the receiving business object is correct. That small distinction saves large support incidents.</p>
    </header>
    <div class="research-route-list">
      {% for pattern in topic.data_distribution.reference_patterns %}
      <a href="#reliability"><span>PATH</span><strong>{{ pattern.name }}</strong><small>{{ pattern.path }} · Best fit: {{ pattern.best_fit }} <b>Risk:</b> {{ pattern.risk }}</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="reliability" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Reliability</p>
      <h2>Architecture starts where the happy path ends.</h2>
      <p>Retries, duplicates, ordering, replay, reconciliation, and correlation are not production details. They define whether logistics keeps moving when systems disagree.</p>
    </header>
    <div class="research-route-list">
      {% for control in topic.reliability_controls %}
      <a href="/labs/enterprise-context/data/topics.json"><span>CTRL</span><strong>{{ control.title }}</strong><small>{{ control.question }} <b>Design:</b> {{ control.design_hint }}</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="anti-patterns" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Failure modes</p>
      <h2>What I would challenge in a design review.</h2>
      <p>Most integration debt does not start with a bad protocol. It starts with unclear ownership and then gets automated very efficiently.</p>
    </header>
    <div class="research-route-list">
      {% for anti in topic.anti_patterns %}
      <a href="#assessment-cards"><span>!</span><strong>{{ anti.title }}</strong><small>{{ anti.symptom }} {{ anti.why_it_hurts }} <b>Better:</b> {{ anti.better_move }}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="assessment-cards" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead assessment</p>
      <h2>Short answers that show architecture thinking.</h2>
      <p>The goal is not to recite protocols. Explain the boundary, trade-off, failure mode, and why the choice fits the process.</p>
    </header>
    <div class="research-route-list">
      {% for card in topic.assessment_cards %}
      <a href="#sources"><span>Q</span><strong>{{ card.question }}</strong><small>{{ card.answer }}</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="memory-model" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Architect memory model</p>
      <h2>Eight sentences to keep the landscape in your head.</h2>
      <p>If these eight questions stay clear, individual products become much easier to place.</p>
    </header>
    <div class="research-route-list">
      {% for item in language.memory_model %}
      <a href="#sources"><span>{{ forloop.index }}</span><strong>{{ item }}</strong><small>Use this sentence to explain one layer before moving to the next.</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="business-partner-api" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Master-data API deep dive</p>
      <h2>Business Partner API: the object graph behind customer and supplier integration.</h2>
      <p>Before building a BP interface, understand the hierarchy: central Business Partner, customer and supplier views, then company code, sales area, and purchasing organization. The deep dive also covers CVI, deep create versus updates, recovery, and assessment questions.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/integrations/business-partner-api/"><span>BP</span><strong>SAP Business Partner API — Data Model, Segments, CVI and Integration Design</strong><small>Learn how <code>API_BUSINESS_PARTNER</code> maps to real FI, SD, and MM master-data segments and how to design writes, retries, and reconciliation without treating BP as one flat payload.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="sources" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Primary sources</p>
      <h2>Facts checked, explanations written independently.</h2>
      <p>Product capabilities and protocol support are linked to current primary documentation. The decision rules, terminology model, and trade-offs are independent architecture synthesis for learning.</p>
    </header>
    <div class="research-route-list">
      {% for source in registry.sources %}
      <a href="{{ source.url }}" target="_blank" rel="noopener"><span>SRC</span><strong>{{ source.publisher }} · {{ source.title }}</strong><small>{{ source.product_scope }} · checked {{ source.verified_at }}</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
