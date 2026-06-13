---
layout: default
title: "SAP Delivery Block Analysis"
description: "A conservative diagnostic frame for delivery blocks in SAP sales documents."
permalink: /atlas/diagnostics/sap-delivery-block-analysis/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Delivery control
concept_type: diagnostic guide
sap_area: "SD delivery"
business_process: Order to cash
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau

tags:
  - order-to-cash
  - sap-sd
  - diagnostics
  - delivery
related:
  - /atlas/diagnostics/sap-sales-order-block-diagnosis/
  - /atlas/diagnostics/sap-credit-management-diagnostics/
  - /atlas/concepts/order-to-cash/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Delivery Block Analysis</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP delivery block analysis</h1>
    <p class="note-subtitle">A first-pass structure for understanding why a sales order cannot create a delivery.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Order to cash</dd></div>
      <div><dt>SAP area</dt><dd>Sales delivery</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until delivery block behavior is verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>A delivery block prevents the creation of a delivery document for a sales order. The block may be automatic — set by the system when a condition is not met — or manual, set by a user for a specific business reason. The support goal is to identify which block is active, whether it is at header or item level, and what condition must change before delivery can proceed.</p>

    <h2>Why it matters</h2>
    <p>Delivery blocks are often confused with shipping blocks or general order blocks. A delivery block operates upstream: it stops the delivery document from being created at all. A shipping block operates downstream: it stops goods issue on a delivery that already exists. Treating them as the same problem leads to wrong diagnostic paths and incorrect escalation.</p>

    <h2>First split</h2>
    <ul>
      <li><strong>Credit-related delivery block:</strong> the customer's exposure exceeds the credit limit, and the system prevents delivery as a financial control.</li>
      <li><strong>Incompletion block:</strong> required data is missing from the order, and the incompletion procedure prevents delivery until the data is provided.</li>
      <li><strong>Manual block:</strong> a user has set a block for a business reason such as a customer request to hold shipment, a quality concern, or a pending approval.</li>
      <li><strong>Custom rule block:</strong> an enhancement, workflow, or interface has set a block based on landscape-specific logic.</li>
      <li><strong>Item-level block:</strong> some order lines can deliver while others are held, enabling partial shipment.</li>
    </ul>

    <h2>Diagnostic questions</h2>
    <ul>
      <li>Is the block at order header level or item level?</li>
      <li>What is the block reason, and is it automatic or manual?</li>
      <li>If automatic — what triggered it: credit check, incompletion, or another system condition?</li>
      <li>If manual — who set it, when, and for what business reason?</li>
      <li>Are multiple blocks active? Removing one may reveal another underneath.</li>
      <li>Does the user attempting to release the block have the appropriate authorization?</li>
      <li>Is the order visible in the delivery due list, or is it filtered out because of the block?</li>
    </ul>

    <h2>Common failure patterns</h2>
    <p>Many delivery block tickets arise from layered controls. A credit block may be released by a credit manager, but an incompletion block or manual hold may still prevent delivery. Users often report "the block is gone but delivery still fails" because they addressed only the top layer. Another common issue is custom delivery creation programs that do not check for item-level blocks, creating a control gap.</p>

    <h2>Support takeaway</h2>
    <p>Before attempting to release a delivery block, confirm the block type, the business reason it was set, and whether other blocks are also active. A useful delivery block ticket should include the order number, the block reason, the level (header or item), any recent changes to the order or customer master data, and the business outcome the user expected.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a delivery block configuration guide. It does not cover the technical setup of block reason codes, authorization objects, or copy control behavior. It does not replace the judgment of operations or finance teams who own the underlying business rules.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>

    <h2>Next diagnostic steps</h2>
    <ul>
      <li><a href="/atlas/maps/order-to-cash-map/">Order to Cash Map</a> — use this map to place the delivery block in the wider order-to-cash workflow.</li>
      <li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a> — start here if the block originates at order level rather than delivery level.</li>
      <li><a href="/atlas/diagnostics/sap-billing-block-analysis/">SAP Billing Block Analysis</a> — check this when delivery exists but billing is stopped.</li>
      <li><a href="/atlas/diagnostics/sap-delivery-processing-diagnostics/">SAP Delivery Processing Diagnostics</a> — go here when delivery creation succeeds but downstream processing fails.</li>
      <li><a href="/atlas/diagnostics/sap-credit-management-diagnostics/">SAP Credit Management Diagnostics</a> — use this if the block reason points to credit exposure.</li>
    </ul>

    <h2>Practical checklist</h2>
    <div markdown="1">
- [ ] Collect sales order, delivery block reason, header/item level, and goods issue status. **Synthetic example:** order 1234567890, block "Manual hold" at header level.

- [ ] Check VL10/VA02 for the active block reason and whether other blocks are layered underneath.

- [ ] Confirm if the block is automatic (credit/incompletion) or manual, and document who set it.

- [ ] Verify the delivery due list filters are not hiding the order because of the block.

- [ ] Document the expected shipment date and the business approver who can release.

- [ ] Safety limit: do not remove a manual hold without confirmation from the team that placed it.
</div>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a></li>
      <li><a href="/atlas/diagnostics/sap-credit-management-diagnostics/">SAP Credit Management Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-delivery-processing-diagnostics/">SAP Delivery Processing Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-returns-processing-diagnostics/">SAP Returns Processing Diagnostics</a></li>
      <li><a href="/atlas/concepts/order-to-cash/">Order to Cash</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
