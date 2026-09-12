---
layout: default
title: "SAP Case: A Business Partner Change as an Event Graph"
description: "An illustrative SAP MDG-to-S/4 case showing how execution, domain, event, and provenance models change diagnosis and safe automation."
permalink: /atlas/ai-operations/prompts-agents-graphs/sap-business-partner-change-case/
atlas_section: ai-operations
domain: SAP Enterprise AI
subdomain: Business Partner and MDG diagnostics
concept_type: illustrative case study
status: needs_verification
verified: false
level: 1
last_modified_at: 2026-09-12
author: Dzmitryi Kharlanau
robots: noindex,follow
sitemap: false
tags:
  - sap-mdg
  - business-partner
  - event-graph
  - reconciliation
  - enterprise-ai
related:
  - /atlas/ai-operations/prompts-agents-graphs/
  - /atlas/ai-operations/prompts-agents-graphs/three-graphs/
  - /atlas/ai-operations/prompts-agents-graphs/closed-loop-enterprise-ai/
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/ai-operations/">AI Operations</a></li><li><a href="/atlas/ai-operations/prompts-agents-graphs/">Prompts → Agents → Graphs</a></li><li aria-current="page">SAP Business Partner case</li></ol></nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Illustrative case · SAP MDG and S/4</p>
    <h1>A Business Partner change as an event graph</h1>
    <p class="note-subtitle">A snapshot tells you that two systems disagree. A change graph can tell you how they came to disagree — which is usually the more valuable question.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <div class="note-body">
    <p><strong>Boundary:</strong> this is a deliberately generic, illustrative architecture case. IDs, times, systems, and events below are fictional and are not taken from a client landscape.</p>

    <h2>The incident</h2>
    <p>A customer email is changed through SAP MDG. The change is approved. Later, a user notices that MDG shows the new email while S/4 shows the old one.</p>
    <p>The naive diagnostic question is:</p>
    <blockquote>Why did replication fail?</blockquote>
    <p>That question already contains an assumption. Perhaps replication did not fail. Perhaps it succeeded and something else wrote the old value later.</p>

    <h2>What a snapshot comparison can tell us</h2>
    <pre><code>MDG       EMAIL = new@example.test
S/4       EMAIL = old@example.test

Result: mismatch</code></pre>
    <p>This is enough to detect a problem and not enough to explain it.</p>
    <p>A spreadsheet reconciliation can be very valuable here. It identifies the population requiring investigation. But a snapshot does not contain causality. To find the cause, we need changes, messages, ownership, and time.</p>

    <h2>Start with the domain graph</h2>
    <p>The domain model tells the diagnostic system what objects can plausibly participate in the incident.</p>
    <pre><code>Business Partner BP-100023
  ├── HAS_CONTACT_POINT ──→ Email
  ├── GOVERNED_IN ────────→ MDG
  ├── REPRESENTED_IN ─────→ S/4
  ├── CHANGED_BY ─────────→ Change Request
  └── REPLICATED_THROUGH ─→ Replication Path RP-01

Replication Path RP-01
  ├── READS_FROM ─────────→ MDG
  ├── DELIVERS_TO ────────→ S/4
  ├── USES ───────────────→ Message / Service
  └── SUBJECT_TO ─────────→ Filter / mapping / ownership rules</code></pre>
    <p>The model does not need to contain every SAP object ever invented. It needs the relationships necessary to answer the operational questions we care about.</p>

    <h2>Then reconstruct the event graph</h2>
    <p>Assume the system collects the following evidence:</p>
    <div class="decision-table"><table><thead><tr><th>Time</th><th>Event</th><th>Observed result</th></tr></thead><tbody>
      <tr><td>10:04</td><td>MDG change submitted</td><td>Email becomes <code>new@example.test</code> in governed change context.</td></tr>
      <tr><td>10:11</td><td>Change approved</td><td>Change request reaches approved state.</td></tr>
      <tr><td>10:12</td><td>Outbound message M42 created</td><td>Payload contains the new email.</td></tr>
      <tr><td>10:13</td><td>M42 processed in S/4</td><td>S/4 change evidence shows the new email.</td></tr>
      <tr><td>10:19</td><td>Another inbound event M57 processed</td><td>Payload contains the old email.</td></tr>
      <tr><td>10:20</td><td>S/4 value changed again</td><td>Email returns to the old value.</td></tr>
      <tr><td>10:25</td><td>Reconciliation runs</td><td>MDG and S/4 mismatch detected.</td></tr>
    </tbody></table></div>

    <p>The graph is now much more informative:</p>
    <pre><code>MDG change E1
   ↓ approved_as
Approval E2
   ↓ produced
Message M42
   ↓ processed_as
S/4 change E3: old → new
   ↓ followed_by
Message M57
   ↓ processed_as
S/4 change E4: new → old
   ↓ observed_by
Mismatch R1</code></pre>

    <h2>The diagnosis changes</h2>
    <p>“Replication failed” is now contradicted by evidence. The primary replication path delivered the intended value successfully. The discrepancy was produced later.</p>
    <p>This distinction matters because the obvious correction — resend M42 or update the field again — may repair the symptom but leave the failure mechanism active. If M57 is part of a recurring inbound path, the value can be overwritten again.</p>

    <h2>The next question is ownership</h2>
    <p>Now the domain graph becomes important again. The diagnostic system needs to know whether M57 was a legitimate writer.</p>
    <p>Possible explanations include:</p>
    <ul>
      <li>a second source system is intentionally authoritative for the field in some scope;</li>
      <li>a loop-prevention rule is incomplete;</li>
      <li>a delayed message contains stale master data;</li>
      <li>a mapping path incorrectly populates the contact field;</li>
      <li>a migration or mass-maintenance interface is still active;</li>
      <li>the same business concept is represented differently across systems and the apparent overwrite is semantically legitimate.</li>
    </ul>
    <p>The graph should not make the answer up. It should tell the agent where evidence is missing.</p>

    <h2>What the agent does differently</h2>
    <p>Without structured history, an LLM might generate a generic checklist: inspect DRF, middleware, inbound processing, filters, mappings, locks, and master-data ownership. That checklist can still be useful, but it is broad.</p>
    <p>With event and domain evidence, the agent can narrow the next step:</p>
    <ol>
      <li>Confirm M42 contained the expected value.</li>
      <li>Confirm the target processed M42 successfully.</li>
      <li>Identify later writers of the same field for the same BP.</li>
      <li>Resolve M57 to its source system, interface, and ownership rule.</li>
      <li>Determine whether M57 was stale, invalid, or legitimately authoritative.</li>
      <li>Only then propose correction and prevention.</li>
    </ol>
    <p>The value is not that the model “reasons harder.” The value is that the system gives reasoning a better map of reality.</p>

    <h2>Add the execution graph</h2>
    <p>The execution graph controls the investigation itself:</p>
    <pre><code>Mismatch detected
    ↓
Read source and target values
    ↓
Find latest source change
    ↓
Find outbound event
    ├── not found → investigate selection/filter path
    └── found
          ↓
      find target processing
          ├── failed → investigate processing error
          └── succeeded
                ↓
           inspect later writers
                ├── none → inspect read/cache/representation issue
                └── found
                      ↓
                 resolve ownership
                      ↓
                 propose remedy
                      ↓
                 approval if write-risk requires
                      ↓
                    act
                      ↓
                   verify</code></pre>
    <p>Notice that this execution graph is different from the event graph describing what happened to the BP. One graph controls the investigation; the other is evidence being investigated.</p>

    <h2>What a safe correction proposal should contain</h2>
    <p>A production-oriented agent should not end with “change the email.” A useful proposal is closer to a change package:</p>
    <ul>
      <li><strong>Observed discrepancy:</strong> source value, target value, timestamps.</li>
      <li><strong>Evidence chain:</strong> IDs for change, outbound message, inbound processing, later writer.</li>
      <li><strong>Root-cause confidence:</strong> what is proven and what remains inferred.</li>
      <li><strong>Correction:</strong> smallest action that restores intended state.</li>
      <li><strong>Prevention:</strong> change to ownership, mapping, filtering, sequencing, or monitoring if required.</li>
      <li><strong>Blast radius:</strong> whether other BPs or attributes may be affected.</li>
      <li><strong>Verification:</strong> exact post-action checks.</li>
      <li><strong>Rollback / escalation:</strong> what happens if verification fails.</li>
    </ul>

    <h2>Reconciliation becomes more powerful when it creates investigation edges</h2>
    <p>Traditional reconciliation often produces a list of differences. A stronger architecture uses each mismatch as the start of a trace. The mismatch is connected to entity history, message history, transformation rules, and ownership.</p>
    <p>That creates a progression:</p>
    <pre><code>detect difference
   → identify affected entity
   → reconstruct change path
   → identify competing cause
   → propose controlled remedy
   → verify convergence
   → retain reusable pattern</code></pre>
    <p>At that point reconciliation is no longer only a report. It becomes an entry point into operational intelligence.</p>

    <h2>The reusable pattern is larger than SAP BP</h2>
    <p>The same model applies to materials, prices, credit data, partner functions, mappings, configuration, interface payloads, and many non-SAP systems. The nouns change; the architecture remains recognizable:</p>
    <pre><code>Entity
 + authoritative sources
 + transformations
 + messages / events
 + target states
 + ownership
 + provenance
 + verification</code></pre>

    <h2>What this case demonstrates</h2>
    <p>The progression from prompt to agent to graph is not really about newer AI fashion. It is a progression in what the system can represent.</p>
    <ul>
      <li>A <strong>prompt</strong> can tell the model how to investigate.</li>
      <li>An <strong>agent</strong> can choose and execute diagnostic steps.</li>
      <li>An <strong>execution graph</strong> can control those steps and recovery paths.</li>
      <li>A <strong>domain graph</strong> can represent the entities and ownership relationships involved.</li>
      <li>An <strong>event/provenance graph</strong> can explain how the current state arose.</li>
      <li>A <strong>closed loop</strong> can correct the state and verify the outcome.</li>
    </ul>
    <p>That composition is much harder to reduce to a copied prompt because the value lives in the model of the enterprise and the evidence flowing through it.</p>

    <h2>Next</h2>
    <p>Finish with the <a href="/atlas/ai-operations/prompts-agents-graphs/architecture-selection-guide/">architecture selection guide</a>: when prompts, rules, workflows, agents, retrieval, or graphs are actually justified.</p>
  </div>

  <section class="atlas-related"><h2>Related pages</h2><ul><li><a href="/atlas/ai-operations/prompts-agents-graphs/three-graphs/">Three graph types</a></li><li><a href="/atlas/ai-operations/prompts-agents-graphs/closed-loop-enterprise-ai/">Verified closed-loop enterprise AI</a></li><li><a href="/atlas/ai-operations/ai-agent-for-sap-support/">AI Agent for SAP Support</a></li></ul></section>
  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>