#!/usr/bin/env python3
"""Generate the downloadable SAP Lead assessment workbook from canonical site data.

The output is a real XLSX (OOXML ZIP package) built with Python's standard library
plus PyYAML, which is already part of the repository validation environment.
No browser-side spreadsheet library is required for the primary download path.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable
from xml.sax.saxutils import escape

import yaml

ROOT = Path(__file__).resolve().parents[1]
REQUIREMENTS_PATH = ROOT / "_data" / "career" / "assessment_requirements.yml"
ROADMAP_PATH = ROOT / "_data" / "career" / "roadmap.yml"
FACTORY_PATH = ROOT / "ai" / "career-factory.json"
OUTPUT_PATH = ROOT / "assets" / "downloads" / "sap-lead-assessment-master.xlsx"
SITE_ORIGIN = "https://dkharlanau.github.io"
STATUS_DEFAULT = "Not Started"
TIER_PRIORITY = {"core": "P1", "cross_boundary": "P2", "differentiator": "P3"}
INVALID_SHEET_CHARS = re.compile(r"[\\/?*\[\]:]")


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def as_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (str, int, float, bool)):
        return str(value)
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def absolute_url(path: Any) -> str:
    value = as_text(path).strip()
    if not value:
        return ""
    if value.startswith(("http://", "https://")):
        return value
    return SITE_ORIGIN + (value if value.startswith("/") else "/" + value)


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise RuntimeError(f"Expected mapping in {path.relative_to(ROOT)}")
    return data


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise RuntimeError(f"Expected object in {path.relative_to(ROOT)}")
    return data


def safe_sheet_name(existing: Iterable[str], name: Any) -> str:
    base = INVALID_SHEET_CHARS.sub("-", as_text(name) or "Sheet")
    base = re.sub(r"\s+", " ", base).strip() or "Sheet"
    base = base[:31]
    used = set(existing)
    candidate = base
    index = 2
    while candidate in used:
        suffix = f" {index}"
        candidate = base[: 31 - len(suffix)] + suffix
        index += 1
    return candidate


def infer_component(item: dict[str, Any]) -> str:
    value = f"{as_text(item.get('route'))} {as_text(item.get('title'))}".lower()
    rules: list[tuple[str, tuple[str, ...]]] = [
        ("SAP AIF", ("/aif", "application interface framework")),
        ("SAP aATP / ATP", ("/atp", "available-to-promise", "available to promise")),
        ("SAP Automotive JIT/JIS", ("automotive-jit", "just-in-time", "just-in-sequence")),
        ("SAP Billing", ("/billing", "billing")),
        ("Business Partner / CVI", ("business-partner", "business partner", "cvi")),
        ("Condition Contract Management", ("condition-contract-management", "condition contract")),
        ("SAP Credit Management", ("/credit", "credit management")),
        ("Data Governance", ("data-governance", "data governance")),
        ("S/4HANA Deployment Models", ("deployment-models", "public cloud", "private cloud")),
        ("ABAP / Extensibility", ("/development", "extensibility", "clean core")),
        ("Analytics / Observability", ("end-to-end-analytics", "observability", "analytics")),
        ("SAP EWM", ("/ewm", "extended warehouse management")),
        ("Integration Architecture", ("/integrations", "integration architecture")),
        ("Integration Operations", ("integration-operations", "idoc", "qrfc", "trfc", "interface operations")),
        ("SAP Inventory Management", ("inventory-management", "inventory management", "movement type")),
        ("SAP Kanban", ("/kanban", "kanban")),
        ("SAP Logistics", ("logistics-capabilities", "logistics")),
        ("SAP Master Data", ("master-data", "material-behavior", "material master")),
        ("SAP MDG / DRF", ("/mdg", "/drf", "master data governance", "data replication framework")),
        ("SAP Migration", ("migration", "migration cockpit", "data migration")),
        ("SAP Performance", ("performance", "sm50", "sm12", "sm13", "sm58", "smq1", "smq2", "st03n", "st05")),
        ("SAP Pricing", ("/pricing", "pricing")),
        ("SAP Procurement / MM", ("/procurement", "procure-to-pay", "purchasing")),
        ("SAP Production / PP", ("/production", "production planning")),
        ("SAP Quality Management", ("quality-management", "quality management")),
        ("SAP Sales / SD", ("sales-processes", "sales-order", "sales-diagnostics")),
        ("SAP Shipping", ("/shipping", "shipping", "delivery execution")),
        ("SAP Tax", ("/tax", "tax")),
        ("SAP TM", ("transportation-management", "transportation management")),
        ("Variant Configuration", ("variant-configuration", "variant configuration")),
        ("Business AI", ("business-ai", "business ai")),
        ("AI / RAG / Agents", ("ai-ready", "rag", "agent", "mcp", "retrieval")),
        ("Assessment Practice", ("/assessment", "assessment")),
        ("Interview Readiness", ("interview-readiness", "interview")),
        ("Reusable Data Procedures", ("reusable-data-procedures",)),
        ("Enterprise Assurance", ("enterprise-assurance",)),
        ("Tooling / Roadmap", ("tool-roadmap",)),
        ("Templates / Work Artifacts", ("/templates", "template")),
    ]
    for component, tokens in rules:
        if any(token in value for token in tokens):
            return component
    return "Other / Cross-domain"


def skill_priority(skill: dict[str, Any]) -> str:
    return TIER_PRIORITY.get(as_text(skill.get("tier")), "P2")


def source_summary(skill: dict[str, Any]) -> str:
    values: list[str] = []
    for source in as_list(skill.get("sources")):
        if isinstance(source, dict):
            values.append(f"{as_text(source.get('label'))} — {absolute_url(source.get('href'))}")
    return "\n".join(values)


def suggested_skill_ids(item: dict[str, Any]) -> list[str]:
    values: list[str] = []
    for candidate in as_list(item.get("suggested_skills")):
        if isinstance(candidate, str):
            value = candidate
        elif isinstance(candidate, dict):
            value = as_text(candidate.get("skill_id"))
        else:
            value = ""
        if value:
            values.append(value)
    return values


def topic_priority(item: dict[str, Any], skill_by_id: dict[str, dict[str, Any]]) -> str:
    ids = [as_text(value) for value in as_list(item.get("skills"))] + suggested_skill_ids(item)
    best = "P3"
    for skill_id in ids:
        priority = skill_priority(skill_by_id[skill_id]) if skill_id in skill_by_id else "P2"
        if priority == "P1":
            best = "P1"
        elif priority == "P2" and best == "P3":
            best = "P2"
    if item.get("state") == "needs_decision" and not ids:
        return "P2"
    return best


class Sheet:
    def __init__(self, name: str, rows: list[list[Any]], widths: list[int], autofilter: bool = True) -> None:
        self.name = name
        self.rows = rows
        self.widths = widths
        self.autofilter = autofilter


def build_sheet_model(
    roadmap: dict[str, Any], requirements_model: dict[str, Any], factory: dict[str, Any]
) -> list[Sheet]:
    sheets: list[Sheet] = []
    skills = [item for item in as_list(roadmap.get("skills")) if isinstance(item, dict)]
    requirements = [item for item in as_list(requirements_model.get("requirements")) if isinstance(item, dict)]
    domains = requirements_model.get("domains") if isinstance(requirements_model.get("domains"), dict) else {}
    tracks = roadmap.get("tracks") if isinstance(roadmap.get("tracks"), dict) else {}
    labs = [item for item in as_list(factory.get("lab_inventory")) if isinstance(item, dict)]
    skill_by_id = {as_text(skill.get("id")): skill for skill in skills if skill.get("id")}
    route_set = {as_text(item.get("route")) for item in labs if item.get("route")}

    p1_required = sum(1 for item in requirements if item.get("priority") == "P1")
    required_covered = sum(
        1
        for item in requirements
        if any(as_text(route) in route_set for route in as_list(item.get("sources")))
    )
    mapped_labs = sum(1 for item in labs if item.get("state") == "mapped")
    needs_decision = sum(1 for item in labs if item.get("state") == "needs_decision")
    summary = factory.get("summary") if isinstance(factory.get("summary"), dict) else {}
    coverage = summary.get("decision_coverage_percent")

    sheets.append(
        Sheet(
            "Dashboard",
            [
                ["SAP Lead Assessment Master Workbook"],
                ["Three layers: required assessment topics, Lead capabilities, and the complete site inventory."],
                [],
                ["Metric", "Value"],
                ["Assessment requirements", len(requirements)],
                ["P1 required topics", p1_required],
                ["Lead skills", len(skills)],
                ["Lab pages", len(labs)],
                ["Required topics with at least one exact source page", required_covered],
                ["Mapped Lab pages", mapped_labs],
                ["Lab pages needing career mapping", needs_decision],
                ["Career decision coverage", f"{coverage}%" if coverage is not None else ""],
                [],
                ["Preparation rule"],
                ["1", "Start with Required Topics and filter P1."],
                ["2", "Answer the prompt from memory before opening a source page."],
                ["3", "Use Lead Skills to move from configuration detail to design, diagnosis and leadership."],
                ["4", "Use Site Topics when you need deeper component material."],
                ["5", "Add one real project example before you mark a topic Ready."],
            ],
            [8, 92],
            False,
        )
    )

    req_rows: list[list[Any]] = [[
        "Domain", "Component", "Requirement ID", "Required Topic", "Priority", "Assessment Prompt",
        "Source Pages", "Site Coverage", "Confidence (1-5)", "Status", "Last Review", "Next Review",
        "Project Example", "Notes",
    ]]
    for item in requirements:
        domain = domains.get(item.get("domain"), {}) if isinstance(domains, dict) else {}
        if not isinstance(domain, dict):
            domain = {}
        sources = as_list(item.get("sources"))
        covered = any(as_text(route) in route_set for route in sources)
        req_rows.append([
            domain.get("label") or item.get("domain"), item.get("component"), item.get("id"), item.get("title"),
            item.get("priority"), item.get("prompt"), "\n".join(absolute_url(route) for route in sources),
            "Covered" if covered else "Check source", 1, STATUS_DEFAULT, "", "", "", "",
        ])
    sheets.append(Sheet("Required Topics", req_rows, [34, 26, 28, 46, 10, 66, 74, 16, 16, 16, 14, 14, 48, 42]))

    ordered_domains = sorted(
        domains.items(),
        key=lambda pair: (pair[1].get("order", 999) if isinstance(pair[1], dict) else 999, pair[0]),
    )
    for domain_id, domain_meta in ordered_domains:
        meta = domain_meta if isinstance(domain_meta, dict) else {}
        rows: list[list[Any]] = [[
            "Component", "Requirement ID", "Required Topic", "Priority", "Assessment Prompt", "Sources",
            "Confidence (1-5)", "Status", "Project Example", "Notes",
        ]]
        for item in requirements:
            if item.get("domain") != domain_id:
                continue
            rows.append([
                item.get("component"), item.get("id"), item.get("title"), item.get("priority"), item.get("prompt"),
                "\n".join(absolute_url(route) for route in as_list(item.get("sources"))),
                1, STATUS_DEFAULT, "", "",
            ])
        sheets.append(Sheet(as_text(meta.get("label") or domain_id), rows, [28, 28, 44, 10, 64, 72, 16, 16, 48, 42]))

    skill_rows: list[list[Any]] = [[
        "Track", "Skill ID", "Skill", "Tier", "Priority", "Capabilities", "Why it matters", "Interview signal",
        "Sources", "Confidence (1-5)", "Status", "Project Example", "Notes",
    ]]
    for skill in skills:
        track = tracks.get(skill.get("track"), {}) if isinstance(tracks, dict) else {}
        if not isinstance(track, dict):
            track = {}
        skill_rows.append([
            track.get("label") or skill.get("track"), skill.get("id"), skill.get("title"), skill.get("tier"),
            skill_priority(skill), ", ".join(as_text(value) for value in as_list(skill.get("capabilities"))),
            skill.get("why"), skill.get("interview_signal"), source_summary(skill), 1, STATUS_DEFAULT, "", "",
        ])
    sheets.append(Sheet("Lead Skills", skill_rows, [30, 26, 42, 18, 10, 26, 60, 60, 74, 16, 16, 48, 42]))

    site_rows: list[list[Any]] = [[
        "Component / Area", "Topic", "Route", "Source File", "Career State", "Career Impact", "Mapped Skills",
        "Suggested Skills", "Priority", "Confidence (1-5)", "Status", "URL", "Notes",
    ]]
    for item in labs:
        site_rows.append([
            infer_component(item), item.get("title"), item.get("route"), item.get("source_file"), item.get("state"),
            item.get("career_impact"), ", ".join(as_text(value) for value in as_list(item.get("skills"))),
            ", ".join(suggested_skill_ids(item)), topic_priority(item, skill_by_id), 1, STATUS_DEFAULT,
            absolute_url(item.get("route")), "",
        ])
    sheets.append(Sheet("Site Topics", site_rows, [30, 50, 50, 56, 18, 18, 34, 34, 10, 16, 16, 60, 42]))

    component_map: dict[str, dict[str, int]] = {}

    def bucket(name: Any) -> dict[str, int]:
        key = as_text(name) or "Other / Cross-domain"
        return component_map.setdefault(key, {"required": 0, "p1": 0, "pages": 0, "mapped": 0, "gaps": 0})

    for item in requirements:
        item_bucket = bucket(item.get("component"))
        item_bucket["required"] += 1
        if item.get("priority") == "P1":
            item_bucket["p1"] += 1
    for item in labs:
        item_bucket = bucket(infer_component(item))
        item_bucket["pages"] += 1
        if item.get("state") == "mapped":
            item_bucket["mapped"] += 1
        if item.get("state") == "needs_decision":
            item_bucket["gaps"] += 1

    component_rows: list[list[Any]] = [[
        "Component / Area", "Required Topics", "P1 Required", "Site Pages", "Mapped Pages", "Career Mapping Gaps"
    ]]
    for name in sorted(component_map):
        item_bucket = component_map[name]
        component_rows.append([
            name, item_bucket["required"], item_bucket["p1"], item_bucket["pages"], item_bucket["mapped"], item_bucket["gaps"]
        ])
    sheets.append(Sheet("Components", component_rows, [38, 16, 14, 14, 16, 20]))

    gap_rows: list[list[Any]] = [[
        "Component / Area", "Topic", "Route", "Suggested Skills", "Priority", "URL", "Decision / Notes"
    ]]
    for item in labs:
        if item.get("state") != "needs_decision":
            continue
        gap_rows.append([
            infer_component(item), item.get("title"), item.get("route"), ", ".join(suggested_skill_ids(item)),
            topic_priority(item, skill_by_id), absolute_url(item.get("route")), "",
        ])
    sheets.append(Sheet("Needs Mapping", gap_rows, [32, 52, 52, 38, 10, 60, 48]))

    sprint_rows: list[list[Any]] = [[
        "Date", "Domain", "Topic", "Goal", "20-minute Block", "Result / Gap", "Next Action", "Done"
    ]]
    for _ in range(30):
        sprint_rows.append(["", "", "", "", "Recall → review → project example", "", "", "No"])
    sheets.append(Sheet("Daily Sprint", sprint_rows, [14, 30, 44, 44, 36, 44, 44, 10]))

    sheets.append(
        Sheet(
            "How to Use",
            [
                ["Rule", "Action"],
                ["1. Required Topics are the syllabus", "This sheet is the detailed assessment programme. Start with P1."],
                ["2. Lead Skills are the capability model", "Use them to turn module knowledge into diagnosis, architecture and leadership answers."],
                ["3. Site Topics are the knowledge inventory", "Every Lab page is visible, but not every page is automatically mandatory for the assessment."],
                ["4. Recall before reading", "Answer from memory first. Study the gap in your answer, not the whole page again."],
                ["5. Add project evidence", "For important topics, add one real incident, design decision, trade-off or result."],
                ["6. Rate confidence", "1 = cannot explain; 3 = can explain basics; 5 = can lead a design or troubleshooting discussion."],
                ["7. Ready has a strict meaning", "You can explain purpose, flow, one design decision, one failure path and one project example."],
                ["8. Needs Mapping is content debt", "These Lab pages exist but still need a career decision. Keep them visible until mapped or explicitly excluded."],
                ["9. Regenerate instead of maintaining manually", "Generate a new workbook after Career Factory or Assessment Requirements changes."],
            ],
            [34, 108],
        )
    )

    used: list[str] = []
    for model in sheets:
        model.name = safe_sheet_name(used, model.name)
        used.append(model.name)
    return sheets


def xml_text(value: Any) -> str:
    return escape(as_text(value), {'"': "&quot;", "'": "&apos;"})


def column_name(index: int) -> str:
    value = index + 1
    result = ""
    while value:
        value, remainder = divmod(value - 1, 26)
        result = chr(65 + remainder) + result
    return result


def cell_xml(value: Any, ref: str, style: int = 0) -> str:
    style_attr = f' s="{style}"' if style else ""
    if isinstance(value, bool):
        return f'<c r="{ref}" t="b"{style_attr}><v>{1 if value else 0}</v></c>'
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return f'<c r="{ref}" t="n"{style_attr}><v>{value}</v></c>'
    text = xml_text(value)
    return f'<c r="{ref}" t="inlineStr"{style_attr}><is><t xml:space="preserve">{text}</t></is></c>'


def worksheet_xml(model: Sheet) -> str:
    cols = "".join(
        f'<col min="{index}" max="{index}" width="{float(width):g}" customWidth="1"/>'
        for index, width in enumerate(model.widths, start=1)
    )
    rows_xml: list[str] = []
    for row_index, row in enumerate(model.rows, start=1):
        cells: list[str] = []
        for col_index, value in enumerate(row):
            style = 1 if row_index == 1 and model.autofilter else 0
            cells.append(cell_xml(value, f"{column_name(col_index)}{row_index}", style))
        rows_xml.append(f'<row r="{row_index}">{"".join(cells)}</row>')

    sheet_views = (
        '<sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" '
        'activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>'
        if model.autofilter and len(model.rows) > 1
        else '<sheetViews><sheetView workbookViewId="0"/></sheetViews>'
    )
    autofilter = ""
    if model.autofilter and len(model.rows) > 1 and model.rows[0]:
        autofilter = f'<autoFilter ref="A1:{column_name(len(model.rows[0]) - 1)}{len(model.rows)}"/>'
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        f'{sheet_views}<cols>{cols}</cols><sheetData>{"".join(rows_xml)}</sheetData>{autofilter}'
        '</worksheet>'
    )


def content_types_xml(sheet_count: int) -> str:
    sheet_overrides = "".join(
        f'<Override PartName="/xl/worksheets/sheet{index}.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
        for index in range(1, sheet_count + 1)
    )
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
        '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
        '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
        '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>'
        f'{sheet_overrides}</Types>'
    )


def root_rels_xml() -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
        '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>'
        '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>'
        '</Relationships>'
    )


def workbook_xml(models: list[Sheet]) -> str:
    entries = "".join(
        f'<sheet name="{xml_text(model.name)}" sheetId="{index}" r:id="rId{index}"/>'
        for index, model in enumerate(models, start=1)
    )
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        f'<bookViews><workbookView activeTab="0"/></bookViews><sheets>{entries}</sheets></workbook>'
    )


def workbook_rels_xml(sheet_count: int) -> str:
    rels = "".join(
        f'<Relationship Id="rId{index}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" '
        f'Target="worksheets/sheet{index}.xml"/>'
        for index in range(1, sheet_count + 1)
    )
    rels += (
        f'<Relationship Id="rId{sheet_count + 1}" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
    )
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        f'{rels}</Relationships>'
    )


def styles_xml() -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        '<fonts count="2">'
        '<font><sz val="11"/><name val="Calibri"/><family val="2"/></font>'
        '<font><b/><sz val="11"/><name val="Calibri"/><family val="2"/></font>'
        '</fonts>'
        '<fills count="3">'
        '<fill><patternFill patternType="none"/></fill>'
        '<fill><patternFill patternType="gray125"/></fill>'
        '<fill><patternFill patternType="solid"><fgColor rgb="FFE7E6E6"/><bgColor indexed="64"/></patternFill></fill>'
        '</fills>'
        '<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>'
        '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>'
        '<cellXfs count="2">'
        '<xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>'
        '<xf numFmtId="0" fontId="1" fillId="2" borderId="0" xfId="0" applyFont="1" applyFill="1"/>'
        '</cellXfs>'
        '<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>'
        '</styleSheet>'
    )


def app_xml(models: list[Sheet]) -> str:
    titles = "".join(f'<vt:lpstr>{xml_text(model.name)}</vt:lpstr>' for model in models)
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" '
        'xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">'
        '<Application>DKHARLANAU.github.io</Application><DocSecurity>0</DocSecurity><ScaleCrop>false</ScaleCrop>'
        '<HeadingPairs><vt:vector size="2" baseType="variant"><vt:variant><vt:lpstr>Worksheets</vt:lpstr></vt:variant>'
        f'<vt:variant><vt:i4>{len(models)}</vt:i4></vt:variant></vt:vector></HeadingPairs>'
        f'<TitlesOfParts><vt:vector size="{len(models)}" baseType="lpstr">{titles}</vt:vector></TitlesOfParts>'
        '<Company></Company><LinksUpToDate>false</LinksUpToDate><SharedDoc>false</SharedDoc>'
        '<HyperlinksChanged>false</HyperlinksChanged><AppVersion>1.0</AppVersion></Properties>'
    )


def core_xml() -> str:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
        'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
        'xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        '<dc:title>SAP Lead Assessment Master Workbook</dc:title>'
        '<dc:subject>SAP Lead assessment preparation</dc:subject>'
        '<dc:creator>DKHARLANAU.github.io</dc:creator><cp:lastModifiedBy>DKHARLANAU.github.io</cp:lastModifiedBy>'
        f'<dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created>'
        f'<dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified>'
        '</cp:coreProperties>'
    )


def write_workbook(models: list[Sheet], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        archive.writestr("[Content_Types].xml", content_types_xml(len(models)))
        archive.writestr("_rels/.rels", root_rels_xml())
        archive.writestr("docProps/app.xml", app_xml(models))
        archive.writestr("docProps/core.xml", core_xml())
        archive.writestr("xl/workbook.xml", workbook_xml(models))
        archive.writestr("xl/_rels/workbook.xml.rels", workbook_rels_xml(len(models)))
        archive.writestr("xl/styles.xml", styles_xml())
        for index, model in enumerate(models, start=1):
            archive.writestr(f"xl/worksheets/sheet{index}.xml", worksheet_xml(model))


def validate_xlsx(path: Path, expected_sheets: int) -> None:
    required_entries = {
        "[Content_Types].xml",
        "_rels/.rels",
        "xl/workbook.xml",
        "xl/_rels/workbook.xml.rels",
        "xl/styles.xml",
    }
    with zipfile.ZipFile(path) as archive:
        bad = archive.testzip()
        if bad:
            raise RuntimeError(f"Corrupt XLSX member: {bad}")
        names = set(archive.namelist())
        missing = required_entries - names
        if missing:
            raise RuntimeError(f"Missing XLSX package entries: {sorted(missing)}")
        worksheet_count = sum(1 for name in names if name.startswith("xl/worksheets/sheet") and name.endswith(".xml"))
        if worksheet_count != expected_sheets:
            raise RuntimeError(f"Expected {expected_sheets} worksheets, found {worksheet_count}")


def generate(output: Path = OUTPUT_PATH) -> Path:
    roadmap = load_yaml(ROADMAP_PATH)
    requirements = load_yaml(REQUIREMENTS_PATH)
    factory = load_json(FACTORY_PATH)
    models = build_sheet_model(roadmap, requirements, factory)
    write_workbook(models, output)
    validate_xlsx(output, len(models))
    return output


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    parser.add_argument("--check", action="store_true", help="Generate to memory-equivalent temporary path and verify tracked output is current.")
    args = parser.parse_args(argv)

    if args.check:
        import tempfile

        if not OUTPUT_PATH.exists():
            print(f"Missing generated workbook: {OUTPUT_PATH.relative_to(ROOT)}", file=sys.stderr)
            return 1
        with tempfile.TemporaryDirectory() as tmp:
            candidate = Path(tmp) / OUTPUT_PATH.name
            generate(candidate)
            # Core timestamps differ by design, so validate both packages and compare canonical sheet XML + workbook XML.
            with zipfile.ZipFile(candidate) as left, zipfile.ZipFile(OUTPUT_PATH) as right:
                comparable = [
                    name for name in left.namelist()
                    if name.startswith("xl/") and name.endswith(".xml")
                ]
                for name in comparable:
                    if name not in right.namelist() or left.read(name) != right.read(name):
                        print(f"Generated workbook is stale: {name}", file=sys.stderr)
                        return 1
        print(f"Workbook is current: {OUTPUT_PATH.relative_to(ROOT)}")
        return 0

    output = args.output
    if not output.is_absolute():
        output = (ROOT / output).resolve()
    generated = generate(output)
    print(f"Generated {generated.relative_to(ROOT) if generated.is_relative_to(ROOT) else generated}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
