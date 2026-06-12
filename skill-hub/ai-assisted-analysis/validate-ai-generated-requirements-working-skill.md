---
layout: default
title: "Validate AI-Generated Requirements Working Skill"
description: "Check AI-generated requirements for hallucinations, missing context, fake certainty, and hidden assumptions before they enter a requirements document."
permalink: /skill-hub/ai-assisted-analysis/validate-ai-generated-requirements-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/ai-assisted-analysis/">AI-Assisted Analysis</a></li>
    <li aria-current="page">Validate AI-Generated Requirements</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — AI-Assisted Analysis</p>
  <h1>Validate AI-Generated Requirements</h1>
  <p class="lead">Check AI-generated requirements for hallucinations, missing context, fake certainty, and hidden assumptions before they enter a requirements document.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>AI can draft requirements quickly, but it invents fields, omits stakeholders, and states business rules with fake confidence. This skill provides a structured validation workflow to catch these failures before the requirements reach a stakeholder or a system. The output is a validated requirements brief where every item has a confidence label and a traceable source.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>After using AI to generate or expand a requirements draft.</li>
      <li>Before sending AI-generated requirements to business stakeholders for review.</li>
      <li>When AI output references SAP transactions, tables, or fields you do not recognize.</li>
      <li>When integrating AI-generated content into an official requirements document or backlog.</li>
      <li>When a stakeholder challenges a requirement and the only source is an AI session.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>AI invents a field that does not exist</h3>
    <p>An AI drafts requirements for a new SAP SD pricing workflow and includes a requirement to "set the customer credit override flag in table KNA1." There is no such flag in KNA1. If this enters the requirements document, the development team will waste time searching for a nonexistent field, and the business will lose trust in the analysis.</p>
    <h3>AI omits a critical integration prerequisite</h3>
    <p>An AI generates requirements for a new EDI invoice interface and describes message mapping, error handling, and monitoring — but never mentions the EDI partner agreement or the need for SAP S/4 compatibility pack validation. The project proceeds without these checks and stalls during technical design.</p>
    <h3>AI assumes real-time data availability</h3>
    <p>An AI drafts requirements for a real-time operational dashboard and assumes the SAP data warehouse supports near-real-time latency. The actual warehouse is batch-updated nightly. The requirements are approved, the dashboard is built, and the first demonstration reveals a 24-hour data lag that makes the metrics unusable for the intended use case.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li><strong>AI-generated requirements draft</strong> — the raw output from the AI tool.</li>
      <li><strong>System documentation</strong> — SAP module guides, existing configuration, transaction reference.</li>
      <li><strong>Stakeholder interview notes</strong> — to verify that the AI captured the right people and needs.</li>
      <li><strong>Business process maps</strong> — to confirm that the AI described the actual process, not an idealized one.</li>
      <li><strong>Existing requirements baseline</strong> — if any (optional).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Which SAP transactions, tables, or fields does the AI reference, and do they exist in this version?</li>
      <li>Which business rules are stated, and who in the organization confirmed them?</li>
      <li>Which stakeholders are mentioned, and who is missing from the AI output?</li>
      <li>What assumptions does the AI make about system behavior, data availability, or process timing?</li>
      <li>What evidence does the AI provide for each claim, and is the evidence verifiable?</li>
      <li>Does the AI confuse a need with a solution, or a symptom with a requirement?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Freeze the AI output.</strong> Save the raw AI-generated requirements as a separate document so you can compare before and after.</li>
      <li><strong>Flag every system-specific claim.</strong> Highlight every mention of a transaction code, table name, field name, configuration object, or API endpoint.</li>
      <li><strong>Cross-reference with system documentation.</strong> Verify each flagged claim against SAP Help, existing system documentation, or a sandbox system. Mark verified, unverified, or false.</li>
      <li><strong>Check for missing stakeholders.</strong> Compare the AI output against the stakeholder list from the project. Flag any missing owners, reviewers, or approvers.</li>
      <li><strong>Surface hidden assumptions.</strong> Read each requirement and ask: what must be true for this to work? List assumptions that the AI never stated.</li>
      <li><strong>Assess confidence versus evidence.</strong> For each requirement, rate the AI's confidence (high, medium, low, speculative) based on the evidence it provided.</li>
      <li><strong>Label each requirement.</strong> Apply one of: <strong>Verified</strong>, <strong>Assumption</strong>, <strong>Needs Review</strong>, <strong>Hallucination</strong>, <strong>Conflict</strong>.</li>
      <li><strong>Produce a validated brief.</strong> Rewrite the requirements with labels, sources, and a log of what was corrected or removed.</li>
      <li><strong>Share the hallucination log.</strong> Document what the AI got wrong so the team can improve prompts or avoid the same patterns.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the AI claims a field or transaction exists, verify it in the system before accepting the requirement.</li>
      <li>If the AI states a business rule, find the business owner who confirmed it; otherwise label it as an assumption.</li>
      <li>If the AI omits a stakeholder who owns the affected data or process, add them and flag the gap.</li>
      <li>If the AI is confident but provides no evidence, downgrade the requirement to "unverified assumption."</li>
      <li>If the AI contradicts existing documentation, trust the documentation and flag the AI output for review.</li>
      <li>If a requirement is a hallucination, remove it and log it; do not try to salvage it.</li>
      <li>If two requirements depend on the same assumption, group them and elevate the assumption to a risk.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Validated Requirements Brief</strong> — requirements with confidence labels and sources.</li>
      <li><strong>Hallucination Log</strong> — a list of invented or false claims found in the AI output.</li>
      <li><strong>Assumption Register</strong> — unstated assumptions that must be verified before implementation.</li>
      <li><strong>Stakeholder Gap List</strong> — missing stakeholders who need to be consulted before the requirements are finalized.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Validated Requirements Brief</h3>
    <pre><code>---
title: Validated Requirements Brief
source: AI-generated draft + human validation
project: [project name]
validated_by: [name]
date: [YYYY-MM-DD]
---

## Requirement V-001
- **Statement**: [exact requirement text]
- **Confidence**: [Verified / Assumption / Needs Review / Hallucination / Conflict]
- **Source**: [AI output, stakeholder interview, system doc, unknown]
- **System claim**: [transaction / table / field mentioned]
- **Verification result**: [confirmed / not found / contradicts doc]
- **Stakeholder**: [owner or reviewer]
- **Assumption**: [what must be true]
- **Risk if assumption is wrong**: [consequence]

## Hallucination Log
| # | AI Claim | Actual Status | Impact |
|---|----------|---------------|--------|
| 1 | [claim] | [false / unverified] | [what would have gone wrong] |

## Assumption Register
| # | Assumption | Affects Requirements | Owner to Verify |
|---|------------|----------------------|-----------------|
| 1 | [assumption] | [V-001, V-002] | [stakeholder name] |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>[ ] Every requirement has a confidence label.</li>
      <li>[ ] Every system-specific claim is verified or flagged as unverified.</li>
      <li>[ ] Every stakeholder mentioned in the source material is present, or the gap is documented.</li>
      <li>[ ] The hallucination log contains at least one entry if the AI made a system-specific claim.</li>
      <li>[ ] No requirement enters the final document with a "Hallucination" label.</li>
      <li>[ ] The assumption register links assumptions to specific requirements.</li>
      <li>[ ] The brief can be read by someone who did not see the AI output and still makes sense.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Trusting the AI's tone of confidence as evidence. <strong>Consequence:</strong> A hallucinated field or transaction enters the requirements document and wastes development time.</li>
      <li><strong>Mistake:</strong> Skipping cross-reference because the requirement "looks right." <strong>Consequence:</strong> A plausible-sounding but incorrect business rule is adopted, creating downstream compliance or process failure.</li>
      <li><strong>Mistake:</strong> Accepting AI output without traceability to source. <strong>Consequence:</strong> When stakeholders challenge a requirement, there is no evidence of who said it or why it was included.</li>
      <li><strong>Mistake:</strong> Treating hallucinations as minor errors that can be ignored. <strong>Consequence:</strong> The same AI tool will hallucinate again on the next project because the pattern was never logged or corrected.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>
    <h3>Weak output — bad AI usage</h3>
    <p>A consultant pastes AI-generated requirements into a Word document without review. The AI included a requirement to "update the Z-CUSTOM-FIELD in the sales order header via BAPI_SALESORDER_CREATE." The team spends three days searching for the field before discovering it does not exist. The requirement also assumed that all sales organizations use the same incompletion procedure, which is false in this landscape. The client receives a document with two critical errors and loses confidence in the analysis.</p>
    <h3>Strong output — good AI usage</h3>
    <p>The consultant uses AI to draft requirements, then applies the validation skill. The hallucination log catches a fake transaction code (BAPI_SALESORDER_MODIFY) and a nonexistent table (VBAK_EXT). The assumption register surfaces that the AI assumed real-time ATP availability for a make-to-order process. The validated brief rewrites requirement V-003 with a "Needs Review" label and assigns it to the SD lead. The stakeholder review session is productive because every question has a source and every risk has an owner.</p>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <h3>AI Prompt Pattern</h3>
    <pre><code>Role: You are a requirements validation assistant.
Context: I have an AI-generated requirements draft for a [SAP module / business process] project. I need you to validate it.
Tasks:
1. Flag every mention of a transaction code, table, field, or configuration object.
2. Compare each claim against [system documentation / known SAP behavior].
3. Identify missing stakeholders from this list: [list].
4. Surface hidden assumptions.
5. Label each requirement as Verified, Assumption, Needs Review, Hallucination, or Conflict.
6. Output a validated brief in the template format provided.
Constraints: Do not invent system objects. Do not present assumptions as facts. If you cannot verify a claim, label it as unknown.</code></pre>
    <h3>Agent dos</h3>
    <ul>
      <li>Ask for the system documentation or SAP version before validating system claims.</li>
      <li>Produce the hallucination log and assumption register as separate artifacts.</li>
      <li>Link each requirement to a source document or stakeholder quote.</li>
      <li>Flag conflicts between AI output and existing documentation explicitly.</li>
    </ul>
    <h3>Agent don'ts</h3>
    <ul>
      <li>Do not trust the AI's confidence level as evidence.</li>
      <li>Do not skip cross-referencing because a claim "sounds right."</li>
      <li>Do not merge hallucinated requirements into the validated brief.</li>
      <li>Do not present your own assumptions as verified facts.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/business-analysis/requirements-elicitation-working-skill/">Requirements Elicitation</a> — capturing original stakeholder needs before AI generation.</li>
      <li><a href="/skill-hub/business-analysis/gap-analysis-working-skill/">Gap Analysis</a> — comparing validated requirements against current state.</li>
      <li><a href="/skill-hub/agent-usage-guide/">Agent Usage Guide</a> — general rules for how agents should use Skill Hub.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> — structured diagnostic frame for cross-process audits.</li>
      <li><a href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">SAP Incompletion Procedure Diagnostics</a> — example of how specific SAP diagnostics surface hidden requirements.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of AI-assisted requirements validation. It is not an official SAP, BABOK, or vendor guideline. The validation steps assume access to system documentation or a sandbox environment; if neither is available, the confidence labels will be less reliable. AI tools change frequently; the hallucination patterns described here are representative, not exhaustive. Use this skill as a structured starting point, not as a guarantee of accuracy.</p>
  </section>
</article>
