---
layout: default
title: "SAP S/4HANA"
description: "SAP S/4HANA explained: the ERP application, HANA foundation, core data-model changes, deployment variants, and extension boundaries."
permalink: /atlas/sap/sap-s4hana/
atlas_section: sap
domain: SAP operations
subdomain: Core ERP
concept_type: product
sap_area: "S/4HANA"
business_process: "Enterprise operations"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - sap-s4hana
  - erp
  - core-system
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/maps/integration-architecture-map/
  - /atlas/maps/event-driven-architecture-map/
  - /atlas/maps/data-mesh-architecture-map/
  - /atlas/maps/sap-data-products-map/
  - /atlas/maps/integration-monitoring-reliability-map/
  - /atlas/sap/sap-btp/
  - /atlas/sap/abap-platform/
  - /atlas/sap/abap-cloud/
  - /atlas/concepts/sap-integration-architecture/
  - /atlas/concepts/data-mesh-for-sap-landscapes/
  - /atlas/concepts/sap-data-product/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP S/4HANA</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP S/4HANA</h1>
    <p class="note-subtitle">SAP's ERP application suite for running core business transactions on the SAP HANA database.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Enterprise operations</dd></div>
      <div><dt>SAP area</dt><dd>S/4HANA core</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>SAP S/4HANA is an ERP application suite built for the SAP HANA database. It runs the business transactions behind areas such as finance, sales, sourcing and procurement, manufacturing, asset management, service, and supply-chain execution, depending on the licensed scope and deployment.</p>

    <p>The useful distinction is between the <strong>business application</strong> and the <strong>technical platform</strong>. SAP HANA is the database. ABAP Platform provides much of the application runtime and development foundation. SAP S/4HANA is the business application layer above them. A Fiori app, a CDS view, an ABAP class, and a sales order can all belong to the same solution landscape while serving very different roles.</p>

    <h2>The data model changed, but it did not become one giant table</h2>
    <p>S/4HANA simplified several parts of the older SAP ERP data model, but statements such as “everything is stored in one table” are misleading. In Finance, the Universal Journal uses <code>ACDOCA</code> as the central line-item structure for many accounting processes. Other application areas still have their own business objects, persistence, indexes, and compatibility structures.</p>

    <p>Material Ledger is another important S/4HANA foundation. SAP documents Material Ledger as mandatory in S/4HANA, while <strong>actual costing remains optional</strong>. Those are separate statements: using the Material Ledger data structures does not mean every customer must run an actual-costing close.</p>

    <h2>Business Partner is the leading master-data object for customers and suppliers</h2>
    <p>Customer and supplier master data is another major change from SAP ERP. In S/4HANA, Business Partner is the leading object for creating customer and supplier master data. Customer/Supplier Integration, commonly known as CVI, keeps the Business Partner model synchronized with the customer and supplier application structures that business processes still use.</p>

    <p>This matters during both implementation and conversion. A customer or supplier is not simply renamed to “BP.” The Business Partner carries shared identity and relationship data, while customer and supplier roles add the application-specific views needed for sales, purchasing, and accounting. For conversions from SAP ERP, SAP requires the relevant customer and supplier records to be converted to Business Partners.</p>

    <h2>A transaction still crosses several application layers</h2>
    <p>Consider an ordinary order-to-cash flow. A sales order uses master data, pricing, availability logic, partner data, and organizational assignments. Delivery adds logistics execution. Billing creates the commercial invoice and, where relevant, accounting postings. The resulting journal entries become part of Finance. S/4HANA integrates these steps, but it does not erase their process boundaries.</p>

    <p>That is why support work should follow the business document chain instead of starting with a random table or transaction code. A wrong sales price, a blocked delivery, and an accounting posting error can appear in one end-to-end process while originating in completely different configuration or data layers.</p>

    <h2>Deployment changes the operating and extension model</h2>
    <p>SAP currently offers S/4HANA in several deployment models. SAP S/4HANA Cloud Public Edition is positioned as the public-cloud ERP foundation of SAP Cloud ERP. SAP S/4HANA Cloud Private Edition and SAP S/4HANA on-premise provide a different degree of lifecycle control and extensibility. The exact feature scope, upgrade model, and available extension techniques are therefore deployment-specific.</p>

    <p>This distinction is more useful than saying that “S/4HANA supports cloud and on-premise.” A design that is valid in an on-premise or private-edition system may not be available in Public Edition, and a public-cloud extension should not be described using unrestricted classic ABAP assumptions.</p>

    <h2>Extensions should start from the supported contract</h2>
    <p>Modern S/4HANA extensibility ranges from configuration and key-user extensions to developer extensibility with ABAP Cloud and side-by-side applications on SAP BTP. RAP, CDS, released APIs, business events, and documented enhancement points are important parts of that model.</p>

    <p>Clean core is not the absence of custom requirements. It is a way of controlling dependencies on the ERP core. Before adding custom logic, we should know which system owns the business rule, which released interface or extension point is the contract, and how the extension survives an upgrade. Direct access to an internal object may work technically while creating a poor lifecycle dependency.</p>

    <h2>Integration and analytics are part of the landscape, not one built-in mechanism</h2>
    <p>S/4HANA exposes different integration styles for different business interactions, including OData and other APIs, IDocs, SOAP services, and business events. SAP Integration Suite can mediate and govern cross-system integrations, but it is not required for every interface. The right path depends on the released interface, interaction pattern, landscape, and operating model.</p>

    <p>Analytics follows the same principle. S/4HANA includes embedded analytical capabilities based on CDS and the analytical engine for operational analysis close to the transaction. Cross-system data harmonization, enterprise planning, and larger analytical architectures may use SAP Datasphere, SAP Analytics Cloud, or other platforms. Embedded analytics should not be presented as a replacement for every data-warehouse or planning use case.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP — <a href="https://www.sap.com/products/erp/s4hana-erp.html">SAP S/4HANA Cloud Public Edition and SAP Cloud ERP</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/25b46c8241fd4852bf7876d87bed8fd0.html">Business Partner Approach (Customer/Supplier Integration)</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMI-SE/af9ef57f504840d2b81be8667206d485/97f1d353ca9f4408e10000000a174cb4.html">Installation: Actual Costing/Material Ledger</a>.</li>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">Feature scope for SAP S/4HANA 2025</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Feature scope, terminology, lifecycle policy, available APIs, and extension options differ across SAP S/4HANA deployments and releases. Verify a requirement against the documentation for the exact target product and release before treating it as implementable.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/abap-platform/">ABAP Platform</a></li>
      <li><a href="/atlas/sap/abap-cloud/">ABAP Cloud</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
