import json
import stat
import subprocess
from pathlib import Path

import pytest

from scripts import github_traffic_snapshot as traffic
from scripts.portfolio_inventory import RepositorySpec


class FakeTrafficClient:
    def get_json(self, endpoint):
        payloads = {
            "repos/dkharlanau/example/traffic/views": {
                "count": 9,
                "uniques": 4,
                "views": [
                    {"timestamp": "2026-08-31T00:00:00Z", "count": 9, "uniques": 4}
                ],
            },
            "repos/dkharlanau/example/traffic/clones": {
                "count": 3,
                "uniques": 2,
                "clones": [
                    {"timestamp": "2026-08-31T00:00:00Z", "count": 3, "uniques": 2}
                ],
            },
            "repos/dkharlanau/example/traffic/popular/referrers": [
                {
                    "referrer": "https://user:password@source.example/path?access_token=secret#fragment",
                    "count": 5,
                    "uniques": 3,
                }
            ],
            "repos/dkharlanau/example/traffic/popular/paths": [
                {
                    "path": "https://github.com/dkharlanau/example/docs/start?token=secret#fragment",
                    "title": "Start\u0000 here",
                    "count": 7,
                    "uniques": 4,
                }
            ],
        }
        return payloads[endpoint]


def example_spec():
    return RepositorySpec(
        name="example",
        repository_url="https://github.com/dkharlanau/example",
        page_url=None,
        live_docs_url=None,
        agent_manifest_url=None,
        pages_expected=False,
        expected_links=(),
        inventory_source="fixture",
    )


def test_snapshot_sanitizes_url_evidence_and_never_keeps_raw_responses():
    snapshot = traffic.build_snapshot(
        {"owner": "dkharlanau", "excluded_repositories": ["dkharlanau.github.io"]},
        [example_spec()],
        FakeTrafficClient(),
        generated_at="2026-09-01T10:00:00Z",
    )

    repo = snapshot["repositories"][0]
    assert repo["referrers"] == [{"referrer": "source.example", "count": 5, "uniques": 3}]
    assert repo["popular_paths"] == [
        {"path": "/dkharlanau/example/docs/start", "title": "Start here", "count": 7, "uniques": 4}
    ]
    encoded = json.dumps(snapshot)
    assert "password" not in encoded
    assert "access_token" not in encoded
    assert "secret" not in encoded
    assert "raw" not in repo
    assert snapshot["handling"]["safe_for_public_report"] is False
    assert traffic.sanitize_referrer("https://[invalid]?token=secret") == "invalid"
    assert traffic.sanitize_popular_path("https://[invalid]/docs?token=secret") == "/docs"


def test_malformed_url_fallback_is_python_version_independent(monkeypatch):
    def reject_malformed_url(_value):
        raise ValueError("malformed URL")

    monkeypatch.setattr(traffic, "urlsplit", reject_malformed_url)

    assert traffic.sanitize_referrer("https://[invalid]?token=secret") == "invalid"
    assert traffic.sanitize_popular_path("https://[invalid]/docs?token=secret") == "/docs"


def test_private_output_is_ignored_untracked_and_owner_only(tmp_path, monkeypatch):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    (tmp_path / ".gitignore").write_text(".local/portfolio-traffic/\n", encoding="utf-8")
    monkeypatch.setattr(traffic, "ROOT", tmp_path)
    snapshot = traffic.build_snapshot(
        {"owner": "dkharlanau", "excluded_repositories": []},
        [example_spec()],
        FakeTrafficClient(),
        generated_at="2026-09-01T10:00:00Z",
    )

    json_path, markdown_path = traffic.write_snapshot(snapshot, tmp_path / ".local" / "portfolio-traffic")

    assert stat.S_IMODE(json_path.stat().st_mode) == 0o600
    assert stat.S_IMODE(markdown_path.stat().st_mode) == 0o600
    assert stat.S_IMODE(json_path.parent.stat().st_mode) == 0o700
    assert stat.S_IMODE(json_path.parent.parent.stat().st_mode) == 0o700
    ignored = subprocess.run(
        ["git", "check-ignore", "--no-index", "--quiet", str(json_path)], cwd=tmp_path, check=False
    )
    assert ignored.returncode == 0
    tracked = subprocess.run(
        ["git", "ls-files", "--", ".local/portfolio-traffic"],
        cwd=tmp_path,
        text=True,
        stdout=subprocess.PIPE,
        check=True,
    )
    assert tracked.stdout == ""


def test_private_output_rejects_unignored_or_external_paths(tmp_path, monkeypatch):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    (tmp_path / ".gitignore").write_text(".local/portfolio-traffic/\n", encoding="utf-8")
    monkeypatch.setattr(traffic, "ROOT", tmp_path)

    assert traffic.validate_private_output_root(tmp_path / ".local" / "portfolio-traffic") == (
        tmp_path / ".local" / "portfolio-traffic"
    )
    with pytest.raises(ValueError, match="not covered by .gitignore"):
        traffic.validate_private_output_root(tmp_path / "reports" / "traffic")
    with pytest.raises(ValueError, match="inside the repository"):
        traffic.validate_private_output_root(tmp_path.parent / "private-traffic")
