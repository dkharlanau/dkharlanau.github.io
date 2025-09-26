#!/usr/bin/env python3
"""LinkedIn CSV to resume exporter.

Parses LinkedIn archive CSVs and produces YAML + JSON resume outputs.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import OrderedDict
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
from urllib.parse import urlparse, urlunparse
import re

# ----------------------------- Text helpers -----------------------------

SMART_CHAR_MAP = {
    "\u2018": "'",
    "\u2019": "'",
    "\u201c": '"',
    "\u201d": '"',
    "\u2014": " - ",
    "\u2013": "-",
    "\xa0": " ",
    "\u2022": "- ",
    "\u2023": "- ",
    "\u25cf": "- ",
    "\u25a0": "- ",
}

BULLET_PATTERN = re.compile(r"^[\-\*\u2022\u2023\u25cf\u25a0]+\s*")
WHITESPACE_RE = re.compile(r"\s+")


def clean_text(value: Optional[str]) -> str:
    """Normalise whitespace, replace smart characters, and strip noise."""
    if not value:
        return ""
    text = str(value)
    for bad, good in SMART_CHAR_MAP.items():
        text = text.replace(bad, good)
    text = text.replace("\ufeff", "")
    text = text.replace("\ufffd", "")
    text = WHITESPACE_RE.sub(" ", text)
    text = text.strip()
    text = text.encode("ascii", "ignore").decode("ascii")
    return text


def split_highlights(blob: str, limit: int = 6) -> Tuple[str, List[str]]:
    """Split a descriptive blob into summary + highlight bullets."""
    if not blob:
        return "", []
    summaries: List[str] = []
    for raw_line in re.split(r"[\r\n]+", blob):
        line = clean_text(raw_line)
        if not line:
            continue
        line = BULLET_PATTERN.sub("", line)
        if not line:
            continue
        pieces = [p.strip() for p in re.split(r";", line) if p.strip()]
        summaries.extend(pieces)
    if not summaries:
        return "", []
    seen = OrderedDict()
    for item in summaries:
        if item not in seen:
            seen[item] = None
    ordered = list(seen.keys())
    if len(ordered) == 1:
        return ordered[0], []
    return ordered[0], ordered[1: limit + 1]


# ----------------------------- Date helpers -----------------------------

DATE_FORMATS = (
    "%Y-%m-%d",
    "%Y/%m/%d",
    "%Y.%m.%d",
    "%d-%m-%Y",
    "%B %d, %Y",
    "%b %d, %Y",
    "%B %Y",
    "%b %Y",
    "%m/%d/%Y",
    "%Y-%m",
    "%Y/%m",
)
MONTH_MAP = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "sept": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
}


def parse_date(raw: str) -> Optional[date]:
    if not raw:
        return None
    value = clean_text(raw)
    if not value:
        return None
    lowered = value.lower()
    if lowered in {"present", "current", "now", "ongoing"}:
        return None
    if re.fullmatch(r"\d{4}", value):
        return date(int(value), 1, 1)
    m = re.fullmatch(r"([a-zA-Z]+)\s+(\d{4})", value)
    if m:
        month = MONTH_MAP.get(m.group(1).lower()[:3])
        if month:
            return date(int(m.group(2)), month, 1)
    m = re.fullmatch(r"(\d{4})\s+([a-zA-Z]+)", value)
    if m:
        month = MONTH_MAP.get(m.group(2).lower()[:3])
        if month:
            return date(int(m.group(1)), month, 1)
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    if re.fullmatch(r"\d{8}", value):
        try:
            return datetime.strptime(value, "%Y%m%d").date()
        except ValueError:
            pass
    return None


def format_date(value: Optional[date]) -> Optional[str]:
    if not value:
        return None
    if value.day != 1:
        return value.strftime("%Y-%m-%d")
    if value.month != 1:
        return value.strftime("%Y-%m")
    return value.strftime("%Y")


# ----------------------------- CSV helpers -----------------------------

@dataclass
class CsvRows:
    filename: str
    rows: List[Dict[str, str]]


def load_csv(base_dir: Path, filename: str) -> CsvRows:
    path = base_dir / filename
    if not path.exists():
        print(f"Missing {filename}, skipping.")
        return CsvRows(filename, [])
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        normalised_rows: List[Dict[str, str]] = []
        for raw_row in reader:
            normalised: Dict[str, str] = {}
            for key, value in raw_row.items():
                if key is None:
                    continue
                norm_key = key.strip().lower()
                norm_val = clean_text(value)
                normalised[norm_key] = norm_val
            if any(value for value in normalised.values()):
                normalised_rows.append(normalised)
    print(f"Loaded {filename}: {len(normalised_rows)} rows")
    return CsvRows(filename, normalised_rows)


def pick(row: Dict[str, str], aliases: Sequence[str]) -> str:
    for key in aliases:
        if key in row and row[key]:
            return row[key]
    return ""


# ----------------------------- Link helpers -----------------------------

KNOWN_LABELS = {
    "linkedin.com": "LinkedIn",
    "www.linkedin.com": "LinkedIn",
    "github.com": "GitHub",
    "www.github.com": "GitHub",
    "twitter.com": "Twitter",
    "www.twitter.com": "Twitter",
    "x.com": "X",
    "www.x.com": "X",
    "medium.com": "Medium",
    "hashnode.com": "Hashnode",
    "www.hashnode.com": "Hashnode",
    "reddit.com": "Reddit",
    "www.reddit.com": "Reddit",
    "youtube.com": "YouTube",
    "www.youtube.com": "YouTube",
}


def normalise_url(raw: str) -> Optional[str]:
    if not raw:
        return None
    value = raw.strip()
    if not value:
        return None
    if value.startswith("mailto:"):
        return value.lower()
    parsed = urlparse(value if re.match(r"^[a-z]+://", value, re.I) else f"https://{value}")
    if not parsed.netloc:
        return None
    scheme = (parsed.scheme or "https").lower()
    netloc = parsed.netloc.lower()
    if netloc.endswith(":80"):
        netloc = netloc[:-3]
    path = parsed.path.rstrip("/")
    query = parsed.query
    normalised = urlunparse((scheme, netloc, path, "", query, ""))
    if not path and not query:
        normalised = normalised.rstrip("/")
    return normalised


@dataclass
class Link:
    label: str
    url: str


def label_for(url: str, fallback: Optional[str] = None) -> str:
    host = urlparse(url).netloc
    return KNOWN_LABELS.get(host, fallback or host)


# ----------------------------- Resume builder -----------------------------

class ResumeBuilder:
    def __init__(self, input_dir: Path, output_root: Path) -> None:
        self.input_dir = input_dir
        self.output_root = output_root
        self.summary_text: str = ""
        self.profile_links: List[Link] = []
        self.links_added = 0
        self.links_deduped = 0

    def load_profile(self) -> None:
        profile = load_csv(self.input_dir, "Profile.csv")
        if not profile.rows:
            return
        primary = profile.rows[0]
        self.summary_text = pick(primary, ["summary", "about", "description"])
        website_blob = pick(primary, ["websites", "website", "urls"])
        twitter_blob = pick(primary, ["twitter handles", "twitter", "x"])
        if website_blob:
            for chunk in self._split_link_blob(website_blob):
                self.profile_links.append(Link(label="Website", url=chunk))
        if twitter_blob:
            for chunk in self._split_link_blob(twitter_blob):
                self.profile_links.append(Link(label="Twitter", url=chunk))

    def _split_link_blob(self, blob: str) -> List[str]:
        parts = re.split(r"[\n\r,;|]", blob)
        return [clean_text(part) for part in parts if clean_text(part)]

    def load_positions(self) -> List[Dict[str, object]]:
        csv_rows = load_csv(self.input_dir, "Positions.csv")
        experiences: List[Dict[str, object]] = []
        for row in csv_rows.rows:
            title = pick(row, ["title", "position", "role"])
            company = pick(row, ["company name", "company", "organization"])
            if not (title and company):
                continue
            start_raw = pick(row, ["started on", "start date", "from", "date started"])
            end_raw = pick(row, ["finished on", "end date", "to", "date finished"])
            start_date = parse_date(start_raw)
            end_date = parse_date(end_raw)
            flag = pick(row, ["is current", "current", "ongoing"]).lower()
            current = flag in {"true", "yes", "1"}
            if not end_date and clean_text(end_raw).lower() in {"present", "current"}:
                current = True
            summary_blob = pick(row, ["description", "summary", "notes"])
            summary, highlights = split_highlights(summary_blob)
            location = pick(row, ["location", "city", "region"])
            entry: Dict[str, object] = {
                "company": company,
                "title": title,
                "location": location or None,
                "start": format_date(start_date),
                "end": None if current else format_date(end_date),
                "current": current,
            }
            if summary:
                entry["summary"] = summary
            if highlights:
                entry["highlights"] = highlights
            experiences.append(entry)
        experiences.sort(key=lambda item: (item.get("start") or "0000", item.get("end") or "9999"), reverse=True)
        return experiences[:20]

    def load_education(self) -> List[Dict[str, object]]:
        csv_rows = load_csv(self.input_dir, "Education.csv")
        education: List[Dict[str, object]] = []
        for row in csv_rows.rows:
            school = pick(row, ["school name", "institution", "university"])
            if not school:
                continue
            degree = pick(row, ["degree name", "degree", "qualification"])
            field = pick(row, ["field of study", "field"])
            start_date = parse_date(pick(row, ["start date", "started on", "from"]))
            end_raw = pick(row, ["end date", "finished on", "to"])
            end_date = parse_date(end_raw)
            entry = {
                "school": school,
                "degree": degree or None,
                "field": field or None,
                "start": format_date(start_date),
                "end": format_date(end_date),
            }
            notes = pick(row, ["notes", "activities"])
            if notes:
                entry["notes"] = notes
            education.append(entry)
        education.sort(key=lambda item: (item.get("end") or "9999", item.get("start") or "0000"), reverse=True)
        return education[:10]

    def load_skills(self) -> List[str]:
        csv_rows = load_csv(self.input_dir, "Skills.csv")
        seen: OrderedDict[str, None] = OrderedDict()
        for row in csv_rows.rows:
            name = pick(row, ["name", "skill", "title"])
            if not name:
                continue
            if name not in seen:
                seen[name] = None
        return list(seen.keys())[:30]

    def load_certifications(self) -> List[Dict[str, object]]:
        csv_rows = load_csv(self.input_dir, "Certifications.csv")
        certs: List[Dict[str, object]] = []
        for row in csv_rows.rows:
            name = pick(row, ["name", "certification", "title"])
            authority = pick(row, ["authority", "issuer"])
            if not name:
                continue
            entry = {
                "name": name,
                "issuer": authority or None,
                "issued": format_date(parse_date(pick(row, ["started on", "issue date", "date"]))),
            }
            url = normalise_url(pick(row, ["url", "link"]))
            if url:
                entry["url"] = url
            certs.append(entry)
        certs.sort(key=lambda item: item.get("issued") or "0000", reverse=True)
        return certs[:15]

    def load_projects(self) -> List[Dict[str, object]]:
        csv_rows = load_csv(self.input_dir, "Projects.csv")
        projects: List[Dict[str, object]] = []
        for row in csv_rows.rows:
            title = pick(row, ["title", "name"])
            if not title:
                continue
            description_blob = pick(row, ["description", "summary"])
            summary, highlights = split_highlights(description_blob, limit=4)
            entry = {
                "title": title,
                "summary": summary or None,
                "start": format_date(parse_date(pick(row, ["started on", "start date"]))),
                "end": format_date(parse_date(pick(row, ["finished on", "end date"]))),
            }
            if highlights:
                entry["highlights"] = highlights
            url = normalise_url(pick(row, ["url", "link"]))
            if url:
                entry["url"] = url
            projects.append(entry)
        projects.sort(key=lambda item: (item.get("start") or "0000", item.get("end") or "9999"), reverse=True)
        return projects[:10]

    def load_languages(self) -> List[Dict[str, Optional[str]]]:
        csv_rows = load_csv(self.input_dir, "Languages.csv")
        languages: List[Dict[str, Optional[str]]] = []
        for row in csv_rows.rows:
            name = pick(row, ["name", "language"])
            if not name:
                continue
            proficiency = pick(row, ["proficiency", "level"])
            languages.append({"name": name, "proficiency": proficiency or None})
        return languages

    def merge_links(self, cli_links: List[Link], website_links: Iterable[Link]) -> List[Dict[str, str]]:
        combined = cli_links + list(website_links)
        normalised: OrderedDict[str, Link] = OrderedDict()
        for link in combined:
            normalised_url = normalise_url(link.url)
            if not normalised_url:
                continue
            label = link.label or label_for(normalised_url)
            if normalised_url not in normalised:
                normalised[normalised_url] = Link(label=label_for(normalised_url, fallback=label), url=normalised_url)
            else:
                self.links_deduped += 1
        self.links_added = len(normalised)
        return [{"label": item.label, "url": item.url} for item in normalised.values()]

    def build(self, args: SimpleNamespace) -> Dict[str, object]:
        self.load_profile()
        experience = self.load_positions()
        if not experience:
            print("Error: no positions found.", file=sys.stderr)
            sys.exit(1)
        education = self.load_education()
        skills = self.load_skills()
        certifications = self.load_certifications()
        projects = self.load_projects()
        languages = self.load_languages()

        cli_links: List[Link] = []
        cli_links.append(Link("Website", args.site))
        if getattr(args, "email", None):
            cli_links.append(Link("Email", f"mailto:{args.email}"))
        if args.linkedin:
            cli_links.append(Link("LinkedIn", args.linkedin))
        if args.github:
            cli_links.append(Link("GitHub", args.github))
        if args.twitter:
            cli_links.append(Link("Twitter", args.twitter))
        if args.location_link:
            cli_links.append(Link("Location", args.location_link))
        if args.link:
            for pair in args.link:
                if "=" in pair:
                    label, url = pair.split("=", 1)
                    cli_links.append(Link(clean_text(label), url.strip()))
                else:
                    cli_links.append(Link("Link", pair.strip()))

        all_links = self.merge_links(cli_links, self.profile_links)

        contact = {
            "site": normalise_url(args.site) or args.site,
        }
        if getattr(args, "email", None):
            contact["email"] = args.email
        if args.linkedin:
            contact["linkedin"] = normalise_url(args.linkedin)
        if args.github:
            contact["github"] = normalise_url(args.github)
        if args.twitter:
            contact["twitter"] = normalise_url(args.twitter)

        resume: Dict[str, object] = OrderedDict()
        resume["name"] = args.name
        resume["headline"] = args.headline
        if args.location:
            resume["location"] = args.location
        if self.summary_text:
            resume["summary"] = self.summary_text
        resume["contact"] = contact
        resume["links"] = all_links
        resume["experience"] = experience
        if education:
            resume["education"] = education
        if skills:
            resume["skills"] = skills
        if certifications:
            resume["certifications"] = certifications
        if projects:
            resume["projects"] = projects
        if languages:
            resume["languages"] = languages

        self.write_outputs(resume)

        print(
            "Summary: "
            f"experience={len(experience)}, "
            f"education={len(education)}, "
            f"skills={len(skills)}, "
            f"certifications={len(certifications)}, "
            f"projects={len(projects)}, "
            f"languages={len(languages)}, "
            f"links={self.links_added} (deduped {self.links_deduped})"
        )
        return resume

    def write_outputs(self, resume: Dict[str, object]) -> None:
        data_dir = self.output_root / "_data"
        ai_dir = self.output_root / "ai"
        data_dir.mkdir(parents=True, exist_ok=True)
        ai_dir.mkdir(parents=True, exist_ok=True)
        yaml_path = data_dir / "resume.yml"
        json_path = ai_dir / "resume.json"
        yaml_content = dump_yaml(resume)
        yaml_path.write_text(yaml_content + "\n", encoding="utf-8")
        json_path.write_text(json.dumps(resume, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {yaml_path.relative_to(self.output_root)}")
        print(f"Wrote {json_path.relative_to(self.output_root)}")


# ----------------------------- YAML helper -----------------------------

def dump_yaml(data: object, indent: int = 0) -> str:
    """Simple YAML serializer (fallback when PyYAML is unavailable)."""
    try:
        import yaml  # type: ignore

        return yaml.safe_dump(data, sort_keys=False, allow_unicode=False)
    except Exception:
        pass

    def emit(value: object, level: int) -> List[str]:
        prefix = "  " * level
        if isinstance(value, dict):
            if not value:
                return [f"{prefix}{{}}"]
            lines: List[str] = []
            for key, item in value.items():
                if item is None:
                    continue
                if isinstance(item, (dict, list)):
                    lines.append(f"{prefix}{key}:")
                    lines.extend(emit(item, level + 1))
                else:
                    lines.append(f"{prefix}{key}: {format_scalar(item)}")
            return lines
        if isinstance(value, list):
            if not value:
                return [f"{prefix}[]"]
            lines = []
            for item in value:
                if isinstance(item, (dict, list)):
                    lines.append(f"{prefix}-")
                    lines.extend(emit(item, level + 1))
                else:
                    lines.append(f"{prefix}- {format_scalar(item)}")
            return lines
        return [f"{prefix}{format_scalar(value)}"]

    return "\n".join(emit(data, indent))


def format_scalar(value: object) -> str:
    if value is None:
        return """"""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if text == "":
        return "''"
    needs_quote = bool(re.search(r"[:#\-?&*!%{}\[\],>|'\"@`\\]", text) or text.strip() != text or "\n" in text)
    if not needs_quote:
        return text
    escaped = text.replace("\\", "\\\\").replace("\"", "\\\"").replace("\n", "\\n")
    return f'"{escaped}"'


# ----------------------------- Config helpers -----------------------------

DEFAULT_CONFIG_CANDIDATES = [
    Path(__file__).with_name("li2resume.config.json"),
    Path(__file__).with_name("li2resume.config.yml"),
    Path(__file__).with_name("li2resume.config.yaml"),
]


def load_config_data(config_arg: Optional[str]) -> Tuple[Dict[str, Any], Optional[Path]]:
    candidates: List[Path] = []
    if config_arg:
        candidates.append(Path(config_arg).expanduser())
    else:
        candidates.extend(DEFAULT_CONFIG_CANDIDATES)
    for candidate in candidates:
        if candidate.exists():
            try:
                return parse_config_file(candidate), candidate
            except Exception as exc:
                print(f"Error reading config {candidate}: {exc}", file=sys.stderr)
                sys.exit(1)
    return {}, None


def parse_config_file(path: Path) -> Dict[str, Any]:
    text = path.read_text(encoding="utf-8-sig")
    suffix = path.suffix.lower()
    if suffix == ".json":
        data = json.loads(text or "{}")
    elif suffix in {".yml", ".yaml"}:
        try:
            import yaml  # type: ignore
        except ImportError as exc:
            raise RuntimeError("PyYAML is required to parse YAML config files. Install it or use JSON.") from exc
        data = yaml.safe_load(text) or {}
    else:
        data = json.loads(text or "{}")
    if not isinstance(data, dict):
        raise ValueError("Config root must be an object/mapping.")
    return data


def coalesce_args(args: argparse.Namespace, config: Dict[str, Any]) -> Dict[str, Any]:
    merged: Dict[str, Any] = {}
    fields = [
        "input",
        "name",
        "email",
        "site",
        "headline",
        "location",
        "location_link",
        "linkedin",
        "github",
        "twitter",
    ]
    for field in fields:
        value = getattr(args, field, None)
        if value is None or (isinstance(value, str) and value.strip() == ""):
            value = config.get(field)
        merged[field] = value
    if not merged.get("input"):
        merged["input"] = "./Complete_LinkedIn"
    link_args: List[str] = []
    config_links = config.get("links")
    if isinstance(config_links, list):
        for entry in config_links:
            if isinstance(entry, str):
                link_args.append(entry)
            elif isinstance(entry, dict):
                label = clean_text(str(entry.get("label") or entry.get("name") or "Link"))
                url = entry.get("url") or entry.get("href")
                if url:
                    link_args.append(f"{label}={url}")
    if args.link:
        link_args.extend(args.link)
    merged["link"] = link_args
    return merged


# ----------------------------- CLI -----------------------------

def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert LinkedIn CSV archive to resume outputs.")
    parser.add_argument("--config", help="Optional path to a config file (JSON or YAML).")
    parser.add_argument("--input", help="Path to LinkedIn CSV directory")
    parser.add_argument("--name", help="Full name for the resume")
    parser.add_argument("--email", help="Primary email address")
    parser.add_argument("--site", help="Primary personal site URL")
    parser.add_argument("--headline", help="Resume headline")
    parser.add_argument("--location", help="Location string")
    parser.add_argument("--location-link", help="Optional location link for links list")
    parser.add_argument("--linkedin", help="LinkedIn profile URL")
    parser.add_argument("--github", help="GitHub profile URL")
    parser.add_argument("--twitter", help="Twitter/X profile URL")
    parser.add_argument("--link", action="append", help="Additional links (LABEL=URL)")
    return parser.parse_args(argv)


def resolve_input(path_str: str) -> Path:
    path = Path(path_str).expanduser()
    if path.exists():
        return path
    alt = path.parent / "Complete_LinkedIn"
    if alt.exists():
        print(f"Input '{path}' not found; using '{alt}' instead.")
        return alt
    print(f"Error: input directory '{path}' not found.", file=sys.stderr)
    sys.exit(1)


def main(argv: Optional[Sequence[str]] = None) -> Dict[str, object]:
    args = parse_args(argv)
    config_data, config_path = load_config_data(getattr(args, "config", None))
    merged = coalesce_args(args, config_data)
    required = ["input", "name", "site", "headline"]
    missing = [field for field in required if not merged.get(field)]
    if missing:
        hint = f" (config: {config_path})" if config_path else ""
        print(f"Missing required fields{hint}: {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)
    input_dir = resolve_input(str(merged.pop("input")))
    output_root = Path.cwd()
    namespace = SimpleNamespace(**merged)
    builder = ResumeBuilder(input_dir=input_dir, output_root=output_root)
    return builder.build(namespace)


if __name__ == "__main__":
    main()

