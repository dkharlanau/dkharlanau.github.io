---
layout: default
title: "RAP Draft Workflow | SAP Development Patterns"
description: "Separate 'I am editing' from 'the active business state has changed'. Practical SAP ABAP, RAP, CAP architecture pattern."
permalink: /atlas/sap/development-patterns/draft-workflow/
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
  <li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">RAP Draft Workflow</li>
</ol></nav>
<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">SDP-11 · RAP · Architecture vocabulary</p>
    <h1>RAP Draft Workflow</h1>
    <p class="note-subtitle">Separate 'I am editing' from 'the active business state has changed'.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>
  <div class="note-body">
    <h2>The situation</h2>
    <p>A multi-step edit form writes incomplete records directly to active tables or builds a bespoke work-in-progress mechanism.</p>
    <h2>The mental model</h2>
    <pre><code>Active instance ⇄ draft edit state → prepare/validate → activate</code></pre>
    <p><strong>Use when:</strong> Fiori forms with long-running edits, temporary incomplete state and multi-step user interaction supported by RAP draft.</p>
    <h2>How to apply it</h2>
    <ol>
<li>Define whether a user needs to park an incomplete transactional change without publishing it as active.</li>
<li>Model a draft-enabled RAP BO, draft actions and appropriate locks, authorizations and validations.</li>
<li>Define when Prepare and Activate validate, and how users handle conflicts with active state.</li>
<li>Test abandoned drafts, concurrent editors, activation errors and cleanup policy.</li>
</ol>
    <h2>A small SAP example</h2>
    <p>A buyer starts an adjustment, saves an incomplete draft, resumes later and activates only once required values are valid. Other consumers still see the active state until activation.</p>
    <p><strong>Implementation sketch</strong> — conceptual only. This is not a compiled SAP sample, an API availability guarantee, or a production-ready implementation.</p>
    <pre><code>Active → Edit → Draft → Prepare → Activate → Active
                     ↘ Discard

Draft persistence is a framework mechanism, not a generic audit log.</code></pre>
    <h2>Say it in a design review</h2>
    <blockquote><p>Use RAP Draft if the real requirement is safe multi-step editing; do not invent an extra 'temporary' active status.</p></blockquote>
    <h2>Trade-offs and failure modes</h2>
    <p><strong>Watch for:</strong> Draft does not automatically solve workflow approvals, distributed sagas or cross-system consistency. Draft action availability depends on BO setup and release.</p>
    <p><strong>Choose differently when:</strong> For a background import or one-step API command, non-draft RAP may be simpler.</p>
    <h2>Acceptance question</h2>
    <p>What is visible to external consumers before activation, and how are conflicting edits resolved?</p>
    <h2>References and scope</h2>
    <p>These are independent architecture explanations. Vendor sources establish platform capabilities; the design recommendation is a synthesis that still requires release, security and transaction-boundary verification in your own landscape.</p>
    <ul><li><a href="https://help.sap.com/docs/abap-cloud/abap-rap/draft-actions">RAP Draft Actions — SAP Help</a></li>
<li><a href="https://help.sap.com/docs/abap-cloud/abap-rap/documentation-overview-24e7a732427d42c2acdfab907eda26e7">ABAP RAP documentation overview — SAP Help</a></li></ul>
    <h2>Continue the design</h2>
    <ul><li><a href="/atlas/sap/development-patterns/behavior-rule-placement/">SDP-10 · RAP Validation vs Determination vs Action</a></li>
<li><a href="/atlas/sap/development-patterns/managed-rap-business-object/">SDP-08 · Managed RAP Business Object</a></li><li><a href="/atlas/sap/development-patterns/design-review/">Design-review template</a></li></ul>
    <p><a href="/atlas/sap/development-patterns/">← Back to the Pattern Library</a></p>
  </div>
</article>
{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
