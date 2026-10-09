---
layout: default
title: "Agent Usage Guide — How AI Agents Should Use Skill Hub"
description: "Instructions for AI agents on how to use Skill Hub: choose skills, combine them, ask for missing context, separate facts from assumptions, produce artifacts, and avoid generic framework summaries."
permalink: /skill-hub/agent-usage-guide/
last_modified_at: 2026-10-08
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
  <p class="lead">Start with a work situation, choose a matching skill, and produce a record someone can review and act on. Use this guide to move from an incomplete request to a usable handoff.</p>

  <section>
    <h2>Establish the situation before choosing a skill</h2>
    <p>“Data quality problem” is too broad. “Sales orders blocked by missing tax data” gives you a symptom and a process to investigate. Ask for the missing context:</p>
    <ul>
      <li><strong>System and process:</strong> which SAP module, middleware, database, or API is involved, and which business process is affected?</li>
      <li><strong>Symptom and scope:</strong> what failed, and does it affect one record, customer, region, or all records?</li>
      <li><strong>Previous checks:</strong> what has already been tried (for example, reprocessing, manual correction, or a configuration change), and what was the result?</li>
      <li><strong>Ownership and constraints:</strong> who owns the data or process, and is there a deadline or regulatory constraint?</li>
    </ul>
    <p>Wait until you have enough context to choose a skill and follow its method before giving advice. Record the gaps; do not fill them with guesses.</p>
  </section>

  <section>
    <h2>Choose the method and its output</h2>
    <ol>
      <li>Use the <a href="/skill-hub/">Skill Hub index</a> to find a matching group: DAMA/Data for data problems, Integration Architecture for interfaces, or Business Analysis for unclear stakeholder needs.</li>
      <li>Check the skill page’s “When to use this skill” and “Real work situations.” If they do not fit, follow its related skills. If the closest skill covers only part of the problem, name that gap rather than treating it as a complete method.</li>
      <li>Choose the output before starting: a root cause analysis (RCA) note for cause and prevention, an interview brief for stakeholder questions, an architecture decision record for options and consequences, or a data quality rule for field, condition, owner, and enforcement.</li>
    </ol>
    <p>For a SAP symptom, consult Atlas diagnostics for the technical checks, then use Skill Hub to structure the decision, communication, or handoff. Link the relevant Atlas pages in the output instead of copying their diagnostic content. A reference page does not confirm the cause of this incident.</p>
  </section>

  <section>
    <h2>Pass evidence between skills</h2>
    <p>An incident may need several methods in sequence:</p>
    <ol>
      <li><strong>Incident Triage:</strong> classify and contain the incident.</li>
      <li><strong>Root Cause Analysis:</strong> use the triage findings to test a cause hypothesis.</li>
      <li><strong>Stakeholder Analysis:</strong> identify who needs to approve the fix.</li>
      <li><strong>Change Impact Analysis:</strong> check what else the proposed fix could affect.</li>
      <li><strong>Operational Knowledge Capture:</strong> record the pattern for reuse.</li>
    </ol>
    <p>Follow each skill’s steps in order. Pass its output to the next skill, label which skill produced each part, and flag any remaining gaps. Do not flatten the methods into one unordered checklist.</p>
  </section>

  <section>
    <h2>Keep conclusions separate from evidence</h2>
    <p>Use explicit labels in the output. The examples below illustrate the labels; they are not records of a real incident.</p>
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
    <p>State confidence as high, medium, low, or unknown, and identify any unverified assumption behind the conclusion. Limited evidence may support “appears to be”; it does not make an assumption a fact or a risk a certainty. Keep open questions visible.</p>
    <p>Do not invent SAP behavior for a version you have not checked, client names, project details, or internal paths. Say what is unknown.</p>
  </section>

  <section>
    <h2>Deliver a usable record</h2>
    <p>Use the skill’s template or <a href="/skill-hub/artifact-templates/">Artifact Templates</a>. Produce the actual RCA note, decision record, rule, or other agreed output. A paragraph explaining why governance or architecture matters cannot replace it.</p>
    <p>Before handing it over, check:</p>
    <ul>
      <li>The situation summary distinguishes what is known, assumed, and missing.</li>
      <li>The selected skills and the reason for using them are clear.</li>
      <li>Every required field is filled or marked “Unknown — needs input from [owner].”</li>
      <li>Dates, owners, evidence, and unresolved questions are included.</li>
      <li>Next actions say who does what by when; unknown owners or dates remain explicit gaps.</li>
      <li>The record can be pasted into a ticket, document, or wiki without rewriting.</li>
    </ul>
    <p>Keep this context and the quality check with the deliverable. Do not append a prose summary that repeats the artifact.</p>
  </section>
</article>
