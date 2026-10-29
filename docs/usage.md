# OpenDota API endpoint reference and client usage

This reference lists all 30 public OpenDota API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/opendota`, `crawlora-opendota`, and `crawlora-opendota` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape OpenDota locally; Crawlora is independent from and not endorsed by OpenDota or its owners.

The package tracks the public API contract revision `sha256:bd541087bc32280cd45ea20c8afb0f976d4a9b54df109f589f4a858eb14b9c3a` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `opendota`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `abilities` | `abilities` | `opendota.abilities` | `GET /opendota/abilities` | `q` (query, optional), `limit` (query, optional) | OpenDota Dota 2 ability reference |
| `benchmarks` | `benchmarks` | `opendota.benchmarks` | `GET /opendota/benchmarks` | `hero_id` (query, required), `bracket` (query, optional), `role` (query, optional; values: `core`, `support`) | OpenDota Dota 2 hero benchmarks by percentile |
| `constants` | `constants` | `opendota.constants` | `GET /opendota/constants` | `resource` (query, required; values: `game_mode`, `lobby_type`, `patch`, `region`, `cluster`, `item_ids`, `ability_ids`, `permanent_buffs`, `xp_level`, `countries`, `order_types`, `player_colors`, `chat_wheel`, `item_colors`, `ancients`, `skillshots`) | OpenDota Dota 2 id lookup tables |
| `findMatches` | `find_matches` | `opendota.find_matches` | `GET /opendota/find-matches` | `team_a` (query, optional), `team_b` (query, optional) | OpenDota Dota 2 matches by hero lineup |
| `heroDescriptions` | `hero_descriptions` | `opendota.hero_descriptions` | `GET /opendota/hero-descriptions` | `hero_id` (query, optional), `include_lore` (query, optional) | OpenDota Dota 2 Aghanim's Scepter and Shard descriptions |
| `heroDurations` | `hero_durations` | `opendota.hero_durations` | `GET /opendota/hero-durations` | `hero_id` (query, required) | OpenDota Dota 2 hero win rate by game duration |
| `heroes` | `heroes` | `opendota.heroes` | `GET /opendota/heroes` | — | OpenDota hero directory |
| `heroItems` | `hero_items` | `opendota.hero_items` | `GET /opendota/hero-items` | `hero_id` (query, required) | OpenDota Dota 2 hero item popularity |
| `heroMatches` | `hero_matches` | `opendota.hero_matches` | `GET /opendota/hero-matches` | `hero_id` (query, required) | OpenDota Dota 2 recent matches of a hero |
| `heroMatchups` | `hero_matchups` | `opendota.hero_matchups` | `GET /opendota/hero-matchups` | `hero_id` (query, required) | OpenDota Dota 2 hero matchup records |
| `heroStats` | `hero_stats` | `opendota.hero_stats` | `GET /opendota/hero-stats` | `primary_attr` (query, optional; values: `agi`, `all`, `int`, `str`), `attack_type` (query, optional; values: `Melee`, `Ranged`), `role` (query, optional; values: `Carry`, `Disabler`, `Durable`, `Escape`, `Initiator`, `Nuker`, `Pusher`, `Support`), `sort` (query, optional; values: `id`, `name`, `pro_pick`, `pro_win`, `pro_ban`, `pro_win_rate`, `pub_pick`, `pub_win`, `pub_win_rate`, `turbo_pick`, `turbo_win_rate`), `desc` (query, optional), `limit` (query, optional) | OpenDota Dota 2 hero pick and win statistics |
| `items` | `items` | `opendota.items` | `GET /opendota/items` | `q` (query, optional), `quality` (query, optional), `limit` (query, optional) | OpenDota Dota 2 item reference |
| `league` | `league` | `opendota.league` | `GET /opendota/league` | `league_id` (query, required) | OpenDota Dota 2 league detail and teams |
| `leagueMatches` | `league_matches` | `opendota.league_matches` | `GET /opendota/league-matches` | `league_id` (query, required), `team_id` (query, optional) | OpenDota matches for one league |
| `leagueMatchIds` | `league_match_ids` | `opendota.league_match_ids` | `GET /opendota/league-match-ids` | `league_id` (query, required) | OpenDota match IDs for one league |
| `leagues` | `leagues` | `opendota.leagues` | `GET /opendota/leagues` | `tier` (query, optional; values: `amateur`, `excluded`, `premium`, `professional`, `unrated`) | OpenDota league directory |
| `live` | `live` | `opendota.live` | `GET /opendota/live` | — | OpenDota live games |
| `match` | `match` | `opendota.match_` | `GET /opendota/match` | `id` (query, required) | OpenDota match detail |
| `patchNotes` | `patch_notes` | `opendota.patch_notes` | `GET /opendota/patch-notes` | `patch` (query, optional) | OpenDota Dota 2 patch notes |
| `proMatches` | `pro_matches` | `opendota.pro_matches` | `GET /opendota/pro-matches` | `less_than_match_id` (query, optional) | OpenDota recent professional matches |
| `proPlayers` | `pro_players` | `opendota.pro_players` | `GET /opendota/pro-players` | `team_id` (query, optional), `q` (query, optional), `limit` (query, optional), `offset` (query, optional) | OpenDota professional player roster |
| `publicMatches` | `public_matches` | `opendota.public_matches` | `GET /opendota/public-matches` | `min_rank` (query, optional; values: `11`, `12`, `13`, `14`, `15`, `21`, `22`, `23`, `24`, `25`, `31`, `32`, `33`, `34`, `35`, `41`, `42`, `43`, `44`, `45`, `51`, `52`, `53`, `54`, `55`, `61`, `62`, `63`, `64`, `65`, `71`, `72`, `73`, `74`, `75`, `81`, `82`, `83`, `84`, `85`), `max_rank` (query, optional; values: `11`, `12`, `13`, `14`, `15`, `21`, `22`, `23`, `24`, `25`, `31`, `32`, `33`, `34`, `35`, `41`, `42`, `43`, `44`, `45`, `51`, `52`, `53`, `54`, `55`, `61`, `62`, `63`, `64`, `65`, `71`, `72`, `73`, `74`, `75`, `81`, `82`, `83`, `84`, `85`), `less_than_match_id` (query, optional) | OpenDota Dota 2 recent public matches by rank |
| `rankDistribution` | `rank_distribution` | `opendota.rank_distribution` | `GET /opendota/rank-distribution` | — | OpenDota Dota 2 rank distribution |
| `records` | `records` | `opendota.records` | `GET /opendota/records` | `field` (query, required; values: `kills`, `deaths`, `assists`, `last_hits`, `denies`, `gold_per_min`, `xp_per_min`, `hero_damage`, `tower_damage`, `hero_healing`, `duration`) | OpenDota Dota 2 single-match record leaderboards |
| `scenarios` | `scenarios` | `opendota.scenarios` | `GET /opendota/scenarios` | `kind` (query, required; values: `item-timings`, `lane-roles`, `misc`), `hero_id` (query, optional), `item` (query, optional), `lane_role` (query, optional), `scenario` (query, optional; values: `courier_kill`, `first_blood`, `neg_chat_1min`, `pos_chat_1min`), `limit` (query, optional) | OpenDota Dota 2 scenario win rates |
| `team` | `team` | `opendota.team` | `GET /opendota/team` | `team_id` (query, required) | OpenDota team details |
| `teamHeroes` | `team_heroes` | `opendota.team_heroes` | `GET /opendota/team-heroes` | `team_id` (query, required) | OpenDota Dota 2 team hero pool |
| `teamMatches` | `team_matches` | `opendota.team_matches` | `GET /opendota/team-matches` | `team_id` (query, required) | OpenDota team match history |
| `teamPlayers` | `team_players` | `opendota.team_players` | `GET /opendota/team-players` | `team_id` (query, required) | OpenDota Dota 2 team player history |
| `teams` | `teams` | `opendota.teams` | `GET /opendota/teams` | `page` (query, optional) | OpenDota team directory |

## Client forms

- JavaScript: import `OpenDotaClient` (also exported as `Client`) from `@crawlora-org/opendota`; use `new OpenDotaClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `OpenDotaClient` (also exported as `Client`) from `crawlora_opendota`; use `with OpenDotaClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncOpenDotaClient`, used with `async with` and `await`.
- Rust: add `crawlora-opendota` with Cargo; import `Client` and the generated operation parameter struct, then call `client.opendota.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-opendota/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
