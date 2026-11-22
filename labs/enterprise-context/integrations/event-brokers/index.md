---
layout: default
title: "Kafka vs RabbitMQ — Architecture Decision Guide for SAP and Logistics"
description: "Choose event streaming, work queues, API, or SAP event services by requirements. Compare replay, consumer groups, acknowledgements, cost, monitoring, and recovery."
permalink: /labs/enterprise-context/integrations/event-brokers/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-22
last_reviewed: 2026-11-22
review_method: "Official Apache Kafka 4.4, RabbitMQ 4.x and SAP Integration Suite product documentation; architectural judgement requires project validation"
content_model: technical_guide
hide_global_cta: true
career_impact: mapped
career_skills:
  - integration-patterns
  - integration-recovery
  - integration-ownership
tags: [kafka, rabbitmq, amqp, sap-event-mesh, integration-architecture, logistics, architecture-decisions]
structured_data:
  type: TechArticle
  primary_topic: sap-integration
semantic_links:
  - type: part_of
    title: "SAP Integration Architecture"
    url: "/labs/enterprise-context/integrations/"
  - type: deep_dive
    title: "Apache Kafka Practical Lab"
    url: "/labs/enterprise-context/integrations/kafka/"
  - type: deep_dive
    title: "RabbitMQ Practical Lab"
    url: "/labs/enterprise-context/integrations/rabbitmq/"
  - type: related_topic
    title: "SAP Integration Operations"
    url: "/labs/enterprise-context/integration-operations/"
source_links:
  - title: "Apache Kafka introduction"
    url: "https://kafka.apache.org/44/getting-started/"
  - title: "RabbitMQ developer documentation"
    url: "https://www.rabbitmq.com/docs"
  - title: "RabbitMQ protocol guide"
    url: "https://www.rabbitmq.com/docs/protocols"
  - title: "SAP Cloud Integration adapter overview"
    url: "https://help.sap.com/docs/cloud-integration/sap-cloud-integration/introduction"
  - title: "SAP Integration Suite RabbitMQ adapter"
    url: "https://help.sap.com/docs/integration-suite/sap-integration-suite/rabbitmq-adapter"
---
<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">SAP Enterprise</a></li><li><a href="/labs/enterprise-context/integrations/">Integrations</a></li><li aria-current="page">Event Brokers</li></ol></nav>
<div class="research-canvas">
<header class="research-canvas__hero" data-reveal>
<div class="research-canvas__hero-copy"><p class="research-canvas__eyebrow">SAP Enterprise / Architecture Decision / Practical learning</p>
<h1>Kafka or RabbitMQ? Start with the business dependency.</h1>
<p>An event stream and a work queue can both move JSON, but they give applications different control over delivery, replay, routing, scale, and recovery. The right choice starts with the business interaction, not the product name.</p>
<a class="research-canvas__button" href="#decision-matrix">Compare the behavior <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a></div>
<div class="research-canvas__signal" aria-label="Decision sequence">
<p>Decision sequence</p>
<div class="research-canvas__signal-line"><span>01</span><strong>Meaning</strong><small>Event or command?</small></div>
<div class="research-canvas__signal-line"><span>02</span><strong>Shape</strong><small>Stream or queue?</small></div>
<div class="research-canvas__signal-line"><span>03</span><strong>Failure</strong><small>Retry and replay</small></div>
<div class="research-canvas__signal-line"><span>04</span><strong>Fit</strong><small>SAP integration owner</small></div>
<em>Comparison concerns conventional RabbitMQ queues; RabbitMQ Streams differ.</em></div></header>
<section class="research-canvas__boundary" data-reveal><span class="material-symbols-outlined" aria-hidden="true">compare_arrows</span>
<p><strong>Memory rule:</strong> Kafka is strongest when independent consumers need a retained event history and controlled replay. RabbitMQ queues are often simpler when a producer needs work routed to consumers with acknowledgements and failure queues.</p>
<p><strong>Not a binary choice:</strong> API calls, IDocs, SAP Event Mesh or Advanced Event Mesh, Cloud Integration, scheduled files, and plain database transactions may be a better fit. Streaming is not automatically better architecture.</p></section>
<section class="research-canvas__inventory" id="decision-matrix" data-reveal><header><p class="research-canvas__eyebrow">01 / Compare responsibility</p><h2>Same payload, different operational contract</h2><p>Use the matrix to decide which behavior you need. The table focuses on Kafka's event-log model and RabbitMQ's conventional queue model.</p></header>
<div class="table-scroll study-table"><table class="study-table__table"><thead><tr><th>Design dimension</th><th>Apache Kafka</th><th>RabbitMQ queues</th></tr></thead><tbody>
<tr><td>Primary model</td><td>Append records to partitioned logs</td><td>Route messages into queues for delivery</td></tr>
<tr><td>Typical question</td><td>“What happened, and who else wants to read it?”</td><td>“Who should perform this task?”</td></tr>
<tr><td>Reading</td><td>Consumers manage positions (offsets) in retained logs</td><td>Consumers receive and acknowledge deliveries</td></tr>
<tr><td>Independent subscribers</td><td>Different consumer groups read independently</td><td>Use separate bound queues to give each subscriber its own copy</td></tr>
<tr><td>Work sharing</td><td>Consumers share topic partitions inside one group</td><td>Multiple consumers compete for deliveries from one queue</td></tr>
<tr><td>Replay</td><td>A natural feature within configured retention limits</td><td>Not the usual queue model; consider RabbitMQ Streams or a separate event archive</td></tr>
<tr><td>Ordering</td><td>Within a partition; key and consumer behavior matter</td><td>Queue ordering and effective processing order depend on concurrency, priority, requeues and topology</td></tr>
<tr><td>Failed processing</td><td>Retries, error streams, pause/seek and offset handling are designed by the application</td><td>Acks, negative acks, dead-letter exchange and queue policies support recovery</td></tr>
<tr><td>Scaling constraint</td><td>Partition count, broker capacity, client throughput and group rebalance</td><td>Queue type, number of consumers, prefetch, routing and broker capacity</td></tr>
<tr><td>Operations and cost</td><td>Storage/retention, partitions, replication, lag and schema governance</td><td>Queue length, message age, consumers, DLQ, publisher confirms and queue replication</td></tr>
</tbody></table></div>
<p><strong>Scope warning:</strong> RabbitMQ Streams also offer retained, replayable data. That feature makes RabbitMQ broader than this simple comparison. Kafka and RabbitMQ are not the same class of platform in every deployment or protocol mode.</p></section>
<section class="research-canvas__inventory" id="cases" data-reveal><header><p class="research-canvas__eyebrow">02 / Put the business first</p><h2>Three realistic SAP-related requirements</h2><p>These are synthetic decision cases, not claims about a particular customer landscape.</p></header>
<div class="ecg-decision-columns">
<div><h3>A. Shipment visibility for many consumers</h3><p>External tracking, BI and an anomaly detector must independently consume status history. New services may rebuild state from past events. <strong>Prefer Kafka</strong> if retained replay and consumer independence justify the platform. Confirm the SAP event source first.</p></div>
<div><h3>B. Render an ASN document in background</h3><p>One worker processes each job; failures need retry and DLQ, without a historical stream requirement. <strong>Prefer a work queue such as RabbitMQ</strong> if a broker is needed, or a simpler managed job service if one already exists.</p></div>
<div><h3>C. Create a customer in S/4HANA</h3><p>The caller needs a clear application result, duplicate protection and authority checks. <strong>Start with a released API or established SAP integration pattern</strong>, not a broker solely because “asynchronous” sounds modern. An async queue may still mediate load if business acceptance is asynchronous.</p></div>
<div><h3>D. Distribute Business Partner changes</h3><p>First examine the supported S/4HANA/MDG replication path, filtering and receivers. DRF, APIs, IDocs and event services may apply by scenario. <strong>Do not substitute Kafka for source-side business ownership</strong>; a broker transports the contract, not master-data governance.</p></div></div>
<p><strong>Critical question:</strong> what does the producer consider success? Accepted for delivery, processed by a consumer, or committed as a business object? Define these separately in the interface contract.</p></section>
<section class="research-canvas__inventory" id="sap-landscape" data-reveal><header><p class="research-canvas__eyebrow">03 / SAP integration fit</p><h2>Where Integration Suite and Event Mesh enter the picture</h2><p>Treat products as layers of the architecture, not synonyms.</p></header>
<div class="research-route-list">
<a href="/labs/enterprise-context/integrations/"><span>SAP</span><strong>S/4HANA source or receiver</strong><small>Owns business rules, released APIs and available events. Edition, release, configuration and data determine what can be emitted or changed.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
<a href="/labs/enterprise-context/integrations/api-management/"><span>API</span><strong>API Management</strong><small>Controls published APIs, authentication, quotas and visibility. It does not replace a broker or business processing.</small><i class="material-symbols-outlined" aria-hidden="true">settings_ethernet</i></a>
<a href="/labs/enterprise-context/integrations/"><span>INT</span><strong>SAP Cloud Integration</strong><small>Routes and transforms payloads, applies mappings and handles connectivity. Kafka and RabbitMQ adapters have documented feature and tenant boundaries.</small><i class="material-symbols-outlined" aria-hidden="true">settings_input_component</i></a>
<a href="/labs/enterprise-context/integrations/"><span>EVT</span><strong>SAP Event Mesh / Advanced Event Mesh</strong><small>Related SAP event-messaging offerings; compare their own capabilities, scope, plans, protocols and operations rather than assuming a one-to-one replacement.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a></div>
<p><strong>Example flow — events:</strong> released SAP event / API → supported integration route → Kafka topic → tracking group + analytics group. <strong>Example flow — work:</strong> SAP-released message → Cloud Integration → RabbitMQ exchange → ASN worker queue → file status callback. These are designs to validate, not default SAP configuration.</p></section>
<section class="research-canvas__inventory" id="worksheet" data-reveal><header><p class="research-canvas__eyebrow">04 / Use this in a workshop</p><h2>Seven questions before you choose a broker</h2><p>Write the answers before the architecture diagram.</p></header>
<ol>
<li><strong>Business meaning:</strong> is the payload a fact that occurred, a command to do work, or an application response?</li>
<li><strong>Consumers:</strong> how many systems need it now, and will new independent consumers arrive later?</li>
<li><strong>History:</strong> must a new consumer replay days or months of events? What is the retention and legal/privacy boundary?</li>
<li><strong>Ordering:</strong> is strict per-business-object order necessary? Which key identifies that object? How is stale data rejected?</li>
<li><strong>Delivery semantics:</strong> may duplicates occur? What event/message ID enables idempotency? What is the final commit point?</li>
<li><strong>Operations:</strong> who monitors consumer lag or queue age, investigates DLQ records, replays messages, and reconciles application state?</li>
<li><strong>Economics:</strong> do the business value and reuse justify an additional platform, security model, operations team and runtime cost?</li></ol>
<p><strong>Decision record:</strong> “Given requirement X, choose Y because of A/B. Accept trade-off C. Revisit this choice when condition D changes.” This is more defensible than “Kafka scales better.”</p></section>
<section class="research-canvas__inventory" id="acceptance" data-reveal><header><p class="research-canvas__eyebrow">05 / Architecture proof</p><h2>Test the unhappy path before go-live</h2><p>A broker demo is not an end-to-end acceptance test.</p></header>
<div class="table-scroll study-table"><table class="study-table__table"><thead><tr><th>Test</th><th>Pass condition</th><th>Owner / evidence</th></tr></thead><tbody>
<tr><td>Producer timeout or unavailable broker</td><td>No silent loss; event is retried or recovered through a defined source mechanism</td><td>Source + integration owner; source log/outbox and publish result</td></tr>
<tr><td>Consumer crashes before commit</td><td>Redelivery is safe; external action remains idempotent</td><td>Consumer owner; event ID and target state</td></tr>
<tr><td>Invalid schema or unexpected value</td><td>Record is quarantined with cause, alert and recovery procedure</td><td>Contract owner; error payload metadata without secrets</td></tr>
<tr><td>Message backlog rises</td><td>Meaningful thresholds detect delayed business outcomes</td><td>Operations; lag or queue age and SLA</td></tr>
<tr><td>Replay or manual requeue</td><td>Recovered events are traceable and do not duplicate business effects</td><td>Recovery owner; reconciliation of source and target</td></tr>
<tr><td>Schema change</td><td>Old and new consumers behave as agreed under a compatibility policy</td><td>Producer + consumer owners; contract tests</td></tr>
</tbody></table></div>
<p><strong>Red flag:</strong> “We have exactly-once delivery because Kafka / RabbitMQ supports it.” The full chain may still be at-least-once. Validate source transaction, publish confirmation, offsets/acks, receiver commit and retry together.</p></section>
<section class="research-canvas__inventory" id="practice" data-reveal><header><p class="research-canvas__eyebrow">06 / Do the labs</p><h2>Learn the behavior, not the slide</h2><p>Run the two exercises with the same synthetic delivery reference and compare their outcomes.</p></header>
<div class="research-route-list">
<a href="/labs/enterprise-context/integrations/kafka/"><span>LAB 1</span><strong>Kafka — Publish, consume and replay</strong><small>Start Kafka 4.4, create three partitions, send keyed delivery events and read them from two consumer groups.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
<a href="/labs/enterprise-context/integrations/rabbitmq/"><span>LAB 2</span><strong>RabbitMQ — Route, acknowledge and dead-letter</strong><small>Start RabbitMQ 4.x, publish through a topic exchange, consume one queue and inspect a deliberately rejected message.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a></div>
<h3>Explain it in English (B2)</h3>
<p><strong>30-second version:</strong> “I would use Kafka when we need a retained event history with several independent consumers. RabbitMQ queues are a good option when workers need tasks routed, acknowledged and retried. For SAP, I would first confirm the released interface and ownership of the business process. Then I would design idempotency, monitoring and recovery. The broker alone does not guarantee business success.”</p>
<p><strong>Follow-up interview case:</strong> The tracking team wants Kafka, but the actual requirement is to generate one PDF per delivery and notify SAP when it is ready. Defend either choice using expected traffic, replay, failure recovery, operating cost, and existing platform investments.</p></section>
<section class="research-canvas__inventory" id="sources" data-reveal><header><p class="research-canvas__eyebrow">Official reference material</p><h2>Sources and validation status</h2><p>The matrix is an authored design comparison, not a vendor benchmark. Actual performance, price, availability and product support depend on the deployment.</p></header>
<ul><li><a href="https://kafka.apache.org/44/getting-started/" target="_blank" rel="noopener">Apache Kafka 4.4 documentation</a> and <a href="https://kafka.apache.org/44/getting-started/quickstart/" target="_blank" rel="noopener">quickstart</a>.</li>
<li><a href="https://www.rabbitmq.com/docs" target="_blank" rel="noopener">RabbitMQ 4.4 documentation</a>, <a href="https://www.rabbitmq.com/docs/protocols" target="_blank" rel="noopener">protocols</a>, and <a href="https://www.rabbitmq.com/docs/confirms" target="_blank" rel="noopener">acknowledgements</a>.</li>
<li><a href="https://help.sap.com/docs/cloud-integration/sap-cloud-integration/introduction" target="_blank" rel="noopener">SAP Cloud Integration adapter overview</a> and <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/rabbitmq-adapter" target="_blank" rel="noopener">RabbitMQ adapter</a>.</li>
<li><a href="/labs/enterprise-context/integrations/">Existing SAP Integration Architecture</a> for SAP Event Mesh, Advanced Event Mesh, IDocs, DRF and other patterns.</li></ul>
<p>Checked against official documentation on 22 November 2026. The examples are synthetic and not proof of a live SAP implementation. Human and hands-on verification pending.</p></section>
<div class="research-canvas__support" data-reveal><p><a href="/labs/enterprise-context/integrations/">Integration Architecture</a> · <a href="/labs/enterprise-context/integration-operations/">Integration Operations</a></p></div></div>