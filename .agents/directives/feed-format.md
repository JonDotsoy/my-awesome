# Directive: feeds/ (anuncios estilo X)

Instrucciones para agentes que agreguen anuncios de nuevas herramientas en `feeds/`, el registro de publicaciones estilo X (Twitter) de "my awesome".

## Estructura

Una carpeta por publicación, no un archivo único que crece indefinidamente:

```
feeds/
  <slug>/
    es.md
    en.md
    pt.md
```

- `<slug>`: nombre de la herramienta en kebab-case, minúsculas, sin espacios ni acentos (ej. `namethatui`, `magic-ui`).
- Un archivo por idioma dentro de la carpeta, con el mismo conjunto de idiomas que los README (`es`, `en`, `pt`, y cualquier código adicional de `new-languages.md`).
- Cada archivo `<idioma>.md` contiene **únicamente** el bloque del post (sin encabezado `# Feed`, sin separadores `---` — esos ya no aplican porque cada publicación vive en su propia carpeta).

## Cuándo crear una entrada

Cada vez que se agregue una nueva herramienta a los README (ver `add-links.md`), crear la carpeta `feeds/<slug>/` con un archivo por idioma.

## Formato del post (estilo B: pregunta/gancho)

```markdown
¿<Pregunta o gancho relatable sobre el problema que resuelve la herramienta>? 🤔

Con **<Nombre de la herramienta>** <beneficio concreto en una frase>.

🔗 <URL>
```

- **Gancho**: una pregunta corta y relatable que conecte con el problema que resuelve la herramienta. Debe terminar en `?` y puede llevar un emoji de cierre (ej. 🤔).
- **Cuerpo**: una sola frase, con el nombre de la herramienta en negrita, explicando el beneficio concreto (no repitas la descripción textual del README; reformúlala en tono conversacional).
- **Link**: precedido por 🔗, en su propia línea. La URL es idéntica en todos los idiomas.
- **Sin hashtags**: el post no debe incluir hashtags (`#tag`).
- **Límite de 280 caracteres**: el post completo (gancho + cuerpo + link) no debe superar los 280 caracteres, contando la URL tal cual aparece en el texto.
- No usar el formato "🆕 Se agregó X a la lista..." (estilo A, descartado) ni formatos tipo changelog/lista.

## Sincronización multi-idioma (obligatorio)

- Cada publicación nueva debe tener su archivo en todos los idiomas soportados (`es.md`, `en.md`, `pt.md`, y cualquier `<CODE>.md` adicional).
- Solo se traduce el texto (gancho, cuerpo); la URL y el nombre de la herramienta permanecen iguales.
- `es.md` es la fuente de verdad del contenido a traducir (mismo criterio que `README.md` para los README).

## Linter

Después de crear o modificar cualquier `feeds/<slug>/<idioma>.md`, ejecutar:

```bash
node scripts/lint-feeds.js
```

Valida que cada carpeta `feeds/<slug>/` tenga los idiomas requeridos, que cada post respete el límite de 280 caracteres (contando la URL) y que no contenga hashtags. El comando debe salir con código `0` antes de dar por terminado el cambio.

## Ejemplo

`feeds/namethatui/es.md`:
```markdown
¿Viste un componente en un sitio y no sabías cómo se llamaba? 🤔

Con **NameThatUI** encuentras el nombre exacto de patrones UI reales, catalogados y buscables.

🔗 https://namethatui.com/
```

`feeds/namethatui/en.md`:
```markdown
Ever seen a UI component on a site and had no idea what it's called? 🤔

With **NameThatUI** you find the exact name of real UI patterns, catalogued and searchable.

🔗 https://namethatui.com/
```
