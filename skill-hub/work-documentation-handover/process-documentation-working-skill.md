---
layout: default
title: "Process Documentation Working Skill"
description: "Document how a business process actually works, who owns each step, what systems are involved, and where it breaks."
permalink: /skill-hub/work-documentation-handover/process-documentation-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/work-documentation-handover/">Work Documentation and Handover</a></li>
    <li aria-current="page">Process Documentation</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Work Documentation and Handover</p>
  <h1>Process Documentation Working Skill</h1>
  <p class="lead">Document how a business process actually works, who owns each step, what systems are involved, and where it breaks.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Most business processes exist partially in people's heads, partially in system configurations, and partially in outdated wiki pages. This skill produces a Process Document: a structured description of how a process actually operates, not how it is supposed to operate. The document captures the sequence of steps, the systems and transactions used, the owners and approvers, the data inputs and outputs, and the known failure points. The output is designed to help new team members, auditors, and AI agents understand the process without relying on tribal knowledge. It is also the foundation for process improvement, automation, and training.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A process exists only in the heads of a few people and the team needs to capture it before they leave or go on vacation.</li>
      <li>An audit or compliance review requires documented process evidence showing who does what and where.</li>
      <li>A process is being considered for automation or improvement and the team needs a baseline of current state.</li>
      <li>A new team member needs to understand a process quickly without shadowing someone for two weeks.</li>
      <li>A process is generating repeated errors or incidents and the team needs to map the breakpoints to fix them.</li>
      <li>An AI agent needs to understand a process to suggest improvements or generate automation logic.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>

    <h3>SAP order-to-cash: shadowing the process to find gaps</h3>
    <p>A new SAP functional consultant needs to understand how the order-to-cash process works in a specific S/4HANA system. The process is not standard: custom credit checks, a modified delivery block logic, and a manual step where a sales admin updates a Z-table. The existing documentation is a three-year-old PowerPoint that does not mention the Z-table. The consultant uses this skill to document the actual process: sales order creation in VA01, credit check via custom transaction ZCREDIT, delivery block removal in VL02N, manual Z-table update by the sales admin, and goods issue in VL02N. Without this documentation, the consultant misses the Z-table step and creates orders that fail downstream.</p>

    <h3>Master data governance: mapping the vendor creation process</h3>
    <p>The vendor master data creation process involves three departments: procurement requests the vendor, finance validates the tax number, and master data maintains the record in SAP. The process breaks when finance takes five days to validate and procurement creates duplicate records because they do not know the vendor is already in process. The team documents the actual process: request form in the portal, validation queue in a shared mailbox, manual entry in SAP via FK01, and notification to procurement. The documentation reveals the bottleneck and the duplication trigger. The team then redesigns the process with a status tracker.</p>

    <h3>Integration operations: documenting the IDoc error handling flow</h3>
    <p>An integration team handles failed IDocs between SAP and a warehouse system. The process is reactive: a monitoring alert fires, an operator checks SM58, opens the IDoc in WE02, checks the mapping in SAP PI, and either reprocesses or forwards to the functional team. The process is not documented. When the senior operator is on vacation, a junior operator reprocesses an IDoc with a mapping error, causing duplicate warehouse movements. The team uses this skill to document the actual flow with decision points: if status is 51, check WE02 first; if error is mapping, forward to PI team; if error is data, forward to functional team; never reprocess without checking the error category.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li>Subject matter expert or process owner who can walk through the actual steps.</li>
      <li>System documentation showing transactions, tables, programs, and configurations involved.</li>
      <li>Sample documents or screenshots showing the process in action (optional but helpful).</li>
      <li>Incident or ticket history showing where the process breaks.</li>
      <li>Organizational chart or role definitions showing who owns each step.</li>
      <li>Existing process documentation, even if outdated, to understand what has changed.</li>
      <li>Data flow diagrams or integration maps if the process crosses systems.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>What triggers the process? What is the first event or input?</li>
      <li>What is the sequence of steps? What happens first, second, third?</li>
      <li>Who performs each step? What is their role, and what system access do they need?</li>
      <li>What systems, transactions, or programs are used at each step?</li>
      <li>What data enters the process, what data is transformed, and what data leaves the process?</li>
      <li>Where does the process break? What are the top three failure points?</li>
      <li>What are the workarounds? When the process breaks, what do people actually do?</li>
      <li>What are the breakpoints between manual and automated steps?</li>
      <li>What are the compliance, audit, or SLA requirements that constrain the process?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Identify the process scope.</strong> Define the start and end of the process. Name the process and the version of the system it runs on. State what is in scope and what is out of scope.</li>
      <li><strong>Interview the process owner.</strong> Ask the person who performs the process to walk through it step by step. Do not accept summary descriptions. Ask for transaction codes, screen names, and field names.</li>
      <li><strong>Shadow the process if possible.</strong> Watch the process owner perform the steps. Record the actual sequence, not the theoretical one. Note deviations, workarounds, and shortcuts.</li>
      <li><strong>Map the steps.</strong> Create a numbered list of steps. For each step: name the action, identify the actor, list the system or transaction, describe the input, describe the output, and note the decision logic.</li>
      <li><strong>Identify breakpoints.</strong> Mark where the process fails, where manual intervention is required, where data quality issues arise, and where handoffs between teams occur.</li>
      <li><strong>Document workarounds.</strong> For each known failure point, document the workaround that people actually use. Include when the workaround is valid and when it is dangerous.</li>
      <li><strong>Validate with the process owner.</strong> Walk through the document with the person who performs the process. Correct errors, add missing steps, and clarify ambiguous descriptions.</li>
      <li><strong>Validate with a new person.</strong> Ask someone who does not know the process to follow the document. If they cannot, the document is incomplete.</li>
      <li><strong>Write the Process Document.</strong> Use the template below. Include process summary, step list, system map, owner matrix, breakpoint analysis, and known workarounds.</li>
      <li><strong>Publish and maintain.</strong> Store the document in the agreed location. Set a review date. Update the document when the process changes, not when someone complains that it is wrong.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the process owner describes the ideal process, ask for the actual process. Document what happens, not what should happen.</li>
      <li>If a step has no system transaction, document it as a manual step and note the tool or format used.</li>
      <li>If a breakpoint is caused by a known system limitation, document the limitation and the workaround. Do not pretend the system works perfectly.</li>
      <li>If a process crosses multiple systems, document each system handoff as a separate step with its own owner and validation.</li>
      <li>If a process has multiple variants, document the most common variant first and list exceptions separately.</li>
      <li>If a step is performed by a different person depending on the day or shift, document the variability and the escalation rule.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Process Document</strong> — Structured description of the actual process, including steps, owners, systems, breakpoints, and workarounds. See template below.</li>
      <li><strong>Process Owner Matrix</strong> — Table showing each step, the responsible role, and the escalation contact.</li>
      <li><strong>Breakpoint Analysis</strong> — List of known failure points, their frequency, impact, and current workarounds.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>

    <h3>Process Document (compact)</h3>
    <pre><code>---
artifact: Process Document
id: PROC-&lt;area&gt;-&lt;number&gt;
process_name: &lt;Name of process&gt;
scope_start: &lt;Trigger event&gt;
scope_end: &lt;End state&gt;
system: &lt;Primary system, e.g., S/4HANA&gt;
version: &lt;System version or release&gt
document_date: YYYY-MM-DD
owner: &lt;Process owner name and role&gt
doc_author: &lt;Document author&gt
doc_reviewer: &lt;Document reviewer&gt
doc_status: draft | reviewed | approved
---

## Process Summary
- Trigger: &lt;What starts the process&gt;
- End state: &lt;What successful completion looks like&gt;
- Frequency: &lt;How often the process runs&gt;
- SLA: &lt;Time or quality target&gt;
- Compliance requirement: &lt;Audit or regulatory requirement&gt;

## Process Steps
| Step | Action | Actor | System / Transaction | Input | Output | Decision Rule |
|------|--------|-------|---------------------|-------|--------|---------------|
| 1 | &lt;Action&gt; | &lt;Role&gt; | &lt;T-code or program&gt; | &lt;Data or document&gt; | &lt;Result&gt; | &lt;If X then Y&gt; |
| 2 | &lt;Action&gt; | &lt;Role&gt; | &lt;T-code or program&gt; | &lt;Data or document&gt; | &lt;Result&gt; | &lt;If X then Y&gt; |

## System and Data Flow
- &lt;Describe data movement between systems, tables, and interfaces&gt;

## Owner Matrix
| Step | Primary Owner | Backup Owner | Escalation Contact |
|------|---------------|--------------|---------------------|
| 1 | &lt;Name&gt; | &lt;Name&gt; | &lt;Name&gt; |

## Breakpoints and Workarounds
| Breakpoint | Symptom | Frequency | Workaround | Risk of Workaround |
|------------|---------|-----------|------------|-------------------|
| &lt;Where it breaks&gt; | &lt;What the user sees&gt; | &lt;How often&gt; | &lt;What people do&gt; | &lt;What could go wrong&gt; |

## Related Documents
- &lt;Link to decision log, runbook, or knowledge article&gt;
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The process document describes the actual process, not the ideal process.</li>
      <li>Every step has a specific action, actor, system, input, and output.</li>
      <li>Decision rules are documented for steps that branch based on conditions.</li>
      <li>Known breakpoints and workarounds are documented honestly.</li>
      <li>A person who does not know the process can follow the document and perform the steps.</li>
      <li>The process owner has reviewed and approved the document.</li>
      <li>System transactions, tables, and programs are named explicitly.</li>
      <li>The document is stored in a findable location with a review date.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Documenting the ideal process instead of the actual process.</strong> Consequence: new team members follow the document, hit a real-world deviation, and do not know what to do. The document becomes unreliable.</li>
      <li><strong>Using generic step descriptions without transaction codes or screen names.</strong> Consequence: the reader cannot locate the exact screen or program. "Go to the material screen" is not enough; "MM03, display material, basic data 1 tab" is.</li>
      <li><strong>Omitting workarounds.</strong> Consequence: when the process breaks, people invent ad-hoc fixes that are not validated, leading to data quality issues or compliance violations.</li>
      <li><strong>Documenting a process without validating it with a new person.</strong> Consequence: the document contains gaps that the expert forgot to mention. The new person discovers them the hard way.</li>
      <li><strong>Writing the document once and never updating it.</strong> Consequence: the document becomes outdated within months. People stop trusting it and revert to asking the expert directly.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>

    <h3>Weak output</h3>
    <p>A one-page wiki entry: "The order-to-cash process starts with a sales order. The order is checked for credit. Then it is delivered. Then it is billed. Then it is paid. The sales team handles orders. The finance team handles billing. If there are issues, contact the functional lead." No transaction codes, no step numbers, no decision rules, no breakpoints, no workarounds, no system names. The reader learns nothing useful about how to actually perform the process.</p>
    <p><strong>Why it fails:</strong> The document is so generic that it applies to any company. It does not help a new person perform the process. It does not reveal breakpoints. It cannot be used for automation or improvement.</p>

    <h3>Strong output</h3>
    <pre><code>---
artifact: Process Document
id: PROC-O2C-2026-001
process_name: S/4HANA Order-to-Cash with Custom Credit Check
scope_start: Customer purchase order received
scope_end: Payment posted in FI
system: S/4HANA 2023
version: 2023 FPS01
document_date: 2026-06-10
owner: S. Mueller, Sales Process Lead
doc_author: M. Chen
doc_reviewer: S. Mueller
doc_status: approved
---

## Process Summary
- Trigger: Customer purchase order received via EDI or portal
- End state: Payment posted in FI, customer account cleared
- Frequency: 200–400 orders per day
- SLA: Order to delivery within 48 hours; invoice within 24 hours of delivery
- Compliance requirement: All credit checks must be logged in ZCREDIT_LOG for audit

## Process Steps
| Step | Action | Actor | System / Transaction | Input | Output | Decision Rule |
|------|--------|-------|---------------------|-------|--------|---------------|
| 1 | Create sales order | Sales Admin | VA01 | Purchase order | Sales order number | If customer is new, trigger credit check step 2a |
| 2 | Run custom credit check | Sales Admin | ZCREDIT | Customer number, order value | Credit status: green / yellow / red | If red, block order and notify finance (step 2b) |
| 3 | Remove delivery block | Warehouse Planner | VL02N | Sales order, stock availability | Delivery document | If stock is insufficient, create backorder (step 3a) |
| 4 | Perform goods issue | Warehouse Clerk | VL02N | Delivery document, pick list | Goods issue document, inventory update | If batch determination fails, use manual batch (step 4a) |
| 5 | Create invoice | Billing Clerk | VF01 | Delivery document, pricing data | Invoice document | If pricing is incomplete, trigger incompletion log (step 5a) |
| 6 | Post payment | Finance Clerk | F-28 | Bank statement, invoice | Payment document, cleared item | If payment is partial, create dunning note (step 6a) |

## System and Data Flow
- Purchase order arrives via EDI -> IDoc processed in WE02 -> Sales order created in VA01 -> Credit check writes to ZCREDIT_LOG -> Delivery created in VL02N -> Goods issue updates MARD -> Invoice created in VF01 -> Accounting document in BKPF -> Payment posted in F-28.

## Breakpoints and Workarounds
| Breakpoint | Symptom | Frequency | Workaround | Risk of Workaround |
|------------|---------|-----------|------------|-------------------|
| ZCREDIT times out for high-volume customers | Credit status remains blank | 2–3 times per week | Sales admin runs ZCREDIT manually after 5 minutes | Order may ship without credit check; audit log missing |
| Batch determination fails for new materials | "No batch found" error | Daily for new SKUs | Warehouse clerk manually selects batch in MSC1N | Wrong batch selected; expiry risk if not verified |
| Pricing incomplete for promotional materials | Incompletion log blocks billing | Weekly during promotions | Billing clerk manually updates pricing in VK11 | Incorrect pricing posted; margin impact |

## Related Documents
- Decision Log: DS-O2C-2026-001 (custom credit check rationale)
- Runbook: RB-ZCREDIT-001 (manual credit check procedure)
- Knowledge Article: KA-001 (batch determination troubleshooting)
</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>

    <h3>AI Prompt Pattern</h3>
    <p><strong>Role:</strong> Process documentation writer for an SAP enterprise environment.</p>
    <p><strong>Context:</strong> You have interviewed a process owner and observed a business process. You need to produce a Process Document that a new person can follow without additional explanation.</p>
    <p><strong>Task:</strong> Create a structured Process Document using the template below. Include actual steps, systems, owners, breakpoints, and workarounds. Document the actual process, not the ideal one.</p>
    <p><strong>Output format:</strong> Structured Process Document in Markdown with tables for steps, owners, breakpoints, and system flow.</p>

    <ul>
      <li><strong>Never document the ideal process if the actual process differs.</strong> The value of process documentation is in capturing reality, not theory.</li>
      <li><strong>Always include transaction codes, program names, and table names.</strong> "Go to the material screen" is not enough. Use exact names: MM03, basic data 1.</li>
      <li><strong>Always document workarounds and breakpoints.</strong> If people use a workaround, document it with its conditions and risks. Do not hide it.</li>
      <li><strong>Validate the document with the process owner and a new person.</strong> If the new person cannot follow it, the document is incomplete.</li>
      <li><strong>Do not invent steps, owners, or systems.</strong> If you are unsure, state "Unknown" and flag for review.</li>
      <li><strong>Link to Atlas diagnostics</strong> when the process touches SAP areas with documented failure modes. For example, order-to-cash processes should reference <a href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">SAP Incompletion Procedure Diagnostics</a>.</li>
      <li><strong>Update the document when the process changes.</strong> A process document that is outdated is worse than no document because it creates false confidence.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/work-documentation-handover/runbook-writing-working-skill/">Runbook Writing Working Skill</a> — Use to produce the step-by-step operational procedures for specific breakpoints in the process.</li>
      <li><a href="/skill-hub/work-documentation-handover/knowledge-article-writing-working-skill/">Knowledge Article Writing Working Skill</a> — Use to document known workarounds and troubleshooting steps as self-service articles.</li>
      <li><a href="/skill-hub/business-analysis/process-analysis-working-skill/">Process Analysis Working Skill</a> — Use to analyze and redesign the process before documenting it.</li>
      <li><a href="/skill-hub/work-documentation-handover/handover-note-writing-working-skill/">Handover Note Writing Working Skill</a> — Use to package process documentation into a handover package.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/concepts/order-to-cash/">Order-to-Cash</a> — Conceptual context for O2C process documentation.</li>
      <li><a href="/atlas/diagnostics/sap-incompletion-procedure-diagnostics/">SAP Incompletion Procedure Diagnostics</a> — Diagnostic context for incompletion breakpoints in sales processes.</li>
      <li><a href="/atlas/ai-operations/ai-ready-process-documentation/">AI-Ready Process Documentation</a> — Guidance on structuring process documentation for AI consumption.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of process documentation practices. It is not official BPMN, SAP, or ITIL documentation. It focuses on capturing actual processes in enterprise and SAP environments where tribal knowledge is common and process drift is frequent.</p>
    <p>Known limitations: the skill does not cover BPMN modeling, flowchart creation, or formal process mining. It produces text-based process documents suitable for wikis and knowledge bases. It assumes access to a process owner who can describe the actual process. It does not replace formal process audit or process redesign activities; it documents the current state as input for those activities.</p>
  </section>
</article>
