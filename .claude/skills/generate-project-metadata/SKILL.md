---
name: generate-project-metadata
description: Genera el archivo YAML de metadata (`metadata/<id>.yaml`) de un proyecto de la lista "my awesome", paso a paso. Úsalo cuando se pida crear, actualizar o investigar la metadata (URL canónica, labels, summary, segmento, etc.) de una herramienta. Requisito: el proyecto debe estar listado en `README.md`.
---

# Generar metadata de un proyecto

Produce `metadata/<id>.yaml` para una herramienta de la lista. Etapa exploratoria: el objetivo es descubrir qué datos se pueden extraer, así que se documentan también las preguntas abiertas.

Referencia de formato: `metadata/portless.yaml` (muestra canónica). Cópiala como plantilla.

## Requisito previo: el proyecto debe estar en el README

`README.md` es la fuente de verdad. Si la herramienta no está listada, **detente**: no generes metadata y propón agregarla primero con `.agents/directives/add-links.md`.

```bash
# Reemplaza <termino> por el nombre o dominio de la herramienta
grep -n -i "<termino>" README.md
```

- Sin coincidencias en una línea de entrada (`- [Nombre](URL) - ...`) → no continuar.
- Con coincidencias → anota: nombre, URL, descripción, categoría (`## ` más cercano hacia arriba) y subgrupo (`**...**` más cercano, si existe).

```bash
# Categoría y subgrupo de una línea N
awk -v n=<N> 'NR<=n && /^## /{c=$0; s=""} NR<=n && /^\*\*.*\*\*$/{s=$0} END{print c; print s}' README.md
```

## Pasos

1. **Verificar el requisito** (sección anterior). Obtén `id` = nombre en minúsculas con guiones (`Magic UI` → `magic-ui`).
2. **Verificar que no exista ya** `metadata/<id>.yaml`. Si existe, actualízalo en vez de recrearlo.
3. **Recolectar descripciones por idioma**: busca la misma URL en `README-EN.md`, `README-PT.md` y cualquier `README-<CODE>.md`, y copia la descripción de cada uno en `readme.descriptions`.
4. **Consultar la fuente**: abre la URL del README (WebFetch). Si es un repositorio de GitHub, extrae: descripción, licencia, lenguaje, stars/forks/watchers, issues y PRs abiertos, topics, último release, instalación, features, plataformas y homepage. Si no es un repo, usa la página oficial y deja `repository: null`.
4b. **Capturar precios** (si el producto tiene planes): consulta `pricing_url` (o la URL de precios que indique quien pide la tarea; si no la hay, busca el enlace "Pricing" en la página oficial) con WebFetch y registra cada plan visible en `pricing_plans`. Es una captura genérica, tal como aparece en la página:
   - Por plan: `name`, `price` (número o `null` si es "contactar ventas"), `currency` (ISO 4217, p. ej. `EUR`), `billing_period` (`month`, `year`, `one-time`, `usage`, `custom` o `null`), `price_note` (aclaraciones como "facturado anualmente"), `audience`, `hosting`, `limits` y `features` (listas de texto breve).
   - Incluye también planes gratuitos y ediciones comunitarias (`price: 0`).
   - Anota a nivel raíz `pricing_source_url` y `pricing_captured_at` (fecha de consulta). Los precios cambian: son un snapshot, no un dato estable.
   - No conviertas monedas, no calcules descuentos ni completes precios que la página no muestre (usa `null`).
   - Sin planes públicos o producto gratuito sin página de precios → `pricing_plans: []`.
5. **Resolver `url_canonical`**: sigue redirecciones, quita parámetros de tracking (`utm_*`, `ref`) y barras finales; si hay homepage distinta al repo, la canónica es la URL listada en el README y la otra va en `homepage`.
6. **Completar el YAML** siguiendo las secciones de `metadata/portless.yaml`: identidad, curación, clasificación, resumen, features, técnico, salud, procedencia.
7. **Reglas de honestidad de datos**:
   - Dato no encontrado → `null` (o lista vacía); nunca inventarlo.
   - Valor deducido por ti (`segment`, `labels`, `audience`, `language` si la fuente no lo dice) → comentario `# inferred`.
   - Las métricas de salud llevan `captured_at` con la fecha de consulta; registra cada fuente en `sources` con `fetched_at`.
   - `summary` en inglés, 2–3 frases, sin copiar el texto literal del README.
   - Si la URL del README es un sitio de producto y existe un repo, la canónica es la del README y el repo va en `repository.url` (ver `metadata/isbetter-ai.yaml`).
   - Licencias no OSI (p. ej. FSL, BUSL, Sustainable Use): registra el identificador SPDX en `license` (o el nombre si no tiene SPDX) y usa `open_source: false`.
   - `license_type` clasifica la licencia: `permissive`, `copyleft`, `fair-code`, `source-available`, `proprietary` o `null` si no se conoce. Debe ser coherente con `open_source` (`permissive`/`copyleft` → `true`; el resto → `false`).
   - `pricing_url`: URL de la página de precios si existe y la verificaste (WebFetch); si no, `null`. Nunca la adivines. `pricing` (free/freemium/paid) sigue siendo inferido y debe ser coherente con `pricing_plans` cuando existan.
   - El HTML de GitHub no entrega la fecha del último commit; déjala en `null` o consúltala vía API.
8. **Anotar preguntas abiertas** al final del archivo (qué campos salen de API vs. requieren LLM, vocabulario por cerrar, etc.).
9. **Validar**:
   ```bash
   python3 scripts/lint-metadata.py metadata/<id>.yaml   # requiere PyYAML
   node scripts/lint-awesome-list.js
   ```
   Ambos deben terminar sin error (el primero también corre en CI: `.github/workflows/lint-metadata.yml`). `lint-awesome-list.js` solo valida los `README*.md`; no se deben modificar al generar metadata.
10. **Commit**: `docs: add exploratory YAML metadata for <Nombre>` (usa `feat` solo si también cambiaron los README).

## Salida esperada

Un único archivo `metadata/<id>.yaml` con las mismas secciones que `metadata/portless.yaml`. Al terminar, informa qué campos quedaron `null` y cuáles son inferidos.
