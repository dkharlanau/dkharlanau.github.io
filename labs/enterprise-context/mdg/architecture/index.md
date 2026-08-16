---
layout: default
title: "SAP MDG Solution Architecture — Enterprise Context Lab"
description: "How an SAP MDG solution is built: application layers, data-model engineering, runtime governance, lineage, interfaces, extensibility, security, monitoring, and practical design decisions."
permalink: /labs/enterprise-context/mdg/architecture/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags:
  - sap
  - mdg
  - architecture
  - integration
  - extensibility
  - lineage
  - data-model
  - rap
  - abap-cloud
---

{% assign topic = site.data.labs.enterprise_context.topics.mdg_solution_architecture %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/mdg/">MDG</a></li><li aria-current="page">Architecture</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise Context Lab / MDG architecture</p>
      <h1>Build the governance path, not only the application.</h1>
      <p>{{ topic.summary }}</p>
      <a class="research-canvas__button" href="#build-map">Open the build map <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Architecture research status">
      <p>Build model</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ topic.architecture_layers | size }}</strong><small>Architecture layers</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ topic.interface_catalog | size }}</strong><small>Interface patterns</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ topic.application_build_patterns | size }}</strong><small>Build patterns</small></div>
      <em>Source scan {{ topic.source_reviewed_at }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">architecture</span>
    <p><strong>Memory line:</strong> {{ topic.memory_model.phrase }}.</p>
    <p><strong>Design rule:</strong> {{ topic.memory_model.principle }}</p>
    <a href="/labs/enterprise-context/mdg/implementation/">Move from architecture to implementation <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Engineering deep dives</p>
      <h2>The architecture becomes real when model, runtime, and evidence meet.</h2>
      <p>These three routes go below the component diagram. They explain where a field belongs, what happens to one concrete change at runtime, and how to prove the value from origin to business use.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/mdg/data-model/engineering/"><span>MODEL</span><strong>Data Model Engineering</strong><small>Business grain, root and dependent entities, keys, cardinality, staging, active-area strategy, field impact, and model evolution.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="/labs/enterprise-context/mdg/build-runtime/"><span>RUN</span><strong>Build &amp; Runtime Anatomy</strong><small>Separate design-time artifacts from the runtime chain: source → staging → rules → authority → activation → replication → consumer proof.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/labs/enterprise-context/mdg/lineage/"><span>LIN</span><strong>Lineage &amp; Provenance</strong><small>Trace who or what supplied a value, what changed it, who approved it, what became active, where it was distributed, and where business used it.</small><i class="material-symbols-outlined" aria-hidden="true">timeline</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="build-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Solution build map</p>
      <h2>Six layers must fit together.</h2>
      <p>A good MDG design connects the business object to governance logic, integration, extension, security, and operations. A beautiful form with weak distribution is still a broken governance solution.</p>
    </header>
    <div class="research-route-list">
      {% for layer in topic.architecture_layers %}
      <a href="/labs/enterprise-context/data/topics.json"><span>{{ forloop.index | prepend: '0' }}</span><strong>{{ layer.title }}</strong><small><b>{{ layer.question }}</b> {{ layer.design_rule | default: layer.warning }}</small><i class="material-symbols-outlined" aria-hidden="true">layers</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Build patterns</p>
      <h2>Classic, cloud-ready, and cloud edition are different engineering choices.</h2>
      <p>The functional scope changes, but so does the extension model. Cloud-ready mode is based on ABAP Cloud, CDS, RAP, and SAP Fiori. The extension boundary is intentionally stricter than “find an object and modify it”.</p>
    </header>
    <div class="research-route-list">
      {% for pattern in topic.application_build_patterns %}
      <a href="/labs/enterprise-context/mdg/deployments/"><span>BUILD</span><strong>{{ pattern.title }}</strong><small><b>{{ pattern.strength }}</b> {{ pattern.caution }}</small><i class="material-symbols-outlined" aria-hidden="true">construction</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="interfaces" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Interfaces</p>
      <h2>Know what each interface is responsible for.</h2>
      <p>DRF, SOAP, MDI, load APIs, and key mapping solve different parts of the distribution problem. “We have an interface” is not an architecture.</p>
    </header>
    <div class="research-route-list">
      {% for interface in topic.interface_catalog %}
      <a href="/labs/enterprise-context/integrations/"><span>INT</span><strong>{{ interface.title }}</strong><small><b>{{ interface.direction }}</b> · {{ interface.used_for }}{% if interface.boundary %} Boundary: {{ interface.boundary }}{% endif %}</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="extensibility" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Extensibility</p>
      <h2>Extend at the lowest safe layer.</h2>
      <p>First ask whether configuration is enough. Then use supported field, UI, business-logic, or RAP extension points. A new business responsibility may belong in a side-by-side application instead of inside MDG.</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.extensibility_model.decision_order %}
      <a href="/labs/enterprise-context/data/topics.json"><span>→</span><strong>{{ item.question }}</strong><small>{{ item.choice }}</small><i class="material-symbols-outlined" aria-hidden="true">extension</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Integration design</p>
      <h2>Questions that expose hidden interface work.</h2>
      <p>The hard part is usually not sending XML or JSON. It is ownership, identifiers, code mappings, retries, filters, and what happens when a consumer rejects an approved record.</p>
    </header>
    <div class="research-route-list">
      {% for question in topic.integration_design_questions %}
      <a href="/labs/enterprise-context/integrations/"><span>?</span><strong>{{ question }}</strong><small>Resolve this before the interface contract is treated as complete.</small><i class="material-symbols-outlined" aria-hidden="true">device_hub</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Operations</p>
      <h2>Activation is not the end of the process.</h2>
      <p>The real outcome is an approved record that every required consumer can identify, accept, and use. Monitoring therefore crosses workflow, data quality, replication, mappings, and consumer exceptions.</p>
    </header>
    <div class="research-route-list">
      {% for signal in topic.operational_model.monitor %}
      <a href="/labs/enterprise-context/data/topics.json"><span>OPS</span><strong>{{ signal }}</strong><small>Define owner, alert path, diagnostic evidence, and reprocessing procedure.</small><i class="material-symbols-outlined" aria-hidden="true">monitor_heart</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead answer</p>
      <h2>A compact architecture explanation for an assessment.</h2>
      <p>{{ topic.lead_assessment_answer.short }}</p>
      <p><strong>Path:</strong> {{ topic.lead_assessment_answer.architecture_path }}</p>
    </header>
    <div class="research-route-list">
      {% for flag in topic.lead_assessment_answer.red_flags %}
      <a href="/labs/enterprise-context/mdg/implementation/"><span>!</span><strong>{{ flag }}</strong><small>This is a design smell because it breaks ownership, lifecycle stability, or operational control.</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
