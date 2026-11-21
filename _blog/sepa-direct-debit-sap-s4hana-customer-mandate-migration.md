---
layout: default
title: "SEPA Direct Debit in SAP S/4HANA — From Sales Order to Bank Collection"
description: "A visual SAP S/4HANA FI-AR and SD guide: why SEPA mandates matter, where they enter the order-to-cash chain, how to check tables and transactions, and how to migrate safely."
permalink: /blog/sepa-direct-debit-sap-s4hana-customer-mandate-migration/
date: 2026-10-29
last_modified_at: 2026-11-04
author: "Dzmitryi Kharlanau"
language: en
category: "SAP process architecture"
tags:
  - sap-s4hana
  - sap-sd
  - fi-ar
  - sepa
  - data-migration
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
hide_global_cta: true
reading_time_minutes: 11
canonical_url: https://dkharlanau.github.io/blog/sepa-direct-debit-sap-s4hana-customer-mandate-migration/
semantic_links:
  - type: "related_topic"
    title: "Payments, Banks and Rejections"
    url: "/labs/enterprise-context/finance-logistics/payments-banks-rejections/"
  - type: "related_topic"
    title: "Sales Process Atlas"
    url: "/labs/enterprise-context/sales-processes/"
  - type: "related_topic"
    title: "FI/CO for Logistics"
    url: "/labs/enterprise-context/finance-logistics/"
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/finance-logistics/">FI/CO</a></li><li aria-current="page">SEPA Mandates</li></ol></nav>
<div class="research-canvas context-graph">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">SD × FI-AR / order-to-cash / migration</p>
      <h1>A customer can buy and be invoiced.<br />That does not mean you can debit their bank.</h1>
      <p>A SEPA mandate is the customer's authorization to collect money from a specific account. SAP uses that authorization in a configured direct-debit flow. It is not the customer's IBAN, not an SD partner function, and not a generic requirement for every sales order.</p>
      <a class="research-canvas__button" href="#chain">Trace the collection <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="SEPA control model">
      <p>Three independent questions</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Who pays?</strong><small>Customer / actual payer</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>May we debit?</strong><small>Valid mandate + bank account</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Did we collect?</strong><small>Payment run + bank response</small></div>
      <em>Customer existence, legal authority, and bank settlement are separate states.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">key</span>
    <div><p><strong>The business difference:</strong> without a valid mandate, an invoice can still create a receivable, but the intended SEPA direct-debit collection may not be eligible. That means manual payment, exception handling, delays, and collection risk.</p><p><strong>Not universal:</strong> actual order, billing, and payment-run behavior depends on SEPA activation, payment-method settings, document data, and your SAP release.</p></div>
    <a href="#compare">Compare outcomes <span class="material-symbols-outlined" aria-hidden="true">compare_arrows</span></a>
  </section>

  <section class="research-canvas__inventory" id="compare" data-reveal>
    <header><p class="research-canvas__eyebrow">Why the business cares</p><h2>Same invoice. Two different collection outcomes.</h2><p>Fictional example: customer A buys a EUR 1,000 service on recurring direct debit.</p></header>
    <div class="ecg-decision-columns">
      <div><h3>Valid mandate exists</h3><p>FI-AR can reference the authorized payer and bank account. Provided the item and payment setup qualify, the payment proposal can select the mandate and prepare the debit instruction.</p><strong>Business effect: an automated collection path is available.</strong></div>
      <div><h3>Mandate missing or unusable</h3><p>The sale and invoice may still exist; the bank account may even be correct. But mandate selection may fail, so the collection needs repair or an alternative agreed payment method.</p><strong>Business effect: receivable remains at risk of delayed collection.</strong></div>
      <div><h3>Mandate exists, bank returns debit</h3><p>A valid mandate is not proof of successful payment. The bank can reject or return a collection, and accounting must reflect the result.</p><strong>Business effect: investigate bank and clearing evidence, not only the master record.</strong></div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="chain" data-reveal>
    <header><p class="research-canvas__eyebrow">Visual process map / FI-AR</p><h2>Where the mandate actually enters the SD → FI → bank chain.</h2><p>Read left to right as a sequence of decisions. A standard invoice and a successful cash collection are not the same business event.</p></header>
    <div class="ecg-determination-list">
      <article class="ecg-determination-detail"><header><div><span>01</span><small>BP / master data</small></div><h3>Identify the payer and bank account</h3><p class="ecg-question">Who is the debtor, and which IBAN is authorized?</p></header><div class="ecg-decision-columns"><div><h4>Data</h4><p>BP, FI customer role, company-code segment, payer relationship and bank details.</p></div><div><h4>Check</h4><p>The payer can differ from Sold-to. Match the actual payer to the mandate; do not assume the Sold-to owns the bank account.</p></div><div><h4>Boundary</h4><p>An IBAN is payment data, not a signed authorization.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>02</span><small>FI-AR</small></div><h3>Maintain the authorization</h3><p class="ecg-question">Does a valid, eligible SEPA mandate exist?</p></header><div class="ecg-decision-columns"><div><h4>Mandate</h4><p>Reference, creditor ID, payer, IBAN, scheme (Core/B2B), signature evidence, validity, status, reuse and usage.</p></div><div><h4>SAP</h4><p>FI-AR manages the mandate. Inspect with FSEPA_M3/M4; maintain using supported functions, not direct table updates.</p></div><div><h4>Consequence</h4><p>If the mandate is missing, expired, incorrectly linked, or disallowed, do not assume the collection can proceed.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>03</span><small>SD / sales order</small></div><h3>Determine SEPA relevance</h3><p class="ecg-question">Is this sales document intended for direct debit?</p></header><div class="ecg-decision-columns"><div><h4>Standard mechanism</h4><p>SEPA-relevant terms of payment and payment method can determine relevance. In supported SD processing, an eligible FI-AR mandate may be selected or created from the sales document.</p></div><div><h4>Checks</h4><p>Actual payer, payment terms, payment method, mandate at header/item where supported, and relevant customizing.</p></div><div><h4>Do not assume</h4><p>Every sales document uses SEPA, or a missing mandate always causes an order block. Verify the system design.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>04</span><small>SD → FI-AR</small></div><h3>Billing creates the receivable</h3><p class="ecg-question">Is there an open customer invoice to collect?</p></header><div class="ecg-decision-columns"><div><h4>Accounting event</h4><p>Billing transfers relevant amounts to FI-AR and posts the customer receivable.</p></div><div><h4>SEPA handoff</h4><p>Payment-relevant data and, where used, mandate reference must be consistent with the later collection process.</p></div><div><h4>Pre-notification</h4><p>The payer must receive the applicable direct-debit notice. FI-AR pre-notification can use the more precise collection date and amount.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>05</span><small>FI-AR / F110</small></div><h3>Evaluate due items and mandates</h3><p class="ecg-question">Can the payment program collect this invoice?</p></header><div class="ecg-decision-columns"><div><h4>Selection</h4><p>Due open item, payment method, payment block, company code, payer, bank data, mandate availability and eligibility.</p></div><div><h4>Evidence</h4><p>Use the proposal and error log to prove why a collection was selected or rejected.</p></div><div><h4>Output</h4><p>Approved payment run and configured payment medium prepare the bank-facing instruction; postings depend on the process.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>06</span><small>Bank → FI reconciliation</small></div><h3>Confirm the money movement</h3><p class="ecg-question">Did the bank execute the debit, and does FI match the result?</p></header><div class="ecg-decision-columns"><div><h4>External state</h4><p>Bank acceptance, settlement, rejection or return must be established from banking evidence.</p></div><div><h4>SAP state</h4><p>Check payment/clearing postings, bank statement processing, returned items and charges.</p></div><div><h4>Business closure</h4><p>Close only after the customer receivable and the bank outcome agree.</p></div></div></article>
    </div>
    <p class="ecg-caption">Related maps: <a href="/labs/enterprise-context/sales-processes/">Sales Process Atlas</a> · <a href="/labs/enterprise-context/billing/">Billing</a> · <a href="/labs/enterprise-context/finance-logistics/">FI/CO for Logistics</a> · <a href="/labs/enterprise-context/finance-logistics/payments-banks-rejections/">Payments, Banks and Rejections</a>.</p>
  </section>

  <section class="research-canvas__inventory" id="objects" data-reveal>
    <header><p class="research-canvas__eyebrow">Technical inspection</p><h2>Transactions, table, and the evidence each one proves.</h2><p>GUI references apply to supported FI-AR configurations; availability and Fiori alternatives vary by release.</p></header>
    <div class="ecg-decision-columns">
      <div><h3>Mandate tools</h3><p><strong>FSEPA_M1</strong> — create<br /><strong>FSEPA_M2</strong> — change<br /><strong>FSEPA_M3</strong> — display<br /><strong>FSEPA_M4</strong> — list, filter, investigate</p><p>Start with FSEPA_M4 when someone says: “The mandate is missing.”</p></div>
      <div><h3>Technical evidence</h3><p><strong>SEPA_MANDATE</strong> — read-only technical investigation, where present. Use SE11 to inspect field definitions and keys in your system, then SE16H/SE16N for controlled selection.</p><p>Do not infer that a record is usable only from a table row, and never repair it by direct SQL update.</p></div>
      <div><h3>Related process</h3><p><strong>BP</strong> — customer, actual payer, bank details<br /><strong>F110</strong> — payment proposal and run, where applicable<br /><strong>FI open-item and payment evidence</strong> — show whether the invoice is open, paid, or returned.</p><p>Separate SD document status from FI payment status.</p></div>
    </div>
    <div class="research-canvas__boundary"><span class="material-symbols-outlined" aria-hidden="true">fact_check</span><div><p><strong>Minimal evidence set:</strong> mandate reference + creditor ID + payer + IBAN + scheme + validity/status + signature evidence + target customer mapping + payment proposal message.</p><p><strong>Important:</strong> status codes and the exact change options must be verified against your FI-AR application and SAP release. A display status alone does not authorize a collection.</p></div></div>
  </section>

  <section class="research-canvas__inventory" id="migration" data-reveal>
    <header><p class="research-canvas__eyebrow">Migration / controlled example</p><h2>The customer is migrated. The mandate still needs its own migration decision.</h2><p>Fictional source ERP customer 00004567 → target S/4HANA customer 10004567. The authorized account stays the same, but the payer number changes.</p></header>
    <div class="ecg-decision-columns">
      <div><h3>Before load</h3><p>Export the mandate inventory and count all, in-scope, excluded and blocked records separately. Build source-to-target payer mapping; check target bank data, creditor ID, Core/B2B, reference, status, signature and evidence.</p><strong>Do not equate “BP migrated” with “mandate migrated”.</strong></div>
      <div><h3>During load</h3><p>Use the target release's supported <strong>FI - SEPA mandate</strong> Migration Cockpit object or approved mechanism. Pilot realistic cases first. Record rejected, created and duplicate records; do not invent signature dates.</p><strong>No direct table insert or silent activation.</strong></div>
      <div><h3>After load</h3><p>Reconcile by business keys, not row count alone. Inspect in FSEPA_M4; check the mapped payer/IBAN and run a controlled F110 proposal against a representative receivable.</p><strong>Do not send a live bank debit in a routine migration test.</strong></div>
    </div>
    <div class="ecg-control-stack">
      <article><span>EXTRACT</span><h3>Source inventory</h3><p>Mandate reference · Source payer · IBAN · Creditor ID · Scheme · Status · Signature date · Evidence</p></article>
      <article><span>MAP</span><h3>Target readiness</h3><p>Target payer · BP FI role · Bank match · Company code · Creditor setup · Duplicate check · Decision owner</p></article>
      <article><span>RECON</span><h3>Acceptance evidence</h3><p>Source scope = migrated + excluded (approved) + unresolved. Compare keys and test mandate selection, payment proposal and cutover delta.</p></article>
    </div>
    <p>Migration object availability is deployment-specific: verify the <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/1d1601c422e94d569d37263875ee4ff6.html">SAP FI - SEPA mandate object documentation</a> and your own Migration Cockpit catalogue.</p>
  </section>

  <section class="research-canvas__inventory" id="diagnostic" data-reveal>
    <header><p class="research-canvas__eyebrow">Support / first wrong state</p><h2>Five checks when the customer exists but SEPA collection does not work.</h2></header>
    <div class="ecg-control-stack">
      <article><span>01</span><h3>Was SEPA intended?</h3><p>Check the SD payer, payment terms, and payment method. An ordinary bank transfer does not need a direct-debit mandate.</p></article>
      <article><span>02</span><h3>Does the FI-AR mandate exist?</h3><p>Use FSEPA_M4 and, if required, read-only SEPA_MANDATE. Confirm creditor/payer/reference, not only a similar name.</p></article>
      <article><span>03</span><h3>Can that mandate be used?</h3><p>Check validity, status, reusable/usage rules, authorized IBAN, scheme and evidence. A record may exist but be ineligible.</p></article>
      <article><span>04</span><h3>What did the payment proposal say?</h3><p>Inspect the due invoice, payment block, method and exact F110 exception. Distinguish mandate lookup failure from payment configuration failure.</p></article>
      <article><span>05</span><h3>Did the bank accept the collection?</h3><p>If the payment file was sent, switch from master-data analysis to bank response, return and reconciliation.</p></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Architecture boundary</p><h2>Who owns each part?</h2></header>
    <div class="ecg-decision-columns">
      <div><h3>MDG / master data</h3><p>BP identity, FI customer extension, payer mapping, governed bank details and replication. MDG replication alone is not evidence that an FI-AR mandate exists.</p></div>
      <div><h3>FI-AR / payments</h3><p>Mandate lifecycle, supported maintenance, payment method, selection, proposal, accounting and exceptions.</p></div>
      <div><h3>Bank / compliance / migration</h3><p>Creditor identifier, mandate evidence, Core/B2B eligibility, bank exchange, migration mapping and controlled reconciliation.</p></div>
    </div>
    <div class="research-canvas__boundary"><span class="material-symbols-outlined" aria-hidden="true">psychology</span><div><p><strong>Architect question:</strong> If BP replication is green but the direct debit fails, which object or step has not been proven?</p><p>Answer: the authorized mandate's existence and eligibility for the <em>actual payer and account</em>, followed by payment selection and bank execution. A successful BP replication proves none of those on its own.</p></div></div>
  </section>

  <section class="research-canvas__inventory" id="sources" data-reveal>
    <header><p class="research-canvas__eyebrow">Evidence and further routes</p><h2>Check SAP standard before assuming custom behavior.</h2></header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/6f1d59146ff144748b1ee315026ff2df.html" target="_blank" rel="noopener"><span>SAP</span><strong>Process a Sales Document with SEPA Mandate</strong><small>SEPA relevance, payment terms, payer, and mandate selection (S/4HANA 2025 FPS02).</small></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/ad0bef26b37045ddb256f0bcfb8ff445.html" target="_blank" rel="noopener"><span>SAP</span><strong>SEPA Direct Debits in SD</strong><small>SD and FI-AR integration, customizing, and pre-notification.</small></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ONPREMISE/7b24a64d9d0941bda1afa753263d9e39/8931523fecaa40a89f164c4f3416ea47.html" target="_blank" rel="noopener"><span>SAP</span><strong>Direct Debit Pre-Notification</strong><small>Billing and FI-AR communication options.</small></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/99fb46a79ab241d5984df80fe7a9aa32/d5ff4252ba5f1b13e10000000a44176d.html" target="_blank" rel="noopener"><span>SAP</span><strong>FI SEPA Transactions</strong><small>FSEPA_M1 / M2 / M3 / M4 documented for relevant SAP GUI deployments.</small></a>
      <a href="/labs/enterprise-context/finance-logistics/payments-banks-rejections/"><span>LAB</span><strong>Payments, Banks and Rejections</strong><small>Proposal → bank response → reconciliation and exception handling.</small></a>
      <a href="/labs/enterprise-context/procurement/suppliers/automatic-payments/"><span>LAB</span><strong>Automatic Payments</strong><small>How to diagnose the F110 selection and payment execution pipeline.</small></a>
    </div>
    <p class="ecg-caption">Scope: standard FI-AR SEPA Direct Debit, not FI-CA or SEPA Credit Transfer. Example data are synthetic. Release-specific status codes, payment configuration, and exact field lists require system verification before production use.</p>
  </section>
  <div class="research-canvas__support" data-reveal>{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
