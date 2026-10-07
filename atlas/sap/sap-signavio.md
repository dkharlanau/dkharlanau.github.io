---
layout: default
title: "SAP Signavio"
description: "SAP Signavio Process Manager explained as a working system: Explorer, Editor, QuickModel, Dictionary, navigation maps, value chains, governance, publishing, simulation, reporting, and the boundary to Process Intelligence."
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
  - process-manager
  - process-mining
  - bpm
  - bpmn
  - dictionary
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
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP Signavio</h1>
    <p class="note-subtitle">A working model of how SAP Signavio Process Manager organizes, models, governs, publishes, and analyzes process knowledge — and how that designed process view differs from observed execution in Process Intelligence.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Process management</dd></div>
      <div><dt>Primary focus</dt><dd>Process Manager</dd></div>
      <div><dt>Assessment lens</dt><dd>Architecture, modeling, governance, analysis</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP documentation.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>SAP Signavio Process Manager is easier to understand as a system rather than as a list of buttons. A company needs to capture processes, organize them, reuse the same business language, control modeling quality, publish the content, collect feedback, and analyze possible improvements. Process Manager brings these tasks into one governed workspace.</p>

    <p>The main idea is simple: a process diagram is useful only when people can find it, understand it, trust its terminology, see who owns it, and use it to make a decision. Modeling is therefore only one part of process management.</p>

    <h2>Process Manager in one mental model</h2>

    <table class="study-table">
      <thead>
        <tr>
          <th>Capability</th>
          <th>Main job</th>
          <th>Typical question</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Explorer</td>
          <td>Organize and manage process content</td>
          <td>Where is the process, who can access it, and which version is current?</td>
        </tr>
        <tr>
          <td>Graphical Editor</td>
          <td>Create and maintain detailed diagrams</td>
          <td>How does the process work and is the model correct?</td>
        </tr>
        <tr>
          <td>QuickModel</td>
          <td>Capture a simple BPMN flow in a table</td>
          <td>How can we document the main path quickly?</td>
        </tr>
        <tr>
          <td>Dictionary</td>
          <td>Reuse centrally managed business objects</td>
          <td>Are we using the same role, system, document, or term everywhere?</td>
        </tr>
        <tr>
          <td>Process Collaboration Hub</td>
          <td>Publish and consume process content</td>
          <td>How do process viewers find, read, and discuss the published process?</td>
        </tr>
        <tr>
          <td>Simulation and reporting</td>
          <td>Analyze modeled processes</td>
          <td>What does the model imply and what information can we aggregate?</td>
        </tr>
      </tbody>
    </table>

    <p>A useful Lead-level distinction is therefore: <strong>Explorer manages the process landscape; Editor builds the model; Dictionary standardizes shared objects; Collaboration Hub exposes published content to consumers; analysis functions help evaluate the modeled process.</strong></p>

    <p>Process Manager also supports collaboration and feedback. A commenting feature lets users discuss process content and provide feedback instead of treating the diagram as a static document.</p>

    <h2>The Explorer: manage the process landscape</h2>

    <p>The Explorer is the entry and management point of Process Manager. It provides the folder tree, search, diagram repository, diagram details, and access to other functions. From here, users can create or open diagrams, manage files, publish content, export diagrams, generate reports, and access analysis functions.</p>

    <p>Its two main jobs are <strong>content management</strong> and <strong>content analysis</strong>.</p>

    <h3>Managing content</h3>
    <ul>
      <li>Create a folder structure that reflects the organization or process architecture.</li>
      <li>Save, copy, delete, and move diagrams.</li>
      <li>Control access rights through the workspace access concept; access rights are assigned by the workspace administrator.</li>
      <li>Share or publish diagrams to SAP Signavio Process Collaboration Hub.</li>
      <li>Use the Dictionary to enrich models with centrally managed business objects.</li>
      <li>Manage and restore diagram revisions.</li>
      <li>Import and export diagrams.</li>
    </ul>

    <h3>Analyzing content</h3>
    <ul>
      <li>Create standard reports from selected processes.</li>
      <li>Simulate process instances.</li>
      <li>Compare process diagrams and use comparison to contrast states such as As-Is and To-Be.</li>
    </ul>

    <h3>Folder structure is a governance decision</h3>
    <p>A functional or divisional structure can work well, but the correct design depends on how the company manages ownership and access. A practical pattern is to place department folders under a common parent so that access rights can be assigned at the parent level instead of being maintained repeatedly.</p>

    <p>Sensitive processes should be separated from general process content. For example, budgeting or strategic planning can sit in a dedicated parent folder that is visible only to an authorized group. The folder structure is therefore not only navigation; it is part of the access model.</p>

    <h3>Search depends on metadata quality</h3>
    <p>Advanced Search can filter by standard and custom attributes. This makes attributes important outside the model itself. A useful filter is the publishing state, especially when several variants or revisions of a process exist.</p>

    <h2>The Graphical Editor: model and enrich processes</h2>

    <p>The Graphical Editor is the main modeling environment. BPMN 2.0 is central for business process modeling, but the editor also supports other diagram types. The learning material highlights DMN 1.2 for decision logic and ArchiMate 3.0 for enterprise architecture, together with navigation maps and value chains for higher-level views.</p>

    <p>The important point for an SAP Lead is not the number of supported notations. It is the separation of concerns: <strong>BPMN explains process flow, DMN explains decision logic, and ArchiMate can describe architecture around the process.</strong></p>

    <h3>Attributes add business context</h3>
    <p>A process diagram shows the flow. Attributes add information such as descriptions, responsibilities, systems, documents, risks, or other organization-specific details. Workspace administrators can define custom attributes and rules for their visualization.</p>

    <p>Attributes are reusable operational metadata. They can support filtering in the Explorer, reporting, documentation, and governance. A diagram with good visual flow but weak metadata may still be difficult to govern at scale.</p>

    <p>Administrators can also define how custom attributes are visualized. Modelers can assign the attributes in the Editor, while their configured icons can be shown to process consumers in Process Collaboration Hub.</p>

    <h3>Syntax checks and convention checks solve different problems</h3>

    <table class="study-table">
      <thead>
        <tr>
          <th>Check</th>
          <th>What it validates</th>
          <th>Example</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Syntax</td>
          <td>Correct use of the notation</td>
          <td>Elements are connected and BPMN rules are respected.</td>
        </tr>
        <tr>
          <td>Convention</td>
          <td>Organization-specific modeling standards</td>
          <td>Naming, required attributes, layout, or allowed modeling patterns.</td>
        </tr>
      </tbody>
    </table>

    <p>Syntax correctness is important for consistent models and for downstream capabilities such as reporting and simulation. Convention checks add a second governance layer. SAP Signavio provides best-practice conventions, while administrators can customize or define additional rules for the workspace.</p>

    <p>The checks run when a model is saved, and users can also start them with the Review function. Errors, warnings, and hints help the modeler understand what needs attention. Where guideline information is available, the result panel can link the modeler to the relevant guidance.</p>

    <h3>Model translation avoids duplicate process copies</h3>
    <p>If several languages are enabled in the workspace, the same process can be maintained in multiple languages. Users can switch language and translate the model instead of creating separate diagram copies. The learning material also describes automatic translation options. This reduces duplicate maintenance and helps keep one governed process definition.</p>

    <h2>QuickModel: capture the happy path first</h2>

    <p>QuickModel is a table-based way to create BPMN 2.0 diagrams. The modeler enters process information into rows and columns while the system generates the basic process diagram. This gives users who do not fully master BPMN a simple way to create a compliant starting model while they focus on process information rather than graphical notation. The table can also expose selected attributes as columns.</p>

    <p>QuickModel works well for initial modeling, workshops, and the main sequence of activities. It is especially useful for a <strong>happy path</strong>: the normal sequence without exceptions or complex branching.</p>

    <p>Its limit is also important. Once the process needs gateways, parallel paths, subprocesses, or other complex BPMN structures, the work should move to the Graphical Editor. A good modeling approach is therefore:</p>

    <ol>
      <li>Capture the main sequence and key attributes quickly.</li>
      <li>Document missing decisions or exceptions.</li>
      <li>Move to the Graphical Editor when the process needs richer BPMN logic.</li>
    </ol>

    <p>This is a useful facilitation pattern because it separates <strong>process discovery</strong> from <strong>notation detail</strong>.</p>

    <h2>The Dictionary: one shared business vocabulary</h2>

    <p>The Dictionary is the central object repository of Process Manager. It prevents teams from redefining the same business objects independently in many process models. Common entries can represent organizational responsibilities, IT systems, applications, documents, activities, events, or other reusable business concepts.</p>

    <p>In the Explorer, Dictionary parent categories and subcategories are shown as the organizing structure, while the entries inside the selected category represent the reusable business objects. This makes the Dictionary both a vocabulary and a traceable repository.</p>

    <p>The core value is reuse. A role, system, or document can be created once and linked from many models. This gives the process landscape a shared vocabulary and makes the usage of an object traceable across diagrams.</p>

    <h3>Create and link entries</h3>
    <p>Modelers can view and reuse Dictionary content. Additional permissions are required to create or manage entries. New entries can be created directly in the Dictionary or while modeling in the Editor, depending on permissions and workspace configuration.</p>

    <p>Documents and images that belong to a reusable business object should be linked to the Dictionary entry rather than copied independently into many process models. This keeps the supporting information close to the governed object.</p>

    <h3>Avoid duplicates before creating new objects</h3>
    <p>When a new entry is created, the Dictionary can warn that an entry with the same name already exists. Duplicate names are technically possible, but they weaken governance. Search first, reuse when possible, and create a new object only when it is genuinely different. If the exact name is unknown, the learning material shows that entering <code>**</code> in the search field lists all entries in the selected category.</p>

    <h3>Dictionary entries can carry custom attributes</h3>
    <p>Dictionary entries can be enriched with additional information through custom attributes defined by the workspace administrator. This is useful when the shared object needs governed metadata beyond its title or standard properties.</p>

    <h3>Use Dictionary entries from QuickModel</h3>
    <p>The Dictionary is not limited to the Graphical Editor. In QuickModel, typing in an activity attribute field can suggest existing Dictionary entries from the matching category. Additional columns can be added to reach entries from other categories. This keeps fast table-based capture connected to the same governed vocabulary.</p>

    <h3>Local diagram change vs central Dictionary change</h3>
    <p>This is an important ownership boundary. A change made to attributes while modeling can affect only that diagram. A change made to the underlying Dictionary entry is a central change and applies to linked process models.</p>

    <p>Before editing a Dictionary object, ask: <strong>am I changing this one diagram, or am I changing the shared business definition?</strong> The second action has a wider impact and should follow governance rules.</p>

    <h3>Use clear Dictionary ownership</h3>
    <p>A central repository needs accountable owners. A small responsible group can maintain terminology, review proposed objects, correct duplicates, and keep categories usable. Giving every modeler unrestricted productive maintenance rights usually increases inconsistency over time.</p>

    <h3>The sandbox approach balances contribution and control</h3>
    <p>A practical governance pattern is to create sandbox subcategories. The learning material recommends a sandbox for each Dictionary parent category, with modeler access controlled by an appropriate administrator-defined access concept. Modelers can propose missing entries there without directly changing productive Dictionary categories. Dictionary owners then review proposals, approve useful entries, and move them into the correct productive category.</p>

    <p>The sandbox is therefore not only a temporary folder. It is a controlled intake mechanism: contribution stays open, while productive terminology remains governed.</p>

    <h3>Bulk maintenance with Excel</h3>
    <p>For large maintenance tasks, Dictionary entries can be exported to an XLS or XLSX file, edited in bulk, and imported again. During import, categories and attributes must be mapped correctly. This is useful when many entries need to be created or adjusted, but it also increases the need for ownership and review.</p>

    <h3>Merge duplicate entries</h3>
    <p>If duplicate Dictionary entries are found, the Merge function can combine them into a target entry. During the merge, the responsible user can decide which information should be retained in the target entry. This is an important cleanup capability because duplicate objects weaken reuse, reporting, and consistent process language.</p>

    <h2>Navigation Maps and Value Chains: two different high-level views</h2>

    <p>Both navigation maps and value chains can provide an entry point into a process landscape, but they solve different communication problems.</p>

    <table class="study-table">
      <thead>
        <tr>
          <th>View</th>
          <th>Main purpose</th>
          <th>Best use</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Navigation Map</td>
          <td>Create a flexible, visual entry point</td>
          <td>Company-on-a-page views, customer journeys, branded navigation, user-friendly process portals.</td>
        </tr>
        <tr>
          <td>Value Chain</td>
          <td>Show high-level process architecture and sequence</td>
          <td>End-to-end process groups, business-unit process structure, hierarchical process landscapes.</td>
        </tr>
      </tbody>
    </table>

    <p>A navigation map can use shapes, text boxes, and images. Shapes can be customized through properties such as size, description, color, gradient, stroke, and flat design, and administrators can provide custom attributes. Elements and uploaded images can link to diagrams, workspace folders, URLs, and Dictionary entries. Dictionary links can also be assigned to images, shapes, and text boxes. The goal is usability: help process consumers enter the process world without opening a detailed BPMN diagram first.</p>

    <p>A value chain is more structured. Each element can represent a process or process group, and the elements can be linked in chronological order to show high-level and hierarchical relationships. Many of the same modeling options used for navigation maps also apply here, including links, images, custom attributes, and Live Insights. Navigation maps and value chains can also be connected to each other, which makes it possible to build a clear hierarchy from company-level view down to detailed process models.</p>

    <h3>Live Insights connect the map to analytics</h3>
    <p>Live Insights can place analytics or KPI information from SAP Signavio Process Intelligence into a navigation map or value chain. This moves the high-level map from static navigation toward operational awareness. Visibility depends on authorization, and the feature requires the relevant Process Intelligence license.</p>

    <h2>A practical process architecture</h2>

    <p>One useful way to structure a large process landscape is:</p>

    <ol>
      <li><strong>Navigation Map</strong> — user-friendly entry point.</li>
      <li><strong>Value Chain</strong> — high-level process architecture.</li>
      <li><strong>BPMN process</strong> — detailed flow, responsibilities, decisions, and handoffs.</li>
      <li><strong>Dictionary objects</strong> — shared roles, systems, documents, and business terms.</li>
      <li><strong>Attributes and conventions</strong> — governance metadata and modeling quality.</li>
      <li><strong>Collaboration Hub</strong> — published process consumption and feedback.</li>
      <li><strong>Reporting and simulation</strong> — analysis of the modeled process.</li>
    </ol>

    <p>This hierarchy separates navigation, architecture, detailed process logic, and reusable enterprise objects. It also makes ownership clearer: changing the entry page is not the same as changing the process, and changing one process is not the same as changing a shared Dictionary object.</p>

    <h2>Designed process vs observed process</h2>

    <p>Process Manager mainly helps describe and govern how work is intended to run. Process Intelligence answers a different question: <strong>what actually happened in execution data?</strong></p>

    <p>Process Intelligence analyzes event data from source systems. A process-data model needs a correct case definition, activities, timestamps, attributes, and metrics. If these semantics are wrong, the analysis can be visually convincing while describing the wrong business process.</p>

    <table class="study-table">
      <thead>
        <tr>
          <th>Designed process</th>
          <th>Observed process</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Target flow, ownership, policy, controls, documentation</td>
          <td>Actual variants, timing, deviations, attributes, outcomes</td>
        </tr>
        <tr>
          <td>Process Manager</td>
          <td>Process Intelligence</td>
        </tr>
        <tr>
          <td>What should happen?</td>
          <td>What did happen?</td>
        </tr>
      </tbody>
    </table>

    <p>Neither view replaces the other. If the model is wrong, the design needs to change. If execution differs, the team must determine whether the variation is valid, caused by data or configuration, or evidence of a real process problem.</p>

    <h2>Lead decisions to remember</h2>

    <table class="study-table">
      <thead>
        <tr>
          <th>Question</th>
          <th>Decision</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Explorer or Editor?</td>
          <td>Use Explorer to manage and analyze content; use Editor to model and enrich diagrams.</td>
        </tr>
        <tr>
          <td>QuickModel or Graphical Editor?</td>
          <td>Use QuickModel for fast, simple, table-based capture; switch to the Editor for complex BPMN logic.</td>
        </tr>
        <tr>
          <td>Syntax or convention issue?</td>
          <td>Syntax is notation correctness; conventions are modeling standards and governance rules.</td>
        </tr>
        <tr>
          <td>Local change or Dictionary change?</td>
          <td>Change the diagram for local information; change the Dictionary when the shared business object itself is changing.</td>
        </tr>
        <tr>
          <td>Navigation Map or Value Chain?</td>
          <td>Use Navigation Maps for user-friendly entry and storytelling; use Value Chains for high-level process architecture.</td>
        </tr>
        <tr>
          <td>Process Manager or Process Intelligence?</td>
          <td>Use the model to define and govern intended work; use event data to investigate actual execution.</td>
        </tr>
      </tbody>
    </table>

    <h2>Assessment answer pattern</h2>

    <p>For a Lead-level question about process management, a strong answer should connect five layers:</p>

    <ol>
      <li><strong>Architecture</strong> — how people enter and navigate the process landscape.</li>
      <li><strong>Modeling</strong> — how the process flow and decisions are represented.</li>
      <li><strong>Governance</strong> — how terms, attributes, access, versions, and conventions stay consistent.</li>
      <li><strong>Consumption</strong> — how users see published process content and provide feedback.</li>
      <li><strong>Improvement</strong> — how reporting, simulation, comparison, and execution data support better decisions.</li>
    </ol>

    <p>A concise answer can be: “I would define the process architecture first, model detailed flows in BPMN, use the Dictionary for shared business objects, apply conventions and access rules for governance, publish the process content for process consumers, and then use analysis or execution data to identify improvement opportunities.”</p>

    <h2>Operational details from the learning material</h2>

    <ul>
      <li>Navigation Map images are uploaded through Image Management and use SVG format. The training material states that modelers can upload images there, with a 50 KB limit, while images provided through administrator setup use a separate 20 KB limit.</li>
      <li>Administrator setup does not support bulk image uploads, and uploaded images can only be deleted by workspace administrators.</li>
      <li>Uploaded images are checked for possible security vulnerabilities and may require approval before they become available.</li>
      <li>After saving a Navigation Map, preview it in Process Collaboration Hub and test the links.</li>
      <li>QuickModel is intended for BPMN process capture; more complex elements are added later in the Graphical Editor. Gateway or other missing logic can first be recorded in documentation for a more experienced modeler to incorporate later.</li>
      <li>Bulk Dictionary maintenance uses Excel import/export and requires correct category and attribute mapping.</li>
      <li>Dictionary sandbox proposals should be reviewed regularly and moved to productive categories only after approval.</li>
    </ul>

    <h2>Current product boundary</h2>

    <p>SAP Signavio is a suite rather than one monolithic runtime. Product capabilities, licenses, APIs, and workspace behavior can change independently. A solution design should name the exact Signavio component and verify the licensed feature set instead of using “Signavio” as if every capability were always present.</p>

    <p>Current SAP documentation also reflects ongoing changes in Process Intelligence terminology. Older material may refer to investigations, while SAP has been moving this area toward customizable dashboards. The stable concept is more important than the historical UI name: execution analysis starts from event data and must be interpreted against the correct process semantics.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Signavio Process Manager — <a href="https://help.sap.com/docs/signavio-process-manager/user-guide/fa78b95c6dad1014a4730ff5fb2ca89e.html">Explorer Overview</a>.</li>
      <li>SAP Signavio Process Manager — <a href="https://help.sap.com/doc/10ae12665b494798a8a332bcc195689d/SHIP/en-US/sap-signavio-process-manager-user-guide-en.pdf">Process Manager User Guide</a>.</li>
      <li>SAP Signavio Process Manager — <a href="https://help.sap.com/doc/126253d0517d4ae9afffd4d1c7a01c63/SHIP/en-US/sap-signavio-process-manager-workspace-admin-guide-en.pdf">Workspace Admin Guide</a>.</li>
      <li>SAP Signavio Process Manager — <a href="https://help.sap.com/docs/signavio-process-manager/user-guide/fa8963fa6dad1014a4730ff5fb2ca89e.html">Navigation Map Elements</a>.</li>
      <li>SAP Signavio Process Intelligence — <a href="https://help.sap.com/docs/signavio-process-intelligence/onboarding-and-data-integration-guide/creating-customizable-data-connections">Creating Customizable Data Connections</a>.</li>
      <li>SAP Signavio Process Intelligence — <a href="https://help.sap.com/docs/signavio-process-intelligence/user-guide/about-investigations">Investigations and dashboard transition</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page combines current public SAP documentation with SAP Learning material used for assessment preparation. Product scope, licensing, UI behavior, limits, APIs, workspace administration, and terminology can change. Verify the documentation for the specific Signavio product, tenant, and release before using this page as implementation guidance.</p>
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
