---
layout: default
title: "EDI"
description: "Analytical overview of EDI in SAP: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/edi/
atlas_section: sap
domain: SAP operations
subdomain: Integration
concept_type: integration
sap_area: "EDI"
business_process: "System integration"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - edi
  - edifact
  - supply-chain
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-integration-landscape-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/idoc/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">EDI</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Integration</p>
    <h1>EDI</h1>
    <p class="note-subtitle">Electronic Data Interchange for structured trading partner communication in supply chain integration.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>System integration</dd></div>
      <div><dt>SAP area</dt><dd>EDI</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until integration claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>EDI (Electronic Data Interchange) is the structured exchange of business documents between trading partners using standardized formats. Common standards include EDIFACT (international), X12 (North America), and XML/EDI variants. It replaces paper-based transactions with machine-readable messages.</p>

    <h2>Business purpose</h2>
    <p>Automate order-to-cash and procure-to-pay cycles with suppliers, customers, and logistics providers. Reduce manual data entry, accelerate transaction processing, and enforce contractual data quality.</p>

    <h2>Where it sits in the landscape</h2>
    <p>EDI operates at the boundary between SAP and external trading partners. SAP systems typically use IDoc as the internal format, with EDI standards applied at the exchange layer. SAP Integration Suite, PI/PO, or third-party translators handle format conversion and transmission.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>EDIFACT message: ORDERS, INVOIC, DESADV, etc.</li>
      <li>X12 transaction set: 850 (PO), 810 (invoice), 856 (ASN).</li>
      <li>IDoc type: internal SAP representation (e.g., ORDERS05).</li>
      <li>Partner agreement: message type, version, and communication protocol.</li>
      <li>Mapping rules: EDI segment to IDoc segment conversion.</li>
      <li>Communication protocol: AS2, SFTP, VAN, or HTTP.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: IDoc-based EDI inbound and outbound.</li>
      <li>SAP PI/PO: EDI-to-IDoc mapping and protocol adapters.</li>
      <li>Integration Suite: cloud-based EDI processing and partner management.</li>
      <li>External: trading partners, VANs, third-party EDI translators.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom IDoc types for non-standard EDI messages.</li>
      <li>Mapping extensions in PI/PO or Integration Suite.</li>
      <li>Partner-specific segment and qualifier handling.</li>
      <li>Side-by-side EDI monitoring apps on BTP.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>IDoc status monitor: WE02, WE05 for post-EDI processing.</li>
      <li>EDI acknowledgments: CONTRL, 997 functional acknowledgment.</li>
      <li>Mapping errors: segment mismatch, qualifier invalid.</li>
      <li>Transmission logs: AS2 MDN, SFTP transfer status.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Industry-standard formats ensure broad partner compatibility.</li>
      <li>Automated end-to-end document exchange reduces latency.</li>
      <li>Auditable trail with acknowledgments and status tracking.</li>
      <li>Mature tooling for mapping, validation, and error recovery.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Standard versions differ by region and partner.</li>
      <li>Mapping maintenance is labor-intensive.</li>
      <li>Error resolution often requires manual partner coordination.</li>
      <li>Legacy VANs add cost and latency.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>EDI message rejected — mapping error, segment mismatch, or qualifier issue.</li>
      <li>Missing acknowledgment — partner not responding or AS2 failure.</li>
      <li>Duplicate EDI — resend without deduplication logic.</li>
      <li>Partner profile mismatch — wrong GLN, DUNS, or test flag.</li>
      <li>IDoc stuck after EDI — post-processing error in SAP.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
      <li><a href="/atlas/sap/idoc/">IDoc</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. EDI standards, partner configurations, and integration mechanisms vary by S/4HANA release and must be verified against the customer's system.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
      <li><a href="/atlas/sap/idoc/">IDoc</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
