---
layout: default
title: "SAP Tax Determination Diagnostics"
description: "A conservative diagnostic frame for tax code, jurisdiction, and condition record issues in SAP."
permalink: /atlas/diagnostics/sap-tax-determination-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Procurement and logistics
concept_type: diagnostic guide
sap_area: "SD / MM tax"
business_process: Order to cash / procure to pay
status: needs_verification
verified: false
level: 1
author: Dzmitryi Kharlanau
tags:
  - diagnostics
  - sap-ams
  - tax
related:
  - /atlas/diagnostics/sap-purchase-order-diagnostics/
  - /atlas/diagnostics/sap-sales-order-block-diagnosis/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Tax Determination Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP tax determination diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why SAP does not determine the expected tax code, rate, or jurisdiction.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Order to cash / procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>SD / MM tax</dd></div>
      <div><dt>Indexing</dt><dd>Noindex, review candidate</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>SAP determines tax based on a combination of tax classification, jurisdiction, tax code, and condition records. A wrong tax rate or missing tax line usually points to missing or expired condition records, incorrect tax codes, or organizational setup. The diagnostic task is to trace the determination path from the document to the condition record and confirm the legal and jurisdictional settings.</p>
    <p>This guide covers tax determination for sales and procurement documents, not tax reporting or statutory filing.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Sales order or purchase order shows a tax code different from the expected one.</li>
      <li>Tax amount is zero even though the transaction is taxable.</li>
      <li>Error: "Tax code does not exist" or "Tax jurisdiction code is invalid."</li>
      <li>Condition record is found but the rate is outdated after a tax law change.</li>
      <li>Intercompany transaction uses the wrong tax classification.</li>
      <li>Invoices fail accounting interface due to tax account determination errors.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Missing tax condition record:</strong> the tax procedure does not find a record for the tax code and jurisdiction combination.</li>
      <li><strong>Wrong tax code in master data:</strong> customer, vendor, or material tax classification points to an unintended tax code.</li>
      <li><strong>Jurisdiction mismatch:</strong> the ship-to, plant, or tax departure location resolves to the wrong jurisdiction code.</li>
      <li><strong>Tax procedure misconfiguration:</strong> the procedure assigned to the country or company code lacks the expected condition type.</li>
      <li><strong>Expired or inactive condition record:</strong> the validity period does not cover the document date.</li>
      <li><strong>Tax indicator conflict:</strong> tax-relevant indicators on the material or business partner override expected determination.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li><strong>VK13</strong> — display condition records for sales tax conditions.</li>
      <li><strong>FTXP</strong> — tax code properties and percentage rates per tax code.</li>
      <li><strong>OB40</strong> — tax account determination posting keys and G/L accounts.</li>
      <li><strong>FV11 / FV13</strong> — create/display tax condition records for FI.</li>
      <li><strong>VA03 / ME23N</strong> — check the document's tax code, jurisdiction, and pricing analysis.</li>
      <li><strong>XD03 / MK03</strong> — customer/vendor tax classification by country.</li>
      <li><strong>MM03</strong> — material tax indicator by plant and sales organization.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>A003, A053, A056</strong> — tax condition tables (examples; actual tables depend on procedure).</li>
      <li><strong>T007A</strong> — tax codes.</li>
      <li><strong>T007B</strong> — tax code properties.</li>
      <li><strong>KONP</strong> — condition item data (rates and values).</li>
      <li><strong>TAXNUMBER</strong> — tax jurisdiction code derivation logic via function modules.</li>
      <li><strong>SKB1</strong> — G/L account company code data for tax account posting.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the document type, company code, country, tax code, and jurisdiction from the error.</li>
      <li>Open the document condition screen and run pricing analysis to see which condition was found.</li>
      <li>Check VK13 or FV13 for the relevant tax condition record and validity period.</li>
      <li>Verify the tax code in FTXP and the tax procedure assignment in the company code/country.</li>
      <li>Check customer/vendor tax classification in XD03/MK03 and material tax indicator in MM03.</li>
      <li>Confirm jurisdiction code derivation using the ship-to/plant address and tax departure rules.</li>
      <li>Check OB40 if the issue is account determination rather than rate determination.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Create or extend the missing tax condition record for the affected jurisdiction and validity period.</li>
      <li>Correct the tax classification on the customer, vendor, or material master.</li>
      <li>Update the tax code rate in FTXP after a statutory change.</li>
      <li>Fix the jurisdiction code derivation or address master data if the location is wrong.</li>
      <li>Escalate to the tax team if the issue affects statutory reporting or intercompany tax policy.</li>
    </ul>

    <h2>What to capture first</h2>
    <p>Capture the company code, country, tax procedure, tax code, jurisdiction code, document number, material number, customer/vendor number, exact error message, and the expected versus actual tax rate.</p>

    <h2>Escalation signals</h2>
    <ul>
      <li>Tax rates are incorrect for a whole country or company code after a legal change.</li>
      <li>Multiple documents posted with the wrong tax code and require correction.</li>
      <li>Jurisdiction codes are missing or inconsistent across plants and ship-to addresses.</li>
      <li>Tax account determination errors block invoice posting for many transactions.</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame for tax determination in operational documents, not a tax law or statutory reporting guide. It does not cover Vertex, Avalara, or other external tax engines unless the failure is inside the SAP integration point.</p>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
