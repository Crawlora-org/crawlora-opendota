require_relative "lib/crawlora/opendota/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-opendota"
  spec.version = Crawlora::Opendota::VERSION
  spec.summary = "OpenDota API client for Crawlora (30 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted OpenDota API. Covers Dota 2 matches, heroes, players, teams, leagues, statistics, and game constants across 30 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=opendota-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-opendota", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-opendota/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
