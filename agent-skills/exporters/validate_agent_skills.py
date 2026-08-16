#!/usr/bin/env python3
"""Validate portable agent skills, index fragments, profiles, and public-safety basics."""

import re
import sys
import yaml
from pathlib import Path

from index_loader import load_skill_index

AGENT_SKILLS_DIR = Path("agent-skills")
PROFILES_DIR = AGENT_SKILLS_DIR / "profiles"
SKILLS_DIR = AGENT_SKILLS_DIR / "skills"

REQUIRED_SKILL_SECTIONS = [
    "## Purpose", "## Use when", "## Do not use when", "## Required inputs",
    "## Workflow", "## Decision rules", "## Output format", "## Quality gates",
    "## References",
]


def error(msg: str) -> None:
    print(f"  ❌ {msg}")


def ok(msg: str) -> None:
    print(f"  ✅ {msg}")


def warn(msg: str) -> None:
    print(f"  ⚠️  {msg}")


def validate_frontmatter(skill_path: Path) -> tuple[dict, bool]:
    content = skill_path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        error(f"{skill_path}: missing YAML frontmatter")
        return {}, False
    parts = content.split("---", 2)
    if len(parts) < 3:
        error(f"{skill_path}: malformed YAML frontmatter")
        return {}, False
    try:
        data = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:
        error(f"{skill_path}: invalid YAML frontmatter: {exc}")
        return {}, False
    if not isinstance(data, dict):
        error(f"{skill_path}: YAML frontmatter is not a mapping")
        return {}, False
    valid = True
    name = data.get("name")
    desc = data.get("description", "")
    if not name:
        error(f"{skill_path}: missing 'name'")
        valid = False
    if not isinstance(desc, str) or len(desc.strip()) < 20:
        error(f"{skill_path}: description is too short or empty")
        valid = False
    elif "use when" not in desc.lower() and "use this" not in desc.lower():
        warn(f"{skill_path}: description may lack trigger words")
    return data, valid


def validate_index() -> tuple[set[str], bool]:
    try:
        data = load_skill_index(AGENT_SKILLS_DIR)
    except (FileNotFoundError, ValueError, yaml.YAMLError) as exc:
        error(f"agent skill index: {exc}")
        return set(), False
    indexed = set()
    valid = True
    for entry in data.get("skills", []):
        name = entry.get("name")
        if not name:
            error("skill index entry missing 'name'")
            valid = False
            continue
        indexed.add(name)
        for field in ["title", "category", "source_page", "path", "outputs", "tags"]:
            if field not in entry:
                error(f"skill index entry '{name}': missing '{field}'")
                valid = False
        source_page = entry.get("source_page", "")
        if source_page and not Path(source_page).exists():
            warn(f"skill index entry '{name}': source_page '{source_page}' does not exist")
        path = entry.get("path", "")
        if path and not Path(path).exists():
            error(f"skill index entry '{name}': path '{path}' does not exist")
            valid = False
    ok(f"skill indexes: {len(indexed)} skills indexed")
    return indexed, valid


def validate_profiles(indexed: set[str]) -> bool:
    valid = True
    for profile_path in sorted(PROFILES_DIR.glob("*.yml")):
        try:
            data = yaml.safe_load(profile_path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            error(f"{profile_path.name}: invalid YAML: {exc}")
            valid = False
            continue
        if not isinstance(data, dict):
            error(f"{profile_path.name}: root is not a mapping")
            valid = False
            continue
        for field in ["profile", "description", "skills"]:
            if field not in data:
                error(f"{profile_path.name}: missing '{field}'")
                valid = False
        skills = data.get("skills", [])
        if not isinstance(skills, list):
            error(f"{profile_path.name}: 'skills' is not a list")
            valid = False
            continue
        for name in skills:
            if name not in indexed:
                error(f"{profile_path.name}: references unknown skill '{name}'")
                valid = False
        ok(f"{profile_path.name}: valid profile with {len(skills)} skills")
    return valid


def validate_skills() -> tuple[set[str], bool]:
    found = set()
    valid = True
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        found.add(skill_dir.name)
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            error(f"{skill_dir.name}: missing SKILL.md")
            valid = False
            continue
        frontmatter, frontmatter_ok = validate_frontmatter(skill_md)
        if not frontmatter_ok:
            valid = False
        if frontmatter.get("name") != skill_dir.name:
            warn(f"{skill_dir.name}: frontmatter name does not match directory")
        content = skill_md.read_text(encoding="utf-8")
        missing = [section for section in REQUIRED_SKILL_SECTIONS if section not in content]
        if missing:
            error(f"{skill_dir.name}: missing sections: {', '.join(missing)}")
            valid = False
        refs = skill_dir / "references"
        for fname in ["method.md", "templates.md", "examples.md"]:
            path = refs / fname
            if not path.exists():
                error(f"{skill_dir.name}: missing reference file {fname}")
                valid = False
            elif path.stat().st_size < 100:
                warn(f"{path}: very short reference file")
        ok(f"{skill_dir.name}: portable skill checked")
    return found, valid


def check_private_paths() -> None:
    patterns = [r"/Users/\w+", r"/home/\w+", r"C:\\Users\\\w+", r"\.env", r"password\s*=", r"secret\s*=", r"token\s*="]
    for skill_dir in SKILLS_DIR.iterdir():
        if not skill_dir.is_dir():
            continue
        for md_file in skill_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            for pattern in patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    warn(f"{md_file}: may contain private path or secret pattern: {pattern}")
    ok("Private path scan completed")


def main() -> int:
    print("=" * 60)
    print("Agent Skills Validation")
    print("=" * 60)
    exit_code = 0

    indexed, index_ok = validate_index()
    found, skills_ok = validate_skills()
    if not index_ok or not skills_ok:
        exit_code = 1

    missing = found - indexed
    extra = indexed - found
    if missing:
        error(f"Skills not indexed: {', '.join(sorted(missing))}")
        exit_code = 1
    if extra:
        error(f"Indexed skills without directory: {', '.join(sorted(extra))}")
        exit_code = 1
    if not missing and not extra:
        ok("All skills are indexed and all indexed skills exist")

    if not validate_profiles(indexed):
        exit_code = 1
    check_private_paths()

    print("=" * 60)
    print("✅ All validations passed." if exit_code == 0 else "❌ Some validations failed.")
    print("=" * 60)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
