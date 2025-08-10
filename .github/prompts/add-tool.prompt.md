---
mode: agent
tools: ['codebase', 'usages', 'vscodeAPI', 'problems', 'changes', 'testFailure', 'terminalSelection', 'terminalLastCommand', 'openSimpleBrowser', 'fetch', 'findTestFiles', 'searchResults', 'githubRepo', 'extensions', 'editFiles', 'runNotebooks', 'search', 'new', 'runCommands', 'runTasks']
description: "Prompt para solicitar agregar una herramienta a la lista curada de recomendaciones"
---

# Agregar nueva herramienta

Por favor, agrega una nueva herramienta a la lista "my awesome" siguiendo estos pasos:

1. **Investigación**: Busca información actualizada sobre la herramienta en Internet para verificar:
   - Que la herramienta siga activa
   - Sus características principales
   - La URL correcta

2. **Información de la herramienta**:
   - **Nombre**: [Nombre de la herramienta]
   - **URL**: [URL completa]
   - **Descripción**: [Qué hace la herramienta y por qué es útil]
   - **Categoría sugerida**: [Financiera, Productividad, etc.]

3. **Formato esperado**:
   ```markdown
   - [Nombre de la Herramienta](URL) - Descripción detallada de qué hace la herramienta y por qué es útil.
   ```

## Ejemplos de herramientas por categoría:

### Financiera
- Herramientas para dividir gastos
- Plataformas de transferencias
- Apps de gestión financiera

### Productividad
- Herramientas de organización
- Apps de gestión de tiempo
- Plataformas de colaboración

## Instrucciones adicionales:
- Verifica que la URL funcione correctamente
- Incluye casos de uso específicos en la descripción
- Considera el contexto local (especialmente para Chile)
- Mantén la descripción clara y específica sobre el valor que aporta

## Ejemplo de solicitud:
"Quiero agregar la herramienta [Nombre] que encontré en [URL]. Esta herramienta es útil para [descripción del uso] y creo que debería ir en la categoría [categoría]."
