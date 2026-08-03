# Directive: feed-es.md (anuncios estilo X)

Instrucciones para agentes que agreguen entradas a `feed-es.md`, el registro de cambios del proyecto en formato de post tipo X (Twitter).

## Cuándo actualizar

Cada vez que se agregue una nueva herramienta a los README (ver `add-links.md`), se debe agregar una entrada correspondiente en `feed-es.md`.

## Formato de la entrada (estilo B: pregunta/gancho)

```markdown
¿<Pregunta o gancho relatable sobre el problema que resuelve la herramienta>? 🤔

Con **<Nombre de la herramienta>** <beneficio concreto en una frase>.

🔗 <URL>

#myawesome #<tag relevante 1> #<tag relevante 2>
```

- **Gancho**: una pregunta corta y relatable que conecte con el problema que resuelve la herramienta. Debe terminar en `?` y puede llevar un emoji de cierre (ej. 🤔).
- **Cuerpo**: una sola frase, con el nombre de la herramienta en negrita, explicando el beneficio concreto (no repitas la descripción textual del README; reformúlala en tono conversacional).
- **Link**: precedido por 🔗, en su propia línea.
- **Hashtags**: siempre incluir `#myawesome`, más 1-2 hashtags relevantes al tema de la herramienta (ej. `#UI`, `#frontend`, `#finanzas`, `#productividad`).
- No usar el formato "🆕 Se agregó X a la lista..." (estilo A, descartado) ni formatos tipo changelog/lista.

## Dónde agregar la entrada

- Agregar la nueva entrada **al final** del archivo, después de la última entrada existente (no sobrescribir entradas anteriores).
- Separar cada entrada de la siguiente con una línea `---`.

## Ejemplo

```markdown
¿Viste un componente en un sitio y no sabías cómo se llamaba? 🤔

Con **NameThatUI** encuentras el nombre exacto de patrones UI reales, catalogados y buscables.

🔗 https://namethatui.com/

#myawesome #UI #frontend
```
