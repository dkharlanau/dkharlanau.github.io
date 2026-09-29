---
layout: default
title: "SAP S/4HANA Output Control"
description: "Practical SAP S/4HANA Output Control guide: OPD, BRFplus decision tables, output relevance, channels, forms, extensibility, and troubleshooting."
permalink: /atlas/sap/output-control/
atlas_section: sap
domain: SAP operations
subdomain: Document output
concept_type: integration
sap_area: "SAP S/4HANA Output Control"
business_process: "Cross-application document communication"
last_reviewed: 2026-09-29
author: Dzmitryi Kharlanau
output_control_page: true

tags:
  - output-control
  - output-management
  - brfplus
  - document-output
  - sap-s4hana
related:
  - /atlas/diagnostics/sap-output-message-control-diagnostics/
  - /labs/enterprise-context/sales-order/
  - /labs/assessment/sales/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP S/4HANA Output Control</li>
  </ol>
</nav>

<article class="section note-detail atlas-page output-control-page">
  <header class="note-header">
    <p class="eyebrow">SAP Sales · Output Management</p>
    <h1>SAP S/4HANA Output Control</h1>
    <p class="note-subtitle">A sales document is ready. Now SAP has to decide: should anything leave the system, who gets it, by which channel, and with which form? Output Control is where these decisions meet.</p>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Start here</dt><dd><strong>OPD</strong> · Output Parameter Determination</dd></div>
      <div><dt>Rules</dt><dd>BRFplus decision tables</dd></div>
      <div><dt>Think</dt><dd>Type → Receiver → Channel → Form → Relevance</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <section class="oc-memory" aria-label="Output Control memory model">
      <p class="oc-kicker">Memory model</p>
      <div class="oc-flow">
        <span>Business document</span><b>→</b>
        <span>Output type</span><b>→</b>
        <span>Receiver</span><b>→</b>
        <span>Channel</span><b>→</b>
        <span>Form</span><b>→</b>
        <span>Relevance</span><b>→</b>
        <span>Processing</span>
      </div>
      <p>When something goes wrong, find the first step where expected and actual behavior become different. Do not start from the printer.</p>
    </section>

    <h2>Start with the business question</h2>
    <p>Output Control is easier to understand when we stop thinking about it as “printing configuration”. Printing is only one possible end. The real question is: <strong>what communication should this document create?</strong></p>

    <p>A sales order can create an order confirmation. One customer may receive it by email. Another scenario may require print. A document with a block may not be allowed to go out at all. The business document provides facts; Output Parameter Determination turns those facts into communication decisions.</p>

    <div class="oc-callout">
      <strong>Lead habit</strong>
      <p>Separate determination from processing. First prove that SAP chose the right output type, receiver, channel, form, and relevance. Only then investigate mail, spool, ADS, EDI, or another technical channel.</p>
    </div>

    <h2>First check: which output framework owns the document?</h2>
    <p>S/4HANA can contain both the classic message-control world and the newer S/4HANA Output Control framework. Do not mix their terminology.</p>

    <div class="table-wrap" role="region" aria-label="Output framework comparison" tabindex="0">
      <table>
        <thead>
          <tr><th>Classic message control</th><th>S/4HANA Output Control</th></tr>
        </thead>
        <tbody>
          <tr><td>Condition technique</td><td>BRFplus-backed business rules</td></tr>
          <tr><td>Condition tables, access sequences, procedures</td><td>Decision tables and determination steps</td></tr>
          <tr><td>NAST/message-oriented model</td><td>Output item with determined parameters</td></tr>
          <tr><td>Think NACE / condition records</td><td>Think <strong>OPD</strong> / Output Parameter Determination</td></tr>
        </tbody>
      </table>
    </div>

    <p>For Sales documents, the active framework can depend on system version and configuration. Existing documents can also keep the framework that was active when they were created. So the first diagnostic question is simple: <strong>what framework owns this exact document?</strong></p>

    <h2>Open it in SAP</h2>
    <div class="oc-tool-grid">
      <div class="oc-tool">
        <code>OPD</code>
        <strong>Output Parameter Determination</strong>
        <p>Main place to maintain decision tables for output parameters.</p>
      </div>
      <div class="oc-tool">
        <code>VA02 / VA03</code>
        <strong>Sales document</strong>
        <p>Check the document, partners, status, output items, and the data that should drive the rule.</p>
      </div>
      <div class="oc-tool">
        <code>SOST</code>
        <strong>Email processing</strong>
        <p>Use it after determination is correct and the problem is in email processing.</p>
      </div>
      <div class="oc-tool">
        <code>SP01</code>
        <strong>Spool</strong>
        <p>Use it after PRINT is correctly determined and the issue is in print processing.</p>
      </div>
      <div class="oc-tool">
        <code>SFP</code>
        <strong>Adobe form</strong>
        <p>Useful when the problem is the form layout or form development.</p>
      </div>
      <div class="oc-tool">
        <code>SPRO</code>
        <strong>Framework setup</strong>
        <p>Cross-Application Components → Output Control for core configuration.</p>
      </div>
    </div>

    <h2>OPD is the control desk</h2>
    <p>In <strong>Output Parameter Determination</strong>, we choose a business application such as <strong>Sales Document</strong>, then a determination step. Each step answers one specific question.</p>

    <div class="table-wrap" role="region" aria-label="Output Parameter Determination steps" tabindex="0">
      <table>
        <thead>
          <tr><th>Determination step</th><th>Question it answers</th><th>Typical result</th></tr>
        </thead>
        <tbody>
          <tr><td><strong>Output Type</strong></td><td>What communication should exist?</td><td>Order confirmation, quotation, contract output</td></tr>
          <tr><td><strong>Receiver</strong></td><td>Who receives it?</td><td>Sold-to, bill-to, another partner role</td></tr>
          <tr><td><strong>Channel</strong></td><td>How should it leave SAP?</td><td>EMAIL, PRINT, EDI, supported external output channel</td></tr>
          <tr><td><strong>Printer Settings</strong></td><td>Where and how should it print?</td><td>Print queue, copies</td></tr>
          <tr><td><strong>Email Settings</strong></td><td>How should the email be built?</td><td>Sender, email template</td></tr>
          <tr><td><strong>Email Recipient</strong></td><td>Which concrete email address?</td><td>Recipient address or supported expression</td></tr>
          <tr><td><strong>Form Template</strong></td><td>Which document layout?</td><td>Order-confirmation form variant</td></tr>
          <tr><td><strong>Output Relevance</strong></td><td>Are we allowed to send it at all?</td><td>Relevant = true / false</td></tr>
        </tbody>
      </table>
    </div>

    <h2>Read a decision table as business English</h2>
    <p>A decision-table row is simply an <strong>IF → THEN</strong> statement. Document attributes are conditions. The result is an output parameter.</p>

    <div class="oc-rule">
      <span>IF</span>
      <strong>Sales Org = 1010</strong>
      <span>AND</span>
      <strong>Distribution Channel = 10</strong>
      <span>THEN</span>
      <strong>Channel = EMAIL</strong>
    </div>

    <p>Specific rules should normally come before broad fallback rules. Several rules can match, especially for receiver and channel determination, so the <strong>Exclusive</strong> behavior matters when only one result is wanted.</p>

    <h2>Practical extension: use a new field to decide whether output should be sent</h2>
    <p>Assume the business asks for a new checkbox on the sales document:</p>

    <div class="oc-scenario">
      <p><strong>Requirement</strong></p>
      <p>“If <code>Suppress Order Confirmation</code> is selected, do not send the order confirmation.”</p>
    </div>

    <p>This is a good Output Control extension because the new field represents a clear business fact and the output rule only needs to consume it.</p>

    <h3>Target design</h3>
    <div class="oc-flow oc-flow--large">
      <span>Custom field</span><b>→</b>
      <span>Expose to Output Parameter Determination</span><b>→</b>
      <span>Refresh OPD context</span><b>→</b>
      <span>Add condition column</span><b>→</b>
      <span>Output Relevance = false</span>
    </div>

    <h3>Step 1 — create the field in the right business context</h3>
    <p>For an extensibility-enabled Sales scenario, create the field in <strong>Custom Fields</strong> using the business context <strong>Sales: Sales Document</strong>. A field such as <code>YY1_SUPPRESS_OUTPUT</code> can be a simple Boolean/checkbox.</p>

    <p>The important part is not the name. The important part is the <strong>business context</strong>. A field created in the wrong context will not magically become available to Output Control.</p>

    <h3>Step 2 — enable it for Output Parameter Determination</h3>
    <p>Enable the field for the Sales output parameter data source <strong>Output Parameter Determination for Sales</strong> (<code>C_SALESORDEROMPARAMDET</code>), then publish it.</p>

    <div class="oc-callout">
      <strong>Why this matters</strong>
      <p>BRFplus does not read every field in the sales document. The application exposes a controlled set of condition parameters. Extensibility adds your field to that contract.</p>
    </div>

    <h3>Step 3 — refresh the condition parameters in OPD</h3>
    <ol>
      <li>Open <strong>Output Parameter Determination</strong> / <code>OPD</code>.</li>
      <li>Choose <strong>Sales Document</strong> in <em>Show Rules for</em>.</li>
      <li>Refresh <strong>Condition Parameters of Application</strong>.</li>
      <li>Confirm the refresh.</li>
    </ol>

    <p>This refresh is easy to miss. If the field was published correctly but does not appear in the decision table, check this step before debugging anything deeper.</p>

    <h3>Step 4 — add the field as a decision-table column</h3>
    <ol>
      <li>Choose the determination step you want to control. For “send / do not send”, start with <strong>Output Relevance</strong>.</li>
      <li>Switch the decision table to edit mode.</li>
      <li>Open <strong>Table Settings</strong>.</li>
      <li>Choose <strong>Insert Column → From Context Data Objects</strong>.</li>
      <li>Select the custom field.</li>
      <li>Maintain the rule and activate the table.</li>
    </ol>

    <h3>Step 5 — make the rule obvious</h3>
    <div class="table-wrap" role="region" aria-label="Custom Output Relevance rule" tabindex="0">
      <table>
        <thead>
          <tr><th>Output Type</th><th>Suppress Order Confirmation</th><th>Output Relevance</th></tr>
        </thead>
        <tbody>
          <tr><td>ORDER_CONFIRMATION</td><td><strong>Yes</strong></td><td><strong>False</strong></td></tr>
          <tr><td>ORDER_CONFIRMATION</td><td>blank / No</td><td>True</td></tr>
        </tbody>
      </table>
    </div>

    <p>Now the business rule can be read without code: <strong>if suppression is selected, the output is not relevant.</strong></p>

    <h3>Step 6 — test the full runtime, not only the table</h3>
    <ol>
      <li>Create or change a test sales order.</li>
      <li>Set the custom field.</li>
      <li>Save the document.</li>
      <li>Check the output item and its status.</li>
      <li>Repeat with the field cleared.</li>
      <li>Confirm that only the relevance decision changes; receiver, channel, and form should remain stable unless another rule intentionally changes them.</li>
    </ol>

    <h2>If the new field does not appear in OPD</h2>
    <div class="oc-checklist">
      <div><strong>1</strong><span>Correct business context?</span></div>
      <div><strong>2</strong><span>Usage enabled for Output Parameter Determination?</span></div>
      <div><strong>3</strong><span>Field published?</span></div>
      <div><strong>4</strong><span>Condition Parameters of Application refreshed?</span></div>
      <div><strong>5</strong><span>Correct business application and determination step?</span></div>
    </div>

    <p>In current SAP Sales extensibility, SAP documents this flow for sales and billing output. The binding refresh is performed in each system; it is not simply transported as part of the rule table.</p>

    <h2>Where should custom logic live?</h2>
    <p>A Lead should not solve every output requirement in BRFplus. Choose the extension layer based on the kind of problem.</p>

    <div class="table-wrap" role="region" aria-label="Output Control extension choices" tabindex="0">
      <table>
        <thead>
          <tr><th>Requirement</th><th>Best first place</th><th>Reason</th></tr>
        </thead>
        <tbody>
          <tr><td>Send only when a field/status has a value</td><td><strong>OPD decision table</strong></td><td>The data already exists; the rule only decides.</td></tr>
          <tr><td>Need a derived business flag</td><td><strong>Derive the field first, then expose it to OPD</strong></td><td>Keep calculation separate from communication rules.</td></tr>
          <tr><td>Choose another form by country/customer type</td><td><strong>Form Template step</strong></td><td>This is a direct determination decision.</td></tr>
          <tr><td>Choose EMAIL vs PRINT</td><td><strong>Channel step</strong></td><td>The channel is the result you are deciding.</td></tr>
          <tr><td>Add special email-recipient logic</td><td><strong>Supported recipient extensibility / BAdI</strong></td><td>Recipient creation can require application logic, not only a table.</td></tr>
          <tr><td>Add data to the PDF layout</td><td><strong>Form/data-source extension</strong></td><td>That is a rendering/data problem, not output relevance.</td></tr>
          <tr><td>Create completely new output behavior</td><td><strong>Application-specific extension</strong></td><td>A new output type may need callback/application logic.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="oc-callout oc-callout--strong">
      <strong>Design rule</strong>
      <p>Let OPD decide. Let the application provide facts. Let forms render. Let channels deliver. When one layer starts doing another layer’s job, Output Control becomes difficult to explain and even harder to support.</p>
    </div>

    <h2>Output Relevance is more powerful than it looks</h2>
    <p>Output Relevance is the clean gate between “we know how to send this” and “we are allowed to send this”. It is a strong place for rules such as:</p>
    <ul>
      <li>do not send while a sales order is blocked;</li>
      <li>do not send a confirmation for a special internal scenario;</li>
      <li>send only after a required status is complete;</li>
      <li>suppress output when a custom business flag is set.</li>
    </ul>

    <p>This is better than allowing output to reach the email or print layer and then trying to stop it there.</p>

    <h2>Forms are a separate decision</h2>
    <p>Output Control decides <strong>which form template</strong> should be used. The form technology decides <strong>what the document looks like</strong> and how data is rendered.</p>

    <p>That gives us three different failure patterns:</p>
    <ul>
      <li><strong>Wrong form was selected</strong> → check the Form Template decision table.</li>
      <li><strong>Correct form, wrong/missing data</strong> → check the form data source and application data.</li>
      <li><strong>Correct data, bad layout/rendering</strong> → check the form design / ADS side.</li>
    </ul>

    <h2>Fast diagnostic path</h2>
    <div class="oc-diagnostic">
      <div><span>01</span><strong>Framework</strong><p>Is this document using S/4HANA Output Control or classic message control?</p></div>
      <div><span>02</span><strong>Output item</strong><p>Does the expected output exist?</p></div>
      <div><span>03</span><strong>Output Type</strong><p>Did the right rule create the right communication?</p></div>
      <div><span>04</span><strong>Relevance</strong><p>Is SAP actually allowed to issue it?</p></div>
      <div><span>05</span><strong>Receiver + Channel</strong><p>Right partner? EMAIL, PRINT, EDI, EXTOM?</p></div>
      <div><span>06</span><strong>Form</strong><p>Was the correct template selected?</p></div>
      <div><span>07</span><strong>Processing</strong><p>Only now move to SOST, SP01, ADS, EDI, or external output infrastructure.</p></div>
    </div>

    <h2>Common traps</h2>
    <ul>
      <li><strong>Starting with SOST.</strong> First prove that EMAIL was actually determined and output is relevant.</li>
      <li><strong>Calling every S/4HANA output “BRFplus”.</strong> First identify the active framework for the document.</li>
      <li><strong>Creating a custom field but not exposing it to OPD.</strong> The field exists, but the rule engine cannot see it.</li>
      <li><strong>Publishing the field but forgetting the OPD refresh.</strong> The decision-table context is still old.</li>
      <li><strong>Putting calculation logic into decision tables.</strong> Derive stable business facts first; let OPD make the communication decision.</li>
      <li><strong>Mixing form problems with determination problems.</strong> A correct output rule cannot fix a bad PDF layout.</li>
      <li><strong>Broad fallback rules before specific rules.</strong> Row order and multiple matches can change the result.</li>
    </ul>

    <h2>60-second assessment answer</h2>
    <p>SAP S/4HANA Output Control is a cross-application framework for business-document communication. I first identify which framework owns the document. In the S/4HANA framework, Output Parameter Determination uses BRFplus decision tables. Document attributes are conditions; the rules return output type, receiver, channel, channel settings, form template, and output relevance. If I need a new business field, I expose that field to the application’s Output Parameter Determination context, refresh the OPD condition parameters, add it as a decision-table column, and use it in the correct determination step. For a send-or-don’t-send requirement, Output Relevance is the natural gate. During troubleshooting I go from framework and determination to relevance and form, and only then to email, spool, ADS, or integration processing.</p>

    <h2>Sources</h2>
    <ul class="oc-sources">
      <li><a href="https://learning.sap.com/courses/customizing-output-control-in-sap-s-4hana-sales/determining-output-parameters">SAP Learning · Determining Output Parameters</a></li>
      <li><a href="https://learning.sap.com/courses/customizing-output-control-in-sap-s-4hana-sales/explaining-the-concept-of-output-control">SAP Learning · Explaining the Concept of Output Control</a></li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/4aea5a6d73744ea2ae66430230ebcba0.html">SAP Help · Add Custom Fields as Condition Parameters in Output Parameter Determination</a></li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/d9cc17d1aa404aee9bf2d10599c9a8d1.html">SAP Help · Output Management for Sales and Billing Documents</a></li>
    </ul>
  </div>

  <section class="atlas-related">
    <h2>Continue</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-output-message-control-diagnostics/">Output and Message Control Diagnostics</a></li>
      <li><a href="/labs/enterprise-context/sales-order/">Sales Order Decision Map</a></li>
      <li><a href="/labs/assessment/sales/">SAP Lead Sales Assessment</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
</article>
