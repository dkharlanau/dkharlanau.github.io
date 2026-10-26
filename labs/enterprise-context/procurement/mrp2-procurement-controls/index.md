---
layout: default
title: "SAP MRP 2 — Procurement Types, Special Procurement and Storage Locations"
description: "Explain SAP MRP 2 procurement type E/F/X, special procurement keys, production storage location, proposed supply area and storage location for external procurement through business flows and diagnostics."
permalink: /labs/enterprise-context/procurement/mrp2-procurement-controls/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-10-15
hide_global_cta: true
tags:
  - sap-s4hana
  - sap-mm
  - sap-pp
  - mrp
  - material-master
  - special-procurement
  - production-supply-area
  - procurement
  - assessment
career_impact: mapped
career_skills:
  - logistics-p2p
  - logistics-master-data
  - logistics-production-quality
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">SAP Enterprise</a></li><li><a href="/labs/enterprise-context/procurement/">Procurement</a></li><li aria-current="page">MRP 2 Procurement Controls</li></ol>
</nav>

<div class="research-canvas context-graph">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Material master / MRP 2 / MM + PP</p>
      <h1>How do we get the material?<br />Where will it go?</h1>
      <p>Five fields on the MRP 2 view answer different questions. Procurement Type chooses the broad supply route. Special Procurement changes the route for a specific scenario. Three location fields propose where material is received, issued, or staged. Understanding the difference helps us explain wrong MRP proposals and warehouse problems.</p>
      <a class="research-canvas__button" href="#five-fields">Compare the five fields <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">school</span>
    <div>
      <p><strong>After this page:</strong> explain E, F, and X; read the five special procurement examples from an MRP 2 value list; separate a storage location from a production supply area; trace the proposal into the right purchasing or production document; and choose the first useful check when the result is wrong.</p>
      <p><strong>Scope:</strong> classic material master / MRP 2 terminology, with SAP S/4HANA planning and production references. Key numbers and document defaults depend on plant configuration, MRP area, process and release. This working study page remains draft / noindex pending human publication review.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="mental-model" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Mental model</p>
      <h2>One shortage. Three separate decisions.</h2>
      <p>Think about a missing component on an assembly line. MRP does not only calculate the missing quantity. It also needs a supply method and a meaningful location.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>1. How is supply created?</h3><p><strong>Procurement Type:</strong> make it, buy it, or allow both. This influences the kind of planning proposal.</p></div>
      <div><h3>2. Is there a special supply route?</h3><p><strong>Special Procurement:</strong> consignment, subcontracting, stock transfer, phantom assembly, or another configured route.</p></div>
      <div><h3>3. Where is the material needed?</h3><p><strong>Location controls:</strong> proposed production receipt or issue storage location, external receiving storage location, and shop-floor supply area.</p></div>
    </div>
    <p><strong>Important:</strong> a storage location is an inventory-management level. A production supply area (PSA) identifies a point at the shop floor. A PSA can be assigned to a storage location, but it is not a separate stock-quantity level in MM-IM.</p>
  </section>

  <section class="research-canvas__inventory" id="five-fields" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Quick comparison</p>
      <h2>Read the field by the decision it controls.</h2>
    </header>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Five MRP 2 fields and their roles">
      <table class="study-table__table">
        <thead><tr><th scope="col">Field</th><th scope="col">Question</th><th scope="col">Main role</th><th scope="col">Look for the result in</th></tr></thead>
        <tbody>
          <tr><th scope="row">Procurement Type</th><td>Make or buy?</td><td>Broad allowed procurement method.</td><td>MRP proposal: planned order, purchase requisition or schedule line, depending on the process.</td></tr>
          <tr><th scope="row">Special Procurement</th><td>Any exception to normal supply?</td><td>Plant-defined replenishment route.</td><td>Specially created requirement, proposal, BOM explosion or follow-on procurement document.</td></tr>
          <tr><th scope="row">Production Storage Location</th><td>Where should production receive or issue material?</td><td>Default used in production planning and execution.</td><td>Planned/production order receipt location or component issue location.</td></tr>
          <tr><th scope="row">Proposed Supply Area</th><td>At which line-side point is this component supplied?</td><td>Shop-floor staging context, especially Kanban and dependent requirements.</td><td>Dependent requirements, pull list, control cycle or production staging process.</td></tr>
          <tr><th scope="row">Storage Location for External Procurement</th><td>Where should externally sourced material be received?</td><td>Default receiving location for an MRP-created procurement proposal.</td><td>Purchase requisition or external planned order, then downstream purchasing and receipt documents.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="procurement-type" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Field 01 / Procurement Type</p>
      <h2>E, F and X decide the broad supply route.</h2>
      <p>MRP first calculates the shortage and procurement quantity. Procurement Type helps it choose how that quantity will be supplied. The field is maintained for a material and plant, subject to material-type and planning settings.</p>
    </header>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Procurement Type values">
      <table class="study-table__table">
        <thead><tr><th scope="col">Value</th><th scope="col">Meaning</th><th scope="col">Typical planning result</th><th scope="col">Assessment point</th></tr></thead>
        <tbody>
          <tr><th scope="row">E</th><td>In-house production.</td><td>Planned order, later converted to a production order if required.</td><td>We expect to manufacture or assemble the material.</td></tr>
          <tr><th scope="row">F</th><td>External procurement.</td><td>Purchase requisition or scheduling-agreement schedule line; classic MRP settings can also create an external planned order.</td><td>The buying process must take supply forward.</td></tr>
          <tr><th scope="row">X</th><td>Both procurement methods allowed.</td><td>Standard MRP starts with in-house production unless sourcing logic such as a quota arrangement makes another choice.</td><td>X does not automatically mean a 50/50 split.</td></tr>
          <tr><th scope="row">Blank</th><td>No procurement.</td><td>No normal replenishment proposal based on a make-or-buy decision.</td><td>Check why replenishment is intentionally disabled.</td></tr>
        </tbody>
      </table>
    </div>
    <div class="ecg-decision-columns">
      <div><h3>In-house example</h3><p>Demand for 100 finished units → MRP shortage → planned order → production order → confirmation and goods receipt. Master data such as a valid production version affects the execution route.</p></div>
      <div><h3>External example</h3><p>Demand for 100 purchased parts → MRP shortage → purchase requisition or scheduling agreement schedule line → supplier delivery → goods receipt.</p></div>
    </div>
    <p><strong>Lead boundary:</strong> Procurement Type is not the same as source determination. F does not choose the supplier; sourcing data, agreements, source lists, quota arrangements and related planning settings do that. Also, do not infer an MRP proposal from the field alone: check the MRP run, requirement, lot size, dates and any special procurement setting.</p>
  </section>

  <section class="research-canvas__inventory" id="special-procurement" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Field 02 / Special Procurement</p>
      <h2>The key changes how a material is supplied, not what the material is.</h2>
      <p>Special procurement types are configured for a plant. The numbers below match one common value-list pattern, but the maintained key definition is the authority. In classic configuration, check <strong>Define Special Procurement Type</strong> (transaction <code>OMD9</code> where available). A key can contain a procurement method, special procurement indicator, supplying plant, issuing location and BOM-component control settings.</p>
    </header>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Special procurement keys from a sample plant">
      <table class="study-table__table">
        <thead><tr><th scope="col">Example key</th><th scope="col">Process</th><th scope="col">What changes</th><th scope="col">Do not confuse with</th></tr></thead>
        <tbody>
          <tr><th scope="row">10</th><td>Consignment</td><td>Supplier-owned stock can be kept at our site; settlement is linked to withdrawal or consumption, not an ordinary purchased-stock receipt.</td><td>Customer consignment in Sales, which has a different stock owner and document flow.</td></tr>
          <tr><th scope="row">20</th><td>External procurement</td><td>An external-procurement route is defined by the key. This can be useful when normal material settings would otherwise lead toward in-house production.</td><td>An actual supplier selection. The key is not a purchasing info record.</td></tr>
          <tr><th scope="row">30</th><td>Subcontracting</td><td>We buy a processed material from a supplier and may provide components for that supplier to consume.</td><td>A standard PO with no component-provision process.</td></tr>
          <tr><th scope="row">45</th><td>Stock transfer from plant to MRP area</td><td>Material for one separately planned MRP area is replenished from another, for example from the plant MRP area.</td><td>Interplant stock transport orders. This sample key describes an MRP-area planning route.</td></tr>
          <tr><th scope="row">50</th><td>Phantom assembly</td><td>The phantom groups BOM components, but normally does not have its own planned order and goods receipt. Requirements pass to its lower-level components.</td><td>A physically stocked semi-finished assembly.</td></tr>
        </tbody>
      </table>
    </div>
    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">warning</span>
      <p><strong>Do not memorize the number without its definition.</strong> The same numerical key can be configured for a different scenario in another plant or system. Keys such as 40 for interplant stock transfer, 52 for direct production, or 80 for production in another plant may also exist, but they are not part of this example value list.</p>
    </div>
    <div class="ecg-determination-list">
      <article class="ecg-determination-detail">
        <header><div><span>10</span><small>Vendor stock</small></div><h3>Consignment</h3><p class="ecg-question">The supplier owns it until we use it.</p></header>
        <p>A supplier may deliver material to our premises while retaining ownership. The physical stock is at our location, but SAP manages it as consignment stock. The receipt, withdrawal and settlement rules differ from ordinary purchased inventory. In a common classic process, consignment withdrawals can be settled through consignment settlement rather than a standard invoice for the original receipt.</p>
        <p><strong>Trace:</strong> replenishment need → consignment supply arrangement → goods receipt into vendor consignment stock → withdrawal or consumption → settlement of consumed quantity.</p>
      </article>
      <article class="ecg-determination-detail">
        <header><div><span>20</span><small>Supply route</small></div><h3>External procurement</h3><p class="ecg-question">Treat this supply as bought, not made.</p></header>
        <p>An external procurement special key can direct the planning route toward external supply, subject to its actual configuration. This matters when a material can be made in-house but a particular planning setup requires buying it. If the general Procurement Type and the special key appear to disagree, inspect the key definition and the resulting MRP proposal before changing master data.</p>
        <p><strong>Trace:</strong> shortage → effective procurement route → external proposal → source determination → purchasing document.</p>
      </article>
      <article class="ecg-determination-detail">
        <header><div><span>30</span><small>Supplier work</small></div><h3>Subcontracting</h3><p class="ecg-question">We pay the supplier for processing and provide the required components.</p></header>
        <p>For planning-driven subcontracting, a common setup uses Procurement Type F with Special Procurement 30. Purchasing creates a subcontracting PO (often item category <code>L</code>). A BOM or other supported component determination provides the list of material to send to the supplier. In a common classic stock process, movement <code>541</code> provides components to the vendor; goods receipt <code>101</code> for the subcontracted item is linked to consumption <code>543</code> of provided components. Verify stock and movement design in the target system.</p>
        <p><strong>Trace:</strong> MRP demand → subcontracting PR → subcontracting PO + components → provision to vendor → processed goods receipt + component consumption → invoice verification.</p>
      </article>
      <article class="ecg-determination-detail">
        <header><div><span>45</span><small>Planning area</small></div><h3>Stock transfer to an MRP area</h3><p class="ecg-question">The need is in a separately planned area, but supply exists elsewhere.</p></header>
        <p>A storage-location MRP area can be replenished from the plant MRP area or another configured source MRP area. Depending on the setup, planning creates a stock transfer reservation or a stock transport requisition. A receiving storage location matters because it places the receipt in the target planning area. This is not the same as buying from a supplier or automatically moving stock just because a material master field was changed.</p>
        <p><strong>Trace:</strong> requirement in target MRP area → source-area transfer proposal → physical transfer/posting → stock in target location.</p>
      </article>
      <article class="ecg-determination-detail">
        <header><div><span>50</span><small>BOM logic</small></div><h3>Phantom assembly</h3><p class="ecg-question">Keep the engineering group, but plan the real components.</p></header>
        <p>Imagine a cable set in a finished product BOM. Engineering wants a named group for the cable, plug and clips, but production does not manufacture or stock the set as a separate assembly. The phantom stays in the BOM structure; planning passes requirements to the lower-level components instead of creating a separate normal procurement proposal for the phantom header.</p>
        <p><strong>Trace:</strong> finished-product demand → BOM explosion → phantom skipped as a stocked supply object → component requirements at the next level.</p>
      </article>
    </div>
    <p><strong>Costing nuance:</strong> the material's Costing view can contain a separate special procurement key. In product cost planning, that Costing key can take priority over the MRP key. Therefore, correct MRP behavior does not guarantee that the cost estimate uses the same quantity structure.</p>
  </section>

  <section class="research-canvas__inventory" id="production-storage-location" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Field 03 / Production Storage Location</p>
      <h2>One field supports two different production roles.</h2>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Produced material: where it is received</h3><p>For a finished or semi-finished material being produced, the field can propose the receiving storage location on a planning or production document. A valid production version or other process-specific setting can provide a more specific location.</p></div>
      <div><h3>Component: where it is issued</h3><p>For a component consumed by production, the same field can help propose the issuing storage location. However, order-level entries, a work center's supply area, BOM item data and determination strategy may take priority.</p></div>
    </div>
    <p><strong>Example:</strong> we produce a control panel. Finished panels should arrive at storage location <code>FIN1</code>; bolts consumed by the order are picked from <code>COMP</code>. Both materials can have a Production Storage Location, but the field serves a different role depending on whether that material is the produced header or an issued component.</p>
    <p><strong>Diagnostic:</strong> if the production order proposes the wrong storage location, check whether we are looking at the <em>receipt</em> or <em>issue</em> side. For components, inspect the actual component assignment, work center and PSA, BOM item, and material master in the relevant determination sequence. Never assume the material-master default must win.</p>
  </section>

  <section class="research-canvas__inventory" id="proposed-supply-area" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Field 04 / Proposed Supply Area</p>
      <h2>A supply area is where the line needs material, not another inventory ledger.</h2>
    </header>
    <p>A production supply area (PSA) represents a shop-floor supply point, for example <code>LINE-A</code> or <code>PACK-02</code>. Material can be staged there for a work center or assembly line. The proposed supply area in the material master is particularly useful for Kanban materials and can help determine the supply area on dependent requirements or pull-list selections.</p>
    <div class="ecg-decision-columns">
      <div><h3>Storage location</h3><p>Inventory quantity and material movements are recorded for the storage location, stock type and other relevant stock dimensions.</p></div>
      <div><h3>Production supply area</h3><p>The operational point at which material is expected on the shop floor. It is linked to a storage location for inventory postings and can participate in staging logic.</p></div>
    </div>
    <p><strong>Example:</strong> a warehouse supplies 500 bolts to <code>LINE-A</code>. The PSA tells the shop floor and staging process where the bolts are needed. The underlying stock is still managed at the relevant storage location, not as an independent MM-IM PSA balance.</p>
    <p><strong>Diagnostic:</strong> a missing or wrong PSA can make Kanban control cycles, pull lists or production staging use an unexpected supply point. Check PSA definition, its storage-location assignment, BOM or work-center settings, dependent requirements, and the active staging process. Entering a PSA in MRP 2 does not itself perform a stock transfer.</p>
  </section>

  <section class="research-canvas__inventory" id="external-storage-location" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Field 05 / Storage Location for External Procurement</p>
      <h2>This is a receiving proposal for bought material.</h2>
    </header>
    <p>When MRP plans an externally procured material, this field can propose the receiving storage location in the purchase requisition or external planned order. That proposal may then move into purchasing and goods receipt. It is not the supplier, purchasing organization, or shipping address.</p>
    <p><strong>Example:</strong> a purchased motor is normally received into <code>RECV</code> before warehouse putaway. The material's external procurement storage location is set to <code>RECV</code>. MRP can propose this location on the PR, and Purchasing or Receiving can check it in the follow-on document.</p>
    <p><strong>Diagnostic:</strong> if the PR has no storage location, compare the material and plant, the relevant MRP area segment, the material's default, the created planning element and the PR itself. MRP-area-specific settings can override plant settings. SAP also documents cases where a location maintained in the material master does not appear in an MRP-created PR; diagnose that exception rather than treating the field as an unconditional copy rule.</p>
    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">compare_arrows</span>
      <p><strong>Quick distinction:</strong> Production Storage Location supports a production receipt or component issue. Storage Location for External Procurement supports an externally procured receipt. Proposed Supply Area identifies a point at the line. They are connected, but none is an automatic substitute for the others.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="business-case" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Synthetic end-to-end case</p>
      <h2>Follow one assembly and one purchased component.</h2>
      <p>Assume plant <code>PL10</code> builds control panels. The final panel is produced in-house; a motor is purchased; assembly takes place at <code>LINE-A</code>.</p>
    </header>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Example material settings">
      <table class="study-table__table">
        <thead><tr><th scope="col">Material</th><th scope="col">Procurement</th><th scope="col">Special</th><th scope="col">Production storage location</th><th scope="col">Supply area</th><th scope="col">External location</th></tr></thead>
        <tbody>
          <tr><th scope="row">Finished panel</th><td>E</td><td>Blank</td><td>FIN1</td><td>Not needed for this example</td><td>Blank</td></tr>
          <tr><th scope="row">Motor component</th><td>F</td><td>Blank</td><td>COMP</td><td>LINE-A</td><td>RECV</td></tr>
        </tbody>
      </table>
    </div>
    <div class="ecg-decision-columns">
      <div><h3>Planning</h3><p>A sales or forecast requirement creates demand for panels. MRP proposes in-house supply for the panels and an external supply proposal for any missing motors.</p></div>
      <div><h3>Purchasing and receiving</h3><p>The motor PR can propose <code>RECV</code>. A PO and supplier goods receipt follow. If motors must move from <code>RECV</code> to <code>COMP</code>, that requires the appropriate physical and inventory process.</p></div>
      <div><h3>Staging and production</h3><p>Motors are staged for <code>LINE-A</code> and issued from the determined component location. The finished panel is received at its determined receiving storage location, for example <code>FIN1</code>.</p></div>
    </div>
    <p><strong>What changes with Special Procurement 30?</strong> The motor is no longer a simple purchased component in this example if it becomes a subcontracted result. We need a subcontracting PO, supplier-provided-component logic, and consumption evidence. A storage-location field does not create that process; the special procurement and purchasing document control it.</p>
  </section>

  <section class="research-canvas__inventory" id="diagnose" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead diagnostic</p>
      <h2>Start from the first wrong document, not from the last error.</h2>
    </header>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="MRP 2 field troubleshooting">
      <table class="study-table__table">
        <thead><tr><th scope="col">Symptom</th><th scope="col">Competing causes</th><th scope="col">Evidence to collect first</th></tr></thead>
        <tbody>
          <tr><th scope="row">MRP plans production but the buyer expected a PR.</th><td>Procurement Type E/X; missing quota; special key not as expected.</td><td>MRP result, effective procurement type, special-key definition, quota and source evidence.</td></tr>
          <tr><th scope="row">Subcontracting PR is not created.</th><td>Special key missing; sourcing setup incomplete; material/plant or planning mode differs.</td><td>MRP 2 settings, OMD9 definition, PR or planned order, component structure, assigned source.</td></tr>
          <tr><th scope="row">Phantom receives a planned order.</th><td>Special procurement not effective; BOM usage/explosion context differs; material planned independently.</td><td>BOM item, explosion result, special key and exact requirement that produced the proposal.</td></tr>
          <tr><th scope="row">Production issues from the wrong location.</th><td>BOM item, PSA/work center, production version, manual order change, or material default.</td><td>Order component data, PSA assignment, BOM item, determination strategy and material master.</td></tr>
          <tr><th scope="row">MRP PR has no receiving location.</th><td>MRP area, missing or overridden default, process-specific behavior.</td><td>Material/plant and MRP area segment, created PR, relevant SAP KBA and system configuration.</td></tr>
          <tr><th scope="row">Stock is at the plant but not at the line.</th><td>Staging incomplete, wrong PSA, wrong storage location or stock state.</td><td>MM inventory by storage location, warehouse staging task/delivery, PSA and production component need.</td></tr>
        </tbody>
      </table>
    </div>
    <p><strong>Proof after a correction:</strong> repeat the planning or document-determination step in a controlled test, compare the proposed object and its storage location, and verify the downstream goods movement or staging state. Changing master data after documents already exist does not guarantee that old documents will automatically inherit the new values.</p>
  </section>

  <section class="research-canvas__inventory" id="assessment-answer" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Assessment practice</p>
      <h2>Explain the distinction in under one minute.</h2>
    </header>
    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">record_voice_over</span>
      <p><strong>Spoken answer:</strong> “In MRP 2, Procurement Type controls whether a material is made or bought. Special Procurement defines a particular route, such as subcontracting, consignment, a stock transfer, or a phantom assembly. Production Storage Location can propose the receiving location for a finished product or the issue location for a component. The external procurement location proposes where purchased goods are received. Proposed Supply Area identifies the point where components are needed on the shop floor. I would check the resulting MRP proposal and production or purchasing document before changing a default.”</p>
    </div>
    <div class="ecg-decision-columns">
      <div><h3>Why can X create a planned order?</h3><p>Both supply routes are allowed, but standard planning starts with in-house production unless further sourcing rules change the decision.</p></div>
      <div><h3>Can a PSA hold separate MM stock?</h3><p>No. It is a shop-floor supply point. Inventory is still recorded at the associated storage location and other stock dimensions.</p></div>
      <div><h3>Does Special Procurement 30 create a subcontracting PO by itself?</h3><p>No. It guides planning. The actual PR, PO item category, components and supplier process must also be correct.</p></div>
      <div><h3>Why are two storage location fields needed?</h3><p>In-house production and external procurement are different receipt/issue contexts, so separate defaults make sense.</p></div>
      <div><h3>Why does a production order ignore the location from MRP 2?</h3><p>Because another valid source such as a production version, PSA/work center, BOM item or manual order entry may have higher priority.</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="technical-check" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Technical reference / optional</p>
      <h2>Use field names only when they help you verify a real case.</h2>
    </header>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="MRP 2 technical field mapping">
      <table class="study-table__table">
        <thead><tr><th scope="col">Business field</th><th scope="col">Plant-level field</th><th scope="col">Useful check</th></tr></thead>
        <tbody>
          <tr><th scope="row">Procurement Type</th><td><code>MARC-BESKZ</code></td><td>Material/plant; actual MRP planning proposal.</td></tr>
          <tr><th scope="row">Special Procurement</th><td><code>MARC-SOBSL</code></td><td>Plant-specific key definition in Customizing; MRP result.</td></tr>
          <tr><th scope="row">Production Storage Location</th><td><code>MARC-LGPRO</code></td><td>Header receipt or component issue determination.</td></tr>
          <tr><th scope="row">Proposed Supply Area</th><td><code>MARC-VSPVB</code></td><td>Dependent requirements, Kanban/pull list, PSA assignment.</td></tr>
          <tr><th scope="row">Storage Location for External Procurement</th><td><code>MARC-LGFSB</code></td><td>External MRP proposal and PR receiving location.</td></tr>
        </tbody>
      </table>
    </div>
    <p>For materials with MRP-area-specific data, inspect the relevant MRP area segment rather than assuming the plant field wins. In classic SAP GUI systems, material master, stock/requirements list, production order, purchasing documents, BOM and special procurement Customizing can be inspected with the appropriate transactions. SAP S/4HANA Cloud Public Edition uses its supported apps and configuration environment; classic transaction availability must not be assumed there.</p>
  </section>

  <section class="research-canvas__inventory" id="sources" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Primary product sources</p>
      <h2>SAP documentation behind these rules.</h2>
      <p>The examples are synthetic and the explanation is independently written. These sources support the main planning, storage-location and staging distinctions. Validate the active release and customizing before changing a productive system.</p>
    </header>
    <div class="research-route-list">
      <a href="https://learning.sap.com/courses/exploring-production-planning-in-sap-s-4hana/understanding-mrp-in-sap-s-4hana" target="_blank" rel="noopener"><span>SAP</span><strong>Understanding MRP in SAP S/4HANA</strong><small>E/F/X and MRP sourcing decisions.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://learning.sap.com/courses/business-processes-in-sap-s-4hana-sourcing-procurement/running-materials-requirements-planning" target="_blank" rel="noopener"><span>SAP</span><strong>Running Materials Requirements Planning</strong><small>MRP 2 material data, special procurement and MRP areas.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/2e98b6535fe6b74ce10000000a174cb4.html" target="_blank" rel="noopener"><span>SAP</span><strong>Determining and Assigning Storage Locations to the MRP Area</strong><small>Receiving-location priority and MRP-area assignment.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://learning.sap.com/courses/manage-production-orders-in-sap-s-4hana-manufacturing/posting-goods-issues-for-production-orders" target="_blank" rel="noopener"><span>SAP</span><strong>Posting Goods Issues for Production Orders</strong><small>Component issue-location determination priority.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/18fe3fab96864826bfa0be0de4f65b85/6c2c3ab5b661455a8f8995309c2bb30d.html" target="_blank" rel="noopener"><span>SAP</span><strong>Product Plant Supply Planning</strong><small>Proposed supply area field meaning.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/49d0972a760b4646918ce9fddb034d64/b45fbd534f22b44ce10000000a174cb4.html" target="_blank" rel="noopener"><span>SAP</span><strong>Storage Location Assignment for Kanban</strong><small>PSA is not an inventory stock-management level.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/2bba750d1e124e1ea2a039bb1cd9b6c5/3498b6535fe6b74ce10000000a174cb4.html" target="_blank" rel="noopener"><span>SAP</span><strong>Stock Transfer Between MRP Areas</strong><small>MRP-area replenishment and transfer proposals.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE_UPA/cd100ef6721d4f9f96df2960a0601f64/0706c453f57eb44ce10000000a174cb4.html" target="_blank" rel="noopener"><span>SAP</span><strong>Special Procurement Key</strong><small>Phantom assembly and direct production.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://learning.sap.com/courses/product-cost-planning-in-sap-s-4hana/using-special-procurement-types" target="_blank" rel="noopener"><span>SAP</span><strong>Using Special Procurement Types</strong><small>Costing view priority and quantity structure.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://userapps.support.sap.com/sap/support/knowledge/en/2568137" target="_blank" rel="noopener"><span>SAP KBA</span><strong>Purchase requisitions created without storage location</strong><small>Example of release- and configuration-dependent behavior; full KBA may require login.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">route</span>
    <p><strong>Continue the process:</strong> Procurement owns purchasing documents and supplier decisions; Production owns orders and component requirements; Inventory Management owns ERP stock movements; EWM or Kanban may own physical staging.</p>
    <a href="/labs/enterprise-context/production/">Open Production Planning <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <div class="research-canvas__support" data-reveal>{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
