#!/usr/bin/env python3
import json
import os
import re
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(parents=True, exist_ok=True)

ACCOUNTS = ["TheCesarCross", "sovren_software"]
MAX_TIMELINE = int(os.getenv("CMO_TIMELINE_MAX", "20"))


def load_credential_mapping() -> None:
    """Load X API credentials. Data collection uses bearer token only (read-only)."""
    bearer = os.getenv("X_BEARER_TOKEN")
    if not bearer:
        raise SystemExit("Missing required credential: X_BEARER_TOKEN")
    os.environ["X_BEARER_TOKEN"] = bearer
    # x-cli also needs app credentials for some endpoints
    for key in ("X_API_KEY", "X_API_SECRET"):
        val = os.getenv(key)
        if val:
            os.environ[key] = val


def run_json(cmd: list[str], retries: int = 2):
    for attempt in range(retries + 1):
        p = subprocess.run(cmd, capture_output=True, text=True)
        if p.returncode == 0:
            return json.loads(p.stdout)

        # Rate-limit handling from x-cli runtime error string
        m = re.search(r"Resets at (\d+)", p.stderr)
        if m and attempt < retries:
            reset_ts = int(m.group(1))
            sleep_for = max(1, reset_ts - int(time.time()) + 1)
            print(f"rate limited; sleeping {sleep_for}s", flush=True)
            time.sleep(sleep_for)
            continue

        raise RuntimeError(f"Command failed: {' '.join(cmd)}\nSTDERR:\n{p.stderr}")


def main() -> None:
    load_credential_mapping()

    snapshot = {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "accounts": {},
    }

    for handle in ACCOUNTS:
        profile = run_json(["x-cli", "-j", "user", "get", handle])
        timeline = run_json(["x-cli", "-j", "user", "timeline", handle, "--max", str(MAX_TIMELINE)])
        snapshot["accounts"][handle] = {
            "profile": profile,
            "timeline": timeline,
        }

    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    out = DATA / f"snapshot-{stamp}.json"
    out.write_text(json.dumps(snapshot, indent=2))

    latest = DATA / "latest.json"
    latest.write_text(json.dumps(snapshot, indent=2))

    print(str(out))


if __name__ == "__main__":
    main()
