---
title: "Domain Research: Requirements and Acceptance Criteria"
robots: noindex
sitemap: false
---

# Requirements and Acceptance Criteria

## Research question

What professional skills, artifacts, rules, and quality gates should Skill Hub extract from requirements elicitation, acceptance criteria authoring, and Definition of Done practices?

## Best sources

| Source | Tier | Why it matters | Useful for |
|---|---:|---|---|
| [The 2020 Scrum Guide](https://scrumguides.org/scrum-guide.html) (src-104) | 1 | Canonical definition of Scrum and Definition of Done | DoD, Increment quality, Sprint Review |
| [Agile Alliance Glossary](https://agilealliance.org/agile101/agile-glossary/) (src-108) | 2 | Vendor-neutral glossary for Definition of Ready, Given-When-Then | Acceptance criteria patterns, INVEST |
| [Jama RTM Guide](https://www.jamasoftware.com/requirements-management-guide/requirements-traceability/how-to-create-and-use-a-requirements-traceability-matrix-rtm/) (src-109) | 2 | Practical step-by-step guide to RTM | Bidirectional traceability, compliance mapping |
| [GDS User Research Assessment](https://userresearch.blog.gov.uk/2016/02/15/passing-the-user-research-points-in-your-service-assessment/) (src-110) | 2 | Candid assessor guidance on user research criteria | Research quality gates, inclusive recruiting |
| [USDS Playbook](https://playbook.usds.gov/) (src-103) | 1 | Play 1: Understand what people need | User-centered requirements |

## Key practical patterns

- Write criteria from the user's perspective, not the system's internal behavior.
- Use Given-When-Then for behavior-driven clarity; use bullet format for simple conditions.
- Include edge cases, error conditions, and integration points upfront.
- Make criteria collaborative: product owner, developers, UX, and QA all contribute.
- Definition of Ready checklist must be met before a story enters a sprint.

## Artifacts found

- Acceptance criteria lists per user story
- Given-When-Then scenario specifications
- Test case mappings in the RTM
- Definition of Done (product-level quality standard)
- Definition of Ready checklist

## Decision rules found

- If a story has no acceptance criteria, then it is not ready for development.
- If criteria are written by only one role, then ambiguities will surface during development.
- If a criterion cannot be tested, then it is not a valid acceptance criterion.
- If a Product Backlog item does not meet the Definition of Done, then it cannot be released.
- If acceptance criteria only cover the happy path, then edge cases will cause scope creep mid-sprint.

## Quality gates found

- Acceptance criteria must be reviewed and agreed upon before sprint start.
- Criteria must cover functional and non-functional requirements (security, performance, accessibility).
- DoD must be met for every Increment; undone work returns to the Product Backlog.
- Every requirement must have at least one verification method (test, inspection, analysis).

## Common failure modes

- Confusing acceptance criteria (story-level) with Definition of Done (product-level).
- Writing criteria that prescribe implementation rather than define outcomes.
- Missing error paths and edge cases.
- Allowing mid-sprint changes to criteria without transparent team agreement.

## Candidate skills

- `given-when-then-authoring`
- `definition-of-done-crafting`
- `edge-case-identification`
- `acceptance-test-mapping`
- `user-story-refinement`

## Source-backed notes

- Scrum Guide defines DoD as a formal description of the state of the Increment when it meets quality measures; undone work cannot be presented at Sprint Review (src-104).
- Agile Alliance Glossary defines Definition of Ready based on INVEST properties (src-108).
- Jama guide emphasizes bidirectional traceability and compliance references for regulated industries (src-109).

## Gaps / further research needed

- Requirements management tools documentation (Jama, DOORS) is product-centric; vendor-neutral process guides are scarce.
- Lightweight traceability guidance for commercial software (non-safety-critical) is less rigorous.