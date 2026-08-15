---
layout: default
title: "BRFplus, AIF and ISLM — Decision, Recovery and AI Lifecycle"
description: "SAP map for BRFplus rules, AIF exception handling, and ISLM intelligent-scenario lifecycle."
permalink: /labs/enterprise-context/frameworks/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags:
  - sap
  - brfplus
  - aif
  - islm
  - business-rules
  - exception-handling
  - integration
  - machine-learning
  - generative-ai
  - ai-lifecycle
  - mdg
  - output-management
---

{% assign brf = site.data.labs.enterprise_context.topics.brfplus_rule_framework %}
{% assign aif = site.data.labs.enterprise_context.topics.application_interface_framework %}
{% assign islm = site.data.labs.enterprise_context.topics.intelligent_scenario_lifecycle_management %}
{% assign registry = site.data.labs.enterprise_context.sources.cross_application_frameworks_registry %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li aria-current="page">Cross-Application Frameworks</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise Context Lab / Cross-Application Frameworks</p>
      <h1>BRFplus decides.<br />AIF recovers.<br />ISLM operationalizes AI.</h1>
      <p>Three reusable SAP frameworks solve different problems. BRFplus externalizes selected business decisions. AIF makes interface failures understandable and recoverable. ISLM manages the lifecycle that connects S/4HANA business use cases to embedded or side-by-side AI.</p>
      <a class="research-canvas__button" href="#brfplus">Start with BRFplus <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Framework research status">
      <p>Research scope</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ brf.maturity.gates_complete }}/{{ brf.maturity.gates_total }}</strong><small>BRFplus gates</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ aif.maturity.gates_complete }}/{{ aif.maturity.gates_total }}</strong><small>AIF gates</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ islm.maturity.gates_complete }}/{{ islm.maturity.gates_total }}</strong><small>ISLM gates</small></div>
      <div class="research-canvas__signal-line"><span>04</span><strong>{{ registry.sources | size }}</strong><small>Primary sources</small></div>
      <em>Sources checked {{ registry.source_checked_at }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <p><strong>Do not merge the responsibilities.</strong> A rule engine is not a workflow engine. An exception monitor is not middleware. An AI lifecycle framework is not the model runtime and does not own the business action after inference.</p>
    <p><strong>Memory line:</strong> {{ brf.memory_model.phrase }} · {{ aif.memory_model.phrase }} · {{ islm.memory_model.phrase }}.</p>
    <a href="/labs/enterprise-context/data/brfplus.json">Open BRFplus structured data <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
  </section>

  <section class="research-canvas__inventory" id="brfplus" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">BRFplus / Business decisions</p>
      <h2>{{ brf.title }}</h2>
      <p>{{ brf.memory_model.short_definition }} <strong>Lead view:</strong> {{ brf.memory_model.lead_line }}</p>
    </header>
    <div class="research-route-list">
      {% for item in brf.availability.timeline %}
      <a href="#brfplus-model"><span>VER</span><strong>{{ item.release }}</strong><small>{{ item.meaning }}</small><i class="material-symbols-outlined" aria-hidden="true">history</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="brfplus-model" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">BRFplus object model</p>
      <h2>Function is the contract. Rules are the implementation.</h2>
      <p>This distinction matters. The application should depend on a stable context and result, not on the internal shape of a decision table.</p>
    </header>
    <div class="research-route-list">
      {% for item in brf.object_model %}
      <a href="/labs/enterprise-context/data/brfplus.json"><span>OBJ</span><strong>{{ item.object }}</strong><small>{{ item.role }}</small><i class="material-symbols-outlined" aria-hidden="true">deployed_code</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="brfplus-use" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Where BRFplus fits</p>
      <h2>Same rule engine, different consuming applications.</h2>
      <p>Do not start with “we have BRFplus”. Start with the decision that needs an owner and the SAP application that consumes the result.</p>
    </header>
    <div class="research-route-list">
      {% for item in brf.use_cases %}
      <a href="/labs/enterprise-context/data/brfplus.json"><span>USE</span><strong>{{ item.title }}</strong><small>{{ item.problem }} <b>BRFplus:</b> {{ item.how_brfplus_fits }} <b>Boundary:</b> {{ item.lead_boundary }}</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="brfplus-setup" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">BRFplus setup</p>
      <h2>Model a decision service, not a spreadsheet with runtime privileges.</h2>
      <p>The sequence keeps ownership, interface contract, testing, and transport visible before rules become production behavior.</p>
    </header>
    <div class="research-route-list">
      {% for item in brf.setup_sequence %}
      <a href="/labs/enterprise-context/data/brfplus.json"><span>{{ item.step }}</span><strong>{{ item.title }}</strong><small>{{ item.detail }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">BRFplus design review</p>
      <h2>Good rules stay explainable.</h2>
      <p>Decision tables are excellent until they become a programming language invented during a workshop.</p>
    </header>
    <div class="research-route-list">
      {% for rule in brf.design_rules %}
      <a href="/labs/enterprise-context/data/brfplus.json"><span>RULE</span><strong>{{ rule.statement }}</strong><small>{{ rule.questions | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
      {% endfor %}
      {% for item in brf.limitations %}
      <a href="/labs/enterprise-context/data/brfplus.json"><span>!</span><strong>Boundary</strong><small>{{ item }}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">sync_problem</span>
    <p><strong>Now the other problem:</strong> a correct business rule does not help when an interface fails at 02:00 and nobody knows who owns the message, which field is wrong, or whether restart will create a duplicate.</p>
    <a href="#aif">Open AIF exception handling <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
  </section>

  <section class="research-canvas__inventory" id="aif" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">AIF / Exception handling</p>
      <h2>{{ aif.title }}</h2>
      <p>{{ aif.memory_model.short_definition }} <strong>Lead view:</strong> {{ aif.memory_model.lead_line }}</p>
    </header>
    <div class="research-route-list">
      {% for item in aif.availability.timeline %}
      <a href="#aif-position"><span>VER</span><strong>{{ item.release }}</strong><small>{{ item.meaning }}</small><i class="material-symbols-outlined" aria-hidden="true">history</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="aif-position" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Architecture position</p>
      <h2>AIF is application-side recovery, not another middleware layer.</h2>
      <p>The useful boundary is operational: middleware moves and transforms data across systems; AIF can make SAP-side processing failures understandable and recoverable.</p>
    </header>
    <div class="research-route-list">
      {% for item in aif.architecture_position.owns %}
      <a href="/labs/enterprise-context/data/aif.json"><span>YES</span><strong>AIF responsibility</strong><small>{{ item }}</small><i class="material-symbols-outlined" aria-hidden="true">check_circle</i></a>
      {% endfor %}
      {% for item in aif.architecture_position.does_not_replace %}
      <a href="/labs/enterprise-context/data/aif.json"><span>NO</span><strong>Do not replace</strong><small>{{ item }}</small><i class="material-symbols-outlined" aria-hidden="true">block</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="aif-setup" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">AIF setup</p>
      <h2>Design the support contract before opening the monitor.</h2>
      <p>Namespace, interface, engines, business keys, editable fields, recipients, and reprocessing rules are one operating model.</p>
    </header>
    <div class="research-route-list">
      {% for item in aif.setup_sequence %}
      <a href="/labs/enterprise-context/data/aif.json"><span>{{ item.step }}</span><strong>{{ item.title }}</strong><small>{{ item.detail }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="aif-exceptions" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Exception classes</p>
      <h2>Not every red message should be repaired the same way.</h2>
      <p>Data errors, customizing errors, temporary technical failures, code defects, and reconciliation gaps require different owners and actions.</p>
    </header>
    <div class="research-route-list">
      {% for item in aif.exception_types %}
      <a href="/labs/enterprise-context/data/aif.json"><span>ERR</span><strong>{{ item.type }}</strong><small><b>Example:</b> {{ item.example }} <b>Response:</b> {{ item.preferred_response }}</small><i class="material-symbols-outlined" aria-hidden="true">report_problem</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="brfplus-aif" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">BRFplus + AIF</p>
      <h2>One decision can support many interfaces without moving operations into the rule engine.</h2>
      <p>{{ aif.integration_with_brfplus.statement }}</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/data/aif.json"><span>BRF</span><strong>BRFplus owns</strong><small>{{ aif.integration_with_brfplus.design_split.brfplus }}</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      <a href="/labs/enterprise-context/data/aif.json"><span>AIF</span><strong>AIF owns</strong><small>{{ aif.integration_with_brfplus.design_split.aif }}</small><i class="material-symbols-outlined" aria-hidden="true">sync_problem</i></a>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">model_training</span>
    <p><strong>Now add AI:</strong> a model is useful only when a business application can define the scenario, connect the right runtime, operate the lifecycle, consume inference, and decide what action follows.</p>
    <a href="#islm">Open ISLM AI lifecycle <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
  </section>

  <section class="research-canvas__inventory" id="islm" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">ISLM / AI scenario lifecycle</p>
      <h2>{{ islm.title }}</h2>
      <p>{{ islm.memory_model.short_definition }} <strong>Lead view:</strong> {{ islm.memory_model.lead_line }}</p>
    </header>
    <div class="research-route-list">
      {% for item in islm.availability.timeline %}
      <a href="#islm-types"><span>VER</span><strong>{{ item.release }}</strong><small>{{ item.meaning }}</small><i class="material-symbols-outlined" aria-hidden="true">history</i></a>
      {% endfor %}
      <a href="/labs/enterprise-context/data/islm.json"><span>DATA</span><strong>Open structured ISLM topic</strong><small>Scenario types, lifecycle, use cases, heuristics, limits, relations, and assessment cards.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="islm-types" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Embedded or side-by-side</p>
      <h2>The business scenario stays in S/4HANA. The AI runtime can be local or remote.</h2>
      <p>Runtime choice should follow the data, model, latency, lifecycle, and governance needs. “BTP because AI” is not an architecture principle.</p>
    </header>
    <div class="research-route-list">
      {% for item in islm.scenario_types %}
      <a href="/labs/enterprise-context/data/islm.json"><span>TYPE</span><strong>{{ item.title }}</strong><small><b>Runtime:</b> {{ item.runtime }} <b>Best for:</b> {{ item.best_for }} <b>Boundary:</b> {{ item.lead_boundary }}</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="islm-lifecycle" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">ISLM lifecycle</p>
      <h2>Define the business contract before training or calling a model.</h2>
      <p>The lifecycle is more than deploy and activate. It begins with the business event and ends with a measured process outcome.</p>
    </header>
    <div class="research-route-list">
      {% for item in islm.lifecycle_model %}
      <a href="/labs/enterprise-context/data/islm.json"><span>{{ item.step }}</span><strong>{{ item.title }}</strong><small>{{ item.detail }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="islm-use" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Where ISLM fits</p>
      <h2>One lifecycle framework, several AI consumption patterns.</h2>
      <p>Use ISLM when S/4HANA is the business consumer and the AI capability needs a governed scenario contract and lifecycle.</p>
    </header>
    <div class="research-route-list">
      {% for item in islm.use_cases %}
      <a href="/labs/enterprise-context/data/islm.json"><span>USE</span><strong>{{ item.title }}</strong><small>{{ item.problem }} <b>ISLM:</b> {{ item.how_islm_fits }} <b>Boundary:</b> {{ item.lead_boundary }}</small><i class="material-symbols-outlined" aria-hidden="true">neurology</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="islm-design" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">ISLM design review</p>
      <h2>Model lifecycle health is not business value.</h2>
      <p>An active model can still be inaccurate, ignored, expensive, unsafe, or attached to the wrong business action. Green status remains a surprisingly weak strategy.</p>
    </header>
    <div class="research-route-list">
      {% for rule in islm.design_rules %}
      <a href="/labs/enterprise-context/data/islm.json"><span>RULE</span><strong>{{ rule.statement }}</strong><small>{{ rule.questions | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
      {% endfor %}
      {% for item in islm.limitations %}
      <a href="/labs/enterprise-context/data/islm.json"><span>!</span><strong>Boundary</strong><small>{{ item }}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Synthetic cases</p>
      <h2>Run the frameworks through a business outcome.</h2>
      <p>These examples are fictional and exist to test reasoning without pretending a green technical status is the business result.</p>
    </header>
    <div class="research-route-list">
      {% for item in brf.synthetic_examples %}
      <a href="/labs/enterprise-context/data/brfplus.json"><span>BRF</span><strong>{{ item.title }}</strong><small>{{ item.lesson }}</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      {% endfor %}
      <a href="/labs/enterprise-context/data/aif.json"><span>AIF</span><strong>{{ aif.synthetic_example.title }}</strong><small>{{ aif.synthetic_example.lesson }}</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      {% for item in islm.synthetic_examples %}
      <a href="/labs/enterprise-context/data/islm.json"><span>AI</span><strong>{{ item.title }}</strong><small>{{ item.lesson }}</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="assessment" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead assessment</p>
      <h2>Explain ownership and boundaries, not transaction codes.</h2>
      <p>The strongest answer separates decision, execution, transport, monitoring, recovery, AI runtime, inference, and business action.</p>
    </header>
    <div class="research-route-list">
      {% for item in brf.assessment_cards %}
      <a href="/labs/enterprise-context/data/brfplus.json"><span>Q</span><strong>{{ item.question }}</strong><small>{{ item.answer }}</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      {% endfor %}
      {% for item in aif.assessment_cards %}
      <a href="/labs/enterprise-context/data/aif.json"><span>Q</span><strong>{{ item.question }}</strong><small>{{ item.answer }}</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      {% endfor %}
      {% for item in islm.assessment_cards %}
      <a href="/labs/enterprise-context/data/islm.json"><span>Q</span><strong>{{ item.question }}</strong><small>{{ item.answer }}</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="sources" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Primary sources</p>
      <h2>Product facts are checked. The architecture language is independent synthesis.</h2>
      <p>Release-sensitive statements stay tied to a product and release scope instead of becoming timeless folklore.</p>
    </header>
    <div class="research-route-list">
      {% for source in registry.sources %}
      <a href="{{ source.url }}" target="_blank" rel="noopener"><span>SRC</span><strong>{{ source.publisher }} · {{ source.title }}</strong><small>{% if source.release_scope %}{{ source.release_scope }} · {% endif %}{{ source.product_scope }} · checked {{ source.verified_at }}</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>