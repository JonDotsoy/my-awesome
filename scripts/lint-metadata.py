#!/usr/bin/env python3
"""Validates metadata/*.yaml against the schema documented in
.claude/skills/generate-project-metadata/SKILL.md and cross-checks each file
against README*.md (the project must be listed there).

Usage: python3 scripts/lint-metadata.py [file.yaml ...]
Requires PyYAML. Exit code 0 = ok, 1 = problems found.
"""
import datetime
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = [
    "schema_version", "id", "name", "url", "url_canonical", "readme",
    "segment", "labels", "summary", "sources",
]
ENTRY_RE = re.compile(r"^- \[(?P<name>[^\]]+)\]\((?P<url>[^)]+)\) - (?P<desc>.+)$")
LICENSE_TYPES = {"permissive", "copyleft", "fair-code", "source-available", "proprietary"}


def readme_entries(path):
    """Return {url: (category, subgroup, description)} for a README file."""
    out, cat, sub = {}, None, None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            cat, sub = line[3:].strip(), None
        elif re.fullmatch(r"\*\*.+\*\*", line.strip()):
            sub = line.strip().strip("*")
        else:
            m = ENTRY_RE.match(line)
            if m:
                out[m["url"].strip()] = (cat, sub, m["desc"].strip())
    return out


def load_readmes():
    files = {"es": ROOT / "README.md"}
    for p in sorted(ROOT.glob("README-*.md")):
        files[p.stem.split("-", 1)[1].lower()] = p
    return {lang: readme_entries(p) for lang, p in files.items()}


def is_http_url(v):
    u = urlparse(v) if isinstance(v, str) else None
    return bool(u and u.scheme in ("http", "https") and u.netloc)


def lint(path, readmes):
    errs = []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        return [f"invalid YAML: {e}"]
    if not isinstance(data, dict):
        return ["top level must be a mapping"]

    for k in REQUIRED:
        if k not in data:
            errs.append(f"missing required key: {k}")
    if errs:
        return errs

    if data["id"] != path.stem:
        errs.append(f"id '{data['id']}' must match filename '{path.stem}'")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", str(data["id"])):
        errs.append("id must be lowercase kebab-case")
    for k in ("url", "url_canonical"):
        if not is_http_url(data[k]):
            errs.append(f"{k} must be an http(s) URL")
    for k in ("homepage", "docs_url"):
        if data.get(k) is not None and not is_http_url(data[k]):
            errs.append(f"{k} must be null or an http(s) URL")
    if not isinstance(data["labels"], list) or not data["labels"] or not all(
        isinstance(x, str) and re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", x) for x in data["labels"]
    ):
        errs.append("labels must be a non-empty list of kebab-case strings")
    if not isinstance(data["summary"], str) or not data["summary"].strip():
        errs.append("summary must be a non-empty string")
    if not isinstance(data["sources"], list) or not data["sources"]:
        errs.append("sources must be a non-empty list")
    else:
        for i, s in enumerate(data["sources"]):
            if not isinstance(s, dict) or not is_http_url(s.get("url")):
                errs.append(f"sources[{i}].url must be an http(s) URL")
            elif not isinstance(s.get("fetched_at"), (datetime.date, datetime.datetime)):
                errs.append(f"sources[{i}].fetched_at must be a date (YYYY-MM-DD)")
    lt = data.get("license_type")
    if lt is not None and lt not in LICENSE_TYPES:
        errs.append(f"license_type must be null or one of {sorted(LICENSE_TYPES)}")
    elif lt is not None and "open_source" in data:
        if (lt in ("permissive", "copyleft")) != (data["open_source"] is True):
            errs.append(f"license_type '{lt}' is inconsistent with open_source: {data['open_source']}")
    if data.get("pricing_url") is not None and not is_http_url(data["pricing_url"]):
        errs.append("pricing_url must be null or an http(s) URL")
    stats = data.get("stats")
    if stats is not None:
        if not isinstance(stats.get("captured_at"), (datetime.date, datetime.datetime)):
            errs.append("stats.captured_at must be a date (YYYY-MM-DD)")
        for k, v in stats.items():
            if k in ("stars", "forks", "watchers", "open_issues", "open_pull_requests", "commits") and not (
                isinstance(v, int) and v >= 0
            ):
                errs.append(f"stats.{k} must be a non-negative integer")

    # README cross-check: the project must be listed (skill prerequisite).
    rd = data["readme"] if isinstance(data["readme"], dict) else {}
    es = readmes.get("es", {})
    entry = es.get(str(data["url"]).strip())
    if entry is None:
        errs.append(f"url {data['url']} is not listed in README.md (prerequisite)")
        return errs
    cat, sub, _ = entry
    if rd.get("category") != re.sub(r"^\S+\s+", "", cat):
        errs.append(f"readme.category '{rd.get('category')}' != README.md category '{cat}'")
    if rd.get("subgroup") != sub:
        errs.append(f"readme.subgroup '{rd.get('subgroup')}' != README.md subgroup '{sub}'")
    descs = rd.get("descriptions") or {}
    for lang, entries in readmes.items():
        e = entries.get(str(data["url"]).strip())
        if e is None:
            errs.append(f"url not listed in README for language '{lang}'")
        elif descs.get(lang) != e[2]:
            errs.append(f"readme.descriptions.{lang} differs from the README entry")
    return errs


def main(argv):
    files = [Path(a) for a in argv] or sorted((ROOT / "metadata").glob("*.yaml"))
    if not files:
        print("No metadata/*.yaml files found.")
        return 0
    readmes = load_readmes()
    bad = 0
    for f in files:
        errs = lint(f, readmes)
        for e in errs:
            print(f"{f}: {e}")
        bad += bool(errs)
    if bad:
        print(f"\n✖ {bad} of {len(files)} metadata file(s) have problems")
        return 1
    print(f"✔ {len(files)} metadata file(s) checked, no issues found")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
