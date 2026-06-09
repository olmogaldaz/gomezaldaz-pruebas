# gomezaldaz.com — Web structure

Este repositorio contiene la estructura y el contenido estático de la web pública gomezaldaz.com.

La web se publica mediante GitHub Pages, desde la rama main y la carpeta raíz del repositorio.

El proyecto está organizado por rutas, idiomas y bloques conceptuales. La estructura de carpetas responde a un criterio de orden, claridad y estabilidad a largo plazo.

El sitio usa rutas dentro del dominio principal gomezaldaz.com.

---

## Estructura general del repositorio

/
├── index.html        # Home principal en español
├── en/               # Versión inglesa
├── es/               # Páginas interiores en español
├── css/              # Hojas de estilo
├── js/               # JavaScript: menú e interacción
├── img/              # Imágenes y recursos gráficos
├── docs/             # Documentos públicos y PDFs
├── _layouts/         # Layouts de Jekyll
├── 404.html          # Página de error
├── CNAME             # Dominio personalizado
├── _config.yml       # Configuración del sitio
├── sitemap.xml       # Mapa del sitio
├── robots.txt        # Instrucciones para rastreadores
└── README.md         # Documentación del repositorio

---

## Publicación

La web está publicada mediante GitHub Pages.

Configuración actual:

- Rama de publicación: main
- Carpeta publicada: raíz del repositorio
- Dominio personalizado: gomezaldaz.com
- HTTPS activado

---

## Portada principal — /

La raíz del sitio / actúa como punto de entrada principal y como home oficial en español.

Desde la portada principal se accede a los bloques principales del proyecto.

Las páginas interiores en español se organizan bajo /es/...

La ruta /es/ funciona como página técnica de compatibilidad hacia /.

---

## Español — /es/...

Las páginas interiores en español están organizadas bajo /es/...

Estructura actual:

/es/
├── index.html                  # Página técnica de compatibilidad hacia /
├── autor/                      # Autor
├── historia/                   # Historia
├── demanda/                    # Demanda
├── sentencia/                  # Sentencia
├── memoria/                    # Memoria
├── genus-homo/                 # Editorial Genus Homo
├── libros/                     # Libros
└── prensa/                     # Prensa
    ├── index.html              # Índice de prensa
    ├── el-observatorio-9-2026/ # Entrevista en El Observatorio nº 9
    └── medios/                 # Dosier de medios

---

## Inglés — /en/

La versión inglesa está organizada bajo /en/ y funciona como versión internacional del sitio.

Estructura actual:

/en/
├── index.html                  # English home
├── author/                     # Author
├── story/                      # Story
├── claim/                      # Claim
├── sentence/                   # Court ruling / judgment
├── memory/                     # Memory
├── genus-homo/                 # Genus Homo publishing imprint
├── books/                      # Books
└── press/                      # Press
    ├── index.html              # Press index
    ├── el-observatorio-9-2026/ # El Observatorio no. 9 interview
    └── media/                  # Media dossier

---

## Documentos públicos — /docs/

La carpeta docs/ contiene documentos públicos enlazados desde la web o incluidos en el sitemap.

Puede incluir PDFs, revistas, entrevistas, documentos de reconocimiento o reparación y materiales complementarios del proyecto.

Los documentos situados en docs/ forman parte del contenido público del sitio cuando están enlazados desde páginas de la web o incluidos en sitemap.xml.

---

## Recursos comunes

Los recursos compartidos por todos los idiomas se alojan en la raíz del proyecto:

- css/ → estilos globales
- js/ → lógica de navegación y comportamiento
- img/ → imágenes y elementos gráficos
- _layouts/ → layouts comunes de Jekyll

Estas rutas son absolutas y comunes a todo el sitio.

---

## Navegación

La navegación principal se genera mediante JavaScript común.

Archivo principal:

/js/menu.js

El menú utiliza rutas absolutas y adapta los enlaces según la versión lingüística de la página.

El selector de idioma enlaza páginas equivalentes entre español e inglés cuando existe correspondencia.

---

## Indexación

El archivo robots.txt permite el rastreo completo del sitio y declara el sitemap oficial:

https://gomezaldaz.com/sitemap.xml

El archivo sitemap.xml recoge las URLs públicas principales del sitio: home española, versión inglesa, páginas interiores, prensa, dosier de medios y documentos públicos seleccionados.

---

## Notas importantes

- La web se organiza exclusivamente por rutas.
- La raíz / es la home oficial en español.
- /en/ es la home oficial en inglés.
- /es/ es una ruta técnica de compatibilidad hacia /.
- Las páginas interiores en español viven bajo /es/...
- Las páginas interiores en inglés viven bajo /en/...
- Los documentos públicos viven bajo /docs/.
- Las rutas del sitemap corresponden a páginas o documentos existentes.
- La estructura de carpetas sostiene la coherencia editorial y técnica del sitio.

Este README documenta la arquitectura real y vigente del proyecto.
