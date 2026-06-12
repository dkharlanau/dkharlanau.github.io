---
layout: default
title: "Handover Note Writing Working Skill"
description: "Produce a handover package that transfers context, decisions, risks, and open items so the receiving team can continue without starting from scratch."
permalink: /skill-hub/work-documentation-handover/handover-note-writing-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/work-documentation-handover/">Work Documentation and Handover</a></li>
    <li aria-current="page">Handover Note Writing</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Work Documentation and Handover</p>
  <h1>Handover Note Writing Working Skill</h1>
  <p class="lead">Produce a handover package that transfers context, decisions, risks, and open items so the receiving team can continue without starting from scratch.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Handover notes bridge the gap between a person or team who knows the work and a person or team who must continue it. This skill produces a Handover Package: a structured document that captures what was done, why it was done that way, what remains open, and what risks the receiver must manage. A good handover package prevents repeated questions, wrong assumptions, and knowledge loss during staff changes, project phase transitions, or contractor rotations. The output is designed to be read once and acted upon, not stored unread in a shared folder.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A consultant or team member is rolling off a project and the remaining team needs to continue the work.</li>
      <li>A project phase is ending and operations or the next implementation team needs to take ownership.</li>
      <li>A support engineer is leaving the team and the remaining engineers need to know the state of open incidents and custom configurations.</li>
      <li>A vacation or long-term absence is approaching and coverage must be prepared with enough context to make decisions.</li>
      <li>An AI agent is compiling a project close-out package and needs to know what to include and what to flag.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP support: rolling off a critical customer account</h3>
    <p>An AMS consultant has spent six months stabilizing an S/4HANA customer-vendor replication landscape. They are rolling off next week. The replacement consultant needs to know: which custom Z-transactions exist, which BP relationships are manually maintained, which IDoc message types fail every month, and which open tickets are waiting for the customer. Without a handover package, the replacement spends three weeks rediscovering what the original consultant already knew, and two critical tickets miss SLAs.</p>

    <h3>Integration project: handing over to operations after go-live</h3>
    <p>An integration team has built a middleware flow between SAP and a warehouse management system. The project is closing. The operations team needs to know: the error handling procedures, the monitoring dashboards, the escalation contacts, the rollback steps, and the known failure patterns. Without a handover package, the first production error becomes a three-hour bridge call because no one knows where to look.</p>

    <h3>Data migration: handing over master data governance to the business team</h3>
    <p>A data migration team has migrated customer and material master data into S/4HANA. The business team must now own data quality. The handover package must include: the data validation rules that were applied, the records that were rejected and why, the duplicates that were merged, the open data defects, and the governance process for future changes. Without this, the business team loads new data using old rules and recreates the same quality problems.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Project or support scope definition showing what was in scope and what was not.</li>
      <li>Decision log or meeting minutes showing key decisions, their rationale, and who made them.</li>
      <li>Inventory of custom objects, configurations, and transactions that were created or modified.</li>
      <li>List of open items, tickets, or tasks with status, owner, and next action.</li>
      <li>Risk register or known issue list with severity, impact, and mitigation status.</li>
      <li>Contact list of stakeholders, subject matter experts, and escalation paths.</li>
      <li>System documentation, diagrams, or links to existing knowledge base entries.</li>
      <li>Access credentials or instructions for how to obtain access (if handing over to a new team member).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What work has been completed, and what evidence exists that it was completed?</li>
      <li>What work is in progress, who is doing it, and what is the next step?</li>
      <li>What decisions were made, and what alternatives were rejected? Why?</li>
      <li>What custom configurations, code, or processes exist that are not standard?</li>
      <li>What are the top three risks the receiver must manage, and what should they do about them?</li>
      <li>What are the recurring failures, known workarounds, and tribal knowledge that is not documented anywhere else?</li>
      <li>Who are the key contacts for each domain, and what do they know?</li>
      <li>What access, permissions, or tools does the receiver need, and how do they get them?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Define the receiver.</strong> Identify who will read the handover package and what they need to do. A new consultant needs different detail than an operations manager. Tailor depth and tone to the receiver.</li>
      <li><strong>Collect the inputs.</strong> Gather the decision log, ticket list, custom object inventory, risk register, and contact list. If inputs are missing, flag gaps explicitly rather than guess.</li>
      <li><strong>Write the scope summary.</strong> State what was in scope, what was delivered, and what was explicitly excluded. Include dates, milestones, and any scope changes with approval references.</li>
      <li><strong>Document key decisions.</strong> For each significant decision, record: the decision, the date, the decision maker, the alternatives considered, the rationale, and the consequence. Link to the Decision Summary if one exists.</li>
      <li><strong>Catalog custom objects and configurations.</strong> List every custom transaction, report, enhancement, configuration change, or integration flow. Include purpose, owner, and location. Flag anything that is temporary or experimental.</li>
      <li><strong>List open items with owners and deadlines.</strong> For each open ticket, task, or issue: describe the item, state the current status, name the owner, specify the next action, and give a deadline or follow-up date.</li>
      <li><strong>Describe risks and mitigations.</strong> List the top risks that the receiver will face. For each: describe the risk, explain the impact, state the current mitigation, and recommend what the receiver should do next.</li>
      <li><strong>Provide access and contact information.</strong> List systems, clients, transactions, and dashboards the receiver needs. Provide contact details for escalation and subject matter experts. Do not include passwords in the document; reference the secure credential process.</li>
      <li><strong>Package and validate.</strong> Assemble the Handover Package using the template below. Review it with the outgoing person and the receiver together. Correct any gaps or misunderstandings before the handover date.</li>
      <li><strong>Store and distribute.</strong> Place the package in the agreed location with the right permissions. Confirm the receiver has access. Schedule a brief walkthrough meeting if possible.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the receiver is new to the project, include a glossary and a context paragraph before each section. If the receiver is experienced, keep it brief.</li>
      <li>If a decision has no documented rationale, state that the rationale is unknown rather than invent one.</li>
      <li>If an open item has no owner, flag it as unassigned and recommend an owner. Do not leave it blank.</li>
      <li>If a custom object is temporary or experimental, label it clearly. Do not let the receiver treat it as production-stable.</li>
      <li>If a risk has no mitigation, escalate it to management before handover. Do not hand over unowned risks.</li>
      <li>If sensitive data or credentials are needed, reference the secure process. Do not embed passwords or personal data in the package.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Handover Package</strong> — Structured document containing scope summary, decision log, custom object catalog, open item list, risk register, and contact directory. See template below.</li>
      <li><strong>Handover Walkthrough Agenda</strong> — Optional one-page agenda for a live handover meeting that walks through the package.</li>
      <li><strong>Receiver Acknowledgment</strong> — Short confirmation that the receiver has read the package and has access to all referenced systems.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Handover Package (compact)</h3>
    <pre><code>---
artifact: Handover Package
id: HOV-&lt;project&gt;-&lt;date&gt;
receiver: &lt;Name and role&gt;
outgoing: &lt;Name and role&gt;
handover_date: YYYY-MM-DD
status: draft | reviewed | approved
---

## 1. Scope Summary
- Project / Support area: &lt;Name&gt;
- In scope: &lt;What was delivered&gt;
- Out of scope: &lt;What was excluded&gt;
- Key milestones: &lt;Dates and outcomes&gt;
- Scope changes: &lt;Changes with approval references&gt;

## 2. Key Decisions
| Decision | Date | Decision Maker | Rationale | Consequence |
|----------|------|----------------|-----------|-------------|
| &lt;Decision text&gt; | YYYY-MM-DD | &lt;Name&gt; | &lt;Why&gt; | &lt;What changed&gt; |

## 3. Custom Objects and Configurations
| Object / Config | Type | Purpose | Owner | Status | Location |
|-----------------|------|---------|-------|--------|----------|
| ZCUST_REP | Z-report | Customer reconciliation | &lt;Name&gt; | Active | SE80 / &lt;package&gt; |

## 4. Open Items
| Item | Description | Status | Owner | Next Action | Due Date |
|------|-------------|--------|-------|-------------|----------|
| TICKET-1234 | BP replication timeout | Waiting for customer | &lt;Name&gt; | Send log file | YYYY-MM-DD |

## 5. Risks and Mitigations
| Risk | Impact | Mitigation | Recommended Action |
|------|--------|------------|---------------------|
| Monthly IDoc volume spikes | SLAs missed | Manual monitoring | Implement threshold alert |

## 6. Contacts and Escalation
| Role | Name | Contact | What they know |
|------|------|---------|----------------|
| Functional Lead | &lt;Name&gt; | &lt;Email&gt; | Business rules and approvals |
| Technical Lead | &lt;Name&gt; | &lt;Email&gt; | Middleware and integration |

## 7. Access and Systems
| System | Client / Environment | Purpose | How to request access |
|--------|----------------------|---------|----------------------|
| S/4HANA | 300 | Configuration | ITSM portal request |

## 8. Known Workarounds and Tribal Knowledge
- &lt;Describe workaround, when it applies, and who approved it&gt;
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The receiver can read the package once and know what to do next without asking for clarification.</li>
      <li>Every key decision has a rationale, even if the rationale is "unknown."</li>
      <li>Every open item has an owner, a next action, and a due date or follow-up date.</li>
      <li>Every custom object has a purpose, an owner, and a location.</li>
      <li>Risks are ranked by severity and every risk has a recommended action.</li>
      <li>Contact information is current and includes what each person knows.</li>
      <li>Access instructions reference the secure process; no passwords or secrets are embedded.</li>
      <li>The package has been reviewed by both the outgoing and receiving parties.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Writing a chronological narrative instead of a structured package.</strong> Consequence: the receiver must read ten pages to find one phone number. Chronological notes are for journals, not handovers.</li>
      <li><strong>Omitting the rationale behind decisions.</strong> Consequence: the receiver re-opens closed decisions because they do not understand why the original choice was made.</li>
      <li><strong>Listing open items without owners or next actions.</strong> Consequence: open items fall into a black hole after handover and surface as escalations weeks later.</li>
      <li><strong>Skipping risks because they are "obvious."</strong> Consequence: the receiver is blindsided by a known issue that the outgoing person assumed everyone knew about.</li>
      <li><strong>Embedding passwords or sharing credentials in the document.</strong> Consequence: security violation and credential rotation. Always reference the secure process.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A two-page email: "Hey, I am rolling off next week. The project went well. There are a few open tickets in the system. The customer is nice but strict about SLAs. You can find the configs in the system. Let me know if you have questions." No structure, no owners, no dates, no custom object list, no decision rationale, no risk register. The receiver has no starting point and must reverse-engineer the entire context.</p>
    <p><strong>Why it fails:</strong> The receiver wastes weeks discovering what the outgoing person already knew. Tickets miss SLAs. Decisions are re-opened. Risks become incidents.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Handover Package
id: HOV-S4-AMS-2026-001
receiver: Maria Chen, SAP Support Consultant
outgoing: Dmitry Volkov, SAP Support Consultant
handover_date: 2026-06-15
status: reviewed
---

## 1. Scope Summary
- Project / Support area: S/4HANA Customer-Vendor Replication Stabilization
- In scope: BP replication, IDoc monitoring, custom Z-report validation, monthly reconciliation
- Out of scope: New middleware implementation, pricing replication, tax number validation rules
- Key milestones: 2026-03-01 — baseline assessment; 2026-05-01 — Z-report deployed; 2026-06-10 — monthly reconciliation automated
- Scope changes: Added MDG-to-S4 replication diagnostics on 2026-04-01 (approved by S. Mueller)

## 2. Key Decisions
| Decision | Date | Decision Maker | Rationale | Consequence |
|----------|------|----------------|-----------|-------------|
| Use ZCUST_REP for monthly reconciliation instead of standard report | 2026-04-10 | D. Volkov | Standard report lacks vendor-side view | One custom report to maintain; documented in SE80 |

## 3. Custom Objects and Configurations
| Object / Config | Type | Purpose | Owner | Status | Location |
|-----------------|------|---------|-------|--------|----------|
| ZCUST_REP | Z-report | Monthly customer-vendor reconciliation | M. Chen (from 2026-06-15) | Active | SE80 / Z_AMS_RECON |
| ZIDOC_ALERT | Background job | Daily IDoc failure alert | M. Chen | Active | SM37 / ZIDOC_ALERT |

## 4. Open Items
| Item | Description | Status | Owner | Next Action | Due Date |
|------|-------------|--------|-------|-------------|----------|
| TICKET-4421 | BP relationship timeout during bulk load | Waiting for basis team | Basis Team | Increase queue worker count | 2026-06-18 |
| TASK-88 | Update ZCUST_REP material selection for new division | In progress | M. Chen | Add division filter | 2026-06-20 |

## 5. Risks and Mitigations
| Risk | Impact | Mitigation | Recommended Action |
|------|--------|------------|---------------------|
| Monthly IDoc volume spikes above 10k | SLAs missed | Manual monitoring | Implement threshold alert in SM58 |
| BP master data changes not reflected in S/4 | Orders blocked | Daily reconciliation | Review SMW01 daily for next 30 days |

## 6. Contacts and Escalation
| Role | Name | Contact | What they know |
|------|------|---------|----------------|
| Functional Lead | S. Mueller | s.mueller@company.com | Business rules, approval matrix |
| Basis Lead | T. Nguyen | t.nguyen@company.com | Queue workers, background jobs |
| Middleware Owner | K. Schmidt | k.schmidt@company.com | PI/PO mappings, error routing |

## 7. Access and Systems
| System | Client / Environment | Purpose | How to request access |
|--------|----------------------|---------|----------------------|
| S/4HANA | 300 | Configuration and monitoring | ITSM portal — request "SAP AMS 300" |
| SAP PI | Production | Middleware monitoring | ITSM portal — request "SAP PI Monitoring" |

## 8. Known Workarounds and Tribal Knowledge
- When BP replication fails with status 51 in SMW01, run ZCUST_REP first to check if the customer exists before re-triggering the IDoc. Re-triggering without existence check causes duplicate partner entries.
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Handover package writer for an SAP enterprise project.</p>
    <p><strong>Context:</strong> You have project records, ticket lists, decision logs, and system documentation. You need to produce a Handover Package that a new team member can read and act on.</p>
    <p><strong>Task:</strong> Create a structured Handover Package using the template below. Include scope summary, key decisions, custom objects, open items, risks, contacts, and access instructions.</p>
    <p><strong>Output format:</strong> Structured Handover Package in Markdown, with tables for decisions, objects, open items, and risks.</p>

    <ul>
      <li><strong>Never invent decisions, owners, or deadlines.</strong> If an input is missing, state "Unknown" or "Unassigned" and flag it as a gap.</li>
      <li><strong>Always include the rationale behind key decisions.</strong> If the rationale is missing, state "Rationale not documented."</li>
      <li><strong>Label temporary or experimental custom objects clearly.</strong> Do not let the receiver treat them as production-stable.</li>
      <li><strong>Every open item must have an owner, a next action, and a due date.</strong> If any are missing, flag them explicitly.</li>
      <li><strong>Do not embed passwords, tokens, or personal data in the package.</strong> Reference the secure access process.</li>
      <li><strong>Write for the receiver, not the sender.</strong> Use the receiver's level of knowledge as the baseline. Include a glossary if the receiver is new.</li>
      <li><strong>Link to Atlas diagnostics</strong> when the handover touches SAP support areas. For example, BP replication handovers should reference <a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/work-documentation-handover/decision-summary-writing-working-skill/">Decision Summary Writing Working Skill</a> — Use to document the rationale behind key decisions before adding them to the handover package.</li>
      <li><a href="/skill-hub/work-documentation-handover/status-update-writing-working-skill/">Status Update Writing Working Skill</a> — Use to capture the current state of open items before handover.</li>
      <li><a href="/skill-hub/sap-ams/operational-knowledge-capture-working-skill/">Operational Knowledge Capture Working Skill</a> — Use to capture tribal knowledge that belongs in the handover package.</li>
      <li><a href="/skill-hub/work-documentation-handover/lessons-learned-capture-working-skill/">Lessons Learned Capture Working Skill</a> — Use to capture improvements that the next team should implement.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a> — Diagnostic context for BP replication handovers.</li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> — Monitoring context for IDoc-related handovers.</li>
      <li><a href="/atlas/automation/operational-memory-for-sap-ams/">Operational Memory for SAP AMS</a> — Framework for capturing and transferring operational knowledge.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of knowledge transfer practices. It is not official ITIL, BABOK, or SAP documentation. It focuses on practical handover packages for enterprise and SAP contexts where knowledge loss is expensive and receivers are often new to the environment.</p>
    <p>Known limitations: the skill assumes the outgoing person has some documentation to work with. It does not cover formal legal handover processes, intellectual property transfers, or classified environment transfers. It does not replace live walkthroughs; it complements them. The templates should be adapted to the organization's wiki, document management system, or knowledge base.</p>
  </section>
</article>
