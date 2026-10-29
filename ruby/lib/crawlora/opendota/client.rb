require "json"
require "net/http"
require "uri"

module Crawlora
  module Opendota
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"opendota-abilities": {"bodyParam": null, "bodyRequired": false, "id": "opendota-abilities", "method": "GET", "params": [{"description": "Case-insensitive search on the ability key or display name, for example blink", "in": "query", "name": "q", "type": "string"}, {"description": "Number of abilities to return, 1 to 500; defaults to 50", "in": "query", "maximum": 500, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/opendota/abilities", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-benchmarks": {"bodyParam": null, "bodyRequired": false, "id": "opendota-benchmarks", "method": "GET", "params": [{"description": "Positive hero ID from opendota-heroes", "in": "query", "name": "hero_id", "required": true, "type": "integer", "x-example": 1}, {"description": "Rank bracket 1 (Herald) to 8 (Immortal) to benchmark against; omit for all ranks", "in": "query", "maximum": 8, "minimum": 1, "name": "bracket", "type": "integer"}, {"description": "Role of the games counted; one of core, support; omit for all roles", "enum": ["core", "support"], "in": "query", "name": "role", "type": "string"}], "path": "/opendota/benchmarks", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "hero_id", "required": true, "type": "integer"}, {"in": "query", "name": "bracket", "type": "integer"}, {"enum": ["core", "support"], "in": "query", "name": "role", "type": "string"}], "security": ["ApiKeyAuth"]}, "opendota-constants": {"bodyParam": null, "bodyRequired": false, "id": "opendota-constants", "method": "GET", "params": [{"description": "Lookup table; one of game_mode, lobby_type, patch, region, cluster, item_ids, ability_ids, permanent_buffs, xp_level, countries, order_types, player_colors, chat_wheel, item_colors, ancients, skillshots", "enum": ["game_mode", "lobby_type", "patch", "region", "cluster", "item_ids", "ability_ids", "permanent_buffs", "xp_level", "countries", "order_types", "player_colors", "chat_wheel", "item_colors", "ancients", "skillshots"], "in": "query", "name": "resource", "required": true, "type": "string", "x-example": "game_mode"}], "path": "/opendota/constants", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["game_mode", "lobby_type", "patch", "region", "cluster", "item_ids", "ability_ids", "permanent_buffs", "xp_level", "countries", "order_types", "player_colors", "chat_wheel", "item_colors", "ancients", "skillshots"], "in": "query", "name": "resource", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "opendota-find-matches": {"bodyParam": null, "bodyRequired": false, "id": "opendota-find-matches", "method": "GET", "params": [{"description": "Comma-separated hero ids (up to 5) that must be on team A", "in": "query", "name": "team_a", "type": "string", "x-example": "1,2"}, {"description": "Comma-separated hero ids (up to 5) that must be on team B", "in": "query", "name": "team_b", "type": "string", "x-example": "3"}], "path": "/opendota/find-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_a", "type": "string"}, {"in": "query", "name": "team_b", "type": "string"}], "security": ["ApiKeyAuth"]}, "opendota-hero-descriptions": {"bodyParam": null, "bodyRequired": false, "id": "opendota-hero-descriptions", "method": "GET", "params": [{"description": "Positive hero id from opendota-heroes; omit it for all heroes", "in": "query", "minimum": 1, "name": "hero_id", "type": "integer", "x-example": 1}, {"description": "true adds each hero's lore text; defaults to false", "in": "query", "name": "include_lore", "type": "boolean"}], "path": "/opendota/hero-descriptions", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "hero_id", "type": "integer"}, {"in": "query", "name": "include_lore", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "opendota-hero-durations": {"bodyParam": null, "bodyRequired": false, "id": "opendota-hero-durations", "method": "GET", "params": [{"description": "Positive hero ID from opendota-heroes", "in": "query", "name": "hero_id", "required": true, "type": "integer", "x-example": 1}], "path": "/opendota/hero-durations", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "hero_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-hero-items": {"bodyParam": null, "bodyRequired": false, "id": "opendota-hero-items", "method": "GET", "params": [{"description": "Positive hero ID from opendota-heroes", "in": "query", "name": "hero_id", "required": true, "type": "integer", "x-example": 1}], "path": "/opendota/hero-items", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "hero_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-hero-matches": {"bodyParam": null, "bodyRequired": false, "id": "opendota-hero-matches", "method": "GET", "params": [{"description": "Positive hero ID from opendota-heroes", "in": "query", "name": "hero_id", "required": true, "type": "integer", "x-example": 1}], "path": "/opendota/hero-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "hero_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-hero-matchups": {"bodyParam": null, "bodyRequired": false, "id": "opendota-hero-matchups", "method": "GET", "params": [{"description": "Positive hero ID from opendota-heroes", "in": "query", "name": "hero_id", "required": true, "type": "integer", "x-example": 1}], "path": "/opendota/hero-matchups", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "hero_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-hero-stats": {"bodyParam": null, "bodyRequired": false, "id": "opendota-hero-stats", "method": "GET", "params": [{"description": "Primary attribute filter; one of agi, all, int, str", "enum": ["agi", "all", "int", "str"], "in": "query", "name": "primary_attr", "type": "string"}, {"description": "Attack type filter; one of Melee, Ranged", "enum": ["Melee", "Ranged"], "in": "query", "name": "attack_type", "type": "string"}, {"description": "Role filter; one of Carry, Disabler, Durable, Escape, Initiator, Nuker, Pusher, Support", "enum": ["Carry", "Disabler", "Durable", "Escape", "Initiator", "Nuker", "Pusher", "Support"], "in": "query", "name": "role", "type": "string"}, {"description": "Sort key; one of id, name, pro_pick, pro_win, pro_ban, pro_win_rate, pub_pick, pub_win, pub_win_rate, turbo_pick, turbo_win_rate; defaults to id", "enum": ["id", "name", "pro_pick", "pro_win", "pro_ban", "pro_win_rate", "pub_pick", "pub_win", "pub_win_rate", "turbo_pick", "turbo_win_rate"], "in": "query", "name": "sort", "type": "string"}, {"description": "Sort descending (the default for every key except id and name)", "in": "query", "name": "desc", "type": "boolean"}, {"description": "Number of heroes to return, 1 to 200; defaults to all", "in": "query", "maximum": 200, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/opendota/hero-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["agi", "all", "int", "str"], "in": "query", "name": "primary_attr", "type": "string"}, {"enum": ["Melee", "Ranged"], "in": "query", "name": "attack_type", "type": "string"}, {"enum": ["Carry", "Disabler", "Durable", "Escape", "Initiator", "Nuker", "Pusher", "Support"], "in": "query", "name": "role", "type": "string"}, {"enum": ["id", "name", "pro_pick", "pro_win", "pro_ban", "pro_win_rate", "pub_pick", "pub_win", "pub_win_rate", "turbo_pick", "turbo_win_rate"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "desc", "type": "boolean"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-heroes": {"bodyParam": null, "bodyRequired": false, "id": "opendota-heroes", "method": "GET", "params": [], "path": "/opendota/heroes", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "opendota-items": {"bodyParam": null, "bodyRequired": false, "id": "opendota-items", "method": "GET", "params": [{"description": "Case-insensitive search on the item key or display name, for example blink", "in": "query", "name": "q", "type": "string"}, {"description": "Item quality from the qualities list in the response; currently artifact, common, component, consumable, consumable;laning, epic, rare, secret_shop", "in": "query", "name": "quality", "type": "string"}, {"description": "Number of items to return, 1 to 500; defaults to 50", "in": "query", "maximum": 500, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/opendota/items", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "type": "string"}, {"in": "query", "name": "quality", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-league": {"bodyParam": null, "bodyRequired": false, "id": "opendota-league", "method": "GET", "params": [{"description": "Positive OpenDota league ID from opendota-leagues", "in": "query", "name": "league_id", "required": true, "type": "integer", "x-example": 20395}], "path": "/opendota/league", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-league-match-ids": {"bodyParam": null, "bodyRequired": false, "id": "opendota-league-match-ids", "method": "GET", "params": [{"description": "Positive OpenDota league ID from opendota_leagues", "format": "int64", "in": "query", "name": "league_id", "required": true, "type": "integer", "x-example": 20395}], "path": "/opendota/league-match-ids", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-league-matches": {"bodyParam": null, "bodyRequired": false, "id": "opendota-league-matches", "method": "GET", "params": [{"description": "Positive league ID from opendota_leagues", "format": "int64", "in": "query", "name": "league_id", "required": true, "type": "integer", "x-example": 20395}, {"description": "Optional positive team ID; keeps matches where this team is Radiant or Dire", "format": "int64", "in": "query", "name": "team_id", "type": "integer", "x-example": 8255888}], "path": "/opendota/league-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "league_id", "required": true, "type": "integer"}, {"in": "query", "name": "team_id", "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-leagues": {"bodyParam": null, "bodyRequired": false, "id": "opendota-leagues", "method": "GET", "params": [{"description": "Optional exact source tier filter", "enum": ["amateur", "excluded", "premium", "professional", "unrated"], "in": "query", "name": "tier", "type": "string"}], "path": "/opendota/leagues", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["amateur", "excluded", "premium", "professional", "unrated"], "in": "query", "name": "tier", "type": "string"}], "security": ["ApiKeyAuth"]}, "opendota-live": {"bodyParam": null, "bodyRequired": false, "id": "opendota-live", "method": "GET", "params": [], "path": "/opendota/live", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "opendota-match": {"bodyParam": null, "bodyRequired": false, "id": "opendota-match", "method": "GET", "params": [{"description": "Positive OpenDota match ID from live, pro-match, league-match, or league-match-ID results", "format": "int64", "in": "query", "name": "id", "required": true, "type": "integer", "x-example": 9063495955}], "path": "/opendota/match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-patch-notes": {"bodyParam": null, "bodyRequired": false, "id": "opendota-patch-notes", "method": "GET", "params": [{"description": "Patch key such as 7_38 or 7_06d; omit it to list every patch key", "in": "query", "name": "patch", "type": "string", "x-example": "7_38"}], "path": "/opendota/patch-notes", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "patch", "type": "string"}], "security": ["ApiKeyAuth"]}, "opendota-pro-matches": {"bodyParam": null, "bodyRequired": false, "id": "opendota-pro-matches", "method": "GET", "params": [{"description": "Return professional matches with IDs lower than this positive match ID; copy next_less_than_match_id from the previous response", "format": "int64", "in": "query", "name": "less_than_match_id", "type": "integer", "x-example": 9063495955}], "path": "/opendota/pro-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "less_than_match_id", "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-pro-players": {"bodyParam": null, "bodyRequired": false, "id": "opendota-pro-players", "method": "GET", "params": [{"description": "Optional positive team ID from opendota_teams", "format": "int64", "in": "query", "name": "team_id", "type": "integer", "x-example": 8255888}, {"description": "Case-insensitive substring in player/team names, team tags or country codes; maximum 200 characters", "in": "query", "name": "q", "type": "string"}, {"description": "Local page size, default 50, maximum 100", "in": "query", "name": "limit", "type": "integer", "x-example": 50}, {"description": "Zero-based local offset, default 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/opendota/pro-players", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "type": "integer"}, {"in": "query", "name": "q", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-public-matches": {"bodyParam": null, "bodyRequired": false, "id": "opendota-public-matches", "method": "GET", "params": [{"description": "Lowest average rank tier, medal 1-8 times ten plus stars 1-5", "enum": [11, 12, 13, 14, 15, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 41, 42, 43, 44, 45, 51, 52, 53, 54, 55, 61, 62, 63, 64, 65, 71, 72, 73, 74, 75, 81, 82, 83, 84, 85], "in": "query", "name": "min_rank", "type": "integer"}, {"description": "Highest average rank tier, same form as min_rank; not below min_rank", "enum": [11, 12, 13, 14, 15, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 41, 42, 43, 44, 45, 51, 52, 53, 54, 55, 61, 62, 63, 64, 65, 71, 72, 73, 74, 75, 81, 82, 83, 84, 85], "in": "query", "name": "max_rank", "type": "integer"}, {"description": "Return matches older than this match id", "in": "query", "name": "less_than_match_id", "type": "integer", "x-example": 9066000000}], "path": "/opendota/public-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["11", "12", "13", "14", "15", "21", "22", "23", "24", "25", "31", "32", "33", "34", "35", "41", "42", "43", "44", "45", "51", "52", "53", "54", "55", "61", "62", "63", "64", "65", "71", "72", "73", "74", "75", "81", "82", "83", "84", "85"], "in": "query", "name": "min_rank", "type": "integer"}, {"enum": ["11", "12", "13", "14", "15", "21", "22", "23", "24", "25", "31", "32", "33", "34", "35", "41", "42", "43", "44", "45", "51", "52", "53", "54", "55", "61", "62", "63", "64", "65", "71", "72", "73", "74", "75", "81", "82", "83", "84", "85"], "in": "query", "name": "max_rank", "type": "integer"}, {"in": "query", "name": "less_than_match_id", "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-rank-distribution": {"bodyParam": null, "bodyRequired": false, "id": "opendota-rank-distribution", "method": "GET", "params": [], "path": "/opendota/rank-distribution", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "opendota-records": {"bodyParam": null, "bodyRequired": false, "id": "opendota-records", "method": "GET", "params": [{"description": "Record field; one of kills, deaths, assists, last_hits, denies, gold_per_min, xp_per_min, hero_damage, tower_damage, hero_healing, duration", "enum": ["kills", "deaths", "assists", "last_hits", "denies", "gold_per_min", "xp_per_min", "hero_damage", "tower_damage", "hero_healing", "duration"], "in": "query", "name": "field", "required": true, "type": "string", "x-example": "kills"}], "path": "/opendota/records", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["kills", "deaths", "assists", "last_hits", "denies", "gold_per_min", "xp_per_min", "hero_damage", "tower_damage", "hero_healing", "duration"], "in": "query", "name": "field", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "opendota-scenarios": {"bodyParam": null, "bodyRequired": false, "id": "opendota-scenarios", "method": "GET", "params": [{"description": "Dataset; one of item-timings, lane-roles, misc", "enum": ["item-timings", "lane-roles", "misc"], "in": "query", "name": "kind", "required": true, "type": "string", "x-example": "item-timings"}, {"description": "Positive hero ID from opendota-heroes; item-timings and lane-roles only", "in": "query", "name": "hero_id", "type": "integer", "x-example": 1}, {"description": "Item name from opendota-constants item_ids, for example bfury; item-timings only", "in": "query", "name": "item", "type": "string"}, {"description": "Lane role 1 to 4 (1 safe lane, 2 mid, 3 off lane, 4 jungle); lane-roles only", "in": "query", "maximum": 4, "minimum": 1, "name": "lane_role", "type": "integer"}, {"description": "Scenario; one of courier_kill, first_blood, neg_chat_1min, pos_chat_1min; misc only", "enum": ["courier_kill", "first_blood", "neg_chat_1min", "pos_chat_1min"], "in": "query", "name": "scenario", "type": "string"}, {"description": "Number of rows to return, 1 to 2000, most games first; defaults to all", "in": "query", "maximum": 2000, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/opendota/scenarios", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["item-timings", "lane-roles", "misc"], "in": "query", "name": "kind", "required": true, "type": "string"}, {"in": "query", "name": "hero_id", "type": "integer"}, {"in": "query", "name": "item", "type": "string"}, {"in": "query", "name": "lane_role", "type": "integer"}, {"enum": ["courier_kill", "first_blood", "neg_chat_1min", "pos_chat_1min"], "in": "query", "name": "scenario", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-team": {"bodyParam": null, "bodyRequired": false, "id": "opendota-team", "method": "GET", "params": [{"description": "Positive OpenDota team ID from opendota_teams or a match response", "format": "int64", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 8255888}], "path": "/opendota/team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-team-heroes": {"bodyParam": null, "bodyRequired": false, "id": "opendota-team-heroes", "method": "GET", "params": [{"description": "Positive OpenDota team ID from opendota-teams or a match response", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 8255888}], "path": "/opendota/team-heroes", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-team-matches": {"bodyParam": null, "bodyRequired": false, "id": "opendota-team-matches", "method": "GET", "params": [{"description": "Positive OpenDota team ID from opendota_teams or a match response", "format": "int64", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 8255888}], "path": "/opendota/team-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-team-players": {"bodyParam": null, "bodyRequired": false, "id": "opendota-team-players", "method": "GET", "params": [{"description": "Positive OpenDota team ID from opendota-teams or a match response", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 8255888}], "path": "/opendota/team-players", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "opendota-teams": {"bodyParam": null, "bodyRequired": false, "id": "opendota-teams", "method": "GET", "params": [{"description": "Zero-based page index; defaults to 0", "format": "int64", "in": "query", "name": "page", "type": "integer", "x-example": 0}], "path": "/opendota/teams", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["opendota-abilities", "opendota-benchmarks", "opendota-constants", "opendota-find-matches", "opendota-hero-descriptions", "opendota-hero-durations", "opendota-hero-items", "opendota-hero-matches", "opendota-hero-matchups", "opendota-hero-stats", "opendota-heroes", "opendota-items", "opendota-league", "opendota-league-match-ids", "opendota-league-matches", "opendota-leagues", "opendota-live", "opendota-match", "opendota-patch-notes", "opendota-pro-matches", "opendota-pro-players", "opendota-public-matches", "opendota-rank-distribution", "opendota-records", "opendota-scenarios", "opendota-team", "opendota-team-heroes", "opendota-team-matches", "opendota-team-players", "opendota-teams"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-opendota-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('abilities') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-abilities', params, response_type: response_type)
      end
      define_method('benchmarks') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-benchmarks', params, response_type: response_type)
      end
      define_method('constants') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-constants', params, response_type: response_type)
      end
      define_method('find_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-find-matches', params, response_type: response_type)
      end
      define_method('hero_descriptions') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-hero-descriptions', params, response_type: response_type)
      end
      define_method('hero_durations') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-hero-durations', params, response_type: response_type)
      end
      define_method('hero_items') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-hero-items', params, response_type: response_type)
      end
      define_method('hero_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-hero-matches', params, response_type: response_type)
      end
      define_method('hero_matchups') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-hero-matchups', params, response_type: response_type)
      end
      define_method('hero_stats') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-hero-stats', params, response_type: response_type)
      end
      define_method('heroes') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-heroes', params, response_type: response_type)
      end
      define_method('items') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-items', params, response_type: response_type)
      end
      define_method('league') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-league', params, response_type: response_type)
      end
      define_method('league_match_ids') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-league-match-ids', params, response_type: response_type)
      end
      define_method('league_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-league-matches', params, response_type: response_type)
      end
      define_method('leagues') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-leagues', params, response_type: response_type)
      end
      define_method('live') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-live', params, response_type: response_type)
      end
      define_method('match') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-match', params, response_type: response_type)
      end
      define_method('patch_notes') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-patch-notes', params, response_type: response_type)
      end
      define_method('pro_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-pro-matches', params, response_type: response_type)
      end
      define_method('pro_players') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-pro-players', params, response_type: response_type)
      end
      define_method('public_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-public-matches', params, response_type: response_type)
      end
      define_method('rank_distribution') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-rank-distribution', params, response_type: response_type)
      end
      define_method('records') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-records', params, response_type: response_type)
      end
      define_method('scenarios') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-scenarios', params, response_type: response_type)
      end
      define_method('team') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-team', params, response_type: response_type)
      end
      define_method('team_heroes') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-team-heroes', params, response_type: response_type)
      end
      define_method('team_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-team-matches', params, response_type: response_type)
      end
      define_method('team_players') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-team-players', params, response_type: response_type)
      end
      define_method('teams') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('opendota-teams', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
