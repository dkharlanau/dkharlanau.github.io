---
layout: default
title: "Codex Pilot Operating Model — Context, Runtime, Evidence, and Accountability"
description: "An architect's practical guide to converting a qualified software delivery opportunity into a bounded, reviewable Codex pilot, with a fictional SAP/ABAP case and evidence gates."
permalink: /labs/business-ai/software-delivery-discovery/operating-model/
status: reviewed
verified: false
robots: index,follow
sitemap: true
last_modified_at: 2026-11-26
tags: [enterprise-ai, codex, software-delivery, operating-model, governance, sap, architecture]
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li><a href="/labs/business-ai/software-delivery-discovery/">AI Delivery Discovery</a></li><li aria-current="page">Pilot Operating Model</li></ol></nav>
<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise AI / Architecture playbook</p>
      <h1>A promising use case<br>is not a pilot plan.</h1>
      <p>Discovery identifies work worth improving. An operating model explains where an engineering agent can work, which information it may use, what people must approve, and what evidence will justify the next decision. Design that boundary before selecting a Codex client.</p>
      <a class="research-canvas__button" href="#three-lenses">Examine the operating model <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <div>
      <p><strong>Architecture principle:</strong> begin with a recurring, measurable engineering task; then decide which context, execution environment, control points, and evidence it requires. A local editor, terminal, desktop client, or managed cloud environment is a delivery choice, not the business requirement.</p>
      <p><strong>Safety boundary:</strong> product permissions, regulatory obligations, and technical controls must be checked against the customer's actual environment. The patterns below are design guidance, not a claim that a setting is enabled or a specific compliance requirement is met.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="opportunity-to-operations" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Handoff / From sales qualification to design</p>
      <h2>Replace enthusiasm with operating decisions</h2>
      <p>An opportunity brief may explain why the customer wants better delivery. Before an architect recommends a pilot, the customer and delivery team must agree how the selected work can be performed and accepted.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">The opportunity says</th><th scope="col">The pilot decision must establish</th></tr></thead>
        <tbody>
          <tr><th scope="row">We lose time in testing and reviews.</th><td>Which specific repeated task can be reproduced and measured?</td></tr>
          <tr><th scope="row">Our developers want to try an agent.</th><td>Which team has working practices, reviewers, and an owner suitable for an initial evaluation?</td></tr>
          <tr><th scope="row">We have relevant code and documentation.</th><td>Which of those sources are necessary, approved, current, and accessible in the intended environment?</td></tr>
          <tr><th scope="row">We expect productivity improvements.</th><td>Which accepted-result metrics and quality guardrails will test that expectation?</td></tr>
          <tr><th scope="row">We eventually want many teams to use it.</th><td>What justifies expanding beyond the first workflow, and who approves each change in scope?</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="workflow-first-visual" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Architecture framing / Visual comparison</p>
      <h2>From a feature demo to a controlled delivery practice</h2>
      <p>The product capability may be identical in both conversations. What changes is the reasoning: start with the work that needs to improve, define an agent-sized contribution, and decide how engineers will verify it.</p>
    </header>
    <div class="ecg-decision-columns" aria-label="Feature-led and workflow-led engineering conversations">
      <div>
        <h3>Feature-first conversation</h3>
        <p><strong>Starting point:</strong> What can the agent demonstrate?</p>
        <ol>
          <li>Show that it can inspect repository files.</li>
          <li>Demonstrate code editing and test execution.</li>
          <li>Present review suggestions.</li>
          <li>Compare editor, terminal, and cloud options.</li>
          <li>Suggest broad adoption after a successful demo.</li>
        </ol>
        <p><strong>Missing:</strong> the customer bottleneck, acceptance standards, action boundaries, and accountable reviewer are still undefined.</p>
      </div>
      <div>
        <h3>Workflow-first conversation</h3>
        <p><strong>Starting point:</strong> Which engineering job repeatedly creates delay?</p>
        <ol>
          <li>Trace a recent change and identify the costly handoff.</li>
          <li>Choose a narrow task with relevant repository context.</li>
          <li>Specify the exact artifact the agent may prepare.</li>
          <li>Require test evidence, open questions, and human review.</li>
          <li>Choose an execution surface that fits access and risk.</li>
        </ol>
        <p><strong>Decision:</strong> compare accepted work, reviewer effort, and quality before considering wider use.</p>
      </div>
    </div>
    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span>
      <div>
        <p><strong>The shift:</strong> product capability → delivery bottleneck → bounded agent task → independent verification → accountable decision.</p>
        <p>The agent does not acquire release authority just because it can prepare a correct-looking patch or review summary.</p>
      </div>
    </div>
    <div class="research-canvas__table-wrap">
      <h3>Example: prepare a pull request for engineering review</h3>
      <table>
        <thead><tr><th scope="col">Operating element</th><th scope="col">Hypothetical SAP enhancement example</th></tr></thead>
        <tbody>
          <tr><th scope="row">Problem</th><td>Reviewers spend repeated cycles reconstructing why a mapping rule changed and whether tests cover the affected fields.</td></tr>
          <tr><th scope="row">Agent's limited job</th><td>Read the approved change request and repository diff; draft an intent summary, highlight uncertain logic, and identify missing test evidence.</td></tr>
          <tr><th scope="row">Workflow requirement</th><td>Provide the expected field behavior, test references, and unverified assumptions before a reviewer is asked to approve the change.</td></tr>
          <tr><th scope="row">Human responsibility</th><td>The assigned engineer confirms the business logic, checks the proposed findings, and decides whether the change may proceed.</td></tr>
          <tr><th scope="row">Evaluation</th><td>Measure review preparation effort, useful findings, false alarms, rework, and time to an accepted change against a comparable baseline.</td></tr>
        </tbody>
      </table>
    </div>
    <blockquote><p>“Rather than evaluating Codex on a general coding demonstration, I suggest trying it on one recurring review-preparation task. We can provide the approved change context, ask for an inspectable review package, and have the engineering owner validate its usefulness. That will show whether the workflow improves without changing approval authority.”</p></blockquote>
  </section>

  <section class="research-canvas__inventory" id="three-lenses" data-reveal>
    <header><p class="research-canvas__eyebrow">Three operating lenses</p><h2>Context, execution, and evidence are separate design problems</h2></header>
    <div class="ecg-decision-columns">
      <div>
        <h3>01 / Context: what the agent can use</h3>
        <p>Define the smallest set of repository files, task descriptions, conventions, policies, test data, and previous decisions that make the work understandable. Relevance is as important as availability.</p>
        <p><strong>Ask:</strong> What is essential? What is stale? What is sensitive? What belongs outside this evaluation? Who confirms that the supplied context is correct?</p>
        <p><strong>SAP example:</strong> a mapping change may need source code, a field-rule specification, and sanitized IDoc examples, but not full customer master extracts.</p>
      </div>
      <div>
        <h3>02 / Runtime: where the work happens</h3>
        <p>Determine whether the task requires a local developer session, known terminal tools, a visual desktop workflow, or a prepared cloud project environment. An agent can only test dependencies it can actually access in that environment.</p>
        <p><strong>Ask:</strong> Which files, tools, networks, and credentials are needed? Which commands or changes need approval? What must the agent never change?</p>
        <p><strong>Boundary:</strong> preparing a cloud task does not make a developer's inaccessible local SAP system or private dependency magically available.</p>
      </div>
    </div>
    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">fact_check</span>
      <div>
        <h3>03 / Evidence: what people can inspect</h3>
        <p>The useful outcome is not “the agent finished.” It is a traceable, reviewable change with enough information for a responsible engineer to accept, correct, or reject it.</p>
        <p><strong>Ask:</strong> What diff or artifact is expected? Which tests ran? Which checks could not run? Who reviews? Where are decisions and problems recorded? How will the team detect worsening quality or hidden review effort?</p>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="pilot-candidate" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Pilot selection / Practical filter</p>
      <h2>Choose an experiment you can learn from</h2>
      <p>A good first task is not necessarily the one with the biggest theoretical savings. Choose a useful workflow that the team can run repeatedly, contain, and judge.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table><thead><tr><th scope="col">Filter</th><th scope="col">What good evidence looks like</th><th scope="col">Poor candidate</th></tr></thead><tbody>
        <tr><th scope="row">Recurring</th><td>Recent examples show similar work happens regularly.</td><td>A single unusual production emergency.</td></tr>
        <tr><th scope="row">Scoped</th><td>A specific repository, branch, task, and change limit are known.</td><td>“Improve everything in the codebase.”</td></tr>
        <tr><th scope="row">Inspectable</th><td>An engineer can understand and challenge the generated artifact.</td><td>Opaque changes with no identifiable reviewer.</td></tr>
        <tr><th scope="row">Testable</th><td>Relevant checks, examples, or review criteria exist.</td><td>No feasible way to determine whether the result is right.</td></tr>
        <tr><th scope="row">Worthwhile</th><td>Observed effort, quality problems, or delivery delays warrant the experiment.</td><td>A demo with no owner or operational consequence.</td></tr>
      </tbody></table>
    </div>
    <p>These are candidate selection criteria, not evidence that Codex will outperform the existing workflow. That conclusion requires an evaluation with a fair baseline and quality safeguards.</p>
  </section>

  <section class="research-canvas__inventory" id="responsibility-split" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Accountability / Design before delegation</p>
      <h2>Give decisions to people, rules to the workflow, and bounded work to the agent</h2>
      <p>This split avoids two failures: expecting a model to enforce a business approval policy, and forcing engineers to manually repeat work the agent could prepare safely.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table><thead><tr><th scope="col">Owner</th><th scope="col">Responsibility</th><th scope="col">Example: code review preparation</th></tr></thead><tbody>
        <tr><th scope="row">Human</th><td>Choose tasks, resolve ambiguity, decide acceptance, approve or reject changes, and own escalation.</td><td>Responsible reviewer signs off on a proposed fix; authorized team merges it.</td></tr>
        <tr><th scope="row">Workflow and platform</th><td>Implement access restrictions, branch policy, required evidence, approval steps, and audit or retention expectations where supported.</td><td>Required checks and repository protections apply independently of agent instructions.</td></tr>
        <tr><th scope="row">Agent</th><td>Investigate a defined problem, prepare a diff, draft tests or a review summary, and report limitations.</td><td>Flag likely gaps and explain the code path without deciding that the change is production-ready.</td></tr>
      </tbody></table>
    </div>
    <p><strong>Do not confuse permissions:</strong> being technically able to call a tool or write a branch does not grant organizational authority to submit an approval, merge a PR, release a transport, or change a productive system.</p>
  </section>

  <section class="research-canvas__inventory" id="select-runtime" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Execution / Match the environment to the job</p>
      <h2>Pick a Codex surface after the task is understood</h2>
      <p>Available clients and workspace controls evolve. Confirm current support for the intended account, operating system, integrations, and task type before making a product recommendation.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table><thead><tr><th scope="col">Potential surface</th><th scope="col">When it may fit</th><th scope="col">Question before choosing</th></tr></thead><tbody>
        <tr><th scope="row">IDE integration</th><td>An engineer stays in the editor while investigating code and inspecting edits.</td><td>How do local project access, user review, and approval settings apply?</td></tr>
        <tr><th scope="row">Codex CLI</th><td>Work involves terminal inspection, repository commands, or reproducible scripts.</td><td>Which working directory, commands, sandbox policy, model setting, and approvals are effective?</td></tr>
        <tr><th scope="row">ChatGPT desktop Codex experience</th><td>A developer wants to organize project threads, local tasks, or supported remote work visually.</td><td>Which features and workspace permissions are available on the chosen platform?</td></tr>
        <tr><th scope="row">Codex Cloud</th><td>A task can run with an explicitly prepared environment and return results for review.</td><td>Are the repository, dependencies, services, credentials, and network requirements supported and approved?</td></tr>
        <tr><th scope="row">Integration or API-based workflow</th><td>The organization needs repeatable tasks integrated into a defined engineering process.</td><td>Which orchestration, review, audit, access, and failure-handling responsibilities move into the integration?</td></tr>
      </tbody></table>
    </div>
    <p><strong>Current product fact:</strong> OpenAI documents Codex CLI, IDE extension, desktop, and cloud experiences. Managed workspaces can govern local and cloud access separately. Cloud tasks use a prepared environment and isolated working state. Specific options, approvals, and availability remain release- and workspace-dependent.</p>
    <p>Verify against <a href="https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan">Codex clients and workspace access</a> and <a href="https://help.openai.com/en/articles/20001545-using-codex-cloud">Codex Cloud environments</a>, rather than relying on a fixed feature matrix.</p>
  </section>

  <section class="research-canvas__inventory" id="minimum-safeguards" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Pilot boundary / Minimum decision record</p>
      <h2>Write down the rules before the first delegated task</h2>
      <p>Keep the pilot small enough that the team knows what happened, what could go wrong, and how to stop. The checklist is a starting point for the authorized technical and security owners, not a substitute for their approval.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table><thead><tr><th scope="col">Decision</th><th scope="col">Example evidence or control question</th></tr></thead><tbody>
        <tr><th scope="row">Scope</th><td>Which team, repository, task type, working branch, and environment are included?</td></tr>
        <tr><th scope="row">Allowed context</th><td>Which files, specifications, test cases, and instructions are necessary and approved?</td></tr>
        <tr><th scope="row">Excluded context</th><td>Which customer data, secrets, systems, repositories, and private endpoints must stay outside?</td></tr>
        <tr><th scope="row">Expected artifact</th><td>What diff, report, test result, or review package must the agent return?</td></tr>
        <tr><th scope="row">Verification</th><td>Which automated checks and human criteria determine success or failure?</td></tr>
        <tr><th scope="row">Approval authority</th><td>Who can accept a change, publish review feedback, merge code, or release a transport?</td></tr>
        <tr><th scope="row">Action restrictions</th><td>Which commands, tool connections, network operations, or side effects are prohibited or need approval?</td></tr>
        <tr><th scope="row">Escalation</th><td>Who responds to missing context, failed checks, unexpected changes, or sensitive-data concerns?</td></tr>
        <tr><th scope="row">Visibility</th><td>What task, access, review, cost, incident, and outcome evidence must be recorded? Which product surfaces supply it?</td></tr>
        <tr><th scope="row">Value and stop rule</th><td>What baseline, target, quality threshold, and failure threshold govern the decision to continue?</td></tr>
      </tbody></table>
    </div>
    <p><strong>Mandatory review:</strong> bring in a technical, platform, or security specialist when the task requires new access, managed/cloud execution, sensitive information, elevated permissions, non-reversible actions, policy reporting, or unclear approval ownership. Record unresolved issues explicitly; do not present them as completed safeguards.</p>
  </section>

  <section class="research-canvas__inventory" id="sap-pilot-example" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Worked example / SAP implementation simulation</p>
      <h2>Evaluate an ABAP mapping regression without exposing customer data</h2>
      <p>A fictional S/4HANA migration team repeatedly investigates inbound customer mapping changes. The proposed first pilot is not to automate the migration. It is to prepare and review regression evidence for one mapping rule with a known expected result.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table><thead><tr><th scope="col">Operating element</th><th scope="col">Pilot design choice</th></tr></thead><tbody>
        <tr><th scope="row">Business aim</th><td>Reduce rework before validation of customer master interfaces.</td></tr>
        <tr><th scope="row">Agent task</th><td>Inspect a versioned, approved code excerpt and sanitized test fixtures; propose additional tests for a defined field-retention rule.</td></tr>
        <tr><th scope="row">Context limit</th><td>Only the relevant specification, enhancement code, and non-customer fixture; no production customer data, credentials, or uncontrolled SAP access.</td></tr>
        <tr><th scope="row">Runtime choice</th><td>Begin in the engineer's controlled repository environment if the local test harness is required; consider cloud only after environment and access fit are proven.</td></tr>
        <tr><th scope="row">Verification evidence</th><td>Proposed diff, test cases, executed checks where possible, assumptions, and explicit untested dependencies.</td></tr>
        <tr><th scope="row">Human owner</th><td>ABAP developer evaluates code; SAP functional lead checks business behavior; normal release authority remains unchanged.</td></tr>
        <tr><th scope="row">Stop condition</th><td>Missing test system, incomplete mapping specification, unexpected access request, or inability to verify a critical result.</td></tr>
        <tr><th scope="row">Evaluation measure</th><td>Total time until a review-accepted result, human correction effort, and regression quality against the team's baseline.</td></tr>
      </tbody></table>
    </div>
    <p><strong>Non-negotiable distinction:</strong> a passing local unit test does not by itself prove S/4HANA business behavior, organizational customization, or transport readiness. When the necessary SAP validation is unavailable, label the result as not verified.</p>
  </section>


  <section class="research-canvas__inventory" id="collaboration-patterns" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Engineering collaboration / Match autonomy to the task</p>
      <h2>Not every task should be delegated</h2>
      <p>Useful AI collaboration is a choice about the amount of human steering, not simply a choice of product. Start from how uncertain the work is, how easily it can be verified, and how costly a wrong action would be.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Pattern</th><th scope="col">When it helps</th><th scope="col">Human role</th><th scope="col">Failure to watch</th></tr></thead>
        <tbody>
          <tr><th scope="row">Local suggestion</th><td>Small mechanical edits where the developer already knows the target.</td><td>Engineer chooses and applies each suggestion.</td><td>Speeding up typing while ignoring the real delivery constraint.</td></tr>
          <tr><th scope="row">Interactive investigation</th><td>Debugging, unfamiliar code, or requirements that need frequent clarification.</td><td>Engineer guides each step and adjusts the hypothesis.</td><td>Exploration expands beyond the relevant system or change.</td></tr>
          <tr><th scope="row">Evidence preparation</th><td>Review summaries, test inventories, and documentation needed at an approval checkpoint.</td><td>Reviewer checks the facts and makes the decision.</td><td>Unverified statements become authoritative review evidence.</td></tr>
          <tr><th scope="row">Bounded delegation</th><td>A reproducible, multi-step job with a known result and reliable checks.</td><td>Owner defines limits; reviewer validates changes and exceptions.</td><td>Missing dependencies or broad permissions create false confidence.</td></tr>
          <tr><th scope="row">Human-only decision</th><td>Production release approval, ambiguous business policy, and high-impact unresolved risks.</td><td>Authorized people make the decision using suitable evidence.</td><td>Agents are mistakenly given authority they do not hold.</td></tr>
        </tbody>
      </table>
    </div>
    <p><strong>Practical heuristic:</strong> more autonomy requires clearer objectives, stricter action boundaries, stronger verification, and a definite path back to a person. Do not treat all five patterns as separate Codex products: they describe ways of working.</p>
  </section>

  <section class="research-canvas__inventory" id="task-brief" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Reusable skill / Task design</p>
      <h2>Give the agent a result to reach and a boundary it must respect</h2>
      <p>“Please fix the test suite” does not tell an engineer or agent what is broken, which files may change, or when to stop. A strong task brief is concise but precise enough to distinguish investigation from approved implementation.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Brief field</th><th scope="col">Decision to make explicit</th><th scope="col">SAP example: IDoc field rule</th></tr></thead>
        <tbody>
          <tr><th scope="row">Result</th><td>What observable condition would make the work complete?</td><td>Explain why one retained customer field is overwritten in a reproducible test.</td></tr>
          <tr><th scope="row">Evidence sources</th><td>Which code, tickets, logs, requirements, and conventions are authoritative?</td><td>Approved mapping rule, enhancement implementation, sample IDoc, and existing tests.</td></tr>
          <tr><th scope="row">Change boundary</th><td>Which files and operations are permitted, and which are forbidden?</td><td>Initially inspect only; no changes to business mappings or productive SAP data.</td></tr>
          <tr><th scope="row">Deliverable</th><td>What report, patch, test proposal, or question list is expected?</td><td>Likely failing path, evidence references, minimal change options, and unresolved questions.</td></tr>
          <tr><th scope="row">Proof and handoff</th><td>Which checks can run, who validates them, and what must trigger escalation?</td><td>Existing ABAP tests where available, functional sign-off on rule interpretation, and explicit unverified system dependencies.</td></tr>
        </tbody>
      </table>
    </div>
    <div class="ecg-decision-columns">
      <div>
        <h3>Phase A — Investigate without editing</h3>
        <p>“Inspect the approved mapping rule and related implementation. Trace the failing scenario and explain the most likely cause with source references. Do not edit files or change any rule. Report missing system context and recommend a narrow validation test.”</p>
        <p><strong>Checkpoint:</strong> the owner confirms the diagnosis and decides whether the change is authorized.</p>
      </div>
      <div>
        <h3>Phase B — Prepare an authorized patch</h3>
        <p>“Only after approval, update the agreed implementation and associated tests. Preserve unrelated mappings and existing interfaces. Return the diff, executed checks, failures, and anything that could not be tested. Stop before publishing or merging.”</p>
        <p><strong>Checkpoint:</strong> a human checks both the technical change and intended SAP behavior.</p>
      </div>
    </div>
    <p><strong>Important:</strong> a no-edit instruction remains in force until the owner changes the task. A request for a diagnosis never implicitly grants permission to refactor, push, merge, alter configuration, or update business data.</p>
  </section>

  <section class="research-canvas__inventory" id="review-routes" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Code review / Choose the correct route</p>
      <h2>Reviewing local changes is different from reviewing a repository pull request</h2>
      <p>Both can produce useful feedback, but they have different context, integration, and permission requirements. Choose the route based on where the change lives and who must receive the evidence.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Route</th><th scope="col">Typical trigger</th><th scope="col">Evidence and control question</th></tr></thead>
        <tbody>
          <tr><th scope="row">Local review</th><td>Developer asks for a review of an uncommitted or local change.</td><td>Which working tree and baseline are in scope? Who inspects findings before a commit or PR?</td></tr>
          <tr><th scope="row">In-app PR review</th><td>Engineer opens an accessible repository PR in a supported code-review experience.</td><td>Are repository access and review permissions available? Which diff, checks, and comments are visible?</td></tr>
          <tr><th scope="row">Repository-triggered review</th><td>A configured GitHub review is requested or triggered according to repository setup.</td><td>Who configures the integration, where is feedback posted, and are findings checked before action?</td></tr>
          <tr><th scope="row">Custom review automation</th><td>A company uses its own CI runner or integration for review assistance.</td><td>Who owns the runner, model invocation, data path, comment posting, and recovery from errors?</td></tr>
        </tbody>
      </table>
    </div>
    <p><strong>Repository rules:</strong> project-specific constraints can be documented in <code>AGENTS.md</code> where the chosen Codex review workflow supports them. Use narrow rules for non-obvious invariants, such as preserving a field's external contract or excluding customer data from logs. Keep mechanical checks in CI.</p>
    <p><strong>Verification exercise:</strong> choose one PR that should violate the rule, one compliant PR, and one unrelated PR. If every PR triggers the same warning, the rule is too broad. Codex review findings add evidence; tests, branch protection, and required human approvals remain independent controls.</p>
    <p>Check the latest <a href="https://help.openai.com/en/articles/20001552-review-pull-requests-with-codex">Codex pull-request review guidance</a> and <a href="https://developers.openai.com/blog/custom-code-review-rules-for-codex">repository review rules guidance</a> before committing to a specific route. Product permissions and available review triggers may change.</p>
  </section>

  <section class="research-canvas__inventory" id="collaboration-assessment" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Architecture exercise / Make a choice</p>
      <h2>Which collaboration pattern would you recommend?</h2>
      <p>In a fictional SAP team, an outbound IDoc enhancement intermittently produces an unexpected field value. The functional specification is available, but the failure cannot be reproduced outside an internal SAP test client. The delivery manager asks for a fully delegated cloud fix.</p>
    </header>
    <div class="ecg-decision-columns">
      <div>
        <h3>Recommendation</h3>
        <p>Start with a locally controlled, interactive investigation using the source and non-sensitive evidence already accessible to the developer. Ask for a trace of likely code paths and a proposed test. Do not claim end-to-end reproduction or a verified fix until the required SAP system tests are possible.</p>
      </div>
      <div>
        <h3>Decision boundary</h3>
        <p>Move to delegated implementation only after the team confirms the cause, authorizes a bounded change, prepares a suitable test environment, and identifies an ABAP and functional reviewer. An asynchronous cloud workflow is not automatically suitable for dependencies unavailable to that environment.</p>
      </div>
    </div>
    <p><strong>Interview challenge (B2):</strong> Explain your recommendation to a CIO in 45 seconds. Cover context availability, the correct collaboration pattern, required proof, and what remains a human decision.</p>
  </section>


  <section class="research-canvas__inventory" id="sdlc-ownership-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">SDLC / Responsibility matrix</p>
      <h2>Decide what Codex prepares, what engineers decide, and what the workflow checks</h2>
      <p>The question is not whether an agent can contribute at every lifecycle stage. It is whether the particular activity has useful context, an acceptable action boundary, a reliable check, and someone accountable for the result. Start with one stage rather than deploying assistance across the entire delivery chain.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Work stage</th><th scope="col">Possible agent contribution</th><th scope="col">Human decision</th><th scope="col">Evidence or safeguard</th></tr></thead>
        <tbody>
          <tr><th scope="row">Planning</th><td>Connect ticket details with repository context; expose missing assumptions or affected dependencies.</td><td>Product owner and architect settle requirements, trade-offs, priority, and the definition of done.</td><td>Approved ticket sources, open-question list, scope owner, and a stop before inventing business rules.</td></tr>
          <tr><th scope="row">Implementation</th><td>Explain an existing path, propose options, or prepare a small authorized diff with related tests.</td><td>Engineer selects the design, evaluates compatibility, accepts code, and decides on merge.</td><td>File limits, project conventions, diff review, targeted checks, and no unrelated refactoring.</td></tr>
          <tr><th scope="row">Review</th><td>Summarize changes and flag likely missing tests, behavioral risks, or uncertain assumptions.</td><td>Named reviewers decide feedback, approval, risk acceptance, and merge authorization.</td><td>Correct local or repository review route, relevant PR context, traceable findings, and independent branch protections.</td></tr>
          <tr><th scope="row">Testing</th><td>Propose cases, update test code, and execute permitted checks in a prepared environment.</td><td>Test owner judges coverage, business acceptance, and release risk.</td><td>Record commands actually run, pass/fail results, missing environments, and unverified scenarios separately.</td></tr>
          <tr><th scope="row">Debugging</th><td>Inspect approved logs, narrow a suspected cause, and suggest a reproducible experiment or limited fix.</td><td>Engineering owner confirms root cause and authorizes any production-sensitive action.</td><td>Redacted input, reproducible case, restrictions on side effects, and explicit escalation if evidence conflicts.</td></tr>
          <tr><th scope="row">Documentation</th><td>Prepare explanations of changed behavior, technical notes, and handoff drafts from approved sources.</td><td>Documentation or process owner verifies facts, policy-sensitive language, and publication.</td><td>Source links, version context, editorial review, and no unsupported customer-specific claims.</td></tr>
          <tr><th scope="row">Extended or asynchronous work</th><td>Complete a bounded repository investigation, dependency inventory, or other approved multi-step job and return a result package.</td><td>Task owner decides whether to continue, accept, re-scope, or escalate.</td><td>Prepared execution environment, measurable goal, checkpoints, command boundaries, test evidence, and a reviewer.</td></tr>
          <tr><th scope="row">Continuity and handoff</th><td>Summarize inspected files, decisions, changes, tests, uncertainties, and next actions for a new engineer or resumed task.</td><td>Team decides which notes become authoritative and whether the work can be resumed safely.</td><td>Durable record with source references, task and commit identity, verified/unverified status, and explicit ownership.</td></tr>
        </tbody>
      </table>
    </div>
    <p><strong>Architecture insight:</strong> the same agent may be useful in several stages, but its authority should not expand merely because a task has moved forward. A draft implementation is not permission to merge, and a proposed test is not evidence that it passed.</p>
  </section>

  <section class="research-canvas__inventory" id="asynchronous-follow-through" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Extended tasks / Execution contract</p>
      <h2>When an engineer is not steering every step, the task needs an explicit contract</h2>
      <p>Longer-running work can save interruptions, but it amplifies mistakes in scope, environment assumptions, and completion reporting. The instruction must say whether the agent may only investigate or is authorized to edit and validate. Neither elapsed time nor a reassuring progress message is proof of completion.</p>
    </header>
    <div class="ecg-decision-columns">
      <div>
        <h3>Before starting</h3>
        <ol>
          <li>Name one expected result and the files or repository it concerns.</li>
          <li>Confirm the exact environment and the dependencies that can run there.</li>
          <li>Set permissions, disallowed actions, and the point where human input is required.</li>
          <li>Define the checks and evidence the reviewer expects back.</li>
          <li>Specify what the agent must do when tests fail or information is missing.</li>
        </ol>
      </div>
      <div>
        <h3>Before accepting</h3>
        <ol>
          <li>Inspect the proposed diff and changed-file list.</li>
          <li>Check which tests actually ran, with the relevant results.</li>
          <li>Read failures, unresolved dependencies, and assumptions.</li>
          <li>Compare the result with the original scope and acceptance criteria.</li>
          <li>Accept, request corrections, or stop through the normal approval path.</li>
        </ol>
      </div>
    </div>
    <p><strong>Codex Cloud boundary:</strong> a published environment can supply reusable dependencies and access settings, but each new cloud task has a separate workspace and working files. Another task's uncommitted edits are not carried across automatically. Record and commit important artifacts before a handoff; confirm the environment owner and approved external service access. See <a href="https://help.openai.com/en/articles/20001545-using-codex-cloud">Using Codex Cloud</a> for current details.</p>
  </section>

  <section class="research-canvas__inventory" id="context-continuity-contract" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Continuity / Evidence that survives a handoff</p>
      <h2>Make progress resumable without turning summaries into a new source of truth</h2>
      <p>When work changes hands, the next engineer needs more than “investigation complete.” A useful handoff distinguishes established observations from conclusions and unfinished checks. It also identifies the specific repository revision, environment, and artifacts behind the claims.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Handoff field</th><th scope="col">Example for an SAP mapping change (simulation)</th></tr></thead>
        <tbody>
          <tr><th scope="row">Objective and boundary</th><td>Investigate one customer-field retention scenario; do not modify mappings or production data.</td></tr>
          <tr><th scope="row">Evidence inspected</th><td>Approved rule specification, enhancement revision, a sanitized test IDoc, and existing test cases.</td></tr>
          <tr><th scope="row">What changed</th><td>No files changed during diagnosis; any subsequent authorized patch is linked by branch and commit.</td></tr>
          <tr><th scope="row">Checks performed</th><td>Local tests and static checks listed with actual outcomes; SAP integration test recorded as not run if the system is unavailable.</td></tr>
          <tr><th scope="row">Open questions</th><td>Whether organizational context changes the expected rule and which owner can confirm it.</td></tr>
          <tr><th scope="row">Next decision owner</th><td>ABAP engineer validates technical diagnosis; SAP functional lead decides whether the business rule is correct.</td></tr>
        </tbody>
      </table>
    </div>
    <p><strong>Storage rule:</strong> save this record in an approved team location with references to the authoritative code and requirements. A generated summary should never silently replace configuration, source control, a validated test report, or a signed decision.</p>
  </section>

  <section class="research-canvas__inventory" id="lifecycle-control-check" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Workshop checklist / Readiness to collaborate</p>
      <h2>Seven questions before introducing the next agent workflow</h2>
      <p>Use this short decision gate when moving between planning, coding, review, testing, and handoff. If a critical answer is missing, clarify the task or keep the decision human-led.</p>
    </header>
    <div class="ecg-decision-columns">
      <div>
        <ol>
          <li>What exact task, artifact, and environment are included?</li>
          <li>Which systems, data, commands, or changes are excluded?</li>
          <li>What source context must the agent use?</li>
          <li>Which tests or independent evidence must be returned?</li>
        </ol>
      </div>
      <div>
        <ol start="5">
          <li>Who inspects and accepts the result?</li>
          <li>What needs explicit permission, and when should the agent stop?</li>
          <li>What outcome and guardrails would justify using this approach again?</li>
        </ol>
      </div>
    </div>
    <p><strong>Exercise (B2 English):</strong> An SAP integration manager wants Codex to investigate, correct, and deploy recurring IDoc failures overnight. The issue is reproducible only in a restricted quality system. In 60 seconds, identify the safe starting workflow, runtime constraints, evidence requirements, and decisions that must remain human-owned.</p>
  </section>

  <section class="research-canvas__inventory" id="pilot-decision-brief" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Workshop output / One-page architecture brief</p>
      <h2>Turn the discussion into a decision the customer can review</h2>
      <p>Before the first task, summarize the objective, task, owners, execution choice, evidence, unknowns, and next decision. Avoid a deployment diagram that has no accountable owner or measurable acceptance test.</p>
    </header>
    <div class="ecg-decision-columns">
      <div>
        <h3>Decision record fields</h3>
        <ol>
          <li>Expected delivery improvement and baseline.</li>
          <li>One repeatable task, input boundary, and output artifact.</li>
          <li>Necessary context, excluded information, and selected environment.</li>
          <li>Permitted actions, workflow safeguards, and human authority.</li>
          <li>Test criteria, review owner, visibility, and escalation.</li>
          <li>Open technical questions, specialist owners, and expansion rule.</li>
        </ol>
      </div>
      <div>
        <h3>Consulting response (B2 English)</h3>
        <blockquote><p>“We have a promising engineering task, but we should not begin by choosing a Codex client. First I would confirm the code and tests the task needs, where it can run, who will approve the result, and which checks will demonstrate value. That gives us a controlled pilot and a clear reason to expand—or stop.”</p></blockquote>
        <p><strong>Interview question:</strong> The CIO wants an asynchronous cloud pilot, but the team's mapping tests only run against an internal SAP system. What would you recommend, what would you verify first, and what would you refuse to assume?</p>
      </div>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">shield</span>
    <div>
      <p><strong>Next: decide which controls the pilot actually needs.</strong> Compare task risk, context sensitivity, execution permissions, customer approvals, validation evidence, and escalation. Includes a practical SAP control record.</p>
      <a href="/labs/business-ai/software-delivery-discovery/operating-model/governance/">Codex Governance Decisions: Risk & Operating Boundaries <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">menu_book</span>
    <div>
      <p><strong>Continue learning:</strong> <a href="/labs/business-ai/software-delivery-discovery/">AI Delivery Discovery</a> · <a href="/labs/business-ai/software-delivery-discovery/stakeholder-trust/">Stakeholder Trust and Adoption</a> · <a href="/labs/ai-ready/">AI Ready Architecture Lab</a>.</p>
      <p><strong>References checked 26 November 2026:</strong> <a href="https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan">Using Codex</a> · <a href="https://help.openai.com/en/articles/20001545-using-codex-cloud">Using Codex Cloud</a>. Release behavior and workspace controls should be reconfirmed before customer commitments.</p>
      <p><strong>Editorial note:</strong> independent synthesis and fictional enterprise/SAP examples. This page is not official vendor deployment guidance or a guarantee of product capabilities, compliance, or business outcomes.</p>
    </div>
  </section>
</div>
