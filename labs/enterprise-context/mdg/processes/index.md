---
layout: default
title: "SAP MDG Governance Processes and Tools — Enterprise Context Lab"
description: "Central Governance, consolidation, mass processing, data quality, workflow, staging, activation, and replication in SAP MDG."
permalink: /labs/enterprise-context/mdg/processes/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-30
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
