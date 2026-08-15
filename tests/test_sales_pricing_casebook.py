from pathlib import Path
import math

import yaml


ROOT = Path(__file__).resolve().parents[1]
GRAPH_PATH = ROOT / "_data/labs/enterprise_context/graphs/pricing_casebook.yml"
SOURCE_PATHS = [
    ROOT / "_data/labs/enterprise_context/sources/pricing_anatomy.yml",
    ROOT / "_data/labs/enterprise_context/sources/pricing_scenarios.yml",
    ROOT / "_data/labs/enterprise_context/sources/pricing_casebook.yml",
]
PAGE_PATH = ROOT / "labs/enterprise-context/pricing/casebook/index.html"
JSON_PATH = ROOT / "labs/enterprise-context/data/pricing-casebook.json"
SOURCE_JSON_PATH = ROOT / "labs/enterprise-context/data/pricing-casebook-sources.json"


def load_yaml(path):
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def cases_by_id():
    graph = load_yaml(GRAPH_PATH)
    return graph, {item["id"]: item for item in graph["worked_cases"]}


def test_casebook_contract_and_unique_ids():
    graph, cases = cases_by_id()
    assert graph["id"] == "GRAPH-SD-PRICING-CASEBOOK"
    assert graph["status"] == "draft"
    assert graph["verified"] is False
    assert len(cases) == len(graph["worked_cases"])
    assert len(cases) >= 9
    assert len(graph["assessment_drills"]) >= 6
    assert len({x["id"] for x in graph["assessment_drills"]}) == len(graph["assessment_drills"])


def test_all_source_refs_resolve_across_pricing_registries():
    graph, _ = cases_by_id()
    source_ids = set()
    for path in SOURCE_PATHS:
        registry = load_yaml(path)
        source_ids.update(item["id"] for item in registry["sources"])

    referenced = {
        ref
        for case in graph["worked_cases"]
        for ref in case.get("source_refs", [])
    }
    missing = referenced - source_ids
    assert not missing, f"Unknown pricing casebook source refs: {sorted(missing)}"


def test_layered_price_math():
    _, cases = cases_by_id()
    case = cases["PCR.CASE.01"]
    data = case["inputs"]
    expected = case["expected"]

    gross = data["quantity"] * data["unit_price"]
    customer_discount = gross * data["customer_discount_percent"] / 100
    campaign_discount = data["quantity"] * data["campaign_discount_per_unit"]
    selected_discount = max(customer_discount, campaign_discount)
    net = gross - selected_discount + data["freight"]
    tax = net * data["tax_percent"] / 100

    assert math.isclose(gross, expected["gross_before_discount"], rel_tol=0, abs_tol=0.001)
    assert math.isclose(selected_discount, expected["selected_discount"], rel_tol=0, abs_tol=0.001)
    assert math.isclose(net, expected["net_before_tax"], rel_tol=0, abs_tol=0.001)
    assert math.isclose(tax, expected["tax"], rel_tol=0, abs_tol=0.001)
    assert math.isclose(net + tax, expected["amount_due"], rel_tol=0, abs_tol=0.001)


def test_group_scale_math_and_distribution():
    _, cases = cases_by_id()
    case = cases["PCR.CASE.02"]
    data = case["inputs"]
    calc = case["calculation"]

    a_value = data["item_a_qty"] * data["item_a_unit_price"]
    b_value = data["item_b_qty"] * data["item_b_unit_price"]
    total_value = a_value + b_value
    total_qty = data["item_a_qty"] + data["item_b_qty"]
    total_discount = total_value * data["discount_percent"] / 100

    assert total_qty >= data["threshold_qty"]
    assert math.isclose(total_value, calc["combined_value"], abs_tol=0.001)
    assert math.isclose(total_discount, calc["total_discount"], abs_tol=0.001)
    assert math.isclose(calc["item_a_discount"] + calc["item_b_discount"], total_discount, abs_tol=0.001)
    assert math.isclose(total_value - total_discount, calc["final_net"], abs_tol=0.001)


def test_free_goods_modes_keep_quantity_semantics_distinct():
    _, cases = cases_by_id()
    case = cases["PCR.CASE.03"]
    modes = {item["mode"]: item for item in case["variants"]}

    inclusive = modes["inclusive"]
    exclusive = modes["exclusive"]
    assert inclusive["delivered_qty"] == inclusive["ordered_or_requested_qty"]
    assert inclusive["paid_qty"] + inclusive["free_qty"] == inclusive["delivered_qty"]
    assert exclusive["delivered_qty"] == exclusive["paid_qty"] + exclusive["free_qty"]
    assert exclusive["delivered_qty"] > exclusive["ordered_or_requested_qty"]


def test_variant_configuration_case_math():
    _, cases = cases_by_id()
    case = cases["PCR.CASE.04"]
    data = case["inputs"]
    calc = case["calculation"]

    subtotal = data["base_price"] + data["battery_surcharge"] + data["precision_package_surcharge"]
    discount = subtotal * data["fleet_discount_percent"] / 100
    assert math.isclose(subtotal, calc["configured_subtotal"], abs_tol=0.001)
    assert math.isclose(discount, calc["fleet_discount"], abs_tol=0.001)
    assert math.isclose(subtotal - discount, calc["net_value"], abs_tol=0.001)


def test_billing_pricing_types_show_copy_vs_redetermine_boundary():
    _, cases = cases_by_id()
    case = cases["PCR.CASE.05"]
    variants = {item["pricing_type"]: item for item in case["variants"]}
    assert variants["D"]["expected_invoice_value"] == 1000.0
    assert variants["B"]["expected_invoice_value"] == 1100.0
    assert "manual" in variants["C"]["simplified_effect"]
    assert "tax" in variants["G"]["simplified_effect"]


def test_retroactive_delta_math():
    _, cases = cases_by_id()
    case = cases["PCR.CASE.06"]
    data = case["inputs"]
    calc = case["calculation"]

    original = data["billed_qty"] * data["old_unit_rate"]
    corrected = data["billed_qty"] * data["new_unit_rate"]
    assert math.isclose(corrected - original, calc["retroactive_delta"], abs_tol=0.001)
    assert math.isclose(data["unbilled_qty"] * data["new_unit_rate"], calc["future_unbilled_value_at_new_rate"], abs_tol=0.001)


def test_rebate_true_up_math():
    _, cases = cases_by_id()
    case = cases["PCR.CASE.07"]
    data = case["inputs"]
    calc = case["calculation"]

    final_rebate = data["eligible_business_volume"] * data["final_rebate_percent"] / 100
    accrued = data["eligible_business_volume"] * data["accrued_percent"] / 100
    assert math.isclose(final_rebate, calc["final_rebate"], abs_tol=0.001)
    assert math.isclose(accrued, calc["accrued_amount"], abs_tol=0.001)
    assert math.isclose(final_rebate - accrued, calc["final_true_up_before_other_adjustments"], abs_tol=0.001)


def test_intercompany_case_keeps_external_and_internal_values_separate():
    _, cases = cases_by_id()
    case = cases["PCR.CASE.08"]
    data = case["inputs"]
    calc = case["calculation"]
    internal = data["external_customer_net"] * data["intercompany_percent"] / 100

    assert math.isclose(internal, calc["internal_intercompany_value"], abs_tol=0.001)
    assert calc["external_invoice_value"] != calc["internal_intercompany_value"]
    assert math.isclose(
        calc["external_invoice_value"] - calc["internal_intercompany_value"],
        calc["selling_company_spread_before_other_costs"],
        abs_tol=0.001,
    )


def test_formula_case_tests_both_sides_of_minimum_boundary():
    _, cases = cases_by_id()
    case = cases["PCR.CASE.09"]
    data = case["inputs"]
    alt = case["alternative_test"]

    assert math.isclose(data["gross_weight_kg"] * data["rate_per_kg"], case["calculation"]["weight_charge"], abs_tol=0.001)
    assert case["calculation"]["final_freight"] == max(data["minimum_charge"], case["calculation"]["weight_charge"])
    assert alt["final_freight"] == max(data["minimum_charge"], alt["weight_charge"])


def test_human_and_machine_views_exist_and_are_draft():
    page = PAGE_PATH.read_text(encoding="utf-8")
    machine = JSON_PATH.read_text(encoding="utf-8")
    source_machine = SOURCE_JSON_PATH.read_text(encoding="utf-8")

    assert "status: draft" in page
    assert "robots: noindex,follow" in page
    assert "Pricing Casebook" in page
    assert "pricing-casebook.json" in page
    assert "site.data.labs.enterprise_context.graphs.pricing_casebook" in machine
    assert "site.data.labs.enterprise_context.sources.pricing_casebook" in source_machine
