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
├── apple-touch-icon.png         # Icono para dispositivos Apple
├── android-chrome-192x192.png   # Icono para Android / Chrome
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
│   ├── testimonios/            # Textos testimoniales e intervenciones públicas
│   │   ├── index.html          # Índice de testimonios
│   │   └── voy-a-hablar-de-resiliencia/ # Testimonio sobre resiliencia frente a la adopción
│   ├── adopcion/               # Textos críticos sobre adopción / Undoing Adoption
│   │   ├── index.html
│   │   ├── identicidio/
│   │   ├── abolicion-del-identicidio/
│   │   ├── abolifobia/
│   │   ├── adopcion-genocidio-identicida-colonial/
│   │   └── estigma-registral-adopcion/
│   └── bebes-robados/          # Investigación sobre bebés robados
│       ├── index.html          # Índice de investigación sobre bebés robados
│       ├── informe-asociacion-maria-madre-bilbao/ # Informe IAMM
│       └── informe-adoptados-bilbao/              # Informe AdoptadosBilbao
├── libros/                     # Redirección técnica hacia /es/obra/libros/
└── prensa/                     # Prensa
    ├── index.html              # Índice de prensa
    ├── el-observatorio-9-2026/ # Entrevista en El Observatorio nº 9
    ├── el-correo-primer-bebe-robado-victima-franquismo/ # Página documental sobre el primer reconocimiento publicado por El Correo
    ├── medios/                 # Dosier de medios
    └── notas-de-prensa/        # Archivo de notas de prensa emitidas por Olmo Gómez Aldaz
        ├── index.html
        ├── sentencia-pionera-identidad-dni/
        ├── reconocimiento-bebe-robado-nulidad-adopcion/
        └── ley-memoria-democratica-bebes-robados/

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
│   ├── testimonies/                 # Testimonial texts and public interventions
│   │   ├── index.html               # Testimonies index
│   │   └── i-am-going-to-speak-about-resilience/ # Testimony on resilience against adoption
│   ├── adoption/                    # Critical texts on adoption / Undoing Adoption
│   │   ├── index.html
│   │   ├── identicide/
│   │   ├── abolition-of-identicide/
│   │   ├── aboliphobia/
│   │   ├── adoption-as-colonial-identicide-genocide/
│   │   └── registry-stigma-of-adoption/
│   └── stolen-babies/               # Research on stolen babies
│       ├── index.html               # Research on stolen babies index
│       ├── maria-madre-association-report/ # IAMM report
│       └── adoptados-bilbao-report/        # AdoptadosBilbao report
├── books/                           # Technical redirect to /en/work/books/
└── press/                           # Press
    ├── index.html                   # Press index
    ├── el-observatorio-9-2026/      # El Observatorio no. 9 interview
    ├── el-correo-first-stolen-baby-recognised-francoism-victim/ # English documentary page on El Correo's first-recognition report
    ├── media/                       # Media dossier
    └── press-releases/              # English archive of press releases
        ├── index.html
        ├── landmark-ruling-identity-restored-id-card/
        ├── stolen-baby-recognition-adoption-annulment/
        └── democratic-memory-law-stolen-babies/

---

## Obra / Work

La sección Obra / Work organiza cuatro líneas principales:

- Libros / Books
- Testimonios / Testimonies
- Adopción / Adoption
- Bebés robados / Stolen babies

La estructura busca separar la obra publicada, la línea testimonial, los textos críticos sobre adopción y la investigación documental sobre bebés robados.

Las páginas índice correspondientes son:

- /es/obra/
- /en/work/
- /es/obra/libros/
- /en/work/books/
- /es/obra/testimonios/
- /en/work/testimonies/
- /es/obra/adopcion/
- /en/work/adoption/
- /es/obra/bebes-robados/
- /en/work/stolen-babies/

---

## Testimonios / Testimonies

La sección Testimonios / Testimonies reúne textos testimoniales e intervenciones públicas de Olmo Gómez Aldaz.

Rutas principales:

- /es/obra/testimonios/
- /en/work/testimonies/

Primer testimonio publicado dentro de esta sección:

- /es/obra/testimonios/voy-a-hablar-de-resiliencia/
- /en/work/testimonies/i-am-going-to-speak-about-resilience/

El texto corresponde a “Voy a hablar de resiliencia: Resiliencia frente a la adopción”, preparado para el panel abierto “Diferentes voces”, dentro de las jornadas “Caminos de Resiliencia”, XV Aniversario de La Voz de los Adoptados.

---

## Notas de prensa / Press releases

La sección Notas de prensa / Press releases conserva los comunicados emitidos directamente por Olmo Gómez Aldaz y los separa de la cobertura publicada por medios externos.

Rutas de archivo:

- /es/prensa/notas-de-prensa/
- /en/press/press-releases/

Notas incorporadas:

1. 20 de enero de 2026: sentencia pionera y recuperación de la identidad en el DNI sin anular la adopción. La nota original se difundió en el cuerpo del correo y se reproduce en HTML, sin crear posteriormente un PDF artificial.
2. 14 de julio de 2026: reconocimientos oficiales como «bebé robado» y oposición de la Diputación Foral de Bizkaia a la nulidad de la adopción. Se conserva en HTML y mediante el PDF original en español.
3. 4 de agosto de 2026: «¿Está fracasando la Ley de Memoria Democrática con los bebés robados?». Se conserva en HTML y mediante el PDF original en español.

Las páginas inglesas contienen la traducción íntegra del texto. Cuando existe PDF, enlazan el documento original en español y lo identifican expresamente como tal.

Las páginas índice utilizan datos estructurados de tipo `CollectionPage`. Las páginas individuales utilizan `NewsArticle`, con fecha de publicación, titular, descripción, idioma y referencia al autor. Las páginas generales de prensa mantienen el tipo `WebPage` y relacionan el archivo de notas y el dosier de medios mediante `hasPart`.

---

## Documentos públicos — /docs/

La carpeta docs/ contiene documentos públicos enlazados desde la web o incluidos en el sitemap.

Puede incluir PDFs, revistas, entrevistas, documentos de reconocimiento o reparación y materiales complementarios del proyecto.

Los documentos situados en docs/ forman parte del contenido público del sitio cuando están enlazados desde páginas de la web o incluidos en sitemap.xml.

Entre los documentos asociados a las notas de prensa se encuentran los PDF originales de las notas difundidas en julio y agosto de 2026. La nota de enero de 2026 se conserva únicamente como texto HTML porque fue distribuida directamente en el cuerpo del correo.

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

El archivo sitemap.xml recoge las URLs públicas principales del sitio: home española, versión inglesa, páginas interiores, secciones de Obra / Work, testimonios, investigación sobre bebés robados, informes documentales, prensa, dosier de medios, archivo bilingüe de notas de prensa y documentos públicos seleccionados.

Las páginas nuevas de notas de prensa están emparejadas mediante `hreflang`. El sitemap incluye `lastmod` para las ocho páginas nuevas y para las dos páginas generales de prensa actualizadas el 4 de agosto de 2026.

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
