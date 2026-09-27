---
layout: default
title: "Methods & Frameworks Catalog — Practical Analysis Toolkit"
description: "A practical selector for business analysis, systems analysis, architecture, product discovery, process improvement, and delivery methods. Choose a method by the problem you need to solve."
permalink: /skill-hub/methods-catalog/
last_modified_at: 2026-09-27
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li aria-current="page">Methods &amp; Frameworks Catalog</li>
  </ol>
</nav>

<section class="section atlas-hero">
  <p class="eyebrow">Skill Hub — Methods &amp; Frameworks</p>
  <h1>Choose the method by the problem, not by the acronym.</h1>
  <p class="lead">A working catalog for business analysts, systems analysts, architects, product teams, and SAP Leads. Start with the decision you need to make or the uncertainty you need to remove. Then pick the smallest method that produces useful evidence.</p>
  <div class="atlas-hero__actions">
    <a class="button button--primary" href="#method-selector">Choose a method</a>
    <a class="button" href="/skill-hub/business-analysis/">Business Analysis</a>
    <a class="button" href="/skill-hub/systems-analysis/">Systems Analysis</a>
    <a class="button" href="/skill-hub/framework-map/">Framework Map</a>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <h2>How to use this catalog</h2>
  </header>
  <ol>
    <li><strong>Name the uncertainty.</strong> Do not start with “we need a workshop.” Start with “ownership is unclear,” “the process boundary is disputed,” or “the rule has too many exceptions.”</li>
    <li><strong>Choose one primary method.</strong> A method should answer one important question well. Add a second method only when the first output exposes a different problem.</li>
    <li><strong>Produce an artifact.</strong> A RACI should end as an ownership matrix. SIPOC should end as a bounded process view. DMN should end as reviewable decision logic.</li>
    <li><strong>Validate with the people who own the work.</strong> A clean diagram is not evidence that the model is true.</li>
    <li><strong>Connect the artifact to the next decision.</strong> Use the output as an input to requirements, architecture, testing, backlog, governance, or operating procedures.</li>
  </ol>
</section>

<section class="section" id="method-selector">
  <header class="section-heading">
    <h2>Method selector</h2>
    <p>Start from the problem you can observe.</p>
  </header>
  <div class="table-scroll">
    <table class="study-table">
      <thead>
        <tr>
          <th>When the problem is…</th>
          <th>Start with</th>
          <th>Output you should expect</th>
          <th>Use next when needed</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Several people “own” the same work, or nobody does</td>
          <td><a href="/skill-hub/methods-catalog/raci-matrix/">RACI Matrix</a></td>
          <td>Role-by-activity ownership matrix</td>
          <td><a href="/skill-hub/methods-catalog/daci/">DACI</a> if decision authority is the real issue</td>
        </tr>
        <tr>
          <td>A decision is slow because approval roles are unclear</td>
          <td><a href="/skill-hub/methods-catalog/daci/">DACI</a></td>
          <td>Driver, approver, contributors, informed parties</td>
          <td><a href="/skill-hub/architecture/architecture-decision-record-working-skill/">ADR</a> to preserve the decision</td>
        </tr>
        <tr>
          <td>The team cannot agree where a process starts and ends</td>
          <td><a href="/skill-hub/methods-catalog/sipoc/">SIPOC</a></td>
          <td>Suppliers, inputs, high-level process, outputs, customers</td>
          <td><a href="/skill-hub/methods-catalog/bpmn/">BPMN</a> for detailed flow</td>
        </tr>
        <tr>
          <td>The process is understood differently by each team</td>
          <td><a href="/skill-hub/methods-catalog/bpmn/">BPMN</a></td>
          <td>Shared process model with events, activities, gateways, and handoffs</td>
          <td><a href="/skill-hub/methods-catalog/value-stream-mapping/">Value Stream Mapping</a> for time and waste</td>
        </tr>
        <tr>
          <td>Lead time is long but local teams each look efficient</td>
          <td><a href="/skill-hub/methods-catalog/value-stream-mapping/">Value Stream Mapping</a></td>
          <td>Current-state flow with wait time, work time, inventory/queues, and information flow</td>
          <td><a href="/skill-hub/business-analysis/gap-analysis-working-skill/">Gap Analysis</a> for the future-state closure plan</td>
        </tr>
        <tr>
          <td>Stakeholders have different influence and different information needs</td>
          <td><a href="/skill-hub/methods-catalog/stakeholder-power-interest-matrix/">Power–Interest Matrix</a></td>
          <td>Engagement strategy by stakeholder</td>
          <td><a href="/skill-hub/methods-catalog/raci-matrix/">RACI</a> when work ownership must be assigned</td>
        </tr>
        <tr>
          <td>Everything is called “Must Have”</td>
          <td><a href="/skill-hub/methods-catalog/moscow-prioritization/">MoSCoW</a></td>
          <td>Explicit priority with rationale and time horizon</td>
          <td><a href="/skill-hub/methods-catalog/impact-mapping/">Impact Mapping</a> if value is still unclear</td>
        </tr>
        <tr>
          <td>A requirement is vague and edge cases appear late</td>
          <td><a href="/skill-hub/methods-catalog/example-mapping/">Example Mapping</a></td>
          <td>Rules, examples, unanswered questions, story splits</td>
          <td><a href="/skill-hub/business-analysis/acceptance-criteria-working-skill/">Acceptance Criteria</a></td>
        </tr>
        <tr>
          <td>A flat backlog hides the end-to-end user journey</td>
          <td><a href="/skill-hub/methods-catalog/user-story-mapping/">User Story Mapping</a></td>
          <td>User journey backbone, slices, release options</td>
          <td><a href="/skill-hub/methods-catalog/moscow-prioritization/">MoSCoW</a> for release trade-offs</td>
        </tr>
        <tr>
          <td>Features are not clearly connected to a business outcome</td>
          <td><a href="/skill-hub/methods-catalog/impact-mapping/">Impact Mapping</a></td>
          <td>Goal → actors → impacts → deliverables</td>
          <td><a href="/skill-hub/methods-catalog/user-story-mapping/">User Story Mapping</a> for delivery structure</td>
        </tr>
        <tr>
          <td>Business knowledge is fragmented across functions and systems</td>
          <td><a href="/skill-hub/methods-catalog/eventstorming/">EventStorming</a></td>
          <td>Domain events, commands, actors, policies, hotspots, boundaries</td>
          <td><a href="/skill-hub/methods-catalog/bpmn/">BPMN</a> for stable process detail or <a href="/skill-hub/architecture/system-context-mapping-working-skill/">System Context Mapping</a> for boundaries</td>
        </tr>
        <tr>
          <td>Decision logic has many conditions, combinations, and exceptions</td>
          <td><a href="/skill-hub/methods-catalog/dmn-decision-tables/">DMN Decision Tables</a></td>
          <td>Explicit input conditions and outcomes</td>
          <td><a href="/skill-hub/business-analysis/business-rules-discovery-working-skill/">Business Rules Discovery</a> when rules are still hidden</td>
        </tr>
        <tr>
          <td>It is unclear which system creates, reads, updates, or deletes an entity</td>
          <td><a href="/skill-hub/methods-catalog/crud-matrix/">CRUD Matrix</a></td>
          <td>Entity-to-system or entity-to-process responsibility matrix</td>
          <td><a href="/skill-hub/systems-analysis/interface-requirement-analysis-working-skill/">Interface Requirement Analysis</a></td>
        </tr>
        <tr>
          <td>System scope and external dependencies are unclear</td>
          <td><a href="/skill-hub/architecture/system-context-mapping-working-skill/">System Context Mapping / C4 context</a></td>
          <td>System boundary, people, neighboring systems, data flows</td>
          <td><a href="/skill-hub/systems-analysis/interface-requirement-analysis-working-skill/">Interface Requirement Analysis</a></td>
        </tr>
        <tr>
          <td>An object can enter invalid or unexplained statuses</td>
          <td><a href="/skill-hub/systems-analysis/state-lifecycle-analysis-working-skill/">State &amp; Lifecycle Analysis</a></td>
          <td>States, events, transitions, guards</td>
          <td><a href="/skill-hub/methods-catalog/dmn-decision-tables/">DMN</a> if transition rules are complex</td>
        </tr>
        <tr>
          <td>An architecture choice needs a durable explanation</td>
          <td><a href="/skill-hub/architecture/architecture-decision-record-working-skill/">Architecture Decision Record</a></td>
          <td>Context, options, decision, consequences</td>
          <td><a href="/skill-hub/decision-validation/">Decision &amp; Validation skills</a> for deeper comparison</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <h2>Ownership and stakeholder methods</h2>
  </header>
  <div class="topic-grid">
    <div class="topic-card">
      <h3><a href="/skill-hub/methods-catalog/raci-matrix/">RACI Matrix</a></h3>
      <p>Clarify who does the work, who approves the result, who gives input, and who receives the outcome.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/methods-catalog/daci/">DACI</a></h3>
      <p>Clarify who drives a decision and who has final approval when a RACI is too activity-focused.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/methods-catalog/stakeholder-power-interest-matrix/">Power–Interest Matrix</a></h3>
      <p>Choose how closely to engage stakeholders based on influence and interest rather than job title alone.</p>
    </div>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <h2>Process and improvement methods</h2>
  </header>
  <div class="topic-grid">
    <div class="topic-card">
      <h3><a href="/skill-hub/methods-catalog/sipoc/">SIPOC</a></h3>
      <p>Set process boundaries before detailed mapping and agree the critical inputs and outputs.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/methods-catalog/bpmn/">BPMN</a></h3>
      <p>Model events, activities, gateways, roles, messages, and exceptions with a shared notation.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/methods-catalog/value-stream-mapping/">Value Stream Mapping</a></h3>
      <p>See end-to-end lead time, work time, queues, handoffs, and information flow before optimizing local steps.</p>
    </div>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <h2>Requirements and product discovery methods</h2>
  </header>
  <div class="topic-grid">
    <div class="topic-card">
      <h3><a href="/skill-hub/methods-catalog/moscow-prioritization/">MoSCoW</a></h3>
      <p>Force explicit trade-offs between Must, Should, Could, and Won’t Have this time.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/methods-catalog/example-mapping/">Example Mapping</a></h3>
      <p>Use concrete examples to expose rules, missing cases, questions, and oversized stories.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/methods-catalog/user-story-mapping/">User Story Mapping</a></h3>
      <p>Arrange backlog items around the user journey and slice coherent releases.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/methods-catalog/impact-mapping/">Impact Mapping</a></h3>
      <p>Connect a measurable goal to the people who can affect it, the behavior change needed, and possible deliverables.</p>
    </div>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <h2>Domain and systems methods</h2>
  </header>
  <div class="topic-grid">
    <div class="topic-card">
      <h3><a href="/skill-hub/methods-catalog/eventstorming/">EventStorming</a></h3>
      <p>Build shared domain understanding quickly by mapping what happens, why it happens, and where knowledge conflicts.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/methods-catalog/dmn-decision-tables/">DMN Decision Tables</a></h3>
      <p>Move complex decision logic out of prose and into reviewable rules with explicit inputs and outputs.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/methods-catalog/crud-matrix/">CRUD Matrix</a></h3>
      <p>Expose data responsibility and missing ownership across processes, systems, or capabilities.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/architecture/system-context-mapping-working-skill/">System Context Mapping</a></h3>
      <p>Use the existing Skill Hub method for a C4-style big-picture boundary around people and external systems.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/systems-analysis/state-lifecycle-analysis-working-skill/">State &amp; Lifecycle Analysis</a></h3>
      <p>Use the existing Systems Analysis skill for object states, transitions, events, and guards.</p>
    </div>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <h2>Selection rules</h2>
  </header>
  <ul>
    <li><strong>If the problem is about ownership, do not start with BPMN.</strong> Start with RACI or DACI, then place ownership into the process model.</li>
    <li><strong>If the process boundary is still disputed, do not draw detailed BPMN.</strong> Use SIPOC first.</li>
    <li><strong>If a flow contains many policy decisions, keep process flow and decision logic separate.</strong> BPMN shows the flow; DMN can show the decision.</li>
    <li><strong>If a backlog is large but the outcome is unclear, do not prioritize the list yet.</strong> Use Impact Mapping before MoSCoW.</li>
    <li><strong>If requirements are abstract, ask for examples before more prose.</strong> Example Mapping is often faster than another document review.</li>
    <li><strong>If an optimization improves one team but not the end-to-end result, move up one level.</strong> Use Value Stream Mapping.</li>
    <li><strong>If teams disagree about the domain itself, model together before designing systems.</strong> EventStorming can expose language, boundary, and policy conflicts early.</li>
    <li><strong>If the same artifact has no next decision, stop producing it.</strong> A method is useful only when its output changes what the team understands or does next.</li>
  </ul>
</section>

<section class="section">
  <header class="section-heading">
    <h2>How methods combine on an SAP project</h2>
  </header>
  <div class="table-scroll">
    <table class="study-table">
      <thead>
        <tr>
          <th>Situation</th>
          <th>Useful chain</th>
          <th>Lead-level question</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Order-to-cash redesign</td>
          <td>SIPOC → BPMN → RACI → DMN → acceptance criteria</td>
          <td>Where is the real boundary, who owns each handoff, and which decisions belong in rules rather than process branches?</td>
        </tr>
        <tr>
          <td>S/4 integration design</td>
          <td>System Context → CRUD → Interface Requirements → ADR</td>
          <td>Which system owns the object, which boundary moves it, and what failure responsibility remains after go-live?</td>
        </tr>
        <tr>
          <td>Pricing or credit rule redesign</td>
          <td>Business Rules Discovery → DMN → Example Mapping → test scenarios</td>
          <td>Can the business explain the rule with examples and can QA prove every decision outcome?</td>
        </tr>
        <tr>
          <td>Procure-to-pay delay</td>
          <td>Value Stream Mapping → BPMN → RACI → Gap Analysis</td>
          <td>Is time lost in processing, waiting, approval, data correction, or cross-team queues?</td>
        </tr>
        <tr>
          <td>New business capability</td>
          <td>Impact Mapping → EventStorming → User Story Mapping → MoSCoW</td>
          <td>Which behavior change creates the outcome, what domain events matter, and what is the smallest coherent release?</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <h2>Methods radar — candidates to add next</h2>
  </header>
  <p>This catalog is designed to grow. A method is added when it gives a distinct decision advantage, has a repeatable working pattern, and can produce a reviewable artifact. Candidates for the next passes include Domain Storytelling, Bounded Context Canvas, Wardley Mapping, Opportunity Solution Trees, A3 problem solving, Assumption Mapping, Story Splitting, and dependency mapping.</p>
  <p>The goal is not to collect acronyms. The goal is to keep a small, strong toolkit that helps a Lead choose the right thinking model for the situation.</p>
</section>

<section class="section">
  <header class="section-heading">
    <h2>Primary references</h2>
  </header>
  <ul>
    <li><a href="https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/glossary/">IIBA BABOK glossary</a> — includes the RACI definition and business analysis terminology.</li>
    <li><a href="https://www.omg.org/bpmn/">Object Management Group — BPMN</a> — official BPMN standard information.</li>
    <li><a href="https://www.omg.org/dmn/">Object Management Group — DMN</a> — official DMN standard information.</li>
    <li><a href="https://cucumber.io/docs/bdd/example-mapping/">Cucumber — Example Mapping</a> — rules, examples, questions, and story discovery.</li>
    <li><a href="https://www.eventstorming.com/">EventStorming</a> — official resources and workshop material.</li>
    <li><a href="https://www.impactmapping.org/">Impact Mapping</a> — goal, actors, impacts, and deliverables.</li>
    <li><a href="https://asq.org/quality-resources/sipoc">ASQ — SIPOC</a> — process-boundary and process-input/output guidance.</li>
    <li><a href="https://www.lean.org/lexicon-terms/value-stream-mapping/">Lean Enterprise Institute — Value Stream Mapping</a>.</li>
    <li><a href="https://www.agilebusiness.org/resource/what-is-moscow-prioritization/">Agile Business Consortium — MoSCoW prioritization</a>.</li>
  </ul>
</section>

<section class="section">
  <header class="section-heading">
    <h2>Status and limitations</h2>
  </header>
  <p>This is a working cross-framework catalog, not official BABOK, BPMN, DMN, DSDM, Lean, C4, or SAP documentation. Method pages focus on practical use in enterprise delivery. Formal standards can contain more notation and rules than a working page needs.</p>
  <p>New pages stay in review-candidate status until they receive human review. Use the official sources when formal compliance with a standard matters.</p>
</section>
