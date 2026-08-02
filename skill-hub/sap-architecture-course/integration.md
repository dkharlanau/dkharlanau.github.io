---
layout: default
title: "Make Integration Carry Its Own Weight — SAP Architect Field Course"
description: "Choose interfaces, events, ownership, and recovery behaviour without creating a brittle SAP landscape."
permalink: /skill-hub/sap-architecture-course/integration/
last_modified_at: 2026-07-31
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
sap_architecture_course: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/sap-architecture-course/">SAP Architect Field Course</a></li><li aria-current="page">Integration</li></ol></nav>

<article class="course-bite">
  <header><p class="eyebrow">02 / Integration</p><h1>Make integration carry its own weight.</h1><p class="lead">The hard part is not connecting two systems. The hard part is deciding what they are allowed to expect from each other when timing, data, or availability become inconvenient.</p></header>

  <section><h2>Every interface is a promise</h2><p>An interface is a promise about a change or a question. “Tell me the current credit status now.” “Let me know when a business partner is approved.” “Here is the nightly file you asked for.” The technology is secondary until the promise is clear.</p><p>Architects get into trouble when an interface is selected because it is familiar. Synchronous calls feel immediate. Events feel modern. Files feel old but safe. None is automatically right. The choice has to follow the business tolerance for delay, duplicate processing, partial failure, and temporary unavailability.</p></section>

  <section><h2>Start with the conversation shape</h2><h3>Question: I need an answer before I can continue</h3><p>Use a request-response pattern only when the caller genuinely cannot make the next decision without the answer. Keep the response narrow and design the timeout, fallback, and user message before the happy path.</p><h3>Fact: something changed and others may care</h3><p>Use an event when the source owns a state change and should not need to know every consumer. The event is not “call my service later.” It is a durable statement of fact, with an owner, a contract, and a recovery story.</p><h3>Transfer: here is a controlled set of records</h3><p>Use a file or managed batch when timing is intentionally grouped, volume is high, or the business control expects reconciliation. Batch is not architecture failure. Unexplained batch is.</p>
  <aside class="course-bite__checkpoint"><h3>Rule of thumb</h3><p>If a receiving system’s outage can stop the originating business process, that dependency is a design decision—not a transport detail. Put it in the decision record.</p></aside></section>

  <section><h2>Give every message an owner and a recovery owner</h2><p>Ownership comes in pairs. The producer owns whether the message is true and complete. The consumer owns whether it can use the message. Operations owns neither by magic: it needs an agreed runbook, visibility, and a place to send a failed item.</p><p>That distinction prevents the familiar “the middleware team says it left their queue” deadlock. A useful incident path can show: source state, message ID, handover timestamp, receipt evidence, consumer result, retry count, and business impact.</p><div class="course-bite__artifact"><h3>Interface contract card</h3><pre><code>Business promise: [what change/question?]
Producer + truth owner: [role/system]
Consumer + use: [role/system]
Pattern: request-response | event | batch
Allowed delay: [minutes/hours + reason]
Idempotency key: [how repeats are detected]
Failure route: [retry, queue, manual recovery]
Monitoring owner: [named role]
Reconciliation: [how missing or wrong records are found]</code></pre></div></section>

  <section><h2>Keep the most dangerous details visible</h2><ul><li><strong>Identity:</strong> which key survives the boundary? A display name is not a contract.</li><li><strong>Order:</strong> can status “B” arrive before status “A”? If it can, the consumer needs a rule.</li><li><strong>Duplicates:</strong> retries are normal. Posting twice is not.</li><li><strong>Deletion and correction:</strong> what does a retraction mean downstream?</li><li><strong>Versioning:</strong> can a new field appear without breaking a receiver?</li><li><strong>Observability:</strong> can a support analyst trace one business case end to end?</li></ul></section>

  <section><h2>Three things to stop doing</h2><p>Do not use synchronous integration to hide weak asynchronous handling. Do not call every emitted message an event when it is really a command to one known receiver. Do not draw a central middleware box and declare the integration solved. The interface contract, recovery path, and ownership model are the design.</p><p>For SAP landscapes, standard APIs, IDocs, OData, events, and integration services have different characteristics and version dependencies. Make your decision with actual product documentation, actual volume, and actual business timing—not architecture fashion.</p></section>

  <section><h2>Next: data is more than payload</h2><p>Integration moves data, but it does not make that data meaningful, governed, or ready for analytics and AI. The next module deals with the harder question: what can the organisation trust after the message arrives?</p><p class="course-bite__links"><a href="/skill-hub/sap-architecture-course/data-and-intelligence/">Continue: Turn data into a dependable product</a><br><a href="/skill-hub/integration-architecture/interface-ownership-working-skill/">Deepen the skill: Interface Ownership</a><br><a href="/atlas/concepts/rest-vs-odata-vs-soap-vs-idoc-vs-events/">Atlas: Integration pattern choices</a></p><p class="course-source">Independent course material informed by the SAP Architecture Center’s public integration and event-driven architecture references. It does not replace SAP product documentation or your organisation’s integration standards.</p></section>

  {% include atlas/author-block.html %}
</article>
