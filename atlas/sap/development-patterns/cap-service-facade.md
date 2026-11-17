---
layout: default
title: "CAP Service Facade | SAP Development Patterns"
description: "Expose a purpose-built service contract instead of publishing the database model verbatim. Practical SAP ABAP, RAP, CAP architecture pattern."
permalink: /atlas/sap/development-patterns/cap-service-facade/
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
  <li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">CAP Service Facade</li>
</ol></nav>
<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">SDP-12 · CAP · Architecture vocabulary</p>
    <h1>CAP Service Facade</h1>
    <p class="note-subtitle">Expose a purpose-built service contract instead of publishing the database model verbatim.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>
  <div class="note-body">
    <h2>The situation</h2>
    <p>A side-by-side app exposes every persistence field and makes its consumers depend on the internal data schema or a remote S/4HANA entity layout.</p>
    <h2>The mental model</h2>
    <pre><code>Domain model or remote API → service projection → consumer contract</code></pre>
    <p><strong>Use when:</strong> SAP CAP Node.js/Java services, side-by-side extensions, remote API aggregation and consumer-specific API surfaces.</p>
    <h2>How to apply it</h2>
    <ol>
<li>Start from the use case and contract; define entities, actions and authorizations the consumer actually needs.</li>
<li>Model the domain in CDS and expose projections through an application service.</li>
<li>For remote S/4 data, import the remote service contract and implement the required query/delegation behavior.</li>
<li>Keep translation, identity, data ownership, pagination and errors explicit; restrict sensitive fields.</li>
</ol>
    <h2>A small SAP example</h2>
    <p>A CAP approval app presents a compact business-partner summary instead of directly exposing every field of the remote SAP API.</p>
    <p><strong>Implementation sketch</strong> — conceptual only. This is not a compiled SAP sample, an API availability guarantee, or a production-ready implementation.</p>
    <pre><code>using { my.domain as d } from '../db/schema';
service ReviewService {
  @readonly entity Requests as projection on d.Requests;
  action submit(ID: UUID);
}
// Illustrative CDS; actual types and handlers depend on the app.</code></pre>
    <h2>Say it in a design review</h2>
    <blockquote><p>Use a CAP Service Facade. Let the consumer see a stable use-case contract, not the underlying storage or remote ERP schema.</p></blockquote>
    <h2>Trade-offs and failure modes</h2>
    <p><strong>Watch for:</strong> A simple CAP projection onto a remote entity is not guaranteed to work without remote delegation. CAP runtime/version and actual service binding matter.</p>
    <p><strong>Choose differently when:</strong> For a requirement that is an extension of an S/4HANA-owned transaction with tight local consistency, an on-stack RAP or released BAdI may fit better.</p>
    <h2>Acceptance question</h2>
    <p>Can the internal DB or remote API change without a breaking consumer change, and are authorization/data exposure bounded?</p>
    <h2>References and scope</h2>
    <p>These are independent architecture explanations. Vendor sources establish platform capabilities; the design recommendation is a synthesis that still requires release, security and transaction-boundary verification in your own landscape.</p>
    <ul><li><a href="https://cap.cloud.sap/docs/get-started/concepts">CAP core concepts — SAP CAP documentation</a></li>
<li><a href="https://cap.cloud.sap/docs/guides/services/providing-services">CAP providing services — SAP CAP documentation</a></li>
<li><a href="https://cap.cloud.sap/docs/guides/services/consuming-services">CAP consuming remote services — SAP CAP documentation</a></li></ul>
    <h2>Continue the design</h2>
    <ul><li><a href="/atlas/sap/development-patterns/anti-corruption-layer/">SDP-04 · Anti-Corruption Layer (ACL)</a></li>
<li><a href="/atlas/sap/development-patterns/cap-event-handler/">SDP-13 · CAP Event Handler / Lifecycle Hook</a></li><li><a href="/atlas/sap/development-patterns/design-review/">Design-review template</a></li></ul>
    <p><a href="/atlas/sap/development-patterns/">← Back to the Pattern Library</a></p>
  </div>
</article>
{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
