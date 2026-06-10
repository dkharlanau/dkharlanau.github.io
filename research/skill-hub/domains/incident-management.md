---
title: "Domain Research: Incident Management"
robots: noindex
sitemap: false
---

# Incident Management

## Research question

What professional skills, artifacts, rules, and quality gates should Skill Hub extract from incident triage, command structures, and operational response?

## Best sources

| Source | Tier | Why it matters | Useful for |
|---|---:|---|---|
| [Anatomy of an Incident (Google SRE)](https://sre.google/static/pdf/Anatomy_Of_An_Incident.pdf) (src-401) | 1 | Defines incident lifecycle and IMAG structure | Incident roles, postmortems, SLOs |
| [Google SRE Book](https://sre.google/sre-book/table-of-contents/) (src-403) | 1 | Foundational SRE text with public chapters | Emergency response, playbooks, role definition |
| [Google SRE Incident Management Guide](https://sre.google/resources/practices-and-processes/incident-management-guide/) (src-404) | 1 | Condensed guide on remediation and learning | Postmortem timeliness, structured response |
| [ITIL 4 Incident Management Overview](https://www.beyond20.com/resources/blog/an-overview-of-the-incident-management-practice-in-itil-4/) (src-408) | 2 | Practitioner-oriented ITIL 4 summary | Incident registration, major incident procedures |
| [incident.io Best Practices 2026](https://incident.io/blog/incident-management-best-practices-2026) (src-411) | 2 | Phase-based guide with concrete checklists | Maturity phases, severity definitions, postmortem scheduling |
| [Rootly SRE Incident Management](https://rootly.com/sre/sre-incident-management-best-practices-boost-reliability) (src-417) | 2 | Full lifecycle guide with automation focus | Blameless postmortems, MTTA/MTTR tracking |
| [SAP Incident Processing](https://assets.dm.ux.sap.com/webinars/sap-user-groups-k4u/pdfs/200421_essential_tips_on_end_to_end_sap_incident_processing.pdf) (src-415) | 1 | Official SAP guidance on incident quality | Perfect incident criteria, CIC escalation, Guided Answers |

## Key practical patterns

- Declare incidents early and use a dedicated communication channel (war room / incident channel).
- Assign clear roles within the first 5 minutes: Incident Commander, Operations Lead, Communications Lead, Planning/Scribe.
- Prioritize mitigation (service restoration) over root cause investigation during active incidents.
- Use severity levels (SEV1–SEV4) with explicit criteria to drive consistent escalation.
- Automate administrative toil: auto-create incident channels, page on-call, pull monitoring graphs.
- Playbook presence results in ~3x lower MTTR.

## Artifacts found

- Incident declaration and severity classification record
- Real-time incident timeline (timestamped observations, not conclusions)
- Dedicated incident channel transcript / war room log
- Handoff document (when rotating staff during long incidents)
- Post-incident action item tickets
- Runbook / Pager Playbook (per-alert response guide)
- Service Catalog with ownership and severity classification

## Decision rules found

- If an alert fires and meets SEV1/SEV2 criteria, then auto-create a dedicated incident channel and page the primary on-call within 2 minutes.
- If the Operations Lead is overloaded, then the Incident Commander delegates additional staff; the IC never does technical work.
- If mitigation and root cause investigation are competing for attention, then prioritize mitigation first.
- If an incident lasts longer than the on-call shift, then arrange a structured handoff with verbal briefing and explicit role transfer confirmation.
- If an alert consistently fires without leading to action, then increase the threshold or convert it to a dashboard metric.

## Quality gates found

- Service Catalog is complete: every service has an owner, severity classification, and linked runbook.
- On-call rotation is documented in the incident management tool, not a spreadsheet.
- Severity levels are defined, published, and understood by all engineers.
- Rollback runbooks are tested and linked to relevant alert types.
- 100% of SEV1 and SEV2 incidents have a scheduled postmortem review within 48–72 hours.

## Common failure modes

- Alert fatigue: everything pages, so engineers ignore or silence notifications.
- Hero culture: one senior engineer handles every major incident; when unavailable, the team has no muscle memory.
- Freelancing: uncoordinated changes during an incident make the situation worse.
- Fix-it trap: resolving the incident and skipping the postmortem guarantees recurrence.
- Poor communication: stakeholders receive no updates, or updates are inconsistent with internal status.

## Candidate skills

- `incident-commander-basics`
- `severity-classification`
- `war-room-discipline`
- `mitigation-first-response`
- `alert-tuning`
- `playbook-driven-response`

## Source-backed notes

- Google SRE defines the incident lifecycle: detection, response, mitigation, resolution, postmortem (src-401).
- Google SRE Book states that playbook presence results in ~3x lower MTTR and clearly defined roles resolve incidents faster (src-403).
- ITIL 4 requires all incidents to be registered, classified, and prioritized; major incident procedures should be predefined (src-408).
- SAP defines the "perfect customer incident": correct system, component, meaningful text, screenshots, SAP Notes search done, remote connection open (src-415).

## Gaps / further research needed

- Public operational postmortems or detailed RCA case studies from SAP landscapes are rare.
- ITIL 4 primary source depth is limited; official AXELOS Practice Guides are paywalled.