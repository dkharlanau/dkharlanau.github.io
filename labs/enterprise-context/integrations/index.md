---
layout: default
title: "SAP Integration Architecture — Logistics, Events and Data Distribution"
description: "A practical SAP integration architecture guide to APIs, IDocs, events, messaging, Integration Suite, Event Mesh, Kafka, B2B, and master-data distribution."
permalink: /labs/enterprise-context/integrations/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-24
hide_global_cta: true
tags:
  - sap
  - integration
  - logistics
  - event-driven-architecture
  - master-data
last_reviewed: 2026-09-24
publication_wave: "logistics-search-wave-01"
review_method: "SAP primary sources + current Integration Suite and event-mesh review + full editorial rewrite"
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
  - title: "Quality of Service Exactly Once"
    url: "https://help.sap.com/docs/integration-suite/sap-integration-suite/quality-of-service-exactly-once"
  - title: "Kafka Adapter"
    url: "https://help.sap.com/docs/cloud-integration/sap-cloud-integration/kafka-adapter"
  - title: "Migration from Event Mesh in SAP Integration Suite to SAP Integration Suite, Advanced Event Mesh"
    url: "https://help.sap.com/docs/integration-suite/isuite-event-mesh/migration-from-event-mesh-in-sap-integration-suite-to-sap-integration-suite-advanced-event-mesh"
  - title: "Working with Trading Partner Agreements"
    url: "https://help.sap.com/docs/integration-suite/sap-integration-suite/creating-trading-partner-agreement"
  - title: "Synchronization of Master Data"
    url: "https://help.sap.com/docs/master-data-integration/sap-master-data-integration-prod/synchronization-of-master-data"
  - title: "Data Replication Framework"
    url: "https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/88e3f5577c84bc12e10000000a4450e5.html"
# ai-discovery-managed:end
---
{% assign topic = site.data.labs.enterprise_context.topics.integration_architecture_landscape %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li aria-current="page">Integrations</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise Context Lab / Integration Architecture</p>
      <h1>{{ topic.title }}</h1>
      <p>SAP integration architecture starts with a business dependency, not with middleware. One system needs a fact, command, document, or change from another. The design becomes much easier to reason about when we separate business meaning, interface contract, delivery mechanism, and proof that the receiving process really completed.</p>
      <a class="research-canvas__button" href="#architecture-stack">Follow the boundary <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Integration architecture path">
      <p>Architecture path</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Meaning</strong><small>What business interaction crosses the boundary?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Contract</strong><small>What must sender and receiver agree on?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Delivery</strong><small>How should the interaction travel?</small></div>
      <div class="research-canvas__signal-line"><span>04</span><strong>Proof</strong><small>What counts as business completion?</small></div>
      <em>Product choice comes after the dependency is clear.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">hub</span>
    <div>
      <p><strong>Protocol, message meaning, and platform are different decisions.</strong> An HTTP call can carry a query or a command. An IDoc is a structured SAP message format used by business interfaces. Kafka is a distributed event-streaming platform. Event Mesh is a broker. Cloud Integration can mediate between endpoints. None of these names tells us by itself what the business interaction means.</p>
      <p>Start with the dependency: who owns the business object, what the receiver is expected to do, whether the caller needs an immediate answer, and what happens when either side is unavailable.</p>
    </div>
    <a href="/labs/enterprise-context/integration-operations/">Continue into runtime recovery <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="architecture-stack" data-reveal>
    <span id="lead-answer-frame" aria-hidden="true"></span>
    <span id="selection-questions" aria-hidden="true"></span>
    <header>
      <p class="research-canvas__eyebrow">The integration boundary</p>
      <h2>Four decisions before we compare technologies.</h2>
      <p>A strong design can explain these four decisions without naming a product. Only then is a platform comparison meaningful.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>1 · Business meaning</h3><p>Is this a query, a command, a business document, a notification that something happened, or synchronization of a data set? Name the object and its owner.</p></div>
      <div><h3>2 · Contract</h3><p>Define identity, required fields, semantics, versioning, authorization expectations, and the business meaning of success. A payload schema is only part of the contract.</p></div>
      <div><h3>3 · Delivery</h3><p>Choose synchronous request/response, asynchronous messaging, brokered events, streaming, file exchange, or B2B communication from the dependency and operating model.</p></div>
      <div><h3>4 · Completion</h3><p>Define how we know the receiver accepted the message and reached the expected business state. Transport success and business completion are not the same signal.</p></div>
    </div>
    <p>Consider a Business Partner change. A source application may decide that the object is ready for distribution; DRF or Master Data Integration may control part of that distribution; an interface or middleware layer transports it; and the receiving application still has to validate and commit its own representation. Calling the whole chain “CPI replication” hides the boundaries we need for design and support.</p>
  </section>

  <section class="research-canvas__inventory" id="interface-patterns" data-reveal>
    <span id="terminology" aria-hidden="true"></span>
    <span id="not-the-same" aria-hidden="true"></span>
    <span id="walkthroughs" aria-hidden="true"></span>
    <span id="integration-rules" aria-hidden="true"></span>
    <header>
      <p class="research-canvas__eyebrow">Interaction patterns</p>
      <h2>Choose the dependency first; the protocol comes later.</h2>
      <p>The same SAP business object can participate in several integration styles at different moments. The useful distinction is how sender and receiver depend on each other.</p>
    </header>

    <h3>Synchronous request</h3>
    <p>Use a synchronous interaction when the caller needs an answer before it can continue. The benefit is immediate feedback; the cost is runtime coupling. The caller now depends on the receiver, network path, response time, and error contract at that moment. REST or OData may implement this pattern, but the pattern is the request/response dependency, not HTTP itself.</p>

    <h3>Asynchronous business message</h3>
    <p>An asynchronous message hands work to another process without keeping the sender's business transaction open. SAP IDocs are a familiar example of this style for supported interfaces. The important design questions are message identity, retry behavior, duplicate handling, ordering where required, and how receiver errors are surfaced.</p>

    <h3>Business event</h3>
    <p>An event states that something happened. It is useful when the producer should not know every consumer and when several consumers may react independently. A broker can route the event to subscriptions, but the event still needs a stable business meaning and enough context or identifiers for consumers to act safely.</p>

    <h3>Event stream</h3>
    <p>Streaming platforms are useful when consumers need a durable sequence of records, independent consumption positions, or high-volume event processing. SAP Cloud Integration's Kafka adapter connects Cloud Integration to an <em>external</em> Kafka broker; the adapter does not turn Cloud Integration itself into Kafka. That distinction matters when we assign ownership for topics, partitions, retention, replay, and broker operations.</p>

    <h3>B2B and file exchange</h3>
    <p>A partner interface is not merely “send a file.” The agreement may define partner identity, transaction type, document standard, transmission protocol, security, and processing expectations. SAP Trading Partner Management models those B2B relationships explicitly. Files can still be the right transport when the process is naturally batch-oriented or constrained by a partner, but they need the same contract discipline as APIs and messages.</p>
  </section>

  <section class="research-canvas__inventory" id="platform-map" data-reveal>
    <span id="decision-guide" aria-hidden="true"></span>
    <header>
      <p class="research-canvas__eyebrow">SAP Integration Suite</p>
      <h2>One suite, several different responsibilities.</h2>
      <p>SAP Integration Suite groups multiple capabilities, but they should not be treated as interchangeable runtimes.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/decide-on-integration-technology" target="_blank" rel="noopener"><span>FLOW</span><strong>Cloud Integration</strong><small>Mediates and orchestrates application-to-application and process integrations through integration flows, adapters, transformations, routing, and related runtime services.</small><i class="material-symbols-outlined" aria-hidden="true">conversion_path</i></a>
      <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/decide-on-integration-technology" target="_blank" rel="noopener"><span>API</span><strong>API Management and API Composition</strong><small>Expose, protect, govern, and compose APIs. This solves a different problem from asynchronous message brokerage.</small><i class="material-symbols-outlined" aria-hidden="true">api</i></a>
      <a href="https://help.sap.com/docs/integration-suite/isuite-event-mesh/migration-from-event-mesh-in-sap-integration-suite-to-sap-integration-suite-advanced-event-mesh" target="_blank" rel="noopener"><span>EVT</span><strong>Event Mesh and Advanced Event Mesh</strong><small>Provide brokered event and messaging capabilities. SAP documents distinct Event Mesh offerings and migration paths; check the capability, service plan, protocol, scale, and product-specific support instead of treating the names as synonyms.</small><i class="material-symbols-outlined" aria-hidden="true">device_hub</i></a>
      <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/creating-trading-partner-agreement" target="_blank" rel="noopener"><span>B2B</span><strong>Trading Partner Management</strong><small>Models partner agreements and B2B transaction requirements such as formats, protocols, identities, and security.</small><i class="material-symbols-outlined" aria-hidden="true">handshake</i></a>
    </div>
    <p>As of July 23, 2026, SAP Help includes a dedicated migration guide from the Event Mesh capability in SAP Integration Suite to SAP Integration Suite, Advanced Event Mesh. That is a useful architecture signal, but it is not a license to replace one broker with another blindly: client libraries, protocols, topic rules, and product prerequisites can differ.</p>
  </section>

  <section class="research-canvas__inventory" id="logistics-patterns" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">One process, several patterns</p>
      <h2>A sales order can cross system boundaries in more than one way.</h2>
      <p>Integration style follows the business moment. There is no single “sales-order integration pattern.”</p>
    </header>
    <p>An external storefront creating an order may need an immediate acceptance or rejection from the order-owning system, which favors a synchronous contract when the supported API and latency model fit. A downstream fulfillment or legacy system may instead receive a business document asynchronously. After a meaningful state change, independent consumers such as analytics, notification, or planning services may react to an event without the sales application calling each one directly.</p>
    <p>These patterns can coexist. What should stay stable is ownership: the system of record owns the business state, the contract defines what crosses the boundary, and the integration layer should not quietly become the owner of business rules simply because it can transform a message.</p>
  </section>

  <section class="research-canvas__inventory" id="master-data" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Master-data distribution</p>
      <h2>Replication frameworks and middleware solve different jobs.</h2>
      <p>Master data makes this distinction especially visible because selection, governance, transport, and target acceptance often sit in different components.</p>
    </header>
    <p><a href="/labs/enterprise-context/integrations/drf/">Data Replication Framework (DRF)</a> is a source-side framework for supported replication scenarios: replication models, outbound implementations, target assignments, filters, and execution belong to that control plane. SAP Master Data Integration is different again: SAP describes it as a central master-data hub that synchronizes application-local master data through initial and delta loads controlled by distribution models.</p>
    <p>Cloud Integration can still mediate an interface in either landscape, but mediation does not decide which master record is authoritative. With Master Data Integration, SAP explicitly describes delta synchronization as eventually delivering the same information to applications with identical filter settings. That is a synchronization model, not one distributed database transaction across every consumer.</p>
    <a class="research-canvas__button" href="/labs/enterprise-context/data-governance/">Review data ownership and governance <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="reliability" data-reveal>
    <span id="anti-patterns" aria-hidden="true"></span>
    <span id="assessment-cards" aria-hidden="true"></span>
    <span id="memory-model" aria-hidden="true"></span>
    <header>
      <p class="research-canvas__eyebrow">Reliability</p>
      <h2>“Exactly once” is an end-to-end property, not a middleware checkbox.</h2>
      <p>Reliable delivery is where architecture claims need the most precision.</p>
    </header>
    <p>SAP's current Integration Suite guidance describes Exactly Once as the combination of guaranteed delivery and duplicate-safe processing. Guaranteed delivery can cause redelivery, so the scenario also needs an idempotent receiver or an equivalent duplicate-handling design. The exact mechanism depends on the sender, middleware, receiver, and protocol.</p>
    <p>A classic failure is a timeout after the receiver has already committed the business object. The sender or middleware retries because it did not receive the acknowledgement. If the retry cannot be recognized as the same business operation, the technical recovery creates a business duplicate. Stable message identity, idempotency, correlation, and reconciliation therefore belong in the contract, not in a support appendix.</p>
    <p>Ordering deserves the same discipline. Preserve sequence only where the business invariant requires it, and define the scope of that order. Global ordering is expensive and often unnecessary; no ordering at all can be wrong when later changes depend on earlier state.</p>
    <p>Finally, a green integration monitor proves only the layer it observes. The receiver may still reject, park, or misapply the data. The operational chain and safe-reprocessing model are covered in <a href="/labs/enterprise-context/integration-operations/">Integration Operations & Recovery</a>.</p>
  </section>

  <section class="research-canvas__inventory" id="business-partner-api" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Concrete object boundary</p>
      <h2>Business Partner is a useful test of interface design.</h2>
      <p>A Business Partner is not one flat record. Central BP data, customer and supplier roles, and organizational segments such as company code, sales area, and purchasing organization have different business meaning and lifecycle requirements.</p>
    </header>
    <p>An integration contract should therefore say which part of that object graph it owns, whether it creates or extends an existing partner, how keys are reconciled, and what a successful target state looks like. The dedicated <a href="/labs/enterprise-context/integrations/business-partner-api/">Business Partner API deep dive</a> follows that object model in detail.</p>
  </section>

  <section class="research-canvas__inventory" id="sources" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Primary sources</p>
      <h2>Product facts checked against current SAP documentation.</h2>
      <p>The architecture reasoning above is independent synthesis. Product capabilities, migration status, reliability behavior, and master-data synchronization claims are linked to first-party SAP documentation.</p>
    </header>
    <div class="research-route-list">
      {% for source in page.source_links %}
      <a href="{{ source.url }}" target="_blank" rel="noopener"><span>SRC</span><strong>{{ source.title }}</strong><small>SAP Help Portal · reviewed 2026-09-24</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
