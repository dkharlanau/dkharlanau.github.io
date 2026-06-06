---
layout: default
title: "Manufacturing — SAP S/4HANA Domain"
description: "Analytical overview of the Manufacturing domain in SAP S/4HANA: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/manufacturing-domain/
atlas_section: sap
domain: SAP operations
subdomain: Manufacturing
concept_type: domain
sap_area: "PP"
business_process: "Production planning and execution"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - sap-pp
  - manufacturing
  - production
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/sap/supply-chain-domain/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-ibp/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">Manufacturing Domain</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Domain</p>
    <h1>Manufacturing — SAP S/4HANA domain</h1>
    <p class="note-subtitle">Production planning, execution, quality, and shop-floor integration.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Production planning and execution</dd></div>
      <div><dt>SAP area</dt><dd>PP</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until domain claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>The Manufacturing domain in S/4HANA covers production planning, execution, and control: demand management, MRP, production orders, process orders, repetitive manufacturing, and shop-floor integration. It transforms material and capacity plans into finished goods.</p>

    <h2>Business purpose</h2>
    <p>Plan what to produce, when, and with which resources. Execute production, track material consumption, confirm operations, record quality results, and settle costs to the correct cost objects.</p>

    <h2>Where it sits in the landscape</h2>
    <p>Upstream: demand from sales (make-to-order), forecast (make-to-stock), or IBP supply planning. Downstream: inventory (goods receipt), quality management (inspection), warehousing (putaway), and finance (cost settlement). Cross-domain: procurement (subcontracting), plant maintenance (resource availability).</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Material master: MRP views, BOM, routing, work center.</li>
      <li>Production order: header, operations, components, capacity requirements.</li>
      <li>Process order: for process industries, with phases and resources.</li>
      <li>Repetitive manufacturing: planning table, backflush, cost collector.</li>
      <li>BOM: material BOM, variant BOM, multiple BOM.</li>
      <li>Routing / recipe: operations, work centers, standard times.</li>
      <li>Work center: capacity, formulas, scheduling.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>SD: sales orders driving make-to-order production.</li>
      <li>MM: material availability, goods issue, goods receipt, subcontracting.</li>
      <li>QM: inspection lots, results recording, usage decisions.</li>
      <li>PM: equipment availability, maintenance orders blocking capacity.</li>
      <li>CO: cost collection, variance calculation, order settlement.</li>
      <li>IBP: supply planning and finite scheduling (advanced planning).</li>
      <li>External: MES, shop-floor data collection, IoT sensors.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>BAdIs in production order processing and confirmation.</li>
      <li>Custom MRP enhancements and user exits.</li>
      <li>RAP extensions for manufacturing objects.</li>
      <li>Side-by-side apps for shop-floor dashboards and OEE.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Production order variance: planned vs. actual costs.</li>
      <li>Capacity overload: work center load vs. available capacity.</li>
      <li>MRP exceptions: exception messages, bottleneck materials.</li>
      <li>Confirmation backlog: operations not confirmed on time.</li>
      <li>Quality hold: inspection lot blocking goods receipt.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Deep integration between planning, execution, and cost control.</li>
      <li>Flexible manufacturing modes: discrete, process, repetitive, subcontracting.</li>
      <li>Real-time inventory and cost visibility via material ledger.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>MRP performance degrades with large BOMs and complex routing.</li>
      <li>Production order settlement errors are common and hard to trace.</li>
      <li>Shop-floor integration with MES is often custom and brittle.</li>
      <li>Capacity planning is rough-cut; finite scheduling requires advanced tools.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Production order cannot be released — missing BOM, routing, or material availability.</li>
      <li>Backflush error — component not available or batch determination failure.</li>
      <li>Cost settlement failed — missing settlement rule or cost collector.</li>
      <li>MRP exception flood — master data changes triggering mass replanning.</li>
      <li>Quality inspection blocking goods receipt — usage decision pending.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/sap/supply-chain-domain/">Supply Chain Domain</a></li>
      <li><a href="/atlas/sap/sap-ibp/">SAP IBP</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. Manufacturing module scope, object names, and transaction availability vary by S/4HANA release, edition, and industry solution.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/sap/supply-chain-domain/">Supply Chain Domain</a></li>
      <li><a href="/atlas/sap/sap-ibp/">SAP IBP</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
