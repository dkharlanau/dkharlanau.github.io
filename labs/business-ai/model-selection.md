---
layout: default
title: "AI Model Selection — Model Classes, Context, Latency, Cost and Evals"
description: "A practical enterprise AI model-selection framework using stable capability classes, workflow fit, context, reasoning depth, latency, cost, scale, and representative evals."
permalink: /labs/business-ai/model-selection/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-08-19
last_reviewed: 2026-08-19
hide_global_cta: true
publication_wave: "business-ai-model-selection-01"
review_method: "user-supplied model-selection framework + official OpenAI primary-source verification + editorial synthesis"
evidence_review_mode: "selective_or_heuristic"
search_intent: "AI model selection model classes reasoning latency cost context evals enterprise API"
structured_data:
  type: TechArticle
tags:
  - business-ai
  - enterprise-ai
  - model-selection
  - reasoning
  - multimodal
  - embeddings
  - retrieval
  - api
  - evaluation
career_impact: mapped
career_skills:
  - ai-readiness
  - ai-business-value
  - ai-evaluation
# ai-discovery-managed:start
primary_topic: "business-ai"
ai_sidecar: "/ai/pages/labs--business-ai--model-selection.json"
semantic_links:
  - type: "parent_context"
    title: "Business AI Lab — Processes, Patterns, Technologies, Evidence"
    url: "/labs/business-ai/"
  - type: "same_domain"
    title: "AI Architecture Patterns — From Reusable Shapes to First-Pass Blueprints"
    url: "/labs/business-ai/architecture-patterns/"
  - type: "same_domain"
    title: "AI Platform Building Blocks — Capability Roles, Minimum Set and Control Boundaries"
    url: "/labs/business-ai/platform-building-blocks/"
  - type: "same_domain"
    title: "Document-to-ERP AI Pilot — From PDF to Controlled Transaction"
    url: "/labs/business-ai/document-to-erp-ai/"
  - type: "same_domain"
    title: "ERP Agent Gateway Pilot — Safe AI Tool Access to Enterprise Systems"
    url: "/labs/business-ai/erp-agent-gateway/"
  - type: "same_domain"
    title: "AI Implementation Readiness — Evals, Safeguards, Observability, Release and Rollback"
    url: "/labs/business-ai/implementation-readiness/"
# ai-discovery-managed:end
---
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li aria-current="page">Model Selection</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Business AI / model selection</p>
      <h1>Choose the fit.<br />Then prove it.</h1>
      <p>API model selection becomes useful when intelligence must be embedded into software, operations, products, or customer experiences. The model is one component in a larger workflow, so the decision should be based on task shape, output requirements, risk, context, latency, cost, scale, and evidence.</p>
      <a class="research-canvas__button" href="#selection-sequence">Open the selection sequence <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Model selection sequence">
      <p>Selection sequence</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Fit</strong><small>Task and capability</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Test</strong><small>Representative examples</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Trade</strong><small>Quality, latency, cost</small></div>
      <em>A more capable model is not automatically the better production choice.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal aria-label="Model selection principle">
    <span class="material-symbols-outlined" aria-hidden="true">tune</span>
    <p><strong>Problem.</strong> Model selection often starts from a remembered model name, one impressive answer, or the assumption that the largest available model is always safest.</p>
    <p><strong>Working rule.</strong> Start from the workflow and define what good enough means. Then compare model classes and architecture options on the same representative examples.</p>
    <p><strong>Important distinction.</strong> The categories below are decision aids, not mutually exclusive vendor boxes. A model can be general-purpose, multimodal, tool-capable, and support configurable reasoning at the same time.</p>
  </section>

  <section class="research-canvas__inventory" id="selection-sequence" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Selection sequence</p>
      <h2>Move from task shape to evidence.</h2>
      <p>Do not compare models before the workflow can explain what it needs from them.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Step</th><th scope="col">Decision</th><th scope="col">Question</th></tr></thead>
        <tbody>
          <tr><th scope="row">1. Task shape</th><td>Clarify the work the AI must perform.</td><td>Is this drafting, classification, retrieval, multi-step reasoning, extraction, voice interaction, planning, or another job?</td></tr>
          <tr><th scope="row">2. Output contract</th><td>Define what the workflow needs back.</td><td>Does the result need prose, structured fields, a ranking, a tool decision, audio, or a bounded recommendation?</td></tr>
          <tr><th scope="row">3. Risk and authority</th><td>Understand the consequence of error.</td><td>What happens if the result is wrong, and can the system only advise or also change business state?</td></tr>
          <tr><th scope="row">4. Model class</th><td>Select the smallest credible capability class.</td><td>How much reasoning, modality support, speed, context, or specialization does the task require?</td></tr>
          <tr><th scope="row">5. Architecture</th><td>Add retrieval, ranking, tools, safety, state, or deployment controls where needed.</td><td>Which requirements belong outside the model itself?</td></tr>
          <tr><th scope="row">6. Success criteria</th><td>Choose two or three measures that can change the recommendation.</td><td>What would make one option clearly better or unacceptable?</td></tr>
          <tr><th scope="row">7. Representative eval</th><td>Build a small seed set and run the same realistic examples across the options.</td><td>Which choice meets the required quality and control level at acceptable latency and cost?</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="model-classes" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Model classes</p>
      <h2>Use stable capability categories, not model names from memory.</h2>
      <p>A model class is a stable discussion category. Specific model names, snapshots, prices, and limits change faster than the business task.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Decision category</th><th scope="col">Practical use in a workflow</th><th scope="col">Selection signal</th></tr></thead>
        <tbody>
          <tr><th scope="row">Reasoning-oriented models</th><td>Multi-step analysis, planning, ambiguity handling, policy interpretation, technical reasoning, and judgment-heavy work.</td><td>The task requires several dependent reasoning steps or careful trade-offs, not only fluent language generation.</td></tr>
          <tr><th scope="row">General-purpose models</th><td>Drafting, summarization, rewriting, classification, extraction, and broad workflow support.</td><td>The task is language-heavy but does not require deep planning on every request.</td></tr>
          <tr><th scope="row">Efficient models</th><td>Stable, simpler, high-volume tasks where speed, cost, and throughput matter.</td><td>The task can be well specified and quality remains acceptable with a smaller or faster model.</td></tr>
          <tr><th scope="row">Multimodal models</th><td>Workflows involving images, documents, screenshots, diagrams, or mixed input types.</td><td>Important evidence is not available as plain text alone.</td></tr>
          <tr><th scope="row">Audio or real-time models</th><td>Speech, transcription, streaming, voice interaction, and low-latency conversations.</td><td>The workflow is interactive and response timing or native audio matters.</td></tr>
          <tr><th scope="row">Embedding models</th><td>Semantic search, similarity comparison, clustering, retrieval, and knowledge organization.</td><td>The system needs vector representations for matching or retrieval rather than a generated answer from the embedding model itself.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">psychology</span>
      <p><strong>Reasoning depth</strong> describes how much planning, analysis, or multi-step problem solving the task requires.</p>
      <p>Do not pay for deep reasoning by default. Some current model families allow reasoning effort to be adjusted, so reasoning depth can be part of the configuration decision as well as the model-class decision.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="capabilities-and-architecture" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Capabilities and architecture</p>
      <h2>Not every requirement is a model class.</h2>
      <p>Moderation, tool use, retrieval, ranking, and deployment constraints often sit beside the main model. Keeping these layers separate makes architecture decisions easier to defend.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Capability or option</th><th scope="col">Useful when</th><th scope="col">Lead boundary</th></tr></thead>
        <tbody>
          <tr><th scope="row">Moderation and safety filtering</th><td>The workflow needs to identify unsafe, sensitive, disallowed, or escalation-worthy content.</td><td>Treat moderation as one safety layer. It does not replace business authorization, human review, or workflow-specific policy checks.</td></tr>
          <tr><th scope="row">Tool use</th><td>The workflow needs functions, APIs, retrieval, calculations, or actions across systems.</td><td>Tool capability does not grant business authority. Scope and authorize every read or write capability outside the model.</td></tr>
          <tr><th scope="row">Retrieval and ranking</th><td>The workflow needs current or enterprise-specific context from approved sources.</td><td>Retrieval returns candidates; ranking or reranking orders the candidates by relevance before downstream use.</td></tr>
          <tr><th scope="row">Open-weight models</th><td>Hosting, customization, deployment environment, infrastructure, policy, latency, or cost structure require a different operating model.</td><td>This is a deployment and ownership decision as much as a model decision. Include infrastructure, evaluation, security, upgrades, and support.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="selection-factors" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Selection factors</p>
      <h2>Quality is only one production constraint.</h2>
      <p>Model fit depends on the whole operating requirement. The same task may justify a different option when volume, response time, context, or risk changes.</p>
    </header>

    <div class="ecg-decision-columns">
      <div>
        <h3>Latency</h3>
        <p>Latency is the time the system takes to return a useful result. It matters most when a person or another system is waiting for the response inside an active workflow.</p>
        <p>Streaming can improve perceived responsiveness, but it does not remove the need to measure end-to-end task completion time.</p>
      </div>
      <div>
        <h3>Cost</h3>
        <p>Cost is the resource impact of running the workflow. Model tokens are only part of it. Retrieval, tools, retries, human review, infrastructure, and failed runs may also matter.</p>
        <p>Compare cost per useful business outcome, not only cost per API request.</p>
      </div>
      <div>
        <h3>Scale</h3>
        <p>Scale is how often the workflow runs and how many users, documents, requests, or actions it must support.</p>
        <p>A small quality difference can become expensive at high volume. A small latency difference can become painful in an interactive workflow.</p>
      </div>
    </div>

    <div class="research-canvas__table-wrap">
      <h3>Context is an architecture input</h3>
      <p>Context is the information the AI system can use to complete the task. In enterprise workflows, this may include company knowledge, documents, policies, records, system state, permissions, business rules, and operating context.</p>
      <table>
        <thead><tr><th scope="col">Context question</th><th scope="col">Why it changes model selection</th></tr></thead>
        <tbody>
          <tr><th scope="row">How much context is needed?</th><td>Large inputs may affect latency, cost, retrieval design, and whether all information should be sent to the model at once.</td></tr>
          <tr><th scope="row">How fresh must it be?</th><td>Current operational data usually belongs in retrieval or tool calls rather than static prompt text.</td></tr>
          <tr><th scope="row">Who may see it?</th><td>Permission filtering can be more important than maximum context size.</td></tr>
          <tr><th scope="row">How reliable is it?</th><td>Poor or conflicting source data can limit answer quality regardless of model capability.</td></tr>
          <tr><th scope="row">What must remain deterministic?</th><td>Business rules, authorization, transaction state, and hard validation may belong in application logic rather than model context.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="success-criteria" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Success criteria</p>
      <h2>Define two or three criteria that can change the recommendation.</h2>
      <p>Success criteria describe what “good enough” means for the workflow. Choose only criteria that matter to the task shape, output requirements, risk level, and how the result will be used.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Criterion</th><th scope="col">Useful when</th><th scope="col">Example evidence</th></tr></thead>
        <tbody>
          <tr><th scope="row">Task quality</th><td>The main concern is correctness, completeness, usefulness, or judgment quality.</td><td>Eval pass rate, human review result, field accuracy, ranking quality, or task-specific grader.</td></tr>
          <tr><th scope="row">Control and safety</th><td>The output or action can create material business, security, legal, or policy risk.</td><td>Critical-error rate, correct refusal or escalation, authorization compliance, safe tool behavior.</td></tr>
          <tr><th scope="row">Latency</th><td>The workflow is interactive or time-sensitive.</td><td>Time to first useful output and end-to-end completion time at expected load.</td></tr>
          <tr><th scope="row">Cost</th><td>The workflow runs at significant volume or has a strict operating budget.</td><td>Cost per completed case or per acceptable result, including retries where relevant.</td></tr>
          <tr><th scope="row">Format reliability</th><td>Another system consumes the result automatically.</td><td>Schema validity, required-field completeness, allowed-value compliance, business-rule validation.</td></tr>
          <tr><th scope="row">Tool success</th><td>The workflow depends on function calls or external systems.</td><td>Correct tool choice, valid arguments, successful completion, safe failure and retry behavior.</td></tr>
        </tbody>
      </table>
      <p>A criterion without a release consequence is just an interesting metric. State what result is acceptable, what requires review, and what disqualifies an option.</p>
    </div>

    <div class="ecg-decision-columns">
      <div>
        <h3>Good two-criterion example</h3>
        <p>For high-volume ticket classification, the decision may depend mainly on <strong>classification quality</strong> and <strong>cost per completed case</strong>. A larger model that improves wording but not routing quality adds little value.</p>
      </div>
      <div>
        <h3>Good three-criterion example</h3>
        <p>For an interactive policy assistant, the decision may depend on <strong>grounded answer quality</strong>, <strong>safe escalation on unsupported cases</strong>, and <strong>response latency</strong>.</p>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="eval-seed-set" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Eval seed set</p>
      <h2>Start small, but make the difficult cases visible.</h2>
      <p>An eval seed set is a small group of test cases that represents the workflow well enough to compare options. It should be small enough for the team to inspect manually and broad enough to expose failure modes that could change the recommendation.</p>
    </header>

    <div class="ecg-decision-columns">
      <div>
        <h3>Normal cases show baseline fit</h3>
        <p>Include realistic examples of the main workflow path. These cases show whether the model, prompt, context, retrieval, and output design can perform the work users will see most often.</p>
      </div>
      <div>
        <h3>Difficult cases reveal the decision boundary</h3>
        <p>Difficult cases show what happens when information is incomplete, the request is ambiguous, risk increases, the output format is strict, or the workflow depends on retrieval or tools.</p>
      </div>
    </div>

    <div class="research-canvas__table-wrap">
      <h3>Seed-set coverage</h3>
      <table>
        <thead><tr><th scope="col">Case type</th><th scope="col">What it tests</th><th scope="col">Expected behavior to define</th></tr></thead>
        <tbody>
          <tr><th scope="row">Typical case</th><td>The normal business path with representative inputs.</td><td>Produce the expected useful result with the required quality and format.</td></tr>
          <tr><th scope="row">Edge case</th><td>A valid but unusual input, limit, combination, or exception.</td><td>Handle the case without losing important constraints or silently degrading the result.</td></tr>
          <tr><th scope="row">Ambiguous input</th><td>More than one interpretation is plausible.</td><td>Ask for clarification, qualify the answer, or choose a safe bounded interpretation according to the workflow design.</td></tr>
          <tr><th scope="row">Missing information</th><td>A required field, fact, source, or business condition is absent.</td><td>Identify the gap instead of inventing the missing information.</td></tr>
          <tr><th scope="row">Sensitive or high-risk case</th><td>The consequence of an incorrect answer or action is materially higher.</td><td>Apply the required safeguard, review, refusal, or escalation path.</td></tr>
          <tr><th scope="row">Format-constrained case</th><td>The result must follow a schema, field list, allowed values, or another machine-readable contract.</td><td>Return a valid result or fail clearly when the required structure cannot be produced.</td></tr>
          <tr><th scope="row">Retrieval-dependent case</th><td>The answer depends on approved external or enterprise knowledge.</td><td>Use the right evidence, respect permissions, and show uncertainty when the required evidence is missing or conflicting.</td></tr>
          <tr><th scope="row">Tool-use case</th><td>The workflow must select or call a function, API, calculation, or enterprise action.</td><td>Choose the right tool, produce valid arguments, stay inside authority limits, and handle tool failure safely.</td></tr>
        </tbody>
      </table>
      <p>Not every workflow needs every category. Include the difficult cases that match the real task, risk, data, output, retrieval, and tool boundaries.</p>
    </div>

    <div class="research-canvas__table-wrap">
      <h3>Define each case before running it</h3>
      <table>
        <thead><tr><th scope="col">Case field</th><th scope="col">Capture</th></tr></thead>
        <tbody>
          <tr><th scope="row">Input</th><td>The user request, document, event, record, or other work object being tested.</td></tr>
          <tr><th scope="row">Approved context</th><td>The information, permissions, retrieval sources, state, and tools available for this case.</td></tr>
          <tr><th scope="row">Expected behavior</th><td>What a good result should do, including any required clarification, escalation, tool call, or output structure.</td></tr>
          <tr><th scope="row">Must not happen</th><td>A critical failure such as inventing a fact, crossing an access boundary, using the wrong tool, hiding uncertainty, or producing an invalid downstream payload.</td></tr>
          <tr><th scope="row">Grading signal</th><td>The success criterion, rule, human review, or automated check used to judge the result.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">dataset</span>
      <p><strong>Seed-set rule:</strong> do not make the first set large just to look rigorous. Make it representative enough to expose meaningful differences between options.</p>
      <p>When a pilot, review, or production trace reveals a new failure mode, add that case to the eval set. The seed set should grow from evidence, not from imagination alone.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="representative-examples" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Representative comparison</p>
      <h2>Compare options on the same work.</h2>
      <p>Representative examples help teams compare model classes, prompting, retrieval, structured outputs, tool-use behavior, safety behavior, latency, and cost without changing the test every time the preferred model changes.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <h3>What to hold constant</h3>
      <table>
        <thead><tr><th scope="col">Comparison area</th><th scope="col">Keep visible</th></tr></thead>
        <tbody>
          <tr><th scope="row">Inputs</th><td>Use the same representative normal, edge, ambiguous, and higher-risk examples.</td></tr>
          <tr><th scope="row">Output contract</th><td>Ask each option to produce the same business result or structured schema.</td></tr>
          <tr><th scope="row">Context</th><td>Keep approved source material and permissions equivalent unless retrieval strategy itself is under test.</td></tr>
          <tr><th scope="row">Tools</th><td>Compare the same tool catalog and authority boundary when tool behavior matters.</td></tr>
          <tr><th scope="row">Success criteria</th><td>Grade each option against the same two or three decision criteria.</td></tr>
          <tr><th scope="row">Operating signals</th><td>Record latency, token or resource use, retries, failures, and review burden where they affect the decision.</td></tr>
        </tbody>
      </table>
      <p>One impressive answer is weak evidence. A useful selection result explains where each option succeeds, where it fails, and which trade-off matters for the real workflow.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="workflow-examples" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Workflow examples</p>
      <h2>Different jobs create different model decisions.</h2>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Workflow</th><th scope="col">Likely starting point</th><th scope="col">What to prove</th></tr></thead>
        <tbody>
          <tr><th scope="row">Weekly project update drafting</th><td>General-purpose or efficient model with approved project context.</td><td>Useful summary quality, factual grounding, format consistency, and low review effort.</td></tr>
          <tr><th scope="row">Complex policy interpretation</th><td>Reasoning-oriented model plus retrieval from approved policy sources.</td><td>Correct interpretation, grounded evidence, uncertainty handling, and escalation on unsupported cases.</td></tr>
          <tr><th scope="row">Document and screenshot review</th><td>Multimodal model, possibly with structured output.</td><td>Extraction accuracy, missing-field handling, image understanding, and format reliability.</td></tr>
          <tr><th scope="row">High-volume service routing</th><td>Efficient model or classification approach.</td><td>Routing quality, latency, cost per case, and safe handling of uncertain requests.</td></tr>
          <tr><th scope="row">Voice service assistant</th><td>Audio or real-time model with scoped tools.</td><td>Conversation quality, latency, transcription or interpretation behavior, tool safety, and handoff quality.</td></tr>
          <tr><th scope="row">Enterprise semantic search</th><td>Embedding model plus retrieval and ranking.</td><td>Relevant candidate recall, ranking quality, permission filtering, and downstream answer quality if generation follows.</td></tr>
          <tr><th scope="row">ERP action assistant</th><td>General or reasoning-capable model plus tightly scoped tool use.</td><td>Correct tool selection, valid arguments, authorization, approval, transaction integrity, and safe recovery.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="lead-questions" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead lens</p>
      <h2>Questions that make model selection defensible.</h2>
    </header>

    <div class="ecg-decision-columns">
      <div>
        <h3>Workflow fit</h3>
        <ul>
          <li>What task must the AI perform?</li>
          <li>What must it produce?</li>
          <li>How much reasoning depth is actually required?</li>
          <li>Which modalities are involved?</li>
          <li>What context must be available?</li>
          <li>Does the workflow need tools, retrieval, ranking, or real-time interaction?</li>
        </ul>
      </div>
      <div>
        <h3>Production fit</h3>
        <ul>
          <li>What happens if the result is wrong?</li>
          <li>What latency is acceptable?</li>
          <li>What volume and cost structure must the design support?</li>
          <li>Which data, hosting, or deployment constraints matter?</li>
          <li>Which two or three criteria decide whether the option is good enough?</li>
          <li>Which representative eval cases will prove the choice?</li>
        </ul>
      </div>
    </div>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">record_voice_over</span>
      <p><strong>Assessment answer.</strong> I would not select an API model from a remembered name or one demo result. I would define the task, output, risk, reasoning depth, context, latency, cost, and scale. Then I would choose the smallest credible model class and any required retrieval, tool, safety, or deployment layers. I would define two or three success criteria and compare the options on the same representative eval set. The selected model is the one that meets the workflow requirement with the best acceptable production trade-off, not necessarily the most capable model available.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="primary-references" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Primary references</p>
      <h2>Verify current API details before implementation.</h2>
      <p>Model names, supported modalities, reasoning settings, pricing, limits, and regional availability can change. Use current vendor documentation when moving from model class to a concrete implementation choice.</p>
    </header>
    <div class="research-route-list">
      <a href="https://platform.openai.com/docs/models" target="_blank" rel="noopener"><span>01</span><strong>OpenAI model catalog</strong><small>Current model families, specialized models, embeddings, moderation, audio, real-time, and open-weight options.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://platform.openai.com/docs/api-reference/realtime" target="_blank" rel="noopener"><span>02</span><strong>Realtime API</strong><small>Low-latency multimodal and speech interaction.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://platform.openai.com/docs/api-reference/moderations" target="_blank" rel="noopener"><span>03</span><strong>Moderation API</strong><small>Classification of potentially harmful text and image inputs.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://platform.openai.com/docs/api-reference/vector-stores" target="_blank" rel="noopener"><span>04</span><strong>Vector stores and retrieval</strong><small>Semantic retrieval, ranking controls, and file-search infrastructure.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://platform.openai.com/docs/api-reference/evals" target="_blank" rel="noopener"><span>05</span><strong>Evals API</strong><small>Structured evaluation definitions, runs, graders, and comparison evidence.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Decision rule</p><h2>Keep the selection in seven moves.</h2></div>
    <ol>
      <li><span>01</span><strong>Task</strong><p>Define the business job and the output.</p></li>
      <li><span>02</span><strong>Risk</strong><p>Understand the consequence of a wrong result or action.</p></li>
      <li><span>03</span><strong>Capability</strong><p>Choose the smallest credible model class and supporting architecture.</p></li>
      <li><span>04</span><strong>Context</strong><p>Define what information, permissions, tools, and state the workflow needs.</p></li>
      <li><span>05</span><strong>Criteria</strong><p>Choose two or three measures that can change the recommendation.</p></li>
      <li><span>06</span><strong>Eval</strong><p>Build a small representative seed set and compare options under equivalent conditions.</p></li>
      <li><span>07</span><strong>Trade-off</strong><p>Select the option that meets quality and control needs at acceptable latency, cost, and scale.</p></li>
    </ol>
  </section>

  <div class="research-canvas__support" data-reveal>{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
