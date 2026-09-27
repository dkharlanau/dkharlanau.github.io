---
layout: default
title: "Impact Mapping — Practical Outcome-to-Delivery Method"
description: "Use Impact Mapping to connect a measurable goal to actors, behavior changes, and deliverables before building a feature backlog."
permalink: /skill-hub/methods-catalog/impact-mapping/
last_modified_at: 2026-09-27
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/methods-catalog/">Methods &amp; Frameworks</a></li>
    <li aria-current="page">Impact Mapping</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Methods Catalog — Outcomes</p>
  <h1>Impact Mapping</h1>
  <p class="lead">Use Impact Mapping when a project has many requested features but the connection to the business goal is weak or assumed.</p>

  <section>
    <h2>What this method is for</h2>
    <p>Impact Mapping connects four levels: <strong>Goal → Actors → Impacts → Deliverables</strong>. The goal states the measurable outcome. Actors are people or groups who can influence that outcome. Impacts describe behavior changes or effects needed from those actors. Deliverables are possible solution changes that may create those impacts.</p>
    <p>The order matters. Starting from deliverables turns the map into justification for a solution already chosen.</p>
  </section>

  <section>
    <h2>When to use it</h2>
    <ul>
      <li>The roadmap contains features but no measurable outcome.</li>
      <li>Stakeholders propose solutions before agreeing what behavior must change.</li>
      <li>A transformation initiative is too broad and needs a focused first milestone.</li>
      <li>A team needs to compare several possible ways to achieve the same business effect.</li>
      <li>A backlog needs a clear reason for what should not be built.</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Define one measurable goal.</strong> Example: reduce sales-order release lead time from 18 hours to 4 hours for standard orders.</li>
      <li><strong>Identify actors who can help or hinder the goal.</strong> Sales users, credit controllers, master-data stewards, customers, support teams, external partners.</li>
      <li><strong>Describe impacts as behavior or capability changes.</strong> “Sales enters complete tax data first time,” not “new validation screen.”</li>
      <li><strong>Generate alternative deliverables.</strong> Process change, training, validation, automation, data rule, policy, integration, analytics.</li>
      <li><strong>Challenge assumptions.</strong> What evidence says this deliverable will create the impact?</li>
      <li><strong>Select a small experiment or delivery slice.</strong> Prefer the cheapest way to learn whether the impact is real.</li>
      <li><strong>Measure the goal and impact.</strong> Stop or change deliverables that do not move the outcome.</li>
    </ol>
  </section>

  <section>
    <h2>SAP example — reduce blocked sales orders</h2>
    <div class="table-scroll">
      <table class="study-table">
        <thead><tr><th>Level</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>Goal</td><td>Reduce standard sales orders blocked for master-data errors by 60% in one quarter.</td></tr>
          <tr><td>Actor</td><td>Sales user</td></tr>
          <tr><td>Impact</td><td>Detects missing customer/material data before saving the order.</td></tr>
          <tr><td>Deliverables</td><td>Pre-check, clearer message, guided correction link, training for top recurring defects.</td></tr>
          <tr><td>Actor</td><td>Data steward</td></tr>
          <tr><td>Impact</td><td>Fixes high-frequency root causes upstream rather than correcting orders one by one.</td></tr>
          <tr><td>Deliverables</td><td>Defect dashboard, ownership rule, preventive validation in master-data workflow.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If the goal cannot be measured, improve the goal before discussing features.</li>
      <li>If an “impact” is a system feature, move it down to deliverables and ask what behavior it should change.</li>
      <li>If a deliverable has no impact branch, question why it exists.</li>
      <li>If several deliverables could create the same impact, compare cost, risk, time, and learning value.</li>
      <li>If the team needs delivery structure after choosing direction, continue with <a href="/skill-hub/methods-catalog/user-story-mapping/">User Story Mapping</a>.</li>
    </ul>
  </section>

  <section>
    <h2>Copy-ready template</h2>
    <pre><code>## Goal
Metric:
Baseline:
Target:
Time horizon:

## Actor 1
&lt;who can help or hinder&gt;

### Impact A
&lt;behavior/capability change&gt;
Evidence / assumption:
- ...

Possible deliverables:
- ...
- ...

### Impact B
...

## Actor 2
...

## First experiment / slice
&lt;smallest delivery that can test an impact&gt;

## Measurement
- Impact signal:
- Goal signal:
- Review date:
- Stop/change condition:</code></pre>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>The goal has metric, baseline, target, and horizon.</li>
      <li>Actors can actually influence the goal.</li>
      <li>Impacts describe behavior or effects, not features.</li>
      <li>Each deliverable connects to a specific impact.</li>
      <li>Alternative deliverables exist for important impacts.</li>
      <li>The map contains an explicit learning or measurement plan.</li>
    </ul>
  </section>

  <section>
    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Starting from a chosen solution.</strong> The map becomes decorative justification.</li>
      <li><strong>Using vague goals such as “improve user experience.”</strong> The team cannot know whether an impact worked.</li>
      <li><strong>Writing impacts as deliverables.</strong> “Build dashboard” is not a behavior change.</li>
      <li><strong>Assuming every actor must receive a feature.</strong> Some impacts may be created through policy, process, or data changes.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>An AI agent should test the hierarchy: goal is measurable, actors can influence it, impacts describe changed behavior, and deliverables are possible interventions. It should surface assumptions and generate alternatives rather than optimize a pre-selected feature list.</p>
  </section>

  <section>
    <h2>Related skills and methods</h2>
    <ul>
      <li><a href="/skill-hub/methods-catalog/user-story-mapping/">User Story Mapping</a></li>
      <li><a href="/skill-hub/methods-catalog/moscow-prioritization/">MoSCoW</a></li>
      <li><a href="/skill-hub/business-analysis/stakeholder-analysis-working-skill/">Stakeholder Analysis</a></li>
      <li><a href="/skill-hub/decision-validation/trade-off-analysis-working-skill/">Trade-off Analysis</a></li>
    </ul>
  </section>

  <section>
    <h2>Reference and limitations</h2>
    <p><a href="https://www.impactmapping.org/">Impact Mapping</a> uses the structure Goal, Actors, Impacts, and Deliverables to connect business outcomes to delivery options. This page focuses on practical use in enterprise transformation and SAP change portfolios.</p>
  </section>
</article>