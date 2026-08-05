from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESOURCES = ROOT / "_data" / "resources.yml"
RESOURCE_RE = re.compile(r'^\s*- \{(?P<body>.*)\}\s*$')
FIELD_RE = re.compile(r'(?P<key>url|published|modified):\s*"(?P<value>[^"]+)"')
LOCAL_IMG_RE = re.compile(r'<img\b[^>]*\bsrc=["\'](?P<src>/img/[^"\']+)["\']', re.I)
PAGE_TYPES = {"WebPage", "ProfilePage", "CollectionPage", "AboutPage", "ContactPage", "ItemPage", "FAQPage", "SearchResultsPage", "QAPage", "CheckoutPage", "MedicalWebPage", "RealEstateListing"}
COLLECTION_URLS = {"/es/obra/libros/", "/en/work/books/", "/es/prensa/medios/", "/en/press/media/", "/es/prensa/notas-de-prensa/", "/en/press/press-releases/"}


def resource_to_file(url: str) -> Path:
    return ROOT / "index.html" if url == "/" else ROOT / url.strip("/") / "index.html"


def parse_resources(lines: list[str]) -> list[dict[str, str]]:
    entries = []
    in_html = False
    for idx, line in enumerate(lines):
        if line.strip() == "html:":
            in_html = True
            continue
        if line.strip() == "pdf:":
            break
        if not in_html:
            continue
        match = RESOURCE_RE.match(line)
        if not match:
            continue
        fields = {m.group("key"): m.group("value") for m in FIELD_RE.finditer(match.group("body"))}
        if "url" in fields:
            fields["line_index"] = str(idx)
            entries.append(fields)
    return entries


def split_front_matter(text: str) -> tuple[str, list[str], str]:
    if not text.startswith("---\n"):
        raise ValueError("front matter ausente")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("front matter sin cierre")
    return text[:4], text[4:end].splitlines(), text[end:]


def top_value(lines: list[str], key: str) -> str:
    for line in lines:
        if line.startswith(f"{key}:"):
            return line.split(":", 1)[1].strip()
    raise ValueError(f"campo {key} ausente")


def schema_bounds(lines: list[str]) -> tuple[int | None, int]:
    start = next((i for i, line in enumerate(lines) if line.strip() == "schema_nodes:"), None)
    if start is None:
        return None, len(lines)
    end = len(lines)
    for i in range(start + 1, len(lines)):
        line = lines[i]
        if line and not line.startswith(" ") and re.match(r'^[A-Za-z_][A-Za-z0-9_-]*:', line):
            end = i
            break
    return start, end


def node_ranges(lines: list[str], start: int, end: int) -> list[tuple[int, int]]:
    starts = [i for i in range(start + 1, end) if re.match(r'^  - ', lines[i])]
    return [(a, starts[pos + 1] if pos + 1 < len(starts) else end) for pos, a in enumerate(starts)]


def node_value(block: list[str], key: str) -> str | None:
    key_re = re.escape(key)
    pattern = re.compile(r'^(?:  - |    )["\']?' + key_re + r'["\']?:\s*["\']?([^"\'\n]+)', re.M)
    match = pattern.search("\n".join(block))
    return match.group(1).strip() if match else None


def replace_node_value(block: list[str], key: str, value: str) -> None:
    key_re = re.escape(key)
    pattern = re.compile(r'^((?:  - |    )["\']?' + key_re + r'["\']?:\s*)["\']?[^"\'\n]+["\']?\s*$')
    for i, line in enumerate(block):
        if pattern.match(line):
            block[i] = pattern.sub(r'\1"' + value + '"', line)
            return


def insert_dates(block: list[str], published: str | None, modified: str | None) -> bool:
    text = "\n".join(block)
    additions = []
    if published and not re.search(r'^\s{4}datePublished:', text, re.M):
        additions.append(f'    datePublished: "{published}"')
    if modified and not re.search(r'^\s{4}dateModified:', text, re.M):
        additions.append(f'    dateModified: "{modified}"')
    if not additions:
        return False
    relation_keys = {"isPartOf:", "about:", "mainEntity:", "author:", "publisher:", "primaryImageOfPage:", "breadcrumb:", "hasPart:", "mainEntityOfPage:"}
    insert_at = len(block)
    for i, line in enumerate(block[1:], start=1):
        if line.startswith("    ") and not line.startswith("      ") and line.strip() in relation_keys:
            insert_at = i
            break
    block[insert_at:insert_at] = additions
    return True


def entity_suffix(node_type: str | None) -> str:
    mapping = {"Article": "article", "NewsArticle": "newsarticle", "ScholarlyArticle": "scholarlyarticle", "Organization": "organization", "Book": "book", "Report": "report", "CreativeWork": "creativework", "Thing": "thing"}
    return mapping.get(node_type or "", re.sub(r'[^a-z0-9]+', '', (node_type or "entity").lower()) or "entity")


def page_node_lines(url: str, title: str, description: str, lang: str, page_type: str, published: str | None, modified: str | None, main_entity_id: str | None) -> list[str]:
    abs_url = f"https://gomezaldaz.com{url}"
    out = ['  - "@context": "https://schema.org"', f'    "@type": {page_type}', f'    "@id": "{abs_url}#webpage"', f'    url: "{abs_url}"', f'    name: {title}', f'    description: {description}', f'    inLanguage: {lang}']
    if published:
        out.append(f'    datePublished: "{published}"')
    if modified:
        out.append(f'    dateModified: "{modified}"')
    out.extend(['    isPartOf:', '      "@id": "https://gomezaldaz.com/#website"'])
    if main_entity_id:
        out.extend(['    mainEntity:', f'      "@id": "{main_entity_id}"'])
    return out


def update_page(path: Path, entry: dict[str, str]) -> tuple[bool, list[str]]:
    url = entry["url"]
    text = path.read_text(encoding="utf-8")
    prefix, lines, suffix = split_front_matter(text)
    title, description, lang = top_value(lines, "title"), top_value(lines, "description"), top_value(lines, "lang")
    schema_start, schema_end = schema_bounds(lines)
    changed = False
    notes = []
    abs_url = f"https://gomezaldaz.com{url}"

    if schema_start is None:
        lines.append("schema_nodes:")
        schema_start, schema_end = len(lines) - 1, len(lines)
        changed = True
        notes.append("creado schema_nodes")

    ranges = node_ranges(lines, schema_start, schema_end)
    entity_id = None
    is_press_release = (("/notas-de-prensa/" in url or "/press-releases/" in url) and not url.endswith("/notas-de-prensa/") and not url.endswith("/press-releases/"))

    for start, end in reversed(ranges):
        block = lines[start:end]
        node_type, node_url, node_id = node_value(block, "@type"), node_value(block, "url"), node_value(block, "@id")
        if is_press_release and node_url == abs_url and node_type == "Article":
            replace_node_value(block, "@type", "NewsArticle")
            node_type = "NewsArticle"
            changed = True
            notes.append("Article→NewsArticle")
        if node_url == abs_url and node_type in PAGE_TYPES:
            if insert_dates(block, entry.get("published"), entry.get("modified")):
                changed = True
                notes.append("fechas añadidas")
            lines[start:end] = block
        elif node_url == abs_url and node_type not in PAGE_TYPES:
            if node_id == f"{abs_url}#webpage":
                new_id = f"{abs_url}#{entity_suffix(node_type)}"
                old_id = node_id
                replace_node_value(block, "@id", new_id)
                lines[start:end] = block
                lines = [line.replace(old_id, new_id) for line in lines]
                entity_id = new_id
                changed = True
                notes.append(f"@id entidad corregido ({entity_suffix(node_type)})")
            elif node_id:
                entity_id = node_id

    schema_start, schema_end = schema_bounds(lines)
    assert schema_start is not None
    page_found = False
    for start, end in node_ranges(lines, schema_start, schema_end):
        block = lines[start:end]
        if node_value(block, "url") == abs_url and node_value(block, "@type") in PAGE_TYPES:
            page_found = True
            break
    if not page_found:
        page_type = "CollectionPage" if url in COLLECTION_URLS else "WebPage"
        lines[schema_end:schema_end] = page_node_lines(url, title, description, lang, page_type, entry.get("published"), entry.get("modified"), entity_id)
        changed = True
        notes.append(f"creado {page_type}")

    if changed:
        path.write_text(prefix + "\n".join(lines) + suffix, encoding="utf-8")
    return changed, notes


def add_unambiguous_images(resource_lines: list[str], entries: list[dict[str, str]]) -> int:
    count = 0
    for entry in entries:
        idx = int(entry["line_index"])
        line = resource_lines[idx]
        if "images:" in line:
            continue
        path = resource_to_file(entry["url"])
        if not path.exists():
            continue
        images = sorted(set(LOCAL_IMG_RE.findall(path.read_text(encoding="utf-8"))))
        if len(images) == 1:
            resource_lines[idx] = re.sub(r'}\s*$', f', images: [{{url: "{images[0]}"}}]}}', line)
            count += 1
    return count


def validate(entries: list[dict[str, str]]) -> None:
    errors = []
    for entry in entries:
        path = resource_to_file(entry["url"])
        if not path.exists():
            errors.append(f'{entry["url"]}: archivo ausente')
            continue
        _, lines, _ = split_front_matter(path.read_text(encoding="utf-8"))
        schema_start, schema_end = schema_bounds(lines)
        if schema_start is None:
            errors.append(f'{entry["url"]}: sin schema_nodes')
            continue
        abs_url = f'https://gomezaldaz.com{entry["url"]}'
        pages, ids = [], []
        for start, end in node_ranges(lines, schema_start, schema_end):
            block = lines[start:end]
            node_type, node_url, node_id = node_value(block, "@type"), node_value(block, "url"), node_value(block, "@id")
            if node_id:
                ids.append(node_id)
            if node_url == abs_url and node_type in PAGE_TYPES:
                pages.append(block)
        if len(pages) != 1:
            errors.append(f'{entry["url"]}: nodos de página={len(pages)}')
            continue
        page_text = "\n".join(pages[0])
        if entry.get("published") and f'datePublished: "{entry["published"]}"' not in page_text:
            errors.append(f'{entry["url"]}: falta datePublished')
        if entry.get("modified") and f'dateModified: "{entry["modified"]}"' not in page_text:
            errors.append(f'{entry["url"]}: falta dateModified')
        if len(ids) != len(set(ids)):
            errors.append(f'{entry["url"]}: @id duplicado')
    if errors:
        raise SystemExit("Validación fallida:\n" + "\n".join(f"- {e}" for e in errors))


def main() -> None:
    resource_lines = RESOURCES.read_text(encoding="utf-8").splitlines()
    entries = parse_resources(resource_lines)
    changed_pages = 0
    for entry in entries:
        path = resource_to_file(entry["url"])
        if path.exists():
            changed, notes = update_page(path, entry)
            if changed:
                changed_pages += 1
                print(entry["url"], "|", "; ".join(notes))
    image_count = add_unambiguous_images(resource_lines, entries)
    RESOURCES.write_text("\n".join(resource_lines) + "\n", encoding="utf-8")
    validate(entries)
    print(f"Páginas modificadas: {changed_pages}")
    print(f"Imágenes inequívocas añadidas: {image_count}")
    print("Validación completa: correcta")


if __name__ == "__main__":
    main()
