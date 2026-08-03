# Directive: Adding new links (tools)

Instructions for agents adding a new tool to "my awesome".

## Current structure

The READMEs (`README.md`, `README-EN.md`, `README-PT.md`) organize tools into **8 macro-categories** (`##`):

1. 🤖 IA y Automatización
2. 💻 Desarrollo Web
3. 🖥️ Infraestructura y Código
4. 💰 Finanzas
5. 🚀 Productividad y Comunicación
6. 🎬 Contenido y Diseño
7. 📚 Aprendizaje y Carrera
8. 🔗 Relacionado

Some macro-categories are split into **bold thematic subgroups** (no `#`), for example within "🤖 IA y Automatización": **Agentes y desarrollo asistido por IA**, **Comparadores de LLMs**, **Automatización de procesos**. Not every category uses subgroups (e.g. "💰 Finanzas" doesn't).

## Steps to add a tool

1. **Verify the tool**: search the internet for up-to-date information to confirm it's still active, that the URL is correct, and to understand what it does.

2. **Choose the category and subgroup**:
   - Find the most suitable macro-category among the 8 existing ones.
   - If that category has subgroups, pick the right thematic subgroup; if none fits, a new bold subgroup can be created within the category.
   - Only create a **new macro-category** (`##`) if the tool doesn't reasonably fit any of the 8 existing ones. In that case:
     - Choose an appropriate thematic emoji (see examples in `awesome-list-format.md`).
     - Add the new entry to the "Contenido"/"Contents" index in all README files.
     - Keep a logical order between categories.

3. **Entry format** — a single line, no long paragraphs:
   ```markdown
   - [Tool Name](URL) - Brief description of what it is and what it's useful for.
   ```
   - One sentence. Avoid the old-style long descriptions ("It's especially useful for...").
   - Include what the tool is and its main value, with no filler.

4. **Multi-language sync (mandatory)**: add the entry to **every** README file in the project (`README.md`, `README-EN.md`, `README-PT.md`, and any additional `README-<CODE>.md`), translating the description into each language. The entry must stay in the same category/subgroup and in the same relative position across all files.

5. **Order within the subgroup**: append the new tool at the end of the corresponding subgroup or category, unless there's a clear reason to place it elsewhere (e.g. grouping very similar tools together).

6. **Feed announcement (mandatory)**: create a `feeds/<slug>/` folder with one X-style post per language (`es.md`, `en.md`, `pt.md`, and any additional `feed-<CODE>.md` language), following [`feed-format.md`](feed-format.md).

## Example

✅ Correct:
```markdown
- [Fintoc.me](https://fintoc.me/) - Comparte datos de transferencia bancaria en Chile mediante una URL simple.
```

❌ Avoid (too long, old style):
```markdown
- [Fintoc.me](https://fintoc.me/) - Esta herramienta es perfecta para compartir la información de datos de transferencia bancaria sin tener que enviarla de manera indirecta. En Chile, para hacer una transferencia a una cuenta bancaria de otra persona se necesita demasiada información...
```

❌ Avoid (too short, no usage context):
```markdown
- [Fintoc.me](https://fintoc.me/) - App de transferencias.
```
