---
layout: default
title: "Retry + Dead Letter / Quarantine | SAP Development Patterns"
description: "Retry a temporary outage; quarantine bad data; never run an infinite retry storm. Practical SAP ABAP, RAP, CAP architecture pattern."
permalink: /atlas/sap/development-patterns/retry-and-dead-letter/
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
  <li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Retry + Dead Letter / Quarantine</li>
</ol></nav>
<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">SDP-16 · Integration · Architecture vocabulary</p>
    <h1>Retry + Dead Letter / Quarantine</h1>
    <p class="note-subtitle">Retry a temporary outage; quarantine bad data; never run an infinite retry storm.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>
  <div class="note-body">
    <h2>The situation</h2>
    <p>A consumer retries a malformed payload forever, or drops a valid event after one temporary SAP API timeout.</p>
    <h2>The mental model</h2>
    <pre><code>Classify failure → retry with budget or quarantine → investigate/replay</code></pre>
    <p><strong>Use when:</strong> API and messaging integrations, CAP event queues, workers, IDoc monitoring and high-volume background processing.</p>
    <h2>How to apply it</h2>
    <ol>
<li>Separate transient faults (network, 429, service unavailable) from permanent faults (schema, business validation, authorization).</li>
<li>Use a bounded retry policy with exponential backoff and jitter for transient failures.</li>
<li>Move exhausted or non-retriable messages to a visible quarantine/dead-letter path with sanitized diagnostics.</li>
<li>Define operator replay, poison-message handling, deduplication and alert thresholds.</li>
</ol>
    <h2>A small SAP example</h2>
    <p>A synthetic partner update is rejected for an invalid country code. Retrying cannot make the payload valid; it goes to quarantine. A timeout on the same API can be retried within a bounded budget.</p>
    <p><strong>Implementation sketch</strong> — conceptual only. This is not a compiled SAP sample, an API availability guarantee, or a production-ready implementation.</p>
    <pre><code>transient → retry (max attempts, backoff, jitter)
permanent → quarantine + actionable reason
unknown   → bounded retry → quarantine + triage
replay    → idempotency check → process</code></pre>
    <h2>Say it in a design review</h2>
    <blockquote><p>Add a Retry Budget and Dead Letter policy: operators must know what failed, why it stopped and how to replay safely.</p></blockquote>
    <h2>Trade-offs and failure modes</h2>
    <p><strong>Watch for:</strong> Do not log personal data or credentials in DLQ diagnostics. A dead-letter queue is a recovery process, not a substitute for root-cause analysis.</p>
    <p><strong>Choose differently when:</strong> For a one-time synchronous command where the user owns immediate remediation, surface a clear error instead of adding a queue.</p>
    <h2>Acceptance question</h2>
    <p>Can we test 429, timeout, validation failure, repeated poison messages, duplicate replay and recovery alerts?</p>
    <h2>References and scope</h2>
    <p>These are independent architecture explanations. Vendor sources establish platform capabilities; the design recommendation is a synthesis that still requires release, security and transaction-boundary verification in your own landscape.</p>
    <ul><li><a href="https://cap.cloud.sap/docs/guides/events/event-queues">CAP transactional event queues — SAP CAP documentation</a></li>
<li><a href="https://cap.cloud.sap/docs/guides/">CAP cookbook — SAP CAP documentation</a></li></ul>
    <h2>Continue the design</h2>
    <ul><li><a href="/atlas/sap/development-patterns/idempotent-consumer/">SDP-14 · Idempotent Consumer</a></li>
<li><a href="/atlas/sap/development-patterns/transactional-outbox/">SDP-15 · Transactional Outbox / Commit-Then-Publish</a></li><li><a href="/atlas/sap/development-patterns/design-review/">Design-review template</a></li></ul>
    <p><a href="/atlas/sap/development-patterns/">← Back to the Pattern Library</a></p>
  </div>
</article>
{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
