# @crawlora-org/opendota — OpenDota API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted OpenDota API.
It exposes 30 API endpoints for Dota 2 matches, heroes, players, teams, leagues, statistics, and game constants through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=opendota-javascript-homepage). It does not run a browser or scrape OpenDota locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by OpenDota or its owners.

## Install

```sh
npm install @crawlora-org/opendota
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=opendota-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=opendota-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { OpenDotaClient } from "@crawlora-org/opendota";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new OpenDotaClient({ apiKey });
const result1 = await client.heroes({});
console.log(result1);
const result2 = await client.proMatches({});
console.log(result2);
```

The client also exports `Client` as an alias for `OpenDotaClient`. Operation
methods are available directly in camelCase and through the `opendota`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-opendota/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-opendota/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported OpenDota API endpoints

This package exposes each route below as a direct method and through the `opendota` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-opendota/blob/main/docs/usage.md) for complete input details.

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

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
