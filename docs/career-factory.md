# Career Factory

The Career Factory keeps SAP Lead interview preparation connected to the working Labs instead of maintaining a second knowledge base by hand.

## Purpose

The system has four layers:

1. **Labs and evidence** — technical, business, assessment, framework, and project material.
2. **Career skills** — the capability a Lead candidate should demonstrate.
3. **Interview signal** — what a strong answer should prove.
4. **Practice and evidence** — questions, project stories, mock interviews, and progress.

The source model is `_data/career/roadmap.yml`. The human UI is `/labs/interview-readiness/roadmap/`. The machine-readable view is `/ai/career-roadmap.json`.

## Skill model

Each skill has:

- a stable ID;
- one career track;
- a tier: Core, Cross-boundary, or Differentiator;
- a short reason why the skill matters;
- an interview signal;
- one or more capability stages: Know, Diagnose, Design, Lead;
- one or more source routes.

Source routes can point to Labs, Assessment, Frameworks, the Machine layer, or other public evidence. The career layer links to the source; it does not copy it.

## Lab-to-career contract

Existing Labs are grandfathered. Every new Lab page must make an explicit career decision.

For new Markdown, use frontmatter.

Mapped:

```yaml
career_impact: mapped
career_skills:
  - logistics-p2p
  - logistics-master-data
```

Not mapped:

```yaml
career_impact: none
career_reason: "Navigation-only page; it does not add a new interview skill or evidence source."
```

For a new static `labs/**/index.html` route, make the decision in `_data/career/roadmap.yml`: reference the route from a relevant skill source, or add it to `lab_exclusions` with a useful reason.

If a new Lab introduces a real skill that does not exist in the roadmap, add the skill to `_data/career/roadmap.yml`. Do not map it to a vaguely similar skill only to make CI green.

## CI

`.github/workflows/career-factory.yml` runs when Labs or the career model change. It checks:

- roadmap schema and minimum Lead-level scope;
- unique skill IDs;
- track, tier, and capability references;
- Markdown and static-HTML source routes;
- any Lab page that already declares career metadata;
- every newly added Lab Markdown or HTML page on a pull request;
- regression tests for the career UI and machine endpoint.

Run locally:

```bash
python3 scripts/check_career_factory.py
python3 scripts/check_career_factory.py --changed-from origin/main
python3 -m pytest tests/test_career_factory.py tests/test_interview_readiness.py
```

## Agent workflow

When an agent creates a Lab page:

1. Decide whether the page adds or strengthens an interview skill.
2. Find the best existing skill ID in `_data/career/roadmap.yml`.
3. If no accurate skill exists, add one with an interview signal and evidence source.
4. Record the career decision in Markdown frontmatter or the central roadmap model for static HTML.
5. Run the Career Factory validation.
6. Keep publication status separate. Career relevance does not mean the page is human-reviewed or indexable.

This rule is also repeated in `labs/AGENTS.md` so agents working inside Labs see it close to the files they edit.

## Future extensions

The source model is intentionally reusable. Later iterations can add role variants such as Senior Consultant, SAP Lead, Solution Architect, or AI/SAP Lead without duplicating the underlying Lab content. The same model can also drive skill-gap reports, practice recommendations, and evidence coverage checks.
