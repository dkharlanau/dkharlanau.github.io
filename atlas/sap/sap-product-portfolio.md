---
layout: default
title: "SAP Product Portfolio"
description: "A practical map of the current SAP product portfolio: how cloud ERP, line-of-business applications, data, AI, BTP, networks, and transformation products fit together."
permalink: /atlas/sap/sap-product-portfolio/
atlas_section: sap
domain: SAP operations
subdomain: Product landscape
concept_type: reference
sap_area: "Cross-product"
business_process: "Enterprise operations"
status: needs_verification
verified: false
last_synced: 2026-09-23
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - sap-products
  - sap-portfolio
  - sap-landscape
related:
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-btp/
  - /atlas/sap/sap-business-ai/
  - /atlas/sap/sap-ariba/
  - /atlas/sap/sap-ibp/
  - /atlas/sap/sap-ewm/
  - /atlas/sap/sap-tm/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Product Portfolio</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Reference</p>
    <h1>SAP Product Portfolio</h1>
    <p class="note-subtitle">A practical map of the SAP landscape: which products run the business, which extend it, and where the important system boundaries sit.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Scope</dt><dd>Current portfolio structure and major product families</dd></div>
      <div><dt>Source</dt><dd>SAP public product pages and product documentation</dd></div>
      <div><dt>Last synced</dt><dd>2026-09-23</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Read the portfolio as a landscape, not a shopping list</h2>
    <p>SAP has many product names, but the useful question is not how many products exist. It is which role each product plays in an enterprise landscape. Some products run core transactions. Others plan work before execution, connect companies, govern data, analyze processes, or provide the technology used to extend and integrate applications.</p>

    <p>SAP's public product index currently groups the portfolio into 14 categories. Those categories are useful for navigation, but they are not technical layers and they do not define one fixed architecture. A product can serve more than one business domain, and one end-to-end process can cross several products.</p>

    <table>
      <thead>
        <tr><th>Portfolio category</th><th>What it represents in practice</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Business AI</strong></td><td>Joule, assistants, agents, and AI services that work across business applications rather than forming a separate ERP.</td></tr>
        <tr><td><strong>Business applications</strong></td><td>The modular application portfolio spanning finance, supply chain, procurement, HR, and customer experience.</td></tr>
        <tr><td><strong>Business data cloud</strong></td><td>Governed business data, analytics, planning, data engineering, and data products across SAP and third-party sources.</td></tr>
        <tr><td><strong>Business network</strong></td><td>Cross-company collaboration with suppliers, logistics partners, and other trading partners.</td></tr>
        <tr><td><strong>Business process transformation</strong></td><td>SAP Signavio capabilities for process modeling, analysis, mining, and transformation.</td></tr>
        <tr><td><strong>Business technology platform</strong></td><td>Integration, application development, automation, extension, and platform services.</td></tr>
        <tr><td><strong>Cloud ERP</strong></td><td>Core cloud ERP applications and the operating model around SAP Cloud ERP.</td></tr>
        <tr><td><strong>CRM and customer experience</strong></td><td>Commerce, sales, service, marketing, and customer engagement applications.</td></tr>
        <tr><td><strong>Financial management</strong></td><td>Core finance plus treasury, consolidation, compliance, and related financial capabilities.</td></tr>
        <tr><td><strong>Human capital management</strong></td><td>SAP SuccessFactors and related applications for core HR and talent processes.</td></tr>
        <tr><td><strong>Small and midsize enterprise</strong></td><td>ERP and business-management options aimed at smaller and growing organizations.</td></tr>
        <tr><td><strong>Spend management</strong></td><td>SAP Ariba, SAP Fieldglass, and SAP Concur families for procurement, external workforce, travel, and expense.</td></tr>
        <tr><td><strong>Supply chain management</strong></td><td>Planning, manufacturing, warehouse, transportation, asset, and logistics applications.</td></tr>
        <tr><td><strong>Sustainability management</strong></td><td>Applications for emissions, footprint, ESG, environmental, health, and safety processes.</td></tr>
      </tbody>
    </table>

    <h2>SAP Business Suite is the umbrella, not one replacement application</h2>
    <p>SAP currently describes <strong>SAP Business Suite</strong> as the combination of business applications, SAP Business Data Cloud, and SAP Business AI, powered by SAP Business Technology Platform. That is an architectural and portfolio umbrella. It should not be read as one monolithic application that replaces S/4HANA, SuccessFactors, Ariba, or the other products underneath it.</p>

    <p>This distinction matters in architecture discussions. A company can say it is adopting SAP Business Suite while still making separate design decisions about ERP deployment, HR ownership, procurement, planning, integration, data, and AI. The suite story connects those decisions; it does not erase their boundaries.</p>

    <h2>Cloud ERP naming needs careful reading</h2>
    <p><strong>SAP Cloud ERP</strong> is now the main public cloud ERP label, with SAP S/4HANA Cloud Public Edition described as a foundational application. <strong>SAP Cloud ERP Private</strong> is the private-cloud option for organizations that need greater continuity with complex existing ERP processes and extensions.</p>

    <p><strong>SAP GROW</strong> and <strong>RISE with SAP</strong> are better understood as adoption and transformation offerings around cloud ERP, not as separate ERP engines. SAP states that GROW is an entry point to cloud ERP built on SAP S/4HANA Cloud Public Edition. RISE with SAP can have SAP Cloud ERP or SAP Cloud ERP Private at its core. Treating GROW, RISE, Public Edition, and Private Edition as four equivalent products obscures the real deployment choice.</p>

    <p><a href="/atlas/sap/sap-business-one/">SAP Business One</a> remains a separate ERP product for small businesses with its own architecture, data model, APIs, and lifecycle. It should not be described as a reduced S/4HANA edition.</p>

    <h2>Line-of-business applications usually own a specific part of the process</h2>
    <p>The rest of the application portfolio becomes easier to understand when we ask what each product is authoritative for.</p>

    <table>
      <thead>
        <tr><th>Product family</th><th>Primary role</th><th>Boundary to remember</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>SAP SuccessFactors</strong></td><td>Core HR, talent, learning, recruiting, compensation, and related workforce processes.</td><td>Employee Central can be the HR system of record, but authority still depends on the customer's HR and payroll architecture.</td></tr>
        <tr><td><strong>SAP Ariba</strong></td><td>Sourcing, supplier management, contracts, buying, and invoicing.</td><td>The Ariba application process and the external supplier-network conversation are related but not the same boundary.</td></tr>
        <tr><td><strong>SAP Fieldglass</strong></td><td>Contingent workforce and services procurement.</td><td>Contingent labor, statement-of-work services, and worker profiles use different business objects and controls.</td></tr>
        <tr><td><strong>SAP Concur</strong></td><td>Travel, expense, and invoice processes.</td><td>An approved expense or invoice still needs the appropriate ERP/accounting integration to become a financial posting.</td></tr>
        <tr><td><strong>SAP Commerce Cloud</strong></td><td>Digital commerce for B2B and B2C scenarios.</td><td>Catalog, pricing, stock, order capture, and fulfillment ownership are architecture choices; Commerce is not automatically the system of record for all of them.</td></tr>
        <tr><td><strong>SAP Sales Cloud and SAP Service Cloud</strong></td><td>Sales and customer-service processes.</td><td>CRM activity can coexist with ERP-owned orders, billing, logistics, and accounting.</td></tr>
      </tbody>
    </table>

    <h2>Supply-chain products separate planning from physical execution</h2>
    <p>The supply-chain portfolio is not one linear stack. <a href="/atlas/sap/sap-ibp/">SAP Integrated Business Planning</a> plans demand, supply, inventory, and response scenarios. <a href="/atlas/sap/sap-ewm/">SAP Extended Warehouse Management</a> controls warehouse execution. <a href="/atlas/sap/sap-tm/">SAP Transportation Management</a> plans and executes transportation. SAP Digital Manufacturing connects production execution with the wider manufacturing landscape.</p>

    <p>The key boundary is planning versus execution. A plan in IBP is not yet a production, warehouse, or transportation transaction. Likewise, a warehouse task or freight order belongs to an execution model with its own statuses and operational evidence. Integration between products should therefore be read object by object, not as a generic statement that “the supply chain is integrated.”</p>

    <h2>Business Data Cloud changes the way the data portfolio is presented</h2>
    <p>SAP Business Data Cloud is now a top-level part of the portfolio. SAP describes it as a managed data and analytics solution that brings together capabilities including SAP Datasphere, SAP Analytics Cloud, SAP HANA Cloud, SAP Master Data Governance, SAP BW, SAP Databricks, and governed SAP data products.</p>

    <p>This does not make those products interchangeable. <a href="/atlas/sap/sap-datasphere/">Datasphere</a> focuses on data modeling and integration with business semantics; <a href="/atlas/sap/sap-analytics-cloud/">Analytics Cloud</a> provides analytics and planning experiences; HANA Cloud is a database platform; MDG governs master data. Business Data Cloud provides the broader data foundation in which these capabilities are increasingly presented together.</p>

    <h2>BTP is the extension and integration foundation</h2>
    <p><a href="/atlas/sap/sap-btp/">SAP Business Technology Platform</a> sits underneath many cross-product designs. <a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a> handles integration capabilities, while <a href="/atlas/sap/sap-build/">SAP Build</a> covers application development, automation, and digital-workspace capabilities across low-code, pro-code, and AI-assisted development.</p>

    <p>The useful distinction is between extending a business application and changing its core. BTP services can host side-by-side logic, integrations, applications, and automation without pretending that all business data and transactional authority move out of the source system. The exact boundary still depends on the chosen API, event, identity model, and persistence design.</p>

    <h2>Business Network begins where one company's system ends</h2>
    <p><a href="/atlas/sap/sap-business-network/">SAP Business Network</a> provides collaboration across company boundaries. Current SAP documentation distinguishes solutions for procurement, supply-chain collaboration, logistics, trading partners, and asset collaboration. The buyer's ERP, the supplier's ERP, and the network remain separate systems even when documents flow between them.</p>

    <p>That separation is essential during support. A purchase order can be correct in ERP, transformed successfully by an integration layer, accepted by the network, and still fail a supplier-side business rule. “It is in Business Network” is therefore not the same as “the partner completed the process.”</p>

    <h2>Signavio describes and measures the process; it does not execute the ERP transaction</h2>
    <p><a href="/atlas/sap/sap-signavio/">SAP Signavio</a> covers process modeling, collaboration, mining, analysis, and transformation. Its job is to help teams understand how processes are designed and how they actually run. The execution itself still happens in the relevant business applications.</p>

    <p>This boundary also keeps the portfolio map honest. A process-mining result may reveal that invoice approval is slow, but the actual control change might belong in S/4HANA, Ariba, a workflow product, or another application. Signavio helps locate and understand the problem; it does not automatically become the system that owns the business transaction.</p>

    <h2>Business AI is increasingly cross-cutting</h2>
    <p>SAP's current AI portfolio centers on Joule, Joule Assistants, and Joule Agents. SAP describes agents as able to perform multi-step tasks using business context and tools across applications, while assistants coordinate work around a user's role and intent. Joule Work provides an engagement layer for interacting with these capabilities.</p>

    <p>For architecture, the important point is that AI does not replace the underlying authorization, data, and transaction models. An agent may call tools across systems, but the source applications still determine which objects exist, which data is authoritative, and which actions are permitted. The AI layer is therefore strongest when its scope is grounded in explicit business contracts rather than broad access to everything.</p>

    <h2>A simple way to place a product in an architecture</h2>
    <p>When a product name appears in a design, four questions usually clarify its role:</p>
    <ol>
      <li><strong>Which business object does it own?</strong> For example, an employee record, a purchase order, a warehouse task, or a planning key figure.</li>
      <li><strong>Is it planning, executing, collaborating, analyzing, or integrating?</strong> Products that touch the same process can still have very different responsibilities.</li>
      <li><strong>What crosses the system boundary?</strong> Identify the API, event, message, replicated master data, or user action rather than saying only that two products are “integrated.”</li>
      <li><strong>Where is the final business outcome proven?</strong> A successful message, workflow approval, or AI action is not automatically evidence that the target transaction posted correctly.</li>
    </ol>

    <p>This view is more durable than memorizing a catalog. Product names and packaging change; ownership, business objects, and system boundaries are what make the landscape understandable.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP — <a href="https://www.sap.com/products.html">SAP Products</a> (portfolio categories and featured products, accessed 2026-09-23).</li>
      <li>SAP — <a href="https://www.sap.com/products/business-suite.html">SAP Business Suite</a>.</li>
      <li>SAP — <a href="https://www.sap.com/products/erp/s4hana-erp.html">SAP Cloud ERP / SAP S/4HANA Cloud Public Edition</a>.</li>
      <li>SAP — <a href="https://www.sap.com/products/erp/s4hana-private-edition.html">SAP Cloud ERP Private</a>.</li>
      <li>SAP — <a href="https://www.sap.com/products/erp/grow.html">SAP GROW</a>.</li>
      <li>SAP — <a href="https://www.sap.com/products/data-cloud/what-is-sap-business-data-cloud.html">What is SAP Business Data Cloud?</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/business-network">SAP Business Network</a>.</li>
      <li>SAP — <a href="https://www.sap.com/products/artificial-intelligence.html">Joule and SAP Business AI</a>.</li>
      <li>SAP — <a href="https://www.sap.com/products/business-transformation-management/process-mining.html">SAP Signavio process mining</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a landscape map, not a licensing catalog. SAP changes product names, packaging, commercial offers, and feature availability over time. Verify the exact product edition, release, region, license, and supported integration before using this page for a purchasing or implementation decision.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-product-landscape-map/">SAP Product Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
