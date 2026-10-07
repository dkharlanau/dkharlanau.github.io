---
layout: default
title: "SAP Signavio Product Guide"
description: "A concise Lead-level guide to SAP Signavio: product map, components, licensing boundaries, BPMN and DMN, collaboration, journeys, governance, process intelligence, transformation management, integrations, administration, best practices, and glossary."
permalink: /atlas/sap/sap-signavio/
atlas_section: sap
domain: SAP operations
subdomain: Process transformation
concept_type: product
sap_area: "SAP Signavio"
business_process: "Process management"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
last_modified_at: 2026-10-07
author: Dzmitryi Kharlanau

tags:
  - sap-signavio
  - process-modeler
  - process-manager
  - process-intelligence
  - process-governance
  - journey-modeler
  - process-transformation-manager
  - bpmn
  - dmn
  - process-mining
  - process-variants
  - business-process-model-connector
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/sap-btp/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-build/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Signavio</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">SAP Product Guide / Lead Preparation</p>
    <h1>SAP Signavio</h1>
    <p class="note-subtitle">Understand the full product picture: what each component does, how they work together, where the licensing boundaries are, and how to explain the suite to a client.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Goal</dt><dd>Explain SAP Signavio clearly to a client or interviewer</dd></div>
      <div><dt>Scope</dt><dd>Process design, collaboration, governance, journeys, mining, transformation, integration</dd></div>
      <div><dt>Level</dt><dd>SAP Lead mental model</dd></div>
      <div><dt>Language</dt><dd>English B2</dd></div>
      <div><dt>Status</dt><dd>Current-state product guide with explicit licensing boundaries</dd></div>
    </dl>
  </aside>

  <div class="note-body">

    <h2 id="start">1. Start with one picture</h2>

    <p>SAP Signavio is a process transformation suite. It connects process design, business collaboration, customer or employee journeys, workflow governance, operational process data, and improvement initiatives.</p>

    <p>The simplest mental model is:</p>

    <p><strong>Reference → Model → Collaborate → Govern → Observe → Improve → Model again</strong></p>

    <table class="study-table">
      <thead>
        <tr>
          <th>Need</th>
          <th>Primary component</th>
          <th>Plain-English explanation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Design the process</td>
          <td>SAP Signavio Process Modeler</td>
          <td>Describe how the business should work.</td>
        </tr>
        <tr>
          <td>Publish and discuss the process</td>
          <td>SAP Signavio Process Collaboration Hub</td>
          <td>Give business users one place to consume and discuss process knowledge.</td>
        </tr>
        <tr>
          <td>Understand the experience</td>
          <td>SAP Signavio Journey Modeler</td>
          <td>See the company from the customer, employee, supplier, or partner perspective.</td>
        </tr>
        <tr>
          <td>Execute governance work</td>
          <td>SAP Signavio Process Governance</td>
          <td>Run approvals, reviews, tasks, reminders, and controlled workflow cases.</td>
        </tr>
        <tr>
          <td>Understand real execution</td>
          <td>SAP Signavio Process Intelligence</td>
          <td>Use operational data to see what actually happened.</td>
        </tr>
        <tr>
          <td>Manage improvement work</td>
          <td>SAP Signavio Process Transformation Manager</td>
          <td>Turn findings into prioritized initiatives, objectives, tasks, and value cases.</td>
        </tr>
        <tr>
          <td>Start from SAP reference content</td>
          <td>SAP Signavio Process Navigator / Value Accelerator Library</td>
          <td>Reuse reference processes, capabilities, metrics, and accelerators instead of starting from a blank page.</td>
        </tr>
      </tbody>
    </table>

    <p><strong>The key Lead skill is product selection.</strong> Do not answer every question with “Signavio”. Name the problem first, then the component that owns it.</p>

    <h3>Current naming you should know</h3>

    <p><strong>Process Modeler</strong> is the current product name. Older SAP Learning content and customer environments can still use <strong>Process Manager</strong>. Treat them as the same modeling product generation, not as two different products.</p>

    <p><strong>Process Explorer is no longer the current reference-content product.</strong> SAP retired SAP Signavio Process Explorer on June 30, 2026 and moved its reference content to <strong>SAP Signavio Process Navigator</strong>. Process Navigator is now the reference point for SAP process content through SAP for Me. The Value Accelerator Library remains available for accelerator content inside the Signavio suite.</p>

    <h2 id="client-map">2. Client question → Signavio component</h2>

    <table class="study-table">
      <thead>
        <tr>
          <th>Client says...</th>
          <th>Think first about...</th>
          <th>Why</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>“Every country models the same process differently.”</td>
          <td>Process Modeler + Dictionary + conventions + Variant Management</td>
          <td>The problem is standardization and controlled variation.</td>
        </tr>
        <tr>
          <td>“Nobody knows which process is current.”</td>
          <td>Process Modeler + Collaboration Hub + governance</td>
          <td>The problem is ownership, publication, and consumption.</td>
        </tr>
        <tr>
          <td>“We need approval before a process is published.”</td>
          <td>Process Governance + Process Modeler</td>
          <td>The model is in Modeler; the approval work executes in Governance.</td>
        </tr>
        <tr>
          <td>“The BPMN model looks fine, but orders are still late.”</td>
          <td>Process Intelligence</td>
          <td>You need evidence from real execution, not another drawing.</td>
        </tr>
        <tr>
          <td>“Our process works internally, but customers hate it.”</td>
          <td>Journey Modeler + linked processes</td>
          <td>The internal view and the outside-in experience are different.</td>
        </tr>
        <tr>
          <td>“We found ten improvement ideas. Which one should we fund?”</td>
          <td>Process Transformation Manager</td>
          <td>The problem is prioritization, ownership, value, and initiative execution.</td>
        </tr>
        <tr>
          <td>“We need SAP best-practice process content for a workshop.”</td>
          <td>Process Navigator / Value Accelerator Library</td>
          <td>Use reference content before modeling from zero.</td>
        </tr>
        <tr>
          <td>“Business models in Signavio, IT documents in Solution Manager.”</td>
          <td>Business Process Model Connector</td>
          <td>The problem is controlled Business–IT process synchronization.</td>
        </tr>
      </tbody>
    </table>

    <h2 id="example">3. One simple example across the suite</h2>

    <p>Assume a company wants to improve Order-to-Cash.</p>

    <ol>
      <li><strong>Start with reference content.</strong> Review SAP process content in Process Navigator or relevant accelerators.</li>
      <li><strong>Model the target process.</strong> In Process Modeler, define the O2C flow, roles, systems, documents, and reusable Dictionary objects.</li>
      <li><strong>Separate complex decisions.</strong> Put discount or credit decision logic in DMN instead of building a large gateway tree in BPMN.</li>
      <li><strong>Review and publish.</strong> Stakeholders comment in the collaboration layer. If formal approval is required, Process Governance runs the approval workflow before publication.</li>
      <li><strong>Look outside-in.</strong> Journey Modeler shows what the customer experiences from order creation to delivery and invoice.</li>
      <li><strong>Connect real data.</strong> Process Intelligence shows actual variants, delays, rework, bottlenecks, and performance.</li>
      <li><strong>Create an improvement initiative.</strong> Process Transformation Manager turns the finding into owned work with value, objectives, tasks, and status.</li>
      <li><strong>Update the model.</strong> When the operating model changes, the designed process is updated and the cycle starts again.</li>
    </ol>

    <p>This is the suite story: <strong>design and execution evidence are connected, but they are not the same thing.</strong></p>

    <h2 id="licensing">4. Licensing and access boundaries</h2>

    <p>Do not memorize commercial prices. Understand the boundaries. SAP contracts, packages, and feature scope can change.</p>

    <table class="study-table">
      <thead>
        <tr>
          <th>Product / access</th>
          <th>Boundary to remember</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Process Modeler user</td>
          <td>A modeling user gets the functionality of the licensed Modeler edition and access to Process Collaboration Hub.</td>
        </tr>
        <tr>
          <td>Collaboration Hub user</td>
          <td>A separate consumer license. It also exposes a limited Modeler feature set such as QuickModel, reporting, comparison, export, and Dictionary access.</td>
        </tr>
        <tr>
          <td>External commenter</td>
          <td>Can receive a restricted commenting license after invitation. This is not broad workspace access.</td>
        </tr>
        <tr>
          <td>Journey Modeler</td>
          <td>Separate user licenses exist. SAP identity documentation names Journey Modeling Standard and Journey Modeling Advanced.</td>
        </tr>
        <tr>
          <td>Process Governance</td>
          <td>Separate workflow entitlement. SAP SAML documentation uses the license name Workflow. Process Governance Collaborator is a limited sub-license and is not sold stand-alone.</td>
        </tr>
        <tr>
          <td>Process Intelligence</td>
          <td>The license is assigned to the workspace, not to each user. User access is then controlled with feature sets and data permissions.</td>
        </tr>
        <tr>
          <td>Process Transformation Manager</td>
          <td>Activation, source-product access, product license, and object roles determine available functions. Advanced functions require the relevant license.</td>
        </tr>
        <tr>
          <td>API technical user</td>
          <td>Use API Edition for technical integrations. SAP provides it at no additional cost; it is not a normal UI user license.</td>
        </tr>
        <tr>
          <td>Business Process Model Connector</td>
          <td>Requires the connector entitlement/subscription on SAP BTP plus roles and technical prerequisites.</td>
        </tr>
        <tr>
          <td>AI capabilities</td>
          <td>Feature-specific. A base Signavio license does not automatically mean every AI capability or AI consumption model is included.</td>
        </tr>
      </tbody>
    </table>

    <p><strong>License ≠ authorization.</strong> A license gives access to a product. Groups, object permissions, feature sets, and data permissions decide what the user can actually do.</p>

    <h2 id="modeler">5. Process Modeler: what you must understand</h2>

    <h3>The four building blocks</h3>

    <table class="study-table">
      <thead>
        <tr>
          <th>Part</th>
          <th>Purpose</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Explorer / Repository</td>
          <td>Organize process content, folders, search, revisions, access, reports, and analysis entry points.</td>
        </tr>
        <tr>
          <td>Graphical Editor</td>
          <td>Create detailed BPMN, DMN, attributes, and other models.</td>
        </tr>
        <tr>
          <td>QuickModel</td>
          <td>Capture a simple BPMN happy path in a spreadsheet-like view and refine it later in the Editor.</td>
        </tr>
        <tr>
          <td>Dictionary</td>
          <td>Maintain reusable business objects such as roles, systems, documents, risks, controls, and terms.</td>
        </tr>
      </tbody>
    </table>

    <h3>Architecture before diagrams</h3>

    <p>A strong workspace has levels. A simple pattern is:</p>

    <p><strong>Navigation Map → Value Chain → BPMN process → subprocesses → Dictionary objects</strong></p>

    <p>A <strong>Navigation Map</strong> is a flexible entry point. A <strong>Value Chain</strong> is a structured high-level process architecture. BPMN then gives the detailed flow.</p>

    <h3>Dictionary is the shared vocabulary</h3>

    <p>Create a role, system, document, risk, or control once and reuse it. This gives consistent naming and traceability across models.</p>

    <p>A central Dictionary change can affect many linked models. A local diagram attribute can remain local. That is a governance decision, not only an editing choice.</p>

    <p><strong>Best practice:</strong> use sandbox categories for proposed Dictionary entries and a small responsible group to review, merge, and promote them.</p>

    <h3>Syntax vs convention vs business correctness</h3>

    <table class="study-table">
      <thead>
        <tr>
          <th>Check</th>
          <th>Question</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Syntax</td><td>Is the notation used correctly?</td></tr>
        <tr><td>Convention</td><td>Does the model follow company modeling standards?</td></tr>
        <tr><td>Semantic review</td><td>Does the model describe the real business correctly?</td></tr>
      </tbody>
    </table>

    <p>The tool can help with syntax and configured conventions. Subject-matter experts are still needed for semantic correctness.</p>

    <h2 id="bpmn-dmn">6. BPMN and DMN: the minimum Lead toolkit</h2>

    <h3>BPMN</h3>

    <p>Use BPMN to explain <strong>what happens, in what order, and who is responsible</strong>.</p>

    <table class="study-table">
      <thead>
        <tr>
          <th>Element</th>
          <th>Meaning</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Task</td><td>Work that must be done.</td></tr>
        <tr><td>Event</td><td>Trigger, wait, state, or result.</td></tr>
        <tr><td>XOR gateway</td><td>Exactly one alternative path.</td></tr>
        <tr><td>AND gateway</td><td>All parallel paths.</td></tr>
        <tr><td>OR gateway</td><td>One or several valid paths.</td></tr>
        <tr><td>Pool</td><td>Participant or organizational boundary.</td></tr>
        <tr><td>Lane</td><td>Responsibility partition.</td></tr>
        <tr><td>Sequence Flow</td><td>Execution flow inside one pool.</td></tr>
        <tr><td>Message Flow</td><td>Communication between pools.</td></tr>
      </tbody>
    </table>

    <p><strong>A gateway is not the decision.</strong> The decision is made in business logic or a task; the gateway routes the result.</p>

    <p>Use the <strong>token concept</strong> to understand execution behavior. It makes deadlocks, parallel paths, waiting, and duplicate execution easier to reason about.</p>

    <h3>Subprocess choice</h3>

    <table class="study-table">
      <thead>
        <tr><th>Pattern</th><th>Use</th></tr>
      </thead>
      <tbody>
        <tr><td>Collapsed subprocess</td><td>Hide detail and keep the parent process readable.</td></tr>
        <tr><td>Call Activity</td><td>Reuse the same global process logic in several parent processes.</td></tr>
        <tr><td>Expanded subprocess</td><td>Show local grouped detail inside one process.</td></tr>
      </tbody>
    </table>

    <h3>DMN</h3>

    <p>Use DMN when the process contains decision logic that deserves its own model.</p>

    <p><strong>BPMN = process flow.</strong><br>
    <strong>DMN = decision logic.</strong></p>

    <p>DMN has two practical levels:</p>

    <ul>
      <li><strong>Decision Requirements Diagram</strong> — decisions, sub-decisions, input data, and knowledge sources.</li>
      <li><strong>Decision Table</strong> — exact rules that map inputs to outputs.</li>
    </ul>

    <p>Example: BPMN contains the task <strong>Determine customer discount</strong>. DMN evaluates customer type, order value, and policy rules and returns the discount. BPMN then continues with the result.</p>

    <h3>Hit policies</h3>

    <table class="study-table">
      <thead>
        <tr><th>Policy</th><th>Use</th></tr>
      </thead>
      <tbody>
        <tr><td>Unique</td><td>Only one rule may match.</td></tr>
        <tr><td>First</td><td>Rules can overlap; first match wins.</td></tr>
        <tr><td>Any</td><td>Several rules may match only when they return the same output.</td></tr>
        <tr><td>Priority</td><td>Several rules may match; highest-priority output wins.</td></tr>
        <tr><td>Collect</td><td>Several rules may fire and results are collected or aggregated.</td></tr>
      </tbody>
    </table>

    <p><strong>Verify</strong> checks formal completeness and consistency. <strong>Simulation</strong> evaluates outputs for selected inputs. <strong>Test Lab</strong> checks expected outcomes and regression cases after rule changes.</p>

    <h2 id="collaboration-governance">7. Collaboration Hub and Process Governance</h2>

    <h3>Collaboration Hub = consume and collaborate</h3>

    <p>The Hub is the business-facing layer for published process content. It supports navigation, comments, feedback, reporting, read confirmations, ratings, and audience-specific presentation.</p>

    <p><strong>Audience is not authorization.</strong> An audience changes the presentation for a viewer group. Access rights decide whether a user may see or change content.</p>

    <table class="study-table">
      <thead>
        <tr><th>Feature</th><th>Purpose</th></tr>
      </thead>
      <tbody>
        <tr><td>Comment</td><td>Discuss model content with stakeholders.</td></tr>
        <tr><td>Read Confirmation</td><td>Ask users to confirm that they read a process or new revision.</td></tr>
        <tr><td>Process Rating</td><td>Collect structured feedback about a process revision.</td></tr>
      </tbody>
    </table>

    <h3>Process Governance = execute governed work</h3>

    <p>Process Governance is a workflow modeling and execution product. The key objects are:</p>

    <p><strong>Workflow → Case → Tasks → Result</strong></p>

    <ul>
      <li><strong>Workflow</strong> — reusable execution template.</li>
      <li><strong>Case</strong> — one running instance.</li>
      <li><strong>User Task</strong> — one person or role performs work.</li>
      <li><strong>Multi-User Task</strong> — several people perform the same work in parallel or sequence.</li>
      <li><strong>Trigger</strong> — starts a case, for example a form, e-mail, or Process Modeler event.</li>
      <li><strong>Form</strong> — captures or changes workflow data.</li>
    </ul>

    <h3>Approval example</h3>

    <p>A process model is ready for publication. Process Modeler holds the diagram. Process Governance starts an approval case, assigns review tasks, sends reminders, records decisions, and returns the result. Only then is the content published.</p>

    <p>This is a strong product boundary:</p>

    <p><strong>Modeler owns process content. Governance owns workflow execution.</strong></p>

    <h3>Workflow versions</h3>

    <table class="study-table">
      <thead>
        <tr><th>Action</th><th>Meaning</th></tr>
      </thead>
      <tbody>
        <tr><td>Publish</td><td>Create an executable version for new cases.</td></tr>
        <tr><td>Re-Publish</td><td>Make a copy of an older version the version used by new cases.</td></tr>
        <tr><td>Restore</td><td>Bring an older version back into the editable draft without changing the current published execution version.</td></tr>
      </tbody>
    </table>

    <h2 id="journey">8. Journey Modeler: outside-in view</h2>

    <p>A process is usually inside-out: what the company does. A journey is outside-in: what the person experiences.</p>

    <p>Use Journey Modeler for customers, employees, applicants, suppliers, partners, or other people interacting with the organization.</p>

    <p>The basic structure is:</p>

    <p><strong>Persona → Stages → Steps → Touchpoints → Sentiment → Linked process/system/KPI</strong></p>

    <p>A <strong>step</strong> is something the person goes through. A <strong>touchpoint</strong> is an interaction with the company, product, partner, or channel.</p>

    <h3>Journey Modeler vs Customer Journey Map</h3>

    <table class="study-table">
      <thead>
        <tr><th>Approach</th><th>Use</th></tr>
      </thead>
      <tbody>
        <tr><td>Journey Modeler</td><td>Table-based holistic view with journey information, processes, systems, organizations, sentiment, metrics, and data widgets.</td></tr>
        <tr><td>Customer Journey Map</td><td>Visual storytelling of the persona's journey and touchpoints, with details available through attributes and links.</td></tr>
      </tbody>
    </table>

    <p><strong>Journey Complexity</strong> estimates operational complexity behind linked processes. <strong>Journey Model Dimensions</strong> describe the size and populated content of the journey table. They are different metrics.</p>

    <p>The valuable pattern is:</p>

    <p><strong>Pain point → linked internal process → process change → KPI → verify experience improvement</strong></p>

    <h2 id="intelligence">9. Process Intelligence and Process Insights</h2>

    <p>This is the most important distinction in the suite:</p>

    <p><strong>Process Modeler: what should happen?</strong><br>
    <strong>Process Intelligence: what did happen?</strong></p>

    <h3>Minimum process-mining data model</h3>

    <p>Before trusting a dashboard, make sure the analysis represents the business process correctly:</p>

    <ul>
      <li><strong>Case / object</strong> — what one process instance is.</li>
      <li><strong>Activity / event</strong> — what happened.</li>
      <li><strong>Timestamp</strong> — when it happened.</li>
      <li><strong>Attributes</strong> — business context such as company code, customer, material, channel, or status.</li>
      <li><strong>Metrics</strong> — how performance is measured.</li>
    </ul>

    <p>If this semantic model is wrong, a beautiful dashboard can still tell the wrong story.</p>

    <h3>What Process Intelligence does</h3>

    <ul>
      <li>Integrates and prepares process data.</li>
      <li>Supports out-of-the-box and custom process analysis.</li>
      <li>Uses dashboards, metrics, filters, variants, and insights.</li>
      <li>Supports automated root-cause analysis.</li>
      <li>Adds value analysis and monetary impact.</li>
      <li>Uses Analysis Workflows to monitor data and trigger actions.</li>
      <li>Includes AI-assisted analysis capabilities where enabled and licensed.</li>
    </ul>

    <h3>Process Insights relationship</h3>

    <p>Current SAP documentation states that <strong>SAP Signavio Process Insights capabilities are available in SAP Signavio Process Intelligence</strong>. Think of Process Insights as predefined SAP-focused process flows, performance indicators, recommendations, and integration content, while Process Intelligence provides the broader analysis and mining platform.</p>

    <h3>Current UI direction</h3>

    <p>Since May 26, 2026, new Process Intelligence investigations can no longer be created or imported. Existing investigations remain available for now; customizable dashboards are the forward path.</p>

    <h3>Simulation vs reporting vs mining</h3>

    <table class="study-table">
      <thead>
        <tr><th>Capability</th><th>Evidence</th><th>Question</th></tr>
      </thead>
      <tbody>
        <tr><td>Simulation</td><td>Assumptions in a designed model</td><td>What could happen?</td></tr>
        <tr><td>Model reporting</td><td>Model elements and attributes</td><td>What did we document?</td></tr>
        <tr><td>Process Intelligence</td><td>Operational process data</td><td>What actually happened?</td></tr>
      </tbody>
    </table>

    <h2 id="transformation">10. Process Transformation Manager</h2>

    <p>Process Intelligence can find a problem. Process Transformation Manager helps manage the improvement work that follows.</p>

    <p>A simple flow is:</p>

    <p><strong>Finding → Insight → Initiative → Objective → Tasks → Value / progress</strong></p>

    <table class="study-table">
      <thead>
        <tr><th>Object</th><th>Purpose</th></tr>
      </thead>
      <tbody>
        <tr><td>Benchmarking</td><td>Compare performance with available peer or best-in-class benchmarks.</td></tr>
        <tr><td>Insight</td><td>Capture an important finding or improvement idea.</td></tr>
        <tr><td>Initiative</td><td>Organize and prioritize improvement work.</td></tr>
        <tr><td>Objective</td><td>Define the goal the initiative should support.</td></tr>
        <tr><td>Task</td><td>Assign concrete work and ownership.</td></tr>
        <tr><td>Value Analysis</td><td>Connect improvement work with monetary impact.</td></tr>
        <tr><td>Asset</td><td>Attach relevant process, dashboard, document, or external reference to an initiative.</td></tr>
      </tbody>
    </table>

    <p>Do not confuse Process Transformation Manager with Process Governance. <strong>Governance executes repeatable workflows. Transformation Manager manages improvement initiatives.</strong></p>

    <h2 id="reference-content">11. Reference content: Process Navigator and Value Accelerator Library</h2>

    <h3>SAP Signavio Process Navigator</h3>

    <p>Process Navigator is SAP's current reference point for SAP process content. It is available through SAP for Me and provides process hierarchies, solution processes, variants, roles, capabilities, documentation, and related implementation content.</p>

    <p>Use it when the client asks: <strong>“What is the SAP standard or reference process?”</strong></p>

    <h3>Value Accelerator Library</h3>

    <p>The Value Accelerator Library is embedded in the Signavio suite and provides installable or reusable accelerator content for supported Signavio products. Accelerators can include process models, metrics, dashboards, maps, templates, and other transformation content.</p>

    <p><strong>Important:</strong> accelerators are starting content, not the customer's final operating model. SAP states that value accelerators are optional and not part of core product business functionality.</p>

    <h3>Legacy term: Process Explorer</h3>

    <p>SAP Signavio Process Explorer was retired on June 30, 2026. Its reference content moved to Process Navigator. Do not present Process Explorer as the current strategic content product.</p>

    <h2 id="integration">12. Integration model</h2>

    <p>There is no single “Signavio integration”. Different products integrate for different reasons.</p>

    <table class="study-table">
      <thead>
        <tr><th>Integration</th><th>Use</th><th>Key boundary</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Process Modeler API</td>
          <td>Read or maintain models, Dictionary objects, and related content programmatically.</td>
          <td>Use a dedicated API Edition technical user and least-privilege access.</td>
        </tr>
        <tr>
          <td>Process Intelligence data integration</td>
          <td>Bring operational data from ERP, CRM, and other systems into process analysis.</td>
          <td>Technical connectivity is not enough; process semantics must be correct.</td>
        </tr>
        <tr>
          <td>Process Governance connectors / Trigger API</td>
          <td>Start workflows, exchange data, and call supported external activities.</td>
          <td>Governance remains the workflow execution owner.</td>
        </tr>
        <tr>
          <td>Business Process Model Connector</td>
          <td>Align process structure between Signavio and SAP Solution Manager.</td>
          <td>System-of-record and synchronization direction must be explicit.</td>
        </tr>
      </tbody>
    </table>

    <h3>API technical-user rule</h3>

    <p>SAP recommends <strong>one API technical user per integration scenario or integration system</strong>. API Edition is provided at no additional cost and technical users with this license do not use the normal UI.</p>

    <h3>Business Process Model Connector</h3>

    <p>The connector is a stand-alone SAP BTP application between Process Modeler and SAP Solution Manager.</p>

    <p>Think about ownership this way:</p>

    <ul>
      <li><strong>Signavio</strong> — process structure and business artifacts.</li>
      <li><strong>Solution Manager</strong> — solution design and IT lifecycle artifacts.</li>
    </ul>

    <p>If process information already exists in Solution Manager, an initial synchronization can move it into Signavio. After this alignment, Signavio becomes the leading system for process information and ongoing process updates are synchronized toward Solution Manager.</p>

    <p>The learning material also states that BPMN diagrams synchronized from Solution Manager to Signavio are not a simple symmetric round trip back.</p>

    <p>A Synchronization Project defines the system pair, Solution/Branch, Dictionary mappings, attribute mappings, optional governance revision state, direction, and scope.</p>

    <h2 id="admin">13. Administration: the boundaries that matter</h2>

    <h3>Identity and user management</h3>

    <p>Current SAP Signavio identity management has changed. Workspaces created after November 25, 2025 have SAP Cloud Identity Services SSO enabled automatically. For workspaces created after May 6, 2026, users and groups are created and managed through SAP Cloud Identity Services.</p>

    <p>This means older learning material that shows only local Signavio user/group administration is tenant-dependent, not a universal current-state design.</p>

    <h3>Four access layers</h3>

    <table class="study-table">
      <thead>
        <tr><th>Layer</th><th>Question</th></tr>
      </thead>
      <tbody>
        <tr><td>License</td><td>Can this user access the product?</td></tr>
        <tr><td>Feature set</td><td>Which product capabilities are enabled?</td></tr>
        <tr><td>Object access</td><td>Which folders, models, workflows, initiatives, or other objects can the user access?</td></tr>
        <tr><td>Data access</td><td>Which process data or analysis scope can the user see?</td></tr>
      </tbody>
    </table>

    <p>Never use “the user has a license” as proof that the authorization design is correct.</p>

    <h3>Process Modeler access design</h3>

    <p>Use groups based on stable organizational roles and design the folder structure with access rights in mind. Apply least privilege. In the traditional Process Modeler permission model, access granted through one group is additive; a second group with less access does not remove the stronger permission.</p>

    <h3>Administrator controls worth knowing</h3>

    <ul>
      <li>Languages and default language.</li>
      <li>Modeling conventions and notation subsets.</li>
      <li>Custom attributes and attribute overlays.</li>
      <li>Dictionary categories and sandbox governance.</li>
      <li>Audiences and Hub presentation.</li>
      <li>SSO, identity provisioning, IP filtering, and security policy.</li>
      <li>Product licenses, feature sets, and access reviews.</li>
    </ul>

    <h2 id="best-practices">14. Best practices that create real value</h2>

    <table class="study-table">
      <thead>
        <tr><th>Practice</th><th>Reason</th></tr>
      </thead>
      <tbody>
        <tr><td>Define process levels and ownership before mass modeling.</td><td>Prevents a repository full of unrelated diagrams.</td></tr>
        <tr><td>Use the Dictionary for shared business objects.</td><td>Creates one vocabulary and traceability.</td></tr>
        <tr><td>Use roles, not named people, in process responsibility.</td><td>Reduces maintenance and keeps the model stable.</td></tr>
        <tr><td>Use DMN for complex rule logic.</td><td>Keeps BPMN readable and makes decisions testable.</td></tr>
        <tr><td>Use Call Activities for reusable process logic.</td><td>Avoids copying the same process into many models.</td></tr>
        <tr><td>Use conventions plus human review.</td><td>Syntax correctness does not prove business correctness.</td></tr>
        <tr><td>Use variants for justified local differences.</td><td>Balances global standardization with local requirements.</td></tr>
        <tr><td>Use simulation for hypotheses and mining for evidence.</td><td>Separates designed assumptions from real execution.</td></tr>
        <tr><td>Connect journey pain points to internal processes and KPIs.</td><td>Turns CX work into operational improvement.</td></tr>
        <tr><td>Turn findings into owned initiatives.</td><td>Analysis without ownership does not create transformation.</td></tr>
        <tr><td>Separate licenses, permissions, feature sets, and data access.</td><td>Avoids weak security and false assumptions about entitlements.</td></tr>
        <tr><td>Use dedicated technical users and explicit systems of record.</td><td>Makes integrations supportable and ownership clear.</td></tr>
      </tbody>
    </table>

    <h2 id="interview">15. How to explain SAP Signavio in an interview</h2>

    <h3>60-second answer</h3>

    <p>SAP Signavio is a process transformation suite. I would not treat it as one modeling tool. Process Modeler defines how the process should work and keeps the process architecture and business vocabulary consistent. Collaboration Hub publishes this knowledge to business users. Journey Modeler adds the outside-in customer or employee perspective. Process Governance executes approval and governance workflows. Process Intelligence analyzes operational data to show what actually happened. Process Transformation Manager converts findings into owned improvement initiatives. The main design principle is to connect these layers without mixing their responsibilities: model versus execution data, process versus journey, governance workflow versus transformation initiative, and license versus authorization.</p>

    <h3>Five questions before recommending a component</h3>

    <ol>
      <li>Are we trying to <strong>design</strong> the process or understand <strong>actual execution</strong>?</li>
      <li>Is the problem about the internal process or the outside-in experience?</li>
      <li>Do we need documentation and collaboration, or an executable workflow?</li>
      <li>Do we need a finding, or do we need to manage the improvement initiative?</li>
      <li>What is the source of truth, and what license and access model is required?</li>
    </ol>

    <h2 id="current-state">16. Current-state notes for 2026</h2>

    <ul>
      <li><strong>Process Modeler</strong> is the current modeling product name; Process Manager remains common in older material.</li>
      <li><strong>Process Explorer retired on June 30, 2026.</strong> Use Process Navigator for SAP reference process content.</li>
      <li>For new workspaces, identity management is moving through <strong>SAP Cloud Identity Services</strong>; workspaces created after May 6, 2026 manage users and groups there.</li>
      <li><strong>Process Intelligence</strong> is licensed at workspace level; feature sets and data permissions control user access.</li>
      <li><strong>Process Insights capabilities</strong> are available in Process Intelligence in current SAP documentation.</li>
      <li>New Process Intelligence <strong>investigations</strong> cannot be created or imported since May 26, 2026; customizable dashboards are the current direction.</li>
      <li>AI features and commercial consumption rules change faster than core modeling concepts. Verify the exact feature before promising scope.</li>
    </ul>

    <h2 id="glossary">17. Glossary</h2>

    <table class="study-table">
      <thead>
        <tr><th>Term</th><th>Meaning</th></tr>
      </thead>
      <tbody>
        <tr><td>Process Modeler</td><td>SAP Signavio product for designing and governing process and decision models. Older content often says Process Manager.</td></tr>
        <tr><td>Explorer / Repository</td><td>Area used to organize, find, manage, and govern process content.</td></tr>
        <tr><td>Graphical Editor</td><td>Detailed modeling environment.</td></tr>
        <tr><td>QuickModel</td><td>Spreadsheet-like tool for fast simple BPMN capture.</td></tr>
        <tr><td>BPMN</td><td>Business Process Model and Notation; standard notation for process flow.</td></tr>
        <tr><td>DMN</td><td>Decision Model and Notation; standard for decision requirements and decision logic.</td></tr>
        <tr><td>DRD</td><td>Decision Requirements Diagram; shows decision dependencies and required inputs or knowledge.</td></tr>
        <tr><td>Decision Table</td><td>Business rules that map input conditions to outputs.</td></tr>
        <tr><td>Hit Policy</td><td>Rule for how a DMN table handles matching rows.</td></tr>
        <tr><td>Dictionary</td><td>Central repository of reusable business objects.</td></tr>
        <tr><td>Dictionary Entry</td><td>One governed reusable object such as a role, system, document, risk, or control.</td></tr>
        <tr><td>Attribute</td><td>Structured metadata on a diagram, element, or Dictionary entry.</td></tr>
        <tr><td>Modeling Convention</td><td>Organization-specific rule for modeling quality and consistency.</td></tr>
        <tr><td>Navigation Map</td><td>Flexible visual entry point into the process landscape.</td></tr>
        <tr><td>Value Chain</td><td>High-level structured process architecture.</td></tr>
        <tr><td>Token</td><td>Mental model used to understand BPMN execution behavior.</td></tr>
        <tr><td>Call Activity</td><td>BPMN element that calls reusable global process logic.</td></tr>
        <tr><td>Process Collaboration Hub</td><td>Business-facing layer for published process content and collaboration.</td></tr>
        <tr><td>Audience</td><td>Viewer group used to tailor Hub presentation; it is not the same as authorization.</td></tr>
        <tr><td>Read Confirmation</td><td>Request for acknowledgement that process content was read.</td></tr>
        <tr><td>Process Rating</td><td>Structured feedback on a process revision.</td></tr>
        <tr><td>Variant</td><td>Controlled local variation of a common process template.</td></tr>
        <tr><td>Variant Group</td><td>A process template together with its variants and dimensions.</td></tr>
        <tr><td>Simulation</td><td>What-if analysis using modeled assumptions such as time, cost, volume, probability, and resources.</td></tr>
        <tr><td>Journey Modeler</td><td>Outside-in modeling product for journeys, touchpoints, sentiments, processes, systems, and metrics.</td></tr>
        <tr><td>Persona</td><td>Representative person whose journey is modeled.</td></tr>
        <tr><td>Touchpoint</td><td>Interaction between a person and the company, product, partner, or channel.</td></tr>
        <tr><td>Journey Complexity</td><td>Operational complexity behind the processes linked to a journey.</td></tr>
        <tr><td>Journey Model Dimensions</td><td>Size and populated content of the journey table.</td></tr>
        <tr><td>Process Governance</td><td>Workflow modeling and execution product for governed work.</td></tr>
        <tr><td>Workflow</td><td>Reusable template for executable work.</td></tr>
        <tr><td>Case</td><td>One running instance of a workflow.</td></tr>
        <tr><td>User Task</td><td>Workflow task completed by one person or role.</td></tr>
        <tr><td>Multi-User Task</td><td>Same workflow task created for several participants.</td></tr>
        <tr><td>Process Intelligence</td><td>Data-driven process analysis and process-mining product.</td></tr>
        <tr><td>Process Insights</td><td>Predefined SAP-focused process performance content and recommendations now available through the Process Intelligence direction.</td></tr>
        <tr><td>Insight</td><td>Saved analytical finding or improvement observation.</td></tr>
        <tr><td>Analysis Workflow</td><td>Process Intelligence automation that monitors process data and acts on defined conditions.</td></tr>
        <tr><td>Process Transformation Manager</td><td>Product for insights, initiatives, objectives, tasks, benchmarking, assets, and value-oriented improvement management.</td></tr>
        <tr><td>Process Navigator</td><td>SAP for Me service for SAP reference process and implementation content.</td></tr>
        <tr><td>Value Accelerator</td><td>Optional reusable content used to accelerate modeling, analysis, or transformation work.</td></tr>
        <tr><td>Feature Set</td><td>Authorization mechanism used to enable product capabilities for a group.</td></tr>
        <tr><td>API Edition</td><td>Technical-user license for Process Modeler API integrations.</td></tr>
        <tr><td>Business Process Model Connector</td><td>SAP BTP application for controlled synchronization between Signavio and SAP Solution Manager.</td></tr>
        <tr><td>Synchronization Project</td><td>Connector configuration for a system pair, mappings, scope, and synchronization rules.</td></tr>
      </tbody>
    </table>

    <h2 id="sources">18. Source register</h2>

    <ul>
      <li><a href="https://help.sap.com/docs/signavio-process-transformation-suite">SAP Signavio Process Transformation Suite — product documentation</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-intelligence/user-guide/navigating-sap-signavio-process-transformation-suite">Navigating SAP Signavio Process Transformation Suite</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-modeler/workspace-admin-guide/about-licenses">Process Modeler — License Assignment</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-transformation-suite/user-management-authentication-and-authorization/harmonization-of-authentication-and-identity-management">SAP Signavio — Identity-management harmonization</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-modeler/security-guide/single-sign-on-using-saml">SAP Signavio — SAML license names</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-manager/sap-signavio-process-manager-api/user-access-and-licensing">Process Modeler API — Access and Licensing</a></li>
      <li><a href="https://help.sap.com/docs/signavio-journey-modeler/user-guide/intro">Journey Modeler — User Guide</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-governance/user-guide/intro">Process Governance — Fundamentals</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-governance/fsd-collaborator/sap-signavio-process-governance-collaborator">Process Governance Collaborator — Feature Scope Description</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-intelligence/user-guide/57542d3a6dab10148cfcc70dfc2ca89e.html">Process Intelligence — User Guide</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-intelligence/user-guide/about-investigations">Process Intelligence — Investigations transition</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-insights/administration-guide/source-systems-supported">Process Insights capabilities in Process Intelligence</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-transformation-manager">Process Transformation Manager — User Guide</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-manager/user-guide/value-accelerator-library-for-sap-signavio-solutions">Value Accelerator Library</a></li>
      <li><a href="https://help.sap.com/docs/cloud-alm/getting-started-process-navigator/accessing-details-of-solution-process">SAP Signavio Process Navigator</a></li>
      <li><a href="https://community.sap.com/t5/technology-blog-posts-by-sap/sap-signavio-process-explorer-sunsetting-on-june-30-2026/ba-p/14417041">SAP Signavio Process Explorer retirement</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-transformation-suite/business-process-model-connector/business-process-model-connector-for-sap-signavio-solutions">Business Process Model Connector</a></li>
      <li><a href="https://www.omg.org/spec/BPMN/2.0.2/PDF">OMG BPMN 2.0.2 specification</a></li>
    </ul>

    <p><strong>Verification boundary:</strong> this guide combines SAP Learning material used for assessment preparation with current public SAP documentation. Product names, commercial packages, AI consumption rules, regional availability, and feature scope can change. Verify the customer's current contract and SAP Feature Scope Description before making a commercial or implementation commitment.</p>

  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/labs/assessment/">SAP Lead Assessment Lab</a></li>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-build/">SAP Build</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
