# OpenDota clients for Crawlora

Official Crawlora client packages for the hosted OpenDota API. Access 30 API endpoints covering Dota 2 matches, heroes, players, teams, leagues, statistics, and game constants from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape OpenDota locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by OpenDota or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/opendota`](javascript/README.md)
- Python: [`crawlora-opendota`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-opendota`](go.mod)
- Ruby: [`crawlora-opendota`](ruby/README.md)
- Java: [`net.crawlora:crawlora-opendota:0.1.0`](java/README.md)
- PHP: [`crawlora/opendota`](php/README.md)
- Rust: [`crawlora-opendota`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=opendota-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=opendota-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=opendota-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 30 selected public OpenDota API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/opendota/abilities` | `opendota-abilities` | OpenDota Dota 2 ability reference |
| `GET` | `/opendota/benchmarks` | `opendota-benchmarks` | OpenDota Dota 2 hero benchmarks by percentile |
| `GET` | `/opendota/constants` | `opendota-constants` | OpenDota Dota 2 id lookup tables |
| `GET` | `/opendota/find-matches` | `opendota-find-matches` | OpenDota Dota 2 matches by hero lineup |
| `GET` | `/opendota/hero-descriptions` | `opendota-hero-descriptions` | OpenDota Dota 2 Aghanim's Scepter and Shard descriptions |
| `GET` | `/opendota/hero-durations` | `opendota-hero-durations` | OpenDota Dota 2 hero win rate by game duration |
| `GET` | `/opendota/hero-items` | `opendota-hero-items` | OpenDota Dota 2 hero item popularity |
| `GET` | `/opendota/hero-matches` | `opendota-hero-matches` | OpenDota Dota 2 recent matches of a hero |
| `GET` | `/opendota/hero-matchups` | `opendota-hero-matchups` | OpenDota Dota 2 hero matchup records |
| `GET` | `/opendota/hero-stats` | `opendota-hero-stats` | OpenDota Dota 2 hero pick and win statistics |
| `GET` | `/opendota/heroes` | `opendota-heroes` | OpenDota hero directory |
| `GET` | `/opendota/items` | `opendota-items` | OpenDota Dota 2 item reference |
| `GET` | `/opendota/league` | `opendota-league` | OpenDota Dota 2 league detail and teams |
| `GET` | `/opendota/league-match-ids` | `opendota-league-match-ids` | OpenDota match IDs for one league |
| `GET` | `/opendota/league-matches` | `opendota-league-matches` | OpenDota matches for one league |
| `GET` | `/opendota/leagues` | `opendota-leagues` | OpenDota league directory |
| `GET` | `/opendota/live` | `opendota-live` | OpenDota live games |
| `GET` | `/opendota/match` | `opendota-match` | OpenDota match detail |
| `GET` | `/opendota/patch-notes` | `opendota-patch-notes` | OpenDota Dota 2 patch notes |
| `GET` | `/opendota/pro-matches` | `opendota-pro-matches` | OpenDota recent professional matches |
| `GET` | `/opendota/pro-players` | `opendota-pro-players` | OpenDota professional player roster |
| `GET` | `/opendota/public-matches` | `opendota-public-matches` | OpenDota Dota 2 recent public matches by rank |
| `GET` | `/opendota/rank-distribution` | `opendota-rank-distribution` | OpenDota Dota 2 rank distribution |
| `GET` | `/opendota/records` | `opendota-records` | OpenDota Dota 2 single-match record leaderboards |
| `GET` | `/opendota/scenarios` | `opendota-scenarios` | OpenDota Dota 2 scenario win rates |
| `GET` | `/opendota/team` | `opendota-team` | OpenDota team details |
| `GET` | `/opendota/team-heroes` | `opendota-team-heroes` | OpenDota Dota 2 team hero pool |
| `GET` | `/opendota/team-matches` | `opendota-team-matches` | OpenDota team match history |
| `GET` | `/opendota/team-players` | `opendota-team-players` | OpenDota Dota 2 team player history |
| `GET` | `/opendota/teams` | `opendota-teams` | OpenDota team directory |

## License

MIT. See [LICENSE](LICENSE).
