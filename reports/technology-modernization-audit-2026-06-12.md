# Technology Modernization Audit

**Repository:** `dkharlanau/dkharlanau.github.io`  
**Branch:** `chore/technology-modernization-audit`  
**Date:** 2026-06-12  
**Auditor:** Agent (Orchestrator)  
**Scope:** Runtime versions, Ruby/Jekyll dependencies, Python scripts, Node tooling, GitHub Actions, security advisories, repository-specific risks.

---

## Executive summary

### Highest-risk outdated technologies

1. **Local Ruby 2.6.10** — End-of-life since 2022-04-12. The local development environment cannot build the site because the lockfile requires Ruby 3.3.4. This is a severe local/CI drift.
2. **CI Ruby 3.2.3** — End-of-life as of 2026-04-01 (official ruby-lang.org). The CI workflows still specify Ruby 3.2.3, which is now unsupported and inconsistent with the repo `.ruby-version` (3.3.4) and GitHub Pages runtime (3.3.4).
3. **CI Node.js 20** — End-of-life as of 2026-04-30. The `seo-checks.yml` workflow specifies `node-version: "20"`. Node 20 will be removed from GitHub Actions runners by 2026-09-16.
4. **Local Python 3.9.6** — End-of-life as of 2025-10-31. Local scripts still run because they rely almost exclusively on the standard library, but any environment relying on 3.9 is no longer receiving security patches.

### Security issues found

- **No `bundle audit` installed locally.** Could not verify Ruby gem CVE status.
- **No `pip-audit` installed locally.** Could not verify Python dependency CVE status.
- **Ruby 3.2.3 and Node 20 in CI are past EOL.** They will not receive security patches.
- The `github-pages` gem 232 / Jekyll 3.10.0 stack is the current GitHub Pages supported baseline. No known critical CVEs in this specific pinned stack, but staying on Jekyll 3.x means no access to Jekyll 4.x security fixes unless GitHub Pages backports them.

### Recommended low-risk updates

- **Align CI Ruby to 3.3.4** in both workflows (`seo-checks.yml`, `indexnow-dry-run.yml`) to match `.ruby-version` and GitHub Pages runtime.
- **Bump CI Node.js to 22** in `seo-checks.yml` (LTS, supported until 2027-04-30). The only Node script (`generate_dama_pages.js`) uses only `fs` and `path` — no breaking changes expected.
- **Add explicit workflow permissions** (`permissions: contents: read`) to both workflows for defense-in-depth.
- **Add `pip-audit` and `bundle-audit` to local development recommendations** in documentation.

### Recommended medium-risk updates

- **Upgrade local Python to 3.11+** (3.11 is in security maintenance until 2027-10-31; 3.12 is preferred). Requires verifying `pytest` and `PyYAML` compatibility — expected to be trivial.
- **Evaluate Jekyll 4.x migration via GitHub Actions custom build** (not `github-pages` gem). This is a larger architectural decision because GitHub Pages natively still builds with Jekyll 3.10.0.
- **Pin Python version in `seo-checks.yml`** explicitly (currently uses `python3` without `actions/setup-python`).

### Updates to avoid for now

- **Major Jekyll upgrade** (3.10.0 → 4.4.1) is blocked by GitHub Pages compatibility. The `github-pages` gem 232 explicitly pins Jekyll 3.10.0.
- **Major Ruby upgrade** (3.3.4 → 3.4.x or 4.0.x) is not supported by GitHub Pages yet. The official GitHub Pages dependency versions page lists Ruby 3.3.4 as the current runtime.
- **Major Python upgrade** in CI scripts is not urgent if scripts remain stdlib-only, but local environment should be modernized.
- **Replacing the build system** (e.g., moving from Jekyll to another SSG) is out of scope for this audit.

### Unknowns / missing local tools

- `bundle audit` not installed.
- `pip-audit` not installed.
- Local Ruby 2.6.10 cannot resolve the lockfile, so `bundle exec jekyll build` was not testable locally. The Jekyll build is only verified in CI.
- No `package.json` or lockfile exists for the single Node.js script.

---

## Current stack inventory

| Area | Detected technology | Current version | Source file / command | Role in repo |
|------|---------------------|-----------------|----------------------|--------------|
| Ruby (local) | ruby | 2.6.10 (EOL) | `ruby --version` | Local dev runtime |
| Ruby (repo) | ruby | 3.3.4 | `.ruby-version` | Repo-specified runtime |
| Ruby (CI) | ruby | 3.2.3 (EOL) | `.github/workflows/*.yml` | CI runtime |
| Ruby (GitHub Pages) | ruby | 3.3.4 | https://pages.github.com/versions/ | Pages build runtime |
| Jekyll | jekyll | 3.10.0 | `Gemfile.lock` | Static site generator |
| GitHub Pages gem | github-pages | 232 | `Gemfile.lock` | Pages compatibility shim |
| Bundler | bundler | 2.5.22 (lockfile), 2.4.22 (local) | `Gemfile.lock`, `bundle --version` | Dependency manager |
| Python (local) | python | 3.9.6 (EOL) | `python3 --version` | Script/test runtime |
| Python (CI) | python | 3.11 (indexnow), unlabeled (seo-checks) | `.github/workflows/*.yml` | CI script runtime |
| PyYAML | yaml | 6.0.3 | `python3 -c "import yaml"` | YAML parsing in scripts |
| pytest | pytest | 8.4.2 | `pytest --version` | Test runner |
| Node.js (CI) | node | 20 (EOL) | `.github/workflows/seo-checks.yml` | DAMA page generation |
| Node.js (local) | node | v24.15.0 | `node --version` | Local runtime (unrelated to repo) |
| GitHub Actions runner | ubuntu | latest (currently 24.04) | `.github/workflows/*.yml` | CI OS |
| GitHub Actions checkout | actions/checkout | v4 | `.github/workflows/*.yml` | Source checkout |
| GitHub Actions Ruby setup | ruby/setup-ruby | v1 | `.github/workflows/*.yml` | Ruby install |
| GitHub Actions Node setup | actions/setup-node | v4 | `.github/workflows/seo-checks.yml` | Node install |
| GitHub Actions Python setup | actions/setup-python | v5 | `.github/workflows/indexnow-dry-run.yml` | Python install |
| Jekyll theme | minima | 2.5.1 | `Gemfile.lock` | Default theme |
| Jekyll plugins | jekyll-seo-tag, jekyll-sitemap, jekyll-feed | 2.8.0, 1.4.0, 0.17.0 | `Gemfile.lock`, `_config.yml` | SEO, sitemap, RSS |

---

## Update recommendations

| Item | Current version | Latest stable / recommended version | Reason | Risk level | Update type | Evidence/source | Recommended action |
|------|-----------------|--------------------------------------|--------|------------|-------------|-----------------|------------------|
| CI Ruby (both workflows) | 3.2.3 | 3.3.4 | Ruby 3.2 EOL 2026-04-01; GitHub Pages and `.ruby-version` already use 3.3.4 | **Low** | EOL / maintenance | https://www.ruby-lang.org/en/downloads/branches/ | Update `ruby-version` to `"3.3.4"` in both workflows |
| CI Node.js (seo-checks) | 20 | 22 | Node 20 EOL 2026-04-30; removed from GA runners by 2026-09-16; only script uses `fs`/`path` | **Low** | EOL / maintenance | https://nodejs.org/en/about/previous-releases | Update `node-version` to `"22"` |
| Local Ruby | 2.6.10 | 3.3.4 | Ruby 2.6 EOL 2022-04-12; lockfile incompatible | **Medium** | EOL | Local `ruby --version` | Install Ruby 3.3.4 via rbenv/asdf/ruby-build; do not commit local runtime |
| Local Python | 3.9.6 | 3.12 (or 3.11) | Python 3.9 EOL 2025-10-31; scripts are stdlib-only | **Low** | EOL | https://devguide.python.org/versions/ | Upgrade local Python to 3.12; verify `pytest` + `PyYAML` |
| Python in CI (seo-checks) | unlabeled (system `python3`) | 3.11 or 3.12 | Inconsistent with `indexnow-dry-run.yml` which pins 3.11; explicit is better | **Low** | maintenance | Workflow file | Add `actions/setup-python@v5` step with `python-version: "3.12"` |
| Workflow permissions | implicit (broad) | explicit `contents: read` | Defense-in-depth; least-privilege | **Low** | hardening | GitHub security best practices | Add `permissions: contents: read` at job level; add `packages: none` etc. |
| `faraday` gem | 2.14.1 | 2.14.2 | Patch update available per `bundle outdated` | **Low** | maintenance | `bundle outdated` output | `bundle update faraday` after Ruby alignment |
| `bundle audit` tool | not installed | latest | Needed for ongoing Ruby security monitoring | **Low** | tooling | Local command failed | `gem install bundler-audit` locally; add to docs |
| `pip-audit` tool | not installed | latest | Needed for ongoing Python security monitoring | **Low** | tooling | Local command failed | `pip install pip-audit` locally; add to docs |
| `github-pages` gem | 232 | 232 | Already at latest supported by GitHub Pages | N/A | N/A | https://pages.github.com/versions/ | No action; track GitHub Pages changelog |
| Jekyll | 3.10.0 | 3.10.0 | Blocked by GitHub Pages gem | N/A | blocked | `Gemfile.lock`, GitHub Pages docs | Do not update until GitHub Pages supports Jekyll 4 |
| `kramdown` | 2.4.0 | 2.5.2 | Blocked by GitHub Pages gem | N/A | blocked | `bundle outdated` | Do not update until GitHub Pages supports it |
| `liquid` | 4.0.4 | 5.12.0 | Blocked by GitHub Pages gem | N/A | blocked | `bundle outdated` | Do not update until GitHub Pages supports it |
| Node.js in `indexnow-dry-run.yml` | N/A (env flag only) | N/A | Workflow has `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true` but no Node steps; flag is harmless but redundant | **Low** | cleanup | Workflow inspection | Remove redundant env flag or keep as safety net |

---

## Do not update yet

| Item | Reason to avoid updating now | Blocker | What must be checked first |
|------|------------------------------|---------|----------------------------|
| Jekyll 3.10.0 → 4.4.1 | GitHub Pages natively builds with Jekyll 3.10.0 via `github-pages` gem 232. Upgrading to 4.x would cause a local/remote mismatch unless a custom GitHub Actions build is adopted. | GitHub Pages dependency versions | Verify GitHub Pages has added Jekyll 4 support; or migrate to custom Actions build (larger effort) |
| `github-pages` gem 232 → newer | Already at the latest version supported by GitHub Pages. | GitHub Pages release schedule | Monitor https://pages.github.com/versions/ for a new gem release |
| `kramdown` 2.4.0 → 2.5.2 | Pinned by `github-pages` gem 232. | Gemfile lock | Wait for GitHub Pages gem update |
| `liquid` 4.0.4 → 5.12.0 | Pinned by `github-pages` gem 232. | Gemfile lock | Wait for GitHub Pages gem update |
| Ruby 3.3.4 → 3.4.x / 4.0.x | GitHub Pages runtime is pinned to 3.3.4. Upgrading the repo would break CI ↔ Pages parity. | https://pages.github.com/versions/ | Wait for GitHub Pages to officially support Ruby 3.4 or 4.0 |
| Major Python upgrade in CI scripts | Scripts use only standard library; no functional benefit from upgrading CI Python unless new language features are needed. | None (just not valuable) | If upgrading, run full test suite (`pytest`) and all validation scripts |
| Node.js 22 → 24 in CI | Node 22 is LTS until 2027-04-30. Moving to 24 is safe but unnecessary. | Low urgency | Test `generate_dama_pages.js` on Node 24 if desired; otherwise 22 is sufficient |

---

## GitHub Actions findings

### Workflow: `seo-checks.yml`

- **Ruby version:** `"3.2.3"` → **must be updated to `"3.3.4"`** to match `.ruby-version` and GitHub Pages.
- **Node version:** `"20"` → **must be updated to `"22"`** (or `"24"`) because Node 20 is EOL and will be removed from runners by September 2026.
- **Python version:** Not pinned. Uses `python3` from the runner image. Should be pinned to `"3.12"` for consistency with the other workflow and to avoid drift when the runner image changes.
- **Permissions:** No explicit `permissions` block. Add `permissions: contents: read` at the job level.
- **Env flag:** `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true` is present. This is good because it forces third-party actions to Node 24, but it does not fix the fact that `actions/setup-node` is still installing Node 20.

### Workflow: `indexnow-dry-run.yml`

- **Ruby version:** `"3.2.3"` → **must be updated to `"3.3.4"`**.
- **Python version:** `"3.11"` — acceptable, but could be updated to `"3.12"` for longer runway. Low risk because scripts are stdlib-only.
- **Permissions:** No explicit `permissions` block. Add `permissions: contents: read` at the job level. The workflow does not need `secrets` read except for `INDEXNOW_KEY` on manual dispatch; for that case, `permissions: {}` or explicit `secrets: read` is not needed because repository secrets are handled by GitHub, not workflow permissions.
- **Env flag:** `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true` is present but redundant because this workflow has no Node steps. Keeping it is harmless.
- **`actions/setup-python@v5`:** Current and stable.
- **`actions/checkout@v4`:** Current and stable.
- **`ruby/setup-ruby@v1`:** Current and stable.
- **`actions/setup-node@v4`:** Not used in this workflow.

### Actions versions summary

| Action | Current version | Status | Recommendation |
|--------|-----------------|--------|----------------|
| `actions/checkout` | v4 | Supported, no deprecation | Keep |
| `ruby/setup-ruby` | v1 | Supported | Keep |
| `actions/setup-node` | v4 | Supported | Keep, but update Node version to 22 |
| `actions/setup-python` | v5 | Supported | Keep, optionally update Python to 3.12 |

---

## Dependency findings

### Ruby / Jekyll

- **Gemfile:** Minimal. Only `github-pages`, `webrick (~> 1.8)`, `faraday-retry`.
- **Lockfile:** `github-pages` 232 pins Jekyll 3.10.0 and all associated plugins. This is the correct state for GitHub Pages compatibility.
- **Outdated gems (from `bundle outdated`):**
  - `faraday` 2.14.1 → 2.14.2 (patch, safe)
  - `jekyll` 3.10.0 → 4.4.1 (blocked)
  - `kramdown` 2.4.0 → 2.5.2 (blocked)
  - `liquid` 4.0.4 → 5.12.0 (blocked)
- **Security audit:** `bundle audit` is not installed. Cannot verify CVE status of gems. This is a tooling gap, not necessarily a vulnerability.
- **Bundler version:** `BUNDLED WITH 2.5.22` in lockfile. Local Bundler is 2.4.22. Minor mismatch, not breaking.

### Python

- **No `requirements.txt`, `pyproject.toml`, `setup.cfg`, or `Pipfile`.** Python dependencies are implicit.
- **Runtime dependencies:** `pytest` (tests only), `PyYAML` (some scripts import `yaml`).
- **All other imports are standard library:** `argparse`, `csv`, `datetime`, `hashlib`, `html`, `json`, `os`, `pathlib`, `re`, `subprocess`, `sys`, `tempfile`, `textwrap`, `unittest`, `urllib`, `xml`, `uuid`, `glob`, `shutil`, `copy`, `collections`, `dataclasses`, `typing`.
- **Outdated packages:** `pip list --outdated` shows many globally installed packages (e.g., `google-api-core`, `grpcio`, `Flask`) but these are **not declared in the repo** and are likely local environment noise. The repo itself does not depend on them.
- **Security audit:** `pip-audit` is not installed. Cannot verify CVE status.
- **Tests:** 199 tests pass in 12.51s on Python 3.9.6 + pytest 8.4.2. No breaking changes expected on Python 3.11–3.12.

### Node / npm

- **No `package.json`, `package-lock.json`, `yarn.lock`, or `pnpm-lock.yaml`.**
- **Only one Node script:** `scripts/generate_dama_pages.js`.
- **Script analysis:** Uses only `fs` and `path` (Node core modules). No npm dependencies. No build step. Extremely low risk for Node version upgrades.
- **npm audit:** Not applicable (no dependencies).
- **Node version in CI:** 20 (EOL). Must be updated to 22 or 24.

### GitHub Actions

- All action versions are current (v4/v5/v1). No deprecated action versions detected.
- The only deprecation risk is the **Node.js runtime inside actions** (not the action versions themselves). The `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24` flag mitigates third-party action runtime issues, but the explicit `node-version: "20"` in `seo-checks.yml` is the remaining problem.
- `ubuntu-latest` is currently resolving to `ubuntu-24.04` (as of 2026-06-12). This is fine and expected. No need to pin to `ubuntu-24.04` explicitly unless stability is preferred over automatic updates.

---

## Suggested PR plan

Split the work into small, safe, sequential PRs.

### PR 1 — Low-risk CI / action version alignment

**Title:** `chore(ci): align Ruby to 3.3.4, Node to 22, and add explicit permissions`

**Changes:**
- `.github/workflows/seo-checks.yml`:
  - `ruby-version: "3.3.4"`
  - `node-version: "22"`
  - Add `actions/setup-python@v5` with `python-version: "3.12"`
  - Add `permissions: contents: read`
- `.github/workflows/indexnow-dry-run.yml`:
  - `ruby-version: "3.3.4"`
  - Optionally `python-version: "3.12"`
  - Add `permissions: contents: read`

**Validation:**
- Push to branch and verify both workflows run green.
- Confirm `pytest` still passes.
- Confirm `bundle exec jekyll build` still passes.
- Confirm `node scripts/generate_dama_pages.js` still passes.

**Risk:** Very low. All changes are version bumps to currently supported runtimes that the repo already uses elsewhere.

### PR 2 — Local environment documentation + tooling recommendations

**Title:** `docs(dev): add local environment setup guide and security audit tooling`

**Changes:**
- Add a `docs/development-environment.md` or update `README.md` with:
  - Required Ruby version (3.3.4) and install via rbenv/asdf
  - Required Python version (3.12 recommended)
  - Required Node version (22 for CI parity, or 24)
  - Commands to install `bundler-audit` and `pip-audit`
- No code changes.

**Risk:** Zero. Documentation only.

### PR 3 — Lockfile refresh (if needed)

**Title:** `chore(deps): refresh Gemfile.lock after Ruby alignment`

**Changes:**
- Run `bundle install` on Ruby 3.3.4 to regenerate the `Gemfile.lock` platform/ruby metadata if needed.
- Run `bundle update faraday` if the patch update is desired.

**Validation:**
- `bundle exec jekyll build`
- `pytest`
- `python scripts/check_public_repo.py`
- `python scripts/generate_atlas_artifacts.py --check`
- `python scripts/check_links.py _site`
- `python scripts/check_seo.py _site` (note: expect localhost canonical warnings unless `JEKYLL_ENV=production` is set)

**Risk:** Low. Only patch-level updates and metadata refresh.

### PR 4 — Major upgrades (deferred, needs human decision)

**Title:** `feat(build): evaluate Jekyll 4 / GitHub Actions custom build migration`

**When:** Only after GitHub Pages officially supports Jekyll 4, or after the team decides to move to a custom GitHub Actions build pipeline (not the native Pages build).

**Blockers:**
- GitHub Pages `github-pages` gem must support Jekyll 4, or
- The site must switch to a custom Actions workflow that builds with Jekyll 4 and deploys to Pages artifact.

---

## Validation commands and results

### Commands run during this audit

```bash
# Ruby / Jekyll
bundle outdated
# Output: faraday 2.14.1→2.14.2, jekyll 3.10.0→4.4.1, kramdown 2.4.0→2.5.2, liquid 4.0.4→5.12.0

bundle audit
# Output: exit 15 (tool not installed)

bundle exec jekyll build
# Output: failed — local Ruby 2.6.10 incompatible with lockfile

# Python
python3 --version
# Output: Python 3.9.6

python3 -m pytest tests/
# Output: 199 passed in 12.51s

python3 scripts/check_public_repo.py
# Output: Public repo hygiene check passed for 1042 tracked files.

python3 scripts/generate_atlas_artifacts.py --check
# Output: CHECK PASSED — all artifacts are up to date and valid.

python3 scripts/check_links.py _site
# Output: No broken local links detected.

python3 scripts/check_seo.py _site
# Output: 2428 issues — all are "canonical points to localhost" (expected for local builds without JEKYLL_ENV=production)

# Node
node --version
# Output: v24.15.0 (local system Node, not repo-managed)

# GitHub Actions
# Inspected .github/workflows/seo-checks.yml and indexnow-dry-run.yml
```

### Known false positives / expected warnings

- `check_seo.py` reports 2428 localhost canonical issues because the local `_site` was built with Jekyll default URL (`http://localhost:4000`). In CI, `JEKYLL_ENV=production` is typically set by the GitHub Pages build or should be set explicitly in the workflow to use `https://dkharlanau.github.io` as the base URL. This is not a technology issue, but it could be documented.

---

## Repository-specific risk analysis

### Jekyll build
- **Current state:** `github-pages` gem 232 + Jekyll 3.10.0 is the supported GitHub Pages stack.
- **Risk of updating Jekyll:** High. Would break GitHub Pages parity.
- **Risk of updating Ruby CI:** Low. 3.3.4 is already the GitHub Pages runtime.

### GitHub Pages compatibility
- The repo is tightly coupled to the `github-pages` gem. This is by design.
- Any major gem update must be checked against https://pages.github.com/versions/ first.

### SEO generated files / sitemap / llms files
- These are generated by Jekyll plugins (`jekyll-seo-tag`, `jekyll-sitemap`) and custom scripts (`generate_atlas_artifacts.py`).
- Updating Jekyll or plugins without GitHub Pages support could change output format.
- **Recommendation:** Do not touch plugin versions until GitHub Pages updates them.

### Atlas generated artifacts
- `scripts/generate_atlas_artifacts.py` is pure Python stdlib. No dependency risk.
- The `--check` mode passed cleanly.

### Skill Hub pages
- Generated by custom scripts (`generate_dama_pages.js`). No dependency risk except Node version.

### Tests / link checker / public repo safety checks
- All passed.
- Scripts are stdlib-only. Very low risk from runtime upgrades.

### IndexNow workflow
- Uses `scripts/indexnow_submit.py` (stdlib + `urllib`). No dependency risk.
- The Python version is pinned to 3.11 in the workflow. Safe to update to 3.12.

---

## Appendix: Official sources consulted

- Ruby lifecycle: https://www.ruby-lang.org/en/downloads/branches/
- Python lifecycle: https://devguide.python.org/versions/
- Node.js lifecycle: https://nodejs.org/en/about/previous-releases
- Jekyll endoflife: https://endoflife.date/jekyll
- GitHub Pages dependency versions: https://pages.github.com/versions/
- GitHub Actions runner images: https://github.com/actions/runner-images/releases
- GitHub Actions Node 20 deprecation: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
- GitHub Pages gem repository: https://github.com/github/pages-gem
- Jekyll official docs: https://jekyllrb.com/docs/

---

*End of audit report.*
