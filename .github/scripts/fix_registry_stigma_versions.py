from pathlib import Path

ES = Path('es/obra/adopcion/estigma-registral-adopcion/index.html')
EN = Path('en/work/adoption/registry-stigma-of-adoption/index.html')
WORKFLOW = Path('.github/workflows/fix-registry-stigma-versions.yml')
SCRIPT = Path('.github/scripts/fix_registry_stigma_versions.py')


def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise AssertionError(f'{label}: expected 1 occurrence, found {count}')
    return text.replace(old, new, 1)


es_text = ES.read_text(encoding='utf-8')
en_text = EN.read_text(encoding='utf-8')

es_text = replace_once(es_text,
'''          <p>
            <strong>Estado:</strong> traducción pendiente.
          </p>''',
'''          <p>
            <strong>Título:</strong> <em>The Registry Stigma of Adoption. When Supposed Protection Becomes Discrimination</em><br>
            <strong>Autor:</strong> Olmo Gómez Aldaz<br>
            <strong>Fecha:</strong> 23 de junio de 2026<br>
            <strong>Versión:</strong> 1.0<br>
            <strong>Licencia:</strong> CC BY 4.0
          </p>

          <p>
            <strong>Zenodo · DOI general:</strong>
            <a href="https://doi.org/10.5281/zenodo.20820051" target="_blank" rel="noopener noreferrer">10.5281/zenodo.20820051</a><br>
            <strong>Zenodo · DOI versión v1.0:</strong>
            <a href="https://doi.org/10.5281/zenodo.20820052" target="_blank" rel="noopener noreferrer">10.5281/zenodo.20820052</a><br>
            <a href="/en/work/adoption/registry-stigma-of-adoption/">Ver página inglesa</a>
          </p>''', 'Spanish English-version block')

es_text = replace_once(es_text,
'La publicación está disponible en Zenodo en su versión española. La traducción inglesa está pendiente.',
'La publicación está disponible en Zenodo en español y en inglés.',
'Spanish access paragraph')

old_es_buttons = '''        <a class="cta" href="https://doi.org/10.5281/zenodo.20159685" target="_blank" rel="noopener noreferrer">Publicación en Zenodo</a>
        <a class="cta" href="/docs/el-estigma-registral-de-la-adopcion-v1.pdf" target="_blank" rel="noopener noreferrer">PDF local</a>'''
new_es_buttons = '''        <a class="cta" href="https://doi.org/10.5281/zenodo.20159685" target="_blank" rel="noopener noreferrer">Publicación española en Zenodo</a>
        <a class="cta" href="/docs/el-estigma-registral-de-la-adopcion-v1.pdf" target="_blank" rel="noopener noreferrer">PDF español</a>
        <a class="cta" href="https://doi.org/10.5281/zenodo.20820051" target="_blank" rel="noopener noreferrer">Publicación inglesa en Zenodo</a>
        <a class="cta" href="/docs/the-registry-stigma-of-adoption-v1.pdf" target="_blank" rel="noopener noreferrer">PDF inglés</a>'''
if es_text.count(old_es_buttons) != 2:
    raise AssertionError(f'Spanish buttons: expected 2 occurrences, found {es_text.count(old_es_buttons)}')
es_text = es_text.replace(old_es_buttons, new_es_buttons)

en_text = en_text.replace('https://doi.org/10.5281/zenodo.20159685', 'https://doi.org/10.5281/zenodo.20820051')
en_text = en_text.replace('/docs/el-estigma-registral-de-la-adopcion-v1.pdf', '/docs/the-registry-stigma-of-adoption-v1.pdf')
en_text = en_text.replace('Local PDF (Spanish)', 'Local PDF')

en_text = replace_once(en_text,
'''          <h3>Spanish version</h3>

          <p>
            <strong>Title:</strong> <em>El estigma registral de la adopción. Cuando la supuesta protección se convierte en discriminación</em><br>
            <strong>Author:</strong> Olmo Gómez Aldaz<br>
            <strong>Project:</strong> Undoing Adoption Project<br>
            <strong>ORCID:</strong> <a href="https://orcid.org/0009-0003-3362-6763" target="_blank" rel="noopener noreferrer">0009-0003-3362-6763</a><br>
            <strong>Date:</strong> 13 May 2026<br>
            <strong>Licence:</strong> CC BY 4.0
          </p>

          <p>
            <strong>Zenodo · General DOI:</strong>
            <a href="https://doi.org/10.5281/zenodo.20820051" target="_blank" rel="noopener noreferrer">10.5281/zenodo.20159685</a><br>
            <strong>Zenodo · DOI version v1.0:</strong>
            <a href="https://doi.org/10.5281/zenodo.20159686" target="_blank" rel="noopener noreferrer">10.5281/zenodo.20159686</a>
          </p>''',
'''          <h3>English version</h3>

          <p>
            <strong>Title:</strong> <em>The Registry Stigma of Adoption. When Supposed Protection Becomes Discrimination</em><br>
            <strong>Author:</strong> Olmo Gómez Aldaz<br>
            <strong>Project:</strong> Undoing Adoption Project<br>
            <strong>ORCID:</strong> <a href="https://orcid.org/0009-0003-3362-6763" target="_blank" rel="noopener noreferrer">0009-0003-3362-6763</a><br>
            <strong>Date:</strong> 23 June 2026<br>
            <strong>Version:</strong> 1.0<br>
            <strong>Licence:</strong> CC BY 4.0
          </p>

          <p>
            <strong>Zenodo · General DOI:</strong>
            <a href="https://doi.org/10.5281/zenodo.20820051" target="_blank" rel="noopener noreferrer">10.5281/zenodo.20820051</a><br>
            <strong>Zenodo · DOI version v1.0:</strong>
            <a href="https://doi.org/10.5281/zenodo.20820052" target="_blank" rel="noopener noreferrer">10.5281/zenodo.20820052</a>
          </p>''', 'English primary-version block')

en_text = replace_once(en_text,
'''          <h3>English version</h3>

          <p>
            <strong>Status:</strong> translation pending.
          </p>''',
'''          <h3>Spanish version</h3>

          <p>
            <strong>Title:</strong> <em>El estigma registral de la adopción. Cuando la supuesta protección se convierte en discriminación</em><br>
            <strong>Date:</strong> 13 May 2026<br>
            <strong>Version:</strong> 1.0
          </p>

          <p>
            <strong>Zenodo · General DOI:</strong>
            <a href="https://doi.org/10.5281/zenodo.20159685" target="_blank" rel="noopener noreferrer">10.5281/zenodo.20159685</a><br>
            <strong>Zenodo · DOI version v1.0:</strong>
            <a href="https://doi.org/10.5281/zenodo.20159686" target="_blank" rel="noopener noreferrer">10.5281/zenodo.20159686</a><br>
            <a href="/es/obra/adopcion/estigma-registral-adopcion/">View Spanish page</a>
          </p>''', 'English Spanish-version block')

en_text = replace_once(en_text,
'The publication is available on Zenodo in its Spanish version. The full English translation is pending.',
'The publication is available on Zenodo in English and Spanish.',
'English access paragraph')

en_text = replace_once(en_text,
'''Gómez Aldaz, Olmo. <em>El estigma registral de la adopción. Cuando la supuesta protección se convierte en discriminación</em>. 13 May 2026. Zenodo. DOI:
        <a href="https://doi.org/10.5281/zenodo.20159686" target="_blank" rel="noopener noreferrer">10.5281/zenodo.20159686</a>.''',
'''Gómez Aldaz, Olmo. <em>The Registry Stigma of Adoption. When Supposed Protection Becomes Discrimination</em>. 23 June 2026. Zenodo. DOI:
        <a href="https://doi.org/10.5281/zenodo.20820052" target="_blank" rel="noopener noreferrer">10.5281/zenodo.20820052</a>.''', 'English recommended citation')

for label, text in [('Spanish', es_text), ('English', en_text)]:
    for phrase in ['traducción pendiente', 'translation pending', 'translation is pending']:
        if phrase in text:
            raise AssertionError(f'{label}: pending text remains: {phrase}')

for required in ['10.5281/zenodo.20820051', '10.5281/zenodo.20820052', '/docs/the-registry-stigma-of-adoption-v1.pdf']:
    if required not in es_text or required not in en_text:
        raise AssertionError(f'Missing required value: {required}')

ES.write_text(es_text, encoding='utf-8')
EN.write_text(en_text, encoding='utf-8')
WORKFLOW.unlink()
SCRIPT.unlink()
