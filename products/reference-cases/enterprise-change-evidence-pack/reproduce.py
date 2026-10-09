#!/usr/bin/env python3
"""Reproduce retained outputs using prepared, pinned sibling checkouts. No downloads."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys

from normalize_render import normalize
from validate import ROOT, load_json, sha256_file, validate_case


REPOSITORIES = {
    "signal-to-insight": "STI_REPO",
    "enterprise-architecture-composer": "EAC_REPO",
    "visual-workbench": "VW_REPO",
    "project-evidence-graph": "PEG_REPO",
}
OUTPUTS = {
    "architecture.blueprint.json": "artifacts/architecture.blueprint.json",
    "architecture.visual.md": "artifacts/architecture.visual.txt",
    "architecture.executive.svg": "artifacts/architecture.executive.svg",
    "project-evidence.analysis.json": "artifacts/project-evidence.analysis.json",
}


class ReproductionError(ValueError):
    pass


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    if result.returncode:
        raise ReproductionError(f"{repo.name}: Git check failed; use a prepared repository checkout")
    return result.stdout.strip()


def verify_checkout(repo: Path, name: str, expected: str) -> None:
    if not re.fullmatch(r"[0-9a-f]{40}", expected):
        raise ReproductionError(f"{name}: invalid commit pin")
    actual = git(repo, "rev-parse", "HEAD")
    if actual != expected:
        raise ReproductionError(f"{name}: expected {expected}, found {actual}; prepare a separate pinned checkout")
    if git(repo, "status", "--porcelain", "--untracked-files=all"):
        raise ReproductionError(f"{name}: checkout is dirty; use a clean pinned checkout")


def check_output_path(output: Path, repositories: dict[str, Path]) -> None:
    if output.exists():
        raise ReproductionError("output directory already exists; choose a new directory to retain earlier results")
    for source in [ROOT.parents[2], *repositories.values()]:
        if output == source or source in output.parents:
            raise ReproductionError("output must be outside the site and sibling checkouts")


def compare_output(output: Path, relative: str) -> dict:
    expected = ROOT / relative
    if not output.is_file() or output.read_bytes() != expected.read_bytes():
        raise ReproductionError(f"{relative}: byte mismatch; stop and review, do not update retained hashes")
    return {"retained_path": relative, "sha256": sha256_file(output), "bytes": output.stat().st_size}


def reproduce(output: Path, repositories: dict[str, Path]) -> None:
    check_output_path(output, repositories)
    output.mkdir(parents=True)
    receipt = {
        "schema_version": "1.0.0", "case_id": "enterprise-change-evidence-pack",
        "status": "failed", "scope": "Pinned reproduction only; no approval or latest-version compatibility claim.",
        "repositories": {}, "steps": [], "outputs": {},
    }

    def run(label: str, command: list[str], destination: Path | None = None) -> str:
        result = subprocess.run(command, capture_output=True, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
        (output / f"{label}.stdout.log").write_bytes(result.stdout)
        (output / f"{label}.stderr.log").write_bytes(result.stderr)
        receipt["steps"].append({"id": label, "exit_code": result.returncode})
        if result.returncode:
            raise ReproductionError(f"{label} failed (exit {result.returncode}); inspect the retained logs")
        if destination is not None:
            destination.write_bytes(result.stdout)
        return result.stdout.decode("utf-8").strip()

    try:
        lock = load_json(ROOT / "runtime-lock.json")
        if lock.get("schema_version") != "1.0.0" or lock.get("case_id") != "enterprise-change-evidence-pack":
            raise ReproductionError("unsupported runtime lock schema or case")
        if set(lock.get("repositories", {})) != set(REPOSITORIES):
            raise ReproductionError("runtime lock must declare exactly the four participating repositories")
        errors = validate_case()
        if errors:
            raise ReproductionError("retained pack validation failed: " + "; ".join(errors))
        for name, repo in repositories.items():
            record = lock["repositories"][name]
            verify_checkout(repo, name, record["commit"])
            receipt["repositories"][name] = record
        receipt["runtime_lock_sha256"] = sha256_file(ROOT / "runtime-lock.json")
        receipt["manifest_sha256"] = sha256_file(ROOT / "manifest.json")
        receipt["inventory_sha256"] = sha256_file(ROOT / "expected-artifacts.json")
        receipt["inputs"] = {
            record["path"]: {"sha256": record["sha256"], "bytes": record["bytes"]}
            for record in load_json(ROOT / "expected-artifacts.json")["files"]
        }
        receipt["python"] = sys.version.split()[0]
        if sys.version_info < (3, 10):
            raise ReproductionError("Python 3.10 or later is required")
        receipt["node"] = run("node-version", ["node", "--version"])
        if int(receipt["node"].lstrip("v").split(".")[0]) < 20:
            raise ReproductionError("Node.js 20 or later is required")
        vw = repositories["visual-workbench"]
        if sha256_file(vw / "package-lock.json") != lock["visual_workbench_package_lock_sha256"]:
            raise ReproductionError("Visual Workbench dependency lock differs from the baseline")
        compiler = vw / "node_modules" / "typescript" / "bin" / "tsc"
        if not compiler.is_file():
            raise ReproductionError("Visual Workbench dependencies are missing; follow the preparation guide")
        # Compile the pinned source before use; never trust an old ignored dist directory.
        run("visual-build", ["node", str(compiler), "-p", str(vw / "tsconfig.json")])
        run("research-validate", [sys.executable, str(repositories["signal-to-insight"] / "sti.py"),
            "handoff", "validate", str(ROOT / "fixtures/research-context.json")])
        eac = str(repositories["enterprise-architecture-composer"] / "bin/eac.mjs")
        context = str(ROOT / "fixtures/architecture-context.json")
        run("composer-blueprint", ["node", eac, "compose", context], output / "architecture.blueprint.json")
        receipt["outputs"]["architecture.blueprint.json"] = compare_output(output / "architecture.blueprint.json", OUTPUTS["architecture.blueprint.json"])
        run("composer-visual", ["node", eac, "visual", context, "--markdown", "--output", str(output / "architecture.visual.md")])
        receipt["outputs"]["architecture.visual.md"] = compare_output(output / "architecture.visual.md", OUTPUTS["architecture.visual.md"])
        cli = str(vw / "dist/cli.js")
        run("visual-validate", ["node", cli, "validate", str(output / "architecture.visual.md")])
        run("visual-render", ["node", cli, "render", str(output / "architecture.visual.md"),
            "--view", "executive", "--output", str(output / "architecture.executive.svg")])
        normalize(output / "architecture.executive.svg")
        run("project-analysis", [sys.executable, str(repositories["project-evidence-graph"] / "evidence_graph.py"),
            str(ROOT / "fixtures/project-evidence.json"), "analyze"], output / "project-evidence.analysis.json")
        for name, relative in OUTPUTS.items():
            receipt["outputs"][name] = compare_output(output / name, relative)
        for name, repo in repositories.items():
            verify_checkout(repo, name, lock["repositories"][name]["commit"])
        if validate_case():
            raise ReproductionError("retained pack changed during reproduction")
        receipt["status"] = "passed"
    except (OSError, ValueError, KeyError, TypeError) as exc:
        receipt["error"] = str(exc)
        raise ReproductionError(str(exc)) from exc
    finally:
        (output / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="New directory outside all source checkouts")
    args = parser.parse_args()
    missing = [env for env in REPOSITORIES.values() if not os.environ.get(env)]
    if missing:
        parser.error("set prepared checkout paths: " + ", ".join(missing))
    repositories = {name: Path(os.environ[env]).resolve() for name, env in REPOSITORIES.items()}
    try:
        reproduce(args.output.resolve(), repositories)
    except (OSError, ValueError) as exc:
        print(f"Reproduction failed: {exc}", file=sys.stderr)
        return 1
    print(f"PASS: four retained outputs match exactly; receipt: {args.output / 'receipt.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
