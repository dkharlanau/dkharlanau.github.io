---
layout: default
title: "Anti-Corruption Layer (ACL) | SAP Development Patterns"
description: "Translate legacy or external meanings once, before they reach core rules. Practical SAP ABAP, RAP, CAP architecture pattern."
permalink: /atlas/sap/development-patterns/anti-corruption-layer/
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
  <li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Anti-Corruption Layer (ACL)</li>
</ol></nav>
<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">SDP-04 · ABAP OO · Architecture vocabulary</p>
    <h1>Anti-Corruption Layer (ACL)</h1>
    <p class="note-subtitle">Translate legacy or external meanings once, before they reach core rules.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>
  <div class="note-body">
    <h2>The situation</h2>
    <p>A source has sales organization A100, the target uses B200, and business partners are identified differently. Raw external identifiers leak into every validation and update method.</p>
    <h2>The mental model</h2>
    <pre><code>External contract → validated mapping adapter → canonical domain model → target adapter</code></pre>
    <p><strong>Use when:</strong> IDoc migration, system-to-system extensions, BTP side-by-side apps, remote SAP APIs and value mapping with different vocabulary.</p>
    <h2>How to apply it</h2>
    <ol>
<li>Define an internal model with stable names and keys independent of the sender.</li>
<li>Translate identifiers, enumerations, units and field semantics at the inbound boundary.</li>
<li>Represent unmapped and ambiguous values as errors or explicit review outcomes, never as silent defaults.</li>
<li>Keep mapping version, source system and evidence traceable for reprocessing.</li>
</ol>
    <h2>A small SAP example</h2>
    <p>A synthetic customer feed carries a legacy distribution channel code. The ACL maps it to the target code and records which mapping version was applied. All later rules evaluate only canonical target values.</p>
    <p><strong>Implementation sketch</strong> — conceptual only. This is not a compiled SAP sample, an API availability guarantee, or a production-ready implementation.</p>
    <pre><code>source message → parse → schema checks → value mapping → canonical CustomerChange
                                                   ↓
                                       policy + target API</code></pre>
    <h2>Say it in a design review</h2>
    <blockquote><p>Put an Anti-Corruption Layer in front of the domain; source-system codes must not control downstream business rules.</p></blockquote>
    <h2>Trade-offs and failure modes</h2>
    <p><strong>Watch for:</strong> An ACL is not a reason to copy an entire legacy schema into a new platform. It is a translation boundary with explicit ownership.</p>
    <p><strong>Choose differently when:</strong> If both sides share a stable published contract and terminology, a lightweight adapter may be sufficient.</p>
    <h2>Acceptance question</h2>
    <p>Can a sender-side mapping change be implemented without touching the rule engine?</p>
    <h2>References and scope</h2>
    <p>These are independent architecture explanations. Vendor sources establish platform capabilities; the design recommendation is a synthesis that still requires release, security and transaction-boundary verification in your own landscape.</p>
    <ul><li><a href="https://cap.cloud.sap/docs/guides/services/consuming-services">CAP consuming remote services — SAP CAP documentation</a></li>
<li><a href="https://help.sap.com/saphelp_em900/helpdata/en/4a/66efbfcbff260be10000000a42189b/content.htm">Processing Inbound Master Data — SAP Help</a></li>
<li><a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/b5670aaaa2364a29935f40b16499972d/ef0301f6b908409c8e0802270a96a316.html">Working with ABAP for Cloud Development and Released APIs — SAP Help</a></li></ul>
    <h2>Continue the design</h2>
    <ul><li><a href="/atlas/sap/development-patterns/delta-aware-merge/">SDP-05 · Delta-Aware Merge / Patch Semantics</a></li>
<li><a href="/atlas/sap/development-patterns/strategy-policy/">SDP-02 · Strategy / Policy Resolver</a></li><li><a href="/atlas/sap/development-patterns/design-review/">Design-review template</a></li></ul>
    <p><a href="/atlas/sap/development-patterns/">← Back to the Pattern Library</a></p>
  </div>
</article>
{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
