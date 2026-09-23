---
layout: default
title: "SAP MDG Governance Processes and Tools — Enterprise Context Lab"
description: "Central Governance, consolidation, mass processing, data quality, workflow, staging, activation, and replication in SAP MDG."
permalink: /labs/enterprise-context/mdg/processes/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-23
hide_global_cta: true
tags: [sap, mdg, workflow, data-quality, mass-processing]
---

{% assign topic = site.data.labs.enterprise_context.topics.master_data_governance_landscape %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/mdg/">MDG</a></li><li aria-current="page">Processes</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">MDG / governance processes</p>
      <h1>One acronym. Four very different jobs.</h1>
      <p>Central Governance controls change. Consolidation repairs and unifies source data. Mass Processing changes many records. Data Quality Management makes rules measurable and reusable.</p>
      <a class="research-canvas__button" href="#governed-change">Trace a governed change <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal">
      <p>Memory line</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Request</strong><small>Why should data change?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Decide</strong><small>Is it valid and approved?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Publish</strong><small>Activate and distribute.</small></div>
      <em>Then monitor</em>
    </div>
  </header>

  <section class="research-canvas__inventory">
    <header>
      <p class="research-canvas__eyebrow">Capabilities</p>
      <h2>Pick the capability by the problem.</h2>
    </header>
    <div class="research-route-list">
      {% for capability in topic.capabilities %}
      <a id="{{ capability.id | downcase }}" href="/labs/enterprise-context/data/topics.json"><span>CAP</span><strong>{{ capability.title }}</strong><small><b>{{ capability.remember }}</b> {{ capability.purpose }}</small><i class="material-symbols-outlined" aria-hidden="true">settings</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="governed-change" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Central Governance</p>
      <h2>{{ topic.memory_model.phrase }}</h2>
      <p>Think of Central Governance as a controlled state transition. A record is not “good” because a form was completed. It becomes usable after the correct roles, rules, activation, and distribution have completed.</p>
    </header>
    <div class="research-route-list">
      {% for step in topic.process_model.central_governance.steps %}
      <a href="/labs/enterprise-context/data/topics.json"><span>STEP</span><strong>{{ step.title }}</strong><small>{{ step.detail }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="snapshot-refresh" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Open change requests and backend updates</p>
      <h2>Keep the change request in sync with the active master record.</h2>
      <p>An open change request can live for hours or days. During that time, the active Material or Business Partner may still be changed in the backend. If the change request keeps an older snapshot, its later activation can conflict with those newer backend changes. SAP provides an automatic snapshot refresh so the open request can continue from the current master-data state instead of an outdated baseline.</p>
    </header>

    <div class="ecg-control-stack">
      <article>
        <span>01</span>
        <h3>Why the refresh exists</h3>
        <p>The refresh is designed to protect intended backend changes from being overwritten when an existing change request is activated. SAP describes the refresh as updating the snapshot and inactive data after relevant master-data updates.</p>
        <strong>Lead point: approval history is not enough if the request is working with stale active data.</strong>
      </article>
      <article>
        <span>02</span>
        <h3>bgRFC prerequisite</h3>
        <p>Configure the inbound bgRFC destination <code>MDG_SNAPSHOT_REFRESH</code> with queue prefix <code>MDG_SNAP_</code> in <code>SBGRFCCONF</code>. Use <code>SBGRFCMON</code> when you need to check whether background refresh processing is running or blocked.</p>
        <strong>Operational proof: the queue is configured and processing without unresolved errors.</strong>
      </article>
      <article>
        <span>03</span>
        <h3>Material trigger</h3>
        <p>For Material, use <code>MDGIMG</code> and navigate to Classic Mode in SAP MDG → Central Governance → Central Governance for Material → Activate Business Transaction Events. The <code>MDGCRU</code> application must be active for this refresh integration.</p>
        <strong>Configuration proof: the Material refresh event is active in the target client.</strong>
      </article>
      <article>
        <span>04</span>
        <h3>Business Partner trigger</h3>
        <p>For Business Partner, Customer, and Supplier, use <code>BUPA_CALL_FU</code> or the corresponding Activate Function Modules activity. The documented event is <code>BPOUT</code>, object <code>BUPX</code>, item <code>5500001</code>, with function module <code>MDG_BS_BP_SNAPSHOT_UPD</code> and the Call indicator active.</p>
        <strong>Configuration proof: the BP outbound event calls the MDG snapshot-update function.</strong>
      </article>
    </div>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">sync</span>
      <p><strong>How we should think about it:</strong> snapshot refresh is a consistency safeguard inside Central Governance. It is not the same as DRF replication. Snapshot refresh keeps an open request aligned with changes to its source master object; DRF distributes activated master data to consuming systems.</p>
      <p><strong>Test pattern:</strong> in a non-production system, open a change request, change the same master object through an approved backend path, confirm bgRFC processing, reopen the request, and verify that the intended backend change is still present before activation.</p>
      <p><strong>Release boundary:</strong> do not copy the settings blindly between releases. Confirm the Help Portal topic and relevant SAP Notes for the exact S/4HANA release and support-package level.</p>
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/50ec75e0419b45909abe72fe92a35275.html">SAP Help: Set Up Integration of Refresh Change Request in Master Data Updates <span class="material-symbols-outlined" aria-hidden="true">open_in_new</span></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="snapshot-refresh-faq" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">FAQ</p>
      <h2>Questions worth remembering for an assessment.</h2>
    </header>
    <div class="research-route-list">
      <a href="#snapshot-refresh"><span>Q</span><strong>Why can a valid change request still be risky?</strong><small>Because validation and approval do not guarantee that the active master record stayed unchanged while the request was open. A stale snapshot can create a consistency problem at activation.</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
      <a href="#snapshot-refresh"><span>Q</span><strong>What is the first technical dependency?</strong><small>bgRFC. The documented inbound destination is <code>MDG_SNAPSHOT_REFRESH</code> with queue prefix <code>MDG_SNAP_</code>.</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
      <a href="#snapshot-refresh"><span>Q</span><strong>Where do Material and Business Partner differ?</strong><small>Material uses the MDGCRU Business Transaction Event activation in MDGIMG. Business Partner uses the BPOUT/BUPX event and function module MDG_BS_BP_SNAPSHOT_UPD.</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
      <a href="#snapshot-refresh"><span>Q</span><strong>What do we monitor when refresh does not happen?</strong><small>Start with SBGRFCMON, then verify the inbound destination and the object-specific trigger. After that, check whether the backend update path actually reached the expected event for your release.</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">difference</span>
    <p><strong>Central Governance vs Consolidation:</strong> governance controls future creation and change. Consolidation resolves what already exists across sources by standardizing, matching, merging, and selecting the best record.</p>
    <p><strong>Mass Processing:</strong> scales controlled change across many records. It should keep validation and ownership, not become a respectable name for bulk bypass.</p>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">lock</span>
    <p><strong>Bulk-change limitation:</strong> master-data changes outside the governed Fiori flow — for example with backend transactions, MASS, custom ABAP, APIs, or BAPIs — can still trigger automatic DRF replication when direct output is active. With a large population, repeated outbound processing can overlap with the update and create enqueue contention, target-side locks, or duplicate outbound messages.</p>
    <p><strong>Operational workaround:</strong> first prove that replication is the source of the lock in SM12 and the relevant replication logs. For a controlled maintenance window, temporarily deactivate only the affected replication model in DRFIMG, run the bulk change, then reactivate the model and execute the planned catch-up replication and source-to-target reconciliation.</p>
    <p><strong>Boundary:</strong> do not treat this as a universal lock fix. DRFIMG controls replication-model configuration, so use owner approval and record the before-and-after state.</p>
    <a href="/atlas/diagnostics/sap-master-data-diagnostics-hub/">Open master-data diagnostics <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Tools and technology</p>
      <h2>Each tool owns a different part of the control loop.</h2>
    </header>
    <div class="research-route-list">
      {% for tool in topic.tools %}
      <a href="/labs/enterprise-context/data/topics.json"><span>TOOL</span><strong>{{ tool.title }}</strong><small>{{ tool.role }}{% if tool.commercial_boundary %} <b>Commercial boundary:</b> {{ tool.commercial_boundary }}{% endif %}</small><i class="material-symbols-outlined" aria-hidden="true">construction</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Data model</p>
      <h2>Governance needs a clear place for inactive and active data.</h2>
      <p>{{ topic.data_architecture.principle }}</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/mdg/deployments/"><span>S4</span><strong>Classic S/4HANA MDG</strong><small>{{ topic.data_architecture.classic_mode.staging }} {{ topic.data_architecture.classic_mode.active_data }}</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="/labs/enterprise-context/mdg/deployments/"><span>CE</span><strong>MDG cloud edition</strong><small>{{ topic.data_architecture.cloud_edition.core_model }} {{ topic.data_architecture.cloud_edition.federation }}</small><i class="material-symbols-outlined" aria-hidden="true">cloud</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Diagnostic questions</p>
      <h2>Before changing workflow, ask what is failing.</h2>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/mdg/implementation/"><span>?</span><strong>Is data wrong before approval or after replication?</strong><small>This separates governance-rule problems from distribution or consumer problems.</small><i class="material-symbols-outlined" aria-hidden="true">troubleshoot</i></a>
      <a href="/labs/enterprise-context/mdg/implementation/"><span>?</span><strong>Is the issue one record or a population?</strong><small>Single governance, consolidation, and mass processing need different diagnostics.</small><i class="material-symbols-outlined" aria-hidden="true">troubleshoot</i></a>
      <a href="/labs/enterprise-context/mdg/implementation/"><span>?</span><strong>Who owns the attribute?</strong><small>If nobody can answer this, adding another approval step will not solve the real problem.</small><i class="material-symbols-outlined" aria-hidden="true">troubleshoot</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
