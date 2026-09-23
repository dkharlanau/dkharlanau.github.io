---
layout: default
title: "SAP Signavio"
description: "SAP Signavio explained: process modeling, process intelligence, collaboration, and how designed processes connect to observed process data."
permalink: /atlas/sap/sap-signavio/
atlas_section: sap
domain: SAP operations
subdomain: Process transformation
concept_type: product
sap_area: "SAP Signavio"
business_process: "Process management"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - sap-signavio
  - process-mining
  - bpm
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/sap-btp/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-build/
  - /atlas/sap/sap-datasphere/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Signavio</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP Signavio</h1>
    <p class="note-subtitle">A process-management environment for describing how work should run, analyzing how it actually runs, and coordinating improvement.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Process management</dd></div>
      <div><dt>SAP area</dt><dd>SAP Signavio</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>SAP Signavio is easier to understand when we separate <strong>process design</strong> from <strong>process observation</strong>. A modeled process says how work is intended to happen. Process intelligence reconstructs what happened from event data and lets analysts compare variants, timing, and outcomes. The value comes from connecting those two views without pretending that a diagram is proof of actual execution.</p>

    <p>SAP Signavio is also a suite rather than one monolithic runtime. Different products cover process modeling, collaboration, process intelligence, governance, and transformation-management tasks. Which capabilities are available depends on the licensed products and workspace configuration, so a landscape description should name the relevant Signavio component instead of using “Signavio” as if every feature were always present.</p>

    <h2>Process models create a shared design language</h2>
    <p>SAP Signavio Process Modeler and Process Manager support BPMN 2.0 for describing activities, decisions, handoffs, organizational responsibilities, data, and system dependencies. Models can also reference reusable dictionary entries, which helps a process landscape use the same business terms, systems, roles, and documents instead of redefining them diagram by diagram.</p>

    <p>A good model is therefore more than a picture. It is a governed description of a process that people can review, publish, and discuss. SAP Signavio Process Collaboration Hub provides the consumption and collaboration layer for published content. Approval and publication rules can be used where a company needs controlled process documentation rather than an unrestricted drawing workspace.</p>

    <h2>Process Intelligence starts from event data, not from the BPMN diagram</h2>
    <p>SAP Signavio Process Intelligence analyzes process data created from source-system events. Depending on the scenario, data can come through supported connectors and data-integration patterns or through prepared file uploads. The important design step is the transformation from source records into a usable process-data model: cases, activities, timestamps, attributes, and metrics must represent the business process correctly before the analysis is trustworthy.</p>

    <p>This boundary matters in SAP landscapes. An S/4HANA sales order, delivery, invoice, or purchasing document contains transactional evidence, but a process-mining model still needs a deliberate definition of the case and event sequence. If those semantics are wrong, a polished dashboard can describe the wrong process very convincingly.</p>

    <h2>Designed and observed processes answer different questions</h2>
    <p>The modeled process is useful for ownership, policy, controls, target design, and communication. Process Intelligence is useful for questions such as which variants actually occur, where time is spent, how often a path deviates, and which attributes correlate with an outcome. Neither view replaces the other.</p>

    <p>That distinction also changes how we investigate a gap. If the model is wrong, we improve the process design. If the observed process differs because users take another valid path, the model may need to acknowledge reality. If the deviation is undesirable, we need to understand the business rule, data, system behavior, and operating practice that produced it before proposing automation.</p>

    <h2>Current analysis terminology is moving toward dashboards</h2>
    <p>Older SAP Signavio material often refers to <strong>investigations</strong> in Process Intelligence. SAP changed this area in 2026: from May 26, 2026, new investigations can no longer be created or imported, while existing ones remain accessible for the time being. SAP is replacing that experience with customizable dashboards. New guidance should therefore avoid teaching “create an investigation” as the default current workflow.</p>

    <p>This is a useful reminder for Signavio content generally. Product terminology and workspace behavior evolve quickly, while process-management concepts change more slowly. We can keep the conceptual model stable and verify the current UI and feature names before implementation.</p>

    <h2>Integration should follow the process question</h2>
    <p>There is no single generic “S/4HANA to Signavio” interface. Process Intelligence has data-connection and ingestion options for supported sources, while process models can be managed independently of transactional extraction. Other Signavio products have their own integration points and APIs. A project should first decide which process evidence or model artifact is needed, then select the supported connection for that component.</p>

    <p>This is also why SAP Build, SAP Datasphere, and SAP Signavio should not be collapsed into one workflow stack. They can participate in the same transformation program, but they solve different problems: process understanding, application or workflow execution, and governed analytical data are separate architectural responsibilities.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Signavio Process Modeler — <a href="https://help.sap.com/docs/signavio-process-modeler/user-guide/bpmn">Business Process Modeling and Notation (BPMN)</a>.</li>
      <li>SAP Signavio Process Manager — <a href="https://help.sap.com/docs/SIGNAVIO_PROCESS_MANAGER/8365d6ee9cdb46a5a22243a9922e96d2/fa8c00bd6dad1014a4730ff5fb2ca89e.html">Publishing Diagrams to SAP Signavio Process Collaboration Hub</a>.</li>
      <li>SAP Signavio Process Intelligence — <a href="https://help.sap.com/docs/signavio-process-intelligence/onboarding-and-data-integration-guide/creating-customizable-data-connections">Creating Customizable Data Connections</a>.</li>
      <li>SAP Signavio Process Intelligence — <a href="https://help.sap.com/docs/signavio-process-intelligence/user-guide/about-investigations">Investigations and the 2026 transition to dashboards</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>SAP Signavio product scope, connectors, identity behavior, APIs, workspace administration, and licensed capabilities change independently. Verify the documentation for the specific Signavio product and tenant before turning this conceptual model into an integration or operating design.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-build/">SAP Build</a></li>
      <li><a href="/atlas/sap/sap-datasphere/">SAP Datasphere</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
