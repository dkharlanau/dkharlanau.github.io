---
layout: default
title: "SAP Plant Maintenance Order Diagnostics"
description: "A conservative diagnostic frame for PM orders, notifications, operations, and settlements in SAP."
permalink: /atlas/diagnostics/sap-plant-maintenance-order-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: SAP operations
concept_type: diagnostic guide
sap_area: "PM"
business_process: Plant maintenance
status: needs_verification
verified: false
level: 1
author: Dzmitryi Kharlanau
tags:
  - diagnostics
  - sap-ams
  - plant-maintenance
related:
  - /atlas/diagnostics/sap-background-job-diagnostics/
  - /atlas/diagnostics/sap-incident-triage-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Plant Maintenance Order Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP plant maintenance order diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a PM order cannot be created, released, confirmed, or settled.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Plant maintenance</dd></div>
      <div><dt>SAP area</dt><dd>PM</dd></div>
      <div><dt>Indexing</dt><dd>Noindex, review candidate</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Plant Maintenance orders structure repair and inspection work through operations, components, and settlement rules. A failure can occur at creation, release, confirmation, goods issue, or settlement. The diagnostic task is to read the order status network, check the underlying notification and component reservations, and confirm that settlement rules and cost centers are valid.</p>
    <p>This guide covers corrective and preventive maintenance orders, not project-based maintenance or investment programs.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>PM order cannot be created from a notification in IW31.</li>
      <li>Order is created but cannot be released due to missing data.</li>
      <li>Time confirmation in IW41 fails because an operation is not released.</li>
      <li>Material components cannot be issued to the order.</li>
      <li>Settlement fails in KO88 or through the periodic settlement job.</li>
      <li>Costs remain on the order after technical completion.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Missing order type or planning plant:</strong> the order type is not configured for the planning plant.</li>
      <li><strong>Incomplete settlement rule:</strong> no valid cost receiver is defined for the order.</li>
      <li><strong>Operation or component status:</strong> operations are not released or components are not available.</li>
      <li><strong>Reservation or stock issue:</strong> the component reservation is missing or stock is unavailable.</li>
      <li><strong>Cost center or WBS invalid:</strong> the settlement receiver is blocked or does not exist.</li>
      <li><strong>Notification not converted:</strong> the maintenance notification is still open and blocks order creation.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>IW33 / IW32</strong> — display/change PM order and status.</li>
      <li><strong>IW21 / IW22 / IW29</strong> — create/change/display maintenance notifications.</li>
      <li><strong>IW41 / IW42</strong> — time confirmations and cancellation.</li>
      <li><strong>MB25 / MB51</strong> — reservation and goods movement history.</li>
      <li><strong>KO03 / KO88</strong> — order settlement rule and actual settlement.</li>
      <li><strong>IW49N</strong> — order and operation information system.</li>
      <li><strong>CO03</strong> — order cost analysis if the order is also a CO order.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>AUFK</strong> — order master data header.</li>
      <li><strong>AUFM</strong> — order material movements.</li>
      <li><strong>AFVC / AFVU</strong> — operations and user fields.</li>
      <li><strong>RESB</strong> — reservation items for order components.</li>
      <li><strong>JSTO / JEST</strong> — object status and status transitions.</li>
      <li><strong>COBRB</strong> — settlement rule distribution rules.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Open the order in IW33 and note the system status and user status.</li>
      <li>Check the notification in IW22 if the order was created from a notification.</li>
      <li>Review operations for release status and planned work values.</li>
      <li>Check component reservations in RESB or MB25 for missing stock or reservations.</li>
      <li>Verify settlement rules in KO03 and confirm the receiver cost center or WBS is valid.</li>
      <li>Attempt confirmation in IW41 and read the exact error message.</li>
      <li>Run settlement preview or actual settlement in KO88 if costs remain open.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Complete missing order header data and release the order.</li>
      <li>Release individual operations if they are required before confirmation.</li>
      <li>Create or correct the settlement rule with a valid cost center or WBS element.</li>
      <li>Check and correct component reservations or issue alternative material.</li>
      <li>Run settlement after technical completion to clear order costs.</li>
      <li>Convert or close the maintenance notification if it blocks order creation.</li>
    </ul>

    <h2>What to capture first</h2>
    <p>Capture the PM order number, notification number, order type, planning plant, current status, operation number, component material, exact error message, and whether the issue blocks creation, release, confirmation, goods issue, or settlement.</p>

    <h2>Escalation signals</h2>
    <ul>
      <li>Orders cannot be created for an entire order type or planning plant.</li>
      <li>Settlements fail across many PM orders after period-end close.</li>
      <li>Confirmations are blocked due to widespread operation status problems.</li>
      <li>Material reservations are missing for many orders after MRP or purchase requisition creation.</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame for operational PM orders, not a guide to plant maintenance strategy, investment programs, or equipment calibration. It does not cover customer service orders or project systems.</p>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
