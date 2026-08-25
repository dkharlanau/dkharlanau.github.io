# Labs Agent Contract

This file applies to work under `labs/` in addition to the repository-level `AGENTS.md`.

## Career Factory

Labs are source material for the SAP Lead career roadmap. New Lab content must not appear without an explicit career decision.

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

For a new static `labs/**/index.html` route, there is no YAML frontmatter contract. Make the career decision in `_data/career/roadmap.yml` instead:

- map the route as a `sources` entry on one or more relevant skills; or
- add the route to `lab_exclusions` with a useful reason when it is deliberately not career material.

## Required agent loop

When an agent adds or materially expands Lab content, it must run this reasoning loop before the change is complete:

1. **Discover** — identify the new business, SAP, architecture, AI, delivery, or leadership capability introduced by the Lab.
2. **Map** — connect it to one to three existing skill IDs in `_data/career/roadmap.yml`.
3. **Create** — if no existing skill accurately describes the interview capability, add a new skill with track, tier, rationale, interview signal, capabilities, and sources.
4. **Prove** — prefer a direct Lab route as evidence and add Assessment, Framework, Machine, or Story routes when they improve the interview path.
5. **Regenerate** — run `python3 scripts/generate_career_factory.py` so `/ai/career-factory.json` reflects the new state.
6. **Validate** — run the Career Factory validator and tests. A stale machine inventory is a CI failure.

The generated inventory is not merely reporting. It is the work queue for the next agent. Entries with `state: needs_decision` include heuristic `suggested_skills`; these are candidates, not automatic truth. Agents must review the match before changing the roadmap.

Rules:

- Skill IDs come from `_data/career/roadmap.yml`.
- If the Lab introduces a genuinely new interview skill, add the skill to the roadmap instead of forcing it into a weak existing category.
- Prefer one to three accurate skill mappings. Do not tag every skill that mentions the same technology.
- `career_impact: none` and `lab_exclusions` are real decisions, not escape hatches. Give a useful reason.
- A Lab can be unverified/noindex and still map to the career roadmap as working study material. Publication eligibility and career relevance are separate concerns.
- Do not change a page to `verified: true` merely because it is useful for interview preparation.
- Do not hand-edit `ai/career-factory.json`. It is generated from Labs and `_data/career/roadmap.yml`.
- CI/CD itself is part of Lead readiness: delivery automation, quality gates, evidence, rollback, and human-review boundaries should be mapped when a Lab demonstrates them.

## Rendered markup safety

Lab pages frequently mix Markdown, Liquid, and hand-written HTML. A Jekyll build can succeed even when Markdown inside an HTML wrapper is left as literal browser text.

Rules:

- Do not rely on `markdown="1"` for pipe tables, fenced code blocks, or large Markdown sections nested inside custom HTML components.
- For mixed HTML pages, prefer explicit semantic HTML. When a Markdown table is materially easier to maintain, capture it with Liquid and render it explicitly with `markdownify`.
- A successful Jekyll build is not sufficient evidence that a page is readable. Validate the rendered `_site` output.
- Raw table delimiters such as `|---|---|`, raw triple-backtick fences, or other Markdown syntax visible in built HTML are publication failures, even when the build itself succeeds.
- Keep wide tables inside an accessible horizontal scroll region rather than compressing many columns into unreadable text.

After building the site, run:

```bash
python3 scripts/check_rendered_markdown.py --site-dir _site --source-dir .
```

The main CI workflow runs this check after Jekyll so future agent edits cannot silently reintroduce the raw-Markdown rendering failure.

Run before publishing:

```bash
python3 scripts/generate_career_factory.py
python3 scripts/check_career_factory.py
python3 scripts/check_career_factory.py --changed-from origin/main
python3 scripts/generate_career_factory.py --check
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/test_career_factory.py tests/test_interview_readiness.py
```

The permanent `Career Factory` workflow enforces this contract on pull requests that touch Labs or the career model.