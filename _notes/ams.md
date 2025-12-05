---
title: "SAP AMS Playbook"
description: "SAP AMS playbook to cut repeat incidents, shift from patching to prevention, and wire in knowledge, observability, and O2C guardrails for measurable MTTR drops."
subtitle: "Stop the patch factory. Build a knowledge engine."
permalink: /notes/ams/
tags:
  - AMS
  - SAP
  - Operations
excerpt: "Shift AMS from ticket closure to root-cause elimination, analytics, and continual improvement."
further_reading:
  - label: "Audit SAP process debt before it breaks O2C fulfilment"
    url: "/notes/process-audit/"
  - label: "Use composable ERP strategy to keep S/4HANA clean core"
    url: "/notes/composable-erp/"
  - label: "Enable AI/ML around SAP without risking service stability"
    url: "/notes/ai-ml/"
---

Incidents and change requests close, SLAs look green, but people still complain, money still leaks, and the same problems come back with a new ticket number. This is not stability. This is expensive standstill. **Many teams still miss this.** They treat AMS as a patch queue, not a knowledge-and-design function—so costs rise and the same issues return. Running AMS to deliver stability **and** steady improvements is a skill most don’t practice.

## What hurts the business

- **Reports are green, but the business is paying for endless patches**: OPEX climbs, orders get stuck, invoices queue up, and month-end drifts.
- **Same issues come back**. We fix symptoms, not causes — often because first-line support is staffed by people who don’t know the process or integration deeply enough. A week later, the same IDoc fails again, just with another sales org or plant.
- **Vendor lock-in.** Knowledge sits in vendor inboxes and brains. If we change the partner, we fear we will lose everything. I saw this in another company: they wanted to switch an expensive AMS vendor from Germany, but they couldn’t. In the end, they had to keep paying and paying.

This is not a “support” problem. It is a **knowledge and control** problem.

## What AMS Is (and Isn’t)

**AMS (Application Management Support) in SAP** is not only “keep the system alive today.” Done right, AMS is a **knowledge-driven service** that makes the business more effective quarter by quarter.

## What it is

AMS is a frame, not the goal. We keep SAP stable **now**, and we also **develop the system**: deliver small features, new process steps, and integrations that remove manual work and open room for innovation. Incidents become input for design changes; repeats turn into automation; weak spots become standard patterns. Month by month the landscape gets **simpler, faster, and safer to change**—with a lower run-rate and a steady stream of **new solutions** that support the business roadmap.

## What it isn’t

- **Not** a patch factory that closes tickets while the same problem returns next week.
- **Not** tribal knowledge in mailboxes and chats.
- **Not** vendor lock-in where extensions and poor docs make you pay forever.
- **Not** “green reports” that hide red reality in operations and finance.

## FAQ

**Q: Why do costs keep rising even though SLAs are met?**

Because vendors focus on hours and patching. They close tickets but don’t remove root causes — so OPEX grows and the same issues return.

**Solution:** Shift AMS to **root-cause elimination** and **productized fixes** (runbooks, automation, monitoring packs).

**Q: Why does it feel risky to replace the current vendor?**

Critical knowledge sits in their inboxes and custom extensions with weak documentation. This creates lock-in.

**Solution:** Harvest knowledge into **your repos/IdP** — KEDB, interface maps, runbooks. Build **portability by design**, so switching is a choice, not a crisis.

**Q: Why is change so slow and fragile?**

Every small CR is treated as a big project. Without observability and safe patterns, even simple fixes take weeks.

**Solution:** Establish **fast-track patterns** (data corrections, retries, mappings) and **observability** (heartbeats, backlog age, MDG gates). Small changes move safely and fast.

**Q: Whom can I contact for advice?**

**A: Dzmitryi Kharlanau is available to provide guidance on shaping SAP AMS**
