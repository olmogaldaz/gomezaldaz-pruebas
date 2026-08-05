# gomezaldaz.com — Estructura y mantenimiento

Este repositorio contiene la estructura, el contenido y los recursos públicos de **gomezaldaz.com**.

La web se publica mediante GitHub Pages desde la rama `main` y la raíz del repositorio. El sitio es bilingüe, con la portada española en `/` y la versión inglesa en `/en/`.

---

## Publicación

Configuración actual:

- Rama de publicación: `main`
- Carpeta publicada: raíz del repositorio
- Dominio personalizado: `gomezaldaz.com`
- HTTPS activado
- Generación estática mediante Jekyll

Jekyll procesa Liquid, los datos YAML, los layouts y los includes durante cada compilación. GitHub Pages publica después archivos HTML, XML, CSS y JavaScript ya generados. Las peticiones de los visitantes o de los buscadores no vuelven a ejecutar Liquid.

---

## Estructura general

```text
/
├── index.html                  # Portada principal en español
├── en/                         # Versión inglesa
├── es/                         # Páginas interiores en español
├── _data/                      # Datos estructurados comunes
│   └── resources.yml           # Catálogo central de páginas y PDF
├── _includes/                  # Fragmentos comunes
│   └── menu.html               # Navegación principal
├── _layouts/
│   └── default.html            # Layout general, metadatos y Schema
├── css/
│   ├── style.css               # Estilos generales y de escritorio
│   └── mobile.css              # Adaptación responsive y menú móvil
├── js/
│   └── menu.js                 # Comportamiento interactivo del menú
├── img/                        # Imágenes y recursos gráficos
├── docs/                       # Documentos públicos y PDF
├── sitemap.xml                 # Plantilla Liquid del sitemap
├── robots.txt                  # Instrucciones para rastreadores
├── _config.yml                 # Configuración de Jekyll
├── 404.html                    # Página de error
├── CNAME                       # Dominio personalizado
└── README.md                   # Documentación del repositorio
```

Los archivos antiguos o temporales de paquetes de actualización no forman parte de la arquitectura vigente y deben eliminarse una vez integrados sus cambios.

---

## Organización bilingüe

### Español

- `/` — portada oficial en español
- `/es/` — ruta técnica de compatibilidad hacia `/`
- `/es/autor/`
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
- `/en/story/`
- `/en/claim/`
- `/en/sentence/`
- `/en/memory/`
- `/en/genus-homo/`
- `/en/work/`
- `/en/press/`

Cada página declara su idioma, su URL equivalente y sus metadatos propios. El layout genera los enlaces `hreflang` español/inglés.

---

## Navegación

La estructura del menú se genera en:

```text
_includes/menu.html
```

El layout lo incorpora con Liquid mediante `{% include menu.html %}`. El archivo `/js/menu.js` ya no construye el menú: se limita a gestionar su comportamiento interactivo, especialmente en móvil.

El título o logotipo del menú enlaza a la portada correspondiente y conserva su apariencia visual sin subrayado ni cambios de opacidad al pasar el cursor.

---

## CSS

Los estilos están separados en dos archivos:

- `/css/style.css`: estilos generales y de escritorio.
- `/css/mobile.css`: reglas responsive, adaptación a pantallas pequeñas y menú móvil.

El antiguo archivo `css/menu-mobile.css` fue eliminado. El layout carga únicamente `style.css` y `mobile.css`.

---

## Layout y Schema

El archivo `_layouts/default.html` centraliza:

- título y descripción;
- URL canónica;
- iconos;
- hojas de estilo;
- enlaces `hreflang`;
- nodo Schema `Person` común;
- incorporación de los nodos Schema específicos de cada página;
- menú, contenido, pie y JavaScript común.

El nodo `Person` se genera siempre desde el layout. Los nodos específicos de cada página se declaran en su front matter mediante `schema_nodes` y el layout los serializa con `jsonify`.

Una página puede contener varios nodos Schema. El nodo que representa la URL concreta puede ser `WebPage` o uno de sus subtipos, como `ProfilePage` o `CollectionPage`. Otros nodos pueden representar personas, artículos, libros, organizaciones u otras entidades.

---

## Catálogo central de recursos

El archivo:

```text
_data/resources.yml
```

es el catálogo central de recursos indexables.

Contiene dos grupos:

- `html`: páginas HTML públicas;
- `pdf`: documentos PDF públicos.

Las entradas HTML pueden contener:

- `url`
- `lang`
- `alternate`
- `published`
- `modified`
- `images`

Las imágenes pueden incluir:

- `url`
- `title`
- `caption`

Este catálogo evita mantener manualmente en el sitemap una segunda lista independiente de URLs.

---

## Fechas centralizadas

El layout busca automáticamente la entrada de la página actual dentro de `site.data.resources.html` comparando `page.url` con `resource.url`.

Deja disponibles estas variables Liquid:

```liquid
resource_published
resource_modified
```

Su origen único es `_data/resources.yml`.

Estas variables se han preparado para incorporarlas posteriormente, página por página, al nodo Schema que representa cada URL concreta. La lógica de búsqueda está centralizada en el layout y no tendrá que repetirse en cada archivo.

---

## Sitemap

`sitemap.xml` es una plantilla Liquid, no una lista manual de URLs.

Durante la compilación de Jekyll:

```text
_data/resources.yml + sitemap.xml
                 ↓
       sitemap.xml publicado
```

La plantilla genera automáticamente:

- las URLs HTML;
- `lastmod` cuando existe `modified`;
- los enlaces alternativos `hreflang`;
- los datos opcionales de imágenes;
- las URLs de documentos PDF;
- `lastmod` de los PDF cuando está definido.

El sitemap publicado es un XML estático. Cuando Google lo solicita, GitHub Pages entrega el archivo ya compilado; no vuelve a leer `resources.yml` en cada petición.

---

## Indexación

`robots.txt` permite el rastreo del sitio y declara:

```text
https://gomezaldaz.com/sitemap.xml
```

Las URLs indexables deben mantenerse en `_data/resources.yml`. Al añadir, eliminar o modificar una página o un PDF, debe revisarse su entrada en ese catálogo central.

Las correspondencias bilingües se declaran mediante `alternate` y se publican en el sitemap y en el HTML mediante `hreflang`.

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

Las páginas índice de notas de prensa pueden utilizar `CollectionPage`; las notas individuales, `NewsArticle`; y las páginas generales de prensa, `WebPage`.

---

## Documentos públicos

La carpeta `/docs/` contiene PDF y otros documentos públicos enlazados desde la web o incluidos en el catálogo de recursos.

Los documentos públicos pueden ser:

- resoluciones y reconocimientos;
- notas de prensa originales;
- entrevistas y revistas;
- informes de investigación;
- materiales documentales complementarios.

Los documentos anonimizados deben contener una eliminación real de los datos personales, no una simple cobertura visual.

---

## Cambios técnicos consolidados el 5 de agosto de 2026

- Creación de `_data/resources.yml` como catálogo central de páginas HTML y PDF.
- Conversión de `sitemap.xml` en una plantilla generada desde ese catálogo.
- Generación automática de `lastmod`, `hreflang` e imágenes del sitemap.
- Separación de los estilos responsive en `css/mobile.css`.
- Eliminación de `css/menu-mobile.css`.
- Actualización del layout para cargar `style.css` y `mobile.css`.
- Conversión del título o logotipo del menú en enlace a la portada.
- Ajustes visuales del enlace del título y de su foco de teclado.
- Centralización de la navegación estructural en `_includes/menu.html`.
- Actualización del nodo Schema `Person`, de las etiquetas del nombre registral anterior y del texto del pie en español e inglés.
- Incorporación en el layout de la búsqueda centralizada de `published` y `modified` para la página actual.
- Eliminación de notas temporales de paquetes de actualización ya integrados.

---

## Reglas de mantenimiento

- La raíz `/` es la portada oficial en español.
- `/en/` es la portada oficial en inglés.
- `/es/` se conserva como ruta técnica de compatibilidad.
- Las páginas interiores españolas viven bajo `/es/`.
- Las páginas inglesas viven bajo `/en/`.
- Los documentos públicos viven bajo `/docs/`.
- Las URLs indexables y sus fechas se mantienen en `_data/resources.yml`.
- El sitemap no debe volver a convertirse en una lista manual de URLs.
- El menú estructural debe mantenerse en `_includes/menu.html`.
- `menu.js` debe limitarse al comportamiento interactivo.
- Los estilos generales y responsive deben permanecer separados.
- Los nodos Schema específicos deben mantenerse en el front matter de cada página.
- El nodo Schema que representa cada URL será el destinatario de las fechas centralizadas.
- Las redirecciones técnicas antiguas solo se conservan cuando siguen siendo necesarias.

Este README documenta la arquitectura principal y vigente del proyecto a 5 de agosto de 2026.
