# Crawlora OpenDota Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `30`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| opendota | `opendota.abilities` | `opendota-abilities` | `GET /opendota/abilities` | `q` (query String)<br>`limit` (query i64) | `ApiKeyAuth` | `OpendotaAbilitiesResponse` |  |
| opendota | `opendota.benchmarks` | `opendota-benchmarks` | `GET /opendota/benchmarks` | `hero_id` (query i64 required)<br>`bracket` (query i64)<br>`role` (query String enum{core, support}) | `ApiKeyAuth` | `OpendotaBenchmarksResponse` |  |
| opendota | `opendota.constants` | `opendota-constants` | `GET /opendota/constants` | `resource` (query String enum{game_mode, lobby_type, patch, region, cluster, item_ids, ability_ids, permanent_buffs, xp_level, countries, order_types, player_colors, chat_wheel, item_colors, ancients, skillshots} required) | `ApiKeyAuth` | `OpendotaConstantsResponse` |  |
| opendota | `opendota.find_matches` | `opendota-find-matches` | `GET /opendota/find-matches` | `team_a` (query String)<br>`team_b` (query String) | `ApiKeyAuth` | `OpendotaFindMatchesResponse` |  |
| opendota | `opendota.hero_descriptions` | `opendota-hero-descriptions` | `GET /opendota/hero-descriptions` | `hero_id` (query i64)<br>`include_lore` (query bool) | `ApiKeyAuth` | `OpendotaHeroDescriptionsResponse` |  |
| opendota | `opendota.hero_durations` | `opendota-hero-durations` | `GET /opendota/hero-durations` | `hero_id` (query i64 required) | `ApiKeyAuth` | `OpendotaHeroDurationsResponse` |  |
| opendota | `opendota.hero_items` | `opendota-hero-items` | `GET /opendota/hero-items` | `hero_id` (query i64 required) | `ApiKeyAuth` | `OpendotaHeroItemsResponse` |  |
| opendota | `opendota.hero_matches` | `opendota-hero-matches` | `GET /opendota/hero-matches` | `hero_id` (query i64 required) | `ApiKeyAuth` | `OpendotaHeroMatchesResponse` |  |
| opendota | `opendota.hero_matchups` | `opendota-hero-matchups` | `GET /opendota/hero-matchups` | `hero_id` (query i64 required) | `ApiKeyAuth` | `OpendotaHeroMatchupsResponse` |  |
| opendota | `opendota.hero_stats` | `opendota-hero-stats` | `GET /opendota/hero-stats` | `primary_attr` (query String enum{agi, all, int, str})<br>`attack_type` (query String enum{Melee, Ranged})<br>`role` (query String enum{Carry, Disabler, Durable, Escape, Initiator, Nuker, Pusher, Support})<br>`sort` (query String enum{id, name, pro_pick, pro_win, pro_ban, pro_win_rate, pub_pick, pub_win, pub_win_rate, turbo_pick, turbo_win_rate})<br>`desc` (query bool)<br>`limit` (query i64) | `ApiKeyAuth` | `OpendotaHeroStatsResponse` |  |
| opendota | `opendota.heroes` | `opendota-heroes` | `GET /opendota/heroes` | none | `ApiKeyAuth` | `OpendotaHeroesResponse` |  |
| opendota | `opendota.items` | `opendota-items` | `GET /opendota/items` | `q` (query String)<br>`quality` (query String)<br>`limit` (query i64) | `ApiKeyAuth` | `OpendotaItemsResponse` |  |
| opendota | `opendota.league` | `opendota-league` | `GET /opendota/league` | `league_id` (query i64 required) | `ApiKeyAuth` | `OpendotaLeagueResponse` |  |
| opendota | `opendota.league_match_ids` | `opendota-league-match-ids` | `GET /opendota/league-match-ids` | `league_id` (query i64 required) | `ApiKeyAuth` | `OpendotaLeagueMatchIdsResponse` |  |
| opendota | `opendota.league_matches` | `opendota-league-matches` | `GET /opendota/league-matches` | `league_id` (query i64 required)<br>`team_id` (query i64) | `ApiKeyAuth` | `OpendotaLeagueMatchesResponse` |  |
| opendota | `opendota.leagues` | `opendota-leagues` | `GET /opendota/leagues` | `tier` (query String enum{amateur, excluded, premium, professional, unrated}) | `ApiKeyAuth` | `OpendotaLeaguesResponse` |  |
| opendota | `opendota.live` | `opendota-live` | `GET /opendota/live` | none | `ApiKeyAuth` | `OpendotaLiveResponse` |  |
| opendota | `opendota.match_` | `opendota-match` | `GET /opendota/match` | `id` (query i64 required) | `ApiKeyAuth` | `OpendotaMatchResponse` |  |
| opendota | `opendota.patch_notes` | `opendota-patch-notes` | `GET /opendota/patch-notes` | `patch` (query String) | `ApiKeyAuth` | `OpendotaPatchNotesResponse` |  |
| opendota | `opendota.pro_matches` | `opendota-pro-matches` | `GET /opendota/pro-matches` | `less_than_match_id` (query i64) | `ApiKeyAuth` | `OpendotaProMatchesResponse` |  |
| opendota | `opendota.pro_players` | `opendota-pro-players` | `GET /opendota/pro-players` | `team_id` (query i64)<br>`q` (query String)<br>`limit` (query i64)<br>`offset` (query i64) | `ApiKeyAuth` | `OpendotaProPlayersResponse` |  |
| opendota | `opendota.public_matches` | `opendota-public-matches` | `GET /opendota/public-matches` | `min_rank` (query String enum{11, 12, 13, 14, 15, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 41, 42, 43, 44, 45, 51, 52, 53, 54, 55, 61, 62, 63, 64, 65, 71, 72, 73, 74, 75, 81, 82, 83, 84, 85})<br>`max_rank` (query String enum{11, 12, 13, 14, 15, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 41, 42, 43, 44, 45, 51, 52, 53, 54, 55, 61, 62, 63, 64, 65, 71, 72, 73, 74, 75, 81, 82, 83, 84, 85})<br>`less_than_match_id` (query i64) | `ApiKeyAuth` | `OpendotaPublicMatchesResponse` |  |
| opendota | `opendota.rank_distribution` | `opendota-rank-distribution` | `GET /opendota/rank-distribution` | none | `ApiKeyAuth` | `OpendotaRankDistributionResponse` |  |
| opendota | `opendota.records` | `opendota-records` | `GET /opendota/records` | `field` (query String enum{kills, deaths, assists, last_hits, denies, gold_per_min, xp_per_min, hero_damage, tower_damage, hero_healing, duration} required) | `ApiKeyAuth` | `OpendotaRecordsResponse` |  |
| opendota | `opendota.scenarios` | `opendota-scenarios` | `GET /opendota/scenarios` | `kind` (query String enum{item-timings, lane-roles, misc} required)<br>`hero_id` (query i64)<br>`item` (query String)<br>`lane_role` (query i64)<br>`scenario` (query String enum{courier_kill, first_blood, neg_chat_1min, pos_chat_1min})<br>`limit` (query i64) | `ApiKeyAuth` | `OpendotaScenariosResponse` |  |
| opendota | `opendota.team` | `opendota-team` | `GET /opendota/team` | `team_id` (query i64 required) | `ApiKeyAuth` | `OpendotaTeamResponse` |  |
| opendota | `opendota.team_heroes` | `opendota-team-heroes` | `GET /opendota/team-heroes` | `team_id` (query i64 required) | `ApiKeyAuth` | `OpendotaTeamHeroesResponse` |  |
| opendota | `opendota.team_matches` | `opendota-team-matches` | `GET /opendota/team-matches` | `team_id` (query i64 required) | `ApiKeyAuth` | `OpendotaTeamMatchesResponse` |  |
| opendota | `opendota.team_players` | `opendota-team-players` | `GET /opendota/team-players` | `team_id` (query i64 required) | `ApiKeyAuth` | `OpendotaTeamPlayersResponse` |  |
| opendota | `opendota.teams` | `opendota-teams` | `GET /opendota/teams` | `page` (query i64) | `ApiKeyAuth` | `OpendotaTeamsResponse` |  |
