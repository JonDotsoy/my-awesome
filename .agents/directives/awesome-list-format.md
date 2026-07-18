# Directive: Awesome list format

Canonical Markdown format that every `README*.md` file in this project must follow. `add-links.md` and `new-languages.md` build on top of these rules — when in doubt about formatting, this file wins.

Compliance is checked automatically by the linter: `node scripts/lint-awesome-list.js`. Run it after any change to a README file.

## File structure

Each `README*.md` file must contain, in this order:

1. **Title**: a single `# my awesome` H1 — identical and untranslated in every language file.
2. **Language menu**: one line right after the title, listing every `README*.md` in the project in the same fixed order (`README.md` first, then the rest alphabetically) separated by ` | `. The file you're currently in is rendered as `**Label**` (bold, no link); every other file is a link `[Label](Filename.md)`. The label text for a given language is identical across all files (e.g. `English` is always `English`, never translated per viewing file) — only bold-vs-link changes between files. See "Language menu rules" below.
3. **Intro paragraph**: one paragraph right after the language menu, translated per language.
4. **Index section**: one `## ` heading (`Contenido` / `Contents` / `Conteúdo` / equivalent) followed only by bullet links, one per macro-category, in the same order the categories appear below, each pointing to `#<anchor>` of its category heading.
5. **Categories**: one `## <emoji> <Name>` heading per macro-category, in the same order as the index, and nothing else at heading level (no `###`).

## Language menu rules

```markdown
**Español** | [English](README-EN.md) | [Português](README-PT.md)
```

- One item per existing `README*.md` file, in the same order in every file: `README.md` first, then the others in alphabetical filename order.
- Exactly one item is bold plain text (`**Label**`, no link) — the file you're currently reading. All other items are links pointing at the other files' exact filenames.
- The set of labels and link targets must be identical across all files; only which one is bold changes.
- When a new `README-<CODE>.md` is created, its entry must be added to the menu of every existing file (see `new-languages.md`).

## Category heading rules

- Format: `## <emoji><space><Name>` — must start with exactly one thematic emoji followed by a space and the category name.
- The anchor generated from the heading text (GitHub slug rules: strip diacritics, drop any character outside `[a-z0-9 -]`, lowercase, spaces → hyphens) must match the `#anchor` used by its link in the index.
- The emoji must be intuitive and visually represent the category's topic. Reuse an existing category's emoji when the topic overlaps; otherwise pick a new one that isn't already used by another category.

**Emojis currently in use:**

- 🤖 IA y Automatización
- 💻 Desarrollo Web
- 🖥️ Infraestructura y Código
- 💰 Finanzas
- 🚀 Productividad y Comunicación
- 🎬 Contenido y Diseño
- 📚 Aprendizaje y Carrera
- 🔗 Relacionado

This list grows as new categories are added — check the "Contenido"/"Contents" index of any README for the current, authoritative set before picking a new emoji.

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
