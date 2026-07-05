---
name: check-codex-reset-credits
description: Safely query and summarize remaining Codex manual rate-limit reset credits and their expiration times without exposing local ChatGPT credentials or profile data. Use when the user asks about Codex banked resets, manual resets, reset credits, remaining reset count, earned reset count, reset status, or reset expiration.
---

# Check Codex Reset Credits

Query the read-only reset-credit endpoint with the bundled script:

```bash
python3 scripts/check_reset_credits.py
```

Use `--json` only when structured output is useful. Its output is sanitized.

## Safety requirements

- Run only the bundled script; do not print, copy, parse interactively, or persist `~/.codex/auth.json`.
- Permit only `GET https://chatgpt.com/backend-api/wham/rate-limit-reset-credits`.
- Never call `/consume`, issue POST requests, redeem a reset, or modify account state.
- Never show access tokens, account IDs, credit IDs, profile user IDs, profile images, titles, descriptions, or raw API responses.
- If network access needs approval, request approval specifically for the read-only GET to `chatgpt.com`.
- Treat this endpoint as an undocumented implementation detail that may change. Do not present community observations as official policy.

## Report

Return:

- available manual reset count;
- total earned reset count;
- each sanitized credit's status and reset type;
- grant, expiration, redemption-started, and redeemed times when present;
- expiration in both UTC and the machine's local timezone.

State that the query was read-only and no reset was consumed. If the response schema changes, report the failure without exposing the raw response. Mention the documented interactive alternative, Codex CLI `/usage`, when useful.
