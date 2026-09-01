#!/usr/bin/env python3
"""Build a bounded public-safe health snapshot for the public repository portfolio."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Protocol
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from portfolio_inventory import RepositorySpec, author_footer, load_inventory  # noqa: E402


SCHEMA_VERSION = "0.2"
MAX_ACTION_RUNS = 20
MAX_RELEASES_OR_TAGS = 100
ACCEPTABLE_CONCLUSIONS = {"success", "neutral", "skipped"}
FAILURE_CONCLUSIONS = {"failure", "timed_out", "cancelled", "action_required", "startup_failure", "stale"}


class ApiFailure(RuntimeError):
    """A deliberately sanitized remote-read failure."""


class PortfolioClient(Protocol):
    def get_json(self, endpoint: str) -> Any: ...

    def get_text(self, endpoint: str) -> str: ...

    def probe(self, url: str) -> dict[str, Any]: ...


class GhPublicClient:
    """Read public GitHub data without exposing authentication details."""

    def get_json(self, endpoint: str) -> Any:
        result = subprocess.run(
            ["gh", "api", "-H", "Accept: application/vnd.github+json", endpoint],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if result.returncode != 0:
            raise ApiFailure("github_api_unavailable")
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError as exc:
            raise ApiFailure("github_api_invalid_json") from exc

    def get_text(self, endpoint: str) -> str:
        result = subprocess.run(
            ["gh", "api", "-H", "Accept: application/vnd.github.raw+json", endpoint],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if result.returncode != 0:
            raise ApiFailure("github_content_unavailable")
        return result.stdout

    def probe(self, url: str) -> dict[str, Any]:
        request = Request(url, headers={"User-Agent": "dkharlanau-portfolio-health/0.1"})
        try:
            with urlopen(request, timeout=15) as response:  # noqa: S310 - URLs are checked-in public endpoints.
                response.read(512)
                return {
                    "status": int(response.status),
                    "live": 200 <= int(response.status) < 400,
                    "final_url": str(response.geturl()).split("?", 1)[0].split("#", 1)[0],
                }
        except HTTPError as exc:
            return {"status": int(exc.code), "live": False, "final_url": None}
        except (URLError, TimeoutError, ValueError):
            return {"status": None, "live": False, "final_url": None}


class FixtureClient:
    """Deterministic client used by regression fixtures and local contract checks."""

    def __init__(self, fixture_path: Path):
        self.payload = json.loads(fixture_path.read_text(encoding="utf-8"))

    def get_json(self, endpoint: str) -> Any:
        try:
            return self.payload["json"][endpoint]
        except KeyError as exc:
            raise ApiFailure("fixture_json_missing") from exc

    def get_text(self, endpoint: str) -> str:
        try:
            return str(self.payload["text"][endpoint])
        except KeyError as exc:
            raise ApiFailure("fixture_text_missing") from exc

    def probe(self, url: str) -> dict[str, Any]:
        try:
            return dict(self.payload["http"][url])
        except KeyError as exc:
            raise ApiFailure("fixture_http_missing") from exc


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def safe_json(client: PortfolioClient, endpoint: str, fallback: Any) -> tuple[Any, bool]:
    try:
        return client.get_json(endpoint), True
    except ApiFailure:
        return fallback, False


def safe_text(client: PortfolioClient, endpoint: str) -> tuple[str, bool]:
    try:
        return client.get_text(endpoint), True
    except ApiFailure:
        return "", False


def safe_probe(client: PortfolioClient, url: str | None) -> dict[str, Any]:
    if not url:
        return {"checked": False, "status": None, "live": None, "url": None, "final_url": None}
    try:
        result = client.probe(url)
    except ApiFailure:
        result = {"status": None, "live": False, "final_url": None}
    return {
        "checked": True,
        "status": result.get("status"),
        "live": bool(result.get("live")),
        "url": url,
        "final_url": result.get("final_url"),
    }


def workflow_summary(runs: list[dict[str, Any]], default_sha: str | None) -> dict[str, Any]:
    matching = [run for run in runs if default_sha and run.get("head_sha") == default_sha]
    latest_by_workflow: dict[str, dict[str, Any]] = {}
    for run in matching:
        name = str(run.get("name") or "unnamed-workflow")
        if name not in latest_by_workflow:
            latest_by_workflow[name] = run
    bounded = []
    for name, run in sorted(latest_by_workflow.items()):
        bounded.append(
            {
                "name": name,
                "status": run.get("status"),
                "conclusion": run.get("conclusion"),
                "event": run.get("event"),
                "url": run.get("html_url"),
            }
        )
    conclusions = {str(item.get("conclusion")) for item in bounded if item.get("conclusion")}
    statuses = {str(item.get("status")) for item in bounded if item.get("status")}
    if not bounded:
        aggregate = "unknown"
    elif conclusions & FAILURE_CONCLUSIONS:
        aggregate = "failing"
    elif any(status != "completed" for status in statuses):
        aggregate = "pending"
    elif conclusions <= ACCEPTABLE_CONCLUSIONS:
        aggregate = "passing"
    else:
        aggregate = "unknown"
    return {"status": aggregate, "workflow_count": len(bounded), "workflows": bounded}


def discovered_repository_links(readme: str, owner: str, known_names: set[str]) -> list[str]:
    pattern = re.compile(rf"https://(?:github\.com/{re.escape(owner)}/|{re.escape(owner)}\.github\.io/)([A-Za-z0-9._-]+)")
    found = {match.removesuffix(".git") for match in pattern.findall(readme)}
    return sorted((found & known_names))


def has_exact_author_footer(readme: str, footer: str) -> bool:
    normalized = readme.rstrip("\n")
    return normalized == footer or normalized.endswith(f"\n{footer}")


def find_checkout(name: str, roots: list[Path], overrides: dict[str, Path]) -> Path | None:
    if name in overrides and (overrides[name] / ".git").exists():
        return overrides[name]
    for root in roots:
        candidate = root / name
        if (candidate / ".git").exists():
            return candidate
    return None


def git_output(checkout: Path, *args: str) -> tuple[str, bool]:
    result = subprocess.run(
        ["git", *args],
        cwd=checkout,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.stdout.strip(), result.returncode == 0


def local_publication_state(checkout: Path | None, default_sha: str | None) -> dict[str, Any]:
    if checkout is None:
        return {
            "checked": False,
            "clean_worktree": None,
            "branch": None,
            "head_sha": None,
            "matches_published_default_sha": None,
            "publication_clean": None,
        }
    status, status_ok = git_output(checkout, "status", "--porcelain=v1")
    branch, branch_ok = git_output(checkout, "branch", "--show-current")
    head, head_ok = git_output(checkout, "rev-parse", "HEAD")
    checked = status_ok and branch_ok and head_ok
    clean = status == "" if status_ok else None
    matches = head == default_sha if head_ok and default_sha else None
    return {
        "checked": checked,
        "clean_worktree": clean,
        "branch": branch or None,
        "head_sha": head or None,
        "matches_published_default_sha": matches,
        "publication_clean": bool(clean and branch == "main" and matches) if checked and matches is not None else None,
    }


def finding(code: str, severity: str, message: str) -> dict[str, str]:
    return {"code": code, "severity": severity, "message": message}


def inspect_repository(
    spec: RepositorySpec,
    *,
    owner: str,
    known_names: set[str],
    footer: str,
    client: PortfolioClient,
    checkout: Path | None,
    release_required: bool,
) -> dict[str, Any]:
    base = f"repos/{owner}/{spec.name}"
    metadata, metadata_ok = safe_json(client, base, {})
    branches, branches_ok = safe_json(client, f"{base}/branches?per_page=100", [])
    releases, releases_ok = safe_json(client, f"{base}/releases?per_page={MAX_RELEASES_OR_TAGS}", [])
    tags, tags_ok = safe_json(client, f"{base}/tags?per_page={MAX_RELEASES_OR_TAGS}", [])
    readme, readme_ok = safe_text(client, f"{base}/readme?ref=main")

    branch_names = sorted(str(item.get("name")) for item in branches if isinstance(item, dict) and item.get("name"))
    main_branch = next((item for item in branches if isinstance(item, dict) and item.get("name") == "main"), {})
    default_sha = ((main_branch.get("commit") or {}).get("sha")) if isinstance(main_branch, dict) else None
    runs, runs_ok = safe_json(client, f"{base}/actions/runs?branch=main&per_page={MAX_ACTION_RUNS}", {})
    run_items = runs.get("workflow_runs", []) if isinstance(runs, dict) else []
    ci = workflow_summary(run_items if isinstance(run_items, list) else [], default_sha)
    ci["checked"] = runs_ok

    published_releases = (
        [item for item in releases if isinstance(item, dict) and not item.get("draft")]
        if isinstance(releases, list)
        else []
    )
    latest_release = published_releases[0] if published_releases else {}
    latest_release_tag = str(latest_release.get("tag_name") or "") or None
    tag_names = {
        str(item.get("name")) for item in tags if isinstance(item, dict) and item.get("name")
    } if isinstance(tags, list) else set()
    latest_release_tag_present = latest_release_tag in tag_names if latest_release_tag else False
    release_commit: Any = {}
    release_commit_ok = False
    if release_required and latest_release_tag:
        release_commit, release_commit_ok = safe_json(
            client,
            f"{base}/commits/{quote(latest_release_tag, safe='')}",
            {},
        )
    latest_release_sha = release_commit.get("sha") if isinstance(release_commit, dict) else None
    latest_release_matches_default = (
        latest_release_sha == default_sha if latest_release_sha and default_sha else None
    )

    live_docs = safe_probe(client, spec.live_docs_url)
    agent_manifest = safe_probe(client, spec.agent_manifest_url)
    footer_exact = has_exact_author_footer(readme, footer) if readme_ok else False
    discovered = discovered_repository_links(readme, owner, known_names) if readme_ok else []
    missing_links = sorted(set(spec.expected_links) - set(discovered))
    local = local_publication_state(checkout, default_sha)

    repo_findings: list[dict[str, str]] = []
    if not metadata_ok:
        repo_findings.append(finding("metadata_unavailable", "error", "Repository metadata could not be read."))
    else:
        if metadata.get("private") or metadata.get("fork") or metadata.get("archived"):
            repo_findings.append(finding("repository_scope_mismatch", "error", "Repository is not active, public, and independently owned."))
        if metadata.get("default_branch") != "main":
            repo_findings.append(finding("default_branch_not_main", "error", "Default branch is not main."))
        if not str(metadata.get("description") or "").strip():
            repo_findings.append(finding("description_missing", "warning", "Public repository description is missing."))
        if not str(metadata.get("homepage") or "").strip():
            repo_findings.append(finding("homepage_missing", "warning", "Public homepage or documentation URL is missing."))
    if not branches_ok:
        repo_findings.append(finding("branches_unavailable", "error", "Remote branch inventory could not be read."))
    elif branch_names != ["main"]:
        repo_findings.append(finding("remote_branches_not_main_only", "error", "Remote branch inventory is not limited to main."))
    if not default_sha:
        repo_findings.append(finding("default_sha_unavailable", "error", "Published main SHA could not be resolved."))
    if not readme_ok:
        repo_findings.append(finding("readme_unavailable", "error", "README could not be read."))
    elif not footer_exact:
        repo_findings.append(finding("author_footer_mismatch", "error", "README does not end with the exact portfolio author footer."))
    if spec.live_docs_url and not live_docs["live"]:
        repo_findings.append(finding("live_docs_unavailable", "error", "Configured live documentation endpoint did not return a successful response."))
    if spec.pages_expected and not bool(metadata.get("has_pages")):
        repo_findings.append(finding("pages_not_enabled", "error", "Portfolio expects GitHub Pages, but repository metadata does not report Pages."))
    if spec.agent_manifest_url and not agent_manifest["live"]:
        repo_findings.append(finding("agent_manifest_unavailable", "warning", "Configured public agent manifest is not reachable."))
    if missing_links:
        repo_findings.append(finding("contract_links_missing", "error", "README is missing one or more required cross-project contract links."))
    if release_required:
        if not releases_ok:
            repo_findings.append(finding("required_release_unavailable", "error", "Required release state could not be read."))
        elif not latest_release_tag:
            repo_findings.append(finding("required_release_missing", "error", "This flagship repository has no published release."))
        elif not tags_ok or not latest_release_tag_present:
            repo_findings.append(finding("required_release_tag_missing", "error", "The latest published release tag is not present in the bounded tag inventory."))
        elif not release_commit_ok or not latest_release_sha:
            repo_findings.append(finding("required_release_sha_unavailable", "error", "The latest published release tag could not be resolved to a commit SHA."))
        elif not latest_release_matches_default:
            repo_findings.append(finding("required_release_not_at_published_main", "error", "The latest published release tag does not resolve to the current published main SHA."))
    elif not releases_ok or not tags_ok:
        repo_findings.append(finding("release_state_unavailable", "warning", "Release or tag state could not be read."))
    if ci["status"] == "failing":
        repo_findings.append(finding("published_sha_ci_failing", "error", "A latest workflow on the published main SHA is failing."))
    elif ci["status"] == "pending":
        repo_findings.append(finding("published_sha_ci_pending", "warning", "A latest workflow on the published main SHA is still pending."))
    elif ci["status"] == "unknown":
        repo_findings.append(finding("published_sha_ci_unknown", "warning", "No conclusive workflow status was found for the published main SHA."))
    if local["checked"]:
        if not local["clean_worktree"]:
            repo_findings.append(finding("local_worktree_dirty", "error", "The optional local checkout is not clean."))
        if local["branch"] != "main":
            repo_findings.append(finding("local_branch_not_main", "error", "The optional local checkout is not on main."))
        if not local["matches_published_default_sha"]:
            repo_findings.append(finding("local_sha_not_published", "error", "The optional local checkout HEAD does not match the published main SHA."))

    error_count = sum(item["severity"] == "error" for item in repo_findings)
    return {
        "name": spec.name,
        "repository_url": spec.repository_url,
        "inventory_source": spec.inventory_source,
        "status": "attention" if error_count else "healthy",
        "metadata": {
            "checked": metadata_ok,
            "default_branch": metadata.get("default_branch") if metadata_ok else None,
            "active_public_independent": (
                not metadata.get("private") and not metadata.get("fork") and not metadata.get("archived")
                if metadata_ok
                else None
            ),
            "visibility": metadata.get("visibility") if metadata_ok else None,
            "archived": metadata.get("archived") if metadata_ok else None,
            "fork": metadata.get("fork") if metadata_ok else None,
            "description_present": bool(str(metadata.get("description") or "").strip()) if metadata_ok else None,
            "homepage": metadata.get("homepage") if metadata_ok else None,
            "has_pages": metadata.get("has_pages") if metadata_ok else None,
            "topics": sorted(metadata.get("topics", []))[:20] if metadata_ok and isinstance(metadata.get("topics"), list) else [],
        },
        "remote_branches": {
            "checked": branches_ok,
            "names": branch_names,
            "only_main": branch_names == ["main"] if branches_ok else None,
            "truncated": len(branch_names) >= 100,
        },
        "published_default": {
            "sha": default_sha,
            "ci": ci,
        },
        "local_publication": local,
        "documentation": {
            "pages_expected": spec.pages_expected,
            "live_docs": live_docs,
            "agent_manifest": agent_manifest,
            "readme_checked": readme_ok,
            "author_footer_exact": footer_exact if readme_ok else None,
        },
        "release_state": {
            "release_required": release_required,
            "releases_checked": releases_ok,
            "release_count_bounded": len(published_releases),
            "release_count_truncated": isinstance(releases, list) and len(releases) >= MAX_RELEASES_OR_TAGS,
            "latest_release_tag": latest_release_tag,
            "latest_release_tag_present": latest_release_tag_present if latest_release_tag else None,
            "latest_release_sha": latest_release_sha,
            "latest_release_matches_published_sha": latest_release_matches_default,
            "tags_checked": tags_ok,
            "tag_count_bounded": len(tags) if isinstance(tags, list) else 0,
            "tag_count_truncated": isinstance(tags, list) and len(tags) >= MAX_RELEASES_OR_TAGS,
            "latest_tag": tags[0].get("name") if tags_ok and isinstance(tags, list) and tags else None,
        },
        "cross_project_contracts": {
            "expected_links": list(spec.expected_links),
            "discovered_links": discovered,
            "missing_links": missing_links,
        },
        "findings": repo_findings,
    }


def build_report(
    config: dict[str, Any],
    specs: list[RepositorySpec],
    client: PortfolioClient,
    *,
    checkout_roots: list[Path] | None = None,
    checkout_overrides: dict[str, Path] | None = None,
    generated_at: str | None = None,
) -> dict[str, Any]:
    owner = str(config["owner"])
    known_names = {spec.name for spec in specs}
    roots = checkout_roots or []
    overrides = checkout_overrides or {}
    footer = author_footer(config)
    release_required = set(config.get("release_required_repositories", []) or [])
    repositories = [
        inspect_repository(
            spec,
            owner=owner,
            known_names=known_names,
            footer=footer,
            client=client,
            checkout=find_checkout(spec.name, roots, overrides),
            release_required=spec.name in release_required,
        )
        for spec in specs
    ]
    attention = [repo["name"] for repo in repositories if repo["status"] == "attention"]
    checked_local = sum(bool(repo["local_publication"]["checked"]) for repo in repositories)
    required_releases = [repo for repo in repositories if repo["release_state"]["release_required"]]
    public_surfaces = []
    for configured in config.get("required_public_surfaces", []) or []:
        surface_id = str(configured.get("id") or "").strip()
        surface_url = str(configured.get("url") or "").strip()
        probe = safe_probe(client, surface_url)
        public_surfaces.append(
            {
                "id": surface_id,
                "url": surface_url,
                "status": "healthy" if probe["live"] else "attention",
                "probe": probe,
            }
        )
    unavailable_surfaces = [
        surface["id"] for surface in public_surfaces if surface["status"] == "attention"
    ]
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": generated_at or utc_now(),
        "scope": {
            "owner": owner,
            "repository_count": len(repositories),
            "excluded_repositories": list(config.get("excluded_repositories", [])),
            "inventory_sources": sorted({repo["inventory_source"] for repo in repositories}),
        },
        "status": "attention" if attention or unavailable_surfaces else "healthy",
        "summary": {
            "healthy": len(repositories) - len(attention),
            "attention": len(attention),
            "only_main": sum(repo["remote_branches"]["only_main"] is True for repo in repositories),
            "pages_or_docs_live": sum(repo["documentation"]["live_docs"]["live"] is True for repo in repositories),
            "author_footer_exact": sum(repo["documentation"]["author_footer_exact"] is True for repo in repositories),
            "published_sha_ci_passing": sum(repo["published_default"]["ci"]["status"] == "passing" for repo in repositories),
            "release_required": len(required_releases),
            "required_release_at_published_sha": sum(
                repo["release_state"]["latest_release_matches_published_sha"] is True
                for repo in required_releases
            ),
            "local_checkouts_checked": checked_local,
            "local_publication_clean": sum(repo["local_publication"]["publication_clean"] is True for repo in repositories),
            "required_public_surfaces": len(public_surfaces),
            "required_public_surfaces_live": len(public_surfaces) - len(unavailable_surfaces),
        },
        "repositories": repositories,
        "public_surfaces": public_surfaces,
        "boundaries": {
            "public_metadata_only": True,
            "private_traffic_included": False,
            "credentials_or_tokens_included": False,
            "local_checkout_paths_included": False,
            "api_error_bodies_included": False,
        },
    }


def render_markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "# Public portfolio health",
        "",
        f"Generated: `{report['generated_at']}`",
        "",
        f"Overall status: **{report['status'].upper()}**",
        "",
        "## Summary",
        "",
        f"- Repositories: **{report['scope']['repository_count']}**",
        f"- Healthy: **{summary['healthy']}**",
        f"- Need attention: **{summary['attention']}**",
        f"- Remote branch set is only `main`: **{summary['only_main']}**",
        f"- Pages or configured live docs reachable: **{summary['pages_or_docs_live']}**",
        f"- Exact final README author footer: **{summary['author_footer_exact']}**",
        f"- Published main SHA with passing CI: **{summary['published_sha_ci_passing']}**",
        f"- Required flagship release tag resolves to published main SHA: **{summary['required_release_at_published_sha']}/{summary['release_required']}**",
        f"- Optional local checkouts clean and equal to published SHA: **{summary['local_publication_clean']}/{summary['local_checkouts_checked']}**",
        f"- Required central public surfaces reachable: **{summary['required_public_surfaces_live']}/{summary['required_public_surfaces']}**",
        "",
        "## Repository ledger",
        "",
        "| Repository | Status | Branches | CI | Docs | Footer | Releases / tags | Contract links |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for repo in report["repositories"]:
        release = repo["release_state"]
        if release["release_required"]:
            releases = "required @ main" if release["latest_release_matches_published_sha"] else "required / attention"
        else:
            releases = f"{release['release_count_bounded']} / {release['tag_count_bounded']}"
        links = repo["cross_project_contracts"]
        link_state = "ok" if not links["missing_links"] else f"missing {len(links['missing_links'])}"
        lines.append(
            "| {name} | {status} | {branches} | {ci} | {docs} | {footer} | {releases} | {links} |".format(
                name=repo["name"],
                status=repo["status"],
                branches="main only" if repo["remote_branches"]["only_main"] else "attention",
                ci=repo["published_default"]["ci"]["status"],
                docs="live" if repo["documentation"]["live_docs"]["live"] else "unavailable",
                footer="exact" if repo["documentation"]["author_footer_exact"] else "mismatch",
                releases=releases,
                links=link_state,
            )
        )
    findings = [
        (repo["name"], item)
        for repo in report["repositories"]
        for item in repo["findings"]
        if item["severity"] in {"error", "warning"}
    ]
    surface_findings = [
        surface for surface in report.get("public_surfaces", []) if surface["status"] == "attention"
    ]
    lines += ["", "## Findings", ""]
    if findings:
        for name, item in findings:
            lines.append(f"- **{name} / {item['severity']} / `{item['code']}`:** {item['message']}")
    else:
        lines.append("No error or warning findings.")
    if surface_findings:
        for surface in surface_findings:
            lines.append(
                f"- **public surface / error / `{surface['id']}`:** Required public URL is unavailable."
            )
    lines += [
        "",
        "## Evidence boundary",
        "",
        "This report contains public repository metadata, public workflow state, public documentation checks, release/tag presence, and optional local clean-state booleans. It contains no GitHub Traffic API data, credentials, token material, API error bodies, or local filesystem paths.",
        "",
    ]
    return "\n".join(lines)


def write_report(report: dict[str, Any], output_dir: Path) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "portfolio-health.json"
    markdown_path = output_dir / "portfolio-health.md"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(report), encoding="utf-8")
    return json_path, markdown_path


def parse_checkout_overrides(values: list[str]) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for value in values:
        if "=" not in value:
            raise ValueError("--checkout must use repository=path")
        name, raw_path = value.split("=", 1)
        if not name.strip() or not raw_path.strip():
            raise ValueError("--checkout must use repository=path")
        result[name.strip()] = Path(raw_path).expanduser().resolve()
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=ROOT / "config" / "portfolio-health.json")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--checkouts-root", action="append", default=[], type=Path)
    parser.add_argument("--checkout", action="append", default=[], help="optional repository=path checkout override")
    parser.add_argument("--fixture", type=Path, help="deterministic response fixture; disables live reads")
    parser.add_argument("--generated-at", help="explicit ISO-8601 timestamp for deterministic fixture runs")
    parser.add_argument("--strict", action="store_true", help="exit non-zero when any repository needs attention")
    args = parser.parse_args()

    try:
        config_path = args.config.resolve()
        config, specs = load_inventory(ROOT, config_path)
        output_dir = (args.output_dir or ROOT / str(config["public_report_output"])).resolve()
        client: PortfolioClient = FixtureClient(args.fixture.resolve()) if args.fixture else GhPublicClient()
        report = build_report(
            config,
            specs,
            client,
            checkout_roots=[path.expanduser().resolve() for path in args.checkouts_root],
            checkout_overrides=parse_checkout_overrides(args.checkout),
            generated_at=args.generated_at,
        )
        json_path, markdown_path = write_report(report, output_dir)
    except (OSError, ValueError, ApiFailure) as exc:
        print(f"portfolio health failed: {exc}", file=sys.stderr)
        return 2

    print(f"Portfolio health: {report['status']} ({report['summary']['healthy']}/{report['scope']['repository_count']} healthy)")
    print(f"JSON: {json_path}")
    print(f"Markdown: {markdown_path}")
    return 1 if args.strict and report["status"] != "healthy" else 0


if __name__ == "__main__":
    raise SystemExit(main())
