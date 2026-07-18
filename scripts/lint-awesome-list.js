#!/usr/bin/env node
"use strict";

/**
 * Lints every README*.md file in the repo root against the format
 * described in .agents/directives/awesome-list-format.md.
 *
 * Usage: node scripts/lint-awesome-list.js
 */

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");

// Re-implementation of GitHub's heading-to-anchor algorithm: strip Latin
// diacritics, drop anything outside [a-zA-Z0-9 -] (this removes emoji and
// punctuation), lowercase, spaces -> hyphens. A heading starting with an
// emoji keeps a leading hyphen because the emoji is dropped but the space
// that followed it is not.
function githubSlug(headingText) {
  const stripped = headingText.normalize("NFD").replace(/[̀-ͯ]/g, "");
  const withoutSymbols = Array.from(stripped)
    .map((ch) => (/[a-zA-Z0-9 -]/.test(ch) ? ch : ""))
    .join("");
  return withoutSymbols.toLowerCase().replace(/ /g, "-");
}

function findReadmeFiles() {
  return fs
    .readdirSync(ROOT)
    .filter((f) => /^README(-[A-Z]{2}(-[A-Z]{2})?)?\.md$/.test(f))
    .sort();
}

const ENTRY_RE = /^- \[(.+?)\]\((\S+)\) - (.+)$/;
const SUBGROUP_RE = /^\*\*(.+)\*\*$/;
const HEADING2_RE = /^## (.+)$/;
const HEADING1_RE = /^# (.+)$/;
const INDEX_LINK_RE = /^- \[(.+?)\]\(#(.+?)\)$/;

function parseFile(file) {
  const content = fs.readFileSync(path.join(ROOT, file), "utf8");
  const lines = content.split("\n");

  const errors = [];
  let title = null;
  let indexLinks = null; // [{text, anchor, lineNo}]
  const categories = []; // [{emoji, name, heading, anchor, lineNo, subgroups:[], entries:[]}]

  let mode = "before-title"; // before-title | before-index | in-index | in-body
  let currentCategory = null;
  let currentBucket = null; // entries array currently being filled (category.entries or subgroup.entries)

  lines.forEach((line, i) => {
    const lineNo = i + 1;
    const trimmed = line.trim();

    if (mode === "before-title") {
      if (trimmed === "") return;
      const m = trimmed.match(HEADING1_RE);
      if (m) {
        title = m[1];
        mode = "before-index";
      } else {
        errors.push(`${file}:${lineNo}: expected the file to start with "# <title>", found "${trimmed}"`);
        mode = "before-index";
      }
      return;
    }

    const h2 = trimmed.match(HEADING2_RE);

    if (mode === "before-index") {
      if (trimmed === "") return;
      if (h2) {
        indexLinks = [];
        mode = "in-index";
        return;
      }
      // intro paragraph text, ignore
      return;
    }

    if (mode === "in-index") {
      if (trimmed === "") return;
      const linkMatch = trimmed.match(INDEX_LINK_RE);
      if (linkMatch) {
        indexLinks.push({ text: linkMatch[1], anchor: linkMatch[2], lineNo });
        return;
      }
      if (h2) {
        // index section ended, this is the first category
        mode = "in-body";
        openCategory(h2[1], lineNo);
        return;
      }
      errors.push(`${file}:${lineNo}: expected an index bullet link "- [Name](#anchor)", found "${trimmed}"`);
      return;
    }

    // mode === in-body
    if (trimmed === "") return;

    if (h2) {
      openCategory(h2[1], lineNo);
      return;
    }

    const subgroupMatch = trimmed.match(SUBGROUP_RE);
    if (subgroupMatch && !trimmed.includes("](")) {
      if (!currentCategory) {
        errors.push(`${file}:${lineNo}: subgroup found outside of any category`);
        return;
      }
      const subgroup = { name: subgroupMatch[1], lineNo, entries: [] };
      currentCategory.subgroups.push(subgroup);
      currentBucket = subgroup.entries;
      return;
    }

    const entryMatch = trimmed.match(ENTRY_RE);
    if (entryMatch) {
      if (!currentCategory) {
        errors.push(`${file}:${lineNo}: entry found outside of any category`);
        return;
      }
      const [raw, name, url, desc] = entryMatch;
      if (!/^https?:\/\//.test(url)) {
        errors.push(`${file}:${lineNo}: entry "${name}" URL must be absolute http(s), got "${url}"`);
      }
      if (!desc.endsWith(".")) {
        errors.push(`${file}:${lineNo}: entry "${name}" description must end with a period`);
      }
      if ((desc.match(/\. /g) || []).length > 0) {
        errors.push(`${file}:${lineNo}: entry "${name}" description looks like more than one sentence`);
      }
      currentBucket.push({ name, url, desc, lineNo, raw: trimmed });
      return;
    }

    errors.push(`${file}:${lineNo}: unexpected line inside body (not a heading, subgroup, or entry): "${trimmed}"`);

    function openCategory(headingText, ln) {
      const spaceIdx = headingText.indexOf(" ");
      const emoji = spaceIdx === -1 ? "" : headingText.slice(0, spaceIdx);
      const name = spaceIdx === -1 ? headingText : headingText.slice(spaceIdx + 1);
      if (!emoji) {
        errors.push(`${file}:${ln}: category heading "${headingText}" must start with an emoji followed by a space`);
      }
      currentCategory = {
        emoji,
        name,
        heading: headingText,
        anchor: githubSlug(headingText),
        lineNo: ln,
        subgroups: [],
        entries: [],
      };
      currentBucket = currentCategory.entries;
      categories.push(currentCategory);
    }
  });

  // Validate index <-> category consistency
  if (indexLinks) {
    if (indexLinks.length !== categories.length) {
      errors.push(
        `${file}: index has ${indexLinks.length} entries but there are ${categories.length} category headings`
      );
    }
    indexLinks.forEach((link, idx) => {
      const cat = categories[idx];
      if (!cat) return;
      if (link.text !== cat.heading) {
        errors.push(
          `${file}:${link.lineNo}: index entry "${link.text}" does not match category heading "${cat.heading}"`
        );
      }
      if (link.anchor !== cat.anchor) {
        errors.push(
          `${file}:${link.lineNo}: index anchor "#${link.anchor}" does not match generated anchor "#${cat.anchor}" for "${cat.heading}"`
        );
      }
    });
  } else {
    errors.push(`${file}: no index section found (expected a "## Contenido/Contents/..." section right after the intro)`);
  }

  return { file, title, indexLinks, categories, errors };
}

function flattenUrls(parsed) {
  const urls = [];
  for (const cat of parsed.categories) {
    for (const e of cat.entries) urls.push(e.url);
    for (const sg of cat.subgroups) {
      for (const e of sg.entries) urls.push(e.url);
    }
  }
  return urls;
}

function crossFileChecks(parsedFiles) {
  const errors = [];
  if (parsedFiles.length < 2) return errors;

  const base = parsedFiles[0];
  const baseUrls = flattenUrls(base);

  for (const other of parsedFiles.slice(1)) {
    if (other.title !== base.title) {
      errors.push(`${other.file}: title "${other.title}" differs from ${base.file} title "${base.title}"`);
    }

    if (other.categories.length !== base.categories.length) {
      errors.push(
        `${other.file}: has ${other.categories.length} categories, expected ${base.categories.length} (matching ${base.file})`
      );
    }

    const len = Math.min(other.categories.length, base.categories.length);
    for (let i = 0; i < len; i++) {
      const a = base.categories[i];
      const b = other.categories[i];
      if (a.emoji !== b.emoji) {
        errors.push(
          `${other.file}: category #${i + 1} emoji "${b.emoji}" differs from ${base.file} emoji "${a.emoji}"`
        );
      }
      if (a.subgroups.length !== b.subgroups.length) {
        errors.push(
          `${other.file}: category "${b.heading}" has ${b.subgroups.length} subgroups, expected ${a.subgroups.length} (matching "${a.heading}" in ${base.file})`
        );
      }
      if (a.entries.length !== b.entries.length) {
        errors.push(
          `${other.file}: category "${b.heading}" has ${b.entries.length} direct entries, expected ${a.entries.length}`
        );
      }
      const sgLen = Math.min(a.subgroups.length, b.subgroups.length);
      for (let j = 0; j < sgLen; j++) {
        if (a.subgroups[j].entries.length !== b.subgroups[j].entries.length) {
          errors.push(
            `${other.file}: subgroup "${b.subgroups[j].name}" (category "${b.heading}") has ${b.subgroups[j].entries.length} entries, expected ${a.subgroups[j].entries.length}`
          );
        }
      }
    }

    const otherUrls = flattenUrls(other);
    if (otherUrls.length === baseUrls.length) {
      for (let i = 0; i < otherUrls.length; i++) {
        if (otherUrls[i] !== baseUrls[i]) {
          errors.push(
            `${other.file}: tool #${i + 1} URL "${otherUrls[i]}" does not match ${base.file} URL "${baseUrls[i]}" at the same position`
          );
        }
      }
    } else {
      const missing = baseUrls.filter((u) => !otherUrls.includes(u));
      const extra = otherUrls.filter((u) => !baseUrls.includes(u));
      if (missing.length) errors.push(`${other.file}: missing tools present in ${base.file}: ${missing.join(", ")}`);
      if (extra.length) errors.push(`${other.file}: has tools not present in ${base.file}: ${extra.join(", ")}`);
    }
  }

  return errors;
}

function main() {
  const files = findReadmeFiles();
  if (files.length === 0) {
    console.error("No README*.md files found in repo root.");
    process.exit(1);
  }

  const parsedFiles = files.map(parseFile);
  const allErrors = [];
  for (const p of parsedFiles) allErrors.push(...p.errors);
  allErrors.push(...crossFileChecks(parsedFiles));

  if (allErrors.length > 0) {
    console.error(`✖ ${allErrors.length} issue(s) found:\n`);
    for (const err of allErrors) console.error(`  - ${err}`);
    process.exit(1);
  }

  console.log(`✔ ${files.length} README file(s) checked, no issues found: ${files.join(", ")}`);
}

main();
