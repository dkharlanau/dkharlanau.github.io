---
layout: default
title: "SOAP"
description: "Analytical overview of SOAP in SAP: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/soap/
atlas_section: sap
domain: SAP operations
subdomain: Integration
concept_type: integration
sap_area: "SOAP"
business_process: "System integration"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - soap
  - wsdl
  - integration
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-integration-landscape-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/rest-apis/
  - /atlas/sap/odata/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SOAP</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Integration</p>
    <h1>SOAP</h1>
    <p class="note-subtitle">Legacy web service standard for structured, protocol-heavy enterprise integration in SAP.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>System integration</dd></div>
      <div><dt>SAP area</dt><dd>SOAP</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until integration claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>SOAP (Simple Object Access Protocol) is a messaging protocol for exchanging structured information via XML envelopes. It relies on WSDL (Web Services Description Language) for service contracts and supports WS-* standards for security, reliability, and transactions.</p>

    <h2>Business purpose</h2>
    <p>Provide a standardized, contract-first integration mechanism for enterprise systems. Support rigid, auditable service interactions with built-in error handling and transactional integrity.</p>

    <h2>Where it sits in the landscape</h2>
    <p>SOAP is declining in new development but remains prevalent in established SAP landscapes. It is used for Enterprise Services, BAPI exposure as web services, PI/PO interfaces, and Integration Suite protocol conversion. It competes with REST and OData for new projects.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>WSDL: machine-readable service contract (operations, types, bindings).</li>
      <li>SOAP envelope: XML wrapper with header and body.</li>
      <li>XML payload: strongly typed request and response data.</li>
      <li>WS-Security: encryption, signatures, and token profiles.</li>
      <li>Endpoint URL: service address for SOAP binding.</li>
      <li>SOAPAction: HTTP header indicating the intended operation.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: Enterprise Services, BAPI as web service.</li>
      <li>SAP PI/PO: SOAP sender and receiver adapters.</li>
      <li>Integration Suite: SOAP-to-REST conversion, protocol bridging.</li>
      <li>External: legacy ERP, banking, government, and partner systems.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom Enterprise Services and BAPI wrappers.</li>
      <li>WSDL customization and XSD extensions.</li>
      <li>WS-Security policy configuration.</li>
      <li>Mapping and transformation in PI/PO or Integration Suite.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>SOAP fault messages: structured error responses.</li>
      <li>HTTP status: 500 for SOAP faults, 200 with fault body.</li>
      <li>WSDL validation: schema compliance, binding errors.</li>
      <li>PI/PO or Integration Suite message monitor.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Strict contracts via WSDL reduce integration ambiguity.</li>
      <li>WS-* standards provide enterprise-grade security and reliability.</li>
      <li>Tooling support for code generation from WSDL.</li>
      <li>Mature error handling with standardized fault envelopes.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Verbose XML payloads increase bandwidth and parsing overhead.</li>
      <li>Complex WS-* stack is hard to debug and configure.</li>
      <li>Declining ecosystem support in modern frameworks.</li>
      <li>Interoperability issues between vendor implementations.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>SOAP fault — schema validation or business rule failure.</li>
      <li>WSDL mismatch — service updated, consumer not regenerated.</li>
      <li>WS-Security error — certificate expiry, token mismatch.</li>
      <li>Timeout — large XML payload or slow downstream processing.</li>
      <li>Encoding issue — character set mismatch in XML declaration.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
      <li><a href="/atlas/sap/rest-apis/">REST APIs</a></li>
      <li><a href="/atlas/sap/odata/">OData</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. SOAP service availability, WS-* configuration, and integration mechanisms vary by S/4HANA release and must be verified against the customer's system.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
