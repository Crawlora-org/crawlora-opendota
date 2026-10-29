package net.crawlora.opendota;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the OpenDota endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 30;
    public static final List<String> OPERATION_IDS = List.of(
            "opendota-abilities",
            "opendota-benchmarks",
            "opendota-constants",
            "opendota-find-matches",
            "opendota-hero-descriptions",
            "opendota-hero-durations",
            "opendota-hero-items",
            "opendota-hero-matches",
            "opendota-hero-matchups",
            "opendota-hero-stats",
            "opendota-heroes",
            "opendota-items",
            "opendota-league",
            "opendota-league-match-ids",
            "opendota-league-matches",
            "opendota-leagues",
            "opendota-live",
            "opendota-match",
            "opendota-patch-notes",
            "opendota-pro-matches",
            "opendota-pro-players",
            "opendota-public-matches",
            "opendota-rank-distribution",
            "opendota-records",
            "opendota-scenarios",
            "opendota-team",
            "opendota-team-heroes",
            "opendota-team-matches",
            "opendota-team-players",
            "opendota-teams"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("opendota-abilities", new Operation("opendota-abilities", "GET", "/opendota/abilities", Map.ofEntries(Map.entry("q", new Param("q", "query", false, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-benchmarks", new Operation("opendota-benchmarks", "GET", "/opendota/benchmarks", Map.ofEntries(Map.entry("hero_id", new Param("hero_id", "query", true, "integer", List.of(), "csv")), Map.entry("bracket", new Param("bracket", "query", false, "integer", List.of(), "csv")), Map.entry("role", new Param("role", "query", false, "string", List.of("core", "support"), "csv"))), List.of("application/json")));
        operations.put("opendota-constants", new Operation("opendota-constants", "GET", "/opendota/constants", Map.ofEntries(Map.entry("resource", new Param("resource", "query", true, "string", List.of("game_mode", "lobby_type", "patch", "region", "cluster", "item_ids", "ability_ids", "permanent_buffs", "xp_level", "countries", "order_types", "player_colors", "chat_wheel", "item_colors", "ancients", "skillshots"), "csv"))), List.of("application/json")));
        operations.put("opendota-find-matches", new Operation("opendota-find-matches", "GET", "/opendota/find-matches", Map.ofEntries(Map.entry("team_a", new Param("team_a", "query", false, "string", List.of(), "csv")), Map.entry("team_b", new Param("team_b", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-hero-descriptions", new Operation("opendota-hero-descriptions", "GET", "/opendota/hero-descriptions", Map.ofEntries(Map.entry("hero_id", new Param("hero_id", "query", false, "integer", List.of(), "csv")), Map.entry("include_lore", new Param("include_lore", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-hero-durations", new Operation("opendota-hero-durations", "GET", "/opendota/hero-durations", Map.ofEntries(Map.entry("hero_id", new Param("hero_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-hero-items", new Operation("opendota-hero-items", "GET", "/opendota/hero-items", Map.ofEntries(Map.entry("hero_id", new Param("hero_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-hero-matches", new Operation("opendota-hero-matches", "GET", "/opendota/hero-matches", Map.ofEntries(Map.entry("hero_id", new Param("hero_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-hero-matchups", new Operation("opendota-hero-matchups", "GET", "/opendota/hero-matchups", Map.ofEntries(Map.entry("hero_id", new Param("hero_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-hero-stats", new Operation("opendota-hero-stats", "GET", "/opendota/hero-stats", Map.ofEntries(Map.entry("primary_attr", new Param("primary_attr", "query", false, "string", List.of("agi", "all", "int", "str"), "csv")), Map.entry("attack_type", new Param("attack_type", "query", false, "string", List.of("Melee", "Ranged"), "csv")), Map.entry("role", new Param("role", "query", false, "string", List.of("Carry", "Disabler", "Durable", "Escape", "Initiator", "Nuker", "Pusher", "Support"), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("id", "name", "pro_pick", "pro_win", "pro_ban", "pro_win_rate", "pub_pick", "pub_win", "pub_win_rate", "turbo_pick", "turbo_win_rate"), "csv")), Map.entry("desc", new Param("desc", "query", false, "boolean", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-heroes", new Operation("opendota-heroes", "GET", "/opendota/heroes", Map.of(), List.of("application/json")));
        operations.put("opendota-items", new Operation("opendota-items", "GET", "/opendota/items", Map.ofEntries(Map.entry("q", new Param("q", "query", false, "string", List.of(), "csv")), Map.entry("quality", new Param("quality", "query", false, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-league", new Operation("opendota-league", "GET", "/opendota/league", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-league-match-ids", new Operation("opendota-league-match-ids", "GET", "/opendota/league-match-ids", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-league-matches", new Operation("opendota-league-matches", "GET", "/opendota/league-matches", Map.ofEntries(Map.entry("league_id", new Param("league_id", "query", true, "integer", List.of(), "csv")), Map.entry("team_id", new Param("team_id", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-leagues", new Operation("opendota-leagues", "GET", "/opendota/leagues", Map.ofEntries(Map.entry("tier", new Param("tier", "query", false, "string", List.of("amateur", "excluded", "premium", "professional", "unrated"), "csv"))), List.of("application/json")));
        operations.put("opendota-live", new Operation("opendota-live", "GET", "/opendota/live", Map.of(), List.of("application/json")));
        operations.put("opendota-match", new Operation("opendota-match", "GET", "/opendota/match", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-patch-notes", new Operation("opendota-patch-notes", "GET", "/opendota/patch-notes", Map.ofEntries(Map.entry("patch", new Param("patch", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-pro-matches", new Operation("opendota-pro-matches", "GET", "/opendota/pro-matches", Map.ofEntries(Map.entry("less_than_match_id", new Param("less_than_match_id", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-pro-players", new Operation("opendota-pro-players", "GET", "/opendota/pro-players", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", false, "integer", List.of(), "csv")), Map.entry("q", new Param("q", "query", false, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-public-matches", new Operation("opendota-public-matches", "GET", "/opendota/public-matches", Map.ofEntries(Map.entry("min_rank", new Param("min_rank", "query", false, "integer", List.of("11", "12", "13", "14", "15", "21", "22", "23", "24", "25", "31", "32", "33", "34", "35", "41", "42", "43", "44", "45", "51", "52", "53", "54", "55", "61", "62", "63", "64", "65", "71", "72", "73", "74", "75", "81", "82", "83", "84", "85"), "csv")), Map.entry("max_rank", new Param("max_rank", "query", false, "integer", List.of("11", "12", "13", "14", "15", "21", "22", "23", "24", "25", "31", "32", "33", "34", "35", "41", "42", "43", "44", "45", "51", "52", "53", "54", "55", "61", "62", "63", "64", "65", "71", "72", "73", "74", "75", "81", "82", "83", "84", "85"), "csv")), Map.entry("less_than_match_id", new Param("less_than_match_id", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-rank-distribution", new Operation("opendota-rank-distribution", "GET", "/opendota/rank-distribution", Map.of(), List.of("application/json")));
        operations.put("opendota-records", new Operation("opendota-records", "GET", "/opendota/records", Map.ofEntries(Map.entry("field", new Param("field", "query", true, "string", List.of("kills", "deaths", "assists", "last_hits", "denies", "gold_per_min", "xp_per_min", "hero_damage", "tower_damage", "hero_healing", "duration"), "csv"))), List.of("application/json")));
        operations.put("opendota-scenarios", new Operation("opendota-scenarios", "GET", "/opendota/scenarios", Map.ofEntries(Map.entry("kind", new Param("kind", "query", true, "string", List.of("item-timings", "lane-roles", "misc"), "csv")), Map.entry("hero_id", new Param("hero_id", "query", false, "integer", List.of(), "csv")), Map.entry("item", new Param("item", "query", false, "string", List.of(), "csv")), Map.entry("lane_role", new Param("lane_role", "query", false, "integer", List.of(), "csv")), Map.entry("scenario", new Param("scenario", "query", false, "string", List.of("courier_kill", "first_blood", "neg_chat_1min", "pos_chat_1min"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-team", new Operation("opendota-team", "GET", "/opendota/team", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-team-heroes", new Operation("opendota-team-heroes", "GET", "/opendota/team-heroes", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-team-matches", new Operation("opendota-team-matches", "GET", "/opendota/team-matches", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-team-players", new Operation("opendota-team-players", "GET", "/opendota/team-players", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("opendota-teams", new Operation("opendota-teams", "GET", "/opendota/teams", Map.ofEntries(Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown OpenDota operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object abilities(Map<String, ?> params) { return request("opendota-abilities", params); }
    public Object benchmarks(Map<String, ?> params) { return request("opendota-benchmarks", params); }
    public Object constants(Map<String, ?> params) { return request("opendota-constants", params); }
    public Object findMatches(Map<String, ?> params) { return request("opendota-find-matches", params); }
    public Object heroDescriptions(Map<String, ?> params) { return request("opendota-hero-descriptions", params); }
    public Object heroDurations(Map<String, ?> params) { return request("opendota-hero-durations", params); }
    public Object heroItems(Map<String, ?> params) { return request("opendota-hero-items", params); }
    public Object heroMatches(Map<String, ?> params) { return request("opendota-hero-matches", params); }
    public Object heroMatchups(Map<String, ?> params) { return request("opendota-hero-matchups", params); }
    public Object heroStats(Map<String, ?> params) { return request("opendota-hero-stats", params); }
    public Object heroes(Map<String, ?> params) { return request("opendota-heroes", params); }
    public Object items(Map<String, ?> params) { return request("opendota-items", params); }
    public Object league(Map<String, ?> params) { return request("opendota-league", params); }
    public Object leagueMatchIds(Map<String, ?> params) { return request("opendota-league-match-ids", params); }
    public Object leagueMatches(Map<String, ?> params) { return request("opendota-league-matches", params); }
    public Object leagues(Map<String, ?> params) { return request("opendota-leagues", params); }
    public Object live(Map<String, ?> params) { return request("opendota-live", params); }
    public Object match(Map<String, ?> params) { return request("opendota-match", params); }
    public Object patchNotes(Map<String, ?> params) { return request("opendota-patch-notes", params); }
    public Object proMatches(Map<String, ?> params) { return request("opendota-pro-matches", params); }
    public Object proPlayers(Map<String, ?> params) { return request("opendota-pro-players", params); }
    public Object publicMatches(Map<String, ?> params) { return request("opendota-public-matches", params); }
    public Object rankDistribution(Map<String, ?> params) { return request("opendota-rank-distribution", params); }
    public Object records(Map<String, ?> params) { return request("opendota-records", params); }
    public Object scenarios(Map<String, ?> params) { return request("opendota-scenarios", params); }
    public Object team(Map<String, ?> params) { return request("opendota-team", params); }
    public Object teamHeroes(Map<String, ?> params) { return request("opendota-team-heroes", params); }
    public Object teamMatches(Map<String, ?> params) { return request("opendota-team-matches", params); }
    public Object teamPlayers(Map<String, ?> params) { return request("opendota-team-players", params); }
    public Object teams(Map<String, ?> params) { return request("opendota-teams", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
