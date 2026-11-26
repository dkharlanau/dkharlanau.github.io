---
layout: default
title: "Codex Governance Decisions — Risk Levels, Checkpoints, and Operating Boundaries"
description: "An original enterprise AI decision kit for selecting Codex controls in proportion to task risk, distinguishing runtime permission from human approval, and validating a governed engineering pilot."
permalink: /labs/business-ai/software-delivery-discovery/operating-model/governance/
status: reviewed
verified: false
robots: index,follow
sitemap: true
last_modified_at: 2026-11-26
tags: [codex, enterprise-ai, governance, risk-management, approval, observability, software-delivery, sap]
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li><a href="/labs/business-ai/software-delivery-discovery/">AI Delivery Discovery</a></li><li><a href="/labs/business-ai/software-delivery-discovery/operating-model/">Pilot Operating Model</a></li><li aria-current="page">Governance Decisions</li></ol></nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Architecture practice / Risk & controls</p>
      <h1>Govern the action.<br>Not the buzzword.</h1>
      <p>Two Codex tasks can use the same model and carry very different risks. Explaining an ABAP method is not the same as modifying a transport or contacting a productive SAP system. Use this decision kit to identify the right collaboration pattern, action boundaries, checkpoints, and evidence before approving an engineering pilot.</p>
      <a class="research-canvas__button" href="#risk-levels">Start with risk <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <div>
      <p><strong>Key distinction:</strong> the authority to run a command is not the authority to approve its business result. A technically permitted tool action may still be prohibited by company policy or require an independent human decision.</p>
      <p><strong>Use of this page:</strong> risk classes and templates are author-developed decision aids, not official OpenAI policy tiers. Confirm actual product controls, configured sandbox and approval behavior, legal obligations, and customer process requirements with authorized owners.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="pattern-decision" data-reveal>
    <header><p class="research-canvas__eyebrow">Collaboration choice</p><h2>Choose how much autonomy the work can safely carry</h2>
      <p>Before setting permissions, determine the shape of the work. A vague request may need clarification, not a more autonomous agent.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table><thead><tr><th scope="col">Observed work condition</th><th scope="col">Suitable starting pattern</th><th scope="col">Decision boundary</th></tr></thead><tbody>
        <tr><th scope="row">The engineer is still discovering what the issue means.</th><td>Interactive exploration</td><td>Engineer steers each hypothesis and approves any change in scope.</td></tr>
        <tr><th scope="row">The task has a known result, accessible evidence, and repeatable checks.</th><td>Constrained delegation</td><td>Agent works within defined limits; owner inspects results before acceptance.</td></tr>
        <tr><th scope="row">The artifact informs an approval or architectural choice.</th><td>Review preparation</td><td>Agent prepares findings; authorized reviewer makes the decision.</td></tr>
        <tr><th scope="row">The step affects production, legal commitments, or sensitive policy.</th><td>Human-led decision, with optional bounded analysis</td><td>No agent-owned approval or high-impact action by default.</td></tr>
        <tr><th scope="row">The request has no acceptance test, owner, or clear boundary.</th><td>Clarify the task first</td><td>Do not treat an open-ended instruction as delegation readiness.</td></tr>
      </tbody></table>
    </div>
  </section>

  <section class="research-canvas__inventory" id="risk-levels" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Proportionate safeguards</p>
      <h2>Classify the consequence of being wrong, not how impressive the task looks</h2>
      <p>A three-level risk scale helps teams avoid over-controlling routine assistance and under-controlling actions with significant side effects. Reassess the level when context, permissions, or the target environment changes.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Risk class</th><th scope="col">Example (fictional)</th><th scope="col">Initial safeguard</th><th scope="col">Reason to escalate</th></tr></thead>
        <tbody>
          <tr><th scope="row">A. Informational support</th><td>Explain a non-sensitive method or draft tests without changing files.</td><td>Approved context, no write access needed, source-aware output, engineer checks factual claims.</td><td>The task requires confidential data or moves from explanation to editing.</td></tr>
          <tr><th scope="row">B. Limited engineering changes</th><td>Prepare a small ABAP test update in a development branch.</td><td>Scoped workspace and write permissions, reproducible tests, diff, reviewer, and no automatic merge.</td><td>Unknown dependencies, failing tests, cross-repository changes, or additional tool access.</td></tr>
          <tr><th scope="row">C. High-impact action</th><td>Deploy a transport, change business rules in production, or execute privileged operations.</td><td>Keep action human-led or separately authorized through the customer's established production controls. Specialist review is required.</td><td>By definition, elevated impact and reversibility must be assessed before any execution is considered.</td></tr>
        </tbody>
      </table>
    </div>
    <p><strong>Risk is contextual.</strong> An apparently read-only analysis may still be high-risk when it exposes credentials or personal data. An isolated test patch may remain medium-risk if its scope is controlled and its effects are reversible. Never infer risk from a command name alone.</p>
  </section>

  <section class="research-canvas__inventory" id="control-inputs" data-reveal>
    <header><p class="research-canvas__eyebrow">Control selection / Five inputs</p><h2>Start with what could go wrong in this customer's environment</h2>
      <p>The following factors should change the recommended safeguards. Record them explicitly rather than copying a generic list of security features.</p></header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Input</th><th scope="col">What the architect investigates</th><th scope="col">Possible design consequence</th></tr></thead>
        <tbody>
          <tr><th scope="row">Impact of an error</th><td>Could a wrong suggestion harm business behavior, release quality, system availability, or a customer commitment?</td><td>Restrict to proposal-only work or add mandatory tests and independent approval.</td></tr>
          <tr><th scope="row">Information sensitivity</th><td>Could the agent read secrets, financial records, personal data, unreleased source, or restricted logs?</td><td>Minimize inputs, sanitize fixtures, isolate the environment, or decline the task.</td></tr>
          <tr><th scope="row">Effective identity</th><td>Whose privileges are used for reading, editing, tool invocation, and publication?</td><td>Apply least privilege and separate engineering access from merge or administrative authority.</td></tr>
          <tr><th scope="row">Reachable tools and systems</th><td>Which repositories, CI services, package sources, MCP servers, network endpoints, and SAP environments can the runtime access?</td><td>Limit connections and commands; require explicit expansion review when scope changes.</td></tr>
          <tr><th scope="row">Customer governance</th><td>Which approvals, records, segregation of duties, retention rules, and exception processes apply?</td><td>Map customer process gates to enforceable controls and named decision owners.</td></tr>
        </tbody>
      </table>
    </div>
    <p><strong>Architectural rule:</strong> selecting a checkbox in a product is not proof that a customer control objective has been satisfied. For every important control, identify its owner, actual enforcement point, and evidence of operation.</p>
  </section>

  <section class="research-canvas__inventory" id="checkpoint-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Four checkpoints / Different questions</p>
      <h2>Do not collapse permission, validation, review, and escalation into one button</h2>
      <p>These checkpoints happen at different times. A valid runtime approval does not demonstrate correct code, and a passed unit test does not authorize production release.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Checkpoint</th><th scope="col">Question it answers</th><th scope="col">Illustration</th><th scope="col">Accountable party</th></tr></thead>
        <tbody>
          <tr><th scope="row">Execution permission</th><td>May this requested operation run within configured and authorized limits?</td><td>File write or network request asks for additional permission, where supported.</td><td>Configured runtime policy and any designated permission reviewer.</td></tr>
          <tr><th scope="row">Technical validation</th><td>Does the artifact meet an objective check?</td><td>Targeted tests, build, lint, or a reproducible defect check.</td><td>Engineering and test owners define and evaluate the checks.</td></tr>
          <tr><th scope="row">Human acceptance</th><td>Should the organization adopt, approve, or release this result?</td><td>Named engineer accepts a PR; SAP change owner authorizes transport.</td><td>Customer's authorized reviewer or change authority.</td></tr>
          <tr><th scope="row">Escalation</th><td>When must work stop because the next step is unsafe or under-specified?</td><td>Agent encounters secrets, inconsistent requirements, failed critical tests, or unknown production impact.</td><td>Task owner routes to engineering, platform, or security specialist.</td></tr>
        </tbody>
      </table>
    </div>
    <div class="ecg-decision-columns">
      <div>
        <h3>Model the normal path</h3>
        <p><strong>Task accepted → Context approved → Bounded execution → Checks recorded → Human review → Authorized next action.</strong></p>
        <p>At each transition, define the evidence that allows the workflow to proceed.</p>
      </div>
      <div>
        <h3>Model the exception path</h3>
        <p><strong>Unexpected access, ambiguous scope, or failed critical check → Stop → Preserve evidence → Escalate to owner.</strong></p>
        <p>Stopping is the correct result when the task's preconditions no longer hold.</p>
      </div>
    </div>
    <p><strong>Runtime caveat:</strong> Codex approval prompts and automatic review features depend on the client, configuration, and workspace. Even when a request is approved by an automatic reviewer, independent filesystem, network, identity, and organizational controls still matter. See <a href="https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan">Codex access and approval guidance</a> and <a href="https://help.openai.com/en/articles/20001548-agent-security-and-local-work-sync-in-chatgpt">Agent Security management</a>.</p>
  </section>

  <section class="research-canvas__inventory" id="boundary-record" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Reusable artifact / Pilot boundary record</p>
      <h2>A compact control agreement that engineers can actually use</h2>
      <p>Fill in these fields before a controlled pilot. Record decisions and unknowns, not optimistic promises about a product configuration.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Record field</th><th scope="col">What must be defined</th><th scope="col">Illustrative SAP review pilot</th></tr></thead>
        <tbody>
          <tr><th scope="row">Task and expected result</th><td>One workflow, bounded artifact, and measurable success.</td><td>Prepare a review summary and test-gap list for a customer mapping change.</td></tr>
          <tr><th scope="row">Permitted context</th><td>Approved repository revision, ticket, standards, fixtures, and evidence.</td><td>Development branch, change request, sanitized mapping examples.</td></tr>
          <tr><th scope="row">Explicit exclusions</th><td>Data and environments that must not be opened, copied, or modified.</td><td>No production BP extracts, customer identifiers, secrets, or productive SAP access.</td></tr>
          <tr><th scope="row">Identity and runtime</th><td>Chosen client, execution environment, effective permissions, network and sandbox policy.</td><td>Approved developer environment, restricted repository write scope.</td></tr>
          <tr><th scope="row">Prohibited actions</th><td>Operations not authorized, even if technically possible.</td><td>No business-rule override, no push to protected branch, no merge, no transport release.</td></tr>
          <tr><th scope="row">Permission requests</th><td>Actions needing a configured runtime approval or separately documented business authorization.</td><td>New tool connection or any move from read-only review to editing.</td></tr>
          <tr><th scope="row">Required proof</th><td>Diff, test results, identified limitations, and reviewer acceptance criteria.</td><td>Relevant files, findings, false-positive review, and clearly untested cases.</td></tr>
          <tr><th scope="row">Review and escalation</th><td>Named human decision owner and exception route.</td><td>ABAP lead checks technical claims; SAP process owner resolves functional ambiguity.</td></tr>
          <tr><th scope="row">Visibility and retention</th><td>What activity, decisions, artifacts, and failures must be traceable; approved storage location.</td><td>Task ID, revision, accepted/rejected findings, check output, owner decision.</td></tr>
          <tr><th scope="row">Go/no-go rule</th><td>Baseline, quality floor, budget, stop condition, and evidence needed to expand.</td><td>Compare accepted findings and review time; stop if sensitive context is required or quality falls.</td></tr>
        </tbody>
      </table>
    </div>
    <p><strong>Configuration evidence:</strong> for a CLI evaluation, preserve the client version and actual effective settings rather than assuming defaults. For a managed environment, record who prepared it, approved network/service access, and can change its setup. Access to a shared setup does not authorize every task that could run inside it.</p>
  </section>

  <section class="research-canvas__inventory" id="risk-examples" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">SAP simulations / Reassess at the action boundary</p>
      <h2>The same engineering program can contain all three risk classes</h2>
      <p>These examples are hypothetical. The purpose is to show why a single global rule for “all Codex work” is usually a poor architecture choice.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Scenario</th><th scope="col">Initial risk judgment</th><th scope="col">Safe starting approach</th><th scope="col">Escalation trigger</th></tr></thead>
        <tbody>
          <tr><th scope="row">Explain an outbound IDoc mapping method</th><td>Informational if approved, non-sensitive code is sufficient.</td><td>Read-only explanation with citations to inspected source and uncertainty notes.</td><td>Investigation requires confidential logs or privileged system access.</td></tr>
          <tr><th scope="row">Add regression tests for an organizational field rule</th><td>Limited engineering change when test fixtures and branch are isolated.</td><td>Prepare tests in a scoped branch and return an inspectable diff and actual checks.</td><td>Expected behavior is undocumented or a wider business mapping change is needed.</td></tr>
          <tr><th scope="row">Resend failed master-data messages in a productive landscape</th><td>High impact due to potential business-system side effects.</td><td>Use agent assistance to prepare a diagnostic report only; keep operational action under approved customer procedures.</td><td>Any request to run a productive resend or modify business data.</td></tr>
        </tbody>
      </table>
    </div>
    <p><strong>Do not overclaim SAP testing:</strong> a passing repository test does not prove production customizing, partner determination, integration side effects, or transport safety. Mark unavailable SAP-system validation as unverified.</p>
  </section>

  <section class="research-canvas__inventory" id="evidence-and-scale" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Observability / Evidence for the next decision</p>
      <h2>Record what happened, what was checked, and what remains unknown</h2>
      <p>An audit-ready story requires more than a summary generated by the agent. The team needs enough evidence to reproduce key steps, understand human decisions, and detect whether the control boundary still matches the work.</p>
    </header>
    <div class="ecg-decision-columns">
      <div>
        <h3>Useful evidence set</h3>
        <ul>
          <li>Task ID, scope, initiator, owner, and execution location.</li>
          <li>Repository revision, supplied context, relevant tools, and declared exclusions.</li>
          <li>Approval requests, outcomes, exceptions, and identity of decision-makers where captured.</li>
          <li>Files changed, diff, commands executed, and actual validation results.</li>
          <li>Human review decision, unresolved issues, rework, and any unexpected access.</li>
          <li>Time and quality measures compared with the current workflow.</li>
        </ul>
      </div>
      <div>
        <h3>Do not confuse telemetry with assurance</h3>
        <p>Some signals are available through product logs, some require CI or Git records, and others need customer-owned workflow records. Verify the actual collection and retention capability before promising a complete audit trail.</p>
        <p><strong>Expansion gate:</strong> enlarge scope only when the work remains useful, accepted quality is stable, access and approval boundaries hold, and responsible owners can inspect failures.</p>
      </div>
    </div>
    <p>For current capabilities and distinctions, consult <a href="https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan">Codex workspace controls and Compliance API guidance</a> and <a href="https://help.openai.com/en/articles/20001545-using-codex-cloud">Codex Cloud environment rules</a>. Neither page proves any customer's actual logging completeness.</p>
  </section>

  <section class="research-canvas__inventory" id="governance-interview" data-reveal>
    <header><p class="research-canvas__eyebrow">Consulting practice / B2 interview</p><h2>Explain the boundary without sounding obstructive</h2></header>
    <div class="ecg-decision-columns">
      <div>
        <h3>Situation</h3>
        <p>A fictional SAP delivery director wants Codex to find and fix IDoc mapping errors overnight. The ABAP team can offer a test repository, but reproducing some defects requires a restricted system. Security asks for traceability, and the sponsor does not want every low-risk command to wait for manual approval.</p>
      </div>
      <div>
        <h3>Your task</h3>
        <p>Give a 90-second recommendation. Identify a low-risk first step, the transition to limited delegation, the point at which a human must decide, and the minimum evidence needed before expansion.</p>
        <p><strong>Strong framing:</strong> “We can reduce unnecessary interruptions while keeping the high-impact decisions under human control. The right boundary depends on the data, tools, and actions needed for this specific workflow.”</p>
      </div>
    </div>
    <p><strong>Decision challenge:</strong> a runtime approval system permits a command, but the customer's segregation-of-duties policy requires another person to authorize the business action. Which rule takes precedence, and how would you make that requirement enforceable rather than simply writing it in a prompt?</p>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">menu_book</span>
    <div>
      <p><strong>Continue:</strong> <a href="/labs/business-ai/software-delivery-discovery/operating-model/">Codex Pilot Operating Model</a> · <a href="/labs/business-ai/software-delivery-discovery/stakeholder-trust/">Stakeholder Trust & Adoption</a> · <a href="/labs/business-ai/software-delivery-discovery/">AI Delivery Discovery</a>.</p>
      <p><strong>Official references checked 26 November 2026:</strong> <a href="https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan">Codex access, auto-review and enterprise controls</a>, <a href="https://help.openai.com/en/articles/20001548-agent-security-and-local-work-sync-in-chatgpt">Agent Security</a>, <a href="https://help.openai.com/en/articles/20001545-using-codex-cloud">Codex Cloud environments</a>. All controls require verification for the selected customer and product surface.</p>
      <p><strong>Editorial method:</strong> original analysis and fictional SAP examples based on learning notes. This is not an OpenAI security certification, a reproduction of course materials, or an implementation approval.</p>
    </div>
  </section>
</div>
