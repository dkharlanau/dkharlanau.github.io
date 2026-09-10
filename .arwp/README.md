# Agent-Ready Web Profile adoption

Start with the repository's governing instructions and `.arwp/adoption.json`. This is a publisher-authored adoption contract, not a ranking, indexing, citation or conversion certification.

The site has one umbrella ARWP audience definition and exactly two human-facing intent owners:

- **Learn & Prepare** — `https://dkharlanau.github.io/learn/` for SAP interview preparation, assessment practice and professional learning. Atlas, Skill Hub, scenarios and reviewed learning material provide supporting evidence.
- **Improve & Operate** — `https://dkharlanau.github.io/services/sap-ams-consulting/` for SAP AMS improvement, recurring-incident reduction, integration reliability, master-data stability, diagnostics and bounded automation.

AI, Atlas, Labs, Skill Hub, datasets, Agent Skills and MCP surfaces support these journeys; they are not a third primary site direction.

## Sources and publication

- Canonical publication: `https://dkharlanau.github.io/`
- Profile source: `ai/site-profile.json`
- Two-focus routing source: `ai/focus-map.json`
- Authoritative site source: this Jekyll/static repository.
- Published directory: `_site`.
- Generated machine artifacts are owned by the repository generators. Do not patch generated output manually when a generator owns the file.
- CLI, Agent Skill, dataset or MCP source availability does not imply a hosted agent endpoint or an observed adoption outcome.

## Intent and evidence discipline

Reuse the canonical intent owner before adding a new page. A primary query family should resolve to one owner; supporting pages should deepen the answer and link back without competing for the same job.

For high-intent pages prefer: direct answer → concrete failure or worked example → decision criteria → evidence → strongest limitation → next useful action. Label synthetic scenarios as synthetic. Keep external factual claims sourceable and preserve the verified/unverified Atlas publication boundary.

Apply the ARWP evidence chain as: source or rule → target evidence → applicability → recommendation → exact surface → implementation → verification. Existing provenance tooling remains authoritative where it already records lineage; do not create a parallel provenance model merely for ARWP.

The tactic IDs in the adoption contract resolve against the current canonical [Goose ARWP discoverability corpus](https://github.com/dkharlanau/agent-ready-web-profile/blob/main/knowledge/discoverability-corpus.json). Follow its lifecycle, review-passport and versioning rules; do not reuse remembered tactic semantics when the canonical corpus has changed.

## Validation and measurement

Validate `ai/site-profile.json` with the exact ARWP commit pinned in `.github/workflows/arwp.yml`, and validate `ai/ai-search-profile.json` against the schema from the same pin. The site is built with Jekyll/GitHub Pages; inspect emitted `_site` HTML and JSON, not only source templates.

ARWP validation is implementation conformance. It does **not** prove crawl, index, ranking, AI citation, traffic or conversion outcomes.

Measure the two journeys separately when evidence exists: crawl eligibility, indexed state, search impressions/clicks and query families, Track A/Track B landing cohorts and route selection, useful-action completion, external AI citations/referrals and commercial contact action. Missing observations remain unknown, never zero.

Crawler-policy, privacy, public-repository safety and knowledge-publication approvals remain in force.
