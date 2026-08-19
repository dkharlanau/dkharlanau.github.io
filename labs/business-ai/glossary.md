---
layout: default
title: "Business AI Glossary — Plain Language for Discovery, Architecture, Governance and Delivery"
description: "A plain-English Business AI glossary and language guide connecting workflow, architecture, governance, security evidence, model selection, evaluation, and implementation terms."
permalink: /labs/business-ai/glossary/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-08-19
last_reviewed: 2026-08-19
hide_global_cta: true
publication_wave: "business-ai-glossary-02"
review_method: "cross-framework terminology review across Business AI discovery, architecture, governance, security, model selection, evaluation, and implementation pages"
evidence_review_mode: "authored_heuristic"
search_intent: "Business AI glossary plain language terminology workflow architecture governance security evidence evals guardrails observability blueprint implementation readiness"
structured_data:
  type: TechArticle
tags:
  - business-ai
  - glossary
  - terminology
  - ai-fluency
  - architecture
  - governance
  - security
  - evidence
  - evaluation
  - implementation-readiness
career_impact: mapped
career_skills:
  - ai-readiness
  - ai-business-value
  - ai-security
  - ai-evaluation
  - delivery-lifecycle
# ai-discovery-managed:start
primary_topic: "business-ai"
ai_sidecar: "/ai/pages/labs--business-ai--glossary.json"
semantic_links:
  - type: "parent_context"
    title: "Business AI Lab — Processes, Patterns, Technologies, Evidence"
    url: "/labs/business-ai/"
  - type: "same_domain"
    title: "AI Platform Building Blocks — Capability Roles, Minimum Set and Control Boundaries"
    url: "/labs/business-ai/platform-building-blocks/"
  - type: "same_domain"
    title: "AI Architecture Patterns — From Reusable Shapes to First-Pass Blueprints"
    url: "/labs/business-ai/architecture-patterns/"
  - type: "same_domain"
    title: "AI Governance and Data Boundaries — Ownership, Access, Action Risk and Validation"
    url: "/labs/business-ai/governance-data-boundaries/"
  - type: "same_domain"
    title: "AI Model Selection — Model Classes, Context, Latency, Cost and Evals"
    url: "/labs/business-ai/model-selection/"
  - type: "same_domain"
    title: "AI Implementation Readiness — Evals, Safeguards, Observability, Release and Rollback"
    url: "/labs/business-ai/implementation-readiness/"
  - type: "related_topic"
    title: "AI Ready — Security and Governance"
    url: "/labs/ai-ready/security-governance/"
# ai-discovery-managed:end
---
{% assign glossary = site.data.labs.business_ai.glossary %}
{% assign extension = site.data.labs.business_ai.glossary_extensions %}
{% assign terms = glossary.terms | concat: extension.terms %}
{% assign non_synonyms = glossary.non_synonyms | concat: extension.non_synonyms %}
{% assign writing_rules = glossary.writing_rules | concat: extension.writing_rules %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li aria-current="page">Glossary</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Business AI / language guide</p>
      <h1>One term.<br />One meaning.</h1>
      <p>Business AI becomes harder than it needs to be when the same idea gets a new name on every slide. This glossary keeps the main terms simple and consistent across discovery, architecture, governance, security, model selection, implementation, and assessment answers.</p>
      <a class="research-canvas__button" href="#journey">Open the common language <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Business AI language sequence">
      <p>Common journey</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Discover</strong><small>Problem and workflow</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Shape</strong><small>Capabilities and pattern</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Bound</strong><small>Data and authority</small></div>
      <div class="research-canvas__signal-line"><span>04</span><strong>Choose</strong><small>Model and options</small></div>
      <div class="research-canvas__signal-line"><span>05</span><strong>Prove</strong><small>Evidence and controls</small></div>
      <div class="research-canvas__signal-line"><span>06</span><strong>Release</strong><small>Operate and recover</small></div>
      <em>Use the phase names for the overall journey. Use each framework's local sequence for detailed reasoning inside a phase.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">translate</span>
    <p><strong>Language rule.</strong> {{ glossary.principle }}</p>
    <p><strong>Reader rule.</strong> Prefer plain words before technical labels. Explain the business meaning first, then introduce the technical term if it helps.</p>
    <p><strong>Framework rule.</strong> A term should keep the same meaning when it appears in AI Fluency, architecture, governance, security, model selection, or implementation work.</p>
  </section>

  <section class="research-canvas__inventory" id="journey" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Canonical framework journey</p>
      <h2>Use six phases to connect the Business AI frameworks.</h2>
      <p>The phases give the Lab one shared map. They do not replace the smaller decision sequences inside each page.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Phase</th><th scope="col">Main question</th><th scope="col">Plain meaning</th><th scope="col">Frameworks</th></tr></thead>
        <tbody>
        {% for phase in glossary.journey %}
          <tr>
            <th scope="row">{{ phase.label }}</th>
            <td>{{ phase.question }}</td>
            <td>{{ phase.meaning }}</td>
            <td>{% for page in phase.pages %}<a href="{{ page.url }}">{{ page.title }}</a>{% unless forloop.last %}<br />{% endunless %}{% endfor %}</td>
          </tr>
        {% endfor %}
        </tbody>
      </table>
    </div>
    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">route</span>
      <p><strong>Assessment shortcut:</strong> Discover the work → Shape the solution → Bound the risk → Choose the fit → Prove the behavior → Release with control.</p>
      <p><strong>Security support:</strong> <a href="/labs/ai-ready/security-governance/">Security and Governance</a> deepens the Bound and Prove phases with trust boundaries, authorization, bounded evaluation, evidence levels, and revalidation.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="quick-index" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Quick index</p>
      <h2>Jump to the decision you are trying to make.</h2>
      <p>The glossary is large enough now that scrolling from A to vaguely-near-Z is no longer a serious navigation model.</p>
    </header>
    <div class="research-route-list">
      <a href="#workflow"><span>01</span><strong>Workflow and problem</strong><small>Business problem, workflow, context, owner, evidence, tradeoffs.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="#architecture-pattern"><span>02</span><strong>Solution shape</strong><small>Building blocks, patterns, blueprint, retrieval, tools, orchestration, state.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#action-authority"><span>03</span><strong>Authority and governance</strong><small>Authentication, authorization, access, approval, tool boundaries, safeguards.</small><i class="material-symbols-outlined" aria-hidden="true">policy</i></a>
      <a href="#bounded-evaluation"><span>04</span><strong>Evidence and validation</strong><small>Bounded evaluation, evidence ceiling, source fact, inference, runtime proof, revalidation.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="#model-class"><span>05</span><strong>Model choice</strong><small>Model class, reasoning depth, latency, modality, representative comparison.</small><i class="material-symbols-outlined" aria-hidden="true">tune</i></a>
      <a href="#implementation-readiness"><span>06</span><strong>Release and operation</strong><small>Implementation readiness, release, fallback, rollback, observability, operating owner.</small><i class="material-symbols-outlined" aria-hidden="true">rocket_launch</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="maturity-language" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Recommendation maturity</p>
      <h2>Keep confidence language separate from delivery phases.</h2>
      <p>The six phases describe where the work is happening. Confidence describes how strong the evidence is behind the current recommendation. Mixing the two creates fake certainty surprisingly efficiently.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Preferred term</th><th scope="col">Plain meaning</th><th scope="col">Use when</th></tr></thead>
        <tbody>
          <tr><th scope="row">Preliminary solution path</th><td>A likely direction based on what is currently known.</td><td>The workflow is bounded enough to suggest a route, but important assumptions are still open.</td></tr>
          <tr><th scope="row">Validated architecture</th><td>A solution direction whose important technical assumptions have been tested or confirmed.</td><td>Key data, integration, permission, risk, and quality assumptions have supporting evidence.</td></tr>
          <tr><th scope="row">Deployment-ready implementation plan</th><td>A plan ready for controlled implementation and release planning.</td><td>Requirements, ownership, controls, monitoring, fallback, release, and recovery decisions are defined.</td></tr>
        </tbody>
      </table>
    </div>
    <p>See <a href="/labs/ai-fluency/#confidence-levels">AI Fluency recommendation confidence</a> for the full model.</p>
  </section>

  <section class="research-canvas__inventory" id="uncertainty-language" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Uncertainty language</p>
      <h2>Use four states instead of vague confidence words.</h2>
      <p>These terms make it clear what is known, what is assumed, and who needs to resolve the remaining gap.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">State</th><th scope="col">Plain meaning</th><th scope="col">Lead action</th></tr></thead>
        <tbody>
          <tr><th scope="row">Known</th><td>Supported by current evidence or an accountable owner.</td><td>Use it as an explicit design input.</td></tr>
          <tr><th scope="row"><a href="#assumption">Assumption</a></th><td>A working belief that has not yet been confirmed.</td><td>State it and keep the recommendation conditional.</td></tr>
          <tr><th scope="row"><a href="#validation-need">Validation need</a></th><td>An open question that needs evidence or review.</td><td>Name the evidence, owner, test, or specialist required.</td></tr>
          <tr><th scope="row">Specialist decision</th><td>A decision that belongs to an accountable expert or control function.</td><td><a href="#escalation-question">Escalate a decision-ready question</a> instead of inventing an answer.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="evidence-ladder" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Evidence language</p>
      <h2>Do not let a plausible claim quietly become proof.</h2>
      <p>The same evidence vocabulary used in security review is useful across architecture and implementation work. It makes the claim strength visible before the wording becomes more confident than the facts.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Term</th><th scope="col">What it means</th><th scope="col">Lead use</th></tr></thead>
        <tbody>
          <tr><th scope="row"><a href="#source-fact">Source fact</a></th><td>Directly visible in approved source material.</td><td>Use as the strongest source-level statement.</td></tr>
          <tr><th scope="row"><a href="#supported-inference">Supported inference</a></th><td>A reasonable conclusion drawn from source facts.</td><td>Keep the conclusion conditional when runtime or specialist proof is missing.</td></tr>
          <tr><th scope="row"><a href="#runtime-proof">Runtime proof</a></th><td>Behavior actually observed in explicitly approved runtime testing.</td><td>Limit the claim to the tested path and environment.</td></tr>
          <tr><th scope="row"><a href="#proof-gap">Proof gap</a></th><td>Something important remains unproven.</td><td>Keep the gap visible and define what would close it.</td></tr>
          <tr><th scope="row"><a href="#unsupported-claim">Unsupported claim</a></th><td>The statement goes beyond available evidence.</td><td>Remove, downgrade, or convert it into a validation need.</td></tr>
        </tbody>
      </table>
    </div>
    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">vertical_align_top</span>
      <p><strong><a href="#evidence-ceiling">Evidence ceiling</a>:</strong> agree the highest level of proof the permitted activity can support before a bounded evaluation begins.</p>
      <p>For the detailed security workflow, see <a href="/labs/ai-ready/security-governance/#ai-security-evidence-levels">Security and Governance evidence levels</a>.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="glossary" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Canonical glossary</p>
      <h2>Define the term once. Reuse the meaning everywhere.</h2>
      <p>The definitions below are deliberately plain. Technical depth belongs in the linked framework, not inside the definition.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Term</th><th scope="col">Plain meaning</th><th scope="col">Preferred use</th><th scope="col">Do not confuse with</th><th scope="col">Used in</th></tr></thead>
        <tbody>
        {% for item in terms %}
          <tr id="{{ item.id }}">
            <th scope="row">{{ item.term }}<br /><small>{{ item.group }}</small></th>
            <td>{{ item.plain }}</td>
            <td>{{ item.preferred_use }}</td>
            <td>{{ item.do_not_confuse }}</td>
            <td>{% for page in item.used_in %}<a href="{{ page.url }}">{{ page.title }}</a>{% unless forloop.last %}<br />{% endunless %}{% endfor %}</td>
          </tr>
        {% endfor %}
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="related-terms" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Related terms</p>
      <h2>Follow the decision, not the alphabet.</h2>
      <p>These links show which terms usually belong in the same reasoning chain. They are not synonyms. They are the next concepts worth checking when the first term affects a design or assessment answer.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Start here</th><th scope="col">Then check</th><th scope="col">Why they connect</th></tr></thead>
        <tbody>
        {% for connection in extension.connections %}
          {% assign source_term = terms | where: "id", connection.from | first %}
          <tr>
            <th scope="row"><a href="#{{ source_term.id }}">{{ source_term.term }}</a></th>
            <td>
              {% for target_id in connection.to %}
                {% assign target_term = terms | where: "id", target_id | first %}
                <a href="#{{ target_term.id }}">{{ target_term.term }}</a>{% unless forloop.last %}<br />{% endunless %}
              {% endfor %}
            </td>
            <td>{{ connection.why }}</td>
          </tr>
        {% endfor %}
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="not-synonyms" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Terms that should stay separate</p>
      <h2>Related does not mean interchangeable.</h2>
      <p>These pairs carry different decisions. Blurring them makes architecture and governance language sound simpler while making the actual design less clear, which is a rather expensive bargain.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Term A</th><th scope="col">Term B</th><th scope="col">Rule</th></tr></thead>
        <tbody>
        {% for pair in non_synonyms %}
          <tr><th scope="row">{{ pair.left }}</th><td>{{ pair.right }}</td><td>{{ pair.rule }}</td></tr>
        {% endfor %}
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="writing-rules" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Framework writing contract</p>
      <h2>Use the same language in new and revised Business AI pages.</h2>
      <p>New terms are allowed when they add a new meaning. Renaming an existing idea because a new diagram needs a fresher noun is not a new meaning.</p>
    </header>
    <ol>
      {% for rule in writing_rules %}<li>{{ rule }}</li>{% endfor %}
    </ol>
  </section>

  <section class="research-canvas__inventory" id="framework-links" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Framework map</p>
      <h2>Move from a term to the framework that makes it operational.</h2>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Framework</th><th scope="col">Use it for</th></tr></thead>
        <tbody>
          <tr><th scope="row"><a href="/labs/ai-fluency/">AI Fluency</a></th><td>Workflow discovery, tradeoffs, recommendation confidence, evidence, and early technical judgment.</td></tr>
          <tr><th scope="row"><a href="/labs/business-ai/platform-building-blocks/">Platform Building Blocks</a></th><td>Capability roles, minimum capability set, context, tools, orchestration, and capability obligations.</td></tr>
          <tr><th scope="row"><a href="/labs/business-ai/architecture-patterns/">Architecture Patterns</a></th><td>Reusable solution shapes, first-pass blueprints, retrieval-grounded patterns, orchestration, and blueprint pressure tests.</td></tr>
          <tr><th scope="row"><a href="/labs/business-ai/governance-data-boundaries/">Governance and Data Boundaries</a></th><td>Ownership, approved data use, access, action authority, approval gates, validation needs, and escalation questions.</td></tr>
          <tr><th scope="row"><a href="/labs/ai-ready/security-governance/">Security and Governance</a></th><td>Trust boundaries, prompt injection, authentication, authorization, bounded evaluation, evidence levels, decision quality, remediation, and revalidation.</td></tr>
          <tr><th scope="row"><a href="/labs/business-ai/model-selection/">Model Selection</a></th><td>Model classes, reasoning depth, context, modality, latency, cost, scale, and representative comparison.</td></tr>
          <tr><th scope="row"><a href="/labs/business-ai/implementation-readiness/">Implementation Readiness</a></th><td>Evals, safeguards, observability, release, fallback, rollback, recovery, and operating ownership.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">bookmark</span>
    <p><strong>Working convention:</strong> when a framework introduces one of these terms, keep the glossary meaning. Add detail locally, but do not quietly redefine the term.</p>
    <p><strong>Linking convention:</strong> link the first important use to the exact glossary anchor when the definition helps the reader. A link to <code>/glossary/#authorization</code> is more useful than making the reader rediscover authorization somewhere below forty other nouns.</p>
    <p><strong>Assessment convention:</strong> use the plain definition first. Add technical detail only when the interviewer asks for design depth or when the risk depends on it.</p>
  </section>
</div>
