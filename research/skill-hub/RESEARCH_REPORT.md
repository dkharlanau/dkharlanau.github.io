---
title: Skill Hub Research Report
robots: noindex
sitemap: false
---

# Skill Hub Research Base — Research Report

## Executive Summary

This research base documents the evidence, patterns, and decision rules collected across 7 parallel research tracks covering 18 domains relevant to agent skill design. It contains **84 curated sources** (41 Tier 1, 39 Tier 2, 4 Tier 3), **18 domain research notes**, and 6 synthesis artifacts that map candidate skills, artifacts, decision rules, quality gates, output patterns, and recommended next work batches.

**Goal**: Provide a source-backed foundation for creating and strengthening agent skills and public skill pages, ensuring every skill is grounded in authoritative practitioner guidance rather than generic advice.

---

## Research Tracks and Domains

| Track | Domains | Sources | Key Findings |
|---|---|---:|---|
| A — Data Governance | data-governance, data-quality, metadata-management, master-data-management, data-lineage | 12 | Governance must be federated for autonomous domains; quality gates belong at pipeline ingestion; lineage requires open standards |
| B — Business Analysis | business-analysis, requirements-and-acceptance-criteria | 10 | Discovery sprints must validate problems with users; acceptance criteria must be Given-When-Then with edge cases; DoD is a release gate |
| C — Architecture | architecture-decisions, non-functional-requirements | 12 | MADR is the standard for ADRs; quality attribute scenarios bridge architecture and implementation; Well-Architected Reviews are production gates |
| D — Integration | integration-architecture, api-design, event-driven-architecture | 12 | Design-first APIs with linting; idempotency keys for side-effectful operations; event-driven requires operational runbooks |
| E — Operations | observability-and-sre, incident-management, root-cause-analysis, change-impact-analysis | 20 | SLOs and error budgets are reliability foundations; incident command requires explicit roles and severity classification; postmortems must be blameless |
| F — Professional Skills | professional-operating-skills | 10 | Problem statements must exclude solutions; assumptions must be converted to risks when probability × impact is high; escalation briefs need structured format |
| G — AI Agent Skills | ai-agent-skills | 10 | Structured outputs and function calling are complementary; safety requires adversarial evaluation; reflection loops need termination criteria |

---

## Source Quality Summary

| Tier | Count | Description |
|---|---|---|
| Tier 1 — Official / Standard | 41 | Official documentation, standards bodies, peer-reviewed research, government playbooks |
| Tier 2 — Strong Practitioner / Open Source | 39 | Mature open-source projects, respected practitioner blogs, vendor best-practice guides |
| Tier 3 — Supporting / Community | 4 | Community discussions, niche practitioner posts, supplementary references |

**Safety rules enforced**: No private material, no client names, no copyrighted framework text copied, no fake citations, no weak sources as authoritative. All sources are paraphrased and linked.

---

## Synthesis Artifacts

| Artifact | Purpose | Key Output |
|---|---|---|
| `skill-candidate-map.md` | Maps 37 candidate skills to domains, evidence strength, and recommendations | 6 immediate create recommendations, 6 strengthen-existing recommendations |
| `artifact-template-map.md` | Identifies 38 artifacts needed by skills, their template status, and gaps | 22 gaps identified for template creation |
| `decision-rule-map.md` | Collects 33 "If X, then Y" rules with source backing | Rules span governance, quality, architecture, integration, operations, professional skills, and AI agent design |
| `quality-gate-map.md` | Defines 40 quality gates across all domains | Gates include coverage audits, compliance scans, review meetings, and automated checks |
| `weak-vs-strong-output-patterns.md` | Provides 6 practical examples of bad and good agent outputs | Patterns cover governance, acceptance criteria, ADRs, incident briefs, tool instructions, and risk triage |
| `recommended-next-skill-batches.md` | Prioritizes 6 batches of future work | Batch 1 = immediate (6 skills), Batch 2 = next sprint (7 skills), Batch 3 = future (8 skills), Batch 4 = strengthen existing (7 skills) |

---

## Key Decision Rules (Sample)

- **Governance**: If multiple autonomous domains exist, then federate governance rather than centralizing all decisions. (src-010, src-011)
- **Quality**: If data enters a pipeline, then validate at ingestion before downstream consumption. (src-008, src-009)
- **Requirements**: If a story has no acceptance criteria, then it is not ready for development. (src-104, src-108)
- **Architecture**: If a decision affects more than one team, then use MADR with full RACI front matter. (src-206, src-212)
- **Integration**: If a POST operation has side effects, require an idempotency key. (src-305)
- **Operations**: If mitigation and root cause investigation are competing for attention, then prioritize mitigation first. (src-401, src-403)
- **Professional**: If a problem statement includes a proposed solution, then rewrite it to describe the issue only. (src-501)
- **AI Agent**: If the model must decide between multiple external actions, use function calling; if it only needs to format data, use structured outputs. (src-602)

---

## Recommended Next Steps

1. **Batch 1 skills** (immediate): Create `expectation-suite-design-and-maintenance`, `pipeline-quality-gate-engineering`, `openapi-design-first`, `asyncapi-contract-design`, `blameless-postmortem-writing`, `escalation-brief-writing`
2. **Strengthen existing skills** (ongoing): Enhance `data-governance-ownership`, `architecture-decision-record`, `acceptance-criteria`, `incident-triage`, `root-cause-analysis`, `change-impact-analysis`, `non-functional-requirements`
3. **Template creation** (parallel): Fill 22 identified artifact template gaps
4. **Validation**: Run `validate_agent_skills.py` and `check_public_repo.py` before each skill release

---

## Files in This Research Base

```
research/skill-hub/
├── README.md
├── RESEARCH_REPORT.md
├── source-quality-rules.md
├── research-method.md
├── source-registry.yml (84 sources)
├── validate_research_registry.py
├── domains/
│   ├── data-governance.md
│   ├── data-quality.md
│   ├── metadata-management.md
│   ├── master-data-management.md
│   ├── data-lineage.md
│   ├── business-analysis.md
│   ├── requirements-and-acceptance-criteria.md
│   ├── architecture-decisions.md
│   ├── non-functional-requirements.md
│   ├── integration-architecture.md
│   ├── api-design.md
│   ├── event-driven-architecture.md
│   ├── observability-and-sre.md
│   ├── incident-management.md
│   ├── root-cause-analysis.md
│   ├── change-impact-analysis.md
│   ├── professional-operating-skills.md
│   └── ai-agent-skills.md
└── synthesis/
    ├── skill-candidate-map.md
    ├── artifact-template-map.md
    ├── decision-rule-map.md
    ├── quality-gate-map.md
    ├── weak-vs-strong-output-patterns.md
    └── recommended-next-skill-batches.md
```

---

*Research conducted June 2025. All sources verified and cited. No private or client material included.*
