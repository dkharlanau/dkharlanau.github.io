---
layout: default
title: "Idempotent Consumer | SAP Development Patterns"
description: "A retry must not create a second business effect. Practical SAP ABAP, RAP, CAP architecture pattern."
permalink: /atlas/sap/development-patterns/idempotent-consumer/
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
  <li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Idempotent Consumer</li>
</ol></nav>
<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">SDP-14 · Integration · Architecture vocabulary</p>
    <h1>Idempotent Consumer</h1>
    <p class="note-subtitle">A retry must not create a second business effect.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>
  <div class="note-body">
    <h2>The situation</h2>
    <p>An IDoc or message broker redelivers the same business event. A handler inserts twice, sends two emails or posts the same business request twice.</p>
    <h2>The mental model</h2>
    <pre><code>Receive → identify intent → reserve/deduplicate → apply effect → record outcome</code></pre>
    <p><strong>Use when:</strong> Inbound IDocs, asynchronous events, webhook consumers, scheduled reprocessing and at-least-once messaging.</p>
    <h2>How to apply it</h2>
    <ol>
<li>Define an idempotency key from stable source identity and business intent; do not rely only on payload hash.</li>
<li>Store processing state atomically with the local business update wherever the transaction boundary allows.</li>
<li>On duplicates return the previous outcome or a safe no-op; distinguish repeat delivery from a legitimate newer change.</li>
<li>Define retention, ordering, concurrent delivery and recovery from 'in progress' explicitly.</li>
</ol>
    <h2>A small SAP example</h2>
    <p>A synthetic shipment notification is delivered three times. The handler recognizes one message identity and records one business effect, while allowing a new notification with the same shipment ID and new event ID.</p>
    <p><strong>Implementation sketch</strong> — conceptual only. This is not a compiled SAP sample, an API availability guarantee, or a production-ready implementation.</p>
    <pre><code>message key = source-system + event-id
if completed(key): return recorded result
atomically claim key + execute local effect
record success; recover interrupted claims explicitly</code></pre>
    <h2>Say it in a design review</h2>
    <blockquote><p>Add an Idempotent Consumer. We must tolerate duplicate delivery, not hope the broker sends once.</p></blockquote>
    <h2>Trade-offs and failure modes</h2>
    <p><strong>Watch for:</strong> Exactly-once business outcomes are not guaranteed merely by a dedup table; remote side effects and race conditions need their own design.</p>
    <p><strong>Choose differently when:</strong> For a genuinely read-only, side-effect-free operation, deduplication may not be necessary.</p>
    <h2>Acceptance question</h2>
    <p>What happens on concurrent duplicates, timeout after commit, replay and an event with a different ID but same business key?</p>
    <h2>References and scope</h2>
    <p>These are independent architecture explanations. Vendor sources establish platform capabilities; the design recommendation is a synthesis that still requires release, security and transaction-boundary verification in your own landscape.</p>
    <ul><li><a href="https://cap.cloud.sap/docs/guides/events/event-queues">CAP transactional event queues — SAP CAP documentation</a></li>
<li><a href="https://help.sap.com/saphelp_em900/helpdata/en/4a/66efbfcbff260be10000000a42189b/content.htm">Processing Inbound Master Data — SAP Help</a></li></ul>
    <h2>Continue the design</h2>
    <ul><li><a href="/atlas/sap/development-patterns/transactional-outbox/">SDP-15 · Transactional Outbox / Commit-Then-Publish</a></li>
<li><a href="/atlas/sap/development-patterns/retry-and-dead-letter/">SDP-16 · Retry + Dead Letter / Quarantine</a></li><li><a href="/atlas/sap/development-patterns/design-review/">Design-review template</a></li></ul>
    <p><a href="/atlas/sap/development-patterns/">← Back to the Pattern Library</a></p>
  </div>
</article>
{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
