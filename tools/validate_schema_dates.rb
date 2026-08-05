require 'yaml'
require 'json'
require 'date'

resources = YAML.load_file('_data/resources.yml').fetch('html')
errors = []
checked = 0
pending = 0
patterns = Hash.new { |hash, key| hash[key] = [] }

resources.each do |resource|
  url = resource.fetch('url')
  source = url == '/' ? 'index.html' : File.join(url.sub(%r{^/}, '').sub(%r{/$}, ''), 'index.html')
  front = File.read(source).match(/\A---\s*\n(.*?)\n---\s*\n/m)
  data = YAML.safe_load(front[1], permitted_classes: [Date, Time], aliases: true)
  target_id = data['schema_date_target']
  unless target_id
    pending += 1
    next
  end

  output = url == '/' ? '_site/index.html' : File.join('_site', url.sub(%r{^/}, ''), 'index.html')
  scripts = File.read(output).scan(/<script type="application\/ld\+json">(.*?)<\/script>/m).flatten
  begin
    graph = JSON.parse(scripts.fetch(0))
    nodes = graph.is_a?(Array) ? graph : [graph]
  rescue => error
    errors << "#{url}: JSON inválido #{error.message}"
    next
  end

  targets = nodes.select { |node| node.is_a?(Hash) && node['@id'] == target_id }
  if targets.size != 1
    errors << "#{url}: objetivo aparece #{targets.size} veces"
    next
  end

  target = targets.first
  expected_published = resource['published']
  expected_modified = resource['modified']
  published_ok = expected_published ? target['datePublished'] == expected_published : !target.key?('datePublished')
  modified_ok = expected_modified ? target['dateModified'] == expected_modified : !target.key?('dateModified')
  errors << "#{url}: datePublished incorrecta" unless published_ok
  errors << "#{url}: dateModified incorrecta" unless modified_ok

  nodes.each do |node|
    next unless node.is_a?(Hash)
    if %w[Person Organization WebSite].include?(node['@type']) && (node.key?('datePublished') || node.key?('dateModified'))
      errors << "#{url}: fecha en auxiliar #{node['@type']}"
    end
  end

  signature = [target['@type'], nodes.map { |node| node['@type'] if node.is_a?(Hash) }.compact.sort]
  patterns[signature] << url
  checked += 1
end

puts "JSONLD_PAGES_CHECKED=#{checked}"
puts "PENDING_NOT_VALIDATED=#{pending}"
puts "JSONLD_ERRORS=#{errors.size}"
puts 'STRUCTURE_PATTERNS_BEGIN'
patterns.each { |key, urls| puts "#{key.inspect} | sample=#{urls.first} | count=#{urls.size}" }
puts 'STRUCTURE_PATTERNS_END'
errors.each { |error| puts "ERROR=#{error}" }
exit 1 unless errors.empty?
