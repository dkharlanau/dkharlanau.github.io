---
layout: default
title: "SAP Signavio Product Guide"
description: "A consolidated SAP Signavio product guide: suite components, capabilities, licensing boundaries, Process Modeler, Collaboration Hub, Journey Modeler, Process Governance, Process Intelligence, Process Insights, Transformation Manager, integrations, administration, best practices, and glossary."
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
  - /atlas/sap/sap-datasphere/
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
    <p class="eyebrow">Atlas Product Guide</p>
    <h1>SAP Signavio</h1>
    <p class="note-subtitle">One product map for process design, collaboration, governance, journey modeling, process mining, transformation management, administration, licensing boundaries, and integrations.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Purpose</dt><dd>Lead-level product understanding</dd></div>
      <div><dt>Scope</dt><dd>SAP Signavio Process Transformation Suite</dd></div>
      <div><dt>Language</dt><dd>English B2</dd></div>
      <div><dt>Current-state note</dt><dd>Includes product changes verified against SAP documentation available in 2026.</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until human review confirms the full product and license matrix.</dd></div>
    </dl>
  </aside>

  <div class="note-body">

    <h2 id="mental-model">1. Product mental model</h2>

    <p>SAP Signavio is not one application. It is a suite of products that cover different parts of process transformation. The fastest way to understand the suite is to separate six questions:</p>

    <table class="study-table">
      <thead>
        <tr>
          <th>Question</th>
          <th>Primary capability</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>How should the process work?</td><td>Process Modeler / Process Manager</td></tr>
        <tr><td>How do people consume and discuss the process?</td><td>Process Collaboration Hub</td></tr>
        <tr><td>How does a customer, employee, supplier, or partner experience the process?</td><td>Journey Modeler</td></tr>
        <tr><td>How do approvals, reviews, and governance tasks execute?</td><td>Process Governance</td></tr>
        <tr><td>What actually happened in operational data?</td><td>Process Intelligence and Process Insights capabilities</td></tr>
        <tr><td>How do we organize, prioritize, and track transformation initiatives?</td><td>Process Transformation Manager</td></tr>
      </tbody>
    </table>

    <p><strong>Lead rule:</strong> do not answer a Signavio question with only the product name. First identify whether the problem is about process design, consumption, experience, workflow execution, process data, or transformation management.</p>

    <h3>Current naming</h3>

    <p>Current SAP documentation exposes both names. SAP's 2026 trust documentation describes <strong>SAP Signavio Process Modeler</strong> as the product previously called <strong>SAP Signavio Process Manager</strong>, while many Help pages and learning courses still use Process Manager. This guide uses <strong>Process Modeler</strong> as the primary current name and keeps Process Manager where it helps match course or customer terminology.</p>

    <h2 id="suite-map">2. Suite component map</h2>

    <table class="study-table">
      <thead>
        <tr>
          <th>Component</th>
          <th>Main purpose</th>
          <th>Key capabilities</th>
          <th>Typical users</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>SAP Signavio Process Modeler</td>
          <td>Design and govern process models</td>
          <td>BPMN, DMN, QuickModel, Dictionary, simulation, reports, conventions, variants, process documentation</td>
          <td>Process architects, modelers, process owners, BPM teams</td>
        </tr>
        <tr>
          <td>SAP Signavio Process Collaboration Hub</td>
          <td>Consume and collaborate on published process content</td>
          <td>Published process access, comments, feedback, read confirmations, ratings, reporting, audience-based presentation</td>
          <td>Process consumers, business users, reviewers</td>
        </tr>
        <tr>
          <td>SAP Signavio Journey Modeler</td>
          <td>Model the outside-in experience</td>
          <td>Personas, stages, steps, touchpoints, sentiments, linked processes, systems, organizations, metrics, complexity</td>
          <td>CX teams, process owners, transformation teams</td>
        </tr>
        <tr>
          <td>SAP Signavio Process Governance</td>
          <td>Execute governed workflows</td>
          <td>Triggers, forms, tasks, approvals, cases, reminders, escalations, workflow versions, connectors</td>
          <td>Process governance teams, workflow designers, approvers</td>
        </tr>
        <tr>
          <td>SAP Signavio Process Intelligence</td>
          <td>Analyze actual process execution</td>
          <td>Data management, out-of-the-box and custom process analysis, dashboards, metrics, insights, root-cause analysis, analysis workflows</td>
          <td>Process analysts, data teams, process owners</td>
        </tr>
        <tr>
          <td>SAP Signavio Process Insights</td>
          <td>Provide predefined SAP process performance content</td>
          <td>Predefined process flows, performance indicators, recommendations, SAP-focused analysis content</td>
          <td>Business process experts, transformation teams</td>
        </tr>
        <tr>
          <td>SAP Signavio Process Transformation Manager</td>
          <td>Manage improvement and transformation initiatives</td>
          <td>Benchmarking, insights, initiatives, objectives, tasks, value-oriented prioritization</td>
          <td>Transformation leads, process owners, program teams</td>
        </tr>
        <tr>
          <td>SAP Signavio Process Explorer</td>
          <td>Discover transformation content and accelerators</td>
          <td>Access to value accelerators, reference content, and resources</td>
          <td>Process teams, transformation teams</td>
        </tr>
      </tbody>
    </table>

    <h3>Cross-suite capabilities</h3>

    <p>The suite also includes shared capabilities such as the launchpad, user and workspace administration, Value Accelerator Library, AI capabilities, APIs, and integrations. These are not a replacement for the product boundaries above. Their availability depends on product licenses, packages, authorizations, and sometimes additional commercial terms.</p>

    <h2 id="capability-matrix">3. Capability matrix</h2>

    <table class="study-table">
      <thead>
        <tr>
          <th>Capability</th>
          <th>Primary owner</th>
          <th>Important boundary</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>BPMN modeling</td><td>Process Modeler</td><td>Describes designed process flow; it is not process mining.</td></tr>
        <tr><td>DMN decision modeling</td><td>Process Modeler</td><td>Separates decision logic from BPMN flow.</td></tr>
        <tr><td>Quick process capture</td><td>QuickModel in Process Modeler</td><td>Best for simple flows; complex BPMN belongs in the Graphical Editor.</td></tr>
        <tr><td>Shared business vocabulary</td><td>Dictionary</td><td>Central object change can affect many linked diagrams.</td></tr>
        <tr><td>Process architecture</td><td>Navigation Maps and Value Chains</td><td>Navigation Maps optimize entry and usability; Value Chains express high-level process architecture.</td></tr>
        <tr><td>Process simulation</td><td>Process Modeler</td><td>What-if analysis based on assumptions, not evidence of real execution.</td></tr>
        <tr><td>Model-based reporting</td><td>Process Modeler / Collaboration Hub</td><td>Uses model elements and attributes, not event-log evidence.</td></tr>
        <tr><td>Publishing and consumption</td><td>Collaboration Hub</td><td>Published content is different from editable working content.</td></tr>
        <tr><td>Feedback and semantic review</td><td>Collaboration Hub + Editor comments</td><td>Syntax can be checked by the system; business meaning still needs people.</td></tr>
        <tr><td>Variant management</td><td>Process Modeler / Collaboration Hub</td><td>Controls standard-to-local differences; it is not uncontrolled copy-and-paste.</td></tr>
        <tr><td>Journey modeling</td><td>Journey Modeler</td><td>Outside-in perspective; link pain points back to internal processes.</td></tr>
        <tr><td>Governance workflow execution</td><td>Process Governance</td><td>Executes tasks and cases; Process Modeler defines process content.</td></tr>
        <tr><td>Approval before publishing</td><td>Process Modeler + Process Governance</td><td>Requires Process Governance in addition to the modeling product.</td></tr>
        <tr><td>Process mining</td><td>Process Intelligence</td><td>Uses operational event/process data to explain actual execution.</td></tr>
        <tr><td>Predefined SAP performance analysis</td><td>Process Insights capabilities</td><td>Current SAP documentation places these capabilities in the Process Intelligence direction/package.</td></tr>
        <tr><td>Transformation initiative management</td><td>Process Transformation Manager</td><td>Manages improvement work; it is not a BPMN modeling tool.</td></tr>
        <tr><td>Business-to-IT model synchronization</td><td>Business Process Model Connector</td><td>Connects Signavio and SAP Solution Manager with explicit ownership and mapping rules.</td></tr>
      </tbody>
    </table>

    <h2 id="licensing">4. Licensing and access: what is included and what is separate</h2>

    <p>Licensing and authorization are different layers. The table below describes product boundaries, not commercial pricing. Exact entitlements depend on the contract, package, edition, region, and current SAP Feature Scope Description.</p>

    <table class="study-table">
      <thead>
        <tr>
          <th>Product / access type</th>
          <th>Boundary</th>
          <th>Assignment model</th>
          <th>Key point</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Process Modeler modeling user</td>
          <td>Base modeling license</td>
          <td>User-level, workspace-bound</td>
          <td>Gets the functionality of the licensed Process Modeler edition and access to Process Collaboration Hub.</td>
        </tr>
        <tr>
          <td>Process Collaboration Hub user</td>
          <td>Separate consumer license, but included for modeling users</td>
          <td>User-level</td>
          <td>Hub users receive consumer access plus a limited Modeler feature set such as QuickModel, comparison, export, reporting, and Dictionary access. The license itself is not an authorization rule.</td>
        </tr>
        <tr>
          <td>External commenting user</td>
          <td>Included feedback path</td>
          <td>Automatic commenting license after invitation</td>
          <td>Restricted to invited diagram feedback; no broad workspace or product access.</td>
        </tr>
        <tr>
          <td>Journey Modeler</td>
          <td>Separate product license</td>
          <td>User-level</td>
          <td>SAP identity documentation exposes <strong>Journey Modeling Standard</strong> and <strong>Journey Modeling Advanced</strong>. Exact feature differences must be checked in the current scope/contract.</td>
        </tr>
        <tr>
          <td>Process Governance</td>
          <td>Separate product license</td>
          <td>User-level workflow access</td>
          <td>SAP SAML documentation uses the license name <strong>Workflow</strong>. Approval workflows in Process Modeler require Process Governance in addition to the modeling license.</td>
        </tr>
        <tr>
          <td>Process Governance Collaborator</td>
          <td>Sub-license</td>
          <td>Limited user access</td>
          <td>Can start cases, complete tasks, use the task inbox and notifications, and participate in supported variant change propagation. SAP states that this sub-license cannot be purchased stand-alone.</td>
        </tr>
        <tr>
          <td>Process Intelligence</td>
          <td>Separate workspace/package entitlement</td>
          <td>License on workspace; user access through feature sets and data permissions</td>
          <td>Unlike most Signavio products, the Process Intelligence license is not assigned individually to each user.</td>
        </tr>
        <tr>
          <td>Process Insights</td>
          <td>Separate package/BTP entitlement</td>
          <td>Contract + BTP subscription + role collections</td>
          <td>Current SAP documentation says Process Insights capabilities are available in Process Intelligence. Standardized integration and out-of-the-box analysis use the Process Insights and Intelligence package.</td>
        </tr>
        <tr>
          <td>Process Transformation Manager</td>
          <td>Separate product/capability license</td>
          <td>User access plus object roles</td>
          <td>Benchmarking, initiatives, insights, objectives, tasks, and related functions depend on license and access rights.</td>
        </tr>
        <tr>
          <td>Process Explorer / Value Accelerator Library</td>
          <td>Package/entitlement dependent</td>
          <td>Depends on workspace products and authorization</td>
          <td>Use as acceleration content. SAP states that value accelerators are optional and are not part of core product business functionality.</td>
        </tr>
        <tr>
          <td>API technical user</td>
          <td>Technical license</td>
          <td>Dedicated technical account</td>
          <td>Use API Edition when available instead of consuming a paid business-user license. SAP API documentation describes support-driven API Edition assignment and no additional license cost for this technical use.</td>
        </tr>
        <tr>
          <td>Business Process Model Connector</td>
          <td>BTP application entitlement</td>
          <td>BTP subscription + connector roles</td>
          <td>Requires connector entitlement, supported BTP setup, Cloud Connector where applicable, system prerequisites, and assigned roles. Verify commercial entitlement in the contract.</td>
        </tr>
        <tr>
          <td>AI capabilities</td>
          <td>Feature-specific</td>
          <td>Base product + possible AI entitlement/AI Units</td>
          <td>Do not infer AI access from the base product. SAP commercial requirements vary by AI feature and can change.</td>
        </tr>
      </tbody>
    </table>

    <h3>License is not permission</h3>

    <p>A license gives product access. Groups, feature sets, object permissions, and data access decide what the user can actually do or see. This is especially important in Collaboration Hub, Process Governance, and Process Intelligence.</p>

    <h3>2026 identity-management boundary</h3>

    <p>For new workspaces, current SAP documentation has moved identity management toward SAP Cloud Identity Services. Workspaces created after November 25, 2025 have SAP Cloud Identity Services SSO enabled automatically. For workspaces created after May 6, 2026, users and groups are created and managed through SAP Cloud Identity Services. Older course material that shows local Signavio user/group administration remains relevant for older tenants, but it is not the universal current-state flow.</p>

    <h2 id="modeler">5. Process Modeler: design, structure, and govern process knowledge</h2>

    <h3>Explorer, Editor, QuickModel, and Dictionary</h3>

    <table class="study-table">
      <thead>
        <tr>
          <th>Capability</th>
          <th>Use it for</th>
          <th>Lead question</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Explorer</td><td>Folders, models, search, revisions, access, reporting, simulation entry points</td><td>Where is the process and who owns the content?</td></tr>
        <tr><td>Graphical Editor</td><td>Detailed BPMN, DMN, attributes, review, conventions</td><td>How is the process or decision modeled?</td></tr>
        <tr><td>QuickModel</td><td>Fast table-based BPMN capture</td><td>Can the business capture the happy path before detailed modeling?</td></tr>
        <tr><td>Dictionary</td><td>Reusable roles, systems, documents, risks, controls, and other business objects</td><td>Are we using one governed business vocabulary?</td></tr>
      </tbody>
    </table>

    <p><strong>Best practice:</strong> define the process architecture and governance model before creating hundreds of diagrams. Folder structure, access rights, Dictionary categories, attributes, naming rules, and process levels are architecture decisions.</p>

    <h3>Recommended process architecture</h3>

    <ol>
      <li><strong>Navigation Map</strong> — user-friendly entry point.</li>
      <li><strong>Value Chain</strong> — high-level process architecture.</li>
      <li><strong>BPMN model</strong> — detailed process flow and responsibility.</li>
      <li><strong>Subprocess / Call Activity</strong> — controlled detail and reusable global logic.</li>
      <li><strong>Dictionary objects</strong> — shared roles, systems, documents, risks, controls, and terms.</li>
      <li><strong>Attributes and conventions</strong> — metadata and quality rules.</li>
      <li><strong>Collaboration Hub</strong> — consumption and feedback.</li>
    </ol>

    <h3>BPMN rules that matter in practice</h3>

    <table class="study-table">
      <thead>
        <tr>
          <th>Concept</th>
          <th>Rule</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Task</td><td>Describe work with active wording, normally verb + object.</td></tr>
        <tr><td>Event</td><td>Describe a state, trigger, wait, or result; start events catch, end events throw.</td></tr>
        <tr><td>XOR</td><td>Select exactly one route. The gateway routes a decision result; it is not the decision task.</td></tr>
        <tr><td>AND</td><td>Create all parallel paths and synchronize all required tokens at the join.</td></tr>
        <tr><td>OR</td><td>Create one or several valid paths and wait only for paths that were activated.</td></tr>
        <tr><td>Sequence Flow</td><td>Connect work inside one pool.</td></tr>
        <tr><td>Message Flow</td><td>Represent communication between pools.</td></tr>
        <tr><td>Pool</td><td>Represent a participant or organization boundary.</td></tr>
        <tr><td>Lane</td><td>Represent responsibility according to the chosen modeling convention.</td></tr>
      </tbody>
    </table>

    <p>The <strong>token concept</strong> is the best way to reason about BPMN behavior. It explains parallel execution, waiting, synchronization, deadlocks, and multi-merges.</p>

    <h3>Deadlock vs multi-merge</h3>

    <table class="study-table">
      <thead>
        <tr><th>Problem</th><th>What happens</th><th>Typical fix</th></tr>
      </thead>
      <tbody>
        <tr><td>Deadlock</td><td>An AND join waits for a token that can never arrive.</td><td>Correct the split/join structure, often by merging alternative branches before synchronization.</td></tr>
        <tr><td>Multi-merge</td><td>Several tokens continue and execute a downstream task more than once.</td><td>Synchronize parallel tokens with the correct AND join.</td></tr>
      </tbody>
    </table>

    <h3>Subprocess choice</h3>

    <table class="study-table">
      <thead>
        <tr><th>Pattern</th><th>Use</th><th>Reuse</th></tr>
      </thead>
      <tbody>
        <tr><td>Collapsed subprocess</td><td>Hide detail and keep the main process readable.</td><td>Can point to a separate detailed model.</td></tr>
        <tr><td>Call Activity</td><td>Reference reusable global process logic.</td><td>Designed for reuse across processes.</td></tr>
        <tr><td>Expanded subprocess</td><td>Show grouped detail inside the parent model.</td><td>Local to that process scenario.</td></tr>
      </tbody>
    </table>

    <h3>Dictionary governance</h3>

    <p>The Dictionary is a central object repository, not a tag list. Reuse the same object instead of creating local copies. A central Dictionary edit can affect linked models, while a local attribute change can remain diagram-specific.</p>

    <p>Use a <strong>sandbox</strong> for proposed entries and a small <strong>Dictionary Responsible</strong> group for review, merge, category maintenance, and productive promotion. Use Excel import/export for controlled bulk maintenance, not as an unmanaged parallel master-data store.</p>

    <h3>Modeling conventions</h3>

    <p>Syntax checks validate notation behavior. Convention checks validate organization-specific standards such as naming, required attributes, architecture, structure, and layout. A model can pass syntax and still be wrong for the business.</p>

    <h2 id="dmn">6. DMN: keep business rules out of gateway spaghetti</h2>

    <p>DMN separates decision structure from decision logic. Use BPMN for activity flow and DMN for the rules that determine an outcome.</p>

    <table class="study-table">
      <thead>
        <tr><th>DMN layer</th><th>Purpose</th></tr>
      </thead>
      <tbody>
        <tr><td>Decision Requirements Diagram</td><td>Shows decisions, sub-decisions, input data, and knowledge sources.</td></tr>
        <tr><td>Decision Table</td><td>Defines detailed input conditions and outputs as business rules.</td></tr>
      </tbody>
    </table>

    <h3>Core elements</h3>

    <ul>
      <li><strong>Decision</strong> — returns an outcome and can be decomposed.</li>
      <li><strong>Input Data</strong> — information required for the decision.</li>
      <li><strong>Knowledge Source</strong> — policy, regulation, law, or authoritative source.</li>
    </ul>

    <h3>Input types</h3>

    <p>Common input types are Boolean, Number, Enumeration, Text, Date, and Hierarchy. Prefer controlled enumerations over free text when possible because they reduce input variation.</p>

    <h3>Hit policies</h3>

    <table class="study-table">
      <thead>
        <tr><th>Policy</th><th>Meaning</th></tr>
      </thead>
      <tbody>
        <tr><td>Unique</td><td>Exactly one rule may match; overlaps are invalid.</td></tr>
        <tr><td>First</td><td>Rules can overlap; first match from top to bottom wins.</td></tr>
        <tr><td>Any</td><td>Several rules may match only if all return the same output.</td></tr>
        <tr><td>Priority</td><td>Several rules may match; the highest-priority output wins.</td></tr>
        <tr><td>Collect</td><td>Several rules may fire; results are returned or aggregated with Sum, Min, Max, or Count.</td></tr>
      </tbody>
    </table>

    <p>Split a decision when complexity, reuse, or different sources of authority make one table hard to maintain. The learning material treats more than seven inputs and/or sub-decisions as a strong complexity warning, not as a hard technical limit.</p>

    <h3>Verify vs Simulation vs Test Lab</h3>

    <table class="study-table">
      <thead>
        <tr><th>Tool</th><th>Question</th></tr>
      </thead>
      <tbody>
        <tr><td>Verify</td><td>Are rules complete and consistent for the selected hit policy?</td></tr>
        <tr><td>Simulation</td><td>What output does the decision model produce for these inputs?</td></tr>
        <tr><td>Test Lab</td><td>Does the changed decision still produce expected and regression-safe results?</td></tr>
      </tbody>
    </table>

    <h2 id="simulation-reporting">7. Simulation, reporting, variants, and collaboration</h2>

    <h3>Simulation</h3>

    <p>BPMN simulation is a <strong>what-if</strong> tool. Its four main parameter groups are Costs, Duration, Frequency, and Resources.</p>

    <table class="study-table">
      <thead>
        <tr><th>Parameter</th><th>What it controls</th></tr>
      </thead>
      <tbody>
        <tr><td>Costs</td><td>Activity-specific execution costs. Do not put labor cost here if it is modeled through Resources.</td></tr>
        <tr><td>Duration</td><td>Task execution time and optional distributions.</td></tr>
        <tr><td>Frequency</td><td>Case arrivals and gateway path probabilities.</td></tr>
        <tr><td>Resources</td><td>Working schedules, capacity, and hourly wages by lane.</td></tr>
      </tbody>
    </table>

    <p><strong>Execution time is not total cycle time.</strong> Cycle time can include waiting caused by resource constraints and queues. Simulation can expose potential bottlenecks, but it does not prove what happened in production.</p>

    <h3>Reporting</h3>

    <table class="study-table">
      <thead>
        <tr><th>Report</th><th>Use</th></tr>
      </thead>
      <tbody>
        <tr><td>Process Cost Analysis</td><td>Estimate task cost using execution cost, frequency, and routing probability.</td></tr>
        <tr><td>Resource Consumption</td><td>Analyze workload and time by roles or departments.</td></tr>
        <tr><td>RACI / Responsibility Assignment</td><td>Show Responsible, Accountable, Consulted, and Informed roles.</td></tr>
        <tr><td>Responsibility Handovers</td><td>Expose handoffs between participants.</td></tr>
        <tr><td>IT System Usage</td><td>Show system usage across activities and roles.</td></tr>
        <tr><td>Document Usage</td><td>Show documents used as inputs or outputs.</td></tr>
        <tr><td>Modeling Conventions</td><td>Check model populations against BPMN and workspace rules.</td></tr>
        <tr><td>Process Model Metrics</td><td>Measure model size, element types, linked files, and Dictionary links.</td></tr>
        <tr><td>Process Characteristics</td><td>List used BPMN elements and populated attributes.</td></tr>
        <tr><td>Risks and Controls</td><td>Aggregate risk/control information linked from the Dictionary.</td></tr>
        <tr><td>Process Documentation</td><td>Create configurable Word/PDF outputs with diagrams and attributes.</td></tr>
      </tbody>
    </table>

    <h3>Variant Management</h3>

    <p>Use variants when one global process needs controlled regional, organizational, product, customer, or transformation-specific differences.</p>

    <p>The model is:</p>

    <p><strong>Template → Dimensions → Dictionary values → Variant Group → Variants</strong></p>

    <table class="study-table">
      <thead>
        <tr><th>Action</th><th>Meaning</th></tr>
      </thead>
      <tbody>
        <tr><td>Attach</td><td>Connect an existing process to a template as a variant.</td></tr>
        <tr><td>Clone</td><td>Create a new variant from the template structure.</td></tr>
        <tr><td>Detach</td><td>Break the template relationship so the process evolves independently.</td></tr>
      </tbody>
    </table>

    <p>Template changes can be propagated to variants. Supported changes can be handled automatically; others require modeler review and manual adjustment. Update notifications depend on the latest template revision being published.</p>

    <h3>Collaboration</h3>

    <p>Comments, stakeholder review, and publishing are part of process quality. A syntax-valid BPMN diagram can still be semantically wrong. Use comments and subject-matter review before publishing important content.</p>

    <p>A practical lifecycle is:</p>

    <p><strong>Model → review → resolve feedback → approval if required → publish → consume → improve</strong></p>

    <h2 id="hub">8. Process Collaboration Hub: consumption layer</h2>

    <p>Process Collaboration Hub is the central place for business users to consume published process content. It is also a collaboration surface for comments, ratings, read confirmations, reports, and navigation.</p>

    <h3>Published vs Preview</h3>

    <p><strong>Published</strong> shows the governed published version. <strong>Preview</strong> exposes current content according to the user's permissions. Do not use Preview access as a substitute for a publication and approval policy.</p>

    <h3>Audience vs authorization</h3>

    <p>An <strong>Audience</strong> changes how content is presented to a viewer group, for example home page, theme, entry point, and attribute visibility. Access rights decide whether the user is allowed to see or change the content. Presentation and authorization are different controls.</p>

    <h3>Read Confirmation vs Process Rating</h3>

    <table class="study-table">
      <thead>
        <tr><th>Feature</th><th>Purpose</th></tr>
      </thead>
      <tbody>
        <tr><td>Read Confirmation</td><td>Request acknowledgement that a user has read a process or a new revision.</td></tr>
        <tr><td>Process Rating</td><td>Collect structured feedback on a process revision using selected criteria.</td></tr>
      </tbody>
    </table>

    <h2 id="journey">9. Journey Modeler: outside-in process understanding</h2>

    <p>Journey modeling starts with the person who experiences the organization. The person can be a customer, employee, applicant, supplier, partner, or another stakeholder.</p>

    <table class="study-table">
      <thead>
        <tr><th>View</th><th>Main question</th></tr>
      </thead>
      <tbody>
        <tr><td>Inside-out process</td><td>How does the organization execute the work?</td></tr>
        <tr><td>Outside-in journey</td><td>How does the person experience the result of that work?</td></tr>
      </tbody>
    </table>

    <h3>Journey structure</h3>

    <ol>
      <li><strong>Persona</strong> — who is experiencing the journey?</li>
      <li><strong>Stages and steps</strong> — what does the person go through?</li>
      <li><strong>Touchpoints</strong> — where does the person interact with the company or product?</li>
      <li><strong>Sentiment</strong> — how does the person feel at the relevant moments?</li>
      <li><strong>Operational links</strong> — which processes, systems, organizations, and metrics create the experience?</li>
    </ol>

    <p>A <strong>step</strong> is part of the person's journey. A <strong>touchpoint</strong> is an interaction with the company, product, or a related channel. Do not treat them as synonyms.</p>

    <h3>Journey Modeler vs Customer Journey Map</h3>

    <table class="study-table">
      <thead>
        <tr><th>Tool</th><th>Best use</th></tr>
      </thead>
      <tbody>
        <tr><td>Journey Modeler</td><td>Structured table with stages, steps, sentiments, processes, systems, organizations, metrics, and other data.</td></tr>
        <tr><td>Customer Journey Map</td><td>Visual journey storytelling with persona, steps, touchpoints, and linked attributes.</td></tr>
      </tbody>
    </table>

    <h3>Journey Complexity vs Journey Model Dimensions</h3>

    <p><strong>Journey Complexity</strong> measures operational complexity inherited from linked processes. The learning material weights Flow and Handovers at 35% each, and IT Systems, Data Objects, and Linked Processes at 10% each.</p>

    <p><strong>Journey Model Dimensions</strong> measure the size and populated content of the journey table. Model size is not the same as operational complexity.</p>

    <p>Use journey work to create a traceable improvement chain:</p>

    <p><strong>Pain point → linked process/system → process change → KPI → evidence of improved experience</strong></p>

    <h2 id="governance">10. Process Governance: execute governance workflows</h2>

    <p>Process Governance is a web-based workflow modeling and execution platform. It coordinates tasks, cases, handovers, approvals, reminders, escalations, and workflow data.</p>

    <h3>Workflow vs process model</h3>

    <p>A process model explains the broader business flow and outcome. A Process Governance workflow operationalizes repeatable work: who receives a task, what data they enter, what happens next, and how the case is controlled.</p>

    <h3>Four operating areas</h3>

    <p>Current Process Governance documentation organizes the product around workflows, tasks, cases, and analytics. Workflows define the executable template; cases are running instances; tasks are units of human work; analytics reports on workflow execution.</p>

    <h3>Triggers</h3>

    <table class="study-table">
      <thead>
        <tr><th>Trigger</th><th>Use</th></tr>
      </thead>
      <tbody>
        <tr><td>Public Form</td><td>Allow external or public users to start a case.</td></tr>
        <tr><td>Private Form</td><td>Allow registered internal users to start a case.</td></tr>
        <tr><td>E-mail</td><td>Start a case from an incoming message, including system-generated notifications.</td></tr>
        <tr><td>Process Modeler</td><td>Start governance for a process model, for example approval before publication.</td></tr>
      </tbody>
    </table>

    <h3>User Task vs Multi-User Task</h3>

    <table class="study-table">
      <thead>
        <tr><th>Action</th><th>Use</th></tr>
      </thead>
      <tbody>
        <tr><td>User Task</td><td>One person or role performs a task; can include forms, due dates, reminders, and access controls.</td></tr>
        <tr><td>Multi-User Task</td><td>Several people each perform the same task. Execution can be parallel or sequential and results are collected.</td></tr>
      </tbody>
    </table>

    <p>Due date and reminder are separate. A deadline controls expected completion; reminders notify assignees or candidates. The learning material states a maximum of 25 reminders for one task.</p>

    <h3>Workflow design best practices</h3>

    <ul>
      <li>Name a workflow with a short active verb phrase that describes the goal of one case.</li>
      <li>Use labels for categorization instead of encoding categories into long workflow names.</li>
      <li>Use a readable case-name template so users can identify a running case quickly.</li>
      <li>Restrict experimental workflows so unfinished test content does not fill the common workflow list.</li>
      <li>Prefer group-based access control over long-term individual permissions.</li>
    </ul>

    <h3>Workflow versioning</h3>

    <table class="study-table">
      <thead>
        <tr><th>Action</th><th>Effect</th></tr>
      </thead>
      <tbody>
        <tr><td>Publish</td><td>Create a version that can start new cases.</td></tr>
        <tr><td>Re-Publish</td><td>Publish a new copy of an older version for future cases without deleting current unpublished edits.</td></tr>
        <tr><td>Restore</td><td>Replace the editable draft with an older version; the current published execution version does not change.</td></tr>
      </tbody>
    </table>

    <h3>Approval workflow boundary</h3>

    <p>Approval workflows connect Process Modeler and Process Governance. Process Modeler holds the content and publication state; Process Governance executes the approval tasks. SAP documentation requires a Process Governance license in addition to Process Modeler for this function.</p>

    <h3>Integration boundary</h3>

    <p>Process Governance supports external actions, connectors, Trigger API, e-mail, and analytics access. It should not be treated as a general embedded workflow engine for another application: current SAP documentation states that tasks and cases are intended to be interacted with through the Process Governance user interface rather than through a generic task/case execution API.</p>

    <h2 id="intelligence">11. Process Intelligence and Process Insights: observed execution</h2>

    <p>Process Intelligence answers a different question from Process Modeler:</p>

    <p><strong>Process Modeler: what should happen?</strong><br>
    <strong>Process Intelligence: what did happen?</strong></p>

    <h3>Current product areas</h3>

    <ul>
      <li><strong>Data Management</strong> — integrate and prepare process data.</li>
      <li><strong>Analysis Configuration</strong> — define data sources, attributes, metrics, governance, and access.</li>
      <li><strong>Process Analysis</strong> — use out-of-the-box and custom process analysis.</li>
      <li><strong>Dashboards</strong> — visualize performance and process behavior.</li>
      <li><strong>Insights</strong> — save findings and data-backed observations.</li>
      <li><strong>Automated Root Cause Analysis</strong> — identify subgroups that drive performance.</li>
      <li><strong>Value Analysis</strong> — add monetary context to improvement opportunities.</li>
      <li><strong>Analysis Workflows</strong> — monitor process data and trigger actions when conditions are met.</li>
    </ul>

    <h3>Out-of-the-box vs custom analysis</h3>

    <table class="study-table">
      <thead>
        <tr><th>Approach</th><th>Use</th></tr>
      </thead>
      <tbody>
        <tr><td>Out-of-the-box process analysis</td><td>Start quickly with SAP-defined process content, process flows, and performance indicators.</td></tr>
        <tr><td>Custom process analysis</td><td>Define your own process semantics, data integration, metrics, attributes, dashboards, and analysis scope.</td></tr>
      </tbody>
    </table>

    <p>The semantic model matters. A visually convincing analysis can still be wrong if the case definition, activities, timestamps, attributes, or metrics do not represent the business process correctly.</p>

    <h3>Process Insights current-state note</h3>

    <p>Current SAP Help states that SAP Signavio Process Insights capabilities are available in SAP Signavio Process Intelligence. The standardized onboarding path uses the <strong>SAP Signavio Process Insights and Intelligence package</strong> for predefined integration and out-of-the-box analysis. Treat older references to Process Insights as a separate application with care and verify the customer's package and migration state.</p>

    <h3>Investigations transition</h3>

    <p>As of May 26, 2026, SAP documentation states that new investigations can no longer be created or imported. Existing investigations remain accessible for now, while customizable dashboards replace the investigation experience. Use current dashboard terminology in new designs.</p>

    <h3>Simulation vs reporting vs Process Intelligence</h3>

    <table class="study-table">
      <thead>
        <tr><th>Capability</th><th>Evidence</th><th>Question</th></tr>
      </thead>
      <tbody>
        <tr><td>Simulation</td><td>Assumptions on a designed model</td><td>What could happen?</td></tr>
        <tr><td>Model reporting</td><td>Model elements and attributes</td><td>What have we documented?</td></tr>
        <tr><td>Process Intelligence</td><td>Operational process data</td><td>What actually happened?</td></tr>
      </tbody>
    </table>

    <h2 id="transformation-manager">12. Process Transformation Manager and accelerators</h2>

    <h3>Process Transformation Manager</h3>

    <p>Process Transformation Manager manages improvement work across the process landscape. Core concepts include:</p>

    <ul>
      <li><strong>Benchmarking</strong> — compare performance with available benchmark data.</li>
      <li><strong>Insights</strong> — capture findings and evidence.</li>
      <li><strong>Initiatives</strong> — organize and prioritize improvement efforts.</li>
      <li><strong>Objectives</strong> — define and align goals.</li>
      <li><strong>Tasks</strong> — assign work inside initiatives.</li>
      <li><strong>Value-oriented prioritization</strong> — connect improvement work to measurable impact.</li>
    </ul>

    <p>Do not confuse Process Transformation Manager with Process Governance. Governance executes repeatable workflows and cases. Transformation Manager organizes improvement initiatives and the work around them.</p>

    <h3>Process Explorer and Value Accelerator Library</h3>

    <p>Process Explorer and the Value Accelerator Library help teams start from SAP and industry content instead of designing everything from zero. Use accelerators as a starting point and adapt them to the customer's operating model. SAP explicitly describes value accelerators as optional content that can change and is not part of core business functionality.</p>

    <h3>AI capabilities</h3>

    <p>AI is a cross-suite capability, not one single Signavio product. Examples include AI-assisted process analysis and other product-specific AI features. Commercial requirements vary. Some current SAP product pages require AI Units for specific AI features, while others currently do not. Always verify the exact AI feature, base product, entitlement, and current AI Unit policy.</p>

    <h2 id="connector">13. Business Process Model Connector: connect Business and IT</h2>

    <p>The Business Process Model Connector is a stand-alone cloud application on SAP BTP that connects SAP Signavio Process Modeler with SAP Solution Manager.</p>

    <table class="study-table">
      <thead>
        <tr><th>System</th><th>Primary ownership</th></tr>
      </thead>
      <tbody>
        <tr><td>SAP Signavio</td><td>Process structure and business artifacts.</td></tr>
        <tr><td>SAP Solution Manager</td><td>Solution design and IT lifecycle artifacts.</td></tr>
      </tbody>
    </table>

    <h3>Direction and ownership</h3>

    <p>If process information already exists in Solution Manager, an initial synchronization can load it into Signavio. After that alignment, the learning material makes Signavio the leading system for process information and sends ongoing process updates from Signavio to Solution Manager.</p>

    <p>The connector supports transfer in both directions for supported content, but ownership is not symmetric. The course also states that BPMN diagrams synchronized from Solution Manager to Signavio cannot simply be synchronized back as a round trip.</p>

    <h3>Key prerequisites</h3>

    <ul>
      <li>Solution Manager technical user and required rights.</li>
      <li>Required Solution Manager SICF services active.</li>
      <li>Dedicated Signavio technical user with write/API access.</li>
      <li>SAP Cloud Connector installed and connected.</li>
      <li>Supported BTP subaccount region and entitlements.</li>
      <li>Trust relationship between BTP connectivity and Solution Manager.</li>
      <li>Connector subscription and user roles.</li>
    </ul>

    <p>The learning material lists EU10 and US10 as supported BTP regions for the connector. Verify current regional availability before implementation.</p>

    <h3>Synchronization Project</h3>

    <p>A Synchronization Project defines one system pair, Solution/Branch context, Dictionary-category mappings, attribute mappings, optional governance revision state, and synchronization settings.</p>

    <p>Run sequence:</p>

    <p><strong>Create → map categories → map attributes → preview/save → activate → select direction/content → run → inspect logs/history</strong></p>

    <p>If no governance revision state is selected, the learning material uses the latest revision by default. If a state such as Approved is selected, only content in that lifecycle state is transferred. Process Governance is required for revision-state gating.</p>

    <h2 id="administration">14. Administration, access, and security</h2>

    <h3>Admin responsibilities</h3>

    <table class="study-table">
      <thead>
        <tr><th>Area</th><th>Administrator decisions</th></tr>
      </thead>
      <tbody>
        <tr><td>Process Modeler</td><td>Workspace settings, conventions, attributes, Dictionary structure, content access, security.</td></tr>
        <tr><td>Collaboration Hub</td><td>Audiences, presentation, attribute visibility, ratings, read confirmations, consumer experience.</td></tr>
        <tr><td>Journey Modeler</td><td>Journey templates and shared settings.</td></tr>
        <tr><td>Process Governance</td><td>Users/groups, workflow creation control, reusable activities, connectors, credentials, labels, workspace settings.</td></tr>
        <tr><td>Process Intelligence</td><td>Feature access, data access, analysis configuration permissions, semantic-view access.</td></tr>
      </tbody>
    </table>

    <h3>Access rights are additive</h3>

    <p>Design folder structure and groups before assigning large numbers of users. In the traditional Process Modeler access model, rights granted through one group cannot be removed by adding the user to a second group with fewer rights.</p>

    <p>Common Process Modeler rights are:</p>

    <table class="study-table">
      <thead>
        <tr><th>Right</th><th>Meaning</th></tr>
      </thead>
      <tbody>
        <tr><td>H — Hub</td><td>View published Hub content.</td></tr>
        <tr><td>R — Read</td><td>Read working/unpublished content where permitted.</td></tr>
        <tr><td>W — Write</td><td>Edit and save content.</td></tr>
        <tr><td>D — Delete</td><td>Delete and move content with required source/target permissions.</td></tr>
        <tr><td>P — Publish</td><td>Publish to Collaboration Hub.</td></tr>
      </tbody>
    </table>

    <h3>Groups over individual permissions</h3>

    <p>Use groups for stable organizational roles. Use individual permissions only for justified exceptions. This reduces access drift and makes reviews easier.</p>

    <h3>Security</h3>

    <p>Important controls include SSO, identity provisioning, IP filtering, password policy where applicable, least-privilege groups, and separation of technical users from human users. New workspaces should be designed around SAP Cloud Identity Services rather than old local-user assumptions.</p>

    <h2 id="best-practices">15. Best practices and anti-patterns</h2>

    <table class="study-table">
      <thead>
        <tr><th>Do</th><th>Avoid</th></tr>
      </thead>
      <tbody>
        <tr><td>Define process architecture before mass modeling.</td><td>Hundreds of unrelated diagrams with no level or ownership model.</td></tr>
        <tr><td>Use Dictionary objects as governed master references.</td><td>Duplicate roles, systems, documents, risks, and controls in each diagram.</td></tr>
        <tr><td>Use DMN for complex decision logic.</td><td>Gateway-heavy BPMN that hides business rules.</td></tr>
        <tr><td>Use Call Activities for reusable global logic.</td><td>Copying the same subprocess into many models.</td></tr>
        <tr><td>Use process roles instead of named people in lanes.</td><td>Person-specific models that require constant maintenance.</td></tr>
        <tr><td>Use conventions plus stakeholder review.</td><td>Assuming a syntax-valid model is business-correct.</td></tr>
        <tr><td>Use simulation for hypotheses and Process Intelligence for evidence.</td><td>Presenting simulation output as real process performance.</td></tr>
        <tr><td>Use variants for justified controlled differences.</td><td>Independent local copies that silently diverge from the global process.</td></tr>
        <tr><td>Separate license assignment from access rights.</td><td>Assuming a license automatically provides safe authorization.</td></tr>
        <tr><td>Use groups and lifecycle governance.</td><td>Long-term individual access exceptions.</td></tr>
        <tr><td>Link journey pain points to processes and KPIs.</td><td>Customer journey maps that never change internal processes.</td></tr>
        <tr><td>Use dedicated technical users for integrations.</td><td>Sharing one human or technical account across several integrations.</td></tr>
        <tr><td>Define the system of record for synchronized data.</td><td>Treating connectors as unrestricted symmetric replication.</td></tr>
      </tbody>
    </table>

    <h2 id="assessment">16. Lead-level decision guide</h2>

    <table class="study-table">
      <thead>
        <tr><th>Question</th><th>Short answer</th></tr>
      </thead>
      <tbody>
        <tr><td>Process Modeler or Process Intelligence?</td><td>Designed process vs observed execution.</td></tr>
        <tr><td>Process Modeler or Process Governance?</td><td>Process content/model vs executable governance workflow.</td></tr>
        <tr><td>BPMN or DMN?</td><td>Activity flow vs decision logic.</td></tr>
        <tr><td>Navigation Map or Value Chain?</td><td>User-friendly entry vs structured high-level process architecture.</td></tr>
        <tr><td>QuickModel or Graphical Editor?</td><td>Fast simple capture vs detailed BPMN logic.</td></tr>
        <tr><td>Local attribute or Dictionary?</td><td>Diagram-specific fact vs shared governed business object.</td></tr>
        <tr><td>Simulation or Process Intelligence?</td><td>What could happen vs what did happen.</td></tr>
        <tr><td>Journey or process?</td><td>Outside-in experience vs inside-out execution.</td></tr>
        <tr><td>Process Governance or Transformation Manager?</td><td>Repeatable workflow execution vs improvement initiative management.</td></tr>
        <tr><td>License or permission?</td><td>Product entitlement vs authorization to features/content/data.</td></tr>
        <tr><td>Template variant or detached process?</td><td>Keep standard alignment while it adds value; detach only for justified independent evolution.</td></tr>
        <tr><td>Connector direction?</td><td>Know the initial-load direction, ongoing ownership, supported content, and round-trip limits.</td></tr>
      </tbody>
    </table>

    <h3>Strong assessment answer pattern</h3>

    <p>For a broad Signavio design question, structure the answer in this order:</p>

    <ol>
      <li><strong>Purpose</strong> — what business problem are we solving?</li>
      <li><strong>Component</strong> — which Signavio product owns the capability?</li>
      <li><strong>Information model</strong> — process, decision, journey, workflow, or event data?</li>
      <li><strong>Governance</strong> — ownership, Dictionary, conventions, approvals, access, lifecycle.</li>
      <li><strong>Integration</strong> — source/target systems and system-of-record boundary.</li>
      <li><strong>Evidence</strong> — simulation, report, workflow history, or operational process data?</li>
      <li><strong>License</strong> — base product, separate product, workspace package, or additional entitlement?</li>
    </ol>

    <h2 id="current-state">17. Current-state notes for 2026</h2>

    <ul>
      <li>Current SAP documentation uses <strong>Process Modeler</strong>; older learning content commonly uses <strong>Process Manager</strong>.</li>
      <li>New Signavio workspaces use SAP Cloud Identity Services for identity management; workspaces created after May 6, 2026 manage users/groups there.</li>
      <li>Process Intelligence license is workspace-level; user access then depends on feature sets and data permissions.</li>
      <li>Process Insights capabilities are being consumed through the Process Intelligence direction/package in current SAP documentation.</li>
      <li>New Process Intelligence investigations cannot be created or imported since May 26, 2026; customizable dashboards are the forward path.</li>
      <li>Commercial scope changes faster than modeling concepts. Always verify the current Feature Scope Description and contract before promising a feature.</li>
    </ul>

    <h2 id="sources">18. Source register</h2>

    <ul>
      <li><a href="https://help.sap.com/docs/signavio-process-transformation-suite">SAP Signavio Process Transformation Suite — product documentation</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-transformation-suite/user-management-authentication-and-authorization/about-licenses">SAP Signavio — About Licenses</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-transformation-suite/user-management-authentication-and-authorization/harmonization-of-authentication-and-identity-management">SAP Signavio — Harmonization of Authentication and Identity Management</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-manager/fsd-process-manager/sap-signavio-process-manager">Process Modeler / Process Manager — Feature Scope Description</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-collaboration-hub/8b9170c598674518972c9236fa257a7b/a17911fa61884c4fb532988810ad05b8.html">Process Collaboration Hub — Feature Scope Description</a></li>
      <li><a href="https://help.sap.com/docs/signavio-journey-modeler/user-guide/intro">Journey Modeler — User Guide</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-governance/user-guide">Process Governance — User Guide</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-governance/implementation-guidelines">Process Governance — Implementation Guidelines</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-intelligence/user-guide/process-analysis">Process Intelligence — Process Analysis</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-intelligence/user-guide/about-investigations">Process Intelligence — Investigations and dashboard transition</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-insights/feature-scope-description/application-features-insights-and-intelligence-package">Process Insights and Intelligence package</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-transformation-manager">Process Transformation Manager — product documentation</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-transformation-suite/business-process-model-connector/business-process-model-connector-for-sap-signavio-solutions">Business Process Model Connector — overview</a></li>
      <li><a href="https://help.sap.com/docs/signavio-process-transformation-suite/business-process-model-connector/creating-synchronization-project">Business Process Model Connector — synchronization project</a></li>
      <li><a href="https://www.omg.org/spec/BPMN/2.0.2/PDF">OMG BPMN 2.0.2 specification</a></li>
    </ul>

    <p><strong>Verification boundary:</strong> this guide combines SAP Learning material used for assessment preparation with current public SAP documentation. The page explains product architecture and decision boundaries. Exact commercial scope, edition, package, regional availability, AI consumption, and licensed feature set must be checked against the customer's current SAP contract and Feature Scope Description.</p>

    <h2 id="glossary">19. Glossary</h2>

    <table class="study-table">
      <thead>
        <tr><th>Term</th><th>Meaning</th></tr>
      </thead>
      <tbody>
        <tr><td>Process Modeler</td><td>Current SAP Signavio product for process and decision modeling. Older material often calls it Process Manager.</td></tr>
        <tr><td>Process Manager</td><td>Earlier/current-learning name for the modeling product; still appears in SAP documentation and courses.</td></tr>
        <tr><td>Explorer</td><td>Repository and management area for process content, folders, search, revisions, reports, and related functions.</td></tr>
        <tr><td>Graphical Editor</td><td>Detailed modeling environment for BPMN, DMN, attributes, and other diagram types.</td></tr>
        <tr><td>QuickModel</td><td>Table-based way to create simple BPMN models quickly.</td></tr>
        <tr><td>BPMN</td><td>Business Process Model and Notation; standard notation for process flow.</td></tr>
        <tr><td>DMN</td><td>Decision Model and Notation; notation for decision requirements and decision logic.</td></tr>
        <tr><td>DRD</td><td>Decision Requirements Diagram; shows decision dependencies, inputs, and knowledge sources.</td></tr>
        <tr><td>Decision Table</td><td>Table that defines business rules from input conditions to outputs.</td></tr>
        <tr><td>Hit Policy</td><td>Rule that defines how a DMN table handles one or several matching rows.</td></tr>
        <tr><td>Token</td><td>Mental model for BPMN execution that moves through flows, tasks, gateways, and events.</td></tr>
        <tr><td>XOR Gateway</td><td>Exclusive gateway; routes one path.</td></tr>
        <tr><td>AND Gateway</td><td>Parallel gateway; activates all paths and synchronizes required tokens.</td></tr>
        <tr><td>OR Gateway</td><td>Inclusive gateway; activates one or several valid paths.</td></tr>
        <tr><td>Event-Based Gateway</td><td>Routes according to which external catching event occurs first.</td></tr>
        <tr><td>Pool</td><td>BPMN participant or organizational boundary.</td></tr>
        <tr><td>Lane</td><td>Responsibility partition inside a pool according to the modeling convention.</td></tr>
        <tr><td>Sequence Flow</td><td>Execution order inside one pool.</td></tr>
        <tr><td>Message Flow</td><td>Communication between different pools.</td></tr>
        <tr><td>Subprocess</td><td>Process detail grouped below or inside a parent process.</td></tr>
        <tr><td>Call Activity</td><td>BPMN element used to call reusable global process logic.</td></tr>
        <tr><td>Dictionary</td><td>Central repository of reusable business objects such as roles, systems, documents, risks, and controls.</td></tr>
        <tr><td>Dictionary Entry</td><td>One governed reusable business object in the Dictionary.</td></tr>
        <tr><td>Attribute</td><td>Structured metadata attached to a diagram, element, or Dictionary object.</td></tr>
        <tr><td>Overlay</td><td>Visual icon or color that exposes attribute information on a model.</td></tr>
        <tr><td>Modeling Convention</td><td>Organization-specific modeling rule checked in addition to BPMN syntax.</td></tr>
        <tr><td>Navigation Map</td><td>Flexible visual entry point into a process landscape.</td></tr>
        <tr><td>Value Chain</td><td>Structured high-level view of process groups and their relationships.</td></tr>
        <tr><td>Process Collaboration Hub</td><td>Consumption and collaboration surface for published process content.</td></tr>
        <tr><td>Published View</td><td>View of governed published content.</td></tr>
        <tr><td>Preview View</td><td>View of current content according to access rights, including working state.</td></tr>
        <tr><td>Audience</td><td>Viewer group used to tailor Hub presentation and visibility settings.</td></tr>
        <tr><td>Read Confirmation</td><td>Request for users to confirm that they read a process or revision.</td></tr>
        <tr><td>Process Rating</td><td>Structured user feedback on a process revision.</td></tr>
        <tr><td>Variant</td><td>Controlled variation of a process that remains related to a common template.</td></tr>
        <tr><td>Template</td><td>Main process model used as the governed base for variants.</td></tr>
        <tr><td>Dimension</td><td>Characteristic that differentiates process variants, represented through configured Dictionary categories.</td></tr>
        <tr><td>Variant Group</td><td>Template plus its related variants and dimensions.</td></tr>
        <tr><td>Simulation</td><td>What-if calculation using model assumptions such as time, cost, frequency, probability, and resources.</td></tr>
        <tr><td>Journey Modeler</td><td>Table-based outside-in modeling product for journeys, touchpoints, sentiments, processes, systems, and metrics.</td></tr>
        <tr><td>Persona</td><td>Representative person whose experience is modeled.</td></tr>
        <tr><td>Touchpoint</td><td>Direct or indirect interaction between the persona and the company, product, or channel.</td></tr>
        <tr><td>Sentiment</td><td>Recorded positive, neutral, or negative experience at a journey stage.</td></tr>
        <tr><td>Journey Complexity</td><td>Measure of operational complexity behind linked processes.</td></tr>
        <tr><td>Journey Model Dimensions</td><td>Measure of journey-table size and populated content.</td></tr>
        <tr><td>Process Governance</td><td>Workflow modeling and execution product for governed tasks, cases, approvals, and controls.</td></tr>
        <tr><td>Workflow</td><td>Executable template describing how repeatable work is assigned and completed.</td></tr>
        <tr><td>Case</td><td>One running instance of a Process Governance workflow.</td></tr>
        <tr><td>User Task</td><td>Task completed by one assigned person or role.</td></tr>
        <tr><td>Multi-User Task</td><td>Same task created for several users, in parallel or sequence.</td></tr>
        <tr><td>Trigger</td><td>Event or input that starts a workflow case.</td></tr>
        <tr><td>Process Intelligence</td><td>Process-mining and analysis product for operational process data.</td></tr>
        <tr><td>Process Insights</td><td>SAP-focused predefined performance and recommendation capabilities, now documented as available through the Process Intelligence direction/package.</td></tr>
        <tr><td>Process Transformation Manager</td><td>Product for benchmarking, insights, initiatives, objectives, tasks, and transformation management.</td></tr>
        <tr><td>Process Explorer</td><td>Entry point for value accelerators and transformation resources.</td></tr>
        <tr><td>Insight</td><td>Saved analytical finding or observation.</td></tr>
        <tr><td>Analysis Workflow</td><td>Process Intelligence automation that monitors process data and triggers actions when defined conditions are met.</td></tr>
        <tr><td>Feature Set</td><td>Authorization mechanism used to grant access to product capabilities.</td></tr>
        <tr><td>Tenant Owner</td><td>Initial workspace owner with broad administrative responsibility.</td></tr>
        <tr><td>Business Process Model Connector</td><td>BTP-based connector between SAP Signavio process information and SAP Solution Manager solution documentation.</td></tr>
        <tr><td>Synchronization Project</td><td>Connector configuration that defines one system pair, mappings, scope, and synchronization settings.</td></tr>
        <tr><td>Value Accelerator</td><td>Optional prebuilt content used to accelerate analysis, modeling, or transformation work.</td></tr>
      </tbody>
    </table>

  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-build/">SAP Build</a></li>
      <li><a href="/atlas/sap/sap-datasphere/">SAP Datasphere</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
