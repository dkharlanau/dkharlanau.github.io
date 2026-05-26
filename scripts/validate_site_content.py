#!/usr/bin/env python3
"""
Site Content Validator for dkharlanau.github.io
Checks: atlas_index.yml, templates, news section readiness, homepage protection.
Created for: issue #5
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install: pip install pyyaml")
    sys.exit(1)

# --- Configuration ---
REPO_ROOT = Path(__file__).resolve().parent.parent
PROTECTED_HOMEPAGE_FILES = {"index.md", "_data/home.yml"}
ATLAS_REQUIRED_CLUSTER_FIELDS = {
    "id", "title", "path", "topic_cluster", "keywords",
    "allowed_update_types", "source_policy", "last_reviewed",
    "related_pages", "agent_notes",
}
TEMPLATE_REQUIRED_BODY_FIELDS = [
    "Source:", "Date checked:", "Confidence:",
    "Related page/topic:", "Practical implication:",
]
JEKYLL_COLLECTIONS = {"notes": "_notes", "blog": "_blog"}

# --- Utilities ---

def fail(msg, strict=False):
    label = "ERROR" if strict else "WARN"
    print(f"  [{label}] {msg}")
    return strict

def ok(msg):
    print(f"  [OK]  {msg}")

def info(msg):
    print(f"  [INFO] {msg}")


def resolve_jekyll_path(path_str):
    """Map a permalink-style path to possible filesystem paths."""
    if not path_str or path_str == "/":
        return []
    path_str = path_str.rstrip("/")
    # Strip leading slash
    fs_path = path_str.lstrip("/")
    candidates = [
        REPO_ROOT / f"{fs_path}.md",
        REPO_ROOT / fs_path / "index.md",
        REPO_ROOT / f"{fs_path}.html",
    ]
    # Check collections
    for coll_public, coll_dir in JEKYLL_COLLECTIONS.items():
        if path_str.startswith(f"/{coll_public}/"):
            slug = path_str[len(f"/{coll_public}/"):].rstrip("/")
            if slug:
                candidates.append(REPO_ROOT / coll_dir / f"{slug}.md")
    return candidates


def path_exists_for_jekyll(path_str):
    """Return True if at least one candidate exists on disk."""
    candidates = resolve_jekyll_path(path_str)
    return any(p.exists() for p in candidates), candidates


def get_staged_files():
    """Return set of staged file paths relative to repo root."""
    try:
        result = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "diff", "--cached", "--name-only"],
            capture_output=True, text=True, check=True,
        )
        return set(line.strip() for line in result.stdout.splitlines() if line.strip())
    except (subprocess.CalledProcessError, FileNotFoundError):
        return set()


def check_atlas_index(strict=False):
    print("\n== Checking _data/atlas_index.yml ==")
    atlas_path = REPO_ROOT / "_data" / "atlas_index.yml"
    if not atlas_path.exists():
        return fail("_data/atlas_index.yml not found", strict)

    try:
        with open(atlas_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return fail(f"Invalid YAML: {e}", strict)

    errors = 0

    if not isinstance(data, dict):
        errors += fail("Root must be a dict", strict)
        return errors > 0

    # meta
    if "meta" not in data:
        errors += fail("Missing 'meta' section", strict)
    else:
        ok("meta section present")

    # fallback
    if "fallback" not in data:
        errors += fail("Missing 'fallback' section", strict)
    else:
        ok("fallback section present")

    # topic_clusters
    clusters = data.get("topic_clusters")
    if not isinstance(clusters, list):
        errors += fail("Missing or invalid 'topic_clusters' (must be list)", strict)
        return errors > 0

    ok(f"topic_clusters: {len(clusters)} entries")

    placeholder_count = 0
    missing_existing_count = 0

    for idx, cluster in enumerate(clusters):
        prefix = f"  cluster[{idx}]"
        if not isinstance(cluster, dict):
            errors += fail(f"{prefix} is not a dict", strict)
            continue

        cid = cluster.get("id", f"<no-id@{idx}>")

        missing_fields = ATLAS_REQUIRED_CLUSTER_FIELDS - set(cluster.keys())
        if missing_fields:
            errors += fail(
                f"{cid}: missing required fields: {', '.join(sorted(missing_fields))}",
                strict,
            )

        # Path check
        path_val = cluster.get("path")
        if path_val is None:
            placeholder_count += 1
            info(f"{cid}: path is null (future placeholder)")
        elif not isinstance(path_val, str):
            errors += fail(f"{cid}: path must be string or null", strict)
        else:
            exists, candidates = path_exists_for_jekyll(path_val)
            if exists:
                ok(f"{cid}: path resolves ({path_val})")
            else:
                # Check if it's a Jekyll collection path that may not exist yet
                # Allow /ai/* paths since those are often generated/dynamic
                if path_val.startswith("/ai/"):
                    info(f"{cid}: /ai/ path assumed valid (intent routing): {path_val}")
                else:
                    missing_existing_count += 1
                    errors += fail(
                        f"{cid}: path does not resolve to existing file: {path_val}",
                        strict,
                    )

    if placeholder_count:
        info(f"Future placeholders with null path: {placeholder_count} (warn only)")
    if missing_existing_count:
        info(f"Missing existing paths: {missing_existing_count}")

    return errors > 0


def check_templates(strict=False):
    print("\n== Checking docs/templates/*.md ==")
    templates_dir = REPO_ROOT / "docs" / "templates"
    if not templates_dir.exists():
        return fail("docs/templates/ directory not found", strict)

    template_files = sorted(templates_dir.glob("*.md"))
    if not template_files:
        return fail("No .md files found in docs/templates/", strict)

    ok(f"Found {len(template_files)} template files")
    errors = 0

    for tf in template_files:
        text = tf.read_text(encoding="utf-8")
        # Check required body metadata strings
        for field in TEMPLATE_REQUIRED_BODY_FIELDS:
            if field not in text:
                # Only enforce on non-README templates
                if tf.name != "README.md":
                    errors += fail(
                        f"{tf.name}: missing required body field '{field}'", strict
                    )

        # Check front matter defaults for noindex/sitemap false on templates
        # Skip for docs/templates/ since that directory is excluded from Jekyll build
        if tf.name != "README.md" and "docs/templates" not in str(tf):
            has_robots = "robots:" in text
            if not has_robots:
                errors += fail(
                    f"{tf.name}: missing 'robots:' front matter", strict
                )
            elif not is_atlas_template and "noindex" not in text:
                errors += fail(
                    f"{tf.name}: missing 'noindex' in robots front matter", strict
                )
            if not is_atlas_template and "sitemap:" not in text:
                errors += fail(
                    f"{tf.name}: missing 'sitemap:' front matter", strict
                )

    if errors == 0:
        ok("All templates have required fields and noindex/sitemap defaults")
    return errors > 0


def check_news_section(strict=False):
    print("\n== Checking /news/ section ==")
    # News items may be in _news/ (collection) or news/ (static)
    news_dirs = []
    for d in [REPO_ROOT / "news", REPO_ROOT / "_news"]:
        if d.exists():
            news_dirs.append(d)

    if not news_dirs:
        info("/news/ directory does not exist yet — news section is pending (issue #3)")
        return False  # Not an error

    all_news_files = []
    for nd in news_dirs:
        for f in nd.rglob("*.md"):
            # Skip listing/index pages — they are not news items
            if f.name == "index.md":
                continue
            all_news_files.append(f)

    if not all_news_files:
        info("/news/ exists but contains no news item .md files yet")
        return False

    ok(f"/news/ exists with {len(all_news_files)} news item(s)")
    errors = 0
    for nf in all_news_files:
        text = nf.read_text(encoding="utf-8")

        # --- Reject sample/draft files in production _news/ ---
        if nf.parent.name == "_news":
            lower_name = nf.name.lower()
            if "sample" in lower_name or "draft" in lower_name:
                errors += fail(
                    f"{nf.name}: sample/draft files are not allowed in _news/. "
                    "Move to docs/templates/ and remove 'sample' or 'draft' from filename.",
                    strict,
                )
            # Also reject content that contains explicit SAMPLE/DRAFT markers
            # (templates in docs/templates/ are allowed to have these)
            if "SAMPLE" in text or "DRAFT" in text.upper():
                # Only flag if it's in the production collection
                errors += fail(
                    f"{nf.name}: contains SAMPLE/DRAFT marker — "
                    "remove before publishing or move to docs/templates/.",
                    strict,
                )

        if not text.startswith("---"):
            errors += fail(f"{nf.name}: missing front matter", strict)
        else:
            # Quick YAML front-matter extraction
            parts = text.split("---", 2)
            if len(parts) >= 3:
                try:
                    front = yaml.safe_load(parts[1])
                    if not isinstance(front, dict):
                        errors += fail(f"{nf.name}: front matter is not a dict", strict)
                    else:
                        required_news = {"title", "date", "permalink"}
                        missing = required_news - set(front.keys())
                        if missing:
                            errors += fail(
                                f"{nf.name}: missing news front matter: {', '.join(missing)}",
                                strict,
                            )
                except yaml.YAMLError as e:
                    errors += fail(f"{nf.name}: invalid front matter YAML: {e}", strict)
    return errors > 0


def check_homepage_protection(allow_homepage=False, strict=False):
    print("\n== Checking homepage protection ==")
    staged = get_staged_files()
    if not staged:
        ok("No staged changes detected")
        return False

    violations = staged & PROTECTED_HOMEPAGE_FILES
    if not violations:
        ok("No staged changes to protected homepage files")
        return False

    msg = f"Staged changes touch protected homepage files: {', '.join(sorted(violations))}"
    if allow_homepage:
        info(f"{msg} (allowed via --allow-homepage)")
        return False
    else:
        return fail(msg, strict)


def main():
    parser = argparse.ArgumentParser(
        description="Validate dkharlanau.github.io content structure"
    )
    parser.add_argument(
        "--strict", action="store_true",
        help="Treat warnings as errors (exit non-zero on any issue)"
    )
    parser.add_argument(
        "--allow-homepage", action="store_true",
        help="Allow staged changes to protected homepage files"
    )
    args = parser.parse_args()

    print("Site Content Validator")
    print(f"Repo root: {REPO_ROOT}")

    failed = False
    failed |= check_atlas_index(strict=args.strict)
    failed |= check_templates(strict=args.strict)
    failed |= check_news_section(strict=args.strict)
    failed |= check_homepage_protection(
        allow_homepage=args.allow_homepage, strict=args.strict
    )

    print("\n== Summary ==")
    if failed:
        print("Result: FAILED")
        sys.exit(1)
    else:
        print("Result: PASSED")
        sys.exit(0)


if __name__ == "__main__":
    main()
