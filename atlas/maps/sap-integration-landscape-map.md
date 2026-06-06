---
layout: default
title: "SAP Integration Landscape Map"
description: "A landscape map of SAP integration mechanisms, protocols, and middleware for operational navigation."
permalink: /atlas/maps/sap-integration-landscape-map/
atlas_section: maps
domain: SAP operations
subdomain: Integration landscape
concept_type: map
sap_area: "SAP integration"
business_process: "Enterprise operations"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - sap-integration
  - landscape-map
  - middleware
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/sap-btp/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/maps/">Maps</a></li>
    <li aria-current="page">SAP Integration Landscape Map</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Map</p>
    <h1>SAP integration landscape map</h1>
    <p class="note-subtitle">A navigation frame for integration mechanisms, protocols, and middleware in the SAP ecosystem.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Domain</dt><dd>SAP operations</dd></div>
      <div><dt>Type</dt><dd>landscape map</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until integration mechanism claims are verified.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What this map is</h2>
    <p>An integration-level view of the SAP ecosystem. It groups mechanisms by protocol, direction, and typical use case rather than by SAP product name.</p>

    <h2>Business purpose</h2>
    <p>Help integration architects and support teams choose the right mechanism, understand failure modes, and trace where a message or event stopped.</p>

    <h2>API-based integration</h2>
    <ul>
      <li><a href="/atlas/sap/odata/">OData</a> — RESTful APIs for synchronous read/write, Fiori, and third-party access.</li>
      <li>SOAP — legacy web services, often used for BAPI exposure.</li>
    </ul>

    <h2>Event-based integration</h2>
    <ul>
      <li><a href="/atlas/sap/business-events/">Business Events</a> — SAP's event mesh for asynchronous, decoupled communication.</li>
    </ul>

    <h2>Document-based integration</h2>
    <ul>
      <li><a href="/atlas/sap/idoc/">IDoc</a> — structured EDI-like documents for batch and real-time exchange.</li>
    </ul>

    <h2>Output and communication</h2>
    <ul>
      <li><a href="/atlas/sap/output-control/">Output Control</a> — print, email, PDF, and electronic output from SAP documents.</li>
    </ul>

    <h2>Middleware and orchestration</h2>
    <ul>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a> — cloud integration platform with prebuilt content.</li>
      <li>SAP BTP Integration — API management, event mesh, and data intelligence.</li>
    </ul>

    <h2>Where they sit</h2>
    <p>OData and SOAP are the API layer. Business Events are the event layer. IDoc is the document layer. Output Control is the communication layer. SAP Integration Suite and BTP sit above them as orchestration and management layers.</p>

    <h2>Integration decision frame</h2>
    <ul>
      <li>Real-time UI data → OData.</li>
      <li>Real-time system notification → Business Events.</li>
      <li>Batch master data sync → IDoc or OData bulk.</li>
      <li>Third-party EDI → IDoc + SAP Integration Suite.</li>
      <li>Document output → Output Control + Adobe Forms / Smart Forms.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Multiple integration styles cover most enterprise patterns.</li>
      <li>SAP Integration Suite reduces custom middleware.</li>
      <li>Business Events enable real-time, decoupled architectures.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>IDoc monitoring is verbose and error-prone at scale.</li>
      <li>OData performance degrades with complex expands and large result sets.</li>
      <li>Event ordering and delivery guarantees vary by middleware.</li>
      <li>Output Control configuration is release-specific and often under-documented.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>IDoc stuck in status 51 or 64 — partner profile, segment definition, or port issue.</li>
      <li>OData service returns 500 — metadata mismatch or authorization.</li>
      <li>Business event not delivered — event mesh subscription or filter issue.</li>
      <li>Output not generated — condition table, access sequence, or spool issue.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-product-landscape-map/">SAP Product Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Integration descriptions are based on public SAP documentation. Specific configuration, supported protocols, and middleware versions must be verified against the customer's S/4HANA release and integration tenant.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-product-landscape-map/">SAP Product Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
