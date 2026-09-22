---
layout: default
title: "CDS Views"
description: "ABAP CDS views explained: semantic data modeling, view entities, associations, annotations, and how applications consume them."
permalink: /atlas/sap/cds-views/
atlas_section: sap
domain: SAP operations
subdomain: Data modeling
concept_type: technology
sap_area: "CDS"
business_process: "Data access and analytics"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - cds-views
  - data-modeling
  - analytics
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-datasphere/
  - /atlas/sap/sap-analytics-cloud/
  - /atlas/sap/rap/
  - /atlas/sap/odata/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">CDS Views</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>CDS Views</h1>
    <p class="note-subtitle">A semantic data-modeling layer in ABAP that describes data, relationships, and meaning above the physical tables.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Data access and analytics</dd></div>
      <div><dt>SAP area</dt><dd>CDS</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until technology claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Why CDS exists</h2>
    <p>ABAP Core Data Services (CDS) lets developers define reusable data models close to the application semantics instead of making every consumer reconstruct business meaning from database tables. A CDS entity can select and combine data, define relationships, add semantic annotations, and become a building block for other CDS entities or ABAP applications.</p>

    <p>This is the useful shift: a table tells us how data is stored; a CDS model can tell us what the data represents and how it relates to the rest of the business model. That distinction is especially important in SAP S/4HANA, where application consumers should not assume that a physical table is the best long-term interface.</p>

    <h2>View entities are the modern default</h2>
    <p>Modern ABAP CDS development uses <strong>CDS view entities</strong>, defined with <code>DEFINE VIEW ENTITY</code>. SAP describes them as the successor to older DDIC-based CDS views. A view entity can select from database tables or other CDS entities, expose elements, define associations, and carry annotations that add technical or semantic information.</p>

    <p>Once activated, the CDS entity becomes a repository object that other CDS models and ABAP SQL can use. This makes CDS compositional: a low-level entity can expose stable fields and associations, while higher-level entities add a projection or a domain-specific view for a particular application.</p>

    <h2>Associations express relationships</h2>
    <p>Associations are one of the most important CDS ideas. Instead of repeating join logic in every consumer, the model can describe how one entity relates to another. A sales document item, for example, may expose an association to its product or business partner. Consumers can follow that relationship when they need it rather than treating every data model as one giant flattened query.</p>

    <p>Cardinality still matters. An association that is modeled incorrectly can mislead consumers and can change query behavior. CDS makes relationships easier to express, but it does not remove the need to understand the underlying data.</p>

    <h2>Annotations add meaning for frameworks</h2>
    <p>Annotations enrich the model with metadata. Depending on the annotation vocabulary and consuming framework, they can describe labels, analytical semantics, authorization behavior, search characteristics, UI metadata, or service-related properties. Because annotations can be inherited and propagated through CDS layers, the effective value seen by a consumer may come from more than one definition.</p>

    <p>This is why an annotation problem is not always visible in the file currently open in the editor. SAP provides an Annotation Propagation view in the ABAP development tools so developers can trace where effective annotation values originate.</p>

    <h2>CDS is used by several application models</h2>
    <p>ABAP CDS is a shared modeling foundation rather than a reporting-only technology. RAP uses CDS entities to model transactional business objects and service projections. ABAP analytics uses CDS to model dimensions, facts, cubes, hierarchies, and analytical queries. ABAP programs can read CDS entities through ABAP SQL. Other frameworks can consume metadata exposed from the same model.</p>

    <p>That does not mean that every CDS view automatically becomes an OData API, a Fiori application, or an analytical query. Exposure requires the corresponding service or application model. Keeping these layers separate avoids a common misconception: CDS defines the model; another framework decides how that model is executed or exposed for a particular use case.</p>

    <h2>ABAP CDS and CAP CDS are related, but not interchangeable</h2>
    <p>SAP also uses the name Core Data Services in CAP. The two worlds share declarative modeling ideas and similar vocabulary, but they run in different development environments and have different runtimes and feature sets. On this page, “CDS view” refers to <strong>ABAP CDS</strong> in the ABAP platform context.</p>

    <h2>What makes a CDS model durable</h2>
    <p>A good CDS model does more than return the right rows today. Its entities have clear responsibility, associations reflect real relationships, semantic annotations are intentional, and consumers depend on stable released interfaces where required. Deep stacks of views, unnecessary associations, and accidental dependencies can make a model harder to understand and operate even when the individual definitions are valid.</p>

    <p>In practice, we treat CDS as an application contract rather than a convenient SQL shortcut. That mindset makes it easier to decide which fields belong in a reusable model, which logic belongs in a higher layer, and which SAP-delivered entity is safe to consume.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP ABAP Keyword Documentation — <a href="https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/abencds_v2_views.htm">ABAP CDS - View Entities</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/abap-cloud/abap-data-models/analyticsdetails-annotations">ABAP Data Models</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/abap_platform/f2e545608079437ab165c105649b89db/119ff2bc079a48d5bb784b2bc3de19ef.html">Annotation Propagation View</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Available CDS features, annotations, release states, and framework behavior depend on the ABAP product and release. Verify the specific entity and its release contract in the target environment before using it as a stable extension interface.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/rap/">RAP</a></li>
      <li><a href="/atlas/sap/cds-analytical-views/">CDS Analytical Views</a></li>
      <li><a href="/atlas/sap/odata/">OData</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
