---

layout: default
title: "SAP ATP Is Not Inventory"
description: "A practical explanation of why SAP available-to-promise is customer commitment logic, not a simple inventory count."
permalink: /atlas/concepts/sap-atp-is-not-inventory/
last_modified_at: 2026-08-11
atlas_section: concepts
domain: SAP operations
subdomain: Sales and fulfillment
concept_type: business concept
sap_area: "SD availability check / ATP"
business_process: Order to cash
status: reviewed
verified: true
level: 2
last_reviewed: 2026-05-06
author: Dzmitryi Kharlanau

tags:
  - order-to-cash
  - sap-sd
  - diagnostics
related:
  - /atlas/concepts/order-to-cash/
  - /atlas/diagnostics/sap-sales-order-block-diagnosis/
  - /services/sap-ams-consulting/
  - /atlas/concepts/sap-stock-exists-not-promisable/
  - /atlas/maps/order-to-cash-map/
robots: index,follow
sitemap: true
---

**Sources:** [SAP scope of availability check](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/d0960a564b52fb37e10000000a44147b.html), [SAP ATP checking rules](https://help.sap.com/docs/SAP_S4HANA_CLOUD/32da8359c8ee4e8b8e8c5e15cacba5aa/10e9ab50bc27406296b0b78eff3f9fba.html), and [SAP supply protection integration](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/e541e617043545a0bb60e5067d037046.html).
**Date checked:** 2026-08-11
**Confidence:** high for the checking-group/rule/scope relationship; medium for the result of any customer-specific ATP design.
**Related page/topic:** /atlas/concepts/sap-stock-exists-not-promisable/
**Practical implication:** Compare the ATP result with its included supply, demand, date, location, and prioritization rules—not with a standalone stock total.
**Tags:** order-to-cash, sap-sd, atp, availability-check, inventory, diagnostics

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/concepts/">Concepts</a></li>
    <li aria-current="page">SAP ATP Is Not Inventory</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Concept</p>
    <h1>SAP ATP is not inventory</h1>
    <p class="note-subtitle">ATP is promise logic. Inventory is stock visibility. Confusing the two creates bad support tickets and bad customer commitments.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Order to cash</dd></div>
      <div><dt>SAP area</dt><dd>Availability check / ATP</dd></div>
      <div><dt>Reviewed</dt><dd>06 May 2026</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Available-to-promise answers a commitment question: what quantity can the business responsibly promise to a customer, and when? It is not the same as asking what quantity exists physically in a plant or warehouse.</p>
    <p>Conceptually, an ATP result is shaped by eligible stock and receipts minus relevant requirements, evaluated for a date and document context. The actual categories are not universal: SAP uses the checking group and checking rule to determine the scope of availability check, including which stocks, receipts, issue elements, and requirements are considered.</p>

    <h2>Inventory question versus ATP question</h2>
    <table>
      <thead><tr><th>Inventory asks</th><th>ATP asks</th></tr></thead>
      <tbody>
        <tr><td>What quantity is recorded in this stock category and location?</td><td>What quantity can this demand confirm, on which date, under this checking scope?</td></tr>
        <tr><td>What is physically or financially present now?</td><td>Which current and future supply/requirements are eligible for the calculation?</td></tr>
        <tr><td>Where is the stock and what status does it have?</td><td>Can this document, customer, channel, or priority consume it?</td></tr>
        <tr><td>Has inventory changed?</td><td>Has supply, demand, allocation, protection, or the requested date changed?</td></tr>
      </tbody>
    </table>

    <h2>Why the distinction matters</h2>
    <p>Many support issues start with a user seeing stock in one report while the sales order confirms less than expected. The first useful question is not whether ATP is wrong. It is which supply and demand elements the check is allowed to consider for this material, location, requested date, and document context.</p>
    <p>Classic availability checking and advanced ATP do not have identical capabilities. Where advanced ATP functions are active, product allocation, supply protection, backorder processing, and alternative confirmation can further shape or reassign confirmations. Treat those as explicit controls, not invisible adjustments.</p>

    <h2>Diagnostic sequence</h2>
    <ol>
      <li>Capture the sales document/item, material, plant and storage location if applicable, requested quantity/date, and confirmed quantity/date.</li>
      <li>Identify the material checking group and the checking rule used by the business process. Confirm the resulting scope of check rather than relying on a remembered default.</li>
      <li>Review the eligible stock and receipt elements by date. Record which supply is included, excluded, delayed, or outside the check horizon.</li>
      <li>Review requirements and existing commitments that consume the available quantity. Use the same segment, location, and time context as the original check.</li>
      <li>If aATP is active, inspect product allocation, supply protection, backorder processing, or alternative confirmation evidence relevant to the item.</li>
      <li>Repeat or simulate the check only after the original context is reproducible, then compare the new confirmation with the documented cause.</li>
    </ol>

    <h2>Evidence for a useful ATP incident</h2>
    <ul>
      <li>Material, plant, storage location or stock segment, document/item, sales area, and requirement class where relevant.</li>
      <li>Requested and confirmed quantities/dates before and after the issue.</li>
      <li>Checking group, checking rule, scope of check, and availability result.</li>
      <li>Relevant supply and demand elements with dates, plus any active allocation or protection object.</li>
      <li>The inventory report and selection criteria used for comparison.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Do not diagnose ATP from stock quantity alone. Diagnose the promise result from its time, location, document, supply, demand, and prioritization context. Changing the scope may improve one confirmation while weakening other commitments, so configuration changes require process ownership and regression evidence.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page explains the diagnostic distinction; it is not a configuration recipe. Release level, classic versus advanced ATP, fulfilment sourcing, external order management, industry functions, and custom enhancements can change the applicable monitor and calculation. Confirm the active architecture before using transaction-level advice.</p>

    <h2>Official references</h2>
    <ul>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/d0960a564b52fb37e10000000a44147b.html">SAP: scope of availability check</a></li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/32da8359c8ee4e8b8e8c5e15cacba5aa/10e9ab50bc27406296b0b78eff3f9fba.html">SAP: checking rules for the product availability check</a></li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/e541e617043545a0bb60e5067d037046.html">SAP: supply protection integration with product availability check</a></li>
    </ul>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a></li>
      <li><a href="/atlas/concepts/sap-stock-exists-not-promisable/">SAP Stock Exists but Is Not Promisable</a></li>
      <li><a href="/atlas/maps/order-to-cash-map/">Order to Cash Map</a></li>
      <li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
