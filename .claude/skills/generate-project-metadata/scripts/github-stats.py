#!/usr/bin/env python3
"""Capture GitHub stats for a repository and print the YAML fragment used by
metadata/<id>.yaml (`repository`-derived fields, `license`, `stats`, ...).

Usage:
  python3 github-stats.py <owner/repo | https://github.com/owner/repo> [--json]
  python3 github-stats.py --from-fixture repo.json [--json]   # offline testing

Stdlib only. Uses GITHUB_TOKEN / GH_TOKEN when set (higher rate limits).
Exit codes: 0 ok, 1 usage/parse error, 2 API/network error.
"""
import datetime
import json
import os
import re
import sys
import urllib.error
import urllib.request

API = "https://api.github.com"
# License ids that are OSI-approved permissive / copyleft, for a license_type hint.
PERMISSIVE = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "0BSD", "Unlicense", "MIT-0"}
COPYLEFT = {"GPL-2.0", "GPL-3.0", "AGPL-3.0", "LGPL-2.1", "LGPL-3.0", "MPL-2.0", "EUPL-1.2"}


def parse_repo(arg):
    m = re.match(r"^(?:https?://github\.com/)?([\w.-]+)/([\w.-]+?)(?:\.git)?/?$", arg.strip())
    if not m:
        raise ValueError(f"cannot parse repository from {arg!r}")
    return m.group(1), m.group(2)


def get(path, token=None, raw_headers=False):
    req = urllib.request.Request(
        API + path,
        headers={"Accept": "application/vnd.github+json", "User-Agent": "my-awesome-metadata"},
    )
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=20) as r:
        body = json.load(r)
        return (body, r.headers) if raw_headers else body


def count_from_link(headers):
    """With per_page=1 the `last` page number in the Link header is the item count."""
    m = re.search(r'[?&]page=(\d+)>; rel="last"', headers.get("Link", ""))
    return int(m.group(1)) if m else None


def collect(owner, repo, token=None):
    r = get(f"/repos/{owner}/{repo}", token)
    out = {"repo": r}
    try:
        out["open_prs"] = get(f"/search/issues?q=repo:{owner}/{repo}+type:pr+state:open&per_page=1", token)["total_count"]
    except urllib.error.HTTPError:
        out["open_prs"] = None
    try:
        _, h = get(f"/repos/{owner}/{repo}/commits?per_page=1", token, raw_headers=True)
        out["commits"] = count_from_link(h)
    except urllib.error.HTTPError:
        out["commits"] = None
    try:
        out["release"] = get(f"/repos/{owner}/{repo}/releases/latest", token)
    except urllib.error.HTTPError:
        out["release"] = None  # 404 = no releases
    return out


def summarize(data, today=None):
    r = data["repo"]
    today = today or datetime.date.today().isoformat()
    lic = (r.get("license") or {}).get("spdx_id")
    if lic in (None, "NOASSERTION"):
        lic_type = None
    elif lic in PERMISSIVE:
        lic_type = "permissive"
    elif lic in COPYLEFT:
        lic_type = "copyleft"
    else:
        lic_type = None
    rel = data.get("release")
    # GitHub's open_issues_count includes open PRs; subtract when we know the PR count.
    issues = r.get("open_issues_count")
    if issues is not None and data.get("open_prs") is not None:
        issues = max(issues - data["open_prs"], 0)
    return {
        "repository": {
            "host": "github.com",
            "owner": r["owner"]["login"],
            "name": r["name"],
            "kind": "git",
            "url": r["html_url"],
        },
        "description": r.get("description"),
        "homepage": r.get("homepage") or None,
        "license": lic if lic != "NOASSERTION" else None,
        "license_type": lic_type,  # null => classify manually (fair-code, source-available, ...)
        "language": r.get("language"),
        "topics_upstream": r.get("topics", []),
        "stats": {
            "stars": r.get("stargazers_count"),
            "forks": r.get("forks_count"),
            "watchers": r.get("subscribers_count"),
            "open_issues": issues,
            "open_pull_requests": data.get("open_prs"),
            "commits": data.get("commits"),
            "latest_release": rel["tag_name"] if rel else None,
            "last_commit_at": r.get("pushed_at"),
            "archived": r.get("archived"),
            "captured_at": today,
        },
        "sources": [{"url": r["html_url"], "kind": "github-api", "fetched_at": today}],
    }


def scalar(v):
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
        return s
    return json.dumps(s, ensure_ascii=False)  # JSON strings are valid YAML


def to_yaml(obj, indent=0):
    pad, lines = "  " * indent, []
    for k, v in obj.items():
        if isinstance(v, dict):
            lines.append(f"{pad}{k}:")
            lines.extend(to_yaml(v, indent + 1))
        elif isinstance(v, list) and v and isinstance(v[0], dict):
            lines.append(f"{pad}{k}:")
            for item in v:
                first, *rest = to_yaml(item, indent + 2)
                lines.append(f"{pad}  - {first.strip()}")
                lines.extend(rest)
        elif isinstance(v, list):
            lines.append(f"{pad}{k}: [{', '.join(scalar(x) for x in v)}]")
        else:
            lines.append(f"{pad}{k}: {scalar(v)}")
    return lines


def main(argv):
    as_json = "--json" in argv
    args = [a for a in argv if a != "--json"]
    try:
        if args[:1] == ["--from-fixture"] and len(args) == 2:
            data = json.load(open(args[1]))
        elif len(args) == 1:
            owner, repo = parse_repo(args[0])
            token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
            data = collect(owner, repo, token)
        else:
            print(__doc__)
            return 1
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    except (urllib.error.URLError, OSError) as e:
        print(f"error: GitHub API request failed: {e}", file=sys.stderr)
        return 2
    summary = summarize(data)
    print(json.dumps(summary, indent=2, ensure_ascii=False) if as_json else "\n".join(to_yaml(summary)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
