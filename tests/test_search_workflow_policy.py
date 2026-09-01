from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_google_search_workflow_uses_quota_safe_trigger_policies():
    text = (ROOT / ".github/workflows/google-search.yml").read_text(encoding="utf-8")
    assert 'echo "max=120"' in text
    assert 'echo "max=100"' in text
    assert 'echo "cooldown=6"' in text
    assert "--require-credentials" in text
    assert "--inspection-mode" in text
    assert "--min-inspection-interval-hours" in text


def test_google_search_workflow_fails_closed_without_credentials():
    text = (ROOT / ".github/workflows/google-search.yml").read_text(encoding="utf-8")
    assert "GOOGLE_SEARCH_CONSOLE_SERVICE_ACCOUNT is not configured" in text
    assert 'echo "configured=false"' not in text
    assert "Production indexing checks cannot run" in text


def test_indexnow_production_waits_for_successful_ci_and_reuses_site_artifact():
    text = (ROOT / ".github/workflows/indexnow.yml").read_text(encoding="utf-8")
    assert "workflow_run:" in text
    assert "- CI" in text
    assert "github.event.workflow_run.conclusion == 'success'" in text
    assert "--name ci-built-site" in text
    assert "Reuse validated CI site" in text
    assert "Real IndexNow submission" in text


def test_indexnow_reports_no_changes_without_claiming_network_submission():
    text = (ROOT / ".github/workflows/indexnow.yml").read_text(encoding="utf-8")
    assert "Resolve IndexNow result" in text
    assert 'status="no_changes"' in text
    assert 'network="no"' in text
    assert 'status="submitted"' in text
    assert 'network="yes"' in text
    assert "steps.result.outputs.status" in text
    assert "steps.result.outputs.network" in text


def test_ci_publishes_built_site_for_search_workflows():
    text = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    assert "Upload built site for downstream search workflows" in text
    assert "name: ci-built-site" in text
    assert "path: _site/" in text
