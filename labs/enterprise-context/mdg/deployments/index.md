---
layout: default
title: "SAP MDG Deployment Options — Enterprise Context Lab"
description: "Compare SAP MDG on S/4HANA, cloud edition, classic mode, cloud-ready mode, and Public Edition boundaries."
permalink: /labs/enterprise-context/mdg/deployments/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [sap, mdg, cloud, s4hana, architecture]
---

{% assign topic = site.data.labs.enterprise_context.topics.master_data_governance_landscape %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/mdg/">MDG</a></li><li aria-current="page">Deployments</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">MDG / deployment decision</p>
      <h1>Cloud is not “the same MDG somewhere else”.</h1>
      <p>The product boundary changes the domains, data model, replication model, extensibility, and the ownership split between core data and application data.</p>
      <a class="research-canvas__button" href="#portfolio">Compare the options <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal">
      <p>Decision anchor</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Domain</strong><small>What data must be governed?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Depth</strong><small>Core or application attributes?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Owner</strong><small>Central or federated?</small></div>
      <em>Then choose deployment</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">warning</span>
    <p><strong>Problem:</strong> the word “cloud” hides materially different MDG products, modes, domain scope, and ownership models.</p>
    <p><strong>Current boundary:</strong> SAP MDG, cloud edition 2605 focuses on core Business Partner. SAP MDG on S/4HANA remains the broad multi-domain choice for Business Partner, Material/Product, Financials, and Custom Objects.</p>
    <p><strong>Architectural consequence:</strong> if Material governance is a hard requirement, “cloud edition because we want cloud” is not a design decision. It is a scope mismatch.</p>
    <a href="/labs/enterprise-context/mdg/logistics/">See the logistics consequence <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="portfolio" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Portfolio</p>
      <h2>Three related choices with different boundaries.</h2>
      <p>Use the memory hook first, then inspect the domain and replication details.</p>
    </header>
    <div class="research-route-list">
      {% for variant in topic.variants %}
      <a href="/labs/enterprise-context/data/topics.json"><span>APP</span><strong>{{ variant.title }}</strong><small><b>{{ variant.remember }}</b> {{ variant.architecture_role }} · {{ variant.deployment }}</small><i class="material-symbols-outlined" aria-hidden="true">deployed_code</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">S/4HANA MDG modes</p>
      <h2>Classic and cloud-ready are modes inside S/4HANA MDG.</h2>
      <p>This distinction is easy to confuse with “MDG cloud edition”. Keep it explicit in architecture discussions.</p>
    </header>
    <div class="research-route-list">
      {% for variant in topic.variants %}
        {% if variant.id == "APP-SAP-MDG-S4" %}
          {% for mode in variant.modes %}
          <a href="/labs/enterprise-context/data/topics.json"><span>MODE</span><strong>{{ mode.title }}</strong><small>{{ mode.scope }} {{ mode.technology }}{% if mode.boundary %} <b>Boundary:</b> {{ mode.boundary }}{% endif %}</small><i class="material-symbols-outlined" aria-hidden="true">tune</i></a>
          {% endfor %}
        {% endif %}
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Mode-switch warning</p>
      <h2>A switch can change which apps and processes remain usable.</h2>
      <p>Cloud-ready mode is not a harmless UI toggle. SAP documents restrictions around classic consolidation and mass-processing apps, and processes created in cloud-ready mode cannot be continued after switching back to classic mode.</p>
    </header>
    <div class="research-route-list">
      <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/34085136212d495aa7718063a34c5485.html" target="_blank" rel="noopener"><span>!</span><strong>Check mode-switch consequences before testing in a shared landscape</strong><small>Read the current SAP restriction before treating classic and cloud-ready modes as reversible configuration variants.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Decision rules</p>
      <h2>Choose by governance responsibility.</h2>
    </header>
    <div class="research-route-list">
      {% for item in topic.presales_decision_guide %}
      <a href="/labs/enterprise-context/mdg/implementation/#presales"><span>→</span><strong>{{ item.question }}</strong><small>{{ item.guidance }}</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
