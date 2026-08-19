---
layout: default
title: "Business AI Lab — Processes, Patterns, Technologies, Evidence"
description: "An enterprise-wide Business AI map linking processes, reusable patterns, technology families, implementation outcomes, failures, and evidence."
permalink: /labs/business-ai/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-08-19
hide_global_cta: true
tags:
  - business-ai
  - enterprise-ai
  - processes
  - technologies
  - architecture
last_reviewed: 2026-08-16
publication_wave: "public-framework-search-wave-04"
review_method: "selective external evidence + page-level editorial review + authored heuristic boundary"
evidence_review_mode: "selective_or_heuristic"
search_intent: "enterprise Business AI patterns, technologies, controls and implementation evidence"
# ai-discovery-managed:start
structured_data:
  type: TechArticle
primary_topic: "business-ai"
ai_sidecar: "/ai/pages/labs--business-ai.json"
semantic_links:
  - type: "deep_dive"
    title: "Document-to-ERP AI Pilot — From PDF to Controlled Transaction"
    url: "/labs/business-ai/document-to-erp-ai/"
  - type: "deep_dive"
    title: "ERP Agent Gateway Pilot — Safe AI Tool Access to Enterprise Systems"
    url: "/labs/business-ai/erp-agent-gateway/"
  - type: "deep_dive"
    title: "Open Enterprise AI Research — ERP Evidence, Safety, and Readiness"
    url: "/labs/business-ai/open-research/"
  - type: "deep_dive"
    title: "Open Enterprise AI Pilots — ERP, Documents, Agents, and Controls"
    url: "/labs/business-ai/pilots/"
  - type: "related_topic"
    title: "SAP Business AI and AI Platform Landscape — Enterprise Context Lab"
    url: "/labs/enterprise-context/business-ai/"
  - type: "related_topic"
    title: "Enterprise Agent Architecture — Tools, Identity, Autonomy and Governance"
    url: "/labs/enterprise-context/business-ai/agents/"
# ai-discovery-managed:end
---
{% assign catalog = site.data.labs.business_ai.catalog %}
{% assign expansion = site.data.labs.business_ai.expansion_2026_08_15 %}
{% assign expansion_b = site.data.labs.business_ai.expansion_2026_08_15_b %}
{% assign expansion_c = site.data.labs.business_ai.expansion_2026_08_15_c %}
{% assign domain_map = site.data.labs.business_ai.domain_map %}
{% assign process_map = site.data.labs.business_ai.process_map %}
{% assign tech = site.data.labs.business_ai.technology_landscape %}
{% assign scenario_library = site.data.labs.business_ai.scenario_library %}
{% assign assessment_matrix = site.data.labs.business_ai.assessment_matrix %}
{% assign all_patterns = catalog.patterns | concat: expansion.patterns | concat: expansion_b.patterns | concat: expansion_c.patterns %}
{% assign all_cases = catalog.cases | concat: expansion.cases | concat: expansion_b.cases %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li aria-current="page">Business AI</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Lab 03 / Business AI</p>
      <h1>Process first.<br />Pattern second. Technology third.</h1>
      <p>This lab maps Business AI across the enterprise. It starts from business work and decisions, connects them to reusable AI patterns, compares technology families and platforms, and keeps both successful and failed implementation evidence attached.</p>
      <a class="research-canvas__button" href="#business-ai-map">Open the map <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Business AI catalog status">
      <p>Current catalog</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ process_map.processes | size }}</strong><small>End-to-end processes</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ all_patterns | size }}</strong><small>Reusable patterns</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ scenario_library.scenarios | size }}</strong><small>Outcome scenarios</small></div>
      <em>{{ domain_map.domains | size }} domains, {{ tech.families | size }} technology families, {{ assessment_matrix.profiles | size }} assessment profiles, and {{ all_cases | size }} implementation cases are linked to the map.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <p><strong>Problem:</strong> enterprise AI discussions often start with a vendor or model and only later ask which business process should improve.</p>
    <p><strong>Context:</strong> this lab covers corporate scenarios across commercial, supply-chain, manufacturing, finance, people, service, IT, legal, data, and knowledge processes. Failed pilots and bad outcomes are part of the evidence model, not an embarrassing appendix.</p>
    <p><strong>Working rule.</strong> A model or platform name is metadata, not a use case. First define the process step, business job, system boundary, KPI, cost of error, and control model.</p>
    <a href="/labs/business-ai/processes/">Start from end-to-end processes <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="ai-opportunity-qualification" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Opportunity qualification</p>
      <h2>Start with the problem. Increase confidence with evidence.</h2>
      <p>Strong AI opportunities begin with a customer problem, workflow challenge, or operational constraint. Customers often describe a possible solution before they have clearly described the problem. That is normal. The useful move is to understand the work behind the request before judging the AI idea.</p>
    </header>

    <div class="ecg-decision-columns">
      <div>
        <h3>Translate interest into evidence</h3>
        <p>Strong AI opportunities become visible through business evidence, not through interest in AI alone.</p>
        <p>Instead of asking <em>“Does this customer want AI?”</em>, ask:</p>
        <ul>
          <li>What business problem or decision needs to improve?</li>
          <li>Where does the problem appear in the process or workflow?</li>
          <li>Who performs the work, makes the decision, or owns the outcome?</li>
          <li>What data and business context are available?</li>
          <li>Why is AI suitable here instead of standard automation or process redesign?</li>
          <li>What measurable value could the use case create?</li>
          <li>What risks, controls, or human approvals are required?</li>
          <li>Has the customer agreed to validate the use case through a workshop, prototype, pilot, or another meaningful next step?</li>
        </ul>
      </div>
      <div>
        <h3>Qualification chain</h3>
        <p>A strong AI opportunity connects <strong>business problem → workflow → owner → data → AI capability → measurable value → controlled validation</strong>.</p>
        <p>This keeps the conversation grounded in a business outcome. AI is a possible capability inside the solution, not the starting requirement.</p>
      </div>
    </div>

    <div class="research-canvas__table-wrap">
      <h3>Example: “AI for contract review”</h3>
      <p>The customer is not simply asking for AI for contract review. The request describes a workflow problem that can be made more concrete.</p>
      <table>
        <thead><tr><th scope="col">Problem</th><th scope="col">Description</th></tr></thead>
        <tbody>
          <tr><th scope="row">Workflow</th><td>Reviewers identify and assess clauses across different contract types.</td></tr>
          <tr><th scope="row">Pain</th><td>Reviews take too long, and similar contracts are assessed inconsistently.</td></tr>
          <tr><th scope="row">Owner</th><td>The Head of Legal Operations owns the process.</td></tr>
          <tr><th scope="row">Reason to act</th><td>Delays affect business stakeholders, and the team wants more consistent review.</td></tr>
          <tr><th scope="row">Boundary</th><td>Human oversight still matters because legal decisions require review and accountability.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="research-canvas__table-wrap">
      <h3>Opportunity states</h3>
      <p>Use these stages to describe how much confidence the available evidence supports. The important question is not how excited the customer sounds. It is how much is actually known.</p>
      <table>
        <thead><tr><th scope="col">Opportunity state</th><th scope="col">What it means</th><th scope="col">What is usually known</th></tr></thead>
        <tbody>
          <tr><th scope="row">Lead</th><td>The earliest indication that a potential AI opportunity may exist.</td><td>There is customer interest or a possible problem area, but the opportunity is not yet clear.</td></tr>
          <tr><th scope="row">Stage 0</th><td>Structured validation of whether the opportunity is real and ready to progress.</td><td>The problem is becoming more specific, a plausible use case is emerging, and stakeholders or next steps are becoming visible.</td></tr>
          <tr><th scope="row">Stage 1</th><td>The opportunity has enough evidence to justify deeper joint work.</td><td>The customer problem, relevant stakeholders, reason AI may be worth exploring, and justified next steps are clear enough to support structured opportunity development.</td></tr>
        </tbody>
      </table>
      <p>A Lead can come from a customer conversation, event, referral, outreach, or inbound interest. It may be worth exploring, but it usually needs more discovery before anyone can judge whether there is a real opportunity.</p>
    </div>

    <div class="ecg-decision-columns">
      <div>
        <h3>Evidence that builds confidence</h3>
        <p>As the opportunity progresses, look for evidence that answers a few practical questions:</p>
        <ul>
          <li>Is the customer problem clear?</li>
          <li>Is the workflow understood?</li>
          <li>Are relevant stakeholders visible?</li>
          <li>Is there a plausible direction to explore?</li>
        </ul>
      </div>
      <div>
        <h3>Business problem clarity</h3>
        <p>Problem clarity exists when the customer can describe a specific operational challenge that is important enough to investigate.</p>
        <p>Try to understand:</p>
        <ul>
          <li>What is happening today?</li>
          <li>Who is affected by the problem?</li>
          <li>What is the impact on time, cost, risk, speed, quality, or customer experience?</li>
          <li>What would a better outcome look like?</li>
        </ul>
      </div>
    </div>

    <div class="research-canvas__table-wrap">
      <h3>Stakeholder discovery</h3>
      <p>Once a workflow problem begins to take shape, discovery needs to clarify who is connected to it. Different stakeholders often experience the same workflow in different ways: one group may carry the daily burden, another may own the business result, and another may influence whether a future change can move forward.</p>
      <p>Stakeholder discovery helps identify who experiences the pain, who owns the outcome, who influences decisions, who needs to support validation, and who cares about adoption, approval, risk, or success measures. Opportunities become easier to validate when this ownership is visible.</p>
      <table>
        <thead><tr><th scope="col">Stakeholder type</th><th scope="col">What they usually tell you</th><th scope="col">Why they matter</th></tr></thead>
        <tbody>
          <tr><th scope="row">Affected users</th><td>What the work feels like day to day, where friction appears, and which exceptions make the workflow harder.</td><td>They reveal practical workflow friction and provide current-state evidence.</td></tr>
          <tr><th scope="row">Outcome owner</th><td>What business result needs to improve, such as turnaround time, quality, risk, cost, or service.</td><td>They help validate priority, accountability, and what success should mean.</td></tr>
          <tr><th scope="row">Influencers</th><td>What constraints, approvals, dependencies, or risks may affect progress.</td><td>They help identify what could block, shape, validate, or govern the opportunity. This may include IT, security, procurement, legal, compliance, or other control teams.</td></tr>
          <tr><th scope="row">Executive sponsor or senior stakeholder</th><td>Why the issue matters at a broader business level and how it connects to wider priorities.</td><td>They can create urgency, visibility, sponsorship, or access to the people needed for progress.</td></tr>
        </tbody>
      </table>
      <p>An interested contact is still useful, but interest alone is weak evidence if that person does not experience the pain, own the outcome, influence a decision, or provide a path to the people who do.</p>
    </div>

    <div class="ecg-decision-columns">
      <div>
        <h3>Identifying the outcome owner</h3>
        <p>An outcome owner is the person accountable for improving the workflow or business result. They may be a team lead, department head, process owner, or business sponsor.</p>
        <p>The outcome owner may not perform the work every day. Their role is to connect the workflow problem to a result that matters and help judge whether improving it is a real priority.</p>
      </div>
      <div>
        <h3>Questions that reveal ownership</h3>
        <ul>
          <li>Who is accountable for the current workflow result?</li>
          <li>Who is measured on the outcome that should improve?</li>
          <li>Who can decide that the problem deserves deeper validation?</li>
          <li>Who needs to agree on success measures or acceptable boundaries?</li>
        </ul>
      </div>
    </div>

    <div class="ecg-decision-columns">
      <div>
        <h3>Customer commitment</h3>
        <p>Customer commitment means the customer has shown credible willingness to keep moving. It is stronger when the customer contributes time, access, evidence, people, or decisions rather than only expressing interest.</p>
        <p>Useful signals include:</p>
        <ul>
          <li>Agreeing to a specific discovery workshop, validation session, prototype, or pilot.</li>
          <li>Bringing the workflow owner, operators, or required control teams into the discussion.</li>
          <li>Sharing approved process examples, requirements, data samples, or current-state evidence.</li>
          <li>Helping define success criteria, constraints, ownership, and a next decision point.</li>
        </ul>
      </div>
      <div>
        <h3>Do not confuse interest with movement</h3>
        <p>A curious contact can open the door, but the opportunity becomes stronger when there is a path from interest to the people, evidence, and decisions required to validate it.</p>
        <p>Commitment does not prove that AI is the right solution. It shows that the customer is willing to do the work required to find out.</p>
      </div>
    </div>

    <div class="ecg-decision-columns">
      <div>
        <h3>Keep discovery useful</h3>
        <p>A good discovery conversation feels like joint problem-solving, not a product pitch or a checklist interview.</p>
        <ul>
          <li><strong>Ask before prescribing.</strong> Understand the work before suggesting a solution.</li>
          <li><strong>Stay close to the workflow.</strong> Follow tasks, decisions, handoffs, and outcomes rather than product labels.</li>
          <li><strong>Check the evidence.</strong> Separate what the customer knows from what still needs validation.</li>
          <li><strong>Build the picture together.</strong> Use questions to create shared clarity, not to test the customer.</li>
        </ul>
      </div>
      <div>
        <h3>Signs the opportunity is ready to move</h3>
        <p>Readiness becomes visible through action. Look for a combination of:</p>
        <ul>
          <li>A named owner and a problem that can be explained clearly.</li>
          <li>The right users and decision-makers joining the discussion.</li>
          <li>Enough workflow detail to define a realistic validation scope.</li>
          <li>Customer willingness to share approved examples, context, or process evidence.</li>
          <li>A concrete validation activity or next meeting with the people needed to make progress.</li>
        </ul>
        <p>No single signal is enough. Together, they show whether the opportunity is becoming testable rather than simply interesting.</p>
      </div>
    </div>

    <div class="research-canvas__table-wrap">
      <h3>Watch for red flags</h3>
      <p>Red flags do not always mean the opportunity should stop. They show where discovery is too weak, too broad, or too risky to support the next decision.</p>
      <table>
        <thead><tr><th scope="col">Red flag area</th><th scope="col">What it may sound like</th><th scope="col">Why it matters</th></tr></thead>
        <tbody>
          <tr><th scope="row">Unclear problem definition</th><td><em>“We want to do something with AI.”</em></td><td>The problem is vague, and the partner may end up defining the customer’s problem for them.</td></tr>
          <tr><th scope="row">Workflow uncertainty</th><td><em>“We need an AI assistant.”</em></td><td>The label does not explain which workflow changes, who uses it, or what output improves.</td></tr>
          <tr><th scope="row">Unclear ownership</th><td><em>“One contact is interested, but they do not own the process.”</em></td><td>The opportunity may stall if no operator, outcome owner, or sponsor path is visible.</td></tr>
          <tr><th scope="row">Sensitive workflow without boundaries</th><td><em>“We want AI for compliance decisions.”</em></td><td>The workflow may need clear ownership, oversight, approval paths, and validation boundaries before it can progress.</td></tr>
          <tr><th scope="row">No customer commitment</th><td><em>“Let’s check back later.”</em></td><td>Without a credible next step, there may not be enough engagement to move forward.</td></tr>
          <tr><th scope="row">Value is implied but not stated</th><td><em>“AI should improve the business somehow.”</em></td><td>The opportunity lacks a testable reason to act.</td></tr>
          <tr><th scope="row">First use case is too broad or risky</th><td><em>“We want AI to transform the whole compliance process.”</em></td><td>Early validation needs a bounded workflow, owner, and approval path.</td></tr>
          <tr><th scope="row">Stakeholders cannot support validation</th><td><em>“No one can join a discovery session or share workflow details.”</em></td><td>Without participation, the opportunity cannot build credible evidence.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="ecg-decision-columns">
      <div>
        <h3>Create clarity through discovery</h3>
        <p>Strong discovery helps the customer move from broad statements to specific evidence. Do not accept <em>“we need AI”</em> as a complete requirement. Help the customer explain the workflow, pain, people involved, business impact, and next validation step.</p>
        <p>Effective discovery should answer:</p>
        <ul>
          <li>What problem is the customer trying to solve?</li>
          <li>Where does the problem appear in the workflow?</li>
          <li>Who owns or experiences the problem?</li>
          <li>Why does the problem matter?</li>
          <li>What evidence supports deeper validation?</li>
          <li>What next step would improve understanding?</li>
        </ul>
      </div>
      <div>
        <h3>Map where the problem appears</h3>
        <p>A workflow is the sequence of activities that turns an input into an output. It usually combines people, systems, decisions, handoffs, reviews, and approvals.</p>
        <p>Business problems rarely affect every step equally. Locating the friction makes the opportunity easier to understand and helps determine whether deeper investigation is worthwhile.</p>
      </div>
    </div>

    <div class="research-canvas__table-wrap">
      <h3>Workflow mapping questions</h3>
      <p>Map enough of the current workflow to find the problem boundary before discussing the target AI capability.</p>
      <table>
        <thead><tr><th scope="col">Workflow element</th><th scope="col">Discovery question</th><th scope="col">Evidence to look for</th></tr></thead>
        <tbody>
          <tr><th scope="row">Input</th><td>What starts the work, and what information arrives with it?</td><td>Documents, requests, records, events, messages, or system states.</td></tr>
          <tr><th scope="row">Activity</th><td>What work is performed, and by whom?</td><td>Manual steps, system actions, repeated tasks, and exception handling.</td></tr>
          <tr><th scope="row">Decision</th><td>Where must someone interpret, classify, compare, approve, or choose?</td><td>Decision rules, judgment points, uncertainty, and escalation criteria.</td></tr>
          <tr><th scope="row">Handoff</th><td>Where does responsibility or information move between people, teams, or systems?</td><td>Queues, integrations, emails, ownership changes, and waiting time.</td></tr>
          <tr><th scope="row">Review or approval</th><td>Which steps require oversight before the work can continue?</td><td>Control points, approvers, legal or compliance checks, and audit evidence.</td></tr>
          <tr><th scope="row">Output</th><td>What business result should the workflow produce?</td><td>Completed transaction, decision, document, recommendation, response, or measurable outcome.</td></tr>
          <tr><th scope="row">Friction</th><td>Where does time, inconsistency, rework, risk, cost, or poor quality appear?</td><td>Delays, error rates, backlog, repeated corrections, escalations, or user complaints.</td></tr>
          <tr><th scope="row">Owner</th><td>Who is accountable for improving the result at the problem boundary?</td><td>Named process owner, team lead, department head, sponsor, or control owner.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="business-ai-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Knowledge map</p>
      <h2>Processes, domains, patterns, technologies, outcomes, evidence.</h2>
      <p>SAP is part of this map because many enterprise processes run there. Microsoft, Google, AWS, OpenAI, Salesforce, ServiceNow, Oracle, UiPath, specialist ML tools, optimizers, and internal platforms belong to the same architecture discussion.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/business-ai/processes/"><span>01</span><strong>End-to-End Enterprise Processes</strong><small>{{ process_map.processes | size }} process chains with stages, AI jobs, patterns, technology families, and control points.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="/labs/business-ai/domains/"><span>02</span><strong>Enterprise Domains</strong><small>{{ domain_map.domains | size }} ownership views with business jobs, system touchpoints, technology families, architecture questions, and evidence gaps.</small><i class="material-symbols-outlined" aria-hidden="true">domain</i></a>
      <a href="/labs/business-ai/patterns/"><span>03</span><strong>Reusable AI Patterns</strong><small>Decision and workflow shapes that survive a vendor change: extraction, forecasting, recommendation, exception management, copilots, optimization, and more.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/labs/business-ai/technologies/"><span>04</span><strong>Enterprise AI Technology Landscape</strong><small>{{ tech.families | size }} capability families and {{ tech.platforms | size }} platform examples compared by architecture role.</small><i class="material-symbols-outlined" aria-hidden="true">memory</i></a>
      <a href="/labs/business-ai/cases/"><span>05</span><strong>Implementation Cases</strong><small>Who changed which process, what technology was disclosed, what result was reported, and what remains uncertain.</small><i class="material-symbols-outlined" aria-hidden="true">cases</i></a>
      <a href="/labs/business-ai/scenarios/"><span>06</span><strong>Scenario Outcomes</strong><small>{{ scenario_library.scenarios | size }} strong, mixed, and failed scenarios compared by process, controls, results, failure mode, and reusable lesson.</small><i class="material-symbols-outlined" aria-hidden="true">compare_arrows</i></a>
      <a href="/labs/business-ai/practices/"><span>07</span><strong>Best Practices and Anti-Patterns</strong><small>{{ scenario_library.best_practices | size }} operating rules and {{ scenario_library.failure_patterns | size }} recurring failure shapes for design reviews and assessments.</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      <a href="/labs/business-ai/matrix/"><span>08</span><strong>Assessment Decision Matrix</strong><small>{{ assessment_matrix.profiles | size }} process profiles linking AI job, autonomy, risk, KPI, system authority, controls, failure patterns, and evidence.</small><i class="material-symbols-outlined" aria-hidden="true">grid_view</i></a>
      <a href="/labs/business-ai/model/"><span>09</span><strong>Graph Model</strong><small>Nodes and edges for companies, processes, domains, patterns, technologies, outcomes, controls, metrics, evidence, limitations, and decision profiles.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="/labs/business-ai/pilots/"><span>10</span><strong>Open Enterprise AI Pilots</strong><small>Vendor-neutral pilots for document-to-ERP automation, ERP agent access, safety benchmarks, readiness, and open evidence.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="/labs/business-ai/data/processes.json"><span>PROC</span><strong>Process Data</strong><small>Machine-readable stages, AI jobs, patterns, technologies, controls, and owning domains.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/labs/business-ai/data/domains.json"><span>DOM</span><strong>Domain Data</strong><small>Machine-readable business jobs, enterprise systems, technology families, architecture questions, and case IDs.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/labs/business-ai/data/technologies.json"><span>TECH</span><strong>Technology Data</strong><small>Machine-readable capability families, platform roles, fit conditions, limits, and primary-source registry.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/labs/business-ai/data/catalog.json"><span>CASE</span><strong>Case and Pattern Data</strong><small>Machine-readable cases, patterns, evidence grades, sources, metrics, limits, and consultant notes.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/labs/business-ai/data/scenarios.json"><span>RISK</span><strong>Scenario and Failure Data</strong><small>Machine-readable strong patterns, mixed results, failures, best practices, anti-patterns, controls, lessons, and sources.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/labs/business-ai/data/matrix.json"><span>DEC</span><strong>Assessment Matrix Data</strong><small>Machine-readable autonomy levels, risk classes, decision rules, scenario profiles, KPIs, authority boundaries, controls, and Lead answer shapes.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/labs/ai-ready/"><span>SYS</span><strong>AI Ready Architecture Lab</strong><small>Deeper vendor-neutral engineering patterns for RAG, tools, MCP, agents, evaluations, security, deployment, and production operation.</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      <a href="/labs/enterprise-context/business-ai/"><span>SAP</span><strong>SAP Business AI Detail</strong><small>Joule, Joule Studio, AI Core, generative AI hub, grounding, runtime, and SAP-specific integration. It is one technology detail view, not the scope of Business AI.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
    </div>
  </section>

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Review method</p><h2>Read Business AI in six layers.</h2></div>
    <ol>
      <li><span>01</span><strong>Process</strong><p>Which stage, task, decision, exception, or business outcome should improve?</p></li>
      <li><span>02</span><strong>Pattern</strong><p>Is the uncertain part extraction, retrieval, prediction, optimization, recommendation, generation, or adaptive orchestration?</p></li>
      <li><span>03</span><strong>Technology</strong><p>Which platform, model, workflow, data, and integration components fit the existing enterprise landscape?</p></li>
      <li><span>04</span><strong>Authority</strong><p>How much autonomy is acceptable, and which business system still owns identity, policy, transaction state, and final commitment?</p></li>
      <li><span>05</span><strong>Control</strong><p>Where are approval, fallback, monitoring, rollback, exception handling, and risk limits defined?</p></li>
      <li><span>06</span><strong>Evidence</strong><p>What was measured, who reported it, what failed, and what important result is still missing?</p></li>
    </ol>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
