---
title: "Domain Research: Non-Functional Requirements"
robots: noindex
sitemap: false
---

# Non-Functional Requirements

## Research question

What professional skills, artifacts, rules, and quality gates should Skill Hub extract from NFR specification, quality attribute scenarios, and architecture review frameworks?

## Best sources

| Source | Tier | Why it matters | Useful for |
|---|---:|---|---|
| [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) (src-201) | 1 | Foundational six-pillar cloud architecture evaluation | NFR assessment, trade-off guidance, review process |
| [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/) (src-202) | 1 | Five-pillar model with explicit trade-off heatmaps | Workload review, cost/reliability trade-offs |
| [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework) (src-203) | 1 | Six-category framework with System Design as foundational pillar | Region selection, resource hierarchy, data lifecycle |
| [SEI ATAM](https://www.sei.cmu.edu/) (src-209) | 1 | Foundational academic method for evaluating architectures against quality attributes | Quality Attribute Scenarios, trade-off analysis |
| [TOGAF 10th Edition](https://www.opengroup.org/togaf) (src-204) | 1 | Enterprise architecture framework with NFR governance | Architecture principles, compliance assessment |

## Key practical patterns

- Use the "Cloud CORPS" common pillars across AWS/Azure/GCP: Cost, Operational Excellence, Reliability, Performance Efficiency, Security.
- Express NFRs as measurable Quality Attribute Scenarios (stimulus → response → measure).
- Evaluate architectures against NFRs early using structured review frameworks (Well-Architected, ATAM).
- Map NFRs to specific service-level objectives (SLOs, SLIs, SLAs).
- Treat trade-offs explicitly (e.g., Reliability vs. Cost, Security vs. Performance).

## Artifacts found

- Quality Attribute Tree / NFR specification
- Quality Attribute Scenarios (SEI format)
- Well-Architected Review report (AWS/Azure/GCP)
- SLO/SLI/SLA definitions
- Trade-off heatmap
- Risk register for unmet NFRs

## Decision rules found

- If a quality attribute scenario cannot be mapped to an architectural approach, then the architecture has a risk.
- If a workload is business-critical, then prioritize Reliability and Security over Cost Optimization.
- If sustainability impact is measurable, then include it as a design constraint.
- If a trade-off affects multiple stakeholders, then document it explicitly and obtain acceptance.
- If NFRs are vague (e.g., "fast"), then rewrite them as measurable scenarios before design begins.

## Quality gates found

- Architecture must be evaluated against quality attribute scenarios before implementation.
- Well-Architected Review (or equivalent) must be completed before production go-live.
- High-risk NFR gaps must have remediation plans with owners and timelines.
- SLOs must be defined, instrumented, and reviewed continuously.
- Trade-off points must be explicitly documented and accepted by stakeholders.

## Common failure modes

- Defining NFRs as vague adjectives ("fast," "secure," "scalable") without measurable scenarios.
- Evaluating architecture too late in the development cycle.
- Optimizing one pillar (e.g., Cost) at the expense of another (e.g., Reliability) without explicit trade-off acceptance.
- Ignoring business qualities (time to market, cost) in favor of technical qualities only.
- Not revisiting NFRs after major architectural changes.

## Candidate skills

- `nfr-scenario-writing`
- `well-architected-review`
- `slo-sli-design`
- `architecture-trade-off-analysis`
- `nfr-governance`

## Source-backed notes

- AWS Well-Architected Framework uses six pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability (src-201).
- SEI ATAM defines Quality Attribute Scenarios with stimulus, source, environment, artifact, response, and response measure (src-209).
- Azure Well-Architected Framework provides trade-off heatmaps showing pillar conflicts (src-202).

## Gaps / further research needed

- Missing strong public sources on ATAM in practice for modern cloud-native/SaaS organizations.
- Missing official SAP Well-Architected equivalent; SAP BTP Guidance Framework is fragmented across decision guides.
- Missing NFR-to-SAP-service mapping for quality attribute scenarios in SAP contexts.