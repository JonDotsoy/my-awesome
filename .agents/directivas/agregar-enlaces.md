# Directiva: Agregar nuevos enlaces (herramientas)

Instrucciones para agentes que agreguen una nueva herramienta a "my awesome".

## Estructura actual

Los README (`README.md`, `README-EN.md`, `README-PT.md`) organizan las herramientas en **8 macro-categorías** (`##`):

1. 🤖 IA y Automatización
2. 💻 Desarrollo Web
3. 🖥️ Infraestructura y Código
4. 💰 Finanzas
5. 🚀 Productividad y Comunicación
6. 🎬 Contenido y Diseño
7. 📚 Aprendizaje y Carrera
8. 🔗 Relacionado

Algunas macro-categorías se dividen en **subgrupos temáticos** en negrita (sin `#`), por ejemplo dentro de "🤖 IA y Automatización": **Agentes y desarrollo asistido por IA**, **Comparadores de LLMs**, **Automatización de procesos**. No todas las categorías tienen subgrupos (p. ej. "💰 Finanzas" no los usa).

## Pasos para agregar una herramienta

1. **Verificar la herramienta**: buscar información actualizada en internet para confirmar que sigue activa, que la URL es correcta y entender qué hace.

2. **Elegir la categoría y subgrupo**:
   - Ubicar la macro-categoría más adecuada entre las 8 existentes.
   - Si esa categoría tiene subgrupos, elegir el subgrupo temático correcto; si ninguno encaja, se puede crear un nuevo subgrupo en negrita dentro de la categoría.
   - Solo crear una **nueva macro-categoría** (`##`) si la herramienta no encaja razonablemente en ninguna de las 8 existentes. En ese caso:
     - Elegir un emoji temático apropiado (ver ejemplos en `AGENTS.md`).
     - Agregar la nueva entrada en la sección "Contenido" (índice) de los tres README.
     - Mantener un orden lógico entre categorías.

3. **Formato de la entrada** — una sola línea, sin párrafos largos:
   ```markdown
   - [Nombre de la Herramienta](URL) - Descripción breve de qué es y para qué sirve.
   ```
   - Una sola oración. Evitar el formato antiguo de descripciones extensas ("Es especialmente útil para...").
   - Incluir qué es la herramienta y su valor principal, sin relleno.

4. **Sincronización multiidioma (obligatorio)**: agregar la entrada en **todos** los archivos README existentes del proyecto (`README.md`, `README-EN.md`, `README-PT.md`, y cualquier `README-<CODE>.md` adicional que exista), traduciendo la descripción a cada idioma. La entrada debe quedar en la misma categoría/subgrupo y en la misma posición relativa en todos los archivos.

5. **Orden dentro del subgrupo**: agregar la nueva herramienta al final del subgrupo o categoría correspondiente, salvo que exista una razón clara para ubicarla en otro punto (p. ej. agrupar herramientas muy similares).

## Ejemplo

✅ Correcto:
```markdown
- [Fintoc.me](https://fintoc.me/) - Comparte datos de transferencia bancaria en Chile mediante una URL simple.
```

❌ Evitar (demasiado largo, estilo antiguo):
```markdown
- [Fintoc.me](https://fintoc.me/) - Esta herramienta es perfecta para compartir la información de datos de transferencia bancaria sin tener que enviarla de manera indirecta. En Chile, para hacer una transferencia a una cuenta bancaria de otra persona se necesita demasiada información...
```

❌ Evitar (demasiado corto, sin contexto de uso):
```markdown
- [Fintoc.me](https://fintoc.me/) - App de transferencias.
```
