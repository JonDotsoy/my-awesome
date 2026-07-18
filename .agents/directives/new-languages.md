# Directive: Creating a new language

Instructions for agents adding a new complete translation of "my awesome".

## Current languages

- `README.md` - Spanish (main version, source of truth for structure)
- `README-EN.md` - English
- `README-PT.md` - Portuguese

## Naming convention

Additional language files follow this pattern:

```
README-<CODE>.md
```

- `<CODE>` is the uppercase language code, following ISO 639-1 (2 letters) when available: `README-FR.md` (French), `README-DE.md` (German), `README-IT.md` (Italian), etc.
- If the language needs to distinguish a regional variant, use the `README-<LANGUAGE>-<REGION>.md` pattern in uppercase (e.g. `README-PT-BR.md` if Brazilian and European Portuguese ever need to be split).

## Steps to create a new language

1. **Use `README.md` as the structural base**: the new file must mirror exactly the same structure as the Spanish version:
   - Same title, followed by the language menu (see step 2), followed by the intro paragraph (translated).
   - Same "Contenido"/"Contents" section with anchor links to each category (translated, including anchors in the corresponding Markdown format).
   - Same 8 macro-categories, in the same order, with the same thematic emoji.
   - Same bold subgroups within each category, in the same order.
   - Same tools, in the same order, within each subgroup/category.

2. **Add the language menu and update it everywhere**: right after the title, add the language menu line described in `awesome-list-format.md`. In the new file, its own entry is bold (`**Label**`); every other language is a link. Then go back and add a link to the new file in the menu of **every existing** `README*.md`, keeping the fixed order (`README.md` first, then the rest alphabetically) and identical labels across all files.

3. **Translate, don't summarize or expand**: each description must be faithfully translated into the target language, keeping the same level of detail (one line) as the existing versions. Don't omit tools or add tools that don't exist in `README.md`.

4. **Don't translate**: tool proper names, URLs, and brand/technology names (e.g. "React", "WebGPU", "Zustand"). Language menu labels use each language's endonym (native name), e.g. `Français`, `Deutsch`, `Italiano`.

5. **Completeness check**: the new file must have the same number of categories, subgroups, and entries as `README.md`. If `README.md` is updated afterward (new tool or category), every language file — including the new one — must be updated in the same change (see `add-links.md`).

6. **Future maintenance**: once created, the new `README-<CODE>.md` becomes part of the set of README files that must stay in sync on every future change (adding tools, categories, restructuring, or further new languages).

## Example of a translated header (French)

```markdown
# my awesome

[Español](README.md) | [English](README-EN.md) | **Français** | [Português](README-PT.md)

Ceci est une liste de recommandations personnelles pour l'utilisation de certains outils au quotidien ou dans des institutions spécifiques. Les outils sont organisés par catégories pour faciliter leur recherche et leur utilisation.

## Contenu

- [🤖 IA et Automatisation](#-ia-et-automatisation)
- [💻 Développement Web](#-developpement-web)
...
```
