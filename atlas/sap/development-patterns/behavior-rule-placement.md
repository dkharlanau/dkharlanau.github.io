---
layout: default
title: "RAP Validation vs Determination vs Action | SAP Development Patterns"
description: "Use the RAP behavior concept that matches the business meaning. Practical SAP ABAP, RAP, CAP architecture pattern."
permalink: /atlas/sap/development-patterns/behavior-rule-placement/
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
  <li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">RAP Validation vs Determination vs Action</li>
</ol></nav>
<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">SDP-10 · RAP · Architecture vocabulary</p>
    <h1>RAP Validation vs Determination vs Action</h1>
    <p class="note-subtitle">Use the RAP behavior concept that matches the business meaning.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>
  <div class="note-body">
    <h2>The situation</h2>
    <p>A developer uses an action for automatic data filling, a determination to block an invalid record, and UI-side validation as the only safeguard.</p>
    <h2>The mental model</h2>
    <pre><code>Check invariant → Validation | derive state → Determination | explicit command → Action</code></pre>
    <p><strong>Use when:</strong> RAP behavior design: derived values, invariants, explicit business operations, authorization and user-visible errors.</p>
    <h2>How to apply it</h2>
    <ol>
<li>Choose validation when a rule must reject or report invalid business-object state at the supported execution point.</li>
<li>Choose determination when the framework should derive or update values based on triggers.</li>
<li>Choose action when an explicit consumer command changes business state (approve, submit, cancel).</li>
<li>Model trigger timing, draft behavior, side effects, authorization and messages in the behavior contract.</li>
</ol>
    <h2>A small SAP example</h2>
    <p>A synthetic expense request derives its default currency, validates a required approver and exposes Submit as an explicit action. Those are three different business reasons, so they get three different RAP contracts.</p>
    <p><strong>Implementation sketch</strong> — conceptual only. This is not a compiled SAP sample, an API availability guarantee, or a production-ready implementation.</p>
    <pre><code>Currency default   → determination
Missing approver   → validation
Submit request     → action
'Can submit?'      → authorization / feature control as appropriate</code></pre>
    <h2>Say it in a design review</h2>
    <blockquote><p>This needs a Determination, not an Action; the user did not request an explicit command. Keep the invariant in Validation.</p></blockquote>
    <h2>Trade-offs and failure modes</h2>
    <p><strong>Watch for:</strong> Do not assume a determination runs on every conceivable update or can replace authorization. Triggers and save-phase semantics depend on RAP modeling.</p>
    <p><strong>Choose differently when:</strong> If the rule belongs to a reusable pure domain service, keep it outside the behavior pool and call it from the correct RAP hook.</p>
    <h2>Acceptance question</h2>
    <p>Can you name the trigger, execution phase, error contract and draft behavior for this rule?</p>
    <h2>References and scope</h2>
    <p>These are independent architecture explanations. Vendor sources establish platform capabilities; the design recommendation is a synthesis that still requires release, security and transaction-boundary verification in your own landscape.</p>
    <ul><li><a href="https://help.sap.com/docs/abap-cloud/abap-rap/documentation-overview-24e7a732427d42c2acdfab907eda26e7">ABAP RAP documentation overview — SAP Help</a></li>
<li><a href="https://help.sap.com/docs/abap-cloud/abap-rap/rap-business-object-contract">RAP Business Object Contract — SAP Help</a></li></ul>
    <h2>Continue the design</h2>
    <ul><li><a href="/atlas/sap/development-patterns/managed-rap-business-object/">SDP-08 · Managed RAP Business Object</a></li>
<li><a href="/atlas/sap/development-patterns/draft-workflow/">SDP-11 · RAP Draft Workflow</a></li><li><a href="/atlas/sap/development-patterns/design-review/">Design-review template</a></li></ul>
    <p><a href="/atlas/sap/development-patterns/">← Back to the Pattern Library</a></p>
  </div>
</article>
{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
