---
layout: default
title: "Architecture Design Review — SAP Pattern Vocabulary"
description: "An executable architecture discussion format for ABAP, RAP, CAP and integration design reviews."
permalink: /atlas/sap/development-patterns/design-review/
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

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Atlas</a></li><li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Design Review</li></ol></nav>
<article class="section note-detail atlas-page">
<header class="note-header"><p class="eyebrow">SAP Development Pattern Library · Working agreement</p><h1>Architectural vocabulary for code reviews</h1><p class="note-subtitle">A pattern name should speed up reasoning, not replace it.</p><div class="atlas-pill-row">{% include atlas/status-badge.html %}</div></header>
<div class="note-body">
<h2>A useful review comment</h2>
<blockquote><p>"Use <strong>SDP-05 Delta-Aware Merge</strong> at the inbound boundary. The sender omits unchanged fields, so raw structure assignment risks overwriting valid target data. First normalize keys, then evaluate MSGFN per segment and write only explicitly allowed fields. Reject unrecognized message operations. Test changed, unchanged-carrier, delete and replay scenarios."</p></blockquote>
<h2>A weak comment</h2>
<blockquote><p>"Please apply a design pattern and make the code clean."</p></blockquote>
<p>The first comment names a shared model, its reason, a concrete implementation boundary and observable tests. The second gives the developer no decision information.</p>
<h2>Copy this architecture decision record</h2>
<pre><code>Decision ID: ADR-000
Context: [business problem, trigger, existing process]
Systems / edition: [S/4 Public, Private, on-prem, BTP]
Transaction owner: [where state is committed]
Pattern: [SDP-ID + canonical name]
Decision: [what moves where, and why]
Rejected alternatives: [at least one credible option]
Interfaces and data contract: [inputs, outputs, mapping]
Failure and replay model: [errors, retries, duplication]
Security and release checks: [roles, released APIs, ATC]
Acceptance tests: [happy path, negative, concurrency, rollback]
Evidence: [vendor docs, design/test links]
Owner and review date: [...]
</code></pre>
<h2>Five questions that reveal a real architecture</h2>
<ol>
<li><strong>Ownership:</strong> Who owns the business object, data and commit?</li>
<li><strong>Boundary:</strong> What can change independently, and what is the stable contract?</li>
<li><strong>Variation:</strong> Is the next requirement a new algorithm, a new configuration row or a new interface?</li>
<li><strong>Failure:</strong> What happens after a timeout, duplicate delivery, partial save or stale read?</li>
<li><strong>Proof:</strong> What test or operational signal would demonstrate the design is wrong?</li>
</ol>
<h2>Use names precisely</h2>
<div class="table-scroll study-table" tabindex="0" role="region" aria-label="Pattern terminology">
<table class="study-table__table"><thead><tr><th scope="col">Term</th><th scope="col">Means</th><th scope="col">Does not mean</th></tr></thead><tbody>
<tr><td>Strategy</td><td>Interchangeable algorithms through a common contract</td><td>Any customizing table</td></tr>
<tr><td>Repository</td><td>Persistence/access abstraction for a consumer</td><td>A universal generic SELECT wrapper</td></tr>
<tr><td>RAP Managed BO</td><td>Framework-managed transactional persistence within RAP</td><td>Any new OData service</td></tr>
<tr><td>CAP Service Facade</td><td>Consumer-specific service projection and behavior</td><td>A copy of the ERP database</td></tr>
<tr><td>Idempotent Consumer</td><td>Safe handling of repeated business intent</td><td>Global exactly-once delivery</td></tr>
<tr><td>Outbox</td><td>Durable event intent tied to local state transaction</td><td>Arbitrary post-commit HTTP call</td></tr>
</tbody></table></div>
<h2>Try the method</h2>
<p>Review a synthetic inbound customer update with multiple organization keys and optional fields. Choose between Strategy and Decision Table for a country-specific rule; identify the ACL boundary; specify Delta-Aware Merge; then design Idempotent Consumer and replay. If the request becomes a new S/4-owned transactional UI, decide whether Managed RAP is appropriate. If the capability must combine several systems, evaluate CAP and its transaction boundary. Note how changing one requirement can change the pattern selection.</p>
<p><a href="/atlas/sap/development-patterns/">← Browse all 16 patterns</a></p>
</div></article>
{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
