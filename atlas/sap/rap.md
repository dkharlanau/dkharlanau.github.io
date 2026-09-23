---
layout: default
title: "RAP"
description: "How the ABAP RESTful Application Programming Model structures business objects, behavior, services, and transactional applications."
permalink: /atlas/sap/rap/
atlas_section: sap
domain: SAP operations
subdomain: Development framework
concept_type: technology
sap_area: "RAP"
business_process: "Application development"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - rap
  - abap-cloud
  - development
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/abap-cloud/
  - /atlas/sap/cds-views/
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
    <li aria-current="page">RAP</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>RAP</h1>
    <p class="note-subtitle">The ABAP RESTful Application Programming Model for transactional business objects and services.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Application development</dd></div>
      <div><dt>SAP area</dt><dd>RAP</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until technology claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>A business object model, not just an OData generator</h2>
    <p>RAP, the ABAP RESTful Application Programming Model, is SAP's model for building transactional applications and services on the ABAP platform. It brings the data model, business-object behavior and service exposure into one development approach. OData is an important output, especially for SAP Fiori applications and web APIs, but the business object is the central idea.</p>

    <p>That distinction matters. A customer order is not simply a set of database rows exposed through HTTP. It has a structure, permitted operations, validations, determinations, actions, locking rules and a save sequence. RAP gives those rules an explicit place instead of leaving them scattered across UI code, service implementations and database updates.</p>

    <h2>From data model to behavior</h2>
    <p>The data model is normally defined with ABAP CDS entities. A root entity and its compositions describe the business-object structure; associations connect it to related information. A behavior definition then says what clients are allowed to do with that model: for example create, update, delete or execute a business action. It can also define transactional properties such as locking, authorization control, validations and determinations.</p>

    <p>RAP supports both <strong>managed</strong> and <strong>unmanaged</strong> business objects. With managed behavior, the framework can provide standard transactional handling for common operations while the application supplies the business-specific logic. With unmanaged behavior, the developer implements the essential transactional contract. That makes unmanaged RAP useful when a service must sit over existing application logic that cannot simply be replaced by framework-managed persistence.</p>

    <p>The behavior implementation lives in ABAP behavior pools where custom handler logic is needed. RAP also provides Entity Manipulation Language (EML), ABAP statements for reading and modifying RAP business objects through their defined behavior. This lets ABAP code consume a business object through its transactional contract rather than bypassing it with direct table updates.</p>

    <h2>Service definition and service binding do different jobs</h2>
    <p>Once a business object is ready for external consumption, a service definition selects the CDS entities that belong to the business service. A service binding then connects that definition to a specific protocol and service scenario. For example, a RAP service can be bound for an OData UI service or web API depending on the supported binding type in the target ABAP release.</p>

    <p>This separation is useful because the internal business object and the public service do not have to be identical. Projection layers can expose only the fields and behavior required for a particular consumer. A Fiori application may need annotations and actions for an interactive UI, while another consumer may need a narrower API contract.</p>

    <h2>Draft is a business interaction pattern</h2>
    <p>Draft handling is optional, not a defining requirement of RAP. When a process needs users to work on changes before committing them to the active business object, draft-enabled behavior can preserve an intermediate state and support longer-running interaction. SAP supports draft capabilities for both managed and unmanaged RAP business objects.</p>

    <p>A simple API that performs short atomic operations may not need draft at all. Adding it automatically can make the transactional model harder to reason about. The decision should follow the interaction: do users need a recoverable work-in-progress state, or should each request change active data directly?</p>

    <h2>RAP, ABAP Cloud, and existing ABAP</h2>
    <p>RAP and ABAP Cloud are closely related but not synonyms. RAP is the application programming model; ABAP Cloud defines a cloud-ready ABAP development model with language restrictions and released APIs. RAP is used in modern ABAP development across supported ABAP environments, while the exact available features depend on the platform and release.</p>

    <p>RAP also does not mean that existing application logic must be rewritten before it can participate. An unmanaged RAP business object can integrate legacy business logic while presenting a structured RAP contract to new consumers. This gives teams a migration path: modernize the service boundary and transactional model where useful without pretending that every mature S/4HANA process starts from a new database table.</p>

    <h2>Example: a maintenance object</h2>
    <p>Suppose a team needs a small business configuration application. CDS entities model the configuration records. The behavior definition enables the permitted changes and adds validation. A service definition exposes the relevant entities, and an OData V4 UI service binding makes the service available to the UI layer. SAP documents this pattern for business configuration applications built with RAP and the Custom Business Configurations app.</p>

    <p>The important design question is not how quickly the artifacts can be generated. It is whether the business-object boundary is correct. If validation depends on rules owned by another object, or if updates bypass existing application logic, a technically valid RAP service can still create inconsistent business data.</p>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/sap/abap-cloud/">ABAP Cloud</a> — the development model and released-API boundary used for cloud-ready ABAP.</li>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a> — the data-modeling foundation used by RAP.</li>
      <li><a href="/atlas/sap/odata/">OData</a> — a common protocol used by RAP service bindings.</li>
      <li><a href="/atlas/sap/fiori-ui5/">Fiori and UI5</a> — UI technologies that can consume RAP services.</li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>ABAP RESTful Application Programming Model — <a href="https://help.sap.com/docs/abap-cloud/abap-rap/abap-restful-application-programming-model">SAP Help Portal</a>.</li>
      <li>Developing Unmanaged Transactional Apps — <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/fc4c71aa50014fd1b43721701471913d/f6cb3e3402694f5585068e5e5161a7c1.html">SAP Help Portal</a>.</li>
      <li>Creating Business Configuration Apps with RAP — <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/b5670aaaa2364a29935f40b16499972d/fa420dd6272b41858a7b31f8dc5090f8.html">SAP Help Portal</a>.</li>
    </ul>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/abap-cloud/">ABAP Cloud</a></li>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
