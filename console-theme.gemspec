# coding: utf-8

Gem::Specification.new do |spec|
  spec.name          = "console-theme"
  spec.version       = "1.0.1"
  spec.authors       = ["Jae Hee Lee"]
  spec.email         = ["jaeheelee0113@gmail.com"]

  spec.summary       = %q{A fast and simple Jekyll theme that resembles console line.}
  spec.homepage      = "https://www.github.com/jaehee0113/console"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r{^(assets|_layouts|_includes|_sass|LICENSE|README)}i) }

  spec.add_runtime_dependency "jekyll", "~> 3.3"
  spec.add_development_dependency "bundler", "~> 1.12"
  spec.add_development_dependency "rake", "~> 10.0"
  spec.add_development_dependency "jekyll-polyglot", ">= 1.2.4"
  spec.add_development_dependency "jekyll-seo-tag", ">= 2.1.0"
  spec.add_development_dependency "jekyll-paginate", ">= 1.1.0"
  spec.add_development_dependency "jekyll-feed", "~> 0.6"
end
