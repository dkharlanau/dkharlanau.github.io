# Repository Technology Policy

Status: active  
Purpose: define the technology choices and migration boundaries for `dkharlanau.github.io`  
Last updated: 2026-06-12

---

## Principle

Stay **GitHub Pages-compatible for the core publishing stack**, while using **modern tooling around it** for validation, automation, and local development.

This repository is a public personal site and structured knowledge base. The build must remain reproducible on GitHub Pages without a custom deployment pipeline, because the cost and complexity of a custom build outweigh the benefits for a content-first site.

---

## Supported core stack

| Component | Version / choice | Rationale |
|---|---|---|
| GitHub Pages build | Native | Zero-config publishing from the `main` branch. |
| `github-pages` gem | Latest supported by GitHub Pages (currently 232) | Pins Jekyll, plugins, and themes to the exact versions GitHub Pages runs in production. |
| Jekyll | Version pinned by `github-pages` gem (currently 3.10.0) | Guarantees local builds match production builds. |
| Ruby | 3.3.4 | Matches `.ruby-version` and the GitHub Pages production runtime. |
| Bundler | 2.5.22 (lockfile) | Tracks the lockfile `BUNDLED WITH` value. |
| Theme | `minima` 2.5.1 | Default GitHub Pages theme; kept until GitHub Pages changes it. |

Reference: [GitHub Pages dependency versions](https://pages.github.com/versions/)

---

## Modern tooling stack

These tools run alongside the core stack but do not replace it.

| Tool | Version / choice | Role |
|---|---|---|
| Python | 3.12 | Validation scripts, tests, link checking, SEO checks, artifact generation. |
| pytest | Latest stable | Python test runner. |
| PyYAML | Latest stable | YAML parsing in validation scripts. |
| Node.js | 22 LTS | Runs `scripts/generate_dama_pages.js` in CI. Script uses only `fs` and `path`. |
| GitHub Actions | `ubuntu-latest`, current action versions | CI validation (`seo-checks.yml`, `indexnow-dry-run.yml`). |

All Python scripts remain **stdlib-first**; the only declared runtime dependencies are `pytest` and `PyYAML`, installed in CI.

---

## Allowed frontend approach

The site is intentionally static and lightweight:

- **Markup:** Markdown, Liquid includes, and static HTML.
- **Styling:** Modern CSS with no build step.
- **Behavior:** Small, vanilla JavaScript modules for progressive enhancement.
- **Assets:** Static images, fonts, and icons committed to `assets/`.

Avoid heavy client-side frameworks. Pages must render correctly without JavaScript, then enhance when JavaScript is available.

---

## Avoid for now

Do not pursue these changes unless a concrete, documented limitation makes them necessary:

| Change | Reason to defer |
|---|---|
| Jekyll 4 migration | GitHub Pages natively builds with Jekyll 3.10.0 via the `github-pages` gem. A Jekyll 4 build would require a custom GitHub Actions deployment pipeline and break parity with native Pages builds. |
| Astro / Vite / React rebuild | Adds build complexity, npm dependency management, and a deployment pipeline for no clear content benefit. |
| Custom GitHub Pages deploy | Native Pages deployment is sufficient. A custom deploy is extra operational surface area. |
| Major Ruby upgrade beyond 3.3.4 | GitHub Pages runtime is pinned to 3.3.4. Upgrading the repo would create CI ↔ Pages drift. |
| Major Node.js beyond 22 LTS | Node 22 is supported until 2027-04-30. The single Node script has no dependency risk, so there is no urgency. |

---

## Future evaluation

A **custom GitHub Actions Pages deployment** may be evaluated only as research, not as a planned migration. Before it becomes a real proposal, it must be justified by:

1. A concrete limitation of native GitHub Pages that blocks a needed feature.
2. A migration plan that includes local build parity, CI validation, and rollback steps.
3. Explicit confirmation that the benefit outweighs the added operational complexity.

Until then, the default position is to stay on the native GitHub Pages build.

---

## Related documents

- `docs/local-site-validation.md` — Local Ruby/Jekyll setup and validation pipeline.
- `reports/technology-modernization-audit-2026-06-12.md` — Audit that produced this policy.
- `.ruby-version` — Ruby runtime pin.
- `.github/workflows/seo-checks.yml` — CI validation workflow.
- `.github/workflows/indexnow-dry-run.yml` — IndexNow CI workflow.
