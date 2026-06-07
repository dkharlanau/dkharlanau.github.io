---
layout: default
title: "IDoc"
description: "Analytical overview of IDoc in SAP: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/idoc/
atlas_section: sap
domain: SAP operations
subdomain: Document integration
concept_type: integration
sap_area: "IDoc"
business_process: "System integration"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - idoc
  - edi
  - integration
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-integration-landscape-map/
  - /atlas/maps/integration-architecture-map/
  - /atlas/maps/integration-monitoring-reliability-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-integration-suite/
  - /atlas/concepts/sap-integration-architecture/
  - /atlas/concepts/integration-pattern-decision-matrix/
  - /atlas/concepts/rest-vs-odata-vs-soap-vs-idoc-vs-events/
  - /atlas/concepts/retry-and-error-handling/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">IDoc</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Integration</p>
    <h1>IDoc</h1>
    <p class="note-subtitle">Intermediate Document for structured batch and real-time data exchange in SAP.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>System integration</dd></div>
      <div><dt>SAP area</dt><dd>IDoc</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until integration claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>IDoc (Intermediate Document) is SAP's structured document format for exchanging business data between systems. It supports both batch and real-time processing via ALE (Application Link Enabling), EDI, and RFC.</p>

    <h2>Business purpose</h2>
    <p>Exchange master data and transactional data between SAP systems and with external partners. Support EDI standards for supply chain integration. Provide a robust, auditable document trail.</p>

    <h2>Where it sits in the landscape</h2>
    <p>IDoc is the document layer beneath OData and business events. It is used for system-to-system integration (ALE), EDI with trading partners, and legacy RFC-based interfaces. It is processed via SAP Gateway, PI/PO, or Integration Suite.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>IDoc type: structure definition (e.g., ORDERS05, INVOIC02).</li>
      <li>Message type: business meaning (e.g., ORDERS, DESADV, INVOIC).</li>
      <li>Partner profile: sender/receiver configuration.</li>
      <li>Port: communication method (file, RFC, tRFC, HTTP).</li>
      <li>Segment: data record within an IDoc.</li>
      <li>Status: processing state (01-74, success, error, warning).</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: ALE distribution, change pointers, master data replication.</li>
      <li>SAP PI/PO: IDoc-to-EDI mapping, protocol conversion.</li>
      <li>Integration Suite: modern IDoc processing and monitoring.</li>
      <li>External: EDI partners, third-party ERP, customs systems.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom IDoc types and segments.</li>
      <li>Custom processing logic (user exits, BAdIs).</li>
      <li>Mapping and transformation in PI/PO or Integration Suite.</li>
      <li>Side-by-side monitoring apps on BTP.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>IDoc status monitor: WE02, WE05, BD87.</li>
      <li>Partner profile consistency: WE20, WE21.</li>
      <li>Segment error: data format, length, or mandatory field.</li>
      <li>Port and RFC connection: SM59, gateway status.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Mature, well-documented integration mechanism.</li>
      <li>Robust error handling and retry.</li>
      <li>Auditable document trail with status history.</li>
      <li>Broad EDI and partner support.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Verbose status management and monitoring overhead.</li>
      <li>Segment definition changes require partner coordination.</li>
      <li>Performance: large IDoc volumes can bottleneck.</li>
      <li>Error resolution is manual and time-consuming.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>IDoc stuck in status 51 or 64 — partner profile, segment, or port.</li>
      <li>Duplicate IDoc — change pointer or trigger misconfiguration.</li>
      <li>Segment error — data format, length, or mandatory field.</li>
      <li>Partner not found — profile missing or wrong partner number.</li>
      <li>IDoc not generated — message type, change pointer, or filter.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. IDoc types, message types, and processing mechanisms vary by S/4HANA release and must be verified against the customer's system.</p>

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
