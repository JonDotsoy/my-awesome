# AGENTS.md - Instructions for Agents

This document has instructions for agents that will help maintain and update the README.md file of "my awesome".

## Propósito del Proyecto

"my awesome" es una lista curada de recomendaciones personales de herramientas útiles para el día a día o instituciones específicas. Las herramientas se organizan por categorías para facilitar su búsqueda y uso.

**Este es un proyecto en crecimiento**: Se pueden agregar nuevas categorías y herramientas en cualquier momento según las necesidades y descubrimientos del usuario.

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

Cada categoría debe tener un emoji que represente visualmente su contenido. Al crear nuevas categorías, elegir un emoji apropiado que facilite la identificación visual.

**Ejemplos de emojis usados actualmente:**

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

**Para nuevas categorías**: Elige un emoji que sea intuitivo y represente claramente el tema. Puedes usar emojis que no estén en la lista anterior si son más apropiados para la nueva categoría.

### Categorías Existentes

El proyecto organiza las herramientas en múltiples categorías temáticas. **Esta lista puede crecer con el tiempo** a medida que se agreguen nuevas herramientas. Para ver la lista actualizada de todas las categorías, consulta la sección "Contenido" en cualquiera de los archivos README.

Algunas categorías incluyen (pero no se limitan a):

- **💰 Financiera**: Herramientas relacionadas con finanzas, pagos, transferencias, división de gastos, inversiones
- **🚀 Productividad**: Herramientas para mejorar la eficiencia y gestión de tareas
- **🎬 Generador de Contenido**: Plataformas para crear contenido multimedia
- **📧 Comunicación**: Servicios de email, mensajería y comunicación
- **📝 Diagramación**: Herramientas para crear diagramas, gráficos y visualizaciones
- **🎮 Motores Gráficos para el Navegador**: Bibliotecas para gráficos 3D y WebGL/WebGPU
- **🤖 Automatización**: Plataformas para automatizar flujos de trabajo y procesos
- **🤖 IA Agents**: Frameworks y herramientas para agentes de IA y desarrollo asistido
- **🖥️ Infraestructura**: Servidores web, proxies, plataformas serverless
- **🔧 Herramientas de Prueba de API**: Clientes HTTP y herramientas para testing de APIs
- **🧪 Automatización de Navegadores y Testing**: Frameworks para testing E2E y automatización web
- **👥 Comunidades**: Grupos y comunidades tecnológicas
- **📰 Noticias**: Plataformas de noticias tecnológicas y actualizaciones
- **📚 Recursos de Conocimiento**: Sitios de inspiración, aprendizaje y documentación
- **🧩 Bibliotecas de Componentes UI**: Colecciones de componentes para interfaces de usuario
- **🌐 Aprendizaje de Idiomas**: Recursos para aprender otros idiomas
- **📖 Lectura**: Plataformas para gestionar y descubrir libros
- **💼 Empleo**: Portales de búsqueda de trabajo y transparencia salarial
- **📦 Repositorios de Código**: Plataformas de alojamiento de código fuente
- **🔗 Relacionado**: Listas curadas y proyectos relacionados

**Nota**: Al agregar una nueva categoría, asegúrate de actualizarla en los tres archivos README y en sus respectivas secciones de "Contenido".

## Proceso para Agregar Nuevas Herramientas

Cuando se solicite agregar una nueva herramienta:

1. **Investigación Previa**: Antes de agregar cualquier herramienta, debe buscarse información actualizada en Internet (usando Bing o Google) para verificar:
   - Que la herramienta siga activa
   - Información actual sobre sus características
   - Confirmar la URL correcta

2. **Categorización**: Determinar la categoría apropiada para la herramienta:
   - Si la categoría ya existe, agregar la herramienta a esa sección
   - Si no existe una categoría apropiada, **crear una nueva sección**:
     - Elegir un emoji temático apropiado (ver sección "Emojis Temáticos")
     - Crear la nueva sección en los tres archivos README
     - Actualizar la sección "Contenido" en los tres archivos con el enlace a la nueva categoría
     - Mantener el orden lógico de las categorías

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
