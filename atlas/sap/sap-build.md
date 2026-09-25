---
layout: default
title: "SAP Build"
description: "SAP Build explained as SAP's application-development and automation portfolio across low-code, pro-code, AI-assisted development, and digital workspaces."
permalink: /atlas/sap/sap-build/
atlas_section: sap
domain: SAP operations
subdomain: Low-code development
concept_type: product
sap_area: "SAP Build"
business_process: "Application development"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - sap-build
  - low-code
  - btp
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/sap-btp/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/cap/
  - /atlas/sap/fiori-ui5/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Build</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP Build</h1>
    <p class="note-subtitle">Application development, process automation, and digital-workspace tools spanning low-code, pro-code, and AI-assisted development.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Application development</dd></div>
      <div><dt>SAP area</dt><dd>SAP Build</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>SAP Build is no longer well described as one low-code tool for citizen developers. SAP now positions it as a broader development and automation offering that combines drag-and-drop tools, professional development, and AI assistance. The common name is useful, but the runtime still depends on what we are actually building.</p>

    <p>A custom application, a business-process automation, and a digital workspace can all belong to SAP Build while having different artifacts, deployment models, authorizations, and operational evidence. For architecture and support work, the first useful question is therefore not “is this on Build?” but “which Build capability owns this part of the solution?”</p>

    <h2>Application development spans low-code and pro-code</h2>
    <p>For professional Java and JavaScript development, <strong>SAP Build Code</strong> provides a cloud development environment for building, testing, integrating, and managing applications. SAP positions the Cloud Application Programming Model (CAP) as an important programming model in this path, while the wider SAP Build offering also includes ABAP Cloud development options. CAP and ABAP Cloud are still programming models and runtimes in their own right; SAP Build does not erase that distinction.</p>

    <p><strong>SAP Build Apps</strong> provides visual application development for web and mobile scenarios. Its current SAP product page also carries an important lifecycle note: SAP Build Apps is being deprecated as a <em>standalone</em> product as SAP moves application development into the unified SAP Build offering. Existing customers are not described as losing access immediately; SAP states that they can continue to use the product for the duration of their current contract. That makes the exact entitlement and migration path more important than an older diagram that treats Build Apps as a permanent independent product.</p>

    <h2>Process Automation owns orchestration and task automation</h2>
    <p><strong>SAP Build Process Automation</strong> is a separate SAP BTP service for modeling and running business processes and automations. It can combine workflow steps, user tasks, decisions, forms, APIs, and robotic automation. Current SAP positioning also includes AI-assisted and agentic workflow patterns, but that does not turn every process into an autonomous agent: deterministic steps, approvals, and ordinary business rules remain part of the same automation landscape.</p>

    <p>This distinction matters when a process fails. A form waiting for a user, an API action rejected by a target system, and a desktop automation failing on an agent are different runtime states. Process Automation provides its own deployed projects, environments, monitoring, traces, and agent administration. A generic BTP health check does not replace that process-level evidence.</p>

    <h2>Work Zone is the workspace, not the business application</h2>
    <p><strong>SAP Build Work Zone</strong> provides role-based business sites and workspaces that bring together applications, tasks, and content. It can surface local and federated content and provide a common entry point, but the application behind a tile or card can still run in SAP S/4HANA, SAP BTP, or another system.</p>

    <p>That boundary is useful in design reviews. Work Zone can solve navigation, composition, and digital-workplace needs without moving the underlying transaction into Work Zone. If an embedded application fails, we still have to trace its own destination, identity, frontend, service, and backend path.</p>

    <h2>A shared portfolio does not mean one runtime</h2>
    <p>SAP is making the Build experience more unified, including shared discovery and collaboration across development tools. That should not be confused with technical sameness. A CAP application built with Build Code may depend on Cloud Foundry services and its own database. A Process Automation project runs in the automation service and may use agents or actions. Work Zone has its own site and content lifecycle. Visual applications have their own deployment and integration choices.</p>

    <p>The surrounding SAP BTP account still matters: subaccounts, entitlements, identity, destinations, connectivity, and service plans define what can be created and reached. “SAP Build supports this” is therefore not enough to prove that a particular subaccount, region, contract, or target system supports the intended design.</p>

    <h2>Integration should start from the supported contract</h2>
    <p>Build tools can connect to SAP and non-SAP systems, but the connection model depends on the tool. SAP documents REST and OData integration plus BTP destinations for SAP Build Apps; Process Automation has actions and APIs for process integration; pro-code applications can consume released services through their application architecture. These are more precise statements than saying that SAP Build directly “connects by RFC, OData, events, and SOAP” as if every Build component exposed the same adapters.</p>

    <p>For an SAP S/4HANA extension, we still decide which system owns the business object and which released API, event, or supported extension point forms the contract. Moving the UI or orchestration to SAP Build can support a clean-core approach, but it does not make an unsupported backend dependency safe.</p>

    <h2>Governance follows the artifact that will run</h2>
    <p>Low-code reduces the amount of code a team writes; it does not remove software lifecycle responsibilities. Productive apps and automations still need owners, access control, environment separation, deployment discipline, dependency management, and an operational path for failures. The relevant controls differ between Build Code, Process Automation, Work Zone, and visual app development.</p>

    <p>This is also a better way to choose a Build tool. Start with the business behavior: are we building a service-oriented application, a visual front end, a workflow, a task automation, or a workspace? Then choose the component whose runtime and lifecycle fit that behavior. Selecting “SAP Build” first and forcing every requirement into one tool usually hides the real architectural boundary.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP — <a href="https://www.sap.com/products/technology-platform/build.html">SAP Build</a>.</li>
      <li>SAP — <a href="https://www.sap.com/products/technology-platform/developer-tools.html">SAP Build Code</a>.</li>
      <li>SAP — <a href="https://www.sap.com/products/technology-platform/low-code-app-builder.html">SAP Build Apps</a>, including the current standalone-product deprecation notice.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/build-process-automation/sap-build-process-automation">SAP Build Process Automation</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/build-work-zone-standard-edition/sap-build-work-zone-standard-edition">SAP Build Work Zone, standard edition</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>SAP Build packaging is changing quickly. Product names, entitlements, AI capabilities, migration paths, runtime options, regional availability, and the boundary between standalone products and the unified SAP Build offering can change. Verify the exact Build capability, plan, and target landscape before using this overview as an implementation specification.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/cap/">CAP</a></li>
      <li><a href="/atlas/sap/fiori-ui5/">Fiori / UI5</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
