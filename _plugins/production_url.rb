# Keep canonical and discovery URLs on the public origin during local previews.
# Jekyll's development server rewrites `site.url` to localhost; that is useful
# for the server address but unsafe for canonical, Open Graph, feed, and JSON-LD
# URLs emitted into the generated HTML.
Jekyll::Hooks.register :site, :after_init do |site|
  production_url = site.config["production_url"].to_s.chomp("/")
  site.config["url"] = production_url unless production_url.empty?
end
