---
title: "Domain Research: Architecture Decisions"
robots: noindex
sitemap: false
---

# Architecture Decisions

## Research question

What professional skills, artifacts, rules, and quality gates should Skill Hub extract from architecture decision records, trade-off analysis, and decision governance?

## Best sources

| Source | Tier | Why it matters | Useful for |
|---|---:|---|---|
| [MADR Template](https://adr.github.io/madr/) (src-206) | 2 | Most widely adopted lightweight ADR template | ADR format, lifecycle, decision drivers |
| [ADR Examples (joelparkerhenderson)](https://github.com/joelparkerhenderson/architecture-decision-record) (src-207) | 2 | Comprehensive collection of ADR templates and examples | Format choice, real-world examples |
| [TOGAF 10th Edition](https://www.opengroup.org/togaf) (src-204) | 1 | Enterprise architecture framework with ADM and principles | Architecture principles, capability mapping |
| [SAP BTP Guidance Framework](https://architecture.learning.sap.com/) (src-205) | 1 | SAP official architecture guidance for BTP and S/4HANA | Decision guides, reference architectures |
| [Konishi ADR Operations](https://hidekazu-konishi.com/entry/architecture_decision_records_templates_and_operations.html) (src-212) | 2 | Practitioner synthesis of why ADR practices fail | Operationalizing ADRs, format selection, quarterly review |

## Key practical patterns

- Use lightweight ADRs (Nygard for small teams, MADR for larger/regulated, Y-Statement for rapid logging).
- Store ADRs in `docs/adr/` inside the code repository for version control and discoverability.
- Start with a Meta-ADR (0000) that records the decision to use ADRs.
- Link ADRs from code comments so they are visible at the point of decision.
- Enforce an immutable lifecycle: Proposed → Accepted → Deprecated/Superseded.

## Artifacts found

- Architecture Decision Record (Markdown file)
- Decision Log / Index
- Meta-ADR (0000)
- Trade-off analysis table (options vs. criteria)
- Risk register linked to decisions

## Decision rules found

- If a decision affects more than one team, then use MADR with full RACI front matter.
- If a decision is small and local, then append a Y-Statement to the decision log.
- If a decision changes, then create a new superseding ADR rather than editing the accepted one.
- If ADRs are not referenced from code, then the practice is failing silently.
- If a team has audit requirements, then use MADR with extended front matter and confirmation section.

## Quality gates found

- Every ADR must list considered options, not just the chosen one.
- Status must be actively maintained (Proposed → Accepted → Deprecated/Superseded).
- ADRs must be discoverable via `grep` or code search.
- A quarterly review must verify that the ADR collection is still trusted and current.
- Cross-cutting decisions must be stored in a shared repository with stable URLs.

## Common failure modes

- "Decision Documentation Theater" — writing ADRs without operational integration.
- Using the most complex template for every decision, causing fatigue and abandonment.
- Storing ADRs in wikis where they become invisible to developers.
- Not linking ADRs from the code they govern.
- Allowing accepted ADRs to be edited, destroying trust in the log.

## Candidate skills

- `adr-authoring-madr`
- `adr-operationalize`
- `adr-trade-off-analysis`
- `adr-governance`
- `lightweight-decision-log`

## Source-backed notes

- MADR provides YAML front matter for status, date, decision-makers, consulted, informed (RACI-style) and requires a "Considered Options" section (src-206).
- TOGAF defines Architecture Principles with statement, rationale, and implications (src-204).
- SAP BTP Guidance Framework provides Decision Guides for Integration, Extension, Developer, and Administrator scenarios (src-205).
- Konishi's blog identifies "Decision Documentation Theater" as the primary failure mode and recommends quarterly review cadences (src-212).

## Gaps / further research needed

- Public ADR repositories from enterprise SAP contexts are very few.
- Modern trade-off analysis templates (lightweight "If X, then Y" decision matrices for cloud architecture) are scattered across blogs.