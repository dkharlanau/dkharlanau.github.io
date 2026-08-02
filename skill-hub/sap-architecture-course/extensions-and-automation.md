---
layout: default
title: "Extend Without Losing the Core — SAP Architect Field Course"
description: "Decide where an SAP capability belongs and how to build extensions that remain operable and changeable."
permalink: /skill-hub/sap-architecture-course/extensions-and-automation/
last_modified_at: 2026-07-31
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
sap_architecture_course: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/sap-architecture-course/">SAP Architect Field Course</a></li><li aria-current="page">Extensions and automation</li></ol></nav>

<article class="course-bite">
  <header><p class="eyebrow">04 / Build</p><h1>Extend without losing the core.</h1><p class="lead">“Custom” is not a dirty word. Unowned custom behaviour that bypasses process truth and cannot survive change is the problem.</p></header>

  <section><h2>Every change needs a home</h2><p>When a business request arrives, do not begin with “Can we build it?” Begin with “Where should this behaviour live?” The answer has consequences for upgrades, data ownership, authorisation, support, integration, and the next team that needs to change it.</p><p>Sometimes the right answer is standard configuration. Sometimes it is a small in-app extension that belongs close to the business object. Sometimes it is a side-by-side capability because the logic is separate, changes independently, or serves more than one system. And sometimes the honest answer is that the process should be simplified before software gets involved.</p></section>

  <section><h2>Use distance from the core as a design signal</h2><p>Stay close to the core when the behaviour is truly part of the canonical SAP transaction and the platform supports the extension path. Move outward when the capability has its own lifecycle, needs independent release timing, combines several systems, or would create a large custom footprint inside a standard process.</p><p>Distance is not a moral score. A side-by-side service brings freedom, but it also brings identity, lifecycle, monitoring, deployment, and support responsibilities. A small enhancement inside a core process can be sensible, but it has to respect the upgrade path and business object rules.</p>
  <aside class="course-bite__checkpoint"><h3>Architecture question</h3><p>If SAP were unavailable for two hours, does this capability need to run, wait, or fail safely? The answer often tells you whether it is genuinely core process logic or a separate service.</p></aside></section>

  <section><h2>Automation is a process decision with code attached</h2><p>Automation work is often sold as removing manual steps. The architect’s job is to find out whether those steps contain judgment, policy, exception handling, or an ownership gap. Automating an ambiguous approval merely scales ambiguity.</p><p>Separate deterministic automation from assistance. Deterministic rules should have clear inputs, outcomes, controls, and an exception path. AI-assisted steps need an even tighter boundary: a review point, a permitted action set, and evidence showing what the assistant used to make its recommendation.</p><div class="course-bite__artifact"><h3>Extension placement note</h3><pre><code>Requested outcome: [business change]
Current process owner: [role]
Canonical object/state: [what must remain true]
Candidate homes: [standard | in-app | side-by-side | process change]
Why this placement: [lifecycle + ownership reasoning]
Integration needs: [events/APIs/data]
Security boundary: [identity + permissions]
Operational owner: [who supports it]
Exit or reversal path: [how it is retired or replaced]</code></pre></div></section>

  <section><h2>Common traps</h2><ul><li><strong>“It is only a small app.”</strong> Small apps still need identity, error handling, logs, ownership, and a retirement path.</li><li><strong>“The bot can decide it.”</strong> A model may assist. Do not silently move a business control to a probabilistic system.</li><li><strong>“We can query the table directly.”</strong> A shortcut can bypass semantics, authorisations, or lifecycle rules. Prove the supported boundary first.</li><li><strong>“We will document it later.”</strong> The missing document is usually the reason the next change becomes expensive.</li></ul></section>

  <section><h2>What good looks like</h2><p>A good extension can be explained in a few sentences: what it owns, which core object it respects, how it gets data, who can operate it, how it fails, and how it can be removed. If those answers require a long apology, the design is probably too coupled or too vague.</p><p class="course-bite__links"><a href="/skill-hub/sap-architecture-course/operations-security-resilience/">Continue: Operate the architecture you designed</a><br><a href="/atlas/concepts/sap-clean-core-strategy/">Atlas: SAP clean core strategy</a><br><a href="/skill-hub/architecture/architecture-decision-record-working-skill/">Deepen the skill: Architecture Decision Record</a></p><p class="course-source">Independent course material informed by public SAP Architecture Center application development, automation, AI, and extensibility references. Validate release, product, and governance choices in your own SAP landscape.</p></section>

  {% include atlas/author-block.html %}
</article>
