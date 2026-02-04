---
layout: default
title: "Decision Rights &amp; RACI for Master Data (Who decides what?)"
description: "Decision Rights &amp; RACI for Master Data (Who decides what?)"
permalink: /datasets/view/DAMA/db_governance_decision_rights_v0_1/
sitemap: true
---

<div class="dataset-hero">
  <p class="eyebrow">Dataset entry</p>
  <h1 class="dataset-hero__title">Decision Rights &amp; RACI for Master Data (Who decides what?)</h1>
  <div class="dataset-hero__meta">
    <span class="pill pill--dataset">DAMA</span>
    <span class="pill pill--type">data_governance_byte</span>
    <span class="pill">db_governance_decision_rights_v0_1</span>
    <span class="pill">governance</span> <span class="pill">raci</span> <span class="pill">ownership</span> <span class="pill">accountability</span> <span class="pill">operating_model</span>
  </div>
  <div class="dataset-actions">
    <a class="button" href="/datasets/DAMA/db_governance_decision_rights_v0_1.json">Open JSON</a>
    <a class="button button--secondary" href="/datasets/DAMA/">Back to list</a>
  </div>
</div>

<div class="neub-card dataset-entry-lead">Decision Rights &amp; RACI for Master Data (Who decides what?)</div>

<div class="dataset-grid dataset-grid--wide">
  <div class="neub-card">
    <h2>Attribution</h2>
    <p>Creator: <strong>Dzmitryi Kharlanau</strong> (SAP Lead).</p>
    <p>Canonical: <a href="https://dkharlanau.github.io/datasets/DAMA/db_governance_decision_rights_v0_1.json">https://dkharlanau.github.io/datasets/DAMA/db_governance_decision_rights_v0_1.json</a></p>
    <p><a class="link-arrow" href="https://www.linkedin.com/in/dkharlanau" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
  </div>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Decision Rights & RACI for Master Data (Who decides what?)",
  "description": "Decision Rights & RACI for Master Data (Who decides what?)",
  "url": "https://dkharlanau.github.io/datasets/view/DAMA/db_governance_decision_rights_v0_1/",
  "isAccessibleForFree": true,
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
      "contentUrl": "https://dkharlanau.github.io/datasets/DAMA/db_governance_decision_rights_v0_1.json"
    }
  ],
  "keywords": [
    "governance",
    "raci",
    "ownership",
    "accountability",
    "operating_model"
  ]
}
</script>

<div class="dataset-json">
<details open>
<summary>JSON (copy / reuse)</summary>

<pre><code class="language-json">{
  "id": "db_governance_decision_rights_v0_1",
  "type": "decision_block",
  "title": "Decision Rights &amp; RACI for Master Data (Who decides what?)",
  "dama_alignment": {
    "knowledge_areas": [
      "Data Governance",
      "Reference &amp; Master Data",
      "Data Quality",
      "Metadata"
    ],
    "principles": [
      "Explicit decision rights",
      "Clear accountability (RACI)",
      "Policies enforced by controls + exception flow"
    ]
  },
  "scope": {
    "domains": [
      "Master Data"
    ],
    "subdomains": [
      "Business Partner",
      "Material",
      "Reference Data"
    ],
    "processes": [
      "Create",
      "Change",
      "Approve",
      "Replicate",
      "Exception Handling"
    ]
  },
  "tags": [
    "governance",
    "raci",
    "ownership",
    "accountability",
    "operating_model"
  ],
  "decision_question": "How do we assign decision rights and responsibilities for master data changes so governance is enforceable and does not drift into bypass/shadow processes?",
  "context": {
    "when_to_use": [
      "Starting or reworking MDG/MDM operating model",
      "Approvals are slow or inconsistent",
      "Business bypasses governance by changing data directly downstream",
      "Multiple teams argue about who 'owns' a field"
    ],
    "preconditions": [
      "Domains are defined (e.g., BP, Material, Reference Data)",
      "At least one business function is willing to own outcomes (not just tasks)"
    ]
  },
  "inputs": {
    "signals_observable": [
      "Approval cycle time (p50/p90) exceeds agreed SLA or is undefined",
      "Rejections occur without meaningful comments or clear criteria",
      "Same attribute is maintained by multiple teams/systems",
      "Downstream manual fixes are common after replication",
      "Recurring disputes: 'not my responsibility' for data defects"
    ],
    "constraints": [
      "Segregation of duties (SoD) requirements (if applicable)",
      "Regulatory / audit requirements for specific attributes",
      "Business capacity: named owners must have time to approve",
      "System landscape complexity (MDG hub, S/4, legacy consumers)"
    ],
    "stakeholders": [
      "Data Owner (business accountable role)",
      "Data Steward (operational quality role)",
      "IT/MDG Team (custodian/enabler)",
      "Architecture/Integration",
      "Compliance/Audit (if required)"
    ]
  },
  "options": [
    {
      "id": "A",
      "name": "Owner-based model (recommended default)",
      "summary": "Assign a single accountable Data Owner per domain; Stewards execute quality; IT enforces controls.",
      "tradeoffs": [
        "Requires real business ownership (hard to negotiate)",
        "Owner must commit to SLA to avoid bottlenecks"
      ]
    },
    {
      "id": "B",
      "name": "Steward-led approvals (temporary / transitional)",
      "summary": "Data Steward approves most changes; Data Owner approves only high-impact changes via thresholds.",
      "tradeoffs": [
        "Risk of weak accountability (quality becomes 'IT problem')",
        "Owners disengage; governance may drift"
      ]
    },
    {
      "id": "C",
      "name": "Committee approvals (avoid unless mandatory)",
      "summary": "Council/committee approves changes by consensus or meetings.",
      "tradeoffs": [
        "High cycle time and high bypass risk",
        "Hard to scale; ownership becomes diluted"
      ]
    }
  ],
  "decision_logic": {
    "preferred_option_rules": [
      {
        "if": [
          "There is recurring bypass/shadow maintenance",
          "Approval cycle time is a top complaint",
          "Ownership is unclear or disputed"
        ],
        "then": "Choose Option A and define decision rights per attribute group with one accountable owner."
      },
      {
        "if": [
          "Business owners are not yet ready to take full load",
          "You need a fast stabilization phase (e.g., migration/cutover)"
        ],
        "then": "Use Option B with explicit thresholds and a deadline to transition to Option A."
      },
      {
        "if": [
          "Regulation requires multi-party approval",
          "You can prove capacity and SLA adherence"
        ],
        "then": "Option C only for the regulated subset of attributes, not as a global model."
      }
    ],
    "anti_patterns_to_avoid": [
      "Approval without ownership (many approvers, nobody accountable)",
      "IT becomes de-facto owner of business semantics",
      "Undefined exception path → users bypass governance"
    ],
    "exceptions_flow": [
      "Define a 'fast-track' exception for urgent operational cases",
      "Every exception must have: reason, accountable approver, expiry date, and post-review",
      "Exception quotas (optional): if exceptions exceed threshold → governance redesign trigger"
    ]
  },
  "expected_outcomes": {
    "positive": [
      "Clear accountability for data defects and improvements",
      "Reduced decision disputes and faster resolution",
      "Lower bypass rate because governance becomes usable",
      "Better auditability (who approved what and why)"
    ],
    "possible_negative": [
      "If owners are overloaded, cycle time may initially increase",
      "Political friction while assigning ownership"
    ]
  },
  "controls_enforcement": {
    "policies": [
      {
        "id": "pol_ownership_required_v0_1",
        "statement": "Every governed attribute must have one accountable Data Owner and one operational Data Steward."
      }
    ],
    "standards": [
      {
        "id": "std_raci_minimum_v0_1",
        "statement": "For each domain, maintain a RACI matrix at attribute-group level (not just object level)."
      }
    ],
    "technical_controls": [
      "Workflow routing based on domain + attribute group",
      "Mandatory justification fields for critical changes",
      "Mandatory comment on rejection",
      "Escalation after SLA breach"
    ]
  },
  "owner_rights_raci": {
    "accountable": [
      "Data Owner"
    ],
    "responsible": [
      "Data Steward"
    ],
    "consulted": [
      "IT/MDG Team",
      "Architecture/Integration",
      "Compliance/Audit (if applicable)"
    ],
    "informed": [
      "Business Users",
      "Downstream System Owners"
    ]
  },
  "metrics": {
    "operational": [
      {
        "name": "approval_cycle_time_p50",
        "target_hint": "Define per domain; track weekly"
      },
      {
        "name": "approval_cycle_time_p90",
        "target_hint": "Key for pain; should not explode"
      },
      {
        "name": "bypass_rate",
        "definition": "Share of changes made outside governed process"
      },
      {
        "name": "rejection_without_comment_rate",
        "target_hint": "Near 0%"
      }
    ],
    "data_quality_dimensions": [
      "completeness",
      "consistency",
      "validity",
      "uniqueness",
      "timeliness"
    ],
    "governance_health": [
      {
        "name": "ownership_coverage",
        "definition": "% of governed attributes with assigned accountable owner"
      },
      {
        "name": "exception_rate",
        "definition": "Exceptions per 100 change requests"
      }
    ]
  },
  "examples_generic": [
    {
      "scenario": "BP master data changes are delayed for days; business updates directly in S/4 to ship orders.",
      "application": "Assign a Data Owner for BP domain; keep stewards operational; introduce SLA + escalation; add fast-track exception with expiry."
    },
    {
      "scenario": "Two regions fight about who owns tax classification; changes get rejected without comments.",
      "application": "Split decision rights by attribute group; make rejection comment mandatory; define one accountable owner per group."
    }
  ],
  "version": "0.1",
  "status": "draft",
  "meta": {
    "schema": "dkharlanau.dataset.byte",
    "schema_version": "1.1",
    "dataset": "DAMA",
    "source_project": "cv-ai",
    "source_path": "DAMA/db_governance_decision_rights_v0_1.json",
    "generated_at_utc": "2026-02-03T14:33:32+00:00",
    "creator": {
      "name": "Dzmitryi Kharlanau",
      "role": "SAP Lead",
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "attribution": {
      "attribution_required": true,
      "preferred_citation": "Dzmitryi Kharlanau (SAP Lead). Dataset bytes: https://dkharlanau.github.io"
    },
    "license": {
      "name": "",
      "spdx": "",
      "url": ""
    },
    "links": {
      "website": "https://dkharlanau.github.io",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "contact": {
      "preferred": "linkedin",
      "linkedin": "https://www.linkedin.com/in/dkharlanau"
    },
    "canonical_url": "https://dkharlanau.github.io/datasets/DAMA/db_governance_decision_rights_v0_1.json",
    "created_at_utc": "2026-02-03T14:33:32+00:00",
    "updated_at_utc": "2026-02-03T15:29:02+00:00",
    "provenance": {
      "source_type": "chat_export_extraction",
      "note": "Extracted and curated by Dzmitryi Kharlanau; enriched for attribution and crawler indexing."
    },
    "entity_type": "data_governance_byte",
    "entity_subtype": "version:0.1",
    "summary": "Decision Rights &amp; RACI for Master Data (Who decides what?)"
  }
}
</code></pre>

</details>
</div>
