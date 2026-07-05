#!/usr/bin/env python3
"""Safely query Codex manual reset credits without exposing credentials."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


ENDPOINT = "https://chatgpt.com/backend-api/wham/rate-limit-reset-credits"
MAX_RESPONSE_BYTES = 1_048_576
SAFE_CREDIT_FIELDS = (
    "status",
    "reset_type",
    "granted_at",
    "expires_at",
    "redeem_started_at",
    "redeemed_at",
)


class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Prevent credentials from being forwarded through an unexpected redirect."""

    def redirect_request(
        self,
        req: urllib.request.Request,
        fp: Any,
        code: int,
        msg: str,
        headers: Any,
        newurl: str,
    ) -> None:
        return None


def parse_args() -> argparse.Namespace:
    default_auth = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")) / "auth.json"
    parser = argparse.ArgumentParser(
        description="Read remaining Codex manual reset credits without consuming them."
    )
    parser.add_argument(
        "--auth-file",
        type=Path,
        default=default_auth,
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print sanitized JSON instead of a human-readable summary.",
    )
    return parser.parse_args()


def load_credentials(path: Path) -> tuple[str, str]:
    try:
        payload = json.loads(path.expanduser().read_text(encoding="utf-8"))
        tokens = payload["tokens"]
        access_token = tokens["access_token"]
        account_id = tokens["account_id"]
    except FileNotFoundError as exc:
        raise RuntimeError("Codex authentication was not found; run `codex login`.") from exc
    except (KeyError, TypeError, json.JSONDecodeError, OSError) as exc:
        raise RuntimeError("Codex authentication is unreadable; run `codex login`.") from exc

    if not isinstance(access_token, str) or not access_token:
        raise RuntimeError("Codex access token is missing; run `codex login`.")
    if not isinstance(account_id, str) or not account_id:
        raise RuntimeError("Codex account ID is missing; run `codex login`.")
    return access_token, account_id


def fetch_credits(access_token: str, account_id: str) -> Dict[str, Any]:
    request = urllib.request.Request(
        ENDPOINT,
        method="GET",
        headers={
            "Authorization": f"Bearer {access_token}",
            "ChatGPT-Account-ID": account_id,
            "originator": "Codex Desktop",
            "Accept": "application/json",
        },
    )
    opener = urllib.request.build_opener(NoRedirectHandler())
    try:
        with opener.open(request, timeout=20) as response:
            raw = response.read(MAX_RESPONSE_BYTES + 1)
    except urllib.error.HTTPError as exc:
        if exc.code in (301, 302, 303, 307, 308):
            raise RuntimeError("The endpoint redirected unexpectedly; refusing to forward credentials.") from exc
        if exc.code in (401, 403):
            raise RuntimeError("Codex authentication was rejected; run `codex login`.") from exc
        raise RuntimeError(f"The reset-credit query failed with HTTP {exc.code}.") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError("The reset-credit query could not reach chatgpt.com.") from exc

    if len(raw) > MAX_RESPONSE_BYTES:
        raise RuntimeError("The endpoint returned an unexpectedly large response.")
    try:
        payload = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RuntimeError("The endpoint returned an invalid response.") from exc
    if not isinstance(payload, dict):
        raise RuntimeError("The endpoint response schema changed.")
    return payload


def sanitize(payload: Dict[str, Any]) -> Dict[str, Any]:
    available_count = payload.get("available_count")
    total_earned_count = payload.get("total_earned_count")
    credits = payload.get("credits")

    if not isinstance(available_count, int) or not isinstance(total_earned_count, int):
        raise RuntimeError("The endpoint response schema changed.")
    if not isinstance(credits, list):
        raise RuntimeError("The endpoint response schema changed.")

    safe_credits: List[Dict[str, Any]] = []
    for credit in credits:
        if not isinstance(credit, dict):
            raise RuntimeError("The endpoint response schema changed.")
        safe_credit: Dict[str, Any] = {}
        for field in SAFE_CREDIT_FIELDS:
            value = credit.get(field)
            if value is not None and not isinstance(value, str):
                raise RuntimeError("The endpoint response schema changed.")
            safe_credit[field] = value
        safe_credits.append(safe_credit)

    safe_credits.sort(key=lambda item: item.get("expires_at") or "")
    return {
        "queried_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "available_count": available_count,
        "total_earned_count": total_earned_count,
        "credits": safe_credits,
    }


def format_timestamp(value: Optional[str]) -> str:
    if not value:
        return "—"
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        utc_text = parsed.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
        local_text = parsed.astimezone().isoformat()
        return f"{utc_text} (local: {local_text})"
    except ValueError:
        return "unrecognized timestamp"


def print_human(result: Dict[str, Any]) -> None:
    print(f"Available manual resets: {result['available_count']}")
    print(f"Total earned resets: {result['total_earned_count']}")
    credits = result["credits"]
    if not credits:
        print("Credits: none")
        return

    print("Credits:")
    for index, credit in enumerate(credits, start=1):
        print(
            f"  {index}. status={credit['status'] or 'unknown'}, "
            f"type={credit['reset_type'] or 'unknown'}"
        )
        print(f"     granted: {format_timestamp(credit['granted_at'])}")
        print(f"     expires: {format_timestamp(credit['expires_at'])}")
        if credit["redeem_started_at"]:
            print(f"     redeem started: {format_timestamp(credit['redeem_started_at'])}")
        if credit["redeemed_at"]:
            print(f"     redeemed: {format_timestamp(credit['redeemed_at'])}")


def main() -> int:
    args = parse_args()
    try:
        access_token, account_id = load_credentials(args.auth_file)
        result = sanitize(fetch_credits(access_token, account_id))
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print_human(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
