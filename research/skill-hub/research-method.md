---
title: Research Method
robots: noindex
sitemap: false
---

# Research Method

## Overview

This document defines how research is conducted, documented, and synthesized for the Skill Hub research base.

## Research Process

### 1. Source Discovery

For each domain, search for public material using these strategies:

- **Official docs first**: Start with official documentation from framework bodies and vendors
- **Architecture centers**: Search major cloud provider architecture centers
- **Open source**: Search well-maintained open-source project documentation
- **Community**: Search recognized professional communities and reputable blogs
- **Postmortems**: Search public incident postmortems and ADR repositories
- **Standards**: Search NIST, ISO, and other standards body public guidance

### 2. Source Evaluation

For each candidate source:

1. Check authorship and publisher credibility
2. Verify date and maintenance status
3. Assess technical depth (not just high-level summaries)
4. Check for operational applicability (can a professional use this tomorrow?)
5. Assign tier based on `source-quality-rules.md`
6. Record in `source-registry.yml` with full metadata

### 3. Domain Analysis

For each domain note in `domains/*.md`:

1. **Research question**: What professional skills, artifacts, rules, and quality gates should Skill Hub extract?
2. **Best sources**: Table of top sources with tier and relevance
3. **Key practical patterns**: Reusable work patterns, not abstract theory
4. **Artifacts found**: Examples of real professional artifacts
5. **Decision rules**: "If X, then Y" style rules
6. **Quality gates**: How to judge whether work is good enough
7. **Common failure modes**: What professionals and agents usually get wrong
8. **Candidate skills**: Possible Skill Hub skills supported by this research
9. **Source-backed notes**: Short notes with links, no long copies
10. **Gaps / further research needed**: Honest assessment of what's missing

### 4. Cross-Domain Synthesis

After domain analysis, create synthesis files:

1. **Skill candidate map**: Cross-reference all candidate skills with evidence strength
2. **Artifact template map**: Map artifacts to skills and identify template gaps
3. **Decision rule map**: Collect strong rules across domains
4. **Quality gate map**: Define quality gates with source support
5. **Weak vs. strong output patterns**: Practical examples for agent skill design
6. **Recommended next skill batches**: Prioritized recommendations for future work

### 5. Validation

Before committing:

1. Run all validation scripts
2. Check for broken links
3. Verify no private material
4. Verify no copyrighted text copied
5. Verify source metadata completeness
6. Review synthesis for consistency

## Documentation Standards

### Domain Notes

- Use the standard structure defined above
- Keep notes concise and actionable
- Every claim should have a source ID or be labeled as synthetic/grounded
- Use tables for structured comparisons
- Use bullet lists for patterns and rules

### Source Registry

- Use the YAML schema defined in `source-registry.yml`
- Assign sequential IDs (src-001, src-002, etc.)
- Record access date for all web sources
- Note reliability concerns honestly
- Note copyright and citation permissions

### Synthesis Files

- Use tables for mapping and comparison
- Include evidence strength ratings
- Note gaps and limitations explicitly
- Link back to source IDs and domain notes
- Make recommendations actionable and specific

## Research Depth Targets

| Domain Group | Target Strong Sources |
|---|---|
| Data Governance / Quality / Metadata / MDM | 8–12 |
| Business Analysis / Requirements / Acceptance Criteria | 8–12 |
| Architecture / ADR / NFR / Capability / Context Mapping | 8–12 |
| Integration / API / Events / Observability | 8–12 |
| Operations / ITSM / RCA / Incident / Change Impact | 8–12 |
| Professional Operating Skills | 6–10 |
| AI Agent Skills | 6–10 |

## Update Cycle

- Research base should be updated when new high-quality sources are discovered
- Domain notes should be updated when new patterns or artifacts are identified
- Synthesis should be updated after significant domain note changes
- `RESEARCH_REPORT.md` should be updated after each research cycle
