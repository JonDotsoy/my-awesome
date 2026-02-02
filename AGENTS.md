# AGENTS.md - Instructions for Agents

This document has instructions for agents that will help maintain and update the README.md file of "my awesome".

## Propósito del Proyecto

"my awesome" es una lista curada de recomendaciones personales de herramientas útiles para el día a día o instituciones específicas. Las herramientas se organizan por categorías para facilitar su búsqueda y uso.

## Estructura de los Archivos README

El proyecto mantiene **tres archivos README en diferentes idiomas**:
- `README.md` - Versión en español (principal)
- `README-EN.md` - Versión en inglés
- `README-PT.md` - Versión en portugués

**Importante**: Todos los archivos README deben mantenerse sincronizados. Cuando se agrega o modifica una herramienta, debe actualizarse en los tres archivos con las traducciones correspondientes.

### Formato General
- El documento debe usar formato Markdown
- Los títulos deben comenzar con `#` (h1: `# titulo`, h2: `## titulo`)
- Las categorías deben incluir un emoji temático seguido del nombre (ej: `## 💰 Financiera`)
- Las herramientas se organizan por categorías
- Cada herramienta debe incluir un enlace y una descripción
- Debe incluirse una sección "Contenido" al inicio con enlaces a todas las categorías

### Formato de Entrada de Herramientas

Cada herramienta debe seguir este formato:
```markdown
- [Nombre de la Herramienta](URL) - Descripción detallada de qué hace la herramienta y por qué es útil.
```

### Emojis Temáticos

Cada categoría debe tener un emoji que represente visualmente su contenido. Al crear nuevas categorías, elegir un emoji apropiado que facilite la identificación visual:

- 💰 para finanzas
- 🚀 para productividad
- 🎬 para contenido multimedia
- 📧 para comunicación
- 📝 para diagramación/documentación
- 🎮 para gráficos/gaming
- 🤖 para automatización/IA
- 🖥️ para infraestructura/servidores
- 🔧 para herramientas/testing
- 🧪 para testing/experimentación
- 👥 para comunidades
- 📰 para noticias
- 📚 para conocimiento/aprendizaje
- 🧩 para componentes/bibliotecas
- 🌐 para idiomas/internacionalización
- 📖 para lectura/libros
- 💼 para empleo/carrera
- 📦 para repositorios/paquetes
- 🔗 para enlaces/relacionados

### Categorías Existentes

1. **💰 Financiera**: Herramientas relacionadas con finanzas, pagos, transferencias, división de gastos, inversiones, etc.
2. **🚀 Productividad**: Herramientas para mejorar la eficiencia y gestión de tareas
3. **🎬 Generador de Contenido**: Plataformas para crear contenido multimedia
4. **📧 Comunicación**: Servicios de email, mensajería y comunicación
5. **📝 Diagramación**: Herramientas para crear diagramas, gráficos y visualizaciones
6. **🎮 Motores Gráficos para el Navegador**: Bibliotecas para gráficos 3D y WebGL/WebGPU
7. **🤖 Automatización**: Plataformas para automatizar flujos de trabajo y procesos
8. **🤖 IA Agents**: Frameworks y herramientas para agentes de IA y desarrollo asistido
9. **🖥️ Infraestructura**: Servidores web, proxies, plataformas serverless
10. **🔧 Herramientas de Prueba de API**: Clientes HTTP y herramientas para testing de APIs
11. **🧪 Automatización de Navegadores y Testing**: Frameworks para testing E2E y automatización web
12. **👥 Comunidades**: Grupos y comunidades tecnológicas
13. **📰 Noticias**: Plataformas de noticias tecnológicas y actualizaciones
14. **📚 Recursos de Conocimiento**: Sitios de inspiración, aprendizaje y documentación
15. **🧩 Bibliotecas de Componentes UI**: Colecciones de componentes para interfaces de usuario
16. **🌐 Aprendizaje de Idiomas**: Recursos para aprender otros idiomas
17. **📖 Lectura**: Plataformas para gestionar y descubrir libros
18. **💼 Empleo**: Portales de búsqueda de trabajo y transparencia salarial
19. **📦 Repositorios de Código**: Plataformas de alojamiento de código fuente
20. **🔗 Relacionado**: Listas curadas y proyectos relacionados

## Proceso para Agregar Nuevas Herramientas

Cuando se solicite agregar una nueva herramienta:

1. **Investigación Previa**: Antes de agregar cualquier herramienta, debe buscarse información actualizada en Internet (usando Bing o Google) para verificar:
   - Que la herramienta siga activa
   - Información actual sobre sus características
   - Confirmar la URL correcta

2. **Categorización**: Determinar la categoría apropiada para la herramienta:
   - Si la categoría ya existe, agregar la herramienta a esa sección
   - Si no existe una categoría apropiada, crear una nueva sección con su emoji temático correspondiente
   - Actualizar la sección "Contenido" con el enlace a la nueva categoría

3. **Formato de Descripción**: La descripción debe incluir:
   - Qué hace la herramienta
   - Por qué es útil
   - Casos de uso específicos cuando sea relevante

4. **Actualización Multiidioma**: **CRÍTICO** - La herramienta debe agregarse en los tres archivos README:
   - `README.md` (español)
   - `README-EN.md` (inglés - traducir descripción)
   - `README-PT.md` (portugués - traducir descripción)

5. **Orden**: Mantener las herramientas organizadas dentro de cada categoría

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

- **Sincronización multiidioma**: Siempre actualizar los tres archivos README (español, inglés y portugués) cuando se agregue o modifique una herramienta
- Siempre verificar que las URLs funcionen antes de agregarlas
- Mantener las descripciones claras y específicas sobre el valor que aporta cada herramienta
- Considerar el contexto local (por ejemplo, herramientas específicas para Chile)
- Usar emojis temáticos apropiados al crear nuevas categorías
- Actualizar la sección "Contenido" cuando se agreguen nuevas categorías
- No es necesario ejecutar pruebas automatizadas tras realizar cambios en este repositorio

## Convenciones de commits

- Los mensajes de commit deben seguir el formato [Conventional Commits](https://www.conventionalcommits.org/).
- Si se modifican los archivos README, el commit debe ser de tipo `feat` con el formato `feat: <mensaje>`.
- Cuando se actualizan los tres archivos README simultáneamente, usar una descripción que lo indique claramente:
  - Ejemplo: `feat: add [herramienta] to [categoría] section in all README files`
  - Ejemplo: `feat: add new [categoría] category to all README files`
