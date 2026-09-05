---
layout: default
title: "SAP Integration Architecture — Logistics, Events and Data Distribution"
description: "A practical decision map for SAP logistics integration: APIs, IDocs, events, queues, Kafka, files, B2B, Event Mesh, TIBCO, and data distribution."
permalink: /labs/enterprise-context/integrations/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-08-16
hide_global_cta: true
tags:
  - sap
  - integration
  - logistics
  - event-driven-architecture
  - master-data
last_reviewed: 2026-08-16
publication_wave: "logistics-search-wave-01"
review_method: "primary sources + factual review + page-level editorial review"
search_intent: "SAP integration architecture with IDoc, API, events, Event Mesh and Kafka"
# ai-discovery-managed:start
structured_data:
  type: TechArticle
primary_topic: "sap-integration"
ai_sidecar: "/ai/pages/labs--enterprise-context--integrations.json"
semantic_links:
  - type: "used_by"
    title: "SAP Sales Integration Map — IDocs, APIs, Events and Handoffs"
    url: "/labs/enterprise-context/sales-processes/integrations/"
  - type: "integrates_with"
    title: "Integration Operations & Recovery — Enterprise Context Lab"
    url: "/labs/enterprise-context/integration-operations/"
  - type: "integrates_with"
    title: "SAP Development Architecture — RAP, CAP, ABAP Cloud and Clean Core"
    url: "/labs/enterprise-context/development/"
  - type: "deep_dive"
    title: "SAP DRF — Data Replication Framework"
    url: "/labs/enterprise-context/integrations/drf/"
  - type: "deep_dive"
    title: "SAP Data Migration and Controlled Bulk Loading"
    url: "/labs/enterprise-context/integrations/data-migration/"
  - type: "related_topic"
    title: "SAP Decision Cards — Enterprise Context Lab"
    url: "/labs/enterprise-context/decisions/"
source_links:
  - title: "What Is SAP Integration Suite?"
    url: "https://help.sap.com/docs/integration-suite/sap-integration-suite/decide-on-integration-technology"
  - title: "Connectivity Options"
    url: "https://help.sap.com/docs/integration-suite/sap-integration-suite/connectivity-options"
  - title: "Understanding the Basic Concepts"
    url: "https://help.sap.com/docs/integration-suite/sap-integration-suite/understanding-basic-concepts-a81309fbdc4446b98e138a328bf1776c"
  - title: "Trading Partner Management"
    url: "https://help.sap.com/docs/SAP_INTEGRATION_SUITE/sap-integration-suite/trading-partner-management"
  - title: "IDoc Adapter"
    url: "https://help.sap.com/docs/integration-suite/sap-integration-suite/idoc-adapter"
  - title: "Kafka Adapter"
    url: "https://help.sap.com/docs/SAP_INTEGRATION_SUITE/sap-integration-suite/kafka-adapter"
  - title: "What Is SAP Event Mesh?"
    url: "https://help.sap.com/docs/SAP_EM/bf82e6b26456494cbdd197057c09979f/what-is-sap-event-mesh"
  - title: "Event Mesh"
    url: "https://help.sap.com/docs/SAP_INTEGRATION_SUITE/sap-integration-suite/event-mesh"
  - title: "What Is SAP Integration Suite, Advanced Event Mesh?"
    url: "https://help.sap.com/docs/sap-integration-suite/advanced-event-mesh"
  - title: "Event Mesh Bridge"
    url: "https://help.sap.com/docs/integration-suite/sap-integration-suite/event-mesh-bridge"
  - title: "Synchronization of Master Data"
    url: "https://help.sap.com/docs/master-data-integration/sap-master-data-integration-prod/synchronization-of-master-data"
  - title: "Integration Models"
    url: "https://help.sap.com/docs/master-data-integration/sap-master-data-integration-prod/integration-models"
# ai-discovery-managed:end
---
{% assign topic = site.data.labs.enterprise_context.topics.integration_architecture_landscape %}
{% assign language = site.data.labs.enterprise_context.topics.integration_architecture_language %}
{% assign registry = site.data.labs.enterprise_context.sources.integration_registry %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li aria-current="page">Integrations</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise Context Lab / Integration Architecture</p>
      <h1>{{ topic.title }}</h1>
      <p>{{ topic.summary }}</p>
      <a class="research-canvas__button" href="#architecture-stack">Start with the architecture language <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Research status">
      <p>Reviewed architecture</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ topic.interface_types | size }}</strong><small>Interface patterns</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ topic.platforms | size }}</strong><small>Platform views</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ language.terms | size }}</strong><small>Architecture terms</small></div>
      <div class="research-canvas__signal-line"><span>04</span><strong>{{ topic.maturity.gates_complete }}/{{ topic.maturity.gates_total }}</strong><small>Maturity gates</small></div>
      <em>Primary sources reviewed together {{ topic.reviewed_together_at }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">hub</span>
    <p><strong>Problem:</strong> integration discussions often mix business meaning, protocols, brokers, middleware, and products in one sentence.</p>
    <p><strong>Working rule.</strong> First define the business meaning and interaction. Then define the contract, transport, mediation, broker or stream, application owner, and recovery model.</p>
    <a href="/labs/enterprise-context/data/topics.json">Open machine-readable topic data <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
  </section>

  <section class="research-canvas__inventory" id="lead-answer-frame" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead answer frame</p>
      <h2>Explain the dependency before the platform.</h2>
      <p>For an assessment answer, move through the design in a fixed order. A technology name is useful only after the business interaction and failure model are clear.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>01 · Business interaction</h3><p>What business object or event crosses the boundary, who owns it, and does the sender need an immediate answer?</p></div>
      <div><h3>02 · Contract and semantics</h3><p>Define identity, version, required fields, idempotency expectation, ordering need, and what a successful receiver state means.</p></div>
      <div><h3>03 · Delivery pattern</h3><p>Choose synchronous request, asynchronous command, event, queue, stream, file, or B2B exchange from the dependency and operating model.</p></div>
      <div><h3>04 · Platform fit</h3><p>Only now select the SAP or non-SAP runtime, broker, mediation layer, or streaming platform that fits the contract.</p></div>
      <div><h3>05 · Recovery</h3><p>Explain retries, duplicates, replay, ordering, monitoring, dead-letter or error handling, and the owner of recovery.</p></div>
      <div><h3>06 · Business proof</h3><p>Close with reconciliation in the receiving business object. A green transport status is not proof of business completion.</p></div>
    </div>
    <p class="ecg-caption"><strong>Evidence boundary:</strong> reviewed product documentation supports the named platform and interface behavior. The architecture stack, selection sequence, and design heuristics were reviewed as authored reasoning and are intentionally kept separate from vendor product facts.</p>
    <a href="/labs/enterprise-context/integration-operations/">Continue into runtime recovery and reconciliation <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="architecture-stack" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Architecture language</p>
      <h2>Eight layers. Do not mix them.</h2>
      <p>This is the mental model I use before choosing a product. If the first answer is “Kafka”, “CPI”, or “TIBCO”, the discussion started too low in the stack.</p>
    </header>
    <div class="research-route-list">
      {% for item in language.architecture_stack %}
      <a href="#terminology"><span>{{ item.order }}</span><strong>{{ item.layer }}</strong><small>{{ item.question }} <b>Examples:</b> {{ item.examples | join: ", " }}. <b>Lead rule:</b> {{ item.lead_rule }}</small><i class="material-symbols-outlined" aria-hidden="true">layers</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="selection-questions" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Design sequence</p>
      <h2>Twelve questions before middleware.</h2>
      <p>These questions expose coupling, ownership, reliability, and semantics before anyone starts comparing adapters.</p>
    </header>
    <div class="research-route-list">
      {% for question in language.selection_questions %}
      <a href="#integration-rules"><span>?</span><strong>{{ question }}</strong><small>Answer this with a business object and a failure scenario, not only a technology name.</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="terminology" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Terminology</p>
      <h2>One language for integration architecture.</h2>
      <p>A message is not automatically an event. A broker is not an integration runtime. A topic does not mean exactly the same thing in JMS and Kafka. Naming things correctly removes a surprising amount of architecture fog.</p>
    </header>
    <div class="research-route-list">
      {% for item in language.terms %}
      <a href="#not-the-same"><span>TERM</span><strong>{{ item.term }}</strong><small><b>{{ item.category }}</b> · {{ item.definition }} <b>Architect view:</b> {{ item.architect_view }} <b>Example:</b> {{ item.example }}</small><i class="material-symbols-outlined" aria-hidden="true">menu_book</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="not-the-same" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Do not confuse</p>
      <h2>Similar words, different architecture decisions.</h2>
      <p>Most terminology errors are harmless until someone uses them to select a platform. Then they become invoices.</p>
    </header>
    <div class="research-route-list">
      {% for pair in language.not_the_same %}
      <a href="#walkthroughs"><span>≠</span><strong>{{ pair.left }} ≠ {{ pair.right }}</strong><small>{{ pair.distinction }}</small><i class="material-symbols-outlined" aria-hidden="true">difference</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="walkthroughs" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Read the stack end to end</p>
      <h2>Four examples using the same language.</h2>
      <p>The point is not memorizing diagrams. The point is being able to explain every layer of a design consistently.</p>
    </header>
    <div class="research-route-list">
      {% for item in language.walkthroughs %}
      <a href="#interface-patterns"><span>FLOW</span><strong>{{ item.title }}</strong><small>{{ item.business_need }} <b>Path:</b> {{ item.flow }} <b>Meaning:</b> {{ item.language.business_meaning }} · <b>Interaction:</b> {{ item.language.interaction }} · <b>Contract:</b> {{ item.language.contract }} · <b>Transport:</b> {{ item.language.transport }} · <b>Reliability:</b> {{ item.language.reliability }} <b>Architect take:</b> {{ item.architect_take }}</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="integration-rules" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Memory hooks</p>
      <h2>Ten rules before middleware.</h2>
      <p>I use these rules to keep the discussion on coupling, reliability, and business ownership instead of adapter names.</p>
    </header>
    <div class="research-route-list">
      {% for principle in topic.architecture_principles %}
      <a href="#interface-patterns"><span>{{ forloop.index }}</span><strong>{{ principle }}</strong><small>Use this as a design check, then validate the concrete interface contract.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="interface-patterns" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Interface patterns</p>
      <h2>Choose the message meaning first.</h2>
      <p>REST, IDoc, Kafka, JMS, and SFTP are not different spellings of the same thing. Each creates a different dependency between sender and receiver.</p>
    </header>
    <div class="research-route-list">
      {% for interface in topic.interface_types %}
      <a href="#decision-guide"><span>INT</span><strong>{{ interface.title }}</strong><small><b>{{ interface.message_meaning }}</b> · {{ interface.best_for }} <b>Lead rule:</b> {{ interface.lead_rule }}</small><i class="material-symbols-outlined" aria-hidden="true">compare_arrows</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="platform-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Platform map</p>
      <h2>Do not put every middleware product in one bucket.</h2>
      <p>Integration runtimes, brokers, and event-streaming platforms solve different parts of the problem. A mature landscape often uses more than one on purpose.</p>
    </header>
    <div class="research-route-list">
      {% for platform in topic.platforms %}
      <a href="/labs/enterprise-context/data/topics.json"><span>PLT</span><strong>{{ platform.title }}</strong><small><b>{{ platform.platform_type }}</b> · {{ platform.remember }} Best fit: {{ platform.best_fit[0] }} Trade-off: {{ platform.trade_offs[0] }}</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="decision-guide" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Decision guide</p>
      <h2>Start from the dependency you need.</h2>
      <p>The first question is not “Kafka or Event Mesh?” It is “What must the sender know about the receiver, and when?”</p>
    </header>
    <div class="research-route-list">
      {% for decision in topic.decision_guide %}
      <a href="#reliability"><span>→</span><strong>{{ decision.need }}</strong><small><b>{{ decision.primary_pattern }}</b> · {{ decision.preferred_stack }}. {{ decision.why }} <b>Avoid:</b> {{ decision.avoid }}</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="logistics-patterns" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Logistics</p>
      <h2>Apply the same rules to real process boundaries.</h2>
      <p>Sales, purchasing, warehouse, and transportation need different latency and reliability choices, but the design logic stays consistent.</p>
    </header>
    <div class="research-route-list">
      {% for pattern in topic.logistics_patterns %}
      <a href="/labs/enterprise-context/data/topics.json"><span>LOG</span><strong>{{ pattern.title }}</strong><small>{{ pattern.path }} <b>First Lead check:</b> {{ pattern.lead_focus[0] }}</small><i class="material-symbols-outlined" aria-hidden="true">local_shipping</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="master-data" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Data distribution</p>
      <h2>{{ topic.data_distribution.title }}</h2>
      <p>{{ topic.data_distribution.principle }} Governance, replication, synchronization, and protocol mediation are separate jobs.</p>
    </header>
    <div class="research-route-list">
      {% for responsibility in topic.data_distribution.responsibilities %}
      <a href="/labs/enterprise-context/data/topics.json"><span>MD</span><strong>{{ responsibility.title }}</strong><small><b>{{ responsibility.owner_options | join: " / " }}</b> · {{ responsibility.job }} {{ responsibility.rule }}</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Master-data patterns</p>
      <h2>Distribute deliberately, then reconcile.</h2>
      <p>A successful outbound message is not proof that the receiving business object is correct. That small distinction saves large support incidents.</p>
    </header>
    <div class="research-route-list">
      {% for pattern in topic.data_distribution.reference_patterns %}
      <a href="#reliability"><span>PATH</span><strong>{{ pattern.name }}</strong><small>{{ pattern.path }} · Best fit: {{ pattern.best_fit }} <b>Risk:</b> {{ pattern.risk }}</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="reliability" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Reliability</p>
      <h2>Architecture starts where the happy path ends.</h2>
      <p>Retries, duplicates, ordering, replay, reconciliation, and correlation are not production details. They define whether logistics keeps moving when systems disagree.</p>
    </header>
    <div class="research-route-list">
      {% for control in topic.reliability_controls %}
      <a href="/labs/enterprise-context/data/topics.json"><span>CTRL</span><strong>{{ control.title }}</strong><small>{{ control.question }} <b>Design:</b> {{ control.design_hint }}</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="anti-patterns" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Failure modes</p>
      <h2>What I would challenge in a design review.</h2>
      <p>Most integration debt does not start with a bad protocol. It starts with unclear ownership and then gets automated very efficiently.</p>
    </header>
    <div class="research-route-list">
      {% for anti in topic.anti_patterns %}
      <a href="#assessment-cards"><span>!</span><strong>{{ anti.title }}</strong><small>{{ anti.symptom }} {{ anti.why_it_hurts }} <b>Better:</b> {{ anti.better_move }}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="assessment-cards" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead assessment</p>
      <h2>Short answers that show architecture thinking.</h2>
      <p>The goal is not to recite protocols. Explain the boundary, trade-off, failure mode, and why the choice fits the process.</p>
    </header>
    <div class="research-route-list">
      {% for card in topic.assessment_cards %}
      <a href="#sources"><span>Q</span><strong>{{ card.question }}</strong><small>{{ card.answer }}</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="memory-model" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Architect memory model</p>
      <h2>Eight sentences to keep the landscape in your head.</h2>
      <p>If these eight questions stay clear, individual products become much easier to place.</p>
    </header>
    <div class="research-route-list">
      {% for item in language.memory_model %}
      <a href="#sources"><span>{{ forloop.index }}</span><strong>{{ item }}</strong><small>Use this sentence to explain one layer before moving to the next.</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="sources" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Primary sources</p>
      <h2>Facts checked, explanations written independently.</h2>
      <p>Product capabilities and protocol support are linked to current primary documentation. The decision rules, terminology model, and trade-offs are independent architecture synthesis for learning.</p>
    </header>
    <div class="research-route-list">
      {% for source in registry.sources %}
      <a href="{{ source.url }}" target="_blank" rel="noopener"><span>SRC</span><strong>{{ source.publisher }} · {{ source.title }}</strong><small>{{ source.product_scope }} · checked {{ source.verified_at }}</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
