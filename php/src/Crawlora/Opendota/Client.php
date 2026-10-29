<?php

declare(strict_types=1);

namespace Crawlora\Opendota;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'opendota';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 30;
    public const OPERATION_IDS = ["opendota-abilities", "opendota-benchmarks", "opendota-constants", "opendota-find-matches", "opendota-hero-descriptions", "opendota-hero-durations", "opendota-hero-items", "opendota-hero-matches", "opendota-hero-matchups", "opendota-hero-stats", "opendota-heroes", "opendota-items", "opendota-league", "opendota-league-match-ids", "opendota-league-matches", "opendota-leagues", "opendota-live", "opendota-match", "opendota-patch-notes", "opendota-pro-matches", "opendota-pro-players", "opendota-public-matches", "opendota-rank-distribution", "opendota-records", "opendota-scenarios", "opendota-team", "opendota-team-heroes", "opendota-team-matches", "opendota-team-players", "opendota-teams"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"opendota-abilities": {"bodyParam": null, "bodyRequired": false, "id": "opendota-abilities", "method": "GET", "params": [{"description": "Case-insensitive search on the ability key or display name, for example blink", "in": "query", "name": "q", "type": "string"}, {"description": "Number of abilities to return, 1 to 500; defaults to 50", "in": "query", "maximum": 500, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/opendota/abilities", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-benchmarks": {"bodyParam": null, "bodyRequired": false, "id": "opendota-benchmarks", "method": "GET", "params": [{"description": "Positive hero ID from opendota-heroes", "in": "query", "name": "hero_id", "required": true, "type": "integer", "x-example": 1}, {"description": "Rank bracket 1 (Herald) to 8 (Immortal) to benchmark against; omit for all ranks", "in": "query", "maximum": 8, "minimum": 1, "name": "bracket", "type": "integer"}, {"description": "Role of the games counted; one of core, support; omit for all roles", "enum": ["core", "support"], "in": "query", "name": "role", "type": "string"}], "path": "/opendota/benchmarks", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "hero_id", "required": true, "type": "integer"}, {"in": "query", "name": "bracket", "type": "integer"}, {"enum": ["core", "support"], "in": "query", "name": "role", "type": "string"}], "security": ["ApiKeyAuth"]}, "opendota-constants": {"bodyParam": null, "bodyRequired": false, "id": "opendota-constants", "method": "GET", "params": [{"description": "Lookup table; one of game_mode, lobby_type, patch, region, cluster, item_ids, ability_ids, permanent_buffs, xp_level, countries, order_types, player_colors, chat_wheel, item_colors, ancients, skillshots", "enum": ["game_mode", "lobby_type", "patch", "region", "cluster", "item_ids", "ability_ids", "permanent_buffs", "xp_level", "countries", "order_types", "player_colors", "chat_wheel", "item_colors", "ancients", "skillshots"], "in": "query", "name": "resource", "required": true, "type": "string", "x-example": "game_mode"}], "path": "/opendota/constants", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["game_mode", "lobby_type", "patch", "region", "cluster", "item_ids", "ability_ids", "permanent_buffs", "xp_level", "countries", "order_types", "player_colors", "chat_wheel", "item_colors", "ancients", "skillshots"], "in": "query", "name": "resource", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "opendota-find-matches": {"bodyParam": null, "bodyRequired": false, "id": "opendota-find-matches", "method": "GET", "params": [{"description": "Comma-separated hero ids (up to 5) that must be on team A", "in": "query", "name": "team_a", "type": "string", "x-example": "1,2"}, {"description": "Comma-separated hero ids (up to 5) that must be on team B", "in": "query", "name": "team_b", "type": "string", "x-example": "3"}], "path": "/opendota/find-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_a", "type": "string"}, {"in": "query", "name": "team_b", "type": "string"}], "security": ["ApiKeyAuth"]}, "opendota-hero-descriptions": {"bodyParam": null, "bodyRequired": false, "id": "opendota-hero-descriptions", "method": "GET", "params": [{"description": "Positive hero id from opendota-heroes; omit it for all heroes", "in": "query", "minimum": 1, "name": "hero_id", "type": "integer", "x-example": 1}, {"description": "true adds each hero's lore text; defaults to false", "in": "query", "name": "include_lore", "type": "boolean"}], "path": "/opendota/hero-descriptions", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "hero_id", "type": "integer"}, {"in": "query", "name": "include_lore", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "opendota-hero-durations": {"bodyParam": null, "bodyRequired": false, "id": "opendota-hero-durations", "method": "GET", "params": [{"description": "Positive hero ID from opendota-heroes", "in": "query", "name": "hero_id", "required": true, "type": "integer", "x-example": 1}], "path": "/opendota/hero-durations", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "hero_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-hero-items": {"bodyParam": null, "bodyRequired": false, "id": "opendota-hero-items", "method": "GET", "params": [{"description": "Positive hero ID from opendota-heroes", "in": "query", "name": "hero_id", "required": true, "type": "integer", "x-example": 1}], "path": "/opendota/hero-items", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "hero_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-hero-matches": {"bodyParam": null, "bodyRequired": false, "id": "opendota-hero-matches", "method": "GET", "params": [{"description": "Positive hero ID from opendota-heroes", "in": "query", "name": "hero_id", "required": true, "type": "integer", "x-example": 1}], "path": "/opendota/hero-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "hero_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-hero-matchups": {"bodyParam": null, "bodyRequired": false, "id": "opendota-hero-matchups", "method": "GET", "params": [{"description": "Positive hero ID from opendota-heroes", "in": "query", "name": "hero_id", "required": true, "type": "integer", "x-example": 1}], "path": "/opendota/hero-matchups", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "hero_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-hero-stats": {"bodyParam": null, "bodyRequired": false, "id": "opendota-hero-stats", "method": "GET", "params": [{"description": "Primary attribute filter; one of agi, all, int, str", "enum": ["agi", "all", "int", "str"], "in": "query", "name": "primary_attr", "type": "string"}, {"description": "Attack type filter; one of Melee, Ranged", "enum": ["Melee", "Ranged"], "in": "query", "name": "attack_type", "type": "string"}, {"description": "Role filter; one of Carry, Disabler, Durable, Escape, Initiator, Nuker, Pusher, Support", "enum": ["Carry", "Disabler", "Durable", "Escape", "Initiator", "Nuker", "Pusher", "Support"], "in": "query", "name": "role", "type": "string"}, {"description": "Sort key; one of id, name, pro_pick, pro_win, pro_ban, pro_win_rate, pub_pick, pub_win, pub_win_rate, turbo_pick, turbo_win_rate; defaults to id", "enum": ["id", "name", "pro_pick", "pro_win", "pro_ban", "pro_win_rate", "pub_pick", "pub_win", "pub_win_rate", "turbo_pick", "turbo_win_rate"], "in": "query", "name": "sort", "type": "string"}, {"description": "Sort descending (the default for every key except id and name)", "in": "query", "name": "desc", "type": "boolean"}, {"description": "Number of heroes to return, 1 to 200; defaults to all", "in": "query", "maximum": 200, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/opendota/hero-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["agi", "all", "int", "str"], "in": "query", "name": "primary_attr", "type": "string"}, {"enum": ["Melee", "Ranged"], "in": "query", "name": "attack_type", "type": "string"}, {"enum": ["Carry", "Disabler", "Durable", "Escape", "Initiator", "Nuker", "Pusher", "Support"], "in": "query", "name": "role", "type": "string"}, {"enum": ["id", "name", "pro_pick", "pro_win", "pro_ban", "pro_win_rate", "pub_pick", "pub_win", "pub_win_rate", "turbo_pick", "turbo_win_rate"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "desc", "type": "boolean"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-heroes": {"bodyParam": null, "bodyRequired": false, "id": "opendota-heroes", "method": "GET", "params": [], "path": "/opendota/heroes", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "opendota-items": {"bodyParam": null, "bodyRequired": false, "id": "opendota-items", "method": "GET", "params": [{"description": "Case-insensitive search on the item key or display name, for example blink", "in": "query", "name": "q", "type": "string"}, {"description": "Item quality from the qualities list in the response; currently artifact, common, component, consumable, consumable;laning, epic, rare, secret_shop", "in": "query", "name": "quality", "type": "string"}, {"description": "Number of items to return, 1 to 500; defaults to 50", "in": "query", "maximum": 500, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/opendota/items", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "type": "string"}, {"in": "query", "name": "quality", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-league": {"bodyParam": null, "bodyRequired": false, "id": "opendota-league", "method": "GET", "params": [{"description": "Positive OpenDota league ID from opendota-leagues", "in": "query", "name": "league_id", "required": true, "type": "integer", "x-example": 20395}], "path": "/opendota/league", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-league-match-ids": {"bodyParam": null, "bodyRequired": false, "id": "opendota-league-match-ids", "method": "GET", "params": [{"description": "Positive OpenDota league ID from opendota_leagues", "format": "int64", "in": "query", "name": "league_id", "required": true, "type": "integer", "x-example": 20395}], "path": "/opendota/league-match-ids", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-league-matches": {"bodyParam": null, "bodyRequired": false, "id": "opendota-league-matches", "method": "GET", "params": [{"description": "Positive league ID from opendota_leagues", "format": "int64", "in": "query", "name": "league_id", "required": true, "type": "integer", "x-example": 20395}, {"description": "Optional positive team ID; keeps matches where this team is Radiant or Dire", "format": "int64", "in": "query", "name": "team_id", "type": "integer", "x-example": 8255888}], "path": "/opendota/league-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_id", "required": true, "type": "integer"}, {"in": "query", "name": "team_id", "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-leagues": {"bodyParam": null, "bodyRequired": false, "id": "opendota-leagues", "method": "GET", "params": [{"description": "Optional exact source tier filter", "enum": ["amateur", "excluded", "premium", "professional", "unrated"], "in": "query", "name": "tier", "type": "string"}], "path": "/opendota/leagues", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["amateur", "excluded", "premium", "professional", "unrated"], "in": "query", "name": "tier", "type": "string"}], "security": ["ApiKeyAuth"]}, "opendota-live": {"bodyParam": null, "bodyRequired": false, "id": "opendota-live", "method": "GET", "params": [], "path": "/opendota/live", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "opendota-match": {"bodyParam": null, "bodyRequired": false, "id": "opendota-match", "method": "GET", "params": [{"description": "Positive OpenDota match ID from live, pro-match, league-match, or league-match-ID results", "format": "int64", "in": "query", "name": "id", "required": true, "type": "integer", "x-example": 9063495955}], "path": "/opendota/match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-patch-notes": {"bodyParam": null, "bodyRequired": false, "id": "opendota-patch-notes", "method": "GET", "params": [{"description": "Patch key such as 7_38 or 7_06d; omit it to list every patch key", "in": "query", "name": "patch", "type": "string", "x-example": "7_38"}], "path": "/opendota/patch-notes", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "patch", "type": "string"}], "security": ["ApiKeyAuth"]}, "opendota-pro-matches": {"bodyParam": null, "bodyRequired": false, "id": "opendota-pro-matches", "method": "GET", "params": [{"description": "Return professional matches with IDs lower than this positive match ID; copy next_less_than_match_id from the previous response", "format": "int64", "in": "query", "name": "less_than_match_id", "type": "integer", "x-example": 9063495955}], "path": "/opendota/pro-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "less_than_match_id", "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-pro-players": {"bodyParam": null, "bodyRequired": false, "id": "opendota-pro-players", "method": "GET", "params": [{"description": "Optional positive team ID from opendota_teams", "format": "int64", "in": "query", "name": "team_id", "type": "integer", "x-example": 8255888}, {"description": "Case-insensitive substring in player/team names, team tags or country codes; maximum 200 characters", "in": "query", "name": "q", "type": "string"}, {"description": "Local page size, default 50, maximum 100", "in": "query", "name": "limit", "type": "integer", "x-example": 50}, {"description": "Zero-based local offset, default 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/opendota/pro-players", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "type": "integer"}, {"in": "query", "name": "q", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-public-matches": {"bodyParam": null, "bodyRequired": false, "id": "opendota-public-matches", "method": "GET", "params": [{"description": "Lowest average rank tier, medal 1-8 times ten plus stars 1-5", "enum": [11, 12, 13, 14, 15, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 41, 42, 43, 44, 45, 51, 52, 53, 54, 55, 61, 62, 63, 64, 65, 71, 72, 73, 74, 75, 81, 82, 83, 84, 85], "in": "query", "name": "min_rank", "type": "integer"}, {"description": "Highest average rank tier, same form as min_rank; not below min_rank", "enum": [11, 12, 13, 14, 15, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 41, 42, 43, 44, 45, 51, 52, 53, 54, 55, 61, 62, 63, 64, 65, 71, 72, 73, 74, 75, 81, 82, 83, 84, 85], "in": "query", "name": "max_rank", "type": "integer"}, {"description": "Return matches older than this match id", "in": "query", "name": "less_than_match_id", "type": "integer", "x-example": 9066000000}], "path": "/opendota/public-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["11", "12", "13", "14", "15", "21", "22", "23", "24", "25", "31", "32", "33", "34", "35", "41", "42", "43", "44", "45", "51", "52", "53", "54", "55", "61", "62", "63", "64", "65", "71", "72", "73", "74", "75", "81", "82", "83", "84", "85"], "in": "query", "name": "min_rank", "type": "integer"}, {"enum": ["11", "12", "13", "14", "15", "21", "22", "23", "24", "25", "31", "32", "33", "34", "35", "41", "42", "43", "44", "45", "51", "52", "53", "54", "55", "61", "62", "63", "64", "65", "71", "72", "73", "74", "75", "81", "82", "83", "84", "85"], "in": "query", "name": "max_rank", "type": "integer"}, {"in": "query", "name": "less_than_match_id", "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-rank-distribution": {"bodyParam": null, "bodyRequired": false, "id": "opendota-rank-distribution", "method": "GET", "params": [], "path": "/opendota/rank-distribution", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "opendota-records": {"bodyParam": null, "bodyRequired": false, "id": "opendota-records", "method": "GET", "params": [{"description": "Record field; one of kills, deaths, assists, last_hits, denies, gold_per_min, xp_per_min, hero_damage, tower_damage, hero_healing, duration", "enum": ["kills", "deaths", "assists", "last_hits", "denies", "gold_per_min", "xp_per_min", "hero_damage", "tower_damage", "hero_healing", "duration"], "in": "query", "name": "field", "required": true, "type": "string", "x-example": "kills"}], "path": "/opendota/records", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["kills", "deaths", "assists", "last_hits", "denies", "gold_per_min", "xp_per_min", "hero_damage", "tower_damage", "hero_healing", "duration"], "in": "query", "name": "field", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "opendota-scenarios": {"bodyParam": null, "bodyRequired": false, "id": "opendota-scenarios", "method": "GET", "params": [{"description": "Dataset; one of item-timings, lane-roles, misc", "enum": ["item-timings", "lane-roles", "misc"], "in": "query", "name": "kind", "required": true, "type": "string", "x-example": "item-timings"}, {"description": "Positive hero ID from opendota-heroes; item-timings and lane-roles only", "in": "query", "name": "hero_id", "type": "integer", "x-example": 1}, {"description": "Item name from opendota-constants item_ids, for example bfury; item-timings only", "in": "query", "name": "item", "type": "string"}, {"description": "Lane role 1 to 4 (1 safe lane, 2 mid, 3 off lane, 4 jungle); lane-roles only", "in": "query", "maximum": 4, "minimum": 1, "name": "lane_role", "type": "integer"}, {"description": "Scenario; one of courier_kill, first_blood, neg_chat_1min, pos_chat_1min; misc only", "enum": ["courier_kill", "first_blood", "neg_chat_1min", "pos_chat_1min"], "in": "query", "name": "scenario", "type": "string"}, {"description": "Number of rows to return, 1 to 2000, most games first; defaults to all", "in": "query", "maximum": 2000, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/opendota/scenarios", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["item-timings", "lane-roles", "misc"], "in": "query", "name": "kind", "required": true, "type": "string"}, {"in": "query", "name": "hero_id", "type": "integer"}, {"in": "query", "name": "item", "type": "string"}, {"in": "query", "name": "lane_role", "type": "integer"}, {"enum": ["courier_kill", "first_blood", "neg_chat_1min", "pos_chat_1min"], "in": "query", "name": "scenario", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-team": {"bodyParam": null, "bodyRequired": false, "id": "opendota-team", "method": "GET", "params": [{"description": "Positive OpenDota team ID from opendota_teams or a match response", "format": "int64", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 8255888}], "path": "/opendota/team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-team-heroes": {"bodyParam": null, "bodyRequired": false, "id": "opendota-team-heroes", "method": "GET", "params": [{"description": "Positive OpenDota team ID from opendota-teams or a match response", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 8255888}], "path": "/opendota/team-heroes", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-team-matches": {"bodyParam": null, "bodyRequired": false, "id": "opendota-team-matches", "method": "GET", "params": [{"description": "Positive OpenDota team ID from opendota_teams or a match response", "format": "int64", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 8255888}], "path": "/opendota/team-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-team-players": {"bodyParam": null, "bodyRequired": false, "id": "opendota-team-players", "method": "GET", "params": [{"description": "Positive OpenDota team ID from opendota-teams or a match response", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 8255888}], "path": "/opendota/team-players", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-teams": {"bodyParam": null, "bodyRequired": false, "id": "opendota-teams", "method": "GET", "params": [{"description": "Zero-based page index; defaults to 0", "format": "int64", "in": "query", "name": "page", "type": "integer", "x-example": 0}], "path": "/opendota/teams", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-opendota-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function abilities(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-abilities", $params, $responseType);
    }
    public function benchmarks(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-benchmarks", $params, $responseType);
    }
    public function constants(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-constants", $params, $responseType);
    }
    public function find_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-find-matches", $params, $responseType);
    }
    public function hero_descriptions(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-hero-descriptions", $params, $responseType);
    }
    public function hero_durations(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-hero-durations", $params, $responseType);
    }
    public function hero_items(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-hero-items", $params, $responseType);
    }
    public function hero_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-hero-matches", $params, $responseType);
    }
    public function hero_matchups(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-hero-matchups", $params, $responseType);
    }
    public function hero_stats(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-hero-stats", $params, $responseType);
    }
    public function heroes(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-heroes", $params, $responseType);
    }
    public function items(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-items", $params, $responseType);
    }
    public function league(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-league", $params, $responseType);
    }
    public function league_match_ids(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-league-match-ids", $params, $responseType);
    }
    public function league_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-league-matches", $params, $responseType);
    }
    public function leagues(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-leagues", $params, $responseType);
    }
    public function live(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-live", $params, $responseType);
    }
    public function match(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-match", $params, $responseType);
    }
    public function patch_notes(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-patch-notes", $params, $responseType);
    }
    public function pro_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-pro-matches", $params, $responseType);
    }
    public function pro_players(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-pro-players", $params, $responseType);
    }
    public function public_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-public-matches", $params, $responseType);
    }
    public function rank_distribution(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-rank-distribution", $params, $responseType);
    }
    public function records(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-records", $params, $responseType);
    }
    public function scenarios(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-scenarios", $params, $responseType);
    }
    public function team(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-team", $params, $responseType);
    }
    public function team_heroes(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-team-heroes", $params, $responseType);
    }
    public function team_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-team-matches", $params, $responseType);
    }
    public function team_players(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-team-players", $params, $responseType);
    }
    public function teams(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("opendota-teams", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
