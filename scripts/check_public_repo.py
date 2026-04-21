#!/usr/bin/env python3
"""Check tracked files for public-repo hygiene mistakes."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DISALLOWED_PATH_RE = re.compile(
    r"^(?:TRIZ-bytes|DAMA|LLM-prompts|agentic-bytes|transfer_datasets_[^/]+)(?:/|$)|"
    r"(^|/)(?:"
    r"_site|\.jekyll-cache|\.sass-cache|\.pytest_cache|__pycache__|"
    r"Complete_LinkedIn[^/]*|LinkedinComplete|LinkedInComplete"
    r")(?:/|$)|"
    r"(^|/)Basic_LinkedInDataExport_[^/]+\.zip(?:/|$)|"
    r"(^|/)\.env(?:\.|$)|"
    r"(^|/)li2resume\.local\.[^/]+$|"
    r"(^|/)scripts/li2resume\.config\.(?:json|ya?ml)$|"
    r"(^|/).*\.py[cod]$|"
    r"(^|/).*\.log$|"
    r"(^|/).*\.tmp$|"
    r"(^|/)LinkedIn?\.zip$|"
    r"(^|/)linkedin\.zip$",
    re.IGNORECASE,
)

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |DSA |EC |OPENSSH |PGP )?PRIVATE KEY-----"),
    re.compile(
        r"\b(?:api[_-]?key|client[_-]?secret|secret|password|passwd|private[_-]?key)\b"
        r"\s*[:=]\s*['\"]?(?!os\.(?:environ|getenv)\b)[^'\"\s]{8,}",
        re.I,
    ),
    re.compile(r"\b(?:authorization|bearer)\b\s*[:=]\s*['\"]?(?:bearer\s+)?[A-Za-z0-9._~+/=-]{16,}", re.I),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
]

LOCAL_REFERENCE_PATTERNS = [
    re.compile(r"\bBasic_LinkedInDataExport_\d{2}-\d{2}-\d{4}\.zip/", re.I),
]

TEXT_SUFFIXES = {
    ".cfg",
    ".css",
    ".csv",
    ".html",
    ".js",
    ".json",
    ".lock",
    ".md",
    ".py",
    ".rb",
    ".sh",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}


def git_lines(*args: str) -> list[str]:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return [line for line in result.stdout.splitlines() if line]


def is_text_candidate(path: str) -> bool:
    return Path(path).suffix.lower() in TEXT_SUFFIXES or Path(path).name in {
        ".gitignore",
        "Gemfile",
        "LICENSE",
        "LICENSE-DATA",
        "LLM.txt",
    }


def scan_secret_patterns(path: str) -> list[str]:
    if not is_text_candidate(path):
        return []
    file_path = ROOT / path
    if not file_path.exists():
        return []
    try:
        text = file_path.read_text(encoding="utf-8", errors="ignore")
    except OSError as exc:
        return [f"{path}: cannot read file ({exc})"]

    findings: list[str] = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        for pattern in SECRET_PATTERNS:
            if pattern.search(line):
                findings.append(f"{path}:{line_no}: possible secret or credential")
                break
        for pattern in LOCAL_REFERENCE_PATTERNS:
            if pattern.search(line):
                findings.append(f"{path}:{line_no}: local export path reference")
                break
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--staged", action="store_true", help="accepted for hook compatibility; scans tracked files")
    parser.parse_args()

    tracked = git_lines("ls-files")
    ignored_tracked = git_lines("ls-files", "-ci", "--exclude-standard")

    findings: list[str] = []
    findings.extend(f"{path}: tracked but ignored by .gitignore" for path in ignored_tracked)

    for path in tracked:
        if DISALLOWED_PATH_RE.search(path):
            findings.append(f"{path}: disallowed public tracked path")
        findings.extend(scan_secret_patterns(path))

    if findings:
        print("Public repo hygiene check failed:")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print(f"Public repo hygiene check passed for {len(tracked)} tracked files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
