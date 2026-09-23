---
layout: default
title: "CI/CD"
description: "How continuous integration and delivery fit SAP development, testing, deployment, and transport management."
permalink: /atlas/sap/cicd/
atlas_section: sap
domain: SAP operations
subdomain: Developer and platform technologies
concept_type: technology
sap_area: "CI/CD"
business_process: "Application development"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - cicd
  - devops
  - pipeline-automation
related:
  - /atlas/sap/cap/
  - /atlas/sap/abap-cloud/
  - /atlas/sap/sap-btp/
  - /atlas/sap/documentation-as-code/
  - /atlas/sap/static-site-generation/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">CI/CD</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>CI/CD</h1>
    <p class="note-subtitle">Continuous integration and delivery for SAP and enterprise development.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Application development</dd></div>
      <div><dt>SAP area</dt><dd>CI/CD</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until technology claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>CI/CD is not the transport system</h2>
    <p>CI/CD automates the path from a source-code change to a tested, releasable version of software. Continuous integration (CI) gives developers fast feedback: fetch the change, build it, run tests and quality checks, and stop early when something is wrong. Continuous delivery (CD) takes a version that passed those checks and prepares or promotes it toward a target environment.</p>

    <p>In an SAP landscape, this does not remove transport management. A pipeline answers questions such as <em>does this version build and pass our checks?</em> The transport or deployment mechanism answers a different question: <em>how does this approved version move into the next system or tenant?</em> Good delivery design connects the two without pretending they are the same thing.</p>

    <h2>The shape depends on the SAP development model</h2>
    <p>For applications on SAP BTP, source code normally lives in Git and the pipeline can look familiar to teams outside SAP. SAP Continuous Integration and Delivery provides predefined pipelines that connect to Git repositories and automate build, test and deployment steps for supported development scenarios. A team can also use its existing CI platform when that better fits the engineering landscape.</p>

    <p>Promotion between BTP environments is a separate concern. SAP Cloud Transport Management manages development artifacts and application-specific content across a transport landscape. For supported content, a pipeline can hand a release to Cloud Transport Management instead of deploying independently to every environment. This separation is useful when QA and production promotion need their own authorization, audit trail or approval process.</p>

    <p>ABAP has a different lifecycle. In classic Change and Transport System (CTS), development and Customizing changes are recorded in transport requests and tasks and moved through the SAP landscape using transport tools. Git-enabled Change and Transport System (gCTS) adds Git-based software distribution while retaining important CTS concepts: ABAP objects are still recorded in requests and tasks, then represented as files and commits in Git repositories. SAP explicitly supports integrating gCTS into CI pipelines.</p>

    <p>This is why "put SAP in Git" is too simple as a design rule. CAP applications, ABAP Cloud software components, classic ABAP development and configuration content have different lifecycle mechanisms. The pipeline must follow the delivery model of the artifact rather than force every SAP change into one generic Git workflow.</p>

    <h2>A release path in practice</h2>
    <p>Consider a CAP service deployed on SAP BTP. A developer changes the service in a feature branch. The pull request triggers automated checks. After merge, the pipeline builds the deployable artifact and runs the tests that are reliable enough to act as release gates. The resulting version can be deployed to a development environment and, where the scenario is supported, handed to SAP Cloud Transport Management for controlled promotion to QA and production.</p>

    <p>The useful part is not the number of pipeline stages. It is the chain of evidence: we know which commit produced the artifact, which checks ran, which artifact was promoted, and which target received it. Rebuilding a supposedly identical artifact separately for QA and production weakens that traceability. So does letting a deployment job fetch unpinned dependencies or silently change configuration at release time.</p>

    <h2>Quality gates should match the technology</h2>
    <p>A pipeline is valuable when its checks can reject a bad change before the change reaches a shared environment. Typical gates include unit tests, static analysis, dependency and security checks, and deployability tests. For ABAP development, ABAP Unit and ABAP Test Cockpit can be part of an automated quality strategy where the chosen lifecycle and tooling support them. For cloud applications, the build may also validate descriptors, package dependencies and deployment artifacts.</p>

    <p>Not every test belongs in CI. Tests that depend on unstable shared data or a large integrated landscape can become slow and flaky. It is often better to keep fast deterministic checks close to the commit, then run broader integration or business-process tests after deployment to a controlled test environment. A red pipeline should mean something; routinely ignored failures destroy the gate.</p>

    <h2>Where SAP delivery pipelines become difficult</h2>
    <p>The hard part is usually the boundary between software automation and landscape governance. Credentials need access to repositories and target systems without becoming permanent administrator secrets. Transport dependencies can make an otherwise valid ABAP change unsafe to import alone. Configuration may differ between environments even when the application artifact is identical. A successful technical deployment also does not prove that a business process still works with the target system's data and integrations.</p>

    <p>These problems are easier to manage when the pipeline keeps responsibilities visible: source control identifies the change, CI verifies it, an immutable or clearly identified artifact represents the release, the relevant SAP transport/deployment mechanism moves it, and post-deployment checks confirm that the target is healthy. Approvals can then protect high-risk transitions without turning every build into a manual process.</p>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/sap/cap/">CAP</a> — application model commonly delivered through Git-based cloud pipelines.</li>
      <li><a href="/atlas/sap/abap-cloud/">ABAP Cloud</a> — ABAP development model with its own software lifecycle.</li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a> — platform context for cloud runtimes and delivery services.</li>
      <li><a href="/atlas/sap/documentation-as-code/">Documentation as Code</a> — applying repository workflows to technical documentation.</li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP Continuous Integration and Delivery — <a href="https://help.sap.com/docs/continuous-integration-and-delivery">SAP Help Portal</a>.</li>
      <li>Change and Transport System, including gCTS — <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/4a368c163b08418890a406d413933ba7">SAP Help Portal</a>.</li>
      <li>SAP Cloud Transport Management — <a href="https://help.sap.com/docs/cloud-transport-management">SAP Help Portal</a>.</li>
    </ul>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/cap/">CAP</a></li>
      <li><a href="/atlas/sap/abap-cloud/">ABAP Cloud</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
