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
    title: "Business AI Glossary — Plain Language for Discovery, Architecture, Governance and Delivery"
    url: "/labs/business-ai/glossary/"
  - type: "deep_dive"
    title: "AI Implementation Readiness — Evals, Safeguards, Observability, Release and Rollback"
    url: "/labs/business-ai/implementation-readiness/"
  - type: "deep_dive"
    title: "AI Model Selection — Model Classes, Context, Latency, Cost and Evals"
    url: "/labs/business-ai/model-selection/"
  - type: "deep_dive"
    title: "Open Enterprise AI Research — ERP Evidence, Safety, and Readiness"
    url: "/labs/business-ai/open-research/"
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
        <ul><li>Is the customer problem clear?</li><li>Is the workflow understood?</li><li>Are relevant stakeholders visible?</li><li>Is there a plausible direction to explore?</li></ul>
      </div>
      <div>
        <h3>Business problem clarity</h3>
        <p>Problem clarity exists when the customer can describe a specific operational challenge that is important enough to investigate.</p>
        <p>Try to understand:</p>
        <ul><li>What is happening today?</li><li>Who is affected by the problem?</li><li>What is the impact on time, cost, risk, speed, quality, or customer experience?</li><li>What would a better outcome look like?</li></ul>
      </div>
    </div>

    <div class="research-canvas__table-wrap">
      <h3>Stakeholder discovery</h3>
      <p>Once a workflow problem begins to take shape, discovery needs to clarify who is connected to it. Different stakeholders often experience the same workflow in different ways: one group may carry the daily burden, another may own the business result, and another may influence whether a future change can move forward.</p>
      <p>Stakeholder discovery helps identify who experiences the pain, who owns the outcome, who influences decisions, who needs to support validation, and who cares about adoption, approval, risk, or success measures. Opportunities become easier to validate when this ownership is visible.</p>
      <table><thead><tr><th scope="col">Stakeholder type</th><th scope="col">What they usually tell you</th><th scope="col">Why they matter</th></tr></thead><tbody>
        <tr><th scope="row">Affected users</th><td>What the work feels like day to day, where friction appears, and which exceptions make the workflow harder.</td><td>They reveal practical workflow friction and provide current-state evidence.</td></tr>
        <tr><th scope="row">Outcome owner</th><td>What business result needs to improve, such as turnaround time, quality, risk, cost, or service.</td><td>They help validate priority, accountability, and what success should mean.</td></tr>
        <tr><th scope="row">Influencers</th><td>What constraints, approvals, dependencies, or risks may affect progress.</td><td>They help identify what could block, shape, validate, or govern the opportunity. This may include IT, security, procurement, legal, compliance, or other control teams.</td></tr>
        <tr><th scope="row">Executive sponsor or senior stakeholder</th><td>Why the issue matters at a broader business level and how it connects to wider priorities.</td><td>They can create urgency, visibility, sponsorship, or access to the people needed for progress.</td></tr>
      </tbody></table>
      <p>An interested contact is still useful, but interest alone is weak evidence if that person does not experience the pain, own the outcome, influence a decision, or provide a path to the people who do.</p>
    </div>

    <div class="ecg-decision-columns"><div><h3>Identifying the outcome owner</h3><p>An outcome owner is the person accountable for improving the workflow or business result. They may be a team lead, department head, process owner, or business sponsor.</p><p>The outcome owner may not perform the work every day. Their role is to connect the workflow problem to a result that matters and help judge whether improving it is a real priority.</p></div><div><h3>Questions that reveal ownership</h3><ul><li>Who is accountable for the current workflow result?</li><li>Who is measured on the outcome that should improve?</li><li>Who can decide that the problem deserves deeper validation?</li><li>Who needs to agree on success measures or acceptable boundaries?</li></ul></div></div>

    <div class="ecg-decision-columns"><div><h3>Customer commitment</h3><p>Customer commitment means the customer has shown credible willingness to keep moving. It is stronger when the customer contributes time, access, evidence, people, or decisions rather than only expressing interest.</p><p>Useful signals include:</p><ul><li>Agreeing to a specific discovery workshop, validation session, prototype, or pilot.</li><li>Bringing the workflow owner, operators, or required control teams into the discussion.</li><li>Sharing approved process examples, requirements, data samples, or current-state evidence.</li><li>Helping define success criteria, constraints, ownership, and a next decision point.</li></ul></div><div><h3>Do not confuse interest with movement</h3><p>A curious contact can open the door, but the opportunity becomes stronger when there is a path from interest to the people, evidence, and decisions required to validate it.</p><p>Commitment does not prove that AI is the right solution. It shows that the customer is willing to do the work required to find out.</p></div></div>

    <div class="ecg-decision-columns"><div><h3>Keep discovery useful</h3><p>A good discovery conversation feels like joint problem-solving, not a product pitch or a checklist interview.</p><ul><li><strong>Ask before prescribing.</strong> Understand the work before suggesting a solution.</li><li><strong>Stay close to the workflow.</strong> Follow tasks, decisions, handoffs, and outcomes rather than product labels.</li><li><strong>Check the evidence.</strong> Separate what the customer knows from what still needs validation.</li><li><strong>Build the picture together.</strong> Use questions to create shared clarity, not to test the customer.</li></ul></div><div><h3>Signs the opportunity is ready to move</h3><p>Readiness becomes visible through action. Look for a combination of:</p><ul><li>A named owner and a problem that can be explained clearly.</li><li>The right users and decision-makers joining the discussion.</li><li>Enough workflow detail to define a realistic validation scope.</li><li>Customer willingness to share approved examples, context, or process evidence.</li><li>A concrete validation activity or next meeting with the people needed to make progress.</li></ul><p>No single signal is enough. Together, they show whether the opportunity is becoming testable rather than simply interesting.</p></div></div>

    <div class="research-canvas__table-wrap"><h3>Watch for red flags</h3><p>Red flags do not always mean the opportunity should stop. They show where discovery is too weak, too broad, or too risky to support the next decision.</p><table><thead><tr><th scope="col">Red flag area</th><th scope="col">What it may sound like</th><th scope="col">Why it matters</th></tr></thead><tbody>
      <tr><th scope="row">Unclear problem definition</th><td><em>“We want to do something with AI.”</em></td><td>The problem is vague, and the partner may end up defining the customer’s problem for them.</td></tr><tr><th scope="row">Workflow uncertainty</th><td><em>“We need an AI assistant.”</em></td><td>The label does not explain which workflow changes, who uses it, or what output improves.</td></tr><tr><th scope="row">Unclear ownership</th><td><em>“One contact is interested, but they do not own the process.”</em></td><td>The opportunity may stall if no operator, outcome owner, or sponsor path is visible.</td></tr><tr><th scope="row">Sensitive workflow without boundaries</th><td><em>“We want AI for compliance decisions.”</em></td><td>The workflow may need clear ownership, oversight, approval paths, and validation boundaries before it can progress.</td></tr><tr><th scope="row">No customer commitment</th><td><em>“Let’s check back later.”</em></td><td>Without a credible next step, there may not be enough engagement to move forward.</td></tr><tr><th scope="row">Value is implied but not stated</th><td><em>“AI should improve the business somehow.”</em></td><td>The opportunity lacks a testable reason to act.</td></tr><tr><th scope="row">First use case is too broad or risky</th><td><em>“We want AI to transform the whole compliance process.”</em></td><td>Early validation needs a bounded workflow, owner, and approval path.</td></tr><tr><th scope="row">Stakeholders cannot support validation</th><td><em>“No one can join a discovery session or share workflow details.”</em></td><td>Without participation, the opportunity cannot build credible evidence.</td></tr>
    </tbody></table></div>

    <div class="ecg-decision-columns"><div><h3>Create clarity through discovery</h3><p>Strong discovery helps the customer move from broad statements to specific evidence. Do not accept <em>“we need AI”</em> as a complete requirement. Help the customer explain the workflow, pain, people involved, business impact, and next validation step.</p><p>Effective discovery should answer:</p><ul><li>What problem is the customer trying to solve?</li><li>Where does the problem appear in the workflow?</li><li>Who owns or experiences the problem?</li><li>Why does the problem matter?</li><li>What evidence supports deeper validation?</li><li>What next step would improve understanding?</li></ul></div><div><h3>Map where the problem appears</h3><p>A workflow is the sequence of activities that turns an input into an output. It usually combines people, systems, decisions, handoffs, reviews, and approvals.</p><p>Business problems rarely affect every step equally. Locating the friction makes the opportunity easier to understand and helps determine whether deeper investigation is worthwhile.</p></div></div>

    <div class="research-canvas__table-wrap"><h3>Workflow mapping questions</h3><p>Map enough of the current workflow to find the problem boundary before discussing the target AI capability.</p><table><thead><tr><th scope="col">Workflow element</th><th scope="col">Discovery question</th><th scope="col">Evidence to look for</th></tr></thead><tbody><tr><th scope="row">Input</th><td>What starts the work, and what information arrives with it?</td><td>Documents, requests, records, events, messages, or system states.</td></tr><tr><th scope="row">Activity</th><td>What work is performed, and by whom?</td><td>Manual steps, system actions, repeated tasks, and exception handling.</td></tr><tr><th scope="row">Decision</th><td>Where must someone interpret, classify, compare, approve, or choose?</td><td>Decision rules, judgment points, uncertainty, and escalation criteria.</td></tr><tr><th scope="row">Handoff</th><td>Where does responsibility or information move between people, teams, or systems?</td><td>Queues, integrations, emails, ownership changes, and waiting time.</td></tr><tr><th scope="row">Review or approval</th><td>Which steps require oversight before the work can continue?</td><td>Control points, approvers, legal or compliance checks, and audit evidence.</td></tr><tr><th scope="row">Output</th><td>What business result should the workflow produce?</td><td>Completed transaction, decision, document, recommendation, response, or measurable outcome.</td></tr><tr><th scope="row">Friction</th><td>Where does time, inconsistency, rework, risk, cost, or poor quality appear?</td><td>Delays, error rates, backlog, repeated corrections, escalations, or user complaints.</td></tr><tr><th scope="row">Owner</th><td>Who is accountable for improving the result at the problem boundary?</td><td>Named process owner, team lead, department head, sponsor, or control owner.</td></tr></tbody></table></div>

    <div class="research-canvas__table-wrap"><h3>Discovery evidence summary</h3><p>After discovery, capture only what helps the next decision. The summary should make evidence gaps visible, not hide them behind polished wording.</p><table><thead><tr><th scope="col">Evidence area</th><th scope="col">Capture this</th></tr></thead><tbody><tr><th scope="row">Problem</th><td>The customer challenge in one clear sentence. Avoid product names unless they are part of the current environment.</td></tr><tr><th scope="row">Workflow friction</th><td>The step where the problem appears and what goes wrong there: delay, rework, inconsistency, risk, cost, or another concrete pain.</td></tr><tr><th scope="row">People and ownership</th><td>Who feels the pain, who owns the result, and who can enable, shape, approve, or block progress.</td></tr><tr><th scope="row">Why it matters</th><td>The strongest available signal that the problem deserves attention, such as time lost, backlog, quality issues, risk, cost, or service impact.</td></tr><tr><th scope="row">Readiness and constraints</th><td>What is known about participation, data access, approvals, security, governance, operating limits, and willingness to validate.</td></tr><tr><th scope="row">Next proof</th><td>The next activity that should reduce uncertainty, who needs to join, and which question it should answer.</td></tr></tbody></table><p>If an area cannot be supported with facts yet, mark it as a gap. That gap becomes part of the next discovery step rather than an invitation to guess.</p></div>
  </section>

  <section class="research-canvas__inventory" id="ai-use-case-design" data-reveal>
    <header><p class="research-canvas__eyebrow">Use-case design</p><h2>Turn a workflow problem into a testable AI job.</h2><p>Discovery shows where work is slow, inconsistent, risky, expensive, or difficult. Use-case design asks a narrower question: where could AI improve one part of that workflow without losing sight of ownership, control, and business value?</p></header>
    <div class="ecg-decision-columns"><div><h3>Problem statement</h3><p>Describe the current state: where the workflow breaks down, who is affected, and why the issue matters.</p><p><strong>Example:</strong> Contract reviewers spend too much time finding relevant clauses, and similar agreements are reviewed inconsistently.</p></div><div><h3>Use-case statement</h3><p>Describe one improvement AI may support inside that workflow. Keep it specific enough to validate and clear about what people still decide or approve.</p><p><strong>Example:</strong> At clause review, AI retrieves and summarizes relevant approved guidance for the reviewer, who decides whether the clause needs action.</p></div></div>

    <div class="research-canvas__table-wrap"><h3>Common AI jobs in a workflow</h3><p>Start with the output the workflow needs. The technology label comes later.</p><table><thead><tr><th scope="col">AI job</th><th scope="col">Useful output</th><th scope="col">Example</th></tr></thead><tbody><tr><th scope="row">Retrieval</th><td>Grounded answer, comparison, summary, or synthesis.</td><td>Find relevant guidance across approved policy sources.</td></tr><tr><th scope="row">Extraction</th><td>Structured facts or fields from unstructured content.</td><td>Turn submitted forms into the fields needed for processing.</td></tr><tr><th scope="row">Classification and routing</th><td>Category, priority, queue, or routing suggestion.</td><td>Route service requests by issue type and urgency.</td></tr><tr><th scope="row">Generation</th><td>Draft, message, summary, plan, or report.</td><td>Prepare a first customer response using approved case context.</td></tr><tr><th scope="row">Review</th><td>Flags, missing items, quality checks, or findings.</td><td>Check a draft for required information before human approval.</td></tr><tr><th scope="row">Recommendation</th><td>Suggested next action or ranked options.</td><td>Rank follow-up actions for a manager to review.</td></tr><tr><th scope="row">Monitoring and coordination</th><td>Status signal, exception, reminder, or alert.</td><td>Surface onboarding tasks that are delayed or incomplete.</td></tr></tbody></table><p>A strong use case describes the workflow improvement in business terms. “Use an LLM” is an implementation choice, not a use-case definition.</p></div>

    <div class="ecg-decision-columns"><div><h3>One-line use-case frame</h3><p><strong>At [workflow step], [user] uses AI to [produce or prepare an output] from [work object]. [Human role] reviews, decides, approves, or acts on it so [business outcome] can improve.</strong></p><p>The sentence is useful because it forces the use case to name the work, the output, the human boundary, and the intended result.</p></div><div><h3>Keep the boundary visible</h3><p>If the sentence cannot explain who acts on the AI output, the design is probably still too vague. In sensitive workflows, the human or system authority should be explicit before validation begins.</p></div></div>

    <div class="research-canvas__table-wrap"><h3>Use-case anatomy</h3><table><thead><tr><th scope="col">Element</th><th scope="col">Capture</th><th scope="col">Why it matters</th></tr></thead><tbody><tr><th scope="row">Workflow location</th><td>The exact step, decision, handoff, or review point.</td><td>Keeps the idea attached to real work.</td></tr><tr><th scope="row">User</th><td>The person who uses, reviews, or benefits from the output.</td><td>Makes adoption and ownership visible.</td></tr><tr><th scope="row">Work object</th><td>The document, request, case, order, ticket, record, or other item being processed.</td><td>Makes the scope concrete.</td></tr><tr><th scope="row">AI output</th><td>What AI retrieves, extracts, classifies, drafts, checks, recommends, or flags.</td><td>Defines what the AI actually does.</td></tr><tr><th scope="row">Human or system control</th><td>Who reviews, approves, decides, posts, or commits the result.</td><td>Protects authority and accountability.</td></tr><tr><th scope="row">Business outcome</th><td>The result expected to improve: time, quality, risk, cost, service, throughput, or another measurable signal.</td><td>Connects the use case to value.</td></tr></tbody></table></div>

    <div class="research-canvas__table-wrap"><h3>Choose a first use case you can actually validate</h3><p>The best first use case is not always the biggest idea. It is the one that can produce credible evidence without requiring half the company to redesign itself first.</p><table><thead><tr><th scope="col">Factor</th><th scope="col">Good signal</th><th scope="col">Warning</th></tr></thead><tbody><tr><th scope="row">Workflow clarity</th><td>The target step and current pain are understood.</td><td>The team is still debating what work the use case belongs to.</td></tr><tr><th scope="row">Stakeholder access</th><td>Users, owner, and required reviewers can participate.</td><td>The people needed to validate the workflow are unavailable.</td></tr><tr><th scope="row">Process stability</th><td>The current process is stable enough to compare before and after.</td><td>The process itself is being redesigned at the same time.</td></tr><tr><th scope="row">Input availability</th><td>Representative examples and source material can be reviewed appropriately.</td><td>Validation depends on inputs nobody can access or explain.</td></tr><tr><th scope="row">Data readiness</th><td>Inputs are representative, usable, and permissioned for the test.</td><td>Data quality, access, or permission is still unknown.</td></tr><tr><th scope="row">Risk and control</th><td>Errors are manageable, and review, fallback, or approval can be designed.</td><td>A bad output could create material harm with no realistic control.</td></tr><tr><th scope="row">Measurement</th><td>The team can observe whether time, quality, risk, cost, or another outcome improves.</td><td>Success can only be described as “people liked it.”</td></tr><tr><th scope="row">Scope</th><td>The test is bounded and has limited dependencies.</td><td>The first validation requires enterprise-wide change or unclear ownership.</td></tr></tbody></table><p>A use case does not need perfect readiness. It needs enough clarity, access, control, and measurement to learn something trustworthy from the next step.</p></div>

    <div class="research-canvas__table-wrap"><h3>Compare use cases without fake precision</h3><p>Do not turn early discovery into a numerical scorecard. Compare options with the same questions, discuss the evidence, and make the gaps visible. The goal is a better decision, not a decimal point.</p><table><thead><tr><th scope="col">Comparison lens</th><th scope="col">Question</th><th scope="col">What a useful answer reveals</th></tr></thead><tbody><tr><th scope="row">Business value</th><td>What could improve if this works?</td><td>The outcome worth testing: time, quality, cost, risk, service, throughput, or another business result.</td></tr><tr><th scope="row">Workflow readiness</th><td>Do we understand the target step well enough to test a change?</td><td>Whether the use case is grounded in a stable, observable part of the process.</td></tr><tr><th scope="row">Data readiness</th><td>Can we use representative, permissioned inputs for validation?</td><td>Whether the test can run on evidence that resembles real work.</td></tr><tr><th scope="row">Risk and control</th><td>What can go wrong, and how would review, fallback, or approval contain it?</td><td>Whether errors are manageable and authority remains clear.</td></tr><tr><th scope="row">Stakeholder support</th><td>Who cares enough to participate in the test and act on the result?</td><td>Whether users, owners, reviewers, and sponsors can support validation.</td></tr><tr><th scope="row">Measurement</th><td>How will we know the workflow improved?</td><td>Whether the outcome can be observed instead of described only through opinion.</td></tr><tr><th scope="row">Expansion potential</th><td>If this works, what useful capability or evidence could be reused next?</td><td>Whether the first use case can teach something that supports broader adoption without pretending the pilot proves everything.</td></tr></tbody></table><p>For each option, capture three things: <strong>what is known, what is weak, and what needs proof next</strong>. That is usually enough to compare use cases consistently without inventing certainty.</p></div>
  </section>

  <section class="research-canvas__inventory" id="ai-api-fluency" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">API fluency</p>
      <h2>Treat an AI API call as a controlled workflow contract.</h2>
      <p>The request is more than the user’s sentence. In a production workflow, it is the complete package of instructions, approved context, tools, state, identity, permissions, and output requirements needed to perform one controlled step.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <h3>The request contract</h3>
      <p>Before discussing the model, make the full request boundary visible. A useful design review can explain where every important input comes from and who is allowed to supply it.</p>
      <table>
        <thead><tr><th scope="col">Request part</th><th scope="col">What it provides</th><th scope="col">Lead question</th></tr></thead>
        <tbody>
          <tr><th scope="row">User or application input</th><td>The immediate task, question, event, or business data.</td><td>What did the caller actually request, and which parts are untrusted input?</td></tr>
          <tr><th scope="row">System-level instructions</th><td>Stable rules, role, policy, and operating boundaries.</td><td>Which instructions are controlled by the application, and which may come from the user?</td></tr>
          <tr><th scope="row">Approved context</th><td>Enterprise facts, documents, records, or retrieved knowledge needed for the task.</td><td>Is the context relevant, current, permissioned, and traceable to a source?</td></tr>
          <tr><th scope="row">Files or structured data</th><td>Work objects such as documents, orders, tickets, records, images, or tables.</td><td>Are format, size, quality, sensitivity, and validation rules understood?</td></tr>
          <tr><th scope="row">Tools and retrieval</th><td>Controlled ways to read data, call services, search sources, or perform actions.</td><td>Which tools only read, which can write, and what side effects can each tool create?</td></tr>
          <tr><th scope="row">Output contract</th><td>The expected response shape for a person or downstream system.</td><td>Does the consumer need prose, a classification, a tool decision, or a schema-constrained result?</td></tr>
          <tr><th scope="row">State</th><td>Prior response, workflow state, or business context needed to continue the process.</td><td>What must persist across turns or steps, where is it stored, and who owns it?</td></tr>
          <tr><th scope="row">Identity and permissions</th><td>The user, application, tenant, role, and business authority behind the request.</td><td>Whose authority is being exercised when data is returned or an action is taken?</td></tr>
        </tbody>
      </table>
    </div>

    <div class="research-canvas__table-wrap">
      <h3>The response contract</h3>
      <p>The response is also more than a paragraph. The application must know what the result means and what should happen next.</p>
      <table>
        <thead><tr><th scope="col">Response shape</th><th scope="col">What it may contain</th><th scope="col">Why it matters</th></tr></thead>
        <tbody>
          <tr><th scope="row">Human-readable content</th><td>An answer, explanation, summary, or generated draft.</td><td>A person can review or use the result directly.</td></tr>
          <tr><th scope="row">Structured result</th><td>Fields that follow a defined schema for downstream processing.</td><td>The next system can validate and consume the result without parsing free text.</td></tr>
          <tr><th scope="row">Decision signal</th><td>A classification, recommendation, ranking, or proposed next action.</td><td>The workflow can separate advice from authority to execute.</td></tr>
          <tr><th scope="row">Tool interaction</th><td>A tool request, tool result, retrieved evidence, or action outcome.</td><td>The orchestrator can track what happened outside the model.</td></tr>
          <tr><th scope="row">Workflow status</th><td>Completion, continuation, missing information, approval request, or another state.</td><td>The caller knows whether to stop, continue, retry, or ask for review.</td></tr>
          <tr><th scope="row">Refusal or escalation</th><td>A controlled stop when policy, permission, confidence, or business rules do not allow the requested path.</td><td>A safe workflow needs an explicit failure path, not a vague answer that looks successful.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="ecg-decision-columns">
      <div>
        <h3>Authentication</h3>
        <p>Authentication proves that a person, application, or system is allowed to connect. It answers <strong>“Who or what is calling?”</strong></p>
        <p>A valid credential opens the door. It does not grant unlimited business authority.</p>
      </div>
      <div>
        <h3>Access control and authorization</h3>
        <p>Access control decides what the authenticated caller may read, create, change, approve, or execute. It answers <strong>“What is this identity allowed to do here?”</strong></p>
        <p>Keep this decision outside the model wherever possible. The model may help choose an action, but enterprise policy should decide whether that action is permitted.</p>
      </div>
    </div>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">verified_user</span>
      <p><strong>Control chain:</strong> identity → authentication → authorization → context filtering → model or tool decision → approval when required → execution → result validation → audit and recovery.</p>
      <p>If any step is missing, the system may still produce an impressive answer while exercising the wrong authority. Enterprise software has spent decades discovering that “it connected successfully” is not the same as “it was allowed to do that.”</p>
    </div>

    <div class="ecg-decision-columns">
      <div>
        <h3>Structured output is an interface contract</h3>
        <p>When a downstream system needs a reliable machine-readable result, define the expected fields with an appropriate JSON Schema and use schema-constrained output where the API supports it.</p>
        <p>Do not rely on a prompt that merely asks for “valid JSON.” The schema should define required fields, allowed values, data types, and the structure the next system expects.</p>
      </div>
      <div>
        <h3>State is part of architecture</h3>
        <p>Multi-step AI workflows need an explicit answer to what continues across turns: conversation context, business object status, previous tool results, approval state, and retry information.</p>
        <p>State should not quietly become hidden memory. Define what is stored, where it is stored, how long it is needed, and which identity may read or change it.</p>
      </div>
    </div>

    <div class="research-canvas__table-wrap">
      <h3>Lead questions before production</h3>
      <table>
        <thead><tr><th scope="col">Area</th><th scope="col">Question to resolve</th></tr></thead>
        <tbody>
          <tr><th scope="row">Trust boundary</th><td>Which input is controlled by the application, and which input can be influenced by a user, document, retrieved source, or external system?</td></tr>
          <tr><th scope="row">Data access</th><td>Which sources may be retrieved for this user and business purpose?</td></tr>
          <tr><th scope="row">Tool authority</th><td>Which tools are read-only, which can change business state, and which actions require approval?</td></tr>
          <tr><th scope="row">Output consumer</th><td>Will a person read the result, or will another system consume it automatically?</td></tr>
          <tr><th scope="row">Validation</th><td>How are schema, business rules, missing fields, unsupported values, and low-confidence outcomes checked?</td></tr>
          <tr><th scope="row">Failure handling</th><td>What happens on timeout, tool failure, partial completion, refusal, or a business-system rejection?</td></tr>
          <tr><th scope="row">Retry and idempotency</th><td>Can the workflow retry safely without creating duplicate transactions or repeating side effects?</td></tr>
          <tr><th scope="row">Audit</th><td>Can the team reconstruct who requested the action, what context and tools were used, what was approved, and what the business system returned?</td></tr>
        </tbody>
      </table>
    </div>

    <div class="research-canvas__table-wrap">
      <h3>Example: AI prepares a sales-order proposal</h3>
      <p>Consider a workflow where a user asks AI to prepare a sales-order proposal from a customer request. The first API step should prepare a controlled result, not silently create an SAP transaction.</p>
      <table>
        <thead><tr><th scope="col">Step</th><th scope="col">Controlled design</th></tr></thead>
        <tbody>
          <tr><th scope="row">Request</th><td>Include the user identity, customer request, approved sales context, relevant files or records, read-only retrieval tools, and an explicit output schema.</td></tr>
          <tr><th scope="row">AI result</th><td>Return proposed order fields, missing information, warnings, and evidence needed for review. Keep proposal generation separate from transaction authority.</td></tr>
          <tr><th scope="row">Authorization</th><td>Check whether this user and workflow are allowed to create or change the relevant business object before exposing a write tool.</td></tr>
          <tr><th scope="row">Approval</th><td>Require human or policy approval where the business risk demands it, especially before a side effect is committed.</td></tr>
          <tr><th scope="row">Execution</th><td>Call the SAP-facing tool with validated fields and duplicate protection. Treat the SAP response as the transaction result, not the model’s earlier proposal.</td></tr>
          <tr><th scope="row">Continuation</th><td>Record the business result, errors, approval state, and retry status so the next step continues from evidence rather than guessing what happened.</td></tr>
        </tbody>
      </table>
      <p><strong>Lead lens:</strong> the model can help interpret and prepare. Identity, authorization, validation, approval, transaction integrity, and recovery still belong to the application and enterprise control model.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="ai-value-story" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Value story</p>
      <h2>Explain why the use case matters without jumping to ROI.</h2>
      <p>A use case explains what AI may help the customer do. A value story explains why that improvement is worth testing. Keep the path visible from current work to a business priority, and separate evidence from assumptions.</p>
    </header>

    <div class="ecg-decision-columns">
      <div>
        <h3>Six questions keep the story grounded</h3>
        <ul>
          <li>What workflow problem are we trying to improve?</li>
          <li>What AI-supported change may be possible?</li>
          <li>What operational result could improve?</li>
          <li>Which business priority does that result support?</li>
          <li>What evidence already supports the story, and what is still assumed?</li>
          <li>What next step would reduce the biggest uncertainty?</li>
        </ul>
      </div>
      <div>
        <h3>Use case is not the value story</h3>
        <p><strong>Use case:</strong> what changes inside the workflow.</p>
        <p><strong>Value story:</strong> why that change matters to the customer and what evidence would make the claim credible.</p>
        <p>The difference prevents a common leap from <em>“AI can help with this task”</em> to <em>“therefore it creates ROI.”</em> The middle of the argument still needs evidence.</p>
      </div>
    </div>

    <div class="research-canvas__table-wrap">
      <h3>Build value in five steps</h3>
      <p>Move from the customer’s current work to the outcome they may be able to validate. Each step should be supported by something observable or clearly marked as an assumption.</p>
      <table>
        <thead><tr><th scope="col">Step</th><th scope="col">Clarify</th><th scope="col">Useful question</th></tr></thead>
        <tbody>
          <tr><th scope="row">Workflow problem</th><td>Where work is slow, costly, inconsistent, risky, or hard to scale today.</td><td>What is the customer struggling to do in the current workflow?</td></tr>
          <tr><th scope="row">AI-supported improvement</th><td>The specific part of the work AI may help improve.</td><td>What could become faster, clearer, more consistent, or easier to complete?</td></tr>
          <tr><th scope="row">Operational outcome</th><td>The observable result expected to change.</td><td>Which metric, behavior, queue, error rate, cycle time, or service result could move?</td></tr>
          <tr><th scope="row">Business priority</th><td>The customer goal or pressure connected to that operational result.</td><td>Why does this result matter now, and who cares about it?</td></tr>
          <tr><th scope="row">Validation evidence</th><td>The data, examples, stakeholder input, or test needed to make the value claim credible.</td><td>What evidence should we check before making a stronger claim?</td></tr>
        </tbody>
      </table>
    </div>

    <div class="ecg-decision-columns">
      <div>
        <h3>Start from what the customer actually said</h3>
        <p>Do not invent a strategy statement for the customer. Look for the priority, stakeholder, metric, or pressure already visible in discovery.</p>
        <ul>
          <li>Which priority did the customer name?</li>
          <li>Who owns or cares about the outcome?</li>
          <li>Which metric or business pressure is affected?</li>
          <li>What would make the customer decide the idea is worth testing?</li>
          <li>Which evidence would make that outcome believable?</li>
        </ul>
      </div>
      <div>
        <h3>Clarify the work before the value</h3>
        <p>Value claims become easier to defend when the current workflow is concrete.</p>
        <ul>
          <li>Who performs the work today?</li>
          <li>What does the workflow produce?</li>
          <li>Where does time, cost, inconsistency, risk, or scale pressure appear?</li>
          <li>What happens when the workflow performs badly?</li>
          <li>Which operational or business outcome is affected?</li>
        </ul>
      </div>
    </div>

    <div class="research-canvas__table-wrap">
      <h3>Let stakeholder pressure shape the value emphasis</h3>
      <p>The use case may stay the same while the value conversation changes. Emphasize the outcome the stakeholder is accountable for, not every possible benefit at once.</p>
      <table>
        <thead><tr><th scope="col">What you hear</th><th scope="col">Lead with</th><th scope="col">Evidence to examine</th></tr></thead>
        <tbody>
          <tr><th scope="row">“We need to reduce backlog.”</th><td>Throughput and cycle time.</td><td>Queue size, waiting time, completion rate, and available capacity.</td></tr>
          <tr><th scope="row">“We are under cost pressure.”</th><td>Effort and unit cost.</td><td>Manual time, cost per case, volume, avoided work, and the assumptions used to convert time into cost.</td></tr>
          <tr><th scope="row">“We have audit findings.”</th><td>Control and consistency.</td><td>Policy adherence, exception handling, escalation quality, repeat findings, and audit evidence.</td></tr>
          <tr><th scope="row">“Our teams are overloaded.”</th><td>Capacity and employee effort.</td><td>Repetitive work, handoffs, rework, workload, and time available for higher-value tasks.</td></tr>
          <tr><th scope="row">“Customers are waiting too long.”</th><td>Speed and service quality.</td><td>Response time, resolution rate, escalation rate, repeat contacts, and customer experience signals.</td></tr>
        </tbody>
      </table>
      <p>A credible value story is usually narrower than a sales pitch: one workflow problem, one plausible improvement, one observable outcome, one customer priority, and the evidence needed to test the connection.</p>
    </div>

    <div class="ecg-decision-columns">
      <div>
        <h3>Turn the story into a value hypothesis</h3>
        <p>A value hypothesis is a claim the customer can test, not a promise. It connects a workflow change to one expected outcome and makes the assumption visible.</p>
        <p><strong>Useful frame:</strong> If AI helps [user] improve [workflow step] by [specific change], then [indicator] may improve, supporting [business priority]. We will test this against [baseline or evidence] and validate [key assumption].</p>
      </div>
      <div>
        <h3>Measure only what supports the claim</h3>
        <p>More metrics do not make a value story stronger. Choose the smallest set that can confirm or challenge the hypothesis.</p>
        <ul>
          <li>Which business outcome are we trying to support?</li>
          <li>Which indicator would show movement?</li>
          <li>What baseline do we need?</li>
          <li>Which assumption are we testing?</li>
          <li>What evidence would justify further investment?</li>
        </ul>
      </div>
    </div>

    <div class="research-canvas__table-wrap">
      <h3>Match indicators to the outcome</h3>
      <table>
        <thead><tr><th scope="col">Outcome</th><th scope="col">Indicators worth considering</th></tr></thead>
        <tbody>
          <tr><th scope="row">Speed</th><td>Cycle time, turnaround time, wait time, and backlog age.</td></tr>
          <tr><th scope="row">Productivity and capacity</th><td>Manual effort, cases handled, review hours, queue size, and throughput.</td></tr>
          <tr><th scope="row">Cost</th><td>Cost per case, rework cost, external spend, overtime, or avoided future spend.</td></tr>
          <tr><th scope="row">Quality</th><td>Error rate, rework rate, consistency, completeness, and quality review findings.</td></tr>
          <tr><th scope="row">Risk</th><td>Escalation rate, policy exceptions, audit findings, control failures, and risk flags.</td></tr>
          <tr><th scope="row">Customer experience</th><td>Response time, resolution rate, repeat contacts, complaints, and satisfaction signals.</td></tr>
          <tr><th scope="row">Employee experience</th><td>Workload, repetitive-task time, handoffs, satisfaction, and capacity for higher-value work.</td></tr>
        </tbody>
      </table>
      <p>The indicator should match the claim. A faster workflow is not automatically a cheaper workflow, and saved time is not automatically cash savings.</p>
    </div>

    <div class="ecg-decision-columns">
      <div>
        <h3>Directional benefit estimate</h3>
        <p>Early in the opportunity, a range can be useful if the assumptions are visible. Start with baseline performance, work volume, expected improvement, adoption, and the part of the workflow actually affected.</p>
        <p>Call it a directional estimate until the customer has validated both the operational change and how that change converts into business value.</p>
      </div>
      <div>
        <h3>Before calling it ROI</h3>
        <p>ROI needs the economics, not just the benefit side. Include solution, implementation, integration, enablement, change-management, operating, support, and governance costs.</p>
        <p>Also make the time horizon, adoption rate, baseline, benefit conversion, risk adjustment, and confidence level explicit. A productivity gain may create capacity, service improvement, cost reduction, or none of those unless the operating model turns the time into value.</p>
      </div>
    </div>

    <div class="research-canvas__table-wrap">
      <h3>Same evidence, different stakeholder emphasis</h3>
      <p>Tailoring changes the emphasis, not the facts. Use the same evidence base and lead with the part each stakeholder is accountable for.</p>
      <table>
        <thead><tr><th scope="col">Stakeholder</th><th scope="col">Lead with</th><th scope="col">Keep visible</th></tr></thead>
        <tbody>
          <tr><th scope="row">CFO</th><td>Financial exposure, unit cost, capacity, investment assumptions, and confidence in the estimate.</td><td>Cost conversion assumptions, full investment, timing, adoption, and uncertainty.</td></tr>
          <tr><th scope="row">COO</th><td>Throughput, cycle time, operating burden, exceptions, and service quality.</td><td>Process stability, handoffs, capacity, and operational controls.</td></tr>
          <tr><th scope="row">CIO or CTO</th><td>Integration fit, scalability, data access, governance, security, and operational control.</td><td>System authority, dependencies, support model, and production constraints.</td></tr>
          <tr><th scope="row">Workflow owner</th><td>Usability, quality, effort, adoption, exceptions, and handoffs.</td><td>Day-to-day workflow impact and whether users can trust and act on the output.</td></tr>
          <tr><th scope="row">Executive sponsor</th><td>Strategic priority, urgency, business impact, risk of inaction, and expansion potential.</td><td>What is proven, what is still assumed, and why this deserves the next investment decision.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="research-canvas__table-wrap">
      <h3>Keep the seller narrative clean</h3>
      <table>
        <thead><tr><th scope="col">Statement</th><th scope="col">Keep it focused on</th></tr></thead>
        <tbody>
          <tr><th scope="row">Value hypothesis</th><td>What outcome may improve, which priority it supports, and which assumption connects the two.</td></tr>
          <tr><th scope="row">Solution direction</th><td>The likely workflow, AI, data, and integration approach, but only where discovery supports it.</td></tr>
          <tr><th scope="row">Validation need</th><td>The evidence, baseline, stakeholder input, control, or technical question that must be resolved next.</td></tr>
        </tbody>
      </table>
      <p>Keeping these statements separate makes the conversation easier to trust: the value hypothesis explains the possible benefit, the solution direction explains how it may be achieved, and the validation need explains what is still unknown.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="business-ai-map" data-reveal>
    <header><p class="research-canvas__eyebrow">Knowledge map</p><h2>Processes, domains, patterns, technologies, outcomes, evidence.</h2><p>SAP is part of this map because many enterprise processes run there. Microsoft, Google, AWS, OpenAI, Salesforce, ServiceNow, Oracle, UiPath, specialist ML tools, optimizers, and internal platforms belong to the same architecture discussion.</p></header>
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
      <a href="/labs/business-ai/implementation-readiness/"><span>11</span><strong>AI Implementation Readiness</strong><small>Evals, safeguards, observability, release, rollback, and a compact readiness snapshot for controlled production decisions.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
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
    <ol><li><span>01</span><strong>Process</strong><p>Which stage, task, decision, exception, or business outcome should improve?</p></li><li><span>02</span><strong>Pattern</strong><p>Is the uncertain part extraction, retrieval, prediction, optimization, recommendation, generation, or adaptive orchestration?</p></li><li><span>03</span><strong>Technology</strong><p>Which platform, model, workflow, data, and integration components fit the existing enterprise landscape?</p></li><li><span>04</span><strong>Authority</strong><p>How much autonomy is acceptable, and which business system still owns identity, policy, transaction state, and final commitment?</p></li><li><span>05</span><strong>Control</strong><p>Where are approval, fallback, monitoring, rollback, exception handling, and risk limits defined?</p></li><li><span>06</span><strong>Evidence</strong><p>What was measured, who reported it, what failed, and what important result is still missing?</p></li></ol>
  </section>

  <div class="research-canvas__support" data-reveal>{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
