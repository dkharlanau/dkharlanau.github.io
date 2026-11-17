---
layout: default
title: "Unmanaged RAP Facade | SAP Development Patterns"
description: "Modernize the service contract around proven transactional logic without rewriting the engine first. Practical SAP ABAP, RAP, CAP architecture pattern."
permalink: /atlas/sap/development-patterns/unmanaged-rap-facade/
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
  <li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Unmanaged RAP Facade</li>
</ol></nav>
<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">SDP-09 · RAP · Architecture vocabulary</p>
    <h1>Unmanaged RAP Facade</h1>
    <p class="note-subtitle">Modernize the service contract around proven transactional logic without rewriting the engine first.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>
  <div class="note-body">
    <h2>The situation</h2>
    <p>A mature business transaction must be exposed as OData, but it has its own persistence process and cannot be converted to managed RAP without duplicate state or changed semantics.</p>
    <h2>The mental model</h2>
    <pre><code>RAP BO contract → unmanaged handler/buffer → supported legacy API → existing owner</code></pre>
    <p><strong>Use when:</strong> Legacy business logic exposed as RAP when managed persistence is unsuitable and the target API's transaction behavior permits integration.</p>
    <h2>How to apply it</h2>
    <ol>
<li>Identify the actual legacy transaction owner, lock and save contract before writing behavior handlers.</li>
<li>Implement the unmanaged RAP operations and buffering according to RAP BO contract and save sequence.</li>
<li>Map legacy errors into reported/failed messages and preserve transactional guarantees.</li>
<li>Write integration tests for failed saves, repeated requests, concurrency and authorization.</li>
</ol>
    <h2>A small SAP example</h2>
    <p>A synthetic posting process has a proven internal engine. A RAP façade offers a modern contract but does not create a second table to 'mirror' the posting.</p>
    <p><strong>Implementation sketch</strong> — conceptual only. This is not a compiled SAP sample, an API availability guarantee, or a production-ready implementation.</p>
    <pre><code>EML / service request
  → unmanaged RAP handler
  → managed buffer and save contract (implemented by you)
  → transaction-owning legacy API</code></pre>
    <h2>Say it in a design review</h2>
    <blockquote><p>Use an Unmanaged RAP Facade so the existing engine stays the single writer; prove the save-sequence contract first.</p></blockquote>
    <h2>Trade-offs and failure modes</h2>
    <p><strong>Watch for:</strong> Do not call APIs that perform uncontrolled COMMIT WORK inside an incompatible RAP save sequence. Confirm supported integration points and LUW behavior.</p>
    <p><strong>Choose differently when:</strong> If the application owns straightforward custom persistence, Managed RAP is usually less code and operational risk.</p>
    <h2>Acceptance question</h2>
    <p>Who commits? Where are locks acquired? Can a failed legacy call be reflected without partial saves?</p>
    <h2>References and scope</h2>
    <p>These are independent architecture explanations. Vendor sources establish platform capabilities; the design recommendation is a synthesis that still requires release, security and transaction-boundary verification in your own landscape.</p>
    <ul><li><a href="https://help.sap.com/docs/abap-cloud/abap-rap/rap-business-object-contract">RAP Business Object Contract — SAP Help</a></li>
<li><a href="https://help.sap.com/docs/abap-cloud/abap-rap/documentation-overview-24e7a732427d42c2acdfab907eda26e7">ABAP RAP documentation overview — SAP Help</a></li></ul>
    <h2>Continue the design</h2>
    <ul><li><a href="/atlas/sap/development-patterns/managed-rap-business-object/">SDP-08 · Managed RAP Business Object</a></li>
<li><a href="/atlas/sap/development-patterns/released-api-boundary/">SDP-07 · Released API Boundary (Clean Core)</a></li><li><a href="/atlas/sap/development-patterns/design-review/">Design-review template</a></li></ul>
    <p><a href="/atlas/sap/development-patterns/">← Back to the Pattern Library</a></p>
  </div>
</article>
{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
