---
layout: default
title: "SAP Signavio Process Collaboration Hub — Process Knowledge and Navigation"
description: "A Lead-level guide to SAP Signavio Process Collaboration Hub: process landscapes, value chains, published and preview views, search, comments, approvals, read confirmations, and cross-suite navigation."
permalink: /labs/enterprise-context/signavio/collaboration-hub/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-10-04
last_reviewed: 2026-10-04
hide_global_cta: true
career_impact: mapped
career_skills:
  - lead-process-transformation
tags:
  - sap-signavio
  - process-collaboration-hub
  - business-process-management
  - process-landscape
  - value-chain
  - process-governance
  - assessment
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/labs/">Labs</a></li>
    <li><a href="/labs/enterprise-context/">SAP Enterprise</a></li>
    <li><a href="/labs/enterprise-context/signavio/">SAP Signavio</a></li>
    <li aria-current="page">Process Collaboration Hub</li>
  </ol>
</nav>

<div class="research-canvas context-graph">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">SAP Signavio / Process Collaboration Hub</p>
      <h1>The process knowledge entry point for the organization.</h1>
      <p>SAP Signavio Process Collaboration Hub gives business users one place to find published process knowledge, navigate the process landscape, follow changes, and give feedback. For a Lead, the important boundary is clear: the Hub is the consumption and collaboration surface, while process authoring, mining, governance, and transformation management remain owned by their respective Signavio capabilities.</p>
      <a class="research-canvas__button" href="#mental-model">Start with the mental model <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Collaboration Hub mental model">
      <p>Hub mental model</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Find</strong><small>Navigate process knowledge</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Understand</strong><small>See process context and responsibility</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Collaborate</strong><small>Comment, follow, approve, and confirm</small></div>
      <em>Working assessment material · noindex until reviewed</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">hub</span>
    <p><strong>Useful boundary:</strong> the Collaboration Hub is not the same as Process Modeler. The Hub is the main user-facing place to consume and collaborate on process knowledge. Editing and approval actions depend on access rights, licenses, and workspace configuration.</p>
  </section>

  <section class="research-canvas__inventory" id="mental-model" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Why the Hub exists</p>
      <h2>Process knowledge creates value only when people can find and use it.</h2>
      <p>A process repository can be technically complete and still fail if employees cannot locate the right process, understand the current version, or give feedback when reality changes.</p>
    </header>

    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Collaboration Hub responsibilities">
      <table class="study-table__table">
        <thead>
          <tr><th>Responsibility</th><th>What the Hub provides</th><th>Why it matters</th></tr>
        </thead>
        <tbody>
          <tr><td><strong>Process transparency</strong></td><td>Published process models and related information in one process-focused interface</td><td>Employees work from a shared reference instead of local documents and memory</td></tr>
          <tr><td><strong>Process knowledge management</strong></td><td>Processes, documents, systems, responsibilities, process structures, and linked content</td><td>Knowledge stays connected to the work it supports</td></tr>
          <tr><td><strong>Collaboration</strong></td><td>Comments, replies, notifications, favorites, and feedback on process content</td><td>Improvement becomes continuous instead of waiting for annual reviews</td></tr>
          <tr><td><strong>Process understanding</strong></td><td>Navigation from high-level landscape to detailed process context</td><td>Users can understand what changed, why it matters, and where their work fits</td></tr>
        </tbody>
      </table>
    </div>

    <div class="ecg-remember">
      <strong>Lead rule</strong>
      <p>Call the Hub a <em>single source of process truth</em> only inside a governed scope. It does not automatically become the source of truth for ERP transactions, master data, technical configuration, or operational telemetry.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Process landscape</p>
      <h2>Navigation should move from enterprise context to executable detail.</h2>
      <p>A common process architecture uses several levels. The exact number depends on the organization, but three to five levels are common.</p>
    </header>

    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Typical process architecture levels">
      <table class="study-table__table">
        <thead><tr><th>Level</th><th>Purpose</th><th>Example question</th></tr></thead>
        <tbody>
          <tr><td><strong>Value Chain</strong></td><td>High-level enterprise process landscape aligned with strategy</td><td>Which management, core, and support process groups exist?</td></tr>
          <tr><td><strong>Process Area</strong></td><td>Logical grouping around a business domain or responsibility</td><td>Which Sales, Finance, HR, or Supply Chain processes belong together?</td></tr>
          <tr><td><strong>End-to-End Process</strong></td><td>Cross-functional business flow from trigger to outcome</td><td>How does Procure-to-Pay or Order-to-Cash work across teams?</td></tr>
          <tr><td><strong>Subprocess</strong></td><td>Detailed reusable part of a larger process</td><td>What exactly happens in supplier receipt, approval, or exception handling?</td></tr>
        </tbody>
      </table>
    </div>

    <p>Value chains are not the only valid entry point. Navigation maps, organizational views, or customer journeys can also lead users to the relevant processes. The architecture should fit the way employees look for work, not force every organization into one hierarchy.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Hub layout</p>
      <h2>Think of the Hub as navigation, entry content, and utility controls.</h2>
      <p>The initial Hub page is designed to help users reach process knowledge quickly.</p>
    </header>

    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Main areas of SAP Signavio Process Collaboration Hub">
      <table class="study-table__table">
        <thead><tr><th>Area</th><th>Typical use</th></tr></thead>
        <tbody>
          <tr><td><strong>Left-side menu</strong></td><td>Open process diagrams, journey models, newsfeed, favorites, recent diagrams, governance tasks, and Process Intelligence analysis where licensed and authorized</td></tr>
          <tr><td><strong>Entry diagram</strong></td><td>Provide the main navigation map or process landscape for the organization</td></tr>
          <tr><td><strong>Upper-right utilities</strong></td><td>Create content where allowed, search, open help, check notifications, and switch user or view settings</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Published vs Preview</p>
      <h2>Separate the approved process from the working revision.</h2>
      <p>This is one of the most important Collaboration Hub distinctions for assessment questions.</p>
    </header>

    <div class="ecg-decision-columns">
      <div>
        <h3>Published view</h3>
        <p>Shows the published versions of items available to the user. This is the stable consumption view for normal process users.</p>
      </div>
      <div>
        <h3>Preview view</h3>
        <p>Shows the current state of items the user can access, including unpublished changes and drafts. Access depends on workspace settings and permissions.</p>
      </div>
      <div>
        <h3>Lead implication</h3>
        <p>Do not let employees treat an unpublished draft as the approved operating procedure. The release state of process knowledge is part of governance.</p>
      </div>
    </div>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">lock</span>
      <p><strong>Permission boundary:</strong> viewing unpublished content, editing, publishing, and starting approval workflows depend on access rights, feature configuration, and licenses. Do not describe these actions as universally available to every Hub user.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Navigation workflow</p>
      <h2>From landscape to process in four steps.</h2>
    </header>

    <ol>
      <li><strong>Open the process map.</strong> Start from the entry diagram or the relevant process landscape.</li>
      <li><strong>Select the business area.</strong> Move into the process area or topic that owns the business outcome.</li>
      <li><strong>Drill down.</strong> Open the linked end-to-end process or subprocess.</li>
      <li><strong>Use the process context.</strong> Review descriptions, documents, roles, process information, and other available details.</li>
    </ol>

    <p>A legend helps users understand unfamiliar BPMN symbols. Sensitive process information can also be hidden from particular user groups, so different users may not see exactly the same detail.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Find and follow knowledge</p>
      <h2>Search, favorites, recent items, news, and notifications reduce navigation cost.</h2>
      <p>Good process knowledge management is not only about storage. It must also support discovery and change awareness.</p>
    </header>

    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Collaboration Hub discovery features">
      <table class="study-table__table">
        <thead><tr><th>Feature</th><th>Use</th><th>Lead concern</th></tr></thead>
        <tbody>
          <tr><td><strong>Search</strong></td><td>Find process content, dictionary entries, documents, tasks, reports, and other indexed content; filters can narrow results</td><td>Use naming and taxonomy that business users can actually search</td></tr>
          <tr><td><strong>Favorites</strong></td><td>Keep frequently used processes easy to reach</td><td>Useful for role-based daily work</td></tr>
          <tr><td><strong>Recently visited</strong></td><td>Return quickly to recently used process content</td><td>Reduces time spent navigating large landscapes</td></tr>
          <tr><td><strong>Newsfeed and notifications</strong></td><td>See updates, comments, replies, and other relevant changes</td><td>Make important process changes visible without relying on email chains</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Collaboration</p>
      <h2>Feedback stays attached to the process context.</h2>
      <p>Users can comment on a process or, where supported, on a specific process element. Replies and notifications keep the discussion connected to the process instead of scattering it across separate communication channels.</p>
    </header>

    <div class="ecg-decision-columns">
      <div>
        <h3>Comment</h3>
        <p>Raise a question, correction, or improvement idea directly against the process context.</p>
      </div>
      <div>
        <h3>Reply and notify</h3>
        <p>Continue the discussion asynchronously and notify relevant users about new feedback.</p>
      </div>
      <div>
        <h3>Improve</h3>
        <p>Process owners can turn recurring feedback into a controlled change rather than leave it as informal knowledge.</p>
      </div>
    </div>

    <div class="ecg-remember">
      <strong>Lead rule</strong>
      <p>A comment is evidence of user feedback, not automatically an approved process change. Governance still decides whether the model should change.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Cross-suite visibility</p>
      <h2>The Hub can surface work from other Signavio capabilities.</h2>
      <p>This is useful because the employee sees process knowledge and related process work from one process-oriented entry point, while the owning product still keeps its own responsibility.</p>
    </header>

    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Cross-suite content visible from Collaboration Hub">
      <table class="study-table__table">
        <thead><tr><th>Content</th><th>Owner</th><th>Hub role</th></tr></thead>
        <tbody>
          <tr><td><strong>Workflow tasks</strong></td><td>SAP Signavio Process Governance</td><td>Provide access to tasks when the user has the required product access</td></tr>
          <tr><td><strong>Process analysis</strong></td><td>SAP Signavio Process Intelligence</td><td>Display analysis or process performance views where the workspace and user have the required access</td></tr>
          <tr><td><strong>Journey models</strong></td><td>SAP Signavio Journey Modeler</td><td>Navigate journey content together with process knowledge</td></tr>
          <tr><td><strong>Process models</strong></td><td>SAP Signavio process modeling capability</td><td>Consume published models and, for entitled users in Preview, open editing actions</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Editing and approval</p>
      <h2>Consumption, editing, approval, and publication are different permissions.</h2>
      <p>A user may be able to view a process without having the right to edit, approve, or publish it.</p>
    </header>

    <div class="ecg-determination-list">
      <article class="ecg-determination-detail">
        <header>
          <div><span>01</span><small>Edit</small></div>
          <h3>Edit from Preview</h3>
          <p>With the required access and modeling entitlement, a user can switch to Preview and open a process for editing.</p>
        </header>
      </article>
      <article class="ecg-determination-detail">
        <header>
          <div><span>02</span><small>Approve</small></div>
          <h3>Submit for approval</h3>
          <p>If an approval workflow is configured, entitled users can submit a new or changed process revision for approval.</p>
        </header>
      </article>
      <article class="ecg-determination-detail">
        <header>
          <div><span>03</span><small>Publish</small></div>
          <h3>Publish the approved process</h3>
          <p>Publication makes the selected revision available in the published Hub view, subject to access rights and workspace configuration.</p>
        </header>
      </article>
    </div>

    <p>Subprocesses can also participate in approval. With the right authorization, linked unpublished subprocesses can be included in a bulk approval and publication flow.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Read confirmations</p>
      <h2>For some processes, reading the change is itself a controlled action.</h2>
      <p>Read confirmations can ask users to confirm that they have read and reviewed a diagram. The feature must be enabled and its availability depends on administration and authorization.</p>
    </header>
    <p>This is useful when a process change needs evidence that relevant users have seen the updated process. It is not proof that the user can execute the process correctly; training, competence, and operational evidence are separate concerns.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Monitoring process analysis</p>
      <h2>Execution evidence can be brought next to process knowledge.</h2>
      <p>Where SAP Signavio Process Intelligence is licensed and accessible, running analyses and important process KPIs can be surfaced from the Hub. This creates a useful bridge between the documented process and observed performance.</p>
    </header>

    <div class="research-canvas__boundary">
      <span class="material-symbols-outlined" aria-hidden="true">query_stats</span>
      <p><strong>Do not confuse visibility with ownership.</strong> The Hub can show analysis, but Process Intelligence still owns the analysis capability and its data model. The Hub does not become the process-mining engine.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead design checklist</p>
      <h2>A useful Hub needs an information architecture, not just published diagrams.</h2>
    </header>

    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Lead checklist for Collaboration Hub design">
      <table class="study-table__table">
        <thead><tr><th>Decision</th><th>Questions to ask</th></tr></thead>
        <tbody>
          <tr><td><strong>Process architecture</strong></td><td>What are the process levels? Which navigation path will users understand?</td></tr>
          <tr><td><strong>Ownership</strong></td><td>Who owns each end-to-end process, and who approves changes?</td></tr>
          <tr><td><strong>Publication</strong></td><td>What is the difference between draft, approved, and published content?</td></tr>
          <tr><td><strong>Access</strong></td><td>Which users can consume, comment, preview, edit, approve, and publish?</td></tr>
          <tr><td><strong>Taxonomy</strong></td><td>Are process names, roles, systems, and dictionary terms consistent enough for search and reuse?</td></tr>
          <tr><td><strong>Change awareness</strong></td><td>How will people know that a process changed?</td></tr>
          <tr><td><strong>Feedback</strong></td><td>Who reviews comments and converts valid feedback into controlled improvement?</td></tr>
          <tr><td><strong>Evidence</strong></td><td>Which KPIs, analyses, read confirmations, or other evidence prove that the process is understood and performing?</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Assessment traps</p>
      <h2>Keep these distinctions clear.</h2>
    </header>

    <div class="ecg-determination-list">
      <article class="ecg-determination-detail">
        <header><div><span>01</span><small>Hub vs Modeler</small></div><h3>Hub is the consumption and collaboration surface.</h3><p>Modeling and editing require the appropriate modeling capability and permissions.</p></header>
      </article>
      <article class="ecg-determination-detail">
        <header><div><span>02</span><small>Publish vs Preview</small></div><h3>Published is the released view; Preview can include draft and unpublished changes.</h3><p>Access to Preview and editing depends on workspace configuration and rights.</p></header>
      </article>
      <article class="ecg-determination-detail">
        <header><div><span>03</span><small>Hub vs PI</small></div><h3>Hub can display Process Intelligence content; it does not perform the mining itself.</h3><p>Process Intelligence licensing and access are separate.</p></header>
      </article>
      <article class="ecg-determination-detail">
        <header><div><span>04</span><small>Comment vs Change</small></div><h3>User feedback is not an approved process revision.</h3><p>Comments can create improvement input, but process governance still controls the official change.</p></header>
      </article>
      <article class="ecg-determination-detail">
        <header><div><span>05</span><small>Read vs Competent</small></div><h3>A read confirmation proves acknowledgement, not process competence.</h3><p>Training, authorization, execution quality, and process performance need their own evidence.</p></header>
      </article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Assessment drills</p>
      <h2>Answer these without opening the page.</h2>
    </header>

    <div class="ecg-determination-list">
      <article class="ecg-determination-detail">
        <header><div><span>Q1</span><small>Purpose</small></div><h3>What is SAP Signavio Process Collaboration Hub for?</h3></header>
        <div class="ecg-remember"><strong>Answer shape</strong><p>It is the central process-focused entry point for business users to consume published process knowledge, navigate the process landscape, find related information, follow updates, and collaborate through feedback. It connects other Signavio content without replacing the products that own modeling, mining, or governance.</p></div>
      </article>
      <article class="ecg-determination-detail">
        <header><div><span>Q2</span><small>Navigation</small></div><h3>How would you structure process navigation in the Hub?</h3></header>
        <div class="ecg-remember"><strong>Answer shape</strong><p>Start with a clear enterprise entry point such as a value chain or navigation map, then drill down through process areas to end-to-end processes and subprocesses. Use consistent naming, ownership, and dictionary objects so search and navigation support each other.</p></div>
      </article>
      <article class="ecg-determination-detail">
        <header><div><span>Q3</span><small>Governance</small></div><h3>What is the difference between Published and Preview?</h3></header>
        <div class="ecg-remember"><strong>Answer shape</strong><p>Published shows released process content. Preview can show the current accessible state, including drafts and unpublished changes. Preview and editing require the relevant access. This protects the difference between working content and the approved operating reference.</p></div>
      </article>
      <article class="ecg-determination-detail">
        <header><div><span>Q4</span><small>Lead</small></div><h3>What would make a Collaboration Hub implementation fail even if all diagrams are technically correct?</h3></header>
        <div class="ecg-remember"><strong>Answer shape</strong><p>Poor process architecture, weak ownership, inconsistent naming, unclear publication rules, wrong permissions, no change communication, no feedback ownership, or content that users cannot find. The Hub succeeds when process knowledge is governed and usable, not merely stored.</p></div>
      </article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">30-second answer</p>
      <h2>How I would explain the Collaboration Hub in an assessment.</h2>
    </header>
    <blockquote>
      <p>SAP Signavio Process Collaboration Hub is the user-facing entry point for process knowledge in the Signavio suite. It lets employees navigate the process landscape, open published process models, search content, follow updates, and give feedback. The important governance distinction is Published versus Preview: Published is the released process view, while Preview can include drafts and unpublished changes for authorized users. The Hub can also surface governance tasks and Process Intelligence content, but those capabilities remain owned by their respective products.</p>
    </blockquote>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Primary evidence</p>
      <h2>Sources used for this working page.</h2>
      <p>The page is independently written from the assessment notes and checked against current SAP Learning and SAP Help. Workspace configuration, access rights, licenses, and available functions can change, so verify the target tenant before treating a feature as available to a specific user group.</p>
    </header>

    <div class="ecg-source-list">
      <article>
        <span>SAP Learning · Collaboration Hub purpose</span>
        <h3><a href="https://learning.sap.com/courses/managing-business-processes-with-sap-signavio-solutions/sap-signavio-process-collaboration-hub_ac509548-8ff6-4699-8cb1-3f9b54c211ac" rel="noopener noreferrer">SAP Signavio Process Collaboration Hub</a></h3>
        <p>Central process entry point, process transparency, knowledge management, collaboration, and process understanding.</p>
      </article>
      <article>
        <span>SAP Learning · Hub navigation</span>
        <h3><a href="https://learning.sap.com/courses/analyzing-business-processes-with-sap-signavio-solutions/navigating-through-the-collaboration-hub_f17b5290-cb7f-4448-b32a-c4c912a3bef0" rel="noopener noreferrer">Navigating through the Collaboration Hub</a></h3>
        <p>Menu, entry diagram, search, notifications, Preview and Published views, editing, approvals, read confirmations, and Process Intelligence visibility.</p>
      </article>
      <article>
        <span>SAP Learning · process collaboration</span>
        <h3><a href="https://learning.sap.com/courses/managing-business-processes-with-sap-signavio-solutions/collaborate-on-processes-in-the-hub_e28c4d24-1f1c-458e-9d77-fe1b1e1bc93d" rel="noopener noreferrer">Collaborating on Processes in the Hub</a></h3>
        <p>Comments on processes and elements, replies, notifications, and continuous feedback.</p>
      </article>
      <article>
        <span>SAP Learning · process architecture</span>
        <h3><a href="https://learning.sap.com/courses/managing-business-processes-with-sap-signavio-solutions/explaining-process-architecture-and-lifecycle_eded7a9c-509a-4424-b275-b537550fe36d" rel="noopener noreferrer">Explaining Process Architecture and Lifecycle</a></h3>
        <p>Value chains, process areas, end-to-end processes, subprocesses, alternative navigation maps, and the typical three-to-five-level architecture.</p>
      </article>
      <article>
        <span>SAP Help · Collaboration Hub user guide</span>
        <h3><a href="https://help.sap.com/doc/966865eb1a274bccadc05e0bded96694/SHIP/en-US/sap-signavio-process-collaboration-hub-user-guide-EN.pdf" rel="noopener noreferrer">SAP Signavio Process Collaboration Hub User Guide</a></h3>
        <p>Current product documentation, including Preview and Published view behavior.</p>
      </article>
      <article>
        <span>SAP Help · Process Manager</span>
        <h3><a href="https://help.sap.com/docs/SIGNAVIO_PROCESS_MANAGER/8365d6ee9cdb46a5a22243a9922e96d2/fa8c00bd6dad1014a4730ff5fb2ca89e.html" rel="noopener noreferrer">Publishing Diagrams</a></h3>
        <p>Publishing rights, published revisions, and how diagrams become available in the Hub.</p>
      </article>
      <article>
        <span>SAP Help · licenses and access</span>
        <h3><a href="https://help.sap.com/docs/signavio-process-modeler/workspace-admin-guide/about-licenses" rel="noopener noreferrer">License Assignment</a></h3>
        <p>Hub access, commenting licenses, feature restrictions, and Process Intelligence access boundaries.</p>
      </article>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
