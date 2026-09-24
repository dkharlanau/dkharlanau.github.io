---
layout: default
title: "Supplier Payment Readiness — SAP S/4HANA Lead Lab"
description: "A practical SAP S/4HANA guide to supplier payment readiness: Business Partner and company-code data, due dates, payment blocks, bank details, payment methods, and the AP line item that reaches the payment proposal."
permalink: /labs/enterprise-context/procurement/suppliers/readiness/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-24
last_reviewed: 2026-09-24
hide_global_cta: true
career_impact: mapped
career_skills:
  - logistics-p2p
  - logistics-master-data
tags:
  - sap-s4hana
  - supplier-master
  - business-partner
  - accounts-payable
  - payment-terms
  - payment-block
  - supplier-bank-data
  - procure-to-pay
semantic_links:
  - type: "parent_topic"
    title: "Supplier Payments & AP"
    url: "/labs/enterprise-context/procurement/suppliers/"
  - type: "related_topic"
    title: "Business Partner"
    url: "/labs/enterprise-context/business-partner/"
  - type: "related_topic"
    title: "Master Data"
    url: "/labs/enterprise-context/master-data/"
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/procurement/">Procurement</a></li><li><a href="/labs/enterprise-context/procurement/suppliers/">Suppliers</a></li><li aria-current="page">Readiness</li></ol></nav>

<div class="research-canvas context-graph">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Supplier cluster / payment readiness</p>
      <h1>The payment run sees<br />the payable you created.</h1>
      <p>Automatic payment processing does not repair a supplier invoice. It evaluates an AP item that already has an owner, amount, due date, payment controls and, where required, recipient bank data. When an invoice is missing from a proposal, the useful first question is not “what is wrong with the payment run?” but “what state did this payable reach before the run started?”</p>
      <a class="research-canvas__button" href="#readiness-map">Trace the payable <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Supplier readiness model">
      <p>Readiness boundary</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Master</strong><small>Defaults and payment identity</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Item</strong><small>The posted AP state</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Proposal</strong><small>Selection starts here</small></div>
      <em>Master data supplies defaults. The posted line item is the evidence.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_tree</span>
    <p><strong>Keep the layers separate.</strong> In S/4HANA, the Business Partner is the central object, but supplier data still has different scopes. General BP data can hold bank details; the Supplier (Financial Accounting) role carries company-code accounting and payment data; the Supplier (Purchasing) role carries purchasing-organization data. A value that is correct for purchasing is not automatically the value that controls an AP payment.</p>
    <a href="/labs/enterprise-context/business-partner/">Open Business Partner <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="readiness-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Where the payment state comes from</p>
      <h2>Read master data as defaults, then read the document.</h2>
      <p>SAP separates information that identifies the supplier from information that controls accounting for one company code. Posting turns those defaults and document inputs into a concrete supplier line item. That line item is what payment processing must evaluate.</p>
    </header>
    <div class="ecg-decision-columns">
      <div>
        <h3>Business Partner</h3>
        <p>The BP identifies the organization and can carry bank-account information used when a payment method needs recipient bank details. The bank account belongs to the payee side of the payment; it is not the same thing as the paying company’s house-bank selection.</p>
      </div>
      <div>
        <h3>Supplier company-code data</h3>
        <p>The Supplier (Financial Accounting) role is extended to a company code. This is where SAP documents accounting data such as the reconciliation account and payment data such as terms of payment. Payment methods can also be maintained as supplier payment defaults.</p>
      </div>
      <div>
        <h3>Posted supplier item</h3>
        <p>The accounting document has its own payment-relevant state. Payment terms, baseline and due-date information, payment method and payment block can determine what happens to this specific item. If a document value differs from a master-data default, diagnose the document that actually exists rather than assuming the master record still describes it.</p>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">The AP item</p>
      <h2>“Posted” and “ready to pay” are different states.</h2>
      <p>A valid accounting document can still be intentionally unavailable to automatic payment processing. Four checks explain most readiness questions before payment-run configuration becomes relevant.</p>
    </header>
    <div class="ecg-control-stack">
      <article><span>1</span><h3>Is the item still open?</h3><p>Start with the supplier line item. If it has already been cleared, the investigation has moved beyond payment selection. If it is open, keep the document number, company code, supplier and currency as the case identity.</p><strong>Prove the current accounting state first.</strong></article>
      <article><span>2</span><h3>When is it payable?</h3><p>Payment terms and the baseline date drive the item’s discount and net-due dates. The practical question is not whether the invoice “looks old enough”; it is which dates SAP calculated for this item and why.</p><strong>Read the dates from the payable.</strong></article>
      <article><span>3</span><h3>Is payment deliberately blocked?</h3><p>A payment block can be a real control, not bad data. Logistics Invoice Verification can post an invoice and block it for payment when configured tolerance limits are exceeded. Workflow or a manual decision can also leave a payment block in place.</p><strong>Resolve the reason before removing the block.</strong></article>
      <article><span>4</span><h3>Can the chosen method be executed?</h3><p>A line item can specify a payment method, or the payment program can choose from allowed methods when none is fixed on the item. The method can require data such as valid recipient bank details and must be allowed by the payment configuration and run parameters.</p><strong>Method eligibility comes before bank selection.</strong></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Invoice origin</p>
      <h2>The same AP symptom can have a different upstream owner.</h2>
      <p>A direct FI supplier invoice and a PO-based logistics invoice can both end as open supplier items, but they do not reach that state through the same controls.</p>
    </header>
    <div class="ecg-decision-columns">
      <div>
        <h3>Direct accounting invoice</h3>
        <p>Payment data is part of the accounting posting. If the due date or method is wrong, inspect the document and the supplier company-code defaults that fed it.</p>
      </div>
      <div>
        <h3>Logistics invoice</h3>
        <p>Invoice Verification also evaluates purchasing and receipt context. SAP can post an invoice but block it for payment when a relevant variance exceeds the configured tolerance. In that case, the payable is telling us that an upstream purchasing/invoice-verification control is unresolved.</p>
      </div>
      <div>
        <h3>Why the distinction matters</h3>
        <p>Removing an AP block without understanding its origin can bypass the control that created it. Payment readiness therefore includes ownership: who can explain and safely release the item, not only which field contains the block.</p>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="failures" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">From readiness to proposal</p>
      <h2>Stop at the boundary where payment processing takes over.</h2>
      <p>Once the item is open, due, not validly blocked and compatible with an executable payment method, the next evidence belongs to the payment proposal. That is where run parameters, method selection, bank determination and proposal exceptions become the subject.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/procurement/suppliers/automatic-payments/"><span>01</span><strong>Item looks ready, but the proposal excludes it</strong><small>Move to the automatic-payment layer and inspect the run parameters and proposal evidence.</small><i class="material-symbols-outlined" aria-hidden="true">payments</i></a>
      <a href="#readiness-map"><span>02</span><strong>Due date is unexpected</strong><small>Trace the item’s payment terms and baseline date before changing the next payment date in a run.</small><i class="material-symbols-outlined" aria-hidden="true">event</i></a>
      <a href="#readiness-map"><span>03</span><strong>Payment block exists</strong><small>Find its origin. A Logistics Invoice Verification block is evidence about the invoice, not a reason to start with payment customizing.</small><i class="material-symbols-outlined" aria-hidden="true">block</i></a>
      <a href="#readiness-map"><span>04</span><strong>Electronic method has no usable recipient bank data</strong><small>Check the supplier/BP bank information and payment-method requirements. House-bank ranking is a later, payer-side decision.</small><i class="material-symbols-outlined" aria-hidden="true">account_balance</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">A small example</p>
      <h2>One invoice, three different explanations.</h2>
    </header>
    <p>Assume a supplier invoice is still open for EUR 10,000. If its calculated net due date is next week, exclusion from today’s proposal can be correct. If it is due today but carries a payment block created by Invoice Verification, the payment layer is waiting for an upstream control to be resolved. If it is due and unblocked but its required bank-transfer data is incomplete, the item may reach payment processing and still fail method selection. These cases can look identical to a user — “the supplier was not paid” — but they belong to different parts of the chain.</p>
    <p>This is why we use the line item as the handoff record. <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/fd8427fa19d140c7b66d8457a70473a1/86248754a0cd9d62e10000000a445394.html" target="_blank" rel="noopener">Manage Supplier Line Items (F0712)</a> is one current S/4HANA work surface for finding open supplier items, reviewing payment-relevant data and setting or removing payment blocks. The exact operating surface depends on deployment and release, but the diagnostic sequence does not: prove the item, then prove the proposal.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Primary references</p><h2>SAP documentation behind the boundaries.</h2></header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/s4hana-cloud-best-practices/cross-company-purchasing-organization-2r3-kr/extend-business-partner" target="_blank" rel="noopener"><span>SAP</span><strong>Extend Business Partner</strong><small>Shows the separate Supplier (Purchasing) and Supplier (Financial Accounting) roles, including purchasing-organization and company-code data.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/fd8427fa19d140c7b66d8457a70473a1/86248754a0cd9d62e10000000a445394.html" target="_blank" rel="noopener"><span>SAP</span><strong>Manage Supplier Line Items</strong><small>Current F0712 capabilities for finding supplier items and working with payment blocks and payment-relevant data.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3eb1567cf97543c08087efb0936964e6/a84bd953189a424de10000000a174cb4.html" target="_blank" rel="noopener"><span>SAP</span><strong>Payment Control Data (Accounts Payable)</strong><small>Documents item payment blocks, payment methods and how the payment program uses them.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/PRODUCT_ID/af9ef57f504840d2b81be8667206d485/7870b6531de6b64ce10000000a174cb4.html" target="_blank" rel="noopener"><span>SAP</span><strong>Blocking Invoices</strong><small>Explains how Logistics Invoice Verification can post an invoice while blocking it for payment because of variances or other blocking reasons.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/s4hana-cloud-best-practices/accounts-payable-j60-il/payment-run" target="_blank" rel="noopener"><span>SAP</span><strong>Payment Run</strong><small>Confirms the automatic-payment boundary: posted open invoices, supplier payment methods and other prerequisites must exist before payment execution.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
