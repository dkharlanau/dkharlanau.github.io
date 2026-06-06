---
layout: default
title: "SAP Service Entry Sheet Diagnostics"
description: "A conservative diagnostic frame for service entry sheet issues in SAP MM."
permalink: /atlas/diagnostics/sap-service-entry-sheet-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Procurement and logistics
concept_type: diagnostic guide
sap_area: "MM service procurement"
business_process: Procure to pay
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau

tags:
  - procure-to-pay
  - sap-mm
  - diagnostics
  - service-procurement
related:
  - /atlas/diagnostics/sap-purchase-order-creation-diagnostics/
  - /atlas/diagnostics/sap-invoice-verification-diagnostics/
  - /atlas/sap/sap-mm-procurement-overview/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Service Entry Sheet Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP service entry sheet diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a service cannot be accepted, entered, or invoiced.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM service procurement</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until service entry behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Service procurement uses a service entry sheet (SES) instead of a goods receipt to confirm that a service was performed. The SES is the basis for invoice verification and payment. When an SES cannot be created, accepted, or matched to an invoice, the support goal is to identify whether the issue is in the service master, PO item category, account assignment, or acceptance workflow.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>ML81N fails to create or accept a service entry sheet.</li>
      <li>SES shows status 'not accepted' even though the service was performed.</li>
      <li>Invoice verification (MIRO) cannot find the SES or shows quantity mismatch.</li>
      <li>Service PO item does not allow service entry sheet creation.</li>
      <li>SES account assignment differs from the PO and causes posting errors.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Wrong PO item category:</strong> the PO item is not configured for service procurement (D category).</li>
      <li><strong>Service master missing:</strong> the service number or description does not match the service master.</li>
      <li><strong>Quantity or value exceeded:</strong> the SES quantity or value exceeds the PO limit or tolerance.</li>
      <li><strong>Acceptance workflow block:</strong> the SES requires acceptance by a responsible person who has not yet approved it.</li>
      <li><strong>Account assignment mismatch:</strong> the SES account assignment (cost center, WBS) differs from the PO and is rejected.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>ML81N — service entry sheet creation and acceptance.</li>
      <li>ME23N — PO item category and service details.</li>
      <li>ME53N — PR service details if the PO was created from a PR.</li>
      <li>MIRO — invoice verification against SES.</li>
      <li>FBL1N — supplier line items for posted SES.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>ESLL / ESLH</strong> — service entry sheet items and header.</li>
      <li><strong>EKPO</strong> — PO items (item category and service flag).</li>
      <li><strong>RBKP / RSEG</strong> — invoice documents.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the PO number, service item, and the exact error during SES creation or acceptance.</li>
      <li>Check ME23N to confirm the PO item category is D (service) and the service details are correct.</li>
      <li>Verify the SES quantity and value do not exceed the PO limits.</li>
      <li>Check if the SES requires acceptance and who is the responsible person.</li>
      <li>Compare the account assignment on the SES with the PO account assignment.</li>
      <li>If invoice verification fails, check MIRO for the SES reference and quantity match.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Correct the PO item category to D if it was wrong.</li>
      <li>Adjust the SES quantity or value to match the PO limits.</li>
      <li>Route the SES to the correct responsible person for acceptance.</li>
      <li>Align the account assignment with the PO or update the PO if the original was wrong.</li>
      <li>If the service master is missing, create or update it before creating the SES.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>SES issues are usually PO setup or acceptance workflow gaps. A useful ticket should include: PO number, service item, SES number, error message, and whether the service was physically performed.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a service procurement configuration guide. It does not cover service master catalog design, acceptance workflow setup, or ML81N customization. It does not replace SAP's service procurement documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-purchase-order-creation-diagnostics/">SAP Purchase Order Creation Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-invoice-verification-diagnostics/">SAP Invoice Verification Diagnostics</a></li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP Mm Procurement Overview</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
