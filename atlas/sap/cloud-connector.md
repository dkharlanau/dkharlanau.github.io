---
layout: default
title: "Cloud Connector"
description: "SAP Cloud Connector explained through BTP destinations, virtual-to-internal mappings, access control, identity propagation, and high availability."
permalink: /atlas/sap/cloud-connector/
atlas_section: sap
domain: SAP operations
subdomain: Integration
concept_type: integration
sap_area: "Cloud Connector"
business_process: "System integration"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
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
    <p class="note-subtitle">A controlled bridge from SAP BTP to selected services inside a private network.</p>
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
    <p>SAP Cloud Connector is the on-premise component of SAP BTP Connectivity used in hybrid scenarios. It initiates a secure connection from the private network to SAP BTP and routes approved requests to internal systems. That is why it is often described as a reverse-invoke proxy: the company does not need to make an internal SAP system generally reachable from the public internet just because a BTP application needs to call it.</p>

    <p>It is not a VPN for the whole network, an API gateway, or an integration runtime. Its job is narrower: connect a BTP subaccount to selected private resources and enforce the mappings and access rules configured for that route.</p>

    <h2>A request crosses several boundaries</h2>
    <p>A useful way to understand Cloud Connector is to follow one request. A BTP application usually works with a destination or another BTP connectivity mechanism that identifies the target and authentication approach. For an on-premise target, the BTP connectivity layer routes the request through the secure tunnel established by Cloud Connector. Cloud Connector then checks its access-control configuration, translates the virtual target to the internal host and port, and forwards the request to the backend.</p>

    <p>The backend remains a separate security and application boundary. Reaching an ABAP system through Cloud Connector does not bypass its authentication, authorization, service activation, or business validation. A request can therefore pass the BTP connectivity layer and still be rejected correctly by the target system.</p>

    <h2>Virtual hosts separate the cloud contract from the internal address</h2>
    <p>Cloud Connector maps a <strong>virtual host and port</strong> used on the cloud side to a real <strong>internal host and port</strong>. The virtual name does not have to exist in internal DNS. It gives the cloud-facing configuration a stable identifier that does not expose the physical backend address and can remain unchanged when the internal route is adjusted.</p>

    <p>The host mapping is only the first permission. Administrators also define which resources are exposed. For HTTP scenarios, access can be restricted to selected URL paths. For classic RFC, Cloud Connector requires allowed function modules and supports exact names or controlled prefixes. This is an important distinction: a system can be reachable from Cloud Connector while the requested service is still deliberately blocked.</p>

    <p>Protocol choice affects how much control Cloud Connector can apply. HTTP and RFC let it understand application-level resources. Generic TCP is broader; SAP explicitly warns that Cloud Connector cannot inspect TCP requests in the same way and recommends tighter trust and application controls. Treating every protocol as the same kind of “tunnel” loses an important part of the security model.</p>

    <h2>Destination, route, and backend identity are different things</h2>
    <p>Three configurations are easy to mix together. A BTP <strong>destination</strong> describes how a consumer addresses and authenticates toward a remote service. Cloud Connector defines whether that virtual target and resource may cross into the private network. The backend then decides whether the technical user or business user is allowed to perform the requested operation.</p>

    <p>This separation becomes especially visible with principal propagation. Cloud Connector can participate in forwarding the logged-on user's identity to an internal system, but it does not make identity propagation automatic. Trust must be established for the identity source, Cloud Connector needs the required system trust material, and the backend must trust the connector and map the propagated identity to a valid user. Network reachability and user identity are therefore separate chains.</p>

    <h2>Location IDs choose among multiple connector routes</h2>
    <p>A subaccount can use more than one Cloud Connector route. SAP provides a <strong>location ID</strong> so supported consumers can select the intended connector when several connectors are attached to the same subaccount. This is useful when different network locations, subsidiaries, or private landscapes must stay separate even though they are reached from one BTP subaccount.</p>

    <p>A location ID is routing metadata, not high availability by itself. Two independent connectors with different locations do not automatically fail over to each other. Redundancy for one Cloud Connector setup uses the product's master-and-shadow high-availability model.</p>

    <h2>High availability protects the connector, not the backend</h2>
    <p>In the supported high-availability setup, a master Cloud Connector synchronizes its configuration to a separately installed shadow instance. The shadow monitors the master and can take over the connection to SAP BTP when the master becomes unavailable.</p>

    <p>That protects the connector layer, but it does not make the internal target highly available. The backend system, DNS, network route, certificates, and authentication path still need their own availability design. SAP also warns that unstable communication between master and shadow can cause a temporary double-master situation, so the HA pair itself needs a reliable network relationship.</p>

    <h2>A concrete hybrid call</h2>
    <p>Consider a BTP application that reads an OData service from a private SAP S/4HANA system. The cloud-side configuration addresses a virtual host rather than the internal S/4HANA host. BTP connectivity sends the request through the tunnel for the correct subaccount and, where relevant, location. Cloud Connector maps that virtual address to the internal system and checks whether the required HTTP path is exposed. The S/4HANA system then performs its own authentication, authorization, and OData processing.</p>

    <p>If the call fails, these layers give us a better diagnostic order than simply checking whether “Cloud Connector is green.” First confirm that the consumer is using the intended destination and route. Then check the subaccount and location connection, the virtual-to-internal mapping, and the exposed resource. Only after that do backend TLS, authentication, authorization, service, and business errors become the likely next layer.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf/connectivity">What Is SAP BTP Connectivity?</a></li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf/ca5868997e48468395cf0ca4882f5783.html">Configure Access Control (RFC)</a></li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf/configure-access-control-tcp">Configure Access Control (TCP)</a></li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf/set-up-trust-for-principal-propagation">Set Up Trust for Principal Propagation</a></li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf/high-availability-setup">High Availability Setup</a></li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Supported protocols, authentication options, connectivity components, version-specific features, and operational recommendations change over time. Verify the current SAP BTP Connectivity documentation and the exact consumer, protocol, and backend used in the target landscape before turning this overview into a production design.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
