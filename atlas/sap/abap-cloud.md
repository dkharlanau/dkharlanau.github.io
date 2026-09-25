---
layout: default
title: "ABAP Cloud"
description: "ABAP Cloud explained: the development model, language versions, released APIs, and its role in clean-core extensions."
permalink: /atlas/sap/abap-cloud/
atlas_section: sap
domain: SAP operations
subdomain: Cloud development
concept_type: technology
sap_area: "ABAP Cloud"
business_process: "Platform and development"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - abap-cloud
  - cloud-development
  - clean-core
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-btp/
  - /atlas/sap/abap-platform/
  - /atlas/sap/rap/
  - /atlas/sap/cds-views/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">ABAP Cloud</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>ABAP Cloud</h1>
    <p class="note-subtitle">A development model that keeps custom ABAP behind released interfaces instead of coupling it directly to SAP internals.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Platform and development</dd></div>
      <div><dt>SAP area</dt><dd>ABAP Cloud</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until technology claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>The idea behind ABAP Cloud</h2>
    <p>ABAP Cloud is SAP's development model for building cloud-ready ABAP extensions and applications. The important change is not that ABAP suddenly runs in a different language. The change is the boundary around custom code: development uses cloud-optimized ABAP language versions and can access SAP objects only through interfaces that are released for the required use.</p>

    <p>This boundary matters because classical custom code can depend on internal tables, classes, function modules, or other implementation details that SAP may change during an upgrade. ABAP Cloud reduces that coupling. A released CDS view, class, BAdI, or other API becomes the contract between SAP code and the extension.</p>

    <h2>Language version and released APIs work together</h2>
    <p>Every ABAP repository object has a language-version context. <strong>Standard ABAP</strong> provides the broadest language and repository access. <strong>ABAP for Cloud Development</strong> and <strong>ABAP for Key Users</strong> use a restricted scope designed for upgrade-stable development. In these strict language versions, code normally accesses objects in its own software component or objects that SAP has explicitly released with an appropriate release contract.</p>

    <p>This is why ABAP Cloud should not be described simply as “ABAP with fewer statements.” The useful model is <em>restricted language + released interfaces + modern development models</em>. The restrictions are a way to enforce architectural boundaries rather than an end in themselves.</p>

    <h2>Where it is available</h2>
    <p>ABAP Cloud is used across several SAP product contexts. It is the mandatory ABAP development model in SAP BTP, ABAP environment and SAP S/4HANA Cloud Public Edition. In SAP S/4HANA and SAP S/4HANA Cloud Private Edition, Standard ABAP can still exist, while SAP recommends ABAP Cloud for new cloud-ready development where the required extension points and APIs are available.</p>

    <p>That distinction is important in real landscapes. ABAP Cloud does not mean that all existing classical ABAP disappears, and it does not automatically make every old enhancement replaceable. Migration depends on the available released interfaces and on what the custom code actually does.</p>

    <h2>What we build with it</h2>
    <p>ABAP Cloud brings together the newer ABAP development stack. ABAP Core Data Services models the data and semantics. The ABAP RESTful Application Programming Model (RAP) is used for transactional business objects and services. ABAP Development Tools in Eclipse provide the developer environment. Released APIs and extension points connect custom development to SAP-delivered functionality without relying on internal implementation details.</p>

    <p>A simple example is a custom application that needs sales-order information. In a classical design, custom code might read internal application tables directly. In an ABAP Cloud design, we first look for a released CDS view or business API that represents the required data. The second design may feel more constrained, but the dependency is explicit and therefore easier to carry through upgrades.</p>

    <h2>Clean core does not mean zero custom code</h2>
    <p>ABAP Cloud is often discussed together with clean core, but the two ideas should not be collapsed into a slogan. Clean core is about controlling how extensions depend on the ERP core. ABAP Cloud is one technical way to create that control for ABAP development. Custom logic can still be substantial; what changes is where it is placed and which contracts it is allowed to use.</p>

    <p>There is also a practical limit: released API coverage is not identical across products and releases. If the business requirement depends on an internal object for which no suitable released interface exists, the design needs another extension approach or a conscious exception. We should not label a solution “clean core” merely because its code uses modern syntax.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/abap-cloud/abap-cloud/abap-language">Cloud-Optimized ABAP Language</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/abap-cloud/developer-guide-from-classic-abap-to-abap-cloud/overview-of-key-concepts-in-abap-cloud">Overview of the Key Concepts in ABAP Cloud</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/ABAP_Cloud/abap-cloud-docs_abap-keyword-documentation_abap-for-cloud-development/abap-for-cloud-development?locale=en-US&amp;state=PRODUCTION&amp;version=latest">ABAP for Cloud Development</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Exact API availability, release contracts, extension options, and migration paths depend on the SAP product and release. Verify the required interfaces in the target system before treating a design as implementable.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/abap-platform/">ABAP Platform</a></li>
      <li><a href="/atlas/sap/rap/">RAP</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
