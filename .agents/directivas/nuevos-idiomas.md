# Directiva: Crear un nuevo idioma

Instrucciones para agentes que agreguen una nueva traducción completa de "my awesome".

## Idiomas actuales

- `README.md` - Español (versión principal, fuente de verdad para la estructura)
- `README-EN.md` - Inglés
- `README-PT.md` - Portugués

## Convención de nombres

Los archivos de idioma adicionales siguen el patrón:

```
README-<CODIGO>.md
```

- `<CODIGO>` es el código de idioma en mayúsculas, siguiendo ISO 639-1 (2 letras) cuando exista: `README-FR.md` (francés), `README-DE.md` (alemán), `README-IT.md` (italiano), etc.
- Si el idioma necesita distinguir variante regional, usar el patrón `README-<IDIOMA>-<REGION>.md` en mayúsculas (ej: `README-PT-BR.md` si en el futuro se necesitara separar portugués de Brasil y Portugal).

## Pasos para crear un nuevo idioma

1. **Usar `README.md` como base estructural**: el nuevo archivo debe reflejar exactamente la misma estructura que la versión en español:
   - Mismo título y párrafo introductorio (traducidos).
   - Misma sección "Contenido" con enlaces ancla a cada categoría (traducidos, incluyendo los anchors en formato Markdown correspondiente).
   - Mismas 8 macro-categorías, en el mismo orden, con el mismo emoji temático.
   - Mismos subgrupos en negrita dentro de cada categoría, en el mismo orden.
   - Mismas herramientas, en el mismo orden, dentro de cada subgrupo/categoría.

2. **Traducir, no resumir ni ampliar**: cada descripción debe traducirse fielmente al idioma destino, manteniendo el mismo nivel de detalle (una línea) que las versiones existentes. No omitir herramientas ni agregar herramientas que no existan en `README.md`.

3. **No traducir**: nombres propios de herramientas, URLs, y nombres de marcas/tecnologías (ej. "React", "WebGPU", "Zustand").

4. **Verificación de completitud**: el nuevo archivo debe tener el mismo número de categorías, subgrupos y entradas que `README.md`. Si `README.md` se actualiza después (nueva herramienta o categoría), todos los archivos de idioma —incluido el nuevo— deben actualizarse en el mismo cambio (ver `agregar-enlaces.md`).

5. **Mantenimiento futuro**: a partir de su creación, el nuevo `README-<CODIGO>.md` pasa a formar parte del conjunto de README que deben mantenerse sincronizados en cada cambio futuro (agregar herramientas, categorías, o reestructuraciones).

## Ejemplo de cabecera traducida (francés)

```markdown
# my awesome

Ceci est une liste de recommandations personnelles pour l'utilisation de certains outils au quotidien ou dans des institutions spécifiques. Les outils sont organisés par catégories pour faciliter leur recherche et leur utilisation.

## Contenu

- [🤖 IA et Automatisation](#-ia-et-automatisation)
- [💻 Développement Web](#-developpement-web)
...
```
