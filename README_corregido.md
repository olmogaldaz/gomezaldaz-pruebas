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
├── favicon.ico       # Icono principal del sitio
├── favicon-32x32.png # Icono del sitio en formato PNG
├── apple-touch-icon.png # Icono para dispositivos Apple
├── android-chrome-192x192.png # Icono para Android / Chrome
├── yandex_21845d3da951913c.html # Verificación de Yandex Webmaster
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
├── autor/                      # Olmo
├── memoria/                    # Memoria
├── historia/                   # Historia
├── demanda/                    # Demanda
├── sentencia/                  # Sentencias
├── genus-homo/                 # Editorial Genus Homo
├── obra/                       # Obra publicada, archivo crítico e investigación
│   ├── index.html              # Índice de Obra
│   ├── libros/                 # Libros
│   ├── adopcion/               # Textos críticos sobre adopción / Undoing Adoption
│   │   ├── index.html
│   │   ├── identicidio/
│   │   ├── abolicion-del-identicidio/
│   │   ├── abolifobia/
│   │   ├── adopcion-genocidio-identicida-colonial/
│   │   └── estigma-registral-adopcion/
│   ├── bebes-robados/          # Investigación sobre bebés robados
│   │   ├── index.html          # Índice de investigación sobre bebés robados
│   │   ├── informe-asociacion-maria-madre-bilbao/ # Informe IAMM
│   │   └── informe-adoptados-bilbao/              # Informe AdoptadosBilbao
│   └── testimonios/            # Textos testimoniales e intervenciones públicas
│       ├── index.html          # Índice de testimonios
│       └── voy-a-hablar-de-resiliencia/ # Testimonio sobre resiliencia frente a la adopción
├── libros/                     # Redirección técnica hacia /es/obra/libros/
└── prensa/                     # Prensa
    ├── index.html              # Índice de prensa
    ├── el-observatorio-9-2026/ # Entrevista en El Observatorio nº 9
    └── medios/                 # Dosier de medios

---

## Inglés — /en/

La versión inglesa está organizada bajo /en/ y funciona como versión internacional del sitio.

Estructura actual:

/en/
├── index.html                       # English home
├── author/                          # Olmo
├── memory/                          # Memory
├── story/                           # Story
├── claim/                           # Claim
├── sentence/                        # Court rulings / judgments
├── genus-homo/                      # Genus Homo publishing imprint
├── work/                            # Published work, critical archive and research
│   ├── index.html                   # Work index
│   ├── books/                       # Books
│   ├── adoption/                    # Critical texts on adoption / Undoing Adoption
│   │   ├── index.html
│   │   ├── identicide/
│   │   ├── abolition-of-identicide/
│   │   ├── aboliphobia/
│   │   ├── adoption-as-colonial-identicide-genocide/
│   │   └── registry-stigma-of-adoption/
│   ├── stolen-babies/               # Research on stolen babies
│   │   ├── index.html               # Research on stolen babies index
│   │   ├── maria-madre-association-report/ # IAMM report
│   │   └── adoptados-bilbao-report/        # AdoptadosBilbao report
│   └── testimonies/                 # Testimonial texts and public interventions
│       ├── index.html               # Testimonies index
│       └── i-am-going-to-speak-about-resilience/ # Testimony on resilience against adoption
├── books/                           # Technical redirect to /en/work/books/
└── press/                           # Press
    ├── index.html                   # Press index
    ├── el-observatorio-9-2026/      # El Observatorio no. 9 interview
    └── media/                       # Media dossier

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
- favicon.ico, favicon-32x32.png, apple-touch-icon.png y android-chrome-192x192.png → iconos del sitio
- yandex_21845d3da951913c.html → archivo de verificación de Yandex Webmaster

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

El archivo sitemap.xml recoge las URLs públicas principales del sitio: home española, versión inglesa, páginas interiores, secciones de Obra / Work, investigación sobre bebés robados, informes documentales, prensa, dosier de medios y documentos públicos seleccionados.

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
- /es/libros/ y /en/books/ se conservan solo como redirecciones técnicas hacia las nuevas rutas de Obra / Work.

Este README documenta la arquitectura principal y vigente del proyecto.
