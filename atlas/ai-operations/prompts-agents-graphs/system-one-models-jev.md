---
layout: default
title: "Jev and System One Models: Fast Decisions Inside Software"
description: "A practical introduction to TypeSafe AI's Jev and System One Models: typed probabilistic decisions, confidence, workflow design, limits, and enterprise SAP use cases."
permalink: /atlas/ai-operations/prompts-agents-graphs/system-one-models-jev/
atlas_section: ai-operations
domain: Enterprise AI architecture
subdomain: Machine-native decision models
concept_type: emerging architecture pattern
status: reviewed
verified: true
level: 1
last_modified_at: 2026-09-21
author: Dzmitryi Kharlanau
robots: index,follow
sitemap: true
tags:
  - jev
  - system-one-models
  - typesafe-ai
  - decision-intelligence
  - enterprise-ai
  - sap-ai
  - workflow-automation
related:
  - /atlas/ai-operations/prompts-agents-graphs/architecture-selection-guide/
  - /atlas/automation/rule-based-automation-vs-ai/
  - /atlas/ai-operations/ai-agent-for-sap-support/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/ai-operations/">AI Operations</a></li>
    <li><a href="/atlas/ai-operations/prompts-agents-graphs/">Prompts → Agents → Graphs</a></li>
    <li aria-current="page">Jev and System One Models</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Emerging AI architecture · Checked 21 Sep 2026</p>
    <h1>Jev and System One Models: AI for decisions inside software</h1>
    <p class="note-subtitle">Most LLMs are built to produce useful language. Jev takes a different route: give software a fast, typed judgment that can be used directly in a workflow. The interesting idea is not another chatbot. It is a new place to put machine judgment between hard-coded rules and open-ended reasoning.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <div class="note-body">
    <h2>The idea in one minute</h2>
    <p>Imagine an SAP integration error arrives with message text, interface name, retry count, business object, system status, and recent technical history. A normal LLM can read the evidence and write a good explanation. But your program may not need a paragraph. It may need one bounded decision:</p>

    <pre><code>RETRY
BUSINESS_ERROR
TECHNICAL_ERROR
ESCALATE

+ probability / confidence</code></pre>

    <p>This is the space TypeSafe AI is targeting with <strong>System One Models</strong>. Its first public model, <strong>Jev</strong>, was announced on 15 September 2026 and is currently in early access.</p>

    <p>TypeSafe describes the interface as unstructured state in, typed probabilistic decisions out. In practical terms, the model reads context but does not need to generate a free-form answer. You define the possible shape of the decision first, and normal code decides what happens next.</p>

    <blockquote>Think of an LLM as an analyst who can write a memo. Think of Jev as a very fast judgment function inside the program.</blockquote>

    <h2>Why this is different from a normal LLM call</h2>
    <div class="decision-table">
      <table>
        <thead>
          <tr>
            <th>Question</th>
            <th>Typical LLM</th>
            <th>System One / Jev</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Primary output</td>
            <td>Generated text or structured text</td>
            <td>Typed decision</td>
          </tr>
          <tr>
            <td>Best fit</td>
            <td>Explain, write, reason, plan, transform</td>
            <td>Classify, score, route, judge, branch</td>
          </tr>
          <tr>
            <td>Answer space</td>
            <td>Usually very open</td>
            <td>Defined in advance</td>
          </tr>
          <tr>
            <td>Uncertainty</td>
            <td>Often added through prompting</td>
            <td>Probability is part of the result</td>
          </tr>
          <tr>
            <td>Control</td>
            <td>The model can produce many forms of output</td>
            <td>Code keeps the decision inside a known type</td>
          </tr>
          <tr>
            <td>Typical architecture role</td>
            <td>Reasoning or language component</td>
            <td>Fuzzy decision primitive inside a workflow</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>This does not make LLMs obsolete. It separates two jobs that are often mixed together: <strong>producing language</strong> and <strong>making a bounded judgment</strong>.</p>

    <h2>The gap between rules and agents</h2>
    <p>Enterprise systems already have millions of decisions. Most do not need an autonomous agent. Many are simple rules:</p>

    <pre><code>if delivery_block == true:
    stop_processing()</code></pre>

    <p>That is good architecture when the condition is exact. The problem appears when the decision is still bounded but the evidence is fuzzy:</p>

    <ul>
      <li>Does this customer message indicate an urgent business impact?</li>
      <li>Which support queue best matches this incident?</li>
      <li>Does this invoice exception look like a quantity issue, a price issue, or a document-quality issue?</li>
      <li>Is this integration failure probably transient or does it require investigation?</li>
      <li>How severe is the business impact described in this ticket?</li>
    </ul>

    <p>You can try to write hundreds of rules. You can also call a large reasoning model for every case. System One Models propose a third option: keep the workflow in code, but let a model make the small judgments that are difficult to express as deterministic rules.</p>

    <pre><code>Hard facts and rules
        ↓
Typed model judgments
        ↓
Code combines probabilities
        ↓
Branch / route / score / escalate
        ↓
LLM, agent, human, or deterministic action only when needed</code></pre>

    <p>This is why Jev is more interesting as an <strong>architecture primitive</strong> than as a standalone AI product.</p>

    <h2>Three basic question types</h2>
    <p>TypeSafe currently exposes three decision primitives. They are simple on purpose.</p>

    <h3>Choice — pick one option from a known set</h3>
    <p>Use Choice when the program needs one route from a predefined list.</p>
    <pre><code>Question:
What is the primary failure class?

Options:
- BUSINESS_DATA
- AUTHORIZATION
- TRANSIENT_TECHNICAL
- CONFIGURATION
- UNKNOWN</code></pre>
    <p>The response includes the selected choice, a probability distribution over the options, and confidence.</p>

    <h3>Score — place the case on a defined scale</h3>
    <p>Use Score when the answer is ordered rather than categorical.</p>
    <pre><code>How severe is the business impact?

1 = no operational impact
2 = small local impact
3 = important process delay
4 = major process disruption
5 = critical business outage</code></pre>
    <p>The scale is defined by the application, not invented by the model at runtime.</p>

    <h3>Noul — estimate whether a statement is true</h3>
    <p>Noul is TypeSafe's yes/no primitive. The useful result is the probability itself.</p>
    <pre><code>Does the evidence indicate that this error is safe to retry?

0.97 → strong yes
0.52 → uncertain
0.08 → strong no</code></pre>

    <p>TypeSafe's documentation recommends asking small, focused questions and combining the answers in code. If a judgment requires several factors, ask those factors separately instead of hiding the whole policy inside one giant prompt.</p>

    <h2>Confidence is part of the architecture</h2>
    <p>The important idea is not just that Jev returns a label. It returns a decision that software can treat as uncertain.</p>

    <p>A workflow can therefore have different paths:</p>

    <pre><code>high confidence + low-risk action
    → automatic route

medium confidence
    → recommendation + extra evidence

low confidence
    → human review or deeper LLM/agent analysis</code></pre>

    <p>The thresholds should come from your own evaluation data. Do not copy a universal number such as 0.90 or 0.95 and assume it is safe. A wrong decision in ticket routing is very different from a wrong decision that releases payment or changes production master data.</p>

    <h2>Where Jev can sit in an enterprise AI stack</h2>
    <p>A useful architecture is not “Jev instead of agents.” It is a layered system where each component gets the job it is good at.</p>

    <pre><code>Business event / API / IDoc / document
                ↓
     Deterministic extraction and checks
                ↓
        Jev / typed judgments
                ↓
     Policy thresholds and business rules
        ↙          ↓           ↘
 automatic     LLM / agent     human
   route        reasoning      review
        ↘          ↓           ↙
             controlled action
                    ↓
             post-action check</code></pre>

    <p>Rules still own exact constraints. Jev can handle bounded ambiguity. An LLM can explain or reason about complex cases. An agent can investigate when the next step depends on tools and observations. A human remains responsible where the risk or uncertainty requires it.</p>

    <h2>A SAP example: integration exception routing</h2>
    <p>Consider an enterprise landscape with APIs, IDocs, events, queues, AIF monitoring, and several business systems. Support teams often spend time on a basic question before they can solve the issue: <em>what kind of problem is this?</em></p>

    <p>The system can first collect a state object:</p>

    <pre><code>interface: CUSTOMER_REPLICATION
object: Business Partner
direction: inbound
error_text: "..."
retry_count: 3
http_status: 500
previous_success: 12 minutes ago
same_error_count_1h: 47
business_key_exists: true
authorization_check: passed
queue_status: blocked</code></pre>

    <p>Then several bounded judgments can run:</p>

    <ul>
      <li><strong>Choice:</strong> business data, authorization, configuration, transient technical, infrastructure, unknown.</li>
      <li><strong>Noul:</strong> is an automatic retry likely to be safe?</li>
      <li><strong>Score:</strong> how severe is the current business impact?</li>
      <li><strong>Noul:</strong> is this pattern similar to a known recurring incident?</li>
    </ul>

    <p>Normal code can combine those answers with deterministic facts. For example, even a strong “retry” probability should not override a policy that blocks automatic retries after a certain number of attempts or for a sensitive business object.</p>

    <p>The result is not an AI that “runs SAP.” It is a decision layer that can reduce repetitive triage while keeping the real control logic explicit.</p>

    <h2>Candidate SAP and ERP use cases</h2>
    <p>These are architecture candidates, not claims that Jev has an out-of-the-box SAP integration.</p>

    <div class="decision-table">
      <table>
        <thead>
          <tr>
            <th>Area</th>
            <th>Bounded judgment</th>
            <th>Possible next step</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Integration / AIF</td>
            <td>Classify exception and retry safety</td>
            <td>Retry, route, or escalate</td>
          </tr>
          <tr>
            <td>Sales</td>
            <td>Classify order exception or customer intent</td>
            <td>Choose workflow or support queue</td>
          </tr>
          <tr>
            <td>Procurement</td>
            <td>Judge mismatch type or document quality</td>
            <td>Hold, request correction, or continue review</td>
          </tr>
          <tr>
            <td>Invoice processing</td>
            <td>Score risk and categorize discrepancy</td>
            <td>Send to AP specialist or standard path</td>
          </tr>
          <tr>
            <td>Master data</td>
            <td>Classify suspected anomaly</td>
            <td>Auto-route to the right data owner</td>
          </tr>
          <tr>
            <td>AMS / support</td>
            <td>Estimate severity, domain, and likely incident family</td>
            <td>Prioritize and enrich the ticket</td>
          </tr>
          <tr>
            <td>Agent governance</td>
            <td>Judge whether an agent trace needs review</td>
            <td>Close, queue, or escalate the run</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2>Rules vs Jev vs LLM vs agent</h2>
    <div class="decision-table">
      <table>
        <thead>
          <tr>
            <th>Use</th>
            <th>When it fits</th>
            <th>Example</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Deterministic rule</td>
            <td>The condition is exact and explainable in code</td>
            <td>Block posting when a required field is empty</td>
          </tr>
          <tr>
            <td>Jev / typed decision model</td>
            <td>The answer space is known but the evidence needs judgment</td>
            <td>Classify the likely incident family</td>
          </tr>
          <tr>
            <td>LLM</td>
            <td>You need language, synthesis, explanation, or deeper reasoning</td>
            <td>Explain the probable root cause with evidence</td>
          </tr>
          <tr>
            <td>Agent</td>
            <td>The next step cannot be fully planned because new observations change the path</td>
            <td>Inspect logs, query tools, compare configuration, then decide the next diagnostic step</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>A strong enterprise design can use all four. The mistake is asking one technology to do every job.</p>

    <h2>What “zero hallucinations” does — and does not — mean</h2>
    <p>This claim needs careful translation.</p>

    <p>TypeSafe markets Jev as having zero hallucinations and guarantees that the answer matches the declared schema. If your Choice allows only five values, Jev will not suddenly return a sixth invented value or a paragraph that your application cannot parse. TypeSafe states that this schema matching is guaranteed rather than measured empirically.</p>

    <p>That is valuable, but it is <strong>not the same as guaranteeing a correct business decision</strong>. A model can return a perfectly valid value such as <code>TRANSIENT_TECHNICAL</code> and still be wrong about the incident.</p>

    <p>The safe interpretation is:</p>

    <pre><code>Type safety: guaranteed output shape
Decision quality: must be evaluated</code></pre>

    <p>This distinction matters for enterprise architecture. Reliable syntax removes one class of failure. It does not remove the need for domain evaluation, controls, fallback paths, and human accountability.</p>

    <h2>Performance claims: interesting, but test them locally</h2>
    <p>As of 21 September 2026, TypeSafe reports end-to-end Jev response times around 70–500 ms for its service and an input price of $0.042 per million tokens. The company also publishes workflow comparisons showing much larger speed and cost advantages over selected LLM configurations.</p>

    <p>These numbers are useful signals, not universal production guarantees. TypeSafe itself notes that some published gains are at the high end, that its workflow evaluations were created internally, and that the product is still in early access.</p>

    <p>For an enterprise decision, benchmark on your own cases:</p>

    <ul>
      <li>decision accuracy against reviewed historical cases;</li>
      <li>calibration: does higher confidence really mean higher correctness?</li>
      <li>false-positive and false-negative cost;</li>
      <li>latency at your region and workload;</li>
      <li>cost at real context sizes;</li>
      <li>stability across similar inputs;</li>
      <li>human-review rate after thresholds are applied;</li>
      <li>behavior on unknown or out-of-scope cases.</li>
    </ul>

    <h2>A useful pilot design</h2>
    <p>Do not start by replacing a production decision. Start with a shadow evaluation.</p>

    <ol>
      <li><strong>Choose one bounded decision.</strong> For example, classify integration incidents into five support routes.</li>
      <li><strong>Collect historical cases.</strong> Keep the original evidence and the final human resolution.</li>
      <li><strong>Create a deterministic baseline.</strong> Measure what current rules already solve.</li>
      <li><strong>Compare approaches.</strong> Test rules, structured LLM output, and Jev on the same cases.</li>
      <li><strong>Measure probabilities, not only labels.</strong> Check whether confidence can support useful automation thresholds.</li>
      <li><strong>Run in shadow mode.</strong> Record decisions without changing production state.</li>
      <li><strong>Automate only a low-risk slice.</strong> Keep a clear fallback and observe the post-decision result.</li>
    </ol>

    <p>This is a much stronger pilot than a demo where ten examples look convincing on screen.</p>

    <h2>Why the idea matters even if Jev itself changes</h2>
    <p>Jev is new. The product, API, pricing, and benchmark picture can change quickly. But the architectural idea is broader and worth keeping:</p>

    <blockquote>Not every intelligent step needs a chatbot or an agent. Some steps need a small, typed, probabilistic judgment that software can compose with normal code.</blockquote>

    <p>This creates a useful middle layer between brittle rules and expensive open-ended reasoning. If the category develops, enterprise AI may become less about putting one general model everywhere and more about composing different kinds of intelligence.</p>

    <h2>SAP Lead assessment takeaway</h2>
    <p>A concise way to explain the concept in an architecture discussion is:</p>

    <blockquote>“I would not use a generative agent for every uncertain decision. If the output is bounded — route, score, classify, yes/no — I would consider a typed decision model. Deterministic rules keep hard constraints, the decision model handles fuzzy judgment, and an LLM or agent is used only when deeper reasoning or tool-driven investigation is needed. Confidence becomes part of the control flow, but the business decision still needs evaluation and governance.”</blockquote>

    <p>That answer shows the important distinction: <strong>AI architecture is not a choice between rules and agents. It is a choice of the smallest reliable intelligence primitive for each step.</strong></p>

    <h2>Primary sources and current boundary</h2>
    <ul>
      <li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev" target="_blank" rel="noopener noreferrer">TypeSafe AI — Introducing System One Models &amp; Jev</a>, 15 Sep 2026.</li>
      <li><a href="https://docs.typesafe.ai/primitives" target="_blank" rel="noopener noreferrer">TypeSafe AI Docs — Primitives (Choice, Score, Noul)</a>.</li>
      <li><a href="https://evals.typesafe.ai/" target="_blank" rel="noopener noreferrer">TypeSafe AI — Workflow evaluations</a>.</li>
    </ul>
    <p><strong>Boundary:</strong> Jev is an early-access product. Vendor performance and cost claims above are reported as TypeSafe claims, not independently reproduced results. SAP examples on this page are architecture patterns designed for learning; they are not SAP product features or prebuilt Jev integrations.</p>

    <h2>Continue</h2>
    <p>Return to <a href="/atlas/ai-operations/prompts-agents-graphs/">From Prompts to Operational Intelligence</a>, compare this pattern with <a href="/atlas/automation/rule-based-automation-vs-ai/">Rule-Based Automation vs AI</a>, or use the <a href="/atlas/ai-operations/prompts-agents-graphs/architecture-selection-guide/">architecture selection guide</a> to decide where a typed decision model belongs.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/ai-operations/prompts-agents-graphs/architecture-selection-guide/">Architecture Selection Guide</a></li>
      <li><a href="/atlas/automation/rule-based-automation-vs-ai/">Rule-Based Automation vs AI</a></li>
      <li><a href="/atlas/ai-operations/ai-agent-for-sap-support/">AI Agent for SAP Support</a></li>
      <li><a href="/atlas/ai-operations/prompts-agents-graphs/closed-loop-enterprise-ai/">Verified Closed-Loop Enterprise AI</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
