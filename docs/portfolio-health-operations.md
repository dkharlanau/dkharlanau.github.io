---
layout: default
title: "Public portfolio health and private traffic operations"
description: "A two-week operating procedure for checking the public repository portfolio while keeping GitHub traffic evidence private."
permalink: /docs/portfolio-health-operations/
robots: noindex,follow
sitemap: false
---

# Public portfolio health and private traffic operations

Use this procedure every two weeks to answer two different questions:

1. Is the public repository portfolio published cleanly and consistently?
2. Is private GitHub traffic evidence changing enough to influence the next maintenance cycle?

The two evidence sets stay separate. Portfolio health uses public metadata and may be shared after review. Traffic snapshots contain repository analytics and must remain local.

## Prerequisites

- Run from the root of the `dkharlanau.github.io` checkout.
- Install the GitHub CLI and authenticate it as a user who can read Traffic API data for the repositories.
- Treat `products/manifest.json` as the repository inventory. Keep `config/portfolio-health.json` limited to verification-policy overlays and required contract edges.
- Keep `.local/portfolio-traffic/` ignored. Never override the traffic command to write into a tracked or external directory.

Confirm the local boundary before the first run:

```sh
gh auth status --hostname github.com
git check-ignore --no-index .local/portfolio-traffic/.ignore-probe
```

The authentication command may show account details in your terminal. Do not copy that output into a report, issue, or commit.

## Step 1: capture public portfolio health

Run the read-only public check. The two checkout roots allow the command to compare available local `main` checkouts with their published GitHub SHA without fetching or changing them.

```sh
python3 scripts/portfolio_health.py \
  --checkouts-root ../dkharlanau-public \
  --checkouts-root .. \
  --strict
```

The command writes `portfolio-health.json` and `portfolio-health.md` under the ignored `reports/portfolio-health/` directory. The report is intentionally bounded to:

- public repository metadata and default-branch state;
- the exact published `main` SHA and workflows found for that SHA;
- the remote branch inventory;
- live GitHub Pages or configured documentation endpoints;
- the exact final README author footer;
- release and tag presence;
- expected cross-project contract links; and
- optional local booleans for clean worktree, `main`, and equality with the published SHA.

It does not contain GitHub traffic, credentials, API error bodies, or local checkout paths. Review the report before sharing it; public-safe does not mean automatically publication-worthy.

If `--strict` exits with status 1, use the finding codes as a maintenance queue. Do not weaken a check to make the summary green.

## Step 2: capture private traffic evidence

Run the authenticated snapshot separately:

```sh
python3 scripts/github_traffic_snapshot.py
```

The command queries repository views, clones, top referrers, and popular paths. It creates timestamped JSON and Markdown files below `.local/portfolio-traffic/`, restricts directory permissions to the current user, and does not retain raw API responses or error bodies. URL-shaped referrers are reduced to hostnames; popular-path query strings and fragments are removed.

GitHub Traffic API data covers a rolling window of up to 14 days. Run on a stable fortnightly cadence if comparisons matter. A missed window cannot be reconstructed by this tool.

Before closing the run, verify that the evidence is still ignored and untracked:

```sh
git check-ignore --no-index .local/portfolio-traffic/.ignore-probe
test -z "$(git ls-files -- .local/portfolio-traffic)"
git status --short
```

Never copy traffic counts, referrers, popular paths, or traffic snapshot files into the public health report, a commit, a public issue, or a Pages artifact.

## Step 3: compare and decide

Compare the new private snapshot with the previous local snapshot, then choose a small, evidence-backed maintenance slice.

- Treat views and clones as directional signals, not complete analytics.
- Check whether a referrer or popular path repeats across two windows before making a large documentation change.
- Use public health failures as release blockers when they concern branch state, published SHA, broken docs, footer drift, or required handoff links.
- Treat missing releases or tags as context unless the repository has an explicit release contract.
- Record decisions separately from raw traffic. A public maintenance note may state the chosen change without exposing private counts or paths.

## Remediation order

| Finding | First response |
|---|---|
| Default branch or remote branches are wrong | Inspect remote state and ancestry; do not delete a branch without proving it merged or is patch-equivalent. |
| Local checkout does not match published `main` | Fetch read-only, inspect divergence and uncommitted work, then use the repository's safe publication process. |
| Published-SHA CI fails | Read the failing run, reproduce the smallest relevant check, and fix the underlying defect. |
| Pages or documentation is unavailable | Confirm the configured project-site path, the Pages deployment, and live HTTP response. |
| Author footer differs | Restore the exact final footer from `config/portfolio-health.json`. |
| Contract links are missing | Add truthful links that explain the actual producer-consumer or handoff relationship. |
| Traffic endpoint is unavailable | Confirm ownership/authentication and retry later; do not substitute scraped or guessed analytics. |

## Scheduling boundary

`.github/workflows/portfolio-health.yml` runs the public-safe health check weekly and also supports manual dispatch. It has read-only repository and Actions permissions, never commits a report, and retains its report artifact for seven days.

The private traffic command is deliberately absent from GitHub Actions. Its two-week heartbeat is configured outside this repository and may invoke the snapshot locally on a trusted host. Authentication remains in that host's GitHub CLI session; no traffic credential is stored in this repository. The external run must keep output in the ignored private directory, keep notifications free of traffic values, and never auto-commit health or traffic artifacts.
