---
layout: default
title: "Managed RAP Business Object | SAP Development Patterns"
description: "Let the RAP runtime own ordinary persistence, locking and transactional plumbing for custom data. Practical SAP ABAP, RAP, CAP architecture pattern."
permalink: /atlas/sap/development-patterns/managed-rap-business-object/
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
  <li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Managed RAP Business Object</li>
</ol></nav>
<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">SDP-08 · RAP · Architecture vocabulary</p>
    <h1>Managed RAP Business Object</h1>
    <p class="note-subtitle">Let the RAP runtime own ordinary persistence, locking and transactional plumbing for custom data.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>
  <div class="note-body">
    <h2>The situation</h2>
    <p>A new transactional app manually implements CRUD, locks, message mapping, ETags and OData even though RAP already provides a standard business-object model.</p>
    <h2>The mental model</h2>
    <pre><code>CDS root + composition → managed behavior → projection/service → consumer</code></pre>
    <p><strong>Use when:</strong> New transactional apps over suitable custom persistence where managed RAP is supported by the target ABAP release.</p>
    <h2>How to apply it</h2>
    <ol>
<li>Model the aggregate root and compositions in CDS; identify the transaction boundary.</li>
<li>Define managed behavior and required authorization, lock, numbering, validation and determination contracts.</li>
<li>Use service definition and binding for a consumer-specific projection.</li>
<li>Keep domain rules in behavior implementation or callable application services; test EML and save behavior.</li>
</ol>
    <h2>A small SAP example</h2>
    <p>A custom request application owns its own records and has an approval action. RAP handles standard persistence; the behavior definition declares the operations and the action implements the business transition.</p>
    <p><strong>Implementation sketch</strong> — conceptual only. This is not a compiled SAP sample, an API availability guarantee, or a production-ready implementation.</p>
    <pre><code>CDS root entity → behavior definition (managed)
               → behavior pool (custom rules/actions)
               → service projection → OData / Fiori elements</code></pre>
    <h2>Say it in a design review</h2>
    <blockquote><p>This is custom owned persistence: start with Managed RAP rather than hand-written CRUD.</p></blockquote>
    <h2>Trade-offs and failure modes</h2>
    <p><strong>Watch for:</strong> Managed is not 'no code'. Authorizations, aggregation boundaries, consistency and business logic remain design responsibilities.</p>
    <p><strong>Choose differently when:</strong> If persistence is already controlled by a complex legacy transaction or released API, examine Unmanaged RAP rather than forcing a second writer.</p>
    <h2>Acceptance question</h2>
    <p>Does the RAP runtime genuinely own save and persistence, and are authorization, locking and tests explicitly addressed?</p>
    <h2>References and scope</h2>
    <p>These are independent architecture explanations. Vendor sources establish platform capabilities; the design recommendation is a synthesis that still requires release, security and transaction-boundary verification in your own landscape.</p>
    <ul><li><a href="https://help.sap.com/docs/abap-cloud/abap-rap/documentation-overview-24e7a732427d42c2acdfab907eda26e7">ABAP RAP documentation overview — SAP Help</a></li>
<li><a href="https://help.sap.com/docs/abap-cloud/abap-rap/rap-business-object-contract">RAP Business Object Contract — SAP Help</a></li></ul>
    <h2>Continue the design</h2>
    <ul><li><a href="/atlas/sap/development-patterns/behavior-rule-placement/">SDP-10 · RAP Validation vs Determination vs Action</a></li>
<li><a href="/atlas/sap/development-patterns/unmanaged-rap-facade/">SDP-09 · Unmanaged RAP Facade</a></li><li><a href="/atlas/sap/development-patterns/design-review/">Design-review template</a></li></ul>
    <p><a href="/atlas/sap/development-patterns/">← Back to the Pattern Library</a></p>
  </div>
</article>
{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
