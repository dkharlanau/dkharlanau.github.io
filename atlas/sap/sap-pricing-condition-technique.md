---
layout: default
title: "SAP Pricing Condition Technique"
description: "A clear explanation of how SAP S/4HANA Sales builds a price from pricing procedures, condition types, access sequences, and condition records."
permalink: /atlas/sap/sap-pricing-condition-technique/
atlas_section: sap
domain: SAP operations
subdomain: Sales pricing
concept_type: SAP concept
sap_area: "SD pricing"
business_process: Order to cash
status: needs_verification
verified: false
last_reviewed: 2026-09-22
author: Dzmitryi Kharlanau

tags:
  - order-to-cash
  - sap-sd
  - pricing
related:
  - /atlas/sap/sap-pricing-procedure-debugging/
  - /atlas/sap/sales-domain/
  - /atlas/concepts/order-to-cash/
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
    <p class="note-subtitle">SAP does not look up one final sales price. It builds the result from a controlled sequence of price elements.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Order to cash</dd></div>
      <div><dt>SAP area</dt><dd>Sales pricing</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until pricing claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>A price is assembled, not stored as one answer</h2>
    <p>In SAP S/4HANA Sales, the value we call “the price” is usually the result of several pricing conditions. A base price may be followed by customer discounts, material discounts, surcharges, freight, taxes, statistical conditions, or other price elements. The pricing procedure defines which elements belong to the calculation and in which sequence SAP processes them.</p>

    <p>This is the core idea of the condition technique: separate the <strong>structure of the calculation</strong> from the <strong>business values</strong> used inside that structure. The pricing procedure provides the structure. Condition types describe the individual price elements. Access sequences define how SAP searches for automatically maintained values. Condition records contain those values for specific key combinations and validity periods.</p>

    <h2>Pricing procedure: the calculation framework</h2>
    <p>Before SAP can calculate the price, it needs the relevant pricing procedure. In standard sales pricing, procedure determination uses the sales area together with pricing attributes from the sales document type and customer. The selected procedure then gives SAP an ordered set of steps to process.</p>

    <p>A procedure can contain more than simple amounts. A step can be mandatory, statistical, manual-only, subject to a requirement, or connected to a subtotal or calculation rule. This is why two procedures containing the same-looking condition types can still produce different results.</p>

    <h2>Condition type: what kind of price element is this?</h2>
    <p>A condition type gives meaning to a pricing line. It can represent a base price, discount, surcharge, freight amount, tax, or another commercial element. The condition type also carries control information such as the calculation type and whether automatic record access is used.</p>

    <p>Not every condition type needs an access sequence. Some conditions are designed for manual entry, and some are used for technical or statistical purposes. It is therefore better to think of the condition type as a pricing role rather than as a simple pointer to a table.</p>

    <h2>Access sequence: where should SAP look?</h2>
    <p>When a condition type uses automatic determination, its access sequence defines the search strategy. The sequence contains accesses to condition tables with different key combinations. A company might maintain a very specific price for one customer and material, a broader price for a customer group, and a general price for the material. The access sequence determines which combinations SAP tries and in which order.</p>

    <p>The order matters because a more specific record is usually intended to win over a more general one. Once a valid record is found according to the configured access logic, SAP can use its value and scales for the condition.</p>

    <h2>Condition record: the business value</h2>
    <p>The condition record stores the maintained value for a key combination and validity period. This is where a base price of 100 EUR, a 5% customer discount, or another maintained condition value can live. The record can also contain scales, so the rate changes when quantity or another scale basis crosses a threshold.</p>

    <p>Dates are therefore part of pricing logic, not an administrative detail. The same customer and material can legitimately receive different prices on two documents if the pricing dates fall into different condition-record validity periods.</p>

    <h2>Putting the pieces together</h2>
    <p>Suppose we sell 100 units of a material. SAP first determines the pricing procedure for the document. The procedure reaches the base-price condition type. Its access sequence searches from specific to broader keys until a valid record is found. The rate is copied into the document and the relevant scale is applied. The procedure then continues with discounts, surcharges, taxes, and other configured steps until the result is complete.</p>

    <p>A manual condition or copied price can change that story. So can a requirement, formula, exclusion rule, pricing date, unit conversion, or copy-control pricing type. These mechanisms do not contradict the condition technique; they are part of the larger pricing framework around it.</p>

    <h2>Why the model matters</h2>
    <p>Without this structure, pricing looks like a collection of tables and condition codes. With it, the logic becomes easier to follow: <strong>which procedure was selected, which condition type is being processed, how does it search, which record was found, and how is the value calculated?</strong></p>

    <p>The separate <a href="/atlas/sap/sap-pricing-procedure-debugging/">pricing debugging page</a> uses that model for incident analysis. This page stays with the concept itself so the two articles do not repeat the same troubleshooting checklist.</p>

    <h2>Sources</h2>
    <ul>
      <li>SAP Learning — <a href="https://learning.sap.com/courses/configuring-pricing-in-sap-s-4hana-sales/introducing-the-condition-technique_dce0f313-dee6-470e-8851-3f1773cb5d45">Introducing the Condition Technique</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/19d48293097f4a2589433856b034dfa5/13617e81352644c9ad42ea1b40637258.html">Pricing Procedure Subtotal Lines</a>.</li>
    </ul>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-pricing-procedure-debugging/">SAP Pricing Procedure Debugging</a></li>
      <li><a href="/atlas/sap/sales-domain/">Sales — SAP S/4HANA Domain</a></li>
      <li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
