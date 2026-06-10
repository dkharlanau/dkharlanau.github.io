---
title: "Domain Research: Business Analysis"
robots: noindex
sitemap: false
---

# Business Analysis

## Research question

What professional skills, artifacts, rules, and quality gates should Skill Hub extract from business analysis, process modeling, and stakeholder engagement?

## Best sources

| Source | Tier | Why it matters | Useful for |
|---|---:|---|---|
| [USDS Discovery Sprint Guide](https://sprint.usds.gov/) (src-101) | 1 | Federal playbook for 2–4 week discovery sprints | Problem diagnosis, stakeholder interviews |
| [GOV.UK Service Manual](https://www.gov.uk/service-manual) (src-102) | 1 | UK government standard for digital service delivery | Discovery → Alpha → Beta → Live lifecycle |
| [U.S. Digital Service Playbook](https://playbook.usds.gov/) (src-103) | 1 | Thirteen plays for successful digital projects | User needs, agile practices, open data |
| [BPMN 2.0 Specification](https://www.omg.org/bpmn/) (src-105) | 1 | De-facto international standard for process modeling | Process diagrams, execution semantics |
| [SBVR Vocabulary](https://www.brcommunity.com/articles.php?id=b280) (src-106) | 1 | OMG standard for business rules in controlled natural language | Business vocabulary, rule statements |
| [18F Methods](https://methods.18f.gov/) (src-107) | 2 | Public catalog of human-centered design methods | Contextual inquiry, affinity mapping, journey mapping |

## Key practical patterns

- Start with user needs, not organizational structures or technology assumptions.
- Use lightweight, iterative documentation instead of heavy BRDs/FRDs.
- Maintain bidirectional traceability from requirement through to test/verification.
- Separate diagnosis (discovery) from solutioning; do not commit to build before understanding the problem.
- Use BPMN as a common language between business analysts and technical implementers.

## Artifacts found

- User research plans and findings reports
- Process maps (BPMN) and journey maps
- Requirements traceability matrices
- Business vocabularies and rule catalogs (SBVR-style)
- Discovery sprint reports with actionable next steps

## Decision rules found

- If a requirement cannot be traced to a user need, then it should not be in scope.
- If a process map cannot be validated by the people who perform the work, then it is fiction.
- If a business rule is not practicable (an observer cannot decide compliance), then it is a policy, not a rule.
- If organizational standards for "done" exist, then all teams must meet them as a minimum.

## Quality gates found

- Every requirement must have a unique ID and a verification method.
- Service/design must pass assessment against an explicit standard before proceeding to next phase.
- Research findings must be demonstrably linked to design decisions.

## Common failure modes

- Designing around government/organizational silos instead of user needs.
- Confusing business policies with practicable business rules.
- Skipping discovery and jumping to procurement or build.
- Allowing the Definition of Done to degrade over time.

## Candidate skills

- `discovery-sprint-facilitation`
- `business-vocabulary-modeling`
- `process-mapping-with-bpmn`
- `requirements-traceability-management`

## Source-backed notes

- USDS discovery sprints identify root causes, not solutions, through cross-functional team pairing (src-101).
- GDS Service Manual defines the Discovery → Alpha → Beta → Live lifecycle with explicit user-research requirements (src-102).
- BPMN 2.0 provides three diagram types (Process, Collaboration, Choreography) with execution semantics (src-105).
- SBVR separates definitional rules (structural) from behavioral rules (operational) using Structured English (src-106).

## Gaps / further research needed

- IIBA BABOK full content is paywalled; free official summaries are scarce.
- Strong, vendor-neutral gap analysis frameworks are surprisingly thin in public domain.
- Practical stakeholder analysis templates with worked examples from real projects are limited.