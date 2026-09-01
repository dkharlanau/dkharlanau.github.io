import json
from pathlib import Path

from scripts.portfolio_health import (
    FixtureClient,
    build_report,
    has_exact_author_footer,
    render_markdown,
    workflow_summary,
)
from scripts.portfolio_inventory import load_inventory


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "portfolio_health"


def test_live_inventory_is_manifest_backed_and_contains_exact_public_scope():
    config, specs = load_inventory(ROOT, ROOT / "config" / "portfolio-health.json")

    assert len(specs) == 17
    assert {spec.inventory_source for spec in specs} == {"products/manifest.json"}
    assert "dkharlanau.github.io" not in {spec.name for spec in specs}
    assert config["additional_repositories"] == []
    assert set(config["release_required_repositories"]) == {
        "enterprise-architecture-composer",
        "project-evidence-graph",
        "sap-agentic-operations",
        "signal-to-insight",
        "visual-workbench",
    }

    datasets = next(spec for spec in specs if spec.name == "dkharlanau-datasets")
    assert datasets.pages_expected is False
    assert datasets.live_docs_url == "https://doi.org/10.5281/zenodo.18862098"


def test_fixture_report_detects_publication_and_contract_failures_without_private_data():
    config, specs = load_inventory(FIXTURE, FIXTURE / "config.json")
    report = build_report(
        config,
        specs,
        FixtureClient(FIXTURE / "responses.json"),
        generated_at="2026-09-01T10:00:00Z",
    )

    assert report["status"] == "attention"
    assert report["summary"] == {
        "healthy": 2,
        "attention": 1,
        "only_main": 2,
        "pages_or_docs_live": 2,
        "author_footer_exact": 2,
        "published_sha_ci_passing": 1,
        "release_required": 1,
        "required_release_at_published_sha": 1,
        "local_checkouts_checked": 0,
        "local_publication_clean": 0,
    }

    beta = next(repo for repo in report["repositories"] if repo["name"] == "beta-tool")
    alpha = next(repo for repo in report["repositories"] if repo["name"] == "alpha-tool")
    assert alpha["release_state"]["release_required"] is True
    assert alpha["release_state"]["latest_release_matches_published_sha"] is True
    codes = {item["code"] for item in beta["findings"]}
    assert beta["remote_branches"]["names"] == ["legacy", "main"]
    assert beta["documentation"]["author_footer_exact"] is False
    assert beta["cross_project_contracts"]["missing_links"] == ["alpha-tool"]
    assert {
        "remote_branches_not_main_only",
        "author_footer_mismatch",
        "live_docs_unavailable",
        "pages_not_enabled",
        "contract_links_missing",
        "published_sha_ci_failing",
    } <= codes

    encoded = json.dumps(report)
    for private_key in ("views", "clones", "referrers", "popular_paths"):
        assert f'"{private_key}"' not in encoded
    assert str(ROOT) not in encoded
    assert report["boundaries"]["private_traffic_included"] is False

    markdown = render_markdown(report)
    assert "# Public portfolio health" in markdown
    assert "beta-tool / error / `author_footer_mismatch`" in markdown
    assert "no GitHub Traffic API data" in markdown


def test_required_release_must_resolve_to_current_published_main_sha():
    config, specs = load_inventory(FIXTURE, FIXTURE / "config.json")
    client = FixtureClient(FIXTURE / "responses.json")
    client.payload["json"]["repos/dkharlanau/alpha-tool/commits/v1.0.0"] = {
        "sha": "older-release-sha"
    }

    report = build_report(config, specs, client, generated_at="2026-09-01T10:00:00Z")

    alpha = next(repo for repo in report["repositories"] if repo["name"] == "alpha-tool")
    assert alpha["release_state"]["latest_release_matches_published_sha"] is False
    assert "required_release_not_at_published_main" in {
        item["code"] for item in alpha["findings"]
    }
    assert alpha["status"] == "attention"


def test_workflow_summary_is_bound_to_the_exact_published_sha():
    runs = [
        {
            "name": "CI",
            "head_sha": "published",
            "status": "completed",
            "conclusion": "success",
        },
        {
            "name": "CI",
            "head_sha": "old",
            "status": "completed",
            "conclusion": "failure",
        },
    ]

    result = workflow_summary(runs, "published")

    assert result["status"] == "passing"
    assert result["workflow_count"] == 1
    assert result["workflows"][0]["conclusion"] == "success"


def test_exact_author_footer_must_start_on_its_own_final_line():
    footer = "## About the author\n\nAuthor copy"

    assert has_exact_author_footer(f"# Project\n\n{footer}\n", footer) is True
    assert has_exact_author_footer(footer, footer) is True
    assert has_exact_author_footer(f"# Project{footer}", footer) is False
    assert has_exact_author_footer(f"# Project\n\n{footer}\nextra", footer) is False


def test_automated_health_workflow_is_read_only_and_excludes_private_traffic():
    workflow = (ROOT / ".github" / "workflows" / "portfolio-health.yml").read_text(encoding="utf-8")

    assert "schedule:" in workflow
    assert "workflow_dispatch:" in workflow
    assert "contents: read" in workflow
    assert "actions: read" in workflow
    assert "python3 scripts/portfolio_health.py --strict" in workflow
    assert "retention-days: 7" in workflow
    assert "github_traffic_snapshot" not in workflow
    assert "traffic-snapshot" not in workflow
