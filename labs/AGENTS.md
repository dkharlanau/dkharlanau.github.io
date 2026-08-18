# Labs Agent Contract

This file applies to work under `labs/` in addition to the repository-level `AGENTS.md`.

## Career Factory

Labs are source material for the SAP Lead career roadmap. New Lab Markdown must not appear without an explicit career decision.

For every newly added `labs/**/*.md` file, add one of these frontmatter contracts.

Mapped to one or more career skills:

```yaml
career_impact: mapped
career_skills:
  - integration-recovery
  - delivery-observability
```

Not relevant to the career roadmap:

```yaml
career_impact: none
career_reason: "Internal Lab navigation page; it does not add an interview skill or evidence source."
```

Rules:

- Skill IDs come from `_data/career/roadmap.yml`.
- If the Lab introduces a genuinely new interview skill, add the skill to the roadmap instead of forcing it into a weak existing category.
- Prefer one to three accurate skill mappings. Do not tag every skill that mentions the same technology.
- `career_impact: none` is a real decision, not an escape hatch. Give a useful reason.
- A Lab can be unverified/noindex and still map to the career roadmap as working study material. Publication eligibility and career relevance are separate concerns.
- Do not change a page to `verified: true` merely because it is useful for interview preparation.

Run before publishing:

```bash
python3 scripts/check_career_factory.py
python3 scripts/check_career_factory.py --changed-from origin/main
```

The dedicated `Career Factory` workflow enforces this contract on pull requests that touch Labs or the career model.
