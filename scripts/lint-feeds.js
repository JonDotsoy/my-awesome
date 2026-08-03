#!/usr/bin/env node
"use strict";

/**
 * Lints every feeds/<slug>/<lang>.md file against the format described in
 * .agents/directives/feed-format.md.
 *
 * Usage: node scripts/lint-feeds.js
 */

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const FEEDS_DIR = path.join(ROOT, "feeds");
const MAX_LENGTH = 280;
const URL_RE = /https?:\/\/\S+/;
const HASHTAG_RE = /(^|\s)#\w/;

function requiredLanguages() {
  const readmes = fs.readdirSync(ROOT).filter((f) => /^README(-[A-Z]{2}(-[A-Z]{2})?)?\.md$/.test(f));
  const langs = ["es"]; // README.md itself
  for (const f of readmes) {
    const m = f.match(/^README-([A-Z]{2}(-[A-Z]{2})?)\.md$/);
    if (m) langs.push(m[1].toLowerCase());
  }
  return langs.sort();
}

function main() {
  const errors = [];

  if (!fs.existsSync(FEEDS_DIR)) {
    console.log("✔ no feeds/ directory found, nothing to check.");
    return;
  }

  const langs = requiredLanguages();
  const slugs = fs.readdirSync(FEEDS_DIR).filter((f) => fs.statSync(path.join(FEEDS_DIR, f)).isDirectory());

  for (const slug of slugs) {
    const slugDir = path.join(FEEDS_DIR, slug);
    const files = fs.readdirSync(slugDir).filter((f) => f.endsWith(".md"));
    const present = files.map((f) => f.replace(/\.md$/, ""));

    const missing = langs.filter((l) => !present.includes(l));
    if (missing.length) {
      errors.push(`feeds/${slug}: missing language file(s): ${missing.map((l) => `${l}.md`).join(", ")}`);
    }

    for (const file of files) {
      const rel = `feeds/${slug}/${file}`;
      const content = fs.readFileSync(path.join(slugDir, file), "utf8").trim();

      if (!URL_RE.test(content)) {
        errors.push(`${rel}: post must include an absolute http(s) URL`);
      }

      if (HASHTAG_RE.test(content)) {
        errors.push(`${rel}: post must not contain hashtags`);
      }

      if (content.length > MAX_LENGTH) {
        errors.push(`${rel}: post is ${content.length} characters, exceeds the ${MAX_LENGTH} character limit`);
      }
    }
  }

  if (errors.length > 0) {
    console.error(`✖ ${errors.length} issue(s) found:\n`);
    for (const err of errors) console.error(`  - ${err}`);
    process.exit(1);
  }

  console.log(`✔ ${slugs.length} feed folder(s) checked, no issues found.`);
}

main();
