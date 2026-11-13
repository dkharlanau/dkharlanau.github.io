#!/usr/bin/env python3
"""Prepare exact Pages deployment inputs for the IndexNow workflow."""

import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess
import tarfile

PAGES_WORKFLOWS = {"dynamic/pages/pages-build-deployment", ".github/workflows/publish-stable-pages.yml"}
RELEASE_ARTIFACT = "indexnow-production-release"


def gh(*args):
    return subprocess.check_output(["gh", *args], text=True)


def api(route):
    return json.loads(gh("api", route))


def pages_artifact(repo, status, commit, destination):
    match = re.fullmatch(
        rf"https://github\.com/{re.escape(repo)}/actions/runs/(\d+)/job/\d+",
        status["log_url"],
    )
    if match is None:
        raise ValueError("Pages deployment lacks a supported build run URL")
    run_id = match[1]
    run = api(f"repos/{repo}/actions/runs/{run_id}")
    if run["path"] not in PAGES_WORKFLOWS or run["head_branch"] != "main" or run["head_sha"] != commit:
        raise ValueError("Pages artifact source does not match the deployment")
    artifacts = api(f"repos/{repo}/actions/runs/{run_id}/artifacts")["artifacts"]
    candidates = [a for a in artifacts if a["name"] == "github-pages" and not a["expired"]]
    if len(candidates) != 1:
        raise FileNotFoundError(f"Missing Pages artifact from run {run_id}")
    artifact = candidates[0]
    destination.mkdir(parents=True)
    gh("run", "download", run_id, "--repo", repo, "--name", "github-pages", "--dir", str(destination))
    archive = destination / "artifact.tar"
    with tarfile.open(archive) as tar:
        for member in tar:
            path = destination / member.name
            if not member.isfile() or path.suffix not in {".html", ".xml"}:
                continue
            if destination.resolve() not in path.resolve().parents or path.exists():
                raise ValueError(f"Invalid Pages artifact member: {member.name}")
            path.parent.mkdir(parents=True, exist_ok=True)
            with tar.extractfile(member) as source, path.open("xb") as target:
                shutil.copyfileobj(source, target)
    archive.unlink()
    return {"id": artifact["id"], "run": int(run_id), "digest": artifact.get("digest")}


def deployed(repo, limit=2):
    deployments = api(f"repos/{repo}/deployments?environment=github-pages&ref=main&per_page=12")
    successful = []
    for deployment in deployments:
        statuses = api(f"repos/{repo}/deployments/{deployment['id']}/statuses")
        receipt = next((s for s in statuses if s["state"] == "success"), None)
        if receipt:
            successful.append((deployment, receipt, statuses[0]["state"]))
        if len(successful) == limit:
            break
    if not successful or successful[0][2] != "success":
        raise ValueError("No active successful production Pages deployment")
    return successful


def prepare(repo, event, root):
    root.mkdir(parents=True)
    active, *previous = deployed(repo)
    deployment, status, _ = active
    if "deployment" in event and event["deployment"]["id"] != deployment["id"]:
        return {"state": "superseded", "deployment": event["deployment"]["id"]}
    current = pages_artifact(repo, status, deployment["sha"], root / "current")
    result = {
        "state": "ready", "commit": deployment["sha"], "deployment": deployment["id"], "artifact": current,
        "baseline": None,
    }
    # Only successful production processing uploads this artifact. Failed
    # deliveries keep the preceding baseline available for the next release.
    history = api(f"repos/{repo}/actions/artifacts?name={RELEASE_ARTIFACT}&per_page=20")["artifacts"]
    production = [a for a in history if a["workflow_run"]["head_branch"] == "main"]
    latest = max(production, key=lambda a: a["created_at"], default=None)
    if latest and latest["expired"]:
        raise ValueError("Previous IndexNow release artifact expired; restore its manifest before retrying")
    if latest:
        run = str(latest["workflow_run"]["id"])
        run_info = api(f"repos/{repo}/actions/runs/{run}")
        if run_info["path"] != ".github/workflows/indexnow.yml" or run_info["event"] not in {"deployment_status", "workflow_dispatch"}:
            raise ValueError("Unexpected source of the production release manifest")
        gh("run", "download", run, "--repo", repo, "--name", RELEASE_ARTIFACT, "--dir", str(root / "previous"))
        result["baseline"] = "accepted_manifest"
    elif previous:
        prior, prior_status, _ = previous[0]
        try:
            artifact = pages_artifact(repo, prior_status, prior["sha"], root / "previous-site")
        except FileNotFoundError:
            result["baseline"] = "initialize"
        else:
            result["baseline"] = "pages_artifact"
            result["prior"] = {"commit": prior["sha"], "deployment": prior["id"], "artifact": artifact}
    else:
        result["baseline"] = "initialize"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--event", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    event = json.loads(args.event.read_text(encoding="utf-8"))
    try:
        result = prepare(args.repo, event, args.output)
    except (KeyError, ValueError, OSError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"Unable to prepare Pages release: {exc}\n")
    (args.output / "release.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Pages release state: {result['state']}")


if __name__ == "__main__":
    main()
