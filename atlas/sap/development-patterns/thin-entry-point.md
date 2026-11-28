---
layout: default
title: "Thin Entry Point | SAP Development Patterns"
description: "A BAdI, user exit or IDoc hook should route work, not become the application. Practical SAP ABAP, RAP, CAP architecture pattern."
permalink: /atlas/sap/development-patterns/thin-entry-point/
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
  <li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Thin Entry Point</li>
</ol></nav>
<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">SDP-01 · ABAP OO · Architecture vocabulary</p>
    <h1>Thin Entry Point</h1>
    <p class="note-subtitle">A BAdI, user exit or IDoc hook should route work, not become the application.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>
  <div class="note-body">
    <h2>The situation</h2>
    <p>A ten-line enhancement grows into a 600-line mixture of field mapping, lookups, validation, logging and database writes. Nobody can test it without running a complete SAP process.</p>
    <h2>The mental model</h2>
    <pre><code>Adapter or enhancement → application service → domain rules → persistence port</code></pre>
    <p><strong>Use when:</strong> Classic ABAP exits and BAdIs; inbound function modules; event handlers; RAP handler methods that need reusable domain logic.</p>
    <h2>How to apply it</h2>
    <ol>
<li>Keep the framework-specific method responsible for translating its input and output contract.</li>
<li>Call one application service with an explicit request object and dependencies.</li>
<li>Return a result with messages; let the owning transaction decide how to persist and commit.</li>
<li>Place business decisions in small named collaborators, not in the entry-point class.</li>
</ol>
    <h2>A small SAP example</h2>
    <p>A synthetic inbound customer message has company-code data and general data. The enhancement creates one canonical request, calls the application service and returns the decisions for each segment. The same rules can be exercised in ABAP Unit without executing ALE.</p>
    <p><strong>Implementation sketch</strong> — conceptual only. This is not a compiled SAP sample, an API availability guarantee, or a production-ready implementation.</p>
    <pre><code>ENHANCEMENT / BAdI / IDoc ENTRY
  -&gt; to_request( framework_input )
  -&gt; application_service-&gt;execute( request )
  -&gt; to_framework_result( result )

The entry point contains no business-specific CASE on sales organization.</code></pre>
    <h2>Say it in a design review</h2>
    <blockquote><p>Use a Thin Entry Point: the enhancement should translate the SAP contract and delegate to an application service.</p></blockquote>
    <h2>Trade-offs and failure modes</h2>
    <p><strong>Watch for:</strong> A single application service with 30 private methods is still a god class. Measure separation by independently testable responsibilities, not class count.</p>
    <p><strong>Choose differently when:</strong> For a truly trivial one-field rule, extracting a full service layer may be unnecessary; keep the smallest readable implementation.</p>
    <h2>Acceptance question</h2>
    <p>Can we unit-test the rule without executing the BAdI, IDoc or UI runtime?</p>
    <h2>References and scope</h2>
    <p>These are independent architecture explanations. Vendor sources establish platform capabilities; the design recommendation is a synthesis that still requires release, security and transaction-boundary verification in your own landscape.</p>
    <ul><li><a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/ba879a6e2ea04d9bb94c7ccd7cdac446/e18eca61554345429f3a17e30955de8b.html">Managing Dependencies in ABAP Unit Testing — SAP Help</a></li>
<li><a href="https://help.sap.com/docs/abap-cloud/abap-cloud-background-concepts-and-overview/abap-cloud-development-model">ABAP Cloud development model — SAP Help</a></li></ul>
    <h2>Continue the design</h2>
    <ul><li><a href="/atlas/sap/development-patterns/repository-and-dependency-injection/">SDP-03 · Repository + Dependency Injection</a></li>
<li><a href="/atlas/sap/development-patterns/strategy-policy/">SDP-02 · Strategy / Policy Resolver</a></li><li><a href="/atlas/sap/development-patterns/design-review/">Design-review template</a></li></ul>
    <p><a href="/atlas/sap/development-patterns/">← Back to the Pattern Library</a></p>
  </div>
</article>
{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
