#!/usr/bin/env python3
"""Capture private GitHub Traffic API evidence into an ignored local directory."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Protocol
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from portfolio_inventory import RepositorySpec, load_inventory  # noqa: E402


SCHEMA_VERSION = "0.1"
MAX_REFERRERS = 10
MAX_PATHS = 10
MAX_TEXT_LENGTH = 240


class TrafficFailure(RuntimeError):
    """A deliberately sanitized Traffic API failure."""


class TrafficClient(Protocol):
    def get_json(self, endpoint: str) -> Any: ...


class GhTrafficClient:
    """Use the authenticated gh session without printing credentials or API errors."""

    def verify_authentication(self) -> None:
        result = subprocess.run(
            ["gh", "auth", "status", "--hostname", "github.com"],
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if result.returncode != 0:
            raise TrafficFailure("github_authentication_unavailable")

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
            raise TrafficFailure("github_traffic_api_unavailable")
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError as exc:
            raise TrafficFailure("github_traffic_api_invalid_json") from exc


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def bounded_text(value: Any, *, limit: int = MAX_TEXT_LENGTH) -> str:
    text = re.sub(r"[\x00-\x1f\x7f]+", " ", str(value or ""))
    text = re.sub(r"\s+", " ", text).strip()
    return text[:limit]


def sanitize_referrer(value: Any) -> str:
    """Reduce URL-shaped referrers to a host and bound free-form source labels."""

    text = bounded_text(value)
    if not text:
        return "unknown"

    def fallback_label() -> str:
        candidate = text.split("?", 1)[0].split("#", 1)[0]
        if "://" in candidate:
            candidate = candidate.split("://", 1)[1]
        if "@" in candidate:
            candidate = candidate.rsplit("@", 1)[1]
        candidate = candidate.split("/", 1)[0].strip("[]").lower()
        return candidate[:MAX_TEXT_LENGTH] or "unknown"

    try:
        parsed = urlsplit(text if "://" in text else f"//{text}")
        hostname = parsed.hostname
    except ValueError:
        return fallback_label()
    if hostname:
        return hostname.lower()[:MAX_TEXT_LENGTH]
    return fallback_label()


def sanitize_popular_path(value: Any) -> str:
    """Keep only a bounded URL path; discard query strings, fragments, and hosts."""

    text = bounded_text(value)
    if not text:
        return "/"
    try:
        parsed = urlsplit(text)
        path = parsed.path or "/"
    except ValueError:
        path = text.split("?", 1)[0].split("#", 1)[0] or "/"
    if not path.startswith("/"):
        path = f"/{path}"
    return path[:MAX_TEXT_LENGTH]


def non_negative_integer(value: Any) -> int:
    try:
        return max(0, int(value))
    except (TypeError, ValueError):
        return 0


def time_series(payload: Any, key: str) -> list[dict[str, Any]]:
    values = payload.get(key, []) if isinstance(payload, dict) else []
    result: list[dict[str, Any]] = []
    for item in values[:14] if isinstance(values, list) else []:
        if not isinstance(item, dict):
            continue
        result.append(
            {
                "timestamp": bounded_text(item.get("timestamp"), limit=40),
                "count": non_negative_integer(item.get("count")),
                "uniques": non_negative_integer(item.get("uniques")),
            }
        )
    return result


def sanitize_views(payload: Any) -> dict[str, Any]:
    return {
        "count": non_negative_integer(payload.get("count")) if isinstance(payload, dict) else 0,
        "uniques": non_negative_integer(payload.get("uniques")) if isinstance(payload, dict) else 0,
        "daily": time_series(payload, "views"),
    }


def sanitize_clones(payload: Any) -> dict[str, Any]:
    return {
        "count": non_negative_integer(payload.get("count")) if isinstance(payload, dict) else 0,
        "uniques": non_negative_integer(payload.get("uniques")) if isinstance(payload, dict) else 0,
        "daily": time_series(payload, "clones"),
    }


def sanitize_referrers(payload: Any) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for item in payload[:MAX_REFERRERS] if isinstance(payload, list) else []:
        if not isinstance(item, dict):
            continue
        result.append(
            {
                "referrer": sanitize_referrer(item.get("referrer")),
                "count": non_negative_integer(item.get("count")),
                "uniques": non_negative_integer(item.get("uniques")),
            }
        )
    return result


def sanitize_paths(payload: Any) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for item in payload[:MAX_PATHS] if isinstance(payload, list) else []:
        if not isinstance(item, dict):
            continue
        result.append(
            {
                "path": sanitize_popular_path(item.get("path")),
                "title": bounded_text(item.get("title")),
                "count": non_negative_integer(item.get("count")),
                "uniques": non_negative_integer(item.get("uniques")),
            }
        )
    return result


def safe_read(client: TrafficClient, endpoint: str) -> tuple[Any, bool]:
    try:
        return client.get_json(endpoint), True
    except TrafficFailure:
        return None, False


def inspect_repository(spec: RepositorySpec, owner: str, client: TrafficClient) -> dict[str, Any]:
    base = f"repos/{owner}/{spec.name}/traffic"
    views, views_ok = safe_read(client, f"{base}/views")
    clones, clones_ok = safe_read(client, f"{base}/clones")
    referrers, referrers_ok = safe_read(client, f"{base}/popular/referrers")
    paths, paths_ok = safe_read(client, f"{base}/popular/paths")
    return {
        "name": spec.name,
        "repository_url": spec.repository_url,
        "availability": {
            "views": views_ok,
            "clones": clones_ok,
            "referrers": referrers_ok,
            "popular_paths": paths_ok,
        },
        "views": sanitize_views(views),
        "clones": sanitize_clones(clones),
        "referrers": sanitize_referrers(referrers),
        "popular_paths": sanitize_paths(paths),
    }


def build_snapshot(
    config: dict[str, Any],
    specs: list[RepositorySpec],
    client: TrafficClient,
    *,
    generated_at: str | None = None,
) -> dict[str, Any]:
    timestamp = generated_at or utc_now()
    repositories = [inspect_repository(spec, str(config["owner"]), client) for spec in specs]
    complete = sum(all(repo["availability"].values()) for repo in repositories)
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": timestamp,
        "traffic_window": "rolling GitHub Traffic API window, up to 14 days",
        "scope": {
            "owner": str(config["owner"]),
            "repository_count": len(repositories),
            "excluded_repositories": list(config.get("excluded_repositories", [])),
        },
        "summary": {
            "repositories_complete": complete,
            "repositories_with_unavailable_endpoints": len(repositories) - complete,
        },
        "repositories": repositories,
        "handling": {
            "classification": "private-local-traffic-evidence",
            "safe_for_public_report": False,
            "raw_api_responses_retained": False,
            "referrer_urls_reduced_to_hosts": True,
            "popular_path_queries_and_fragments_removed": True,
        },
    }


def markdown_escape(value: Any) -> str:
    return str(value).replace("|", "\\|")


def render_markdown(snapshot: dict[str, Any]) -> str:
    lines = [
        "# Private GitHub traffic snapshot",
        "",
        f"Generated: `{snapshot['generated_at']}`",
        "",
        "> Private local evidence. Do not commit, publish, attach to a public issue, or copy into the public portfolio-health report.",
        "",
        "GitHub exposes a rolling window of up to 14 days. Counts are evidence for comparison, not a complete historical analytics record.",
        "",
        "## Repository summary",
        "",
        "| Repository | Views | Unique viewers | Clones | Unique cloners | Referrers | Popular paths |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for repo in snapshot["repositories"]:
        lines.append(
            "| {name} | {views} | {viewers} | {clones} | {cloners} | {referrers} | {paths} |".format(
                name=markdown_escape(repo["name"]),
                views=repo["views"]["count"],
                viewers=repo["views"]["uniques"],
                clones=repo["clones"]["count"],
                cloners=repo["clones"]["uniques"],
                referrers=len(repo["referrers"]),
                paths=len(repo["popular_paths"]),
            )
        )
    lines += [
        "",
        "## Handling boundary",
        "",
        "This snapshot is stored only under the configured ignored local directory. Referrer URLs are reduced to hostnames; popular-path query strings and fragments are removed; raw API responses and error bodies are not retained.",
        "",
    ]
    return "\n".join(lines)


def _git_output(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )


def validate_private_output_root(output_root: Path) -> Path:
    resolved = output_root.expanduser().resolve()
    if resolved == ROOT or not resolved.is_relative_to(ROOT):
        raise ValueError("private traffic output must be a dedicated directory inside the repository")
    relative = resolved.relative_to(ROOT).as_posix()
    ignore_probe = f"{relative}/.ignore-probe"
    ignored = _git_output("check-ignore", "--no-index", "--quiet", "--", ignore_probe)
    if ignored.returncode != 0:
        raise ValueError("private traffic output is not covered by .gitignore")
    tracked = _git_output("ls-files", "--", relative)
    if tracked.stdout.strip():
        raise ValueError("private traffic output contains tracked files")
    return resolved


def write_snapshot(snapshot: dict[str, Any], output_root: Path) -> tuple[Path, Path]:
    private_root = validate_private_output_root(output_root)
    private_root.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(private_root, 0o700)
    directory_name = re.sub(r"[^0-9A-Za-z]+", "", str(snapshot["generated_at"])) or "snapshot"
    snapshot_dir = private_root / directory_name
    snapshot_dir.mkdir(mode=0o700)
    json_path = snapshot_dir / "traffic-snapshot.json"
    markdown_path = snapshot_dir / "traffic-snapshot.md"
    json_path.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(snapshot), encoding="utf-8")
    os.chmod(json_path, 0o600)
    os.chmod(markdown_path, 0o600)
    return json_path, markdown_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=ROOT / "config" / "portfolio-health.json")
    parser.add_argument("--output-dir", type=Path, help="must remain inside an ignored repository-local directory")
    parser.add_argument("--generated-at", help="explicit timestamp for a deterministic local capture directory")
    args = parser.parse_args()

    try:
        config, specs = load_inventory(ROOT, args.config.resolve())
        output_root = args.output_dir or ROOT / str(config["private_traffic_output"])
        client = GhTrafficClient()
        client.verify_authentication()
        snapshot = build_snapshot(config, specs, client, generated_at=args.generated_at)
        json_path, markdown_path = write_snapshot(snapshot, output_root)
    except (OSError, ValueError, TrafficFailure) as exc:
        print(f"traffic snapshot failed: {exc}", file=sys.stderr)
        return 2

    print(f"Private traffic snapshot captured for {snapshot['scope']['repository_count']} repositories.")
    print(f"JSON: {json_path}")
    print(f"Markdown: {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
