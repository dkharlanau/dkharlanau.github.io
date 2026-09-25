---
layout: default
title: "AI Model Selection — Model Classes, Context, Latency, Cost and Evals"
description: "A practical enterprise AI model-selection framework using stable capability classes, workflow fit, context, reasoning depth, latency, cost, scale, and representative evals."
permalink: /labs/business-ai/model-selection/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-24
last_reviewed: 2026-09-24
hide_global_cta: true
publication_wave: "business-ai-model-selection-01"
review_method: "current OpenAI primary documentation + nearby Labs review + full editorial rewrite"
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
    title: "Business AI Glossary — Plain Language for Discovery, Architecture, Governance and Delivery"
    url: "/labs/business-ai/glossary/"
# ai-discovery-managed:end
---
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li aria-current="page">Model Selection</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Business AI / model selection</p>
      <h1>Choose the job first.<br />Then choose the model.</h1>
      <p>A model is only one part of an AI workflow. The production choice also depends on the output contract, approved context, tools, reasoning settings, risk, latency, cost, and the evidence used to judge the result. Good model selection starts with the work and ends with a measured trade-off.</p>
      <a class="research-canvas__button" href="#selection-sequence">Follow the decision <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Model selection principle">
      <p>Selection principle</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Define</strong><small>Task and output</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Compare</strong><small>Credible candidates</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Prove</strong><small>Representative cases</small></div>
      <em>The strongest model is not automatically the best production choice.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal aria-label="Model selection boundary">
    <span class="material-symbols-outlined" aria-hidden="true">tune</span>
    <div>
      <p><strong>Separate three decisions.</strong> Model capability answers what the model can do. Runtime configuration answers how much reasoning, context, or output it should use. Workflow controls answer what data and tools it may access, what format it must return, and what still needs deterministic validation or human approval.</p>
      <p>If these are mixed together, teams often solve an architecture problem by buying a larger model. Sometimes that works. Often the real issue is missing context, a weak output contract, unsafe tool design, or poor evaluation.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="selection-sequence" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Selection sequence</p>
      <h2>Move from a business task to a measurable choice.</h2>
      <p>Do not start with a model name. Start with the result the workflow must produce and the cost of getting it wrong.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Step</th><th scope="col">Decision</th><th scope="col">What must be clear</th></tr></thead>
        <tbody>
          <tr><th scope="row">1. Task</th><td>Define the unit of work.</td><td>Input, expected result, frequency, user, and where the result goes next.</td></tr>
          <tr><th scope="row">2. Contract</th><td>Define what the system must return.</td><td>Free text, structured fields, ranking, tool request, audio, or another bounded output.</td></tr>
          <tr><th scope="row">3. Risk</th><td>Set the authority and failure boundary.</td><td>What an error can change, what must stay deterministic, and where review or escalation is required.</td></tr>
          <tr><th scope="row">4. Candidates</th><td>Choose a small set of credible model and configuration options.</td><td>Required reasoning, modalities, context, tools, speed, deployment constraints, and cost.</td></tr>
          <tr><th scope="row">5. Evaluation</th><td>Run the same representative work through each option.</td><td>Quality, critical failures, format or tool reliability, latency, and operating cost.</td></tr>
          <tr><th scope="row">6. Decision</th><td>Select the least complex option that meets the requirement.</td><td>Why it passed, which trade-off was accepted, and what would trigger a new evaluation later.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="model-classes" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Model capability</p>
      <h2>Use capability differences, not a permanent taxonomy of model names.</h2>
      <p>Product names and limits change. The useful question is which capability is needed for this task and whether a cheaper or faster option still meets the acceptance criteria.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Capability choice</th><th scope="col">When it matters</th><th scope="col">What to test</th></tr></thead>
        <tbody>
          <tr><th scope="row">General-purpose generation</th><td>Drafting, summarization, extraction, classification, and broad knowledge work.</td><td>Task quality and whether extra reasoning changes the result enough to justify its cost.</td></tr>
          <tr><th scope="row">Deeper reasoning</th><td>Ambiguous analysis, planning, multi-step technical work, or decisions with dependent constraints.</td><td>Whether a more capable model or higher reasoning effort reduces the failures that matter.</td></tr>
          <tr><th scope="row">Efficient inference</th><td>Frequent, well-bounded work where throughput, latency, or cost is important.</td><td>Whether the smaller or faster option stays above the required quality threshold on difficult cases.</td></tr>
          <tr><th scope="row">Modality support</th><td>The evidence includes images, documents, audio, or real-time interaction rather than text alone.</td><td>Quality on the actual modality, not a text-only proxy for it.</td></tr>
          <tr><th scope="row">Specialized representation or safety models</th><td>The system needs embeddings, moderation, speech, or another specialized capability rather than a general generated answer.</td><td>The metric appropriate to that component, such as retrieval quality, classification quality, or transcription accuracy.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">psychology</span>
      <div>
        <p><strong>Reasoning effort is a configuration choice as well as a model choice.</strong> Current APIs can expose several reasoning levels within the same model family. That means the comparison may be “same model, different effort” before it becomes “different model.”</p>
        <p>Keep the experiment practical: if a lower-effort setting passes the same cases with materially better latency or cost, extra reasoning is not automatically useful.</p>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="capabilities-and-architecture" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Workflow contract</p>
      <h2>Do not ask the model to solve controls that belong around it.</h2>
      <p>A stronger model cannot replace a missing permission check, an unstable source of truth, or a transaction rule. Keep those responsibilities visible in the application design.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Workflow concern</th><th scope="col">Where it belongs</th><th scope="col">Selection consequence</th></tr></thead>
        <tbody>
          <tr><th scope="row">Structured output</th><td>Schema and validation around the model response.</td><td>Test whether each candidate reliably produces the fields and allowed values the downstream system requires.</td></tr>
          <tr><th scope="row">Current or private knowledge</th><td>Approved retrieval or scoped tool access.</td><td>Evaluate model and retrieval together when the answer depends on enterprise evidence.</td></tr>
          <tr><th scope="row">Business action</th><td>Explicit tools, authorization, validation, and transaction controls.</td><td>Tool use is not business authority. Test tool choice and arguments separately from permission to execute.</td></tr>
          <tr><th scope="row">Safety and policy</th><td>Workflow rules, specialized filters where useful, and human escalation for material risk.</td><td>Measure critical failures and escalation behavior, not only average answer quality.</td></tr>
          <tr><th scope="row">Multi-step orchestration</th><td>Application or agent workflow with visible state and recovery boundaries.</td><td>Compare the whole path when model calls, retrieval, tools, and retries interact.</td></tr>
        </tbody>
      </table>
      <p>For the broader choice between retrieval, extraction, agentic orchestration, human review, and integration patterns, use the <a href="/labs/business-ai/architecture-patterns/">Architecture Patterns</a> guide. This page stays focused on selecting and proving the model configuration inside that architecture.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="selection-factors" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Production constraints</p>
      <h2>Context, latency, cost, and volume can change the winner.</h2>
      <p>A candidate that looks best in a small demo may be the wrong choice once the workflow runs every minute, waits on several tools, or needs access-controlled operational data.</p>
    </header>

    <div class="ecg-decision-columns">
      <div>
        <h3>Context</h3>
        <p>Decide what the model needs in the request and what should be retrieved only when required. More context is not automatically better: stale, conflicting, or unauthorized material can reduce quality or create risk.</p>
      </div>
      <div>
        <h3>Latency</h3>
        <p>Measure end-to-end time for the job, not only model inference. Retrieval, sequential calls, tools, validation, retries, and human review can dominate the user experience.</p>
      </div>
      <div>
        <h3>Cost and volume</h3>
        <p>Estimate cost per accepted business result. Include model usage and, when material, retrieval, tools, retries, infrastructure, and review effort. A small per-run difference matters more when the workflow is frequent.</p>
      </div>
    </div>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">speed</span>
      <div>
        <p><strong>Latency is an architecture property.</strong> Smaller models can help, but so can fewer sequential requests, shorter generated outputs, parallel work, caching, or removing an unnecessary model call entirely.</p>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="success-criteria" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Acceptance criteria</p>
      <h2>Measure what can change the release decision.</h2>
      <p>A useful comparison needs explicit acceptance criteria before the preferred model is known. Otherwise the team can keep adding metrics until the favorite option appears to win.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Criterion</th><th scope="col">Example measure</th><th scope="col">Why it matters</th></tr></thead>
        <tbody>
          <tr><th scope="row">Task quality</th><td>Correct classification, extraction accuracy, grounded answer quality, or human acceptance.</td><td>Shows whether the workflow solves the job rather than merely producing fluent text.</td></tr>
          <tr><th scope="row">Critical failures</th><td>Unsupported action, invented fact, wrong escalation, permission breach, or another must-not-happen event.</td><td>A low average error rate can still be unacceptable when one class of error has high impact.</td></tr>
          <tr><th scope="row">Contract reliability</th><td>Schema validity, required-field completeness, allowed-value compliance, or correct tool arguments.</td><td>Downstream automation depends on predictable interfaces.</td></tr>
          <tr><th scope="row">Latency</th><td>Time to first useful result and end-to-end completion time at expected load.</td><td>Interactive and time-sensitive workflows have a real response budget.</td></tr>
          <tr><th scope="row">Operating cost</th><td>Cost per accepted case or completed workflow.</td><td>It captures the useful outcome instead of optimizing one API call in isolation.</td></tr>
        </tbody>
      </table>
      <p>State the threshold as well as the metric. “We measure schema validity” is weaker than “an invalid payload blocks release.”</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="eval-seed-set" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Evaluation set</p>
      <h2>Use representative cases, including the cases most likely to change the decision.</h2>
      <p>Start with a small set that the team can inspect. Add production-like examples, difficult boundaries, and known failure modes. For tasks with an objective answer, keep a reference or human-labelled ground truth; for judgment-heavy work, define a review rubric before running the comparison.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Case type</th><th scope="col">Purpose</th><th scope="col">Expected behavior</th></tr></thead>
        <tbody>
          <tr><th scope="row">Typical</th><td>Represents the normal workload.</td><td>Complete the task correctly and in the required format.</td></tr>
          <tr><th scope="row">Difficult but valid</th><td>Tests ambiguity, long context, unusual combinations, or demanding reasoning.</td><td>Preserve the important constraints without inventing missing facts.</td></tr>
          <tr><th scope="row">Missing evidence</th><td>Tests whether the system knows when it cannot support an answer.</td><td>Ask, qualify, retrieve, or escalate according to the workflow rule.</td></tr>
          <tr><th scope="row">High-impact failure</th><td>Targets the error class that must be rare or impossible.</td><td>Apply the required refusal, review, authorization, or safe failure path.</td></tr>
          <tr><th scope="row">Tool or schema boundary</th><td>Tests machine-facing behavior.</td><td>Return valid structured output or a valid tool request without crossing the defined authority.</td></tr>
        </tbody>
      </table>
      <p>When a pilot or production trace reveals a new failure mode, turn it into a regression case. The evaluation set should become more realistic as the workflow learns where it actually breaks.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="representative-examples" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Fair comparison</p>
      <h2>Change one decision at a time where possible.</h2>
      <p>Comparisons become hard to interpret when the model, prompt, retrieval, tool catalog, and grader all change together. Keep the important conditions equivalent unless that layer is the thing being tested.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Hold visible</th><th scope="col">Reason</th></tr></thead>
        <tbody>
          <tr><th scope="row">Inputs</th><td>Run the same representative cases across the candidates.</td></tr>
          <tr><th scope="row">Output contract</th><td>Ask for the same business result and structure.</td></tr>
          <tr><th scope="row">Approved context</th><td>Keep sources and permissions equivalent unless retrieval is under test.</td></tr>
          <tr><th scope="row">Tools and authority</th><td>Use the same available functions and action boundary when tool behavior is compared.</td></tr>
          <tr><th scope="row">Grading</th><td>Apply the same acceptance criteria and critical-failure rules.</td></tr>
          <tr><th scope="row">Operating signals</th><td>Record latency, resource use, retries, and review burden beside quality.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="workflow-examples" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Examples</p>
      <h2>The same model is not the right starting point for every job.</h2>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Workflow</th><th scope="col">Reasonable starting point</th><th scope="col">What should decide the result</th></tr></thead>
        <tbody>
          <tr><th scope="row">High-volume ticket routing</th><td>An efficient model with a strict label contract.</td><td>Routing quality, uncertain-case handling, latency, and cost per accepted case.</td></tr>
          <tr><th scope="row">Policy question answering</th><td>A capable general or reasoning model with permission-aware retrieval.</td><td>Grounding, correct qualification or escalation, and response time.</td></tr>
          <tr><th scope="row">Document-to-ERP extraction</th><td>A model with the required document or image capability plus structured output and deterministic validation.</td><td>Field accuracy, missing-data handling, schema reliability, and correction effort.</td></tr>
          <tr><th scope="row">Complex incident analysis</th><td>A reasoning-capable model with reviewed evidence and no automatic production authority.</td><td>Quality of the evidence chain, uncertainty handling, critical factual errors, and analyst review effort.</td></tr>
          <tr><th scope="row">Enterprise semantic search</th><td>Embedding and ranking components, with generation only when the use case needs an answer.</td><td>Relevant retrieval, permission filtering, ranking quality, and downstream answer quality if generation is added.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="lead-questions" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Decision record</p>
      <h2>A model choice should be explainable after the demo is over.</h2>
      <p>Record the decision in a few sentences: the workflow and output contract, the candidates compared, the representative cases, the acceptance thresholds, the selected configuration, and the trade-off accepted. Also record the trigger for retesting—for example a new model family, a material cost change, a new failure mode, or a change in workload.</p>
    </header>
    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">fact_check</span>
      <div>
        <p><strong>Useful outcome:</strong> “Option B passed the required quality and critical-failure thresholds on the same case set, while reducing median end-to-end latency and cost per accepted case.”</p>
        <p><strong>Weak outcome:</strong> “Option B felt better in the demo.”</p>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="primary-references" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Current implementation references</p>
      <h2>Recheck concrete model details when you implement.</h2>
      <p>The framework above is deliberately stable. Model families, reasoning settings, supported tools, limits, pricing, and evaluation products change faster. The links below point to current OpenAI primary documentation as one concrete implementation reference; use equivalent primary documentation when another provider is under evaluation.</p>
    </header>
    <div class="research-route-list">
      <a href="https://developers.openai.com/api/docs/guides/model-selection" target="_blank" rel="noopener"><span>01</span><strong>Model selection</strong><small>Current model and reasoning-effort guidance for choosing between quality, latency, and cost.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://developers.openai.com/api/docs/models" target="_blank" rel="noopener"><span>02</span><strong>Model catalog</strong><small>Current capabilities, tools, context, limits, and model-specific details.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://developers.openai.com/api/docs/guides/structured-outputs" target="_blank" rel="noopener"><span>03</span><strong>Structured Outputs</strong><small>Schema-constrained responses and the limits of supported JSON Schema features.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://developers.openai.com/api/docs/guides/function-calling" target="_blank" rel="noopener"><span>04</span><strong>Function calling</strong><small>The model-to-application tool-call loop and tool definition contract.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://developers.openai.com/api/docs/guides/evaluation-best-practices" target="_blank" rel="noopener"><span>05</span><strong>Evaluation best practices</strong><small>How to design tests around production behavior and model variability.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://developers.openai.com/api/docs/guides/evaluation-getting-started" target="_blank" rel="noopener"><span>06</span><strong>Datasets for evaluation</strong><small>The current starting point for building and comparing evaluation cases.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://developers.openai.com/api/docs/guides/latency-optimization" target="_blank" rel="noopener"><span>07</span><strong>Latency optimization</strong><small>End-to-end levers including fewer requests, shorter outputs, parallel work, and simpler models.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://developers.openai.com/api/docs/guides/cost-optimization" target="_blank" rel="noopener"><span>08</span><strong>Cost optimization</strong><small>Cost and latency trade-offs, batching, flex processing, and smaller-model options.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</div>
