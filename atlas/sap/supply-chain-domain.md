---
layout: default
title: "Supply Chain — SAP S/4HANA Domain"
description: "Analytical overview of the Supply Chain domain in SAP S/4HANA: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/supply-chain-domain/
atlas_section: sap
domain: SAP operations
subdomain: Supply chain
concept_type: domain
sap_area: "MM / WM / LE / TM"
business_process: "Supply chain management"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - sap-supply-chain
  - inventory
  - warehousing
  - transportation
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/sap/manufacturing-domain/
  - /atlas/sap/sap-ewm/
  - /atlas/sap/sap-tm/
  - /atlas/sap/sap-ibp/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">Supply Chain Domain</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Domain</p>
    <h1>Supply chain — SAP S/4HANA domain</h1>
    <p class="note-subtitle">Inventory, warehousing, transportation, and supply chain planning.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Supply chain management</dd></div>
      <div><dt>SAP area</dt><dd>MM / WM / LE / TM</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until domain claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>The Supply Chain domain in S/4HANA covers inventory management, warehousing, transportation, and logistics execution. It ensures materials are available where needed, stored correctly, and moved efficiently.</p>

    <h2>Business purpose</h2>
    <p>Manage stock levels, execute warehouse operations, plan and execute transportation, and integrate logistics with production and sales. The domain is the physical fulfillment layer of the enterprise.</p>

    <h2>Where it sits in the landscape</h2>
    <p>Upstream: procurement (goods receipt), production (goods issue, receipt), sales (delivery, shipment). Downstream: customer (delivery), carrier (freight order), finance (inventory valuation). Cross-domain: quality management (inspection), plant maintenance (resource availability).</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Inventory: stock, reservations, movements, physical inventory.</li>
      <li>Warehouse: storage bin, transfer order, warehouse task, handling unit.</li>
      <li>Transportation: freight order, freight unit, shipment, route.</li>
      <li>Delivery: inbound, outbound, intercompany, stock transport.</li>
      <li>Movement types: goods receipt, goods issue, transfer posting, reversal.</li>
      <li>Batch: batch master, classification, shelf life, status.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>MM: inventory management, valuation, material documents.</li>
      <li>SD: delivery creation, picking, packing, goods issue.</li>
      <li>PP: goods issue to production order, goods receipt from production.</li>
      <li>QM: inspection lot on receipt, quality stock, usage decision.</li>
      <li>EWM: advanced warehouse management, task management, slotting.</li>
      <li>TM: transportation planning, freight costing, carrier selection.</li>
      <li>IBP: supply planning, inventory optimization.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>BAdIs in delivery processing and shipment.</li>
      <li>Custom warehouse management enhancements.</li>
      <li>RAP extensions for logistics objects.</li>
      <li>Side-by-side apps for yard management, track and trace.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Inventory accuracy: book vs. physical stock.</li>
      <li>Delivery backlog: orders not yet picked, packed, or shipped.</li>
      <li>Warehouse task queue: open tasks, task age, resource load.</li>
      <li>Transportation planning: unplanned freight units, capacity overload.</li>
      <li>Stock in transit: intercompany, cross-plant, customer consignment.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Tight integration between inventory, warehousing, and transportation.</li>
      <li>Flexible storage and movement types for complex warehouse layouts.</li>
      <li>Real-time inventory visibility with material ledger.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>WM and EWM are separate products with different data models.</li>
      <li>Transportation planning complexity increases with multi-modal and cross-border.</li>
      <li>Inventory differences are often symptoms of upstream process failures.</li>
      <li>Batch and serial number tracking adds overhead.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Delivery cannot be created — availability, route, or warehouse block.</li>
      <li>Negative stock — movement type or configuration issue.</li>
      <li>Goods issue failed — batch determination, serial number, or inspection.</li>
      <li>Warehouse task stuck — resource, bin, or handling unit issue.</li>
      <li>Freight order not planned — route, carrier, or capacity constraint.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/sap/manufacturing-domain/">Manufacturing Domain</a></li>
      <li><a href="/atlas/sap/sap-ewm/">SAP EWM</a></li>
      <li><a href="/atlas/sap/sap-tm/">SAP TM</a></li>
      <li><a href="/atlas/sap/sap-ibp/">SAP IBP</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. Supply chain module scope, object names, and transaction availability vary by S/4HANA release, edition, and industry solution.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-ewm/">SAP EWM</a></li>
      <li><a href="/atlas/sap/sap-tm/">SAP TM</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
