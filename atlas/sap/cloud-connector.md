---
layout: default
title: "Cloud Connector"
description: "SAP Cloud Connector explained: reverse-invoke connectivity, virtual-to-internal mappings, resource allowlists, principal propagation, and high availability."
permalink: /atlas/sap/cloud-connector/
atlas_section: sap
domain: SAP operations
subdomain: Integration
concept_type: integration
sap_area: "Cloud Connector"
business_process: "System integration"
status: needs_verification
verified: false
last_reviewed: 2026-09-22
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
    <p class="note-subtitle">Controlled connectivity from SAP BTP applications to selected resources inside a private network.</p>
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
    <p>SAP Cloud Connector is an on-premise component that gives selected SAP BTP applications a controlled path to systems inside a private network. Its most important property is the direction of trust: the connector establishes the connection outward and acts as a reverse-invoke proxy, so the company does not need to expose the whole internal landscape directly to the internet.</p>

    <h2>It exposes mappings and resources, not the whole network</h2>
    <p>The configuration maps a virtual cloud-facing host to an internal system. On top of that mapping, administrators define which resources are accessible. For HTTP scenarios this can mean selected URL paths. For RFC, the allowlist can be narrowed to specific function modules. The cloud application sees the virtual endpoint rather than needing the real internal host name.</p>

    <p>This is a useful security boundary. A working tunnel does not mean that every backend service is reachable. The connector can be connected to the subaccount while a particular application still fails because its system mapping, resource path, function module, or trust configuration is not allowed.</p>

    <h2>Protocol support depends on the scenario</h2>
    <p>Cloud Connector supports several cloud-to-on-premise connectivity patterns, including HTTP and RFC, and current versions also provide options such as WebSocket RFC and TCP/TCP TLS for supported use cases. Each protocol has different access-control possibilities. RFC, for example, allows strict function-module allowlisting, while plain TCP provides less application-level visibility and therefore requires additional care.</p>

    <p>That is why it is better to design the connectivity around the actual application protocol than to describe Cloud Connector as a generic “secure tunnel” and stop there. The security properties depend on what is mapped, which resources are exposed, and how the application authenticates to the backend.</p>

    <h2>Identity propagation is separate from network reachability</h2>
    <p>Cloud Connector can participate in principal-propagation scenarios, but connectivity and identity are different concerns. A request can have a valid network route and still fail because the backend does not trust or authorize the propagated user. Conversely, a technically valid identity configuration is useless if the requested backend resource is not exposed through access control.</p>

    <h2>High availability needs a second instance</h2>
    <p>SAP supports a high-availability setup with a master and a shadow Cloud Connector. The master synchronizes its configuration to the shadow. If the master becomes unavailable, the shadow can take over and establish the connection to SAP BTP.</p>

    <p>This matters because Cloud Connector can sit on the critical path for several hybrid applications. If multiple business processes depend on the same instance, its availability becomes an architectural concern rather than a small infrastructure detail. We should therefore understand which applications depend on each connector and whether the deployment has an appropriate redundancy model.</p>

    <h2>How to read a connectivity failure</h2>
    <p>A useful diagnosis follows the path of the request. Is the Cloud Connector connected to the intended subaccount? Does the virtual system map to the correct internal target? Is the requested resource allowed? Can the connector reach the backend? Is the backend authentication or propagated identity accepted?</p>

    <p>Keeping those layers separate prevents a common mistake: treating every hybrid connectivity error as a network outage. In many cases the network path is healthy and the failure is caused by deliberately restrictive access control, a wrong virtual mapping, or an application-level authorization problem.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf">SAP BTP Connectivity / Cloud Connector</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf/ca5868997e48468395cf0ca4882f5783.html">Configure Access Control (RFC)</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf/high-availability-setup">High Availability Setup</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Supported protocols, identity options, operational recommendations, and connectivity features change with Cloud Connector versions and SAP BTP services. Verify the current documentation for the exact protocol and application before implementing a production path.</p>
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
