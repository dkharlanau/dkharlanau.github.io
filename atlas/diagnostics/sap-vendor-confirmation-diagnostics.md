---
layout: default
title: "SAP Vendor Confirmation Diagnostics"
description: "A diagnostic frame for missing, late, or inconsistent vendor order confirmations in SAP MM."
permalink: /atlas/diagnostics/sap-vendor-confirmation-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Procurement
concept_type: diagnostic guide
sap_area: "MM purchasing"
business_process: Procure to pay
status: needs_verification
verified: false
level: 1
last_reviewed: 2026-06-13
author: Dzmitryi Kharlanau
tags:
  - sap-mm
  - procurement
  - vendor-confirmation
  - diagnostics
related:
  - /atlas/diagnostics/sap-purchase-order-creation-diagnostics/
  - /atlas/diagnostics/sap-source-determination-diagnostics/
  - /atlas/diagnostics/sap-purchasing-info-record-diagnostics/
  - /atlas/diagnostics/sap-goods-receipt-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Vendor Confirmation Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP vendor confirmation diagnostics</h1>
    <p class="note-subtitle">Track why a supplier confirmation is missing, late, or does not match the purchase order.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM purchasing</dd></div>
      <div><dt>Reviewed</dt><dd>13 Jun 2026</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Vendor confirmations are the bridge between a purchase order promise and a planned goods receipt. When confirmations are missing or inconsistent, MRP dates shift, inbound deliveries cannot be created, and downstream planning becomes unreliable. The diagnostic goal is to determine whether the gap is in supplier behavior, PO setup, message output, or confirmation processing.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Purchase order item shows no confirmation despite supplier agreeing to a delivery date.</li>
      <li>Confirmation quantity differs from ordered quantity without explanation.</li>
      <li>Confirmation date is later than the requested delivery date and MRP is out of sync.</li>
      <li>Inbound delivery cannot be created because confirmation is missing or incomplete.</li>
      <li>Multiple confirmations exist for the same PO item and create confusion.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Confirmation control not set:</strong> the PO item does not require or allow confirmations.</li>
      <li><strong>Supplier did not respond:</strong> outbound message was not sent, not received, or ignored.</li>
      <li><strong>Confirmation entered against wrong item:</strong> manual confirmation references a different PO or item.</li>
      <li><strong>Quantity or date mismatch:</strong> supplier confirmed partial quantity or a date outside tolerance.</li>
      <li><strong>MRP type behavior:</strong> MRP does not consider confirmations because of lot-sizing or procurement type settings.</li>
      <li><strong>IDoc or EDI failure:</strong> inbound confirmation message failed validation and was not posted.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>ME23N — PO item confirmation tab and history.</li>
      <li>ME38 / ME39 — maintain and display schedule agreements or confirmation history.</li>
      <li>ME2N / ME2S — PO list filtered by confirmation status.</li>
      <li>SOST — send requests for output messages.</li>
      <li>WE02 / WE05 — IDoc status for inbound confirmations.</li>
      <li>MD04 / MD05 — stock/requirements list to see MRP impact.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>EKEK / EKES</strong> — vendor confirmation header and items.</li>
      <li><strong>EKPO</strong> — purchase order items.</li>
      <li><strong>EKET</strong> — delivery schedules.</li>
      <li><strong>T163</strong> — confirmation control keys.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Confirm whether the PO item is configured to expect confirmations.</li>
      <li>Check whether a confirmation was entered manually or via EDI/IDoc.</li>
      <li>Compare ordered quantity, confirmed quantity, and delivered quantity.</li>
      <li>Verify the confirmation date against the requested delivery date and MRP result.</li>
      <li>If EDI is used, check IDoc status and partner profile settings.</li>
      <li>Escalate to procurement or supplier contact if the issue is supplier behavior.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Adjust confirmation control key on the PO or info record if confirmations are required.</li>
      <li>Resend the PO or order acknowledgment to the supplier.</li>
      <li>Correct or delete a wrongly entered confirmation.</li>
      <li>Update MRP if the confirmed date requires a new planned order or stock transfer.</li>
      <li>Fix EDI mapping or partner profile if inbound confirmations fail validation.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Vendor confirmation problems sit at the boundary of system setup, supplier behavior, and message integration. Always check the confirmation control key first, then the message flow, then the supplier response.</p>

    <h2>Related diagnostics</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-purchase-order-creation-diagnostics/">SAP Purchase Order Creation Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-source-determination-diagnostics/">SAP Source Determination Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-goods-receipt-diagnostics/">SAP Goods Receipt Diagnostics</a></li>
    </ul>
  </div>
</article>

{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
