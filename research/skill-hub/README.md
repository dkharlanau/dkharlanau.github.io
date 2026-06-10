---
title: Skill Hub Research Base
robots: noindex
sitemap: false
---

# Skill Hub Research Base

A structured, public-safe research base for professional enterprise skills that power the Skill Hub and installable agent skills.

## Purpose

This directory collects, evaluates, and synthesizes high-quality public sources to support future Skill Hub pages and agent skill packages. It is a **research-first** workspace: no generic framework summaries, no invented best practices, no weak blog content as primary evidence.

## Structure

```
research/skill-hub/
  README.md                          # This file
  source-registry.yml                # All discovered sources with metadata
  source-quality-rules.md            # Rules for accepting or rejecting sources
  research-method.md                 # How research is conducted and documented
  RESEARCH_REPORT.md               # Final research summary and recommendations

  domains/                           # Domain-specific research notes
    business-analysis.md
    requirements-and-acceptance-criteria.md
    architecture-decisions.md
    non-functional-requirements.md
    integration-architecture.md
    api-design.md
    event-driven-architecture.md
    observability-and-sre.md
    incident-management.md
    root-cause-analysis.md
    change-impact-analysis.md
    professional-operating-skills.md
    ai-agent-skills.md
    # TODO: data-governance.md, data-quality.md, metadata-management.md,
    #       master-data-management.md, data-lineage.md (Track A domains pending)

  synthesis/                         # Cross-domain synthesis
    skill-candidate-map.md
    artifact-template-map.md
    decision-rule-map.md
    quality-gate-map.md
    weak-vs-strong-output-patterns.md
    recommended-next-skill-batches.md
```

## Source Quality Tiers

| Tier | Description | Examples |
|---|---|---|
| **1** | Primary / authoritative | Official framework bodies, standards orgs, vendor architecture guidance, official docs |
| **2** | Strong practitioner | Respected engineering blogs, public postmortems, ADR examples, reputable open-source docs |
| **3** | Supporting | Practitioner articles, conference talks, public case studies, educational material |

## Core Questions Every Source Should Help Answer

- What does a competent professional actually do?
- What artifacts should be produced?
- What questions should be asked?
- What decision rules are useful?
- What quality gates matter?
- What mistakes are common?
- How can an AI agent use this reliably?
- What should be cited or linked for further reading?

## Safety Rules

- No private material published
- No client names exposed
- No copyrighted framework text copied
- No fake citations
- No weak sources used as authoritative evidence
- Prefer paraphrase and link; do not copy long passages
- Label synthetic examples as synthetic but grounded in common enterprise patterns

## How to Use This Research

1. **Source discovery**: Add new sources to `source-registry.yml` with full metadata
2. **Domain analysis**: Extract patterns, artifacts, rules, and gates into `domains/*.md`
3. **Synthesis**: Cross-reference findings in `synthesis/*.md` to identify skill candidates
4. **Skill creation**: Use synthesis outputs to design new Skill Hub pages and agent skills
5. **Validation**: Run validation scripts before committing

## Research Status

**Current state**: 14 of 17 planned domain notes are committed. Track A (Data Governance: data-governance, data-quality, metadata-management, master-data-management, data-lineage) domain notes are pending.

**Source registry**: 20 sources fully registered (src-501–src-520, Track F). Sources for Tracks A–E and G are defined inline within domain notes but not yet consolidated into `source-registry.yml`. A follow-up PR is needed to complete the registry.

See `RESEARCH_REPORT.md` for the latest research summary and recommended next steps.
