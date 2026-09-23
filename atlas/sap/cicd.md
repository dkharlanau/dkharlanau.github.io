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
    <p class="note-subtitle">How source changes become tested release candidates, then move through SAP-specific deployment and transport paths.</p>
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
    <h2>A pipeline verifies a change; it does not replace transport management</h2>
    <p>Continuous integration turns a source-code change into evidence. The pipeline checks out a known version, builds it, runs tests and quality checks, and fails early when the result is not releasable. Continuous delivery takes a version that passed those checks and prepares it for controlled promotion.</p>

    <p>That is only part of delivery in an SAP landscape. A pipeline answers whether a version passed the automated gates. The deployment or transport mechanism answers how that approved version reaches the next system, tenant, or runtime. Mixing these responsibilities makes it harder to tell which version was tested, who approved the move, and what actually reached production.</p>

    <h2>SAP has several delivery models, not one universal pipeline</h2>
    <p>SAP Continuous Integration and Delivery is one SAP BTP service for this job. It runs predefined pipelines for supported scenarios including Cloud Foundry applications, SAP Fiori for the ABAP Platform, SAP Integration Suite artifacts, Kyma runtime, and gCTS-based ABAP development. Teams can also use other CI platforms; the important point is that the pipeline must match the lifecycle of the artifact it handles.</p>

    <p>SAP Cloud Transport Management solves a different problem. It manages the controlled movement of supported development artifacts and application-specific content across a BTP transport landscape. SAP describes it as complementary to CI/CD: a pipeline can create or validate a release candidate, while transport management can provide import queues, routes, separation of duties, and an audit trail for promotion toward test and production.</p>

    <p>The service is not a generic deployment engine for every SAP object. It supports defined content types and application integrations. Current SAP documentation includes Multitarget Application archives, application-specific content, and references to SAP BTP ABAP software-component versions. The source application's transport documentation therefore matters as much as the transport service itself.</p>

    <h2>For cloud applications, preserve the identity of the release</h2>
    <p>Consider a CAP application deployed to the Cloud Foundry environment as a Multitarget Application. A useful pipeline checks the selected commit, builds the deployable archive, runs deterministic tests, and identifies the resulting artifact. The promotion step should then move that tested release through the landscape rather than quietly rebuilding a different one for each environment.</p>

    <p>This is the practical link between CI and transport management. Git identifies the source change, the pipeline produces evidence and a release artifact, and the transport path moves that release under the rules of the target landscape. Environment-specific configuration may still differ, but the software version should remain traceable from source to deployment.</p>

    <h2>Classic ABAP and gCTS keep transport semantics visible</h2>
    <p>Classic ABAP development uses Change and Transport System concepts such as transport requests and tasks. Development and Customizing changes are recorded there and later moved with the appropriate transport tools. A Git-oriented pipeline does not make those semantics disappear.</p>

    <p>Git-enabled Change and Transport System (gCTS) extends the classic model with Git-based software distribution. Developers still assign changes to transport requests and tasks. When a relevant request or task is released, gCTS converts the contained ABAP objects into files, creates a Git commit, and can push that commit to the remote repository. Target systems can then deploy a selected commit from the repository.</p>

    <p>One detail matters for traceability: the original change request is not itself persisted as the deployable Git object. The repository stores software versions as commits. On a target system, gCTS imports the object differences represented by the selected commit and uses ABAP transport tooling internally. This is why a Git commit and an ABAP transport request are related, but they are not interchangeable identifiers.</p>

    <h2>SAP BTP ABAP environment has its own software-component lifecycle</h2>
    <p>In SAP BTP ABAP environment, the main lifecycle unit is a software component with an SAP-managed Git repository. Development changes are still recorded in ABAP transport requests. Releasing a transport commits and pushes the changes to the configured branch of the software component.</p>

    <p>SAP Cloud Transport Management can then transport a reference to that software component version between ABAP environment instances. The reference can use a commit ID, branch, or tag; SAP recommends the commit ID when reproducible deployment matters because the head of a branch can move. This is a good example of why “ABAP in Git” is too broad as an architecture rule: classic CTS, on-premise gCTS, and BTP ABAP lifecycle management all use related concepts but not the same delivery path.</p>

    <h2>Quality gates need to match the technology</h2>
    <p>A good pipeline rejects defects that can be detected reliably before promotion. For cloud applications this may include unit tests, static analysis, dependency checks, descriptor validation, and artifact-build checks. In ABAP scenarios, ABAP Unit and ABAP Test Cockpit can be part of the automated gate where the chosen lifecycle supports them; SAP's gCTS pipeline guidance includes both.</p>

    <p>Not every useful test belongs before deployment. End-to-end checks often depend on shared business data, connected systems, authorizations, or environment-specific configuration. These tests are usually more reliable after deployment to a controlled test environment. The important distinction is between a build gate and a business-process validation, not the number of boxes drawn in the pipeline.</p>

    <h2>A green pipeline proves less than a successful release</h2>
    <p>A successful build proves that the configured checks passed for a known source version. It does not prove that transports were imported in the right order, that target configuration is correct, that credentials and destinations work, or that the business process behaves correctly with production-like integrations.</p>

    <p>For that reason, a strong SAP delivery chain keeps the evidence connected: source version, test result, release artifact or commit, transport request or transport reference, import result, and post-deployment checks. The tools differ by development model, but the reasoning stays the same. We should always be able to answer what changed, what was tested, what was promoted, and what reached the target.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/continuous-integration-and-delivery/sap-continuous-integration-and-delivery/what-is-sap-continuous-integration-and-delivery">What Is SAP Continuous Integration and Delivery</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/cloud-transport-management">SAP Cloud Transport Management</a> and <a href="https://help.sap.com/docs/cloud-transport-management/sap-cloud-transport-management/supported-content-types">Supported Content Types</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/4a368c163b08418890a406d413933ba7/85ca2b82afe942efb2fa244940f0453c.html">Git-Based Software Distribution</a> and <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/4a368c163b08418890a406d413933ba7/96b68f645556471083aaae0b2d574625.html">Integration of gCTS in CI Pipelines</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/sap-btp-abap-environment/abap-environment/how-to-export-using-sap-cloud-transport-management">Export Commits Using SAP Cloud Transport Management</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Pipeline templates, supported transport content, lifecycle APIs, and available deployment options change by SAP product and release. Verify the exact artifact type and target landscape before applying one delivery pattern to another.</p>
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
