---
layout: default
title: "Tax Code Determination in Purchasing & Invoice Receipt — SAP S/4HANA MM"
description: "A practical SAP MM guide to tax-code determination in purchase orders and Logistics Invoice Verification, including deductible, non-deductible, zero-rate, automatic determination, testing, and FI integration."
permalink: /labs/enterprise-context/procurement/tax-code-determination/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-10-01
hide_global_cta: true
tags:
  - sap-s4hana
  - sap-mm
  - procurement
  - tax
  - purchase-order
  - invoice-verification
  - miro
  - fi-integration
  - navs
  - input-tax
source_links:
  - title: "Maintaining Condition Records in MM"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8999cee59b7c44fdb53fbbb4d703f8e6/fd6ad0531d8b4208e10000000a174cb4.html"
  - title: "Condition Technique in Purchasing"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/db7fb65334e6b54ce10000000a174cb4.html"
  - title: "Determining Tax Code in Purchase Documents using Pricing Conditions"
    url: "https://help.sap.com/docs/SAP_S4HANA_CLOUD/164aaa06151b4106b7bc163efe97902a/f091163111194d8a97613ce747eff0df.html"
  - title: "Entering Invoices with Purchase Order Reference"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/8d6fb6531de6b64ce10000000a174cb4.html"
  - title: "Non-Deductible Input Tax"
    url: "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/14d1d1538cdf4608e10000000a174cb4.html"
last_reviewed: 2026-10-01
publication_wave: "logistics-search-wave-01"
review_method: "SAP primary sources + factual review + editorial rewrite"
search_intent: "SAP MM tax code determination in purchase orders and Logistics Invoice Verification"
# ai-discovery-managed:start
structured_data:
  type: TechArticle
primary_topic: "sap-procurement"
ai_sidecar: "/ai/pages/labs--enterprise-context--procurement--tax-code-determination.json"
entity_mentions:
  - "sap-s4hana"
semantic_links:
  - type: "parent_context"
    title: "Procurement Process & Decision Map — Enterprise Context Lab"
    url: "/labs/enterprise-context/procurement/"
  - type: "same_domain"
    title: "Material Valuation in Procurement — Standard Price, Moving Average Price and FI Postings"
    url: "/labs/enterprise-context/procurement/material-valuation/"
  - type: "related_topic"
    title: "SAP Business Partner — Roles, CVI and Organizational Data"
    url: "/labs/enterprise-context/business-partner/"
  - type: "related_topic"
    title: "SAP Decision Cards — Enterprise Context Lab"
    url: "/labs/enterprise-context/decisions/"
  - type: "related_topic"
    title: "Where Should Procurement Cost Ownership Live? — SAP Procurement Decision Card"
    url: "/labs/enterprise-context/decisions/account-assignment-ownership/"
  - type: "parent_context"
    title: "Labs — SAP Enterprise, Assurance, AI, Interview and Assessment"
    url: "/labs/"
# ai-discovery-managed:end
---
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/labs/">Labs</a></li>
    <li><a href="/labs/enterprise-context/">Enterprise Context</a></li>
    <li><a href="/labs/enterprise-context/procurement/">Procurement</a></li>
    <li aria-current="page">Tax Code Determination</li>
  </ol>
</nav>

<div class="research-canvas context-graph">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">SAP MM / Purchase Order → Invoice Verification → FI</p>
      <h1>The tax code is decided early.<br />The financial effect appears later.</h1>
      <p>In purchasing, the tax code belongs to the PO item and later becomes important during supplier invoice processing. A strong MM answer separates three questions: where the tax code came from, how SAP calculates tax, and where the amount is posted.</p>
      <a class="research-canvas__button" href="#memory-model">Learn the flow <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_balance</span>
    <div>
      <p><strong>Assessment rule:</strong> do not treat tax code determination, tax calculation, and tax account determination as one configuration step.</p>
      <p><strong>Runtime chain:</strong> purchasing context → tax code → PO → supplier invoice → Logistics Invoice Verification → FI tax posting.</p>
    </div>
    <a href="/labs/enterprise-context/procurement/">Open the Procurement decision map <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="memory-model" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Memory model</p>
      <h2>Remember five steps: Context → Code → Calculate → Verify → Post.</h2>
      <p>This model works better than memorising transactions because the exact configuration differs by country, release, and deployment model.</p>
    </header>
    <div class="ecg-memory-grid">
      <article class="ecg-memory-card"><span>01</span><strong>CONTEXT</strong><h3>What are we buying?</h3><p>Check company code, plant, supplier, material or service, receiving or consumption location, and country-specific tax rules.</p></article>
      <article class="ecg-memory-card"><span>02</span><strong>CODE</strong><h3>Which tax code applies?</h3><p>The PO item can receive a tax code manually, from a reference document, or through configured purchasing determination logic.</p></article>
      <article class="ecg-memory-card"><span>03</span><strong>CALCULATE</strong><h3>What does the code mean?</h3><p>The country tax procedure and tax-code settings define rate and deductible or non-deductible treatment.</p></article>
      <article class="ecg-memory-card"><span>04</span><strong>VERIFY</strong><h3>Does the supplier invoice agree?</h3><p>Logistics Invoice Verification compares the PO history and invoice data and calculates or checks the invoice tax result.</p></article>
      <article class="ecg-memory-card"><span>05</span><strong>POST</strong><h3>Where does tax go in FI?</h3><p>The accounting result depends on the tax code, tax type, account determination, and whether the tax is deductible.</p></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">60-second assessment answer</p>
      <h2>Explain the business flow before the configuration.</h2>
    </header>
    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">record_voice_over</span>
      <p><strong>Answer:</strong> “In SAP MM, the tax code is maintained or determined at purchase-order item level. It represents how the purchase should be treated for input tax. The PO carries this context into supplier invoice processing. In Logistics Invoice Verification, SAP checks the invoice amount, tax data, PO reference, and tolerances. For deductible input tax, the tax is normally posted separately to an input-tax account. For non-deductible input tax, the amount is not recoverable and can be assigned to the stock, expense, or asset value, or handled through a separate expense treatment depending on configuration. Automatic tax-code determination can use the purchasing condition technique, but the standard mechanism differs between classic/on-premise and current cloud scenarios. I first prove where the tax code came from, then tax calculation, then FI posting.”</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="po-tax-code" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Purchase order</p>
      <h2>The PO tax code is a purchasing decision with an FI consequence.</h2>
      <p>In a PO, the tax code is normally maintained on the item invoice data. It does not only store a percentage. It points to the tax treatment configured for the relevant country procedure.</p>
    </header>
    <div class="ecg-decision-columns">
      <div>
        <h3>Manual entry</h3>
        <p>A buyer can enter or change a valid tax code where the process and authorization allow it. This is simple, but it creates a control risk when users must remember tax rules.</p>
      </div>
      <div>
        <h3>Copied or referenced value</h3>
        <p>A tax code can be carried from a preceding purchasing object or reference context. Always check the current PO item instead of assuming the master record is the active source.</p>
      </div>
      <div>
        <h3>Automatic determination</h3>
        <p>Purchasing can use condition-based logic to derive a tax code from business fields such as country, company code, material group, plant, or other configured keys.</p>
      </div>
    </div>
    <p><strong>Important:</strong> changing a condition record or master-data value later does not automatically prove that an already-created PO item will be redetermined. For an existing PO, inspect the stored item value and trigger redetermination only through the supported process.</p>
  </section>

  <section class="research-canvas__inventory" id="automatic-determination" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Automatic determination</p>
      <h2>Classic/on-premise and cloud use related ideas, but not the same standard object.</h2>
      <p>This distinction matters in interviews. “Use NAVS” is not a universal S/4HANA answer.</p>
    </header>

    <div class="ecg-decision-columns">
      <div>
        <h3>Classic / on-premise purchasing</h3>
        <p>SAP documents automatic tax-code determination in MM using purchasing condition records. The standard condition type <strong>NAVS</strong> can carry an access sequence for tax-code determination, and tax condition records can be maintained with purchasing condition maintenance.</p>
        <ul>
          <li>Typical classic condition type: <strong>NAVS</strong></li>
          <li>Typical classic maintenance: <strong>MEK1 / MEK2</strong></li>
          <li>Tax code remains an FI tax object; MM condition logic determines which code to use.</li>
        </ul>
      </div>
      <div>
        <h3>S/4HANA Cloud Public Edition</h3>
        <p>Current SAP documentation describes the standard purchasing tax-code condition type <strong>TTX1</strong>. Configuration uses purchasing condition tables, access sequences, condition types, calculation schema, schema determination, and the <strong>Set Tax Rates (Purchasing)</strong> app.</p>
        <ul>
          <li>Standard cloud example: <strong>TTX1</strong></li>
          <li>Create condition records with validity dates and the required business key.</li>
          <li>Assign the required tax code to the condition entry.</li>
        </ul>
      </div>
      <div>
        <h3>Lead rule</h3>
        <p>First identify deployment and localization. Then inspect the active purchasing calculation schema and tax-determination condition. Do not copy a NAVS design into a cloud project or a cloud TTX1 example into every on-premise system.</p>
      </div>
    </div>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">schema</span>
      <p><strong>Condition-technique logic:</strong> condition table defines the key → access sequence searches the tables → tax-determination condition type uses the access sequence → calculation schema contains the condition → condition record returns the tax code.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="invoice-verification" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Logistics Invoice Verification</p>
      <h2>MIRO is not just “copy PO and post”.</h2>
      <p>With PO reference, SAP proposes invoice items from the purchasing document and PO history. Invoice tax data still has to be correct for the supplier document and the active tax procedure.</p>
    </header>
    <div class="ecg-determination-list">
      <article class="ecg-determination-detail">
        <header><div><span>01</span><small>reference</small></div><h3>Allocate the invoice</h3><p class="ecg-question">Which PO, delivery, service entry sheet, or supplier context does the invoice belong to?</p></header>
        <div class="ecg-decision-columns">
          <div><h4>Input</h4><p>Supplier invoice header and reference document.</p></div>
          <div><h4>System proposal</h4><p>Relevant PO items and purchasing history are proposed.</p></div>
          <div><h4>Lead check</h4><p>Confirm that the correct PO item and tax context were selected.</p></div>
        </div>
      </article>
      <article class="ecg-determination-detail">
        <header><div><span>02</span><small>tax</small></div><h3>Check tax data</h3><p class="ecg-question">Does the invoice tax match the intended purchase treatment?</p></header>
        <div class="ecg-decision-columns">
          <div><h4>Input</h4><p>Tax code, tax amount, base amount, invoice date/tax date, and localization fields where required.</p></div>
          <div><h4>System action</h4><p>SAP calculates or checks tax using the configured tax procedure and invoice data.</p></div>
          <div><h4>Lead check</h4><p>Compare PO tax code, supplier invoice, and calculated tax. A correct PO does not automatically prove a correct invoice.</p></div>
        </div>
      </article>
      <article class="ecg-determination-detail">
        <header><div><span>03</span><small>post</small></div><h3>Post the invoice</h3><p class="ecg-question">Where should the tax amount be posted?</p></header>
        <div class="ecg-decision-columns">
          <div><h4>Deductible</h4><p>Usually a separate input-tax line is posted to the configured tax account.</p></div>
          <div><h4>Non-deductible</h4><p>The non-recoverable amount can be distributed to the related stock, expense, or asset line, or handled through a separate expense treatment, depending on tax-code configuration.</p></div>
          <div><h4>Lead check</h4><p>Separate “wrong tax rate” from “wrong tax account” and “wrong deductibility treatment”.</p></div>
        </div>
      </article>
    </div>
  </section>

  <section class="research-canvas__inventory" id="scenarios" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Three core scenarios</p>
      <h2>Use business meaning, not only percentages.</h2>
      <p>The codes below are examples. Actual tax-code names are customer- and country-specific.</p>
    </header>
    <div class="ecg-decision-columns">
      <div>
        <h3>1. Zero-rate or exempt purchase</h3>
        <p>Example code: <strong>V0</strong>. The calculated tax amount can be zero, but the code can still be important for legal classification, reporting, and validation.</p>
        <p><strong>Do not say:</strong> “0% means no tax configuration is needed.”</p>
      </div>
      <div>
        <h3>2. Deductible input tax</h3>
        <p>Example: 18% input tax that can be recovered from the tax authority. At invoice posting, the tax is typically separated from the material or expense value and posted to an input-tax account.</p>
        <p><strong>Typical invoice shape:</strong> GR/IR or expense debit + input-tax debit → supplier credit.</p>
      </div>
      <div>
        <h3>3. Non-deductible input tax</h3>
        <p>The business cannot recover all or part of the tax. SAP can assign the non-deductible amount to the related G/L or asset line, which may increase inventory, expense, or asset value depending on the process and configuration.</p>
        <p><strong>Do not say:</strong> “non-deductible tax always posts at GR and never appears separately.” The exact accounting behavior depends on configuration and process.</p>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="fi-configuration" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Configuration stack</p>
      <h2>Know which layer owns the decision.</h2>
    </header>
    <div class="ecg-control-stack">
      <article><span>1</span><h3>Country tax procedure</h3><p>Defines the tax calculation framework used for the country. This is an FI/global tax layer, not an MM-only setting.</p><strong>Question: which procedure is active for the company-code country?</strong></article>
      <article><span>2</span><h3>Tax code</h3><p>Defines the tax treatment, rate-related settings, and deductible or non-deductible behavior.</p><strong>Classic reference: FTXP.</strong></article>
      <article><span>3</span><h3>Tax account determination</h3><p>Maps tax transaction/account keys to G/L accounts.</p><strong>Classic reference: OB40.</strong></article>
      <article><span>4</span><h3>Purchasing tax-code determination</h3><p>Determines which tax code should be proposed in the PO based on purchasing condition logic.</p><strong>Classic/on-premise: NAVS + purchasing condition records. Cloud: TTX1-based configuration.</strong></article>
      <article><span>5</span><h3>Invoice Verification defaults</h3><p>Controls default or proposal behavior for tax codes and how tax data is entered and checked during supplier invoice processing.</p><strong>Question: what can MIRO propose or change in this scenario?</strong></article>
    </div>
  </section>

  <section class="research-canvas__inventory" id="testing" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Testing</p>
      <h2>Test determination, calculation, and posting separately.</h2>
      <p>A green MIRO posting is not enough. The test should prove the source of the tax code and the accounting result.</p>
    </header>
    <div class="ecg-input-grid">
      <article><span>TEST 1</span><h3>Zero-rate / exempt</h3><ul><li>Create PO with the intended zero/exempt tax code.</li><li>Post the supplier invoice with PO reference.</li><li>Confirm zero tax amount and correct legal/reporting code.</li><li>Confirm there is no unexpected tax G/L posting.</li></ul></article>
      <article><span>TEST 2</span><h3>Deductible input tax</h3><ul><li>Create PO with the deductible input-tax code.</li><li>Post GR if the scenario requires it.</li><li>Post invoice and compare supplier tax with SAP calculation.</li><li>Confirm the separate input-tax line and configured tax account.</li></ul></article>
      <article><span>TEST 3</span><h3>Non-deductible input tax</h3><ul><li>Create PO with the non-deductible tax code.</li><li>Check whether purchasing pricing shows the non-deductible component where configured.</li><li>Post GR and invoice.</li><li>Confirm where the non-recoverable amount was assigned: stock, expense, asset, or separate expense account.</li></ul></article>
      <article><span>TEST 4</span><h3>Automatic tax-code determination</h3><ul><li>Maintain a condition record for a known business key.</li><li>Create a PO without manually forcing the tax code.</li><li>Confirm the determined code and trace the successful condition access.</li><li>Change one driver, such as plant or material group, and confirm the expected new result.</li></ul></article>
      <article><span>TEST 5</span><h3>Wrong supplier invoice tax</h3><ul><li>Create a PO with a valid tax code.</li><li>Enter a supplier invoice with a different tax amount or code.</li><li>Observe calculation, messages, tolerances, and allowed correction behavior.</li><li>Confirm the final FI tax posting after correction.</li></ul></article>
      <article><span>TEST 6</span><h3>Existing PO after rule change</h3><ul><li>Create a PO and record its tax code.</li><li>Change the relevant tax condition record.</li><li>Re-open the old PO and create a new PO.</li><li>Prove whether and when redetermination occurs instead of assuming both documents change automatically.</li></ul></article>
    </div>
  </section>

  <section class="research-canvas__inventory" id="diagnostics" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Diagnostics</p>
      <h2>Find the first wrong state.</h2>
    </header>
    <div class="ecg-determination-list">
      <article class="ecg-determination-detail">
        <header><div><span>!</span><small>PO</small></div><h3>Tax code is missing in the PO</h3></header>
        <div class="ecg-decision-columns">
          <div><h4>Check first</h4><p>Active purchasing schema, tax-determination condition, access sequence, condition record, key fields, validity dates, and manual-entry rules.</p></div>
          <div><h4>Then</h4><p>Check whether a reference document should have supplied the value.</p></div>
          <div><h4>Avoid</h4><p>Creating a broad fallback condition record before you know which access failed.</p></div>
        </div>
      </article>
      <article class="ecg-determination-detail">
        <header><div><span>!</span><small>MIRO</small></div><h3>PO tax code is correct, invoice tax is wrong</h3></header>
        <div class="ecg-decision-columns">
          <div><h4>Check first</h4><p>Invoice tax code, tax amount/base, invoice date or tax date, PO reference, and manual changes.</p></div>
          <div><h4>Then</h4><p>Check country/localization rules and invoice-verification settings.</p></div>
          <div><h4>Avoid</h4><p>Changing PO determination when the first divergence starts inside invoice processing.</p></div>
        </div>
      </article>
      <article class="ecg-determination-detail">
        <header><div><span>!</span><small>FI</small></div><h3>Rate is correct, but G/L account is wrong</h3></header>
        <div class="ecg-decision-columns">
          <div><h4>Check first</h4><p>Tax code, tax type, account/transaction key, and tax account determination.</p></div>
          <div><h4>Then</h4><p>Check whether the posting is deductible, non-deductible, or mixed.</p></div>
          <div><h4>Avoid</h4><p>Changing MM condition records to repair a pure tax-account mapping problem.</p></div>
        </div>
      </article>
    </div>
  </section>

  <section class="research-canvas__inventory" id="transaction-codes" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Classic transaction references</p>
      <h2>Useful for support, but not the architecture.</h2>
      <p>These are common classic/on-premise references. Fiori apps and configuration activities can replace or complement them in newer deployments.</p>
    </header>
    <div class="ecg-input-grid">
      <article><span>FI</span><h3>FTXP</h3><p>Create or maintain tax codes for sales and purchases.</p></article>
      <article><span>FI</span><h3>OB40</h3><p>Maintain tax account determination.</p></article>
      <article><span>MM</span><h3>ME21N</h3><p>Create purchase order and inspect item invoice/tax data.</p></article>
      <article><span>MM</span><h3>MEK1 / MEK2</h3><p>Create or change purchasing condition records, including classic tax-code determination records where configured.</p></article>
      <article><span>MM</span><h3>MIGO</h3><p>Post goods receipt where the procurement scenario requires a GR.</p></article>
      <article><span>MM-IV</span><h3>MIRO / MIR4</h3><p>Enter and display supplier invoices in Logistics Invoice Verification.</p></article>
      <article><span>FI</span><h3>FB03</h3><p>Display the accounting document and verify tax lines and accounts.</p></article>
    </div>
  </section>

  <section class="research-canvas__inventory" id="assessment-drills" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead assessment drills</p>
      <h2>Short questions that test understanding.</h2>
    </header>
    <div class="research-route-list">
      <a href="#automatic-determination"><span>Q1</span><strong>Is NAVS always the standard tax-code determination condition in S/4HANA?</strong><small>No. It is a classic/on-premise MM pattern. Current S/4HANA Cloud documentation uses TTX1-based purchasing tax-code determination.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#scenarios"><span>Q2</span><strong>What is the difference between deductible and non-deductible input tax?</strong><small>Deductible tax is recoverable and normally posted to an input-tax account. Non-deductible tax is not recoverable and becomes part of cost or expense according to configuration.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#invoice-verification"><span>Q3</span><strong>If the PO tax code is correct, can MIRO still be wrong?</strong><small>Yes. Invoice tax data, dates, amounts, manual changes, localization, and invoice-verification settings can create a later divergence.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#diagnostics"><span>Q4</span><strong>The rate is right but the tax G/L is wrong. Where do you look?</strong><small>Tax code and FI tax-account determination, not purchasing tax-code determination.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">warning</span>
    <div>
      <p><strong>Localization boundary:</strong> tax procedures, tax-code names, rates, reporting rules, jurisdiction logic, and legal treatment are country-specific.</p>
      <p>Examples such as V0, V1, 18%, VST, or NVV are learning examples or classic references. Confirm the target-country design before using them in a project.</p>
    </div>
    <a href="/labs/enterprise-context/tax/">Review tax across SD, MM and FI <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Primary references</p>
      <h2>Current SAP Help baseline.</h2>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8999cee59b7c44fdb53fbbb4d703f8e6/fd6ad0531d8b4208e10000000a174cb4.html" target="_blank" rel="noopener"><span>SAP</span><strong>Maintaining Condition Records in MM</strong><small>NAVS, access sequence, MEK1/MEK2, and automatic tax-code determination in classic MM.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/db7fb65334e6b54ce10000000a174cb4.html" target="_blank" rel="noopener"><span>SAP</span><strong>Condition Technique</strong><small>Purchasing condition categories, including NAVS and non-deductible input tax.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/164aaa06151b4106b7bc163efe97902a/f091163111194d8a97613ce747eff0df.html" target="_blank" rel="noopener"><span>SAP</span><strong>Determining Tax Code in Purchase Documents using Pricing Conditions</strong><small>Current cloud configuration with TTX1, condition tables, access sequence, schema, and Set Tax Rates (Purchasing).</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/8d6fb6531de6b64ce10000000a174cb4.html" target="_blank" rel="noopener"><span>SAP</span><strong>Entering Invoices with Purchase Order Reference</strong><small>How Logistics Invoice Verification proposes and processes PO-based invoice items.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/14d1d1538cdf4608e10000000a174cb4.html" target="_blank" rel="noopener"><span>SAP</span><strong>Non-Deductible Input Tax</strong><small>How non-recoverable tax can be assigned to expense, G/L, and asset line items.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
