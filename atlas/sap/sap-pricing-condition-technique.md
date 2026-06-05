---
layout: default
title: "SAP Pricing Condition Technique"
description: "A conservative explanation of how SAP pricing condition technique works and where it usually breaks."
permalink: /atlas/sap/sap-pricing-condition-technique/
atlas_section: sap
domain: SAP operations
subdomain: Sales pricing
concept_type: support diagnostic
sap_area: "SD pricing"
business_process: Order to cash
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau

tags:
  - order-to-cash
  - sap-sd
  - pricing
related:
  - /atlas/sap/sap-pricing-procedure-debugging/
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
    <li aria-current="page">SAP Pricing Condition Technique</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas SAP Note</p>
    <h1>SAP pricing condition technique</h1>
    <p class="note-subtitle">How SAP assembles a sales price from conditions, and why the chain breaks more often than individual settings.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Order to cash</dd></div>
      <div><dt>SAP area</dt><dd>Sales pricing</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until condition technique claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>SAP pricing does not store a single "price" for a transaction. It builds the final price dynamically from a sequence of conditions: base price, discounts, surcharges, freight, tax, and statistical values. Each condition is found through a chain of logic that involves the pricing procedure, condition types, access sequences, and condition records. A failure at any step in the chain can produce an unexpected price, even when every individual setting appears correct.</p>

    <h2>Why it matters</h2>
    <p>Support teams often approach pricing issues by checking one condition at a time. This works when the problem is a missing condition record, but it fails when the problem is higher in the chain: the wrong pricing procedure is determined, the access sequence does not match the document context, or a manual change has hidden the automatic result. Understanding the full chain helps the support team ask better questions and collect better evidence.</p>

    <h2>The condition chain</h2>
    <ul>
      <li><strong>Pricing procedure determination:</strong> the system selects a pricing procedure based on the sales area, document type, and customer. If the wrong procedure is selected, every condition inside it may be irrelevant.</li>
      <li><strong>Condition types:</strong> within the procedure, each condition type represents a specific price element such as base price, discount, or tax. The sequence of condition types matters because later conditions can reference earlier ones.</li>
      <li><strong>Access sequences:</strong> each condition type uses an access sequence to search for valid condition records. The access sequence defines which key combinations to try, in what order.</li>
      <li><strong>Condition records:</strong> the actual price values are stored in condition records, which are valid for specific key combinations, date ranges, and scales. A missing or expired record is the most common cause of a missing price element.</li>
      <li><strong>Calculation rules:</strong> once condition values are found, calculation rules determine how they combine into the final price. A rule may reference subtotals, statistical values, or other conditions.</li>
    </ul>

    <h2>Common failure patterns</h2>
    <p>Pricing issues often come from mismatched context. A condition record exists but is not valid for the pricing date of the document. An access sequence tries key combinations in an order that does not match the business expectation. A copied document retains old pricing that no longer reflects current master data. A manual price change overrides the automatic result, and users forget to check whether the automatic result was ever found.</p>

    <h2>Diagnostic questions</h2>
    <ul>
      <li>Which pricing procedure is being used for this document, and is it the expected one?</li>
      <li>Which condition type is missing or unexpected?</li>
      <li>Does the relevant condition record exist, and is it valid for the document's pricing date and key combination?</li>
      <li>Is the issue an automatic pricing failure, a manual override, or a copy-control behavior?</li>
      <li>Has the document been copied from another document that had different pricing?</li>
      <li>Are there custom enhancements that modify pricing behavior beyond standard condition technique?</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>A useful pricing ticket should include the document number, item, pricing date, expected condition, actual condition result, customer and material context, and evidence of which step in the condition chain failed. Avoid asking a configuration team to "fix pricing" without showing which part of the chain is broken.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page explains the condition technique conceptually. It is not a configuration guide for pricing procedures, condition types, access sequences, or calculation schemas. It does not cover release-specific transaction paths or table names. For configuration details, consult SAP Help Portal and system-specific documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-pricing-procedure-debugging/">SAP Pricing Procedure Debugging</a></li>
      <li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a></li>
      <li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
