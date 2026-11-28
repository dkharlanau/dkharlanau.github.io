---
layout: default
title: "Repository + Dependency Injection | SAP Development Patterns"
description: "Hide database and SAP API calls behind a testable boundary. Practical SAP ABAP, RAP, CAP architecture pattern."
permalink: /atlas/sap/development-patterns/repository-and-dependency-injection/
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
  <li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Repository + Dependency Injection</li>
</ol></nav>
<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">SDP-03 · ABAP OO · Architecture vocabulary</p>
    <h1>Repository + Dependency Injection</h1>
    <p class="note-subtitle">Hide database and SAP API calls behind a testable boundary.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>
  <div class="note-body">
    <h2>The situation</h2>
    <p>Domain code directly SELECTs KNA1, calls a function module and checks SY-SUBRC. Each unit test needs a real SAP record and becomes environment-dependent.</p>
    <h2>The mental model</h2>
    <pre><code>Application service → reader/writer interface → SAP adapter (DB, released API or BAPI)</code></pre>
    <p><strong>Use when:</strong> ABAP OO logic that reads persistence, SAP APIs, system time, authorization or external calls; unit-testable legacy refactoring.</p>
    <h2>How to apply it</h2>
    <ol>
<li>Define a consumer-oriented interface (for example read_customer), not a generic CRUD gateway for every table.</li>
<li>Inject the concrete reader through the service constructor or another explicit composition boundary.</li>
<li>In ABAP Unit, substitute a small fake with controlled inputs and inspect calls/output.</li>
<li>Preserve locking, authority and LUW ownership in the real adapter rather than hiding them from the design.</li>
</ol>
    <h2>A small SAP example</h2>
    <p>A customer eligibility rule needs business partner state. In production an adapter reads through an API appropriate to the deployment. During tests a fake returns 'active' or 'blocked' without accessing the database.</p>
    <p><strong>Implementation sketch</strong> — conceptual only. This is not a compiled SAP sample, an API availability guarantee, or a production-ready implementation.</p>
    <pre><code>DATA(service) = NEW zcl_eligibility_service(
  io_customer_reader = reader
  io_clock           = clock ).

&quot;Interfaces and Z classes are illustrative, not executable sample packages.</code></pre>
    <h2>Say it in a design review</h2>
    <blockquote><p>Use Repository + DI. The business decision should not know whether its input came from SQL, EML or a released API.</p></blockquote>
    <h2>Trade-offs and failure modes</h2>
    <p><strong>Watch for:</strong> A repository that exposes raw SELECT options leaks the database model. A repository must protect, not disguise, the dependency.</p>
    <p><strong>Choose differently when:</strong> For a simple read-only RAP query with no business decision, a dedicated abstraction may add more complexity than value.</p>
    <h2>Acceptance question</h2>
    <p>Can we exercise success, missing record, authorization failure and stale data entirely in an ABAP Unit fixture?</p>
    <h2>References and scope</h2>
    <p>These are independent architecture explanations. Vendor sources establish platform capabilities; the design recommendation is a synthesis that still requires release, security and transaction-boundary verification in your own landscape.</p>
    <ul><li><a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/ba879a6e2ea04d9bb94c7ccd7cdac446/e18eca61554345429f3a17e30955de8b.html">Managing Dependencies in ABAP Unit Testing — SAP Help</a></li>
<li><a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/b5670aaaa2364a29935f40b16499972d/ef0301f6b908409c8e0802270a96a316.html">Working with ABAP for Cloud Development and Released APIs — SAP Help</a></li></ul>
    <h2>Continue the design</h2>
    <ul><li><a href="/atlas/sap/development-patterns/thin-entry-point/">SDP-01 · Thin Entry Point</a></li>
<li><a href="/atlas/sap/development-patterns/released-api-boundary/">SDP-07 · Released API Boundary (Clean Core)</a></li><li><a href="/atlas/sap/development-patterns/design-review/">Design-review template</a></li></ul>
    <p><a href="/atlas/sap/development-patterns/">← Back to the Pattern Library</a></p>
  </div>
</article>
{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
