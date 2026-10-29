# Crawlora OpenDota JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `30`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| opendota | `opendota.abilities` | `opendota-abilities` | `GET /opendota/abilities` | `q` (query string)<br>`limit` (query number) | `ApiKeyAuth` | `OpendotaAbilitiesResponse` |  |
| opendota | `opendota.benchmarks` | `opendota-benchmarks` | `GET /opendota/benchmarks` | `hero_id` (query number required)<br>`bracket` (query number)<br>`role` (query "core" \| "support") | `ApiKeyAuth` | `OpendotaBenchmarksResponse` |  |
| opendota | `opendota.constants` | `opendota-constants` | `GET /opendota/constants` | `resource` (query "game_mode" \| "lobby_type" \| "patch" \| "region" \| "cluster" \| "item_ids" \| "ability_ids" \| "permanent_buffs" \| "xp_level" \| "countries" \| "order_types" \| "player_colors" \| "chat_wheel" \| "item_colors" \| "ancients" \| "skillshots" required) | `ApiKeyAuth` | `OpendotaConstantsResponse` |  |
| opendota | `opendota.findMatches` | `opendota-find-matches` | `GET /opendota/find-matches` | `team_a` (query string)<br>`team_b` (query string) | `ApiKeyAuth` | `OpendotaFindMatchesResponse` |  |
| opendota | `opendota.heroDescriptions` | `opendota-hero-descriptions` | `GET /opendota/hero-descriptions` | `hero_id` (query number)<br>`include_lore` (query boolean) | `ApiKeyAuth` | `OpendotaHeroDescriptionsResponse` |  |
| opendota | `opendota.heroDurations` | `opendota-hero-durations` | `GET /opendota/hero-durations` | `hero_id` (query number required) | `ApiKeyAuth` | `OpendotaHeroDurationsResponse` |  |
| opendota | `opendota.heroItems` | `opendota-hero-items` | `GET /opendota/hero-items` | `hero_id` (query number required) | `ApiKeyAuth` | `OpendotaHeroItemsResponse` |  |
| opendota | `opendota.heroMatches` | `opendota-hero-matches` | `GET /opendota/hero-matches` | `hero_id` (query number required) | `ApiKeyAuth` | `OpendotaHeroMatchesResponse` |  |
| opendota | `opendota.heroMatchups` | `opendota-hero-matchups` | `GET /opendota/hero-matchups` | `hero_id` (query number required) | `ApiKeyAuth` | `OpendotaHeroMatchupsResponse` |  |
| opendota | `opendota.heroStats` | `opendota-hero-stats` | `GET /opendota/hero-stats` | `primary_attr` (query "agi" \| "all" \| "int" \| "str")<br>`attack_type` (query "Melee" \| "Ranged")<br>`role` (query "Carry" \| "Disabler" \| "Durable" \| "Escape" \| "Initiator" \| "Nuker" \| "Pusher" \| "Support")<br>`sort` (query "id" \| "name" \| "pro_pick" \| "pro_win" \| "pro_ban" \| "pro_win_rate" \| "pub_pick" \| "pub_win" \| "pub_win_rate" \| "turbo_pick" \| "turbo_win_rate")<br>`desc` (query boolean)<br>`limit` (query number) | `ApiKeyAuth` | `OpendotaHeroStatsResponse` |  |
| opendota | `opendota.heroes` | `opendota-heroes` | `GET /opendota/heroes` | none | `ApiKeyAuth` | `OpendotaHeroesResponse` |  |
| opendota | `opendota.items` | `opendota-items` | `GET /opendota/items` | `q` (query string)<br>`quality` (query string)<br>`limit` (query number) | `ApiKeyAuth` | `OpendotaItemsResponse` |  |
| opendota | `opendota.league` | `opendota-league` | `GET /opendota/league` | `league_id` (query number required) | `ApiKeyAuth` | `OpendotaLeagueResponse` |  |
| opendota | `opendota.leagueMatchIds` | `opendota-league-match-ids` | `GET /opendota/league-match-ids` | `league_id` (query number required) | `ApiKeyAuth` | `OpendotaLeagueMatchIdsResponse` |  |
| opendota | `opendota.leagueMatches` | `opendota-league-matches` | `GET /opendota/league-matches` | `league_id` (query number required)<br>`team_id` (query number) | `ApiKeyAuth` | `OpendotaLeagueMatchesResponse` |  |
| opendota | `opendota.leagues` | `opendota-leagues` | `GET /opendota/leagues` | `tier` (query "amateur" \| "excluded" \| "premium" \| "professional" \| "unrated") | `ApiKeyAuth` | `OpendotaLeaguesResponse` |  |
| opendota | `opendota.live` | `opendota-live` | `GET /opendota/live` | none | `ApiKeyAuth` | `OpendotaLiveResponse` |  |
| opendota | `opendota.match` | `opendota-match` | `GET /opendota/match` | `id` (query number required) | `ApiKeyAuth` | `OpendotaMatchResponse` |  |
| opendota | `opendota.patchNotes` | `opendota-patch-notes` | `GET /opendota/patch-notes` | `patch` (query string) | `ApiKeyAuth` | `OpendotaPatchNotesResponse` |  |
| opendota | `opendota.proMatches` | `opendota-pro-matches` | `GET /opendota/pro-matches` | `less_than_match_id` (query number) | `ApiKeyAuth` | `OpendotaProMatchesResponse` |  |
| opendota | `opendota.proPlayers` | `opendota-pro-players` | `GET /opendota/pro-players` | `team_id` (query number)<br>`q` (query string)<br>`limit` (query number)<br>`offset` (query number) | `ApiKeyAuth` | `OpendotaProPlayersResponse` |  |
| opendota | `opendota.publicMatches` | `opendota-public-matches` | `GET /opendota/public-matches` | `min_rank` (query "11" \| "12" \| "13" \| "14" \| "15" \| "21" \| "22" \| "23" \| "24" \| "25" \| "31" \| "32" \| "33" \| "34" \| "35" \| "41" \| "42" \| "43" \| "44" \| "45" \| "51" \| "52" \| "53" \| "54" \| "55" \| "61" \| "62" \| "63" \| "64" \| "65" \| "71" \| "72" \| "73" \| "74" \| "75" \| "81" \| "82" \| "83" \| "84" \| "85")<br>`max_rank` (query "11" \| "12" \| "13" \| "14" \| "15" \| "21" \| "22" \| "23" \| "24" \| "25" \| "31" \| "32" \| "33" \| "34" \| "35" \| "41" \| "42" \| "43" \| "44" \| "45" \| "51" \| "52" \| "53" \| "54" \| "55" \| "61" \| "62" \| "63" \| "64" \| "65" \| "71" \| "72" \| "73" \| "74" \| "75" \| "81" \| "82" \| "83" \| "84" \| "85")<br>`less_than_match_id` (query number) | `ApiKeyAuth` | `OpendotaPublicMatchesResponse` |  |
| opendota | `opendota.rankDistribution` | `opendota-rank-distribution` | `GET /opendota/rank-distribution` | none | `ApiKeyAuth` | `OpendotaRankDistributionResponse` |  |
| opendota | `opendota.records` | `opendota-records` | `GET /opendota/records` | `field` (query "kills" \| "deaths" \| "assists" \| "last_hits" \| "denies" \| "gold_per_min" \| "xp_per_min" \| "hero_damage" \| "tower_damage" \| "hero_healing" \| "duration" required) | `ApiKeyAuth` | `OpendotaRecordsResponse` |  |
| opendota | `opendota.scenarios` | `opendota-scenarios` | `GET /opendota/scenarios` | `kind` (query "item-timings" \| "lane-roles" \| "misc" required)<br>`hero_id` (query number)<br>`item` (query string)<br>`lane_role` (query number)<br>`scenario` (query "courier_kill" \| "first_blood" \| "neg_chat_1min" \| "pos_chat_1min")<br>`limit` (query number) | `ApiKeyAuth` | `OpendotaScenariosResponse` |  |
| opendota | `opendota.team` | `opendota-team` | `GET /opendota/team` | `team_id` (query number required) | `ApiKeyAuth` | `OpendotaTeamResponse` |  |
| opendota | `opendota.teamHeroes` | `opendota-team-heroes` | `GET /opendota/team-heroes` | `team_id` (query number required) | `ApiKeyAuth` | `OpendotaTeamHeroesResponse` |  |
| opendota | `opendota.teamMatches` | `opendota-team-matches` | `GET /opendota/team-matches` | `team_id` (query number required) | `ApiKeyAuth` | `OpendotaTeamMatchesResponse` |  |
| opendota | `opendota.teamPlayers` | `opendota-team-players` | `GET /opendota/team-players` | `team_id` (query number required) | `ApiKeyAuth` | `OpendotaTeamPlayersResponse` |  |
| opendota | `opendota.teams` | `opendota-teams` | `GET /opendota/teams` | `page` (query number) | `ApiKeyAuth` | `OpendotaTeamsResponse` |  |
