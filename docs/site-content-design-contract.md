# Site Content and Design Contract

Status: living contract
Owner: Dzmitryi Kharlanau
Last updated: 2026-05-25
Purpose: guide agent-assisted updates to `dkharlanau.github.io` so new content fits the site visually, structurally, and strategically.

## 1. Site role

This site is the canonical public professional layer for Dzmitryi Kharlanau.

It should communicate:
- SAP and enterprise systems experience;
- logistics/process reality;
- SAP AMS, SD/MM, master data, integrations, and support operations;
- practical AI and automation;
- architecture decisions that reduce TCO;
- avoidance of unnecessary vendor lock-in;
- practical innovation without hype.

The site is not a generic blog and not a news dump.

## 2. Design principle

Every new page or section must support the existing visual system:

- clean professional layout;
- strong hero / page heading;
- compact cards;
- short paragraphs;
- clear CTAs;
- evidence links;
- readable scanning structure;
- restrained visual density;
- no random component styles.

If the agent cannot identify the existing layout pattern for a new item, it must create a draft or issue instead of adding a visually inconsistent page.

## 3. Content placement rules

| Content type | Place it here | Do not place it here |
|---|---|---|
| Durable concept | Atlas / public knowledge page | News feed only |
| Dated professional signal | News section | Main homepage hero |
| Service offer | Services section | Dataset page |
| Reusable evidence byte | Datasets | Random blog-like page |
| Source / citation policy | AI sources / legal / dataset metadata | Main sales copy |
| Personal positioning | Home / About / Services | News item |
| Social draft source | Materialist OS social drafts | Public page unless approved |

## 4. Page type rules

### Home page

Purpose:
- top-level positioning;
- trust signal;
- strategic frame;
- key CTAs.

Allowed updates:
- small copy refinement;
- updated trust metrics only with source;
- new navigation link if a major site section is added;
- improved CTA if it clarifies the user journey.

Avoid:
- adding every new signal;
- adding long explanations;
- adding temporary news;
- changing positioning without reviewing the full site.

### Services pages

Purpose:
- explain how Dzmitryi can help;
- translate expertise into entry points;
- show concrete pains and outputs.

Allowed updates:
- new service card;
- refined service copy;
- clearer fit/non-fit section;
- CTA updates;
- links to relevant Atlas/news/datasets.

Required structure:
- problem;
- who it helps;
- what is delivered;
- boundaries/non-goals;
- next step.

### Atlas / public knowledge pages

Purpose:
- durable explanations;
- practical frameworks;
- stable professional knowledge.

Allowed updates:
- factual update;
- new source;
- new practical pattern;
- new checklist;
- clarification of architecture/process implication.

Required fields or nearby metadata:
- source;
- date checked;
- confidence;
- related topic;
- practical implication.

Avoid:
- dated news without evergreen value;
- vendor press-release summaries;
- large unstructured essays;
- unsupported claims.

### News section

Purpose:
- dated timeline of professional signals;
- short factual notes;
- links into durable pages.

Allowed updates:
- short dated item;
- weekly digest;
- release/source note;
- signal summary.

Required structure:
- title;
- date;
- source URL;
- summary;
- why it matters;
- related page/topic;
- confidence;
- tags.

Avoid:
- turning news into long articles;
- duplicating Atlas content;
- publishing weak-source opinions.

### Datasets

Purpose:
- reusable bytes for readers, AI systems, citations, and public evidence.

Allowed updates:
- structured entries;
- manifest updates;
- schema-compliant additions;
- attribution/citation metadata.

Avoid:
- vague notes;
- non-structured commentary;
- content without source or citation context.

## 5. Visual consistency rules

Before changing or adding a page, the agent must inspect the nearest existing page or component pattern.

The agent must preserve:
- existing navigation style;
- footer style;
- card spacing;
- heading hierarchy;
- CTA style;
- tone of section labels;
- short paragraph rhythm;
- evidence/reference presentation.

Do not introduce:
- new colors without design review;
- new typography scale without design review;
- random icons or emoji;
- dense tables on marketing pages;
- long wall-of-text sections;
- inconsistent button labels;
- duplicate navigation concepts.

## 6. Information architecture rules

Every new page must answer:

1. What section does this belong to?
2. What user journey does it support?
3. What existing page should link to it?
4. What page should it link back to?
5. Is it evergreen, dated, service-oriented, or dataset content?
6. Is it for humans, AI/crawlers, or both?

If these questions cannot be answered, do not add the page directly. Create a draft or issue.

## 7. Design review checklist

Before accepting a site update:

- Does it fit an existing page type?
- Does it use the existing layout pattern?
- Is the section short enough to scan?
- Does the heading tell the reader what this is?
- Is there a clear next action or related link?
- Is the content placed in the correct section?
- Are sources and confidence visible where needed?
- Is there any duplicate text already elsewhere on the site?
- Does it support the broader positioning, not only SAP AMS?
- Does it avoid hype, vendor worship, and generic AI copy?

## 8. Agent update workflow

For any site addition, the agent should follow this sequence:

```text
1. Inspect existing site structure and nearest similar page.
2. Identify content type: home / service / Atlas / news / dataset / legal / source.
3. Select target path and layout pattern.
4. Generate a small draft or patch.
5. Check internal links and metadata.
6. Run site validation/build if available.
7. Report changed files, design pattern used, validation result, and remaining risk.
```

## 9. When to create an issue instead of changing the site

Create an issue when:

- the correct page location is unclear;
- the new content requires a new layout pattern;
- homepage positioning would change;
- navigation would change significantly;
- a new content type is introduced;
- the update depends on weak or incomplete sources;
- the design impact is larger than a small content addition.

## 10. Relationship to Professional Radar

Professional Radar may propose:
- news items;
- Atlas additions;
- service page refinements;
- dataset additions;
- social drafts.

But every public site update must pass this contract first.

The public site should remain coherent even if Professional Radar produces many signals.

## 11. Keep this file current

Update this contract when:
- the site design system changes;
- navigation changes;
- new page types are introduced;
- Atlas structure changes;
- Professional Radar starts producing visually inconsistent updates;
- repeated placement mistakes appear.
