---
layout: default
title: "Context Graphs for Enterprise Agents: Live, Synced, and Traceable Context"
description: "A practical context-graph architecture: route between live MCP/API reads and synced data, preserve authorization and provenance, and evaluate retrieval with an SAP example."
permalink: /atlas/ai-operations/prompts-agents-graphs/context-graph-runtime/
atlas_section: ai-operations
domain: Enterprise AI architecture
subdomain: Context engineering and retrieval control
concept_type: architecture decision guide
status: needs_verification
verified: false
level: 1
last_modified_at: 2026-10-10
author: Dzmitryi Kharlanau
robots: noindex,follow
sitemap: false
tags:
  - context-graphs
  - context-engineering
  - mcp
  - enterprise-ai
  - retrieval
  - authorization
  - provenance
  - sap
related:
  - /atlas/ai-operations/prompts-agents-graphs/
  - /atlas/ai-operations/prompts-agents-graphs/three-graphs/
  - /atlas/ai-operations/prompts-agents-graphs/state-memory-provenance/
  - /atlas/ai-operations/prompts-agents-graphs/architecture-selection-guide/
  - /atlas/ai-operations/authorization-aware-ai-for-sap/
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/ai-operations/">AI Operations</a></li><li><a href="/atlas/ai-operations/prompts-agents-graphs/">Enterprise AI architecture</a></li><li aria-current="page">Context graphs</li></ol></nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Architecture decision · Enterprise agent context</p>
    <h1>Context graphs: the system that decides what an agent should know</h1>
    <p class="note-subtitle">Connecting an agent to ten systems does not give it ten systems' worth of understanding. The hard part is choosing the right evidence, under the right identity, before the answer becomes too slow, stale, expensive, or unsafe.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <div class="note-body">
    <h2>Start with the query that breaks a tool-only agent</h2>
    <p><strong>Question A:</strong> "What is the status of this one support ticket?" A narrow live API read can usually answer it. <strong>Question B:</strong> "Which customers had repeated unresolved complaints during the previous quarter, and which are still at risk today?" That needs historical coverage, aggregation, identity resolution, a business definition of "at risk," and a fresh check of current state.</p>
    <p>Calling every MCP tool on every request is not a strategy. It creates latency, rate-limit pressure, inconsistent snapshots, excess tokens, and opportunities to surface records the requester must not see. Building a vector index of everything is not a strategy either: similarity search is not a substitute for accurate counts, joins, time filters, or permissions.</p>
    <p>The useful interpretation of a <strong>context graph</strong> here is a <strong>runtime context-selection and assembly layer</strong>. It decides what evidence an AI system may use for this request, where it can obtain it, and how that evidence remains traceable. It may use graph-shaped relationships, but it does <em>not</em> require a graph database. This operating definition follows Gil Feig's presentation and accompanying explanation; the decision rules below are an independent architecture synthesis.</p>

    <h2>Do not confuse four different jobs</h2>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Four different enterprise AI graph and context responsibilities">
      <table class="study-table__table"><thead><tr><th>Representation or layer</th><th>Owns this question</th><th>Example</th></tr></thead><tbody>
        <tr><td>Execution graph</td><td>Which step or approval is next?</td><td>Inspect → diagnose → review → verify</td></tr>
        <tr><td>Domain / knowledge graph</td><td>Which entities and systems relate?</td><td>Business Partner → customer role → sales area</td></tr>
        <tr><td>Event / provenance graph</td><td>Which event or decision produced this state?</td><td>Source change → message → target update</td></tr>
        <tr><td>Context-selection layer</td><td>Which authorized, sufficiently fresh evidence belongs in <em>this</em> model call?</td><td>Choose snapshot + one live read + cited summary</td></tr>
      </tbody></table>
    </div>
    <p>The first three are representations of control, business meaning, and change. The fourth is an <em>operating layer over available representations</em>, not automatically a new fourth type of persisted graph. See <a href="/atlas/ai-operations/prompts-agents-graphs/three-graphs/">Three graphs people keep mixing together</a>.</p>

    <h2>Reference architecture: routing before retrieval</h2>
    <pre><code>Request + principal + task + latency/cost/freshness budget
                         |
             Intent + scope + policy gate
                         |
           Skills / definitions + scoped memory
                         |
                  Context router
               /         |          \
      Live API / MCP   Synced store   Derived index
      current objects  history, SQL   search, summaries
               \         |          /
              Access checks + source trust
                         |
         Resolve identity, timestamps, conflicts
                         |
          Rank, trim, summarize, cite, stop
                         |
           Request-scoped context bundle
                         |
                    Model / agent
                         |
             Evidence trace + evaluation
                         |
             Action gate if writes exist</code></pre>
    <p><strong>The router is the main design decision.</strong> It need not be another autonomous agent. Deterministic rules, a small classifier, or a bounded workflow may be easier to test. Skills encode approved definitions and procedures (for example, what counts as an "unresolved complaint"); memory holds selected reusable knowledge, not indiscriminate chat transcripts. Neither overrides source authorization or live system truth.</p>

    <h2>Choose the evidence path by question, not by fashion</h2>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Context retrieval selection rules">
      <table class="study-table__table"><thead><tr><th>Question / condition</th><th>First choice</th><th>Escalate when</th></tr></thead><tbody>
        <tr><td>One record; current status matters</td><td>Authorized live API/MCP read</td><td>The source fails or the result is ambiguous; report uncertainty rather than guessing</td></tr>
        <tr><td>Many records; totals, filtering, joins, periods</td><td>Permission-scoped synchronized relational/search data</td><td>Snapshot is too old for the business question; selectively refresh matched records</td></tr>
        <tr><td>Find related narratives or similar incidents</td><td>Full-text and/or semantic index of authorized data</td><td>Exact IDs, dates, totals, or original wording must be checked in primary records</td></tr>
        <tr><td>Explain a policy or approved procedure</td><td>Versioned knowledge or approved skill</td><td>Policy version, country, effective date, or exception is unknown</td></tr>
        <tr><td>Repeat question with stable, scoped inputs</td><td>Scoped cache with TTL and invalidation</td><td>Identity, rights, source version, or material facts have changed</td></tr>
        <tr><td>High-risk decision or state-changing recommendation</td><td>Fresh authoritative read and deterministic checks</td><td>Evidence conflicts, authorization is unclear, or a human approval gate is required</td></tr>
      </tbody></table>
    </div>
    <p><strong>Default route:</strong> check identity and authorization → start with the cheapest adequate scoped evidence → make one high-yield live call if current state or confidence demands it → stop when evidence suffices. Do not ask the model to evaluate records it was never authorized to receive.</p>

    <h2>Live, synced, and derived data have different failure modes</h2>
    <h3>Live: accurate now, but not a warehouse</h3>
    <p>MCP can expose useful tools and resources, and APIs can return the current state of a specific object. Neither guarantees a query across every historical record or a safe bulk aggregation. Check pagination, supported filters, rate limits, tenant boundaries, token scope, retries, and timeout behavior. MCP is a protocol for access, not a completeness or freshness guarantee.</p>
    <h3>Synced: coverage and repeatability, at the price of freshness</h3>
    <p>When cross-account history matters, ingest the <em>minimum necessary</em> source data under an explicit ownership, retention, and access model. Keep structured fields for accurate SQL-style aggregation; use full-text and embeddings for narrative discovery. Record source IDs, update times, sync cursor, deletions, and ACL changes. Define when a webhook or change stream invalidates a record; use a documented TTL when events are unavailable.</p>
    <h3>Derived: useful compression, never unquestioned truth</h3>
    <p>Summaries, embeddings, entity links, and previously produced findings are derived evidence. Each needs source lineage, transformation version, freshness, and inherited access restrictions. A summary of a revoked document must not remain readable simply because its text lives in a different database. If the question depends on a nuance removed during compression, return to the source.</p>

    <h2>Make the authorization and provenance contract executable</h2>
    <p>Attach metadata to <em>every retrieved item</em>, including cached and derived items. This illustrative record shows the minimum shape; store principal references and audit correlation IDs securely, not access tokens in retrieval output.</p>
    <pre><code>{
  "source": "support-system",
  "object_id": "SYNTHETIC-CASE-42",
  "record_version": "v3",
  "source_updated_at": "2026-10-09T15:20:00Z",
  "fetched_at": "2026-10-10T08:10:00Z",
  "scope": "requester-authorized-at-query-time",
  "policy_version": "access-rules-v2",
  "derived_from": ["SYNTHETIC-CASE-42"],
  "transformation": "summary-v1",
  "invalidates_on": ["source_change", "acl_change", "ttl"],
  "status": "derived_not_authoritative"
}</code></pre>
    <p>A production contract additionally needs tenant isolation, original object references, classification, collection permissions, retention/deletion policy, and a trace showing which source items actually reached the model. <strong>Filtering after generation is too late.</strong> Re-check access when serving cached results and invalidate derived descendants when original permissions change. For high-risk work, log the exact evidence versions used and do not silently substitute stale snapshots.</p>

    <h2>SAP example: who has a replication problem right now?</h2>
    <p><em>Synthetic example; not a client incident or a claim about standard SAP configuration.</em> Consider: "Show customer records with repeated MDG-to-S/4 replication errors this month, their latest target status, and the likely responsible integration layer."</p>
    <ol>
      <li><strong>Define the business question.</strong> "Repeated" means at least two distinct failed processing attempts within the chosen period; deduplicate retries carefully. Agree the relevant customer identity and source/target boundary.</li>
      <li><strong>Read historical candidates from a synchronized operational index.</strong> Query error events and their normalized cross-system record IDs. A vector database alone cannot reliably count failures or enforce all filters.</li>
      <li><strong>Apply requester-specific access before retrieval.</strong> Enforce permitted organizational scope, data classification, and the source-specific visibility model; absent a safe mapping, omit the record and mark the gap.</li>
      <li><strong>Refresh only matching records.</strong> Read current processing/target state from authorized interfaces. Do not mistake yesterday's failed message for an incident that is still open today.</li>
      <li><strong>Attach the source trail.</strong> Link source event, outbound/inbound processing evidence, transformation, timestamp, and target observation. Treat owner hypotheses as hypotheses until checked against approved routing/mapping ownership.</li>
      <li><strong>Return a bounded recommendation.</strong> Show the list, the evidence behind each candidate, confidence/gaps, and next diagnostic check. Do not resend or change production records without separate authorization and controls.</li>
    </ol>
    <p>The <a href="/atlas/ai-operations/prompts-agents-graphs/sap-business-partner-change-case/">Business Partner change case</a> describes domain and event relationships. The context-selection layer determines which part of those relationships, histories, and current reads this particular authorized investigator needs.</p>

    <h2>Design review: seven questions before implementing</h2>
    <ol>
      <li><strong>Source of truth:</strong> Which system owns each field, and what happens when sources disagree?</li>
      <li><strong>Query shape:</strong> Is this a point lookup, a count across history, semantic retrieval, or a multi-hop dependency question?</li>
      <li><strong>Freshness:</strong> What staleness is acceptable per field and decision? What invalidates a cache or derived summary?</li>
      <li><strong>Authorization:</strong> Which principal and tenant may read the original, its index, its summary, and its linked records?</li>
      <li><strong>Budget:</strong> What are acceptable p95 latency, API quota, token cost, and maximum source fan-out?</li>
      <li><strong>Traceability:</strong> Can a reviewer reconstruct the exact source object versions, transformations, and access policy involved?</li>
      <li><strong>Failure behavior:</strong> When sources time out, conflict, or disappear, does the system abstain, degrade visibly, or call a human?</li>
    </ol>

    <h2>Build the smallest useful pilot</h2>
    <p>Start with <strong>one question family and two source systems</strong>, not a universal company graph. Maintain a fixed evaluation set with point lookups, cross-record aggregate questions, temporal changes, ambiguous identities, inaccessible records, and revoked permissions. Compare four baselines: live-only, synced-only, live-plus-synced, and live-plus-synced with selective derived summaries.</p>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Context graph pilot acceptance measurements">
      <table class="study-table__table"><thead><tr><th>Measure</th><th>What to test</th><th>Gate</th></tr></thead><tbody>
        <tr><td>Correctness and coverage</td><td>Exact counts, identity joins, citations, omissions, temporal answers</td><td>Compare with independently checked ground truth</td></tr>
        <tr><td>Authorization isolation</td><td>Another tenant, revoked object, cached summary, changed role</td><td>No cross-scope disclosure; fail closed when authorization cannot be verified</td></tr>
        <tr><td>Freshness</td><td>Source update, sync lag, invalidation propagation, derived staleness</td><td>Within explicit workflow-specific limits or clearly marked stale</td></tr>
        <tr><td>Efficiency</td><td>p50/p95 latency, API fan-out, quota, tokens, cost per valid answer</td><td>Improves on a measured baseline without harming correctness</td></tr>
        <tr><td>Trace quality</td><td>Can an engineer reproduce inputs to an incorrect answer?</td><td>Every consequential claim links back to authorized source evidence</td></tr>
      </tbody></table>
    </div>
    <p>Prefer incremental complexity. First make live lookups trustworthy. Add synchronization only where history, scale, or repeated queries demand it. Add semantic indexes only for semantic questions. Add graph traversal when relationship queries justify it. Keep the option to replace any vendor component without changing the data and access contracts.</p>

    <h2>What to explain in an architecture review</h2>
    <p><strong>Business explanation:</strong> "We are not collecting all company data for an AI. We are building a governed way to select only the information needed for each decision."</p>
    <p><strong>Technical explanation:</strong> "The request-scoped router enforces identity, freshness, and cost policies; chooses live or synchronized sources; preserves record-level lineage and permissions; and emits a small, auditable context bundle. Exact aggregation remains in structured queries, while semantic retrieval serves narrative discovery."</p>
    <p><strong>Changed-condition exercise:</strong> A support manager loses access to a customer account after a summary was cached. Would the system still return that summary? A working design checks authorization at read time and invalidates or excludes derived descendants, rather than trusting the ACL captured when the cache was built.</p>

    <h2>Sources and interpretation boundary</h2>
    <ul>
      <li><a href="https://www.youtube.com/watch?v=cSz7aL2nl2U" target="_blank" rel="noopener noreferrer">Gil Feig (Merge) — Why Your Company Needs a Context Graph (and How to Build It)</a>, AI Engineer World's Fair 2026 presentation, video published 9 October 2026. The presentation frames a context graph as a combination of live/synced context, routing, skills, memory, and provenance.</li>
      <li><a href="https://www.merge.dev/blog/context-graph-misconceptions" target="_blank" rel="noopener noreferrer">Gil Feig — What everyone is getting wrong about context graphs</a>, author-written explanation of source selection, live/cached/derived tiers, security, and traceability.</li>
      <li><a href="https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/basic/index.mdx" target="_blank" rel="noopener noreferrer">Model Context Protocol specification (2026-07-28)</a>, protocol reference. MCP supplies access primitives; it does not by itself supply business semantics, historical completeness, or application authorization policy.</li>
    </ul>
    <p><strong>Evidence boundary:</strong> the architecture, decision matrix, acceptance gates, and SAP scenario here are independently constructed guidance, not a quoted implementation from Merge, a benchmark claim, or official SAP documentation. Validate semantics, visibility, and available APIs against the actual landscape.</p>

    <h2>Continue</h2>
    <p>Use the <a href="/atlas/ai-operations/prompts-agents-graphs/architecture-selection-guide/">architecture selection guide</a> to decide whether this additional layer is warranted, then review <a href="/atlas/ai-operations/authorization-aware-ai-for-sap/">authorization-aware AI</a> and <a href="/atlas/ai-operations/prompts-agents-graphs/state-memory-provenance/">state, memory, and provenance</a>.</p>
  </div>

  <section class="atlas-related"><h2>Related pages</h2><ul><li><a href="/atlas/ai-operations/prompts-agents-graphs/">Enterprise AI architecture cluster</a></li><li><a href="/atlas/ai-operations/prompts-agents-graphs/three-graphs/">Three graph types</a></li><li><a href="/atlas/ai-operations/prompts-agents-graphs/sap-business-partner-change-case/">SAP Business Partner graph case</a></li></ul></section>
  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
