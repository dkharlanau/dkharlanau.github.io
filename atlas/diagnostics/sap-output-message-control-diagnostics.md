---
layout: default
title: "SAP Sales Output Diagnostics"
description: "Diagnose SAP Sales output by separating output determination, receiver and channel selection, form rendering, and transmission, with clear Public Edition and classic boundaries."
permalink: /atlas/diagnostics/sap-output-message-control-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Sales document output
concept_type: diagnostic guide
sap_area: "Sales Output Management"
business_process: Order to cash
status: needs_verification
verified: false
last_reviewed: 2026-09-24
last_modified_at: 2026-09-24
author: Dzmitryi Kharlanau
sales_preparation: sales

tags:
  - order-to-cash
  - sap-sd
  - diagnostics
  - output-determination
related:
  - /atlas/sap/output-control/
  - /atlas/diagnostics/sap-spool-output-diagnostics/
  - /atlas/diagnostics/sap-outbound-processing-diagnostics/
  - /labs/assessment/sales-certification/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Sales Output Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP Sales output diagnostics</h1>
    <p class="note-subtitle">The sales document can be correct while its output is missing, wrong, or unsent. Find the exact output stage that failed before changing rules or resending anything.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Order to cash</dd></div>
      <div><dt>SAP area</dt><dd>Sales Output Management</dd></div>
      <div><dt>Indexing</dt><dd>Noindex; editorially reviewed, still awaiting human verification.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>An order confirmation or invoice has two lives: the business document inside SAP and the output sent to a customer. Creating the document does not prove that the right output type was determined, that the right receiver and channel were selected, that the form rendered, or that transmission completed.</p>

    <p>For C_S4CS preparation, start with the current SAP S/4HANA Cloud Public Edition model. SAP's Sales configuration course uses <strong>Output Parameter Determination</strong> business rules for sales output. Do not begin a Public Edition question with NACE, NAST, or classic condition records unless the scenario explicitly places you in a classic or Private Edition context.</p>

    <h2>Trace one output through five boundaries</h2>
    <p>The useful mental model is <strong>business document → output relevance and type → receiver and channel → form/rendering → transmission status</strong>. Each boundary proves something different.</p>

    <ol>
      <li><strong>Business document:</strong> the sales order, delivery, or billing document exists and is in the business state expected by the scenario.</li>
      <li><strong>Output determination:</strong> the relevant output type is selected and any output-relevance conditions are satisfied.</li>
      <li><strong>Receiver and channel:</strong> the intended partner and route, such as email or print, are selected.</li>
      <li><strong>Form:</strong> the appropriate template can render the required business data.</li>
      <li><strong>Transmission:</strong> the output request is processed successfully by the selected channel.</li>
    </ol>

    <p>This ordering prevents a common support mistake. If no output is relevant, an email trace is too late in the chain. If the output item is correct but the generated PDF is wrong, changing receiver rules is the wrong layer. If the form is correct and the output request ends in an error, determination may already be healthy.</p>

    <h2>Public Edition: determine the parameters separately</h2>
    <p>SAP's current Public Edition Sales course describes separate determination steps for output type, receiver, channel, printer settings, email settings, email recipient, form template, and output relevance. This is more precise than thinking of “output” as one switch.</p>

    <p>It also explains why one symptom can have several causes. A missing order confirmation may mean no output type was selected, output relevance evaluated to false, or a later processing step failed. An email to the wrong person may have the correct output type and channel but the wrong receiver or email-recipient result. Duplicate outputs can be caused by multiple matching rule rows where multiple results are allowed rather than by a duplicate sales order.</p>

    <h2>Worked example: the order exists, but no confirmation email arrives</h2>
    <p>Assume a sales order is saved and visible in the document flow. The customer reports that no order confirmation arrived. We should not start by resending email or changing the customer's address.</p>

    <p>First inspect the output result. If <strong>ORDER_CONFIRMATION</strong> was not selected, stay in output-type determination. If it was selected but the output is not relevant because the document fails a configured status check, resolve that business state first. If the output is relevant and the receiver is correct but the channel is PRINT, investigate channel determination. If EMAIL is selected and the form is produced correctly, only then move to output-processing and transmission evidence.</p>

    <p>Suppose the rule result is EMAIL to the intended receiver, but processing ends in an error. At that point the sales order and most determination logic are already proven. The investigation belongs to output processing, the email settings or template, and the transmission layer. Changing the sales document type would widen the problem without evidence.</p>

    <h2>Use symptoms to choose the first boundary</h2>
    <div class="decision-table">
      <table>
        <thead><tr><th>Observed result</th><th>First boundary to prove</th><th>Do not assume yet</th></tr></thead>
        <tbody>
          <tr><td>No expected output is shown</td><td>Output type and output relevance</td><td>Do not blame email, print, or EDI infrastructure.</td></tr>
          <tr><td>Output exists, wrong customer receives it</td><td>Receiver and email-recipient determination</td><td>Do not treat the form template as the root cause.</td></tr>
          <tr><td>Receiver is right, channel is wrong</td><td>Channel decision-table result</td><td>Do not change partner master data unless it is evidence for the rule.</td></tr>
          <tr><td>PDF is created but data/layout is wrong</td><td>Form template and form data</td><td>Do not redesign output-type determination.</td></tr>
          <tr><td>Output item exists with processing error</td><td>Output-item log and selected channel</td><td>Do not resend repeatedly before the error is understood.</td></tr>
          <tr><td>Two outputs are produced</td><td>Multiple rule hits and exclusivity</td><td>Do not assume duplicate business documents.</td></tr>
        </tbody>
      </table>
    </div>

    <h2>Evidence in SAP S/4HANA Cloud Public Edition</h2>
    <p>The <strong>Output Parameter Determination</strong> app is the configuration surface for the decision tables used in the Sales course. SAP also provides <strong>Manage Output Items</strong> as a cross-application overview for output requests and their statuses; current Public Edition documentation describes it as a place to analyze failed output processing and perform follow-up actions. Use the application-specific output view where the business object provides one, then move to the central output evidence when appropriate.</p>

    <p>For an incident, capture the business document, application object, output type, receiver, channel, form template, output relevance result where available, processing status, and exact error. That set of evidence makes it possible to state where the chain first becomes unproven.</p>

    <h2>Classic SD and Private Edition are a different branch</h2>
    <p>Classic output determination uses concepts such as condition technique, output types, condition records, partner functions, transmission media, and NAST. SAP's current <strong>Private Edition Sales</strong> learning content explicitly discusses navigation to NAST output control from Sales Fiori apps. That is useful SD depth, but it is not the default mechanism to memorize for a Public Edition C_S4CS question.</p>

    <p>When supporting a real landscape, identify the application's actual output framework before choosing tools. Do not infer the framework from an old transaction list, a familiar form, or the fact that another application in the same S/4HANA system uses classic output.</p>

    <h2>Safe recovery</h2>
    <p>Resending is a business action, not a harmless diagnostic step. Before resending an invoice, order confirmation, or electronic message, confirm whether the original output already left SAP, whether the receiver was correct, and whether duplicate communication has a business or legal consequence. If a determination rule is changed, simulate or test representative cases where the product supports that capability, then verify both the corrected case and a previously working case.</p>

    <p>The incident is closed when the intended output is determined once, rendered with the correct content, addressed to the intended receiver through the intended channel, and its processing result is observable. “Document saved” and “email sent again” are weaker proofs.</p>

    <h2>Recall</h2>
    <ul>
      <li><strong>What is the first question in Public Edition Sales output diagnostics?</strong> Whether the expected output type is relevant and determined for the business document — not whether NAST contains a record.</li>
      <li><strong>Why can the correct output type still reach the wrong person?</strong> Output type, receiver, channel, and email recipient are separate determination decisions.</li>
      <li><strong>Why can two outputs be created from one document?</strong> More than one rule can match in determination steps that allow multiple results; exclusivity controls whether processing stops at the first relevant match in supported steps.</li>
      <li><strong>When is NAST relevant?</strong> In a classic/Private Edition or application-specific context that actually uses classic message control. Establish that context first.</li>
    </ul>

    <h2>Sources and study boundary</h2>
    <ul>
      <li>SAP Learning — <a href="https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-public-edition-sales-configuration/configuring-output-management_c8269e30-dda5-4096-962d-a7e81384bfed">Configuring Output Management</a> — Public Edition Sales determination steps, rule behavior, output relevance, and Sales examples.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/1e3ea57929574984905547ff2f7d8490.html">Output Item Processing Error</a> — Public Edition error handling linked to Manage Output Items.</li>
      <li>SAP Learning — <a href="https://learning.sap.com/courses/sap-s-4hana-cloud-private-edition-sales/output-management-and-nast-navigation-in-sales">Output Management and NAST Navigation in Sales</a> — Private Edition context for NAST navigation.</li>
      <li><a href="/atlas/sap/output-control/">Output Control</a> — architecture companion explaining why the output framework must be identified per application.</li>
      <li><a href="/labs/assessment/sales-certification/">C_S4CS Sales preparation hub</a> — use this diagnostic as the incident companion to the official Public Edition configuration material.</li>
    </ul>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis. Verification and indexing boundaries remain unchanged.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/sap/output-control/">Output Control</a> — framework and architecture explanation.</li>
      <li><a href="/atlas/diagnostics/sap-spool-output-diagnostics/">SAP Spool and Print Output Diagnostics</a> — when print processing is the proven failed boundary.</li>
      <li><a href="/atlas/diagnostics/sap-outbound-processing-diagnostics/">SAP Outbound Processing Diagnostics</a> — when output hands off to a broader outbound integration flow.</li>
      <li><a href="/atlas/diagnostics/idoc-aif-integration-diagnostics/">IDoc and AIF Integration Diagnostics</a> — when a proven IDoc/AIF path, rather than Sales output determination itself, is failing.</li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
