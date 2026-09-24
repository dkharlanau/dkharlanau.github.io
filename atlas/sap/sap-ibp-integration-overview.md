---
layout: default
title: "SAP IBP Integration Overview"
description: "How SAP Integrated Business Planning exchanges time-series and order-based planning data with SAP S/4HANA, including current integration paths and monitoring boundaries."
permalink: /atlas/sap/sap-ibp-integration-overview/
atlas_section: sap
domain: SAP operations
subdomain: Planning integration
concept_type: SAP concept
sap_area: MM / IBP / supply chain planning
business_process: Planning to procurement
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau
tags:
  - sap-mm
  - integration
  - ibp
  - planning
  - supply-chain
related:
  - /atlas/sap/sap-ibp/
  - /atlas/sap/sap-mm-procurement-overview/
  - /atlas/sap/supply-chain-domain/
  - /atlas/data-quality/sap-master-data-quality/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP IBP Integration Overview</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas SAP Note</p>
    <h1>SAP IBP integration overview</h1>
    <p class="note-subtitle">There is no single IBP-to-S/4 interface: the integration path depends on whether the planning process is time-series based or order based.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Planning to procurement</dd></div>
      <div><dt>SAP area</dt><dd>MM / IBP / supply chain planning</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>The first question in an SAP IBP integration design is not “CPI or CIF?” It is <strong>what kind of planning data are we exchanging?</strong> SAP IBP supports several integration scenarios, and the right technical path depends on the planning model, source system, direction of transfer, and objects involved.</p>

    <p>For SAP S/4HANA landscapes, the most useful distinction is between <strong>time-series-based integration</strong> for tactical planning and <strong>order-based integration</strong> for more operational planning. Mixing these models leads to misleading architecture diagrams and poor diagnostics because they move different kinds of data and use different integration mechanisms.</p>

    <h2>Time-series integration moves planning data by period and level</h2>
    <p>Time-series planning works mainly with master data and key-figure values at configured planning levels and time buckets. Typical inbound data can include products, locations, historical demand, stock or other planning inputs. Outbound integration can return supported planning results for downstream use, but it should not be described as a universal conversion of every IBP result into a purchase requisition or another S/4HANA document.</p>

    <p>For current SAP S/4HANA and SAP S/4HANA Cloud Private Edition integration, SAP documents the supply chain integration add-on together with SAP Cloud Integration for time-series-based planning areas. The integration uses Cloud Connector and SAP-delivered or reusable integration flows. SAP Cloud Integration for data services (CI-DS, historically also called CPI-DS) remains relevant for existing customers, but there is now an important licensing boundary: it is not available with SAP IBP licenses obtained after <strong>April 20, 2026</strong>. For licenses obtained after that date, SAP recommends SAP Cloud Integration, which is part of SAP Integration Suite and requires a separate license.</p>

    <h2>Order-based planning works with transactional objects</h2>
    <p>Order-based planning needs a more detailed picture. Individual sales orders, purchase orders, purchase requisitions, planned orders, production orders, deliveries, stocks, and related master data can participate in supported scenarios. Current SAP IBP real-time integration (RTI) connects SAP ECC or SAP S/4HANA with order-based planning areas and uses Core Interface (CIF) concepts for the transfer of supported objects.</p>

    <p>This is why it is inaccurate to describe CIF only as an old APO integration mechanism. In current IBP RTI, the external system can use integration models to select data for initial transfer, and CIF is part of the documented transfer and reconciliation model. SAP also documents OpenAPI/SDI-based order integration for planning areas that use the older external-master-data model. The available path therefore depends on the planning-area model as well as the business requirement.</p>

    <h2>Planning results and execution documents are not the same thing</h2>
    <p>An IBP plan describes what the business intends to supply, move, or confirm. SAP S/4HANA remains the execution system for the transactional documents that purchasing, production, sales, and logistics process. Some supported outbound scenarios can create or update executable objects, but the exact object behavior is scenario-specific.</p>

    <p>For example, SAP documents planned-order integration between IBP and the external system, and a planned order can later become a manufacturing order or purchase requisition depending on its procurement context. That is more precise than saying that “IBP sends replenishment proposals and S/4 creates POs.” We need to identify the actual planning object, the supported direction of transfer, and the conversion step before diagnosing the result.</p>

    <h2>Master data is part of the integration contract</h2>
    <p>A planning result is meaningful only if both systems agree on the objects behind it. Product, location, product-location combinations, sources of supply, resources, calendars, and other master data may be required depending on the planning scenario. Order-based RTI, for example, transfers supported master and transactional objects through explicitly configured integration models and mappings.</p>

    <p>This makes sequencing important. If transactional data reaches IBP without the master data needed to interpret it, the message may fail or the planning model may be incomplete. A support investigation should therefore verify both the business object and the master-data context rather than looking only at the last failed message.</p>

    <h2>Monitoring follows the integration path</h2>
    <p>There is no single IBP integration monitor that explains every failure. For SAP Cloud Integration flows, the message-processing and integration-flow logs are part of the technical path. For RTI, queue state and the IBP reconciliation tools matter because CIF-based transfer can leave objects missing or inconsistent between systems.</p>

    <p>SAP provides the <strong>Data Comparison and Reconciliation for RTI</strong> app and related application jobs to compare supported objects between IBP and SAP ECC or SAP S/4HANA and correct inconsistencies. That is a stronger diagnostic model than treating a successful interface run as proof that the two systems contain the same planning state.</p>

    <h2>A practical way to trace an issue</h2>
    <p>Start with the planning area and the missing or incorrect object. Is the process time-series based or order based? Which system is the source of truth for this object? Which integration technology is configured for this planning area? Then trace one concrete product, location, order, or key-figure value across that path.</p>

    <p>If a forecast value is missing, the relevant evidence may be a time-series integration job and key-figure mapping. If a purchase requisition or planned order is inconsistent in order-based planning, the useful evidence may instead be the RTI integration model, queue state, object comparison, and reconciliation result. The symptom may be “planning is wrong” in both cases, but the technical investigation is different.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/feae3cea3cc549aaa9d9de7d363a83e6/40fc8154fcd0e530e10000000a44538d.html">Data Integration Scenarios</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S_4HANA_SUPPLYCHAIN_INTEGRATION_ADDON_FOR_SAP_INTEGRATED_BUSINESS_PLANNING/0aaced2f025644a69246bd7fe0979562/88f95d75e9b540518cb9191046581799.html">Configuration for Time-Series-Based Integration</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/68fa1e86fe6f41d98421d1ce13a08a9f/1a934ddef89448f38aa78cfb71931b58.html">Initial Data Transfer for Real-Time Integration</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/68fa1e86fe6f41d98421d1ce13a08a9f/2e9c632b870543829addaffd9fc09a4f.html">Comparison and Reconciliation of Transactional Data</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Supported objects, integration technologies, planning-area models, and licensing conditions change over time. The distinctions on this page were checked against current SAP IBP and SAP S/4HANA supply-chain integration documentation in September 2026; implementation details still need to be verified for the exact IBP release, S/4HANA release, planning area, and license.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-ibp/">SAP IBP</a></li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a></li>
      <li><a href="/atlas/sap/supply-chain-domain/">Supply Chain Domain</a></li>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
