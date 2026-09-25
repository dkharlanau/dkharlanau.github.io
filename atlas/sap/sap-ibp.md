---
layout: default
title: "SAP IBP"
description: "SAP Integrated Business Planning explained: planning areas, key figures, time-series planning, order-based planning, scenarios, and the boundary with execution systems."
permalink: /atlas/sap/sap-ibp/
atlas_section: sap
domain: SAP operations
subdomain: Integrated business planning
concept_type: product
sap_area: "IBP"
business_process: "Supply chain planning"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - sap-ibp
  - planning
  - supply-chain
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/sap/supply-chain-domain/
  - /atlas/sap/manufacturing-domain/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-ibp-integration-overview/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP IBP</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP IBP</h1>
    <p class="note-subtitle">A cloud planning environment for turning demand, supply, inventory, and network data into an agreed supply-chain plan.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Supply chain planning</dd></div>
      <div><dt>SAP area</dt><dd>IBP</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>SAP Integrated Business Planning (SAP IBP) is a cloud application for supply-chain planning. It brings demand, supply, inventory, capacity, and other planning data into a common model so planners can calculate a plan, compare alternatives, and coordinate decisions before execution takes place in systems such as SAP S/4HANA.</p>

    <p>The important boundary is that IBP is not simply “MRP in the cloud.” It supports different planning horizons and different data models. Some processes work mainly with aggregated time-series data; others use order-level data for more operational supply planning. Understanding that split makes the rest of the product easier to read.</p>

    <h2>The planning area defines the planning model</h2>
    <p>A <strong>planning area</strong> is the main model container in SAP IBP. It brings together the master-data structure, time profile, planning levels, key figures, and versions used by a planning process. A key figure is a measurable planning value such as forecast demand, projected stock, or planned supply. Its planning level defines the dimensions and granularity at which the value is stored or calculated.</p>

    <p>For example, demand may be planned by product, location, customer, and month, while another calculation works at product-location-week. The model must make those relationships explicit. SAP's current I_SAPIBP2 sample planning area can combine mid- to long-term demand, supply, and inventory planning with time series and shorter-term supply planning with orders in one planning area.</p>

    <h2>Time-series planning and order-based planning answer different questions</h2>
    <p><strong>Time-series planning</strong> is useful when the main question is how quantities develop across periods and planning levels. Forecast demand, capacity, inventory targets, and supply can be calculated and compared in daily, weekly, monthly, or other configured buckets. The planner works with key figures rather than treating every purchase order or sales order as the primary planning object.</p>

    <p><strong>Order-based planning (OBP)</strong> brings individual orders and stock into the planning picture. It supports planning processes where the sequence, source, dates, and constraints of concrete demand and supply elements matter. Current SAP IBP supports OBP with flexible master data and real-time integration profiles; older external-master-data-based OBP models remain a separate compatibility path and should not be assumed to behave the same way.</p>

    <p>The two models are related but not interchangeable. A monthly consensus forecast and an individual sales order may describe demand for the same product, yet they serve different planning decisions. Good IBP design keeps the required planning horizon and level of detail visible instead of forcing every problem into one granularity.</p>

    <h2>Versions and scenarios make alternatives explicit</h2>
    <p>Planning is rarely about one immutable answer. A planning area can contain versions, and planners can create scenarios to explore alternatives. That makes it possible to compare a base plan with a proposed change without immediately replacing the operational planning state.</p>

    <p>A useful scenario might ask what happens if demand rises in one region, a supplier loses capacity, or a production constraint changes. The value is not the scenario itself but the ability to see the consequence across related demand, supply, inventory, and capacity assumptions before a decision is accepted.</p>

    <h2>Planning runs turn assumptions into a feasible or prioritized plan</h2>
    <p>Different IBP processes use different planning operators and algorithms. Demand planning can generate or adjust forecasts. Supply planning can use heuristics or optimization, depending on the configured process. Order-based planning can consider order-level supply, demand, sourcing, and constraints. Inventory planning has its own objectives and inputs.</p>

    <p>These are not one universal “optimizer.” The planning method matters because it defines what the result means. A plan produced by an unconstrained calculation answers a different question from one that respects finite capacity or prioritizes demand under shortage.</p>

    <h2>The plan still needs an execution boundary</h2>
    <p>IBP does not replace the transactional system that creates and executes sales orders, purchase orders, production orders, deliveries, or financial postings. Data moves between planning and execution according to the integration scenario. Time-series integration, order-based real-time integration, and other supported mechanisms use different data objects and different technical paths.</p>

    <p>That distinction is important in support. If a planner sees a correct result in IBP but execution does not reflect it, the problem may be the outbound integration or the rules for creating executable objects rather than the planning calculation itself. Conversely, stale or incomplete source data can make a technically successful planning run produce a poor business result.</p>

    <h2>A compact example</h2>
    <p>Suppose a business plans demand for a product family by location and month. The demand plan is translated into product-location requirements, supply planning checks available sources and constraints, and planners compare the result with inventory and service objectives. Nearer to execution, order-based planning can use individual orders and stocks for a more detailed response. SAP S/4HANA then remains responsible for the transactional documents that purchasing, manufacturing, sales, and logistics actually execute.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/c1fb60cb1e9c49d99ada277ae57e9e6c/ab3490f9a50e464d9cc4de8c95c3e682.html">Data Model for Integrated Business Planning Based on I_SAPIBP2</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/bf99e931b8d44aafb4e306ec3602cbdd/e51d2857248ddd7ae10000000a4450e5.html">Activating Planning Areas in the Planning Areas App</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/feae3cea3cc549aaa9d9de7d363a83e6/f7c2cb2745c340c890e914ff904fb3c3.html">Assigning a Planning Area to Order-Based Planning Processes</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/c1fb60cb1e9c49d99ada277ae57e9e6c/7eae0ec6b61a431d9e7a8046979b3199.html">Creating a Planning Version</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>SAP IBP capabilities, planning algorithms, sample planning areas, integration options, and supported object types evolve by release. This page explains the durable planning model and uses current SAP IBP 2608 documentation for the product-specific boundaries above.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-ibp-integration-overview/">SAP IBP Integration Overview</a></li>
      <li><a href="/atlas/sap/supply-chain-domain/">Supply Chain Domain</a></li>
      <li><a href="/atlas/sap/manufacturing-domain/">Manufacturing Domain</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
