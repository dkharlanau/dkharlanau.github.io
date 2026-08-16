#!/usr/bin/env python3
"""Load the base agent skill index plus optional fragment files."""

from pathlib import Path
import yaml


def load_skill_index(agent_skills_dir: Path) -> dict:
    paths = [agent_skills_dir / "skill-index.yml"]
    fragments = agent_skills_dir / "skill-index.d"
    if fragments.exists():
        paths.extend(sorted(fragments.glob("*.yml")))

    skills = []
    seen = {}
    for path in paths:
        if not path.exists():
            if path.name == "skill-index.yml":
                raise FileNotFoundError(path)
            continue
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        entries = data.get("skills", [])
        if not isinstance(entries, list):
            raise ValueError(f"{path}: 'skills' must be a list")
        for entry in entries:
            if not isinstance(entry, dict):
                raise ValueError(f"{path}: each skill entry must be a mapping")
            name = entry.get("name")
            if name in seen:
                raise ValueError(f"duplicate skill '{name}' in {seen[name]} and {path}")
            if name:
                seen[name] = path
            skills.append(entry)
    return {"skills": skills}
