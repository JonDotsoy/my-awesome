# AGENTS.md - Instructions for Agents

This document has instructions for agents that will help maintain and update the README files of "my awesome".

## Propósito del Proyecto

"my awesome" es una lista curada de recomendaciones personales de herramientas útiles para el día a día o instituciones específicas. Las herramientas se organizan por categorías para facilitar su búsqueda y uso.

**Este es un proyecto en crecimiento**: se pueden agregar nuevas categorías, subgrupos, herramientas e idiomas en cualquier momento según las necesidades y descubrimientos del usuario.

## Estructura de los Archivos README

El proyecto mantiene varios archivos README, uno por idioma:
- `README.md` - Versión en español (principal, fuente de verdad para la estructura)
- `README-EN.md` - Versión en inglés
- `README-PT.md` - Versión en portugués
- Cualquier `README-<CODE>.md` adicional creado siguiendo `new-languages.md`

**Importante**: todos los archivos README deben mantenerse sincronizados. Cuando se agrega o modifica una herramienta o categoría, debe actualizarse en todos los archivos con las traducciones correspondientes.

El formato exacto de estos archivos (estructura, emojis, categorías, subgrupos, formato de entradas) está definido en `.agents/directives/awesome-list-format.md` — no lo dupliques aquí, consulta esa directiva.

## Directivas Adicionales

Este archivo (`AGENTS.md`) es el punto de entrada único para las instrucciones de agentes. Las directivas detalladas para tareas específicas viven en `.agents/directives/` y deben consultarse desde aquí antes de ejecutar la tarea correspondiente:

- [`.agents/directives/awesome-list-format.md`](.agents/directives/awesome-list-format.md) - Especificación canónica del formato Markdown de los README (estructura, categorías, subgrupos, formato de entradas y consistencia entre idiomas). Consulta esta directiva primero.
- [`.agents/directives/add-links.md`](.agents/directives/add-links.md) - Cómo agregar una nueva herramienta: elección de categoría/subgrupo, formato de la entrada y sincronización multiidioma.
- [`.agents/directives/new-languages.md`](.agents/directives/new-languages.md) - Cómo crear un nuevo `README-<CODE>.md`: convención de nombres y cómo replicar la estructura desde `README.md`.
- [`.agents/directives/feed-format.md`](.agents/directives/feed-format.md) - Cómo crear un anuncio en `feeds/<slug>/` (una carpeta por publicación, un archivo por idioma) cada vez que se agrega una herramienta a los README.

No crear directivas nuevas fuera de `.agents/directives/` sin referenciarlas desde esta sección. No dupliques aquí lo que ya esté documentado en una directiva.

### Linter

Después de modificar cualquier `README*.md`, ejecutar:

```bash
node scripts/lint-awesome-list.js
```

Valida el cumplimiento de `awesome-list-format.md` (estructura, formato de entradas y sincronización entre archivos de idioma). El comando debe salir con código `0` antes de dar por terminado el cambio.

## Notas Importantes

- Siempre verificar que las URLs funcionen antes de agregarlas.
- Considerar el contexto local (por ejemplo, herramientas específicas para Chile) cuando sea relevante.
- No hace falta correr ninguna otra suite de pruebas del repositorio más allá del linter anterior.

## Convenciones de commits

- Los mensajes de commit deben seguir el formato [Conventional Commits](https://www.conventionalcommits.org/).
- Si se modifican los archivos README, el commit debe ser de tipo `feat` con el formato `feat: <mensaje>`.
- Cuando se actualizan varios archivos README simultáneamente, usar una descripción que lo indique claramente:
  - Ejemplo: `feat: add [herramienta] to [categoría] section in all README files`
  - Ejemplo: `feat: add new [categoría] category to all README files`
