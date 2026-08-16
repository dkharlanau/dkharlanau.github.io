---
layout: default
title: "Skill → Template Contract"
description: "A practical model for turning repeatable consulting work into executable skills and reusable evidence templates."
permalink: /skill-hub/skill-template-contract/
last_modified_at: 2026-08-16
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li aria-current="page">Skill → Template Contract</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub / Operating model</p>
  <h1>Skill tells you how to work. Template proves what you did.</h1>
  <p class="lead">Use Skills for repeatable reasoning and execution. Use Templates to record one concrete run of that Skill. Keep the two connected, but do not merge them into one giant checklist.</p>

  <section>
    <h2>The model</h2>
    <p><strong>Skill → Run → Template → Evidence → Result → Reuse</strong></p>
    <p>A Skill is a reusable method. It defines when to start, what inputs are needed, which checks to run, how to make decisions, when to stop, and what output is expected. A Template is the case record created while the Skill is executed.</p>
    <p>This split matters because the method should stay stable while case data changes every time. If the method and the case are mixed, the document quickly becomes a copied checklist with old values, missing evidence, and no clear version control.</p>
  </section>

  <section>
    <h2>Skill contract</h2>
    <p>Every operational Skill should define the same core fields:</p>
    <ul>
      <li><strong>Goal</strong> — the business or technical result.</li>
      <li><strong>Use when / do not use when</strong> — clear trigger and boundary.</li>
      <li><strong>Required inputs</strong> — what must be known before useful work starts.</li>
      <li><strong>Workflow</strong> — ordered steps, not a random list of tools.</li>
      <li><strong>Decision points</strong> — conditions that change the path.</li>
      <li><strong>Tools</strong> — transactions, apps, logs, browser tools, APIs, reports, or queries used by the method.</li>
      <li><strong>Evidence</strong> — what must be captured before changing the system.</li>
      <li><strong>Stop conditions</strong> — when to pause, escalate, or switch to another Skill.</li>
      <li><strong>Output</strong> — the artifact produced by a successful run.</li>
      <li><strong>Quality gates</strong> — checks that prevent weak conclusions.</li>
      <li><strong>Related Skills</strong> — the next or previous method in the chain.</li>
      <li><strong>Template</strong> — a copy-ready structure for one execution.</li>
    </ul>
  </section>

  <section>
    <h2>Template contract</h2>
    <p>A Skill-specific Template should record only information needed to execute, explain, validate, and reuse the result.</p>
    <ul>
      <li>Case ID, date, owner, system, process, and scope.</li>
      <li>Observed behavior and expected behavior.</li>
      <li>Evidence collected before changes.</li>
      <li>Checks performed and their results.</li>
      <li>Hypotheses kept or rejected.</li>
      <li>Decision points and why a path was selected.</li>
      <li>Action, risk, rollback, and owner.</li>
      <li>Validation evidence and business result.</li>
      <li>Reusable lesson or follow-up Skill.</li>
    </ul>
    <p>Generic templates such as RCA, Incident Triage, Change Impact, or Decision Record stay reusable across domains. A technical Skill can either use one of them or add a smaller domain-specific template.</p>
  </section>

  <section>
    <h2>Composition instead of duplication</h2>
    <p>A complex Skill should call smaller Skills or templates instead of copying their logic.</p>
    <p>Example:</p>
    <pre><code>Fiori App Troubleshooting
├─ Incident Triage           → classify impact
├─ Browser Evidence Capture  → console + network
├─ OData / Gateway Check     → request + error log
├─ Authorization Check       → SU53 / trace when relevant
├─ Root Cause Analysis       → only if the cause is not obvious
└─ Fiori Troubleshooting Record → case template
</code></pre>
    <p>This creates a graph of reusable methods. A new Skill can reuse existing reasoning instead of becoming another 80-line checklist with slightly different wording.</p>
  </section>

  <section>
    <h2>Skill maturity</h2>
    <ol>
      <li><strong>Draft</strong> — useful method, still missing cases or verification.</li>
      <li><strong>Tested</strong> — executed on synthetic or real sanitized cases and the path works.</li>
      <li><strong>Operational</strong> — clear inputs, outputs, decisions, evidence, and escalation rules.</li>
      <li><strong>Agent-ready</strong> — portable <code>SKILL.md</code>, references, template, examples, and deterministic quality gates.</li>
    </ol>
    <p>Do not call a page agent-ready only because it contains instructions. The method needs enough structure for an agent to know what not to do as well.</p>
  </section>

  <section>
    <h2>Authoring rule</h2>
    <p>When a repeated task appears for the second or third time, ask three questions:</p>
    <ol>
      <li>Is the reasoning reusable?</li>
      <li>Can the inputs and outputs be named clearly?</li>
      <li>Would another consultant or agent get a better result by following the same path?</li>
    </ol>
    <p>If yes, create a Skill. If the task only needs a consistent record, create a Template. If both are useful, connect them.</p>
  </section>

  <section>
    <h2>Good candidates for SAP technical Skills</h2>
    <ul>
      <li>Fiori app troubleshooting.</li>
      <li>OData / Gateway request tracing.</li>
      <li>IDoc failure analysis and safe reprocessing.</li>
      <li>Authorization failure analysis.</li>
      <li>Sales order determination analysis.</li>
      <li>Pricing issue analysis.</li>
      <li>ATP / confirmation issue analysis.</li>
      <li>Delivery and shipping issue analysis.</li>
      <li>Purchase order and goods receipt process deviation analysis.</li>
      <li>Output / form / message determination analysis.</li>
      <li>Background job and queue troubleshooting.</li>
      <li>Integration end-to-end trace.</li>
    </ul>
  </section>

  <section>
    <h2>Related material</h2>
    <ul>
      <li><a href="/labs/templates/">Operational Templates</a> — generic case protocols.</li>
      <li><a href="/skill-hub/sap-ams/fiori-app-troubleshooting-working-skill/">Fiori App Troubleshooting</a> — first technical Skill using this contract.</li>
      <li><a href="/skill-hub/sap-ams/root-cause-analysis-working-skill/">Root Cause Analysis</a> — reusable reasoning Skill.</li>
      <li><a href="/skill-hub/sap-ams/incident-triage-working-skill/">Incident Triage</a> — reusable entry Skill.</li>
    </ul>
  </section>
</article>
