# AGENTS.md - Instructions for Agents

This document has instructions for agents that will help maintain and update the README.md file of "my awesome".

## Propósito del Proyecto

"my awesome" es una lista curada de recomendaciones personales de herramientas útiles para el día a día o instituciones específicas. Las herramientas se organizan por categorías para facilitar su búsqueda y uso.

## Estructura del README.md

### Formato General
- El documento debe usar formato Markdown
- Los títulos deben comenzar con `#` (h1: `# titulo`, h2: `## titulo`)
- Las herramientas se organizan por categorías
- Cada herramienta debe incluir un enlace y una descripción

### Formato de Entrada de Herramientas

Cada herramienta debe seguir este formato:
```markdown
- [Nombre de la Herramienta](URL) - Descripción detallada de qué hace la herramienta y por qué es útil.
```

### Categorías Existentes
- **Financiera**: Herramientas relacionadas con finanzas, pagos, transferencias, división de gastos, etc.

## Proceso para Agregar Nuevas Herramientas

Cuando se solicite agregar una nueva herramienta:

1. **Investigación Previa**: Antes de agregar cualquier herramienta, debe buscarse información actualizada en Internet (usando Bing o Google) para verificar:
   - Que la herramienta siga activa
   - Información actual sobre sus características
   - Confirmar la URL correcta

2. **Categorización**: Determinar la categoría apropiada para la herramienta:
   - Si la categoría ya existe, agregar la herramienta a esa sección
   - Si no existe una categoría apropiada, crear una nueva sección

3. **Formato de Descripción**: La descripción debe incluir:
   - Qué hace la herramienta
   - Por qué es útil
   - Casos de uso específicos cuando sea relevante

4. **Orden**: Mantener las herramientas organizadas dentro de cada categoría

## Ejemplos de Buenas Descripciones

✅ **Buena descripción**:
```markdown
- [Splitwise](https://www.splitwise.com/) - Una aplicación útil para dividir gastos entre personas utilizando el número de teléfono para contactarlos. Es especialmente útil para dividir gastos en salidas a restaurantes o actividades grupales.
```

❌ **Descripción poco útil**:
```markdown
- [Splitwise](https://www.splitwise.com/) - App para dividir gastos.
```

## Notas Importantes

- Siempre verificar que las URLs funcionen antes de agregarlas
- Mantener las descripciones claras y específicas sobre el valor que aporta cada herramienta
- Considerar el contexto local (por ejemplo, herramientas específicas para Chile)
- Actualizar la fecha de última modificación cuando sea relevante
- No es necesario ejecutar pruebas automatizadas tras realizar cambios en este repositorio

## Convenciones de commits

- Los mensajes de commit deben seguir el formato [Conventional Commits](https://www.conventionalcommits.org/).
- Si se modifica el archivo `README.md`, el commit debe ser de tipo `feat` con el formato `feat: <mensaje>`.
