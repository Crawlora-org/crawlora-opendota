# Crawlora OpenDota API client for Java

The official Java client for Crawlora's hosted OpenDota API. It exposes 30 endpoints covering Dota 2 matches, heroes, players, teams, leagues, statistics, and game constants. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-opendota</artifactId>
  <version>0.1.0</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=opendota-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=opendota-java-console) to get an API key.

```java
import net.crawlora.opendota.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.heroes(Map.of());
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported OpenDota API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-opendota/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=opendota-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-opendota)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=opendota-java-api-docs)
