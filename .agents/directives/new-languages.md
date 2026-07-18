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
   - Same title and intro paragraph (translated).
   - Same "Contenido"/"Contents" section with anchor links to each category (translated, including anchors in the corresponding Markdown format).
   - Same 8 macro-categories, in the same order, with the same thematic emoji.
   - Same bold subgroups within each category, in the same order.
   - Same tools, in the same order, within each subgroup/category.

2. **Translate, don't summarize or expand**: each description must be faithfully translated into the target language, keeping the same level of detail (one line) as the existing versions. Don't omit tools or add tools that don't exist in `README.md`.

3. **Don't translate**: tool proper names, URLs, and brand/technology names (e.g. "React", "WebGPU", "Zustand").

4. **Completeness check**: the new file must have the same number of categories, subgroups, and entries as `README.md`. If `README.md` is updated afterward (new tool or category), every language file — including the new one — must be updated in the same change (see `add-links.md`).

5. **Future maintenance**: once created, the new `README-<CODE>.md` becomes part of the set of README files that must stay in sync on every future change (adding tools, categories, or restructuring).

## Example of a translated header (French)

```markdown
# my awesome

Ceci est une liste de recommandations personnelles pour l'utilisation de certains outils au quotidien ou dans des institutions spécifiques. Les outils sont organisés par catégories pour faciliter leur recherche et leur utilisation.

## Contenu

- [🤖 IA et Automatisation](#-ia-et-automatisation)
- [💻 Développement Web](#-developpement-web)
...
```
