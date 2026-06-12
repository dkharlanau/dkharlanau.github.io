---
layout: default
title: "AI-Assisted Meeting Synthesis Working Skill"
description: "Turn raw meeting transcripts or notes into a structured synthesis of decisions, actions, and risks with AI assistance and human review."
permalink: /skill-hub/ai-assisted-analysis/ai-assisted-meeting-synthesis-working-skill/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/ai-assisted-analysis/">AI-Assisted Analysis</a></li>
    <li aria-current="page">AI-Assisted Meeting Synthesis</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — AI-Assisted Analysis</p>
  <h1>AI-Assisted Meeting Synthesis</h1>
  <p class="lead">Turn raw meeting transcripts or notes into a structured synthesis of decisions, actions, and risks with AI assistance and human review.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>Meetings produce long transcripts, scattered notes, and informal chat threads that are hard to convert into actionable records. AI can extract structure from this raw material, but it often misattributes statements, invents actions that were never agreed, and misses the risks that were raised in passing. This skill provides a workflow where AI drafts the synthesis and a human verifies the decisions, actions, and risks before the record is distributed. The output is a Meeting Synthesis that separates verified facts from draft material, with every action item assigned to an owner and every risk linked to a mitigation or escalation path.</p>
  </section>

  <section>
    <h2>When to use this skill</h2>
    <ul>
      <li>A long workshop or meeting has produced a transcript or pages of notes that need to be turned into a structured record.</li>
      <li>A meeting included multiple stakeholders, overlapping conversations, and side discussions that make manual summarization slow.</li>
      <li>The team needs to extract decisions, actions, and risks from a meeting where no formal minutes were taken.</li>
      <li>A recurring meeting produces similar notes each week and the team wants to automate the structural extraction while keeping human verification.</li>
      <li>A critical meeting such as an escalation or design review requires a precise record that will be referenced in future decisions.</li>
      <li>Meeting notes are in an informal format and must be converted into a standard action log or decision summary.</li>
    </ul>
  </section>

  <section>
    <h2>Real work situations</h2>
    <h3>Two-hour workshop on SAP BP replication has ten pages of notes</h3>
    <p>A cross-functional workshop covers business partner replication from SAP MDG to SAP S/4HANA. The notes are ten pages of bullet points, diagrams, and chat comments. AI synthesizes the notes into a structured record. The human reviewer discovers that the AI attributed a decision to the MDG architect that was actually made by the integration lead, missed a risk about duplicate number ranges that was mentioned in a side comment, and invented an action item to "update the mapping document" that no one agreed to. The reviewer corrects the attribution, adds the risk, and removes the invented action before sending the synthesis.</p>
    <h3>Status meeting has decisions but no action owners</h3>
    <p>A weekly project status meeting produces a transcript where decisions are made but no one explicitly volunteers to own the follow-up. AI extracts five decisions but only assigns owners to three of them. The human reviewer listens to the relevant segments of the transcript and identifies that the data migration lead agreed to handle the staging table cleanup, and the test manager agreed to reschedule the UAT start date. The reviewer adds both owners and deadlines, converting vague decisions into executable actions.</p>
    <h3>Escalation meeting has risks but no mitigation owners</h3>
    <p>A steering committee escalation meeting discusses a three-week delay in the SAP Fiori rollout. The transcript contains three risks: missing app library permissions, unplanned device compatibility issues, and trainer unavailability. AI notes the risks but does not link them to mitigations or owners. The human reviewer adds the mitigation actions from the discussion, assigns the app library issue to the security lead, the compatibility issue to the mobile team, and the trainer issue to the HR project partner. The synthesis becomes a working risk register instead of a static list.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li><strong>Meeting transcript or raw notes</strong> — the full text, audio transcript, or notes document from the meeting.</li>
      <li><strong>Attendee list with roles</strong> — to verify attributions and identify who can own actions.</li>
      <li><strong>Meeting agenda</strong> — to check that all topics were covered and to structure the synthesis.</li>
      <li><strong>Previous action log or decision register</strong> — to check for follow-ups and status updates (optional).</li>
      <li><strong>Organizational context</strong> — who has authority to decide, escalate, or approve, so action assignments are realistic.</li>
      <li><strong>Intended output format</strong> — action log, decision summary, risk register, or a combined synthesis.</li>
    </ul>
  </section>

  <section>
    <h2>Questions to ask</h2>
    <ul>
      <li>Which decisions were made, and who has the authority to confirm them?</li>
      <li>Which actions were agreed, and who explicitly accepted ownership?</li>
      <li>Which risks were raised, and what mitigation or escalation was discussed?</li>
      <li>Which topics were discussed but not decided, and do they need a follow-up meeting?</li>
      <li>Does the AI correctly attribute statements and decisions to the right people?</li>
      <li>Did the AI invent any action, decision, or risk that was not in the source material?</li>
      <li>What is missing from the AI synthesis that a human who attended the meeting would expect to see?</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Capture the source material.</strong> Save the transcript, notes, or chat thread as the original record. Note the meeting date, attendees, and any absent stakeholders.</li>
      <li><strong>Define the synthesis scope.</strong> Decide what the output must contain: decisions, actions, risks, open questions, or all of the above.</li>
      <li><strong>Run the AI synthesis.</strong> Prompt the AI to extract decisions, actions, and risks from the source material, using the attendee list and agenda as context.</li>
      <li><strong>Capture the AI draft.</strong> Save the AI output as a draft synthesis. Do not distribute it yet.</li>
      <li><strong>Verify attributions.</strong> Check that every statement attributed to a person was actually said by that person. Correct misattributions.</li>
      <li><strong>Verify decisions.</strong> Confirm that each recorded decision was actually made and that the decision maker is correctly named. Flag tentative agreements as provisional.</li>
      <li><strong>Verify actions.</strong> Confirm that each action item was agreed to and that the owner is correct and realistic. Add missing owners and deadlines.</li>
      <li><strong>Verify risks.</strong> Confirm that each risk was raised in the meeting and that the mitigation or escalation path is correctly recorded. Add missing risks.</li>
      <li><strong>Check for inventions.</strong> Read the AI draft against the source material. Remove any decision, action, or risk that the AI invented.</li>
      <li><strong>Produce the final synthesis.</strong> Output the verified Meeting Synthesis with clear labels for decisions, actions, and risks, and distribute it to attendees for confirmation.</li>
    </ol>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the AI misattributes a statement, correct the attribution and log the error so the prompt can be improved.</li>
      <li>If the AI invents an action, decision, or risk, remove it and do not try to justify it.</li>
      <li>If an action has no owner, assign one based on role and authority, or flag it as unassigned pending clarification.</li>
      <li>If a decision is tentative or conditional, label it as provisional and note the condition that must be met.</li>
      <li>If a risk has no mitigation or escalation path, add one based on the discussion or flag it as open.</li>
      <li>If the AI omits a topic from the agenda, add it to the synthesis as an unaddressed item.</li>
      <li>If the synthesis is for a client or steering committee, apply a stricter verification standard than for internal team notes.</li>
    </ul>
  </section>

  <section>
    <h2>Deliverables</h2>
    <ul>
      <li><strong>Meeting Synthesis</strong> — a structured document with verified decisions, actions, and risks.</li>
      <li><strong>Action Log</strong> — a concise list of actions with owners, deadlines, and dependencies.</li>
      <li><strong>Risk Register</strong> — risks raised in the meeting with mitigation or escalation paths.</li>
      <li><strong>AI Correction Log</strong> — a record of AI misattributions, inventions, and omissions for prompt improvement.</li>
    </ul>
  </section>

  <section>
    <h2>Templates</h2>
    <h3>Meeting Synthesis</h3>
    <pre><code>---
meeting: [meeting name]
date: [YYYY-MM-DD]
attendees: [list]
absent: [list]
synthesizer: [AI tool + human reviewer]
---

## Decisions
| # | Decision | Decision Maker | Status | Condition |
|---|----------|----------------|--------|-----------|
| 1 | [what was decided] | [name] | [Confirmed / Provisional] | [if provisional, what must happen] |

## Actions
| # | Action | Owner | Deadline | Dependency | Status |
|---|--------|-------|----------|------------|--------|
| 1 | [what must be done] | [name] | [YYYY-MM-DD] | [none / action #] | [Open / In Progress] |

## Risks
| # | Risk | Mitigation / Escalation | Owner | Meeting Context |
|---|------|-------------------------|-------|-----------------|
| 1 | [risk] | [what was discussed] | [name] | [when it was raised] |

## Unaddressed Topics
| # | Topic | From Agenda | Follow-Up Plan |
|---|-------|-------------|----------------|
| 1 | [topic] | [Yes / No] | [next meeting / email / owner] |

## AI Correction Log
| # | AI Error | Human Correction | Lesson for Prompt |
|---|----------|------------------|-------------------|
| 1 | [description] | [fix] | [how to avoid] |
</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>[ ] Every decision is attributed to a person who has the authority to make it.</li>
      <li>[ ] Every action has a named owner and a realistic deadline.</li>
      <li>[ ] Every risk has a mitigation, escalation path, or an explicit note that none was discussed.</li>
      <li>[ ] No decision, action, or risk was invented by the AI and not present in the source material.</li>
      <li>[ ] The AI correction log contains at least one entry or a note that no corrections were needed.</li>
      <li>[ ] The synthesis can be read by someone who did not attend the meeting and still understand what happened.</li>
      <li>[ ] Attendees have been given a chance to confirm or correct the synthesis before it is finalized.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Mistake:</strong> Distributing the AI synthesis without human verification. <strong>Consequence:</strong> A misattributed decision creates a conflict between stakeholders, or an invented action item is assigned to someone who never agreed to it.</li>
      <li><strong>Mistake:</strong> Trusting the AI to assign owners based on role alone. <strong>Consequence:</strong> The AI assigns a complex technical action to a business analyst who lacks the system access or expertise to complete it.</li>
      <li><strong>Mistake:</strong> Accepting a vague AI summary that omits the specific risks raised in side conversations. <strong>Consequence:</strong> A critical risk is buried in the transcript and never reaches the risk register or the steering committee.</li>
      <li><strong>Mistake:</strong> Not logging AI errors, so the same misattribution and invention patterns repeat every meeting. <strong>Consequence:</strong> The team spends more time correcting AI drafts than they would have spent writing minutes manually.</li>
    </ul>
  </section>

  <section>
    <h2>Weak output vs Strong output</h2>
    <h3>Weak output — bad AI usage</h3>
    <p>A project manager runs an AI synthesis on a two-hour workshop transcript and receives a one-page summary: "The team discussed BP replication, agreed to proceed with the standard approach, and identified some risks. Action items were noted." The summary is distributed to the team. No one knows what the standard approach is, which risks were identified, who owns the action items, or when they are due. Two weeks later, the same risks appear in a status report as new issues, and an action item that was never actually agreed to is raised as a blocker because the assigned owner never accepted it. The vague synthesis created more confusion than clarity.</p>
    <h3>Strong output — good AI usage</h3>
    <pre><code>## Meeting Synthesis — BP Replication Workshop

### Decisions
| # | Decision | Decision Maker | Status |
|---|----------|----------------|--------|
| 1 | Use MDG-S central governance for BP creation; S/4HANA systems receive replication | MDG Architect | Confirmed |
| 2 | Defer vendor replication scope to Phase 2 | Integration Lead | Provisional — pending budget check by 2026-06-20 |

### Actions
| # | Action | Owner | Deadline |
|---|--------|-------|----------|
| 1 | Update CVI mapping document for customer classification | Integration Lead | 2026-06-15 |
| 2 | Verify number range consistency across target systems | MDG Architect | 2026-06-14 |
| 3 | Schedule Phase 2 vendor scoping session | Project Manager | 2026-06-18 |

### Risks
| # | Risk | Mitigation | Owner |
|---|------|------------|-------|
| 1 | Duplicate number ranges in S/4HANA systems | Run BDLS reconciliation before go-live | MDG Architect |

### AI Correction Log
| # | AI Error | Correction |
|---|----------|------------|
| 1 | AI attributed decision 2 to MDG Architect | Corrected to Integration Lead per transcript segment 00:47:12 |
| 2 | AI invented action "update mapping document" without owner | Confirmed owner is Integration Lead; added deadline |</code></pre>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <h3>AI Prompt Pattern</h3>
    <pre><code>Role: You are a meeting synthesis assistant.
Context: I have a transcript and notes from a meeting about [topic]. There were [number] attendees: [list with roles]. The agenda was: [agenda items]. I need a structured synthesis.
Tasks:
1. Extract every decision made, who made it, and whether it was final or provisional.
2. Extract every action item agreed, who owns it, and any deadline mentioned.
3. Extract every risk raised and any mitigation or escalation discussed.
4. Identify which agenda items were not addressed or were deferred.
5. Do not invent decisions, actions, or risks. If something is unclear, flag it as unclear rather than guessing.
6. Use the attendee list to attribute statements correctly. Do not guess attributions.
Constraints: Output in a structured table format. Do not summarize into vague language. If no actions were agreed for a topic, state "no actions agreed" rather than omitting the topic. If a deadline was not mentioned, leave the deadline blank rather than inventing one.</code></pre>
    <h3>Agent dos</h3>
    <ul>
      <li>Ask for the attendee list, agenda, and previous action log before running the synthesis.</li>
      <li>Verify every attribution, decision, and action against the source material before finalizing.</li>
      <li>Log AI inventions and misattributions so the prompt can be improved for the next meeting.</li>
      <li>Give attendees a window to confirm the synthesis before treating it as the official record.</li>
    </ul>
    <h3>Agent don'ts</h3>
    <ul>
      <li>Do not distribute the AI draft without human verification.</li>
      <li>Do not assign action owners based on role alone; verify that the person agreed to the action.</li>
      <li>Do not omit risks because they were mentioned in a side conversation or a chat thread.</li>
      <li>Do not accept vague summaries that lack specific decisions, owners, and deadlines.</li>
    </ul>
  </section>

  <section>
    <h2>Related skills</h2>
    <ul>
      <li><a href="/skill-hub/ai-assisted-analysis/ai-output-review-working-skill/">AI Output Review</a> — general review workflow for any AI-generated output.</li>
      <li><a href="/skill-hub/ai-assisted-analysis/ai-assisted-status-reporting-working-skill/">AI-Assisted Status Reporting</a> — synthesizing project status from multiple sources, including meeting outcomes.</li>
      <li><a href="/skill-hub/ai-assisted-analysis/business-problem-to-backlog-working-skill/">Business Problem to Backlog</a> — turning meeting risks and decisions into executable analysis tasks.</li>
      <li><a href="/skill-hub/work-documentation-handover/">Work Documentation and Handover</a> — the broader skill group for action logs, decision summaries, and handover notes.</li>
    </ul>
  </section>

  <section>
    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/automation/operational-memory-for-sap-ams/">Operational Memory for SAP AMS</a> — turning meeting outcomes into reusable operational knowledge.</li>
      <li><a href="/atlas/ai-operations/ai-ready-process-documentation/">AI-Ready Process Documentation</a> — structuring documentation so AI can synthesize it accurately.</li>
    </ul>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This skill is a public working interpretation of AI-assisted meeting synthesis. It is not official meeting management, project management, or governance framework documentation. The accuracy of AI synthesis depends on the quality of the transcript or notes, the clarity of the attendee list, and the specificity of the prompt. AI tools may misattribute statements, especially in meetings with overlapping speakers or informal chat threads. The human verification step is mandatory and cannot be automated away. Use this skill as a structured starting point, not as a replacement for human judgment or formal meeting minutes.</p>
  </section>
</article>
