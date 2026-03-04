---
layout: default
title: "Mdg Metric Decision Playbooks V0 1"
description: "Translate breached metrics into deterministic governance actions via linked Decision Blocks."
permalink: /datasets/view/DAMA/mdg_metric_decision_playbooks_v0_1/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Mdg Metric Decision Playbooks V0 1</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">DAMA</span>
    <span class="pill pill--type">mdg_byte</span>
    <span class="pill">mdg_metric_decision_playbooks_v0_1</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/DAMA/mdg_metric_decision_playbooks_v0_1.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/DAMA/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Translate breached metrics into deterministic governance actions via linked Decision Blocks.</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>License &amp; citation</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/DAMA/mdg_metric_decision_playbooks_v0_1.json">https://dkharlanau.github.io/datasets/DAMA/mdg_metric_decision_playbooks_v0_1.json</a></p>
    <p>License: <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC 4.0</a> (non-commercial, attribution required).</p>
    <p>Concept DOI: <a href="https://doi.org/10.5281/zenodo.18862098" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862098</a></p>
    <p>Version DOI (`v1.0.0`): <a href="https://doi.org/10.5281/zenodo.18862097" target="_blank" rel="noopener noreferrer">10.5281/zenodo.18862097</a></p>
    <p>Repository: <a href="https://github.com/dkharlanau/dkharlanau-datasets" target="_blank" rel="noopener noreferrer">https://github.com/dkharlanau/dkharlanau-datasets</a></p>
    <p>Suggested citation: Dzmitryi Kharlanau. “Mdg Metric Decision Playbooks V0 1” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/DAMA/mdg_metric_decision_playbooks_v0_1.json</p>
    <p>Details: <a href="/legal/datasets/">/legal/datasets/</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Mdg Metric Decision Playbooks V0 1",
  "description": "Translate breached metrics into deterministic governance actions via linked Decision Blocks.",
  "url": "https://dkharlanau.github.io/datasets/view/DAMA/mdg_metric_decision_playbooks_v0_1/",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "citation": "Dzmitryi Kharlanau. “Mdg Metric Decision Playbooks V0 1” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/DAMA/mdg_metric_decision_playbooks_v0_1.json",
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
      "contentUrl": "https://dkharlanau.github.io/datasets/DAMA/mdg_metric_decision_playbooks_v0_1.json"
    }
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "mdg_metric_decision_playbooks_v0_1",
  "purpose": "Translate breached metrics into deterministic governance actions via linked Decision Blocks.",
  "rules": [
    "React to trends, not single spikes",
    "Prefer smallest viable intervention",
    "Escalate only if previous step failed"
  ],
  "playbooks": [
    {
      "metric_id": "bypass_rate",
      "when": {
        "warning": "&gt;5% for 2 consecutive periods",
        "critical": "&gt;10% in any period"
      },
      "diagnosis_hypotheses": [
        "Governance friction too high",
        "Wrong tiering for attribute groups",
        "Approval cycle time too long",
        "Rules misaligned with business flow"
      ],
      "decision_blocks": [
        "db_domain_attribute_prioritization_scope_v0_1",
        "db_change_management_for_governance_v0_1",
        "db_rule_lifecycle_management_keep_kill_simplify_v0_1"
      ],
      "actions": {
        "warning": [
          "Identify top bypassed attribute groups (top 5)",
          "Re-tier low-impact attributes to Tier 3",
          "Downgrade selected blocking rules to warnings",
          "Communicate intent and temporary tolerance window"
        ],
        "critical": [
          "Freeze new governance scope immediately",
          "Trigger keep/kill/simplify review for top rules",
          "Shorten approval paths for Tier 3",
          "Assign executive sponsor for Tier 1 friction review"
        ]
      },
      "success_criteria": [
        "Bypass rate decreases within 2 periods",
        "No increase in Tier 1 incidents"
      ]
    },
    {
      "metric_id": "approval_cycle_time_p90",
      "when": {
        "warning": "&gt;3d",
        "critical": "&gt;7d"
      },
      "diagnosis_hypotheses": [
        "Owner capacity overload",
        "Too many attributes routed to same approver",
        "Over-scoped Tier 1",
        "Missing backup approvers"
      ],
      "decision_blocks": [
        "db_operating_model_day2_day100_v0_1",
        "db_attribute_level_ownership_decision_rights_v0_1",
        "db_domain_attribute_prioritization_scope_v0_1"
      ],
      "actions": {
        "warning": [
          "Add backup approvers for overloaded owners",
          "Shift non-critical attributes to Tier 2/3 routing",
          "Introduce SLA-based escalation"
        ],
        "critical": [
          "Reassign ownership for overloaded attribute groups",
          "Split attribute groups by decision complexity",
          "Temporarily relax approvals for Tier 3"
        ]
      },
      "success_criteria": [
        "p90 returns below threshold",
        "No spike in rework or bypass"
      ]
    },
    {
      "metric_id": "exception_repeat_rate",
      "when": {
        "warning": "&gt;20%",
        "critical": "&gt;35%"
      },
      "diagnosis_hypotheses": [
        "Rule design incorrect",
        "Enforcement point wrong",
        "Business reality not reflected in rules"
      ],
      "decision_blocks": [
        "db_rule_lifecycle_management_keep_kill_simplify_v0_1"
      ],
      "actions": {
        "warning": [
          "Identify top repeating exceptions (top 3)",
          "Review rule rationale and scope",
          "Add expiry and tighter criteria to exceptions"
        ],
        "critical": [
          "Simplify or retire offending rules",
          "Move rule from error to warning or derivation",
          "Redesign rule with owner and business examples"
        ]
      },
      "success_criteria": [
        "Repeat exceptions decrease next period",
        "Blocking error rate does not increase"
      ]
    },
    {
      "metric_id": "manual_post_replication_fix_rate",
      "when": {
        "warning": "&gt;3%",
        "critical": "&gt;7%"
      },
      "diagnosis_hypotheses": [
        "Semantic gaps between MDG and downstream",
        "Reference/customizing mismatch",
        "Silent operational fixes"
      ],
      "decision_blocks": [
        "db_replication_errors_accountability_runbook_v0_1"
      ],
      "actions": {
        "warning": [
          "Enforce no-silent-fix policy",
          "Classify top errors by category",
          "Align reference data/customizing"
        ],
        "critical": [
          "Block downstream manual fixes",
          "Force correction at source (MDG)",
          "Escalate to architecture for enforcement redesign"
        ]
      },
      "success_criteria": [
        "Manual fixes trend down",
        "Replication success rate improves"
      ]
    },
    {
      "metric_id": "decision_consistency_rate",
      "when": {
        "warning": "&lt;85%",
        "critical": "&lt;70%"
      },
      "diagnosis_hypotheses": [
        "Decision rights unclear",
        "Owners apply different criteria",
        "Rules or definitions ambiguous"
      ],
      "decision_blocks": [
        "db_attribute_level_ownership_decision_rights_v0_1",
        "db_rule_lifecycle_management_keep_kill_simplify_v0_1"
      ],
      "actions": {
        "warning": [
          "Align decision criteria with examples",
          "Update glossary and rule descriptions",
          "Run calibration session with owners"
        ],
        "critical": [
          "Reassign accountable owner for affected groups",
          "Introduce peer review for high-risk decisions",
          "Freeze rule changes until criteria stabilized"
        ]
      },
      "success_criteria": [
        "Consistency rate improves",
        "Reversal rate decreases"
      ]
    },
    {
      "metric_id": "ownership_coverage_tier1",
      "when": {
        "warning": "&lt;95%",
        "critical": "&lt;85%"
      },
      "diagnosis_hypotheses": [
        "Governance capacity insufficient",
        "Ownership defined too broadly",
        "No backup owners"
      ],
      "decision_blocks": [
        "db_attribute_level_ownership_decision_rights_v0_1",
        "db_domain_attribute_prioritization_scope_v0_1"
      ],
      "actions": {
        "warning": [
          "Assign missing owners and backups",
          "Reduce Tier 1 scope if needed"
        ],
        "critical": [
          "Pause new Tier 1 controls",
          "Re-tier attribute groups to match capacity",
          "Escalate to governance sponsor"
        ]
      },
      "success_criteria": [
        "Tier 1 coverage restored",
        "Approval SLAs stabilize"
      ]
    }
  ],
  "ai_execution_note": "AI should select the playbook based on breached metric and severity, summarize diagnosis, propose actions in order, and track outcomes against success criteria.",
  "version": "0.1",
  "status": "draft",
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "DAMA",
    "source_project": "cv-ai",
    "source_path": "DAMA/mdg_metric_decision_playbooks_v0_1.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau. “Mdg Metric Decision Playbooks V0 1” (dataset bytes). CC BY-NC 4.0. DOI: 10.5281/zenodo.18862098. https://dkharlanau.github.io/datasets/DAMA/mdg_metric_decision_playbooks_v0_1.json"
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
    "canonical_url": "https://dkharlanau.github.io/datasets/DAMA/mdg_metric_decision_playbooks_v0_1.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-03-04T11:23:27+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "title_inferred": true,
    "entity_type": "mdg_byte",
    "entity_subtype": "version:0.1",
    "summary": "Translate breached metrics into deterministic governance actions via linked Decision Blocks.",
    "doi": {
      "concept": "10.5281/zenodo.18862098",
      "version": "10.5281/zenodo.18862097",
      "repository": "https://github.com/dkharlanau/dkharlanau-datasets"
    }
  },
  "title": "Mdg Metric Decision Playbooks V0 1"
}
</code></pre>

</details>
</div>
