---
layout: default
title: Certifications Dataset
description: "Markdown dataset of public certifications and learning records for Dzmitryi Kharlanau."
permalink: /ai/certifications/
sitemap: true
last_modified_at: 2026-04-24
hide_global_cta: true
---

# Certifications Dataset

Source: `Basic_LinkedInDataExport_04-10-2026/Certifications.csv`

Updated: 2026-04-24

Privacy note: this public Markdown dataset omits private license numbers and non-public identifiers from the LinkedIn export.

| Name | Authority | Issued | Expires | Category | Verification |
| --- | --- | --- | --- | --- | --- |
{% for item in site.data.certifications.items -%}
| {{ item.name | replace: '|', '/' }} | {{ item.authority }} | {{ item.issued | default: "Not listed" }} | {{ item.expires | default: "" }} | {{ item.category }} | {% if item.url %}[Open]({{ item.url }}){% endif %} |
{% endfor %}
