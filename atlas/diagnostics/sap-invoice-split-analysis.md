---
title: SAP Invoice Split Analysis
layout: default
description: A focused SAP billing diagnostic for finding the first split-relevant difference when references that were expected to combine create separate billing documents.
permalink: /atlas/diagnostics/sap-invoice-split-analysis/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Billing diagnostics
concept_type: diagnostic guide
sap_area: Sales billing
business_process: Order to cash
status: needs_verification
verified: false
last_reviewed: 2026-05-06
tags:
  - order-to-cash
  - sap-sd
  - diagnostics
related:
  - "/labs/enterprise-context/billing/"
  - "/atlas/diagnostics/sap-billing-block-analysis/"
robots: noindex,follow
short_title: Invoice Split Analysis
h1: SAP invoice split analysis
subtitle: Start with the references you expected to combine, then find the first billing-header difference that prevents convergence.
sitemap: false
author: Dzmitryi Kharlanau
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/diagnostics/">Diagnostics</a></li><li aria-current="page">Invoice Split Analysis</li></ol></nav>

<article class="section note-detail atlas-page">
<header class="note-header">
  <p class="eyebrow">Atlas Diagnostic</p>
  <h1>SAP invoice split analysis</h1>
  <p class="note-subtitle">A failure-specific companion to <a href="/labs/enterprise-context/billing/">Sales Billing</a>. Use it when business users expected one billing document but SAP created two or more.</p>
  <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
</header>

<aside class="atlas-meta-panel"><dl>
  <div><dt>Primary study page</dt><dd><a href="/labs/enterprise-context/billing/">Sales Billing</a></dd></div>
  <div><dt>Question</dt><dd>Which split-relevant value is the first meaningful difference between items that were expected to converge?</dd></div>
  <div><dt>Indexing</dt><dd>Noindex. This is a focused billing failure trace.</dd></div>
</dl></aside>

<div class="note-body">
  <h2>The business problem: two invoices instead of one</h2>
  <p>A billing team selects two outbound deliveries together. Both belong to the same customer, but SAP creates two invoices. This may be a real billing split, an intended separate-invoice rule, or simply two separate billing runs. These are different problems. First prove that the references were eligible and processed together before looking for a split field.</p>
  <p>The process chain is <strong>sales order → outbound delivery (and goods issue where required) → billing due list → billing document creation → FI posting → customer invoice output</strong>. Order-related billing and billing document requests follow different paths into the due list. The split decision belongs to billing document creation; FI and customer communication feel its consequences. SAP documents that billing documents can be posted to Financial Accounting after creation. <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/4c74c957b7018809e10000000a4450e5.html">Source: SAP Sales Billing, S/4HANA 2025 FPS01</a>.</p>

  <h2>Find the difference before changing anything</h2>
  <ol>
    <li><strong>Confirm the expected group.</strong> Record the billable reference documents, their items, the billing type, the billing run or selection, and whether business rules really require one invoice. Two invoices from separate runs are not, by themselves, proof of a split.</li>
    <li><strong>Compare the actual billing headers.</strong> If billing documents already exist, use the <em>Split Analysis</em> feature in <em>Manage Billing Documents</em> where your S/4HANA release and authorization support it. Select two billing documents and compare the displayed header and business-partner differences. SAP documents this in app F0797 for S/4HANA 2025 FPS01. If the app is unavailable, obtain an equivalent approved header comparison rather than assuming a classic GUI path applies everywhere. <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/d2185b549a8c8e4ce10000000a4450e5.html">Source: SAP Manage Billing Documents</a>.</li>
    <li><strong>Trace each difference to its owner.</strong> Compare the billing header with the source order, delivery or billing document request. Check the applicable copy-control or data-transfer rule only for the actual source-to-billing path; then check master data and local extensions if the field was derived there.</li>
    <li><strong>Test whether the difference is mandatory.</strong> SAP identifies fields such as sales organization, sold-to, bill-to, payer, document currency, tax countries, VAT registration, payment terms and Incoterms as standard split criteria. In S/4HANA Cloud Public Edition 2602, SAP warns not to clear the always-split fields to bypass a split. Other fields, including some custom header fields, can influence convergence. <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/89c6419872644e1dbb8db0a17dbd67b7.html">Source: SAP Split Criteria, Public Edition 2602</a>.</li>
    <li><strong>Prove the outcome.</strong> After an approved correction, repeat the same billing scenario in a test environment. Compare the number of invoices, split analysis, payer, payment terms, tax fields, FI posting and customer output. Record the result before considering a production change.</li>
  </ol>

  <h2>Small evidence record</h2>
  <p>Use one row per billable reference. The values below are <strong>synthetic</strong>, not an SAP export or a customer case. The reference-number values illustrate a configuration question, not a universally enabled setting.</p>
  <table class="study-table">
    <thead><tr><th>Evidence</th><th>Delivery A</th><th>Delivery B</th><th>Owner / check</th></tr></thead>
    <tbody>
      <tr><td>Sales organization / payer</td><td>1000 / P-01</td><td>1000 / P-01</td><td>Source and billing header</td></tr>
      <tr><td>Currency / payment terms</td><td>EUR / 0030</td><td>EUR / 0030</td><td>Billing header and source</td></tr>
      <tr><td>Reference number transferred to billing</td><td>DEL-A</td><td>DEL-B</td><td>Copy control or data transfer</td></tr>
      <tr><td>Billing run</td><td>RUN-01</td><td>RUN-01</td><td>Billing job / selection evidence</td></tr>
    </tbody>
  </table>
  <p><strong>Working hypothesis:</strong> the two different delivery reference numbers became billing-header reference values and prevented convergence. SAP's S/4HANA 2025 FPS01 guidance gives an example: using the delivery number as the billing reference number (copy-control option C) causes a split for two different deliveries, while option E can avoid that particular difference. This is <em>not</em> permission to change copy control without checking accounting and interface requirements. <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/ed84b70c199d4470ae2e5ccb93b2e45b/e8ff2732c8bd412a9d52f5b64e75a8f9.html?locale=en-US">Source: SAP Billing Document Split and Convergence, S/4HANA 2025 FPS01</a>.</p>

  <h2>Three decisions, not one universal fix</h2>
  <ol>
    <li><strong>Keep a legitimate split.</strong> If legal entities, payer, tax-related fields or contractual payment terms differ by design, retain the separate invoices. Explain the reason to billing operations; do not make mandatory fields artificially equal. Billing and Finance own the acceptance decision.</li>
    <li><strong>Correct the source for future billing.</strong> If the wrong partner, payment term or other value originated in a source document or governed master record, ask that data owner to correct the approved source. Re-test a fresh billable reference. If an invoice was already posted, Finance must decide the compliant cancellation/rebilling path; do not edit a posted invoice or rerun billing as an automatic shortcut.</li>
    <li><strong>Review the transfer design.</strong> If a nonmandatory reference or custom field causes an unintended split, evaluate the relevant copy-control setting or supported billing data-transfer extension. SAP describes custom header fields and the <code>SD_BIL_DATA_TRANSFER</code> BAdI for specific split behavior. Validate downstream references, tax, FI posting and output in regression tests before approval. The correct implementation depends on edition, release and local configuration. <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/dcb274a8656348e2aad594a1e307b84a.html">Source: SAP Solution Order: Specifics for Billing Documents</a>.</li>
  </ol>

  <h2>Applied AI research: can a model find the next useful check?</h2>
  <p><strong>Fresh tooling signal, not an SAP capability:</strong> GitHub's <a href="https://github.blog/changelog/2026-11-16-github-copilot-weekly-releases-november-9/">16 November 2026 Copilot release note</a> describes an experimental <em>Compare Models</em> feature in VS Code 1.146. With the feature and agent tools enabled, agents can run and summarize model comparisons. It does not connect to SAP or validate SAP billing rules. The same experiment can be run manually in a permitted AI chat interface if the feature is unavailable.</p>
  <p><strong>Ten-working-day offline pilot:</strong> prepare 30 synthetic or irreversibly anonymized billing groups. Include valid business splits, incorrect source values, optional custom/reference-field differences, and misleading separate-run cases. A billing specialist independently labels the expected <em>next evidence check</em> and whether a proposed change is safe. No real customer numbers, tax IDs, prices or confidential configuration leave approved boundaries.</p>
  <p><strong>Baseline:</strong> a spreadsheet rule compares known split-relevant fields and flags unequal values; it also records whether references were processed in the same run. <strong>AI test:</strong> give the same evidence and public SAP source excerpts to one model; if the VS Code feature is available, compare a second model with identical inputs. Require a field-level explanation, source link, uncertainty label and the next check. Do not ask a model to decide a production correction.</p>
  <p><strong>Measure:</strong> correct next-check recommendations out of 30, false-positive defect flags (legitimate split called a defect), unsafe change suggestions, and median reviewer minutes per case. Compare each with the rules-only baseline on the same labelled cases. A useful pilot target is at least 80% correct next checks, fewer false-positive defect flags than the baseline and at least 20% less reviewer time; these are <em>acceptance targets, not achieved results</em>. Stop if any sensitive data enters the test, any model advises bypassing a mandatory split criterion, or three or more of the 30 cases receive false-positive defect labels. A human approves every interpretation and every SAP action. <strong>No SAP write-back, posting, BAdI activation or automated billing.</strong></p>

  <h2>Boundary and review status</h2>
  <p>Standard SAP behavior is documented in the SAP Help sources above. Copy-control settings, custom fields, billing-job design and available app actions are <strong>local configuration or release dependent</strong>. The table and pilot are synthetic proposals. This editorial revision is authored as part of Dzmitryi Kharlanau's site; <strong>editorial and SAP review are pending human confirmation</strong>. The page remains unverified and noindex.</p>

  <p class="disclaimer">This is an independent diagnostic guide, not official SAP documentation or a substitute for legal, tax or financial approval.</p>
</div>

<section class="atlas-related"><h2>Related pages</h2><ul>
  <li><a href="/labs/enterprise-context/billing/">Sales Billing — primary learning page</a></li>
  <li><a href="/atlas/diagnostics/sap-billing-block-analysis/">Billing Block Analysis</a></li>
</ul></section>

{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
</article>
