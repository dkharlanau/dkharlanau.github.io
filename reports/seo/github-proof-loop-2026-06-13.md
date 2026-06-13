# GitHub Repository Proof Audit — SEO Visibility Swarm

**Date:** 2026-06-13  
**Branch:** `feat/seo-visibility-swarm`  
**Repo:** https://github.com/dkharlanau/dkharlanau.github.io  
**Site:** https://dkharlanau.github.io  
**Owner:** Dzmitryi Kharlanau  

---

## 1. README.md Audit

**File:** `README.md` (67 lines)  
**Status:** Exists and covers basics, but has gaps for SEO/repo-proof purposes.

### Checklist

| Requirement | Present? | Evidence / Notes |
|-------------|----------|------------------|
| **What the site is** | ✅ Yes | “This is my public professional website and profile repository.” Also explains it as a “canonical public profile that I can control, structure, reference, and keep machine-readable.” |
| **Who built it** | ✅ Yes | “Dzmitryi Kharlanau, a Senior SAP Consultant…” with domains and background. |
| **Live URL** | ⚠️ Partial | The URL is implied (“machine-readable for search engines and AI systems”) but **not explicitly stated** as a clickable live URL. No `https://dkharlanau.github.io` string appears. |
| **Main sections** | ❌ Missing | No mention of Atlas, Scenarios, Skill Hub, Research, Datasets, AI endpoints, or Services. A reader cannot infer the site structure from the README. |
| **Public-safe status** | ✅ Yes | Clear independence disclaimer: “This is not an official employer, vendor, or client website.” Also: “The views and materials on this site are personal and independent.” |
| **How it’s generated** | ❌ Missing | No mention of Jekyll, GitHub Pages, `bundle exec jekyll build`, or the build system. |
| **Validation commands** | ❌ Missing | No mention of `pytest`, `check_links.py`, `check_seo.py`, `check_public_repo.py`, or `bundle exec jekyll build`. |
| **License / openness** | ⚠️ Partial | Repository is public, but no explicit LICENSE file is referenced in the README. (There is a `LICENSE` file in the repo, per `_config.yml` exclude list.) |
| **AI-readable endpoints** | ✅ Yes | Mentions `llms.txt`, `resume.json`, `resume.yml`. |
| **Contact / networking** | ✅ Yes | LinkedIn link provided. |

### README Strengths
- Tone is honest and conservative (no exaggerated claims).
- Explains the *why* (LinkedIn is not enough).
- Lists focus areas clearly.
- Warns about independence and employer separation.

### README Gaps (Ranked by Impact)
1. **No explicit live URL.** GitHub surfaces README content in search snippets. Missing `https://dkharlanau.github.io` reduces direct discovery.
2. **No site architecture summary.** The README should act as a human-readable map. A maintainer or recruiter should see the major sections at a glance.
3. **No build/validation instructions.** Contributors (and future agents) need to know how to test changes.
4. **No verification policy mention.** The site has a strict three-level verification system. The README does not signal this quality control to readers.
5. **No sitemap/robots.txt mention.** The site has an unusually thorough `robots.txt` and sitemap architecture. This is a positive signal that should be visible.

---

## 2. CNAME Audit

**File:** `CNAME`  
**Status:** **Missing.**  

**Impact:** The site uses the default GitHub Pages subdomain (`dkharlanau.github.io`). No custom domain is configured. This is acceptable for a personal site, but it means:
- No apex-domain redirect options.
- GitHub Pages serves from `https://dkharlanau.github.io` directly.
- No DNS-level verification possible.

**Recommendation:** Not a blocker. If a custom domain is desired later, add `CNAME` at that time. Document the current state in README.

---

## 3. Social Preview Image Audit

**Files:** `assets/og/default.png` (22,498 bytes), `assets/og/default.webp` (14,618 bytes)  
**Status:** ✅ Present.  

**Properties:**
- Format: PNG and WebP variants
- Size: ~22KB PNG, ~15KB WebP
- Dimensions: Not measured in this audit; recommend confirming 1200×630 for optimal LinkedIn/Twitter preview
- Usage: Referenced by `_includes/seo/og.html` or similar template (assumed; not audited in this pass)

**Risk:** Low. The image exists and is small enough for fast load. If dimensions are not 1200×630, update the template to use the correct aspect ratio or regenerate.

**Recommendation:** Verify dimensions are 1200×630. If not, add a generation note in `AGENTS.md` or `DESIGN-SYSTEM.md`.

---

## 4. `.well-known/` Audit

**Directory:** `.well-known/`  
**Status:** ✅ Present and populated.  

**Contents:**
- `.well-known/agent-skills/dataset-discovery.md` — Dataset discovery instructions for AI agents
- `.well-known/agent-skills/index.json` — Machine-readable index of agent skills
- `.well-known/agent-skills/resume-lookup.md` — Resume lookup instructions
- `.well-known/agent-skills/topic-routing.md` — Topic routing for AI agents

**Assessment:** This is a strong signal. The `.well-known/` directory is the modern equivalent of `robots.txt` for AI agents. It shows the owner is actively designing for machine retrieval, not just human SEO.

**Gaps:**
- No `security.txt` (optional, but good for trust signals).
- No `ai.txt` or `llms.txt` here (these are at root, which is fine).
- No `humans.txt` (nostalgic, not critical).

**Recommendation:** Keep `.well-known/agent-skills/` maintained. Add a note in README that the site supports AI agent discovery via `.well-known/`.

---

## 5. `robots.txt` Audit

**File:** `robots.txt` (64 lines)  
**Status:** ✅ **Excellent.** One of the strongest signals in the repo.

**Strengths:**
- **Sitemap references:** Points to `sitemap.xml`, `sitemap-pages.xml`, `sitemap-data.xml`, `sitemap-atlas.xml`. Multi-layer sitemap architecture is rare and signals maturity.
- **AI crawler policy:** Explicit, documented choices for `OAI-SearchBot`, `ChatGPT-User`, `GPTBot`, `Claude-SearchBot`, `Claude-User`, `ClaudeBot`, `Google-Extended`, `PerplexityBot`, `CCBot`, `FacebookBot`. Each is justified with a comment.
- **Content-Signal:** `ai-train=no, search=yes, ai-input=yes`. This is a forward-looking directive that signals intent to crawlers.
- **Disallow rules:** Clear blocking of legacy duplicate paths (`/DAMA/`, `/agentic-bytes/`, `/TRIZ-bytes/`, `/LLM-prompts/`).

**Gaps:**
- **No `Crawl-delay`.** Not needed for a small site, but worth noting.
- **No `Host` directive.** Not standard, but some Russian search engines use it.
- **No `Clean-param`.** Not applicable here.
- **Disallow list may need updating.** If new root duplicate folders are created, they must be added here. The README does not mention this requirement.

**Risk:** None. `robots.txt` is a net positive and should be highlighted in the README as a trust signal.

---

## 6. Sitemap Architecture Audit

**Files:**
- `sitemap.xml` (index, 403 bytes) — references the section sitemaps
- `sitemap-pages.xml` (Jekyll template, 4139 bytes) — generated; excludes `noindex`, research, and unverified Atlas pages
- `sitemap-data.xml` (2404 bytes) — dataset references
- `sitemap-atlas.xml` (2142 bytes) — Atlas page references

**Status:** ✅ **Strong.** The template logic in `sitemap-pages.xml` is rigorous:
- Excludes `noindex` pages (`robots` contains `noindex`).
- Excludes `research/` pages entirely (`is_research`).
- Excludes unverified Atlas pages (`is_atlas` + `verified != true` + `status != 'reviewed'`).

**Gap:** Root-level hub pages (e.g., `/sap-ams-diagnostics/`) are not Atlas or Research, so they will be included if `sitemap != false`. However, they must have `verified: true` and `status: reviewed` to avoid being filtered by other logic. The template checks `atlas_verified` and `atlas_status` only for `is_atlas` paths, so root-level hubs are safe as long as they are not explicitly `noindex`.

**Recommendation:** Document the sitemap logic in README or ARCHITECTURE.md so external contributors understand why their new Atlas page does not appear in search results.

---

## 7. Repository Topics (Recommendations)

GitHub repository topics are set via the GitHub UI, not from files. These are the recommended topics to add to `https://github.com/dkharlanau/dkharlanau.github.io`:

**Primary (SAP domain):**
- `sap`
- `sap-ams`
- `sap-s4hana`
- `sap-sd`
- `sap-mm`
- `sap-mdg`
- `sap-bp`
- `sap-cvi`
- `sap-idoc`
- `sap-integration`

**Secondary (AI and automation):**
- `ai-assisted-support`
- `sap-automation`
- `sidecar-ai`
- `enterprise-ai`
- `knowledge-management`

**Tertiary (methodology and site type):**
- `jekyll`
- `github-pages`
- `personal-website`
- `technical-writing`
- `knowledge-atlas`
- `skill-hub`
- `consulting`

**Topics to avoid:**
- `hacktoberfest` (not a community project)
- `tutorial` (not a tutorial repo)
- `course` (not educational content)
- Any client or employer name (privacy rule)

**Rationale:** Topics improve GitHub search discoverability and signal to profile visitors what the repo contains. The current repo has no visible topics in the GitHub UI (not audited here, but assumed based on the fact that they are not set in files). Add 5–10 of the above.

---

## 8. Suggested README Edits (Exact Text)

**Do not apply these edits without human review.** They are provided as a precise patch for the parent agent or owner.

### Edit 1: Add explicit Live URL and site structure after the opening paragraph

**Location:** After line 5 (the “Why this site exists” paragraph).  
**Insert:**

```markdown
## Live site

- **URL:** https://dkharlanau.github.io
- **Generated with:** Jekyll + GitHub Pages
- **Sitemap:** https://dkharlanau.github.io/sitemap.xml
- **robots.txt:** https://dkharlanau.github.io/robots.txt
```

### Edit 2: Add site structure section after “What this site is about”

**Location:** After the “What this site is about” list (after line 43).  
**Insert:**

```markdown
## Site structure

- **Home** — Positioning and trust signals
- **About / Profile** — Canonical human-readable and machine-readable profile
- **Services** — Consulting engagement model (diagnose, stabilize, structure, extend)
- **Knowledge Atlas** — Curated SAP diagnostics, concepts, and process maps
- **Scenarios** — Business-pain-to-diagnostic-workflow mappings
- **Skill Hub** — Practical working skills for enterprise consultants and AI agents
- **Research / Radar** — Signal tracking and source-backed briefs
- **Datasets** — Canonical machine-readable dataset collections
- **AI endpoints** — `llms.txt`, `resume.json`, `resume.yml`, and agent-skill discovery via `.well-known/`
```

### Edit 3: Add validation and build commands after “What this repository contains”

**Location:** After the “What this repository contains” list (after line 53).  
**Insert:**

```markdown
## Build and validation

```sh
# Local preview
bundle exec jekyll serve

# Full validation sequence (run before publishing)
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests
python3 scripts/check_public_repo.py
bundle exec jekyll build
python3 scripts/check_links.py _site
python3 scripts/check_seo.py _site
```

All committed content is public. The repository uses a three-level verification system for content quality and indexing control.
```

### Edit 4: Add AI and SEO transparency note at the end

**Location:** After the “Independence” section (after line 66).  
**Insert:**

```markdown
## AI and search transparency

This site is designed to be machine-readable for search engines and AI retrieval systems. It includes:

- A detailed `robots.txt` with per-crawler policies and sitemap references
- Section-level sitemaps (`sitemap-atlas.xml`, `sitemap-data.xml`, `sitemap-pages.xml`)
- AI-readable files (`llms.txt`, `resume.json`, `resume.yml`)
- `.well-known/agent-skills/` for AI agent discovery and topic routing
```

---

## 9. Verification / Safety Checklist

- [ ] README updated with live URL and site structure (human review required)
- [ ] README updated with build/validation commands
- [ ] README updated with AI transparency note
- [ ] GitHub repo topics added (5–10 topics from recommendations)
- [ ] Social preview image dimensions verified as 1200×630
- [ ] `.well-known/` maintained and documented in README
- [ ] `robots.txt` kept in sync with any new root-level duplicate paths
- [ ] `CNAME` added only if custom domain is purchased later
- [ ] No private paths exposed in README or repo files
- [ ] No client names, ticket numbers, or proprietary details mentioned

---

## 10. Summary Score

| Surface | Score | Notes |
|---------|-------|-------|
| README completeness | 6/10 | Good tone and identity, missing structure and URL |
| CNAME | N/A | Not needed for GitHub Pages subdomain |
| Social preview | 8/10 | Exists, verify dimensions |
| `.well-known/` | 9/10 | Strong AI-agent discovery signal |
| `robots.txt` | 10/10 | Best-in-class for a personal site |
| Sitemap architecture | 9/10 | Rigorous exclusion logic, well-structured |
| Repo topics | 0/10 | Cannot be set from files; must be done in GitHub UI |
| Overall repo proof | 7/10 | Excellent technical signals, weak human-readable summary |

**Bottom line:** The repo’s *machine-readable* proof surfaces (`robots.txt`, sitemaps, `.well-known/`) are excellent. The *human-readable* proof surface (README) is underwhelming. Fixing the README is the highest-impact, lowest-effort action in this audit.
