---
layout: default
title: "Atlas Signal Matching RAG Evaluation"
description: "Evaluation of whether Atlas signal matching needs RAG/vector search."
permalink: /docs/atlas/atlas-signal-rag-evaluation/
robots: noindex,follow
sitemap: false
---

# Atlas Signal Matching RAG Evaluation

Issue context: #70 asks whether Atlas signal matching needs RAG/vector search.
Issue #51 is relevant only as background for a possible static retrieval pack.
It does not justify adding RAG to the signal-update workflow now.

## Current V1 Stack

- Compact index: `ai/atlas-compact-index.json`
- Matcher: `scripts/match_atlas_signal.py`
- Proposal generator: `scripts/propose_atlas_update.py`
- Quality gate: `scripts/validate_atlas_proposal.py`
- Review workflow: `docs/atlas/ATLAS_SIGNAL_PR_WORKFLOW.md`

The matcher reads public frontmatter/headings/terms only. It does not load full
site content, private notes, generated site output, or embeddings.

## Evaluation Cases

| Case | Result | RAG needed? | Reason |
|---|---|---:|---|
| SAP support agent signal | Existing page update | No | Tags, title, process, and headings match `atlas/ai-operations/ai-agent-for-sap-support.md`. |
| SAP Green Ledger carbon allocation signal | New page candidate | No | No existing page covers the topic. RAG cannot find a page that does not exist; this is a corpus/metadata gap. |
| Title-only AI support signal | Rejected | No | Source evidence is weak. Retrieval would not fix missing source-body evidence. |
| Low-confidence adjacent match | Needs research | Not yet | First response should be better tags/frontmatter or a human decision, not vector infrastructure. |

## Failure Analysis

Observed or expected v1 failures are mostly:

- missing topic in Atlas corpus
- weak page tags or frontmatter
- broad source language that needs better classification
- source evidence too weak for public content
- ambiguous page ownership between related Atlas pages

These are not strong RAG signals. They are content modeling and metadata issues.

## Evaluation Questions

What query types fail with simple matching?
: Missing-topic signals and ambiguous cross-domain signals. Current examples do
  not show a correct existing page missed because of semantic wording alone.

Are failures due to missing metadata, weak tags, or actual semantic search need?
: Current failures are better explained by missing corpus coverage, weak tags,
  or insufficient evidence.

Can better frontmatter/tags solve the issue cheaper?
: Yes. Improve `tags`, `sap_area`, `business_process`, `related`, and headings
  before adding vector infrastructure.

What corpus would RAG search over if needed later?
: Public Atlas Markdown pages only.

Where would embeddings/index files live?
: Under `ai/rag/`, with freshness checks against `atlas/manifest.json`.

How would privacy and public/private separation be enforced?
: Index public Atlas pages only, reject private-path patterns, and fail
  validation if generated artifacts include local files, exports, logs, or
  secrets.

What validation proves the RAG index is fresh and safe?
: A future validator would compare source page content hashes to the Atlas
  manifest and fail on stale or private-path-contaminated artifacts.

## Recommendation

Recommendation: **no RAG/vector search yet**.

Improve metadata first:

1. Add better `tags`, `sap_area`, `business_process`, and `related` fields to
   pages that receive low-confidence matches.
2. Keep `ai/atlas-compact-index.json` fresh through
   `scripts/generate_atlas_artifacts.py --check`.
3. Track matcher misses in proposal review notes.
4. Re-evaluate only after repeated misses show that correct pages exist but are
   missed despite good metadata.

## RAG V2 Trigger Conditions

Consider minimal RAG only if at least one of these becomes true:

- a correct existing page is repeatedly missed even though frontmatter and tags
  are accurate
- matcher reasons show low lexical overlap while humans consistently identify a
  semantically related page
- the same signal needs comparison across many reviewed Atlas pages
- proposal reviewers need paragraph-level citation candidates, not just page
  candidates

## Minimal V2 Constraints If Needed Later

If RAG is later justified, keep it narrow:

- corpus: public Atlas Markdown pages only
- exclude generated site output, private notes, raw logs, local reports, secrets,
  exports, and scratch files
- store generated retrieval artifacts under `ai/rag/`
- include source URL/path, title, section, last reviewed date, and content hash
- validate freshness against the current Atlas manifest
- fail if private-path patterns appear
- do not use RAG output to publish directly; it can only support proposals

## Relationship To #51

#51 proposes a static Atlas Retrieval Pack as a possible RAG foundation. That is
useful context for future v2 design, but #70 does not require implementing it.
For v1 signal matching, the compact index is cheaper, auditable, deterministic,
and sufficient.

## Decision

Status: `no_rag_yet`

Next action: improve metadata and track matcher misses before adding vector or
embedding dependencies.
