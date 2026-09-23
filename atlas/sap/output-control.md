---
layout: default
title: "SAP S/4HANA Output Control"
description: "Practical guide to SAP S/4HANA Output Control: architecture, decision tables, output parameters, channels, forms, technical boundaries, and Sales configuration."
permalink: /atlas/sap/output-control/
atlas_section: sap
domain: SAP operations
subdomain: Document output
concept_type: integration
sap_area: "SAP S/4HANA Output Control"
business_process: "Cross-application document communication"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

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
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP S/4HANA Output Control</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Cross-Application Component</p>
    <h1>SAP S/4HANA Output Control</h1>
    <p class="note-subtitle">A reusable S/4HANA framework that decides what business document output is created, who receives it, through which channel, and with which form.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Component</dt><dd>CA-GTF-OC / SAP S/4HANA Output Control</dd></div>
      <div><dt>Rule engine</dt><dd>Output Parameter Determination with BRFplus decision tables</dd></div>
      <div><dt>Scope</dt><dd>Cross-application; each business application decides which objects, fields, channels, and checks it supports</dd></div>
      <div><dt>Review state</dt><dd>Working study page; noindex until human review</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>The idea in one sentence</h2>
    <p>SAP S/4HANA Output Control sits between a business document and the way that document is communicated outside the transaction. The application owns the business document; Output Control determines and processes the communication parameters.</p>

    <p>A compact memory model is:</p>
    <p><strong>BUSINESS OBJECT → OUTPUT TYPE → RECEIVER → CHANNEL → TEMPLATE → RELEVANCE → PROCESSING → STATUS</strong></p>

    <p>For example, a sales order can lead to an order confirmation. The system can decide that one customer receives it by email, while another business scenario prints it. The same general framework is reused by several S/4HANA applications.</p>

    <h2>First boundary: S/4HANA has more than one output framework</h2>
    <p>In Sales, we must distinguish SAP S/4HANA Output Management from classic Output Determination (SD-BF-OC). Classic output determination uses the condition technique and stores message information in the traditional message-control model. SAP S/4HANA Output Control uses BRFplus-backed decision tables to determine output parameters.</p>

    <div class="table-wrap" role="region" aria-label="Output framework comparison" tabindex="0">
      <table>
        <thead>
          <tr><th>Question</th><th>Classic output determination</th><th>SAP S/4HANA Output Control</th></tr>
        </thead>
        <tbody>
          <tr><td>Decision model</td><td>Condition technique</td><td>Business rules in decision tables</td></tr>
          <tr><td>Typical configuration language</td><td>Condition tables, access sequences, procedures, condition records</td><td>Determination steps, condition columns, result columns, comparison rules</td></tr>
          <tr><td>Runtime concept</td><td>Message / NAST-oriented processing</td><td>Output item with determined output parameters</td></tr>
          <tr><td>Application scope</td><td>Application-specific legacy framework</td><td>Cross-application framework adopted by individual business objects</td></tr>
        </tbody>
      </table>
    </div>

    <p>For the application object type <strong>Sales_Document</strong>, SAP S/4HANA Output Management can be activated or deactivated in Customizing. An important operational detail is that a change in activation applies to <strong>new documents</strong>. Existing documents continue to use the framework that was active when they were created.</p>

    <p><strong>Assessment trap:</strong> “S/4HANA always uses BRFplus output” is too broad. We first identify the deployment, application object, activation, and release.</p>

    <h2>Where the framework sits</h2>
    <ol>
      <li><strong>The application creates or changes a business object.</strong> Example: a sales order is saved.</li>
      <li><strong>The application provides output-relevant business data.</strong> Sales organization, document type, partner data, document status, and other supported attributes can become rule inputs.</li>
      <li><strong>Output Parameter Determination evaluates rules.</strong> The rules derive the output parameters.</li>
      <li><strong>The system renders the document.</strong> A form template combines business data with a layout.</li>
      <li><strong>The selected channel processes the output.</strong> Examples include email or print.</li>
      <li><strong>The output item receives a processing state.</strong> If determination succeeded but processing failed, troubleshooting moves from business rules to the technical channel.</li>
    </ol>

    <h2>Central Customizing objects</h2>
    <p>For a Lead-level explanation, it helps to separate the five central configuration decisions instead of treating “output customizing” as one large activity.</p>

    <div class="table-wrap" role="region" aria-label="Central Output Control Customizing objects" tabindex="0">
      <table>
        <thead>
          <tr><th>Configuration decision</th><th>What it means</th><th>Question to ask</th></tr>
        </thead>
        <tbody>
          <tr><td>1. Application object activation</td><td>Chooses whether a supported business object uses SAP S/4HANA Output Management.</td><td>Which framework owns this document?</td></tr>
          <tr><td>2. Define output types</td><td>Defines the business communication, for example an order confirmation or quotation output.</td><td>What document/message are we producing?</td></tr>
          <tr><td>3. Output Parameter Determination</td><td>Uses decision tables to derive runtime output parameters from document attributes.</td><td>Which rule matched and why?</td></tr>
          <tr><td>4. Assign output channels</td><td>Defines which channels are possible for a given application object and output type.</td><td>Is the requested channel technically allowed for this output?</td></tr>
          <tr><td>5. Assign form templates</td><td>Connects the output to the layout technology and form used for rendering.</td><td>Which template should create the document?</td></tr>
        </tbody>
      </table>
    </div>

    <h3>Output types and callback classes</h3>
    <p>An output type connects the business document with a specific communication purpose. SAP delivers standard output types for supported applications. For <code>Sales_Document</code>, examples include quotation, order confirmation, sales contract, direct debit request, and customer return.</p>

    <p>A useful technical boundary is the callback class. The application-specific callback logic controls how an output type works with the business object. This is why simply creating a new output type does not automatically create useful new business behavior. SAP training explicitly warns that a custom output type is normally meaningful only together with suitable callback logic.</p>

    <h2>Output Parameter Determination is the heart of the framework</h2>
    <p>The central maintenance application is <strong>Output Parameter Determination</strong>. It is the modern place where we define business rules for output parameters. The idea is comparable to asking which classic output condition record should be found, but the rule model is different.</p>

    <h3>Eight determination steps used in the Sales training model</h3>
    <div class="table-wrap" role="region" aria-label="Output Parameter Determination steps" tabindex="0">
      <table>
        <thead>
          <tr><th>Step</th><th>What the result controls</th><th>Typical question</th></tr>
        </thead>
        <tbody>
          <tr><td>Output Type</td><td>Which output is created; dispatch time can also be returned.</td><td>Order confirmation, quotation, contract output, or something else?</td></tr>
          <tr><td>Recipient</td><td>Which partner role or receiver gets the output.</td><td>Sold-to, bill-to, supplier, or another receiver?</td></tr>
          <tr><td>Channel</td><td>How the output is sent.</td><td>Email, print, EDI?</td></tr>
          <tr><td>Printer Settings</td><td>Print queue and number of copies for print output.</td><td>Where should the print request go?</td></tr>
          <tr><td>E-Mail Settings</td><td>Sender address and email template where supported.</td><td>Which sender and email body/template should be used?</td></tr>
          <tr><td>E-Mail Recipient</td><td>The concrete email destination.</td><td>Which address should receive it?</td></tr>
          <tr><td>Form Template</td><td>The layout used to render the PDF/output document.</td><td>Which form variant fits this country, language, role, or channel?</td></tr>
          <tr><td>Output Relevance</td><td>A gate that checks whether the output may actually be issued.</td><td>Is the document in a state where output is allowed?</td></tr>
        </tbody>
      </table>
    </div>

    <p><strong>Important nuance:</strong> these eight steps are a strong mental model for the SAP S/4HANA Sales configuration course, but Output Control is cross-application. Other applications or deployment models can expose additional or different settings. For example, SAP S/4HANA Cloud documentation also describes Output Queue Settings in some scenarios.</p>

    <h2>How to read a decision table</h2>
    <p>A decision table contains <strong>condition columns</strong> and one or more <strong>result columns</strong>. In SAP training screenshots, condition columns are shown as white and result columns as green. The document data is compared with the conditions. If the row matches, the result values become output parameters.</p>

    <p>We can think of one row as a simple rule:</p>
    <p><strong>IF document attributes match these conditions → THEN return these output parameters.</strong></p>

    <h3>Example: one sales organization, two distribution channels</h3>
    <p>Assume a toy company sells through the German sales organization. For end-customer business, it wants to send an order confirmation only by email. For wholesale business, it wants a printed order confirmation.</p>

    <div class="table-wrap" role="region" aria-label="Decision table example" tabindex="0">
      <table>
        <thead>
          <tr><th>Sales Organization</th><th>Distribution Channel</th><th>Result: Channel</th></tr>
        </thead>
        <tbody>
          <tr><td>Germany</td><td>End Customer</td><td>EMAIL</td></tr>
          <tr><td>Germany</td><td>Wholesale</td><td>PRINT</td></tr>
        </tbody>
      </table>
    </div>

    <p>The point is not the toy example itself. The important idea is that <strong>business-document attributes become rule inputs</strong>, while the returned value becomes an output parameter.</p>

    <h3>Evaluation rules that matter</h3>
    <ul>
      <li><strong>Within one row, conditions are evaluated together.</strong> The row must satisfy its required conditions before its result is returned.</li>
      <li><strong>Rows are processed from top to bottom.</strong> Put specific rules before broad fallback rules.</li>
      <li><strong>Conditions can use comparison operators.</strong> Rules can compare exact values, ranges, or patterns depending on the field and application.</li>
      <li><strong>Include and exclude logic is available.</strong> This is useful when one broad rule applies except for particular document types or channels.</li>
      <li><strong>Multiple matching rules can produce multiple results.</strong> This is especially important for receiver and channel determination.</li>
      <li><strong>Exclusive can stop further evaluation.</strong> For example, we can prevent a second matching channel from producing both EMAIL and EDI when only EMAIL is wanted.</li>
      <li><strong>Decision tables can be simulated.</strong> Simulation is one of the best ways to explain why a complex rule produced a particular result.</li>
      <li><strong>Tables can be exported/imported with Excel in supported scenarios.</strong> This can make large rule sets easier to review, but transport and governance still need control.</li>
    </ul>

    <h2>Sales_Document: supported channels and their boundaries</h2>
    <p>For the <code>Sales_Document</code> application object type in the SAP S/4HANA Sales course, the main channels are:</p>
    <ul>
      <li><strong>EMAIL</strong> — sends output by email and can use configurable sender, recipient, and email templates.</li>
      <li><strong>PRINT</strong> — sends the request through the print/spool infrastructure.</li>
      <li><strong>EDI</strong> — supports technical message formats such as IDoc or SOA/XML for supported integration use cases.</li>
    </ul>

    <p>The channel assignment is not only a rule result. The application object type and output type must first allow that channel. If we create a custom output type, we also need a valid application-object/output-type/channel combination before the channel can be selected in the business rules.</p>

    <p>For Sales, SAP documentation also gives narrow boundaries for EDI message formats: IDoc use in this framework is intended for specific internal-billing scenarios, while the XML channel described in the course is designed for SAP Ariba integration. Do not generalize these formats as unrestricted replacements for every legacy outbound interface.</p>

    <h2>Forms: output determination and document layout are separate decisions</h2>
    <p>The decision table determines <em>which</em> form template to use. The form technology then controls <em>how</em> the document looks and how business data is merged into the layout.</p>

    <p>SAP S/4HANA Output Management supports classic form technologies such as SAPscript and Smart Forms as well as PDF-based print forms. SAP training recommends PDF-based forms with fragments for new design work where they are supported.</p>

    <p>For Sales output, the form-template explanation is useful technically: the form combines a data source with the PDF layout. The business data is retrieved and merged with the form design to render the final document. This separates three failure classes:</p>
    <ul>
      <li>the wrong template was <strong>determined</strong>;</li>
      <li>the correct template was selected but the <strong>data source</strong> is wrong or incomplete;</li>
      <li>the data is correct but the <strong>layout/rendering</strong> is wrong.</li>
    </ul>

    <h2>Output relevance is a gate, not just another formatting parameter</h2>
    <p>Output Relevance is slightly different from the other determination steps. It can prevent an output from being issued even when the output type, receiver, channel, and form are already known.</p>

    <p>For example, the application can require the sales document to pass a status check before an order confirmation is issued. SAP training gives examples such as document completeness or availability-related checks. If the output is not relevant, the output item can remain in preparation instead of being sent.</p>

    <p>This distinction is useful during troubleshooting: <strong>“all parameters were determined” does not necessarily mean “the document is allowed to go out.”</strong></p>

    <h2>Dispatch time: now or later</h2>
    <p>Output can be issued immediately when the business document is saved or processed later, for example through scheduled/background processing. Dispatch time is therefore part of the output-type decision, not a separate user expectation that exists outside the rule set.</p>

    <h2>A practical configuration sequence</h2>
    <ol>
      <li><strong>Confirm the business object and framework.</strong> Example: <code>Sales_Document</code> with SAP S/4HANA Output Management active.</li>
      <li><strong>Reuse a standard output type where possible.</strong> Creating a new output type can require application-specific callback logic.</li>
      <li><strong>Confirm allowed channels.</strong> Do this before writing channel rules.</li>
      <li><strong>Assign or verify form templates.</strong> Separate the template assignment from the later business-rule selection.</li>
      <li><strong>Maintain Output Parameter Determination.</strong> Start with output type, then receiver, channel, channel-specific settings, form template, and relevance.</li>
      <li><strong>Put specific rules before general fallback rules.</strong></li>
      <li><strong>Simulate the decision tables.</strong> Prove the rule behavior before testing the full business process.</li>
      <li><strong>Test the runtime output.</strong> Check determination, relevance, rendering, channel processing, and final delivery.</li>
    </ol>

    <h2>Technical prerequisites and platform boundary</h2>
    <p>The functional rules are only one layer. In SAP S/4HANA and SAP S/4HANA Cloud Private Edition, the technical setup also matters. SAP's conversion and operations documentation lists the following prerequisites for Output Control:</p>
    <ul>
      <li><strong>bgRFC must be configured.</strong> Output processing uses background RFC; without the required configuration, output processing cannot run.</li>
      <li><strong>A storage system and storage category must exist.</strong> Rendered PDF output needs a content repository/storage setup.</li>
      <li><strong>BRFplus must be active and usable.</strong> The decision-table layer depends on it.</li>
      <li><strong>Adobe Document Services must be available when Adobe forms are used.</strong></li>
    </ul>

    <p>This gives us a useful ownership split. Functional consultants own business rules, application-object behavior, receivers, channels, and form selection. Basis/platform teams may own bgRFC, storage, spool, mail infrastructure, and ADS connectivity. Form developers own layout and form logic. Integration teams own EDI/SOA endpoints and message recovery.</p>

    <h2>Extensibility and scale</h2>
    <p>Output Parameter Determination can use application-specific fields, and SAP documentation describes extensibility through CDS for supported scenarios. This means we are not limited to one fixed global decision table. However, extra fields should be added only when they represent stable business rules; otherwise the table becomes difficult to explain and test.</p>

    <p>The framework can return multiple messages, receivers, and channels at the same time. That is a capability, not an accident. It also means governance matters: a broad non-exclusive fallback rule can create duplicate communication if row order is not designed carefully.</p>

    <p>For large documents, rendering can become a performance boundary. Current SAP S/4HANA Cloud Sales documentation recommends avoiding print or email output for sales or billing documents with more than 1,000 items because PDF rendering can become technically expensive; complex forms and heavy item-level logic can reduce the safe limit further. For high-volume cases, scheduled output processing is often a better operating model than synchronous user-time rendering.</p>

    <h2>How to diagnose Output Control</h2>
    <p>Do not start from the printer or email server. First locate the layer where expected and actual behavior diverge.</p>

    <div class="table-wrap" role="region" aria-label="Output Control diagnostic layers" tabindex="0">
      <table>
        <thead>
          <tr><th>Layer</th><th>Typical symptom</th><th>First check</th></tr>
        </thead>
        <tbody>
          <tr><td>Framework</td><td>You are checking BRFplus rules but the document behaves like classic output determination.</td><td>Application object activation and document creation date/framework.</td></tr>
          <tr><td>Output type</td><td>No expected output item exists.</td><td>Output Type decision table and document attributes.</td></tr>
          <tr><td>Receiver</td><td>Output exists but is addressed to the wrong partner.</td><td>Receiver rule and partner data.</td></tr>
          <tr><td>Channel</td><td>Email is expected but print or EDI is determined.</td><td>Channel rules, row order, Exclusive flag, allowed channel assignment.</td></tr>
          <tr><td>Relevance</td><td>Output is prepared but not issued.</td><td>Output Relevance checks and business-document status.</td></tr>
          <tr><td>Form</td><td>Wrong layout or wrong language/country variant.</td><td>Form Template rule and template assignment.</td></tr>
          <tr><td>Processing</td><td>All parameters are correct but sending/printing fails.</td><td>Email, spool, EDI, rendering, or communication infrastructure.</td></tr>
        </tbody>
      </table>
    </div>

    <p>This is also the clean boundary with the classic diagnostic page. If the document uses NAST-based output determination, use the classic condition-technique path. If it uses S/4HANA Output Control, begin with the output item and its BRFplus-derived parameters.</p>

    <h2>Lead-level design questions</h2>
    <ul>
      <li>Which application object owns the document, and which output framework is active?</li>
      <li>Can we reuse a standard output type instead of adding application-specific callback logic?</li>
      <li>Which attributes really belong in the decision table, and which are accidental complexity?</li>
      <li>Can several rules match? If yes, do we intentionally want multiple receivers or channels?</li>
      <li>What is the fallback rule when no customer-specific rule matches?</li>
      <li>Should output happen immediately or in controlled batch processing?</li>
      <li>Which status must be true before customer-facing output is allowed?</li>
      <li>How do we prove the rule before end-to-end testing? Use decision-table simulation.</li>
      <li>How will operations distinguish a determination error from a rendering or communication error?</li>
    </ul>

    <h2>Common mistakes</h2>
    <ul>
      <li>Using NACE/NAST terminology for a document that is actually controlled by S/4HANA Output Management.</li>
      <li>Creating a new output type and expecting it to work without application callback behavior.</li>
      <li>Maintaining a channel rule without first allowing that channel for the output type.</li>
      <li>Putting a broad rule before a specific rule and then wondering why the fallback wins or combines with another result.</li>
      <li>Forgetting that non-exclusive receiver/channel rules can intentionally create more than one output.</li>
      <li>Debugging email or print infrastructure before proving that the correct output parameters were determined.</li>
      <li>Treating the Sales list of determination steps and channels as universal for every application object and deployment model.</li>
    </ul>

    <h2>FAQ for assessment review</h2>
    <h3>Is Output Control an SD component?</h3>
    <p>No. The framework is cross-application. Sales is one consumer. Purchasing, billing, maintenance, finance-related applications, and other business objects can also adopt the framework.</p>

    <h3>What replaces condition records?</h3>
    <p>For S/4HANA Output Control, business rules in Output Parameter Determination replace the classic idea of finding an output condition record. Do not translate every classic condition-technique object one-to-one into BRFplus.</p>

    <h3>What is the most important thing to remember about decision tables?</h3>
    <p>Document attributes are conditions; output parameters are results. Rows are evaluated in order, so rule specificity, row order, and exclusivity matter.</p>

    <h3>Why can two channels be created for one document?</h3>
    <p>Several channel rules can match. If the matching rule is not exclusive, the framework can continue and return another channel, for example EMAIL plus EDI.</p>

    <h3>Why can an output exist but still not be sent?</h3>
    <p>Output Relevance can block processing based on business-document status. After relevance, technical processing can still fail in the selected channel.</p>

    <h3>Can we change the framework and have old orders follow the new logic?</h3>
    <p>Not automatically. For Sales application-object activation, SAP states that existing documents remain with the output framework that was active when they were created.</p>

    <h2>60-second assessment answer</h2>
    <p>SAP S/4HANA Output Control is a cross-application framework for business-document communication. First I identify the application object and confirm which output framework is active. In the S/4HANA framework, Output Parameter Determination uses BRFplus decision tables. Document attributes are conditions, and the rules return parameters such as output type, receiver, channel, email or printer settings, form template, and output relevance. For Sales, the main channels are print, email, and supported EDI scenarios. I troubleshoot it layer by layer: framework, output type, receiver, channel, relevance, form, and then technical processing. I would not start with NACE unless the document actually uses classic output determination.</p>

    <h2>Primary sources used for this study page</h2>
    <ul>
      <li><a href="https://learning.sap.com/courses/customizing-output-control-in-sap-s-4hana-sales/customizing-core-components-of-output-control">SAP Learning: Customizing Core Components of Output Control</a></li>
      <li><a href="https://learning.sap.com/courses/customizing-output-control-in-sap-s-4hana-sales/determining-output-parameters">SAP Learning: Determining Output Parameters</a></li>
      <li><a href="https://learning.sap.com/courses/customizing-output-control-in-sap-s-4hana-sales/defining-output-parameters-for-sales-orders">SAP Learning: Defining Output Parameters for Sales Orders</a></li>
      <li><a href="https://learning.sap.com/courses/customizing-output-control-in-sap-s-4hana-sales/explaining-the-concept-of-output-control">SAP Learning: Explaining the Concept of Output Control</a></li>
      <li><a href="https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-public-edition-sales-configuration/configuring-output-management_c8269e30-dda5-4096-962d-a7e81384bfed">SAP Learning: Configuring Output Management in SAP S/4HANA Cloud Public Edition Sales</a></li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/d736578415a340cba84b944798a699b5.html">SAP Help: SAP S/4HANA Output Control</a></li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/05e1f995c35e4716b99ce6d8a04d1473.html">SAP Help: How Does Output Control Work?</a></li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/d9cc17d1aa404aee9bf2d10599c9a8d1.html">SAP Help: Output Management for Sales Documents and Billing Process Documents</a></li>
    </ul>

    <h2>Verification boundary</h2>
    <p>Output Control is application- and release-sensitive. This page separates the general framework from Sales-specific examples, but implementation details must still be checked against the target S/4HANA deployment and release.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-output-message-control-diagnostics/">SAP Output and Message Control Diagnostics</a></li>
      <li><a href="/labs/enterprise-context/sales-order/">Sales Order Decision Map</a></li>
      <li><a href="/labs/assessment/sales/">SAP Lead Sales Assessment</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
