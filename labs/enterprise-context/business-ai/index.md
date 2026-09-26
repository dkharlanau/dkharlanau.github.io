---
layout: default
title: "SAP Business AI and AI Platform Landscape — Enterprise Context Lab"
description: "A compact map of SAP Business AI, Joule, agents, Joule Studio, AI Core, AI Launchpad, generative AI hub, grounding, and governance."
permalink: /labs/enterprise-context/business-ai/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-26
hide_global_cta: true
tags:
  - sap
  - business-ai
  - joule
  - btp
  - architecture
last_reviewed: 2026-09-26
publication_wave: "lead-architecture-search-wave-03"
review_method: "primary sources + factual review + ISLM architecture boundary review + page-level editorial review"
search_intent: "SAP Business AI architecture with Joule, agents and SAP data grounding"
# ai-discovery-managed:start
structured_data:
  type: TechArticle
primary_topic: "sap-business-ai"
ai_sidecar: "/ai/pages/labs--enterprise-context--business-ai.json"
entity_mentions:
  - "business-ai"
semantic_links:
  - type: "deep_dive"
    title: "Enterprise Agent Architecture — Tools, Identity, Autonomy and Governance"
    url: "/labs/enterprise-context/business-ai/agents/"
  - type: "integrates_with"
    title: "SAP Integration Architecture — Logistics, Events and Data Distribution"
    url: "/labs/enterprise-context/integrations/"
  - type: "related_topic"
    title: "SAP Decision Cards — Enterprise Context Lab"
    url: "/labs/enterprise-context/decisions/"
  - type: "related_topic"
    title: "Where Should SAP Extension Logic Live? — Clean Core Decision Card"
    url: "/labs/enterprise-context/decisions/clean-core-extension-placement/"
  - type: "related_topic"
    title: "SAP Development Architecture — RAP, CAP, ABAP Cloud and Clean Core"
    url: "/labs/enterprise-context/development/"
  - type: "integrates_with"
    title: "IDoc, API, or Event? — SAP Integration Decision Card"
    url: "/labs/enterprise-context/decisions/idoc-api-event/"
source_links:
  - title: "SAP Business AI"
    url: "https://www.sap.com/products/artificial-intelligence.html"
  - title: "SAP Business AI Platform"
    url: "https://www.sap.com/products/ai-platform.html"
  - title: "SAP Business AI Packages and Pricing"
    url: "https://www.sap.com/products/artificial-intelligence/pricing.html"
  - title: "What Is Joule?"
    url: "https://help.sap.com/docs/joule/serviceguide/what-is-joule"
  - title: "Joule Agents and Joule Assistants"
    url: "https://www.sap.com/products/artificial-intelligence/ai-agents.html"
  - title: "What Is Joule Studio?"
    url: "https://help.sap.com/docs/Joule_Studio/45f9d2b8914b4f0ba731570ff9a85313/7d6dc3e0d59d43e48f4d7ece55e4c2a3.html"
  - title: "Joule Studio Initial Setup and Prerequisites"
    url: "https://help.sap.com/docs/joule-studio-classic/joule-studio-classic-edition/initial-setup-and-prerequisites"
  - title: "AI Foundation"
    url: "https://www.sap.com/products/artificial-intelligence/ai-foundation-os.html"
  - title: "What Is SAP AI Core?"
    url: "https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/sap-ai-core-overview"
  - title: "SAP AI Core Service Plans"
    url: "https://help.sap.com/docs/ai-core/ai-core/service-plans"
  - title: "Metering and Pricing for SAP AI Core"
    url: "https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/metering-and-pricing-for-sap-ai-core"
  - title: "What Is SAP AI Launchpad?"
    url: "https://help.sap.com/docs/ai-launchpad/sap-ai-launchpad/what-is-sap-ai-launchpad"
# ai-discovery-managed:end
---
{% assign topic = site.data.labs.enterprise_context.topics.business_ai_platform_landscape %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li aria-current="page">Business AI</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise Context Lab / Business AI</p>
      <h1>{{ topic.title }}</h1>
      <p>{{ topic.summary }}</p>
      <a class="research-canvas__button" href="#ai-lead-decision">Start with the AI decision <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Review status">
      <p>Research status</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ topic.maturity.gates_complete }}/{{ topic.maturity.gates_total }}</strong><small>Maturity gates</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ topic.layers | size }}</strong><small>AI layers</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ topic.components | size }}</strong><small>Components</small></div>
      <em>Last reviewed together {{ topic.reviewed_together_at }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">psychology</span>
    <p><strong>Problem:</strong> SAP Business AI names overlap, so architecture responsibilities are easy to mix up.</p>
    <p><strong>Remember:</strong> use AI, build AI, run AI, ground AI, and govern AI. Keep these responsibilities separate.</p>
    <a href="/labs/enterprise-context/deployment-models/">Compare S/4HANA deployment models <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="ai-lead-decision" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead decision model</p>
      <h2>First decide whether AI should own this step at all.</h2>
      <p>Product names come later. Start with the business decision, the acceptable error, the evidence the system may use, and the consequence of an action. A deterministic rule, workflow, API, search, or report is often a better design when the path is already known.</p>
    </header>

    <div class="ecg-decision-columns">
      <div>
        <h3>1. What is uncertain?</h3>
        <p>Name the part that needs interpretation, prediction, generation, or dynamic reasoning. If the expected result can be described as a stable rule, do not add AI only because it is available.</p>
      </div>
      <div>
        <h3>2. What is the source of truth?</h3>
        <p>Define which SAP and non-SAP data may ground the answer, who owns that data, how fresh it must be, and which authorizations must still apply.</p>
      </div>
      <div>
        <h3>3. What may the AI do?</h3>
        <p>Separate read, recommend, prepare, and execute. A system that proposes a purchase-order change has a different risk boundary from one that posts the change automatically.</p>
      </div>
      <div>
        <h3>4. How do we know it is good?</h3>
        <p>Define business evaluation before rollout: correctness, missed cases, harmful actions, latency, cost, traceability, and the fallback when confidence or required evidence is insufficient.</p>
      </div>
      <div>
        <h3>5. Who owns failure?</h3>
        <p>Monitoring model calls is not enough. Define who investigates wrong business outcomes, how actions are traced to evidence and tool calls, and how the process continues when the AI path is unavailable.</p>
      </div>
    </div>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">record_voice_over</span>
      <p><strong>60-second answer:</strong> “I do not start with Joule, AI Core, or an agent. I start with the business job and decide whether the uncertain part really needs AI. Then I define the source of truth and authorization boundary, choose whether the AI may read, recommend, or act, and set an evaluation and fallback. Only after that do I map the responsibility to the SAP AI component that owns it. For transactional use, I also require tool contracts, identity, observability, and proof of the resulting business state.”</p>
    </div>

    <div class="ecg-decision-columns">
      <div>
        <h3>Quality vs latency and cost</h3>
        <p>More context, larger models, and extra reasoning steps can improve some tasks but increase response time and runtime cost. Measure the business outcome rather than optimizing one technical metric.</p>
      </div>
      <div>
        <h3>Autonomy vs control</h3>
        <p>More autonomous execution can remove manual work, but it also increases the consequence of a wrong interpretation or tool call.</p>
      </div>
      <div>
        <h3>Broad context vs data minimization</h3>
        <p>More data can improve relevance while expanding authorization, privacy, and governance scope. Give the AI the evidence it needs, not every object it can technically reach.</p>
      </div>
      <div>
        <h3>Flexible agent vs deterministic automation</h3>
        <p>Agents are useful when the path must adapt. Stable repetitive flows are usually easier to test and operate as rules, workflows, APIs, or conventional automation.</p>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="ai-layers" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">AI layers</p>
      <h2>Start with the job, not the product name.</h2>
      <p>Each layer answers one question: use, act, build, run, ground, or govern.</p>
    </header>
    <div class="research-route-list">
      {% for layer in topic.layers %}
      <a href="#components"><span>AI</span><strong>{{ layer.title }}</strong><small>{{ layer.purpose }}</small><i class="material-symbols-outlined" aria-hidden="true">layers</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="components" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Components</p>
      <h2>One component, one memory hook.</h2>
      <p>Use the short line first. Open the SAP source when you need the deeper detail.</p>
    </header>
    <div class="research-route-list">
      {% for component in topic.components %}
      <a href="{{ component.official_docs_url }}" target="_blank" rel="noopener"><span>{% if component.type == 'ai_asset' %}AI{% else %}PLT{% endif %}</span><strong>{{ component.title }}</strong><small><b>{% if component.remember %}{{ component.remember }}{% else %}{{ component.architecture_role }}{% endif %}</b> {{ component.description }}</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="islm" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">S/4HANA machine learning lifecycle</p>
      <h2>{{ topic.s4hana_islm.title }}</h2>
      <p>{{ topic.s4hana_islm.summary }}</p>
    </header>
    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">memory</span>
      <p><strong>{{ topic.s4hana_islm.memory_rule }}</strong></p>
      <p>{{ topic.s4hana_islm.boundary }}</p>
    </div>
    <div class="ecg-memory-grid">
      {% for scenario in topic.s4hana_islm.scenario_types %}
      <article class="ecg-memory-card">
        <span>{{ scenario.type | upcase }}</span>
        <strong>{{ scenario.memory }}</strong>
        <h3>{{ scenario.architecture }}</h3>
        <p><strong>Runtime:</strong> {{ scenario.runtime }}</p>
        <p><strong>Fit:</strong> {{ scenario.fit }}</p>
      </article>
      {% endfor %}
    </div>
    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">psychology</span>
      <p><strong>Lead question:</strong> {{ topic.s4hana_islm.lead_question }}</p>
      <a href="https://help.sap.com/docs/PRODUCT_ID/7989a582039547ae91d8f483e487058d/1674e0ba8d3f4da7a2e0490111c59044.html" target="_blank" rel="noopener">SAP Help: Intelligent Scenarios in ISLM <span class="material-symbols-outlined" aria-hidden="true">open_in_new</span></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Decision guide</p>
      <h2>Which component owns the job?</h2>
      <p>Several components can work together. Pick the primary owner for the responsibility.</p>
    </header>
    <div class="research-route-list">
      {% for decision in topic.decision_guide %}
      {% assign selected = nil %}
      {% for component in topic.components %}{% if component.id == decision.primary_choice %}{% assign selected = component %}{% endif %}{% endfor %}
      <a href="{% if selected %}{{ selected.official_docs_url }}{% else %}/labs/enterprise-context/data/topics.json{% endif %}" target="_blank" rel="noopener"><span>→</span><strong>{{ decision.need }}</strong><small>{% if selected %}{{ selected.title }} · {% endif %}{{ decision.why }}</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Boundaries</p>
      <h2>Do not make one component the whole AI stack.</h2>
      <p>Joule is not AI Core. AI Core is not the Generative AI Hub. Joule Studio is not Integration Suite.</p>
    </header>
    <div class="research-route-list">
      {% for component in topic.components %}
      <a href="{{ component.official_docs_url }}" target="_blank" rel="noopener"><span>!</span><strong>{{ component.title }}</strong><small>{{ component.not_for }}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Licensing signals</p>
      <h2>Check the service you actually use.</h2>
      <p>Licensing can come from Joule, SAP Build, BTP services, AI Units, model usage, data services, and application rights.</p>
    </header>
    <div class="research-route-list">
      {% for component in topic.components %}
      <a href="{{ component.official_commercial_url }}" target="_blank" rel="noopener"><span>LIC</span><strong>{{ component.title }}</strong><small>{{ component.licensing.commercial_model }}{% if component.licensing.metric %} · {{ component.licensing.metric }}{% endif %}</small><i class="material-symbols-outlined" aria-hidden="true">contract</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Reference patterns</p>
      <h2>Typical combinations.</h2>
      <p>Use the pattern to remember ownership. Validate APIs, authorization, grounding, and evaluation separately.</p>
    </header>
    <div class="research-route-list">
      {% for pattern in topic.reference_patterns %}
      <a href="/labs/enterprise-context/data/topics.json"><span>PATH</span><strong>{{ pattern.name }}</strong><small>{{ pattern.path }}</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
