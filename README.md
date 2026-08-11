# gomezaldaz.com — Estructura, entornos y mantenimiento

Este proyecto contiene la estructura, el contenido y los recursos públicos de **gomezaldaz.com**. Se mantiene en dos repositorios de GitHub Pages: uno de pruebas y otro de producción.

El sitio es bilingüe, con la portada española en `/` y la versión inglesa en `/en/`.

---

## Publicación

Configuración común:

- Rama de publicación: `main`
- Carpeta publicada: raíz del repositorio
- HTTPS activado
- Generación estática mediante Jekyll

Jekyll procesa Liquid, los datos YAML, los layouts y los includes durante cada compilación. GitHub Pages publica después archivos HTML, XML, CSS y JavaScript ya generados. Las peticiones de visitantes y buscadores no vuelven a ejecutar Liquid.

La carpeta `_site/` es la salida local generada automáticamente por Jekyll durante una compilación. No forma parte del código fuente del proyecto, no debe versionarse y está excluida mediante `.gitignore`.

---

## Entornos de pruebas y producción

| Elemento | Pruebas | Producción |
|---|---|---|
| Repositorio | `olmogaldaz/gomezaldaz-pruebas` | `olmogaldaz/olmogaldaz.github.io` |
| Dominio | `pruebas.gomezaldaz.com` | `gomezaldaz.com` |
| `url` | `https://pruebas.gomezaldaz.com` | `https://gomezaldaz.com` |
| `public_url` | `https://gomezaldaz.com` | `https://gomezaldaz.com` |
| `indexable` | `false` | `true` |
| Google Analytics | Desactivado | Activado |
| Meta `noindex` | Sí | No |
| Sitemap anunciado en `robots.txt` | No | Sí |

### Archivos que deben ser diferentes

Solo estos dos archivos activos deben mantenerse distintos entre repositorios:

```text
_config.yml
CNAME
```

Configuración de pruebas:

```yml
url: https://pruebas.gomezaldaz.com
public_url: https://gomezaldaz.com
indexable: false
markdown: kramdown
```

Configuración de producción:

```yml
url: https://gomezaldaz.com
public_url: https://gomezaldaz.com
indexable: true
markdown: kramdown
```

El archivo `CNAME` contiene el dominio propio de cada entorno.

La variable `indexable` controla automáticamente:

- la presencia de `noindex, nofollow, noarchive, nosnippet` en el layout;
- la activación o desactivación de Google Analytics;
- la inclusión o ausencia del sitemap en `robots.txt`.

La variable `public_url` hace que las URL canónicas y los enlaces `hreflang` apunten siempre a la web pública, incluso cuando la página se compila en el entorno de pruebas.

### Google Analytics

En ambos repositorios existen:

```text
_includes/google-analytics.html
_includes/google-analytics-production.html
_includes/google-analytics-pruebas.html
```

`google-analytics.html` selecciona automáticamente la variante según `site.indexable`.

### `robots.txt`

El mismo archivo se utiliza en ambos repositorios. En pruebas permite el rastreo para que los buscadores puedan leer el `noindex`, pero no anuncia sitemap. En producción permite el rastreo y anuncia el sitemap público.

### Traslado de cambios entre entornos

Al copiar cambios de pruebas a producción:

1. No sobrescribir `_config.yml`.
2. No sobrescribir `CNAME`.
3. Copiar el resto de archivos sin cambiar la lógica de entorno.
4. Comprobar que producción no genera `noindex`.
5. Comprobar que Analytics está activo solo en producción.
6. Comprobar que `robots.txt` anuncia el sitemap solo en producción.

---

## Copias de emergencia

Ambos repositorios contienen las dos variantes completas de los archivos de entorno:

```text
.github/environment-backups/
├── CNAME.production
├── CNAME.pruebas
├── _config.production.yml
└── _config.pruebas.yml
```

La carpeta `.github` se conserva en el repositorio, pero no se publica como parte de la web.

---

## Estructura general

```text
/
├── .github/
│   └── environment-backups/          # Copias de emergencia de ambos entornos
├── .gitignore                         # Exclusiones de Git; entre ellas, la salida generada _site/
├── index.html                         # Portada principal en español
├── en/                                # Versión inglesa
├── es/                                # Páginas interiores en español
├── _data/
│   ├── resources.yml                  # Catálogo central de páginas y PDF
│   └── media.yml                      # Fuente única de apariciones en medios
├── _includes/
│   ├── menu.html                      # Navegación principal
│   ├── media-items.html               # Generación de fichas del dosier de medios
│   ├── media-filters.html             # Interfaz bilingüe de búsqueda y filtros
│   ├── google-analytics.html          # Selector automático por entorno
│   ├── google-analytics-production.html
│   └── google-analytics-pruebas.html
├── _layouts/
│   └── default.html                   # Layout, metadatos, indexación y Schema
├── css/
│   ├── style.css                      # Estilos globales
│   ├── mobile.css                     # Responsive global y menú móvil
│   └── media-filters.css              # Estilos propios de búsqueda y filtros
├── js/
│   ├── menu.js                        # Comportamiento interactivo del menú
│   └── media-filters.js               # Búsqueda, filtros y estado en URL del dosier
├── img/                               # Imágenes y recursos gráficos
├── docs/                              # Documentos públicos y PDF
├── sitemap.xml                        # Plantilla Liquid del sitemap
├── robots.txt                         # Plantilla Liquid por entorno
├── _config.yml                        # Configuración activa del entorno
├── 404.html                           # Página de error
├── CNAME                              # Dominio activo del entorno
└── README.md                          # Documentación del proyecto
```

---

## Organización bilingüe

### Español

- `/` — portada oficial en español
- `/es/` — ruta técnica de compatibilidad hacia `/`
- `/es/autor/`
- `/es/contacto/`
- `/es/historia/`
- `/es/demanda/`
- `/es/sentencia/`
- `/es/memoria/`
- `/es/genus-homo/`
- `/es/obra/`
- `/es/prensa/`

### Inglés

- `/en/` — portada oficial en inglés
- `/en/author/`
- `/en/contact/`
- `/en/story/`
- `/en/claim/`
- `/en/sentence/`
- `/en/memory/`
- `/en/genus-homo/`
- `/en/work/`
- `/en/press/`

Cada página declara su idioma, su URL equivalente y sus metadatos propios. El layout genera los enlaces `hreflang` español/inglés utilizando `public_url`.

---

## Navegación

La estructura del menú se genera en `_includes/menu.html`. El layout lo incorpora mediante `{% include menu.html %}`. El archivo `/js/menu.js` se limita al comportamiento interactivo, especialmente en móvil.

El pie contiene una fila independiente de accesos de utilidad, sin duplicar el menú estructural. El orden vigente es:

- Español: `Libros · Notas de prensa · Contacto`
- Inglés: `Books · Press releases · Contact`

Sus destinos son `/es/obra/libros/`, `/es/prensa/notas-de-prensa/`, `/es/contacto/` y sus equivalentes ingleses. Los tres accesos se distribuyen en columnas izquierda, centro y derecha. El selector `ES | EN` permanece separado y no debe partirse entre líneas.

---

## Contacto

Las páginas generales de contacto son:

- `/es/contacto/`
- `/en/contact/`

Ofrecen dos vías:

- contacto general: `contacto@gomezaldaz.com`;
- prensa y medios de comunicación: `prensa@gomezaldaz.com`.

Las páginas `/es/autor/` y `/en/author/` ya no contienen formulario de contacto. Las páginas de Genus Homo tampoco utilizan formulario: mantienen un acceso contextual mediante `mailto:` a `contacto@gomezaldaz.com` con el asunto `Genus Homo`.

El antiguo JavaScript específico de formularios (`/js/contact.js`) fue eliminado al dejar de existir formularios de contacto en las páginas activas.

---

## CSS

Los estilos se organizan por alcance:

- `/css/style.css`: estilos globales de la web.
- `/css/mobile.css`: reglas responsive globales y menú móvil.
- `/css/media-filters.css`: estilos exclusivos de la búsqueda y los filtros del dosier de medios, incluido su responsive.

Las hojas globales `style.css` y `mobile.css` se cargan desde el layout con un parámetro de versión basado en la hora de compilación de Jekyll. Así, cada despliegue genera una URL distinta y evita que el navegador conserve una versión anterior de los estilos.

El layout permite que una página declare hojas de estilo adicionales mediante `extra_css` en el front matter. Así, los estilos específicos no se cargan en el resto del sitio.

Las páginas del dosier declaran:

```yml
extra_css:
  - /css/media-filters.css
```

---

## Layout, metadatos y Schema

El archivo `_layouts/default.html` centraliza:

- título y descripción;
- control automático de `noindex`;
- URL canónica basada en `public_url`;
- iconos y hojas de estilo globales;
- versionado de las hojas CSS globales para evitar caché obsoleta;
- carga opcional de CSS específico mediante `extra_css`;
- enlaces `hreflang` basados en `public_url`;
- nodo Schema `Person` común;
- incorporación de los nodos Schema específicos de cada página;
- Google Analytics según el entorno;
- menú, contenido, pie y JavaScript común.

El nodo `Person` se genera siempre desde el layout. Los nodos específicos de cada página se declaran en su front matter mediante `schema_nodes` y el layout los serializa con `jsonify`.

Una página puede contener varios nodos Schema. El nodo que representa la URL concreta puede ser `WebPage` o uno de sus subtipos, como `ProfilePage` o `CollectionPage`.

---

## Catálogo central de recursos

`_data/resources.yml` es el catálogo central de recursos públicos e indexables de producción. Contiene dos grupos:

- `html`: páginas HTML públicas;
- `pdf`: documentos PDF públicos.

Las entradas HTML pueden contener `url`, `lang`, `alternate`, `published`, `modified` e `images`.

El layout localiza la entrada de la página actual comparando `page.url` con `resource.url` y deja disponibles las variables `resource_published` y `resource_modified`.

El front matter de cada página indica mediante `schema_date_target` qué nodo Schema representa su URL concreta. Durante la compilación, el layout incorpora automáticamente `datePublished` y `dateModified` a ese nodo cuando existen las fechas correspondientes en `_data/resources.yml`.

---

## Sitemap

`sitemap.xml` es una plantilla Liquid generada desde `_data/resources.yml`. Produce automáticamente:

- las URL HTML;
- `lastmod` cuando existe `modified`;
- los enlaces alternativos `hreflang`;
- los datos opcionales de imágenes;
- las URL de documentos PDF y su `lastmod` cuando existe.

Tanto en pruebas como en producción, las URL incluidas en el sitemap apuntan a `https://gomezaldaz.com`.

Las páginas de contacto están incorporadas a `_data/resources.yml`; por tanto, `/es/contacto/` y `/en/contact/` se incluyen automáticamente en el sitemap junto con su `lastmod` y sus alternancias de idioma. Su fecha de creación se conserva en `published` para generar `datePublished` en Schema.

---

## Indexación

### Pruebas

- `indexable: false`;
- todas las páginas generan `noindex, nofollow, noarchive, nosnippet`;
- canonical y `hreflang` apuntan a producción;
- `robots.txt` permite el rastreo, pero no anuncia sitemap;
- Google Analytics permanece desactivado.

### Producción

- `indexable: true`;
- no se genera `noindex`;
- canonical y `hreflang` apuntan a producción;
- `robots.txt` anuncia `https://gomezaldaz.com/sitemap.xml`;
- Google Analytics permanece activo.

---

## Obra / Work

La sección Obra / Work organiza cuatro líneas principales:

- Libros / Books
- Testimonios / Testimonies
- Adopción / Adoption
- Bebés robados / Stolen babies

Rutas principales:

- `/es/obra/` y `/en/work/`
- `/es/obra/libros/` y `/en/work/books/`
- `/es/obra/testimonios/` y `/en/work/testimonies/`
- `/es/obra/adopcion/` y `/en/work/adoption/`
- `/es/obra/bebes-robados/` y `/en/work/stolen-babies/`

---

## Prensa y notas de prensa

Las secciones de prensa distinguen entre cobertura de medios externos y notas emitidas directamente por Olmo Gómez Aldaz.

Rutas principales:

- `/es/prensa/`
- `/en/press/`
- `/es/prensa/medios/`
- `/en/press/media/`
- `/es/prensa/notas-de-prensa/`
- `/en/press/press-releases/`

### Dosier de medios

Las apariciones en medios se mantienen en una única fuente de datos:

```text
_data/media.yml
```

Las páginas `/es/prensa/medios/` y `/en/press/media/` conservan el front matter, Schema, textos de presentación, cabeceras y organización de secciones, pero las fichas individuales ya no se escriben dos veces en HTML.

Durante la compilación:

```text
_data/media.yml
      ↓
_includes/media-items.html
      ↓
/es/prensa/medios/ + /en/press/media/
```

Cada registro puede contener, según el caso:

- `id`
- `section`
- `date`
- `type`
- `territory`
- `medium`
- `meta_es` / `meta_en`
- `title_es` / `title_en`
- `subtitle_es` / `subtitle_en`
- `url` o `url_es` / `url_en`
- `action_es` / `action_en`
- `original_url` y `archived` para noticias retiradas
- `title_note_es` / `title_note_en` para aclaraciones ligadas al título
- `extra_url_es` / `extra_url_en` y acciones correspondientes cuando una ficha necesita un segundo enlace

Los campos de subtítulo admiten HTML puntual cuando sea necesario conservar elementos de presentación existentes, por ejemplo cursivas o enlaces internos.

Los campos `date`, `type`, `territory` y `medium` alimentan los filtros y sus opciones disponibles. No existe una segunda lista independiente que determine qué valores existen.

### Búsqueda y filtros

La interfaz se genera desde `_includes/media-filters.html`, la lógica vive en `/js/media-filters.js` y su presentación en `/css/media-filters.css`.

Permite combinar:

- búsqueda de texto libre;
- año;
- tipo de medio;
- territorio;
- medio concreto.

La búsqueda de texto ignora mayúsculas, minúsculas y tildes, y recorre el contenido visible de cada ficha y sus metadatos. Los filtros se combinan entre sí y el contador muestra el número de resultados visibles.

Cuando una sección no contiene resultados, se oculta completa junto con su cabecera, texto introductorio y enlace «Volver arriba». Si no hay resultados se muestra un aviso bilingüe.

El estado se refleja en la query string mediante `q`, `year`, `type`, `territory` y `medium`. El canonical sigue siendo la URL base del dosier, ya que los filtros no crean páginas indexables independientes.

La interfaz utiliza mejora progresiva: sin JavaScript no se muestran controles inertes y el dosier completo permanece visible en el HTML generado por Jekyll.

### Mantenimiento del dosier

Para incorporar una nueva aparición en medios:

1. Añadir un único registro a `_data/media.yml`.
2. Completar las variantes ES/EN de los textos que procedan.
3. Asignar `section`, `type`, `territory`, `medium` y `date` normalizados.
4. Si la noticia ha desaparecido, conservar `original_url`, la URL archivada y `archived: true`.
5. No añadir manualmente la misma ficha a las dos páginas HTML.
6. Comprobar el resultado en pruebas antes de trasladarlo a producción.

Las páginas índice de notas de prensa pueden utilizar `CollectionPage`; las notas individuales, `NewsArticle`; y las páginas generales de prensa, `WebPage`.

---

## Documentos públicos

La carpeta `/docs/` contiene PDF y otros documentos públicos enlazados desde la web o incluidos en el catálogo de recursos.

Los documentos anonimizados deben contener una eliminación real de los datos personales, no una simple cobertura visual.

---

## Cambios técnicos consolidados

### 5 y 6 de agosto de 2026

- Creación de `_data/resources.yml` como catálogo central de páginas HTML y PDF.
- Conversión de `sitemap.xml` en una plantilla generada desde ese catálogo.
- Generación automática de `lastmod`, `hreflang` e imágenes del sitemap.
- Separación de los estilos responsive en `css/mobile.css`.
- Centralización de la navegación estructural en `_includes/menu.html`.
- Actualización del nodo Schema `Person` y del pie bilingüe.
- Incorporación automática de `datePublished` y `dateModified` al nodo indicado por `schema_date_target`.
- Creación de los entornos diferenciados de pruebas y producción.
- Automatización de `noindex`, canonical, `hreflang`, Google Analytics y `robots.txt` según el entorno.
- Creación de copias de emergencia de `_config.yml` y `CNAME` para ambos entornos.

### 11 de agosto de 2026

- Creación de `_data/media.yml` como fuente única del dosier de medios.
- Creación de `_includes/media-items.html` para generar las fichas bilingües.
- Migración de `/es/prensa/medios/` y `/en/press/media/` desde fichas HTML duplicadas a datos estructurados.
- Conservación de noticias archivadas, URLs originales, enlaces documentales adicionales y formato HTML puntual.
- Normalización de `date`, `type`, `territory` y `medium` para búsqueda y filtros.
- Incorporación de búsqueda libre y filtros combinables por año, tipo, territorio y medio.
- Incorporación de contador de resultados, limpieza de filtros, ocultación de secciones vacías y estado compartible mediante query string.
- Mejora progresiva para conservar el dosier completo cuando JavaScript no está disponible.
- Creación de `/css/media-filters.css` y extracción de los estilos del buscador fuera de los CSS globales.
- Incorporación de `extra_css` en el layout para cargar hojas de estilo específicas solo en las páginas que las declaran.
- Creación de `/es/contacto/` y `/en/contact/` con contacto general y contacto específico para prensa y medios.
- Incorporación de `published` y `modified` para las nuevas páginas de contacto en `_data/resources.yml`.
- Eliminación de los formularios de `/es/autor/`, `/en/author/`, `/es/genus-homo/` y `/en/genus-homo/`, y eliminación de `/js/contact.js`.
- Sustitución de los formularios de Genus Homo por contacto directo mediante correo electrónico.
- Incorporación al pie de los accesos `Libros · Notas de prensa · Contacto` y sus equivalentes ingleses.
- Ajuste responsive del pie para conservar la distribución de los tres accesos y mantener `ES | EN` inseparable.
- Versionado automático de las hojas CSS globales en cada compilación para evitar caché obsoleta tras los despliegues.
- Eliminación del `_site/` generado accidentalmente en una compilación anterior y exclusión permanente de esa salida mediante `.gitignore`.

---

## Reglas de mantenimiento

- La raíz `/` es la portada oficial en español.
- `/en/` es la portada oficial en inglés.
- `/es/` se conserva como ruta técnica de compatibilidad.
- Las páginas interiores españolas viven bajo `/es/`.
- Las páginas inglesas viven bajo `/en/`.
- Los documentos públicos viven bajo `/docs/`.
- Las URL públicas y sus fechas se mantienen en `_data/resources.yml`.
- Las apariciones del dosier de medios se mantienen en `_data/media.yml`.
- Los filtros del dosier deben derivar sus opciones de los registros existentes, no de una lista paralela.
- Los estilos específicos de una página deben declararse mediante `extra_css` cuando no sean globales.
- El sitemap no debe volver a convertirse en una lista manual de URL.
- El menú estructural debe mantenerse en `_includes/menu.html`.
- Los accesos de utilidad del pie se mantienen en `_layouts/default.html` y no deben confundirse con el menú principal.
- `menu.js` debe limitarse al comportamiento interactivo del menú.
- `media-filters.js` debe limitarse a la búsqueda y filtrado del dosier.
- Los estilos globales y responsive deben mantenerse separados de los estilos específicos de componentes o páginas cuando corresponda.
- Los nodos Schema específicos deben mantenerse en el front matter de cada página.
- El nodo Schema que representa cada URL será el destinatario de las fechas centralizadas.
- `_site/` es salida generada por Jekyll y no debe incorporarse al repositorio.
- `_config.yml` y `CNAME` no deben copiarse directamente entre entornos.
- Los archivos comunes deben mantenerse iguales en ambos repositorios.
- Tras cada despliegue debe comprobarse el estado de indexación, Analytics, canonical, `hreflang`, `robots.txt` y sitemap.

Este README documenta la arquitectura principal y vigente del proyecto a **11 de agosto de 2026**.
