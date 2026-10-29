"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class OpenDotaClient(CrawloraClient):
    """Synchronous OpenDota API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-opendota-python/0.1.0')
        super().__init__(*args, **kwargs)

    def abilities(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-abilities', params, response_type=response_type, timeout=timeout, headers=headers)

    def benchmarks(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-benchmarks', params, response_type=response_type, timeout=timeout, headers=headers)

    def constants(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-constants', params, response_type=response_type, timeout=timeout, headers=headers)

    def find_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-find-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def hero_descriptions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-hero-descriptions', params, response_type=response_type, timeout=timeout, headers=headers)

    def hero_durations(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-hero-durations', params, response_type=response_type, timeout=timeout, headers=headers)

    def hero_items(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-hero-items', params, response_type=response_type, timeout=timeout, headers=headers)

    def hero_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-hero-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def hero_matchups(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-hero-matchups', params, response_type=response_type, timeout=timeout, headers=headers)

    def hero_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-hero-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def heroes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-heroes', params, response_type=response_type, timeout=timeout, headers=headers)

    def items(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-items', params, response_type=response_type, timeout=timeout, headers=headers)

    def league(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-league', params, response_type=response_type, timeout=timeout, headers=headers)

    def league_match_ids(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-league-match-ids', params, response_type=response_type, timeout=timeout, headers=headers)

    def league_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-league-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def leagues(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-leagues', params, response_type=response_type, timeout=timeout, headers=headers)

    def live(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-live', params, response_type=response_type, timeout=timeout, headers=headers)

    def match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-match', params, response_type=response_type, timeout=timeout, headers=headers)

    def patch_notes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-patch-notes', params, response_type=response_type, timeout=timeout, headers=headers)

    def pro_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-pro-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def pro_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-pro-players', params, response_type=response_type, timeout=timeout, headers=headers)

    def public_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-public-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def rank_distribution(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-rank-distribution', params, response_type=response_type, timeout=timeout, headers=headers)

    def records(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-records', params, response_type=response_type, timeout=timeout, headers=headers)

    def scenarios(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-scenarios', params, response_type=response_type, timeout=timeout, headers=headers)

    def team(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-team', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_heroes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-team-heroes', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-team-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-team-players', params, response_type=response_type, timeout=timeout, headers=headers)

    def teams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('opendota-teams', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncOpenDotaClient(AsyncCrawloraClient):
    """Asynchronous OpenDota API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-opendota-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def abilities(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-abilities', params, response_type=response_type, timeout=timeout, headers=headers)

    async def benchmarks(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-benchmarks', params, response_type=response_type, timeout=timeout, headers=headers)

    async def constants(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-constants', params, response_type=response_type, timeout=timeout, headers=headers)

    async def find_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-find-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def hero_descriptions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-hero-descriptions', params, response_type=response_type, timeout=timeout, headers=headers)

    async def hero_durations(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-hero-durations', params, response_type=response_type, timeout=timeout, headers=headers)

    async def hero_items(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-hero-items', params, response_type=response_type, timeout=timeout, headers=headers)

    async def hero_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-hero-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def hero_matchups(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-hero-matchups', params, response_type=response_type, timeout=timeout, headers=headers)

    async def hero_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-hero-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def heroes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-heroes', params, response_type=response_type, timeout=timeout, headers=headers)

    async def items(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-items', params, response_type=response_type, timeout=timeout, headers=headers)

    async def league(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-league', params, response_type=response_type, timeout=timeout, headers=headers)

    async def league_match_ids(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-league-match-ids', params, response_type=response_type, timeout=timeout, headers=headers)

    async def league_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-league-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def leagues(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-leagues', params, response_type=response_type, timeout=timeout, headers=headers)

    async def live(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-live', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-match', params, response_type=response_type, timeout=timeout, headers=headers)

    async def patch_notes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-patch-notes', params, response_type=response_type, timeout=timeout, headers=headers)

    async def pro_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-pro-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def pro_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-pro-players', params, response_type=response_type, timeout=timeout, headers=headers)

    async def public_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-public-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def rank_distribution(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-rank-distribution', params, response_type=response_type, timeout=timeout, headers=headers)

    async def records(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-records', params, response_type=response_type, timeout=timeout, headers=headers)

    async def scenarios(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-scenarios', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-team', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_heroes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-team-heroes', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-team-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-team-players', params, response_type=response_type, timeout=timeout, headers=headers)

    async def teams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('opendota-teams', params, response_type=response_type, timeout=timeout, headers=headers)
