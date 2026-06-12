#!/usr/bin/env python3
"""Submit indexable canonical URLs to IndexNow.

Usage:
    INDEXNOW_KEY=your-key python3 scripts/indexnow_submit.py --submit
    INDEXNOW_KEY=your-key python3 scripts/indexnow_submit.py --urls /about/ /services/
    python3 scripts/indexnow_submit.py --from-git-diff HEAD~1 HEAD
    python3 scripts/indexnow_submit.py --all --max-urls 50

Rules:
- Key must come from INDEXNOW_KEY env var, INDEXNOW_KEY_LOCATION file, or .env.local.
- Dry-run mode is the DEFAULT; pass --submit to actually submit.
- Only submits indexable canonical URLs (no noindex, no draft, no research).
- Never submits unverified Atlas or research pages.
- Final URL list is intersected with the generated _site sitemap.
- Skipped paths and submission results are written to a JSON report.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


BASE_URL = "https://dkharlanau.github.io"
INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"
REPO_ROOT = Path(__file__).resolve().parent.parent
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"

CORE_URLS = {
    f"{BASE_URL}/",
    f"{BASE_URL}/about/",
    f"{BASE_URL}/ai/",
    f"{BASE_URL}/services/",
    f"{BASE_URL}/datasets/",
    f"{BASE_URL}/notes/",
    f"{BASE_URL}/blog/",
    f"{BASE_URL}/atlas/",
    f"{BASE_URL}/robots.txt",
    f"{BASE_URL}/llms.txt",
    f"{BASE_URL}/LLM.txt",
    f"{BASE_URL}/sitemap.xml",
    f"{BASE_URL}/sitemap-pages.xml",
    f"{BASE_URL}/sitemap-data.xml",
    f"{BASE_URL}/sitemap-atlas.xml",
}

# Paths that are never public
PRIVATE_PREFIXES = (
    "vendor/",
    ".git/",
    "_site/",
    "scripts/",
    "tests/",
    "docs/templates/",
    "docs/maintenance/",
    "docs/research/",
    "Kimi_Agent_SAP Atlas Expansion/",
    "Basic_LinkedInDataExport_",
    ".env",
    ".bundle/",
    ".ruby-lsp/",
    ".pytest_cache/",
    ".githooks/",
    ".github/",
    ".codex/",
    ".agents/",
    "bin/",
    "_site/",
)

SHARED_LAYOUT_PATHS = (
    "assets/",
    "_data/",
    "_includes/",
    "_layouts/",
    "_config.yml",
    "sitemap.xml",
    "sitemap-pages.xml",
    "sitemap-data.xml",
    "sitemap-atlas.xml",
    "robots.txt",
)


def load_key() -> str:
    """Load IndexNow key from env, location file, or .env.local."""
    global _key_source
    key = os.environ.get("INDEXNOW_KEY", "").strip()
    if key:
        _key_source = "env"
        return key

    key_location = os.environ.get("INDEXNOW_KEY_LOCATION", "").strip()
    if key_location:
        key_path = Path(key_location)
        if key_path.exists():
            key = key_path.read_text(encoding="utf-8").strip().strip('"').strip("'")
            if key:
                _key_source = "location"
                return key

    env_local = REPO_ROOT / ".env.local"
    if env_local.exists():
        for line in env_local.read_text(encoding="utf-8").splitlines():
            if line.startswith("INDEXNOW_KEY="):
                _key_source = "file"
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    _key_source = ""
    return ""


# Module-level key source tracker (for testability)
_key_source: str = ""


def file_permalink(path: Path) -> str | None:
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return None
    for line in match.group(1).splitlines():
        if line.startswith("permalink:"):
            value = line.split(":", 1)[1].strip().strip('"').strip("'")
            if value:
                return value if value.startswith("/") else f"/{value}"
    return None


def _parse_frontmatter_bool(value: str) -> bool | None:
    v = value.lower()
    if v in ("true", "yes", "1"):
        return True
    if v in ("false", "no", "0"):
        return False
    return None


def check_indexable(path: str, abs_path: Path) -> tuple[bool, str | None]:
    """Return (is_indexable, skip_reason)."""
    if not abs_path.exists():
        return False, "file does not exist"
    text = abs_path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return True, None  # No frontmatter = assume indexable
    fm_text = match.group(1)
    robots = ""
    sitemap_val = ""
    verified = ""
    status = ""
    for line in fm_text.splitlines():
        if line.startswith("robots:"):
            robots = line.split(":", 1)[1].strip().strip('"').strip("'")
        elif line.startswith("sitemap:"):
            sitemap_val = line.split(":", 1)[1].strip().strip('"').strip("'")
        elif line.startswith("verified:"):
            verified = line.split(":", 1)[1].strip().strip('"').strip("'")
        elif line.startswith("status:"):
            status = line.split(":", 1)[1].strip().strip('"').strip("'")
    if "noindex" in robots:
        return False, f"robots:noindex ({robots})"
    sitemap_bool = _parse_frontmatter_bool(sitemap_val)
    if sitemap_bool is False:
        return False, "sitemap:false"
    if path.startswith("research/"):
        return False, "research path"
    if path.startswith("atlas/"):
        if verified != "true":
            return False, f"unverified Atlas (verified={verified})"
        if status != "reviewed":
            return False, f"unverified Atlas (status={status})"
    return True, None


def public_url_for_path(path: str) -> tuple[set[str], str | None]:
    """Return (urls, skip_reason) for a repo-relative path."""
    urls: set[str] = set()
    clean = path.strip()
    if not clean:
        return urls, "empty path"

    # Private/internal/local paths
    if clean.startswith(PRIVATE_PREFIXES):
        return urls, "private/internal path"

    abs_path = REPO_ROOT / clean

    # Static well-known files
    if clean in {"robots.txt", "llms.txt", "LLM.txt"}:
        urls.add(f"{BASE_URL}/{clean}")
        return urls, None

    if clean.startswith(".well-known/"):
        urls.add(f"{BASE_URL}/{clean}")
        return urls, None

    # Markdown pages
    if clean.endswith(".md"):
        indexable, reason = check_indexable(clean, abs_path)
        if not indexable:
            return urls, reason
        permalink = file_permalink(abs_path)
        if permalink:
            urls.add(f"{BASE_URL}{permalink}")
            return urls, None
        return urls, "no permalink in frontmatter"

    # Public data files
    if clean.startswith(("ai/", "datasets/", "atlas/")) and clean.endswith(
        (".json", ".yml", ".xml", ".txt")
    ):
        urls.add(f"{BASE_URL}/{clean}")
        return urls, None

    # Shared layout/includes/sitemap/robots changes → core URLs only
    if clean.startswith(SHARED_LAYOUT_PATHS) or clean == "_config.yml":
        urls.update(CORE_URLS)
        return urls, None

    return urls, "not a public path"


def discover_indexable_urls() -> tuple[set[str], dict[str, str]]:
    """Walk the repo and discover all indexable canonical URLs.

    Returns (urls, skipped_paths).
    """
    urls: set[str] = set()
    skipped: dict[str, str] = {}
    for root, dirs, files in os.walk(REPO_ROOT):
        # Skip non-public dirs
        dirs[:] = [
            d
            for d in dirs
            if d not in {
                "_site",
                ".git",
                "vendor",
                "node_modules",
                "Kimi_Agent_SAP Atlas Expansion",
                "scripts",
                "tests",
                ".bundle",
                ".ruby-lsp",
                ".pytest_cache",
                ".githooks",
                ".github",
                ".codex",
                ".agents",
                "bin",
            }
            and not d.startswith("Basic_LinkedInDataExport_")
        ]
        for f in files:
            if f.endswith(".md") or f.endswith((".json", ".yml", ".xml", ".txt")):
                rel = Path(root).relative_to(REPO_ROOT).as_posix()
                if rel == ".":
                    rel_path = f
                else:
                    rel_path = f"{rel}/{f}"
                found_urls, reason = public_url_for_path(rel_path)
                if reason:
                    skipped[rel_path] = reason
                urls.update(found_urls)
    return urls, skipped


def git_diff_files(base: str, head: str) -> list[str]:
    """Return list of changed file paths between two git refs."""
    try:
        output = subprocess.check_output(
            ["git", "diff", "--name-only", base, head],
            cwd=REPO_ROOT,
            text=True,
        ).strip()
    except subprocess.CalledProcessError as exc:
        print(f"ERROR: git diff failed: {exc}", file=sys.stderr)
        sys.exit(1)
    return [line for line in output.splitlines() if line]


def load_sitemap_urls(site_dir: Path) -> set[str]:
    """Parse all sitemap XML files under site_dir and return the set of loc URLs."""
    urls: set[str] = set()
    if not site_dir.exists():
        return urls

    sitemap_files = sorted(site_dir.glob("sitemap*.xml"))
    if not sitemap_files:
        return urls

    for sitemap_path in sitemap_files:
        try:
            tree = ET.parse(sitemap_path)
            root = tree.getroot()
        except ET.ParseError:
            continue

        tag = root.tag.split("}")[-1] if "}" in root.tag else root.tag
        if tag == "sitemapindex":
            for sitemap in root.findall(f"{{{SITEMAP_NS}}}sitemap"):
                loc = sitemap.find(f"{{{SITEMAP_NS}}}loc")
                if loc is None or not loc.text:
                    continue
                # Resolve relative loc against site_dir
                loc_text = loc.text.strip()
                loc_path = site_dir / Path(loc_text).name
                if loc_path.exists():
                    try:
                        sub_tree = ET.parse(loc_path)
                        sub_root = sub_tree.getroot()
                        for url in sub_root.findall(f"{{{SITEMAP_NS}}}url"):
                            url_loc = url.find(f"{{{SITEMAP_NS}}}loc")
                            if url_loc is not None and url_loc.text:
                                urls.add(url_loc.text.strip())
                    except ET.ParseError:
                        continue
        elif tag == "urlset":
            for url in root.findall(f"{{{SITEMAP_NS}}}url"):
                loc = url.find(f"{{{SITEMAP_NS}}}loc")
                if loc is not None and loc.text:
                    urls.add(loc.text.strip())
    return urls


def filter_urls_by_sitemap(
    urls: set[str], site_dir: Path
) -> tuple[set[str], dict[str, str]]:
    """Return (urls_in_sitemap, skipped_urls) where skipped URLs are not in sitemap."""
    sitemap_urls = load_sitemap_urls(site_dir)
    if not sitemap_urls:
        # If no sitemap is present, fail closed unless site_dir is missing.
        if not site_dir.exists():
            return set(), {u: "site directory missing" for u in urls}
        return set(), {u: "not_in_sitemap" for u in urls}

    in_sitemap: set[str] = set()
    skipped: dict[str, str] = {}
    for url in urls:
        if url in sitemap_urls:
            in_sitemap.add(url)
        else:
            skipped[url] = "not_in_sitemap"
    return in_sitemap, skipped


def _built_html_path_for_url(url: str, site_dir: Path) -> Path | None:
    """Map a canonical URL to the corresponding built HTML file in site_dir."""
    if not url.startswith(BASE_URL):
        return None
    rel = url[len(BASE_URL) :]
    if not rel or rel == "/":
        return site_dir / "index.html"
    candidate = site_dir / rel.lstrip("/")
    if candidate.is_dir():
        candidate = candidate / "index.html"
    elif not str(candidate).endswith(".html"):
        candidate = candidate.with_suffix(candidate.suffix + ".html")
    if candidate.exists():
        return candidate
    return None


def check_url_noindex_in_site(url: str, site_dir: Path) -> tuple[bool, str | None]:
    """Return (is_indexable, reason) by inspecting built HTML for noindex robots meta."""
    html_path = _built_html_path_for_url(url, site_dir)
    if html_path is None:
        return False, "built HTML not found"
    try:
        text = html_path.read_text(encoding="utf-8", errors="ignore")
    except OSError as exc:
        return False, f"cannot read built HTML: {exc}"
    match = re.search(
        r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'](.*?)["\']',
        text,
        re.IGNORECASE | re.DOTALL,
    )
    if match and "noindex" in match.group(1).lower():
        return False, "robots:noindex in built HTML"
    return True, None


def write_report(
    report_path: Path,
    mode: str,
    submitted: list[str],
    skipped: dict[str, str],
) -> None:
    report = {
        "mode": mode,
        "submitted": submitted,
        "skipped": [{"url": url, "reason": reason} for url, reason in sorted(skipped.items())],
        "summary": {
            "submitted_count": len(submitted),
            "skipped_count": len(skipped),
        },
    }
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")


def submit(urls: list[str], key: str, dry_run: bool) -> None:
    if dry_run:
        print("[DRY RUN] Would submit the following URLs to IndexNow:")
        for url in urls:
            print(f"  - {url}")
        return

    payload = {
        "host": "dkharlanau.github.io",
        "key": key,
        "keyLocation": f"{BASE_URL}/{key}.txt",
        "urlList": urls,
    }
    request = urllib.request.Request(
        INDEXNOW_ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read().decode("utf-8", errors="replace")
            print(f"IndexNow response: {response.status}")
            if body:
                print(body)
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        print(f"IndexNow HTTP error: {exc.code}\n{detail}", file=sys.stderr)
        raise


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--submit",
        action="store_true",
        help="Actually submit to IndexNow (default is dry-run)",
    )
    parser.add_argument(
        "--urls",
        nargs="*",
        help="Explicit relative paths or URLs to submit",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Submit all indexable URLs discovered in repo",
    )
    parser.add_argument(
        "--from-git-diff",
        nargs=2,
        metavar=("BASE", "HEAD"),
        help="Map changed files between two git refs to public canonical URLs",
    )
    parser.add_argument(
        "--max-urls",
        type=int,
        default=100,
        help="Maximum number of URLs to submit (default: 100)",
    )
    parser.add_argument(
        "--require-key-file",
        action="store_true",
        help="Require a {key}.txt file to exist in repo root for verification",
    )
    parser.add_argument(
        "--site-dir",
        default="_site",
        help="Directory of the built Jekyll site (default: _site)",
    )
    parser.add_argument(
        "--report",
        default="indexnow-report.json",
        help="Path to JSON report artifact (default: indexnow-report.json)",
    )
    args = parser.parse_args(argv)

    site_dir = REPO_ROOT / args.site_dir
    report_path = REPO_ROOT / args.report

    key_required = args.submit or args.require_key_file
    key = load_key()
    if key_required and not key:
        print(
            "ERROR: INDEXNOW_KEY not set. Export it, set INDEXNOW_KEY_LOCATION, or add to .env.local",
            file=sys.stderr,
        )
        return 1

    if args.require_key_file:
        if not key:
            print("ERROR: --require-key-file passed but no key loaded", file=sys.stderr)
            return 1
        key_file = REPO_ROOT / f"{key}.txt"
        if not key_file.exists():
            print(
                f"ERROR: --require-key-file passed but {key_file.name} not found in repo root",
                file=sys.stderr,
            )
            return 1

    urls: set[str] = set()
    skipped: dict[str, str] = {}

    if args.urls:
        for u in args.urls:
            if u.startswith("http"):
                urls.add(u)
            else:
                found, reason = public_url_for_path(u)
                if reason:
                    skipped[u] = reason
                urls.update(found)
    elif args.from_git_diff:
        base, head = args.from_git_diff
        changed = git_diff_files(base, head)
        for path in changed:
            found, reason = public_url_for_path(path)
            if reason:
                skipped[path] = reason
            urls.update(found)
    elif args.all:
        urls, skipped = discover_indexable_urls()
    else:
        urls.update(CORE_URLS)

    # Sitemap-backed filtering
    sitemap_urls, sitemap_skipped = filter_urls_by_sitemap(urls, site_dir)
    skipped.update(sitemap_skipped)
    urls = sitemap_urls

    # Defense-in-depth: fail if any selected URL is noindex in built site
    forbidden: list[tuple[str, str]] = []
    if site_dir.exists():
        for url in sorted(urls):
            indexable, reason = check_url_noindex_in_site(url, site_dir)
            if not indexable:
                forbidden.append((url, reason))

    if forbidden:
        print("ERROR: The following selected URLs are not allowed for submission:", file=sys.stderr)
        for url, reason in forbidden:
            print(f"  - {url}: {reason}", file=sys.stderr)
        return 1

    if not urls:
        write_report(report_path, "dry-run" if not args.submit else "submit", [], skipped)
        print("No URLs to submit.")
        if skipped:
            print(f"\nSkipped {len(skipped)} path(s):")
            for path, reason in sorted(skipped.items()):
                print(f"  - {path}: {reason}")
        return 0

    # Apply max-urls cap
    ordered = sorted(urls)
    if len(ordered) > args.max_urls:
        print(
            f"WARNING: URL count ({len(ordered)}) exceeds --max-urls ({args.max_urls}). "
            f"Capping to first {args.max_urls} URLs.",
            file=sys.stderr,
        )
        ordered = ordered[: args.max_urls]

    if not ordered:
        write_report(report_path, "dry-run" if not args.submit else "submit", [], skipped)
        print("No URLs to submit after applying --max-urls.")
        if skipped:
            print(f"\nSkipped {len(skipped)} path(s):")
            for path, reason in sorted(skipped.items()):
                print(f"  - {path}: {reason}")
        return 0

    mode = "Submitting" if args.submit else "[DRY RUN] Would submit"
    print(f"{mode} {len(ordered)} URL(s) to IndexNow")
    for url in ordered:
        print(f"  - {url}")

    if skipped:
        print(f"\nSkipped {len(skipped)} path(s):")
        for path, reason in sorted(skipped.items()):
            print(f"  - {path}: {reason}")

    write_report(report_path, "submit" if args.submit else "dry-run", ordered, skipped)

    if args.submit:
        submit(ordered, key, dry_run=False)
    else:
        submit(ordered, key, dry_run=True)

    return 0


# Test-friendly alias
is_indexable = check_indexable


if __name__ == "__main__":
    raise SystemExit(main())
