"""Regression contract for the SEPA Direct Debit process lab."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PAGE = "_blog/sepa-direct-debit-sap-s4hana-customer-mandate-migration.md"
ROUTE = "/blog/sepa-direct-debit-sap-s4hana-customer-mandate-migration/"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_sepa_process_lab_has_a_single_title_and_navigable_sections():
    page = read(PAGE)
    assert "sepa_lab: true" in page
    assert f"permalink: {ROUTE}" in page
    assert page.count("<h1 ") == 1
    anchors = re.findall(r'\bid="([^"]+)"', page)
    assert len(anchors) == len(set(anchors))
    for target in re.findall(r'href="#([^"]+)"', page):
        assert target in anchors, f"Broken on-page link: {target}"
    assert page.count("<details") >= 3


def test_sepa_business_process_data_and_migration_are_connected():
    page = read(PAGE)
    for expected in (
        "SEPA Credit Transfer",
        "SEPA Direct Debit",
        "Sales order",
        "Billing",
        "FI-AR",
        "payment proposal",
        "bank",
        "payer",
        "billing split",
        "SEPA_MANDATE",
        "SEPA_MANDATE_USE",
        "MGUID",
        "MNDID",
        "PAY_TYPE",
        "I_CustomerSEPAMandate",
        "I_SEPAMandateUsage",
        "FSEPA_M4",
        "F110",
        "READY",
        "BLOCKED",
        "REVIEW",
        "Obsolete / Completed",
    ):
        assert expected.lower() in page.lower(), expected
    assert "Never update" in page and "directly" in page
    assert "Central Finance" in page
    assert "synthetic" in page.lower()


def test_sepa_lab_styles_are_scoped_and_responsive():
    layout = read("_layouts/default.html")
    css = read("assets/sepa-mandate-lab.css")
    assert "or page.sepa_lab" in layout
    assert "assets/sepa-mandate-lab.css" in layout
    assert ".sepa-lab" in css
    assert ".sepa-flow" in css and "overflow-x: auto" in css
    assert "@media (max-width: 570px)" in css
    assert "focus-visible" in css


def test_related_labs_link_to_the_mandate_guide():
    for path in (
        "labs/enterprise-context/finance-logistics/payments-banks-rejections/index.md",
        "labs/enterprise-context/billing/index.html",
        "labs/enterprise-context/sales-processes/index.html",
    ):
        assert ROUTE in read(path), path
