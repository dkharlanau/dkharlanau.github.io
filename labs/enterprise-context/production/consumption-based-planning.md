---
layout: default
title: "Consumption-Based Planning & Forecasting — SAP S/4HANA MRP"
description: "Assessment-focused SAP S/4HANA guide to reorder point planning, forecasting, lot sizing, scheduling, MRP Live versus classic MRP, MRP areas, and special procurement."
permalink: /labs/enterprise-context/production/consumption-based-planning/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-10-04
hide_global_cta: true
tags:
  - sap-s4hana
  - sap-mrp
  - consumption-based-planning
  - forecasting
  - reorder-point
  - procurement
  - production-planning
  - assessment
career_impact: mapped
career_skills:
  - logistics-p2p
  - logistics-production-quality
  - logistics-master-data
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">SAP Enterprise</a></li><li><a href="/labs/enterprise-context/production/">Production</a></li><li aria-current="page">Consumption-Based Planning</li></ol>
</nav>

<div class="research-canvas context-graph">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">MRP / Consumption-Based Planning</p>
      <h1>Planning starts with a shortage.<br />A Lead explains why the shortage became this proposal.</h1>
      <p>Consumption-based planning uses material master settings, stock and receipts, historical consumption, lot-sizing rules, scheduling data, and source-of-supply logic to decide when and how much to procure. The assessment skill is to trace that decision instead of memorizing one transaction.</p>
      <a class="research-canvas__button" href="#planning-chain">Follow the planning chain <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">school</span>
    <div>
      <p><strong>After this page, you should be able to:</strong> choose the planning procedure, explain reorder point logic, trace quantity and date calculation, distinguish MRP Live from classic MRP, and diagnose whether a wrong proposal came from demand, master data, lot sizing, scheduling, or source determination.</p>
      <p><strong>Evidence boundary:</strong> this is assessment study material derived from the supplied SAP Learning content. It is intentionally <strong>draft / noindex</strong> until a separate human review confirms release-sensitive details for publication.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="planning-chain" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Mental model</p>
      <h2>Read an MRP run as a sequence of decisions.</h2>
      <p>The planning result is easier to explain when each step has one question and one output.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>1. Planning file</h3><p>Should this material be planned in this run? Planning-relevant changes mark the material for a new run unless regenerative planning is forced.</p></div>
      <div><h3>2. Net requirements</h3><p>Is available supply enough for the planning rule? Reorder point planning compares the available situation with the reorder point.</p></div>
      <div><h3>3. Lot size</h3><p>What proposal quantity should cover the shortage after lot-sizing rules, minimum or maximum lot size, and rounding are applied?</p></div>
      <div><h3>4. Scheduling</h3><p>When must purchasing or production start so the material is available on the required date?</p></div>
      <div><h3>5. Proposal type</h3><p>Should the system create a purchase requisition, schedule line, or an in-house planning proposal?</p></div>
      <div><h3>6. Source and exception</h3><p>Can the system determine a valid source of supply, and does any exception message require human action?</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="mrp-types" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Planning procedure</p>
      <h2>The MRP Type in the material master selects the planning logic.</h2>
      <p>Do not start with a transaction code. Start with the business rule used to decide when replenishment is needed.</p>
    </header>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="MRP type comparison">
      <table class="study-table__table">
        <thead><tr><th scope="col">MRP type</th><th scope="col">Meaning</th><th scope="col">Lead-level distinction</th></tr></thead>
        <tbody>
          <tr><th scope="row">VB</th><td>Manual reorder point planning.</td><td>The reorder point and safety stock are maintained manually.</td></tr>
          <tr><th scope="row">VM</th><td>Automatic reorder point planning.</td><td>The forecast run can calculate and update reorder point and safety stock.</td></tr>
          <tr><th scope="row">V1</th><td>Manual reorder point planning with external requirements.</td><td>Use when selected external requirements must influence net requirements.</td></tr>
          <tr><th scope="row">V2</th><td>Automatic reorder point planning with external requirements.</td><td>Combines automatic reorder point logic with inclusion of external requirements.</td></tr>
          <tr><th scope="row">R1</th><td>Time-phased planning.</td><td>The material is planned on dates derived from a planning calendar.</td></tr>
          <tr><th scope="row">R2</th><td>Time-phased planning with reorder point.</td><td>A reorder point shortage can trigger planning before the next regular planning date.</td></tr>
          <tr><th scope="row">VV</th><td>Classic forecast-based planning.</td><td>Compatibility-scope functionality. In 2026, treat it as legacy or exception-based and verify the applicable release and entitlement.</td></tr>
        </tbody>
      </table>
    </div>
    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">warning</span>
      <p><strong>Forecast-based planning:</strong> the supplied SAP Learning material states general compatibility use until 31 December 2025, with some circumstances extending to 31 December 2030. SAP recommends standard MRP types such as PD, P1, P2, P3, or P4 and copying forecast requirements to planned independent requirements instead of relying on VV.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="reorder-point" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Reorder point</p>
      <h2>The reorder point protects demand during replenishment lead time.</h2>
      <p>A shortage is triggered when the available planning situation falls below the reorder point.</p>
    </header>
    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">calculate</span>
      <p><strong>Reorder point = safety stock + expected daily demand × replenishment lead time.</strong></p>
    </div>
    <div class="ecg-decision-columns">
      <div><h3>Expected demand</h3><p>Use previous consumption or future demand assumptions to estimate what will be consumed while replenishment is in progress.</p></div>
      <div><h3>Lead time</h3><p>For external procurement, the replenishment lead time can include purchasing processing time, planned delivery time, and goods receipt processing time.</p></div>
      <div><h3>Safety stock</h3><p>Protects against demand variation and delayed replenishment. In automatic reorder point planning, the forecast run can calculate it.</p></div>
    </div>
    <p><strong>Assessment trap:</strong> standard VB and VM reorder point procedures normally do not add sales orders, dependent requirements, reservations, and similar future requirements to net requirements because those needs are assumed to be covered by the reorder point. If the business requires selected external requirements to be included, use the corresponding procedure such as V1 or V2.</p>
  </section>

  <section class="research-canvas__inventory" id="lot-sizing" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lot sizing and rounding</p>
      <h2>The shortage quantity and the proposal quantity are not always the same.</h2>
      <p>MRP first identifies a shortage, then applies the lot-sizing procedure, quantity limits, and rounding rules.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Minimum lot size</h3><p>Prevents a procurement proposal from falling below the maintained minimum quantity.</p></div>
      <div><h3>Maximum lot size</h3><p>Limits the quantity of one procurement proposal.</p></div>
      <div><h3>Rounding value</h3><p>Rounds the calculated quantity to a multiple of a fixed value, for example a full box quantity.</p></div>
      <div><h3>Rounding profile</h3><p>Supports scaled rounding with threshold and rounding values, for example layers at smaller quantities and pallets at larger quantities.</p></div>
    </div>
    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">inventory_2</span>
      <p><strong>Example logic:</strong> if a supplier ships 5 pieces per layer and 40 pieces per pallet, a rounding profile can round smaller residual quantities to 5 and larger quantities to 40. A rounding profile can also exist in the purchasing info record, where it becomes relevant when the requisition is converted or a purchase order is created manually.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="scheduling" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">External procurement scheduling</p>
      <h2>A late proposal can be caused by time data, not by the shortage calculation.</h2>
      <p>Separate the quantity decision from the date decision.</p>
    </header>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="External procurement scheduling elements">
      <table class="study-table__table">
        <thead><tr><th scope="col">Time element</th><th scope="col">Meaning</th><th scope="col">Typical owner</th></tr></thead>
        <tbody>
          <tr><th scope="row">Purchasing processing time</th><td>Working days needed to convert a purchase requisition into a purchase order.</td><td>Plant planning parameters.</td></tr>
          <tr><th scope="row">Planned delivery time</th><td>Calendar days needed to procure the material externally.</td><td>Material master; can also exist in an info record or outline agreement.</td></tr>
          <tr><th scope="row">Goods receipt processing time</th><td>Working days between receipt and availability after unpacking, checking, or put-away activities.</td><td>Material master; can also exist in an outline agreement.</td></tr>
        </tbody>
      </table>
    </div>
    <p><strong>Source precedence:</strong> when the planning run determines a source of supply and that source carries planned delivery time or goods receipt processing time, those source-specific values take priority over the material master values for scheduling.</p>
  </section>

  <section class="research-canvas__inventory" id="proposal-source" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Proposal and source</p>
      <h2>MRP decides supply type before Purchasing executes the commitment.</h2>
      <p>For external procurement, the planning run can also determine a valid source of supply such as a contract, scheduling agreement, or purchasing info record.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>External procurement</h3><p>The result is a purchasing proposal. In MRP Live, a valid scheduling agreement leads to delivery schedule lines; other externally procured materials lead to purchase requisitions.</p></div>
      <div><h3>In-house production</h3><p>The planning result is a production planning object rather than a purchasing commitment. Continue with the Production Planning & Execution route for conversion and execution.</p></div>
      <div><h3>Special procurement</h3><p>A maintained special procurement type can make planning create proposals for scenarios such as consignment, subcontracting, or stock transfer.</p></div>
    </div>
    <p><strong>Boundary:</strong> MRP proposes supply. The purchase order or production order is a later execution commitment. A wrong PO date may come from the earlier planning proposal, while a correct planning proposal can still be changed during purchasing.</p>
  </section>

  <section class="research-canvas__inventory" id="mrp-live-classic" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">MRP Live versus classic MRP</p>
      <h2>Choose the engine by supported behavior, not only by speed.</h2>
      <p>MRP Live is optimized for SAP HANA and reduces data transfer by processing planning logic close to the database. Classic MRP remains relevant where its detailed options or unsupported scenarios are required.</p>
    </header>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="MRP Live and classic MRP comparison">
      <table class="study-table__table">
        <thead><tr><th scope="col">Area</th><th scope="col">MRP Live</th><th scope="col">Classic MRP</th></tr></thead>
        <tbody>
          <tr><th scope="row">Main execution</th><td>MD01N or Schedule MRP Runs.</td><td>Total planning and single-item planning remain available, including MD01 and MD03; background total planning can use MDBT.</td></tr>
          <tr><th scope="row">External procurement proposals</th><td>Creates delivery schedule lines when a valid scheduling agreement exists; otherwise purchase requisitions.</td><td>Creation indicators can control purchase requisitions, planned orders, and schedule lines for external procurement.</td></tr>
          <tr><th scope="row">MRP lists</th><td>Does not create MRP Lists; use the current stock/requirements view instead.</td><td>Can create MRP Lists depending on the control parameter.</td></tr>
          <tr><th scope="row">Fallback</th><td>If a material cannot be planned with MRP Live, the run can hand it to classic MRP.</td><td>Used for scenarios not supported by MRP Live.</td></tr>
          <tr><th scope="row">Known source limitations</th><td>The supplied study material names some optimum lot-sizing procedures and classic forecast-based planning VV as unsupported.</td><td>Retains broader legacy planning options.</td></tr>
        </tbody>
      </table>
    </div>
    <p>Planning is sequenced by low-level code. For each level, MRP Live processes eligible materials first, and materials that cannot be processed there can be handled by classic MRP.</p>
  </section>

  <section class="research-canvas__inventory" id="classic-controls" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Classic MRP controls</p>
      <h2>Classic MRP exposes more decisions on the initial screen.</h2>
      <p>These controls explain why two planning runs can produce different results even with the same material and demand.</p>
    </header>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Classic MRP control parameters">
      <table class="study-table__table">
        <thead><tr><th scope="col">Control</th><th scope="col">What it changes</th><th scope="col">Assessment point</th></tr></thead>
        <tbody>
          <tr><th scope="row">NEUPL</th><td>Regenerative planning.</td><td>Plans all relevant materials in the planning file, regardless of prior change indicators.</td></tr>
          <tr><th scope="row">NETCH</th><td>Net change planning.</td><td>Plans materials marked as changed and is more selective than regenerative planning.</td></tr>
          <tr><th scope="row">Creation indicator</th><td>Controls external procurement proposal type.</td><td>Classic MRP can create planned orders only, purchase requisitions only, or switch by opening period.</td></tr>
          <tr><th scope="row">MRP list indicator</th><td>Controls snapshot creation.</td><td>Options include no MRP lists, always create them, or create them only for selected exception situations.</td></tr>
          <tr><th scope="row">Planning mode 1</th><td>Adjust existing planning data.</td><td>Usually sufficient for normal replanning.</td></tr>
          <tr><th scope="row">Planning mode 2</th><td>Re-explode BOM after changes.</td><td>Higher priority than mode 1 for the material.</td></tr>
          <tr><th scope="row">Planning mode 3</th><td>Delete and recreate planning data.</td><td>Highest priority of the three modes.</td></tr>
        </tbody>
      </table>
    </div>
    <p>Plant parameters can provide defaults such as purchasing processing time and schedule-line behavior. MRP groups can refine selected planning controls for groups of materials. In total planning, an assigned MRP group can override the plant-level default for those materials.</p>
  </section>

  <section class="research-canvas__inventory" id="mrp-areas" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">MRP areas</p>
      <h2>Plan the stock where the business really needs it.</h2>
      <p>The MRP area is the organizational level used for material requirements planning. It allows separate planning below the full plant when that separation is meaningful.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Plant</h3><p>If no MRP area-specific material data exists, the material is planned at plant level.</p></div>
      <div><h3>Storage location MRP area</h3><p>Maintain MRP area-specific material data when a storage-location group needs its own planning parameters. Only stock in the assigned storage locations is considered in that area's net requirements calculation.</p></div>
      <div><h3>Subcontractor MRP area</h3><p>Components provided to subcontractors can be planned at subcontractor level. If specific area parameters are absent, the system can use plant planning data.</p></div>
    </div>
    <p><strong>Lead decision:</strong> create a separate MRP area when it represents a real supply boundary such as a production line, spare-parts location, or subcontractor stock. Do not create one only to make reporting look more detailed.</p>
  </section>

  <section class="research-canvas__inventory" id="forecasting" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Forecasting</p>
      <h2>Forecasting turns historical consumption into planning parameters or future demand.</h2>
      <p>The source material describes four forecast model families: constant, trend, seasonal, and trend-seasonal.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Individual forecast</h3><p>Run a forecast for one material from material master maintenance when you need to review the parameters and result directly.</p></div>
      <div><h3>Periodic forecast job</h3><p>Schedule a recurring forecast run for a flexible material selection when the process should update automatically.</p></div>
      <div><h3>Automatic reorder point</h3><p>The forecast run can calculate safety stock first, then calculate the reorder point using expected demand during replenishment lead time.</p></div>
    </div>
    <p>Automatic safety stock uses the replenishment lead time, the service level maintained in the material master, and the mean absolute deviation calculated by the forecast as an indicator of forecast accuracy.</p>
  </section>

  <section class="research-canvas__inventory" id="time-phased" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Time-phased planning</p>
      <h2>Plan on the supplier or review cycle when replenishment follows a calendar.</h2>
      <p>Time-phased planning uses a planning calendar and planning cycle. The planning file carries the next planning date, and the material is normally planned only on the defined cycle dates.</p>
    </header>
    <p>The requirements horizon is built from the planning date, the planning cycle, and replenishment lead time. The system compares requirements in that interval with stock and firm receipts, then calculates the quantity to order. R2 combines this calendar logic with a reorder point so a shortage can trigger planning before the next regular cycle date.</p>
  </section>

  <section class="research-canvas__inventory" id="exceptions" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Exceptions and operations</p>
      <h2>Planning is not complete when the run finishes.</h2>
      <p>A Lead needs a way to see the exception, assign the owner, and prove the corrective action.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Coverage monitoring</h3><p>Manage Material Coverage can show shortages and let the planner trigger planning for selected materials. Monitor Material Coverage and the stock/requirements view support operational follow-up.</p></div>
      <div><h3>Situation Handling</h3><p>The MRP Material Exceptions situation template can notify responsible users when changed demand makes purchase or production orders unnecessary and excess stock risk appears.</p></div>
      <div><h3>Exception messages</h3><p>Treat the message as a signal. Trace the demand, proposal, fixed receipts, dates, source, and execution status before changing the planning parameters.</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="lead-lens" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead lens</p>
      <h2>Diagnose the first wrong planning decision.</h2>
      <p>When the proposal looks wrong, do not start by editing the purchase requisition.</p>
    </header>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="MRP diagnosis sequence">
      <table class="study-table__table">
        <thead><tr><th scope="col">Symptom</th><th scope="col">First checks</th><th scope="col">What the evidence proves</th></tr></thead>
        <tbody>
          <tr><th scope="row">Proposal created too early</th><td>MRP type, reorder point, stock and firm receipts, external-requirement setting.</td><td>Whether the shortage trigger itself was justified.</td></tr>
          <tr><th scope="row">Wrong quantity</th><td>Net shortage, lot-sizing procedure, minimum or maximum lot size, rounding value or profile.</td><td>Whether the quantity changed during lot sizing rather than demand calculation.</td></tr>
          <tr><th scope="row">Wrong date</th><td>Required date, purchasing processing time, planned delivery time, GR processing time, source-specific values.</td><td>Whether scheduling or source master data caused the date.</td></tr>
          <tr><th scope="row">Wrong supplier or agreement</th><td>Source determination, source validity, contract or scheduling agreement, purchasing info record.</td><td>Whether the proposal is right but the source decision is wrong.</td></tr>
          <tr><th scope="row">Plant stock looks sufficient but one line is short</th><td>MRP area, storage-location assignment, special procurement, subcontractor context.</td><td>Whether planning is happening at a different organizational boundary.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">record_voice_over</span>
    <div>
      <p><strong>60-second assessment answer:</strong> Consumption-based planning starts from the MRP type in the material master. In reorder point planning, SAP compares the available planning situation with the reorder point. If there is a shortage, it calculates a proposal quantity using lot-sizing and rounding rules, schedules the proposal using procurement lead times, determines the proposal type and possibly the source of supply, and creates exception messages when attention is required. I would diagnose a wrong result in that same order: trigger, quantity, dates, proposal type, source, then execution.</p>
      <p><strong>Lead follow-up:</strong> MRP Live is the preferred HANA-optimized engine where the scenario is supported, but classic MRP remains relevant for unsupported procedures and for more detailed creation and planning controls.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="practice" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Oral practice</p>
      <h2>Answer these without notes.</h2>
      <p>Keep each answer under two minutes, then add one diagnostic follow-up.</p>
    </header>
    <div class="research-route-list">
      <a href="#reorder-point"><span>01</span><strong>Explain VB versus VM.</strong><small>Include who maintains the reorder point and how forecasting changes the control model.</small><i class="material-symbols-outlined" aria-hidden="true">record_voice_over</i></a>
      <a href="#lot-sizing"><span>02</span><strong>Why can a shortage of 31 become a proposal for 35?</strong><small>Separate shortage calculation from lot sizing and rounding.</small><i class="material-symbols-outlined" aria-hidden="true">calculate</i></a>
      <a href="#scheduling"><span>03</span><strong>A requisition date is too early. Where do you look?</strong><small>Trace purchasing processing, planned delivery, GR processing, and source-specific values.</small><i class="material-symbols-outlined" aria-hidden="true">schedule</i></a>
      <a href="#mrp-live-classic"><span>04</span><strong>Why would you still use classic MRP?</strong><small>Discuss unsupported procedures, MRP lists, and detailed creation controls.</small><i class="material-symbols-outlined" aria-hidden="true">compare_arrows</i></a>
      <a href="#mrp-areas"><span>05</span><strong>Why can plant stock exist while one MRP area still has a shortage?</strong><small>Explain the organizational boundary of net requirements calculation.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#proposal-source"><span>06</span><strong>What is the difference between an MRP proposal and a purchasing commitment?</strong><small>Separate planning responsibility from PO execution and later supplier confirmation.</small><i class="material-symbols-outlined" aria-hidden="true">shopping_cart</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="sources" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Study sources</p>
      <h2>Release-sensitive points still require product-level verification.</h2>
      <p>This page is an independent study summary of the SAP Learning material supplied for the assessment preparation. The source itself points to SAP Notes for compatibility and MRP Live restrictions.</p>
    </header>
    <div class="research-route-list">
      <a href="https://me.sap.com/notes/2268095/E" target="_blank" rel="noopener"><span>SAP</span><strong>SAP Note 2268095</strong><small>Referenced by the source for forecast-based planning compatibility scope and replacement guidance.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://me.sap.com/notes/2269324" target="_blank" rel="noopener"><span>SAP</span><strong>SAP Note 2269324</strong><small>Referenced by the source together with the compatibility guidance for classic forecast-based planning.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="http://help.sap.com/disclaimer?site=https://launchpad.support.sap.com/#/notes/1914010" target="_blank" rel="noopener"><span>SAP</span><strong>SAP Note 1914010</strong><small>Referenced by the source for current MRP Live restrictions.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">route</span>
    <div>
      <p><strong>Continue the process:</strong> use Production Planning & Execution for in-house proposals and manufacturing orders; use Procurement for source determination, purchase requisitions, purchase orders, and supplier execution.</p>
      <p><a href="/labs/enterprise-context/production/">Open Production Planning & Execution</a> · <a href="/labs/enterprise-context/procurement/">Open Procurement</a></p>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
