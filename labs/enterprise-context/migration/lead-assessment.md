---
layout: default
title: "SAP S/4HANA Migration Lead Assessment — Architecture Questions and Answers"
description: "Lead-level S/4HANA greenfield migration drills covering scope, Migration Cockpit, Public Cloud, IDoc, LSMW, cutover, reconciliation, partial documents, numbering and recovery."
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
      <p>A strong Lead answer starts with business state, supported target capability, dependencies, evidence and recovery. Tool names matter, but they come after scope and control.</p>
      <a class="research-canvas__button" href="#answer-model">Use the answer model <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Assessment model">
      <p>Lead answer</p>
      <div class="research-canvas__signal-line"><span>1</span><strong>State</strong><small>What must exist on day one</small></div>
      <div class="research-canvas__signal-line"><span>2</span><strong>Path</strong><small>How it gets there safely</small></div>
      <div class="research-canvas__signal-line"><span>3</span><strong>Proof</strong><small>How we know it is correct</small></div>
      <em>Then discuss trade-offs and recovery.</em>
    </div>
  </header>

  <section class="research-canvas__inventory" id="answer-model" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">60-second answer model</p>
      <h2>Scope → dependency → mechanism → control → decision.</h2>
    </header>
    <div class="research-route-list">
      <a href="#answer-model"><span>1</span><strong>Define the business state</strong><small>Is this configuration, master data, open business, stock/balance, closed history or recurring integration?</small><i class="material-symbols-outlined" aria-hidden="true">category</i></a>
      <a href="#answer-model"><span>2</span><strong>Confirm the target contract</strong><small>Check the exact S/4 release, deployment model, migration object, prerequisites, restrictions and supported API/interface.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
      <a href="#answer-model"><span>3</span><strong>Place it in the dependency graph</strong><small>What must exist first, what depends on this object, and what cross-domain balance or process does it affect?</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#answer-model"><span>4</span><strong>Choose the technical path</strong><small>Migration Cockpit staging, direct transfer, released API, supported IDoc or a controlled custom extension.</small><i class="material-symbols-outlined" aria-hidden="true">conversion_path</i></a>
      <a href="#answer-model"><span>5</span><strong>Define proof and recovery</strong><small>Counts, values, business tests, finance tie-out, runtime, retry, stop condition and go/no-go owner.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">psychology_alt</span>
    <p><strong>Assessment rule:</strong> do not answer “Which tool would you use?” before you know the object, source, target deployment and whether the flow is one-time or recurring.</p>
    <p><strong>Challenge rule:</strong> when the requirement is “migrate everything”, ask what business operation, audit need or reporting need requires each data class in S/4.</p>
  </section>

  <section class="research-canvas__inventory" id="q1" data-reveal>
    <header><p class="research-canvas__eyebrow">Question 01</p><h2>Why not migrate all ECC history into a greenfield S/4 system?</h2></header>
    <div class="research-route-list">
      <a href="#q1"><span>ANS</span><strong>Because operational migration and historical retention solve different problems.</strong><small>I migrate the master data, open transactions, stock and balances needed to operate the target. Closed history usually stays in a governed legacy/archive/data platform unless a supported object and a real legal or business requirement justify moving it. Copying all history increases mapping, testing and cutover risk and can also carry obsolete process design into the new system.</small><i class="material-symbols-outlined" aria-hidden="true">history</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="q2" data-reveal>
    <header><p class="research-canvas__eyebrow">Question 02</p><h2>When would you use staging tables and when direct transfer?</h2></header>
    <div class="research-route-list">
      <a href="#q2"><span>ANS</span><strong>Staging is my neutral boundary; direct transfer is my shortcut for a supported SAP source.</strong><small>For non-SAP or heavily transformed legacy data, I prefer staging because the source can be cleansed and mapped into the SAP-defined contract before load. For a supported SAP ERP source and migration object, direct transfer can reduce extraction work. In both cases I still own scope, mappings, dependencies, simulation and reconciliation.</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="q3" data-reveal>
    <header><p class="research-canvas__eyebrow">Question 03</p><h2>Can SAP S/4HANA Cloud Public Edition use IDoc?</h2></header>
    <div class="research-route-list">
      <a href="#q3"><span>ANS</span><strong>Yes, but only where SAP released the required communication scenario and interface.</strong><small>I would not say “IDoc is unavailable in Public Cloud”, and I would not assume classic ALE freedom either. I check the exact interface in SAP Help/API documentation. For initial migration I still prefer the released Migration Cockpit object where it fits. For a recurring interface, a released API or supported IDoc can be appropriate.</small><i class="material-symbols-outlined" aria-hidden="true">mail</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="q4" data-reveal>
    <header><p class="research-canvas__eyebrow">Question 04</p><h2>Would you use LSMW for an S/4HANA migration?</h2></header>
    <div class="research-route-list">
      <a href="#q4"><span>ANS</span><strong>Not as the migration architecture.</strong><small>SAP positions Migration Cockpit as the tool of choice for S/4 data migration, and old LSMW interfaces can point to BAPI, IDoc, direct-input or batch-input techniques that no longer match the S/4 business object. I would first use Migration Cockpit, a released API/interface, or a controlled migration-object enhancement. Familiarity with an ECC tool is not a support argument.</small><i class="material-symbols-outlined" aria-hidden="true">dangerous</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="q5" data-reveal>
    <header><p class="research-canvas__eyebrow">Question 05</p><h2>How do you migrate a partially delivered sales order?</h2></header>
    <div class="research-route-list">
      <a href="#q5"><span>ANS</span><strong>I migrate the remaining commitment, not the historical document flow.</strong><small>First I check whether the target migration object supports the document type and status. Then I separate the already executed legacy part from the quantity/value that still has to be delivered. If the remaining part cannot be represented safely, I close or split the legacy document and create a controlled target order. I reconcile remaining quantity and value and test the target delivery/billing flow.</small><i class="material-symbols-outlined" aria-hidden="true">call_split</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="q6" data-reveal>
    <header><p class="research-canvas__eyebrow">Question 06</p><h2>How do you migrate a purchase order with goods receipt or invoice history?</h2></header>
    <div class="research-route-list">
      <a href="#q6"><span>ANS</span><strong>I treat it as Procurement plus Finance, not only a PO load.</strong><small>The target should represent the remaining open business, while historical receipts and invoices normally remain historical. I check the migration-object restrictions, then agree the remaining quantity/value and GR/IR or open-item treatment with Finance. I do not create fake target goods movements to rebuild legacy PO history.</small><i class="material-symbols-outlined" aria-hidden="true">compare_arrows</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="q7" data-reveal>
    <header><p class="research-canvas__eyebrow">Question 07</p><h2>How do you prove inventory migration is correct?</h2></header>
    <div class="research-route-list">
      <a href="#q7"><span>ANS</span><strong>I reconcile quantity, stock status, valuation and G/L together.</strong><small>Counts by material are not enough. I compare product, plant, storage location, batch, special stock, stock type and valuation dimensions, then tie inventory value to the financial opening position. I also test real use: ATP, goods issue, receipt, transfer and production staging on representative stock.</small><i class="material-symbols-outlined" aria-hidden="true">balance</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="q8" data-reveal>
    <header><p class="research-canvas__eyebrow">Question 08</p><h2>What if S/4 generates new internal numbers for products or Business Partners?</h2></header>
    <div class="research-route-list">
      <a href="#q8"><span>ANS</span><strong>The legacy identity becomes part of the migration contract.</strong><small>I keep the source system and source key as a governed cross-reference. In Migration Cockpit I reuse the legacy number in dependent objects where SAP supports ID mapping. Outside the cockpit I maintain a source-to-target key table so support, reconciliation and later loads can always trace the relationship.</small><i class="material-symbols-outlined" aria-hidden="true">key</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="q9" data-reveal>
    <header><p class="research-canvas__eyebrow">Question 09</p><h2>What do you do when a required field is not supported by the migration object?</h2></header>
    <div class="research-route-list">
      <a href="#q9"><span>ANS</span><strong>I prove the gap before I build around it.</strong><small>First I check the exact release, object notes, custom-field support and whether the field is released for the migration-object modeler. Then I compare a released API, supported IDoc/interface, post-load business maintenance or a small custom loader around a released business API. I do not write directly to application tables.</small><i class="material-symbols-outlined" aria-hidden="true">extension</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="q10" data-reveal>
    <header><p class="research-canvas__eyebrow">Question 10</p><h2>What custom solution would you build for a large migration programme?</h2></header>
    <div class="research-route-list">
      <a href="#q10"><span>ANS</span><strong>A migration engineering layer, not a second ERP loader framework.</strong><small>I would version source-to-target mappings, staging metadata, transformations, validation rules, reconciliation queries and runbooks in Git. CI would check schema, mandatory fields, duplicate keys, value mappings, referential dependencies and transformation tests. The target load would still use Migration Cockpit or released business interfaces wherever possible.</small><i class="material-symbols-outlined" aria-hidden="true">terminal</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="q11" data-reveal>
    <header><p class="research-canvas__eyebrow">Question 11</p><h2>How would you design the final delta?</h2></header>
    <div class="research-route-list">
      <a href="#q11"><span>ANS</span><strong>Per object, with an explicit watermark and retry rule.</strong><small>I define how changes are detected, what timestamp or change pointer is authoritative, how insert/update/delete is represented, and what happens on retry. I do not advance the extraction watermark until the batch is accepted. For stock and finance I use a tighter freeze because late postings change both quantity and value.</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="q12" data-reveal>
    <header><p class="research-canvas__eyebrow">Question 12</p><h2>How many mock migrations do you need?</h2></header>
    <div class="research-route-list">
      <a href="#q12"><span>ANS</span><strong>Enough to prove stable production-like execution; I do not manage by a fixed number.</strong><small>I expect a prototype, an integrated dependency run, a production-volume rehearsal and at least one full cutover rehearsal, but the exit criterion is what matters: critical defects closed, mappings stable, runtime inside the window with contingency, reconciliation passed and recovery decisions tested.</small><i class="material-symbols-outlined" aria-hidden="true">repeat</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="q13" data-reveal>
    <header><p class="research-canvas__eyebrow">Question 13</p><h2>How do you roll back a failed production data migration?</h2></header>
    <div class="research-route-list">
      <a href="#q13"><span>ANS</span><strong>I do not promise a universal delete-and-reload rollback.</strong><small>Many business objects cannot simply be removed once created or referenced. I define a recovery point before cutover. Before business release, the best option may be to abort and keep legacy authoritative, or restore/rebuild the target where the platform supports it. After postings start, recovery becomes object-specific business reversal/correction. That is why stop conditions must be earlier than the point of no return.</small><i class="material-symbols-outlined" aria-hidden="true">restore</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="q14" data-reveal>
    <header><p class="research-canvas__eyebrow">Question 14</p><h2>What changes between Public Cloud, Private Cloud and on-premise migration?</h2></header>
    <div class="research-route-list">
      <a href="#q14"><span>ANS</span><strong>The business migration problem is similar; the technical freedom is not.</strong><small>Public Cloud pushes me toward released migration objects, communication scenarios and limited modeler extensions. Private Edition and on-premise give broader Migration Cockpit/LTMOM and system control. More freedom can help a real gap, but it also makes unsupported custom loaders easier to build. In all three I design from the supported target business object first.</small><i class="material-symbols-outlined" aria-hidden="true">cloud_queue</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="q15" data-reveal>
    <header><p class="research-canvas__eyebrow">Question 15</p><h2>What evidence do you need for go-live approval?</h2></header>
    <div class="research-route-list">
      <a href="#q15"><span>ANS</span><strong>Technical completion, business reconciliation, financial tie-out, executable processes and known residual risk.</strong><small>I want object key-set/count controls, quantities and values, AR/AP/asset/inventory-to-G/L reconciliation, critical end-to-end smoke tests on migrated data, interface readiness, runtime inside the window, open defect/risk list, named workarounds and a signed decision owner.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="q16" data-reveal>
    <header><p class="research-canvas__eyebrow">Question 16</p><h2>What would you do in your first week as the migration architect?</h2></header>
    <div class="research-route-list">
      <a href="#q16"><span>ANS</span><strong>I would establish scope and control before selecting tools.</strong><small>I would map source systems and owners; classify data into configuration, masters, open business, balances/stock, history and recurring integrations; confirm target deployment/release and migration-object availability; create the dependency graph; identify high-risk objects and volume; define reconciliation principles; and set the first prototype path for one cross-domain slice such as customer → product → open sales order.</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="q17" data-reveal>
    <header><p class="research-canvas__eyebrow">Question 17</p><h2>The business says: “Keep the same document numbers.” What do you do?</h2></header>
    <div class="research-route-list">
      <a href="#q17"><span>ANS</span><strong>I ask why the number itself matters.</strong><small>If the need is user lookup, audit or reference, a legacy-number field or source-to-target cross-reference may solve it without forcing target number ranges. If legal or integration requirements depend on the exact number, I check whether the target object supports external numbering and whether the range can coexist with new documents. Number preservation is a design decision, not a default migration requirement.</small><i class="material-symbols-outlined" aria-hidden="true">pin</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="q18" data-reveal>
    <header><p class="research-canvas__eyebrow">Question 18</p><h2>A load has 100% successful records. Are you ready?</h2></header>
    <div class="research-route-list">
      <a href="#q18"><span>ANS</span><strong>No. That proves processing, not correctness.</strong><small>I still need source-to-target scope reconciliation, values and quantities, cross-object references, finance tie-out and end-to-end process tests. A technically valid sales order can still have the wrong customer mapping, wrong price or unusable delivery data.</small><i class="material-symbols-outlined" aria-hidden="true">cancel</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="q19" data-reveal>
    <header><p class="research-canvas__eyebrow">Question 19</p><h2>How do you handle data quality: clean in legacy or transform during migration?</h2></header>
    <div class="research-route-list">
      <a href="#q19"><span>ANS</span><strong>Fix the source when the defect affects ongoing legacy operations; transform when the rule exists only because the target model changed.</strong><small>Duplicates, invalid tax IDs or wrong supplier ownership may deserve source correction. Mapping old plant codes to a redesigned target structure is a migration transformation. I separate remediation from transformation so the business knows which problems still exist in the source and which are deliberate target conversions.</small><i class="material-symbols-outlined" aria-hidden="true">cleaning_services</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="q20" data-reveal>
    <header><p class="research-canvas__eyebrow">Question 20</p><h2>What is the biggest migration architecture mistake?</h2></header>
    <div class="research-route-list">
      <a href="#q20"><span>ANS</span><strong>Treating migration as file loading instead of business-state transition.</strong><small>That mistake hides scope, dependencies, accounting, history, interfaces, ownership and recovery until the cutover. I want every object connected to a day-one business need, a supported target contract, a predecessor graph and an acceptance proof.</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="challenge" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Board challenge</p>
      <h2>Questions a Lead should ask the programme.</h2>
    </header>
    <div class="research-route-list">
      <a href="#challenge"><span>?</span><strong>Why does this data need to be operational in S/4 on day one?</strong><small>If the answer is only “we always migrate it”, reopen the scope.</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
      <a href="#challenge"><span>?</span><strong>What source closing number will prove this object?</strong><small>If there is no source control total, final reconciliation will become subjective.</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
      <a href="#challenge"><span>?</span><strong>What happens when this object is 10% late?</strong><small>Find the true cutover critical path and the dependency that cannot start.</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
      <a href="#challenge"><span>?</span><strong>Where is the last safe stop point?</strong><small>Recovery must be a planned decision, not a panic discussion after data is posted.</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
      <a href="#challenge"><span>?</span><strong>Who signs the business number?</strong><small>The migration team produces evidence. A named business/finance owner accepts it.</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
