---
layout: default
title: "SAP MM Sourcing Overview"
description: "How source determination works in SAP MM, including purchasing info records, source lists, quota arrangements, contracts, and scheduling agreements."
permalink: /atlas/sap/sap-mm-sourcing-overview/
atlas_section: sap
domain: SAP operations
subdomain: Procurement and sourcing
concept_type: SAP concept
sap_area: MM purchasing / sourcing
business_process: Procure to pay
status: needs_verification
verified: false
last_reviewed: 2026-09-22
author: Dzmitryi Kharlanau
tags:
  - procure-to-pay
  - sap-mm
  - procurement
  - sourcing
related:
  - /atlas/sap/sap-mm-procurement-overview/
  - /atlas/diagnostics/sap-source-determination-diagnostics/
  - /atlas/sap/gr-ir-clearing-explained/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP MM Sourcing Overview</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas SAP Note</p>
    <h1>SAP MM sourcing overview</h1>
    <p class="note-subtitle">How SAP connects a procurement requirement with a permitted and useful source of supply.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM purchasing / sourcing</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until sourcing claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What sourcing means in SAP MM</h2>
    <p>A purchase requisition can describe a perfectly valid requirement and still not answer one important question: who should supply it? Source determination is the part of purchasing that connects the requirement with a source of supply. Depending on the scenario, that source may be represented by a purchasing info record, a source-list entry, a contract, a scheduling agreement, or a source participating in a quota arrangement.</p>

    <p>These objects do different jobs, so it helps not to treat them as interchangeable. An info record describes a purchasing relationship between a supplier and a material for an organizational context. A source list controls which sources are valid or preferred for a material and plant during a period. An outline agreement provides a longer-term commercial reference. A quota arrangement influences how requirements are distributed among several allowed sources.</p>

    <h2>Purchasing info records</h2>
    <p>A purchasing info record stores supplier-material purchasing data such as prices and conditions, planned delivery time, and other procurement information. It gives SAP a maintained relationship to work with, but its existence alone does not mean that the supplier will always be selected. Source determination also considers the rest of the sourcing context.</p>

    <p>This distinction is important. We can have a valid info record and still get no automatic source because another sourcing object restricts the choice, the validity does not fit, or the process requires a different reference.</p>

    <h2>Source lists</h2>
    <p>A source list is maintained for a material and plant over a validity period. It can identify permitted sources, fixed sources, or blocked sources. In processes where source-list use is required, an otherwise valid supplier relationship may still be unusable if the source-list entry is missing, expired, or excludes that source.</p>

    <p>The date matters because sourcing is about a requirement at a point in time. A source that was valid last month is not automatically valid for a requisition with a delivery date next month.</p>

    <h2>Quota arrangements</h2>
    <p>A quota arrangement is used when procurement should be distributed across several sources. It is not simply a static percentage split applied independently to every purchase requisition. SAP keeps track of quantities already allocated to the sources and calculates a <em>quota rating</em>. During source determination, that rating helps decide which source should receive the next requirement.</p>

    <p>The basic idea is balancing over time. A source with a larger quota should receive a larger share of the total requirement, but the next assignment also depends on what has already been allocated and on the quota base quantity. This is why two suppliers with the same current demand do not necessarily receive the next requisition in the way a simple percentage calculation would suggest.</p>

    <h2>Contracts and scheduling agreements</h2>
    <p>Contracts and scheduling agreements are outline agreements, but their operational use is different. A contract defines agreed conditions for a period or target quantity/value and is referenced by later purchasing documents. A scheduling agreement goes further by supporting delivery schedules against the agreement.</p>

    <p>Both can act as sources of supply when they are valid for the requirement and the surrounding sourcing rules allow them. This means sourcing is not only about finding a supplier name. It can also be about finding the correct commercial document behind that supplier relationship.</p>

    <h2>How the pieces work together</h2>
    <p>There is no useful universal rule such as “SAP always checks info record, then source list, then quota.” The exact determination depends on the application and configuration. In classic purchasing source determination, a valid quota arrangement can have priority; the source list can then restrict or identify valid sources, and outline agreements or info records can provide source details. Other processes, such as MRP or PP/DS, have their own documented sourcing behavior.</p>

    <p>That is why a sourcing issue should be explained in its process context. We first identify where the source is being determined — for example, during requisition processing, MRP, or another planning flow — and only then interpret the relevant master data.</p>

    <h2>A small example</h2>
    <p>Suppose a plant buys the same material from two suppliers. Both have valid purchasing data. A quota arrangement is configured because the business wants to distribute the volume. SAP does not merely alternate suppliers or assign a fixed percentage to each single requisition. It compares the maintained quotas with the quantities already allocated and uses the resulting quota rating when assigning the next source.</p>

    <p>If the expected supplier is not selected, the explanation may be completely correct from SAP's point of view: the source is valid, but the current quota state favors the other supplier. That is a different problem from an expired source-list entry or a missing info record, even though all three can look like “wrong supplier determination” to the user.</p>

    <h2>What this page does not cover</h2>
    <p>Sourcing behavior differs across classic purchasing, MRP, PP/DS, SAP Ariba, retail scenarios, and custom processes. This page explains the core MM concepts rather than one universal search sequence. For a concrete incident, use the process-specific source-determination documentation and the system's actual master data.</p>

    <h2>Sources</h2>
    <ul>
      <li>SAP Learning — <a href="https://learning.sap.com/courses/purchasing-in-sap-s-4hana/identifying-additional-aspects-of-source-determination">Identifying Additional Aspects of Source Determination</a>.</li>
      <li>SAP Learning — <a href="https://learning.sap.com/courses/sourcing-in-sap-s4hana/introducing-quota-arrangements-in-sap-s-4hana">Introducing Quota Arrangements in SAP S/4HANA</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/0e602d466b99490187fcbb30d1dc897c/57c7e45776bddf12e10000000a4450e5.html">Manage Sources of Supply</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8a57feade137489098f59374c06f1e0e/f006b753128eb44ce10000000a174cb4.html">Maintain Quota Arrangement</a>.</li>
    </ul>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP MM Procurement Overview</a></li>
      <li><a href="/atlas/diagnostics/sap-source-determination-diagnostics/">SAP Source Determination Diagnostics</a></li>
      <li><a href="/atlas/sap/gr-ir-clearing-explained/">SAP GR/IR Clearing Explained</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
