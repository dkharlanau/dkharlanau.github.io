---
layout: default
title: "SAP MDG Implementation and Presales Guide — Enterprise Context Lab"
description: "A practical SAP MDG implementation guide covering ownership, data model, workflow, quality, integration, operations, and delivery decisions."
permalink: /labs/enterprise-context/mdg/implementation/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-14
hide_global_cta: true
tags: [sap, mdg, implementation, presales, data-governance, architecture]
---

{% assign topic = site.data.labs.enterprise_context.topics.master_data_governance_landscape %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/mdg/">MDG</a></li><li aria-current="page">Implementation</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">MDG / implementation and presales</p>
      <h1>Good MDG starts before configuration.</h1>
      <p>First decide ownership and scope. Then design the data model, governance process, quality rules, replication, and operating model. Reversing that order usually creates a very polished workflow around an unclear decision.</p>
      <a class="research-canvas__button" href="#implementation-path">Open the implementation path <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal">
      <p>Architecture sequence</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Own</strong><small>Who decides?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Model</strong><small>What is governed?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Flow</strong><small>How does it change?</small></div>
      <div class="research-canvas__signal-line"><span>04</span><strong>Publish</strong><small>Who consumes it?</small></div>
    </div>
  </header>

  <section class="research-canvas__inventory" id="implementation-path" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Implementation path</p>
      <h2>Ten decisions before the solution is stable.</h2>
      <p>The order matters because each step constrains the next one.</p>
    </header>
    <div class="research-route-list">
      <a href="#presales"><span>01</span><strong>Define the business pain and domain</strong><small>Which master-data problem creates process cost, risk, delay, or rework?</small><i class="material-symbols-outlined" aria-hidden="true">flag</i></a>
      <a href="#ownership"><span>02</span><strong>Define ownership</strong><small>Assign domain owner, attribute owners, requesters, stewards, approvers, and consumers.</small><i class="material-symbols-outlined" aria-hidden="true">groups</i></a>
      <a href="/labs/enterprise-context/mdg/deployments/"><span>03</span><strong>Select the product and deployment boundary</strong><small>Match domain breadth, core-vs-application data, existing S/4HANA, and federated-vs-central operating model.</small><i class="material-symbols-outlined" aria-hidden="true">cloud</i></a>
      <a href="#data-model"><span>04</span><strong>Design the data model and governance scope</strong><small>Govern only the required entities and fields. Define active, staged, derived, read-only, and externally owned data.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="/labs/enterprise-context/mdg/processes/"><span>05</span><strong>Design request types and workflow</strong><small>Use risk and responsibility to drive approvals. Do not copy the organization chart into a workflow.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#quality"><span>06</span><strong>Design data quality</strong><small>Required fields, derivations, validations, duplicates, reference data, and external enrichment should have explicit rules.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="#replication"><span>07</span><strong>Design replication and mappings</strong><small>Define consumers, timing, key mapping, value mapping, error handling, retries, and monitoring.</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a>
      <a href="#migration"><span>08</span><strong>Consolidate and load legacy data</strong><small>Resolve duplicate and survivorship rules before treating one record as authoritative.</small><i class="material-symbols-outlined" aria-hidden="true">merge</i></a>
      <a href="#testing"><span>09</span><strong>Test the whole process</strong><small>Test workflow, rules, activation, replication, authorization, volume, and downstream transactions.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="#operate"><span>10</span><strong>Run the governance operating model</strong><small>Track cycle time, quality, replication failures, exceptions, stewardship load, and ownership decisions.</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="ownership" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Ownership</p>
      <h2>Workflow starts with accountability.</h2>
      <p>A useful ownership model answers who may request, who enriches, who decides, who owns quality, who operates replication, and who resolves downstream exceptions.</p>
    </header>
    <div class="research-route-list">
      {% for principle in topic.implementation_principles %}
      <a href="/labs/enterprise-context/data/topics.json"><span>HEUR</span><strong>{{ principle.statement }}</strong><small>{{ principle.why }}</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="data-model" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Data model</p>
      <h2>Model ownership at field level, not only object level.</h2>
      <p>{{ topic.data_architecture.principle }}</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/mdg/deployments/"><span>S4</span><strong>Classic S/4HANA MDG</strong><small>{{ topic.data_architecture.classic_mode.active_data }} {{ topic.data_architecture.classic_mode.governance_scope }}</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="/labs/enterprise-context/mdg/deployments/"><span>CE</span><strong>Cloud edition</strong><small>{{ topic.data_architecture.cloud_edition.core_model }} {{ topic.data_architecture.cloud_edition.federation }}</small><i class="material-symbols-outlined" aria-hidden="true">cloud</i></a>
      <a href="/labs/enterprise-context/mdg/architecture/#extensibility"><span>EXT</span><strong>Plan extension points with the data model</strong><small>A custom field may also need workflow, validation, replication, search, authorization, and reporting behavior.</small><i class="material-symbols-outlined" aria-hidden="true">extension</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="quality" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Data quality</p>
      <h2>Rules should prevent business exceptions, not only improve a score.</h2>
      <p>Link every important validation or derivation to a process consequence: planning, ordering, shipping, billing, tax, posting, or compliance.</p>
    </header>
  </section>

  <section class="research-canvas__inventory" id="replication" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Replication</p>
      <h2>Approved does not mean available.</h2>
      <p>For S/4HANA MDG, DRF is a central replication mechanism. For MDG cloud edition, supported Business Partner replication uses MDI and SOAP. In both cases, the design still needs consumer readiness, mappings, monitoring, and error ownership.</p>
      <p><a href="/labs/enterprise-context/mdg/architecture/#interfaces">Open the interface architecture →</a></p>
    </header>
  </section>

  <section class="research-canvas__inventory" id="migration" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Legacy data and consolidation</p>
      <h2>Do not govern yesterday's duplicates as tomorrow's truth.</h2>
      <p>Before central governance becomes authoritative, profile source data, define matching and survivorship rules, resolve key conflicts, and decide which attributes win when sources disagree. Initial load is therefore a data-governance decision as much as a migration activity.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/mdg/processes/"><span>01</span><strong>Profile and standardize</strong><small>Find structural errors, weak reference values, missing mandatory data, and inconsistent formats.</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      <a href="/labs/enterprise-context/mdg/processes/"><span>02</span><strong>Match and merge</strong><small>Identify duplicates and define which records represent the same real-world object.</small><i class="material-symbols-outlined" aria-hidden="true">merge</i></a>
      <a href="/labs/enterprise-context/mdg/processes/"><span>03</span><strong>Define survivorship</strong><small>Choose trusted sources and field-level precedence instead of declaring a golden record by slogan.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
      <a href="/labs/enterprise-context/mdg/architecture/#interfaces"><span>04</span><strong>Prepare identifiers and mappings</strong><small>Resolve central keys, local keys, code lists, target mappings, and downstream acceptance before the cutover.</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="testing" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Testing</p>
      <h2>Test a business transaction after the master-data process.</h2>
      <p>A successful workflow is not enough. Create the sales order, purchase order, MRP result, delivery, warehouse task, invoice, or posting that proves the governed data is operationally usable.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/mdg/logistics/"><span>TEST</span><strong>Field and rule tests</strong><small>Required fields, derivation, validation, duplicate checks, and governance scope.</small><i class="material-symbols-outlined" aria-hidden="true">checklist</i></a>
      <a href="/labs/enterprise-context/mdg/logistics/"><span>TEST</span><strong>Workflow and authorization tests</strong><small>Correct agents, roles, segregation of duties, escalation, rejection, restart, and audit trail.</small><i class="material-symbols-outlined" aria-hidden="true">checklist</i></a>
      <a href="/labs/enterprise-context/mdg/logistics/"><span>TEST</span><strong>Replication tests</strong><small>Initial send, delta, retries, mapping failures, duplicate messages, late consumers, and monitoring.</small><i class="material-symbols-outlined" aria-hidden="true">checklist</i></a>
      <a href="/labs/enterprise-context/mdg/logistics/"><span>TEST</span><strong>Downstream regression</strong><small>Prove that consuming sales, procurement, planning, warehouse, transport, and finance processes can use the new data.</small><i class="material-symbols-outlined" aria-hidden="true">checklist</i></a>
      <a href="/labs/enterprise-context/mdg/logistics/"><span>TEST</span><strong>Volume tests</strong><small>Large consolidation and mass-processing runs need realistic package sizes, parallelization, and operating windows.</small><i class="material-symbols-outlined" aria-hidden="true">checklist</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="presales" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Presales discovery</p>
      <h2>Find the pain before showing the product.</h2>
      <p>The best first conversation is usually about blocked business processes, duplicate records, slow onboarding, inconsistent ownership, or unreliable distribution. “We need MDG” is a conclusion, not a requirement.</p>
    </header>
    <div class="research-route-list">
      {% for question in topic.presales_questions %}
      <a href="/labs/enterprise-context/data/topics.json"><span>?</span><strong>{{ question }}</strong><small>Use the answer to narrow scope, deployment, governance capability, and integration design.</small><i class="material-symbols-outlined" aria-hidden="true">forum</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Failure modes</p>
      <h2>How MDG projects become expensive without becoming useful.</h2>
    </header>
    <div class="research-route-list">
      {% for failure in topic.failure_modes %}
      <a href="/labs/enterprise-context/data/topics.json"><span>!</span><strong>{{ failure.title }}</strong><small>{{ failure.cause }}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="operate" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Operating model</p>
      <h2>Measure whether governance improves the process.</h2>
    </header>
    <div class="research-route-list">
      {% for metric in topic.success_metrics %}
      <a href="/labs/enterprise-context/data/topics.json"><span>KPI</span><strong>{{ metric.title }}</strong><small>{{ metric.description }}</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
