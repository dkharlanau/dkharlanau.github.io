---
layout: default
title: "Decision Summary Writing Working Skill"
description: "Document what was decided, what alternatives were rejected, why, and what the consequences are so future teams do not re-open closed decisions."
permalink: /skill-hub/work-documentation-handover/decision-summary-writing-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/work-documentation-handover/">Work Documentation and Handover</a></li>
    <li aria-current="page">Decision Summary Writing</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Work Documentation and Handover</p>
  <h1>Decision Summary Writing Working Skill</h1>
  <p class="lead">Document what was decided, what alternatives were rejected, why, and what the consequences are so future teams do not re-open closed decisions.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Decisions are the most expensive thing to lose in an organization. When the person who made a decision leaves, the rationale often leaves with them. This skill produces a Decision Summary Note: a compact, permanent record of a significant decision that includes the context, the options considered, the chosen path, the rejected paths, and the expected consequences. The output is designed to prevent repeated debates, re-opened decisions, and wrong assumptions by future teams. It complements evidence-based recommendation, which builds the recommendation before the decision is made.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A significant architectural, process, or design decision has been made and the team needs a permanent record.</li>
      <li>A decision is controversial or likely to be questioned later, and the team needs to capture the reasoning before it is forgotten.</li>
      <li>A project is ending and the handover package must include the rationale behind key choices.</li>
      <li>An audit or compliance review requires evidence of why a particular approach was selected.</li>
      <li>A new team member is challenging an existing approach and needs to understand the constraints that shaped the original decision.</li>
      <li>An AI agent is documenting a decision trail and needs to know what to record and what to omit.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP integration: choosing middleware over direct RFC</h3>
    <p>The integration team chose SAP PI over direct RFC calls for a customer master data sync. Six months later, a new architect suggests replacing PI with direct OData calls because "it is simpler." The original Decision Summary Note explains: PI was chosen because the business requires guaranteed delivery, audit logging, and retry logic that direct RFC does not provide. The note includes the rejected option (direct RFC), the rationale (guaranteed delivery and audit requirements), and the consequence (higher infrastructure cost but lower risk of data loss). Without this note, the new architect re-opens the debate and the team spends two weeks re-evaluating a settled question.</p>

    <h3>Data governance: rejecting real-time replication for batch</h3>
    <p>The data governance team decided to use batch replication instead of real-time for material master data. The rationale: real-time replication would require significant middleware investment for a use case where batch updates are sufficient. The rejected option was real-time via SLT. The consequence is that downstream systems receive updates every four hours, not instantly. A new project manager later insists on real-time because it is "modern." The Decision Summary Note prevents the re-opening of a decision that was already validated by cost and need analysis.</p>

    <h3>Support process: changing the incident escalation path</h3>
    <p>The AMS team decided to escalate SAP IDoc failures to the middleware team first, not the basis team. The rationale: 80% of IDoc failures are mapping errors, not infrastructure issues. The rejected option was escalating to basis first. The consequence is that basis team workload is reduced but middleware team response times must be monitored. When a new operations manager joins and reverts the escalation path to basis, IDoc resolution times increase because the wrong team is alerted first. The Decision Summary Note would have prevented this regression.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>The decision statement: what was decided, in one sentence.</li>
      <li>The decision context: the problem, opportunity, or constraint that forced the decision.</li>
      <li>The options considered: at least two alternatives, including the chosen one and the rejected ones.</li>
      <li>The evaluation criteria: the dimensions used to compare options (cost, risk, time, compliance, etc.).</li>
      <li>The rationale: why the chosen option was selected and why each rejected option was rejected.</li>
      <li>The decision maker: who made the decision and who approved it.</li>
      <li>The date of the decision.</li>
      <li>The expected consequences: what will happen as a result, including risks, costs, and dependencies.</li>
      <li>Supporting evidence: documents, data, or analysis that informed the decision (optional but recommended).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What problem or opportunity forced this decision? If there was no real problem, the decision may not need a summary.</li>
      <li>What were the realistic alternatives, and why was each rejected?</li>
      <li>What criteria were used to evaluate the options? Was cost weighted more than risk?</li>
      <li>Who made the decision, and who had the authority to make it?</li>
      <li>What are the consequences if the chosen option fails? What is the fallback?</li>
      <li>What constraints or dependencies shaped the decision? Would the same decision be made under different constraints?</li>
      <li>Who needs to know this decision, and who is likely to challenge it later?</li>
      <li>What evidence exists that supports the rationale? If the evidence is weak, note that in the summary.</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Identify the decision.</strong> State the decision in one clear sentence. If you cannot state it in one sentence, the decision is not yet clear enough to summarize.</li>
      <li><strong>Describe the context.</strong> Explain the problem, opportunity, or constraint that made the decision necessary. Include dates, project phase, and stakeholders involved.</li>
      <li><strong>List the options considered.</strong> Include at least two realistic alternatives: the chosen option and the rejected options. For each, describe what it is, its key features, and its rough cost or effort.</li>
      <li><strong>Define the evaluation criteria.</strong> State the dimensions used to compare options. Common criteria: cost, risk, time to implement, alignment with strategy, compliance, maintainability, and team capability.</li>
      <li><strong>State the rationale.</strong> Explain why the chosen option was selected and why each rejected option was rejected. Be specific. Avoid generic language like "it was the best fit." Say why it was the best fit.</li>
      <li><strong>Record the decision maker and date.</strong> Name the person who made the decision and the date. If the decision was approved by a committee, name the committee and the meeting date.</li>
      <li><strong>Describe the consequences.</strong> List the expected outcomes, risks, costs, and dependencies. Include both positive and negative consequences. If a consequence is uncertain, state the uncertainty.</li>
      <li><strong>Link supporting evidence.</strong> Reference the analysis, data, or documents that informed the decision. Do not paste the entire analysis into the summary; link to it.</li>
      <li><strong>Write the Decision Summary Note.</strong> Use the template below. Keep it to one page if possible. Two pages is the maximum for a single decision.</li>
      <li><strong>Validate and store.</strong> Review the note with the decision maker. Confirm that the rationale is accurate and the consequences are complete. Store it in the agreed decision log or document repository.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the decision has no clear alternatives, do not write a summary yet. The decision may be a directive, not a choice.</li>
      <li>If the rationale is based on assumptions, label the assumptions explicitly. Do not present assumptions as facts.</li>
      <li>If the decision is reversible with low cost, a lighter summary is sufficient. If it is irreversible or expensive, write a full summary.</li>
      <li>If the decision was made under time pressure, note the time constraint and whether the same decision would be made with more time.</li>
      <li>If the rejected option is likely to be proposed again, explain the rejection in enough detail to prevent repetition.</li>
      <li>If the decision affects multiple teams or systems, share the summary with all affected parties, not only the originating team.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Decision Summary Note</strong> — One-page or two-page record of a single significant decision. See template below.</li>
      <li><strong>Decision Log</strong> — Registry of all Decision Summary Notes for a project or program, with IDs, dates, and decision makers.</li>
      <li><strong>Evidence Index</strong> — Optional list of supporting documents, analyses, and data sources referenced in the summary.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Decision Summary Note (compact)</h3>
    <pre><code>---
artifact: Decision Summary Note
id: DS-&lt;project&gt;-&lt;number&gt;
decision: &lt;One-sentence decision statement&gt;
date: YYYY-MM-DD
decision_maker: &lt;Name and role&gt;
approved_by: &lt;Name and role&gt;
status: draft | reviewed | approved
---

## Context
- Problem / Opportunity: &lt;What forced the decision&gt;
- Constraints: &lt;Budget, time, compliance, technical limits&gt;
- Stakeholders: &lt;Who was involved and their interest&gt;

## Options Considered
| Option | Description | Pros | Cons | Estimated Cost / Effort |
|--------|-------------|------|------|------------------------|
| Chosen: &lt;Name&gt; | &lt;What it is&gt; | &lt;Pros&gt; | &lt;Cons&gt; | &lt;Cost&gt; |
| Rejected: &lt;Name&gt; | &lt;What it is&gt; | &lt;Pros&gt; | &lt;Cons&gt; | &lt;Cost&gt; |
| Rejected: &lt;Name&gt; | &lt;What it is&gt; | &lt;Pros&gt; | &lt;Cons&gt; | &lt;Cost&gt; |

## Evaluation Criteria
- &lt;Criterion 1: e.g., implementation cost&gt; — weight: &lt;high / medium / low&gt;
- &lt;Criterion 2: e.g., operational risk&gt; — weight: &lt;high / medium / low&gt;
- &lt;Criterion 3: e.g., compliance alignment&gt; — weight: &lt;high / medium / low&gt;

## Rationale
- Why the chosen option was selected: &lt;Specific reason&gt;
- Why each rejected option was rejected: &lt;Specific reason&gt;
- Assumptions made: &lt;List any assumptions that shaped the decision&gt;

## Consequences
- Positive: &lt;What will improve&gt;
- Negative: &lt;What will become harder or more expensive&gt;
- Risks: &lt;What could go wrong&gt;
- Dependencies: &lt;What must happen for the decision to succeed&gt;
- Reversibility: &lt;Can the decision be undone, and at what cost&gt;

## Supporting Evidence
- &lt;Link to analysis, data, or document&gt;
- &lt;Link to meeting minutes or approval record&gt;
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The decision is stated in one clear sentence.</li>
      <li>At least two realistic alternatives are described, including the chosen one.</li>
      <li>The rationale explains why the chosen option was selected and why each rejected option was rejected.</li>
      <li>The evaluation criteria are explicit and their relative weights are stated.</li>
      <li>Consequences include positive, negative, risks, and dependencies.</li>
      <li>The decision maker and approval authority are named.</li>
      <li>Assumptions are labeled as assumptions, not facts.</li>
      <li>The summary has been reviewed by the decision maker for accuracy.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Recording the decision without the rejected options.</strong> Consequence: future teams propose the same rejected option again because they do not know it was already considered and rejected.</li>
      <li><strong>Using generic rationale like "it was the best fit."</strong> Consequence: the rationale is useless for future review. The decision appears arbitrary.</li>
      <li><strong>Omitting the consequences.</strong> Consequence: the team is surprised by costs, risks, or dependencies that were known but not recorded.</li>
      <li><strong>Confusing a decision with a directive.</strong> Consequence: a directive from leadership is recorded as a decision with alternatives, which is misleading. Directives need different documentation.</li>
      <li><strong>Writing the summary from memory months after the decision.</strong> Consequence: the rationale is distorted, the rejected options are forgotten, and the summary becomes unreliable.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A one-line note in a meeting minutes document: "The team decided to use SAP PI for the integration." No alternatives, no rationale, no consequences, no decision maker, no date. Six months later, a new architect reads this and proposes replacing PI with direct OData because the note gives no reason why PI was chosen.</p>
    <p><strong>Why it fails:</strong> The decision is easily re-opened. The rationale is lost. The team wastes time re-evaluating a settled question. Audits find no evidence of due diligence.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Decision Summary Note
id: DS-INT-2026-003
decision: Use SAP PI over direct RFC for customer master data synchronization.
date: 2026-03-15
decision_maker: K. Schmidt, Integration Architect
approved_by: S. Mueller, Project Steering Committee
status: approved
---

## Context
- Problem / Opportunity: Customer master data must be synchronized between S/4HANA and the CRM system with guaranteed delivery and audit logging.
- Constraints: Budget allows one middleware investment. Compliance requires audit trail for all customer changes.
- Stakeholders: Integration team, CRM team, compliance officer, AMS operations.

## Options Considered
| Option | Description | Pros | Cons | Estimated Cost / Effort |
|--------|-------------|------|------|------------------------|
| Chosen: SAP PI | Middleware with guaranteed delivery, retry, and audit | Audit trail, retry logic, monitoring | Higher infrastructure cost, licensing | 80k EUR + 3 months |
| Rejected: Direct RFC | Real-time RFC calls from S/4 to CRM | Simple, no middleware cost | No guaranteed delivery, no audit log, no retry | 20k EUR + 1 month |
| Rejected: File-based batch | Nightly file transfer | Very cheap | No real-time, no audit trail, failure-prone | 10k EUR + 2 weeks |

## Evaluation Criteria
- Compliance alignment — weight: high
- Operational reliability — weight: high
- Implementation cost — weight: medium
- Maintenance effort — weight: medium

## Rationale
- SAP PI was selected because it is the only option that satisfies compliance requirements for audit logging and guaranteed delivery.
- Direct RFC was rejected because the compliance officer explicitly ruled out any solution without an audit trail.
- File-based batch was rejected because the business requires near-real-time sync for customer service operations.
- Assumptions: PI license cost is fixed for the next three years; CRM team can consume PI messages.

## Consequences
- Positive: Full audit trail, retry on failure, centralized monitoring via PI monitoring cockpit.
- Negative: Higher infrastructure cost and dependency on PI admin team for queue monitoring.
- Risks: PI queue backlog during high volume; mitigation is alert-based monitoring.
- Dependencies: CRM team must implement message consumer by 2026-05-01.
- Reversibility: Reversible within 6 months at approximately 40k EUR cost if PI license is cancelled.

## Supporting Evidence
- Link: Compliance requirements document (COMP-2026-001)
- Link: Cost analysis spreadsheet (COST-INT-2026-003)
- Link: Steering committee meeting minutes (SCM-2026-03-15)
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Decision documentation writer for an enterprise project.</p>
    <p><strong>Context:</strong> You have meeting notes, emails, or project records describing a decision. You need to produce a Decision Summary Note that captures the decision, alternatives, rationale, and consequences.</p>
    <p><strong>Task:</strong> Create a Decision Summary Note using the template below. Include at least two options, explicit evaluation criteria, and consequences.</p>
    <p><strong>Output format:</strong> Structured Decision Summary Note in Markdown, one to two pages.</p>

    <ul>
      <li><strong>Never invent alternatives, rationale, or consequences.</strong> If information is missing, state "Unknown" and flag the gap.</li>
      <li><strong>Always include the rejected options and why they were rejected.</strong> This is the most important part of preventing repeated debates.</li>
      <li><strong>Label assumptions explicitly.</strong> Do not present assumptions as facts.</li>
      <li><strong>Write the decision in one clear sentence.</strong> If you cannot, ask for clarification before writing the summary.</li>
      <li><strong>Do not confuse directives with decisions.</strong> A directive from leadership is not a decision with alternatives. Document it differently.</li>
      <li><strong>Link supporting evidence, do not paste it.</strong> The summary should be compact; the evidence lives elsewhere.</li>
      <li><strong>Validate the summary with the decision maker before marking it complete.</strong></li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/decision-validation/evidence-based-recommendation-working-skill/">Evidence-Based Recommendation Working Skill</a> — Use to build the recommendation and evidence base before the decision is made.</li>
      <li><a href="/skill-hub/decision-validation/trade-off-analysis-working-skill/">Trade-Off Analysis Working Skill</a> — Use to evaluate options systematically before documenting the decision.</li>
      <li><a href="/skill-hub/work-documentation-handover/handover-note-writing-working-skill/">Handover Note Writing Working Skill</a> — Use to package decision summaries into a larger handover package.</li>
      <li><a href="/skill-hub/decision-validation/requirements-review-checklist-working-skill/">Requirements Review Checklist Working Skill</a> — Use to verify that requirements are clear before decisions are made about them.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/integration-pattern-decision-matrix/">Integration Pattern Decision Matrix</a> — Conceptual context for integration architecture decisions.</li>
      <li><a href="/atlas/concepts/data-mesh-for-sap-landscapes/">Data Mesh for SAP Landscapes</a> — Context for data governance and architecture decisions.</li>
      <li><a href="/atlas/concepts/consulting-principles-for-sap/">Consulting Principles for SAP</a> — Principles that shape SAP consulting decisions.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of decision documentation practices. It is not official BABOK, ITIL, or SAP documentation. It focuses on preventing organizational memory loss around significant decisions in enterprise and SAP contexts.</p>
    <p>Known limitations: the skill does not cover decision-making processes or facilitation techniques. It assumes the decision has already been made and the task is to document it. It does not cover legal or regulatory decision records, which may have stricter requirements. It does not replace formal Architecture Decision Records (ADRs) in software engineering contexts, though it can complement them.</p>
  </section>
</article>
