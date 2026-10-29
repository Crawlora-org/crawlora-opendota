# crawlora-opendota — OpenDota API client for Python

Python client for Crawlora's hosted OpenDota API. It exposes 30 API endpoints covering Dota 2 matches, heroes, players, teams, leagues, statistics, and game constants. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=opendota-python-homepage); the package does not run a browser or scrape
OpenDota locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
OpenDota or its owners.

## Install

```sh
python -m pip install crawlora-opendota
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=opendota-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=opendota-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_opendota import OpenDotaClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with OpenDotaClient(api_key=api_key) as client:
    result_1 = client.heroes()
    print(result_1)
    result_2 = client.pro_matches()
    print(result_2)
```

The package also exports `Client` as an alias for `OpenDotaClient`. Operation
methods are available directly in snake_case and through the `opendota`
group. The async package client is `AsyncOpenDotaClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-opendota/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-opendota/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_opendota import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.heroes()
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-opendota/blob/main/examples/python.py) for a complete usage example.

## Supported OpenDota API endpoints

This package exposes every route below through direct snake_case methods and the `opendota` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-opendota/blob/main/docs/usage.md) for complete input details.

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

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
