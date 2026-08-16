---
layout: default
title: "SAP MDG Data Model Engineering — Enterprise Context Lab"
description: "Deep SAP MDG model engineering: business grain, entity boundaries, keys, relationships, active-area design, model evolution and downstream impact."
permalink: /labs/enterprise-context/mdg/data-model/engineering/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags: [sap, mdg, data-model, entity, keys, persistence, master-data]
---
{% assign topic = site.data.labs.enterprise_context.topics.mdg_data_model_engineering %}

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/mdg/">MDG</a></li><li><a href="/labs/enterprise-context/mdg/data-model/">Data Model</a></li><li aria-current="page">Engineering</li></ol></nav>

<div class="research-canvas">
<header class="research-canvas__hero" data-reveal><div class="research-canvas__hero-copy"><p class="research-canvas__eyebrow">MDG / Data Model Engineering</p><h1>A field has a grain, owner, lifecycle and cost.</h1><p>{{ topic.summary }}</p><a class="research-canvas__button" href="#contract">Open the model contract <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a></div><div class="research-canvas__signal"><p>Memory model</p><div class="research-canvas__signal-line"><span>01</span><strong>Grain</strong><small>Where does meaning live?</small></div><div class="research-canvas__signal-line"><span>02</span><strong>Key</strong><small>What identifies one instance?</small></div><div class="research-canvas__signal-line"><span>03</span><strong>Impact</strong><small>What else must change?</small></div><em>{{ topic.memory_model.phrase }}</em></div></header>

<section class="research-canvas__boundary" data-reveal><span class="material-symbols-outlined" aria-hidden="true">schema</span><p><strong>Design rule:</strong> {{ topic.memory_model.principle }}</p><p><a href="/labs/enterprise-context/mdg/build-runtime/">Build & runtime</a> · <a href="/labs/enterprise-context/mdg/lineage/">Lineage & provenance</a></p></section>

<section class="research-canvas__inventory" id="contract" data-reveal><header><p class="research-canvas__eyebrow">Model contract</p><h2>Start with business grain before entity type.</h2></header><div class="research-route-list">{% for question in topic.model_contract.root_questions %}<a href="#keys"><span>ROOT</span><strong>Governed root</strong><small>{{ question }}</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>{% endfor %}{% for question in topic.model_contract.entity_questions %}<a href="#keys"><span>ENT</span><strong>Entity boundary</strong><small>{{ question }}</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>{% endfor %}</div></section>

<section class="research-canvas__inventory" id="keys" data-reveal><header><p class="research-canvas__eyebrow">Key engineering</p><h2>Identity is not the same thing as organizational qualification.</h2><p>{{ topic.key_engineering.rule }}</p></header><div class="research-route-list">{% for item in topic.key_engineering.patterns %}<a href="/labs/enterprise-context/mdg/lineage/"><span>KEY</span><strong>{{ item.pattern }}</strong><small><b>{{ item.example }}</b> {{ item.design_check }}</small><i class="material-symbols-outlined" aria-hidden="true">key</i></a>{% endfor %}</div></section>

<section class="research-canvas__inventory" data-reveal><header><p class="research-canvas__eyebrow">Persistence</p><h2>Staging and active truth are part of the model.</h2></header><div class="research-route-list"><a href="/labs/enterprise-context/mdg/build-runtime/"><span>ACTIVE</span><strong>MDG active area</strong><small>{{ topic.persistence_engineering.mdg_active_area.meaning }} {{ topic.persistence_engineering.mdg_active_area.implications | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a><a href="/labs/enterprise-context/mdg/build-runtime/"><span>REUSE</span><strong>Reuse active area</strong><small>{{ topic.persistence_engineering.reuse_active_area.meaning }} {{ topic.persistence_engineering.reuse_active_area.implications | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">sync</i></a></div></section>

<section class="research-canvas__inventory" data-reveal><header><p class="research-canvas__eyebrow">Change impact</p><h2>A model change fans out across the solution.</h2></header><div class="research-route-list">{% for item in topic.field_impact_matrix %}<a href="/labs/enterprise-context/mdg/extensions/"><span>Δ</span><strong>{{ item.change }}</strong><small>Inspect: {{ item.inspect | join: " → " }}</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>{% endfor %}</div></section>

<section class="research-canvas__inventory" data-reveal><header><p class="research-canvas__eyebrow">Material examples</p><h2>Use organizational grain to avoid bad custom models.</h2></header><div class="research-route-list">{% for scn in topic.material_model_example.scenarios %}<a href="/labs/enterprise-context/mdg/logistics/"><span>MM</span><strong>{{ scn.requirement }}</strong><small><b>Model answer:</b> {{ scn.model_answer }} <b>Check:</b> {{ scn.downstream_checks | join: ", " }}.</small><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a>{% endfor %}</div></section>

<section class="research-canvas__inventory" data-reveal><header><p class="research-canvas__eyebrow">Model smells</p><h2>What I would challenge in a design review.</h2></header><div class="research-route-list">{% for smell in topic.model_smells %}<a href="/labs/enterprise-context/mdg/reasoning/"><span>!</span><strong>Design smell</strong><small>{{ smell }}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>{% endfor %}</div></section>

<div class="research-canvas__support" data-reveal>{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
