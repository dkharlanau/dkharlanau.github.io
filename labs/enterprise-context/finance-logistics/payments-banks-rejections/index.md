---
layout: default
title: "Payments, Banks and Rejections — SAP S/4HANA Lead Lab"
description: "A practical SAP S/4HANA guide to automatic payments, bank statements, direct debits, payment rejections, FI-AR and FI-CA boundaries, and reconciliation."
permalink: /labs/enterprise-context/finance-logistics/payments-banks-rejections/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-24
last_reviewed: 2026-09-24
review_method: "SAP S/4HANA 2025 FPS01 primary-source recheck + FI-AR/FI-CA boundary review + full editorial rewrite"
hide_global_cta: true
career_impact: mapped
career_skills:
  - sales-o2c
  - sales-diagnostics
  - delivery-ams
tags:
  - sap-s4hana
  - sap-fi
  - sap-ar
  - fi-ca
  - f110
  - direct-debit
  - sepa
  - bank-statement
  - payments
  - rejection-processing
  - troubleshooting
semantic_links:
  - type: "parent_topic"
    title: "FI/CO for Logistics"
    url: "/labs/enterprise-context/finance-logistics/"
  - type: "related_topic"
    title: "Billing"
    url: "/labs/enterprise-context/billing/"
  - type: "related_topic"
    title: "Sales Diagnostics"
    url: "/labs/enterprise-context/sales-diagnostics/"
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/finance-logistics/">FI/CO for Logistics</a></li><li aria-current="page">Payments, Banks and Rejections</li></ol></nav>

<div class="research-canvas context-graph">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Finance bridge / payments and bank exceptions</p>
      <h1>A payment is a chain of states,<br />not one green status.</h1>
      <p>SAP can select an open item, decide how it should be paid or collected, post the accounting result, create a bank-facing instruction, receive bank evidence, and clear or reopen the customer position. The useful diagnostic question is simple: which of those states is the first one that no longer matches reality?</p>
      <a class="research-canvas__button" href="#payment-flow">Follow the money <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Payment process model">
      <p>Working model</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Select</strong><small>Which item should move?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Send</strong><small>What instruction left SAP?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Reconcile</strong><small>What did the bank actually do?</small></div>
      <em>FI-AR and FI-CA share the bank boundary, but not the same processing model.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_balance</span>
    <div>
      <p><strong>Keep four states separate:</strong> payment proposal, SAP posting, bank execution, and final reconciliation.</p>
      <p>A successful proposal does not prove that a payment was posted. A posted payment does not prove that the bank accepted it. A bank execution does not prove that SAP cleared the right item.</p>
    </div>
    <a href="#diagnostic">Trace the first wrong state <span class="material-symbols-outlined" aria-hidden="true">route</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">First boundary</p>
      <h2>Start by naming the subledger model.</h2>
      <p>FI-AR and FI-CA both move money between a business partner and a bank, but they do not use the same operational objects. Reusing one recovery procedure in the other area is an easy way to make a payment incident worse.</p>
    </header>
    <div class="ecg-decision-columns">
      <div>
        <h3>FI-AR</h3>
        <p>Classic customer accounting works with customer open items, the automatic payment program, payment media, bank clearing, and bank-statement processing. In SAP S/4HANA 2025 FPS01, the <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3eb1567cf97543c08087efb0936964e6/45698054f87c033de10000000a441470.html" target="_blank" rel="noopener">Manage Automatic Payments</a> app can schedule proposals or payments and create payment media after successful runs.</p>
      </div>
      <div>
        <h3>FI-CA</h3>
        <p>Contract Accounting has its own mass-payment and collection model. It also supports objects such as payment orders, where the open item can deliberately stay open until bank execution is confirmed and the payment-order lot is posted.</p>
      </div>
      <div>
        <h3>What crosses both</h3>
        <p>The bank remains an external source of truth. Outbound instructions, inbound statements, rejection messages, references, value dates, and fees have to be reconciled with the SAP accounting state.</p>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="payment-flow" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Automatic payment flow</p>
      <h2>The payment program makes several decisions before money reaches the bank.</h2>
      <p>SAP documents the automatic payment run as a sequence that selects open items, groups and processes them, chooses payment methods and bank details, determines accounts and value dates, posts the payment, and creates the data needed for payment media. That sequence is more useful than memorizing a transaction-code list.</p>
    </header>

    <h3>1. Selection and proposal</h3>
    <p>The first question is whether the expected open item entered the run. Company code, payment method, due date, payment block, master data, bank data, and other process-specific conditions can all affect selection. If the item appears as an exception, inspect the proposal evidence before changing configuration. SAP provides proposal review and exception analysis in <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/de567c542889063de10000000a441470.html" target="_blank" rel="noopener">Revise Payment Proposals</a>.</p>

    <h3>2. Payment posting</h3>
    <p>Once the run posts the payment, SAP has changed the accounting state. That is a different boundary from the proposal. If a correction is required after posting, treat it as an accounting reversal or return problem rather than as a proposal edit.</p>

    <h3>3. Payment medium and bank handoff</h3>
    <p>The payment medium carries the bank-facing instruction. A correct accounting document does not prove that the generated file, reference, bank account, format mapping, or downstream bank channel is correct. If the bank rejects the instruction, compare what SAP posted with what actually left the system.</p>

    <h3>4. Bank evidence and reconciliation</h3>
    <p>The bank statement closes the loop. It can confirm execution, expose a return, or provide information that SAP must use to post and clear. If automatic processing cannot post or clear a statement item, SAP S/4HANA provides the <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/a8aaa72cb39a48528b39b61623c15baa/bc1fe656fe590950e10000000a44147b.html" target="_blank" rel="noopener">Reprocess Bank Statement Items</a> app for manual or rule-based reprocessing.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Bank statement logic</p>
      <h2>Import, interpretation, posting, and clearing are separate steps.</h2>
      <p>“The bank statement was imported” is useful evidence, but it is not the end of the process. A statement item still has to be interpreted, mapped to the right accounting action, posted, and matched to the intended open item or G/L account.</p>
    </header>
    <p>Current SAP S/4HANA documentation separates bank-statement processing rules from the reprocessing worklist. <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/d6fe6526b26f46e59d9d1dd0f7427fe3.html" target="_blank" rel="noopener">Manage Processing Rules - For Bank Statements</a> defines conditions and actions for G/L and AP/AR postings; Reprocess Bank Statement Items handles items that were not completed automatically.</p>
    <p>This gives a clean diagnostic split. If the bank file itself is wrong, the defect sits before statement processing. If the file imports but a line receives the wrong action, inspect interpretation and processing rules. If the posting is correct but the customer item remains open, inspect reference matching and clearing rather than the bank import.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">SEPA direct debit</p>
      <h2>The mandate and the collection are related, but they are not the same object.</h2>
      <p>A SEPA mandate gives authority to debit the payer's account. The payment process then selects a valid mandate and creates the collection instruction. Pre-notification is a separate communication step that informs the payer about the planned debit.</p>
    </header>
    <p>In SAP Sales, mandates used for SEPA direct debit are managed in FI-AR and can be assigned to sales documents. SAP also recommends the FI-AR pre-notification function when more precise transfer-date and amount handling is needed. See <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/ad0bef26b37045ddb256f0bcfb8ff445.html" target="_blank" rel="noopener">SEPA Direct Debits in SD</a>.</p>
    <p>FI-CA has its own pre-notification run. SAP S/4HANA 2025 FPS01 documents that the run selects and groups items, chooses payment method and bank data, selects the mandate, and creates pre-notification data without posting documents or creating payment orders. See <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/9442486404b54071b4ebeab6a16628e7/bc874f2966d4434cb4b6a6794f0fac70.html" target="_blank" rel="noopener">Pre-Notification of SEPA Direct Debits</a>.</p>
  </section>

  <section class="research-canvas__inventory" id="returns" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Rejection versus return</p>
      <h2>First establish when the bank said “no.”</h2>
      <p>A rejected instruction and a returned collection can produce similar user language but represent different timelines.</p>
    </header>
    <div class="ecg-decision-columns">
      <div>
        <h3>Rejected before settlement</h3>
        <p>The bank or payment channel does not accept the instruction. The investigation starts with the payment medium, bank-facing format, reference, bank data, and rejection evidence. Do not assume that a later bank-statement return has already happened.</p>
      </div>
      <div>
        <h3>Returned after an earlier collection</h3>
        <p>The process had already reached a stronger accounting state, often including clearing. If the customer still owes the money, the final SAP state must not leave the receivable falsely settled. The exact reset and return postings depend on the subledger and configured process.</p>
      </div>
      <div>
        <h3>Bank fee</h3>
        <p>A fee is a separate financial effect from the returned principal. Diagnose the returned payment and the charge independently even when the bank reports them in one statement context.</p>
      </div>
    </div>
    <p>For example, suppose EUR 1,000 was collected and the bank later returns it with a EUR 5 fee. The useful end state is not “post EUR 1,005 somewhere.” SAP must identify the original payment, reflect that the EUR 1,000 receivable is no longer settled when the debt still exists, and account for the EUR 5 fee according to the configured process.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">FI-CA payment orders</p>
      <h2>Payment initiation can deliberately happen before open-item clearing.</h2>
      <p>FI-CA payment orders are a useful counterexample to the assumption that a successful payment run must clear the open item immediately.</p>
    </header>
    <p>SAP documents a model in which the payment run creates a payment order and sends the bank instruction while the actual posting is deferred. The bank statement later confirms execution; posting the payment-order lot then selects the paid open items by payment-order number, clears them, and marks the payment order as executed. See <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/cdccca8e03d74101a0135863bc522b49/0d0bc5536a51204be10000000a174cb4.html" target="_blank" rel="noopener">Payment Orders for Direct Debits and Bank Transfers</a>.</p>
    <p>This is exactly why the subledger boundary matters. An FI-CA payment order is not a generic explanation for every FI-AR payment that remains open after a run.</p>
  </section>

  <section class="research-canvas__inventory" id="diagnostic" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Incident diagnosis</p>
      <h2>Trace evidence in the same order that the money process runs.</h2>
      <p>The first wrong state usually points to the right owner faster than the loudest error message.</p>
    </header>
    <div class="ecg-determination-list">
      <article class="ecg-determination-detail">
        <header><div><span>01</span><small>intent</small></div><h3>What money movement should have happened?</h3><p class="ecg-question">Outgoing payment, customer collection, refund, bank-statement clearing, or return?</p></header>
        <p>Capture the business partner, company code, amount, currency, due date, payment method, and expected accounting result before opening configuration.</p>
      </article>
      <article class="ecg-determination-detail">
        <header><div><span>02</span><small>model</small></div><h3>Which subledger and processing model owns it?</h3><p class="ecg-question">FI-AR or FI-CA? Immediate posting or a payment-order model?</p></header>
        <p>This determines which logs, clearing points, and recovery actions are meaningful.</p>
      </article>
      <article class="ecg-determination-detail">
        <header><div><span>03</span><small>selection</small></div><h3>Did the item enter the proposal?</h3><p class="ecg-question">If not, what exact exception or missing prerequisite explains the exclusion?</p></header>
        <p>Use proposal and application evidence. Do not jump from “not paid” to “bank configuration” when the item never passed selection.</p>
      </article>
      <article class="ecg-determination-detail">
        <header><div><span>04</span><small>bank boundary</small></div><h3>What left SAP and what came back?</h3><p class="ecg-question">Accepted, rejected, executed, returned, or not identifiable?</p></header>
        <p>Compare the outbound payment instruction with the bank response or statement. References matter because they connect external evidence back to the SAP payment.</p>
      </article>
      <article class="ecg-determination-detail">
        <header><div><span>05</span><small>final state</small></div><h3>Do bank reality and SAP accounting agree?</h3><p class="ecg-question">Is the intended customer item open or cleared, is the bank clearing position correct, and are return fees separated?</p></header>
        <p>Close the incident only when the business state and the accounting state tell the same story.</p>
      </article>
    </div>
  </section>

  <section class="research-canvas__inventory" id="practice" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">A compact way to explain an incident</p>
      <h2>Describe the state transition, not a list of transactions.</h2>
    </header>
    <p>A strong explanation can be short: “The item entered the payment proposal and SAP posted the payment, but the bank rejected the outbound instruction. I would keep the accounting state, payment medium, bank response, and any required reversal as separate checkpoints. If instead the bank executed the payment and SAP still shows an open clearing position, I would move to bank-statement interpretation and matching rather than changing the payment proposal.”</p>
    <p>The same structure works for returns: identify the original payment, establish whether settlement had already happened, then prove the final receivable and bank state. It is more reliable than starting with F110, FBZP, a BAdI, or a guessed return reason.</p>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">fact_check</span>
    <div>
      <p><strong>Verification boundary:</strong> the FI-AR payment-run, bank-statement, SEPA, and FI-CA payment-order concepts on this page were rechecked against current SAP documentation. Detailed country-specific rejection formats, classic Customizing paths, bank-specific return codes, and customer enhancements still depend on the target release, deployment model, localization, and bank contract.</p>
      <p>This page therefore remains a review candidate rather than a verified implementation recipe.</p>
    </div>
    <a href="/labs/assessment/factual-review/">Use the factual review process <span class="material-symbols-outlined" aria-hidden="true">fact_check</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Primary references</p>
      <h2>Use the product documentation for release-sensitive behavior.</h2>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3eb1567cf97543c08087efb0936964e6/45698054f87c033de10000000a441470.html" target="_blank" rel="noopener"><span>SAP</span><strong>Manage Automatic Payments</strong><small>SAP S/4HANA 2025 FPS01: proposals, payment runs, payment media, and direct-debit pre-notifications.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/de567c542889063de10000000a441470.html" target="_blank" rel="noopener"><span>SAP</span><strong>Revise Payment Proposals</strong><small>SAP S/4HANA 2025 FPS01: proposal exceptions and payment-related corrections before execution.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/a8aaa72cb39a48528b39b61623c15baa/bc1fe656fe590950e10000000a44147b.html" target="_blank" rel="noopener"><span>SAP</span><strong>Reprocess Bank Statement Items</strong><small>Manual and rule-based reprocessing when automatic posting or clearing does not finish.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/d6fe6526b26f46e59d9d1dd0f7427fe3.html" target="_blank" rel="noopener"><span>SAP</span><strong>Manage Processing Rules - For Bank Statements</strong><small>SAP S/4HANA 2025 FPS01: conditions and actions for bank-statement posting and clearing.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/ad0bef26b37045ddb256f0bcfb8ff445.html" target="_blank" rel="noopener"><span>SAP</span><strong>SEPA Direct Debits in SD</strong><small>SAP S/4HANA 2025 FPS01: mandate use and FI-AR pre-notification integration with Sales.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/9442486404b54071b4ebeab6a16628e7/bc874f2966d4434cb4b6a6794f0fac70.html" target="_blank" rel="noopener"><span>SAP</span><strong>Pre-Notification of SEPA Direct Debits</strong><small>SAP S/4HANA 2025 FPS01 Contract Accounting pre-notification process.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/cdccca8e03d74101a0135863bc522b49/0d0bc5536a51204be10000000a174cb4.html" target="_blank" rel="noopener"><span>SAP</span><strong>Payment Orders for Direct Debits and Bank Transfers</strong><small>FI-CA payment-order execution and clearing after bank confirmation.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
