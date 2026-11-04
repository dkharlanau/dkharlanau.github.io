---
layout: default
title: "SEPA Direct Debit in SAP S/4HANA: Mandates, Sales, Payments and Migration"
description: "An illustrated SAP S/4HANA FI-AR and Sales guide: why SEPA mandates matter, where they affect billing and collections, how to inspect tables and migrate safely."
slug: sepa-direct-debit-sap-s4hana-customer-mandate-migration
permalink: /blog/sepa-direct-debit-sap-s4hana-customer-mandate-migration/
date: 2026-10-29
last_modified_at: 2026-11-04
last_reviewed: 2026-11-04
review_method: "SAP S/4HANA 2025 FPS02 Sales and 2025 FPS01 Financial Operations documentation; Cloud Public Edition 2608 migration object and CDS view references"
author: "Dzmitryi Kharlanau"
language: en
category: "SAP financial operations"
tags:
  - sap-s4hana
  - sap-sd
  - sap-fi-ar
  - sepa
  - data-migration
canonical_url: https://dkharlanau.github.io/blog/sepa-direct-debit-sap-s4hana-customer-mandate-migration/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
hide_global_cta: true
sepa_lab: true
reading_time_minutes: 17
related_articles:
  - /blog/the-hidden-operational-cost-of-poor-master-data-in-sap/
  - /blog/why-master-data-distribution-fails-even-when-every-interface-is-green/
semantic_links:
  - type: "related_topic"
    title: "Payments, Banks and Rejections"
    url: "/labs/enterprise-context/finance-logistics/payments-banks-rejections/"
  - type: "related_topic"
    title: "FI/CO for Logistics"
    url: "/labs/enterprise-context/finance-logistics/"
  - type: "related_topic"
    title: "SAP Sales Process Atlas"
    url: "/labs/enterprise-context/sales-processes/"
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/blog/">Blog</a></li><li><a href="/labs/enterprise-context/finance-logistics/">FI/CO for Logistics</a></li><li aria-current="page">SEPA Direct Debit</li></ol></nav>

<article class="research-canvas context-graph sepa-lab" aria-labelledby="sepa-title">
  <header class="research-canvas__hero sepa-hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">SAP Sales × FI-AR / Payment architecture</p>
      <h1 id="sepa-title">An invoice is not permission<br>to debit a bank account.</h1>
      <p>SEPA Direct Debit lets a company collect money from a customer. The mandate is the customer's authorisation. Follow one €1,000 invoice through Sales, billing, FI-AR, the payment program and the bank — and see exactly what breaks when the mandate is missing.</p>
      <div class="sepa-hero-actions">
        <a class="research-canvas__button" href="#sepa-process">Follow the collection <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
        <a class="sepa-hero-link" href="#sepa-tables">Inspect tables and apps <span aria-hidden="true">↗</span></a>
      </div>
    </div>
    <div class="research-canvas__signal" aria-label="Three separate business objects">
      <p>Do not mix these up</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Invoice</strong><small>What the customer owes</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Mandate</strong><small>Authority to collect</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Collection</strong><small>The actual payment request</small></div>
      <em>Having an IBAN does not create a mandate. Having a mandate does not mean the bank has paid.</em>
    </div>
  </header>

  <nav class="sepa-jump-nav" aria-label="On this page">
    <a href="#sepa-why">Why it matters</a>
    <a href="#sepa-process">End-to-end flow</a>
    <a href="#sepa-impact">Missing-mandate impact</a>
    <a href="#sepa-tables">Tables &amp; apps</a>
    <a href="#sepa-migration">Migration lab</a>
    <a href="#sepa-diagnostics">Troubleshooting</a>
  </nav>

  <section class="research-canvas__boundary sepa-lead-rule" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_balance</span>
    <div>
      <p><strong>Business rule:</strong> a SEPA mandate is the customer's permission to let the creditor initiate a direct debit. It is not the bank account, the sales order, the invoice, or the bank execution result.</p>
      <p>This guide focuses on <strong>incoming customer collections in FI-AR</strong> in an SAP S/4HANA setting. FI-CA, banking products, SEPA Credit Transfers and supplier payments follow different processing models.</p>
    </div>
    <a href="#sepa-scope">See the scope <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section id="sepa-why" class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">01 / Business difference</p><h2>Same customer. Same invoice. Two very different ways to get paid.</h2><p>Imagine a customer owes €1,000. A normal bank transfer and a direct debit may settle the same receivable, but they do not use the same authorisation or payment flow.</p></header>
    <div class="sepa-two-paths">
      <article class="sepa-path sepa-path--transfer">
        <p class="sepa-path__tag">Path A · SEPA Credit Transfer (SCT)</p>
        <h3>The customer sends the money.</h3>
        <ol>
          <li>SAP bills €1,000 and records a receivable.</li>
          <li>The customer instructs their own bank to transfer €1,000.</li>
          <li>Bank statement and clearing confirm the result in SAP.</li>
        </ol>
        <p class="sepa-path__outcome"><strong>No direct-debit mandate is needed</strong> for this transfer. The customer's outgoing bank instruction is the payment action.</p>
      </article>
      <article class="sepa-path sepa-path--debit">
        <p class="sepa-path__tag">Path B · SEPA Direct Debit (SDD)</p>
        <h3>The company asks the bank to collect.</h3>
        <ol>
          <li>The customer authorises the creditor to debit their account.</li>
          <li>FI-AR holds a valid mandate linked to the correct payer and bank account.</li>
          <li>The payment run creates a collection instruction; the bank then processes it.</li>
        </ol>
        <p class="sepa-path__outcome"><strong>The mandate is required for an authorised collection.</strong> Without usable authorisation, the direct-debit route is not payment-ready.</p>
      </article>
    </div>
    <p class="sepa-source-note">SEPA Core and SEPA B2B have different scheme rules and refund protections. A bank account alone is never proof of the signed authority. <a href="https://www.europeanpaymentscouncil.eu/what-we-do/sepa-direct-debit" target="_blank" rel="noopener">European Payments Council: SDD schemes</a>.</p>
  </section>

  <section id="sepa-process" class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">02 / Process map</p><h2>Where the mandate enters the Order-to-Cash chain.</h2><p>Read the sequence left to right. The mandate is a separate FI-AR object that can be selected in an SD document and later used by the collection process. The exact checks depend on your settings.</p></header>
    <ol class="sepa-flow" aria-label="SEPA Direct Debit customer process, from master data to bank clearing">
      <li><span class="sepa-flow__num">01 · Master data</span><a href="/labs/enterprise-context/master-data/">Payer and IBAN</a><p>Customer / BP, FI company-code extension, authorised bank account.</p></li>
      <li><span class="sepa-flow__num">02 · Authority</span><strong>FI-AR mandate</strong><p>Creditor, payer, IBAN, scheme, signature, status and validity.</p></li>
      <li><span class="sepa-flow__num">03 · Sales (optional)</span><a href="/labs/enterprise-context/sales-order/">Sales order</a><p>SEPA payment method; existing mandate may be assigned at header or item level.</p></li>
      <li><span class="sepa-flow__num">04 · Billing</span><a href="/labs/enterprise-context/billing/">Invoice</a><p>Mandate reference may flow into billing and influence the billing split.</p></li>
      <li><span class="sepa-flow__num">05 · FI-AR</span><a href="/labs/enterprise-context/finance-logistics/">Open receivable</a><p>A customer invoice is due; payment method and mandate eligibility matter.</p></li>
      <li><span class="sepa-flow__num">06 · Collection</span><strong>Payment run</strong><p>Proposal, mandate selection, posting and payment medium as configured.</p></li>
      <li><span class="sepa-flow__num">07 · Bank</span><a href="/labs/enterprise-context/finance-logistics/payments-banks-rejections/">Execute &amp; reconcile</a><p>Bank acceptance, rejects, returns, statement processing and final clearing.</p></li>
    </ol>
    <div class="sepa-flow-callout">
      <strong>Two different paths can converge on FI-AR.</strong>
      <p>An FI-only direct debit does not require a Sales Order. The Sales stage is shown because it matters for SD implementations. A mandate can be managed in FI-AR even when the transaction did not originate in SD.</p>
    </div>
  </section>

  <section id="sepa-impact" class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">03 / Failure boundaries</p><h2>What if the mandate is missing, inactive or assigned to the wrong payer?</h2><p>It is not true that every missing mandate stops every sales order. You must find the first process step that actually checks for a usable mandate.</p></header>
    <div class="sepa-table-wrap" role="region" aria-label="SEPA mandate impact by process stage" tabindex="0">
      <table class="sepa-table">
        <thead><tr><th scope="col">Stage</th><th scope="col">When the mandate is usable</th><th scope="col">When it is missing or invalid</th><th scope="col">Controlling factor</th></tr></thead>
        <tbody>
          <tr><th scope="row">Sales order / contract</th><td>A valid mandate may be selected for the payer.</td><td>Mandate assignment can be incomplete; follow-on work can be restricted.</td><td>SEPA-relevant terms/payment method, SD incompletion configuration.</td></tr>
          <tr><th scope="row">Billing</th><td>Mandate reference can be passed to billing and used as a split criterion.</td><td>Billing can be held if the configured mandate check fails. Different references may split invoices.</td><td>Copying control, mandate status checks and incompletion settings.</td></tr>
          <tr><th scope="row">FI payment proposal</th><td>The direct-debit method can use an eligible mandate.</td><td>Collection can be excluded or show an exception; the receivable can remain unpaid.</td><td>Mandate eligibility, payer, account, payment method and run configuration.</td></tr>
          <tr><th scope="row">Bank response</th><td>A properly authorised instruction can be executed, subject to bank checks.</td><td>The bank can reject or return a collection. Accounting needs controlled recovery.</td><td>Scheme, bank registration (notably B2B), payment medium and bank feedback.</td></tr>
        </tbody>
      </table>
    </div>
    <div class="sepa-highlight">
      <span class="material-symbols-outlined" aria-hidden="true">rule</span>
      <p><strong>Subtle but important:</strong> standard SD documentation for S/4HANA 2025 FPS02 describes mandate statuses <code>New (00)</code>, <code>Active (01)</code> and <code>Not Confirmed (02)</code> as candidates for <em>sales-document assignment</em> when other validity conditions are met. The billing documentation describes an <strong>Active (01)</strong> status check for copying a mandate into billing. Do not assume that “selectable in an order” means “ready for direct debit.” <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/6f1d59146ff144748b1ee315026ff2df.html" target="_blank" rel="noopener">SAP: Sales document checks</a> · <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD_PE/7b24a64d9d0941bda1afa753263d9e39/feb4509d0e8742238b0c9572672ea7d7.html" target="_blank" rel="noopener">SAP: Billing checks</a>.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">04 / SD–FI integration</p><h2>Four checks explain most Sales and payment problems.</h2><p>This is the business logic behind the diagram, not a claim that every S/4HANA deployment has exactly the same screens.</p></header>
    <div class="ecg-determination-list">
      <article class="ecg-determination-detail"><header><div><span>01</span><small>relevance</small></div><h3>Is the transaction actually SEPA-relevant?</h3><p>Read the payer's terms of payment, relevant payment method and SD SEPA settings.</p></header><p>If the customer plans to make a normal bank transfer, adding a mandate solves no real problem. In the configured SD process, the payment method may be derived from the payer's terms of payment and changed at header or item level.</p></article>
      <article class="ecg-determination-detail"><header><div><span>02</span><small>party</small></div><h3>Who is the payer — not only the sold-to?</h3><p>The person or entity being debited must be the authorised debtor.</p></header><p>Sold-to, ship-to and payer are not interchangeable. A mandate owned by customer A cannot simply authorise debits from customer B's bank account. Check the SD partner determination and the account actually used for collection.</p></article>
      <article class="ecg-determination-detail"><header><div><span>03</span><small>billing</small></div><h3>Does the mandate survive the billing step?</h3><p>A mandate reference can be copied to billing and become a split criterion.</p></header><p>If two billable transactions have different mandate references, they can create separate invoices. With the relevant status/copy checks, an invalid mandate can also stop billing. A billed document is not the place to casually change the mandate; follow SAP's documented reversal and correction route.</p></article>
      <article class="ecg-determination-detail"><header><div><span>04</span><small>cash</small></div><h3>What does the payment proposal and the bank say?</h3><p>Selection, posting, payment medium and bank confirmation are separate states.</p></header><p>A payment proposal exception is an FI/payment setup investigation. A bank rejection after an instruction was sent is a different problem. Pre-notification is an additional communication requirement, not a substitute for the mandate itself.</p></article>
    </div>
    <div class="sepa-payment-check">
      <h3>What the classic FI payment program checks</h3>
      <ol>
        <li><strong>Payment method:</strong> is the direct-debit method configured as SEPA-relevant, with the appropriate mandate requirement?</li>
        <li><strong>Bank account:</strong> is the debtor's IBAN available for the actual payer?</li>
        <li><strong>Authority:</strong> is an <em>active, unlocked</em> mandate eligible for that debtor, creditor and IBAN?</li>
        <li><strong>Execution:</strong> did the proposal select the item, and did the payment run produce the expected bank instruction?</li>
      </ol>
      <p>These are the documented classic payment-program decision points; verify the exact messages and configuration in your S/4HANA system. <a href="https://help.sap.com/docs/SAP_ERP/ba20fc74bc8c4669870d4da8e3d8b5a6/b049f33c67d348f49a0e4f7b07827112.html" target="_blank" rel="noopener">SAP: evaluation of mandates by payment run</a>.</p>
    </div>
  </section>

  <section id="sepa-tables" class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">05 / Technical map</p><h2>Find the object in SAP, then follow its relationships.</h2><p>Start with a supported app. Use read-only technical views to verify evidence. A database row alone cannot tell you whether an authorisation is legally valid or eligible for the next payment.</p></header>
    <div class="sepa-technical-grid">
      <div class="sepa-object-card sepa-object-card--main">
        <span>Mandate master</span><h3><code>SEPA_MANDATE</code></h3><p>Inspect mandate identity, status, payer, creditor, bank account and dates.</p>
        <dl><div><dt><code>MGUID</code></dt><dd>Technical mandate GUID</dd></div><div><dt><code>MNDID</code></dt><dd>Mandate reference / UMR</dd></div><div><dt><code>REC_CRDID</code></dt><dd>Creditor identifier</dd></div><div><dt><code>SND_ID</code>, <code>SND_TYPE</code></dt><dd>Debtor identity and type</dd></div><div><dt><code>SND_IBAN</code></dt><dd>Mandate's debtor IBAN</dd></div><div><dt><code>PAY_TYPE</code></dt><dd>One-off or recurring mandate</dd></div><div><dt><code>STATUS</code>, <code>SIGN_DATE</code></dt><dd>Lifecycle and signature</dd></div></dl>
      </div>
      <div class="sepa-object-card">
        <span>Mandate use / trace</span><h3><code>SEPA_MANDATE_USE</code></h3><p>Usage evidence for a mandate; inspect the <strong>Use</strong> tab first. Retention may be limited by configuration.</p>
        <dl><div><dt><code>MGUID</code></dt><dd>Links to the technical mandate</dd></div><div><dt><code>USE_DATE</code></dt><dd>Recorded usage date</dd></div><div><dt><code>USE_DOCTYPE</code>, <code>USE_DOCID</code></dt><dd>Type and key of the usage object</dd></div></dl>
      </div>
      <div class="sepa-object-card">
        <span>Business chain / context</span><h3>BP → SD → FI</h3><p>Inspect the payer and bank details in <code>BP</code>; use released CDS views where available.</p>
        <dl><div><dt><code>BUT0BK</code> / <code>KNBK</code></dt><dd>BP / classic customer bank context; release and CVI dependent</dd></div><div><dt><code>VBPA</code></dt><dd>Sales-document partner roles, including payer</dd></div><div><dt><code>I_CustomerSEPAMandate</code></dt><dd>Released customer mandate interface view in documented S/4HANA release</dd></div><div><dt><code>I_SEPAMandateUsage</code></dt><dd>CDS usage reporting view</dd></div></dl>
      </div>
    </div>
    <p class="sepa-source-note"><strong>Usage history has limits:</strong> the classic payment program can retain only a configured number of mandate uses and delete older usage rows. A short or empty <code>SEPA_MANDATE_USE</code> history is not by itself evidence that the mandate was never used. <a href="https://help.sap.com/docs/SAP_ERP/ba20fc74bc8c4669870d4da8e3d8b5a6/b049f33c67d348f49a0e4f7b07827112.html" target="_blank" rel="noopener">SAP: usage recording</a>.</p>
    <p class="sepa-source-note"><strong>Do not join everything by customer number.</strong> The mandate's technical identifier, business reference, creditor, debtor and IBAN have different roles. Confirm field definitions in <code>SE11</code> in your target release and use a released CDS interface or supported API for production integrations. <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/ee6ff9b281d8448f96b4fe6c89f2bdc8/59e1eb1e333949ebb74c6a99c1fbd13b.html" target="_blank" rel="noopener">SAP: I_CustomerSEPAMandate</a> · <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/c0c54048d35849128be8e872df5bea6d/9125b1e147b54a2cbb316b67bc824632.html" target="_blank" rel="noopener">SAP: usage CDS</a>.</p>
    <h3>Useful transactions and apps</h3>
    <div class="sepa-table-wrap" role="region" aria-label="SEPA SAP transactions" tabindex="0">
      <table class="sepa-table sepa-table--compact">
        <thead><tr><th scope="col">Object / transaction</th><th scope="col">Use</th><th scope="col">Boundary</th></tr></thead>
        <tbody>
          <tr><th scope="row"><code>FSEPA_M1</code> / <code>FSEPA_M2</code></th><td>Create / change mandate</td><td>Use supported UI and business approvals; do not force a status to make a test pass.</td></tr>
          <tr><th scope="row"><code>FSEPA_M3</code> / <code>FSEPA_M4</code></th><td>Display / list and filter mandates</td><td>First place to verify a mandate's presence and current version.</td></tr>
          <tr><th scope="row"><code>F5158</code>, <code>FSEPA_M4_FIN</code></th><td>Manage/list mandates in documented Fiori or cloud scenarios</td><td>Availability depends on deployment, role and release.</td></tr>
          <tr><th scope="row"><code>BP</code></th><td>Payer, FI customer and bank data</td><td>IBAN exists ≠ direct-debit authorisation exists.</td></tr>
          <tr><th scope="row"><code>F110</code> / <code>FBZP</code></th><td>Classic payment proposal / payment-program configuration</td><td>Check proposal evidence before changing configuration.</td></tr>
          <tr><th scope="row"><code>SE11</code>, <code>SE16H</code> / <code>SE16N</code></th><td>Dictionary and authorised read-only verification</td><td>Never update <code>SEPA_MANDATE</code> directly.</td></tr>
        </tbody>
      </table>
    </div>
    <p class="sepa-source-note">In <code>FSEPA_M3/M4</code>, inspect <strong>Basic Data</strong> (status/validity), <strong>Sender</strong> (debtor/IBAN), <strong>Recipient</strong> (creditor), <strong>Use</strong> (payment usage) and <strong>Versions</strong>. <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/451fcec7eb02466aab0dfef5a2e54901.html" target="_blank" rel="noopener">SAP: mandate maintenance</a>.</p>
    <div class="sepa-status-ladder" aria-label="SEPA FI-AR mandate lifecycle">
      <h3>Mandate status: what the labels mean for payment readiness</h3>
      <div class="sepa-status-grid">
        <div><span>Preparation</span><strong>Entered / To Be Confirmed</strong><p>A mandate record exists, but this does not itself prove signed and usable authorisation for collection.</p></div>
        <div><span>Payment eligible</span><strong>Active</strong><p>The normal required FI-AR state for direct-debit use, subject to validity, account, scheme and other payment checks.</p></div>
        <div><span>Restricted</span><strong>Locked / Canceled</strong><p>Investigate the reason and business decision. Do not reactivate simply to clear a payment error.</p></div>
        <div><span>End of use</span><strong>Obsolete / Completed</strong><p>Not eligible for new collection; an obsolete mandate and a mandate finished after its intended last use are different histories.</p></div>
      </div>
      <p class="sepa-source-note">These are common FI-AR mandate statuses, not a universal cross-application workflow. Different applications expose different status sets: for example, <em>Reversed</em> appears in other mandate-management contexts. Confirm actual values and allowed transitions in the target system's <code>SEPA_STATUS</code> domain and supported maintenance UI. <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/ee6ff9b281d8448f96b4fe6c89f2bdc8/b601aa9124254d338ee0ec8f5e01ed1a.html" target="_blank" rel="noopener">SAP: mandate status CDS</a>.</p>
    </div>
  </section>

  <section id="sepa-migration" class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">06 / Migration lab · synthetic data</p><h2>The BP was migrated. Can we still collect money?</h2><p>Consider an ERP/AFS-to-S/4HANA move where the customer exists in the target, but mandates need a separate migration. Moving bank accounts is not enough.</p></header>
    <div class="sepa-migration-case">
      <div><span>Source customer</span><strong><code>00004567</code></strong><small>Source ERP/AFS</small></div>
      <div class="sepa-migration-arrow" aria-hidden="true">→</div>
      <div><span>Target customer / payer</span><strong><code>10004567</code></strong><small>Target S/4HANA</small></div>
      <div class="sepa-migration-detail"><span>Authorisation that must remain consistent</span><strong><code>SDD-2026-0042</code></strong><p>Creditor ID · customer/payer mapping · IBAN ending 1234 · scheme · signature evidence · status · usage history as required. All identifiers are fictional.</p></div>
    </div>
    <div class="sepa-step-grid">
      <article><span>01 / Inventory</span><h3>Count the full source scope</h3><p>Use <code>FSEPA_M4</code> and, where allowed, read-only extraction. Separate active, historical, cancelled, obsolete and review-required mandates. Inventory the signatures too.</p></article>
      <article><span>02 / Map</span><h3>Resolve the real payer</h3><p>Map source debtor to target FI customer, not simply sold-to. Verify the target IBAN and collecting entity's creditor ID. Detect duplicate mandate references.</p></article>
      <article><span>03 / Decide</span><h3>Classify each source record</h3><p><strong>READY</strong> if all prerequisites and evidence match; <strong>BLOCKED</strong> if required data is missing; <strong>REVIEW</strong> if validity, owner or consent is unclear.</p></article>
      <article><span>04 / Load</span><h3>Use a supported migration object</h3><p>Check the target system's <strong>FI - SEPA mandate</strong> Migration Cockpit object and available staging/direct-transfer approaches. Validate required fields for the intended status.</p></article>
      <article><span>05 / Prove</span><h3>Reconcile and test safely</h3><p>Compare mandate reference, payer, IBAN, creditor, status and signature. Test a controlled payment proposal; do not send real bank collection instructions from a migration test.</p></article>
      <article><span>06 / Cutover</span><h3>Capture the delta</h3><p>Reconcile mandates created, changed, cancelled or used since extraction. Record approved exclusions and the owner of every unresolved mismatch.</p></article>
    </div>
    <div class="sepa-table-wrap" role="region" aria-label="Sample migration readiness checks" tabindex="0">
      <table class="sepa-table sepa-table--compact">
        <thead><tr><th scope="col">Synthetic test</th><th scope="col">Check</th><th scope="col">Expected result</th></tr></thead>
        <tbody>
          <tr><th scope="row">A · Correct payer</th><td>Source payer maps to target payer, IBAN and creditor agree.</td><td><span class="sepa-state sepa-state--ready">READY</span> · can enter controlled pilot.</td></tr>
          <tr><th scope="row">B · Different SD payer</th><td>Sold-to matches, but the payer is a different BP.</td><td><span class="sepa-state sepa-state--review">REVIEW</span> · do not copy consent to another debtor.</td></tr>
          <tr><th scope="row">C · Missing bank account</th><td>Mandate IBAN not available for target payer.</td><td><span class="sepa-state sepa-state--blocked">BLOCKED</span> · correct master-data prerequisite.</td></tr>
          <tr><th scope="row">D · Cancelled mandate</th><td>Mandate exists in source but is not payment-eligible.</td><td><span class="sepa-state sepa-state--review">REVIEW</span> · approved exclusion/retention decision.</td></tr>
        </tbody>
      </table>
    </div>
    <p class="sepa-source-note">SAP's current Cloud Public Edition <strong>FI - SEPA mandate</strong> template lists extra fields for an active mandate, including <code>SIGN_CITY</code>, <code>SIGN_DATE</code>, <code>REC_CRDID</code>, <code>SND_TYPE</code>, <code>SND_ID</code>, <code>SND_IBAN</code> and <code>SND_BIC</code>. Field rules are release- and method-specific. <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/1d1601c422e94d569d37263875ee4ff6.html" target="_blank" rel="noopener">SAP: FI - SEPA mandate migration object</a>. The <code>FSEPA_M4</code> <em>Migrate</em> button described for <a href="https://help.sap.com/docs/SAP_S4HANA_ONPREMISE/26c2d5e366bc44c1a98f2a9212a0c49d/b96998502ced4252b0cb5a301a0e7d40.html" target="_blank" rel="noopener">Central Finance</a> is <strong>not</strong> a universal migration method.</p>
  </section>

  <section id="sepa-diagnostics" class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">07 / Support playbook</p><h2>Investigate the first wrong state, not the last visible error.</h2><p>Three practical cases show how to separate master-data, FI-AR and banking issues without making dangerous corrections.</p></header>
    <div class="sepa-accordion">
      <details open><summary><span>Case 01</span> The BP has an IBAN, but no SEPA mandate is visible.</summary><div><p><strong>Evidence:</strong> read the payer and bank data in <code>BP</code>; search <code>FSEPA_M4</code> by creditor, payer and mandate reference; inspect the source inventory and Migration Cockpit log.</p><p><strong>Decision:</strong> is the mandate absent, filtered out, mapped to the wrong payer, or held in a different application? Do not create a duplicate before checking the legal record and source-to-target mapping.</p></div></details>
      <details><summary><span>Case 02</span> The mandate exists, but billing or collection does not work.</summary><div><p><strong>Evidence:</strong> check SEPA-relevant payment method, SD payer, mandate reference, status, validity, IBAN, creditor ID, billing copying/incompletion configuration, and <code>F110</code> proposal details.</p><p><strong>Decision:</strong> separate a sales-document assignment issue, a billing status/split issue, and a payment-program eligibility issue. Fix the earliest invalid decision. A status change is not automatically an acceptable fix.</p></div></details>
      <details><summary><span>Case 03</span> SAP posted a payment, but the bank rejected or returned the debit.</summary><div><p><strong>Evidence:</strong> identify the generated bank instruction, rejection/return code, scheme (Core/B2B), bank-side B2B registration, posting state and relevant bank-statement items.</p><p><strong>Decision:</strong> this is a bank-execution and reconciliation investigation, not proof that the customer or sales master data is wrong. Follow the <a href="/labs/enterprise-context/finance-logistics/payments-banks-rejections/">Payments, Banks and Rejections</a> lab before attempting reversals.</p></div></details>
    </div>
    <div class="sepa-highlight">
      <span class="material-symbols-outlined" aria-hidden="true">verified_user</span>
      <p><strong>Do not “repair” mandates by direct database updates.</strong> Mandate state and signature evidence have legal and banking consequences. Involve FI-AR and the business owner for cancellations, completed/obsolete status changes, consent issues, and mass migration decisions.</p>
    </div>
  </section>

  <section id="sepa-scope" class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">08 / Architecture choices</p><h2>What must an SAP Lead decide before implementation?</h2><p>Mandate handling is a cross-functional design. The right answer depends on the collection model and the target deployment.</p></header>
    <div class="ecg-decision-columns">
      <div><h3>Process boundary</h3><p>Is this FI-AR or FI-CA? Does the collection begin in Sales or directly in Finance? Is the payment SCT or SDD, Core or B2B?</p></div>
      <div><h3>Data ownership</h3><p>Who owns payer mapping, BP bank data, signed evidence, mandate status and validity? MDG customer replication does not automatically migrate FI-AR mandates.</p></div>
      <div><h3>Execution and risk</h3><p>Which payment run and payment medium are used? What happens to missing mandates, rejected instructions, returns, and cutover deltas? Who can approve exceptions?</p></div>
    </div>
    <p class="sepa-source-note">SAP deployments differ. <code>FSEPA_M*</code> transactions are typical for GUI-based FI-AR; <code>F5158</code> and other Fiori apps depend on release and authorisations. The FI-CA mandate relationship and payment processes differ. Verify target-system configuration, SAP Help for the exact release, and the current scheme-owner rules before production changes.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Continue along the enterprise process</p><h2>Connected Labs and technical sources.</h2><p>Use these routes to investigate the adjacent business object rather than treating SEPA as an isolated master-data field.</p></header>
    <div class="research-route-list sepa-related-routes">
      <a href="/labs/enterprise-context/master-data/"><span>BP</span><strong>Master Data</strong><small>Customer identity, FI extension and bank-account prerequisites</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-context/sales-processes/"><span>SD</span><strong>Sales Process Atlas</strong><small>How SD partner functions and sales-document decisions affect billing</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-context/billing/"><span>AR</span><strong>Billing</strong><small>Invoice creation, transfer to FI and accounting boundaries</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-context/finance-logistics/payments-banks-rejections/"><span>FI</span><strong>Payments, Banks and Rejections</strong><small>Proposals, bank execution, returns, clearing and reconciliation</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-context/procurement/suppliers/automatic-payments/"><span>APP</span><strong>Automatic Payments</strong><small>Learn the payment-program decision model; supplier flow is a separate scenario</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </div>
    <div class="sepa-references">
      <h3>Primary documentation</h3>
      <ul>
        <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/6f1d59146ff144748b1ee315026ff2df.html" target="_blank" rel="noopener">SAP S/4HANA 2025 FPS02 — Process Sales Document with SEPA Mandate</a></li>
        <li><a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD_PE/7b24a64d9d0941bda1afa753263d9e39/feb4509d0e8742238b0c9572672ea7d7.html" target="_blank" rel="noopener">SAP S/4HANA 2025 FPS01 — Billing Document with SEPA Mandate</a></li>
        <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/451fcec7eb02466aab0dfef5a2e54901.html" target="_blank" rel="noopener">SAP — Creating, Displaying and Changing Mandates</a></li>
        <li><a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/1d1601c422e94d569d37263875ee4ff6.html" target="_blank" rel="noopener">SAP Cloud Public Edition — FI - SEPA Mandate migration</a></li>
        <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/ee6ff9b281d8448f96b4fe6c89f2bdc8/59e1eb1e333949ebb74c6a99c1fbd13b.html" target="_blank" rel="noopener">SAP — I_CustomerSEPAMandate released interface</a></li>
        <li><a href="https://www.europeanpaymentscouncil.eu/what-we-do/epc-payment-schemes/sepa-direct-debit/sdd-mandate" target="_blank" rel="noopener">European Payments Council — SDD Mandate</a></li>
      </ul>
      <p>Checked 4 November 2026 against the sources linked above. This is technical and process guidance, not legal advice. All customer and mandate identifiers in the migration example are synthetic.</p>
    </div>
  </section>
  <footer class="sepa-guide-footer" data-reveal><p>Technical field guide by <a href="/about/">Dzmitryi Kharlanau</a> · reviewed 4 November 2026. Verify release-specific SAP behavior and current payment-scheme requirements before production use.</p></footer>
</article>
