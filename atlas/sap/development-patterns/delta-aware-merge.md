---
layout: default
title: "Delta-Aware Merge / Patch Semantics | SAP Development Patterns"
description: "A missing field, an explicitly cleared field and a deleted segment must not mean the same thing. Practical SAP ABAP, RAP, CAP architecture pattern."
permalink: /atlas/sap/development-patterns/delta-aware-merge/
author: "Dzmitryi Kharlanau"
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-17
hide_global_cta: true
tags:
  - sap
  - abap
  - software-architecture
  - design-patterns
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>
  <li><a href="/">Home</a></li><li><a href="/atlas/">Atlas</a></li><li><a href="/atlas/sap/">SAP</a></li>
  <li><a href="/atlas/sap/development-patterns/">Development Patterns</a></li><li aria-current="page">Delta-Aware Merge / Patch Semantics</li>
</ol></nav>
<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">SDP-05 · Integration · Architecture vocabulary</p>
    <h1>Delta-Aware Merge / Patch Semantics</h1>
    <p class="note-subtitle">A missing field, an explicitly cleared field and a deleted segment must not mean the same thing.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>
  <div class="note-body">
    <h2>The situation</h2>
    <p>An inbound delta updates one field but unexpectedly wipes unrelated customer data, or a hierarchy carrier segment is misread as a full replace.</p>
    <h2>The mental model</h2>
    <pre><code>Decode segment intention → translate keys → field-presence policy → merge or delete</code></pre>
    <p><strong>Use when:</strong> Master-data IDocs, event-driven updates, partial API updates, reduced messages and selective field protection.</p>
    <h2>How to apply it</h2>
    <ol>
<li>Interpret operation and MSGFN at the correct segment level before making a persistence decision.</li>
<li>Determine presence semantics from the actual message format: absent, not supplied, explicit blank, suppression marker and delete can differ.</li>
<li>Resolve external organizational keys through value mappings before locating the target record.</li>
<li>Apply only allowed changes; separately document replace and delete semantics per message type; do not treat 018 as 'delete' or blindly ignore descendants.</li>
</ol>
    <h2>A small SAP example</h2>
    <p>A synthetic customer delta sends changed general data and an unchanged parent carrying a changed child. The parent is not rewritten, but child processing continues. A protected existing field is left intact by an explicit merge rule.</p>
    <p><strong>Implementation sketch</strong> — conceptual only. This is not a compiled SAP sample, an API availability guarantee, or a production-ready implementation.</p>
    <pre><code>FOR EACH segment (illustrative):
  operation = classify_msgfn(segment)
  keys      = map_external_keys(segment)
  IF operation = CARRIER_ONLY: process_children(); CONTINUE
  IF operation = DELETE: apply_authorized_delete(keys); CONTINUE
  changes = select_explicit_allowed_fields(segment)
  merge_into_target(keys, changes)</code></pre>
    <h2>Say it in a design review</h2>
    <blockquote><p>We need Delta-Aware Merge: resolve MSGFN and field presence before lookup or write, then protect fields explicitly.</p></blockquote>
    <h2>Trade-offs and failure modes</h2>
    <p><strong>Watch for:</strong> Never infer that an empty string means 'not supplied' without the precise IDoc reduction and field semantics. Not every segment carries MSGFN. 005 and 009 also need message-specific handling.</p>
    <p><strong>Choose differently when:</strong> If a source sends complete, authoritative snapshots with proven replace semantics, use an explicit snapshot-replacement contract instead of a patch.</p>
    <h2>Acceptance question</h2>
    <p>Do tests cover 003, 004, 005, 009, 018, 023 where supported, blank vs missing, protected fields, parent/child segments and org mapping?</p>
    <h2>References and scope</h2>
    <p>These are independent architecture explanations. Vendor sources establish platform capabilities; the design recommendation is a synthesis that still requires release, security and transaction-boundary verification in your own landscape.</p>
    <ul><li><a href="https://help.sap.com/saphelp_em900/helpdata/en/4a/66efbfcbff260be10000000a42189b/content.htm">Processing Inbound Master Data — SAP Help</a></li></ul>
    <h2>Continue the design</h2>
    <ul><li><a href="/atlas/sap/development-patterns/anti-corruption-layer/">SDP-04 · Anti-Corruption Layer (ACL)</a></li>
<li><a href="/atlas/sap/development-patterns/idempotent-consumer/">SDP-14 · Idempotent Consumer</a></li><li><a href="/atlas/sap/development-patterns/design-review/">Design-review template</a></li></ul>
    <p><a href="/atlas/sap/development-patterns/">← Back to the Pattern Library</a></p>
  </div>
</article>
{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
