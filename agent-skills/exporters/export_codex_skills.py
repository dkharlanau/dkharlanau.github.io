#!/usr/bin/env python3
"""
Export selected agent skills into .agents/skills/ for Codex.

Usage:
    python3 agent-skills/exporters/export_codex_skills.py --profile sap-ams
    python3 agent-skills/exporters/export_codex_skills.py --profile data-governance
    python3 agent-skills/exporters/export_codex_skills.py --all

This script reads agent-skills/skill-index.yml and the selected profile,
then copies the matching skills into .agents/skills/<skill-name>/.
"""

import argparse
import shutil
import sys
import yaml
from pathlib import Path

AGENT_SKILLS_DIR = Path("agent-skills")
PROFILES_DIR = AGENT_SKILLS_DIR / "profiles"
SKILLS_DIR = AGENT_SKILLS_DIR / "skills"
CODEX_SKILLS_DIR = Path(".agents") / "skills"


def load_skill_index() -> dict:
    index_path = AGENT_SKILLS_DIR / "skill-index.yml"
    if not index_path.exists():
        print(f"Error: {index_path} not found", file=sys.stderr)
        sys.exit(1)
    return yaml.safe_load(index_path.read_text(encoding="utf-8"))


def load_profile(profile_name: str) -> list[str]:
    profile_path = PROFILES_DIR / f"{profile_name}.yml"
    if not profile_path.exists():
        print(f"Error: profile '{profile_name}' not found at {profile_path}", file=sys.stderr)
        sys.exit(1)
    data = yaml.safe_load(profile_path.read_text(encoding="utf-8"))
    return data.get("skills", [])


def export_skill(skill_name: str, skill_index: dict) -> None:
    source_dir = SKILLS_DIR / skill_name
    if not source_dir.exists():
        print(f"Warning: skill directory not found: {source_dir}", file=sys.stderr)
        return

    target_dir = CODEX_SKILLS_DIR / skill_name
    if target_dir.exists():
        shutil.rmtree(target_dir)

    shutil.copytree(source_dir, target_dir)
    print(f"  Exported: {skill_name} -> {target_dir}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Export agent skills to .agents/skills/")
    parser.add_argument("--profile", help="Profile name to export (e.g., sap-ams)")
    parser.add_argument("--all", action="store_true", help="Export all skills")
    args = parser.parse_args()

    if not args.profile and not args.all:
        parser.print_help()
        return 1

    skill_index = load_skill_index()
    all_skills = {entry["name"] for entry in skill_index.get("skills", [])}

    if args.all:
        skills_to_export = sorted(all_skills)
    else:
        profile_skills = load_profile(args.profile)
        skills_to_export = sorted(set(profile_skills) & all_skills)
        unknown = set(profile_skills) - all_skills
        if unknown:
            print(f"Warning: profile references unknown skills: {', '.join(unknown)}", file=sys.stderr)

    if not skills_to_export:
        print("No skills to export.")
        return 1

    CODEX_SKILLS_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Exporting {len(skills_to_export)} skill(s) to {CODEX_SKILLS_DIR}...")
    for skill_name in skills_to_export:
        export_skill(skill_name, skill_index)

    print(f"\nDone. Exported {len(skills_to_export)} skill(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
