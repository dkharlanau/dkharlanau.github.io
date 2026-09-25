---
layout: default
title: "OData"
description: "OData in SAP explained: entities, metadata, query options, service bindings, SAPUI5 consumption, and the difference between V2 and V4."
permalink: /atlas/sap/odata/
atlas_section: sap
domain: SAP operations
subdomain: API protocol
concept_type: technology
sap_area: "OData"
business_process: "System integration"
status: needs_verification
verified: false
last_reviewed: 2026-09-22
author: Dzmitryi Kharlanau

tags:
  - odata
  - api
  - integration
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/maps/sap-integration-landscape-map/
  - /atlas/maps/integration-architecture-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-btp/
  - /atlas/sap/cds-views/
  - /atlas/sap/rap/
  - /atlas/sap/cap/
  - /atlas/sap/fiori-ui5/
  - /atlas/concepts/sap-integration-architecture/
  - /atlas/concepts/integration-pattern-decision-matrix/
  - /atlas/concepts/rest-vs-odata-vs-soap-vs-idoc-vs-events/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">OData</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>OData</h1>
    <p class="note-subtitle">An HTTP-based data protocol used widely in SAP APIs and SAP Fiori application services.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>System integration</dd></div>
      <div><dt>SAP area</dt><dd>OData</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until technology claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>OData, the Open Data Protocol, is a standardized web protocol for exposing and working with structured data over HTTP. SAP uses it extensively, but OData is not an SAP-specific protocol and it is not the only API style in an SAP landscape.</p>

    <h2>The data model is part of the contract</h2>
    <p>An OData service describes its data as entities, entity types, properties, relationships, and entity sets. A service also exposes metadata so that a client can understand that model rather than relying only on hand-written endpoint documentation.</p>

    <p>That model shapes how a client reads and changes data. A client can address an entity or collection through a URL and use standard HTTP methods for supported operations. Query options such as <code>$filter</code>, <code>$select</code>, <code>$expand</code>, and <code>$orderby</code> let the client ask for a particular projection of the data.</p>

    <h2>OData is common in SAP Fiori, but the backend model still matters</h2>
    <p>SAPUI5 provides OData models that bind application controls to OData services. SAP Fiori elements goes further: it can interpret OData metadata and annotations and generate common application patterns without requiring developers to hand-code every view and controller.</p>

    <p>The protocol does not remove the backend application model. In modern ABAP development with RAP, a service definition selects what a business service exposes, and a service binding makes that service available through a chosen protocol such as OData V2 or OData V4. Authorization, transactional behavior, validations, and business semantics remain backend responsibilities.</p>

    <h2>V2 and V4 are related, not interchangeable labels</h2>
    <p>SAP landscapes contain both OData V2 and OData V4 services. They share the basic entity-and-metadata model, but capabilities and client behavior differ. A consumer therefore needs to know the version of the actual service rather than assuming that a V2 example can be copied unchanged into a V4 integration.</p>

    <p>The same caution applies to service availability. Saying that an SAP product “supports OData” is less useful than identifying the released service, its version, the operations it exposes, and the release in which it is available.</p>

    <h2>Good OData usage starts with the shape of the request</h2>
    <p>Because OData makes rich querying convenient, it is easy to ask for more data than a user or integration actually needs. Large collections, broad expansions, and unnecessary properties can turn a clean API into an expensive request. We usually get a better result when the client requests the smallest useful entity set, projection, and navigation path.</p>

    <p>This also improves diagnosis. If an application fails, first separate protocol and transport concerns from the business service itself: can the service be reached, does its metadata describe the expected entity, is the requested operation supported, and does the backend accept the business request? An HTTP error alone does not tell us which layer failed.</p>

    <h2>OData complements other SAP integration styles</h2>
    <p>OData is especially natural for resource-oriented APIs and user interfaces that need structured reads and updates. It does not make IDocs, SOAP services, events, or other interfaces obsolete. Those patterns solve different problems: asynchronous business messaging, contract-heavy service integration, event notification, and other forms of coupling. The right choice depends on the business interaction, not on which protocol looks newest.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_NETWEAVER_AS_ABAP_752/68bf513362174d54b58cddec28794093/79b1ea508f88bb7ee10000000a445394.html">SAP Gateway glossary: Open Data Protocol</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/sap_s4hana_on-premise/f2e545608079437ab165c105649b89db/81dc788fbda74883bd775a4036fa4b67.html">Using Service Binding Editor for OData V2 Service</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/abap-cloud/abap-development-tools-for-visual-studio-code/working-with-odata-v4-service-a449458b1816492eb972ae5728ca2a28">Working with OData V4 Service</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Service availability, OData version, supported query options, write behavior, authentication, and performance characteristics are specific to the released API and SAP product version. Verify the actual service contract before designing an integration.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a></li>
      <li><a href="/atlas/sap/fiori-ui5/">Fiori / UI5</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
