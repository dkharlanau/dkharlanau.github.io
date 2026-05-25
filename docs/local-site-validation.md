# Local Site Validation

Status: operational  
Purpose: document how to set up Ruby/Jekyll locally and validate the site build  
Created for: issue #7  
Last updated: 2026-05-26

---

## Ruby version

The site uses the `github-pages` gem, which pins Jekyll and dependencies to the versions GitHub Pages runs in production.

Current production versions (from [pages.github.com/versions](https://pages.github.com/versions)):

| Component | Version |
|---|---|
| Ruby | 3.3.4 |
| Jekyll | 3.10.0 |
| github-pages gem | 232 |

The `.ruby-version` file at repo root contains `3.3.4`.

---

## Setup

### macOS (Homebrew)

```bash
brew install ruby@3.3
export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"
```

### macOS (rbenv)

```bash
rbenv install -s 3.3.4
rbenv local 3.3.4
```

### Linux (apt)

```bash
# Install Ruby 3.3 via your distribution's package manager or rbenv
rbenv install -s 3.3.4
rbenv local 3.3.4
```

### Install dependencies

```bash
# Use bin/setup (reads .ruby-version, installs matching bundler, runs bundle install)
bin/setup

# Or manually:
gem install bundler -v '2.5.22'
bundle _2.5.22_ install
```

---

## Build

```bash
bundle exec jekyll build
```

Output goes to `_site/`.

To serve locally:

```bash
bundle exec jekyll serve
```

---

## Validation pipeline

Run these in order:

### 1. Content validation (no Ruby required)

```bash
python3 scripts/validate_site_content.py
```

Checks:
- `_data/atlas_index.yml` structure and path resolution
- `docs/templates/*.md` required fields
- `/news/` section front matter
- Homepage file protection (staged-change detection)

```bash
python3 scripts/validate_site_content.py --strict
```

Treats all warnings as errors (CI-friendly).

### 2. Syntax check (CI-friendly)

```bash
python3 -m py_compile scripts/validate_site_content.py
```

### 3. Build validation (requires Ruby)

```bash
bundle exec jekyll build
```

### 4. Link check (requires built site)

```bash
python3 scripts/check_links.py _site
```

Checks for broken internal links in the built HTML.

### 5. SEO check (requires built site)

```bash
python3 scripts/check_seo.py _site
```

Checks for:
- Missing `<title>` or meta description
- Missing or malformed canonical links
- Missing or malformed `og:url`
- Canonical / `og:url` mismatches
- Localhost URLs in canonical/og:url

---

## When Ruby is not available

If you are running in an environment without Ruby (e.g., a lightweight agent sandbox), you can still run the Python validator:

```bash
python3 scripts/validate_site_content.py
```

Jekyll build validation (`bundle exec jekyll build`) and post-build checks (`check_links.py`, `check_seo.py`) cannot run without Ruby. Document this in any closeout report:

> Ruby/Jekyll unavailable in this environment. Build validation remains pending and should be run locally before publishing.

---

## Files

| File | Purpose |
|---|---|
| `.ruby-version` | Pin Ruby to 3.3.4 (matches GitHub Pages production) |
| `Gemfile` | Declare `github-pages` gem dependency |
| `Gemfile.lock` | Lock dependency versions (includes `jekyll 3.10.0`) |
| `bin/setup` | Automated setup script (reads `.ruby-version`, installs bundler, runs `bundle install`) |
| `scripts/validate_site_content.py` | Pre-build content validation (issue #5) |
| `scripts/check_links.py` | Post-build broken link detection |
| `scripts/check_seo.py` | Post-build SEO metadata validation |
| `docs/local-site-validation.md` | This documentation |

---

## Notes

- Do not upgrade `github-pages` or `jekyll` unless GitHub Pages itself upgrades. The gem exists to keep local builds in sync with production.
- `Gemfile.lock` is tracked in git to ensure consistent dependency versions across environments.
- `webrick` is listed in `Gemfile` because Ruby 3.x no longer bundles it, and Jekyll 3.x requires it.
- `faraday-retry` is listed because newer `faraday` versions need it explicitly.
