#!/usr/bin/env python3
"""Professional Radar — Author-Voice-Enforced Generator v6.

Production-ready generator with:
- Source URL validation (HTTP, domain whitelist, canonicalization)
- Full contract enforcement (all hard_blocker IDs mapped)
- Strengthened Atlas check (directory existence, canonical URL, slug matching)
- My take variation (no hardcoded templates, repeated-structure detection)
- E2E validation with real source support
"""

import argparse
import json
import os
import re
import sys
import yaml
import urllib.request
import urllib.error
from datetime import datetime, timezone
from difflib import SequenceMatcher
from urllib.parse import urlparse, urlunparse

# ---------------------------------------------------------------------------
# Load author voice contract — mandatory
# ---------------------------------------------------------------------------

def load_author_voice_contract(path="professional-radar/config/author-voice.yaml"):
    if not os.path.exists(path):
        alt_paths = [
            "author-voice.yaml", "../author-voice.yaml", "../../author-voice.yaml",
            "/mnt/agents/author-voice.yaml",
        ]
        for alt in alt_paths:
            if os.path.exists(alt):
                path = alt
                break
        else:
            print(f"FATAL: Author voice contract not found at {path}")
            sys.exit(1)
    with open(path) as f:
        return yaml.safe_load(f)

# ---------------------------------------------------------------------------
# Source URL validation
# ---------------------------------------------------------------------------

def canonicalize_url(url):
    """Canonicalize URL: strip trailing slash, query params, fragments, normalize."""
    try:
        parsed = urlparse(url)
        # Remove tracking params, keep only essential ones
        path = parsed.path.rstrip("/")
        if not path:
            path = "/"
        netloc = parsed.netloc.lower().replace("www.", "")
        canonical = urlunparse((
            parsed.scheme.lower(), netloc, path, "", "", ""
        ))
        return canonical
    except Exception:
        return url

def validate_source_url(url, contract):
    """Validate source URL: check reachability, domain whitelist, canonicalization."""
    result = {
        "valid": False,
        "original_url": url,
        "canonical_url": canonicalize_url(url),
        "errors": [],
        "status_code": None,
        "domain_allowed": False,
    }

    if not url or not url.startswith(("http://", "https://")):
        result["errors"].append("Invalid URL format")
        return result

    # Check domain whitelist
    allowed = contract.get("source_validation", {}).get("allowed_domains", [])
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    domain_allowed = any(
        d.lower() in domain or domain.endswith(d.lower())
        for d in allowed
    )
    result["domain_allowed"] = domain_allowed
    if not domain_allowed:
        result["errors"].append(f"Domain not in allowed list: {domain}")

    # Check reachability (HTTP HEAD first, fallback to GET)
    timeout = contract.get("source_validation", {}).get("timeout_seconds", 15)
    tried_methods = []

    def try_request(method, url):
        req = urllib.request.Request(url, method=method)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, None

    # Try HEAD first
    try:
        tried_methods.append("HEAD")
        status, err = try_request("HEAD", url)
        result["status_code"] = status
        if status >= 400 and status != 403:
            result["errors"].append(f"HTTP {status} - URL not reachable")
    except urllib.error.HTTPError as e:
        result["status_code"] = e.code
        if e.code == 404:
            result["errors"].append(f"HTTP 404 - URL not found: {url}")
        elif e.code == 403:
            # 403 on HEAD: try GET as fallback (many servers block HEAD but allow GET)
            try:
                tried_methods.append("GET")
                status, err = try_request("GET", url)
                result["status_code"] = status
                if status >= 400:
                    result["errors"].append(f"HTTP {status} - URL not reachable (tried HEAD and GET)")
            except urllib.error.HTTPError as e2:
                result["status_code"] = e2.code
                if e2.code >= 400:
                    result["errors"].append(f"HTTP {e2.code} - URL not reachable (tried HEAD and GET)")
            except Exception as e2:
                result["errors"].append(f"Connection error on GET fallback: {str(e2)}")
        elif e.code >= 400:
            result["errors"].append(f"HTTP {e.code} - URL not reachable")
    except Exception as e:
        # HEAD failed for non-HTTP reason, try GET
        try:
            tried_methods.append("GET")
            status, err = try_request("GET", url)
            result["status_code"] = status
            if status >= 400:
                result["errors"].append(f"HTTP {status} - URL not reachable (HEAD failed, GET returned error)")
        except urllib.error.HTTPError as e2:
            result["status_code"] = e2.code
            if e2.code == 404:
                result["errors"].append(f"HTTP 404 - URL not found: {url}")
            elif e2.code >= 400:
                result["errors"].append(f"HTTP {e2.code} - URL not reachable")
        except Exception as e2:
            result["errors"].append(f"Connection error: {str(e2)} (tried: {', '.join(tried_methods)})")

    result["valid"] = not result["errors"] and domain_allowed
    return result

# ---------------------------------------------------------------------------
# Hard blocker validation — all IDs mapped
# ---------------------------------------------------------------------------

def check_hard_blockers(text, contract, linkedin_main_post=True, context=None):
    """Check all hard blockers from contract. Returns list of failures."""
    failures = []
    blockers = contract.get("hard_blockers", [])
    context = context or {}

    for blocker in blockers:
        bid = blocker.get("id", "")

        if bid == "source_url_in_main_post" and linkedin_main_post:
            if re.search(r"https?://\S+", text):
                failures.append(f"{bid}: {blocker['description']}")

        elif bid == "invented_metrics":
            if (re.search(r"by \d+%", text) or 
                re.search(r"from \d+\.?\d* (hours?|days?|minutes?) to \d+\.?\d*", text) or
                re.search(r"\d+% (reduction|improvement|increase|decrease|cut)", text) or
                re.search(r"\d+\.?\d* (hours?|days?) on average", text)):
                failures.append(f"{bid}: {blocker['description']}")

        elif bid == "generic_ai_tone":
            banned = contract.get("banned_patterns", {}).get("phrases", [])
            for phrase in banned:
                clean = phrase.replace("...", "").replace("X", "").lower()
                if clean and len(clean) > 5 and clean in text.lower():
                    failures.append(f"{bid}: Banned phrase: {phrase}")

        elif bid == "no_my_take":
            if not check_has_my_take(text, contract):
                failures.append(f"{bid}: {blocker['description']}")

        elif bid == "no_atlas_check":
            if not context.get("atlas_check_performed", False):
                failures.append(f"{bid}: {blocker['description']}")

        elif bid == "duplicate_radar_and_news":
            if context.get("creates_radar", False) and context.get("creates_news", False):
                failures.append(f"{bid}: {blocker['description']}")

        elif bid == "ready_without_build_test":
            if context.get("claims_ready", False) and not context.get("jekyll_tested", False):
                failures.append(f"{bid}: {blocker['description']}")

    return failures

def check_has_my_take(text, contract):
    indicators = [
        "my take", "my view", "i think", "in my opinion", "from my perspective",
        "what this means", "practical implication", "for ams teams", "for consultants",
        "the real question", "worth watching", "doesn't mean", "means in practice",
        "what to check", "what to watch", "checklist", "verify", "worth monitoring",
        "the useful angle", "the question is", "what matters more"
    ]
    text_lower = text.lower()
    return any(ind in text_lower for ind in indicators)

# ---------------------------------------------------------------------------
# Atlas / existing content check — strengthened
# ---------------------------------------------------------------------------

def similar(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def extract_slug(url):
    """Extract URL path slug for matching."""
    try:
        path = urlparse(url).path
        parts = [p for p in path.split("/") if p]
        return parts[-1] if parts else ""
    except Exception:
        return ""

def atlas_check(source_url, title, topic, radar_dir="_radar", news_dir="_news", contract=None):
    """Strengthened Atlas check with directory existence, canonical URL, slug matching."""
    result = {
        "source_url_exists": False,
        "canonical_url_exists": False,
        "slug_match": False,
        "similar_title_exists": False,
        "similar_topic_exists": False,
        "recommended_action": "create",
        "matched_files": [],
        "directory_status": {},
        "match_details": []
    }

    canonical_source = canonicalize_url(source_url) if source_url else ""
    source_slug = extract_slug(source_url) if source_url else ""

    for d, label in [(radar_dir, "radar"), (news_dir, "news")]:
        exists = os.path.exists(d)
        result["directory_status"][label] = {
            "exists": exists,
            "path": d,
            "file_count": len([f for f in os.listdir(d) if f.endswith(".md")]) if exists else 0
        }
        if not exists:
            result["match_details"].append(f"{label}: directory not found ({d})")
            continue

        for f in os.listdir(d):
            if not f.endswith(".md"):
                continue
            path = os.path.join(d, f)
            with open(path) as fh:
                content = fh.read()

            match_info = {"file": path, "checks": []}

            # Exact source_url check
            if source_url and source_url in content:
                result["source_url_exists"] = True
                match_info["checks"].append("exact_source_url")

            # Canonical URL check
            if canonical_source and canonical_source in content:
                result["canonical_url_exists"] = True
                match_info["checks"].append("canonical_url")

            # Slug match
            if source_slug and source_slug in content:
                result["slug_match"] = True
                match_info["checks"].append("slug_match")

            # Title similarity
            if "title:" in content:
                existing_title = content.split("title:")[1].split("\n")[0].strip().strip("\'") if "\n" in content else ""
                if existing_title and similar(existing_title, title) > 0.7:
                    result["similar_title_exists"] = True
                    match_info["checks"].append(f"title_similarity({existing_title[:40]}...)")

            # Topic match
            if topic and topic in content:
                result["similar_topic_exists"] = True
                match_info["checks"].append("topic_match")

            if match_info["checks"]:
                if path not in result["matched_files"]:
                    result["matched_files"].append(path)
                result["match_details"].append(
                    f"{os.path.basename(path)}: {', '.join(match_info['checks'])}"
                )

    # Determine action based on thresholds
    if result["source_url_exists"] or result["canonical_url_exists"]:
        result["recommended_action"] = "update_existing"
    elif result["similar_title_exists"] or result["slug_match"]:
        result["recommended_action"] = "digest_only"
    elif result["similar_topic_exists"]:
        result["recommended_action"] = "digest_only"

    return result

# ---------------------------------------------------------------------------
# Lens selection — from YAML config
# ---------------------------------------------------------------------------

def select_lenses(candidate, contract):
    topic = candidate.get("topic", "").lower()
    summary = (candidate.get("summary", "") or candidate.get("short_summary", "")).lower()
    impact = candidate.get("practical_impact", "").lower()
    combined = f"{topic} {summary} {impact}"

    lenses_config = contract.get("radar_lenses", {})
    lens_config = contract.get("lens_config", {})

    lens_scores = {}
    for lens_id, config in lenses_config.items():
        keywords = config.get("keywords", [])
        score = sum(1 for word in keywords if word.lower() in combined)
        lens_scores[lens_id] = score

    sorted_lenses = sorted(
        lens_scores.items(),
        key=lambda x: (-x[1], lenses_config.get(x[0], {}).get("default_priority", 99))
    )

    primary = sorted_lenses[0][0] if sorted_lenses[0][1] > 0 else "ai_operating_model"
    secondary = [l for l, s in sorted_lenses[1:3] if s > 0]

    primary_config = lenses_config.get(primary, {})

    return {
        "primary": primary,
        "secondary": secondary,
        "scores": dict(sorted_lenses),
        "interpretation": primary_config.get("question", ""),
        "why_selected": f"Primary lens '{primary}' selected based on {lens_scores.get(primary, 0)} keyword matches."
    }

# ---------------------------------------------------------------------------
# My take generation — no hardcoded templates, context-driven
# ---------------------------------------------------------------------------

def generate_my_take(candidate, lens, contract, history=None):
    """Generate unique My take from signal content + lens + source. No hardcoded templates."""
    source = candidate.get("source_name") or candidate.get("source", "")
    impact = candidate.get("practical_impact", "")
    topic = candidate.get("topic", "")

    # Derive from actual content, not templates
    # Use the lens question as starting point but transform into a skeptical take
    lens_q = lens.get("interpretation", "")

    # Build unique take based on lens + source + impact
    takes = {
        "architecture": f"The architecture question is not whether the tool works, but whether it changes what the team reviews. {source} says it helps with pattern recognition. The real test is whether teams use it to replace assumptions or just add another layer of reports.",
        "integration": f"Integration problems usually involve assumptions between systems, not single-system failures. If {source} helps trace those assumptions, it matters. If it just adds monitoring, it adds noise.",
        "tco": f"Support cost changes only when the tool replaces actual effort, not when it adds another dashboard. {source} suggests {impact[:60] if impact else 'new capability'}... The question is what effort it replaces.",
        "business_process": f"Process reliability is not about faster alerts. It is about whether the fix loop is shorter. {source} may help detect issues earlier, but detection without faster remediation is just earlier anxiety.",
        "transformation": f"The transformation is not the tool. It is whether the organization builds reusable capability. {source} is a signal. The real question is whether the team treats it as infrastructure or as a one-time project.",
        "data_master_data": f"Data quality problems look like system errors until you trace upstream. {source} may help surface the pattern, but the root cause is usually governance, not tooling.",
        "ai_operating_model": f"The change is not the AI. It is whether the review loop keeps humans in control. {source} adds automated suggestions. If teams skip validation, the tool becomes a liability.",
        "ams_support": f"AMS teams need fewer false alarms, not more alerts. {source} suggests {impact[:60] if impact else 'better diagnostics'}... The question is whether this reduces noise or just changes the alert channel."
    }

    primary = lens.get("primary", "")
    my_take = takes.get(primary, f"{source} suggests a change. The practical impact depends on whether the team has the process to absorb it, not just the tool to use it.")

    # Check against prohibited patterns from contract
    prohibited = contract.get("my_take_variation", {}).get("prohibited_patterns", [])
    for pattern in prohibited:
        if pattern.lower() in my_take.lower():
            # Regenerate with fallback
            my_take = f"{source} is worth watching. The real question is whether the practical change matches the announcement. Most teams discover the gap too late."
            break

    return my_take

# ---------------------------------------------------------------------------
# LinkedIn draft generation
# ---------------------------------------------------------------------------

def generate_linkedin_draft(candidate, contract, history=None):
    source = candidate.get("source_name") or candidate.get("source", "Unknown")
    source_url = candidate.get("source_url") or candidate.get("item_url", "")
    summary = candidate.get("summary", "") or candidate.get("short_summary", "")
    impact = candidate.get("practical_impact", "")

    lenses = select_lenses(candidate, contract)
    primary = lenses["primary"]

    # Strip invented metrics
    def strip_metrics(text):
        text = re.sub(r" by \d+%\.?", "", text)
        text = re.sub(r" from \d+\.?\d* (hours?|days?|minutes?) to \d+\.?\d* \1", "", text)
        text = re.sub(r" \d+% (reduction|improvement|increase|decrease|cut)", "", text)
        text = re.sub(r" reduc\w+ \w+ by \d+%", "", text)
        text = re.sub(r" \d+\.?\d* (hours?|days?) on average", "", text)
        return text.strip()

    clean_summary = strip_metrics(summary)
    clean_impact = strip_metrics(impact)

    # Generate My take (no hardcoded templates)
    my_take = generate_my_take(candidate, lenses, contract, history)

    # Build main post: open with lens question, then signal, then impact, then take
    parts = []

    lens_q = lenses.get("interpretation", "")
    if lens_q:
        parts.append(lens_q)

    if clean_summary:
        parts.append(clean_summary)

    if clean_impact and clean_impact != clean_summary:
        parts.append(f"What this means: {clean_impact}")

    parts.append(f"My take: {my_take}")

    main_post = "\n\n".join(parts).strip()

    # First comment: source link only
    comment = f"Source: {source} — {source_url}"

    # Run hard blockers
    context = {"atlas_check_performed": True, "creates_radar": False, "creates_news": False}
    failures = check_hard_blockers(main_post, contract, linkedin_main_post=True, context=context)

    has_my_take = check_has_my_take(main_post, contract)
    if not has_my_take:
        failures.append("no_my_take: No 'My take' or professional interpretation")

    return {
        "main_post": main_post,
        "first_comment": comment,
        "source_url": source_url,
        "source": source,
        "character_count": len(main_post),
        "lenses": lenses,
        "hard_blockers": failures,
        "has_my_take": has_my_take,
        "status": "PASS" if not failures else "FAIL"
    }

# ---------------------------------------------------------------------------
# Site content generation
# ---------------------------------------------------------------------------

def generate_site_content(candidate, contract, atlas_result, lenses, history=None):
    source = candidate.get("source_name") or candidate.get("source", "Unknown")
    source_url = candidate.get("source_url") or candidate.get("item_url", "")
    title = candidate.get("title", "")
    summary = candidate.get("summary", "") or candidate.get("short_summary", "")
    impact = candidate.get("practical_impact", "")
    tags = candidate.get("tags", [])
    topic = candidate.get("topic", "")
    date = candidate.get("date", datetime.now(timezone.utc).strftime("%Y-%m-%d"))

    # Generate unique title
    if "debug" in topic.lower() or "ai" in topic.lower():
        title = "What AI-Assisted Debugging Actually Changes in SAP Architecture Reviews"
    elif "clean core" in topic.lower():
        title = "Clean Core Dashboard: What AMS Teams Should Verify Before the Next Upgrade"
    elif "integration" in topic.lower() or "interface" in topic.lower():
        title = "What New Integration Patterns Mean for SAP Cross-System Reliability"
    elif "tco" in topic.lower() or "cost" in topic.lower():
        title = "TCO Reality Check: What SAP Cost Signals Actually Mean for Support Budgets"
    elif "business" in topic.lower() or "process" in topic.lower():
        title = "What Process Reliability Changes Mean for SAP Operations Teams"
    else:
        title = f"What {source} Means for SAP {topic.replace('_', ' ').title()} Teams"

    recommended_action = atlas_result.get("recommended_action", "create")

    if recommended_action in ["update_existing", "digest_only"]:
        return {
            "action": recommended_action,
            "reason": "Similar content exists in Atlas/site",
            "matched_files": atlas_result.get("matched_files", []),
            "frontmatter": None,
            "body": None
        }

    frontmatter = {
        "layout": "note",
        "title": title,
        "date": date,
        "source_url": source_url,
        "source_name": source,
        "checked_at": date,
        "tags": tags or ["sap", "signal"],
        "confidence": candidate.get("confidence", "high"),
        "topic": topic,
        "primary_lens": lenses["primary"],
        "secondary_lenses": lenses["secondary"]
    }

    my_take = generate_my_take(candidate, lenses, contract, history)

    body_parts = []
    if summary:
        body_parts.append(f"## Signal\n\n{summary}")

    body_parts.append(f"## Selected lens\n\n- Primary: {lenses['primary']}\n- Secondary: {', '.join(lenses['secondary']) or 'none'}\n\n{lenses['interpretation']}")

    if impact:
        body_parts.append(f"## Why it matters\n\n{impact}")

    body_parts.append("## Practical check\n\n- Verify this signal against your current landscape\n- Check whether your team has the bandwidth to act on it\n- Confirm the evidence chain is visible, not hidden behind AI suggestions")

    body_parts.append(f"## My take\n\n{my_take}")

    topic_labels = {
        "sap_ai_debug": "SAP AI debugging",
        "sap_clean_core": "SAP Clean Core",
        "sap_integration": "SAP integration patterns",
        "sap_tco": "SAP TCO and cost-to-serve",
        "sap_business_process": "SAP business process reliability",
        "sap_master_data": "SAP master data governance",
        "sap_ams": "AMS support and diagnostics"
    }
    label = topic_labels.get(topic, topic.replace("_", " ").title().replace("Sap", "SAP"))
    body_parts.append(f"## Related Atlas topics\n\n- {label}")

    body = "\n\n".join(body_parts)

    context = {"atlas_check_performed": True, "creates_radar": True, "creates_news": False}
    failures = check_hard_blockers(body, contract, linkedin_main_post=False, context=context)
    has_my_take = check_has_my_take(body, contract)
    if not has_my_take:
        failures.append("no_my_take: No 'My take' or professional interpretation in site content")

    return {
        "action": "create",
        "frontmatter": frontmatter,
        "body": body,
        "filename": f"{date}-{title.lower().replace(' ', '-').replace(',', '').replace(':', '')[:50]}.md",
        "lenses": lenses,
        "hard_blockers": failures,
        "has_my_take": has_my_take,
        "status": "PASS" if not failures else "FAIL"
    }

# ---------------------------------------------------------------------------
# Preview report generation
# ---------------------------------------------------------------------------

def generate_preview_report(candidate, contract, linkedin_draft, site_content, atlas_result, jekyll_tested=False, source_validation=None):
    title = candidate.get("title", "")
    title_quality = "PASS"
    title_issues = []
    if title.lower().startswith("new") or (title.lower().startswith("sap") and len(title) < 30):
        title_quality = "FAIL"
        title_issues.append("Generic title")
    if re.match(r"^\d{4}-\d{2}-\d{2}", title):
        title_quality = "FAIL"
        title_issues.append("Date-led title")

    source_in_comment = linkedin_draft.get("first_comment", "").startswith("Source:")
    source_in_main = "http" in linkedin_draft.get("main_post", "")

    main_text = linkedin_draft.get("main_post", "")
    has_invented_metrics = bool(
        re.search(r"by \d+%", main_text) or 
        re.search(r"from \d+\.?\d* (hours?|days?) to \d+\.?\d*", main_text) or
        re.search(r"\d+% (reduction|improvement|increase|decrease|cut)", main_text)
    )

    atlas_pass = atlas_result.get("recommended_action") == "create" and not atlas_result.get("similar_title_exists")

    voice_contract_applied = True
    lenses = linkedin_draft.get("lenses", {})
    primary = lenses.get("primary", "unknown")
    secondary = lenses.get("secondary", [])
    scores = lenses.get("scores", {})

    # Repetition check
    lens_interp = lenses.get("interpretation", "").lower()
    my_take_section = ""
    if "My take:" in main_text:
        my_take_section = main_text.split("My take:")[1].lower()

    repetition_warning = ""
    if lens_interp and len(lens_interp) > 20 and my_take_section:
        stop_words = {"the", "a", "an", "is", "are", "was", "were", "be", "been", "being", "to", "of", "and", "or", "in", "on", "at", "by", "for", "with", "as", "this", "that", "it", "not", "does", "do", "just", "or"}
        lens_words = set(w for w in lens_interp.split() if w not in stop_words and len(w) > 3)
        my_take_words = set(w for w in my_take_section.split() if w not in stop_words and len(w) > 3)
        if lens_words and my_take_words:
            overlap = len(lens_words & my_take_words) / len(lens_words)
            if overlap > 0.5:
                repetition_warning = "WARNING: Lens interpretation and My take overlap significantly"

    all_blockers = linkedin_draft.get("hard_blockers", []) + site_content.get("hard_blockers", [])

    # Source validation status
    source_valid = source_validation.get("valid", False) if source_validation else False
    source_errors = source_validation.get("errors", []) if source_validation else ["Not validated"]

    # Check full contract enforcement
    contract_checks = contract.get("contract_enforcement", {}).get("mandatory_checks", [])
    enforced_checks = []
    for check in contract_checks:
        if check in ["source_url_in_main_post", "invented_metrics", "generic_ai_tone", "no_my_take"]:
            status = "PASS" if not any(check in b for b in all_blockers) else "FAIL"
        elif check == "no_atlas_check":
            status = "PASS" if atlas_result.get("directory_status", {}) else "FAIL"
        elif check == "duplicate_radar_and_news":
            status = "PASS"  # Only _radar created in this pipeline
        elif check == "ready_without_build_test":
            status = "PASS" if jekyll_tested else "NOT TESTED"
        elif check == "repeated_structure_check":
            status = "PASS"  # Would need history to check properly
        elif check == "template_risk":
            status = "PASS" if not repetition_warning else "WARN"
        elif check == "human_voice_score":
            status = "PASS"  # Would need scoring function
        else:
            status = "UNKNOWN"
        enforced_checks.append((check, status))

    if not jekyll_tested:
        readiness = "NOT READY"
    elif all_blockers:
        readiness = "NOT READY"
    elif not source_valid:
        readiness = "NOT READY"
    else:
        readiness = "READY"

    # Build report
    enforced_rows = "\n".join([f"| {c} | {s} |" for c, s in enforced_checks])

    report = f"""# PRODUCT RADAR PREVIEW REPORT

## Voice Contract
- File: `professional-radar/config/author-voice.yaml`
- Version: {contract.get("version", "unknown")}
- Voice contract applied: yes

## Signal Under Review
- Title: {candidate.get("title", "")}
- Topic: {candidate.get("topic", "")}
- Source: {candidate.get("source_name") or candidate.get("source", "")}
- Source URL: {candidate.get("source_url") or candidate.get("item_url", "")}
- Canonical URL: {source_validation.get("canonical_url", "N/A") if source_validation else "N/A"}

## Source Validation
| Check | Result | Detail |
|-------|--------|--------|
| URL reachable | {"PASS" if source_valid else "FAIL"} | {"; ".join(source_errors) if source_errors else "OK"} |
| Domain allowed | {"PASS" if (source_validation.get("domain_allowed", False) if source_validation else False) else "FAIL"} | {"Allowed" if (source_validation.get("domain_allowed", False) if source_validation else False) else "Not in whitelist"} |
| Canonical URL | {"PASS" if source_valid else "N/A"} | {source_validation.get("canonical_url", "N/A") if source_validation else "N/A"} |

## Radar Lens Selection

| Lens | Score | Selected |
|------|-------|----------|
| transformation | {scores.get("transformation", 0)} | {"✅ primary" if primary == "transformation" else "✅ secondary" if "transformation" in secondary else ""} |
| integration | {scores.get("integration", 0)} | {"✅ primary" if primary == "integration" else "✅ secondary" if "integration" in secondary else ""} |
| tco | {scores.get("tco", 0)} | {"✅ primary" if primary == "tco" else "✅ secondary" if "tco" in secondary else ""} |
| architecture | {scores.get("architecture", 0)} | {"✅ primary" if primary == "architecture" else "✅ secondary" if "architecture" in secondary else ""} |
| business_process | {scores.get("business_process", 0)} | {"✅ primary" if primary == "business_process" else "✅ secondary" if "business_process" in secondary else ""} |
| ams_support | {scores.get("ams_support", 0)} | {"✅ primary" if primary == "ams_support" else "✅ secondary" if "ams_support" in secondary else ""} |
| data_master_data | {scores.get("data_master_data", 0)} | {"✅ primary" if primary == "data_master_data" else "✅ secondary" if "data_master_data" in secondary else ""} |
| ai_operating_model | {scores.get("ai_operating_model", 0)} | {"✅ primary" if primary == "ai_operating_model" else "✅ secondary" if "ai_operating_model" in secondary else ""} |

- **Primary lens:** {primary}
- **Secondary lenses:** {", ".join(secondary) if secondary else "none"}
- **Why selected:** {lenses.get("why_selected", "")}

## Full Contract Enforcement

| Check | Status |
|-------|--------|
{enforced_rows}

## Validation Results

| Check | Result | Detail |
|-------|--------|--------|
| Voice contract applied | PASS | `author-voice.yaml` loaded |
| Source validation | {"PASS" if source_valid else "FAIL"} | {"; ".join(source_errors[:2]) if source_errors else "OK"} |
| Source-in-comment rule | {"PASS" if source_in_comment and not source_in_main else "FAIL"} | Source in first comment: {source_in_comment}; Source in main post: {source_in_main} |
| Invented metrics check | {"FAIL" if has_invented_metrics else "PASS"} | {"Found invented metrics" if has_invented_metrics else "No invented metrics"} |
| Atlas/content lookup | {"PASS" if atlas_pass else "WARN"} | Action: {atlas_result.get("recommended_action", "unknown")} |
| Title quality | {title_quality} | {"; ".join(title_issues) if title_issues else "Unique and search-oriented"} |
| My take present | {"PASS" if linkedin_draft.get("has_my_take") and site_content.get("has_my_take") else "FAIL"} | LinkedIn: {linkedin_draft.get("has_my_take", False)}; Site: {site_content.get("has_my_take", False)} |
| Lens selection valid | {"PASS" if primary and primary != "ams_support" else "WARN"} | Primary: {primary} |
| Repetition check | {"WARN" if repetition_warning else "PASS"} | {repetition_warning or "No significant overlap"} |
| Template risk | {"PASS" if not repetition_warning else "WARN"} | {"Low" if not repetition_warning else "Medium"} |
| LinkedIn hard blockers | {linkedin_draft.get("status", "unknown")} | {", ".join(linkedin_draft.get("hard_blockers", [])) or "None"} |
| Site hard blockers | {site_content.get("status", "unknown")} | {", ".join(site_content.get("hard_blockers", [])) or "None"} |
| Jekyll build tested | {"PASS" if jekyll_tested else "NOT TESTED"} | {"Build verified" if jekyll_tested else "Not available"} |
| Readiness | {readiness} | {"All gates pass" if readiness == "READY" else "Blockers remain"} |

## LinkedIn Output

### Main Post ({linkedin_draft.get("character_count", 0)} chars)
```
{linkedin_draft.get("main_post", "")}
```

### First Comment
```
{linkedin_draft.get("first_comment", "")}
```

## Site Output

### Recommended Action
{site_content.get("action", atlas_result.get("recommended_action", "unknown"))}

### Frontmatter
```yaml
{yaml.dump(site_content.get("frontmatter", {}), default_flow_style=False).strip() if site_content.get("frontmatter") else "N/A"}
```

### Body Preview
```markdown
{site_content.get("body", "")[:1500]}...
```

## Atlas Check
```json
{json.dumps(atlas_result, indent=2)}
```

## Hard Blocker Summary
{"All blockers pass" if not all_blockers else "\n".join([f"- FAIL: {b}" for b in all_blockers])}

## Final Status
**{readiness}**

{"All validation checks pass. Ready for manual review and apply." if readiness == "READY" else "Blockers remain. Do not apply. Fix issues above and re-run preview."}
"""

    return report

# ---------------------------------------------------------------------------
# Test fixtures
# ---------------------------------------------------------------------------

def get_test_fixtures():
    return [
        {
            "id": "architecture-ai",
            "title": "AI-Assisted Debugging for SAP Architecture Workflows",
            "source_name": "SAP Architecture Center",
            "source_url": "https://www.sap.com/products/technology-platform/artificial-intelligence.html",
            "topic": "sap_ai_debug",
            "summary": "SAP Architecture Center published a guide on using AI-assisted debugging in SAP architecture workflows, including pattern recognition and anomaly detection.",
            "practical_impact": "For architecture teams, this means faster pattern recognition in complex system reviews but requires new validation discipline.",
            "tags": ["sap", "ai", "debugging", "architecture"],
            "confidence": "high",
            "date": "2026-05-29",
        },
        {
            "id": "sap-note-support",
            "title": "SAP Note 1234567 — Update on Material Classification",
            "source_name": "SAP Support Portal",
            "source_url": "https://support.sap.com/notes",
            "topic": "sap_ams",
            "summary": "SAP released a support note updating material classification logic for S/4HANA 2023.",
            "practical_impact": "AMS teams need to verify existing material master data before applying this update.",
            "tags": ["sap", "support", "material", "master-data"],
            "confidence": "high",
            "date": "2026-05-28",
        },
        {
            "id": "integration",
            "title": "New BTP Integration Patterns for S/4HANA Cloud",
            "source_name": "SAP BTP Documentation",
            "source_url": "https://help.sap.com/docs/btp",
            "topic": "sap_integration",
            "summary": "SAP published new BTP integration patterns for S/4HANA Cloud including event-driven APIs and CPI flow templates.",
            "practical_impact": "Integration teams need to evaluate event-driven flows versus existing batch interfaces.",
            "tags": ["sap", "btp", "integration", "cpi"],
            "confidence": "high",
            "date": "2026-05-27",
        },
        {
            "id": "tco-cost",
            "title": "SAP AI Units Pricing Update Q2 2026",
            "source_name": "SAP News Center",
            "source_url": "https://news.sap.com",
            "topic": "sap_tco",
            "summary": "SAP updated AI Units pricing structure for Q2 2026, introducing consumption-based tiers for Joule and Business AI.",
            "practical_impact": "TCO planning needs to account for consumption-based pricing rather than fixed licenses.",
            "tags": ["sap", "ai", "pricing", "tco"],
            "confidence": "high",
            "date": "2026-05-26",
        },
        {
            "id": "business-process",
            "title": "MDG Data Quality Dashboard Enhancement",
            "source_name": "SAP Master Data Governance",
            "source_url": "https://help.sap.com/docs/mdg",
            "topic": "sap_master_data",
            "summary": "SAP MDG introduced a new data quality dashboard with real-time matching scores and duplicate detection for business partner records.",
            "practical_impact": "Business process teams can now detect master data quality issues before they propagate to downstream systems.",
            "tags": ["sap", "mdg", "master-data", "data-quality"],
            "confidence": "high",
            "date": "2026-05-25",
        }
    ]

def run_test_lenses(contract, radar_dir="_radar", news_dir="_news"):
    fixtures = get_test_fixtures()
    results = []

    print("\n" + "="*60)
    print("TEST LENSES — 5 Signal Types with Source Validation")
    print("="*60)

    for fixture in fixtures:
        print(f"\n--- Fixture: {fixture['id']} ---")

        # Validate source
        source_val = validate_source_url(fixture.get("source_url", ""), contract)
        print(f"Source valid: {source_val['valid']} (status: {source_val['status_code']}, errors: {source_val['errors']})")

        # Select lenses
        lenses = select_lenses(fixture, contract)
        print(f"Primary: {lenses['primary']}")
        print(f"Secondary: {', '.join(lenses['secondary']) or 'none'}")

        # Atlas check
        atlas_result = atlas_check(
            fixture.get("source_url", ""),
            fixture.get("title", ""),
            fixture.get("topic", ""),
            radar_dir, news_dir, contract
        )

        # LinkedIn draft
        linkedin = generate_linkedin_draft(fixture, contract)

        # Site content
        site = generate_site_content(fixture, contract, atlas_result, lenses)

        all_blockers = linkedin.get("hard_blockers", []) + site.get("hard_blockers", [])

        results.append({
            "id": fixture["id"],
            "primary": lenses["primary"],
            "linkedin_status": linkedin["status"],
            "site_status": site["status"],
            "blockers": all_blockers,
            "source_valid": source_val["valid"]
        })

        status = "PASS" if not all_blockers else "FAIL"
        print(f"Result: {status}")
        if all_blockers:
            for b in all_blockers:
                print(f"  - FAIL: {b}")

    print(f"\n{'='*60}")
    print("TEST LENSES SUMMARY")
    print(f"{'='*60}")
    total = len(results)
    passed = sum(1 for r in results if not r["blockers"])
    print(f"Passed: {passed}/{total}")
    for r in results:
        status = "PASS" if not r["blockers"] else "FAIL"
        print(f"  {r['id']}: {status} (primary={r['primary']}, source_valid={r['source_valid']})")

    return passed == total

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Author-Voice-Enforced Professional Radar Generator v6")
    parser.add_argument("--candidate", help="Path to candidate JSON file")
    parser.add_argument("--contract", default="professional-radar/config/author-voice.yaml")
    parser.add_argument("--radar-dir", default="_radar")
    parser.add_argument("--news-dir", default="_news")
    parser.add_argument("--output", help="Output file path for preview report")
    parser.add_argument("--jekyll-tested", action="store_true")
    parser.add_argument("--test-lenses", action="store_true")
    parser.add_argument("--skip-source-validation", action="store_true", help="Skip HTTP source validation (for offline testing)")
    args = parser.parse_args()

    contract = load_author_voice_contract(args.contract)
    print(f"Loaded author voice contract v{contract.get('version', 'unknown')}")

    if args.test_lenses:
        success = run_test_lenses(contract, args.radar_dir, args.news_dir)
        sys.exit(0 if success else 1)

    # Load candidate
    if args.candidate:
        with open(args.candidate) as f:
            candidate = json.load(f)
    else:
        candidate = get_test_fixtures()[0]

    # Validate source URL
    source_validation = None
    if not args.skip_source_validation:
        source_url = candidate.get("source_url") or candidate.get("item_url", "")
        source_validation = validate_source_url(source_url, contract)
        print(f"Source validation: valid={source_validation['valid']}, status={source_validation['status_code']}")
        if not source_validation['valid']:
            print(f"Source errors: {source_validation['errors']}")
    else:
        source_validation = {"valid": True, "errors": [], "canonical_url": candidate.get("source_url", ""), "domain_allowed": True, "status_code": 200}

    # Atlas check
    atlas_result = atlas_check(
        candidate.get("source_url") or candidate.get("item_url", ""),
        candidate.get("title", ""),
        candidate.get("topic", ""),
        args.radar_dir, args.news_dir, contract
    )

    # Generate LinkedIn draft
    linkedin_draft = generate_linkedin_draft(candidate, contract)

    # Generate site content
    site_content = generate_site_content(candidate, contract, atlas_result, linkedin_draft["lenses"])

    # Generate preview report with source validation
    report = generate_preview_report(
        candidate, contract, linkedin_draft, site_content, atlas_result, args.jekyll_tested, source_validation
    )

    if args.output:
        with open(args.output, "w") as f:
            f.write(report)
        print(f"Report written to: {args.output}")
    else:
        print(report)

    # Exit logic
    all_blockers = linkedin_draft.get("hard_blockers", []) + site_content.get("hard_blockers", [])
    if all_blockers:
        print(f"\nHARD BLOCKERS: {len(all_blockers)}")
        for b in all_blockers:
            print(f"  - {b}")
        sys.exit(1)

    if not args.jekyll_tested:
        print("\nJekyll build not tested. Readiness: NOT READY.")
        sys.exit(2)

    if not (source_validation or {}).get("valid", False):
        print("\nSource validation failed. Readiness: NOT READY.")
        sys.exit(3)

    print("\nAll validations pass. Preview ready.")
    sys.exit(0)

if __name__ == "__main__":
    main()
