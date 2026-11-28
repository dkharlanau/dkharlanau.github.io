---
layout: default
title: "Transactional Outbox / Commit-Then-Publish | SAP Development Patterns"
description: "Never claim an event was delivered just because business code reached its last line. Practical SAP ABAP, RAP, CAP architecture pattern."
permalink: /atlas/sap/development-patterns/transactional-outbox/
author: "Dzmitryi Kharlanau"
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-17
hide_global_cta: true
tags:
  - sap
  - abap
  - software-architecture
  - design-patterns
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>
  <li><a href="/">Home</a></li><li><a href="/atlas/">Atlas</a></li><li><a href="/atlas/sap/">SAP</a></li>
  <li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Transactional Outbox / Commit-Then-Publish</li>
</ol></nav>
<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">SDP-15 · Integration · Architecture vocabulary</p>
    <h1>Transactional Outbox / Commit-Then-Publish</h1>
    <p class="note-subtitle">Never claim an event was delivered just because business code reached its last line.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>
  <div class="note-body">
    <h2>The situation</h2>
    <p>A transaction commits locally but the event publish fails; or an event escapes before the transaction rolls back.</p>
    <h2>The mental model</h2>
    <pre><code>Local transaction: business state + durable event record → commit → async dispatcher</code></pre>
    <p><strong>Use when:</strong> CAP transactional event queues, integration events and designs where a local state change must eventually produce an external effect.</p>
    <h2>How to apply it</h2>
    <ol>
<li>Identify the system of record and the local transaction boundary.</li>
<li>Persist the intent to publish in the same database transaction as the state change, when the platform supports that contract.</li>
<li>Dispatch asynchronously after commit, retry transient failures and retain correlation/processing state.</li>
<li>Make consumers idempotent: a crash during publication can still produce duplicate deliveries.</li>
</ol>
    <h2>A small SAP example</h2>
    <p>A synthetic approval request becomes approved and a notification needs to be sent. The business update and queued notification persist together, and a worker publishes only after commit.</p>
    <p><strong>Implementation sketch</strong> — conceptual only. This is not a compiled SAP sample, an API availability guarantee, or a production-ready implementation.</p>
    <pre><code>transaction:
  UPDATE request SET status='APPROVED'
  INSERT outbox(event_id, payload, state='PENDING')
COMMIT
worker: publish pending event → mark delivered (duplicates possible)</code></pre>
    <h2>Say it in a design review</h2>
    <blockquote><p>Use a Transactional Outbox or platform-managed event queue, and make the consumer idempotent.</p></blockquote>
    <h2>Trade-offs and failure modes</h2>
    <p><strong>Watch for:</strong> CAP offers transactional event queues; do not infer that arbitrary RAP business events or classic ABAP queues automatically provide the exact same atomicity guarantees.</p>
    <p><strong>Choose differently when:</strong> If an external call must be synchronous for business reasons, use an explicit failure contract and reconciliation instead of pretending it is a distributed atomic commit.</p>
    <h2>Acceptance question</h2>
    <p>Can the state commit without an event intent, or the event intent appear after a rollback? How is pending work monitored?</p>
    <h2>References and scope</h2>
    <p>These are independent architecture explanations. Vendor sources establish platform capabilities; the design recommendation is a synthesis that still requires release, security and transaction-boundary verification in your own landscape.</p>
    <ul><li><a href="https://cap.cloud.sap/docs/guides/events/event-queues">CAP transactional event queues — SAP CAP documentation</a></li>
<li><a href="https://help.sap.com/docs/abap-cloud/abap-rap/documentation-overview-24e7a732427d42c2acdfab907eda26e7">ABAP RAP documentation overview — SAP Help</a></li></ul>
    <h2>Continue the design</h2>
    <ul><li><a href="/atlas/sap/development-patterns/idempotent-consumer/">SDP-14 · Idempotent Consumer</a></li>
<li><a href="/atlas/sap/development-patterns/retry-and-dead-letter/">SDP-16 · Retry + Dead Letter / Quarantine</a></li><li><a href="/atlas/sap/development-patterns/design-review/">Design-review template</a></li></ul>
    <p><a href="/atlas/sap/development-patterns/">← Back to the Pattern Library</a></p>
  </div>
</article>
{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
