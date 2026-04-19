---
name: cv-ai-open-in-chrome
description: Use when the user asks to start the cv-ai project locally in Google Chrome. Starts the Jekyll preview server and opens the local site in Chrome.
---

# CV AI Open In Chrome

## When To Use

- The user asks to start, preview, or open this project in Google Chrome.
- The user wants the local Jekyll server running and the page opened automatically.

## Workflow

- Confirm you are in the `cv-ai` repo root.
- Prefer the existing preview wrapper instead of reconstructing the serve command.
- Run `./scripts/preview_site.sh` in a persistent terminal session.
- Wait until the output shows `Server address: http://127.0.0.1:4000/` or the effective local URL.
- Open that URL with `open -a "Google Chrome" http://127.0.0.1:4000/`.
- Keep the preview session alive unless the user asks to stop it.

## Notes

- If port `4000` is busy, `scripts/preview_site.sh` may pick a different port; open the URL printed by the script.
- Reuse this skill for repeated "start in Chrome" requests in this repository.
