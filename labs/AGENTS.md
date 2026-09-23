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

## Assessment study-note ingestion

Use this workflow when the user is actively preparing for a SAP Lead assessment and sends notes, screenshots, links, remembered facts, or questions for incorporation into Labs.

### Input is not publication-ready

- Treat every incoming study note as candidate material, not as text to paste into the site.
- Never commit raw chat transcripts, private notes, client identifiers, ticket numbers, proprietary configuration, or other sensitive context.
- The public site stays English only. Rewrite source material in clear B2 English, semi-formal and natural. Use "we" when it improves explanation. Avoid generic AI phrasing and copied vendor wording.
- A remembered fact is not automatically a verified fact. Release-sensitive SAP claims need source checking before they are presented as product truth.

### Classify before editing

Route each useful input into one or more of these outcomes:

1. **Durable SAP knowledge** — update the existing SAP Enterprise page that owns the concept.
2. **Assessment memory** — add only the high-recall summary, contrast, or spoken-answer point to the relevant Assessment route.
3. **Diagnostic practice** — when the input contains a symptom, hypotheses, evidence, root cause, fix, or proof, update the relevant diagnostic page or assessment case dataset.
4. **Cross-process boundary** — link the topic to the real owner when the decision moves between Sales, MM, PP, EWM, TM, FI/CO, tax, MDG, or integration.
5. **Source only** — keep a useful primary source as evidence without inflating the page with duplicate prose.
6. **Uncertain** — do not publish a precise claim until the deployment model, release, or source is clear.

### Expand to the process boundary

Do not mirror the structure of the source material mechanically. Before editing, ask which neighboring processes are required to make the concept useful end to end.

- A Sales note may require context from ATP, MM/Procurement, PP, Inventory Management, EWM, TM, Billing, FI/CO, tax, MDG, or integration operations.
- Add only the neighboring concepts that explain ownership, a decision dependency, a financial consequence, or a likely assessment follow-up.
- Prefer strengthening an existing owner page and its cross-links. Creating a new page is the exception, not the default.
- When SAP training material gives a simplified sequence, keep the learning value but add the architectural boundary: which component owns the state, which document proves it, and what changes in a special process variant.

### Sales-first routing

During the Sales preparation phase, prefer these existing routes instead of creating duplicate pages:

- end-to-end and special process variants → `/labs/enterprise-context/sales-processes/`
- sales-order behavior and determinations → `/labs/enterprise-context/sales-order/`
- pricing → `/labs/enterprise-context/pricing/`
- ATP / aATP → `/labs/enterprise-context/atp/`
- credit → `/labs/enterprise-context/credit/`
- shipping and scheduling → `/labs/enterprise-context/shipping/`
- billing → `/labs/enterprise-context/billing/`
- FI/CO consequences → `/labs/enterprise-context/finance-logistics/`
- incident reasoning → `/labs/enterprise-context/sales-diagnostics/`
- short Lead-level recall and oral framing → `/labs/assessment/sales/`

Only create a new route when the existing owner page would become misleading or structurally overloaded.

### Verification boundary

For SAP product behavior that can vary by deployment or release:

- prefer current SAP Help Portal, SAP Learning, SAP Community content from SAP authors when appropriate, and official API/reference documentation;
- distinguish S/4HANA Cloud Public Edition, S/4HANA Cloud Private Edition, and S/4HANA on-premise when the behavior differs;
- do not project classic GUI transactions or on-premise customizing into Public Cloud without evidence;
- state the product/release boundary when it changes configuration, extensibility, integration, or operations;
- preserve `verified: false` and noindex status unless the repository's human-review process explicitly promotes the page.

### What should reach the Assessment page

Do not mirror every technical detail into `/labs/assessment/sales/`. Add a point there only when it improves one of these:

- a 30–90 second spoken answer;
- a high-value contrast that prevents a common mistake;
- a Lead-level ownership or architecture boundary;
- a diagnostic starting point;
- a likely follow-up question;
- a concise memory model that points to the deep-dive page.

The deep technical explanation stays in the owning SAP Enterprise route.

### Completion loop for each study update

1. Read the incoming material and identify the owning concept.
2. Check whether the repository already explains it.
3. Verify release-sensitive facts against current primary sources.
4. Update the smallest correct set of existing pages.
5. Add cross-links only where they help navigation or assessment recall.
6. Update assessment cases only when the material creates a real reasoning exercise.
7. If a new Lab page was required, complete the Career Factory mapping from this contract.
8. Preserve verification/indexing policy and run the relevant validation checks.

This workflow should make the repository better while the user studies: fewer duplicates, stronger explanations, better oral recall, and clearer evidence boundaries.

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