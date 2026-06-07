---
layout: default
title: "CI/CD"
description: "Analytical overview of CI/CD for SAP and enterprise development: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/cicd/
atlas_section: sap
domain: SAP operations
subdomain: Developer and platform technologies
concept_type: technology
sap_area: "CI/CD"
business_process: "Application development"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
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
    <p class="note-subtitle">Continuous integration and continuous delivery for SAP and enterprise development.</p>
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
    <h2>What it is</h2>
    <p>CI/CD is the practice of automating build, test, and deployment stages for software changes. In the SAP context it covers ABAP Git, gCTS, BTP CI/CD services, and third-party tools such as GitHub Actions, GitLab CI, Jenkins, and Azure DevOps.</p>

    <h2>Business purpose</h2>
    <p>Reduce manual effort, catch defects early, and deliver changes to production faster and more predictably. Automated pipelines enforce quality gates before code reaches any SAP system.</p>

    <h2>Where it sits in the landscape</h2>
    <p>CI/CD pipelines run outside SAP systems, typically on cloud-hosted runners or on-premise build servers. They interact with SAP systems via gCTS, abapGit, BTP transport management, or direct deployment APIs.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Pipeline definition: YAML or Groovy scripts describing stages.</li>
      <li>Source repository: Git commits, branches, pull requests.</li>
      <li>Build artifact: compiled code, transport request, or container image.</li>
      <li>Test suite: unit tests, integration tests, static analysis results.</li>
      <li>Deployment target: development, quality, or production SAP system.</li>
      <li>Transport request: ABAP change container for landscape promotion.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>SAP BTP: Cloud Foundry deployments, Kyma container builds.</li>
      <li>S/4HANA: gCTS, abapGit, transport management.</li>
      <li>Git providers: GitHub, GitLab, Bitbucket webhooks and runners.</li>
      <li>Testing: ATC, ABAP unit, SAP Fiori test automation.</li>
      <li>Monitoring: pipeline dashboards, deployment logs, system health checks.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom pipeline stages for security scanning or compliance checks.</li>
      <li>Pre-deployment validation scripts against target system metadata.</li>
      <li>Post-deployment smoke tests and health verification.</li>
      <li>Integration with ticketing systems for change tracking.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Pipeline execution logs: stage duration, failure points, retry counts.</li>
      <li>Test coverage reports and static analysis score trends.</li>
      <li>Deployment frequency, lead time, change failure rate.</li>
      <li>System availability after deployment via health endpoints.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Fast feedback loops for developers through automated testing.</li>
      <li>Repeatable, auditable deployments across landscapes.</li>
      <li>Reduced risk of production incidents from manual errors.</li>
      <li>Support for both ABAP and modern cloud-native stacks.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>ABAP transport dependencies can block parallel development.</li>
      <li>Pipeline secrets and credentials require strict rotation policies.</li>
      <li>Test data availability limits integration test coverage.</li>
      <li>Complex multi-system landscapes increase pipeline maintenance.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Pipeline failure — syntax error, missing dependency, or runner timeout.</li>
      <li>Deployment blocked — transport conflict, locked object, or missing approval.</li>
      <li>Test flakiness — unstable test data or environment drift.</li>
      <li>Credential expiry — service user or certificate rotation missed.</li>
      <li>Post-deployment regression — missing smoke test or data inconsistency.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/sap/cap/">CAP</a></li>
      <li><a href="/atlas/sap/abap-cloud/">ABAP Cloud</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/documentation-as-code/">Documentation as Code</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>GitHub Actions documentation — <a href="https://docs.github.com/en/actions">docs.github.com/en/actions</a>.</li>
      <li>GitLab CI/CD documentation — <a href="https://docs.gitlab.com/ee/ci/">docs.gitlab.com/ee/ci</a>.</li>
      <li>SAP BTP Continuous Integration and Delivery — <a href="https://help.sap.com/docs/btp/sap-business-technology-platform/continuous-integration-and-delivery">SAP Help Portal</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public documentation. Specific SAP CI/CD features, supported tools, and BTP service availability vary by release and must be verified against current SAP documentation.</p>

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
