---
layout: default
title: "CAP"
description: "SAP Cloud Application Programming Model explained: CDS models, services, runtime logic, and its role in cloud extensions."
permalink: /atlas/sap/cap/
atlas_section: sap
domain: SAP operations
subdomain: Cloud development
concept_type: technology
sap_area: "CAP"
business_process: "Application development"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - cap
  - cloud-development
  - side-by-side
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/sap-btp/
  - /atlas/sap/abap-cloud/
  - /atlas/sap/odata/
  - /atlas/sap/fiori-ui5/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">CAP</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>CAP</h1>
    <p class="note-subtitle">SAP's application programming model for building service-oriented cloud applications with CDS, Node.js, or Java.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Application development</dd></div>
      <div><dt>SAP area</dt><dd>CAP</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until technology claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>CAP starts from the domain model</h2>
    <p>SAP Cloud Application Programming Model (CAP) is a framework and set of conventions for building enterprise cloud applications. Its central idea is to describe the domain and services declaratively, then let the runtime handle much of the repetitive application plumbing. CAP supports Node.js and Java runtimes, while Core Data Services (CDS) provides the common modeling language for data structures and service definitions.</p>

    <p>That makes CAP different from a simple web framework. We do not begin only with HTTP routes and database calls. We define entities, relationships, services, annotations, and behavior around a business model. The runtime can then expose services and apply common enterprise concerns around them.</p>

    <h2>CDS is the backbone, not just a schema file</h2>
    <p>In CAP, CDS describes more than database tables. A model can contain entities, associations, types, aspects, and service definitions. The same model becomes input for runtime behavior, persistence mapping, service exposure, validation, annotations, and tooling. Custom logic is added in service handlers when the declarative model is not enough.</p>

    <p>A small application might define an <code>Orders</code> entity, expose it through an application service, and add a handler for an action such as approval. CAP takes care of much of the standard request handling around the service, while the custom code focuses on the business rule that makes the application specific.</p>

    <h2>Where CAP sits in an SAP landscape</h2>
    <p>CAP is commonly used for side-by-side applications and extensions on SAP BTP, but it should not be reduced to “the BTP counterpart of RAP.” RAP is an ABAP programming model for applications and services in the ABAP environment. CAP is a cloud application model for Node.js and Java. They can solve related extension problems, but they use different runtimes, development stacks, and deployment models.</p>

    <p>A CAP application can consume SAP S/4HANA APIs, react to events, call non-SAP services, persist its own application data, and expose APIs to UIs or other systems. Connectivity, identity, destinations, messaging, and database services are therefore part of the surrounding architecture rather than features that magically appear because an application uses CAP.</p>

    <h2>Service exposure is generated, but the contract still matters</h2>
    <p>CAP can expose services from CDS definitions with relatively little code. OData is a common protocol in the SAP ecosystem, and CAP also provides adapters and extension options for other interfaces. This productivity is useful, but generated endpoints are still public contracts from the consumer's perspective. Entity names, keys, associations, actions, authorization rules, and versioning choices deserve the same care as hand-written APIs.</p>

    <p>We should also separate generation from application design. CAP can generate a large amount of technical behavior, but it does not decide where a business boundary belongs, which data should be owned locally, or when information should remain in S/4HANA. Those are architecture decisions.</p>

    <h2>Persistence and deployment are choices, not one fixed stack</h2>
    <p>CAP development can use lightweight local persistence during development and production-grade services in deployed environments. SAP HANA is a common production choice on SAP BTP, while CAP also supports additional persistence options through its runtime and plugin ecosystem. The exact supported setup depends on the runtime and current CAP version, so it is better to verify the intended target rather than assume every database behaves identically.</p>

    <p>SAP documents deployment patterns for SAP BTP Cloud Foundry and provides tooling and plugins for broader cloud-native scenarios. In practice, the important question is not only where the process runs, but which platform services it depends on and how those dependencies are configured across environments.</p>

    <h2>What CAP gives us — and what it does not</h2>
    <p>CAP gives developers a strong default architecture for domain models, services, runtime conventions, and integration with SAP BTP services. It can reduce boilerplate and make a small team productive quickly. It does not, by itself, make an extension loosely coupled, secure, scalable, or clean-core compliant. Those outcomes still depend on using stable APIs, choosing sensible ownership boundaries, defining authorization correctly, and operating the deployed service well.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Cloud Application Programming Model — <a href="https://cap.cloud.sap/docs/">CAP documentation</a>.</li>
      <li>CAP documentation — <a href="https://cap.cloud.sap/docs/cds/index">Core Data Services</a>.</li>
      <li>CAP documentation — <a href="https://cap.cloud.sap/docs/guides/deploy/to-cf">Deploy to Cloud Foundry</a>.</li>
      <li>CAP documentation — <a href="https://cap.cloud.sap/docs/plugins/">Plugins and enhancements</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>CAP evolves frequently. Supported runtimes, adapters, persistence options, plugins, and deployment patterns should be checked against the current CAP documentation for the application version in use.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/odata/">OData</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
