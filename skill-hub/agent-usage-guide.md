---
layout: default
title: "Agent Usage Guide — How AI Agents Should Use Skill Hub"
description: "Instructions for AI agents on how to use Skill Hub: choose skills, combine them, ask for missing context, separate facts from assumptions, produce artifacts, and avoid generic framework summaries."
permalink: /skill-hub/agent-usage-guide/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li aria-current="page">Agent Usage Guide</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Foundation</p>
  <h1>Agent Usage Guide</h1>
  <p class="lead">How AI agents should use Skill Hub to produce useful operational output instead of generic explanations.</p>

  <section>
    <h2>How to choose a skill</h2>
    <ol>
      <li><strong>Identify the work situation</strong>, not the topic. "Data quality problem" is a topic. "Sales orders blocked by missing tax data" is a work situation.</li>
      <li><strong>Match the situation to a skill group</strong> using the Skill Hub index. Data problems map to DAMA/Data skills. Interface problems map to Integration Architecture skills. Stakeholder confusion maps to Business Analysis skills.</li>
      <li><strong>Open the skill page</strong> and read "When to use this skill" and "Real work situations." If the situation matches, use the skill. If not, look at "Related skills."</li>
      <li><strong>If no skill matches exactly</strong>, combine the closest skill with general consulting judgment. Do not default to generic explanation.</li>
    </ol>
  </section>

  <section>
    <h2>How to combine multiple skills</h2>
    <p>Real enterprise problems span multiple domains. A single incident may require:</p>
    <ul>
      <li><strong>Incident Triage</strong> to classify and contain.</li>
      <li><strong>Root Cause Analysis</strong> to find the cause.</li>
      <li><strong>Stakeholder Analysis</strong> to identify who needs to approve the fix.</li>
      <li><strong>Change Impact Analysis</strong> to assess what else breaks if you change the fix.</li>
      <li><strong>Operational Knowledge Capture</strong> to record the pattern for next time.</li>
    </ul>
    <p>When combining skills:</p>
    <ol>
      <li>Run each skill in sequence. Do not merge steps from different skills into a single unordered list.</li>
      <li>Pass the output of one skill as input to the next. For example, the defect classification from Incident Triage feeds into the root cause hypothesis in Root Cause Analysis.</li>
      <li>Label which skill produced which part of the output.</li>
      <li>Flag gaps where a skill does not cover the situation.</li>
    </ol>
  </section>

  <section>
    <h2>How to ask for missing context</h2>
    <p>Agents must not guess. If the user provides an incomplete situation, ask structured questions:</p>
    <ul>
      <li>What system or module is involved? (SAP module, middleware, database, API)</li>
      <li>What is the business process? (order-to-cash, procure-to-pay, record-to-report)</li>
      <li>What is the symptom? (error message, blocked transaction, wrong data, missing data)</li>
      <li>What is the scale? (one record, one customer, one region, all records)</li>
      <li>What has already been tried? (reprocessing, manual correction, config change)</li>
      <li>Who owns the affected data or process?</li>
      <li>Is there a deadline or regulatory constraint?</li>
    </ul>
    <p>Do not proceed with advice until you have enough context to choose a skill and follow its working method.</p>
  </section>

  <section>
    <h2>How to separate facts, assumptions, risks, decisions, and open questions</h2>
    <p>Every agent output must use these labels explicitly:</p>
    <table>
      <thead>
        <tr>
          <th>Label</th>
          <th>Meaning</th>
          <th>Example</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Fact</strong></td>
          <td>Confirmed, observable, verifiable</td>
          <td>"IDoc 12345 failed with status 51 in WE02."</td>
        </tr>
        <tr>
          <td><strong>Assumption</strong></td>
          <td>Believed true but not yet verified</td>
          <td>"Assumed: the partner function was missing because of a recent org change."</td>
        </tr>
        <tr>
          <td><strong>Risk</strong></td>
          <td>Something that may go wrong if the assumption is wrong</td>
          <td>"Risk: if the org change also affected payment terms, invoices may block."</td>
        </tr>
        <tr>
          <td><strong>Decision</strong></td>
          <td>A choice that must be made, with options</td>
          <td>"Decision: correct the 47 affected records manually or via mass update?"</td>
        </tr>
        <tr>
          <td><strong>Open question</strong></td>
          <td>Unknown that blocks progress</td>
          <td>"Open: who approved the org change and was MDG workflow triggered?"</td>
        </tr>
      </tbody>
    </table>
    <p>Never present an assumption as a fact. Never present a risk as a certainty. Never skip open questions.</p>
  </section>

  <section>
    <h2>How to produce artifacts instead of generic explanations</h2>
    <p>An artifact is a structured, reusable output that a human can act on. Examples:</p>
    <ul>
      <li>A <strong>Root Cause Analysis Note</strong> with defect, cause, impact, correction, and prevention.</li>
      <li>A <strong>Stakeholder Interview Brief</strong> with questions, answers, assumptions, and follow-ups.</li>
      <li>An <strong>Architecture Decision Record</strong> with context, options, decision, and consequences.</li>
      <li>A <strong>Data Quality Rule</strong> with field, condition, owner, and enforcement mechanism.</li>
    </ul>
    <p>Rules for artifact production:</p>
    <ol>
      <li>Use the template from the skill page or the <a href="/skill-hub/artifact-templates/">Artifact Templates</a> page.</li>
      <li>Fill every field. If a field is unknown, label it "Unknown — needs input from [owner]."</li>
      <li>Include dates, owners, and next actions.</li>
      <li>Format the artifact so it can be pasted into a ticket, document, or wiki without rewriting.</li>
      <li>Do not summarize the artifact in prose afterward. The artifact is the output.</li>
    </ol>
  </section>

  <section>
    <h2>How to link Skill Hub with Atlas diagnostics</h2>
    <p>Atlas contains SAP-specific diagnostics. Skill Hub contains cross-domain working skills. Use them together:</p>
    <ul>
      <li>When a user describes a SAP symptom, first consult Atlas diagnostics to understand the technical cause.</li>
      <li>Then use Skill Hub skills to structure the response: stakeholder communication, change impact, knowledge capture, decision record.</li>
      <li>Link Atlas pages in the "Related Atlas pages" section of the skill output.</li>
      <li>Do not duplicate Atlas diagnostic content in Skill Hub skill output.</li>
    </ul>
  </section>

  <section>
    <h2>How to avoid fake certainty</h2>
    <p>Agents must not sound confident about things they cannot verify:</p>
    <ul>
      <li>Use "appears to be" or "based on the information provided" when inferring from limited data.</li>
      <li>State confidence levels: high, medium, low, unknown.</li>
      <li>Flag when a conclusion depends on an unverified assumption.</li>
      <li>Do not invent system behavior. If you do not know how a specific SAP transaction works in this version, say so.</li>
      <li>Do not invent client names, project details, or internal paths.</li>
    </ul>
  </section>

  <section>
    <h2>How to avoid generic framework summaries</h2>
    <p>Never output text like:</p>
    <ul>
      <li>"Data governance is important because..."</li>
      <li>"Event-driven architecture provides loose coupling..."</li>
      <li>"Requirements elicitation is the process of..."</li>
    </ul>
    <p>Instead, output:</p>
    <ul>
      <li>"Here is the ownership matrix for the 6 data domains in scope. Gaps are flagged in red."</li>
      <li>"Here are the 4 events this process should produce, with owners, schemas, and failure modes."</li>
      <li>"Here are the 7 requirements extracted from the stakeholder interview, with assumptions and risks."</li>
    </ul>
  </section>

  <section>
    <h2>How to create useful project outputs</h2>
    <p>When a user asks for help with a project, deliver:</p>
    <ol>
      <li><strong>Situation summary</strong> — what is known, what is assumed, what is missing.</li>
      <li><strong>Skill selection</strong> — which Skill Hub skills apply and why.</li>
      <li><strong>Working method execution</strong> — follow the skill steps, produce artifacts.</li>
      <li><strong>Deliverables</strong> — the actual artifacts, not a description of them.</li>
      <li><strong>Quality checklist</strong> — did we cover all required fields? Are there gaps?</li>
      <li><strong>Next actions</strong> — who does what by when, with owners.</li>
    </ol>
  </section>

  <section>
    <h2>Agent instruction summary</h2>
    <ul>
      <li>Choose skills based on work situations, not topics.</li>
      <li>Ask for missing context before giving advice.</li>
      <li>Separate facts, assumptions, risks, decisions, and open questions.</li>
      <li>Produce artifacts using templates. Do not stop at explanation.</li>
      <li>Link to Atlas diagnostics when the situation is SAP-specific.</li>
      <li>Avoid fake certainty and generic framework language.</li>
      <li>Label confidence levels and flag unverified assumptions.</li>
      <li>End with deliverables, quality check, and next actions.</li>
    </ul>
  </section>
</article>
