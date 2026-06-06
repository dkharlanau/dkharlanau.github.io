---
layout: default
title: "SAP Purchase Requisition Diagnostics"
description: "A conservative diagnostic frame for purchase requisition issues in SAP MM."
permalink: /atlas/diagnostics/sap-purchase-requisition-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Procurement and logistics
concept_type: diagnostic guide
sap_area: "MM purchasing"
business_process: Procure to pay
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau

tags:
  - procure-to-pay
  - sap-mm
  - diagnostics
  - purchasing
related:
  - /atlas/diagnostics/sap-purchase-order-creation-diagnostics/
  - /atlas/diagnostics/sap-release-strategy-diagnostics/
  - /atlas/diagnostics/sap-source-determination-diagnostics/
  - /atlas/sap/sap-mm-procurement-overview/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Purchase Requisition Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP purchase requisition diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a purchase requisition cannot be created, approved, or converted to a purchase order.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM purchasing</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until PR behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Purchase requisition is the first document in the procure-to-pay chain. It captures internal demand but does not yet commit the organization to a supplier. When a PR is blocked, cannot be created, or fails conversion, the support goal is to identify whether the issue is in master data, account assignment, sourcing, release strategy, or user authorization.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>ME51N fails to save or shows a hard error.</li>
      <li>PR is created but cannot be converted to PO (ME59N or ME21N).</li>
      <li>PR remains in status 'release strategy active' and cannot be approved.</li>
      <li>MRP-generated PR has wrong plant, quantity, or delivery date.</li>
      <li>PR account assignment is rejected during posting or conversion.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Master data issue:</strong> material not extended to plant, supplier blocked, or purchasing organization mismatch.</li>
      <li><strong>Account assignment error:</strong> cost center, WBS element, or GL account is invalid or not open for posting.</li>
      <li><strong>Release strategy block:</strong> the PR value or material group triggers an approval path that is not complete.</li>
      <li><strong>Source determination failure:</strong> no valid info record, source list, or quota arrangement exists for automatic sourcing.</li>
      <li><strong>Authorization issue:</strong> the user lacks authorization to create PRs for the plant, material group, or account assignment type.</li>
      <li><strong>MRP parameter issue:</strong> lot size, safety stock, or planning horizon produced an unexpected PR quantity or date.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>ME53N — display PR and check status, account assignment, and source of supply.</li>
      <li>ME59N log — automatic PO creation rejection reasons.</li>
      <li>ME54N — PR release status.</li>
      <li>MD04 / MD05 — MRP list to see how the PR was generated.</li>
      <li>SU53 — authorization check after a failed transaction.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>EBAN / EBKN</strong> — PR header and items.</li>
      <li><strong>EKKO / EKPO</strong> — PO header and items (for converted PRs).</li>
      <li><strong>AUFK</strong> — WBS / internal order master.</li>
      <li><strong>CSKS</strong> — cost center master.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the PR number and the exact error or status that blocks progress.</li>
      <li>Check ME53N for PR details: material, plant, quantity, account assignment, and source of supply.</li>
      <li>Verify master data: material plant extension, supplier status, and purchasing organization.</li>
      <li>Check release status if the PR is blocked for approval.</li>
      <li>Check MRP parameters if the PR was system-generated and has unexpected values.</li>
      <li>Test manual PO creation (ME21N) from the PR to isolate conversion issues.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Correct the account assignment if the cost center or WBS element is wrong.</li>
      <li>Extend the material to the plant or unblock the supplier master.</li>
      <li>Complete the release strategy approval if the PR is blocked.</li>
      <li>Create or update the source of supply if automatic sourcing fails.</li>
      <li>Adjust MRP parameters if system-generated PRs are consistently wrong.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>PR issues are usually upstream master data or account assignment problems. A useful ticket should include: PR number, material, plant, error message, account assignment, and whether the issue is isolated or recurring.</p>

    <h2>MRP exception handling</h2>
    <p>MRP exceptions are messages that indicate planning problems requiring human intervention. When MRP generates unexpected purchase requisitions, the support goal is to identify whether the exception is a master data issue, a demand signal problem, or a planning parameter mismatch.</p>
    <ul>
      <li><strong>Check MD04 / MD05:</strong> the MRP list shows exception messages per material and plant. Common messages include stockout (01), excess (02), late receipt (03), and early receipt (07).</li>
      <li><strong>Check MRP parameters:</strong> lot size, safety stock, reorder point, and procurement type in the material master may produce PRs that do not match business intent.</li>
      <li><strong>Check demand signals:</strong> sales orders, planned independent requirements, or reservations may have changed after the last MRP run, creating new exceptions.</li>
      <li><strong>Check supply signals:</strong> purchase orders, production orders, or planned orders may have been delayed or cancelled, causing MRP to propose new PRs.</li>
      <li><strong>Check MRP controller assignment:</strong> the material may be assigned to an MRP controller who is not monitoring exceptions for that group.</li>
    </ul>
    <p>A useful MRP exception ticket should include: material number, plant, exception message number, MRP run date, the PR or planned order number if one was created, and whether the exception is isolated or affects a group of materials.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a PR configuration guide. It does not cover MRP logic, approval workflow design, or catalog integration. It does not replace SAP's purchasing documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-purchase-order-creation-diagnostics/">SAP Purchase Order Creation Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-release-strategy-diagnostics/">SAP Release Strategy Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-source-determination-diagnostics/">SAP Source Determination Diagnostics</a></li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP Mm Procurement Overview</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
