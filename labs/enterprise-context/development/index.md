---
layout: default
title: "SAP Development Architecture — RAP, CAP, ABAP Cloud and Clean Core"
description: "A practical SAP development architecture guide to ABAP Cloud, RAP, CAP, on-stack and side-by-side extensions, BTP runtimes, and clean-core trade-offs."
permalink: /labs/enterprise-context/development/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-23
hide_global_cta: true
tags:
  - sap
  - abap
  - rap
  - cap
  - cds
  - btp
  - clean-core
  - architecture
last_reviewed: 2026-09-23
publication_wave: "lead-architecture-search-wave-03"
review_method: "SAP primary sources + September 2026 CAP release check + full editorial rewrite"
search_intent: "SAP clean core development with ABAP Cloud, RAP, CAP and BTP"
# ai-discovery-managed:start
structured_data:
  type: TechArticle
primary_topic: "sap-s4hana"
ai_sidecar: "/ai/pages/labs--enterprise-context--development.json"
semantic_links:
  - type: "prerequisite"
    title: "SAP S/4HANA Deployment Models — Enterprise Context Lab"
    url: "/labs/enterprise-context/deployment-models/"
  - type: "integrates_with"
    title: "SAP Integration Architecture — Logistics, Events and Data Distribution"
    url: "/labs/enterprise-context/integrations/"
  - type: "related_topic"
    title: "Where Should SAP Extension Logic Live? — Clean Core Decision Card"
    url: "/labs/enterprise-context/decisions/clean-core-extension-placement/"
  - type: "related_topic"
    title: "SAP Business AI and AI Platform Landscape — Enterprise Context Lab"
    url: "/labs/enterprise-context/business-ai/"
  - type: "related_topic"
    title: "SAP Decision Cards — Enterprise Context Lab"
    url: "/labs/enterprise-context/decisions/"
  - type: "same_domain"
    title: "SAP Performance and Technical Operations — Practical S/4HANA Troubleshooting"
    url: "/labs/enterprise-context/performance/"
source_links:
  - title: "Working with ABAP for Cloud Development and Released APIs"
    url: "https://help.sap.com/docs/ABAP_PLATFORM_NEW/b5670aaaa2364a29935f40b16499972d/ef0301f6b908409c8e0802270a96a316.html"
  - title: "ABAP RESTful Application Programming Model"
    url: "https://help.sap.com/docs/abap-cloud/abap-rap/analytics-annotations"
  - title: "Developing Unmanaged Transactional Apps"
    url: "https://help.sap.com/docs/r/fc4c71aa50014fd1b43721701471913d/latest/en-US/f6cb3e3402694f5585068e5e5161a7c1.html"
  - title: "SAP BTP ABAP Environment"
    url: "https://help.sap.com/docs/btp/sap-business-technology-platform/abap-environment"
  - title: "Developing with CAP in SAP BTP Cloud Foundry and Kyma Runtimes"
    url: "https://help.sap.com/docs/btp/btp-developers-guide/cloud-application-programming-model"
  - title: "CAP Releases"
    url: "https://cap.cloud.sap/docs/releases/"
  - title: "Extend SAP S/4HANA in the Cloud and On-Premise with ABAP-Based Extensions"
    url: "https://www.sap.com/documents/2022/10/52e0cd9b-497e-0010-bca6-c68f7e60039b.html"
# ai-discovery-managed:end
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li aria-current="page">Development Architecture</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise Context Lab / Development architecture</p>
      <h1>Choose the transaction boundary<br />before the framework.</h1>
      <p>RAP, CAP, ABAP Cloud, CDS, SAP BTP, Cloud Foundry, and Kyma are not competing products at the same level. A sound design starts with where the business state lives, how tightly new logic must participate in that transaction, and whether an independent lifecycle is worth the extra system boundary.</p>
      <a class="research-canvas__button" href="#decision-matrix">Choose the boundary <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Development architecture summary">
      <p>Three useful layers</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>On-stack</strong><small>Logic belongs with the S/4HANA transaction</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Side-by-side</strong><small>Capability earns an independent lifecycle</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Contract</strong><small>Released APIs and stable extension points</small></div>
      <em>Architecture before tooling</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">architecture</span>
    <div>
      <p><strong>The main choice is not RAP versus CAP.</strong> First decide whether the capability belongs inside the S/4HANA transaction or beside it. RAP is an ABAP programming model. CAP is a cloud application framework. Both can be correct in the same end-to-end solution.</p>
      <p>Moving logic out of S/4HANA can reduce core coupling, but it also creates a network boundary, a second runtime, separate identity and monitoring, and a consistency problem to manage. Decoupling is useful only when that independence buys something real.</p>
    </div>
    <a href="/labs/enterprise-context/deployment-models/">Compare S/4HANA deployment models <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="decision-matrix" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Placement decision</p>
      <h2>Four questions usually narrow the architecture quickly.</h2>
      <p>The purpose of these questions is not to force one technology. They expose the coupling that the solution must carry for years after the first release.</p>
    </header>
    <div class="ecg-decision-columns">
      <div>
        <h3>Where is the authoritative transaction?</h3>
        <p>If the rule must validate, derive, or persist data as part of an S/4HANA business transaction, keeping it close to that transaction avoids a remote dependency during save. If the capability owns its own state and process, a separate runtime becomes more natural.</p>
      </div>
      <div>
        <h3>Which stable contract exists?</h3>
        <p>For new ABAP Cloud development, start from released APIs, released objects, and supported extension points. A convenient internal table or class is not automatically a stable contract for custom code.</p>
      </div>
      <div>
        <h3>What independence do we need?</h3>
        <p>Side-by-side is easier to justify when the capability spans several systems, serves external users, needs another technology stack, has different scaling needs, or must evolve on a lifecycle independent of S/4HANA.</p>
      </div>
      <div>
        <h3>What failure model are we creating?</h3>
        <p>A remote service can be unavailable while S/4HANA is healthy. Before placing synchronous logic outside the core, decide what happens on timeout, retry, duplicate requests, partial completion, and recovery.</p>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">On-stack development</p>
      <h2>Use ABAP Cloud when new logic belongs in the ABAP transaction.</h2>
      <p>ABAP Cloud is a development model built around a restricted ABAP language version and released development objects. SAP uses release contracts to limit custom code to APIs and objects intended to remain stable. This is the important clean-core property: the dependency is governed, not merely written in a newer syntax.</p>
    </header>
    <p>For a small supported change, key-user extensibility may be enough. For a real transactional extension, developer extensibility with ABAP Cloud can use CDS, RAP, released APIs, and defined extension points while staying on the ABAP stack. This keeps local data access, authorizations, and transactional behavior close to the process they extend.</p>
    <p>RAP is the programming model for transactional business objects, OData services, Web APIs, and Fiori-oriented applications in ABAP Cloud. In a <strong>managed</strong> RAP business object, the framework owns much of the standard transactional behavior. In an <strong>unmanaged</strong> business object, the application implements the essential transactional contract and can integrate existing business logic. Unmanaged RAP is therefore useful when the service boundary should modernize without pretending mature backend logic does not exist.</p>
    <div class="ecg-caption"><strong>Practical rule:</strong> do not create a remote service only to move a small deterministic validation away from the transaction that owns it. If the rule must succeed or fail with the S/4HANA save, an on-stack extension is often the simpler architecture.</div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Side-by-side development</p>
      <h2>Move outside S/4HANA when the capability has a real reason to be independent.</h2>
      <p>SAP BTP gives several runtime choices, and the programming model should follow the workload rather than the diagram.</p>
    </header>
    <div class="ecg-decision-columns">
      <div>
        <h3>CAP on Cloud Foundry or Kyma</h3>
        <p>The SAP Cloud Application Programming Model provides CDS-based domain and service modeling with Node.js/TypeScript or Java runtimes. It fits independent services and applications that integrate with SAP and non-SAP systems. SAP documents productive CAP deployment on both Cloud Foundry and Kyma runtimes.</p>
      </div>
      <div>
        <h3>SAP BTP ABAP Environment</h3>
        <p>This is a side-by-side ABAP runtime, not a copy of the S/4HANA database. It supports ABAP Cloud, RAP, CDS, Fiori-related development, released objects, and a dedicated managed SAP HANA database. It is useful when an independent lifecycle is needed but ABAP remains the right development model.</p>
      </div>
      <div>
        <h3>The S/4HANA contract still matters</h3>
        <p>A side-by-side application should consume a supported API, event, or other governed interface. Moving the code to BTP does not make an unreleased S/4HANA dependency clean or stable.</p>
      </div>
    </div>
    <p>Once the boundary is remote, design it as a distributed system. Identity propagation, authorization, connectivity, retries, idempotency, observability, data ownership, and reconciliation are part of the application architecture. They are not integration details to add after development.</p>
    <div class="ecg-caption"><strong>Boundary with Integration:</strong> the <a href="/labs/enterprise-context/integrations/">Integration Architecture guide</a> covers message contracts, synchronous and asynchronous interaction, brokers, recovery, and business-level reconciliation.</div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">RAP and CAP</p>
      <h2>Compare ownership, not acronyms.</h2>
      <p>RAP and CAP can both expose services and support Fiori applications, but they start from different runtime and ownership assumptions.</p>
    </header>
    <div class="ecg-decision-columns">
      <div>
        <h3>Prefer RAP when</h3>
        <p>The business object and transaction belong to an ABAP runtime, the extension needs local S/4HANA semantics or ABAP services, and the required released contracts are available.</p>
      </div>
      <div>
        <h3>Prefer CAP when</h3>
        <p>The capability is an independent cloud service or application, spans systems, needs Node.js/TypeScript or Java, serves a broader audience, or benefits from a lifecycle separate from the ERP release.</p>
      </div>
      <div>
        <h3>Use both when</h3>
        <p>S/4HANA should remain the owner of the core transaction while a BTP application owns a separate process or experience. The ABAP side exposes a stable contract; the cloud side consumes it without reaching into ERP internals.</p>
      </div>
    </div>
    <p class="ecg-caption">CAP is an actively released framework. The September 2026 release line is CAP Node.js 10.1 and CAP Java 5.1. Version numbers are useful for dependency management, but they should not drive the placement decision.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Clean core</p>
      <h2>Clean core is dependency discipline, not a ban on every line of classic ABAP.</h2>
      <p>SAP's current ABAP extensibility guidance moved from the older three-tier model to clean-core levels. ABAP Cloud is the recommended model for new custom extensions because it enforces released contracts and upgrade-stable dependencies. For SAP S/4HANA Cloud Private Edition and on-premise, SAP's newer guidance also classifies classic ABAP by the quality of the dependencies and extension techniques used.</p>
    </header>
    <p>That distinction matters in real systems. Existing classic ABAP does not become harmless, but neither does it become useful to label every object simply “not clean.” A better modernization plan identifies unreleased or fragile dependencies, separates them behind clear boundaries, replaces them where supported alternatives exist, and uses ABAP Cloud for new development whenever the requirement can be met that way.</p>
    <p>SAP S/4HANA Cloud Public Edition has stricter developer-extensibility boundaries. Private Edition and on-premise provide more room for classic ABAP, but that freedom increases the need for governance rather than removing it.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Three examples</p>
      <h2>The boundary becomes clearer when the requirement is concrete.</h2>
    </header>
    <div class="ecg-decision-columns">
      <div>
        <h3>Validate an S/4HANA transaction before save</h3>
        <p>If the rule depends on local transactional state and must block the same save, use a supported on-stack extension point where available. A synchronous call to a remote BTP service adds failure modes without creating useful independence.</p>
      </div>
      <div>
        <h3>Build a supplier workspace across several systems</h3>
        <p>If the application combines multiple ERP systems, external users, and its own workflow or state, a side-by-side application is a stronger boundary. CAP is a natural candidate when its Java or Node.js stack fits the team and requirements.</p>
      </div>
      <div>
        <h3>Expose mature legacy behavior through a modern service</h3>
        <p>If proven ABAP logic must remain the execution engine, an unmanaged RAP business object can integrate existing behavior while providing a modern service contract. Rewriting stable business logic only to obtain a “managed” label is not an architecture goal.</p>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Tooling</p>
      <h2>Choose tools after the runtime and programming model.</h2>
      <p>ABAP development uses ABAP Development Tools, while CAP commonly uses VS Code or SAP Business Application Studio with the normal Node.js or Java toolchain. Tool support changes over time; it should not be confused with the production runtime or with the stability of an API contract.</p>
    </header>
    <p>A useful engineering baseline is simpler than a tool catalogue: version the code, automate tests, use static checks where the platform provides them, keep dependencies explicit, and test the real system boundary. A clean-core design with weak testing is still difficult to change safely.</p>
  </section>

  <section class="research-canvas__inventory" id="evidence" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Primary sources</p>
      <h2>Release-sensitive claims are checked against current SAP documentation.</h2>
      <p>The sources below cover ABAP Cloud and released APIs, RAP, unmanaged RAP, SAP BTP ABAP Environment, CAP runtime choices, the September 2026 CAP release line, and SAP's current clean-core extensibility guidance. Exact feature availability still depends on the target S/4HANA edition and release.</p>
    </header>
    <div class="research-route-list">
      {% for source in page.source_links %}
      <a href="{{ source.url }}" target="_blank" rel="noopener"><span>SRC</span><strong>{{ source.title }}</strong><small>Primary product or framework documentation</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="ecg-machine" data-reveal>
    <div>
      <p class="research-canvas__eyebrow">Structured material</p>
      <h2>The detailed architecture model remains machine-readable.</h2>
      <p>The JSON layer keeps the wider technology map and decision material without forcing the article to read like a catalogue.</p>
    </div>
    <div class="ecg-machine__actions">
      <a class="research-canvas__button" href="/labs/enterprise-context/data/development.json">Development architecture JSON <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>
      <a href="/labs/enterprise-context/decisions/clean-core-extension-placement/">Clean-core placement decision</a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
