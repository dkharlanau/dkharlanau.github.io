---
layout: default
title: "SAP Contract and Scheduling Agreement Diagnostics"
description: "Conservative diagnostic frame for SAP outline agreement, contract, and scheduling agreement release-order and delivery-schedule failures."
permalink: /atlas/diagnostics/sap-contract-scheduling-agreement-diagnostics/
last_modified_at: 2026-06-13
atlas_section: diagnostics
domain: SAP AMS
subdomain: Procure to pay
concept_type: diagnostic guide
sap_area: "Materials Management / Outline agreements"
business_process: "Procure to pay"
status: needs_verification
verified: false
level: 1
last_reviewed: 2026-06-13
author: Dzmitryi Kharlanau
tags:
  - sap-ams
  - p2p
  - procurement
  - outline-agreement
  - scheduling-agreement
related:
  - /atlas/diagnostics/sap-source-determination-diagnostics/
  - /atlas/diagnostics/sap-purchase-order-creation-diagnostics/
  - /atlas/diagnostics/sap-purchasing-info-record-diagnostics/
  - /atlas/sap/sap-mm-procurement-overview/
robots: noindex,follow
sitemap: false
---

**Source:** Practical pattern derived from SAP support experience. Not yet verified against public SAP documentation.
**Date checked:** 2026-06-13
**Confidence:** medium
**Related page/topic:** /atlas/maps/procure-to-pay-map/
**Practical implication:** Use the outline agreement number, target quantity, validity period, and release status to decide whether the failure is in sourcing, quantities, conditions, or release strategy before opening a support ticket.
**Tags:** sap-ams, p2p, procurement, outline-agreement, scheduling-agreement

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Contract and Scheduling Agreement Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP contract and scheduling agreement diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a contract release order or scheduling agreement delivery schedule cannot be created or processed.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>Materials Management / Outline agreements</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until claims are verified against public SAP documentation.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Outline agreements — central contracts, value contracts, and scheduling agreements — control pricing, quantities, and delivery schedules over a longer period. A failure usually appears downstream: a release order cannot be created, a scheduling agreement forecast is missing, or the system pulls the wrong price. The diagnostic goal is to separate agreement-level problems from release-order or PO-level problems.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Release order against a contract fails or does not adopt the agreed price/conditions.</li>
      <li>Scheduling agreement delivery schedule is missing, late, or contains the wrong quantity.</li>
      <li>ME38 cannot create or update scheduling agreement releases.</li>
      <li>Cumulative quantity on the agreement exceeds the target quantity and no further releases are possible.</li>
      <li>Source list or info record points to an outline agreement, but ME21N cannot use it.</li>
      <li>Outline agreement validity has expired or was not extended.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Agreement not released:</strong> the outline agreement itself is still blocked by a release strategy or the release status is incomplete.</li>
      <li><strong>Target quantity exhausted:</strong> cumulative release quantity has reached or exceeded the target quantity on the agreement.</li>
      <li><strong>Validity gap:</strong> the release date falls outside the agreement validity period.</li>
      <li><strong>Conditions missing:</strong> the price or conditions from the agreement are not adopted because of missing info record or condition record.</li>
      <li><strong>Document type mismatch:</strong> the release order document type or item category is not configured for the agreement type.</li>
      <li><strong>Schedule-line issue:</strong> MRP or manual schedule lines for a scheduling agreement were not generated or were deleted.</li>
      <li><strong>Organizational mismatch:</strong> plant, purchasing organization, or supplier on the release differs from the agreement.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>ME31N / ME32N / ME33N</strong> — contract display/change: validity, target quantity, cumulative quantity, release status.</li>
      <li><strong>ME31L / ME32L / ME33L</strong> — scheduling agreement display/change: validity, schedule lines, release status.</li>
      <li><strong>ME38</strong> — maintain scheduling agreement delivery schedules / releases.</li>
      <li><strong>ME28 / ME29N</strong> — release strategy for outline agreements.</li>
      <li><strong>ME21N / ME23N</strong> — release order creation and display.</li>
      <li><strong>ME01 / ME03</strong> — source list; confirm the agreement is the valid source.</li>
      <li><strong>ME11 / ME12 / ME13</strong> — purchasing info record and conditions.</li>
      <li><strong>MK03 / MKVZ</strong> — vendor master blocks and organizational assignments.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>EKKO / EKPO</strong> — outline agreement and release order header and items.</li>
      <li><strong>EKET</strong> — scheduling agreement schedule lines.</li>
      <li><strong>EKES</strong> — vendor confirmations for scheduling agreements.</li>
      <li><strong>EKAB</strong> — release documentation for outline agreements.</li>
      <li><strong>EINA / EINE</strong> — purchasing info record general and org-level data.</li>
      <li><strong>KONV / KONP</strong> — pricing conditions (where available).</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the outline agreement number, type (contract vs. scheduling agreement), and the failing release or schedule.</li>
      <li>Check the agreement validity period and release status in ME33N/ME33L.</li>
      <li>Compare target quantity with cumulative released quantity; confirm the release quantity does not exceed the remaining amount.</li>
      <li>Verify the source list or info record points to the correct agreement and period.</li>
      <li>Attempt the release order or schedule line creation and capture the exact error message.</li>
      <li>Check conditions on the release order to see whether the agreement price was adopted.</li>
      <li>If the symptom is integration-related, check the IDoc or output status for the release.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Release the outline agreement if it is blocked by release strategy.</li>
      <li>Extend the agreement validity or increase the target quantity after procurement confirms the commercial terms.</li>
      <li>Re-create missing schedule lines in ME38 or via MRP.</li>
      <li>Maintain or correct the source list and info record references to the agreement.</li>
      <li>Correct the document type or item category on the release order.</li>
      <li>Escalate to procurement or finance if price/conditions need renegotiation.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Outline agreement failures are often quantity, validity, or sourcing problems rather than system errors. Collect the agreement number, target and cumulative quantities, validity dates, and the exact release error before escalating.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a configuration guide for outline agreement types, release strategies, or condition techniques. It does not cover Ariba, SRM, or supplier self-service scenarios.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>

    <h2>Next diagnostic steps</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-source-determination-diagnostics/">SAP Source Determination Diagnostics</a> — if no valid source of supply is found.</li>
      <li><a href="/atlas/diagnostics/sap-purchase-order-creation-diagnostics/">SAP Purchase Order Creation Diagnostics</a> — if the release order itself cannot be created.</li>
      <li><a href="/atlas/diagnostics/sap-purchasing-info-record-diagnostics/">SAP Purchasing Info Record Diagnostics</a> — if price or conditions are not adopted.</li>
    </ul>

    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a></li>
      <li><a href="/atlas/maps/procure-to-pay-map/">Procure-to-Pay Map</a></li>
    </ul>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
