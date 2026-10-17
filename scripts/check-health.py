#!/usr/bin/env python3
"""Checks the health URL of every metadata/*.yaml.

Uses `health_url` when set; otherwise falls back to `url_canonical`.
Usage: python3 scripts/check-health.py [file.yaml ...]
Requires PyYAML. Exit code 0 = all healthy, 1 = at least one failed.
"""
import sys
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TIMEOUT = 20
HEADERS = {"User-Agent": "my-awesome-health-check (+https://github.com/JonDotsoy/my-awesome)"}


def fetch(url, method):
    req = urllib.request.Request(url, method=method, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return r.status


def check(url):
    """Return (ok, detail). Retries with GET when HEAD is rejected."""
    last = ""
    for method in ("HEAD", "GET"):
        try:
            status = fetch(url, method)
            return True, f"{status}"
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}"
            if method == "HEAD" and e.code in (400, 403, 405, 501):
                continue
            return False, last
        except Exception as e:  # DNS, TLS, timeout, ...
            last = f"{type(e).__name__}: {e}"
    return False, last


def main(argv):
    files = [Path(a) for a in argv] or sorted((ROOT / "metadata").glob("*.yaml"))
    failed = 0
    for f in files:
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        url = data.get("health_url")
        source = "health_url"
        if not url:
            url, source = data.get("url_canonical"), "url_canonical"
        if not url:
            print(f"::warning file={f}::no health_url or url_canonical")
            continue
        ok, detail = check(url)
        if ok:
            print(f"✔ {data['id']}: {url} ({source}) {detail}")
        else:
            failed += 1
            print(f"::error file={f}::{data['id']} unhealthy: {url} ({source}) {detail}")
    print(f"\n{len(files) - failed} of {len(files)} healthy")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
