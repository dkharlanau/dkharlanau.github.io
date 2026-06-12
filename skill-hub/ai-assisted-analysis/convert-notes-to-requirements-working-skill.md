---
layout: default
title: "Convert Notes to Requirements Working Skill"
description: "Turn raw meeting notes, interview transcripts, and ticket comments into structured requirements without losing the nuance that matters."
permalink: /skill-hub/ai-assisted-analysis/convert-notes-to-requirements-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/ai-assisted-analysis/">AI-Assisted Analysis</a></li>
    <li aria-current="page">Convert Notes to Requirements</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — AI-Assisted Analysis</p>
  <h1>Convert Notes to Requirements</h1>
  <p class="lead">Turn raw meeting notes, interview transcripts, and ticket comments into structured requirements without losing the nuance that matters.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Raw notes are full of ambiguity: conflicting statements, unclear ownership, opinions mixed with facts, and solutions masquerading as needs. This skill uses AI to classify, structure, and trace note content into a requirements brief where every item has a source, a type, and an owner. The goal is not to replace the analyst but to accelerate the tedious parts while preserving the nuance that determines project success.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>After a stakeholder workshop where multiple people gave conflicting descriptions of the same process.</li>
      <li>When you have pages of interview transcripts and need to extract structured needs quickly.</li>
      <li>When reviewing a long support ticket thread to find the actual problem beneath the proposed fixes.</li>
      <li>When consolidating workshop notes into a format that can be reviewed by stakeholders who did not attend.</li>
      <li>When AI summarization has flattened important detail and you need to recover it.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Workshop notes contain conflicting ownership claims</h3>
    <p>A workshop on SAP vendor master governance produces notes where the procurement lead says "we own the vendor create process," the finance lead says "we approve payment terms," and the MDG team says "we gate all changes." An AI that simply summarizes this as "vendor master has multiple owners" loses the critical detail that each team owns a different stage. The structured output must preserve the stage-level ownership so the governance design can assign rights correctly.</p>
    <h3>Support ticket thread mixes symptoms with solutions</h3>
    <p>A ticket thread about billing blocks contains 23 comments. Some users propose workarounds, others describe symptoms, and one comment reveals a recent configuration change. A simple summary might say "billing blocks are causing delays." The structured requirements output must classify the configuration change as a potential root cause, the workarounds as temporary solutions, and the symptoms as evidence for a diagnostic requirement.</p>
    <h3>Interview transcript buries needs under complaints</h3>
    <p>A 45-minute interview with a warehouse manager contains complaints about the goods receipt process, the RF device, and the integration with WMS. Buried in the complaints is a real need: real-time visibility of inbound shipments before the truck arrives. A generic summary loses this because the word "need" never appears in the transcript. The structured output must extract the underlying need and separate it from the surrounding complaints.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li><strong>Raw notes or transcripts</strong> — the source material, unedited.</li>
      <li><strong>Attendee or commenter list</strong> — who said what, if identifiable.</li>
      <li><strong>System context</strong> — which SAP modules, processes, or integrations are in scope.</li>
      <li><strong>Existing requirements</strong> — if a baseline exists (optional).</li>
      <li><strong>Stakeholder roles</strong> — to identify decision-makers versus observers.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Who said this — a decision-maker, an observer, or someone repeating hearsay?</li>
      <li>Is this statement a need, a solution, an assumption, a risk, or a complaint?</li>
      <li>What business rule or process step is being referenced?</li>
      <li>Which SAP system touchpoints are mentioned, and are they accurate?</li>
      <li>Does this statement conflict with another statement in the same notes?</li>
      <li>What is the underlying need if this is only a complaint or a solution?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Collect raw notes.</strong> Gather all source material: transcripts, tickets, handwritten notes, whiteboard photos. Do not paraphrase before analysis.</li>
      <li><strong>Identify and tag speakers.</strong> If the source identifies who made each statement, tag each paragraph with the speaker. If not, flag unattributed statements for follow-up.</li>
      <li><strong>Classify each statement.</strong> Use AI to label each significant statement as: Need, Solution, Assumption, Risk, Fact, Complaint, or Unknown.</li>
      <li><strong>Extract needs.</strong> From every statement classified as Need or Complaint, derive the underlying need. For Complaints, ask "what would have to be true for this complaint to go away?"</li>
      <li><strong>Separate solutions from needs.</strong> For every Solution statement, capture the solution but also derive the need it serves. If the need is unclear, flag it as an open question.</li>
      <li><strong>Capture assumptions and risks.</strong> Collect every Assumption and Risk into a register. Link them to the needs they affect.</li>
      <li><strong>Structure requirements.</strong> Rewrite each extracted need as a requirement in the format: "The system must [capability] so that [business outcome]." Include the source statement ID.</li>
      <li><strong>Add traceability.</strong> For every requirement, record the source note, the speaker, and the classification. For conflicts, record both sides and flag for resolution.</li>
      <li><strong>Produce the brief.</strong> Assemble the requirements, assumptions, risks, conflicts, and open questions into a single document.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If two stakeholders conflict, document both positions and flag for a decision session; do not let the AI pick a winner.</li>
      <li>If a statement describes a solution, always derive the underlying need; if the need cannot be derived, discard the solution.</li>
      <li>If a need has no owner, add it to the open questions list and assign a stakeholder to find the owner.</li>
      <li>If a statement is unattributed, flag it as "source unknown" and do not use it as the sole basis for a requirement.</li>
      <li>If a complaint contains no actionable need, log it as context but do not create a requirement.</li>
      <li>If the AI misclassifies a statement, correct it manually and note the correction.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Structured Requirements Brief</strong> — needs rewritten as requirements with traceability.</li>
      <li><strong>Source Traceability Matrix</strong> — links each requirement to the original note, speaker, and classification.</li>
      <li><strong>Assumption and Risk Register</strong> — extracted assumptions and risks linked to requirements.</li>
      <li><strong>Conflict Log</strong> — documented stakeholder conflicts awaiting resolution.</li>
      <li><strong>Open Questions List</strong> — missing owners, unclear needs, or unknown sources.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Structured Requirements Brief</h3>
    <pre><code>---
title: Structured Requirements Brief
source: [workshop notes / interview transcripts / ticket thread]
project: [project name]
analyst: [name]
date: [YYYY-MM-DD]
---

## Requirement N-001
- **Statement**: The system must [capability] so that [business outcome].
- **Source**: [Note ID, Speaker, Original quote]
- **Classification**: [Need / Derived from Complaint / Derived from Solution]
- **Stakeholder**: [owner]
- **Assumption**: [what must be true]
- **Risk**: [what could go wrong]
- **Status**: [Draft / Awaiting Review / Conflicted]

## Conflict Log
| # | Stakeholder A | Position | Stakeholder B | Position | Resolution Needed From |
|---|---------------|----------|---------------|----------|----------------------|
| 1 | [name] | [position] | [name] | [position] | [decision maker] |

## Open Questions
| # | Question | Blocks | Assigned To |
|---|----------|--------|-------------|
| 1 | [question] | [requirement IDs] | [stakeholder] |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>[ ] Every requirement traces back to a specific source note or transcript segment.</li>
      <li>[ ] Speaker attribution is present for every requirement derived from a workshop or interview.</li>
      <li>[ ] Every conflict is documented, not resolved silently by the AI or analyst.</li>
      <li>[ ] Every solution statement has a derived need; orphaned solutions are removed.</li>
      <li>[ ] The assumption register links assumptions to the requirements they affect.</li>
      <li>[ ] The open questions list is non-empty if any source material was ambiguous.</li>
      <li>[ ] A stakeholder who attended the source session can read the brief and recognize their input.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Letting the AI resolve stakeholder conflicts by choosing the majority view. <strong>Consequence:</strong> A minority stakeholder who controls the data or process is sidelined, and the requirements fail at the approval gate.</li>
      <li><strong>Mistake:</strong> Losing nuance in AI summarization. <strong>Consequence:</strong> A critical distinction — such as stage-level ownership versus process-level ownership — is flattened, and the governance design assigns the wrong rights.</li>
      <li><strong>Mistake:</strong> Merging facts with opinions. <strong>Consequence:</strong> A stakeholder's opinion about the root cause is treated as a verified fact, and the requirement targets the wrong problem.</li>
      <li><strong>Mistake:</strong> Treating every complaint as a requirement. <strong>Consequence:</strong> The requirements document bloats with low-value items that do not address root causes.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>
    <h3>Weak output — bad AI usage</h3>
    <p>A consultant feeds workshop notes into an AI and asks for a summary. The AI produces a generic list of "requirements" that merges the procurement lead's ownership claim with the finance lead's approval role into a single vague statement: "Vendor master needs better governance." The AI loses the fact that the MDG team gates changes but does not own data quality. The resulting brief is useless for governance design because the stage boundaries are gone. When stakeholders review it, they say "this is not what we discussed" and the workshop must be repeated.</p>
    <h3>Strong output — good AI usage</h3>
    <p>The consultant uses AI to classify every paragraph of the workshop notes. Requirement N-004 is derived from the procurement lead's statement and explicitly covers the create process. Requirement N-005 is derived from the finance lead and covers payment term approval. The conflict log flags that the MDG team's role is described as both "gatekeeper" and "data quality owner" by different speakers, and the open questions list assigns the procurement lead to clarify the boundary. The brief is reviewed and approved in one session because every stakeholder sees their input preserved and the conflicts honestly surfaced.</p>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <h3>AI Prompt Pattern</h3>
    <pre><code>Role: You are a note-to-requirements analyst.
Context: I have raw notes from a [workshop / interview / ticket thread] about [SAP process / business area].
Tasks:
1. Tag each significant statement with the speaker if known.
2. Classify each statement as: Need, Solution, Assumption, Risk, Fact, Complaint, or Unknown.
3. Extract the underlying need from every Complaint and Solution.
4. Rewrite each need as a requirement with the format: "The system must [capability] so that [business outcome]."
5. Document conflicts, assumptions, and open questions.
6. Output a Structured Requirements Brief using the provided template.
Constraints: Do not resolve conflicts. Do not drop speaker attribution. Do not invent needs that are not in the source material. Flag anything that is unclear.</code></pre>
    <h3>Agent dos</h3>
    <ul>
      <li>Preserve the exact words of stakeholders when they describe needs or constraints.</li>
      <li>Classify every significant statement before extracting requirements.</li>
      <li>Flag conflicts and leave them for human stakeholders to resolve.</li>
      <li>Produce the traceability matrix as a separate artifact, not as an afterthought.</li>
    </ul>
    <h3>Agent don'ts</h3>
    <ul>
      <li>Do not let AI summarization flatten nuance into generic statements.</li>
      <li>Do not merge conflicting stakeholder positions into a single compromise requirement.</li>
      <li>Do not invent requirements that are not supported by the source notes.</li>
      <li>Do not present opinions as facts.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/business-analysis/requirements-elicitation-working-skill/">Requirements Elicitation</a> — capturing stakeholder needs directly.</li>
      <li><a href="/skill-hub/business-analysis/stakeholder-analysis-working-skill/">Stakeholder Analysis</a> — identifying who to interview and who owns what.</li>
      <li><a href="/skill-hub/business-analysis/process-analysis-working-skill/">Process Analysis</a> — mapping how work happens before extracting requirements.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-process-audit/">SAP Process Audit</a> — structured frame for understanding process context before requirement extraction.</li>
      <li><a href="/scenarios/master-data-issues-blocking-sales-orders/">Master Data Issues Blocking Sales Orders</a> — example of how raw symptoms map to structured diagnostic needs.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of AI-assisted note conversion. It is not an official BABOK, SAP, or vendor method. AI classification accuracy depends on the model and the quality of the source notes; ambiguous or unstructured notes will produce more "Unknown" classifications. The skill does not replace stakeholder validation: the brief must always be reviewed by the people who provided the original input. Use it as a structured accelerator, not as a substitute for human judgment.</p>
  </section>
</article>
