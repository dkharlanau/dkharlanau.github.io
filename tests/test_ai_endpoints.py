import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from validate_ai_endpoints import (
    check_json_file,
    check_required_files,
    check_resume_for_sensitive_data,
    check_yaml_file,
    find_sensitive_keys,
)


def test_find_sensitive_keys_detects_email():
    data = {"name": "Dzmitryi Kharlanau", "contact": {"email": "x@example.com"}}
    found = find_sensitive_keys(data)
    assert any("email" in item for item in found)


def test_find_sensitive_keys_ignores_safe_keys():
    data = {"name": "Dzmitryi Kharlanau", "linkedin": "https://linkedin.com/in/x"}
    assert find_sensitive_keys(data) == []


def test_find_sensitive_keys_case_insensitive():
    data = {"EMAIL": "x@example.com"}
    found = find_sensitive_keys(data)
    assert any("EMAIL" in item for item in found)


def test_check_required_files_finds_missing(tmp_path):
    missing = check_required_files(tmp_path)
    assert all(f"Missing required file: {rel}" in missing for rel in [
        "robots.txt", "sitemap.xml", "llms.txt", "ai/resume.json", "ai/resume.yml"
    ])


def test_check_required_files_passes(tmp_path):
    (tmp_path / "robots.txt").write_text("User-agent: *\nAllow: /\n")
    (tmp_path / "sitemap.xml").write_text("<?xml version=\"1.0\"?>")
    (tmp_path / "llms.txt").write_text("# manifest")
    (tmp_path / "ai").mkdir()
    (tmp_path / "ai" / "resume.json").write_text("{}")
    (tmp_path / "ai" / "resume.yml").write_text("---\n")
    assert check_required_files(tmp_path) == []


def test_check_json_file_valid(tmp_path):
    path = tmp_path / "valid.json"
    path.write_text('{"name": "test"}')
    assert check_json_file(path, tmp_path) == []


def test_check_json_file_invalid(tmp_path):
    path = tmp_path / "invalid.json"
    path.write_text("{not valid json}")
    errors = check_json_file(path, tmp_path)
    assert len(errors) == 1
    assert "Invalid JSON" in errors[0]


def test_check_yaml_file_valid(tmp_path):
    path = tmp_path / "valid.yml"
    path.write_text("name: test\n")
    assert check_yaml_file(path, tmp_path) == []


def test_check_yaml_file_invalid(tmp_path):
    path = tmp_path / "invalid.yml"
    path.write_text("name: : : :\n")
    errors = check_yaml_file(path, tmp_path)
    assert len(errors) == 1
    assert "Invalid YAML" in errors[0]


def test_check_resume_for_sensitive_data(tmp_path):
    path = tmp_path / "resume.json"
    path.write_text(json.dumps({"contact": {"email": "x@example.com"}}))
    errors = check_resume_for_sensitive_data(path, tmp_path)
    assert any("Sensitive key found" in item for item in errors)


def test_check_resume_for_sensitive_data_clean(tmp_path):
    path = tmp_path / "resume.json"
    path.write_text(json.dumps({"name": "Dzmitryi Kharlanau", "contact": {"linkedin": "x"}}))
    assert check_resume_for_sensitive_data(path, tmp_path) == []
