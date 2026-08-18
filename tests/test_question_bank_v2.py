from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ROADMAP_PATH = ROOT / "_data/career/roadmap.yml"
BANK_PATH = ROOT / "_data/career/question_bank.yml"
RUNTIME_PATH = ROOT / "assets/js/interview-question-bank.js"
QUESTIONS_PAGE = ROOT / "labs/interview-readiness/questions/index.md"
PRACTICE_PAGE = ROOT / "labs/interview-readiness/practice/index.md"

QUESTION_TYPES = {"explain", "diagnose", "design", "challenge"}
EXPECTED_TRACKS = {"sales", "logistics", "integration", "ai", "delivery", "leadership"}


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_question_bank_covers_every_roadmap_skill_once():
    roadmap = load_yaml(ROADMAP_PATH)
    bank = load_yaml(BANK_PATH)

    roadmap_skills = roadmap["skills"]
    roadmap_ids = {skill["id"] for skill in roadmap_skills}
    bank_ids = [group["skill_id"] for group in bank["skills"]]

    assert len(roadmap_skills) == 42
    assert len(bank_ids) == 42
    assert len(bank_ids) == len(set(bank_ids))
    assert set(bank_ids) == roadmap_ids
    assert {skill["track"] for skill in roadmap_skills} == EXPECTED_TRACKS


def test_every_skill_has_four_lead_question_types():
    bank = load_yaml(BANK_PATH)
    assert bank["version"] == 2
    assert set(bank["types"]) == QUESTION_TYPES

    prompts = []
    for group in bank["skills"]:
        questions = group["questions"]
        assert len(questions) == 4, group["skill_id"]
        assert {item["type"] for item in questions} == QUESTION_TYPES, group["skill_id"]
        for item in questions:
            prompt = item["prompt"].strip()
            assert len(prompt) >= 70, (group["skill_id"], item["type"])
            assert prompt.endswith(("?", ".")), (group["skill_id"], item["type"])
            prompts.append(prompt)

    assert len(prompts) == 168
    assert len(prompts) == len(set(prompts))


def test_question_types_define_pressure_and_evidence_contract():
    bank = load_yaml(BANK_PATH)
    for type_id, item in bank["types"].items():
        assert item["label"]
        assert len(item["pressure"].strip()) >= 60, type_id
        assert len(item["evidence"].strip()) >= 60, type_id


def test_every_question_skill_has_career_evidence_sources():
    roadmap = load_yaml(ROADMAP_PATH)
    skills = {skill["id"]: skill for skill in roadmap["skills"]}
    bank = load_yaml(BANK_PATH)

    for group in bank["skills"]:
        sources = skills[group["skill_id"]].get("sources") or []
        assert sources, group["skill_id"]
        for source in sources:
            assert source.get("label"), group["skill_id"]
            assert str(source.get("href", "")).startswith("/"), group["skill_id"]


def test_runtime_joins_question_bank_to_roadmap_instead_of_copying_sources():
    script = RUNTIME_PATH.read_text(encoding="utf-8")
    assert "site.data.career.question_bank" in script
    assert "site.data.career.roadmap.skills" in script
    assert "skill.sources || []" in script
    assert "delivery: 'Delivery & Operations'" in script
    assert "count = 12" in script


def test_question_and_practice_pages_use_question_bank_v2():
    questions = QUESTIONS_PAGE.read_text(encoding="utf-8")
    practice = PRACTICE_PAGE.read_text(encoding="utf-8")

    for text in (questions, practice):
        assert '/assets/js/interview-readiness.js' in text
        assert '/assets/js/interview-question-bank.js' in text

    assert "42 skills / 168 questions" in questions
    assert "ir-type-filter" in questions
    assert "ir-skill-filter" in questions
    assert "Pressure follow-up" in questions
    assert "Evidence target" in questions

    assert "Twelve questions" in practice
    assert "IR.shuffledQuestions(12)" in practice
    assert "Open pressure follow-up" in practice
    assert "skill_id:q.skill_id" in practice
    assert "type:q.type" in practice
