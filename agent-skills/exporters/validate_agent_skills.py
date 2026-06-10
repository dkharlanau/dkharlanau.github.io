#!/usr/bin/env python3
"""
Validate agent skills in the agent-skills/ directory.

Usage:
    python3 agent-skills/exporters/validate_agent_skills.py

Exit codes:
    0 = all validations passed
    1 = one or more validations failed
"""

import os
import re
import sys
import yaml
from pathlib import Path

AGENT_SKILLS_DIR = Path("agent-skills")
SKILL_INDEX_PATH = AGENT_SKILLS_DIR / "skill-index.yml"
PROFILES_DIR = AGENT_SKILLS_DIR / "profiles"
SKILLS_DIR = AGENT_SKILLS_DIR / "skills"

REQUIRED_SKILL_SECTIONS = [
    "## Purpose",
    "## Use when",
    "## Do not use when",
    "## Required inputs",
    "## Workflow",
    "## Decision rules",
    "## Output format",
    "## Quality gates",
    "## References",
]


def error(msg: str) -> None:
    print(f"  ❌ {msg}")


def ok(msg: str) -> None:
    print(f"  ✅ {msg}")


def warn(msg: str) -> None:
    print(f"  ⚠️  {msg}")


def validate_yaml_frontmatter(skill_path: Path) -> dict:
    """Parse and validate YAML frontmatter from a SKILL.md file."""
    content = skill_path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        error(f"{skill_path}: missing YAML frontmatter")
        return {}

    parts = content.split("---", 2)
    if len(parts) < 3:
        error(f"{skill_path}: malformed YAML frontmatter")
        return {}

    try:
        frontmatter = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        error(f"{skill_path}: invalid YAML frontmatter: {e}")
        return {}

    if not isinstance(frontmatter, dict):
        error(f"{skill_path}: YAML frontmatter is not a dict")
        return {}

    if "name" not in frontmatter:
        error(f"{skill_path}: missing 'name' in frontmatter")
    else:
        ok(f"name: {frontmatter['name']}")

    if "description" not in frontmatter:
        error(f"{skill_path}: missing 'description' in frontmatter")
    else:
        desc = frontmatter["description"]
        if not desc or len(desc.strip()) < 20:
            error(f"{skill_path}: description is too short or empty")
        elif "use when" not in desc.lower() and "use this" not in desc.lower():
            warn(f"{skill_path}: description may lack trigger words")
        else:
            ok(f"description is present and has trigger words")

    return frontmatter


def validate_skill_sections(skill_path: Path) -> bool:
    """Check that all required sections are present in SKILL.md."""
    content = skill_path.read_text(encoding="utf-8")
    missing = []
    for section in REQUIRED_SKILL_SECTIONS:
        if section not in content:
            missing.append(section)
    if missing:
        error(f"{skill_path}: missing sections: {', '.join(missing)}")
        return False
    ok(f"{skill_path.name}: all required sections present")
    return True


def validate_references(skill_dir: Path) -> bool:
    """Check that references/ folder has method.md, templates.md, examples.md."""
    refs_dir = skill_dir / "references"
    required_files = ["method.md", "templates.md", "examples.md"]
    missing = []
    for fname in required_files:
        fpath = refs_dir / fname
        if not fpath.exists():
            missing.append(fname)
        elif fpath.stat().st_size < 100:
            warn(f"{fpath} is very short ({fpath.stat().st_size} bytes)")
    if missing:
        error(f"{skill_dir.name}: missing reference files: {', '.join(missing)}")
        return False
    ok(f"{skill_dir.name}: all reference files present")
    return True


def validate_skill_index() -> tuple[set[str], bool]:
    """Validate skill-index.yml structure and content."""
    if not SKILL_INDEX_PATH.exists():
        error(f"skill-index.yml not found at {SKILL_INDEX_PATH}")
        return set(), False

    try:
        data = yaml.safe_load(SKILL_INDEX_PATH.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        error(f"skill-index.yml: invalid YAML: {e}")
        return set(), False

    if "skills" not in data or not isinstance(data["skills"], list):
        error("skill-index.yml: missing or invalid 'skills' list")
        return set(), False

    indexed_skills = set()
    all_ok = True
    for entry in data["skills"]:
        name = entry.get("name")
        if not name:
            error("skill-index.yml entry missing 'name'")
            all_ok = False
            continue
        indexed_skills.add(name)

        for field in ["title", "category", "source_page", "path", "outputs", "tags"]:
            if field not in entry:
                error(f"skill-index.yml entry '{name}': missing '{field}'")
                all_ok = False

        # Check source_page exists
        source_page = entry.get("source_page", "")
        if source_page and not Path(source_page).exists():
            warn(f"skill-index.yml entry '{name}': source_page '{source_page}' does not exist")

        # Check path exists
        path = entry.get("path", "")
        if path and not Path(path).exists():
            error(f"skill-index.yml entry '{name}': path '{path}' does not exist")
            all_ok = False

    ok(f"skill-index.yml: {len(indexed_skills)} skills indexed")
    return indexed_skills, all_ok


def validate_profiles(indexed_skills: set[str]) -> bool:
    """Validate all profile YAML files."""
    if not PROFILES_DIR.exists():
        error(f"profiles directory not found: {PROFILES_DIR}")
        return False

    all_ok = True
    for profile_path in sorted(PROFILES_DIR.glob("*.yml")):
        try:
            data = yaml.safe_load(profile_path.read_text(encoding="utf-8"))
        except yaml.YAMLError as e:
            error(f"{profile_path.name}: invalid YAML: {e}")
            all_ok = False
            continue

        if not isinstance(data, dict):
            error(f"{profile_path.name}: root is not a dict")
            all_ok = False
            continue

        for field in ["profile", "description", "skills"]:
            if field not in data:
                error(f"{profile_path.name}: missing '{field}'")
                all_ok = False

        skills = data.get("skills", [])
        if not isinstance(skills, list):
            error(f"{profile_path.name}: 'skills' is not a list")
            all_ok = False
            continue

        for skill_name in skills:
            if skill_name not in indexed_skills:
                error(f"{profile_path.name}: references unknown skill '{skill_name}'")
                all_ok = False

        ok(f"{profile_path.name}: valid profile with {len(skills)} skills")

    return all_ok


def validate_skills() -> tuple[set[str], bool]:
    """Validate all skill directories."""
    if not SKILLS_DIR.exists():
        error(f"skills directory not found: {SKILLS_DIR}")
        return set(), False

    all_ok = True
    found_skills = set()

    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue

        skill_name = skill_dir.name
        found_skills.add(skill_name)
        skill_md = skill_dir / "SKILL.md"

        if not skill_md.exists():
            error(f"{skill_name}: missing SKILL.md")
            all_ok = False
            continue

        frontmatter = validate_yaml_frontmatter(skill_md)
        if frontmatter.get("name") != skill_name:
            warn(f"{skill_name}: frontmatter name '{frontmatter.get('name')}' does not match directory name")

        if not validate_skill_sections(skill_md):
            all_ok = False

        if not validate_references(skill_dir):
            all_ok = False

    return found_skills, all_ok


def check_private_paths() -> bool:
    """Check that no private paths are exposed in skill files."""
    all_ok = True
    suspicious_patterns = [
        r"/Users/\w+",
        r"/home/\w+",
        r"C:\\Users\\\w+",
        r"\.env",
        r"password\s*=",
        r"secret\s*=",
        r"token\s*=",
    ]

    for skill_dir in SKILLS_DIR.iterdir():
        if not skill_dir.is_dir():
            continue
        for md_file in skill_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            for pattern in suspicious_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    warn(f"{md_file}: may contain private path or secret pattern: {pattern}")
                    # Not a hard fail, just a warning

    ok("Private path scan completed")
    return all_ok


def main() -> int:
    print("=" * 60)
    print("Agent Skills Validation")
    print("=" * 60)

    exit_code = 0

    print("\n📋 Validating skill-index.yml...")
    indexed_skills, index_ok = validate_skill_index()
    if not index_ok:
        exit_code = 1

    print("\n📁 Validating skill directories...")
    found_skills, skills_ok = validate_skills()
    if not skills_ok:
        exit_code = 1

    print("\n🔗 Checking skill-index coverage...")
    missing_from_index = found_skills - indexed_skills
    extra_in_index = indexed_skills - found_skills
    if missing_from_index:
        error(f"Skills not in skill-index.yml: {', '.join(missing_from_index)}")
        exit_code = 1
    if extra_in_index:
        error(f"Skills in skill-index.yml but no directory: {', '.join(extra_in_index)}")
        exit_code = 1
    if not missing_from_index and not extra_in_index:
        ok("All skills are indexed and all indexed skills exist")

    print("\n👤 Validating profiles...")
    profiles_ok = validate_profiles(indexed_skills)
    if not profiles_ok:
        exit_code = 1

    print("\n🔒 Checking for private path exposure...")
    check_private_paths()

    print("\n" + "=" * 60)
    if exit_code == 0:
        print("✅ All validations passed.")
    else:
        print("❌ Some validations failed. See details above.")
    print("=" * 60)

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
