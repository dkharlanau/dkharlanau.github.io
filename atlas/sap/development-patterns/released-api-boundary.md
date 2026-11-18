---
layout: default
title: "Released API Boundary (Clean Core) | SAP Development Patterns"
description: "Depend on an intentional SAP contract, not on a convenient internal table or implementation detail. Practical SAP ABAP, RAP, CAP architecture pattern."
permalink: /atlas/sap/development-patterns/released-api-boundary/
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
  <li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Released API Boundary (Clean Core)</li>
</ol></nav>
<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">SDP-07 · Clean Core · Architecture vocabulary</p>
    <h1>Released API Boundary (Clean Core)</h1>
    <p class="note-subtitle">Depend on an intentional SAP contract, not on a convenient internal table or implementation detail.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>
  <div class="note-body">
    <h2>The situation</h2>
    <p>An enhancement reads an unreleased SAP table, writes an internal object and works today, but an upgrade or deployment change breaks the assumption.</p>
    <h2>The mental model</h2>
    <pre><code>Extension → permitted release contract → SAP-owned business object</code></pre>
    <p><strong>Use when:</strong> S/4HANA extensibility, ABAP Cloud, RAP extensions, clean-core assessments and classic-code modernization.</p>
    <h2>How to apply it</h2>
    <ol>
<li>First identify deployment: Public Edition, Private Edition, on-premise or BTP ABAP environment.</li>
<li>Check the released business object, CDS/API, BAdI or extension point and its specific release contract.</li>
<li>Put access behind an adapter so application code does not depend on the internal SAP representation.</li>
<li>Use ATC and target-release checks. If no released option exists, record an explicit exception or redesign rather than inventing a stable contract.</li>
</ol>
    <h2>A small SAP example</h2>
    <p>An extension needs business-partner attributes. Instead of directly binding business rules to an internal table, the reader adapter consumes a released object when the target landscape provides one.</p>
    <p><strong>Implementation sketch</strong> — conceptual only. This is not a compiled SAP sample, an API availability guarantee, or a production-ready implementation.</p>
    <pre><code>business decision
    ↓
SAP access port
    ↓
released CDS / business API / released BAdI
    ↓
SAP-owned data and transaction</code></pre>
    <h2>Say it in a design review</h2>
    <blockquote><p>We need a Released API Boundary. Please show the API's release status and the extension ownership model.</p></blockquote>
    <h2>Trade-offs and failure modes</h2>
    <p><strong>Watch for:</strong> Not every object described in documentation is released for ABAP Cloud. API availability, whitelisting and permitted operations vary by edition and release.</p>
    <p><strong>Choose differently when:</strong> In a controlled private/on-premises landscape, classic enhancement may be a conscious exception. Document upgrade and support risk.</p>
    <h2>Acceptance question</h2>
    <p>Which exact released contract and deployment version allow this call? What does ATC report?</p>
    <h2>References and scope</h2>
    <p>These are independent architecture explanations. Vendor sources establish platform capabilities; the design recommendation is a synthesis that still requires release, security and transaction-boundary verification in your own landscape.</p>
    <ul><li><a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/b5670aaaa2364a29935f40b16499972d/ef0301f6b908409c8e0802270a96a316.html">Working with ABAP for Cloud Development and Released APIs — SAP Help</a></li>
<li><a href="https://help.sap.com/docs/abap-cloud/abap-cloud-background-concepts-and-overview/abap-cloud-development-model">ABAP Cloud development model — SAP Help</a></li></ul>
    <h2>Continue the design</h2>
    <ul><li><a href="/atlas/sap/development-patterns/repository-and-dependency-injection/">SDP-03 · Repository + Dependency Injection</a></li>
<li><a href="/atlas/sap/development-patterns/managed-rap-business-object/">SDP-08 · Managed RAP Business Object</a></li><li><a href="/atlas/sap/development-patterns/design-review/">Design-review template</a></li></ul>
    <p><a href="/atlas/sap/development-patterns/">← Back to the Pattern Library</a></p>
  </div>
</article>
{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
