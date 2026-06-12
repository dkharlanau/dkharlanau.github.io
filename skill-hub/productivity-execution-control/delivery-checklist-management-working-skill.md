---
layout: default
title: "Delivery Checklist Management Working Skill"
description: "Build and maintain a delivery checklist that confirms every prerequisite is complete, every risk is addressed, and every stakeholder is ready before a milestone is declared done."
permalink: /skill-hub/productivity-execution-control/delivery-checklist-management-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/productivity-execution-control/">Productivity and Execution Control</a></li>
    <li aria-current="page">Delivery Checklist Management</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Productivity and Execution Control</p>
  <h1>Delivery Checklist Management Working Skill</h1>
  <p class="lead">Build and maintain a delivery checklist that confirms every prerequisite is complete, every risk is addressed, and every stakeholder is ready before a milestone is declared done.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Projects go live with missing prerequisites because no one checked systematically. A transport is imported but the authorization role was never updated. A report is delivered but the user training was skipped. A data migration is declared complete but the reconciliation was never run. This skill prevents those failures by creating a Delivery Checklist: a structured list of prerequisites, verifications, and approvals that must be satisfied before a milestone is declared complete. The checklist is not a generic template; it is built for the specific milestone based on the work packages, risks, and stakeholders involved. It is reviewed and signed off by the people who have the authority to say yes. The checklist turns a subjective "I think we are ready" into an objective "These 12 items are all green."</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A project phase, sprint, or release is approaching its end and the team must confirm readiness.</li>
      <li>A system change, configuration update, or data migration is scheduled for production deployment.</li>
      <li>A deliverable is promised to a stakeholder and the team needs to verify quality before handover.</li>
      <li>A go-live or cutover date is set and the project manager needs a structured readiness check.</li>
      <li>A previous milestone failed because a prerequisite was missed, and the team wants to prevent recurrence.</li>
      <li>An AI agent is validating a delivery and needs a checklist to verify completeness against a standard.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP go-live: missing transport sequence</h3>
    <p>An SAP project team prepares for a go-live on Friday. The configuration is complete in the test system. The transport request is created. On Friday morning, the import to production fails because a prerequisite transport was never released from development. The team spends six hours reconstructing the sequence. The go-live is delayed to Saturday. A Delivery Checklist would have included an item: "All prerequisite transports are released and documented in the transport sequence document." The item would have been checked on Wednesday, the gap would have been found, and the go-live would have proceeded on schedule.</p>

    <h3>Integration deployment: untested error handling</h3>
    <p>A team deploys a new API integration between SAP and a warehouse management system. The happy path is tested. The deployment checklist says "Integration tested." It does not specify what "tested" means. In production, an invalid material number causes an unhandled error that crashes the middleware. The error handling was never tested because the checklist had no item for it. A Delivery Checklist would have included: "Error handling tested for invalid material, missing customer, and timeout scenarios." The team would have found the gap before go-live.</p>

    <h3>Report delivery: incomplete user documentation</h3>
    <p>A business intelligence team delivers a new management report to the finance department. The report runs correctly. The checklist marks it complete. The finance team tries to use it and discovers that the parameter definitions are not documented, the refresh schedule is not explained, and the data sources are not listed. The report is rejected. A Delivery Checklist would have included: "User documentation includes parameter definitions, refresh schedule, data sources, and known limitations." The documentation would have been completed and reviewed before delivery.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Milestone definition: what is being delivered, to whom, and by when.</li>
      <li>Work Breakdown Structure or task list showing all work packages that feed into the milestone.</li>
      <li>Quality checklist from each work package showing what was verified and what was not.</li>
      <li>Risk register showing risks that could prevent a successful delivery.</li>
      <li>Stakeholder list showing who must approve or accept the deliverable.</li>
      <li>Environment and system details: clients, systems, transports, versions, and configurations involved.</li>
      <li>Historical data from previous deliveries showing what was missed and what caused failure.</li>
      <li>Regulatory or compliance requirements that must be satisfied before delivery (optional).</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What is the minimum set of conditions that must be true for this milestone to be considered successful?</li>
      <li>What was missed in the last similar delivery, and how do we prevent it this time?</li>
      <li>Who has the authority to approve each item on the checklist?</li>
      <li>What must be verified in the target environment, not just in the development environment?</li>
      <li>What happens if we go live without this item being complete?</li>
      <li>What documentation must the user or operator have to use the deliverable correctly?</li>
      <li>What rollback or recovery plan is needed if the delivery fails?</li>
      <li>What is the last responsible moment to check each item before the deadline?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Define the milestone.</strong> State what is being delivered, to whom, by what date, and in what environment. If the milestone is vague, clarify it before building the checklist.</li>
      <li><strong>Identify the categories of readiness.</strong> Group checklist items into categories: technical readiness, data readiness, configuration readiness, testing readiness, documentation readiness, user readiness, operational readiness, and sign-off readiness. This ensures no category is forgotten.</li>
      <li><strong>Derive items from the WBS.</strong> For each work package that feeds into the milestone, define the prerequisite that must be verified. Example: if the WBS includes "credit management configuration," the checklist item is: "Credit management configuration is active in target client and verified with test customer."</li>
      <li><strong>Derive items from risks.</strong> For each risk in the risk register, define a verification that confirms the risk is mitigated. Example: if the risk is "API timeout under load," the checklist item is: "Load test confirms API response time under 2 seconds at 100 concurrent requests."</li>
      <li><strong>Derive items from history.</strong> For each failure or near-miss from a previous delivery, define a checklist item that prevents recurrence. Example: if the last go-live failed due to missing authorization, the item is: "All required authorization roles are transported and tested in the target client."</li>
      <li><strong>Define the verification method for each item.</strong> State how the item will be checked: inspection, test, log review, sign-off, or document review. An item without a verification method is a wish, not a checklist entry.</li>
      <li><strong>Assign an approver for each item.</strong> Name the person who has the authority to mark the item complete. If the approver is a role, name the person currently in that role.</li>
      <li><strong>Sequence the items by dependency.</strong> Some items must be checked before others. Order the checklist so that prerequisites are verified first. Example: system access must be checked before configuration testing.</li>
      <li><strong>Define the last responsible moment.</strong> For each item, state the latest date by which it must be checked to allow time for remediation if it fails.</li>
      <li><strong>Review the checklist with stakeholders.</strong> Walk through the checklist with the project sponsor, the technical lead, and the business owner. Confirm that every item is necessary and that no item is missing. Update the checklist based on feedback.</li>
      <li><strong>Execute the checklist.</strong> Check each item in sequence. Record the result, the evidence, and the approver. If an item fails, stop the checklist, remediate, and re-check. Do not proceed to the next milestone item until the current one is green.</li>
      <li><strong>Sign off the checklist.</strong> When all items are green, the milestone owner signs the checklist. The signed checklist is evidence of readiness. It is stored with the project records.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If an item has no verification method, it is not a checklist item. Define the method or remove it.</li>
      <li>If an item has no approver, it is not a checklist item. Assign an approver or remove it.</li>
      <li>If an item fails, the checklist stops. Remediate and re-check before proceeding.</li>
      <li>If a failed item cannot be remediated by the milestone date, the milestone is delayed or the item is removed from scope with a change log entry.</li>
      <li>If an item is waived, record the waiver with a reason, a risk assessment, and the authority who approved the waiver.</li>
      <li>If the checklist is shorter than five items, it is probably incomplete. Review against the WBS and risk register.</li>
      <li>If the checklist is longer than 30 items, it may be too granular. Group related items into a higher-level verification.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Delivery Checklist</strong> — Structured list of readiness items with categories, verification methods, approvers, sequence, last responsible moments, and results. See template below.</li>
      <li><strong>Evidence Package</strong> — Collection of test logs, screenshots, sign-off documents, and configuration exports that prove each checklist item was verified.</li>
      <li><strong>Sign-Off Record</strong> — Document showing who approved the checklist and when, with any waivers recorded.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Delivery Checklist (compact)</h3>
    <pre><code>---
artifact: Delivery Checklist
milestone: &lt;name&gt;
target_date: YYYY-MM-DD
environment: &lt;system / client&gt;
status: draft | in review | executing | complete | waived
---

## Technical readiness
| ID | Item | Verification | Approver | Last responsible moment | Result | Evidence | Notes |
|----|------|--------------|----------|------------------------|--------|----------|-------|
| CL-001 | &lt;Prerequisite&gt; | &lt;How to check&gt; | &lt;name&gt; | YYYY-MM-DD | pass | &lt;reference&gt; | &lt;notes&gt; |
| CL-002 | &lt;Prerequisite&gt; | &lt;How to check&gt; | &lt;name&gt; | YYYY-MM-DD | pass | &lt;reference&gt; | &lt;notes&gt; |

## Data readiness
| ID | Item | Verification | Approver | Last responsible moment | Result | Evidence | Notes |
|----|------|--------------|----------|------------------------|--------|----------|-------|
| CL-003 | &lt;Prerequisite&gt; | &lt;How to check&gt; | &lt;name&gt; | YYYY-MM-DD | pass | &lt;reference&gt; | &lt;notes&gt; |

## Testing readiness
| ID | Item | Verification | Approver | Last responsible moment | Result | Evidence | Notes |
|----|------|--------------|----------|------------------------|--------|----------|-------|
| CL-004 | &lt;Prerequisite&gt; | &lt;How to check&gt; | &lt;name&gt; | YYYY-MM-DD | pass | &lt;reference&gt; | &lt;notes&gt; |

## Documentation readiness
| ID | Item | Verification | Approver | Last responsible moment | Result | Evidence | Notes |
|----|------|--------------|----------|------------------------|--------|----------|-------|
| CL-005 | &lt;Prerequisite&gt; | &lt;How to check&gt; | &lt;name&gt; | YYYY-MM-DD | pass | &lt;reference&gt; | &lt;notes&gt; |

## Sign-off
| Role | Name | Date | Signature |
|------|------|------|-----------|
| Project sponsor | &lt;name&gt; | YYYY-MM-DD | &lt;signature&gt; |
| Technical lead | &lt;name&gt; | YYYY-MM-DD | &lt;signature&gt; |

## Waivers
| ID | Item | Reason | Risk | Approved by | Date |
|----|------|--------|------|-------------|------|
| — | — | — | — | — | — |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>Every item is derived from a work package, a risk, or a historical failure.</li>
      <li>Every item has a defined verification method that produces evidence.</li>
      <li>Every item has a named approver with the authority to sign off.</li>
      <li>Items are sequenced by dependency: prerequisites are checked first.</li>
      <li>Every item has a last responsible moment that allows time for remediation.</li>
      <li>Failed items are remediated and re-checked before the milestone proceeds.</li>
      <li>Any waived items are documented with a reason, risk assessment, and approver.</li>
      <li>The checklist is reviewed with stakeholders before execution.</li>
      <li>The checklist is signed off by the milestone owner when complete.</li>
      <li>The evidence package is stored with the project records.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Copying a generic checklist without tailoring it to the milestone.</strong> Consequence: irrelevant items waste time, and critical items specific to this delivery are missing. The checklist gives false confidence.</li>
      <li><strong>Treating the checklist as a formality to be filled after the milestone.</strong> Consequence: the checklist is completed from memory, not from verification. Failed items are not discovered until production fails.</li>
      <li><strong>Defining items without verification methods.</strong> Consequence: an item says "integration is stable" with no definition of what stable means. The approver guesses and signs off. The integration fails in production.</li>
      <li><strong>Assigning approvers who are not accountable.</strong> Consequence: a junior analyst is asked to approve a configuration change they do not understand. They sign to avoid conflict, and the error is not caught.</li>
      <li><strong>Proceeding with a failed item because the deadline is near.</strong> Consequence: the known risk is accepted implicitly instead of explicitly. When the risk materializes, there is no record of the decision to accept it, and accountability is diffuse.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A mental note: "We tested everything, the documentation is there, the users know about it. Let's go live." No written checklist, no evidence, no named approvers, no sequence. The team proceeds on collective optimism. When something fails in production, no one can say what was checked or who approved it. The post-mortem is a blame exercise because there is no record of the readiness check.</p>
    <p><strong>Why it fails:</strong> The readiness check is invisible and unaccountable. It relies on memory and assumption. It cannot be audited, repeated, or improved. The team learns nothing from success or failure because there is no evidence of what was done.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Delivery Checklist
milestone: O2C Credit Management — Test Environment Ready
target_date: 2026-06-16
environment: S/4 Test Client 300
status: complete
---

## Technical readiness
| ID | Item | Verification | Approver | Last responsible moment | Result | Evidence | Notes |
|----|------|--------------|----------|------------------------|--------|----------|-------|
| CL-101 | Credit management config transported to client 300 | Import log in STMS shows success | Maria Chen | 2026-06-14 | pass | STMS log DEVK123456 | — |
| CL-102 | RFC destination for credit check is active | SM59 connection test passes | Dmitri Volkov | 2026-06-14 | pass | SM59 screenshot | — |
| CL-103 | Authorization roles for credit team are active | SUIM role comparison shows no gaps | Basis lead | 2026-06-14 | pass | SUIM report | — |

## Data readiness
| ID | Item | Verification | Approver | Last responsible moment | Result | Evidence | Notes |
|----|------|--------------|----------|------------------------|--------|----------|-------|
| CL-201 | Test customer C-10001 has credit limit 50,000 EUR | XD03 shows limit 50,000 | Sarah Okafor | 2026-06-15 | pass | XD03 screenshot | — |
| CL-202 | Test customer C-10002 has open orders at 48,000 EUR | VA05 shows open order value | Sarah Okafor | 2026-06-15 | pass | VA05 export | — |

## Testing readiness
| ID | Item | Verification | Approver | Last responsible moment | Result | Evidence | Notes |
|----|------|--------------|----------|------------------------|--------|----------|-------|
| CL-301 | Positive path: order below limit proceeds | VA01 creates order with status Open | Maria Chen | 2026-06-15 | pass | Test log TS-101-POS | — |
| CL-302 | Negative path: order above limit is blocked | VA01 creates order with status Credit block | Maria Chen | 2026-06-15 | pass | Test log TS-101-NEG | — |
| CL-303 | Error handling: invalid customer is rejected | Order creation fails with correct message | Maria Chen | 2026-06-15 | pass | Test log TS-101-ERR | — |

## Documentation readiness
| ID | Item | Verification | Approver | Last responsible moment | Result | Evidence | Notes |
|----|------|--------------|----------|------------------------|--------|----------|-------|
| CL-401 | Configuration guide updated with credit procedure | Document reviewed by peer | Dmitri Volkov | 2026-06-15 | pass | Doc v1.2 | — |
| CL-402 | User guide for credit team updated | Guide reviewed by credit team lead | Sarah Okafor | 2026-06-15 | pass | Guide v1.1 | — |

## Sign-off
| Role | Name | Date | Signature |
|------|------|------|-----------|
| Project sponsor | Anna Kowalski | 2026-06-15 | AK |
| Technical lead | Maria Chen | 2026-06-15 | MC |

## Waivers
| ID | Item | Reason | Risk | Approved by | Date |
|----|------|--------|------|-------------|------|
| — | — | — | — | — | — |
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Delivery checklist manager for enterprise project milestones.</p>
    <p><strong>Context:</strong> You have a milestone definition, a Work Breakdown Structure, a risk register, and historical data from previous deliveries. You need to build a Delivery Checklist that verifies readiness before the milestone is declared complete.</p>
    <p><strong>Task:</strong> Derive checklist items from the WBS, risks, and history. Organize them by category. Define verification methods, approvers, sequence, and last responsible moments. Execute the checklist and record results.</p>
    <p><strong>Output format:</strong> Structured Delivery Checklist per the template, followed by an evidence package summary and a sign-off record.</p>

    <ul>
      <li><strong>Never use a generic checklist without tailoring.</strong> Every checklist must be derived from the specific WBS, risks, and history of this milestone.</li>
      <li><strong>Every item must have a verification method.</strong> An item without a method is a wish, not a checklist entry.</li>
      <li><strong>Every item must have a named approver.</strong> The approver must have the authority and knowledge to verify the item.</li>
      <li><strong>Sequence items by dependency.</strong> Prerequisites first. Do not check user readiness before technical readiness is confirmed.</li>
      <li><strong>Stop on failure.</strong> If an item fails, do not proceed. Remediate and re-check.</li>
      <li><strong>Record waivers explicitly.</strong> If an item is skipped, document the reason, risk, and approving authority.</li>
      <li><strong>Do not invent verification results.</strong> Only mark an item pass if you have evidence. If evidence is missing, flag the item as pending.</li>
      <li><strong>Store the evidence package with the project records.</strong> The checklist without evidence is not proof of readiness.</li>
      <li><strong>Link to Atlas diagnostics</strong> when checklist items involve SAP technical verification. Reference the relevant diagnostic page for the verification method.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/productivity-execution-control/work-breakdown-planning-working-skill/">Work Breakdown Planning Working Skill</a> — Use to create the WBS that feeds into the checklist.</li>
      <li><a href="/skill-hub/productivity-execution-control/follow-up-tracking-working-skill/">Follow-Up Tracking Working Skill</a> — Use to track checklist items that depend on external commitments.</li>
      <li><a href="/skill-hub/decision-validation/risk-dependency-mapping-working-skill/">Risk-Dependency Mapping Working Skill</a> — Use to identify risks that become checklist items.</li>
      <li><a href="/skill-hub/decision-validation/test-scenario-derivation-working-skill/">Test Scenario Derivation Working Skill</a> — Use to derive testing checklist items from requirements.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-credit-management-diagnostics/">SAP Credit Management Diagnostics</a> — Verification context for credit management readiness checklists.</li>
      <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a> — Verification context for integration readiness checklists.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of delivery checklist practices. It is not official PMP, ITIL, or SAP go-live methodology. It focuses on practical readiness verification for enterprise milestones where missing prerequisites cause production failures and rework.</p>
    <p>Known limitations: the skill assumes the WBS and risk register are available. It does not cover automated deployment pipelines, continuous delivery, or infrastructure-as-code verification. For organizations with mature DevOps practices, the checklist may be partially automated. The skill treats the checklist as a human-verified artifact, not a machine-generated report. For regulated industries, additional compliance checks and audit trails may be required beyond the scope of this skill.</p>
  </section>
</article>
