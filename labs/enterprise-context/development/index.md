---
layout: default
title: "SAP Development Architecture — RAP, CAP, ABAP Cloud and Clean Core"
description: "Architect-level SAP development guide: RAP vs CAP, ABAP Cloud, classic ABAP, CDS, BTP runtimes, side-by-side design and clean-core trade-offs."
permalink: /labs/enterprise-context/development/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-25
hide_global_cta: true
tags:
  - sap
  - abap
  - rap
  - cap
  - cds
  - btp
  - clean-core
  - architecture
last_reviewed: 2026-09-24
publication_wave: "lead-architecture-search-wave-03"
review_method: "primary sources + factual review + page-level editorial review"
search_intent: "SAP clean core development with ABAP Cloud, RAP, CAP and BTP"
# ai-discovery-managed:start
structured_data:
  type: TechArticle
primary_topic: "sap-s4hana"
ai_sidecar: "/ai/pages/labs--enterprise-context--development.json"
semantic_links:
  - type: "prerequisite"
    title: "SAP S/4HANA Deployment Models — Enterprise Context Lab"
    url: "/labs/enterprise-context/deployment-models/"
  - type: "integrates_with"
    title: "SAP Integration Architecture — Logistics, Events and Data Distribution"
    url: "/labs/enterprise-context/integrations/"
  - type: "related_topic"
    title: "Where Should SAP Extension Logic Live? — Clean Core Decision Card"
    url: "/labs/enterprise-context/decisions/clean-core-extension-placement/"
  - type: "related_topic"
    title: "SAP Business AI and AI Platform Landscape — Enterprise Context Lab"
    url: "/labs/enterprise-context/business-ai/"
  - type: "related_topic"
    title: "SAP Decision Cards — Enterprise Context Lab"
    url: "/labs/enterprise-context/decisions/"
  - type: "same_domain"
    title: "SAP Performance and Technical Operations — Practical S/4HANA Troubleshooting"
    url: "/labs/enterprise-context/performance/"
source_links:
  - title: "Extend SAP S/4HANA in the cloud and on premise with ABAP-based extensions"
    url: "https://www.sap.com/documents/2022/10/52e0cd9b-497e-0010-bca6-c68f7e60039b.html"
  - title: "Analyzing Customizations after System Conversion"
    url: "https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-private-edition/analyzing-customizations-after-system-conversion_b9083e6d-e207-4578-8aa6-6c85cb42974a"
  - title: "Adapting Custom Code"
    url: "https://learning.sap.com/courses/practicing-clean-core-extensibility-for-sap-s-4hana-cloud/adapting-custom-code_bc14533d-afca-497f-9924-d6457822f2e3"
  - title: "Using the Custom Code Migration AI Assistant"
    url: "https://help.sap.com/docs/abap-cloud/abap-development-tools-user-guide/using-custom-code-migration-ai-assistant"
  - title: "Exploring Clean Core Extensibility Best Practices"
    url: "https://learning.sap.com/courses/practicing-clean-core-extensibility-for-sap-s-4hana-cloud/explaining-extensibility-model-best-practices_e290f382-800e-40ef-a203-85a13115f487"
  - title: "Clean core extensibility for SAP S/4HANA Cloud"
    url: "https://www.sap.com/documents/2024/09/20aece06-d87e-0010-bca6-c68f7e60039b.html"
  - title: "Key User Extensibility"
    url: "https://help.sap.com/docs/SAP_S4HANA_CLOUD/60a09f68f2444ceca31dcac2e7017945/3ccb50e724b045508fea8b2cf1774b2b.html"
  - title: "Extensibility Inventory"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/b5670aaaa2364a29935f40b16499972d/fcf72df4f7c245f1bfea123dbec0613d.html"
  - title: "Setting Up Adaptation Transport Organizer"
    url: "https://help.sap.com/doc/99af63e17e7b4f15a18e0605cb940de4/750_SP02/en-US/e0feb8ac8c9c43b6a318f76ddc56bd3a.html"
  - title: "Register Extensions for Transport"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_2020/b5670aaaa2364a29935f40b16499972d/00797a9f522b4ab59ed66019110834f3.html"
  - title: "Custom Business Objects"
    url: "https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/b45696ca0d9143cba040797e9c71aa44.html"
  - title: "Extension Architecture Guide"
    url: "https://help.sap.com/doc/1e322967d9ef4d788c4165c9aed88c78/Cloud/en-US/892cd77faccc4c959ca87aa600e40eac.pdf"
# ai-discovery-managed:end
---
{% assign topic = site.data.labs.enterprise_context.topics.development_architecture %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li aria-current="page">Development Architecture</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise Context Lab / Development architecture</p>
      <h1>{{ topic.title }}</h1>
      <p>{{ topic.summary }}</p>
      <a class="research-canvas__button" href="#decision-matrix">Start with the decision <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Development architecture research status">
      <p>Research status</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ topic.building_blocks | size }}</strong><small>Core building blocks</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ topic.decision_matrix | size }}</strong><small>Decision scenarios</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ topic.maturity.gates_complete }}/{{ topic.maturity.gates_total }}</strong><small>Maturity gates</small></div>
      <em>Reviewed together {{ topic.reviewed_together_at }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">architecture</span>
    <p><strong>First rule:</strong> RAP, CAP, CDS, ABAP Objects, BTP and Cloud Foundry are not alternatives at the same level. One is a programming model, another a data model, another a runtime, another a deployment target.</p>
    <p><strong>Architecture starts with coupling:</strong> where is the transaction, where is the data, who owns the lifecycle, and what happens when the network is down?</p>
    <a href="/labs/enterprise-context/data/development.json">Open the AI-readable model <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Architecture thesis</p>
      <h2>Build close to the business boundary, not close to the current fashion.</h2>
      <p>These are working architecture rules, not SAP product slogans.</p>
    </header>
    <div class="research-route-list">
      {% for principle in topic.architecture_thesis %}
      <a href="/labs/enterprise-context/data/development.json"><span>{{ forloop.index }}</span><strong>Decision rule</strong><small>{{ principle }}</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Mental model</p>
      <h2>Separate language, data model, programming model, UI, runtime and tooling.</h2>
      <p>This removes most false comparisons before the architecture discussion even starts.</p>
    </header>
    <div class="research-route-list">
      {% for layer in topic.concept_layers %}
      <a href="/labs/enterprise-context/data/development.json"><span>LAY</span><strong>{{ layer.title }}</strong><small>{{ layer.examples | join: " · " }} — {{ layer.architect_note }}</small><i class="material-symbols-outlined" aria-hidden="true">layers</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Technology map</p>
      <h2>What each building block actually owns.</h2>
      <p>A technology earns a place when its responsibility is clear.</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.building_blocks %}
      <a href="/labs/enterprise-context/data/development.json"><span>DEV</span><strong>{{ item.title }}</strong><small><b>{{ item.role }}</b> Best fit: {{ item.best_fit }} Architect view: {{ item.architect_view }}</small><i class="material-symbols-outlined" aria-hidden="true">code</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="decision-matrix" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Decision matrix</p>
      <h2>If I need to build something, where do I start?</h2>
      <p>Prefer the smallest architecture that keeps the correct transaction and lifecycle boundary.</p>
    </header>
    <div class="research-route-list">
      {% for decision in topic.decision_matrix %}
      <a href="/labs/enterprise-context/data/development.json"><span>→</span><strong>{{ decision.need }}</strong><small><b>Prefer:</b> {{ decision.preferred }} · <b>Fallback:</b> {{ decision.fallback }} · <b>Avoid:</b> {{ decision.avoid }} · {{ decision.why }}</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Extensibility</p>
      <h2>Key user, ABAP Cloud, classic ABAP and side-by-side are different coupling choices.</h2>
      <p>Clean core does not require one answer for every requirement.</p>
    </header>
    <div class="research-route-list">
      {% for model in topic.extension_models %}
      <a href="/labs/enterprise-context/data/development.json"><span>EXT</span><strong>{{ model.title }}</strong><small><b>{{ model.coupling }}</b> · Choose when: {{ model.choose_when }} Lead rule: {{ model.lead_rule }}</small><i class="material-symbols-outlined" aria-hidden="true">extension</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Extension decision flow</p>
      <h2>Do not start with a tool. Start with the boundary.</h2>
      <p>{{ topic.extensibility_decision_flow.principle }}</p>
    </header>
    <div class="ecg-determination-list">
      {% for item in topic.extensibility_decision_flow.questions %}
      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">0{{ item.order }}</div>
        <div class="ecg-determination-card__copy">
          <h3>{{ item.question }}</h3>
          <p><strong>Yes:</strong> {{ item.yes }}</p>
          <p><strong>No:</strong> {{ item.no }}</p>
        </div>
      </article>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">alt_route</span>
    <p><strong>Lead shortcut:</strong> small supported last-mile change → key user. Tight ERP transaction → on-stack ABAP Cloud. External users, cross-system ownership, SaaS, independent scaling or lifecycle → side-by-side on BTP.</p>
    <p><strong>Do not use BTP as camouflage:</strong> if ten lines of local business logic need S/4HANA state in the same transaction, a remote service usually makes the design more fragile, not cleaner.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Key-user toolbox</p>
      <h2>Use in-app extensibility for small supported changes, not for a hidden custom application.</h2>
      <p>{{ topic.key_user_toolbox.rule }}</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.key_user_toolbox.capabilities %}
      <a href="/labs/enterprise-context/data/development.json"><span>KEY</span><strong>{{ item.name }}</strong><small>{{ item.use }}</small><i class="material-symbols-outlined" aria-hidden="true">tune</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Can this app be extended?</p>
      <h2>Check the exact app before promising a key-user extension.</h2>
      <p>Extensibility is exposed by app and business context. Similar apps can support different extension points.</p>
    </header>
    <div class="ecg-determination-list">
      {% for check in topic.key_user_toolbox.app_support_check %}
      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">0{{ forloop.index }}</div>
        <div class="ecg-determination-card__copy"><h3>Verification step</h3><p>{{ check }}</p></div>
      </article>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="functional-consultant-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">ABAP for functional consultants</p>
      <h2>Know how to trace and extend. Do not turn every requirement into custom code.</h2>
      <p>{{ topic.functional_consultant_technical_map.summary }}</p>
      <p>{{ topic.functional_consultant_technical_map.source_boundary }}</p>
    </header>

    <div class="ecg-determination-list">
      {% for item in topic.functional_consultant_technical_map.workflow %}
      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">0{{ item.order }}</div>
        <div class="ecg-determination-card__copy">
          <h3>{{ item.title }}</h3>
          <p><strong>Question:</strong> {{ item.question }}</p>
          <p><strong>Action:</strong> {{ item.action }}</p>
        </div>
      </article>
      {% endfor %}
    </div>

    <div class="research-route-list">
      {% for item in topic.functional_consultant_technical_map.consultant_literacy %}
      <a href="/labs/enterprise-context/development/toolbox/abap-runtime-ui/"><span>ABAP</span><strong>{{ item.name }}</strong><small>{{ item.know }} <b>Lead use:</b> {{ item.lead_use }}</small><i class="material-symbols-outlined" aria-hidden="true">troubleshoot</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Legacy to clean core</p>
      <h2>Translate the intent. Do not migrate the old hook name.</h2>
      <p>Classic exits and BAdIs remain important because inherited ERP and Private Edition systems contain them. For new work, the same business intent should be checked against the current released contract.</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.functional_consultant_technical_map.legacy_to_current %}
      <a href="/labs/enterprise-context/data/development.json"><span>MAP</span><strong>{{ item.legacy }} → {{ item.current }}</strong><small>{{ item.rule }}</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a>
      {% endfor %}
    </div>
    <p class="ecg-lead-lens"><strong>Assessment answer:</strong> {{ topic.functional_consultant_technical_map.assessment_answer }}</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Process maps</p>
      <h2>Technical literacy becomes useful only when it is attached to the business process.</h2>
      <p>Use these routes to see which extension and tracing questions matter in each logistics area.</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.functional_consultant_technical_map.process_routes %}
      <a href="{{ item.route }}"><span>SAP</span><strong>{{ item.process }}</strong><small>{{ item.focus }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_outward</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Current Clean Core model</p>
      <h2>Use Levels A–D. The old Tier 1/2/3 model is now historical.</h2>
      <p>{{ topic.clean_core_levels.principle }} {{ topic.clean_core_levels.classification_rule }}</p>
    </header>
    <div class="ecg-memory-grid">
      {% for item in topic.clean_core_levels.levels %}
      <article class="ecg-memory-card">
        <span>LEVEL {{ item.level }}</span>
        <strong>{{ item.title }}</strong>
        <h3>{{ item.lead_view }}</h3>
        <p>{{ item.meaning }}</p>
      </article>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">history</span>
    <p><strong>Why we still learn Tier 1/2/3:</strong> {{ topic.three_tier_history.why_remember }}</p>
    <p><strong>Current position:</strong> {{ topic.three_tier_history.current_position }}</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Old 3-tier model</p>
      <h2>Useful vocabulary for existing landscapes, but not the current qualification model.</h2>
      <p>Status: {{ topic.three_tier_history.status }}.</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.three_tier_history.tiers %}
      <a href="/labs/enterprise-context/data/development.json"><span>{{ item.tier }}</span><strong>{{ item.tier }}</strong><small>{{ item.meaning }}</small><i class="material-symbols-outlined" aria-hidden="true">history_edu</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Extension governance</p>
      <h2>Building the extension is only half the job.</h2>
      <p>A Lead also needs to know what depends on the extension, how it moves through the landscape, and how it will be retired.</p>
    </header>
    <div class="ecg-memory-grid">
      <article class="ecg-memory-card">
        <span>INV</span>
        <strong>{{ topic.extension_governance.inventory.tool }}</strong>
        <h3>Know the dependency graph before you change the object.</h3>
        <p>{{ topic.extension_governance.inventory.purpose }} {{ topic.extension_governance.inventory.lead_use }}</p>
      </article>
      <article class="ecg-memory-card">
        <span>MOVE</span>
        <strong>Transport is edition-specific</strong>
        <h3>Do not memorize one path for every S/4HANA product.</h3>
        <p>{{ topic.extension_governance.transport.public_cloud }} {{ topic.extension_governance.transport.private_onprem }}</p>
      </article>
      <article class="ecg-memory-card">
        <span>OLD</span>
        <strong>{{ topic.extension_governance.discovery_resource.title }}</strong>
        <h3>Status: {{ topic.extension_governance.discovery_resource.status }}</h3>
        <p>{{ topic.extension_governance.discovery_resource.guidance }}</p>
      </article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Side-by-side toolbox</p>
      <h2>Build outside S/4HANA when independence is part of the requirement.</h2>
      <p>{{ topic.side_by_side_toolbox.principle }}</p>
    </header>
    <div class="research-route-list">
      {% for signal in topic.side_by_side_toolbox.choose_when %}
      <a href="/labs/enterprise-context/data/development.json"><span>BTP</span><strong>Side-by-side signal</strong><small>{{ signal }}</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Low-code and pro-code</p>
      <h2>SAP Build, BAS, CAP and BTP ABAP Environment solve different parts of the stack.</h2>
      <p>Do not confuse the development environment, programming model and runtime.</p>
    </header>
    <div class="ecg-memory-grid">
      {% for item in topic.side_by_side_toolbox.sap_build.components %}
      <article class="ecg-memory-card">
        <span>BUILD</span>
        <strong>{{ item.name }}</strong>
        <h3>{{ item.use }}</h3>
      </article>
      {% endfor %}
      <article class="ecg-memory-card">
        <span>BAS</span>
        <strong>SAP Business Application Studio</strong>
        <h3>{{ topic.side_by_side_toolbox.pro_code.bas }}</h3>
      </article>
      <article class="ecg-memory-card">
        <span>CAP</span>
        <strong>CAP</strong>
        <h3>{{ topic.side_by_side_toolbox.pro_code.cap }}</h3>
      </article>
      <article class="ecg-memory-card">
        <span>ABAP</span>
        <strong>SAP BTP ABAP Environment</strong>
        <h3>{{ topic.side_by_side_toolbox.pro_code.abap }}</h3>
      </article>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">sync_alt</span>
    <p><strong>Architecture boundary:</strong> {{ topic.side_by_side_toolbox.integration_boundary }}</p>
    <p><strong>Cost:</strong> {{ topic.side_by_side_toolbox.cost_warning }}</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Runtime choice</p>
      <h2>On-stack, Cloud Foundry, Kyma or BTP ABAP Environment?</h2>
      <p>The runtime changes networking, operations, scaling and lifecycle. This is where side-by-side architecture becomes real rather than decorative.</p>
    </header>
    <div class="research-route-list">
      {% for runtime in topic.runtime_decisions %}
      <a href="/labs/enterprise-context/data/development.json"><span>RUN</span><strong>{{ runtime.title }}</strong><small><b>Default:</b> {{ runtime.default_stack }} · Best for: {{ runtime.best_for }} · Cost signal: {{ runtime.costs[0] }}</small><i class="material-symbols-outlined" aria-hidden="true">dns</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Clean core in practice</p>
      <h2>{{ topic.clean_core_reality.definition }}</h2>
      <p>{{ topic.clean_core_reality.sap_reality_check }}</p>
    </header>
    <div class="research-route-list">
      {% for rule in topic.clean_core_reality.practical_rules %}
      <a href="/labs/enterprise-context/data/development.json"><span>CORE</span><strong>Practical rule</strong><small>{{ rule }}</small><i class="material-symbols-outlined" aria-hidden="true">verified_user</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Clean code</p>
      <h2>Readable code and upgrade-stable core are separate engineering goals.</h2>
      <p>{{ topic.clean_code_reality.definition }} {{ topic.clean_code_reality.caution }}</p>
    </header>
    <div class="research-route-list">
      {% for practice in topic.clean_code_reality.practices %}
      <a href="/labs/enterprise-context/data/development.json"><span>CODE</span><strong>Engineering practice</strong><small>{{ practice }}</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Side-by-side cost model</p>
      <h2>Independence is useful. It is not free.</h2>
      <p>{{ topic.side_by_side_cost_model.architect_rule }}</p>
    </header>
    <div class="research-route-list">
      {% for cost in topic.side_by_side_cost_model.hidden_costs %}
      <a href="/labs/enterprise-context/data/development.json"><span>$</span><strong>Hidden distributed-systems cost</strong><small>{{ cost }}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Toolchain and languages</p>
      <h2>Know enough to choose and challenge a design.</h2>
      <p>A Lead does not need to be the best developer in every stack. A Lead does need to understand what skills, runtime and lifecycle the choice creates.</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.language_map %}
      <a href="/labs/enterprise-context/data/development.json"><span>{{ item.priority_for_sap_lead }}</span><strong>{{ item.language }}</strong><small>{{ item.learn_for }}</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Custom code migration</p>
      <h2>Retire before you adapt.</h2>
      <p>{{ topic.custom_code_migration.boundary }} {{ topic.custom_code_migration.lead_rule }}</p>
    </header>
    <div class="ecg-determination-list">
      {% for step in topic.custom_code_migration.flow %}
      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">0{{ step.order }}</div>
        <div class="ecg-determination-card__copy">
          <h3>{{ step.title }}</h3>
          <p>{{ step.action }}</p>
          <p><strong>Output:</strong> {{ step.output }}</p>
        </div>
      </article>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">database</span>
    <p><strong>Simplification Database:</strong> {{ topic.custom_code_migration.simplification_database.role }}</p>
    <p><strong>Lead view:</strong> {{ topic.custom_code_migration.simplification_database.lead_view }}</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Migration toolbox</p>
      <h2>The tools cover different points in the conversion lifecycle.</h2>
      <p>Do not reduce custom code migration to one ATC run.</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.custom_code_migration.tools %}
      <a href="/labs/enterprise-context/data/development.json"><span>CODE</span><strong>{{ item.name }}</strong><small>{{ item.use }}</small><i class="material-symbols-outlined" aria-hidden="true">construction</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">smart_toy</span>
    <p><strong>{{ topic.custom_code_migration.ai_assistant.tool }}:</strong> {{ topic.custom_code_migration.ai_assistant.value }}</p>
    <p><strong>Boundary:</strong> {{ topic.custom_code_migration.ai_assistant.lead_boundary }}</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Architecture smells</p>
      <h2>Patterns that look modern and age badly.</h2>
      <p>Most bad architecture is not technically impossible. That is the problem.</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.anti_patterns %}
      <a href="/labs/enterprise-context/data/development.json"><span>!</span><strong>{{ item.name }}</strong><small>{{ item.smell }} Correction: {{ item.correction }}</small><i class="material-symbols-outlined" aria-hidden="true">report_problem</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead assessment</p>
      <h2>Answers should expose the trade-off, not recite the product catalog.</h2>
      <p>These are compact interview answers. The reasoning behind them is in the model above.</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.lead_assessment_answers %}
      <a href="/labs/enterprise-context/data/development.json"><span>Q</span><strong>{{ item.question }}</strong><small>{{ item.answer }}</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
