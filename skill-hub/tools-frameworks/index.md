---
layout: default
title: "Tools & Frameworks Catalog — Business and Systems Analysis"
description: "A practical catalog of analysis tools and frameworks: RACI, SIPOC, BPMN, EventStorming, Domain Storytelling, C4, DMN, Example Mapping, SysML v2, and more."
permalink: /skill-hub/tools-frameworks/
last_modified_at: 2026-09-26
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li aria-current="page">Tools &amp; Frameworks</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Analysis Toolkit</p>
  <h1>Tools &amp; Frameworks Catalog</h1>
  <p class="lead">Choose a method by the problem you need to solve. Do not use RACI because everyone knows RACI. Use it when work ownership is unclear. Use EventStorming when the team does not share the same view of what happens in the business. Use DMN when rules are complex enough that prose becomes dangerous.</p>

  <section>
    <h2>How to use this catalog</h2>
    <ol>
      <li><strong>Start with the work problem.</strong> Is the problem ownership, process, rules, scope, behavior, integration, risk, or prioritization?</li>
      <li><strong>Pick the lightest method that can expose the missing structure.</strong> A ten-minute RACI may be enough. A formal model may be unnecessary.</li>
      <li><strong>Produce an artifact.</strong> A method is useful only when it leaves a map, matrix, decision, model, or testable statement behind.</li>
      <li><strong>Combine methods only when each adds a different view.</strong> For example: SIPOC for the boundary, BPMN for flow, DMN for decision logic, and RACI for ownership.</li>
      <li><strong>Stop when the decision is clear.</strong> Do not turn modeling into documentation theatre.</li>
    </ol>
  </section>

  <section>
    <h2>Choose by situation</h2>
    <table class="study-table">
      <thead><tr><th>Situation</th><th>Use</th><th>Main output</th><th>Watch for</th></tr></thead>
      <tbody>
        <tr><td>People disagree about who owns work</td><td><a href="/skill-hub/tools-frameworks/raci/">RACI</a></td><td>Responsibility matrix</td><td>Do not use RACI as a decision-rights model.</td></tr>
        <tr><td>A decision has many voices but no clear decision maker</td><td><a href="/skill-hub/tools-frameworks/decision-rights-daci-rapid/">DACI / RAPID</a></td><td>Decision roles</td><td>Keep one final decision owner.</td></tr>
        <tr><td>The process boundary is unclear</td><td><a href="/skill-hub/tools-frameworks/sipoc/">SIPOC</a></td><td>High-level process boundary</td><td>Do not confuse it with detailed flow.</td></tr>
        <tr><td>The actual process needs precise flow and exceptions</td><td><a href="/skill-hub/tools-frameworks/bpmn/">BPMN</a></td><td>Process model</td><td>Model only the detail needed for the decision.</td></tr>
        <tr><td>Business and IT hold different mental models</td><td><a href="/skill-hub/tools-frameworks/domain-storytelling/">Domain Storytelling</a></td><td>Shared business story</td><td>Let domain experts tell the story.</td></tr>
        <tr><td>The domain is complex and event-driven</td><td><a href="/skill-hub/tools-frameworks/eventstorming/">EventStorming</a></td><td>Event timeline and hotspots</td><td>Do not jump into solution design too early.</td></tr>
        <tr><td>Scope is a flat backlog with no user journey</td><td><a href="/skill-hub/tools-frameworks/user-story-mapping/">User Story Mapping</a></td><td>Journey and release slices</td><td>Keep outcomes and user flow visible.</td></tr>
        <tr><td>A story is vague or acceptance criteria are weak</td><td><a href="/skill-hub/tools-frameworks/example-mapping/">Example Mapping</a></td><td>Rules, examples, questions</td><td>Use concrete examples, not generic statements.</td></tr>
        <tr><td>Rules are nested, repetitive, or contradictory</td><td><a href="/skill-hub/tools-frameworks/dmn-decision-tables/">DMN &amp; Decision Tables</a></td><td>Decision model</td><td>Separate business decision logic from process flow.</td></tr>
        <tr><td>Teams disagree about system boundaries</td><td><a href="/skill-hub/tools-frameworks/c4-system-context/">C4 System Context</a></td><td>System boundary map</td><td>Do not start at component detail.</td></tr>
        <tr><td>An integration fails because interaction order is unclear</td><td><a href="/skill-hub/tools-frameworks/sequence-diagrams/">Sequence Diagram</a></td><td>Time-ordered interaction</td><td>Include errors and retries where relevant.</td></tr>
        <tr><td>An entity can be in invalid or confusing states</td><td><a href="/skill-hub/tools-frameworks/state-machine-diagrams/">State Machine</a></td><td>States and transitions</td><td>Use business-relevant states, not screen labels.</td></tr>
        <tr><td>Data ownership across processes is unclear</td><td><a href="/skill-hub/tools-frameworks/crud-matrix/">CRUD Matrix</a></td><td>Process-to-data responsibility map</td><td>Do not treat every read as ownership.</td></tr>
        <tr><td>Teams jump from a goal directly to features</td><td><a href="/skill-hub/tools-frameworks/impact-mapping/">Impact Mapping</a></td><td>Goal → actor → impact → deliverable</td><td>Keep measurable outcomes above solution ideas.</td></tr>
        <tr><td>A design can fail in several ways</td><td><a href="/skill-hub/tools-frameworks/fmea/">FMEA</a></td><td>Failure-mode risk review</td><td>Scores support discussion; they do not replace judgment.</td></tr>
        <tr><td>Scope must be prioritized under a fixed constraint</td><td><a href="/skill-hub/tools-frameworks/moscow-prioritization/">MoSCoW</a></td><td>Priority classes</td><td>Define what “Must” means before classifying.</td></tr>
        <tr><td>A complex system needs formal, traceable model-based engineering</td><td><a href="/skill-hub/tools-frameworks/sysml-v2/">SysML v2</a></td><td>Integrated system model</td><td>Use only when model rigor justifies the learning cost.</td></tr>
      </tbody>
    </table>
  </section>

  <section>
    <h2>Core mental model</h2>
    <table class="study-table">
      <thead><tr><th>Question</th><th>Useful methods</th></tr></thead>
      <tbody>
        <tr><td>Who owns it?</td><td>RACI, DACI, RAPID</td></tr>
        <tr><td>Where does the process start and end?</td><td>SIPOC, C4 System Context</td></tr>
        <tr><td>What happens?</td><td>BPMN, Domain Storytelling, EventStorming</td></tr>
        <tr><td>What rules decide the outcome?</td><td>Example Mapping, Decision Tables, DMN</td></tr>
        <tr><td>How does the system behave over time?</td><td>Sequence Diagram, State Machine</td></tr>
        <tr><td>Who changes which data?</td><td>CRUD Matrix</td></tr>
        <tr><td>Why are we building this?</td><td>Impact Mapping, User Story Mapping</td></tr>
        <tr><td>What can fail?</td><td>FMEA, Root Cause Analysis</td></tr>
        <tr><td>What do we do first?</td><td>MoSCoW, evidence-based prioritization</td></tr>
        <tr><td>Do we need a formal integrated model?</td><td>SysML v2</td></tr>
      </tbody>
    </table>
  </section>

  <section>
    <h2>Pair the method with a working skill</h2>
    <p>The method page explains the instrument. The working-skill page explains the job.</p>
    <ul>
      <li><a href="/skill-hub/business-analysis/process-analysis-working-skill/">Process Analysis</a> — use SIPOC, BPMN, EventStorming, or Domain Storytelling as needed.</li>
      <li><a href="/skill-hub/business-analysis/stakeholder-analysis-working-skill/">Stakeholder Analysis</a> — use RACI when delivery ownership is unclear.</li>
      <li><a href="/skill-hub/business-analysis/business-rules-discovery-working-skill/">Business Rules Discovery</a> — use Example Mapping, Decision Tables, or DMN.</li>
      <li><a href="/skill-hub/systems-analysis/state-lifecycle-analysis-working-skill/">State &amp; Lifecycle Analysis</a> — use state-machine diagrams for precision.</li>
      <li><a href="/skill-hub/systems-analysis/interface-requirement-analysis-working-skill/">Interface Requirement Analysis</a> — use C4 and sequence diagrams to expose boundaries and interaction order.</li>
      <li><a href="/skill-hub/architecture/architecture-decision-record-working-skill/">Architecture Decision Record</a> — record the decision after the analysis method has exposed the trade-off.</li>
    </ul>
  </section>

  <section>
    <h2>SAP Lead method stacks</h2>
    <p>In an assessment or project, strong analysis usually combines a few views. Use the smallest stack that makes the decision defensible.</p>
    <table class="study-table">
      <thead><tr><th>Situation</th><th>Suggested stack</th><th>Why</th></tr></thead>
      <tbody>
        <tr>
          <td>Redesign an end-to-end SAP process</td>
          <td><a href="/skill-hub/tools-frameworks/sipoc/">SIPOC</a> → <a href="/skill-hub/tools-frameworks/domain-storytelling/">Domain Storytelling</a> or <a href="/skill-hub/tools-frameworks/eventstorming/">EventStorming</a> → <a href="/skill-hub/tools-frameworks/bpmn/">BPMN</a> → <a href="/skill-hub/tools-frameworks/raci/">RACI</a></td>
          <td>Frame the boundary, discover reality, formalize the flow, then assign ownership.</td>
        </tr>
        <tr>
          <td>Define a cross-system integration</td>
          <td><a href="/skill-hub/tools-frameworks/c4-system-context/">C4</a> → <a href="/skill-hub/tools-frameworks/sequence-diagrams/">Sequence Diagram</a> → <a href="/skill-hub/systems-analysis/interface-requirement-analysis-working-skill/">Interface Requirements</a> → <a href="/skill-hub/tools-frameworks/fmea/">FMEA</a></td>
          <td>Clarify boundary, interaction order, contract expectations, and failure behavior.</td>
        </tr>
        <tr>
          <td>Turn vague requirements into testable scope</td>
          <td><a href="/skill-hub/tools-frameworks/user-story-mapping/">Story Mapping</a> → <a href="/skill-hub/tools-frameworks/example-mapping/">Example Mapping</a> → <a href="/skill-hub/tools-frameworks/dmn-decision-tables/">Decision Table / DMN</a> → <a href="/skill-hub/business-analysis/acceptance-criteria-working-skill/">Acceptance Criteria</a></td>
          <td>Keep the journey visible, expose rules with examples, formalize complex decisions, then define proof.</td>
        </tr>
        <tr>
          <td>Resolve a stuck governance decision</td>
          <td><a href="/skill-hub/tools-frameworks/decision-rights-daci-rapid/">DACI / RAPID</a> → <a href="/skill-hub/decision-validation/trade-off-analysis-working-skill/">Trade-Off Analysis</a> → <a href="/skill-hub/architecture/architecture-decision-record-working-skill/">ADR</a></td>
          <td>Clarify decision rights, compare options, then preserve the rationale.</td>
        </tr>
        <tr>
          <td>Find why data is inconsistent across systems</td>
          <td><a href="/skill-hub/tools-frameworks/crud-matrix/">CRUD Matrix</a> → <a href="/skill-hub/tools-frameworks/c4-system-context/">C4</a> → <a href="/skill-hub/tools-frameworks/sequence-diagrams/">Sequence Diagram</a> → <a href="/skill-hub/tools-frameworks/raci/">RACI</a></td>
          <td>Find who changes the data, where it moves, in what order, and who owns correction.</td>
        </tr>
      </tbody>
    </table>
  </section>

  <section>
    <h2>Modern methods worth knowing</h2>
    <p>Modern analysis is moving away from large static requirement documents toward collaborative models, executable decisions, and traceable system models. EventStorming and Domain Storytelling improve cross-functional discovery. Example Mapping ties requirements to concrete examples. C4 keeps architecture diagrams understandable. DMN makes decision logic explicit. SysML v2 adds stronger semantics, textual notation, and a standard API for model-based systems engineering.</p>
  </section>

  <section>
    <h2>Catalog rule</h2>
    <p>This catalog will grow, but new entries should earn their place. A method belongs here when it solves a recurring work problem, produces a reviewable artifact, has clear decision rules, and adds something that existing methods do not already cover.</p>
  </section>

  <section>
    <h2>Verification status and limitations</h2>
    <p>This page is a review candidate. It is a practical selection guide, not official documentation for IIBA, OMG, PMI, Bain, Atlassian, or any other framework owner. Individual method pages link to primary or well-established references where practical.</p>
  </section>
</article>
