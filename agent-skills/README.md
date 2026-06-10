# Agent Skills

Portable, installable agent skill packages for enterprise consulting, business analysis, data governance, architecture, integration, and SAP AMS operations.

## What this is

This directory contains **agent skills** — compact operational instruction sets designed for AI agents (Claude Code, Codex, and similar tools). They are the agent-facing counterpart to the human-readable [Skill Hub](../skill-hub/) pages.

| Human page | Agent skill |
|------------|-------------|
| Rich explanation, examples, context | Compact operational instructions |
| Templates and related links | Trigger description, workflow, decision rules |
| Quality checklist for humans | Quality gates for agent output |
| Agent instructions section | Full SKILL.md with required inputs and output format |

Both share the same professional method, but they serve different audiences.

## Structure

```text
agent-skills/
  README.md                 # This file
  skill-index.yml           # Metadata for all agent skills
  profiles/                 # Role-based skill collections
    data-governance.yml
    business-analysis.yml
    solution-architecture.yml
    integration-architecture.yml
    sap-ams.yml
    full-professional.yml
  skills/                   # Individual agent skill packages
    <skill-name>/
      SKILL.md              # Compact operational instructions
      references/
        method.md           # Detailed method
        templates.md        # Copy-ready artifact templates
        examples.md         # Good/bad examples
  exporters/                # Export scripts
    validate_agent_skills.py
    export_codex_skills.py
    export_claude_skills.py
```

## How to install for Codex

Export skills by profile or all at once:

```bash
# Export a specific profile
python3 agent-skills/exporters/export_codex_skills.py --profile sap-ams

# Export another profile
python3 agent-skills/exporters/export_codex_skills.py --profile integration-architecture

# Export all skills
python3 agent-skills/exporters/export_codex_skills.py --all
```

This copies selected skills into `.agents/skills/<skill-name>/`, where Codex can discover and use them.

## How to install for Claude Code

```bash
# Export a specific profile
python3 agent-skills/exporters/export_claude_skills.py --profile sap-ams

# Export another profile
python3 agent-skills/exporters/export_claude_skills.py --profile data-governance

# Export all skills
python3 agent-skills/exporters/export_claude_skills.py --all
```

This copies selected skills into `.claude/skills/<skill-name>/`, where Claude Code can discover and use them.

## How to use profiles

Profiles are role-based skill collections. They help you install only the skills relevant to your current work:

| Profile | Skills | Use case |
|---------|--------|----------|
| `data-governance` | data-quality-root-cause, data-governance-ownership | Data quality and governance work |
| `business-analysis` | requirements-elicitation, acceptance-criteria | Business analysis and requirements |
| `solution-architecture` | architecture-decision-record | Architecture decisions |
| `integration-architecture` | interface-ownership, integration-observability | Integration design and operations |
| `sap-ams` | incident-triage, root-cause-analysis, change-impact-analysis, operational-knowledge-capture, recurring-ticket-pattern-analysis, interface-ownership, data-quality-root-cause | SAP AMS operations |
| `full-professional` | All 12 skills | Complete professional set |

## How to validate skills

Run the validation script before committing changes:

```bash
python3 agent-skills/exporters/validate_agent_skills.py
```

This checks:
- Every skill has `SKILL.md` with valid YAML frontmatter
- Every skill has `name` and `description`
- Every skill has required sections
- Every skill has reference files
- Every skill is indexed in `skill-index.yml`
- Every profile references existing skills
- No broken local source page paths
- No private paths exposed

## How to add a new skill

1. Create a new directory under `agent-skills/skills/<skill-name>/`
2. Write `SKILL.md` with YAML frontmatter and required sections
3. Create `references/method.md`, `references/templates.md`, `references/examples.md`
4. Add the skill to `agent-skills/skill-index.yml`
5. Add the skill to relevant profiles in `agent-skills/profiles/`
6. Run `python3 agent-skills/exporters/validate_agent_skills.py`
7. Commit only the source files in `agent-skills/`. Do not commit generated exports.

## Why not all skills should be installed at once

Installing all skills at once can:
- Increase context window usage
- Reduce the agent's ability to select the right skill for the task
- Cause skill overlap confusion

Use profiles to install only the skills relevant to your current role or project.

## How to keep descriptions concise

Each `SKILL.md` description should:
- Front-load trigger words
- Explain when to use
- Explain when not to use if needed
- Stay under 200 words
- Avoid generic wording
- Make implicit invocation easier

Example:
```yaml
description: Use when investigating recurring data defects, failed validations, bad master data, migration data errors, duplicate records, or SAP/business process failures caused by missing, invalid, inconsistent, or poorly owned data. Do not use for generic data governance summaries.
```

## Safety rules

- **No private material.** Do not expose client names, ticket numbers, internal incident IDs, or proprietary system details.
- **No proprietary framework text.** Use your own words. Do not copy from DAMA-DMBOK, BABOK, TOGAF, or SAP documentation.
- **No fake citations.** Do not invent external links or validation results.
- **Separate facts from assumptions.** Label every assumption with a risk if it is wrong.
- **Separate decisions from open questions.** List open questions explicitly and assign discovery owners.
- **Do not commit generated exports.** `.agents/skills/` and `.claude/skills/` are generated targets. Commit only the source files in `agent-skills/`.

## Generated exports

The `.agents/skills/` and `.claude/skills/` directories are generated by the exporter scripts. They are not the source of truth. The source of truth is `agent-skills/skills/`.

If you need to update an exported skill:
1. Edit the source in `agent-skills/skills/<skill-name>/`
2. Re-run the exporter
3. Do not edit generated exports by hand

## License and limitations

These skills are public working interpretations of enterprise practices. They are not official framework documentation. Every skill includes a verification status and limitations section. Use them as structured starting points, not as authoritative substitutes.
