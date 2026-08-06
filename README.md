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

El archivo `CNAME` contiene el dominio propio de cada entorno:

```text
pruebas.gomezaldaz.com
```

o:

```text
gomezaldaz.com
```

### Archivos comunes y automáticos

El resto de la arquitectura debe mantenerse idéntico en ambos repositorios.

La variable `indexable` controla automáticamente:

- la presencia de `noindex, nofollow, noarchive, nosnippet` en el layout;
- la activación o desactivación de Google Analytics;
- la inclusión o ausencia del sitemap en `robots.txt`.

La variable `public_url` hace que las URL canónicas y los enlaces `hreflang` apunten siempre a la web pública, incluso cuando la página se compila en el entorno de pruebas.

El sitemap utiliza como base pública:

```text
https://gomezaldaz.com
```

Por tanto, el sitemap generado en pruebas sirve para comprobar la compilación, pero no contiene URL del subdominio de pruebas.

### Google Analytics

En ambos repositorios existen:

```text
_includes/google-analytics.html
_includes/google-analytics-production.html
_includes/google-analytics-pruebas.html
```

`google-analytics.html` es el selector automático:

```liquid
{% if site.indexable %}
  {% include google-analytics-production.html %}
{% else %}
  {% include google-analytics-pruebas.html %}
{% endif %}
```

La variante de producción contiene el código real de Analytics. La variante de pruebas no carga ningún script, para evitar que las comprobaciones contaminen las estadísticas.

### `robots.txt`

El mismo archivo se utiliza en ambos repositorios:

```liquid
---
layout: null
---

User-agent: *
Allow: /

{% if site.indexable %}
Sitemap: {{ site.public_url | default: site.url }}/sitemap.xml
{% endif %}
```

En pruebas permite el rastreo para que los buscadores puedan leer el `noindex`, pero no anuncia sitemap. En producción permite el rastreo y anuncia el sitemap público.

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

Estas copias tienen el mismo contenido en ambos repositorios.

Para restaurar producción:

- copiar el contenido de `_config.production.yml` al `_config.yml` de la raíz;
- copiar el contenido de `CNAME.production` al `CNAME` de la raíz.

Para restaurar pruebas:

- copiar el contenido de `_config.pruebas.yml` al `_config.yml` de la raíz;
- copiar el contenido de `CNAME.pruebas` al `CNAME` de la raíz.

La carpeta `.github` se conserva en el repositorio, pero no se publica como parte de la web.

---

## Estructura general

```text
/
├── .github/
│   └── environment-backups/          # Copias de emergencia de ambos entornos
├── index.html                         # Portada principal en español
├── en/                                # Versión inglesa
├── es/                                # Páginas interiores en español
├── _data/
│   └── resources.yml                  # Catálogo central de páginas y PDF
├── _includes/
│   ├── menu.html                      # Navegación principal
│   ├── google-analytics.html          # Selector automático por entorno
│   ├── google-analytics-production.html
│   └── google-analytics-pruebas.html
├── _layouts/
│   └── default.html                   # Layout, metadatos, indexación y Schema
├── css/
│   ├── style.css                      # Estilos generales y de escritorio
│   └── mobile.css                     # Adaptación responsive y menú móvil
├── js/
│   └── menu.js                        # Comportamiento interactivo del menú
├── img/                               # Imágenes y recursos gráficos
├── docs/                              # Documentos públicos y PDF
├── sitemap.xml                        # Plantilla Liquid del sitemap
├── robots.txt                         # Plantilla Liquid por entorno
├── _config.yml                        # Configuración activa del entorno
├── 404.html                           # Página de error
├── CNAME                              # Dominio activo del entorno
└── README.md                          # Documentación del proyecto
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

Cada página declara su idioma, su URL equivalente y sus metadatos propios. El layout genera los enlaces `hreflang` español/inglés utilizando `public_url`.

---

## Navegación

La estructura del menú se genera en:

```text
_includes/menu.html
```

El layout lo incorpora mediante `{% include menu.html %}`. El archivo `/js/menu.js` no construye el menú: se limita a gestionar su comportamiento interactivo, especialmente en móvil.

El título o logotipo del menú enlaza a la portada correspondiente y conserva su apariencia visual sin subrayado ni cambios de opacidad al pasar el cursor.

---

## CSS

Los estilos están separados en dos archivos:

- `/css/style.css`: estilos generales y de escritorio.
- `/css/mobile.css`: reglas responsive, adaptación a pantallas pequeñas y menú móvil.

El antiguo archivo `css/menu-mobile.css` fue eliminado. El layout carga únicamente `style.css` y `mobile.css`.

---

## Layout, metadatos y Schema

El archivo `_layouts/default.html` centraliza:

- título y descripción;
- control automático de `noindex`;
- URL canónica basada en `public_url`;
- iconos;
- hojas de estilo;
- enlaces `hreflang` basados en `public_url`;
- nodo Schema `Person` común;
- incorporación de los nodos Schema específicos de cada página;
- Google Analytics según el entorno;
- menú, contenido, pie y JavaScript común.

El nodo `Person` se genera siempre desde el layout. Los nodos específicos de cada página se declaran en su front matter mediante `schema_nodes` y el layout los serializa con `jsonify`.

Una página puede contener varios nodos Schema. El nodo que representa la URL concreta puede ser `WebPage` o uno de sus subtipos, como `ProfilePage` o `CollectionPage`. Otros nodos pueden representar personas, artículos, libros, organizaciones u otras entidades.

---

## Catálogo central de recursos

El archivo:

```text
_data/resources.yml
```

es el catálogo central de recursos públicos e indexables de producción.

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

Este catálogo evita mantener manualmente en el sitemap una segunda lista independiente de URL.

---

## Fechas centralizadas

El layout busca automáticamente la entrada de la página actual dentro de `site.data.resources.html` comparando `page.url` con `resource.url`.

Deja disponibles estas variables Liquid:

```liquid
resource_published
resource_modified
```

Su origen único es `_data/resources.yml`.

El front matter de cada página indica mediante `schema_date_target` qué nodo Schema representa su URL concreta. Durante la compilación, el layout incorpora automáticamente `datePublished` y `dateModified` a ese nodo cuando existen `published` y `modified` en `_data/resources.yml`.

La búsqueda y la inyección de fechas están centralizadas en el layout y no deben repetirse manualmente en cada archivo.

---

## Sitemap

`sitemap.xml` es una plantilla Liquid, no una lista manual de URL.

Durante la compilación de Jekyll:

```text
_data/resources.yml + sitemap.xml
                 ↓
       sitemap.xml publicado
```

La plantilla genera automáticamente:

- las URL HTML;
- `lastmod` cuando existe `modified`;
- los enlaces alternativos `hreflang`;
- los datos opcionales de imágenes;
- las URL de documentos PDF;
- `lastmod` de los PDF cuando está definido.

El sitemap publicado es un XML estático. Cuando Google lo solicita, GitHub Pages entrega el archivo ya compilado; no vuelve a leer `resources.yml` en cada petición.

Tanto en pruebas como en producción, las URL incluidas en el sitemap apuntan a `https://gomezaldaz.com`.

---

## Indexación

La indexación depende de `indexable`:

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

Las URL públicas deben mantenerse en `_data/resources.yml`. Al añadir, eliminar o modificar una página o un PDF, debe revisarse su entrada en ese catálogo central.

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

## Cambios técnicos consolidados el 5 y 6 de agosto de 2026

- Creación de `_data/resources.yml` como catálogo central de páginas HTML y PDF.
- Conversión de `sitemap.xml` en una plantilla generada desde ese catálogo.
- Generación automática de `lastmod`, `hreflang` e imágenes del sitemap.
- Separación de los estilos responsive en `css/mobile.css`.
- Eliminación de `css/menu-mobile.css`.
- Actualización del layout para cargar `style.css` y `mobile.css`.
- Conversión del título o logotipo del menú en enlace a la portada.
- Centralización de la navegación estructural en `_includes/menu.html`.
- Actualización del nodo Schema `Person` y del pie bilingüe.
- Incorporación automática de `datePublished` y `dateModified` al nodo indicado por `schema_date_target`.
- Creación de los entornos diferenciados de pruebas y producción.
- Automatización de `noindex`, canonical y `hreflang` mediante `_config.yml`.
- Automatización de Google Analytics según `indexable`.
- Automatización de `robots.txt` según `indexable`.
- Creación de copias de emergencia de `_config.yml` y `CNAME` para ambos entornos.
- Eliminación de notas temporales de paquetes de actualización ya integrados.

---

## Reglas de mantenimiento

- La raíz `/` es la portada oficial en español.
- `/en/` es la portada oficial en inglés.
- `/es/` se conserva como ruta técnica de compatibilidad.
- Las páginas interiores españolas viven bajo `/es/`.
- Las páginas inglesas viven bajo `/en/`.
- Los documentos públicos viven bajo `/docs/`.
- Las URL públicas y sus fechas se mantienen en `_data/resources.yml`.
- El sitemap no debe volver a convertirse en una lista manual de URL.
- El menú estructural debe mantenerse en `_includes/menu.html`.
- `menu.js` debe limitarse al comportamiento interactivo.
- Los estilos generales y responsive deben permanecer separados.
- Los nodos Schema específicos deben mantenerse en el front matter de cada página.
- El nodo Schema que representa cada URL será el destinatario de las fechas centralizadas.
- `_config.yml` y `CNAME` no deben copiarse directamente entre entornos.
- Los archivos comunes deben mantenerse iguales en ambos repositorios.
- Tras cada despliegue debe comprobarse el estado de indexación, Analytics, canonical, `hreflang`, `robots.txt` y sitemap.
- Las redirecciones técnicas antiguas solo se conservan cuando siguen siendo necesarias.

Este README documenta la arquitectura principal y vigente del proyecto a **6 de agosto de 2026**.
