---
author: "Dzmitryi Kharlanau"
layout: default
title: "Systems Analysis — Skill Group Index"
description: "Practical working skills for systems analysts: mapping entity states, lifecycles, and interface requirements across system boundaries."
permalink: /skill-hub/systems-analysis/
last_modified_at: 2026-06-12
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li aria-current="page">Systems Analysis</li>
  </ol>
</nav>

<section class="section atlas-hero">
  <p class="eyebrow">Skill Hub — Systems Analysis</p>
  <h1>Systems Analysis skills</h1>
  <p class="lead">Practical working skills for systems analysts, business analysts, and SAP consultants who need to map how entities behave inside systems, how they move between states, and what data crosses boundaries between systems.</p>
</section>

<section class="section">
  <header class="section-heading">
    <h2>What this group covers</h2>
  </header>
  <p>This skill group covers the core systems analysis activities that help teams understand, document, and improve how data and entities behave across enterprise and SAP landscapes. It focuses on two complementary areas: the internal lifecycle of an entity (states, events, transitions, guards) and the external requirements for data crossing system boundaries (what data, in which direction, under what conditions, with what quality and error handling).</p>
  <p>The skills here are designed to be used by humans and AI agents together. Each page includes decision rules, templates, quality checklists, and explicit agent instructions. They are not framework encyclopedias. They are methods for producing reviewable artifacts and making defensible decisions before design or configuration begins.</p>
</section>

<section class="section">
  <header class="section-heading">
    <h2>Skills in this group</h2>
  </header>
  <div class="topic-grid">
    <div class="topic-card">
      <h3><a href="/skill-hub/systems-analysis/state-lifecycle-analysis-working-skill/">State and Lifecycle Analysis</a></h3>
      <p>Map the states an entity passes through, the events that trigger transitions, and the conditions that must hold at each stage so that no invalid state reaches production.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/systems-analysis/interface-requirement-analysis-working-skill/">Interface Requirement Analysis</a></h3>
      <p>Define what data crosses a system boundary, in which direction, under what conditions, and with what quality and error-handling requirements.</p>
    </div>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <h2>When to use this group</h2>
  </header>
  <ul>
    <li>A sales order, business partner, or material master is stuck in an unexpected status and you need to understand how it got there.</li>
    <li>You are designing a new interface and need to define what data crosses the boundary before technical design begins.</li>
    <li>An incident reveals a race condition between parallel workflows or statuses for the same entity.</li>
    <li>A data quality issue at a system boundary is recurring and the root cause is unclear.</li>
    <li>You need to validate that a new document type or workflow has no deadlocks, invalid states, or missing transitions.</li>
    <li>An AI agent is helping you produce analysis artifacts and you need structured instructions to guide its output.</li>
  </ul>
</section>

<section class="section">
  <header class="section-heading">
    <h2>How the skills connect</h2>
  </header>
  <ol>
    <li><strong>State and Lifecycle Analysis</strong> maps the internal behavior of an entity — the states it occupies, the events that move it, and the guards that protect each transition.</li>
    <li><strong>Interface Requirement Analysis</strong> defines what data crosses the boundary when that entity or its related data must move to another system.</li>
    <li><strong>System Context Mapping</strong> (from Architecture) provides the surrounding system boundaries that both skills operate within.</li>
    <li><strong>Process Analysis</strong> (from Business Analysis) provides the business process context that gives meaning to the states and transitions.</li>
  </ol>
  <p>These skills are often used alongside <a href="/skill-hub/architecture/system-context-mapping-working-skill/">System Context Mapping</a>, <a href="/skill-hub/business-analysis/process-analysis-working-skill/">Process Analysis</a>, and <a href="/skill-hub/integration-architecture/api-integration-working-skill/">API Integration</a>.</p>
</section>

<section class="section">
  <header class="section-heading">
    <h2>How this group connects to other skills</h2>
  </header>
  <ul>
    <li><a href="/skill-hub/architecture/">Architecture</a> — System Context Mapping defines the boundaries; Systems Analysis defines the behavior inside and across those boundaries.</li>
    <li><a href="/skill-hub/integration-architecture/">Integration Architecture</a> — API Integration and Interface Ownership turn interface requirements into technical design and operational accountability.</li>
    <li><a href="/skill-hub/business-analysis/">Business Analysis</a> — Process Analysis and Requirements Elicitation provide the business events and stakeholder needs that drive both lifecycle and interface analysis.</li>
    <li><a href="/skill-hub/sap-ams/">SAP AMS</a> — Change Impact Analysis and Incident Triage use lifecycle and interface maps to diagnose failures and plan corrections.</li>
  </ul>
</section>

<section class="section">
  <header class="section-heading">
    <h2>Status and limitations</h2>
  </header>
  <p>This skill group is a public working interpretation of systems analysis practice. It is not official BABOK, UML, or SAP documentation. It focuses on the subset of systems analysis work that produces immediate, reviewable artifacts for enterprise and SAP support contexts. It does not cover detailed formal modeling, simulation, or comprehensive enterprise architecture. Use these skills as structured starting points for lifecycle and interface analysis, not as authoritative framework substitutes.</p>
</section>
