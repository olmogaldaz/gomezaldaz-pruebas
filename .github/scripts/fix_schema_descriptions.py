from pathlib import Path

pages = [
    Path('index.html'),
    Path('en/index.html'),
    Path('es/autor/index.html'),
    Path('en/author/index.html'),
]

for path in pages:
    text = path.read_text(encoding='utf-8')
    end = text.find('\n---\n', 4)
    if not text.startswith('---\n') or end < 0:
        raise AssertionError(f'Invalid front matter: {path}')
    front = text[4:end]
    body = text[end + 5:]
    lines = front.splitlines()
    top_description = next(line[len('description: '):] for line in lines if line.startswith('description: '))
    target = '    description: "{{ page.description }}"'
    if lines.count(target) != 1:
        raise AssertionError(f'Unexpected placeholder count: {path}')
    lines[lines.index(target)] = '    description: ' + top_description
    path.write_text('---\n' + '\n'.join(lines) + '\n---\n' + body, encoding='utf-8')
    new_text = path.read_text(encoding='utf-8')
    new_end = new_text.find('\n---\n', 4)
    if '{{ page.description }}' in new_text or new_text[new_end + 5:] != body:
        raise AssertionError(f'Validation failed: {path}')

Path('.github/workflows/fix-schema-descriptions.yml').unlink()
Path('.github/scripts/fix_schema_descriptions.py').unlink()
