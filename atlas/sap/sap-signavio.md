---
layout: default
signavio_reader: true
hide_global_cta: true
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
last_modified_at: 2026-10-08
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

<article class="research-canvas signavio-reader" aria-label="SAP Signavio Product Guide">
  <header class="research-canvas__hero signavio-reader__hero">
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Knowledge Atlas / SAP Lead</p>
      <h1>SAP Signavio</h1>
      <p>Understand what each product does, why the business needs it, and how to explain the full suite to a client or interviewer.</p>
      <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
      <a class="research-canvas__button" href="#reading-map">Choose a topic <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <aside class="research-canvas__signal" aria-label="Learning outcomes">
      <p>After reading, you can</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Explain business value</strong></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Choose the right component</strong></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Explain boundaries and trade-offs</strong></div>
      <em>One practical reference for product knowledge, SAP Lead assessment, and client discussions.</em>
    </aside>
  </header>

  <aside class="research-canvas__boundary" aria-label="How to use this guide">
    <span class="material-symbols-outlined" aria-hidden="true">menu_book</span>
    <p><strong>Reading path:</strong> Start with the product map and business questions, then use the component chapters as reference. Finish with the interview answer and glossary.</p>
  </aside>

  <nav class="research-canvas__inventory signavio-reader__toc" id="reading-map" aria-label="Chapters in this guide">
    <header>
      <p class="research-canvas__eyebrow">On this page</p>
      <h2>Choose what you need to understand.</h2>
      <p>Read in order for the full picture, or jump directly to the product, business question, or exam topic.</p>
    </header>
    <div class="signavio-reader__toc-grid">
    <section class="signavio-reader__toc-group" aria-labelledby="signavio-route-0">
      <h3 id="signavio-route-0">Understand the suite</h3>
      <ol>
        <li><a href="#start">Start with one picture</a></li>
        <li><a href="#client-map">Client question → Signavio component</a></li>
        <li><a href="#business">How to explain SAP Signavio to business</a></li>
        <li><a href="#example">One simple example across the suite</a></li>
      </ol>
    </section>
    <section class="signavio-reader__toc-group" aria-labelledby="signavio-route-1">
      <h3 id="signavio-route-1">Choose the products</h3>
      <ol>
        <li><a href="#licensing">Licensing and access boundaries</a></li>
        <li><a href="#modeler">Process Modeler: what you must understand</a></li>
        <li><a href="#bpmn-dmn">BPMN and DMN: the minimum Lead toolkit</a></li>
        <li><a href="#collaboration-governance">Collaboration Hub and Process Governance</a></li>
        <li><a href="#journey">Journey Modeler: outside-in view</a></li>
        <li><a href="#intelligence">Process Intelligence and Process Insights</a></li>
        <li><a href="#transformation">Process Transformation Manager</a></li>
      </ol>
    </section>
    <section class="signavio-reader__toc-group" aria-labelledby="signavio-route-2">
      <h3 id="signavio-route-2">Apply it</h3>
      <ol>
        <li><a href="#reference-content">Reference content: Process Navigator and Value Accelerator Library</a></li>
        <li><a href="#integration">Integration model</a></li>
        <li><a href="#admin">Administration: the boundaries that matter</a></li>
        <li><a href="#best-practices">Best practices that create real value</a></li>
      </ol>
    </section>
    <section class="signavio-reader__toc-group" aria-labelledby="signavio-route-3">
      <h3 id="signavio-route-3">Prepare and verify</h3>
      <ol>
        <li><a href="#interview">How to explain SAP Signavio in an interview</a></li>
        <li><a href="#current-state">Current-state notes for 2026</a></li>
        <li><a href="#sources">Source register</a></li>
        <li><a href="#glossary">Glossary</a></li>
      </ol>
    </section>
    </div>
  </nav>

  <section class="research-canvas__inventory signavio-reader__section" id="start" aria-labelledby="start-title">
    <header class="signavio-reader__section-head">
      <p class="research-canvas__eyebrow">01 / Product map</p>
      <h2 id="start-title">Start with one picture</h2>
    </header>
    <div class="signavio-reader__content">
<p>SAP Signavio is a process transformation suite. It connects process design, business collaboration, customer or employee journeys, workflow governance, operational process data, and improvement initiatives.</p>

    <p>The simplest mental model is:</p>

    <p><strong>Reference → Model → Collaborate → Govern → Observe → Improve → Model again</strong></p>

    <div class="table-scroll study-table" role="region" aria-label="Start with one picture — reference table" tabindex="0">
<table class="study-table__table">
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
</div>

    <p><strong>The key Lead skill is product selection.</strong> Do not answer every question with “Signavio”. Name the problem first, then the component that owns it.</p>

    <h3>AI is a cross-suite capability</h3>

    <p>AI is not a replacement for the product model above. It assists specific jobs inside the suite. For example, AI-assisted Process Modeler can create a BPMN starting point from text or an image, while AI-assisted Process Analyzer can help users work with process metrics, attributes, insights, and dashboard widgets using natural language.</p>

    <p>The Lead boundary stays the same: AI can accelerate modeling or analysis, but the team still owns process semantics, business rules, data quality, governance, and approval. Licensing and AI consumption rules are feature-specific.</p>

    <h3>Current naming you should know</h3>

    <p><strong>Process Modeler</strong> is the current product name. Older SAP Learning content and customer environments can still use <strong>Process Manager</strong>. Treat them as the same modeling product generation, not as two different products.</p>

    <p><strong>Process Explorer is no longer the current reference-content product.</strong> SAP retired SAP Signavio Process Explorer on June 30, 2026 and moved its reference content to <strong>SAP Signavio Process Navigator</strong>. Process Navigator is now the reference point for SAP process content through SAP for Me. The Value Accelerator Library remains available for accelerator content inside the Signavio suite.</p>
    </div>
  </section>

  <section class="research-canvas__inventory signavio-reader__section" id="client-map" aria-labelledby="client-map-title">
    <header class="signavio-reader__section-head">
      <p class="research-canvas__eyebrow">02 / Client questions</p>
      <h2 id="client-map-title">Client question → Signavio component</h2>
    </header>
    <div class="signavio-reader__content">
<div class="table-scroll study-table" role="region" aria-label="Client question → Signavio component — reference table" tabindex="0">
<table class="study-table__table">
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
</div>
    </div>
  </section>

  <section class="research-canvas__inventory signavio-reader__section" id="business" aria-labelledby="business-title">
    <header class="signavio-reader__section-head">
      <p class="research-canvas__eyebrow">03 / Business value</p>
      <h2 id="business-title">How to explain SAP Signavio to business</h2>
    </header>
    <div class="signavio-reader__content">
<p>Do not start a business conversation with BPMN, process mining, or product names. Start with the problem the business is trying to solve.</p>

    <p>In business language, SAP Signavio helps an organization do four things:</p>

    <ol>
      <li><strong>Make the process visible.</strong> Agree how work should happen, who owns it, and which systems and documents are involved.</li>
      <li><strong>Make the process consistent.</strong> Standardize terminology, responsibilities, process variants, and governance without removing justified local differences.</li>
      <li><strong>Measure the real process.</strong> Use operational data to see delays, rework, variants, bottlenecks, and value opportunities.</li>
      <li><strong>Turn findings into change.</strong> Give improvements owners, objectives, tasks, approvals, and measurable outcomes.</li>
    </ol>

    <h3>Business problem → business explanation</h3>

    <div class="table-scroll study-table" role="region" aria-label="Business problem → business explanation — reference table" tabindex="0">
<table class="study-table__table">
      <thead>
        <tr>
          <th>Business problem</th>
          <th>How to explain the Signavio answer</th>
          <th>Business value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Different teams describe the same process differently.</td>
          <td>Create one governed process architecture, common terms, owners, and controlled variants.</td>
          <td>Less ambiguity, easier onboarding, clearer ownership.</td>
        </tr>
        <tr>
          <td>People do not know which process is current.</td>
          <td>Publish approved process knowledge in one collaboration layer instead of distributing uncontrolled files.</td>
          <td>One trusted source for process consumers.</td>
        </tr>
        <tr>
          <td>Approvals and reviews happen in e-mail and spreadsheets.</td>
          <td>Run repeatable governance workflows with assigned tasks, reminders, decisions, and history.</td>
          <td>Traceable governance and fewer missed steps.</td>
        </tr>
        <tr>
          <td>The designed process looks good, but performance is poor.</td>
          <td>Connect operational data and compare the intended process with actual execution.</td>
          <td>Fact-based improvement instead of opinion-based discussion.</td>
        </tr>
        <tr>
          <td>Internal KPIs look fine, but customers or employees struggle.</td>
          <td>Model the outside-in journey and connect pain points to the processes and systems that create them.</td>
          <td>Improvement based on experience, not only internal efficiency.</td>
        </tr>
        <tr>
          <td>There are many improvement ideas but no clear priority.</td>
          <td>Convert findings into initiatives with objectives, value, owners, tasks, and progress.</td>
          <td>Better prioritization and execution of transformation work.</td>
        </tr>
      </tbody>
    </table>
</div>

    <h3>What SAP Signavio does not replace</h3>

    <ul>
      <li><strong>It does not replace SAP S/4HANA or another transactional system.</strong> A sales order, goods movement, invoice, or production confirmation still executes in the operational system.</li>
      <li><strong>It does not make a process correct because the BPMN syntax is correct.</strong> Business owners and subject-matter experts still validate the meaning.</li>
      <li><strong>It does not improve a process automatically.</strong> Analysis creates evidence; people still choose, own, implement, and verify the change.</li>
      <li><strong>It does not remove data and integration responsibility.</strong> Process mining is only useful when the case, events, timestamps, attributes, and metrics represent the business correctly.</li>
      <li><strong>It does not remove governance.</strong> A large repository without ownership, standards, lifecycle rules, and access design becomes another source of confusion.</li>
    </ul>

    <h3>What the business must own</h3>

    <div class="table-scroll study-table" role="region" aria-label="What the business must own — reference table" tabindex="0">
<table class="study-table__table">
      <thead>
        <tr>
          <th>Role</th>
          <th>Business responsibility</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Executive sponsor</td>
          <td>Set transformation direction and remove cross-functional blockers.</td>
        </tr>
        <tr>
          <td>Process owner</td>
          <td>Own the end-to-end process outcome, standards, and improvement decisions.</td>
        </tr>
        <tr>
          <td>Process architect / BPM team</td>
          <td>Maintain process architecture, modeling standards, Dictionary design, and governance approach.</td>
        </tr>
        <tr>
          <td>Subject-matter expert</td>
          <td>Validate that the model and business rules reflect real work.</td>
        </tr>
        <tr>
          <td>Process / data analyst</td>
          <td>Define correct process semantics, metrics, analysis scope, and evidence.</td>
        </tr>
        <tr>
          <td>Improvement owner</td>
          <td>Turn an insight into implemented change and prove the result.</td>
        </tr>
      </tbody>
    </table>
</div>

    <h3>A simple client conversation</h3>

    <p><strong>1. What is the business problem?</strong> Standardization, transparency, compliance, customer experience, performance, or transformation execution?</p>

    <p><strong>2. What evidence do we have?</strong> Process models, stakeholder feedback, operational data, customer journey data, or only assumptions?</p>

    <p><strong>3. Which Signavio capability owns the next step?</strong> Model, collaborate, govern, analyze, or manage the improvement?</p>

    <p><strong>4. Who owns the outcome?</strong> A Signavio tool can support the work, but a business owner must own the decision and measurable result.</p>

    <h3>30-second business explanation</h3>

    <p>SAP Signavio gives the business one connected way to understand and improve processes. We can define how a process should work, publish it to the people who use it, run approvals and governance, understand the customer or employee experience, analyze operational data to see what really happens, and turn the findings into improvement initiatives. The value is not the diagram itself. The value is a common process language, clear ownership, evidence-based improvement, and traceable change.</p>

    <h3>A sensible adoption path</h3>

    <ol>
      <li><strong>Pick an end-to-end process and business outcome.</strong> Do not start with a tool rollout. Start with a real problem such as order delay, procurement cycle time, compliance, or customer friction.</li>
      <li><strong>Name the process owner and governance model.</strong> Decide who owns the process, standards, approvals, and improvement decisions.</li>
      <li><strong>Build the common process language.</strong> Define levels, Dictionary objects, modeling conventions, and controlled variants.</li>
      <li><strong>Publish and involve the business.</strong> Make process knowledge easy to consume and collect feedback from the people who execute the work.</li>
      <li><strong>Add operational evidence.</strong> Connect process data when the organization is ready to compare the designed process with real execution.</li>
      <li><strong>Prioritize and prove improvements.</strong> Assign initiatives, implement changes, and measure whether business outcomes improved.</li>
    </ol>

    <p>Process Governance can be introduced where formal approvals, controls, or recurring governance tasks need executable workflows. It is not a mandatory first step for every Signavio adoption.</p>
    </div>
  </section>

  <section class="research-canvas__inventory signavio-reader__section" id="example" aria-labelledby="example-title">
    <header class="signavio-reader__section-head">
      <p class="research-canvas__eyebrow">04 / Working example</p>
      <h2 id="example-title">One simple example across the suite</h2>
    </header>
    <div class="signavio-reader__content">
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
    </div>
  </section>

  <section class="research-canvas__inventory signavio-reader__section" id="licensing" aria-labelledby="licensing-title">
    <header class="signavio-reader__section-head">
      <p class="research-canvas__eyebrow">05 / Licensing</p>
      <h2 id="licensing-title">Licensing and access boundaries</h2>
    </header>
    <div class="signavio-reader__content">
<p>Do not memorize commercial prices. Understand the boundaries. SAP contracts, packages, and feature scope can change.</p>

    <div class="table-scroll study-table" role="region" aria-label="Licensing and access boundaries — reference table" tabindex="0">
<table class="study-table__table">
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
</div>

    <p><strong>License ≠ authorization.</strong> A license gives access to a product. Groups, object permissions, feature sets, and data permissions decide what the user can actually do.</p>
    </div>
  </section>

  <section class="research-canvas__inventory signavio-reader__section" id="modeler" aria-labelledby="modeler-title">
    <header class="signavio-reader__section-head">
      <p class="research-canvas__eyebrow">06 / Modeling</p>
      <h2 id="modeler-title">Process Modeler: what you must understand</h2>
    </header>
    <div class="signavio-reader__content">
<h3>The four building blocks</h3>

    <div class="table-scroll study-table" role="region" aria-label="The four building blocks — reference table" tabindex="0">
<table class="study-table__table">
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
</div>

    <h3>Architecture before diagrams</h3>

    <p>A strong workspace has levels. A simple pattern is:</p>

    <p><strong>Navigation Map → Value Chain → BPMN process → subprocesses → Dictionary objects</strong></p>

    <p>A <strong>Navigation Map</strong> is a flexible entry point. A <strong>Value Chain</strong> is a structured high-level process architecture. BPMN then gives the detailed flow.</p>

    <h3>Dictionary is the shared vocabulary</h3>

    <p>Create a role, system, document, risk, or control once and reuse it. This gives consistent naming and traceability across models.</p>

    <p>A central Dictionary change can affect many linked models. A local diagram attribute can remain local. That is a governance decision, not only an editing choice.</p>

    <p><strong>Best practice:</strong> use sandbox categories for proposed Dictionary entries and a small responsible group to review, merge, and promote them.</p>

    <h3>Syntax vs convention vs business correctness</h3>

    <div class="table-scroll study-table" role="region" aria-label="Syntax vs convention vs business correctness — reference table" tabindex="0">
<table class="study-table__table">
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
</div>

    <p>The tool can help with syntax and configured conventions. Subject-matter experts are still needed for semantic correctness.</p>

    <h3>Choose the right model type</h3>

    <div class="table-scroll study-table" role="region" aria-label="Choose the right model type — reference table" tabindex="0">
<table class="study-table__table">
      <thead>
        <tr><th>Need</th><th>Model</th></tr>
      </thead>
      <tbody>
        <tr><td>Detailed business process flow</td><td>BPMN</td></tr>
        <tr><td>Decision logic</td><td>DMN</td></tr>
        <tr><td>Enterprise architecture view</td><td>ArchiMate</td></tr>
        <tr><td>High-level process architecture</td><td>Value Chain</td></tr>
        <tr><td>Flexible entry point into process content</td><td>Navigation Map</td></tr>
        <tr><td>Outside-in stakeholder experience</td><td>Journey Model / Customer Journey Map</td></tr>
      </tbody>
    </table>
</div>

    <h3>Simulation = test a hypothesis</h3>

    <p>Process Modeler can simulate BPMN behavior using four main parameter groups: <strong>Costs, Duration, Frequency, and Resources</strong>. Use it to test questions such as “Can we handle 40% more orders?” or “What happens if shipping becomes faster?”</p>

    <p>Remember the boundary: activity execution time is not always total cycle time. Waiting and resource queues can dominate the result.</p>

    <h3>Reporting = analyze what is modeled</h3>

    <p>Model-based reports can aggregate costs, resource consumption, RACI responsibilities, handovers, IT-system usage, documents, modeling conventions, model metrics, risks and controls, and process documentation.</p>

    <p>Reporting answers <strong>what is in the model and its metadata</strong>. Process Intelligence answers <strong>what happened in operational execution</strong>.</p>

    <h3>Variant Management = standard core with controlled differences</h3>

    <p>Use variants when one global process needs justified regional, organizational, product, or customer-specific differences.</p>

    <p><strong>Template → Dimensions → Dimension values → Variant Group → Variants</strong></p>

    <ul>
      <li><strong>Attach</strong> an existing process as a variant.</li>
      <li><strong>Clone</strong> the template to create a new variant.</li>
      <li><strong>Detach</strong> when the local process must evolve independently.</li>
      <li><strong>Propagate</strong> supported template changes to variants and review changes that require manual work.</li>
    </ul>

    <p>The goal is not to eliminate all variation. The goal is to make variation explicit, justified, and governable.</p>
    </div>
  </section>

  <section class="research-canvas__inventory signavio-reader__section" id="bpmn-dmn" aria-labelledby="bpmn-dmn-title">
    <header class="signavio-reader__section-head">
      <p class="research-canvas__eyebrow">07 / Notation</p>
      <h2 id="bpmn-dmn-title">BPMN and DMN: the minimum Lead toolkit</h2>
    </header>
    <div class="signavio-reader__content">
<h3>BPMN</h3>

    <p>Use BPMN to explain <strong>what happens, in what order, and who is responsible</strong>.</p>

    <div class="table-scroll study-table" role="region" aria-label="BPMN — reference table" tabindex="0">
<table class="study-table__table">
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
</div>

    <p><strong>A gateway is not the decision.</strong> The decision is made in business logic or a task; the gateway routes the result.</p>

    <p>Use the <strong>token concept</strong> to understand execution behavior. It makes deadlocks, parallel paths, waiting, and duplicate execution easier to reason about.</p>

    <h3>Subprocess choice</h3>

    <div class="table-scroll study-table" role="region" aria-label="Subprocess choice — reference table" tabindex="0">
<table class="study-table__table">
      <thead>
        <tr><th>Pattern</th><th>Use</th></tr>
      </thead>
      <tbody>
        <tr><td>Collapsed subprocess</td><td>Hide detail and keep the parent process readable.</td></tr>
        <tr><td>Call Activity</td><td>Reuse the same global process logic in several parent processes.</td></tr>
        <tr><td>Expanded subprocess</td><td>Show local grouped detail inside one process.</td></tr>
      </tbody>
    </table>
</div>

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

    <div class="table-scroll study-table" role="region" aria-label="Hit policies — reference table" tabindex="0">
<table class="study-table__table">
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
</div>

    <p><strong>Verify</strong> checks formal completeness and consistency. <strong>Simulation</strong> evaluates outputs for selected inputs. <strong>Test Lab</strong> checks expected outcomes and regression cases after rule changes.</p>
    </div>
  </section>

  <section class="research-canvas__inventory signavio-reader__section" id="collaboration-governance" aria-labelledby="collaboration-governance-title">
    <header class="signavio-reader__section-head">
      <p class="research-canvas__eyebrow">08 / Collaboration</p>
      <h2 id="collaboration-governance-title">Collaboration Hub and Process Governance</h2>
    </header>
    <div class="signavio-reader__content">
<h3>Collaboration Hub = consume and collaborate</h3>

    <p>The Hub is the business-facing layer for published process content. It supports navigation, comments, feedback, reporting, read confirmations, ratings, and audience-specific presentation.</p>

    <p><strong>Audience is not authorization.</strong> An audience changes the presentation for a viewer group. Access rights decide whether a user may see or change content.</p>

    <div class="table-scroll study-table" role="region" aria-label="Collaboration Hub = consume and collaborate — reference table" tabindex="0">
<table class="study-table__table">
      <thead>
        <tr><th>Feature</th><th>Purpose</th></tr>
      </thead>
      <tbody>
        <tr><td>Comment</td><td>Discuss model content with stakeholders.</td></tr>
        <tr><td>Read Confirmation</td><td>Ask users to confirm that they read a process or new revision.</td></tr>
        <tr><td>Process Rating</td><td>Collect structured feedback about a process revision.</td></tr>
      </tbody>
    </table>
</div>

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

    <div class="table-scroll study-table" role="region" aria-label="Workflow versions — reference table" tabindex="0">
<table class="study-table__table">
      <thead>
        <tr><th>Action</th><th>Meaning</th></tr>
      </thead>
      <tbody>
        <tr><td>Publish</td><td>Create an executable version for new cases.</td></tr>
        <tr><td>Re-Publish</td><td>Make a copy of an older version the version used by new cases.</td></tr>
        <tr><td>Restore</td><td>Bring an older version back into the editable draft without changing the current published execution version.</td></tr>
      </tbody>
    </table>
</div>
    </div>
  </section>

  <section class="research-canvas__inventory signavio-reader__section" id="journey" aria-labelledby="journey-title">
    <header class="signavio-reader__section-head">
      <p class="research-canvas__eyebrow">09 / Journey</p>
      <h2 id="journey-title">Journey Modeler: outside-in view</h2>
    </header>
    <div class="signavio-reader__content">
<p>A process is usually inside-out: what the company does. A journey is outside-in: what the person experiences.</p>

    <p>Use Journey Modeler for customers, employees, applicants, suppliers, partners, or other people interacting with the organization.</p>

    <p>The basic structure is:</p>

    <p><strong>Persona → Stages → Steps → Touchpoints → Sentiment → Linked process/system/KPI</strong></p>

    <p>A <strong>step</strong> is something the person goes through. A <strong>touchpoint</strong> is an interaction with the company, product, partner, or channel.</p>

    <h3>Journey Modeler vs Customer Journey Map</h3>

    <div class="table-scroll study-table" role="region" aria-label="Journey Modeler vs Customer Journey Map — reference table" tabindex="0">
<table class="study-table__table">
      <thead>
        <tr><th>Approach</th><th>Use</th></tr>
      </thead>
      <tbody>
        <tr><td>Journey Modeler</td><td>Table-based holistic view with journey information, processes, systems, organizations, sentiment, metrics, and data widgets.</td></tr>
        <tr><td>Customer Journey Map</td><td>Visual storytelling of the persona's journey and touchpoints, with details available through attributes and links.</td></tr>
      </tbody>
    </table>
</div>

    <p><strong>Journey Complexity</strong> estimates operational complexity behind linked processes. <strong>Journey Model Dimensions</strong> describe the size and populated content of the journey table. They are different metrics.</p>

    <p>The valuable pattern is:</p>

    <p><strong>Pain point → linked internal process → process change → KPI → verify experience improvement</strong></p>
    </div>
  </section>

  <section class="research-canvas__inventory signavio-reader__section" id="intelligence" aria-labelledby="intelligence-title">
    <header class="signavio-reader__section-head">
      <p class="research-canvas__eyebrow">10 / Process mining</p>
      <h2 id="intelligence-title">Process Intelligence and Process Insights</h2>
    </header>
    <div class="signavio-reader__content">
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

    <h3>Out-of-the-box vs custom analysis</h3>

    <div class="table-scroll study-table" role="region" aria-label="Out-of-the-box vs custom analysis — reference table" tabindex="0">
<table class="study-table__table">
      <thead>
        <tr><th>Approach</th><th>Use it when</th><th>Trade-off</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>Out-of-the-box analysis</td>
          <td>The SAP-defined process content and standardized source-system integration fit the business question.</td>
          <td>Faster start and predefined metrics, but less freedom to redefine the process semantics.</td>
        </tr>
        <tr>
          <td>Custom process analysis</td>
          <td>The process, data sources, case definition, attributes, or metrics are customer-specific.</td>
          <td>More flexibility, but the team must design and validate the semantic model and data integration.</td>
        </tr>
      </tbody>
    </table>
</div>

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

    <div class="table-scroll study-table" role="region" aria-label="Simulation vs reporting vs mining — reference table" tabindex="0">
<table class="study-table__table">
      <thead>
        <tr><th>Capability</th><th>Evidence</th><th>Question</th></tr>
      </thead>
      <tbody>
        <tr><td>Simulation</td><td>Assumptions in a designed model</td><td>What could happen?</td></tr>
        <tr><td>Model reporting</td><td>Model elements and attributes</td><td>What did we document?</td></tr>
        <tr><td>Process Intelligence</td><td>Operational process data</td><td>What actually happened?</td></tr>
      </tbody>
    </table>
</div>
    </div>
  </section>

  <section class="research-canvas__inventory signavio-reader__section" id="transformation" aria-labelledby="transformation-title">
    <header class="signavio-reader__section-head">
      <p class="research-canvas__eyebrow">11 / Improvement</p>
      <h2 id="transformation-title">Process Transformation Manager</h2>
    </header>
    <div class="signavio-reader__content">
<p>Process Intelligence can find a problem. Process Transformation Manager helps manage the improvement work that follows.</p>

    <p>A simple flow is:</p>

    <p><strong>Finding → Insight → Initiative → Objective → Tasks → Value / progress</strong></p>

    <div class="table-scroll study-table" role="region" aria-label="Process Transformation Manager — reference table" tabindex="0">
<table class="study-table__table">
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
</div>

    <p>Do not confuse Process Transformation Manager with Process Governance. <strong>Governance executes repeatable workflows. Transformation Manager manages improvement initiatives.</strong></p>
    </div>
  </section>

  <section class="research-canvas__inventory signavio-reader__section" id="reference-content" aria-labelledby="reference-content-title">
    <header class="signavio-reader__section-head">
      <p class="research-canvas__eyebrow">12 / Reference content</p>
      <h2 id="reference-content-title">Reference content: Process Navigator and Value Accelerator Library</h2>
    </header>
    <div class="signavio-reader__content">
<h3>SAP Signavio Process Navigator</h3>

    <p>Process Navigator is SAP's current reference point for SAP process content. It is available through SAP for Me and provides process hierarchies, solution processes, variants, roles, capabilities, documentation, and related implementation content.</p>

    <p>Use it when the client asks: <strong>“What is the SAP standard or reference process?”</strong></p>

    <h3>Value Accelerator Library</h3>

    <p>The Value Accelerator Library is embedded in the Signavio suite and provides installable or reusable accelerator content for supported Signavio products. Accelerators can include process models, metrics, dashboards, maps, templates, and other transformation content.</p>

    <p><strong>Important:</strong> accelerators are starting content, not the customer's final operating model. SAP states that value accelerators are optional and not part of core product business functionality.</p>

    <h3>Legacy term: Process Explorer</h3>

    <p>SAP Signavio Process Explorer was retired on June 30, 2026. Its reference content moved to Process Navigator. Do not present Process Explorer as the current strategic content product.</p>
    </div>
  </section>

  <section class="research-canvas__inventory signavio-reader__section" id="integration" aria-labelledby="integration-title">
    <header class="signavio-reader__section-head">
      <p class="research-canvas__eyebrow">13 / Integration</p>
      <h2 id="integration-title">Integration model</h2>
    </header>
    <div class="signavio-reader__content">
<p>There is no single “Signavio integration”. Different products integrate for different reasons.</p>

    <div class="table-scroll study-table" role="region" aria-label="Integration model — reference table" tabindex="0">
<table class="study-table__table">
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
</div>

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
    </div>
  </section>

  <section class="research-canvas__inventory signavio-reader__section" id="admin" aria-labelledby="admin-title">
    <header class="signavio-reader__section-head">
      <p class="research-canvas__eyebrow">14 / Administration</p>
      <h2 id="admin-title">Administration: the boundaries that matter</h2>
    </header>
    <div class="signavio-reader__content">
<h3>Identity and user management</h3>

    <p>Current SAP Signavio identity management has changed. Workspaces created after November 25, 2025 have SAP Cloud Identity Services SSO enabled automatically. For workspaces created after May 6, 2026, users and groups are created and managed through SAP Cloud Identity Services.</p>

    <p>This means older learning material that shows only local Signavio user/group administration is tenant-dependent, not a universal current-state design.</p>

    <h3>Four access layers</h3>

    <div class="table-scroll study-table" role="region" aria-label="Four access layers — reference table" tabindex="0">
<table class="study-table__table">
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
</div>

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
    </div>
  </section>

  <section class="research-canvas__inventory signavio-reader__section" id="best-practices" aria-labelledby="best-practices-title">
    <header class="signavio-reader__section-head">
      <p class="research-canvas__eyebrow">15 / Best practices</p>
      <h2 id="best-practices-title">Best practices that create real value</h2>
    </header>
    <div class="signavio-reader__content">
<div class="table-scroll study-table" role="region" aria-label="Best practices that create real value — reference table" tabindex="0">
<table class="study-table__table">
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
</div>
    </div>
  </section>

  <section class="research-canvas__inventory signavio-reader__section" id="interview" aria-labelledby="interview-title">
    <header class="signavio-reader__section-head">
      <p class="research-canvas__eyebrow">16 / Interview practice</p>
      <h2 id="interview-title">How to explain SAP Signavio in an interview</h2>
    </header>
    <div class="signavio-reader__content">
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
    </div>
  </section>

  <section class="research-canvas__inventory signavio-reader__section" id="current-state" aria-labelledby="current-state-title">
    <header class="signavio-reader__section-head">
      <p class="research-canvas__eyebrow">17 / Current state</p>
      <h2 id="current-state-title">Current-state notes for 2026</h2>
    </header>
    <div class="signavio-reader__content">
<ul>
      <li><strong>Process Modeler</strong> is the current modeling product name; Process Manager remains common in older material.</li>
      <li><strong>Process Explorer retired on June 30, 2026.</strong> Use Process Navigator for SAP reference process content.</li>
      <li>For new workspaces, identity management is moving through <strong>SAP Cloud Identity Services</strong>; workspaces created after May 6, 2026 manage users and groups there.</li>
      <li><strong>Process Intelligence</strong> is licensed at workspace level; feature sets and data permissions control user access.</li>
      <li><strong>Process Insights capabilities</strong> are available in Process Intelligence in current SAP documentation.</li>
      <li>New Process Intelligence <strong>investigations</strong> cannot be created or imported since May 26, 2026; customizable dashboards are the current direction.</li>
      <li>AI features and commercial consumption rules change faster than core modeling concepts. Verify the exact feature before promising scope.</li>
    </ul>
    </div>
  </section>

  <section class="research-canvas__inventory signavio-reader__section" id="sources" aria-labelledby="sources-title">
    <header class="signavio-reader__section-head">
      <p class="research-canvas__eyebrow">18 / Sources</p>
      <h2 id="sources-title">Source register</h2>
    </header>
    <div class="signavio-reader__content">
<ul>
      <li><a href="https://help.sap.com/docs/signavio-process-transformation-suite">SAP Signavio Process Transformation Suite — product documentation</a></li>
      <li><a href="https://www.sap.com/about/trust-center/certification-compliance/sap-signavio-c5-2026.html">SAP Signavio C5 2026 — current product naming</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-intelligence/user-guide/navigating-sap-signavio-process-transformation-suite">Navigating SAP Signavio Process Transformation Suite</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-modeler/workspace-admin-guide/about-licenses">Process Modeler — License Assignment</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-transformation-suite/user-management-authentication-and-authorization/harmonization-of-authentication-and-identity-management">SAP Signavio — Identity-management harmonization</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-modeler/security-guide/single-sign-on-using-saml">SAP Signavio — SAML license names</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-manager/sap-signavio-process-manager-api/user-access-and-licensing">Process Modeler API — Access and Licensing</a></li>
      <li><a href="https://help.sap.com/docs/signavio-journey-modeler/user-guide/intro">Journey Modeler — User Guide</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-governance/user-guide/intro">Process Governance — Fundamentals</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-governance/fsd-collaborator/sap-signavio-process-governance-collaborator">Process Governance Collaborator — Feature Scope Description</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-intelligence/user-guide/57542d3a6dab10148cfcc70dfc2ca89e.html">Process Intelligence — User Guide</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-intelligence/user-guide/ai-assisted-process-analyzer">Process Intelligence — AI-assisted Process Analyzer</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-manager/user-guide/ai-assisted-process-modeler">Process Modeler — AI-assisted Process Modeler</a></li>
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
  </section>

  <section class="research-canvas__inventory signavio-reader__section" id="glossary" aria-labelledby="glossary-title">
    <header class="signavio-reader__section-head">
      <p class="research-canvas__eyebrow">19 / Glossary</p>
      <h2 id="glossary-title">Glossary</h2>
    </header>
    <div class="signavio-reader__content">
<div class="table-scroll study-table" role="region" aria-label="Glossary — reference table" tabindex="0">
<table class="study-table__table">
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
</div>
    </div>
  </section>

  <section class="research-canvas__inventory signavio-reader__related" aria-labelledby="signavio-related-title">
    <header>
      <p class="research-canvas__eyebrow">Continue learning</p>
      <h2 id="signavio-related-title">Related SAP topics</h2>
    </header>
    <div class="research-route-list">
      <a href="/labs/assessment/"><span>ASSESS</span><strong>SAP Lead Assessment Lab</strong><small>Practice product choices, ownership, architecture, and scenario answers.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/atlas/maps/sap-technology-landscape-map/"><span>MAP</span><strong>SAP Technology Landscape Map</strong><small>Understand the SAP product and integration context.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/atlas/sap/sap-btp/"><span>BTP</span><strong>SAP BTP</strong><small>Review platform, extension, identity, and connectivity boundaries.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/atlas/sap/sap-s4hana/"><span>ERP</span><strong>SAP S/4HANA</strong><small>Connect process analysis to the transactional system.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </div>
  </section>

  <div class="research-canvas__support">
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</article>
