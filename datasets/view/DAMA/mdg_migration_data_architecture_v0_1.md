---
layout: default
title: "Mdg Migration Data Architecture V0 1"
description: "Mdg Migration Data Architecture V0 1"
permalink: /datasets/view/DAMA/mdg_migration_data_architecture_v0_1/
sitemap: true
last_modified_at: 2026-04-13T08:37:04+00:00
dataset_detail_page: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Mdg Migration Data Architecture V0 1</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">DAMA</span>
    <span class="pill pill--type">mdg_byte</span>
    <span class="pill">mdg_migration_data_architecture_v0_1</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/DAMA/mdg_migration_data_architecture_v0_1.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/DAMA/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Mdg Migration Data Architecture V0 1</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/DAMA/mdg_migration_data_architecture_v0_1.json">https://dkharlanau.github.io/datasets/DAMA/mdg_migration_data_architecture_v0_1.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial only, attribution with source link required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Mdg Migration Data Architecture V0 1” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/DAMA/mdg_migration_data_architecture_v0_1.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Mdg Migration Data Architecture V0 1",
  "description": "Mdg Migration Data Architecture V0 1",
  "url": "https://dkharlanau.github.io/datasets/view/DAMA/mdg_migration_data_architecture_v0_1/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Mdg Migration Data Architecture V0 1” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/DAMA/mdg_migration_data_architecture_v0_1.json",
  "identifier": "https://doi.org/10.5281/zenodo.18862098",
  "sameAs": [
    "https://doi.org/10.5281/zenodo.18862098",
    "https://github.com/dkharlanau/dkharlanau-datasets"
  ],
  "creator": {
    "@type": "Person",
    "@id": "https://dkharlanau.github.io/#dkharlanau",
    "name": "Dzmitryi Kharlanau",
    "url": "https://dkharlanau.github.io/"
  },
  "distribution": [
    {
      "@type": "DataDownload",
      "encodingFormat": "application/json",
      "contentUrl": "https://dkharlanau.github.io/datasets/DAMA/mdg_migration_data_architecture_v0_1.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "mdg_migration_data_architecture_v0_1",
  "type": "architecture_blueprint",
  "scope": "MDG migration / cutover / stabilization",
  "goal": "Provide a layered data architecture that makes migration predictable: staged loads, quality gates, reconciliation, traceability, and controlled promotion into System of Record.",
  "principles": [
    "Separate raw intake from governed data",
    "Promote data only through explicit quality gates",
    "Reference data alignment is a first-class dependency",
    "Every load is an event with auditability (who/what/when/why)",
    "No silent fixes downstream; fix at source or via governed exception"
  ],
  "layers": [
    {
      "layer_id": "L0_sources",
      "name": "L0 — Sources (Legacy / External / Files)",
      "purpose": "Provide the raw origin of migration data with minimal assumptions.",
      "typical_assets": [
        "legacy extracts",
        "spreadsheets",
        "external reference lists",
        "cutover delta files"
      ],
      "controls": [
        "immutability of extracts (hash + version tag)",
        "source metadata capture (system, date, scope)"
      ],
      "outputs": [
        "raw_extract_packages"
      ]
    },
    {
      "layer_id": "L1_raw_staging",
      "name": "L1 — Raw Staging (Immutable Landing Zone)",
      "purpose": "Store raw payloads exactly as received; enable replay and forensic trace.",
      "typical_assets": [
        "raw tables/files",
        "ingestion logs",
        "file manifests",
        "schema snapshots"
      ],
      "quality_gates": [
        {
          "gate_id": "gate_schema_conformance",
          "description": "File/table structure matches expected schema; required columns exist; datatypes parse.",
          "failure_policy": "block_promotion",
          "evidence_outputs": [
            "schema_report",
            "parse_errors"
          ]
        }
      ],
      "outputs": [
        "staged_raw_records"
      ]
    },
    {
      "layer_id": "L2_standardization",
      "name": "L2 — Standardization (Canonical Formats)",
      "purpose": "Normalize formats and keys without changing business meaning (dates, casing, trimming, locale normalization).",
      "typical_assets": [
        "standardized tables",
        "normalization rules catalog",
        "locale rules (decimal separators, encodings)"
      ],
      "quality_gates": [
        {
          "gate_id": "gate_key_presence",
          "description": "Business keys and required identifiers exist to enable matching and deltas.",
          "failure_policy": "block_promotion_or_route_to_cleansing",
          "evidence_outputs": [
            "missing_key_report"
          ]
        }
      ],
      "outputs": [
        "standardized_records"
      ]
    },
    {
      "layer_id": "L3_mapping_transformation",
      "name": "L3 — Mapping &amp; Transformation (Meaning-preserving conversion)",
      "purpose": "Apply controlled mappings: value mapping, code translations, structural transformations, derivations approved by governance.",
      "typical_assets": [
        "value_mapping_catalog",
        "transformation rules",
        "derivation rules (low risk only)",
        "mapping test cases"
      ],
      "quality_gates": [
        {
          "gate_id": "gate_reference_alignment",
          "description": "All mapped codes exist in target LoV/customizing; unmapped values are quarantined.",
          "failure_policy": "block_promotion",
          "evidence_outputs": [
            "unmapped_values_report",
            "lov_alignment_report"
          ]
        }
      ],
      "outputs": [
        "mapped_records"
      ]
    },
    {
      "layer_id": "L4_cleansing_resolution",
      "name": "L4 — Cleansing &amp; Resolution (Fix or Exception)",
      "purpose": "Resolve data defects: completeness gaps, invalid combos, duplicates; decide cleanse vs exception with expiry.",
      "typical_assets": [
        "cleansing backlog",
        "exception register",
        "match/merge candidates",
        "steward/owner decisions"
      ],
      "quality_gates": [
        {
          "gate_id": "gate_tier1_minimum_quality",
          "description": "Tier 1 attribute groups meet minimum completeness/validity; exceptions are formally approved with expiry.",
          "failure_policy": "block_promotion_for_tier1",
          "evidence_outputs": [
            "tier1_quality_report",
            "exceptions_with_expiry_report"
          ]
        }
      ],
      "outputs": [
        "resolved_records",
        "approved_exceptions"
      ]
    },
    {
      "layer_id": "L5_preload_validation",
      "name": "L5 — Preload Validation (Contract Checks)",
      "purpose": "Validate against data contracts and migration controls before touching MDG.",
      "typical_assets": [
        "contract checks",
        "sampling verification packs",
        "load readiness dashboards"
      ],
      "quality_gates": [
        {
          "gate_id": "gate_sampling_verification",
          "description": "Sample-based verification passes (e.g., &lt;=2% mismatch) for Tier 1 groups; failures trigger containment.",
          "failure_policy": "block_promotion_or_require_owner_signoff",
          "evidence_outputs": [
            "sampling_results",
            "verification_mismatch_rate"
          ]
        }
      ],
      "outputs": [
        "load_ready_packages"
      ]
    },
    {
      "layer_id": "L6_controlled_load",
      "name": "L6 — Controlled Load (MDG Intake)",
      "purpose": "Load into MDG under strict controls: batch IDs, staged waves, rollback/containment, monitoring.",
      "typical_assets": [
        "load batches/waves",
        "cutover runbook steps",
        "technical logs",
        "promotion approvals"
      ],
      "quality_gates": [
        {
          "gate_id": "gate_load_technical_success",
          "description": "Load jobs succeed without critical technical failures; failed records remain traceable and retryable.",
          "failure_policy": "stop_or_retry_with_limits",
          "evidence_outputs": [
            "load_job_logs",
            "failed_record_registry"
          ]
        }
      ],
      "outputs": [
        "mdg_created_or_changed_records"
      ]
    },
    {
      "layer_id": "L7_governed_promotion",
      "name": "L7 — Governed Promotion (Golden/Active State)",
      "purpose": "Promote loaded records into active governance state: workflows closed, ownership established, rules applied, replication initiated.",
      "typical_assets": [
        "final approvals",
        "closed CR evidence",
        "decision notes",
        "active rule registry references"
      ],
      "quality_gates": [
        {
          "gate_id": "gate_auditability_minimum",
          "description": "For Tier 1 records: owner decision, rule outcomes, and exception trace exist (audit-ready).",
          "failure_policy": "block_promotion_or_hold_records",
          "evidence_outputs": [
            "audit_trail_completeness_report"
          ]
        }
      ],
      "outputs": [
        "governed_master_data_in_mdg"
      ]
    },
    {
      "layer_id": "L8_replication_and_reconciliation",
      "name": "L8 — Replication &amp; Reconciliation (Downstream Reality Check)",
      "purpose": "Replicate to S/4 and consumers; reconcile and detect drift; prohibit silent downstream fixes.",
      "typical_assets": [
        "interface monitoring",
        "error taxonomy",
        "runbooks",
        "reconciliation reports"
      ],
      "quality_gates": [
        {
          "gate_id": "gate_replication_stability",
          "description": "Replication error rate is within limits; backlog aging within SLA; top categories owned with runbooks.",
          "failure_policy": "containment_mode",
          "evidence_outputs": [
            "replication_error_rate_by_category",
            "backlog_aging_over_sla",
            "mttr"
          ]
        }
      ],
      "outputs": [
        "stable_consumption_in_s4_and_beyond"
      ]
    }
  ],
  "event_model": {
    "event_types": [
      "extract_created",
      "ingestion_completed",
      "mapping_applied",
      "cleansing_decision_made",
      "exception_approved",
      "package_promoted",
      "load_executed",
      "record_promoted_to_governed",
      "replication_succeeded",
      "replication_failed",
      "reconciliation_completed"
    ],
    "load_event_schema": {
      "load_event_id": "string",
      "entity": "BP|Material|RefData",
      "scope": "string",
      "batch_or_wave": "string",
      "source_package_id": "string",
      "target_system": "sys_mdg",
      "timestamp": "date-time",
      "initiated_by": "role",
      "approvals": [
        "string"
      ],
      "quality_gate_results": [
        {
          "gate_id": "string",
          "status": "pass|fail|pass_with_exception",
          "evidence_ref": "string"
        }
      ],
      "result_summary": {
        "records_total": "number",
        "records_loaded": "number",
        "records_failed": "number"
      },
      "rollback_possible": "boolean",
      "notes": "string"
    }
  },
  "governance_controls": {
    "must_have_controls": [
      "No silent fixes downstream (policy + monitoring + escalation)",
      "Exception register with expiry for Tier 1/2",
      "Reference data alignment gate before load",
      "Sampling verification gate for Tier 1",
      "Traceability: record -&gt; source package -&gt; mapping -&gt; decisions -&gt; load event"
    ],
    "control_ownership": [
      {
        "control": "reference_alignment_gate",
        "owner_role": "Reference Data Owner"
      },
      {
        "control": "tier1_quality_gate",
        "owner_role": "Data Owner"
      },
      {
        "control": "load_event_logging",
        "owner_role": "MDG Ops Lead"
      },
      {
        "control": "replication_runbooks",
        "owner_role": "Integration Team + MDG Ops Lead"
      }
    ]
  },
  "key_metrics_for_gating": [
    {
      "metric_id": "verification_mismatch_rate",
      "use": "Gate L5 -&gt; L6",
      "target_hint": "&lt;=2% in sampling for Tier1"
    },
    {
      "metric_id": "customizing_mismatch_rate",
      "use": "Gate L3 -&gt; L4",
      "target_hint": "near-zero for in-scope value sets"
    },
    {
      "metric_id": "backlog_aging_over_sla",
      "use": "Gate L8 stability",
      "target_hint": "&lt;10% over SLA"
    },
    {
      "metric_id": "manual_post_replication_fix_rate",
      "use": "Governance integrity",
      "target_hint": "near-zero"
    },
    {
      "metric_id": "bypass_rate",
      "use": "Governance drift",
      "target_hint": "&lt;=5% and trending down"
    }
  ],
  "deliverables_mapping": {
    "where_artifacts_live": [
      {
        "artifact": "systems_registry.json",
        "layer": "L0/L6",
        "reason": "Boundaries and SoR decisions"
      },
      {
        "artifact": "interfaces_registry.json",
        "layer": "L8",
        "reason": "Replication operations and monitoring"
      },
      {
        "artifact": "value_mapping_catalog.json",
        "layer": "L3",
        "reason": "Meaning-preserving mapping"
      },
      {
        "artifact": "exception_register.json",
        "layer": "L4/L7",
        "reason": "Controlled deviations with expiry"
      },
      {
        "artifact": "reconciliation_reports.json",
        "layer": "L8",
        "reason": "Detect drift and mismatch"
      },
      {
        "artifact": "load_events.json",
        "layer": "L6",
        "reason": "Auditability and replay"
      }
    ]
  },
  "ai_reasoning_hooks": [
    "AI can evaluate gate failures and pick Metric-Decision playbooks",
    "AI can explain which layer failed (e.g., L3 reference alignment) and propose next actions with citations",
    "RAG corpus should include: mapping catalogs, exception register, runbooks, load events, and reconciliation reports"
  ],
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "DAMA",
    "source_project": "cv-ai",
    "source_path": "DAMA/mdg_migration_data_architecture_v0_1.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Mdg Migration Data Architecture V0 1” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/DAMA/mdg_migration_data_architecture_v0_1.json"
    },
    "license": {
      "name": "Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)",
      "spdx": "CC-BY-NC-4.0",
      "url": "https://creativecommons.org/licenses/by-nc/4.0/"
    },
    "links": {
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau",
      "repository": "https://github.com/dkharlanau/dkharlanau-datasets"
    },
    "contact": {
      "preferred": "linkedin",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "canonical_url": "https://dkharlanau.github.io/datasets/DAMA/mdg_migration_data_architecture_v0_1.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-04-13T08:37:04+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "title_inferred": true,
    "entity_type": "mdg_byte",
    "entity_subtype": "",
    "summary": "Mdg Migration Data Architecture V0 1",
    "doi": {
      "concept": "10.5281/zenodo.18862098",
      "version": "10.5281/zenodo.18862097",
      "repository": "https://github.com/dkharlanau/dkharlanau-datasets"
    }
  },
  "title": "Mdg Migration Data Architecture V0 1"
}
</code></pre>

</details>
</div>
