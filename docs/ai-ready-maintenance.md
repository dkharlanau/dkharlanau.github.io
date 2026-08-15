# AI Ready maintenance

AI Ready is the vendor-neutral architecture learning area under `/labs/ai-ready/`.

## Boundaries

- Keep `/ai/` focused on machine-readable site routing and discovery.
- Keep `/labs/enterprise-context/business-ai/` focused on the SAP Business AI product landscape.
- Keep `/labs/ai-ready/` focused on reusable AI architecture decisions, implementation patterns, controls, datasets, and hands-on labs.
- Prefer primary sources for protocol, security, governance, and platform facts.
- Date fast-moving protocol and product claims. Durable architecture rules do not need artificial freshness labels.

## Content model

Use this learning order unless a topic has a strong reason to live elsewhere:

1. Foundations
2. Data and retrieval
3. Tools and MCP
4. Agent architecture
5. Evals and reliability
6. Security and governance
7. Build and deploy
8. Decision matrix
9. Hands-on labs

Every practical topic should answer four questions: what problem it solves, when to use it, what can fail, and how to test it.

## Machine-readable artifacts

- `labs/ai-ready/data/catalog.json` stores architecture tracks, decision rules, production rules, lab definitions, and reviewed source metadata.
- `labs/ai-ready/data/eval-sample.jsonl` stores small architecture cases with expected patterns, required controls, and failure signals.
- Extend eval data from real failures and ambiguous decisions instead of collecting decorative examples.

## Repository generation rule

Markdown changes can affect generated Atlas discovery artifacts. `.github/workflows/refresh-atlas-artifacts.yml` runs `scripts/generate_atlas_artifacts.py` after Markdown changes and commits tracked generated updates when needed. CI still validates the generated state with `--check`.

Do not hand-edit generated Atlas artifacts to silence CI. Fix source content or the generator contract instead.
