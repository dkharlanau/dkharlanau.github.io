---
layout: default
title: "SAP MDG Material Entity Map — Enterprise Context Lab"
description: "A practical bridge from MDG-M technical entity names to Material business grains, ownership, rules and downstream process proof."
permalink: /labs/enterprise-context/mdg/domains/material/entity-map/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags: [sap, mdg, material, entity-model, master-data, logistics]
---

# SAP MDG Material Entity Map

The entity list matters, but it is not the architecture. I use it as a bridge:

```text
Technical entity → Business grain → Meaning → Owner → Rule → Consumer
```

The current SAP MDG-M documentation describes `MATERIAL` as the main basic-data entity and lists dependent entities such as `MARCBASIC`, `MARCATP`, `MARCPURCH`, `MVKESALES`, `MARDSTOR`, `MBEWVALUA`, `MLGNSTOR`, `QMATBASIC`, `UNITOFMSR` and `CLASSASGN`.

## A useful grouping

| Business grain | Representative MDG entities | Main design question |
|---|---|---|
| Material | `MATERIAL`, `BSCDATTXT`, `UNITOFMSR`, `MEAN_GTIN`, `CLASSASGN` | What is globally true about the product? |
| Material + Plant | `MARCBASIC`, `MARCATP`, `MARCPURCH`, `MARCSALES`, `MARCQTMNG`, `MARCWRKSD`, MRP entities | What changes by plant and who owns that meaning? |
| Material + Storage Location | `MARDSTOR`, `MARDMRP` | Is this execution/planning meaning local to a storage location? |
| Material + Sales Org + Distribution Channel | `MVKESALES`, `MVKEGRPNG`, `SALESTXT` | What is commercial behavior for one distribution chain? |
| Material + Valuation Area | `MBEWACTNG`, `MBEWVALUA`, `MBEWCSTNG` | Which finance owner controls valuation and costing meaning? |
| Material + Warehouse context | `MLGNSTOR`, `MLGTSTOR` | Which warehouse attributes must exist for execution? |

The exact delivered scope is release-specific. The point of this map is not to memorize every entity name. It is to stop design discussions from mixing global product identity with plant, sales, finance or warehouse meaning.

## Field-to-entity protocol

For a new field or extension, I would ask seven questions:

1. What does the field mean in business language?
2. At which grain can the value change?
3. Which delivered entity already represents that grain?
4. Is the field inside the selected governance scope?
5. Who owns the value and who can only propose it?
6. Which validation or derivation controls it?
7. Which process proves that the value works after activation and distribution?

This is much safer than starting with a UI section and adding a custom field wherever there is free space. Screens are excellent at creating false confidence.

## Example: plant extension

A new factory starts producing an existing material.

```text
Existing MATERIAL identity
→ Plant entities
→ MRP / Purchasing / Quality / Work Scheduling data
→ Validation
→ Approval by plant owners
→ Activation
→ Replication where required
→ MRP / production / procurement proof
```

The Lead question is not “Which view do we maintain?” It is “Which plant-dependent decisions become valid, who owns them, and how do we prove downstream use?”

## Boundaries

Do not pull routing, pricing conditions or source-list ownership into the Material root just because those objects reference Material. SAP's delivered MDG-M model itself separates Material data from several process-control objects.

Also keep **technical entity** and **business ownership** separate. `MARCBASIC` tells us there is a plant segment. It does not tell us whether Planning, Procurement or Operations owns each attribute inside it.

## Machine-readable model

The structured model is in `_data/labs/enterprise_context/topics/mdg_material_entity_reference.yml` and links to the broader [Material domain](/labs/enterprise-context/mdg/domains/material/) and [governance engine](/labs/enterprise-context/mdg/governance-engine/).

For assessment practice, pair this page with the [MDG logistics cases](/labs/enterprise-context/mdg/logistics/cases/).
