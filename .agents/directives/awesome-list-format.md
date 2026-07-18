# Directive: Awesome list format

Canonical Markdown format that every `README*.md` file in this project must follow. `add-links.md` and `new-languages.md` build on top of these rules — when in doubt about formatting, this file wins.

Compliance is checked automatically by the linter: `node scripts/lint-awesome-list.js`. Run it after any change to a README file.

## File structure

Each `README*.md` file must contain, in this order:

1. **Title**: a single `# my awesome` H1 — identical and untranslated in every language file.
2. **Intro paragraph**: one paragraph right after the title, translated per language.
3. **Index section**: one `## ` heading (`Contenido` / `Contents` / `Conteúdo` / equivalent) followed only by bullet links, one per macro-category, in the same order the categories appear below, each pointing to `#<anchor>` of its category heading.
4. **Categories**: one `## <emoji> <Name>` heading per macro-category, in the same order as the index, and nothing else at heading level (no `###`).

## Category heading rules

- Format: `## <emoji><space><Name>` — must start with exactly one thematic emoji followed by a space and the category name.
- The anchor generated from the heading text (GitHub slug rules: strip diacritics, drop any character outside `[a-z0-9 -]`, lowercase, spaces → hyphens) must match the `#anchor` used by its link in the index.

## Subgroup rules (optional, within a category)

- A subgroup is a standalone line `**Subgroup Name**` — bold text alone on its own line, no heading marker, no trailing colon, no other inline formatting.
- It must be immediately followed by one or more bullet entries before the next subgroup or the next category.
- Not every category needs subgroups; entries can sit directly under the category heading.

## Entry format

```markdown
- [Tool Name](https://example.com/) - One-sentence description of what it is and why it's useful.
```

- One list item per line — never split an entry across multiple lines.
- The link target must be an absolute URL (`http://` or `https://`).
- The description follows `) - ` and must end with a period.
- The description must be a single sentence — no multi-sentence or multi-paragraph descriptions (see `add-links.md` for the reasoning and examples).

## Cross-file consistency

All `README*.md` files (`README.md`, `README-EN.md`, `README-PT.md`, and any future `README-<CODE>.md`) must match structurally:

- Same number of categories, in the same order, with the same emojis.
- Same number of subgroups, in the same order, within each category.
- Same set of tool URLs, in the same order, within each category/subgroup — only the visible name and description are translated, the underlying list of tools must be identical.

## Running the linter

```bash
node scripts/lint-awesome-list.js
```

Exits with a non-zero status and prints one message per violation if any rule above is broken, in any file. A clean run prints a summary and exits `0`.
