---
layout: default
title: "EDI"
description: "EDI in SAP explained: business-document standards, partner agreements, message implementation and mapping, transport, acknowledgments, and the relationship with IDoc and SAP Integration Suite."
permalink: /atlas/sap/edi/
atlas_section: sap
domain: SAP operations
subdomain: Integration
concept_type: integration
sap_area: "EDI"
business_process: "System integration"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - edi
  - edifact
  - supply-chain
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-integration-landscape-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/idoc/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">EDI</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Integration</p>
    <h1>EDI</h1>
    <p class="note-subtitle">Structured business-document exchange between companies, with explicit rules for message shape, partner agreement, mapping, and transport.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>System integration</dd></div>
      <div><dt>SAP area</dt><dd>EDI</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until integration claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>Electronic Data Interchange, or EDI, is the structured exchange of business documents between organizations. A purchase order, dispatch advice, invoice, or acknowledgment is represented in a machine-readable format agreed by the trading partners instead of being re-entered from paper or email.</p>

    <p>EDI is not one SAP technology and it is not synonymous with IDoc. Standards such as UN/EDIFACT and ASC X12 define external message structures. SAP applications may use IDocs, APIs, XML, or other application interfaces on their side of the exchange. Middleware connects those worlds by validating, transforming, routing, securing, and monitoring the partner message.</p>

    <h2>One exchange contains several contracts</h2>
    <p>A reliable EDI interface has at least three layers. The <strong>business-message contract</strong> says which document is being exchanged and which standard/version is used. The <strong>partner agreement</strong> says which company identifiers, communication settings, acknowledgments, security rules, and scenario-specific parameters apply. The <strong>application mapping</strong> says how the partner message becomes data the sending or receiving business application understands.</p>

    <p>Keeping those layers separate explains many production problems. A technically valid EDIFACT message can still be unacceptable to one partner because a mandatory qualifier is missing. A correct mapping can still fail because the sender identity does not match the agreement. A successful AS2 or SFTP transfer can still carry a document that the target application rejects.</p>

    <h2>Standards are starting points, not complete partner specifications</h2>
    <p>UN/EDIFACT and ASC X12 provide broad message standards, but real trading relationships normally use a narrower implementation of them. A partner may require specific segments, code values, qualifiers, repetitions, or conditional rules. The result is a partner-specific message contract built within the boundaries of the underlying standard.</p>

    <p>SAP Integration Advisor models this distinction explicitly. Its type-system library includes standards such as ASC X12 and UN/EDIFACT as well as SAP message families such as IDoc. A <strong>Message Implementation Guideline (MIG)</strong> narrows a message structure for a particular business purpose. A <strong>Mapping Guideline (MAG)</strong> then describes how a source MIG maps to a target MIG and can provide a runtime mapping artifact for integration processing.</p>

    <h2>IDoc is often one endpoint of EDI, not the definition of EDI</h2>
    <p>In a classic SAP scenario, an outbound application can create an IDoc that middleware maps to a partner's EDI format. On the inbound side, middleware can transform the partner message into an IDoc that SAP application processing understands. This pattern is common because IDocs provide a durable SAP message structure and processing status.</p>

    <p>But the architecture is not required to use IDoc. SAP Integration Advisor's current type systems also cover other structures, and an integration can use another released SAP interface when that fits the business process. The important design question is which interface contract the application owns, not whether every EDI project can be forced through one technical format.</p>

    <h2>Trading Partner Management keeps partner variation out of copied flows</h2>
    <p>Modern B2B integration becomes difficult when every partner gets a separately copied integration flow. SAP Integration Suite's Trading Partner Management addresses that problem with company and trading-partner profiles, agreement templates, trading partner agreements, and runtime partner configuration. Activated agreement information can be made available to Cloud Integration through the Partner Directory so the runtime can apply partner-specific parameters without hard-coding each variation into a separate flow.</p>

    <p>This does not remove partner-specific work. It gives that work a better home. Identifiers, agreements, security material, message choices, and operational rules remain explicit business-to-business configuration rather than becoming scattered constants in mappings and scripts.</p>

    <h2>Transport success and business acceptance are different events</h2>
    <p>An EDI exchange can produce several kinds of confirmation. The transport protocol may confirm that bytes were delivered. The EDI standard may define a functional or syntax acknowledgment. The receiving application may later accept or reject the business document. Those signals answer different questions and should not be collapsed into one generic “success” status.</p>

    <p>For support, we therefore trace the exchange in order: did the sender create the intended business message, did middleware select the correct partner agreement, did validation and mapping succeed, was the payload delivered, did the expected acknowledgment arrive, and did the receiving application post the document? This sequence usually localizes the failure faster than starting from an isolated IDoc or transport log.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/overview-of-sap-integration-advisor">Overview of SAP Integration Advisor</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/creating-post-exit-integration-flow-12398d4ba2ec41728e7221a9f0d5e08c-790">SAP Integration Suite capabilities</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/integration-suite/isuite-trading-partner-management/tasks-and-permissions-for-trading-partner-management">Trading Partner Management: tasks and permissions</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Supported standards, transports, acknowledgments, type-system versions, partner-management features, and SAP application interfaces depend on the product and release. Verify the exact partner specification and runtime capabilities before implementing or migrating a B2B interface.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
      <li><a href="/atlas/sap/idoc/">IDoc</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
