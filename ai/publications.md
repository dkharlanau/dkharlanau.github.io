---
layout: default
title: Publications Dataset
description: "Markdown dataset of public publications, technical notes, and knowledge surfaces by Dzmitryi Kharlanau."
permalink: /ai/publications/
sitemap: true
last_modified_at: 2026-04-24
hide_global_cta: true
---

# Publications Dataset

Source: `Basic_LinkedInDataExport_04-10-2026/Publications.csv`

Updated: 2026-04-24

Privacy note: {{ site.data.publications.privacy_note }}

| Name | Publisher | Published | Category | Description | URL |
| --- | --- | --- | --- | --- | --- |
{% for item in site.data.publications.items -%}
| {{ item.name | replace: '|', '/' }} | {{ item.publisher }} | {{ item.published | default: "Not listed" }} | {{ item.category }} | {{ item.description | default: "" | replace: '|', '/' }} | [Open]({{ item.url }}) |
{% endfor %}
