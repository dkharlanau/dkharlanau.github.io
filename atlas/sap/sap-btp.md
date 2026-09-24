---
layout: default
title: "SAP BTP"
description: "SAP BTP explained through its account model, environments, services, connectivity, and role in extensions and integration."
permalink: /atlas/sap/sap-btp/
atlas_section: sap
domain: SAP operations
subdomain: Business Technology Platform
concept_type: product
sap_area: "BTP"
business_process: "Platform and integration"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - sap-btp
  - cloud-platform
  - extensions
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/maps/integration-architecture-map/
  - /atlas/maps/event-driven-architecture-map/
  - /atlas/maps/integration-monitoring-reliability-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/cap/
  - /atlas/concepts/sap-integration-architecture/
  - /atlas/concepts/sap-event-driven-architecture/
  - /atlas/concepts/ai-ready-data-layer/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP BTP</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP BTP</h1>
    <p class="note-subtitle">SAP's cloud platform for building extensions, integrating applications, and consuming platform services around business systems.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Platform and integration</dd></div>
      <div><dt>SAP area</dt><dd>BTP</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>SAP Business Technology Platform (BTP) is not one application server and not one middleware product. It is a cloud platform with an account model, several runtime environments, managed services, application subscriptions, security services, and connectivity capabilities. That distinction matters because saying “it runs on BTP” does not tell us where an application actually runs or which services it depends on.</p>

    <h2>The account model comes before the runtime</h2>
    <p>A customer starts with a <strong>global account</strong>. Optional directories can organize the landscape, and <strong>subaccounts</strong> are the regional operational boundaries where applications are deployed, services are used, subscriptions are managed, and entitlements are assigned. SAP explicitly treats subaccounts as independent boundaries for areas such as security, members, data, and integration.</p>

    <p>Below the subaccount, structure depends on the environment. Enabling Cloud Foundry creates a Cloud Foundry organization for the subaccount and allows spaces inside that organization. Enabling Kyma provisions Kubernetes-based runtime resources and uses namespaces inside the cluster. These are different runtime models; a “space” is therefore not a universal BTP object.</p>

    <h2>BTP offers several ways to run or consume functionality</h2>
    <p>Cloud Foundry is a managed application runtime commonly used for CAP and other cloud applications. Kyma provides a managed Kubernetes-based environment for containerized workloads and event-driven extensions. SAP BTP also has an ABAP environment for cloud applications and extensions built with ABAP Cloud, RAP, CDS, and released APIs.</p>

    <p>Many BTP capabilities are consumed as managed services or subscriptions rather than deployed as custom code. Integration Suite, SAP HANA Cloud, SAP Build products, identity and connectivity services, and other offerings each have their own plans, lifecycle, quotas, regional availability, and operating model. We therefore design with named services instead of treating “BTP” as a single technical component.</p>

    <h2>Entitlements decide what a subaccount can consume</h2>
    <p>Commercial entitlement and technical configuration are related but separate. Entitlements and quotas purchased or available at global-account level are assigned to subaccounts or directories. A subaccount administrator can then create eligible service instances, subscribe to applications, or enable environments according to the available plans.</p>

    <p>This explains a common source of confusion: a service may exist in the SAP portfolio but still be unavailable in a particular subaccount because the plan, region, entitlement, quota, or commercial contract does not allow it. “BTP supports it” is therefore not enough for an implementation decision.</p>

    <h2>Connectivity and identity are architectural boundaries</h2>
    <p>Side-by-side extensions often need business data or APIs from SAP S/4HANA and other systems. Destinations can hold connectivity and authentication information for consumers on BTP, while SAP Cloud Connector can provide controlled access to resources in private networks for supported scenarios. Integration Suite or event services may sit between systems when mediation or asynchronous communication is needed.</p>

    <p>Identity follows the same principle. A BTP subaccount establishes trust with identity providers, while applications and platform services apply their own authorization models. Role collections are an important BTP authorization construct, but they should not be confused with ABAP PFCG roles or with identity provisioning itself. The full access path can cross corporate identity, SAP Cloud Identity Services, BTP trust configuration, role collections, application roles, and backend authorizations.</p>

    <h2>Clean core is a design goal, not a location rule</h2>
    <p>BTP is often used for side-by-side extensions because extension logic can live outside the ERP core and consume released APIs or events. This can support clean-core goals, but merely moving custom code to BTP does not make an extension clean. A BTP application can still depend on unstable interfaces, duplicate ERP logic, or create tight coupling through undocumented assumptions.</p>

    <p>When we choose BTP for an extension, we still ask where the business transaction belongs, which system owns the data, which released interface forms the contract, how failures are reconciled, and who operates the additional cloud component. BTP gives us more architectural options; it does not remove those decisions.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP BTP — <a href="https://help.sap.com/docs/btp/sap-business-technology-platform/account-model">Account Model</a>.</li>
      <li>SAP BTP — <a href="https://help.sap.com/docs/btp/sap-business-technology-platform/00aa2c23479d42568b18882b1ca90d79.html">Entitlements and Quotas</a>.</li>
      <li>SAP BTP — <a href="https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/468c2f3c3ca24c2c8497ef9f83154c44.html">Kyma Environment</a>.</li>
      <li>SAP BTP — <a href="https://help.sap.com/docs/btp/sap-business-technology-platform/abap-environment">ABAP Environment</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>BTP environments, service plans, quotas, regions, commercial models, and product availability change frequently. Verify the current service catalog, entitlement, regional availability, and documentation for the exact subaccount before using this overview as a deployment design.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
      <li><a href="/atlas/sap/cloud-connector/">Cloud Connector</a></li>
      <li><a href="/atlas/sap/cap/">CAP</a></li>
      <li><a href="/atlas/sap/abap-cloud/">ABAP Cloud</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
