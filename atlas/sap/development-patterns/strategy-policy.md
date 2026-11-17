---
layout: default
title: "Strategy / Policy Resolver | SAP Development Patterns"
description: "Replace a forest of country, channel or organization CASE branches with named policies. Practical SAP ABAP, RAP, CAP architecture pattern."
permalink: /atlas/sap/development-patterns/strategy-policy/
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
  <li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Strategy / Policy Resolver</li>
</ol></nav>
<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">SDP-02 · ABAP OO · Architecture vocabulary</p>
    <h1>Strategy / Policy Resolver</h1>
    <p class="note-subtitle">Replace a forest of country, channel or organization CASE branches with named policies.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>
  <div class="note-body">
    <h2>The situation</h2>
    <p>Every new sales organization adds another nested IF. A rule for one organization accidentally changes behavior for another.</p>
    <h2>The mental model</h2>
    <pre><code>Context (org, company, scenario) → policy resolver → strategy implementation</code></pre>
    <p><strong>Use when:</strong> Organization-dependent enrichments, validation variants, sales-area mapping, calculation strategies and controlled exceptions.</p>
    <h2>How to apply it</h2>
    <ol>
<li>Define the variation point as an interface with a narrow method and stable input/output.</li>
<li>Resolve the implementation from validated context and an explicit priority or configuration rule.</li>
<li>Keep common behavior in the orchestrator; let strategies own only what genuinely varies.</li>
<li>Test default, overlapping selectors, missing selectors and every business-relevant strategy.</li>
</ol>
    <h2>A small SAP example</h2>
    <p>A synthetic master-data extension applies a different tax-number check in two regions. The policy resolver selects the region rule; the inbound processor never hardcodes the region identifiers.</p>
    <p><strong>Implementation sketch</strong> — conceptual only. This is not a compiled SAP sample, an API availability guarantee, or a production-ready implementation.</p>
    <pre><code>INTERFACE zif_tax_policy.
  METHODS check
    IMPORTING is_context TYPE zdev_context
    RETURNING VALUE(rs_result) TYPE zdev_result.
ENDINTERFACE.

&quot;Example contract only; Z types and implementations are illustrative.</code></pre>
    <h2>Say it in a design review</h2>
    <blockquote><p>Use Strategy with a Policy Resolver; the organization rule is a replaceable decision, not a new IF in the transport layer.</p></blockquote>
    <h2>Trade-offs and failure modes</h2>
    <p><strong>Watch for:</strong> Do not use dynamic class-name construction from untrusted customizing. Validate allowed implementations and define a deterministic fallback.</p>
    <p><strong>Choose differently when:</strong> If variation is only data (thresholds or mappings), use a governed decision table rather than a new subclass per value.</p>
    <h2>Acceptance question</h2>
    <p>Can a new region be added without modifying the processor? Do ambiguous matches fail predictably?</p>
    <h2>References and scope</h2>
    <p>These are independent architecture explanations. Vendor sources establish platform capabilities; the design recommendation is a synthesis that still requires release, security and transaction-boundary verification in your own landscape.</p>
    <ul><li><a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/ba879a6e2ea04d9bb94c7ccd7cdac446/e18eca61554345429f3a17e30955de8b.html">Managing Dependencies in ABAP Unit Testing — SAP Help</a></li>
<li><a href="https://help.sap.com/docs/abap-cloud/abap-cloud-background-concepts-and-overview/abap-cloud-development-model">ABAP Cloud development model — SAP Help</a></li></ul>
    <h2>Continue the design</h2>
    <ul><li><a href="/atlas/sap/development-patterns/decision-table/">SDP-06 · Decision Table / Rules as Data</a></li>
<li><a href="/atlas/sap/development-patterns/thin-entry-point/">SDP-01 · Thin Entry Point</a></li><li><a href="/atlas/sap/development-patterns/design-review/">Design-review template</a></li></ul>
    <p><a href="/atlas/sap/development-patterns/">← Back to the Pattern Library</a></p>
  </div>
</article>
{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
