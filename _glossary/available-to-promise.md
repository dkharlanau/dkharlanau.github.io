---
layout: default
title: "Available to Promise (ATP)"
description: "Definition of Available to Promise (ATP) in SAP and enterprise operations."
permalink: /atlas/glossary/available-to-promise/
last_modified_at: 2026-06-13
defined_term: "Available to Promise"
term_code: "ATP"
related_terms:
  - /atlas/glossary/order-to-cash/
status: needs_verification
verified: false
robots: noindex, follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/glossary/">Glossary</a></li>
    <li aria-current="page">Available to Promise</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Glossary term</p>
    <h1>Available to Promise (ATP)</h1>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <div class="note-body">
    <p><strong>Available to Promise (ATP)</strong> is the logic that determines whether a requested quantity can be promised to a customer at a requested date. It balances current stock, expected receipts, production, and existing commitments.</p>

    <h2>Why it matters</h2>
    <p>ATP is often mistaken for inventory on hand. In SAP, ATP checks rules-based availability that may exclude blocked stock, include inbounds, or respect allocations.</p>

    <h2>Related terms</h2>
    <ul>
      <li><a href="/atlas/glossary/order-to-cash/">Order to Cash (O2C)</a></li>
      <li><a href="/atlas/concepts/sap-atp-is-not-inventory/">Atlas concept: ATP is not inventory</a></li>
    </ul>
  </div>
</article>
