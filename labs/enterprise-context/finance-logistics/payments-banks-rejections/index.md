---
layout: default
title: "Payments, Banks and Rejections — SAP S/4HANA Lead Lab"
description: "A practical SAP S/4HANA study module for customer collections, payment runs, bank statements, direct debit returns, FI-AR and FI-CA boundaries, and rejection diagnostics."
permalink: /labs/enterprise-context/finance-logistics/payments-banks-rejections/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-11
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
      <h1>Follow the payment.<br />Then follow the exception.</h1>
      <p>A payment is not one event. SAP can select an item, create a payment instruction, post accounting, send a bank file, receive bank confirmation, clear an account, and later reopen the original receivable after a rejection. A Lead must know which step is wrong before changing configuration.</p>
      <a class="research-canvas__button" href="#payment-flow">Trace the flow <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Payment diagnostic model">
      <p>Diagnostic model</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Select</strong><small>Which item should move?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Send</strong><small>What did SAP tell the bank?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Confirm</strong><small>What did the bank report back?</small></div>
      <em>Selection, posting, bank execution, and reconciliation are different states.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_balance</span>
    <p><strong>Lead rule:</strong> do not say “the payment failed” until you can name the failed layer. Proposal failure, payment posting failure, file rejection, bank-statement mapping failure, and a returned direct debit are different problems with different owners.</p>
    <a href="#diagnostic">Open the diagnostic path <span class="material-symbols-outlined" aria-hidden="true">route</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">First boundary</p><h2>Do not mix FI-AR and FI-CA in one answer.</h2><p>Both areas handle payments, but the operating model and objects are not the same. Start by saying which subledger model you are discussing.</p></header>
    <div class="ecg-decision-columns">
      <div><h3>FI-AR / classic customer accounting</h3><ul><li>Customer open items sit in Accounts Receivable.</li><li>Automatic payment processing is commonly discussed with F110 or the Manage Automatic Payments app.</li><li>Payment methods, house banks, payment media, and bank clearing connect the customer item to the bank process.</li><li>Electronic Bank Statement processing completes the cash-side reconciliation.</li></ul></div>
      <div><h3>FI-CA / Contract Accounting</h3><ul><li>Mass payment processing uses FI-CA payment-run logic such as FPY1.</li><li>SEPA mandate and pre-notification handling can be part of the collection process.</li><li>Payment orders can delay open-item clearing until execution is confirmed by the bank statement.</li><li>Returns and rejection files have FI-CA-specific processing objects and reports.</li></ul></div>
      <div><h3>What a Lead says</h3><ul><li>“First I identify the subledger and payment model.”</li><li>“Then I trace the payment through SAP and the bank.”</li><li>“I do not reuse an FI-CA recovery step as if it were standard FI-AR behavior.”</li><li>“I verify release-specific apps and configuration before proposing a fix.”</li></ul></div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="payment-flow" data-reveal>
    <header><p class="research-canvas__eyebrow">Automatic payment flow</p><h2>Five phases explain most F110 questions.</h2><p>Think of the payment run as a controlled pipeline. Each phase creates evidence for the next one.</p></header>
    <div class="ecg-determination-list">
      <article class="ecg-determination-detail"><header><div><span>01</span><small>scope</small></div><h3>Parameters</h3><p class="ecg-question">What should the run consider?</p></header><div class="ecg-decision-columns"><div><h4>Define</h4><ul><li>Run and posting dates</li><li>Company codes</li><li>Payment methods</li><li>Selection scope</li></ul></div><div><h4>Evidence</h4><p>Saved run parameters and selection settings.</p></div><div><h4>Failure pattern</h4><p>The expected item never enters the proposal because the scope, due date, block, payment method, or master data does not fit.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>02</span><small>decision</small></div><h3>Proposal</h3><p class="ecg-question">Which items can actually be paid or collected?</p></header><div class="ecg-decision-columns"><div><h4>Read</h4><ul><li>Selected open items</li><li>Exceptions</li><li>Payment method</li><li>Bank determination</li></ul></div><div><h4>Lead action</h4><p>Use the proposal log and exception list before changing configuration.</p></div><div><h4>Failure pattern</h4><p>The item is selected but blocked by missing or inconsistent payment data.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>03</span><small>posting</small></div><h3>Payment execution</h3><p class="ecg-question">What accounting state did SAP create?</p></header><div class="ecg-decision-columns"><div><h4>Expected</h4><p>The run creates the payment accounting result and moves the process toward a bank clearing position.</p></div><div><h4>Check</h4><ul><li>Payment document</li><li>Customer clearing status</li><li>Bank clearing account</li></ul></div><div><h4>Recovery</h4><p>After posting, reversal is an accounting decision. Do not treat it like editing a proposal.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>04</span><small>bank file</small></div><h3>Payment medium</h3><p class="ecg-question">What instruction left SAP?</p></header><div class="ecg-decision-columns"><div><h4>Examples</h4><ul><li>SEPA XML</li><li>Transfer file</li><li>Other bank-specific formats</li></ul></div><div><h4>Check</h4><ul><li>Format mapping</li><li>Payment method assignment</li><li>House-bank data</li><li>Note-to-payee content</li></ul></div><div><h4>Failure pattern</h4><p>SAP posted the payment, but the bank file is wrong or rejected.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>05</span><small>confirmation</small></div><h3>Bank statement and reconciliation</h3><p class="ecg-question">What did the bank actually execute?</p></header><div class="ecg-decision-columns"><div><h4>Evidence</h4><ul><li>Bank statement item</li><li>Posting rule</li><li>Matched reference</li><li>Clearing result</li></ul></div><div><h4>Goal</h4><p>The operational bank result and SAP accounting state agree.</p></div><div><h4>Failure pattern</h4><p>The bank executed the transaction, but SAP cannot identify, post, or clear the statement item automatically.</p></div></div></article>
    </div>
    <p class="ecg-caption"><strong>Memory line:</strong> parameters → proposal → payment → payment medium → bank statement. If you can say which stage owns the defect, your answer is already much stronger.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Configuration map</p><h2>Know the stack without turning the answer into a transaction-code dump.</h2><p>The working note uses these classic configuration references. Exact availability and usage can differ by S/4HANA release and deployment model, so treat them as checkpoints, not as a universal recipe.</p></header>
    <div class="ecg-input-grid">
      <article><span>FBZP</span><h3>Payment program configuration</h3><p>Connect payment methods, company-code rules, bank determination, and the payment-medium decision.</p><p><strong>Ask:</strong> can the run determine how and from which bank the payment should be processed?</p></article>
      <article><span>DMEEX</span><h3>Payment format mapping</h3><p>Defines or extends the structure used to create the bank-facing payment medium.</p><p><strong>Ask:</strong> is the bank receiving the structure it expects?</p></article>
      <article><span>OBPM1</span><h3>Payment medium format</h3><p>Classic configuration reference for payment-medium formats.</p><p><strong>Ask:</strong> which format is assigned to the payment process?</p></article>
      <article><span>OBPM2</span><h3>Note to payee</h3><p>Controls information placed in the payment reference area.</p><p><strong>Ask:</strong> will the bank or return process be able to identify the original payment?</p></article>
      <article><span>OBPM3</span><h3>Format parameters and events</h3><p>Classic customer-format configuration reference.</p><p><strong>Ask:</strong> are customer-specific parameters changing standard output behavior?</p></article>
      <article><span>OBPM4</span><h3>Selection variants</h3><p>Classic selection-variant reference used in payment-medium generation scenarios.</p><p><strong>Ask:</strong> is the generation route using the expected variant and format?</p></article>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <p><strong>Assessment signal:</strong> name configuration only after you have explained the business decision it controls. “Check FBZP” is weak. “I would first verify whether the payment method, company-code rule, and bank determination allow the item to enter the expected payment path; then I would inspect the payment program configuration” is Lead-level reasoning.</p>
    <a href="#practice">Practice the answer <span class="material-symbols-outlined" aria-hidden="true">school</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">SEPA direct debit</p><h2>The mandate proves authority. Pre-notification controls timing.</h2><p>SEPA collection is not just a bank format. The process depends on valid customer authorization, the selected mandate, and pre-notification rules.</p></header>
    <div class="ecg-decision-columns">
      <div><h3>Mandate</h3><ul><li>The debtor authorizes the creditor to collect the amount.</li><li>SAP uses mandate data as part of SEPA direct-debit processing.</li><li>SD can use mandates managed in FI-AR.</li></ul></div>
      <div><h3>Pre-notification</h3><ul><li>The payer is informed before the debit.</li><li>SAP supports creation of direct-debit pre-notifications in payment and invoicing scenarios.</li><li>A common SEPA baseline is 14 calendar days before the due date unless another period is agreed.</li></ul></div>
      <div><h3>Diagnostic question</h3><ul><li>Does the item require a pre-notification?</li><li>Was a suitable pre-notification created?</li><li>Does it match the intended mandate, amount, and collection date?</li><li>If FI-CA rejects the item, inspect the application log before changing the mandate.</li></ul></div>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Electronic Bank Statement</p><h2>The bank statement is the return path from financial reality.</h2><p>Payment creation tells the bank what SAP wants. The bank statement tells SAP what actually happened.</p></header>
    <div class="ecg-input-grid">
      <article><span>F1680</span><h3>Manage Incoming Payment Files</h3><p>Current SAP documentation describes this app for importing electronic payment files including bank statements and payment rejections. Parameter sets can control import behavior.</p></article>
      <article><span>F1520</span><h3>Reprocess Bank Statement Items</h3><p>Use the app when automatic posting and clearing did not complete. It supports manual or rule-based reprocessing and open-item assignment.</p></article>
      <article><span>FF_5</span><h3>Classic bank-statement import</h3><p>A classic SAP GUI reference for electronic bank statement upload in on-premise style landscapes.</p></article>
      <article><span>FEB_BSPROC</span><h3>Classic post-processing</h3><p>Use post-processing when an imported bank statement item exists but needs additional assignment or correction.</p></article>
      <article><span>RULE</span><h3>Posting logic</h3><p>Transaction types, posting rules, account symbols, and interpretation logic connect bank codes to accounting actions.</p></article>
      <article><span>PROOF</span><h3>Reconciliation evidence</h3><p>Do not close the incident because the file imported. Confirm the resulting posting and the expected clearing state.</p></article>
    </div>
  </section>

  <section class="research-canvas__inventory" id="returns" data-reveal>
    <header><p class="research-canvas__eyebrow">Direct debit return</p><h2>A return must undo business certainty, not only post a bank charge.</h2><p>Consider a simple case: SAP collected EUR 1,000. The bank later returns the debit and charges EUR 5. The statement can represent EUR 1,005 as one economic event, while SAP still needs to separate the returned payment from the bank fee.</p></header>
    <div class="ecg-determination-list">
      <article class="ecg-determination-detail"><header><div><span>A</span><small>identify</small></div><h3>Find the original payment</h3><p class="ecg-question">Can the bank reference be connected to the payment that cleared the customer invoice?</p></header><div class="ecg-decision-columns"><div><h4>Evidence</h4><p>Payment document, bank reference, note to payee, amount, customer account.</p></div><div><h4>Risk</h4><p>If the reference cannot be resolved, automatic return processing cannot safely reset the original clearing.</p></div><div><h4>Lead question</h4><p>Was the identification problem created by the bank file, payment-medium reference, or statement interpretation?</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>B</span><small>reverse certainty</small></div><h3>Reset the clearing and reopen the receivable</h3><p class="ecg-question">If the money did not stay collected, is the original invoice open again?</p></header><div class="ecg-decision-columns"><div><h4>Business result</h4><p>The customer still owes the amount, so the receivable must return to an open state.</p></div><div><h4>Accounting result</h4><p>The return processing must reverse the previous clearing relationship in a controlled way.</p></div><div><h4>Do not</h4><p>Post only the bank difference while leaving the customer invoice falsely cleared.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>C</span><small>fee</small></div><h3>Separate the bank charge</h3><p class="ecg-question">Is the EUR 5 fee posted separately from the EUR 1,000 returned collection?</p></header><div class="ecg-decision-columns"><div><h4>Why</h4><p>The fee is a different accounting event with different account determination and reporting.</p></div><div><h4>Configuration</h4><p>The working note describes separate posting rules for the return and the charge.</p></div><div><h4>Extension</h4><p>Where the fee must be extracted from note-to-payee content, a release-specific enhancement can be required.</p></div></div></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Return configuration</p><h2>Translate the bank language into an SAP business action.</h2><p>The supplied working note describes this classic return-processing chain. Use it as a diagnostic map and verify exact configuration names against the target release before implementation.</p></header>
    <div class="ecg-control-stack">
      <article><span>1</span><h3>External bank code</h3><p>Identify the Business Transaction Code or return code supplied by the bank.</p><strong>Question: what did the bank mean?</strong></article>
      <article><span>2</span><h3>Internal return reason</h3><p>Map the bank code to an SAP return reason that the process can understand.</p><strong>Question: which business exception does SAP record?</strong></article>
      <article><span>3</span><h3>Posting rules</h3><p>Determine how the returned collection and any bank fee should post.</p><strong>Question: which two financial effects must be separated?</strong></article>
      <article><span>4</span><h3>Reset clearing</h3><p>Where configured and appropriate, reset the clearing of the original payment so the receivable becomes open again.</p><strong>Question: does customer debt now reflect reality?</strong></article>
      <article><span>5</span><h3>Interpret the reference</h3><p>The working note points to document-number search logic for finding the original payment from the bank reference.</p><strong>Question: can SAP prove which payment is being returned?</strong></article>
      <article><span>6</span><h3>Apply controlled extensions</h3><p>Classic enhancement references in the note include FIEB_RET_CHANGE_DOC and FIEB_RETURNS_ADDIN for open-item changes or return-charge handling.</p><strong>Question: is custom logic fixing a real bank-format gap or hiding weak standard configuration?</strong></article>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">warning</span>
    <p><strong>Important separation:</strong> a rejected payment file and a returned payment are not automatically the same incident. A bank can reject an instruction before settlement, or return a collection after the original payment process has already created accounting and clearing effects. Diagnose the timeline first.</p>
    <a href="#diagnostic">Trace the timeline <span class="material-symbols-outlined" aria-hidden="true">timeline</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">FI-CA payment orders</p><h2>Sometimes clearing waits for bank confirmation.</h2><p>FI-CA payment orders provide a useful example of why “payment run completed” does not always mean “open item cleared.”</p></header>
    <div class="ecg-decision-columns">
      <div><h3>Payment run</h3><p>The run creates a payment order and the bank-facing instruction. The business intention is recorded, but the open item can remain open.</p></div>
      <div><h3>Bank confirmation</h3><p>The bank statement reports that the payment order was executed. This is the external proof that the money movement occurred.</p></div>
      <div><h3>Payment-order lot</h3><p>When the reported order is posted, SAP uses the payment-order reference to select and clear the paid open items and marks the order as executed.</p></div>
    </div>
    <p class="ecg-caption"><strong>Assessment point:</strong> this model is useful when you need exact open-item status until bank execution is known. Do not apply it blindly to every FI-AR payment scenario.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Separate rejection XML</p><h2>pain.002 can be a separate return channel in FI-CA.</h2><p>SAP documents report RFKKSEPA_DD_RJCT for SEPA direct-debit rejections delivered separately from the regular bank statement.</p></header>
    <div class="ecg-decision-columns">
      <div><h3>Input</h3><ul><li>Bank sends a pain.002.001.03 rejection message.</li><li>The rejection is not part of the normal bank statement.</li><li>SAP transforms the XML into an internal structure and MultiCash-style processing input.</li></ul></div>
      <div><h3>Technical route</h3><ul><li>Report RFKKSEPA_DD_RJCT</li><li>XSLT transformation</li><li>View V_FKK_SEPA_XSLT</li><li>Follow-on FI-CA bank/return processing</li></ul></div>
      <div><h3>Critical control</h3><ul><li>Do not import the same return through pain.002 and the normal bank statement.</li><li>Duplicate input can create duplicate return processing.</li><li>Confirm the bank contract: which channel is authoritative?</li></ul></div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="diagnostic" data-reveal>
    <header><p class="research-canvas__eyebrow">Diagnostic runtime</p><h2>Use the first wrong state, not the loudest error message.</h2><p>This sequence works for most payment and rejection incidents.</p></header>
    <div class="ecg-determination-list">
      <article class="ecg-determination-detail"><header><div><span>01</span><small>business state</small></div><h3>What should have happened?</h3><p class="ecg-question">Refund, customer collection, outgoing payment, payment-order execution, or return?</p></header><div class="ecg-decision-columns"><div><h4>Collect</h4><p>Customer, company code, amount, currency, due date, payment method, business reason.</p></div><div><h4>Do not</h4><p>Start from a transaction code before you know the intended money movement.</p></div><div><h4>Owner</h4><p>Business process owner plus FI payment owner.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>02</span><small>subledger</small></div><h3>Which payment model?</h3><p class="ecg-question">FI-AR or FI-CA? Standard payment document or payment order?</p></header><div class="ecg-decision-columns"><div><h4>Why</h4><p>The clearing point, return processing, and monitoring tools depend on this answer.</p></div><div><h4>Evidence</h4><p>Account type, payment document/order, application log, process configuration.</p></div><div><h4>Risk</h4><p>Using the wrong model leads to the wrong recovery action.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>03</span><small>payment run</small></div><h3>Did the item pass selection and proposal?</h3><p class="ecg-question">Was the expected open item selected, and if not, what exact exception explains it?</p></header><div class="ecg-decision-columns"><div><h4>Check</h4><p>Proposal log, blocks, due date, payment method, bank data, mandate/pre-notification where relevant.</p></div><div><h4>Proof</h4><p>Use the exception reason, not a guessed configuration cause.</p></div><div><h4>Next</h4><p>If proposal is correct, move to payment posting and medium generation.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>04</span><small>bank boundary</small></div><h3>What left SAP, and what came back?</h3><p class="ecg-question">Did the file contain the expected instruction and reference? Did the bank accept, reject, execute, or return it?</p></header><div class="ecg-decision-columns"><div><h4>Outbound</h4><p>Payment medium, format, account, reference, amount.</p></div><div><h4>Inbound</h4><p>Bank statement, rejection file, reason code, value date, fee.</p></div><div><h4>Owner</h4><p>FI plus bank integration or treasury, depending on landscape.</p></div></div></article>
      <article class="ecg-determination-detail"><header><div><span>05</span><small>accounting</small></div><h3>Does SAP now match the bank reality?</h3><p class="ecg-question">Are the customer item, payment document, clearing account, returned item, and bank fee in the expected final state?</p></header><div class="ecg-decision-columns"><div><h4>Compare</h4><p>Open/cleared customer items, payment document, bank clearing, statement posting.</p></div><div><h4>For return</h4><p>Confirm that the receivable is reopened when the customer still owes the money.</p></div><div><h4>Close</h4><p>Only after business state and accounting state agree.</p></div></div></article>
    </div>
  </section>

  <section class="research-canvas__inventory" id="practice" data-reveal>
    <header><p class="research-canvas__eyebrow">Explain it in the assessment</p><h2>Use one stable answer structure.</h2><p>Business event → payment model → SAP stage → bank evidence → accounting state → recovery.</p></header>
    <div class="ecg-input-grid">
      <article><span>60S</span><h3>Payment run</h3><p>“I separate the payment process into proposal, posting, payment medium, and bank reconciliation. If F110 does not process an item, I start with the proposal exception and master or payment data. If SAP posts successfully but the bank rejects the file, I move to the payment-medium and bank-integration layer. If the bank executes the transaction but clearing is still open, I inspect the bank statement and matching logic. This keeps the diagnosis on the first wrong state.”</p></article>
      <article><span>60S</span><h3>Direct debit return</h3><p>“A returned direct debit is not only a bank fee. I first identify the original payment. Then I check whether clearing was reset so the customer receivable is open again. I separate the returned amount from the bank charge, verify the return reason and posting rules, and reconcile the final customer and bank-clearing state.”</p></article>
      <article><span>60S</span><h3>FI-CA payment order</h3><p>“With a payment order, the payment run can create the instruction without immediately clearing the open item. The bank statement confirms execution. Posting the payment-order lot then clears the related items. I use this example to show that payment initiation and final clearing can be separate control points.”</p></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Fill the gaps</p><h2>Test whether you can rebuild the flow without reading it.</h2><p>Say the missing term aloud before opening the answer.</p></header>
    <div class="ecg-control-stack">
      <article><span>1</span><h3>F110 flow</h3><p>Parameters → ______ → Payment → Payment medium → Bank statement.</p><details><summary>Show answer</summary><p><strong>Proposal.</strong> This is where you inspect selection and exceptions before money movement.</p></details></article>
      <article><span>2</span><h3>Bank statement failure</h3><p>If the bank statement imported but an item did not post or clear automatically, use ______ to reprocess it in Fiori.</p><details><summary>Show answer</summary><p><strong>Reprocess Bank Statement Items, F1520.</strong></p></details></article>
      <article><span>3</span><h3>Return logic</h3><p>A returned direct debit should normally make the original customer ______ open again when the debt still exists.</p><details><summary>Show answer</summary><p><strong>Receivable or invoice.</strong> The prior clearing must no longer show the debt as settled.</p></details></article>
      <article><span>4</span><h3>SEPA control</h3><p>The ______ authorizes the debit; the pre-notification tells the payer about the planned collection.</p><details><summary>Show answer</summary><p><strong>Mandate.</strong></p></details></article>
      <article><span>5</span><h3>FI-CA payment order</h3><p>With payment orders, open-item clearing can wait until the ______ confirms execution.</p><details><summary>Show answer</summary><p><strong>Bank statement.</strong></p></details></article>
      <article><span>6</span><h3>pain.002 control</h3><p>Do not process the same rejection from pain.002 and the regular ______, or you can import the return twice.</p><details><summary>Show answer</summary><p><strong>Bank statement.</strong></p></details></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Lead questions</p><h2>Answer the question, then defend the boundary.</h2><p>Use these prompts as short mock-assessment drills.</p></header>
    <div class="research-route-list">
      <a href="#payment-flow"><span>Q1</span><strong>F110 proposal is missing an expected customer item. Where do you start?</strong><small>Name the selection evidence and exception checks before naming configuration.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#returns"><span>Q2</span><strong>The bank returned a direct debit with a fee. What must happen in SAP?</strong><small>Explain identification, clearing reset, reopened receivable, fee separation, and reconciliation.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#diagnostic"><span>Q3</span><strong>The payment run is green but the bank says the file is invalid. Who owns the defect?</strong><small>Separate SAP payment posting from payment-medium and bank-interface responsibility.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#diagnostic"><span>Q4</span><strong>The bank executed the payment but the clearing account is still open. What do you inspect?</strong><small>Trace bank-statement import, interpretation, posting rule, reference matching, and final clearing.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#practice"><span>Q5</span><strong>Why can an FI-CA payment order keep an open item open after the payment run?</strong><small>Explain the difference between payment initiation and bank-confirmed execution.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      <a href="#practice"><span>Q6</span><strong>When would you reject a custom BAdI solution?</strong><small>When the real issue is standard mapping, weak reference design, or unclear bank-file ownership.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Toolbox</p><h2>Know what each tool helps you prove.</h2><p>Transaction and app availability depends on release and deployment model. Use these as study references, not as a universal operating procedure.</p></header>
    <div class="ecg-input-grid">
      <article><span>F110</span><h3>Automatic Payment Program</h3><p>Parameters, proposal, payment run, exceptions, and payment execution.</p></article>
      <article><span>F-28</span><h3>Incoming payment</h3><p>Classic customer incoming-payment posting reference.</p></article>
      <article><span>F-32</span><h3>Customer clearing</h3><p>Classic customer open-item clearing reference.</p></article>
      <article><span>FBL5N</span><h3>Customer line items</h3><p>Inspect open and cleared customer positions in classic GUI environments.</p></article>
      <article><span>F.13</span><h3>Automatic clearing</h3><p>Periodic clearing reference; use only when matching rules fit the business case.</p></article>
      <article><span>FPY1</span><h3>FI-CA payment run</h3><p>Mass activity for FI-CA payment and collection processing.</p></article>
      <article><span>F1680</span><h3>Incoming payment files</h3><p>Import bank statements, payment rejections, and other supported incoming financial files.</p></article>
      <article><span>F1520</span><h3>Bank statement reprocessing</h3><p>Resolve items that could not post and clear automatically.</p></article>
      <article><span>FF_5</span><h3>Classic EBS import</h3><p>Electronic Bank Statement import reference for classic SAP GUI landscapes.</p></article>
      <article><span>FEB_BSPROC</span><h3>Classic EBS post-processing</h3><p>Worklist and manual processing for open bank-statement items.</p></article>
      <article><span>FBRA</span><h3>Reset clearing</h3><p>Classic clearing-reset reference; assess downstream impact before use.</p></article>
      <article><span>RFKKSEPA</span><h3>SEPA rejection report</h3><p>RFKKSEPA_DD_RJCT handles a specific FI-CA pain.002 rejection-file scenario.</p></article>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">fact_check</span>
    <p><strong>Verification boundary:</strong> this is a working assessment module. The core F110/Fiori bank-statement, SEPA pre-notification, FI-CA payment-order, and pain.002 concepts were checked against current SAP Help material. Detailed classic return configuration, specific BAdIs, and some transaction-level behavior come from the supplied working note and must be validated for the target S/4HANA release before implementation.</p>
    <a href="/labs/assessment/factual-review/">Use the factual review process <span class="material-symbols-outlined" aria-hidden="true">fact_check</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Official references</p><h2>Use current SAP documentation to validate the operating model.</h2><p>These references support the main process boundaries used in this study page.</p></header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3eb1567cf97543c08087efb0936964e6/45698054f87c033de10000000a441470.html" target="_blank" rel="noopener"><span>SAP</span><strong>Manage Automatic Payments</strong><small>Payment proposals, payments, payment media, and direct-debit pre-notification functions.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/PRODUCT_ID/3cb1182b4a184bdd93f8d62e3f1f0741/a1597b757dfd404283a050ab12585e5a.html" target="_blank" rel="noopener"><span>SAP</span><strong>Manage Incoming Payment Files — F1680</strong><small>Incoming bank statements, payment rejections, and parameter sets.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/a8aaa72cb39a48528b39b61623c15baa/bc1fe656fe590950e10000000a44147b.html" target="_blank" rel="noopener"><span>SAP</span><strong>Reprocess Bank Statement Items — F1520</strong><small>Manual and rule-based reprocessing when automatic posting or clearing fails.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/9442486404b54071b4ebeab6a16628e7/bc874f2966d4434cb4b6a6794f0fac70.html" target="_blank" rel="noopener"><span>SAP</span><strong>Pre-Notification of SEPA Direct Debits</strong><small>FI-CA selection, grouping, mandate use, and pre-notification processing.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/cdccca8e03d74101a0135863bc522b49/0d0bc5536a51204be10000000a174cb4.html" target="_blank" rel="noopener"><span>SAP</span><strong>Payment Orders for Direct Debits and Bank Transfers</strong><small>Bank-confirmed execution and clearing through payment-order lots.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SUPPORT_CONTENT/uindustry/3362182661.html" target="_blank" rel="noopener"><span>SAP</span><strong>RFKKSEPA_DD_RJCT</strong><small>FI-CA processing for separate SEPA direct-debit rejection messages in pain.002 format.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
