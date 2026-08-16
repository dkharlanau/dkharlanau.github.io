---
layout: default
title: "SAP MDG Build & Runtime Anatomy — Enterprise Context Lab"
description: "How an SAP MDG solution is built at design time and what happens at runtime from request and staging through rules, workflow, activation, replication and business proof."
permalink: /labs/enterprise-context/mdg/build-runtime/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags: [sap, mdg, architecture, runtime, workflow, replication]
---
{% assign topic = site.data.labs.enterprise_context.topics.mdg_build_runtime %}

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/mdg/">MDG</a></li><li aria-current="page">Build & Runtime</li></ol></nav>

<div class="research-canvas">
<header class="research-canvas__hero" data-reveal><div class="research-canvas__hero-copy"><p class="research-canvas__eyebrow">MDG / Build & Runtime</p><h1>Design-time tells us what should happen. Runtime proves what did happen.</h1><p>{{ topic.summary }}</p><a class="research-canvas__button" href="#build">Open the build stack <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a></div><div class="research-canvas__signal"><p>Memory model</p><div class="research-canvas__signal-line"><span>12</span><strong>Build layers</strong><small>Before go-live</small></div><div class="research-canvas__signal-line"><span>12</span><strong>Runtime stages</strong><small>One governed change</small></div><em>{{ topic.memory_model.phrase }}</em></div></header>

<section class="research-canvas__boundary" data-reveal><span class="material-symbols-outlined" aria-hidden="true">architecture</span><p><strong>Design rule:</strong> {{ topic.memory_model.principle }}</p><p><a href="/labs/enterprise-context/mdg/data-model/engineering/">Data model engineering</a> · <a href="/labs/enterprise-context/mdg/lineage/">Lineage & provenance</a></p></section>

<section class="research-canvas__inventory" id="build" data-reveal><header><p class="research-canvas__eyebrow">Design time</p><h2>Twelve layers have to agree before the first change request matters.</h2><p>The point is not to configure twelve technologies. The point is to make ownership, model, rules, authority, activation, distribution and operations one coherent contract.</p></header><div class="research-route-list">{% for layer in topic.design_time_layers %}<a href="#runtime"><span>{{ layer.order }}</span><strong>{{ layer.title }}</strong><small><b>{{ layer.question }}</b> Outputs: {{ layer.outputs | join: ", " }}.</small><i class="material-symbols-outlined" aria-hidden="true">layers</i></a>{% endfor %}</div></section>

<section class="research-canvas__inventory" id="runtime" data-reveal><header><p class="research-canvas__eyebrow">Runtime</p><h2>Follow one value across every boundary.</h2><p>This is the operational path I use when I want to explain or troubleshoot MDG without jumping directly to a table, workflow, or interface.</p></header><div class="research-route-list">{% for step in topic.runtime_chain %}<a href="/labs/enterprise-context/mdg/lineage/"><span>{{ step.stage }}</span><strong>{{ step.title }}</strong><small>{{ step.state }} <b>Evidence:</b> {{ step.evidence | join: ", " }}.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>{% endfor %}</div></section>

<section class="research-canvas__inventory" data-reveal><header><p class="research-canvas__eyebrow">Controls</p><h2>Where a Lead expects the design to fail.</h2></header><div class="research-route-list">{% for item in topic.control_points %}<a href="/labs/enterprise-context/mdg/reasoning/"><span>CTL</span><strong>{{ item.control }}</strong><small>{{ item.failure_if_missing }}</small><i class="material-symbols-outlined" aria-hidden="true">verified_user</i></a>{% endfor %}</div></section>

<section class="research-canvas__boundary" data-reveal><span class="material-symbols-outlined" aria-hidden="true">school</span><p><strong>Assessment memory:</strong> do not answer “MDG is Fiori + BRFplus + workflow + DRF”. Explain the chain: {{ topic.memory_model.phrase }}.</p></section>

<div class="research-canvas__support" data-reveal>{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
