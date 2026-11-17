from __future__ import annotations

import importlib.util
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_sap_lead_assessment_workbook.py"
SPEC = importlib.util.spec_from_file_location("sap_lead_workbook", SCRIPT)
assert SPEC and SPEC.loader
workbook = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(workbook)


INVALID = re.compile(r"[\\/?*\[\]:]")
NS = {
    "main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
}


def test_safe_sheet_name_handles_excel_constraints() -> None:
    names: list[str] = []
    first = workbook.safe_sheet_name(names, "S/4HANA Migration")
    names.append(first)
    second = workbook.safe_sheet_name(names, "S/4HANA Migration")
    long_name = workbook.safe_sheet_name(names + [second], "Warehouse, Production, Quality and Transport")

    assert first == "S-4HANA Migration"
    assert second != first
    assert len(first) <= 31
    assert len(second) <= 31
    assert len(long_name) <= 31
    assert not INVALID.search(first)
    assert not INVALID.search(second)
    assert not INVALID.search(long_name)


def test_generator_builds_valid_xlsx_from_current_site_data(tmp_path: Path) -> None:
    output = tmp_path / "sap-lead-assessment-master.xlsx"
    generated = workbook.generate(output)

    assert generated == output
    assert output.exists()
    assert output.stat().st_size > 1000

    with zipfile.ZipFile(output) as archive:
        assert archive.testzip() is None
        assert "[Content_Types].xml" in archive.namelist()
        assert "xl/workbook.xml" in archive.namelist()
        root = ET.fromstring(archive.read("xl/workbook.xml"))
        sheets = root.findall("main:sheets/main:sheet", NS)

    assert len(sheets) >= 10
    sheet_names = [sheet.attrib["name"] for sheet in sheets]
    assert "Dashboard" in sheet_names
    assert "Required Topics" in sheet_names
    assert "Lead Skills" in sheet_names
    assert "Site Topics" in sheet_names
    assert "Components" in sheet_names
    assert "Needs Mapping" in sheet_names
    assert "Daily Sprint" in sheet_names
    assert "How to Use" in sheet_names
    assert len(sheet_names) == len(set(sheet_names))
    assert all(len(name) <= 31 and not INVALID.search(name) for name in sheet_names)


def test_regeneration_preserves_identical_workbook_despite_timestamp_changes(tmp_path: Path, monkeypatch) -> None:
    output = tmp_path / "assessment.xlsx"
    workbook.generate(output)
    original = output.read_bytes()
    original_mtime = output.stat().st_mtime_ns
    core_xml = workbook.core_xml

    def different_timestamp() -> str:
        return re.sub(r'(xsi:type="dcterms:W3CDTF">)[^<]+', r'\g<1>2000-01-01T00:00:00Z', core_xml())

    monkeypatch.setattr(workbook, "core_xml", different_timestamp)
    workbook.generate(output)

    assert output.read_bytes() == original
    assert output.stat().st_mtime_ns == original_mtime


def test_regeneration_replaces_workbook_when_metadata_changes(tmp_path: Path, monkeypatch) -> None:
    output = tmp_path / "assessment.xlsx"
    workbook.generate(output)
    core_xml = workbook.core_xml
    monkeypatch.setattr(workbook, "core_xml", lambda: core_xml().replace(
        "SAP Lead Assessment Master Workbook", "Updated Assessment Workbook"
    ))

    workbook.generate(output)

    with zipfile.ZipFile(output) as archive:
        assert b"Updated Assessment Workbook" in archive.read("docProps/core.xml")


def test_check_detects_extra_package_member_and_regeneration_repairs_it(tmp_path: Path, monkeypatch) -> None:
    output = tmp_path / "assessment.xlsx"
    workbook.generate(output)
    with zipfile.ZipFile(output, "a") as archive:
        archive.writestr("unexpected.txt", "stale")
    monkeypatch.setattr(workbook, "OUTPUT_PATH", output)
    monkeypatch.setattr(workbook, "ROOT", tmp_path)

    assert workbook.main(["--check"]) == 1
    workbook.generate(output)
    assert workbook.main(["--check"]) == 0
    with zipfile.ZipFile(output) as archive:
        assert "unexpected.txt" not in archive.namelist()


def test_regeneration_repairs_changed_worksheet(tmp_path: Path) -> None:
    output = tmp_path / "assessment.xlsx"
    workbook.generate(output)
    changed = tmp_path / "changed.xlsx"
    with zipfile.ZipFile(output) as source, zipfile.ZipFile(changed, "w") as target:
        for name in source.namelist():
            data = source.read(name)
            if name == "xl/worksheets/sheet1.xml":
                data += b"<!-- altered -->"
            target.writestr(name, data)
    changed.replace(output)

    workbook.generate(output)

    with zipfile.ZipFile(output) as archive:
        assert b"<!-- altered -->" not in archive.read("xl/worksheets/sheet1.xml")


def test_regeneration_replaces_invalid_existing_workbook(tmp_path: Path) -> None:
    output = tmp_path / "assessment.xlsx"
    output.write_bytes(b"not an xlsx")

    workbook.generate(output)

    with zipfile.ZipFile(output) as archive:
        assert archive.testzip() is None
        assert "xl/workbook.xml" in archive.namelist()
