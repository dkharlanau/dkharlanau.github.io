---
layout: default
title: "SAP Integration Architecture Consulting — APIs, Events, and Clean-Core Boundaries"
description: "SAP integration architecture consulting for APIs, events, IDoc, OData, Integration Suite, and clean-core boundaries across S/4HANA landscapes."
permalink: /services/sap-integration-architecture/
last_modified_at: 2026-07-25
---

<section class="section note-detail">
  <article class="note-article neub-card">
    <header class="note-header">
      <p class="eyebrow">Service</p>
      <h1>SAP integration architecture consulting for stable and portable landscapes</h1>
      <p class="note-subtitle">Design contracts and boundaries that let S/4HANA stay stable while the edge keeps evolving.</p>
    </header>
    <div class="note-body">
      <p>I start integration design with ownership, not protocol. I want to know which system owns the business fact, which systems are allowed to derive or copy it, where transformation logic is maintained, and how the process proves completion after a handoff. Only then do I choose the API, event, IDoc, file, or middleware pattern. My bias is to keep authoritative transactional decisions close to the system that owns them and make edge services replaceable through explicit contracts.</p>

      <h2>What problem this addresses</h2>
      <p>Most landscapes do not need another argument about whether APIs are better than IDocs or events. They need a reliable answer to more practical questions: which system owns the business fact, where mapping logic is maintained, how a failure is detected and recovered, how duplicate or late messages are handled, and who can change the contract without surprising downstream teams.</p>

      <div class="process-rail" aria-label="Integration architecture decision process">
        <div class="process-rail__step"><strong>Inventory</strong><span>Make the business capability, systems, contracts, and operational dependencies visible.</span></div>
        <div class="process-rail__step"><strong>Assign truth</strong><span>Identify the authoritative state and what each other system may consume or derive.</span></div>
        <div class="process-rail__step"><strong>Design recovery</strong><span>Define observability, retries, reconciliation, and accountable recovery before adding scale.</span></div>
        <div class="process-rail__step"><strong>Choose the pattern</strong><span>Select the narrowest pattern that satisfies timing, control, change, and lifecycle needs.</span></div>
      </div>

      <h2>Typical architecture topics</h2>
      <ul>
        <li>OData v2 or v4, REST, IDoc, AIF, SAP Integration Suite, and event-driven patterns.</li>
        <li>Broker choice, schema versioning, replay strategy, and observability design.</li>
        <li>Clean-core boundary decisions for validation, orchestration, analytics, and automation.</li>
      </ul>

      <h2>Expected outputs</h2>
      <ul>
        <li>Integration blueprint with runtime boundaries and ownership model.</li>
        <li>API or event contract guidance, including portability and exit tests.</li>
        <li>Prioritised recommendations for reliability, cost control, and upgrade safety.</li>
      </ul>

      <h2>Decision framework</h2>
      <div class="decision-table"><table><thead><tr><th>Question</th><th>Why it changes the design</th></tr></thead><tbody>
        <tr><td>Is the consumer asking for a current fact, a historical event, or a controlled command?</td><td>It separates read access, event distribution, and transactional action instead of treating them as the same interface.</td></tr>
        <tr><td>What happens when a message is late, duplicated, malformed, or accepted technically but rejected by business rules?</td><td>It makes replay, idempotency, reconciliation, and exception ownership part of the architecture.</td></tr>
        <tr><td>Who owns the contract and can approve a breaking change?</td><td>It prevents a technically successful change from becoming a downstream operational failure.</td></tr>
        <tr><td>What must remain close to SAP transactional truth?</td><td>It helps protect clean-core boundaries without pretending that every capability belongs outside S/4.</td></tr>
      </tbody></table></div>

      <h2>Assessment questions</h2>
      <ul>
        <li>Which system owns the business fact, and which systems only consume a copy or an event?</li>
        <li>Where is transformation logic documented, versioned, tested, and recoverable?</li>
        <li>How does the team prove business completion after a technically successful handoff?</li>
        <li>Which parts of the flow require deterministic control, and where is asynchronous processing acceptable?</li>
      </ul>

      <h2>What this avoids</h2>
      <p>I do not treat APIs or events as a maturity badge. A stable landscape can legitimately keep several integration patterns when ownership, contracts, observability, and recovery are explicit. The expensive state is not "old technology" by itself; it is an accidental mix where nobody can explain who owns the contract, how failure is reconciled, or what a safe change looks like.</p>

      <h2>Public-safe example</h2>
      <p><strong>Illustrative scenario:</strong> an outbound sales event reaches an external consumer, but the downstream business process is not complete. A transport-level success is not sufficient evidence of a business outcome. The design needs a visible contract, an agreed completion signal or reconciliation step, and an owner for cases that remain in an ambiguous state. This applies whether the transport uses an IDoc, API, file, or event.</p>

      <h2>Where AI may help</h2>
      <p>AI can assist with interface-inventory normalization, contract discovery, and incident summarization. It should not infer a missing business contract or make unreviewed changes to mapping, routing, or production recovery. Those need evidence and explicit ownership.</p>

      <h2>Related diagnostics</h2>
      <p><a href="/services/sap-integration-reliability-assessment/">Integration reliability assessment</a> · <a href="/atlas/diagnostics/sap-integration-diagnostics-hub/">SAP integration diagnostics hub</a> · <a href="/atlas/concepts/integration-ownership-model/">Integration ownership model</a> · <a href="/atlas/concepts/integration-pattern-decision-matrix/">Integration pattern decision matrix</a> · <a href="/scenarios/idoc-api-integration-failures-ownership/">Interface ownership scenario</a></p>

      <h2>Related pages</h2>
      <p><a href="/about/">Profile</a> · <a href="/ai/integration-reliability/">AI routing page</a> · <a href="/datasets/DAMA/">DAMA datasets</a> · <a href="/notes/composable-erp/">Composable ERP strategy</a> · <a href="/notes/system-architecture/">System architecture note</a> · <a href="/services/sap-ai-ml-enablement/">SAP AI and ML enablement</a></p>
    </div>
  </article>
</section>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "SAP integration architecture consulting",
  "provider": {
    "@type": "Person",
    "@id": "https://dkharlanau.github.io/#dkharlanau"
  },
  "serviceType": "SAP integration architecture consulting",
  "url": "https://dkharlanau.github.io/services/sap-integration-architecture/",
  "description": "SAP integration architecture consulting for APIs, events, Integration Suite, IDoc, OData, and clean-core boundaries."
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem","position": 1,"name": "Home","item": "https://dkharlanau.github.io/"},
    {"@type": "ListItem","position": 2,"name": "Services","item": "https://dkharlanau.github.io/services/"},
    {"@type": "ListItem","position": 3,"name": "SAP integration architecture consulting","item": "https://dkharlanau.github.io/services/sap-integration-architecture/"}
  ]
}
</script>
