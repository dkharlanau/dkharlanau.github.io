---
layout: default
title: "Cloud Connector"
description: "Analytical overview of SAP Cloud Connector: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/cloud-connector/
atlas_section: sap
domain: SAP operations
subdomain: Integration
concept_type: integration
sap_area: "Cloud Connector"
business_process: "System integration"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - cloud-connector
  - hybrid-cloud
  - btp
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-integration-landscape-map/
  - /atlas/sap/sap-btp/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/sap-s4hana/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">Cloud Connector</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Integration</p>
    <h1>Cloud Connector</h1>
    <p class="note-subtitle">Secure tunnel between SAP BTP cloud services and on-premise systems in hybrid landscapes.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>System integration</dd></div>
      <div><dt>SAP area</dt><dd>Cloud Connector</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until integration claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>SAP Cloud Connector is an on-premise component that establishes a secure tunnel between SAP BTP and internal systems. It exposes selected on-premise resources (RFC, JDBC, HTTP) to cloud applications without opening inbound firewall ports.</p>

    <h2>Business purpose</h2>
    <p>Enable hybrid cloud scenarios where BTP extensions, Integration Suite, and analytics services access on-premise data and functions securely. Maintain network perimeter integrity while extending SAP capabilities to the cloud.</p>

    <h2>Where it sits in the landscape</h2>
    <p>Cloud Connector runs inside the corporate network, connecting outward to SAP BTP subaccounts. It sits between BTP applications and on-premise backends (S/4HANA, ECC, databases, file servers). It is a critical dependency for hybrid integration, side-by-side extensions, and cloud analytics.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Cloud Connector instance: on-premise runtime.</li>
      <li>Subaccount mapping: BTP subaccount to Cloud Connector.</li>
      <li>Access control: exposed resources (RFC, JDBC, HTTP).</li>
      <li>Location ID: identifier for multi-site deployments.</li>
      <li>Principal propagation: user identity forwarding to backend.</li>
      <li>Audit log: connection events and access attempts.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: RFC and HTTP access for BTP extensions.</li>
      <li>BTP: Kyma, CAP, Integration Suite, Datasphere.</li>
      <li>Databases: JDBC access for HANA, Oracle, SQL Server.</li>
      <li>External: on-premise file servers, legacy systems.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Additional resource exposure via access control configuration.</li>
      <li>Multi-site deployment with location IDs.</li>
      <li>Custom principal propagation and SSO setup.</li>
      <li>High-availability pairing of Cloud Connector instances.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Cloud Connector status: connected, disconnected, or degraded.</li>
      <li>Backend availability: RFC ping, HTTP health check.</li>
      <li>Audit logs: failed access attempts, configuration changes.</li>
      <li>BTP cockpit: subaccount connectivity and resource mapping.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>No inbound firewall rules required.</li>
      <li>Fine-grained resource exposure control.</li>
      <li>Principal propagation for secure user context.</li>
      <li>Supports RFC, JDBC, and HTTP protocols.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Single point of failure if not deployed in HA pair.</li>
      <li>Network latency for cloud-to-on-premise calls.</li>
      <li>Version compatibility with BTP subaccount.</li>
      <li>Operational burden: patching, certificate renewal, monitoring.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Cloud Connector down — tunnel broken, all hybrid flows fail.</li>
      <li>Backend unreachable — RFC or HTTP target system offline.</li>
      <li>Certificate expiry — TLS handshake failure.</li>
      <li>Version mismatch — Cloud Connector too old for BTP subaccount.</li>
      <li>Resource not exposed — access control misconfiguration.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP Cloud Connector Documentation — <a href="https://help.sap.com/docs/connectivity/sap-btp-connectivity/cloud-connector">SAP Help Portal</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. Cloud Connector versions, supported protocols, and HA options vary by release and must be verified against the customer's system.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
