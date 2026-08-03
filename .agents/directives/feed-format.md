# Directive: feed-format.md (anuncios estilo X en feed-*.md)

Instrucciones para agentes que agreguen entradas a los archivos `feed-<idioma>.md` (`feed-es.md`, `feed-en.md`, `feed-pt.md`, y cualquier `feed-<CODE>.md` adicional siguiendo los idiomas de `new-languages.md`), el registro de cambios del proyecto en formato de post tipo X (Twitter).

## Cuándo actualizar

Cada vez que se agregue una nueva herramienta a los README (ver `add-links.md`), se debe agregar una entrada correspondiente en **todos** los `feed-<idioma>.md` existentes, traducida a cada idioma.

## Formato de la entrada (estilo B: pregunta/gancho)

```markdown
¿<Pregunta o gancho relatable sobre el problema que resuelve la herramienta>? 🤔

Con **<Nombre de la herramienta>** <beneficio concreto en una frase>.

🔗 <URL>

#myawesome #<tag relevante 1> #<tag relevante 2>
```

- **Gancho**: una pregunta corta y relatable que conecte con el problema que resuelve la herramienta. Debe terminar en `?` y puede llevar un emoji de cierre (ej. 🤔).
- **Cuerpo**: una sola frase, con el nombre de la herramienta en negrita, explicando el beneficio concreto (no repitas la descripción textual del README; reformúlala en tono conversacional).
- **Link**: precedido por 🔗, en su propia línea. La URL es idéntica en todos los idiomas.
- **Hashtags**: siempre incluir `#myawesome`, más 1-2 hashtags relevantes al tema de la herramienta (ej. `#UI`, `#frontend`, `#finanzas`, `#productividad`). Los hashtags no se traducen, se mantienen iguales entre idiomas.
- No usar el formato "🆕 Se agregó X a la lista..." (estilo A, descartado) ni formatos tipo changelog/lista.

## Sincronización multi-idioma (obligatorio)

- Cada entrada nueva debe agregarse en `feed-es.md`, `feed-en.md`, `feed-pt.md` y cualquier `feed-<CODE>.md` adicional, en el mismo orden relativo en todos los archivos.
- Solo se traduce el texto (gancho, cuerpo, hashtags si aplica); la URL y el nombre de la herramienta permanecen iguales.
- `feed-es.md` es la fuente de verdad del contenido a traducir (mismo criterio que `README.md` para los README).

## Dónde agregar la entrada

- Agregar la nueva entrada **al final** del archivo, después de la última entrada existente (no sobrescribir entradas anteriores).
- Separar cada entrada de la siguiente con una línea `---`.

## Ejemplo

`feed-es.md`:
```markdown
¿Viste un componente en un sitio y no sabías cómo se llamaba? 🤔

Con **NameThatUI** encuentras el nombre exacto de patrones UI reales, catalogados y buscables.

🔗 https://namethatui.com/

#myawesome #UI #frontend
```

`feed-en.md`:
```markdown
Ever seen a UI component on a site and had no idea what it's called? 🤔

With **NameThatUI** you find the exact name of real UI patterns, catalogued and searchable.

🔗 https://namethatui.com/

#myawesome #UI #frontend
```
