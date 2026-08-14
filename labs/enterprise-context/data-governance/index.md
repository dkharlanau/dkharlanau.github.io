---
layout: default
title: "Data, Master Data and Governance — Enterprise Context Lab"
description: "An enterprise context map from the Data and Analytics area through master-data domains and SAP MDG applications to governed objects and logistics dependencies."
permalink: /labs/enterprise-context/data-governance/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-14
hide_global_cta: true
tags:
  - sap
  - enterprise-context
  - data-management
  - master-data
  - mdg
  - data-governance
  - logistics
---

{% assign topic = site.data.labs.enterprise_context.topics.data_governance_landscape %}
{% assign mdg = site.data.labs.enterprise_context.topics.master_data_governance_landscape %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/domains/">Domains</a></li><li aria-current="page">Data & Governance</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise Context Lab / Data area</p>
      <h1>{{ topic.title }}</h1>
      <p>{{ topic.summary }}</p>
      <a class="research-canvas__button" href="#hierarchy">Follow the graph <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Data governance map">
      <p>Context depth</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>1</strong><small>Enterprise area</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ topic.hierarchy.domains | size }}</strong><small>Data domains</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ topic.master_data_objects | size }}</strong><small>Master-data objects</small></div>
      <em>{{ topic.mdg_position.remember }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">schema</span>
    <p><strong>Boundary:</strong> SAP MDG is an application. It is not the whole Data and Analytics domain.</p>
    <p><strong>Remember:</strong> {{ topic.architecture_rule.explanation }}</p>
    <a href="/labs/enterprise-context/mdg/">Open the SAP MDG deep dive <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="hierarchy" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Level 1 / Area</p>
      <h2>{{ topic.hierarchy.area.title }}</h2>
      <p><strong>{{ topic.hierarchy.area.remember }}</strong> {{ topic.hierarchy.area.role }}</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/domains/"><span>AREA</span><strong>{{ topic.hierarchy.area.title }}</strong><small>{{ topic.hierarchy.area.role }}</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Level 2 / Domains</p>
      <h2>Separate the data problem before selecting the product.</h2>
      <p>Master Data Management, governance, quality, semantics, integration, and analytics solve different parts of the problem.</p>
    </header>
    <div class="research-route-list">
      {% for domain in topic.hierarchy.domains %}
      <a href="/labs/enterprise-context/data/topics.json"><span>DOM</span><strong>{{ domain.title }}</strong><small><b>{{ domain.remember }}</b> {{ domain.purpose }}</small><i class="material-symbols-outlined" aria-hidden="true">category</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Level 3 / Application</p>
      <h2>Where SAP MDG enters the map.</h2>
      <p>Once the data domain and object scope are clear, choose the MDG variant by responsibility and deployment boundary.</p>
    </header>
    <div class="research-route-list">
      {% for variant in mdg.variants %}
      <a href="/labs/enterprise-context/mdg/deployments/"><span>APP</span><strong>{{ variant.title }}</strong><small><b>{{ variant.architecture_role }}</b> {{ variant.remember }}</small><i class="material-symbols-outlined" aria-hidden="true">deployed_code</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Level 4 / Capabilities</p>
      <h2>What the governance layer actually does.</h2>
      <p>Use capabilities to explain the business job. Product names come after the job is understood.</p>
    </header>
    <div class="research-route-list">
      {% for capability in topic.governance_capabilities %}
      <a href="/labs/enterprise-context/mdg/processes/"><span>CAP</span><strong>{{ capability.title }}</strong><small>{{ capability.role }}</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="objects" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Level 5 / Master-data objects</p>
      <h2>Objects are where architecture becomes operational.</h2>
      <p>For assessment and presales, name the object, its attributes, its owner, and the processes that fail when it is wrong.</p>
    </header>
    <div class="research-route-list">
      {% for object in topic.master_data_objects %}
      <a href="/labs/enterprise-context/mdg/logistics/"><span>MD</span><strong>{{ object.title }}</strong><small>{{ object.business_role }} Typical attributes: {{ object.typical_attributes | join: ", " }}.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Cross-domain dependencies</p>
      <h2>The same master data drives several business domains.</h2>
      <p>This is why master data is cross-cutting. A weak record often surfaces as a logistics or finance incident far away from the maintenance screen.</p>
    </header>
    <div class="research-route-list">
      {% for link in topic.business_domain_links %}
      <a href="/labs/enterprise-context/mdg/logistics/"><span>→</span><strong>{{ link.business_domain }}</strong><small>Depends on {{ link.depends_on | join: ", " }}. Process examples: {{ link.process_examples | join: ", " }}.</small><i class="material-symbols-outlined" aria-hidden="true">conversion_path</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Architecture decision path</p>
      <h2>Area → domain → application → object → process.</h2>
      <p>This sequence keeps the discussion business-led without losing the SAP detail.</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.decision_path %}
      <a href="/labs/enterprise-context/data/topics.json"><span>?</span><strong>{{ item.question }}</strong><small>{{ item.answer }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_right_alt</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Assessment language</p>
      <h2>Explain the model without turning it into product marketing.</h2>
      <p>These are compact talking points for architecture, presales, and Lead-level discussions.</p>
    </header>
    <div class="research-route-list">
      {% for point in topic.assessment_talking_points %}
      <a href="/labs/enterprise-context/mdg/"><span>LEAD</span><strong>{{ point }}</strong><small>Use the graph behind the statement when a deeper question follows.</small><i class="material-symbols-outlined" aria-hidden="true">record_voice_over</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
