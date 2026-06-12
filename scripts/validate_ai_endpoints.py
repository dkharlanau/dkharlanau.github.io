#!/usr/bin/env python3
"""Validate AI-readable endpoints and search/AI discovery files in a built site."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REQUIRED_FILES = [
    "robots.txt",
    "sitemap.xml",
    "llms.txt",
    "ai/resume.json",
    "ai/resume.yml",
]

SENSITIVE_KEYS = {
    "email",
    "phone",
    "mobile",
    "address",
    "streetaddress",
    "birthdate",
    "ssn",
    "passport",
}


def check_required_files(root: Path) -> list[str]:
    missing = []
    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            missing.append(f"Missing required file: {rel}")
    return missing


def check_json_file(path: Path, root: Path) -> list[str]:
    errors = []
    try:
        text = path.read_text(encoding="utf-8")
        json.loads(text)
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON in {path.relative_to(root)}: {exc}")
    except OSError as exc:
        errors.append(f"Cannot read {path}: {exc}")
    return errors


def check_yaml_file(path: Path, root: Path) -> list[str]:
    errors = []
    try:
        import yaml
    except ImportError:
        errors.append("PyYAML is required for YAML validation")
        return errors

    try:
        text = path.read_text(encoding="utf-8")
        yaml.safe_load(text)
    except yaml.YAMLError as exc:
        errors.append(f"Invalid YAML in {path.relative_to(root)}: {exc}")
    except OSError as exc:
        errors.append(f"Cannot read {path}: {exc}")
    return errors


def find_sensitive_keys(data: object, path: str = "") -> list[str]:
    found = []
    if isinstance(data, dict):
        for key, value in data.items():
            current = f"{path}.{key}" if path else key
            if isinstance(key, str) and key.lower() in SENSITIVE_KEYS:
                found.append(f"Sensitive key found: {current}")
            found.extend(find_sensitive_keys(value, current))
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            found.extend(find_sensitive_keys(item, f"{path}[{idx}]"))
    return found


def check_resume_for_sensitive_data(path: Path, root: Path) -> list[str]:
    errors = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        # JSON validity is reported separately.
        return errors
    errors.extend(find_sensitive_keys(data))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate AI-readable endpoints in a built Jekyll site."
    )
    parser.add_argument(
        "root",
        nargs="?",
        default="_site",
        help="Root directory of the built site (default: _site)",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()

    if not root.is_dir():
        print(f"Missing directory: {root}. Build the site before running.")
        return 1

    findings: list[str] = []

    findings.extend(check_required_files(root))

    resume_json = root / "ai" / "resume.json"
    if resume_json.exists():
        findings.extend(check_json_file(resume_json, root))
        findings.extend(check_resume_for_sensitive_data(resume_json, root))

    resume_yml = root / "ai" / "resume.yml"
    if resume_yml.exists():
        findings.extend(check_yaml_file(resume_yml, root))

    if findings:
        print("AI endpoint validation failed:")
        for item in findings:
            print(f"- {item}")
        return 1

    print("AI endpoint validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
