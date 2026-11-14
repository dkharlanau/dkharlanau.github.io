"""Project explicit, visible Atlas sections into the existing retrieval exports."""

from hashlib import sha256
from html.parser import HTMLParser
import json
import re
from urllib.parse import urlsplit


TASK_PARTS = ("task", "conditions", "method", "example", "check", "limits")
ANCHOR = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def content_digest(value):
    return sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


class CitationSections(HTMLParser):
    def __init__(self, anchors, task_anchors):
        super().__init__(convert_charrefs=True)
        self.anchors = set(anchors)
        self.task_anchors = set(task_anchors)
        self.sections = {}
        self.active = None
        self.element = None
        self.chunks = []
        self.part = None
        self.passage = None
        self.ids = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        anchor = attrs.get("id")
        if anchor:
            self.ids[anchor] = self.ids.get(anchor, 0) + 1
        hidden = "hidden" in attrs or attrs.get("aria-hidden") == "true"
        if self.active is None:
            if anchor not in self.anchors:
                return
            if tag != "section" or hidden or anchor in self.sections:
                raise ValueError(f"Expected one visible section with ID {anchor}")
            self.active = {"anchor": anchor, "heading": "", "paragraphs": [], "sources": []}
            if anchor in self.task_anchors:
                self.active["task_parts"] = {part: [] for part in TASK_PARTS}
            self.sections[anchor] = self.active
            return
        if tag in {"section", "script", "style", "template", "details"} or hidden:
            raise ValueError(f"Unsupported or hidden content in #{self.active['anchor']}")
        if tag in {"h2", "p", "li"}:
            if self.element is not None:
                raise ValueError(f"Nested citation text in #{self.active['anchor']}")
            self.element = tag
            self.chunks = []
            self.part = attrs.get("data-atlas-task-part")
            if self.part and (tag == "h2" or self.part not in self.active.get("task_parts", {})):
                raise ValueError(f"Unexpected task part {self.part} in #{self.active['anchor']}")
            if "data-atlas-cite" in attrs:
                if tag == "h2" or not anchor or not ANCHOR.fullmatch(anchor):
                    raise ValueError(f"Expected a stable passage ID in #{self.active['anchor']}")
                self.passage = {"anchor": anchor, "sources": []}
        if tag == "a" and self.element and attrs.get("href"):
            href = attrs["href"]
            parts = urlsplit(href)
            if parts.scheme == "https" and parts.hostname and not (parts.username or parts.password):
                if href not in self.active["sources"]:
                    self.active["sources"].append(href)
                if self.passage is not None and href not in self.passage["sources"]:
                    self.passage["sources"].append(href)

    def handle_data(self, data):
        if self.active is not None and self.element is not None:
            if "{%" in data or "{{" in data:
                raise ValueError(f"Template expressions are unsupported in #{self.active['anchor']}")
            self.chunks.append(data)

    def handle_endtag(self, tag):
        if self.active is None:
            return
        if tag == self.element:
            text = " ".join("".join(self.chunks).split())
            if tag == "h2":
                if self.active["heading"]:
                    raise ValueError(f"Multiple headings in #{self.active['anchor']}")
                self.active["heading"] = text
            elif text:
                self.active["paragraphs"].append(text)
                if self.part:
                    self.active["task_parts"][self.part].append(text)
            if self.passage is not None:
                if not text:
                    raise ValueError(f"Empty citation passage #{self.passage['anchor']}")
                self.active.setdefault("passages", []).append({
                    **self.passage, "text": text, "part": self.part,
                })
                self.passage = None
            self.element = None
            self.part = None
        if tag == "section":
            if self.element is not None:
                raise ValueError(f"Unclosed citation text in #{self.active['anchor']}")
            self.active = None


def read_atlas_citation_sections(body, anchors, canonical, *, task_anchors=None):
    if anchors is None and task_anchors is None:
        return []
    if not isinstance(anchors, list) or any(
        not isinstance(anchor, str) or not ANCHOR.fullmatch(anchor)
        for anchor in anchors
    ) or len(set(anchors)) != len(anchors):
        raise ValueError(f"{canonical}: invalid or duplicate citation section IDs")
    if task_anchors is not None and (
        not isinstance(task_anchors, list)
        or any(not isinstance(anchor, str) or anchor not in anchors for anchor in task_anchors)
        or len(set(task_anchors)) != len(task_anchors)
    ):
        raise ValueError(f"{canonical}: task packs must select distinct declared citation sections")
    parser = CitationSections(anchors, task_anchors or [])
    parser.feed(body)
    parser.close()
    if parser.active is not None:
        raise ValueError(f"{canonical}: unclosed citation section")
    sections = []
    for anchor in anchors:
        match = parser.sections.get(anchor)
        if not match or not all(match[key] for key in ("heading", "paragraphs", "sources")):
            raise ValueError(f"{canonical}#{anchor}: heading, visible text and an HTTPS source are required")
        record = {"section_url": f"{canonical}#{anchor}", **{k: match[k] for k in ("heading", "paragraphs", "sources")}}
        parts = match.get("task_parts")
        pack = None
        if parts is not None:
            if any(not values for values in parts.values()) or len(parts["task"]) != 1:
                raise ValueError(f"{canonical}#{anchor}: task pack needs one task and all six parts")
            pack = {
                "schema": "atlas.read_only_task.v1",
                "canonical": record["section_url"],
                **{name: values[0] if name == "task" else values for name, values in parts.items()},
                "sources": record["sources"],
            }
        if match.get("passages"):
            passages = []
            for passage in match["passages"]:
                passage_anchor = passage["anchor"]
                if parser.ids[passage_anchor] != 1:
                    raise ValueError(f"{canonical}#{passage_anchor}: duplicate citation passage ID")
                row = {
                    "url": f"{canonical}#{passage_anchor}",
                    "text": passage["text"],
                    "sources": passage["sources"],
                }
                if passage["part"] is not None:
                    row["part"] = passage["part"]
                if pack is not None and passage["part"] in {"method", "example", "check"}:
                    row["context"] = {
                        "section_url": record["section_url"],
                        "conditions": parts["conditions"],
                        "limits": parts["limits"],
                    }
                passages.append({**row, "sha256": content_digest(row)})
            record["passages"] = passages
        if pack is not None:
            record["task_pack"] = {**pack, "version": content_digest(pack)}
        record["sha256"] = sha256(json.dumps(record, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()
        sections.append(record)
    return sections
