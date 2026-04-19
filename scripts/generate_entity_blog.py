#!/usr/bin/env python3
"""
Generate a one-time, SEO-ready blog post from a dataset entity using OpenAI Responses API.

Usage:
  /usr/bin/python3 scripts/generate_entity_blog.py --entity ams
  /usr/bin/python3 scripts/generate_entity_blog.py --entity DAMA --output _blog/dama-dataset-overview.md
"""

import argparse
import datetime as dt
import glob
import json
import os
import textwrap
import urllib.error
import urllib.request


DEFAULT_MODEL = os.environ.get("OPENAI_MODEL", "gpt-5")
DEFAULT_BASE_URL = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1/responses")
DEFAULT_MAX_ITEMS = 60


SUMMARY_KEYS = [
    "summary",
    "description",
    "purpose",
    "hook",
    "idea",
    "overview",
    "statement",
    "value",
]


def read_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def first_string(data, keys):
    for key in keys:
        value = data.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def truncate(text, limit=220):
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def extract_entry(data):
    entry_id = data.get("id") or data.get("slug") or data.get("name") or "unknown"
    title = data.get("title") or data.get("name") or entry_id
    summary = first_string(data, SUMMARY_KEYS)
    tags = data.get("tags") or data.get("keywords") or []
    if isinstance(tags, str):
        tags = [tags]
    if not isinstance(tags, list):
        tags = []
    return {
        "id": entry_id,
        "title": title,
        "type": data.get("type"),
        "summary": truncate(summary) if summary else "",
        "tags": [t for t in tags if isinstance(t, str)],
    }


def build_dataset_context(entity, dataset_dir, max_items):
    json_files = sorted(glob.glob(os.path.join(dataset_dir, "*.json")))
    entries = []
    type_counts = {}
    tag_counts = {}
    for path in json_files:
        data = read_json(path)
        entry = extract_entry(data)
        entries.append(entry)
        if entry["type"]:
            type_counts[entry["type"]] = type_counts.get(entry["type"], 0) + 1
        for tag in entry["tags"]:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

    entries = entries[:max_items]
    top_tags = sorted(tag_counts.items(), key=lambda item: item[1], reverse=True)[:15]
    return {
        "entity": entity,
        "entry_count": len(json_files),
        "types": type_counts,
        "top_tags": [tag for tag, _ in top_tags],
        "entries": entries,
    }


def build_prompt(entity, dataset_index_url, dataset_manifest_url, dataset_context):
    return textwrap.dedent(
        f"""
        You are generating a single Markdown blog post about the {entity} dataset collection.
        The output must be valid JSON that matches the provided schema.
        Use the dataset summary JSON below as your only source.

        Constraints:
        - 900 to 1200 words.
        - Use Markdown only. No HTML.
        - Use H2 headings (##) for sections.
        - No nested lists.
        - Include a "Featured entries" section with 6 to 10 bullet items.
        - Mention and link to the dataset index at {dataset_index_url}.
        - Mention and link to the dataset manifest at {dataset_manifest_url}.
        - Write in a confident, concise, consulting tone.

        Dataset summary JSON:
        {json.dumps(dataset_context, ensure_ascii=False, indent=2)}
        """
    ).strip()


def call_openai(prompt, model, api_key, base_url):
    schema = {
        "type": "object",
        "properties": {
            "title": {"type": "string", "minLength": 20, "maxLength": 90},
            "subtitle": {"type": "string", "minLength": 40, "maxLength": 180},
            "meta_description": {"type": "string", "minLength": 80, "maxLength": 160},
            "tags": {"type": "array", "items": {"type": "string"}, "minItems": 4, "maxItems": 12},
            "body_markdown": {"type": "string", "minLength": 1200},
        },
        "required": ["title", "subtitle", "meta_description", "tags", "body_markdown"],
        "additionalProperties": False,
    }

    payload = {
        "model": model,
        "instructions": (
            "Return JSON only. The JSON must match the schema. "
            "Do not include Markdown outside the body_markdown field."
        ),
        "input": prompt,
        "text": {
            "format": {
                "type": "json_schema",
                "name": "entity_blog_post",
                "strict": True,
                "schema": schema,
            }
        },
        "temperature": 0.3,
    }

    request = urllib.request.Request(
        base_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=120) as response:
        return json.loads(response.read().decode("utf-8"))


def extract_output_text(response):
    output = response.get("output", [])
    for item in output:
        if item.get("type") == "message":
            for content in item.get("content", []):
                if content.get("type") == "output_text":
                    return content.get("text", "")
    return ""


def build_front_matter(title, subtitle, description, tags, date_str, further_reading):
    seo_title = f"{title} | Dzmitryi Kharlanau"
    lines = [
        "---",
        "layout: blog",
        f'title: "{title}"',
        f'seo_title: "{seo_title}"',
        f'description: "{description}"',
        f'subtitle: "{subtitle}"',
        f"date: {date_str}",
        f"updated: {date_str}",
        "eyebrow: Dataset Brief",
        "category: Dataset Brief",
        "tags:",
    ]
    for tag in tags:
        lines.append(f"  - {tag}")
    lines.append(f'summary: "{description}"')
    if further_reading:
        lines.append("further_reading:")
        for item in further_reading:
            lines.append(f'  - label: "{item["label"]}"')
            lines.append(f'    url: "{item["url"]}"')
    lines.append("---")
    return "\n".join(lines)


def write_blog_post(output_path, front_matter, body_markdown):
    content = f"{front_matter}\n\n{body_markdown.strip()}\n"
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(content)


def main():
    parser = argparse.ArgumentParser(description="Generate an entity blog post from dataset JSON.")
    parser.add_argument("--entity", required=True, help="Dataset entity name, e.g. ams or DAMA.")
    parser.add_argument("--output", help="Output markdown path. Defaults to _blog/<entity>-dataset-overview.md")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="OpenAI model name.")
    parser.add_argument("--max-items", type=int, default=DEFAULT_MAX_ITEMS, help="Max dataset entries to include.")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help="OpenAI Responses API URL.")
    parser.add_argument("--dry-run", action="store_true", help="Build prompt and print stats without calling API.")
    args = parser.parse_args()

    entity = args.entity
    dataset_dir = os.path.join("datasets", entity)
    if not os.path.isdir(dataset_dir):
        raise SystemExit(f"Dataset directory not found: {dataset_dir}")

    entity_slug = entity.lower()
    output_path = args.output or os.path.join("_blog", f"{entity_slug}-dataset-overview.md")
    dataset_index_url = f"/datasets/{entity}/"
    dataset_manifest_url = "/datasets/manifest.json"

    dataset_context = build_dataset_context(entity, dataset_dir, args.max_items)

    prompt = build_prompt(entity, dataset_index_url, dataset_manifest_url, dataset_context)
    if args.dry_run:
        print(prompt)
        print("\n---\nEntries:", dataset_context["entry_count"])
        return

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY is not set. Aborting.")

    try:
        response = call_openai(prompt, args.model, api_key, args.base_url)
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="ignore")
        raise SystemExit(f"OpenAI API error: {exc.code} {exc.reason}\n{detail}") from exc

    output_text = extract_output_text(response)
    if not output_text:
        raise SystemExit("No output_text found in OpenAI response.")

    payload = json.loads(output_text)
    date_str = dt.date.today().isoformat()
    front_matter = build_front_matter(
        title=payload["title"],
        subtitle=payload["subtitle"],
        description=payload["meta_description"],
        tags=payload["tags"],
        date_str=date_str,
        further_reading=[
            {"label": f"{entity} dataset index", "url": dataset_index_url},
            {"label": "Dataset manifest", "url": dataset_manifest_url},
        ],
    )
    write_blog_post(output_path, front_matter, payload["body_markdown"])
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
