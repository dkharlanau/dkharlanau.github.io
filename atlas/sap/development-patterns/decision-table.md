---
layout: default
title: "Decision Table / Rules as Data | SAP Development Patterns"
description: "When the business owns many combinations, stop encoding them as nested IF statements. Practical SAP ABAP, RAP, CAP architecture pattern."
permalink: /atlas/sap/development-patterns/decision-table/
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
  <li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Decision Table / Rules as Data</li>
</ol></nav>
<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">SDP-06 · ABAP OO · Architecture vocabulary</p>
    <h1>Decision Table / Rules as Data</h1>
    <p class="note-subtitle">When the business owns many combinations, stop encoding them as nested IF statements.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>
  <div class="note-body">
    <h2>The situation</h2>
    <p>Business rules depend on country, distribution channel, risk class and transaction type. The developer has to read 40 branches to find one decision.</p>
    <h2>The mental model</h2>
    <pre><code>Normalized input → ordered decision table → result + rule/version trace</code></pre>
    <p><strong>Use when:</strong> Rule matrices, defaults, exception tables, value derivation and configuration that changes independently of technical code.</p>
    <h2>How to apply it</h2>
    <ol>
<li>Write a complete input/output contract and list rules in a table visible to business reviewers.</li>
<li>Specify priority, overlap resolution, default behavior and effective dates.</li>
<li>Validate decision-table content before transport or activation; reject ambiguities.</li>
<li>Log a non-sensitive rule ID and version for decisions that need explanation.</li>
</ol>
    <h2>A small SAP example</h2>
    <p>For a synthetic partner function, a table determines a billing route by partner type and channel. A reviewer can inspect the table without decoding ABAP control flow.</p>
    <p><strong>Implementation sketch</strong> — conceptual only. This is not a compiled SAP sample, an API availability guarantee, or a production-ready implementation.</p>
    <pre><code>| Partner type | Channel | Result | Priority |
| Payer        | Online  | R01    | 10       |
| Payer        | Any     | R02    | 20       |

First-match is valid only when precedence is explicit and validated.</code></pre>
    <h2>Say it in a design review</h2>
    <blockquote><p>Make this a Decision Table. The rule combinations belong in governed data; the evaluator should stay boring.</p></blockquote>
    <h2>Trade-offs and failure modes</h2>
    <p><strong>Watch for:</strong> A customizing table with no conflict checking is only a hidden IF statement. Also keep technical validation and authority checks in code.</p>
    <p><strong>Choose differently when:</strong> Choose Strategy when behavior changes algorithmically, not just the mapping of input combinations to outputs.</p>
    <h2>Acceptance question</h2>
    <p>Can we explain a result by rule ID, and can we detect conflicting or uncovered combinations before deployment?</p>
    <h2>References and scope</h2>
    <p>These are independent architecture explanations. Vendor sources establish platform capabilities; the design recommendation is a synthesis that still requires release, security and transaction-boundary verification in your own landscape.</p>
    <ul><li><a href="https://help.sap.com/docs/abap-cloud/abap-cloud-background-concepts-and-overview/abap-cloud-development-model">ABAP Cloud development model — SAP Help</a></li></ul>
    <h2>Continue the design</h2>
    <ul><li><a href="/atlas/sap/development-patterns/strategy-policy/">SDP-02 · Strategy / Policy Resolver</a></li>
<li><a href="/atlas/sap/development-patterns/anti-corruption-layer/">SDP-04 · Anti-Corruption Layer (ACL)</a></li><li><a href="/atlas/sap/development-patterns/design-review/">Design-review template</a></li></ul>
    <p><a href="/atlas/sap/development-patterns/">← Back to the Pattern Library</a></p>
  </div>
</article>
{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
