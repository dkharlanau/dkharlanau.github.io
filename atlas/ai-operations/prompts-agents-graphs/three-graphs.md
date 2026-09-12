---
layout: default
title: "Three Graphs People Keep Mixing Together"
description: "A detailed distinction between execution graphs, domain knowledge graphs, and event/provenance graphs in agentic enterprise systems."
permalink: /atlas/ai-operations/prompts-agents-graphs/three-graphs/
atlas_section: ai-operations
domain: Enterprise AI architecture
subdomain: Graph-based system design
concept_type: concept deep dive
status: needs_verification
verified: false
level: 1
last_modified_at: 2026-09-12
author: Dzmitryi Kharlanau
robots: noindex,follow
sitemap: false
tags:
  - workflow-graphs
  - knowledge-graphs
  - event-graphs
  - provenance
  - agents
related:
  - /atlas/ai-operations/prompts-agents-graphs/
  - /atlas/ai-operations/prompts-agents-graphs/state-memory-provenance/
  - /atlas/ai-operations/prompts-agents-graphs/sap-business-partner-change-case/
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/ai-operations/">AI Operations</a></li><li><a href="/atlas/ai-operations/prompts-agents-graphs/">Prompts → Agents → Graphs</a></li><li aria-current="page">Three graph types</li></ol></nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Architecture layer 3 · Graphs</p>
    <h1>Three graphs people keep mixing together</h1>
    <p class="note-subtitle">“We need a graph” is not yet an architecture decision. First ask whether the graph describes how work executes, how the business world is structured, or how that world changed over time.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <div class="note-body">
    <h2>The word is overloaded</h2>
    <p>A graph is simply a set of things and relationships between them. That sounds almost trivial. The trouble starts when three very different graphs appear in one AI discussion and everybody assumes they solve the same problem.</p>
    <p>They do not.</p>
    <div class="decision-table"><table><thead><tr><th>Graph</th><th>Nodes represent</th><th>Edges represent</th><th>Main question</th></tr></thead><tbody>
      <tr><td>Execution / workflow graph</td><td>Steps, agents, tools, checkpoints</td><td>Possible transitions of control</td><td>What can happen next?</td></tr>
      <tr><td>Domain / knowledge graph</td><td>Business entities, concepts, systems, documents</td><td>Semantic relationships</td><td>What is related to what?</td></tr>
      <tr><td>Event / provenance graph</td><td>Changes, messages, decisions, versions, observations</td><td>Temporal or causal dependencies</td><td>How did we get here?</td></tr>
    </tbody></table></div>

    <h2>1. Execution graph: the graph of control</h2>
    <p>An execution graph describes the possible paths of a process. It is close to a state machine or workflow model.</p>
    <pre><code>START
  ↓
Classify request
  ├── simple ──→ deterministic lookup ──→ answer
  └── complex ─→ collect evidence
                    ↓
                 diagnose
                 ├── weak evidence ─→ ask / search more ─┐
                 │                                      │
                 └── sufficient ─→ propose action        │
                                      ↓                   │
                                  risk gate               │
                                  ├── low ─→ execute      │
                                  └── high → approval     │
                                      ↓                   │
                                    verify ←──────────────┘</code></pre>
    <p>The graph answers questions about orchestration: which branch is allowed, when to retry, when to call a specialist, where to checkpoint state, when to stop, and when to escalate to a human.</p>
    <p>Agent frameworks often expose this graph explicitly because long-running workflows need recoverability and observability. But the graph can also exist implicitly in ordinary code. Drawing boxes and arrows does not create intelligence; it makes control structure visible.</p>

    <h3>When an execution graph earns its keep</h3>
    <ul>
      <li>Different inputs legitimately require different paths.</li>
      <li>A run may pause and resume.</li>
      <li>Retries and failure recovery matter.</li>
      <li>Human approval is part of the path.</li>
      <li>You need to inspect how the system reached a decision.</li>
      <li>Several tools or agents can hand control to one another.</li>
    </ul>
    <p>If the process is always A → B → C, ordinary sequential code may be clearer. A graph visualization of three fixed boxes is not an architecture upgrade.</p>

    <h2>2. Domain graph: the graph of meaning</h2>
    <p>A domain graph describes the world the system reasons about. For SAP master data it might contain Business Partners, addresses, roles, sales areas, credit segments, source systems, replication models, interfaces, and ownership rules.</p>
    <pre><code>Business Partner
  ├── HAS_ADDRESS ──→ Address
  ├── HAS_ROLE ─────→ Customer Role
  ├── HAS_SALES_AREA → Sales Area
  ├── GOVERNED_BY ──→ MDG Change Request
  └── REPLICATED_TO → S/4 Business Partner

Replication Model
  ├── SELECTS ──────→ Business Partner
  ├── SENDS_VIA ───→ Service / IDoc / middleware
  └── TARGETS ──────→ Target System</code></pre>
    <p>This graph answers semantic questions that become awkward in flat documents: Which processes depend on this entity? Which interface can write this field? Which owner governs it? Which target systems receive it? Which evidence relates to this Business Partner rather than another one with a similar name?</p>
    <p>Microsoft GraphRAG is one public example of using LLMs to extract entities, relationships, and claims from unstructured text before retrieval. That can improve some forms of corpus exploration. But an enterprise domain graph should not be reduced to “GraphRAG.” The more important question is whether the graph expresses trusted domain relationships, regardless of how those relationships were produced or stored.</p>

    <h3>Knowledge graph versus vector retrieval</h3>
    <p>Vector retrieval asks roughly: <em>Which pieces of text are semantically similar to this query?</em> A graph query asks: <em>Which entities are connected by these relationship types under these constraints?</em></p>
    <p>Both are useful. If the question is “find documentation similar to this error,” semantic retrieval may be enough. If the question is “show every downstream system that can receive this master-data attribute through a path owned by this integration domain,” explicit relationships are much more natural.</p>
    <p>The mature architecture can combine them: retrieve relevant unstructured evidence, resolve the entities it refers to, and use the graph to navigate structured relationships.</p>

    <h2>3. Event and provenance graph: the graph of change</h2>
    <p>Enterprise failures are often temporal. The current value is only the final frame of a movie. To explain the failure, you need the sequence of changes and their dependencies.</p>
    <pre><code>BP email changed in MDG @ 10:04
        ↓ approved_by
CR approved @ 10:11
        ↓ produced
Outbound message M42 @ 10:12
        ↓ processed_by
S/4 inbound @ 10:13
        ↓ changed
S/4 email = new value
        ↓ later_overwritten_by
Inbound message M57 @ 10:19
        ↓ produced
S/4 email = old value
        ↓ detected_by
Reconciliation mismatch @ 10:25</code></pre>
    <p>Now “Why is S/4 wrong?” is not answered by comparing two snapshots. The system can identify a path through time: the correct change arrived, then a later event overwrote it. The corrective action changes too. Resending the original update may temporarily repair the value while leaving the competing writer untouched.</p>

    <h3>Provenance is more than logging</h3>
    <p>A log says something happened. Provenance connects what happened to the artifact, decision, source, actor, rule, or previous event that produced it. That difference matters when an agent must defend a recommendation.</p>
    <p>A useful provenance record may answer:</p>
    <ul>
      <li>Which source supplied this value?</li>
      <li>Which transformation changed it?</li>
      <li>Which user, service, or model initiated the action?</li>
      <li>Which evidence supported the decision?</li>
      <li>Which version of a rule or prompt was active?</li>
      <li>What downstream records were affected?</li>
      <li>What verification was performed afterwards?</li>
    </ul>

    <h2>The same system may need all three graphs</h2>
    <p>Consider an agent investigating a replication discrepancy.</p>
    <ol>
      <li>The <strong>execution graph</strong> tells the agent which diagnostic step it may choose next and where approval is required.</li>
      <li>The <strong>domain graph</strong> tells it how the Business Partner, field, systems, interfaces, and owners are related.</li>
      <li>The <strong>event graph</strong> tells it which changes and messages actually produced the current mismatch.</li>
    </ol>
    <p>The agent is not “the graph.” The graph is not “the agent.” The useful system is the composition.</p>

    <h2>A fourth graph sometimes appears: the dependency graph</h2>
    <p>Software packages, jobs, interfaces, transformations, and data products often form dependency graphs. These are closely related to domain and event graphs but deserve separate treatment when blast-radius analysis is the main job. For example: <em>If we change this mapping, which downstream interfaces, reports, reconciliations, and controls can be affected?</em></p>
    <p>Do not invent another graph store merely because the relationship has a different name. One underlying model can often expose several views.</p>

    <h2>Graph database is an implementation choice, not the concept</h2>
    <p>You can model graph-shaped information in relational tables, JSON documents, event stores, RDF, property-graph databases, or generated in-memory structures. A dedicated graph database becomes attractive when relationship traversal is central, deep, dynamic, or difficult to express efficiently elsewhere.</p>
    <p>Starting with “we should use Neo4j” reverses the decision. Start with the questions and relationships. Choose storage afterwards.</p>

    <h2>The test</h2>
    <p>Before adding “graph” to an architecture diagram, finish this sentence:</p>
    <blockquote>We need a graph because the system must repeatedly answer ______ by traversing ______ relationships that are difficult to represent or reason about as isolated records or documents.</blockquote>
    <p>If the blanks are vague, the graph may be decorative.</p>

    <h2>Reference</h2>
    <p><a href="https://github.com/microsoft/graphrag/blob/main/docs/index/overview.md" target="_blank" rel="noopener noreferrer">Microsoft GraphRAG indexing overview</a> is a useful concrete example of extracting entities, relationships, and claims for structured retrieval. It is cited here as an implementation example, not as a requirement for the architecture described above.</p>

    <h2>Next</h2>
    <p>Continue with <a href="/atlas/ai-operations/prompts-agents-graphs/state-memory-provenance/">State, memory, and provenance</a>.</p>
  </div>

  <section class="atlas-related"><h2>Related pages</h2><ul><li><a href="/atlas/ai-operations/prompts-agents-graphs/agents-and-control-loops/">Agents and control loops</a></li><li><a href="/atlas/ai-operations/prompts-agents-graphs/sap-business-partner-change-case/">Business Partner change case</a></li><li><a href="/atlas/automation/operational-memory-for-sap-ams/">Operational Memory for SAP AMS</a></li></ul></section>
  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>