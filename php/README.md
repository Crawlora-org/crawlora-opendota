# Crawlora OpenDota API client for PHP (`crawlora/opendota`)

This PHP package calls Crawlora's hosted OpenDota API at `https://api.crawlora.net/api/v1`. It exposes 30 endpoints covering Dota 2 matches, heroes, players, teams, leagues, statistics, and game constants. It does not call or scrape OpenDota directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/opendota
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=opendota-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=opendota-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Opendota\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("opendota-abilities", ['q' => 'sample']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 30 API operations.

## Supported OpenDota API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-opendota/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=opendota-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=opendota-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-opendota). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-opendota/blob/main/docs/usage.md).
