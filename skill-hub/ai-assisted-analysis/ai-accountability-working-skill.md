---
layout: default
title: "AI Accountability Working Skill"
description: "Define who owns AI-generated output, how it is reviewed, and what happens when it is wrong so that AI assistance does not become blame avoidance."
permalink: /skill-hub/ai-assisted-analysis/ai-accountability-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/ai-assisted-analysis/">AI-Assisted Analysis</a></li>
    <li aria-current="page">AI Accountability</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — AI-Assisted Analysis</p>
  <h1>AI Accountability</h1>
  <p class="lead">Define who owns AI-generated output, how it is reviewed, and what happens when it is wrong so that AI assistance does not become blame avoidance.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>AI assistance can speed up analysis, but it also creates a responsibility gap: when the AI is wrong, who is accountable? This skill provides a governance framework for AI-assisted professional work. It defines ownership of AI-generated artifacts, review and sign-off requirements, audit trails for AI contributions, and error handling protocols. The goal is to make AI assistance transparent, reviewable, and accountable — not to replace human judgment with plausible-sounding output.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>When a team or project starts using AI tools for requirements, design, or analysis.</li>
      <li>After an AI-generated error reaches a client, stakeholder, or production system.</li>
      <li>When drafting a team policy or engagement terms for AI-assisted delivery.</li>
      <li>When a manager asks "how do we know the AI output is correct?"</li>
      <li>When a consultant wants to disclose AI use to a client but is unsure how to frame it.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>AI-generated requirement contained a fake transaction code</h3>
    <p>A consultant used AI to draft requirements for a custom SAP SD report. The AI included a requirement to "use transaction ZSD_CUST_REPORT to extract data." The transaction does not exist. The consultant copied the requirement into a client document without review. The client discovered the error during a steering committee meeting and questioned the consultant's credibility. There was no process for who should have reviewed the AI output or what to do when the AI was wrong.</p>
    <h3>AI-drafted architecture decision was not disclosed</h3>
    <p>A solution architect used AI to draft an architecture decision record (ADR) for a middleware change. The ADR contained a plausible but incorrect assumption about event ordering. The architect presented the ADR as their own work without disclosing the AI contribution. When the assumption was challenged during a technical review, the architect could not defend it because they had not done the underlying analysis. The team lost trust in the ADR and had to redo the decision.</p>
    <h3>Team uses AI for incident analysis with no review process</h3>
    <p>An SAP AMS team uses AI to analyze recurring incident tickets and suggest root causes. The AI correctly identifies a pattern 80% of the time but blames the wrong component in 20% of cases. Because there is no review gate, the incorrect diagnoses are passed to the client as findings. The client acts on one incorrect diagnosis and changes a configuration that was not broken, causing a new incident. The team has no protocol for reviewing AI output, no ownership of the error, and no way to prevent recurrence.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li><strong>Team structure</strong> — who does analysis, who reviews, who signs off, who owns the client relationship.</li>
      <li><strong>AI tools in use</strong> — which tools, for what purposes, with what data access.</li>
      <li><strong>Review processes</strong> — existing quality gates, approval workflows, sign-off requirements.</li>
      <li><strong>Risk appetite</strong> — what level of error is acceptable for internal work versus client-facing work.</li>
      <li><strong>Compliance requirements</strong> — any contractual, regulatory, or organizational rules about AI use or disclosure.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Who is accountable for the final output — the AI, the operator, or the reviewer?</li>
      <li>What is the review process for AI-generated artifacts before they leave the team?</li>
      <li>How is AI contribution disclosed to clients, stakeholders, or audit?</li>
      <li>What happens when AI output is wrong — who corrects it, who communicates the correction, and who prevents recurrence?</li>
      <li>Which decisions can the AI assist with, and which decisions must be made by humans alone?</li>
      <li>How is the AI's role documented in project records, contracts, or change logs?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Inventory AI tools and use cases.</strong> List every AI tool the team uses, what it is used for, and what data it accesses. Classify each use case by risk: internal research, draft generation, client-facing output, or production decision support.</li>
      <li><strong>Define the ownership matrix.</strong> For each use case, assign three roles: <strong>Operator</strong> (runs the AI), <strong>Reviewer</strong> (checks the output), <strong>Accountable</strong> (signs off and owns the consequences). These roles can be the same person for low-risk cases but must be separate for high-risk cases.</li>
      <li><strong>Set review gates.</strong> Define what must be reviewed before AI output is used: factual claims, system references, stakeholder attribution, assumptions, and conclusions. Define who performs the review and how it is recorded.</li>
      <li><strong>Define disclosure rules.</strong> Decide when and how to disclose AI use. At minimum, disclose AI use for client-facing deliverables. For internal work, document AI use in the artifact metadata.</li>
      <li><strong>Create an error handling protocol.</strong> Define: how an AI error is detected, who is responsible for correcting it, how the correction is communicated, and what is learned to prevent recurrence.</li>
      <li><strong>Distinguish assistance from delegation.</strong> Assistance means the AI drafts, the human decides. Delegation means the human accepts the AI output without review. Draw a clear line: which tasks are assist-only and which can be delegated with defined review.</li>
      <li><strong>Draft the AI usage policy.</strong> Write a one-page policy covering: tool inventory, ownership matrix, review gates, disclosure rules, error protocol, and assistance boundaries.</li>
      <li><strong>Review and ratify.</strong> Present the policy to the team and to stakeholders. Get explicit agreement on ownership and review gates. Update the policy when tools or use cases change.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If AI generates a recommendation, a human must review it before it is acted upon.</li>
      <li>If AI output is sent to a client or external stakeholder, disclosure is mandatory; the exact wording depends on the engagement terms.</li>
      <li>If AI output is wrong, the human operator is accountable, not the tool vendor.</li>
      <li>If the AI is used for a decision that affects safety, compliance, or contractual obligations, the accountable role must be a human with authority to make that decision.</li>
      <li>If a task requires original analysis or judgment, it is assistance-only; the AI can draft, but the human must decide.</li>
      <li>If the same AI error recurs, the review process is broken, not the AI.</li>
      <li>If there is no time to review, do not use AI for the task.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>AI Accountability Framework</strong> — ownership matrix, review gates, and error protocol.</li>
      <li><strong>Ownership Matrix</strong> — table of use cases with operator, reviewer, and accountable roles.</li>
      <li><strong>AI Usage Policy</strong> — one-page team policy for AI-assisted work.</li>
      <li><strong>Disclosure Template</strong> — standard wording for client communications about AI use.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>AI Accountability Framework</h3>
    <pre><code>---
title: AI Accountability Framework
team: [team name]
date: [YYYY-MM-DD]
review_cycle: [quarterly / on tool change]
---

## AI Tool Inventory
| Tool | Use Case | Data Access | Risk Level |
|------|----------|-------------|------------|
| [tool] | [drafting requirements] | [client data / public data] | [Low / Medium / High] |

## Ownership Matrix
| Use Case | Operator | Reviewer | Accountable | Review Gate | Disclosure |
|----------|----------|----------|-------------|-------------|------------|
| [use case] | [role] | [role] | [role] | [factual / full / none] | [client / internal / none] |

## Error Handling Protocol
1. **Detection**: [how errors are caught — review, client feedback, audit]
2. **Correction**: [who fixes the error and by when]
3. **Communication**: [who tells the client and in what format]
4. **Prevention**: [what changes to prevent recurrence — prompt, process, or tool]

## Assistance vs Delegation Boundaries
| Task Type | AI Role | Human Role |
|-----------|---------|------------|
| [requirements drafting] | [draft] | [review, verify, decide] |
| [incident analysis] | [pattern suggest] | [validate, diagnose, decide] |
| [client communication] | [outline] | [write, review, send] |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>[ ] Every AI use case has an assigned operator, reviewer, and accountable role.</li>
      <li>[ ] Every high-risk use case has a separate reviewer who is not the operator.</li>
      <li>[ ] Review gates are defined with specific criteria, not just "check it."</li>
      <li>[ ] Disclosure rules are documented and cover client-facing work.</li>
      <li>[ ] The error handling protocol names who is responsible for correction, communication, and prevention.</li>
      <li>[ ] Assistance and delegation are distinguished for each task type.</li>
      <li>[ ] The policy has been ratified by the team and relevant stakeholders.</li>
      <li>[ ] The framework is reviewed when tools or use cases change.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Treating AI as a black box that absolves the operator of responsibility. <strong>Consequence:</strong> When the AI is wrong, the operator blames the tool, the client loses trust, and the error is not corrected because no one owns it.</li>
      <li><strong>Mistake:</strong> Skipping disclosure because "everyone uses AI now." <strong>Consequence:</strong> A client discovers undisclosed AI use during an audit or a challenge, and the engagement is damaged.</li>
      <li><strong>Mistake:</strong> Not documenting error handling. <strong>Consequence:</strong> The same AI error recurs across multiple projects because the team has no process for learning from mistakes.</li>
      <li><strong>Mistake:</strong> Blurring assistance and delegation. <strong>Consequence:</strong> A human accepts an AI-generated recommendation without review, acts on it, and causes a configuration error that requires emergency remediation.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>
    <h3>Weak output — bad AI usage</h3>
    <p>A team leader asks AI to "write an AI usage policy for our team." The AI produces a generic document that says "team members should use AI responsibly and verify output before sharing it." There is no ownership matrix, no review criteria, no disclosure rules, and no error protocol. The policy is signed and filed. Six months later, a consultant sends an AI-generated requirements document to a client. The document contains a hallucinated SAP transaction code. The client discovers the error in a steering committee. The team has no documented process for who should have reviewed the output, how to disclose the mistake, or how to prevent it from happening again. The policy is useless because it contains no operational specifics.</p>
    <h3>Strong output — good AI usage</h3>
    <p>The team leader uses AI to draft the framework, then applies the accountability skill. The ownership matrix assigns the operator role to the consultant, the reviewer role to the senior analyst, and the accountable role to the engagement manager. The review gate for client-facing requirements requires cross-checking every SAP transaction code in a sandbox and verifying every business rule with a stakeholder. The disclosure rule says: "AI-assisted deliverables contain a footer note: 'This document was drafted with AI assistance and reviewed by [name].'" The error protocol says: if a client finds an AI error, the accountable role must correct it within 24 hours, log it in the error register, and update the review checklist. The policy is ratified, and the first AI-assisted deliverable passes review because the reviewer knows exactly what to check.</p>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <h3>AI Prompt Pattern</h3>
    <pre><code>Role: You are an AI governance assistant.
Context: I need to create an AI accountability framework for a team of [consultants / analysts / architects] working on [SAP / enterprise / data] projects.
Tasks:
1. Draft an AI tool inventory based on the tools and use cases I provide.
2. Propose an ownership matrix with operator, reviewer, and accountable roles for each use case.
3. Define review gates with specific criteria for each risk level.
4. Draft disclosure rules for internal and client-facing work.
5. Create an error handling protocol with detection, correction, communication, and prevention steps.
6. Distinguish assistance from delegation for each task type.
7. Output the framework in the provided template format.
Constraints: Do not write generic advice like "use AI responsibly." Every rule must name a role, a criteria, or a step. Do not omit error handling. Do not omit disclosure.</code></pre>
    <h3>Agent dos</h3>
    <ul>
      <li>Ask for the team structure, tools, and risk appetite before drafting the framework.</li>
      <li>Produce the ownership matrix as a concrete table, not a prose description.</li>
      <li>Define review gates with specific criteria: what must be checked, by whom, and how it is recorded.</li>
      <li>Include error handling as a full protocol, not a single sentence.</li>
    </ul>
    <h3>Agent don'ts</h3>
    <ul>
      <li>Do not write generic policy language that contains no operational specifics.</li>
      <li>Do not omit disclosure rules.</li>
      <li>Do not omit the error handling protocol.</li>
      <li>Do not allow the same person to be operator, reviewer, and accountable for high-risk use cases.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/agent-usage-guide/">Agent Usage Guide</a> — general rules for how agents use Skill Hub.</li>
      <li><a href="/skill-hub/business-analysis/requirements-elicitation-working-skill/">Requirements Elicitation</a> — capturing needs before AI generates requirements.</li>
      <li><a href="/skill-hub/ai-assisted-analysis/validate-ai-generated-requirements-working-skill/">Validate AI-Generated Requirements</a> — checking AI output before it enters a document.</li>
      <li><a href="/skill-hub/quality-rules/">Quality Rules</a> — criteria for what makes a Skill Hub page good or bad.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> — example of a governance framework applied to SAP operations.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of AI governance for professional services. It is not an official legal, compliance, or SAP guideline. The framework must be adapted to local laws, contractual terms, and organizational policies. AI tools and regulations change rapidly; the ownership matrix and disclosure rules should be reviewed at least quarterly. Use this skill as a structured starting point for accountability design, not as a substitute for legal or compliance review.</p>
  </section>
</article>
