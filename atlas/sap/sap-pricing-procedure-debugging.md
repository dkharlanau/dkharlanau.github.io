---

layout: default
title: "SAP Pricing Procedure Debugging"
description: "A conservative support frame for investigating pricing procedure issues in SAP sales documents."
permalink: /atlas/sap/sap-pricing-procedure-debugging/
atlas_section: sap
domain: SAP operations
subdomain: Sales pricing
concept_type: support diagnostic
sap_area: "SD pricing"
business_process: Order to cash
status: needs_verification
verified: false
last_reviewed: 2026-05-06
author: Dzmitryi Kharlanau

tags:
  - order-to-cash
  - sap-sd
  - diagnostics
related:
  - /atlas/concepts/order-to-cash/
  - /atlas/diagnostics/sap-sales-order-block-diagnosis/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Pricing Procedure Debugging</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas SAP Note</p>
    <h1>SAP pricing procedure debugging</h1>
    <p class="note-subtitle">A support-oriented way to narrow pricing issues without pretending every condition technique setup is identical.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Order to cash</dd></div>
      <div><dt>SAP area</dt><dd>Sales pricing</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until detailed SAP configuration claims are verified.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Pricing issues should be debugged as a chain, not as a guessing exercise. A sales document price is usually the result of procedure determination, condition types, access logic, condition records, dates, master data, manual changes, and calculation rules.</p>
    <p>The exact objects and transactions depend on the SAP release, configuration, and custom enhancements. This page is intentionally a diagnostic frame, not a configuration manual.</p>

    <h2>First-pass diagnostic path</h2>
    <ul>
      <li>Confirm the document context: sales area, document type, customer, material, date, currency, and pricing date.</li>
      <li>Check whether the expected pricing procedure is used for this context.</li>
      <li>Identify the missing or unexpected condition: base price, discount, surcharge, freight, tax, or statistical value.</li>
      <li>Review whether the relevant condition record exists, is valid on the pricing date, and matches the access keys used in this landscape.</li>
      <li>Separate automatic pricing failure from manual override, exclusion, copy-control, or custom enhancement behavior.</li>
    </ul>

    <h2>Common failure patterns</h2>
    <p>Many pricing tickets are not caused by one broken setting. They come from mismatched master data, wrong validity dates, copied documents retaining old pricing, access sequences that do not match the business scenario, or manual changes hiding the original automatic result.</p>

    <h2>Support takeaway</h2>
    <p>A useful pricing ticket should include the document number, item, pricing date, expected condition, actual condition result, customer/material context, and a screenshot or extract of the pricing analysis available in that system. Avoid asking a configurator to “fix pricing” without showing which part of the pricing chain failed.</p>

    <h2>Retail-specific: price discrepancy</h2>
    <p>In retail, price discrepancies often appear at the POS when the selling price in SAP does not match the price expected by the customer or the promotion price advertised.</p>
    <ul>
      <li><strong>Check condition record validity:</strong> VK13 or VK14 shows whether the price or discount condition record is valid for the store, article, and date. A record may have expired or not yet started.</li>
      <li><strong>Check POS price load timing:</strong> in many retail landscapes, prices are loaded to the POS system on a schedule. A price change in SAP may not reach the POS until the next load cycle.</li>
      <li><strong>Check store assortment inclusion:</strong> a promotion price may be valid only for stores in a specific assortment or cluster. The affected store may not be included.</li>
      <li><strong>Check tax or jurisdiction:</strong> the store may be in a different tax jurisdiction than expected, causing the final price to differ.</li>
      <li><strong>Check manual override:</strong> a user may have manually changed the price at the POS or in SAP, bypassing the automatic condition.</li>
    </ul>
    <p>A useful price discrepancy ticket should include: article number, store number, expected price, actual price, transaction date, promotion or campaign ID if applicable, and whether the issue affects one store or multiple stores.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a></li>
      <li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
