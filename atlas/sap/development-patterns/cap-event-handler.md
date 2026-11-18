---
layout: default
title: "CAP Event Handler / Lifecycle Hook | SAP Development Patterns"
description: "Add custom logic around CAP's service events while keeping the service contract in charge. Practical SAP ABAP, RAP, CAP architecture pattern."
permalink: /atlas/sap/development-patterns/cap-event-handler/
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
  <li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">CAP Event Handler / Lifecycle Hook</li>
</ol></nav>
<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">SDP-13 · CAP · Architecture vocabulary</p>
    <h1>CAP Event Handler / Lifecycle Hook</h1>
    <p class="note-subtitle">Add custom logic around CAP's service events while keeping the service contract in charge.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>
  <div class="note-body">
    <h2>The situation</h2>
    <p>A CAP application bypasses the service runtime with ad hoc HTTP endpoints and directly accesses tables for business commands.</p>
    <h2>The mental model</h2>
    <pre><code>Service event → before check / on implementation / after enrichment</code></pre>
    <p><strong>Use when:</strong> CAP lifecycle validations, actions, custom reads and service orchestration in Node.js or Java.</p>
    <h2>How to apply it</h2>
    <ol>
<li>First check whether a declarative CDS constraint or generic service already covers the requirement.</li>
<li>Use before handlers for preconditions, on handlers to implement or override processing, after handlers for appropriate result processing.</li>
<li>Preserve framework transaction context; handle errors using supported service semantics.</li>
<li>Make outbound effects explicit and use a durable async boundary when delivery must survive retries or crashes.</li>
</ol>
    <h2>A small SAP example</h2>
    <p>A synthetic CAP request service rejects creation without an external reference and implements Submit as an explicit action rather than a hidden side effect of READ.</p>
    <p><strong>Implementation sketch</strong> — conceptual only. This is not a compiled SAP sample, an API availability guarantee, or a production-ready implementation.</p>
    <pre><code>this.before('CREATE', 'Requests', req =&gt; {
  if (!req.data.externalRef) req.reject(400, 'External reference required')
})
// Illustrative Node.js CAP handler inside service initialization.</code></pre>
    <h2>Say it in a design review</h2>
    <blockquote><p>Use a CAP Event Handler for the service lifecycle; do not create a second controller that bypasses CAP authorization and transaction rules.</p></blockquote>
    <h2>Trade-offs and failure modes</h2>
    <p><strong>Watch for:</strong> Do not place long-running remote calls in a synchronous handler without timeout, failure policy and ownership analysis.</p>
    <p><strong>Choose differently when:</strong> If the behavior is declarative validation or a standard CRUD case, avoid custom handlers altogether.</p>
    <h2>Acceptance question</h2>
    <p>Can we state which event phase owns the rule, which transaction it joins and whether it may be retried?</p>
    <h2>References and scope</h2>
    <p>These are independent architecture explanations. Vendor sources establish platform capabilities; the design recommendation is a synthesis that still requires release, security and transaction-boundary verification in your own landscape.</p>
    <ul><li><a href="https://cap.cloud.sap/docs/get-started/concepts">CAP core concepts — SAP CAP documentation</a></li>
<li><a href="https://cap.cloud.sap/docs/java/event-handlers/">CAP event handlers — SAP CAP documentation</a></li>
<li><a href="https://cap.cloud.sap/docs/guides/">CAP cookbook — SAP CAP documentation</a></li></ul>
    <h2>Continue the design</h2>
    <ul><li><a href="/atlas/sap/development-patterns/cap-service-facade/">SDP-12 · CAP Service Facade</a></li>
<li><a href="/atlas/sap/development-patterns/transactional-outbox/">SDP-15 · Transactional Outbox / Commit-Then-Publish</a></li><li><a href="/atlas/sap/development-patterns/design-review/">Design-review template</a></li></ul>
    <p><a href="/atlas/sap/development-patterns/">← Back to the Pattern Library</a></p>
  </div>
</article>
{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
