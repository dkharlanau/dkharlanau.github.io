---
layout: default
title: "SAP Signavio"
description: "SAP Signavio explained as a working process system: Process Manager modeling and governance, BPMN practice, simulation, reporting, variants, executable governance workflows, and the boundary to Process Intelligence."
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
  - simulation
  - reporting
  - process-variants
  - bpmn-modeling
  - gateways
  - events
  - subprocesses
  - administration
  - access-control
  - security
  - user-management
  - dmn
  - decision-modeling
  - business-decision-management
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
    <p class="note-subtitle">A working model of how SAP Signavio models and governs process knowledge, executes governance workflows, and separates designed-process assumptions from observed execution data.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Process management</dd></div>
      <div><dt>Primary focus</dt><dd>Process Manager and Process Governance</dd></div>
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
          <td>DMN decision modeling</td>
          <td>Separate decision requirements and decision logic from process flow</td>
          <td>What information, rules, and authorities determine a business decision?</td>
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
          <td>Simulation</td>
          <td>Run what-if scenarios on the designed BPMN process</td>
          <td>What happens to cost, cycle time, capacity, or bottlenecks if assumptions change?</td>
        </tr>
        <tr>
          <td>Reporting</td>
          <td>Aggregate model, attribute, responsibility, system, document, risk, and governance data</td>
          <td>What can we learn across one or many process models?</td>
        </tr>
        <tr>
          <td>Variant Management</td>
          <td>Control template-to-variant relationships</td>
          <td>How do we keep a standard core while allowing justified local differences?</td>
        </tr>
        <tr>
          <td>Process Governance</td>
          <td>Configure and execute governed workflows</td>
          <td>How do approvals, tasks, reminders, escalations, and controlled handovers actually run?</td>
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

    <h2>BPMN modeling practice: build a model that behaves correctly</h2>

    <p>BPMN 2.0 is the common process-modeling notation used throughout these examples. The course frames it as more than a drawing language: a useful model must be syntactically correct, semantically correct, and understandable to its audience.</p>

    <table class="study-table">
      <thead>
        <tr>
          <th>Quality dimension</th>
          <th>Main question</th>
          <th>Who can check it?</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Syntax</td>
          <td>Are BPMN elements connected and used according to notation rules?</td>
          <td>The modeling tool can check many syntax problems.</td>
        </tr>
        <tr>
          <td>Semantics</td>
          <td>Are the tasks, order, responsibilities, conditions, and outcomes correct for the real business process?</td>
          <td>People with process knowledge.</td>
        </tr>
        <tr>
          <td>Understandability</td>
          <td>Can the intended audience follow the model without unnecessary confusion?</td>
          <td>Process viewers and reviewers.</td>
        </tr>
      </tbody>
    </table>

    <p>This creates an important design rule: <strong>business complexity does not justify visual complexity</strong>. Keep the process flow easy to follow, reduce crossing lines, align tasks and flows, use color and annotations carefully, and show only the level of detail required by the target group. Management may need a high-level process, while implementation teams may need a much more precise model.</p>

    <h3>Core BPMN building blocks</h3>

    <p>The course groups the basic modeling language into four areas: <strong>flow objects</strong>, <strong>connecting objects</strong>, <strong>artifacts</strong>, and <strong>responsibilities</strong>. At the simplest level, a process needs a start event, sequence flow, tasks, and an end event.</p>

    <p>Read a process from left to right and top to bottom. A start event describes the trigger, tasks describe work, sequence flows define the order of execution, and the end event describes the state reached when the process goal is achieved.</p>

    <h3>The token concept explains process behavior</h3>

    <p>A useful mental model is to imagine a token moving through the process. Tasks hold the token while work is performed. Splits can create or route tokens, joins can synchronize them, and events can make them wait or react. The token must be able to reach a valid process end.</p>

    <p>This concept is useful even when the BPMN diagram is not technically executed. SAP Signavio uses the same execution logic for syntax checks and simulations, and it is the easiest way to understand deadlocks, duplicate execution, parallel behavior, and event waiting.</p>

    <h3>Name tasks and events differently</h3>

    <p>Tasks describe action and should normally use active wording such as <strong>Create invoice</strong>: verb plus business object. Events describe a state or something that happened, for example <strong>Order received</strong> or <strong>Invoice created</strong>. Start events should make the trigger clear; end events should make the achieved state clear.</p>

    <p>These naming patterns are presented as BPMN modeling best practices rather than absolute syntax rules. A justified deviation can be acceptable if the model remains meaningful and consistent.</p>

    <h2>Responsibilities: Pools, Lanes, and additional participants</h2>

    <p>A pool normally represents the organization or process participant within which the process is modeled. Lanes divide that pool into responsibilities such as process roles, departments, organizational units, or positions. A task placed in a lane is owned by that lane's responsibility.</p>

    <p>A sequence flow that moves from one lane to another is therefore also a handover of execution responsibility. This makes lane design important for communication and ownership analysis.</p>

    <p>More than one participant can be involved in a task, but one main responsibility should still own it. SAP Signavio provides an additional-participant element for this purpose; the course explicitly notes that this is SAP Signavio-specific and not part of the official BPMN 2.0 element set.</p>

    <p>For maintainability, prefer process-related roles or organizational responsibilities over named people. A person's name changes more often than the process role and increases maintenance across all affected models.</p>

    <h2>Gateways: route and synchronize tokens correctly</h2>

    <table class="study-table">
      <thead>
        <tr>
          <th>Gateway</th>
          <th>Split behavior</th>
          <th>Join behavior</th>
          <th>Use when</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>XOR / Exclusive</td>
          <td>Exactly one path is selected.</td>
          <td>Alternative paths are merged without synchronization.</td>
          <td>The result is either/or.</td>
        </tr>
        <tr>
          <td>AND / Parallel</td>
          <td>All outgoing paths are activated.</td>
          <td>Waits for all required incoming tokens.</td>
          <td>Independent work must all be completed.</td>
        </tr>
        <tr>
          <td>OR / Inclusive</td>
          <td>One or several paths can be activated.</td>
          <td>Waits only for the tokens that were actually activated.</td>
          <td>Several optional combinations are valid, with at least one selected.</td>
        </tr>
      </tbody>
    </table>

    <h3>An XOR gateway is not the business decision</h3>

    <p>A gateway is a routing control, not a task. For example, <strong>Select meal</strong> is the decision task; the following XOR gateway reads that result and routes the token. A person cannot own the gateway itself, and placing a gateway inside a lane does not make that lane responsible for a decision that was never modeled.</p>

    <p>For XOR naming, the course recommends a question on the splitting gateway, mutually exclusive answers on the outgoing sequence flows, and no label on the merging gateway.</p>

    <h3>Split and join consistently</h3>

    <p>The course recommends pairing a split with the corresponding merge when the branches later return to one flow. This keeps token behavior explicit and the diagram easier to maintain. An XOR split does not always require a join in the BPMN standard — for example, branches may end at different end events — but an explicit merge is recommended where paths logically come back together.</p>

    <h3>Parallel work only reduces time when resources are actually parallel</h3>

    <p>An AND split makes tasks independent, but it does not create extra people. If two parallel tasks belong to one resource, that person still performs them one after another. Cycle-time reduction becomes possible when separate resources can really work at the same time. The AND join then waits until all parallel work is complete.</p>

    <h3>Two flow errors to recognize immediately</h3>

    <table class="study-table">
      <thead>
        <tr>
          <th>Error</th>
          <th>Token problem</th>
          <th>Typical cause</th>
          <th>Correction</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Deadlock</td>
          <td>A synchronizing join waits for a token that will never arrive.</td>
          <td>An AND join receives branches that were not all created by the preceding logic.</td>
          <td>Correct the branch structure, for example by adding the missing XOR merge before synchronization.</td>
        </tr>
        <tr>
          <td>Multi-merge</td>
          <td>Several tokens continue independently and execute the same downstream task more than once.</td>
          <td>Parallel tokens are merged with logic that does not synchronize them.</td>
          <td>Add the missing AND join to synchronize the tokens into one continuation.</td>
        </tr>
      </tbody>
    </table>

    <p>SAP Signavio Process Manager's Graphical Editor checks for deadlocks and multi-merges and can show where they occur. The token concept explains why the error exists instead of treating the warning as an arbitrary modeling rule.</p>

    <h2>Events: model states, waiting, and external triggers</h2>

    <p>Events mark states in a process and allow the process to react to its environment. Three questions help select the right event: <strong>where</strong> is it used — start, intermediate, or end; <strong>how</strong> does it behave — catching or throwing; and <strong>what type</strong> of trigger or state does it represent?</p>

    <table class="study-table">
      <thead>
        <tr>
          <th>Event position</th>
          <th>Basic behavior</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Start event</td>
          <td>Represents the process trigger and has an outgoing sequence flow.</td>
        </tr>
        <tr>
          <td>Intermediate event</td>
          <td>Appears inside the process; a plain intermediate event has incoming and outgoing flow and can mark a milestone.</td>
        </tr>
        <tr>
          <td>End event</td>
          <td>Represents the reached process state or goal and has incoming flow only.</td>
        </tr>
      </tbody>
    </table>

    <p><strong>Catching</strong> events wait for something to happen. <strong>Throwing</strong> events produce or signal something. Start events are catching; end events are throwing.</p>

    <h3>Common event types</h3>

    <table class="study-table">
      <thead>
        <tr>
          <th>Type</th>
          <th>Main meaning</th>
          <th>Important boundary</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Message</td>
          <td>Interaction such as receiving or sending information, goods, files, or another external signal.</td>
          <td>A catching message can make the process wait; a throwing message can represent that something was sent.</td>
        </tr>
        <tr>
          <td>Timer</td>
          <td>React to a fixed, recurring, relative, or delayed point in time.</td>
          <td>Timer events are catching because the process cannot control time.</td>
        </tr>
        <tr>
          <td>Conditional</td>
          <td>React when an external condition becomes true.</td>
          <td>Conditional events are catching because the process does not control when the condition occurs.</td>
        </tr>
        <tr>
          <td>Link</td>
          <td>Technical connection that can replace a long sequence-flow line.</td>
          <td>Matching link events must use the same name; they add structure, not business meaning.</td>
        </tr>
      </tbody>
    </table>

    <p>A throwing intermediate message event can itself express the state that a message was sent. Modeling both an equivalent send task and the throwing message event can duplicate the action, so the modeler must be clear about what each element represents.</p>

    <h3>Attached events can interrupt or create an additional path</h3>

    <p>An attached catching intermediate event can be used as a cancel condition for a task or subprocess, with an alternative path for the exception. Examples include a timeout or an external condition. The course also shows a <strong>non-interrupting</strong> attached message event: the dashed boundary event does not cancel the subprocess; it creates an additional token so the process can react while the original work continues.</p>

    <h3>Event-based gateway: react to whichever external event happens first</h3>

    <p>An event-based gateway is used when the decision is made outside the process. The token waits for the connected catching intermediate events, and the first event that occurs determines the path. This is useful for scenarios such as waiting for payment while also handling reminder deadlines or cancellation conditions.</p>

    <p>Only catching intermediate events belong after an event-based gateway because the process is waiting to react.</p>

    <h2>Subprocesses: control the level of detail</h2>

    <p>Subprocesses solve a common modeling problem: some activities need much more detail than the main process should display. The main diagram can stay focused on its core facts while detailed steps move into another level.</p>

    <h3>Collapsed subprocess: hide detail behind a process step</h3>

    <p>A collapsed subprocess is shown as one process element with a plus marker. Detailed steps can be moved into a separate process diagram. In SAP Signavio, selecting elements and transforming them into a subprocess can create the new subprocess file directly in the Explorer.</p>

    <p>A subprocess element can be linked either to a newly created process diagram or to an existing process model in the workspace. The system itself does not automatically classify a file as “main process” or “subprocess,” so a clear naming convention can help users recognize its purpose.</p>

    <h3>Reusable global process: use a Call Activity</h3>

    <p>If the same detailed process is needed in several main processes, reuse it instead of modeling it several times. The course represents this reusable global reference as a <strong>Call Activity</strong> with a bold border. Examples such as Product Sourcing or Financial Handling can then be called from Order Handling, Stock Management, Repair, or other processes.</p>

    <p>This creates three benefits: lower modeling effort, stronger process harmonization, and one maintained source for the reusable process logic.</p>

    <h3>Expanded subprocess: local grouping, not reusable global logic</h3>

    <p>An expanded subprocess shows its internal tasks directly inside the parent model. It is useful when several tasks belong to one intermediate goal and should be visually grouped without losing their relationship to the main process. In the course framing, an expanded subprocess belongs to that particular process scenario and is not reused as a separate global model.</p>

    <table class="study-table">
      <thead>
        <tr>
          <th>Pattern</th>
          <th>Detail location</th>
          <th>Reuse</th>
          <th>Use when</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Collapsed subprocess</td>
          <td>Behind the subprocess element / linked detailed model</td>
          <td>Can link to a dedicated model</td>
          <td>The main diagram should stay compact.</td>
        </tr>
        <tr>
          <td>Call Activity</td>
          <td>Referenced global process</td>
          <td>Designed for reuse across processes</td>
          <td>The same process logic appears in several parent processes.</td>
        </tr>
        <tr>
          <td>Expanded subprocess</td>
          <td>Visible inside the parent process</td>
          <td>Local to that process scenario</td>
          <td>A group of tasks needs one visible intermediate context.</td>
        </tr>
      </tbody>
    </table>

    <h2>Process interactions: use Pools and Message Flows for externals</h2>

    <p>An external participant can be modeled as a collapsed pool and treated as a black box. The internal process of that participant is not shown; only the interaction with it matters.</p>

    <p>The BPMN boundary is strict: <strong>sequence flows stay inside a pool; message flows cross between pools</strong>. Message flows are for communication between process participants. They are not used as an internal substitute for sequence flow.</p>

    <p>This distinction is useful in integration discussions. A process handoff inside one organizational process is different from a message exchanged across participant boundaries.</p>

    <h3>When to use a correspondence diagram</h3>

    <p>Model several interacting processes in one diagram only when task-level interaction is important, the processes are not too complex, and the result remains easy to follow. Showing every interacting process together can make the model harder to understand than the process itself.</p>

    <p>For a Lead, this is a scope decision: show enough cross-participant behavior to explain the contract and timing, but avoid turning one diagram into the entire enterprise landscape.</p>

    <h2>IT systems and Data Objects: enrich the process without hiding the flow</h2>

    <p>BPMN provides <strong>Data Objects</strong> as standard elements for information or documents used or created in the process. A data object may represent physical documents, digital data, or abstract information and is connected to activities through data associations.</p>

    <p>SAP Signavio also provides an <strong>IT System</strong> element as a custom modeling element. It indicates that an application or system supports particular process steps and is connected to activities by associations.</p>

    <table class="study-table">
      <thead>
        <tr>
          <th>Element</th>
          <th>Standard status</th>
          <th>What it communicates</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Data Object</td>
          <td>BPMN standard element</td>
          <td>Information or a document consumed or produced by process work.</td>
        </tr>
        <tr>
          <td>IT System object</td>
          <td>SAP Signavio custom element</td>
          <td>An application or system supporting one or more process steps.</td>
        </tr>
      </tbody>
    </table>

    <p>Use these elements moderately. Too many data and system artifacts can hide the actual process flow.</p>

    <h3>A lane can represent more than a department</h3>

    <p>The course notes that BPMN does not prescribe one fixed semantic meaning for lanes. A modeling convention can use lanes for roles, departments, positions, systems, or applications. For example, a CRM system can have a lane when the model needs to show system-performed communication and data handling.</p>

    <p>When the system's internal logic is unknown or not needed, model the human-system interaction without inventing the system's internal process.</p>

    <h2>BPMN practice drill: Order Processing in three iterations</h2>

    <p>The learning exercises build one order process in stages. This is a useful review pattern because each stage adds one modeling problem instead of changing everything at once.</p>

    <ol>
      <li><strong>Part 1 — flow control:</strong> model order processing with responsibilities, one XOR decision for shipment treatment, and an AND pattern for work that can proceed independently.</li>
      <li><strong>Part 2 — events:</strong> move invoice responsibility to Finance, require prepayment before shipment, model seven-day and five-day waiting periods, payment receipt, reminder, and cancellation with event-based behavior.</li>
      <li><strong>Part 3 — interaction and information:</strong> add customer communication, ordering-system support, invoice and cancellation Data Objects, and move payment processing into a subprocess.</li>
    </ol>

    <p>The exercises explicitly allow more than one valid visual solution. The review criteria are more important than copying one layout: check syntax, semantics, naming conventions, responsibility, token behavior, and readability.</p>

    <h2>DMN: separate decision logic from process flow</h2>

    <p>Business Decision Management aims to make operational decisions standardized, consistent, and transparent. The problem it addresses is not that people cannot make decisions, but that repeated ad hoc decisions can drift because the underlying logic is not explicit.</p>

    <p>Decision Modeling Notation (DMN) complements BPMN by making that logic visible. A BPMN model explains the end-to-end activity flow. A DMN model explains <strong>how a decision is made</strong>. The two model types can exist independently, but they are especially useful together when a BPMN activity reaches a decision whose logic would otherwise create many gateways and conditions.</p>

    <p>For example, a BPMN task such as <strong>Determine how to eat dinner</strong> can call decision logic that evaluates motivation and available budget. The decision result then becomes input to the next routing step in the process.</p>

    <h3>Two levels in a DMN model</h3>

    <table class="study-table">
      <thead>
        <tr>
          <th>Level</th>
          <th>Purpose</th>
          <th>Main question</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Decision Requirements Diagram</td>
          <td>Show dependencies between decisions, sub-decisions, input data, and knowledge sources.</td>
          <td>What does this decision depend on?</td>
        </tr>
        <tr>
          <td>Decision Logic</td>
          <td>Define the detailed business rules, commonly in a decision table.</td>
          <td>Given these inputs, what output should be returned?</td>
        </tr>
      </tbody>
    </table>

    <p>This separation is important. The requirements diagram explains the structure of the decision; the decision table explains the exact rule behavior.</p>

    <h2>DMN core elements</h2>

    <table class="study-table">
      <thead>
        <tr>
          <th>Element</th>
          <th>Meaning</th>
          <th>Important property</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Decision</td>
          <td>Uses logic to determine an outcome.</td>
          <td>Contains business rules, can be decomposed into sub-decisions, and can be reused.</td>
        </tr>
        <tr>
          <td>Input Data</td>
          <td>Provides information required by a decision.</td>
          <td>Has a data type and can be reused by several decisions.</td>
        </tr>
        <tr>
          <td>Knowledge Source</td>
          <td>Represents authority or knowledge that guides the decision.</td>
          <td>Can represent internal policy, regulation, law, or another authoritative source.</td>
        </tr>
      </tbody>
    </table>

    <h3>A practical way to build a decision model</h3>

    <ol>
      <li><strong>Identify the decision or business question.</strong> Clarify the objective and the expected kind of answer.</li>
      <li><strong>Gather decision requirements.</strong> Identify the information, policies, regulations, and external authorities required to answer the question.</li>
      <li><strong>Split the decision when necessary.</strong> Create sub-decisions when the top-level logic becomes too complex, reusable, or governed by different authorities.</li>
    </ol>

    <p>A useful review question is: <strong>Can I see which inputs, sub-decisions, and sources of authority explain the final result?</strong></p>

    <h2>Decision tables: rules become explicit rows</h2>

    <p>Decision logic is commonly expressed as a decision table. Input columns contain the facts used by the rules. The output column contains the decision result. Each row is one business rule.</p>

    <p>For example, an insurance decision could use inputs such as number of accidents, age, and traffic points, with an output such as insurability. Operators express comparisons such as equal to, not equal to, element of, not an element of, greater than, less than, less than or equal to, and greater than or equal to.</p>

    <p>The key design objective is that the rules are readable enough for business users and precise enough that the same inputs produce the intended output without hidden interpretation.</p>

    <h2>DMN input types</h2>

    <table class="study-table">
      <thead>
        <tr>
          <th>Type</th>
          <th>Use</th>
          <th>Example</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Boolean</td>
          <td>True/false checks.</td>
          <td>Regular customer?</td>
        </tr>
        <tr>
          <td>Number</td>
          <td>Numeric values, ranges, and units of measure.</td>
          <td>Purchase value, age, percentage, currency.</td>
        </tr>
        <tr>
          <td>Enumeration</td>
          <td>Predefined list of allowed values.</td>
          <td>Express delivery or Standard delivery.</td>
        </tr>
        <tr>
          <td>Text</td>
          <td>Free-form textual information.</td>
          <td>Name or product description.</td>
        </tr>
        <tr>
          <td>Date</td>
          <td>A date or point in time that can be compared with other dates.</td>
          <td>Order date or payment deadline.</td>
        </tr>
        <tr>
          <td>Hierarchy</td>
          <td>Values organized into parent-child classifications.</td>
          <td>Goods → Clothes / Electronics or Geography → Country → City.</td>
        </tr>
      </tbody>
    </table>

    <p>Where possible, the course recommends an enumeration instead of free text because selecting from controlled values is less error-prone than typing names repeatedly.</p>

    <h3>Numeric intervals</h3>

    <p>Numeric rules can use open, closed, or half-open intervals. The boundary symbols matter:</p>

    <ul>
      <li><code>[1..5]</code> — includes 1 and 5.</li>
      <li><code>(1..5)</code> — excludes 1 and 5.</li>
      <li><code>(1..5]</code> — excludes 1, includes 5.</li>
      <li><code>[1..5)</code> — includes 1, excludes 5.</li>
    </ul>

    <p>This is not cosmetic notation. A value exactly on the boundary can change the output, for example a purchase value of 750 qualifying for one discount while 749.99 qualifies for another.</p>

    <h2>Hit policies: define what happens when rules overlap</h2>

    <p>A hit policy defines how the decision table behaves when input values match several rules, and in some designs when no specific rule matches. Choosing the policy is part of the decision semantics, not merely a table setting.</p>

    <table class="study-table">
      <thead>
        <tr>
          <th>Policy</th>
          <th>Behavior</th>
          <th>Key risk or use</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Unique (U)</td>
          <td>Exactly one rule may match for any input combination.</td>
          <td>Overlapping rules are invalid; completeness is important.</td>
        </tr>
        <tr>
          <td>First</td>
          <td>Rules are evaluated top to bottom and the first match wins.</td>
          <td>Rule order changes the result; broad early rules can hide more specific rules.</td>
        </tr>
        <tr>
          <td>Any</td>
          <td>Several rules may match only when all matching rules return the same output.</td>
          <td>Overlap is acceptable only when the result is identical.</td>
        </tr>
        <tr>
          <td>Priority</td>
          <td>Several rules may match; the highest-priority output is returned.</td>
          <td>Output values require an explicit priority order.</td>
        </tr>
        <tr>
          <td>Collect</td>
          <td>Several rules may fire and their outputs are collected or aggregated.</td>
          <td>Useful for scorecards and additive decisions.</td>
        </tr>
      </tbody>
    </table>

    <p>A dash (<code>-</code>) acts as a wildcard and matches any value.</p>

    <h3>Unique vs First</h3>

    <p><strong>Unique</strong> says the rules must not overlap. <strong>First</strong> allows overlap but makes rule order significant. A catch-all rule can be useful at the bottom of a First table, but a catch-all placed too early can make later rules unreachable in practice.</p>

    <h3>Any vs Priority</h3>

    <p><strong>Any</strong> allows overlapping rules only when they all produce the same output. <strong>Priority</strong> allows different outputs and resolves the overlap using the configured output ranking.</p>

    <h3>Collect and aggregation</h3>

    <p>Collect can return a set of matching outputs or aggregate them into one value. The course covers four aggregation functions:</p>

    <ul>
      <li><strong>Sum</strong> — sum of distinct matching outputs.</li>
      <li><strong>Min</strong> — smallest matching output.</li>
      <li><strong>Max</strong> — largest matching output.</li>
      <li><strong>Count</strong> — number of distinct matching outputs.</li>
    </ul>

    <p>This pattern fits scorecards. For example, vacation entitlement can start with standard days and add extra days for age or years of service.</p>

    <h2>Sub-decisions: split logic for clarity and reuse</h2>

    <p>Large decisions become easier to understand and maintain when decomposed into smaller decisions. The course uses three criteria for deciding whether to split:</p>

    <ul>
      <li><strong>Complexity</strong> — too many inputs or dependent decisions make one table difficult to understand.</li>
      <li><strong>Reusability</strong> — a result such as Customer Status may be useful in several decision models.</li>
      <li><strong>Authority</strong> — different parts of the logic may come from different internal policies or external regulations.</li>
    </ul>

    <p>The learning material uses more than seven inputs and/or sub-decisions as a strong warning that the decision logic is likely becoming complex. Treat this as a modeling heuristic, not a mathematical limit.</p>

    <p>Splitting decisions also improves change isolation: one sub-decision can change without forcing unrelated decision logic to change.</p>

    <h2>DMN naming conventions</h2>

    <table class="study-table">
      <thead>
        <tr>
          <th>Style</th>
          <th>Use</th>
          <th>Example pattern</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Activity style</td>
          <td>Useful for a top-level decision linked to a BPMN task.</td>
          <td>Verb + object: Determine discount, Select supplier, Calculate score.</td>
        </tr>
        <tr>
          <td>Output style</td>
          <td>Useful for most other decisions because the name reflects the produced result.</td>
          <td>Customer status, eligibility, score, ranking.</td>
        </tr>
        <tr>
          <td>Question style</td>
          <td>Useful when a direct question is clearer than an output label.</td>
          <td>Is the customer eligible?</td>
        </tr>
      </tbody>
    </table>

    <p>Question style can be intuitive but often creates long labels. For process-linked top-level decisions, activity style keeps the DMN name aligned with the BPMN decision task.</p>

    <h2>Completeness and consistency: decision tables must cover the logic safely</h2>

    <p>A decision table is <strong>incomplete</strong> when an allowed input combination has no matching rule. With a Unique hit policy, the intended model is that exactly one rule fires for every possible input combination, so missing rules are a direct quality problem.</p>

    <p>A decision table is <strong>inconsistent</strong> when rules overlap in a way that violates the selected hit policy. For a Unique table, overlapping rules are not allowed.</p>

    <h3>Verify automates these checks</h3>

    <p>SAP Signavio Process Manager provides a verification function for decision tables. Verify can identify missing combinations and consistency errors such as overlapping rules that do not comply with the hit policy.</p>

    <p><strong>Lead boundary:</strong> verification checks the formal rule space. It does not prove that the business policy itself is correct. Business owners still need to validate the intended rule meaning.</p>

    <h2>Dictionary reuse in DMN</h2>

    <p>DMN models can reuse the same centrally governed Dictionary entries used elsewhere in the process landscape. A knowledge source such as an ERP system can be linked from the Dictionary, and the entry can show where else it is used.</p>

    <p>This keeps decisions aligned with the same business vocabulary as BPMN models. New DMN objects can also be defined and then promoted into governed Dictionary content where appropriate.</p>

    <h2>DMN Simulation: evaluate decision behavior with input data</h2>

    <p>The DMN Simulation tool applies the rules in the decision table to supplied input data and returns the resulting output. This makes the decision executable enough to inspect behavior without confusing it with observed production execution.</p>

    <p>Changing the input data or the decision model makes it possible to compare a new output with the original one. Simulation can also expose sub-decision dependencies and scenarios that the current rules do not cover.</p>

    <p><strong>DMN simulation asks:</strong> “Given this model and these inputs, what result does the logic produce?”</p>

    <h2>DMN Test Lab: preserve expected behavior through change</h2>

    <p>The DMN Test Lab is used for repeatable test cases. The modeler defines input data and an expected output, runs the current decision model, and compares the real result with the expectation.</p>

    <p>This is particularly useful after rule changes. A mismatch between expected and actual output indicates that the implementation does not behave as intended.</p>

    <p>Existing or historical cases can also be imported as regression checks. For example, if a customer must never receive a discount, an older case representing that customer can be rerun after unrelated rule changes to confirm that the protected behavior has not changed.</p>

    <table class="study-table">
      <thead>
        <tr>
          <th>Tool</th>
          <th>Main purpose</th>
          <th>Question</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Verify</td>
          <td>Check formal completeness and consistency of the decision table.</td>
          <td>Are there missing or conflicting rule combinations?</td>
        </tr>
        <tr>
          <td>Simulation</td>
          <td>Evaluate outputs for supplied input data and compare changed decision behavior.</td>
          <td>What output does this logic produce for these inputs?</td>
        </tr>
        <tr>
          <td>Test Lab</td>
          <td>Run repeatable expected-result tests and regression cases.</td>
          <td>Does the changed decision still meet the expected behavior?</td>
        </tr>
      </tbody>
    </table>

    <h2>BPMN and DMN together</h2>

    <p>The strongest architecture uses each notation for the concern it explains best:</p>

    <ol>
      <li>BPMN shows the process activity <strong>Determine discount</strong>.</li>
      <li>DMN shows which inputs, sub-decisions, and policies the decision depends on.</li>
      <li>The decision table defines the exact rules.</li>
      <li>The result returns to the process and drives the next activity or route.</li>
    </ol>

    <p>This reduces gateway-heavy process models and makes decision logic independently maintainable, testable, reusable, and reviewable.</p>

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

    <h2>Simulation: test a designed process before changing reality</h2>

    <p>Process simulation runs BPMN 2.0 models with process assumptions such as execution cost, task duration, case frequency, gateway probabilities, resource schedules, and wages. Its purpose is to estimate behavior before making an operational change: where costs rise, where queues form, whether capacity is sufficient, and how a To-Be design compares with the current model.</p>

    <p>The simulation feature can visualize a process step by step, run a single case, or run multiple cases. It can also support comparison of the current model with a To-Be version. This makes simulation useful for questions such as capacity growth, resource absence, cost reduction, and cycle-time improvement.</p>

    <h3>The four Scenario parameter groups</h3>

    <table class="study-table">
      <thead>
        <tr>
          <th>Parameter</th>
          <th>What you define</th>
          <th>Typical decision</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Costs</td>
          <td>Execution cost for each activity</td>
          <td>If shipping or another task becomes cheaper, how much does the process cost change?</td>
        </tr>
        <tr>
          <td>Duration</td>
          <td>Task execution time and optional duration distributions</td>
          <td>If one step becomes faster, what happens to total cycle time?</td>
        </tr>
        <tr>
          <td>Frequency</td>
          <td>Case arrival frequency and gateway path probabilities</td>
          <td>Can the process handle a higher volume?</td>
        </tr>
        <tr>
          <td>Resources</td>
          <td>Lane schedules, capacity, and hourly wages</td>
          <td>Can available people handle the workload, including reduced availability?</td>
        </tr>
      </tbody>
    </table>

    <h3>Costs: activity expense is not labor cost</h3>
    <p>The Costs tab holds task-specific execution costs such as material, electricity, shipping, or other direct activity expenses. Labor cost should not be entered here because labor is modeled through Resources. Keeping these cost types separate prevents double counting. The workspace administrator configures the currency used by the process models.</p>

    <h3>Duration: execution time is not total cycle time</h3>
    <p>Task execution times contribute to process cycle time, but simply adding task durations normally gives only a minimum. Real cycle time can also include waiting and idle time. For variable tasks, the model can define different durations for different proportions of cases and use distributions instead of one fixed value.</p>

    <p>This distinction is important in diagnosis: making a task itself faster does not necessarily remove waiting caused by scarce resources or queues.</p>

    <h3>Frequency: volume and routing drive demand</h3>
    <p>For a multiple-case simulation, the model defines how often new cases start within a time frame. The learning example uses a default frequency of four new cases per day, or twenty per week, and allows different frequencies for particular days or hours.</p>

    <p>If the BPMN model contains gateways, the Frequency tab also defines the probability of each path. When a process reaches that decision point, the probabilities determine the simulated route independently for each case. Therefore, both demand volume and path mix can change resource consumption and bottlenecks.</p>

    <h3>Resources: availability creates queues</h3>
    <p>The Resources tab defines working schedules and hourly wages for the lanes in the diagram. Resource availability strongly influences process cost, total cycle time, and bottlenecks. A new case may be ready for an activity while the responsible people are still processing previous cases; the waiting queue then becomes part of the simulated process behavior.</p>

    <h3>Read simulation results correctly</h3>

    <table class="study-table">
      <thead>
        <tr>
          <th>Result</th>
          <th>Meaning</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Costs</td>
          <td>Fixed activity costs plus resource costs. If activity durations vary, resource-related cost can vary with execution time.</td>
        </tr>
        <tr>
          <td>Total cycle time</td>
          <td>Execution time plus waiting time.</td>
        </tr>
        <tr>
          <td>Resource consumption</td>
          <td>Total working hours required from process participants.</td>
        </tr>
        <tr>
          <td>Bottlenecks</td>
          <td>Lanes where capacity constraints create waiting; waiting times are shown against activities in the simulation result.</td>
        </tr>
      </tbody>
    </table>

    <p>If total cycle time extends beyond the simulation time span, the learning material gives two main explanations: resources cannot process incoming cases fast enough and instances accumulate, or new cases entered near the end of the simulated period and have not yet finished.</p>

    <p><strong>Lead boundary:</strong> simulation is a what-if calculation based on model assumptions. It is not evidence that the real process behaved that way. Observed execution belongs to process-data analysis.</p>

    <h2>Collaboration: syntax can be checked, semantics need people</h2>

    <p>Process collaboration matters because the Editor can validate notation but cannot prove that the modeled process is semantically correct. A BPMN model may be syntactically valid and still describe the business incorrectly. Process participants, stakeholders, and subject matter experts therefore need a way to challenge the model while knowledge is still fresh.</p>

    <p>Feedback can be requested during modeling. Comments appear in the Editor's Comments panel, where modelers can reply and mark suggestions as <strong>Resolved</strong> or <strong>Rejected</strong>. Comments can also be filtered by individual model elements, which helps connect feedback to the exact activity, event, or other object under discussion.</p>

    <p>External participants can also be invited to provide feedback. After registration, their access is limited to the specific process to which they were invited. This is useful when a process needs review from a participant outside the normal workspace audience without granting broad workspace access.</p>

    <p>Publishing comes after modeling and feedback have been incorporated. The Process Collaboration Hub then becomes the consumption layer for organizational users. A practical governance flow is therefore <strong>model → review → resolve feedback → publish → consume</strong>.</p>

    <h2>Variant Management: standard core, controlled local difference</h2>

    <p>SAP Signavio Variant Management is consumed from the Process Collaboration Hub, where the Variant Management area provides access to templates, Variant Groups, dimensions, values, and variant relationships.</p>

    <p>A process variant is a version of a business process that captures justified differences in execution or documentation while keeping a relationship to a common process framework. Variants are useful when one global process needs different regional, organizational, product, brand, customer-journey, customer-type, or transformation-specific behavior.</p>

    <p>Variant management is therefore not uncontrolled copying. Its purpose is to maintain transparency between a common template and the processes that differ from it.</p>

    <h3>Common reasons for variants</h3>
    <ul>
      <li><strong>Regional differences</strong> — local regulations or operating rules.</li>
      <li><strong>Product and brand harmonization</strong> — one framework with site- or portfolio-specific differences.</li>
      <li><strong>Organizational levels</strong> — local units adapt a common template.</li>
      <li><strong>Transformation journey</strong> — existing and target process variants coexist during change.</li>
      <li><strong>Customer types</strong> — different process behavior for different customer segments.</li>
    </ul>

    <p>The learning material describes Variant Management capabilities to detect variants through integration with process data, control the relationship between template and variant, track and propagate template changes, and help users consume the correct variant for their context or role.</p>

    <h3>Template, dimensions, values, and Variant Group</h3>

    <p>The <strong>process template</strong> is the main model to which variants are attached. The differentiating characteristics are defined as <strong>dimensions</strong>. These dimensions are represented by Dictionary categories, which must first be configured for that purpose in Process Manager. Specific Dictionary entries then become the dimension values.</p>

    <p>Creating a template automatically creates a <strong>Variant Group</strong> containing the template and its attached variants. Variant Groups organize the relationship and are also used when managing dimensions. To remove a Variant Group, the template is reverted. The attached process models are not deleted; they simply stop being variants in that group.</p>

    <h3>Example: one global O2C process, several justified variants</h3>

    <table class="study-table">
      <thead>
        <tr>
          <th>Model</th>
          <th>Purpose</th>
          <th>Typical difference</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Core O2C Template</td>
          <td>Common global process</td>
          <td>Standard order, fulfillment, and invoicing structure.</td>
        </tr>
        <tr>
          <td>US B2B Variant</td>
          <td>Regional and customer-type adaptation</td>
          <td>Credit checks and state-specific tax handling.</td>
        </tr>
        <tr>
          <td>EU B2C Variant</td>
          <td>Regional and customer-type adaptation</td>
          <td>VAT processing and GDPR-related requirements.</td>
        </tr>
        <tr>
          <td>APAC B2B Variant</td>
          <td>Regional adaptation</td>
          <td>Local shipping rules and extended payment terms.</td>
        </tr>
      </tbody>
    </table>

    <p>The point is not to create four unrelated processes. The template keeps the common operating model visible, while variants capture the differences that are actually required for region, customer context, regulation, or operating practice.</p>

    <h3>Attach, clone, or detach?</h3>

    <table class="study-table">
      <thead>
        <tr>
          <th>Action</th>
          <th>Meaning</th>
          <th>Use when</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Attach</td>
          <td>Make an existing process a variant of a template.</td>
          <td>The local model already exists and should enter the governed variant structure.</td>
        </tr>
        <tr>
          <td>Clone</td>
          <td>Copy the template and use the copy as a new variant.</td>
          <td>A new variant should begin from the same core structure.</td>
        </tr>
        <tr>
          <td>Detach</td>
          <td>Break the link between the variant and its template.</td>
          <td>The local process needs extensive independent change and should no longer receive template governance.</td>
        </tr>
      </tbody>
    </table>

    <p>Cloning speeds up local adaptation without changing the original template. Detaching is a stronger decision: the process becomes independent, so future template relationships no longer protect alignment.</p>

    <h3>Change propagation keeps variants aligned</h3>

    <p>When a template changes, a variant can show unresolved updates in Process Collaboration Hub. Those updates are reviewed in the Editor, where the modeler can apply or ignore them. Some changes, such as renaming, can be propagated automatically. The learning material also demonstrates automatic propagation for supported added or deleted process elements. Other changes can require manual adjustment in the variant. The correct boundary is therefore <strong>supported automatic propagation vs changes that require modeler review and manual work</strong>, not simply “non-structural vs structural.”</p>

    <p>The update notification is visible only when the template has been published in its newest revision. Users who need immediate awareness can subscribe to change-propagation notifications.</p>

    <p><strong>Lead decision:</strong> use a variant when the difference is legitimate but the process still belongs to a common standard. Detach only when independent evolution is more important than template alignment. Variant Management is therefore a governance mechanism for balancing global consistency with local compliance and operating needs.</p>

    <h2>Reporting: turn model metadata into governance evidence</h2>

    <p>Process models contain visible diagram content and less visible information stored in attributes. Reporting aggregates that information across many processes or focuses on selected aspects of one model. The output can support decisions, audits, governance, ownership analysis, system analysis, and process improvement. Reports are available from the Explorer and can also be generated in Process Collaboration Hub.</p>

    <h3>Analysis reports</h3>

    <table class="study-table">
      <thead>
        <tr>
          <th>Report</th>
          <th>Main input</th>
          <th>What it helps answer</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Process Cost Analysis</td>
          <td>Execution cost, cost center, yearly start-event frequency, gateway probabilities</td>
          <td>Which activities drive cost, where is waste, and where could budget be reduced or redirected?</td>
        </tr>
        <tr>
          <td>Resource Consumption Analysis</td>
          <td>Task time, participant workload, allowances, work times</td>
          <td>Which departments or roles consume capacity and where do resource constraints create bottlenecks?</td>
        </tr>
      </tbody>
    </table>

    <p>Process Cost Analysis calculates task execution cost and uses the start event's yearly frequency. Gateway probabilities influence the input factor for downstream tasks, so expected path mix changes the calculated cost. Resource Consumption Analysis instead focuses on participant workload and organizes consumed time by department.</p>

    <h3>Four matrices for responsibility and usage</h3>

    <table class="study-table">
      <thead>
        <tr>
          <th>Matrix</th>
          <th>What it shows</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Responsibility Assignment Matrix</td>
          <td>RACI-style mapping of tasks and deliverables to responsible, accountable, consulted, and informed roles.</td>
        </tr>
        <tr>
          <td>Responsibility Handovers Matrix</td>
          <td>Handoffs between participants based on sequence flows and message flows.</td>
        </tr>
        <tr>
          <td>IT System Usage Matrix</td>
          <td>Where process activities read from or write to IT systems; the analysis can also be grouped by role.</td>
        </tr>
        <tr>
          <td>Document Usage Matrix</td>
          <td>Which documents are assigned to tasks as inputs or outputs.</td>
        </tr>
      </tbody>
    </table>

    <p>These matrices connect process design to operating ownership. They can reveal unclear accountability, excessive handoffs, concentration on critical systems, training needs, document dependencies, and outdated documents.</p>

    <h3>Process management and maintenance reports</h3>

    <p><strong>Modeling Conventions</strong> checks selected diagrams against BPMN conventions and workspace-specific modeling rules. Filters can narrow the report by diagram information, publishing state, or custom attributes. The resulting spreadsheet exposes errors, warnings, and hints, with a legend of the conventions that were checked. A high number of violations can point not only to model quality problems but also to a modeler training need.</p>

    <p><strong>Process Model Metrics</strong> reports statistics about diagram elements, linked files, and linked Dictionary entries. It also exposes Process Manager and Collaboration Hub links and can help find highly complex or unpublished diagrams, retrieve a process ID, and review authorship or modification information.</p>

    <p><strong>Process Characteristics</strong> lists BPMN elements and attributes that contain values. It can help identify redundant attributes, compare modeling patterns across processes, and provide an overview of information such as process ownership or certification requirements. Empty attributes across the selected processes are not shown.</p>

    <p><strong>Risks and Controls</strong> aggregates risk and control information defined in the Dictionary and used in selected process diagrams. It can include descriptions, aims, relevant documents, and control frequency, supporting risk evaluation, audits, compliance evidence, control-gap analysis, and IT-risk review.</p>

    <h3>Process Documentation: tailored output, not only standard reports</h3>

    <p>Process Documentation creates a more configurable document that can include diagram graphics, element descriptions, attributes, and Dictionary entries. It can be generated as PDF or Microsoft Word and can use custom templates. Typical uses include BPMN task overviews, Dictionary matrices, process summaries, quality-management documentation, work instructions, and material for participants who do not have Collaboration Hub access.</p>

    <p>Documentation templates can be simple or advanced, including multilingual output. Their design follows an Editor-like approach with objects on a canvas and configuration through an attributes panel. Creating the templates requires the relevant administrator-granted access rights.</p>

    <h3>Simulation vs reporting vs Process Intelligence</h3>

    <table class="study-table">
      <thead>
        <tr>
          <th>Capability</th>
          <th>Primary evidence</th>
          <th>Main question</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Simulation</td>
          <td>Assumptions attached to the designed model</td>
          <td>What could happen if volume, time, cost, routing, or capacity changes?</td>
        </tr>
        <tr>
          <td>Reporting</td>
          <td>Model elements, attributes, Dictionary links, roles, systems, documents, risks</td>
          <td>What does our modeled process landscape contain and where are governance or design signals?</td>
        </tr>
        <tr>
          <td>Process Intelligence</td>
          <td>Observed process event data</td>
          <td>What actually happened in process execution?</td>
        </tr>
      </tbody>
    </table>

    <h2>Process Governance: turn governance rules into executable work</h2>

    <p>SAP Signavio Process Governance is the workflow-management component used to configure and execute governed business workflows. It supports process governance and compliance by coordinating tasks and handovers, tracking relevant information, routing work to the correct people, and handling approvals or rejections.</p>

    <p>The key distinction is that <strong>Process Manager describes and governs process models, while Process Governance executes workflow instances</strong>. A model can describe how approval should work; Process Governance can assign the approval task, collect the result, remind the assignee, escalate delays, and keep a case history.</p>

    <h3>Core governance use cases</h3>

    <table class="study-table">
      <thead>
        <tr>
          <th>Capability</th>
          <th>What it governs</th>
          <th>Typical example</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Process release cycle management</td>
          <td>Review, approval, and publication of process content</td>
          <td>Route a model to process owners, risk owners, and quality managers before publication.</td>
        </tr>
        <tr>
          <td>Process maturity assessment</td>
          <td>Repeatable validation and assessment work</td>
          <td>Replace spreadsheet-based maturity checks with tracked workflow tasks.</td>
        </tr>
        <tr>
          <td>Risk and control management</td>
          <td>Review and maintenance of governed risks and controls</td>
          <td>Use centrally maintained Dictionary risks and controls and schedule recurring verification.</td>
        </tr>
        <tr>
          <td>Configurable governance workflows</td>
          <td>Approval and control logic modeled with BPMN</td>
          <td>Assign tasks, route decisions, and analyze workflow data later in Process Intelligence or another BI tool.</td>
        </tr>
      </tbody>
    </table>

    <p>Supporting features include automatic reminders, escalation to other users when critical work is overdue, reusable workflow data, direct task or case messaging, and task filters that help users focus on open work.</p>

    <h2>Workflow vs business process</h2>

    <p>A workflow and a process are closely related but are not identical. A process provides the broader roadmap and business objective. A workflow describes how work moves through operational steps: who does what, when, with which information, and who continues next.</p>

    <p>One useful assessment formulation is: <strong>a process explains the business outcome and structure; a workflow operationalizes the work required to achieve it</strong>. A process can exist as a documented business model without an executable workflow, while a workflow belongs to a broader process context.</p>

    <p>Workflows can be handled manually, supported by office tools or ERP systems, implemented as custom software, or executed by a workflow-management system. A workflow-management system automates recurring procedures by assigning the right task to the right person at the right time.</p>

    <h2>Process Governance access and operating surfaces</h2>

    <p>SAP Signavio Process Governance is part of SAP Signavio Process Transformation Suite and is accessed from the SAP Signavio environment. The learning material describes entering through Process Collaboration Hub and selecting Process Governance from the application menu.</p>

    <p>Process Collaboration Hub also exposes governance-related functions such as <strong>diagram approvals</strong>, <strong>read confirmations</strong>, and <strong>process rating</strong>.</p>

    <p>The Process Governance landing page is organized around four main menu tabs: <strong>Tasks</strong>, <strong>Cases</strong>, <strong>Processes</strong>, and <strong>Analytics</strong>. The provided lesson introduces these four areas here and continues their detailed navigation separately.</p>

    <p>The learning material also notes that Process Governance does not provide a trial version and requires a Process Governance login. When the SAP Signavio sign-in flow asks again after entering from Collaboration Hub, the lesson instructs users to choose <strong>Log in with Process Manager Account</strong> rather than re-entering credentials.</p>

    <h2>Creating workflows: reuse before starting from zero</h2>

    <p>Process Governance supports three creation paths from the Processes area:</p>

    <ul>
      <li><strong>From Scratch</strong> — create a new workflow directly.</li>
      <li><strong>From Template</strong> — start from an available workflow template and adapt it.</li>
      <li><strong>Import BPMN</strong> — import an existing BPMN process model that meets execution requirements.</li>
    </ul>

    <p>A process can also be transferred from SAP Signavio Process Manager into Process Governance. For assessment purposes, the design rule is <strong>reuse an appropriate template or existing BPMN model before rebuilding the workflow manually</strong>, but confirm that the imported process satisfies execution requirements.</p>

    <h2>Triggers: define how a workflow case begins</h2>

    <p>A workflow starts with a trigger. The trigger determines what information or event creates a new case.</p>

    <table class="study-table">
      <thead>
        <tr>
          <th>Trigger</th>
          <th>Who or what starts it?</th>
          <th>Typical use</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Public form</td>
          <td>Anyone, including an external participant</td>
          <td>A public request form, for example requesting information or materials.</td>
        </tr>
        <tr>
          <td>Private form</td>
          <td>Registered internal users</td>
          <td>Internal requests such as holiday or service requests.</td>
        </tr>
        <tr>
          <td>E-mail</td>
          <td>An incoming message, often from another system or person</td>
          <td>An ERP or HR system sends a notification that starts a case.</td>
        </tr>
        <tr>
          <td>Process Manager</td>
          <td>A process model handed over from Process Manager</td>
          <td>Start a review and approval workflow before a model is published.</td>
        </tr>
      </tbody>
    </table>

    <h3>Forms create and update workflow data</h3>

    <p>Forms are used in two places: <strong>form triggers</strong> and <strong>user tasks</strong>. A trigger form sets workflow variables when a case starts. A user-task form lets an assignee enter or update information while completing work.</p>

    <p>Trigger forms can be private by default or public. Forms contain fields, and the form builder supports structures such as nested sections, mandatory fields, dynamic fields, and field groups. The important architectural point is that form data becomes workflow data that later tasks, decisions, documents, and messages can reuse.</p>

    <h2>Actions: model the work that happens after the trigger</h2>

    <p>Process Governance groups workflow elements into three categories:</p>

    <ol>
      <li><strong>Main actions</strong> — the main human or communication work needed to reach the workflow goal.</li>
      <li><strong>Services and other actions</strong> — automated supporting work such as creating documents or PDFs.</li>
      <li><strong>Events and gateways</strong> — flow-control elements that decide which actions execute and when.</li>
    </ol>

    <h3>User Task</h3>

    <p>A User Task represents work performed by one person. Its configuration can define an assignee or candidate users, a process role, a task form, reminders, and access rights. Assigning by process role helps Process Governance keep related tasks with the same person where that role is reused.</p>

    <p>Due dates and reminders are separate concepts. A due date defines the task deadline. A reminder can notify assignees before or independently of that deadline, and continued reminders can repeat. The learning material states a maximum of 25 reminders for one task.</p>

    <h3>Multi-User Task</h3>

    <p>A Multi-User Task creates the same task for several people and collects their individual results into result lists. It supports the same general configuration areas as a User Task plus a Results configuration.</p>

    <table class="study-table">
      <thead>
        <tr>
          <th>Execution</th>
          <th>Behavior</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Parallel</td>
          <td>Create all individual tasks at the same time; assignees may complete them in any order.</td>
        </tr>
        <tr>
          <td>Sequential</td>
          <td>Create one task at a time; the next is created only after the current assignee completes it.</td>
        </tr>
      </tbody>
    </table>

    <p>This makes Multi-User Task suitable for scenarios such as several reviewers who must each evaluate the same proposal.</p>

    <h3>Send E-mail</h3>

    <p>The Send E-mail action sends workflow-controlled messages to users, addresses, or values held in variables. Workflow fields can be reused in the subject and body, attachments can come from workflow file fields or generated documents, and the body supports Markdown formatting. The case history records successful e-mail events. The lesson also describes a size fallback: if the message is too large, Process Governance attempts to send it without attachments and records that outcome in the case history when successful.</p>

    <h2>Process details and access control</h2>

    <p>The process Details area contains process-level information and configuration, including general information, process owner and description, access control, field overview, and core case information.</p>

    <p>Access control can restrict who can access a process, edit cases, or work with individual tasks. Processes and tasks are described in the learning material as organization-visible by default; making a process private allows permissions to be granted to specific users or groups. Individual User Tasks can also have more specific access restrictions.</p>

    <p><strong>Lead boundary:</strong> process access and task access are related but not identical. A user may need visibility of the overall case without receiving permission to assign, view, or complete every protected task.</p>

    <h2>Versions: editing state and execution state are separate</h2>

    <p>The workflow editor saves model changes while you work, but a new case can start only from a <strong>published process version</strong>. This creates an important governance boundary between the editable workflow definition and the version currently used for execution.</p>

    <h3>Publish, Re-Publish, and Restore solve different problems</h3>

    <table class="study-table">
      <thead>
        <tr>
          <th>Action</th>
          <th>What changes?</th>
          <th>Effect on new cases</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Publish</td>
          <td>Create a published workflow version from the current definition.</td>
          <td>New cases can use the newly published version.</td>
        </tr>
        <tr>
          <td>Re-Publish</td>
          <td>Publish a new copy of an older selected version.</td>
          <td>New cases use that republished version; current unpublished edits are not removed.</td>
        </tr>
        <tr>
          <td>Restore</td>
          <td>Replace current unpublished edits with an older selected version for further editing.</td>
          <td>The already published version used for new cases does not change.</td>
        </tr>
      </tbody>
    </table>

    <p>Version comments can document what changed between releases and make workflow evolution more transparent. The distinction between Re-Publish and Restore is particularly useful in assessment questions because one changes the version used for future cases, while the other changes the editable draft.</p>

    <h2>Process Manager vs Process Governance vs Process Intelligence</h2>

    <table class="study-table">
      <thead>
        <tr>
          <th>Component</th>
          <th>Primary role</th>
          <th>Lead question</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Process Manager</td>
          <td>Model, document, govern, publish, and simulate designed processes</td>
          <td>How should the process be defined and governed?</td>
        </tr>
        <tr>
          <td>Process Governance</td>
          <td>Configure and execute governed workflows, tasks, approvals, reminders, and cases</td>
          <td>How is governed work actually assigned and completed?</td>
        </tr>
        <tr>
          <td>Process Intelligence</td>
          <td>Analyze observed event data and actual process execution</td>
          <td>What actually happened in operational execution?</td>
        </tr>
      </tbody>
    </table>

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

    <h2>Administration: keep the workspace usable as it scales</h2>

    <p>SAP Signavio administrators manage workspace settings, user access, governance controls, and the configuration that keeps process content consistent as the number of users grows. The first user who registers a workspace becomes the <strong>Tenant Owner</strong>. The training material states that this user cannot be deleted.</p>

    <p>Because administrators have broad workspace rights, the role is best suited to users who understand both the product and BPMN. Administrative changes should be communicated and documented so that the admin team works from the same configuration assumptions.</p>

    <h3>Administrative responsibility is product-specific</h3>

    <table class="study-table">
      <thead>
        <tr>
          <th>Component</th>
          <th>Typical administrator responsibilities</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Process Manager</td>
          <td>User groups and access rights, workspace settings, modeling conventions, custom attributes, governance and security settings.</td>
        </tr>
        <tr>
          <td>Process Collaboration Hub</td>
          <td>User accounts and groups, licenses, attribute visualization, audiences, Process Governance enablement, appearance, consumption information, and value accelerators.</td>
        </tr>
        <tr>
          <td>Journey Modeler</td>
          <td>Journey-model templates plus related administration through Process Manager and Collaboration Hub.</td>
        </tr>
        <tr>
          <td>Process Governance</td>
          <td>Workflow users/groups/labels, Process Manager Dictionary integration, connectors, approval-workflow setup, read confirmations, process rating, JavaScript-task enablement, and model-guideline checks.</td>
        </tr>
      </tbody>
    </table>

    <p>Administrative rights do not automatically transfer between products. In particular, being an administrator in Process Manager and Collaboration Hub does not automatically make the same user a Process Governance administrator.</p>

    <h3>Workspace region is visible in the tenant URL</h3>

    <p>The course material maps SAP Signavio workspace URLs to hosting regions. Examples include the US tenant in Northern Virginia, the traditional editor tenant in Frankfurt, and regional tenants for Sydney, Tokyo, Canada Central, Seoul, and Singapore. Because hosting and service availability can change, treat the URL-to-region mapping as operational tenant information and verify current service status before making architecture or compliance decisions.</p>

    <h2>General workspace settings</h2>

    <h3>Languages affect more than diagram labels</h3>

    <p>Administrators can enable multiple workspace languages and must define a default language. The first language in the configured list becomes the default. Adding languages affects Process Manager content broadly, including <strong>attributes, Dictionary terms, and diagrams</strong>, not only visible activity labels.</p>

    <p>A practical governance rule is to enable only languages that the organization actually maintains. Every extra language increases translation and content-maintenance responsibility.</p>

    <h3>Modeling conventions turn standards into automated checks</h3>

    <p>Modeling conventions help administrators enforce consistency across many modelers. The course describes convention checks across areas such as notation syntax, naming, process structure, architecture, and diagram layout. Administrators can create custom conventions and add organization-specific rules.</p>

    <p>This extends the earlier distinction between syntax and semantics: the tool can check formal and configured rules, while people still need to validate whether the process itself is correct.</p>

    <h2>Reduce BPMN complexity with notation subsets</h2>

    <p>BPMN 2.0 contains a large number of elements. Most organizations use only a subset regularly. Administrators can therefore expose a smaller notation subset so modelers see the elements that fit their process type and do not add unnecessary complexity.</p>

    <p>Administrators can also define the corporate appearance of notation elements, such as task colors and fonts. Formatting changes apply across notation subsets for that element type, so visual standards should be designed centrally rather than corrected diagram by diagram.</p>

    <h2>Custom attributes: extend the information model</h2>

    <p>Custom attributes allow the workspace to capture organization-specific information on diagram elements and Dictionary categories. They behave like standard attributes and can also be exposed in Process Collaboration Hub.</p>

    <table class="study-table">
      <thead>
        <tr>
          <th>Object</th>
          <th>Useful attribute examples</th>
          <th>Typical type</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Process</td>
          <td>Process Owner</td>
          <td>Text or Dictionary link</td>
        </tr>
        <tr>
          <td>Process</td>
          <td>Review Date</td>
          <td>Date</td>
        </tr>
        <tr>
          <td>Process</td>
          <td>Process Status / maturity</td>
          <td>Drop-down</td>
        </tr>
        <tr>
          <td>Process</td>
          <td>Customer interaction / ISO relevance</td>
          <td>Boolean</td>
        </tr>
        <tr>
          <td>Task</td>
          <td>Applicable documents or templates</td>
          <td>Dictionary link or external document/URL</td>
        </tr>
        <tr>
          <td>Task</td>
          <td>RACI responsibilities</td>
          <td>Dictionary links</td>
        </tr>
        <tr>
          <td>Task</td>
          <td>Risks and Controls</td>
          <td>Risk-management information backed by the Dictionary</td>
        </tr>
        <tr>
          <td>Task</td>
          <td>IT System</td>
          <td>Dictionary link</td>
        </tr>
      </tbody>
    </table>

    <p>This is an important design principle: use custom attributes when information needs to be searchable, reportable, governed, reused, or visualized. Do not add a custom field only because one diagram needs a note.</p>

    <h2>Attribute visualization: show metadata without rewriting the model</h2>

    <p>Administrators can define visualization layers that render selected attributes as overlays using icons and colors. The training material lists support for BPMN diagrams, value chains, ArchiMate diagrams, and organization charts.</p>

    <p>An IT-system attribute can, for example, display an IT icon next to a task. Rules can also depend on attribute values. The course example colors task-cost overlays red above 15, yellow between 10 and 15, and green below 10.</p>

    <p>Overlays therefore separate <strong>stored metadata</strong> from <strong>visual emphasis</strong>: the attribute remains the source of truth, while the overlay is one way to expose it to viewers.</p>

    <h2>Custom graphics: visual branding with controlled constraints</h2>

    <p>Administrators can upload custom SVG graphics for selected elements in customer journeys, value chains, and BPMN diagrams. The training material defines several restrictions for administrator-uploaded graphics:</p>

    <ul>
      <li>Maximum file size: 20 KB.</li>
      <li>Maximum 2,000 anchor points.</li>
      <li>Valid SVG structure.</li>
      <li>No custom XML, JavaScript, or embedded images inside the SVG.</li>
    </ul>

    <p>Examples of customizable elements include IT systems and additional participants in BPMN, processes and collapsed processes in value chains, and personas, touchpoints, moments of truth, customers, and decorations in Journey Maps.</p>

    <p>Custom graphics belong to the workspace where they are uploaded. If the organization uses several workspaces, the graphics need to be uploaded separately in each workspace.</p>

    <h2>Dictionary administration: structure determines reuse</h2>

    <p>The Dictionary is not only a list of terms. Administrators can remove, extend, or adjust categories and add subcategories to match the organization. Category design affects both reporting and modeling suggestions.</p>

    <p>Dictionary categories have two important system purposes:</p>

    <ol>
      <li><strong>Reporting:</strong> reports such as RACI, document usage, and process documentation rely on object categories.</li>
      <li><strong>Modeling suggestions:</strong> the system suggests entries from relevant categories when a modeler links a Dictionary object.</li>
    </ol>

    <p>Typical parent and subcategory areas include Organizational Units, Documents, IT Systems, Risks, and Controls. Subcategories are useful when different object groups need separate evaluation, access rights, or attributes.</p>

    <h3>Sandbox and Dictionary Responsible</h3>

    <p>The administrator creates sandbox subcategories so modelers can propose new Dictionary content without writing directly into productive categories. A dedicated group with broad Dictionary access periodically reviews the proposals and moves approved content into the productive structure.</p>

    <p>The course example uses a <strong>Dictionary Responsible</strong> group with full Dictionary rights and import/export capability. This is the operational implementation of the sandbox governance pattern covered earlier on the page.</p>

    <h3>Dictionary attributes can link to other Dictionary categories</h3>

    <p>Custom Dictionary attributes can themselves use Dictionary links. This makes it possible to maintain a fact once and reuse it across related objects. The course example creates an SAP Module category and an SAP Transaction Codes category, then adds a Transaction Codes attribute to the SAP Module that links to the central transaction-code entries.</p>

    <p>The resulting principle is useful beyond this example: <strong>normalize governed reference data instead of copying the same value into many entries</strong>.</p>

    <h2>User licenses and account types</h2>

    <p>Every user requires a license for the relevant SAP Signavio solution in the workspace. A license belongs to a user for that workspace; a license in another workspace does not automatically grant access here. Removing a user frees the license for reassignment.</p>

    <h3>Modelers and Collaboration Hub consumers have different access models</h3>

    <p>Modeling users in Process Manager can access workspace content according to folder and group permissions. Collaboration Hub users only consume diagrams that have been explicitly published to the Hub. The course also describes different Hub access behavior depending on the authentication model, including Active Directory/SAML identity or certificate-based rollout.</p>

    <h3>Central User Management vs Process Manager Setup</h3>

    <table class="study-table">
      <thead>
        <tr>
          <th>Administration surface</th>
          <th>Best suited for</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Collaboration Hub / Central User Management</td>
          <td>Invite users, review users, export an e-mail list, remove users across Signavio applications, create or delete user groups.</td>
        </tr>
        <tr>
          <td>Process Manager Setup</td>
          <td>Manage users/groups, folder and Dictionary authorizations, and group feature sets.</td>
        </tr>
      </tbody>
    </table>

    <p>The learning material presents these two administration surfaces as coexisting during a transition toward more centralized user management.</p>

    <h3>Feedback invitations create restricted external accounts</h3>

    <p>Modelers can invite internal or external stakeholders to review a diagram. External invitees register from the invitation and receive a commenting license rather than normal broad workspace access. They can see only the invited diagram, are not added to default groups, and cannot access other SAP Signavio solutions. Revoking that access requires removing the account from user management, not only removing the license.</p>

    <h3>Account deletion has different effects on personal and shared content</h3>

    <p>When an administrator deletes a user account, content in that user's <strong>My Documents</strong> folder is removed from the workspace. Shared Documents content, comments, and changes made by the user remain. Administrators themselves cannot access or manage another modeler's My Documents content.</p>

    <h2>User groups, default groups, and feature sets</h2>

    <p>Groups simplify administration at scale. Administrators can build group hierarchies, add or remove users, and mark groups as default so new users automatically receive a baseline set of permissions.</p>

    <p>Users created through SAML or the CSV API are also assigned to default groups unless another group configuration is supplied. Feature sets can then control which capabilities a modeler group may use, for example limiting document-upload functionality to selected groups.</p>

    <h2>Access rights: understand the additive permission model</h2>

    <p>Folder structure and authorization design should be planned together. The course explicitly recommends deciding the folder structure before assigning user access. Permissions granted through one group cannot be taken away simply by adding the same user to another group with fewer permissions or by assigning a more restrictive user-specific permission.</p>

    <table class="study-table">
      <thead>
        <tr>
          <th>Right</th>
          <th>Meaning</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Hub (H)</td>
          <td>View published content in Process Collaboration Hub.</td>
        </tr>
        <tr>
          <td>Read (R)</td>
          <td>View unpublished content in simulation, revision comparison, commenting view, and Process Collaboration Hub.</td>
        </tr>
        <tr>
          <td>Write (W)</td>
          <td>Edit and save content in the Editor.</td>
        </tr>
        <tr>
          <td>Delete (D)</td>
          <td>Delete and move content; moving between folders also requires the necessary rights on source and target folders.</td>
        </tr>
        <tr>
          <td>Publish (P)</td>
          <td>Publish diagrams to Process Collaboration Hub.</td>
        </tr>
      </tbody>
    </table>

    <p>Groups are normally aligned to organizational roles, and nested groups can be useful when different folder levels require different permissions. A user who receives access only to one diagram without access to the containing folder can view that diagram and its path but not the other diagrams in the folder.</p>

    <p>The sandbox pattern can be applied not only to Dictionary categories but also to the process repository. Process-documentation template authorization is managed similarly to other repository content: administrators can grant read, write, and delete rights to selected users or groups.</p>

    <h2>Collaboration Hub administration</h2>

    <p>Collaboration Hub settings control how process consumers see and interact with published content. Administrators can configure audiences, theme, home page, comments, attribute management, read confirmations, process rating, and related visibility settings.</p>

    <h3>Audiences separate consumption experiences</h3>

    <p>Audience Management is useful when different viewer groups need different entry points or presentation. The course example uses regional audiences with different value-chain entry points and potentially different themes.</p>

    <p>User groups must exist before additional audiences can be created. Users not covered by a specific audience use the General Audience. The training material states that users who belong to more than one user group receive the General Audience settings.</p>

    <h3>Attribute and overlay visibility</h3>

    <p>Administrators can decide which attributes appear at diagram or element level and can group attributes into sections. They can also control overlay visibility and define whether overlays are active by default.</p>

    <p><strong>Featured attributes</strong> highlight a chosen attribute group on the diagram page. <strong>Header attributes</strong> can include process level, revision number, last updated or published information, and last author. Visibility can be configured by audience, including whether process levels count from level 0 or level 1.</p>

    <h3>Read Confirmation vs Process Rating</h3>

    <table class="study-table">
      <thead>
        <tr>
          <th>Feature</th>
          <th>Purpose</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Read Confirmation</td>
          <td>Ask users or groups to acknowledge that they have read a diagram or its latest changes.</td>
        </tr>
        <tr>
          <td>Process Rating</td>
          <td>Collect structured audience feedback against selected criteria; each audience member can rate once per revision.</td>
        </tr>
      </tbody>
    </table>

    <p>If rating results are enabled, users can also see the accumulated process ratings in Collaboration Hub.</p>

    <h2>Administrator reports and dashboards</h2>

    <h3>Governance Report</h3>

    <p>Process Manager administrators can use the Governance Report to review aggregated workspace activity such as diagrams, comments, Dictionary items, files, publishing states, diagram types, and page visits. Selecting a metric tile can open the corresponding Advanced Search result set.</p>

    <p>The course notes an operational limit of up to 50,000 diagrams for this report. Depending on volume, generation can take up to an hour, and the browser tab that started the report must remain open.</p>

    <h3>User/Group Assignment Report</h3>

    <p>This report lists workspace users and their group memberships and can be downloaded as Excel. It distinguishes direct membership from indirect membership through nested groups. The report is available from both Process Manager reporting and Collaboration Hub reports.</p>

    <h3>Process Model Dashboard and Usage Management Dashboard</h3>

    <p>Collaboration Hub administrators can use Process Model Dashboards backed by Process Intelligence without additional setup. The training material describes two dashboards:</p>

    <ul>
      <li><strong>Process Model Dashboard</strong> — published models, most-viewed models, open comments, and model-related filters.</li>
      <li><strong>Usage Management Dashboard</strong> — assigned licenses and unique visitors over time.</li>
    </ul>

    <p>The predefined widgets cannot be changed or removed, but administrators can apply filters, export widget data as CSV, and share the dashboards with workspace users.</p>

    <h2>Security settings: reduce unnecessary access paths</h2>

    <p>Workspace security settings can apply to current and future users. The training material highlights <strong>IP address filtering</strong> and <strong>password policies</strong> as workspace-level controls.</p>

    <p>For organizations already using Single Sign-On, the course recommends configuring SSO for SAP Signavio. SSO is presented as a way to improve access continuity, adoption, and security. The referenced administration path uses SAML-based SSO.</p>

    <h2>Administering approval workflows across Process Manager and Process Governance</h2>

    <p>Approval workflows are a cross-product configuration. To define and manage them as described in the course, the administrator needs a Process Governance license in addition to Process Manager licensing and must have administrator rights in both components.</p>

    <p>The approval workflow prevents a diagram from being published until the required reviewers approve it. The Process Manager administration setup includes <strong>General</strong>, <strong>Diagram states</strong>, <strong>Participants</strong>, and <strong>Approval Expiration</strong>.</p>

    <h3>Process Governance administration is separate</h3>

    <p>Workflow participants and workflow creators require licenses. A Process Manager/Collaboration Hub administrator is not automatically a Process Governance administrator; a Process Governance administrator must explicitly promote that user.</p>

    <h3>Organization settings</h3>

    <p>Process Governance administrators can configure the workspace time zone, restrict workflow creation to one selected group, customize notification e-mail signatures, disable daily digest e-mails for the workspace, and create labels for organizing workflows.</p>

    <h3>Reusable administrator-configured activities</h3>

    <p>The lesson introduces two reusable activity configurations that must be prepared by an administrator before workflow designers can use them:</p>

    <ul>
      <li><strong>Model Guideline Check / Convention Check</strong></li>
      <li><strong>SharePoint File Upload</strong></li>
    </ul>

    <p>The guideline-check activity can return a Boolean error flag and counts for must-level errors, warnings, and hints. A workflow can then route on those results, for example automatically rejecting a model when the configured error count is greater than zero. If the activity does not work, the lesson says to verify the Process Manager integration.</p>

    <h3>SharePoint upload requires credentials and activation</h3>

    <p>The SharePoint activity requires stored credentials before configuration. The course describes a credential name plus a secret key for sensitive information and notes that SAP Support does not have access to that key. After the activity is configured, it must be explicitly activated before workflows can use it. The configuration also requires a SharePoint Tenant ID obtained with the organization's IT team.</p>

    <h3>Services, connectors, and Process Manager integration</h3>

    <p>Services & Connectors allow Process Governance workflows to exchange data with internal or third-party systems. Administrators can configure data connectors and generate API tokens for read-only reporting access to external data.</p>

    <p>Process Manager integration serves two important governance purposes: triggering model approval before publication and exposing selected Dictionary categories to workflow participants, for example Risks & Controls or document entries. The training material states that a system user account must be configured for the Process Manager integration.</p>

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
          <td>BPMN or DMN?</td>
          <td>Use BPMN to model activity flow and responsibility; use DMN to model decision requirements and rule logic.</td>
        </tr>
        <tr>
          <td>Decision Requirements Diagram or decision table?</td>
          <td>Use the requirements diagram for dependencies and authorities; use the decision table for detailed rules and outputs.</td>
        </tr>
        <tr>
          <td>Unique or First hit policy?</td>
          <td>Use Unique when rules must never overlap; use First when ordered overlapping rules are intentional and the first match should win.</td>
        </tr>
        <tr>
          <td>Verify, Simulation, or Test Lab?</td>
          <td>Verify checks rule-space quality, Simulation evaluates model behavior for inputs, and Test Lab checks expected results and regression cases.</td>
        </tr>
        <tr>
          <td>XOR, AND, or OR?</td>
          <td>Use XOR for one alternative, AND for all parallel paths, and OR when one or several optional paths may apply.</td>
        </tr>
        <tr>
          <td>Sequence flow or message flow?</td>
          <td>Use sequence flow inside one pool; use message flow for communication between pools.</td>
        </tr>
        <tr>
          <td>Collapsed subprocess, Call Activity, or expanded subprocess?</td>
          <td>Hide detail with a collapsed subprocess, reuse global logic with a Call Activity, and keep scenario-specific grouped detail visible with an expanded subprocess.</td>
        </tr>
        <tr>
          <td>Data Object or IT System object?</td>
          <td>Use the BPMN Data Object for information/documents; use the SAP Signavio IT System element to show application support.</td>
        </tr>
        <tr>
          <td>Simulation or reporting?</td>
          <td>Use simulation for what-if behavior under assumptions; use reporting to aggregate model and attribute information.</td>
        </tr>
        <tr>
          <td>Template or detached process?</td>
          <td>Keep a variant attached while standard alignment matters; detach when the process must evolve independently.</td>
        </tr>
        <tr>
          <td>Syntax check or stakeholder review?</td>
          <td>Syntax proves notation correctness; stakeholder feedback is needed to challenge semantic correctness.</td>
        </tr>
        <tr>
          <td>Process Manager or Process Governance?</td>
          <td>Use Process Manager to model and govern process content; use Process Governance when the approval, task, or handover must execute as a workflow.</td>
        </tr>
        <tr>
          <td>Central User Management or Process Manager Setup?</td>
          <td>Use central user management for workspace-level user/group administration; use Process Manager Setup for detailed folder, Dictionary, and feature-set permissions.</td>
        </tr>
        <tr>
          <td>Audience or access right?</td>
          <td>Use access rights to control what users may access or change; use audiences to tailor how published process content is presented to viewer groups.</td>
        </tr>
        <tr>
          <td>Read Confirmation or Process Rating?</td>
          <td>Use Read Confirmation for acknowledgement of process content; use Process Rating for structured feedback on a process revision.</td>
        </tr>
        <tr>
          <td>User Task or Multi-User Task?</td>
          <td>Use User Task for one assignee; use Multi-User Task when several people must each perform the same work and their results must be collected.</td>
        </tr>
        <tr>
          <td>Re-Publish or Restore?</td>
          <td>Re-Publish changes which published version future cases use; Restore changes the editable draft without changing the currently published execution version.</td>
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
      <li>Object Management Group — <a href="https://www.omg.org/spec/BPMN/2.0.2/PDF">BPMN 2.0.2 specification</a>.</li>
      <li>SAP Signavio Process Manager — <a href="https://help.sap.com/docs/signavio-process-manager/workspace-admin-guide/manage-security-settings">Workspace security settings</a>.</li>
      <li>SAP Signavio Process Manager — <a href="https://help.sap.com/docs/signavio-process-manager/workspace-admin-guide/enable-sso">Single Sign-On using SAML</a>.</li>
      <li>SAP Signavio Process Manager — <a href="https://help.sap.com/docs/signavio-process-manager/user-guide/custom-graphics">Custom graphics</a>.</li>
      <li>SAP Signavio Process Governance — <a href="https://help.sap.com/docs/signavio-process-governance/user-guide/organization-settings">Organization settings</a>.</li>
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
