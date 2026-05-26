## Closeout Report — dkharlanau.github.io Issue #10

### Result
Completed

### Problem
GitHub Actions workflows emitted Node.js 20 deprecation warnings for:
- `actions/checkout@v4`
- `actions/setup-node@v4`

Timeline:
- June 2, 2026 — Actions forced to Node.js 24 by default
- September 16, 2026 — Node.js 20 removed from runners

### Files Changed

| File | Change |
|---|---|
| `.github/workflows/seo-checks.yml` | Added `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true` at job level |
| `.github/workflows/indexnow.yml` | Added `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true` at job level |

### Why not bump action versions?

`actions/checkout@v4` and `actions/setup-node@v4` are the latest major versions available. No v5 exists yet with native Node 24 support. The minimal safe fix is to opt into Node 24 early via the environment variable GitHub explicitly recommends.

### Validation

| Check | Result |
|---|---|
| `validate_site_content.py` | **PASSED** |
| SEO Checks run 26466411124 | **PASSED** (28s) |
| Link check | No broken links |
| SEO metadata check | 280 HTML files passed |

**Run URL:** https://github.com/dkharlanau/dkharlanau.github.io/actions/runs/26466411124

### Remaining warnings

One informational annotation remains:

> Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-node@v4.

This is expected — it confirms the opt-in is working. The old scarier warning ("may not work as expected") is gone.

This remaining notice will disappear when:
1. GitHub releases v5 of these actions with native Node 24, **or**
2. June 2, 2026 when Node 24 becomes the default runner behavior

### Safety checks

- No homepage changes
- No Jekyll content changes
- No site behavior changes
- No unrelated dependencies upgraded
- Workflow steps identical, only env var added

### Commit
`6ec7064` — `ci: opt into Node 24 for GitHub Actions to remove deprecation warnings`
