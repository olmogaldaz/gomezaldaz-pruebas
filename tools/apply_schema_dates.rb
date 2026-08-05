require 'yaml'
require 'json'
require 'date'

resources = YAML.load_file('_data/resources.yml').fetch('html')
aux = %w[Person Organization WebSite]
press_prefixes = ['/es/prensa/notas-de-prensa/', '/en/press/press-releases/']
press_indexes = press_prefixes
pending = []
modified = []
report = []

path_for = ->(url) { url == '/' ? 'index.html' : File.join(url.sub(%r{^/}, '').sub(%r{/$}, ''), 'index.html') }

resources.each do |resource|
  url = resource.fetch('url')
  path = path_for.call(url)
  text = File.read(path)
  match = text.match(/\A---\s*\n(.*?)\n---\s*\n/m)
  unless match
    pending << [path, url, 'sin front matter']
    next
  end

  data = YAML.safe_load(match[1], permitted_classes: [Date, Time], aliases: true) || {}
  body = text[match.end(0)..] || ''
  nodes = data['schema_nodes']
  unless nodes.is_a?(Array) && !nodes.empty?
    pending << [path, url, 'schema_nodes ausente o vacío; requeriría crear un nodo principal']
    next
  end

  full_url = "https://gomezaldaz.com#{url}"
  individual_press = press_prefixes.any? { |prefix| url.start_with?(prefix) } && !press_indexes.include?(url)

  if individual_press
    articles = nodes.select { |node| node.is_a?(Hash) && node['@type'] == 'Article' && node['url'] == full_url }
    if articles.size != 1 || !articles.first['datePublished']
      pending << [path, url, 'Article histórico no inequívoco']
      next
    end

    article = articles.first
    article_id = "#{full_url}#article"
    webpage_id = "#{full_url}#webpage"
    article['@id'] = article_id
    article.delete('dateModified')
    article['mainEntityOfPage'] = { '@id' => webpage_id }
    webpage = {
      '@type' => 'WebPage',
      '@id' => webpage_id,
      'url' => full_url,
      'name' => article['name'],
      'description' => article['description'],
      'inLanguage' => article['inLanguage'],
      'mainEntity' => { '@id' => article_id }
    }
    nodes.insert(nodes.index(article), webpage)
    data['schema_date_target'] = webpage_id
    report << [path, url, 'WebPage', webpage_id, 'WebPage separado del Article histórico']
  else
    candidates = nodes.select do |node|
      node.is_a?(Hash) && node['url'] == full_url && !aux.include?(node['@type'])
    end
    if candidates.size != 1
      pending << [path, url, "#{candidates.size} nodos principales candidatos; requeriría crear o rediseñar nodo"]
      next
    end

    target = candidates.first
    target.delete('datePublished')
    target.delete('dateModified')
    data['schema_date_target'] = target['@id']
    report << [path, url, target['@type'], target['@id'], 'nodo principal existente']
  end

  data['schema_nodes'] = nodes
  yaml = YAML.dump(data, line_width: -1).sub(/\A---\s*\n/, '')
  File.write(path, "---\n#{yaml}---\n\n#{body.sub(/\A\n*/, '')}")
  modified << path
end

layout_path = '_layouts/default.html'
layout = File.read(layout_path)
old = <<~'LIQUID'.rstrip
  {% if page.schema_nodes %}
    {% for schema_node in page.schema_nodes %}
      {% capture custom_node %}
      ,
      {{ schema_node | jsonify }}
      {% endcapture %}

      {% assign schema_nodes = schema_nodes | append: custom_node %}
    {% endfor %}
  {% endif %}
LIQUID
new = <<~'LIQUID'.rstrip
  {% if page.schema_nodes %}
    {% for schema_node in page.schema_nodes %}
      {% assign serialized_schema_node = schema_node | jsonify %}
      {% if page.schema_date_target and schema_node['@id'] == page.schema_date_target %}
        {% assign serialized_schema_node_size = serialized_schema_node | size | minus: 1 %}
        {% assign serialized_schema_node_without_closing_brace = serialized_schema_node | slice: 0, serialized_schema_node_size %}
        {% capture dated_schema_node %}{{ serialized_schema_node_without_closing_brace }}{% if resource_published %},"datePublished":{{ resource_published | jsonify }}{% endif %}{% if resource_modified %},"dateModified":{{ resource_modified | jsonify }}{% endif %}}{% endcapture %}
        {% assign serialized_schema_node = dated_schema_node | strip %}
      {% endif %}
      {% capture custom_node %}
      ,
      {{ serialized_schema_node }}
      {% endcapture %}

      {% assign schema_nodes = schema_nodes | append: custom_node %}
    {% endfor %}
  {% endif %}
LIQUID
abort 'bloque del layout no encontrado' unless layout.include?(old)
File.write(layout_path, layout.sub(old, new))
modified << layout_path

puts "PAGES_REVIEWED=#{resources.size}"
puts "PAGES_MODIFIED=#{modified.count { |path| path.end_with?('index.html') }}"
puts "PAGES_PENDING=#{pending.size}"
puts 'TARGET_REPORT_BEGIN'
report.each { |row| puts row.join(' | ') }
puts 'TARGET_REPORT_END'
puts 'PENDING_BEGIN'
pending.each { |row| puts row.join(' | ') }
puts 'PENDING_END'
