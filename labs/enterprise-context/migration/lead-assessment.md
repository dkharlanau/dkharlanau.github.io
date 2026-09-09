---
layout: default
title: "SAP S/4HANA Migration Lead Assessment — Architecture Drills"
description: "Lead-level S/4HANA migration drills on scope, tooling, API loading, cloud limits, cutover, reconciliation, numbering, history, and recovery."
permalink: /labs/enterprise-context/migration/lead-assessment/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-09
hide_global_cta: true
tags:
  - sap
  - s4hana
  - migration
  - assessment
  - architecture
career_impact: mapped
career_skills:
  - integration-deployment
  - delivery-release
  - lead-decision
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/migration/">S/4HANA Migration</a></li><li aria-current="page">Lead Assessment</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Greenfield migration / Lead assessment</p>
      <h1>Defend the migration<br />as a business transition.</h1>
      <p>A strong Lead answer starts with business state, supported target capability, dependencies, evidence and recovery. Tool names come after scope and control.</p>
      <a class="research-canvas__button" href="#answer-model">Use the answer model <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Assessment model">
      <p>Lead answer</p>
      <div class="research-canvas__signal-line"><span>1</span><strong>State</strong><small>What must exist on day one</small></div>
      <div class="research-canvas__signal-line"><span>2</span><strong>Path</strong><small>How it gets there safely</small></div>
      <div class="research-canvas__signal-line"><span>3</span><strong>Proof</strong><small>How correctness is proved</small></div>
      <em>Then discuss trade-offs and recovery.</em>
    </div>
  </header>

  <section class="research-canvas__inventory" id="answer-model" data-reveal>
    <header><p class="research-canvas__eyebrow">60-second model</p><h2>Scope → dependency → mechanism → control → decision.</h2></header>
    <div class="research-route-list">
      <a href="#answer-model"><span>1</span><strong>Define the business state</strong><small>Configuration, master data, eligible open business, stock/balance, history or recurring integration?</small><i class="material-symbols-outlined" aria-hidden="true">category</i></a>
      <a href="#answer-model"><span>2</span><strong>Confirm the target contract</strong><small>Exact release, deployment model, migration object, prerequisite, restriction and supported interface.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
      <a href="#answer-model"><span>3</span><strong>Place it in the dependency graph</strong><small>What must exist first and which business or financial controls depend on it?</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#answer-model"><span>4</span><strong>Choose the path</strong><small>Migration Cockpit staging or direct transfer, or a justified released interface or custom extension.</small><i class="material-symbols-outlined" aria-hidden="true">conversion_path</i></a>
      <a href="#answer-model"><span>5</span><strong>Define proof and recovery</strong><small>Counts, values, process tests, financial tie-out, runtime, retry, stop condition and owner.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">psychology_alt</span>
    <p><strong>Assessment rule:</strong> do not choose a tool before you know the object, source, target deployment and whether the flow is one-time or recurring.</p>
    <p><strong>Challenge rule:</strong> when someone says “migrate everything”, ask which day-one operation, audit rule or reporting need requires each data class inside S/4.</p>
  </section>

  <section class="research-canvas__inventory" id="q1" data-reveal><header><p class="research-canvas__eyebrow">Question 01</p><h2>Why not migrate all ECC history?</h2></header><div class="research-route-list"><a href="#q1"><span>ANS</span><strong>Operational migration and historical retention solve different problems.</strong><small>Move the master data, eligible open transactions, stock and balances needed to operate S/4. Closed history usually stays in a governed legacy, archive or data platform. Copying it increases mapping and test risk and carries old process design into greenfield.</small><i class="material-symbols-outlined" aria-hidden="true">history</i></a></div></section>

  <section class="research-canvas__inventory" id="q2" data-reveal><header><p class="research-canvas__eyebrow">Question 02</p><h2>Staging tables or direct transfer?</h2></header><div class="research-route-list"><a href="#q2"><span>ANS</span><strong>Staging is the neutral boundary; direct transfer is the shortcut for a supported SAP source.</strong><small>Use staging for external, mixed or strongly transformed data. Use direct transfer when the SAP source scenario and object are supported. Both still require scope, mappings, prerequisites, simulation and reconciliation.</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a></div></section>

  <section class="research-canvas__inventory" id="q3" data-reveal><header><p class="research-canvas__eyebrow">Question 03</p><h2>Can Public Cloud use IDoc?</h2></header><div class="research-route-list"><a href="#q3"><span>ANS</span><strong>Only where SAP releases the exact communication scenario or interface.</strong><small>Do not claim IDoc is globally unavailable, and do not assume classic ALE freedom. For initial migration, prefer the released migration object. For recurring integration, use the released interface that fits.</small><i class="material-symbols-outlined" aria-hidden="true">mail</i></a></div></section>

  <section class="research-canvas__inventory" id="q4" data-reveal><header><p class="research-canvas__eyebrow">Question 04</p><h2>Would you use LSMW?</h2></header><div class="research-route-list"><a href="#q4"><span>ANS</span><strong>Not as the S/4 migration architecture.</strong><small>Old LSMW objects can call ECC-era interfaces that no longer represent the correct S/4 business object. Start with Migration Cockpit and the supported target interface; use custom migration content only for a proven gap.</small><i class="material-symbols-outlined" aria-hidden="true">dangerous</i></a></div></section>

  <section class="research-canvas__inventory" id="q5" data-reveal><header><p class="research-canvas__eyebrow">Question 05</p><h2>How do you migrate a partially delivered sales order?</h2></header><div class="research-route-list"><a href="#q5"><span>ANS</span><strong>First identify the exact migration object and approach.</strong><small>Open-document rules are not universal. If the selected object cannot carry the executed document flow, keep deliveries and billing as history and recreate only the remaining customer commitment under an approved rule. Reconcile remaining quantity and value, then test delivery and billing in S/4.</small><i class="material-symbols-outlined" aria-hidden="true">call_split</i></a></div></section>

  <section class="research-canvas__inventory" id="q6" data-reveal><header><p class="research-canvas__eyebrow">Question 06</p><h2>What about a PO with GR or invoice history?</h2></header><div class="research-route-list"><a href="#q6"><span>ANS</span><strong>Separate the remaining commitment from the executed procurement and finance history.</strong><small>Check the exact PO migration object and approach. If the old GR or invoice chain cannot move, retain it as history, recreate only the required target commitment, and reconcile remaining quantity, value, GR/IR and open financial items with Finance.</small><i class="material-symbols-outlined" aria-hidden="true">compare_arrows</i></a></div></section>

  <section class="research-canvas__inventory" id="q7" data-reveal><header><p class="research-canvas__eyebrow">Question 07</p><h2>How do you prove inventory migration?</h2></header><div class="research-route-list"><a href="#q7"><span>ANS</span><strong>Reconcile quantity, stock status, valuation and G/L together.</strong><small>Compare product, plant, storage location, batch, special stock, stock type and valuation dimensions. Then test real use: ATP, goods issue or receipt, transfers and production staging.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a></div></section>

  <section class="research-canvas__inventory" id="q8" data-reveal><header><p class="research-canvas__eyebrow">Question 08</p><h2>What if S/4 generates new internal numbers?</h2></header><div class="research-route-list"><a href="#q8"><span>ANS</span><strong>Legacy identity becomes part of the migration contract.</strong><small>Keep source system + source key as a governed cross-reference and use the legacy key consistently in dependent migration data where SAP ID mapping supports it.</small><i class="material-symbols-outlined" aria-hidden="true">key</i></a></div></section>

  <section class="research-canvas__inventory" id="q9" data-reveal><header><p class="research-canvas__eyebrow">Question 09</p><h2>A required field is missing from the migration object. What next?</h2></header><div class="research-route-list"><a href="#q9"><span>ANS</span><strong>Prove the gap before building around it.</strong><small>Check release, object notes, custom-field support and modeler release status. Then compare a supported enhancement, business API or interface, controlled post-load path or redesign. Never write directly to application tables.</small><i class="material-symbols-outlined" aria-hidden="true">extension</i></a></div></section>

  <section class="research-canvas__inventory" id="q10" data-reveal><header><p class="research-canvas__eyebrow">Question 10</p><h2>What custom solution is worth building?</h2></header><div class="research-route-list"><a href="#q10"><span>ANS</span><strong>A migration engineering layer, not a second ERP loader framework.</strong><small>Version mappings, staging metadata, transformations, validation rules, reconciliation queries and runbooks in Git. Let CI reject schema, mandatory-field, duplicate, mapping and referential defects before SAP load.</small><i class="material-symbols-outlined" aria-hidden="true">terminal</i></a></div></section>

  <section class="research-canvas__inventory" id="q11" data-reveal><header><p class="research-canvas__eyebrow">Question 11</p><h2>How do you design the final delta?</h2></header><div class="research-route-list"><a href="#q11"><span>ANS</span><strong>Per object, with an explicit watermark and retry rule.</strong><small>Define change detection, create, update and delete meaning, accepted cut-off and duplicate control. Do not advance the watermark until the batch is accepted. Stock and Finance need especially tight freezes.</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a></div></section>

  <section class="research-canvas__inventory" id="q12" data-reveal><header><p class="research-canvas__eyebrow">Question 12</p><h2>How many mock migrations?</h2></header><div class="research-route-list"><a href="#q12"><span>ANS</span><strong>Enough to prove stable production-like execution; not a fixed number.</strong><small>Expect object prototypes, integrated runs, production-volume rehearsal and full cutover rehearsal. Exit when mappings are stable, critical defects are closed, runtime has contingency, reconciliation passes and recovery is tested.</small><i class="material-symbols-outlined" aria-hidden="true">repeat</i></a></div></section>

  <section class="research-canvas__inventory" id="q13" data-reveal><header><p class="research-canvas__eyebrow">Question 13</p><h2>How do you roll back failed production migration?</h2></header><div class="research-route-list"><a href="#q13"><span>ANS</span><strong>Do not promise universal delete-and-reload.</strong><small>Define the recovery point before cutover. Before business release, abort and keep legacy authoritative or restore or rebuild where supported. After target postings start, recovery becomes object-specific correction or reversal.</small><i class="material-symbols-outlined" aria-hidden="true">restore</i></a></div></section>

  <section class="research-canvas__inventory" id="q14" data-reveal><header><p class="research-canvas__eyebrow">Question 14</p><h2>What changes across Public, Private and on-premise?</h2></header><div class="research-route-list"><a href="#q14"><span>ANS</span><strong>The business problem is similar; technical freedom is not.</strong><small>Public Cloud pushes harder toward released migration objects and communication scenarios with limited modeler extensions. Private and on-premise provide broader LTMOM and system control. More freedom helps gaps but also makes unsupported loaders easier to build.</small><i class="material-symbols-outlined" aria-hidden="true">cloud_queue</i></a></div></section>

  <section class="research-canvas__inventory" id="q15" data-reveal><header><p class="research-canvas__eyebrow">Question 15</p><h2>What evidence is required for go-live?</h2></header><div class="research-route-list"><a href="#q15"><span>ANS</span><strong>Technical completion, business reconciliation, financial tie-out, executable processes and known residual risk.</strong><small>Use key-set and count controls, quantities and values, subledger and inventory-to-G/L checks, critical process smoke tests, interface readiness, measured runtime, defect list and named decision owner.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a></div></section>

  <section class="research-canvas__inventory" id="q16" data-reveal><header><p class="research-canvas__eyebrow">Question 16</p><h2>Your first week as migration architect?</h2></header><div class="research-route-list"><a href="#q16"><span>ANS</span><strong>Establish scope and control before selecting tools.</strong><small>Map source systems and owners; classify configuration, masters, open business, stock and balances, history and integrations; confirm target release and object coverage; build the dependency graph; identify risky volume; define reconciliation; prototype one cross-domain slice.</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a></div></section>

  <section class="research-canvas__inventory" id="q17" data-reveal><header><p class="research-canvas__eyebrow">Question 17</p><h2>The business wants the same document numbers. What do you do?</h2></header><div class="research-route-list"><a href="#q17"><span>ANS</span><strong>Ask why the number itself matters.</strong><small>Lookup or audit may be solved with a legacy key or cross-reference. If legal or integration requirements need the exact number, confirm external numbering and range coexistence for that target object. Number preservation is a design decision.</small><i class="material-symbols-outlined" aria-hidden="true">pin</i></a></div></section>

  <section class="research-canvas__inventory" id="q18" data-reveal><header><p class="research-canvas__eyebrow">Question 18</p><h2>100% successful records. Ready?</h2></header><div class="research-route-list"><a href="#q18"><span>ANS</span><strong>No. That proves processing, not correctness.</strong><small>You still need source-to-target scope reconciliation, quantities and values, references, financial tie-out and end-to-end process tests. A valid order can still contain wrong customer mapping, price or delivery data.</small><i class="material-symbols-outlined" aria-hidden="true">cancel</i></a></div></section>

  <section class="research-canvas__inventory" id="q19" data-reveal><header><p class="research-canvas__eyebrow">Question 19</p><h2>Clean in legacy or transform during migration?</h2></header><div class="research-route-list"><a href="#q19"><span>ANS</span><strong>Fix source defects that affect ongoing legacy operation; transform rules caused by target redesign.</strong><small>Duplicate suppliers or invalid tax data may deserve source correction. Mapping old plants to a new target structure is migration transformation. Keep remediation and conversion logically separate.</small><i class="material-symbols-outlined" aria-hidden="true">cleaning_services</i></a></div></section>

  <section class="research-canvas__inventory" id="q20" data-reveal><header><p class="research-canvas__eyebrow">Question 20</p><h2>Biggest migration architecture mistake?</h2></header><div class="research-route-list"><a href="#q20"><span>ANS</span><strong>Treating migration as file loading instead of business-state transition.</strong><small>That hides scope, dependencies, accounting, history, integrations, ownership and recovery until cutover. Every object needs a day-one business need, supported target contract, predecessor graph and acceptance proof.</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a></div></section>

  <section class="research-canvas__inventory" id="q21" data-reveal><header><p class="research-canvas__eyebrow">Question 21</p><h2>Why not use an API if it can create the object?</h2></header><div class="research-route-list"><a href="/labs/enterprise-context/migration/api-led-migration/#decision"><span>ANS</span><strong>Create capability is only one gate.</strong><small>If a released Migration Cockpit object fits the initial state, it normally gives a migration-specific path with mapping, simulation and processing controls. Use an API when there is a proved gap or when the same governed flow must survive go-live. Then prove semantics, recovery, volume and reconciliation.</small><i class="material-symbols-outlined" aria-hidden="true">api</i></a></div></section>

  <section class="research-canvas__inventory" id="q22" data-reveal><header><p class="research-canvas__eyebrow">Question 22</p><h2>An API POST times out. Retry?</h2></header><div class="research-route-list"><a href="/labs/enterprise-context/migration/api-led-migration/#recovery"><span>ANS</span><strong>Not until the target outcome is known.</strong><small>The request may have been accepted even when the client missed the response. Put it in an uncertain state, query by target or business identity where possible, then decide retry, reconcile or manual resolution. Blind retry can create a duplicate.</small><i class="material-symbols-outlined" aria-hidden="true">restart_alt</i></a></div></section>

  <section class="research-canvas__inventory" id="q23" data-reveal><header><p class="research-canvas__eyebrow">Question 23</p><h2>The API works but misses the cutover window. Add more threads?</h2></header><div class="research-route-list"><a href="/labs/enterprise-context/migration/api-led-migration/#performance"><span>ANS</span><strong>Only if measured receiver capacity still improves safely.</strong><small>Find safe concurrency with production-like data. If errors, throttling or receiver pressure rise, more threads make recovery worse. Change the architecture: reduce scope, move baseline earlier, use Migration Cockpit where it fits, or change the cutover sequence.</small><i class="material-symbols-outlined" aria-hidden="true">speed</i></a></div></section>

  <section class="research-canvas__inventory" id="q24" data-reveal><header><p class="research-canvas__eyebrow">Question 24</p><h2>There is a Material Stock API. Can we load opening stock with it?</h2></header><div class="research-route-list"><a href="/labs/enterprise-context/migration/api-led-migration/#stock"><span>ANS</span><strong>Do not infer write capability from an object name.</strong><small>The current Material Stock API is read-only. A Material Document API can post movements, but using posting APIs for opening stock is a different design with movement, valuation and accounting effects. Check the released stock migration object first and reconcile inventory to G/L.</small><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a></div></section>

  <section class="research-canvas__inventory" id="challenge" data-reveal>
    <header><p class="research-canvas__eyebrow">Board challenge</p><h2>Questions a Lead should ask the programme.</h2></header>
    <div class="research-route-list">
      <a href="#challenge"><span>?</span><strong>Why must this data be operational in S/4 on day one?</strong><small>If the answer is only “we always migrate it”, reopen scope.</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
      <a href="#challenge"><span>?</span><strong>What source closing number proves it?</strong><small>No source control total means final reconciliation becomes subjective.</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
      <a href="#challenge"><span>?</span><strong>What happens if this object is 10% late?</strong><small>Expose the real critical path and blocked dependencies.</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
      <a href="#challenge"><span>?</span><strong>Where is the last safe stop point?</strong><small>Recovery must be a planned decision before data is posted.</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
      <a href="#challenge"><span>?</span><strong>Who signs the business number?</strong><small>The migration team produces evidence; a named business or finance owner accepts it.</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>