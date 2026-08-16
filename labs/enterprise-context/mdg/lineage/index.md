---
layout: default
title: "SAP MDG Lineage & Provenance — Enterprise Context Lab"
description: "Trace one governed master-data value from origin through change request, rules, workflow, activation, replication, key mapping and downstream business consumption."
permalink: /labs/enterprise-context/mdg/lineage/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags: [sap, mdg, lineage, provenance, audit, replication, master-data]
---
{% assign topic = site.data.labs.enterprise_context.topics.mdg_lineage %}

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/mdg/">MDG</a></li><li aria-current="page">Lineage</li></ol></nav>

<div class="research-canvas">
<header class="research-canvas__hero" data-reveal><div class="research-canvas__hero-copy"><p class="research-canvas__eyebrow">MDG / Lineage & Provenance</p><h1>“Approved” is one point in the lineage, not the end of it.</h1><p>{{ topic.summary }}</p><a class="research-canvas__button" href="#dimensions">Trace the value <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a></div><div class="research-canvas__signal"><p>Lineage model</p><div class="research-canvas__signal-line"><span>01</span><strong>Origin</strong><small>Who or what supplied it?</small></div><div class="research-canvas__signal-line"><span>02</span><strong>Decision</strong><small>Who changed/approved it?</small></div><div class="research-canvas__signal-line"><span>03</span><strong>Use</strong><small>Where did business consume it?</small></div><em>{{ topic.memory_model.phrase }}</em></div></header>

<section class="research-canvas__boundary" data-reveal><span class="material-symbols-outlined" aria-hidden="true">account_tree</span><p><strong>Boundary:</strong> {{ topic.lineage_boundary.mdg_scope }}</p><p><strong>Do not overclaim:</strong> {{ topic.lineage_boundary.not_claimed }}</p><p>{{ topic.lineage_boundary.external_metadata_boundary }}</p></section>

<section class="research-canvas__inventory" id="dimensions" data-reveal><header><p class="research-canvas__eyebrow">Six dimensions</p><h2>Lineage is more than a before/after field value.</h2></header><div class="research-route-list">{% for dim in topic.lineage_dimensions %}<a href="#evidence"><span>LIN</span><strong>{{ dim.title }}</strong><small><b>{{ dim.question }}</b> Capture: {{ dim.capture | join: ", " }}.</small><i class="material-symbols-outlined" aria-hidden="true">timeline</i></a>{% endfor %}</div></section>

<section class="research-canvas__inventory" data-reveal><header><p class="research-canvas__eyebrow">Value provenance</p><h2>Name how the value came to exist.</h2><p>{{ topic.provenance_states.vocabulary_status }}. This vocabulary is deliberately simple so a human or agent can preserve provenance even when products use different technical mechanisms.</p></header><div class="research-route-list">{% for state in topic.provenance_states.states %}<a href="/labs/enterprise-context/mdg/build-runtime/"><span>PROV</span><strong>{{ state.title }}</strong><small>{{ state.meaning }}</small><i class="material-symbols-outlined" aria-hidden="true">fingerprint</i></a>{% endfor %}</div></section>

<section class="research-canvas__inventory" id="evidence" data-reveal><header><p class="research-canvas__eyebrow">Audit evidence</p><h2>Each boundary needs evidence of its own.</h2></header><div class="research-route-list">{% for item in topic.audit_evidence %}<a href="/labs/enterprise-context/mdg/reasoning/"><span>EV</span><strong>{{ item.stage }}</strong><small>{{ item.evidence | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>{% endfor %}</div></section>

<section class="research-canvas__boundary" data-reveal><span class="material-symbols-outlined" aria-hidden="true">history</span><p><strong>Change documents:</strong> during change-request processing, MDG uses USMD change documents; activation uses USMD_ACT for the last change written to the active area. With reuse active areas, additional application change documents can depend on the interface and Customizing.</p></section>

<section class="research-canvas__inventory" data-reveal><header><p class="research-canvas__eyebrow">Identity lineage</p><h2>The business object can stay the same while its technical key changes.</h2><p>{{ topic.identity_lineage.problem }}</p></header><div class="research-route-list">{% for control in topic.identity_lineage.controls %}<a href="/labs/enterprise-context/mdg/interfaces/"><span>ID</span><strong>{{ topic.identity_lineage.trace }}</strong><small>{{ control }}</small><i class="material-symbols-outlined" aria-hidden="true">key</i></a>{% endfor %}</div></section>

<section class="research-canvas__inventory" data-reveal><header><p class="research-canvas__eyebrow">Synthetic traces</p><h2>Trace into logistics, not only into MDG.</h2></header><div class="research-route-list">{% for trace in topic.trace_templates %}<a href="/labs/enterprise-context/mdg/logistics/"><span>CASE</span><strong>{{ trace.title }}</strong><small>{{ trace.path | join: " → " }}</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>{% endfor %}</div></section>

<section class="research-canvas__inventory" data-reveal><header><p class="research-canvas__eyebrow">Failure isolation</p><h2>A lineage model becomes useful when something is wrong.</h2></header><div class="research-route-list">{% for fail in topic.lineage_failure_modes %}<a href="/labs/enterprise-context/mdg/reasoning/"><span>!</span><strong>{{ fail.symptom }}</strong><small>Isolate: {{ fail.isolate | join: " → " }}</small><i class="material-symbols-outlined" aria-hidden="true">troubleshoot</i></a>{% endfor %}</div></section>

<div class="research-canvas__support" data-reveal>{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
