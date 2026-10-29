from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelOpendotaTeamsResponse = TypedDict('ModelOpendotaTeamsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'next_page': NotRequired[int],
    'page': NotRequired[int],
    'source_url': NotRequired[str],
    'teams': NotRequired[list[ModelOpendotaTeam]],
}, total=False)

ModelOpendotaTeam = TypedDict('ModelOpendotaTeam', {
    'delta': NotRequired[float],
    'id': NotRequired[int],
    'last_match_id': NotRequired[int],
    'last_match_time': NotRequired[str],
    'logo_url': NotRequired[str],
    'losses': NotRequired[int],
    'name': NotRequired[str],
    'rating': NotRequired[float],
    'tag': NotRequired[str],
    'wins': NotRequired[int],
}, total=False)

ModelOpendotaTeamPlayersResponse = TypedDict('ModelOpendotaTeamPlayersResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'players': NotRequired[list[ModelOpendotaTeamPlayer]],
    'source_url': NotRequired[str],
    'team_id': NotRequired[int],
}, total=False)

ModelOpendotaTeamPlayer = TypedDict('ModelOpendotaTeamPlayer', {
    'games_played': NotRequired[int],
    'is_current_team_member': NotRequired[bool],
    'name': NotRequired[str],
    'wins': NotRequired[int],
}, total=False)

ModelOpendotaTeamMatchesResponse = TypedDict('ModelOpendotaTeamMatchesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'matches': NotRequired[list[ModelOpendotaTeamMatch]],
    'source_url': NotRequired[str],
    'team_id': NotRequired[int],
}, total=False)

ModelOpendotaTeamMatch = TypedDict('ModelOpendotaTeamMatch', {
    'dire_score': NotRequired[int],
    'duration_seconds': NotRequired[int],
    'league_id': NotRequired[int],
    'league_name': NotRequired[str],
    'match_id': NotRequired[int],
    'opposing_team_id': NotRequired[int],
    'opposing_team_logo_url': NotRequired[str],
    'opposing_team_name': NotRequired[str],
    'radiant': NotRequired[bool],
    'radiant_score': NotRequired[int],
    'radiant_win': NotRequired[bool],
    'start_time': NotRequired[str],
    'team_win': NotRequired[bool],
}, total=False)

ModelOpendotaTeamHeroesResponse = TypedDict('ModelOpendotaTeamHeroesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'heroes': NotRequired[list[ModelOpendotaHeroRecord]],
    'source_url': NotRequired[str],
    'team_id': NotRequired[int],
}, total=False)

ModelOpendotaHeroRecord = TypedDict('ModelOpendotaHeroRecord', {
    'games': NotRequired[int],
    'hero_id': NotRequired[int],
    'localized_name': NotRequired[str],
    'win_rate_percent': NotRequired[float],
    'wins': NotRequired[int],
}, total=False)

ModelOpendotaTeamResponse = TypedDict('ModelOpendotaTeamResponse', {
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'team': NotRequired[ModelOpendotaTeam],
}, total=False)

ModelOpendotaScenariosResponse = TypedDict('ModelOpendotaScenariosResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'kind': NotRequired[Literal['item-timings', 'lane-roles', 'misc']],
    'rows': NotRequired[list[ModelOpendotaScenarioRow]],
    'source_url': NotRequired[str],
    'timings': NotRequired[list[int]],
    'total': NotRequired[int],
}, total=False)

ModelOpendotaScenarioRow = TypedDict('ModelOpendotaScenarioRow', {
    'games': NotRequired[int],
    'hero_id': NotRequired[int],
    'hero_name': NotRequired[str],
    'is_radiant': NotRequired[bool],
    'item': NotRequired[str],
    'lane_role': NotRequired[int],
    'region_id': NotRequired[int],
    'scenario': NotRequired[str],
    'time_seconds': NotRequired[int],
    'win_rate_percent': NotRequired[float],
    'wins': NotRequired[int],
}, total=False)

ModelOpendotaRecordsResponse = TypedDict('ModelOpendotaRecordsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'field': NotRequired[str],
    'rows': NotRequired[list[ModelOpendotaRecordRow]],
    'source_url': NotRequired[str],
}, total=False)

ModelOpendotaRecordRow = TypedDict('ModelOpendotaRecordRow', {
    'hero_id': NotRequired[int],
    'hero_name': NotRequired[str],
    'match_id': NotRequired[int],
    'rank': NotRequired[int],
    'score': NotRequired[int],
    'start_time': NotRequired[str],
}, total=False)

ModelOpendotaDistributionsResponse = TypedDict('ModelOpendotaDistributionsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'ranks': NotRequired[list[ModelOpendotaRankTierRow]],
    'source_url': NotRequired[str],
    'total_players': NotRequired[int],
}, total=False)

ModelOpendotaRankTierRow = TypedDict('ModelOpendotaRankTierRow', {
    'cumulative_percent': NotRequired[float],
    'cumulative_players': NotRequired[int],
    'medal': NotRequired[str],
    'players': NotRequired[int],
    'rank_tier': NotRequired[int],
    'share_percent': NotRequired[float],
    'stars': NotRequired[int],
}, total=False)

ModelOpendotaPublicMatchesResponse = TypedDict('ModelOpendotaPublicMatchesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'matches': NotRequired[list[ModelOpendotaPublicMatchRow]],
    'max_rank': NotRequired[int],
    'min_rank': NotRequired[int],
    'next_less_than_match_id': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelOpendotaPublicMatchRow = TypedDict('ModelOpendotaPublicMatchRow', {
    'avg_rank_medal': NotRequired[str],
    'avg_rank_tier': NotRequired[int],
    'cluster': NotRequired[int],
    'dire_heroes': NotRequired[list[ModelOpendotaPickedHero]],
    'duration_seconds': NotRequired[int],
    'game_mode': NotRequired[int],
    'lobby_type': NotRequired[int],
    'match_id': NotRequired[int],
    'radiant_heroes': NotRequired[list[ModelOpendotaPickedHero]],
    'radiant_win': NotRequired[bool],
    'ranked_players': NotRequired[int],
    'start_time': NotRequired[str],
}, total=False)

ModelOpendotaPickedHero = TypedDict('ModelOpendotaPickedHero', {
    'hero_id': NotRequired[int],
    'localized_name': NotRequired[str],
}, total=False)

ModelOpendotaProPlayersResponse = TypedDict('ModelOpendotaProPlayersResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'next_offset': NotRequired[int],
    'offset': NotRequired[int],
    'players': NotRequired[list[ModelOpendotaProPlayer]],
    'q': NotRequired[str],
    'source_url': NotRequired[str],
    'team_id': NotRequired[int],
    'total_count': NotRequired[int],
}, total=False)

ModelOpendotaProPlayer = TypedDict('ModelOpendotaProPlayer', {
    'country_code': NotRequired[str],
    'is_pro': NotRequired[bool],
    'name': NotRequired[str],
    'persona_name': NotRequired[str],
    'team_id': NotRequired[int],
    'team_name': NotRequired[str],
    'team_tag': NotRequired[str],
}, total=False)

ModelOpendotaProMatchesResponse = TypedDict('ModelOpendotaProMatchesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'matches': NotRequired[list[ModelOpendotaProMatch]],
    'next_less_than_match_id': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelOpendotaProMatch = TypedDict('ModelOpendotaProMatch', {
    'dire_name': NotRequired[str],
    'dire_score': NotRequired[int],
    'dire_team_id': NotRequired[int],
    'duration_seconds': NotRequired[int],
    'league_id': NotRequired[int],
    'league_name': NotRequired[str],
    'match_id': NotRequired[int],
    'radiant_name': NotRequired[str],
    'radiant_score': NotRequired[int],
    'radiant_team_id': NotRequired[int],
    'radiant_win': NotRequired[bool],
    'series_id': NotRequired[int],
    'start_time': NotRequired[str],
    'version': NotRequired[int],
}, total=False)

ModelOpendotaPatchNotesResponse = TypedDict('ModelOpendotaPatchNotesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'general': NotRequired[list[str]],
    'heroes': NotRequired[list[ModelOpendotaPatchHeroChange]],
    'items': NotRequired[list[ModelOpendotaPatchItemChange]],
    'misc': NotRequired[list[str]],
    'patch': NotRequired[str],
    'patches': NotRequired[list[ModelOpendotaPatchIndexEntry]],
    'source_url': NotRequired[str],
    'version': NotRequired[str],
}, total=False)

ModelOpendotaPatchIndexEntry = TypedDict('ModelOpendotaPatchIndexEntry', {
    'heroes_changed': NotRequired[int],
    'items_changed': NotRequired[int],
    'patch': NotRequired[str],
    'version': NotRequired[str],
}, total=False)

ModelOpendotaPatchItemChange = TypedDict('ModelOpendotaPatchItemChange', {
    'key': NotRequired[str],
    'notes': NotRequired[list[str]],
}, total=False)

ModelOpendotaPatchHeroChange = TypedDict('ModelOpendotaPatchHeroChange', {
    'abilities': NotRequired[list[ModelOpendotaPatchAbilityChange]],
    'general': NotRequired[list[str]],
    'hero_id': NotRequired[int],
    'key': NotRequired[str],
    'name': NotRequired[str],
    'talents': NotRequired[list[str]],
}, total=False)

ModelOpendotaPatchAbilityChange = TypedDict('ModelOpendotaPatchAbilityChange', {
    'key': NotRequired[str],
    'notes': NotRequired[list[str]],
}, total=False)

ModelOpendotaMatchDetail = TypedDict('ModelOpendotaMatchDetail', {
    'dire': NotRequired[ModelOpendotaMatchTeam],
    'dire_score': NotRequired[int],
    'duration_seconds': NotRequired[int],
    'fetched_at': NotRequired[str],
    'league_id': NotRequired[int],
    'league_name': NotRequired[str],
    'match_id': NotRequired[int],
    'patch': NotRequired[int],
    'players': NotRequired[list[ModelOpendotaMatchPlayer]],
    'radiant': NotRequired[ModelOpendotaMatchTeam],
    'radiant_score': NotRequired[int],
    'radiant_win': NotRequired[bool],
    'source_url': NotRequired[str],
    'start_time': NotRequired[str],
}, total=False)

ModelOpendotaMatchTeam = TypedDict('ModelOpendotaMatchTeam', {
    'id': NotRequired[int],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'tag': NotRequired[str],
}, total=False)

ModelOpendotaMatchPlayer = TypedDict('ModelOpendotaMatchPlayer', {
    'assists': NotRequired[int],
    'deaths': NotRequired[int],
    'denies': NotRequired[int],
    'gold_per_min': NotRequired[int],
    'hero_damage': NotRequired[int],
    'hero_id': NotRequired[int],
    'is_radiant': NotRequired[bool],
    'kills': NotRequired[int],
    'last_hits': NotRequired[int],
    'level': NotRequired[int],
    'name': NotRequired[str],
    'net_worth': NotRequired[int],
    'tower_damage': NotRequired[int],
    'xp_per_min': NotRequired[int],
}, total=False)

ModelOpendotaLiveMatchesResponse = TypedDict('ModelOpendotaLiveMatchesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'matches': NotRequired[list[ModelOpendotaLiveMatch]],
    'source_url': NotRequired[str],
}, total=False)

ModelOpendotaLiveMatch = TypedDict('ModelOpendotaLiveMatch', {
    'delay_seconds': NotRequired[int],
    'dire_name': NotRequired[str],
    'dire_score': NotRequired[int],
    'game_time_seconds': NotRequired[int],
    'last_update_time': NotRequired[int],
    'league_id': NotRequired[int],
    'match_id': NotRequired[int],
    'players': NotRequired[list[ModelOpendotaLivePlayer]],
    'radiant_lead': NotRequired[int],
    'radiant_name': NotRequired[str],
    'radiant_score': NotRequired[int],
    'spectators': NotRequired[int],
}, total=False)

ModelOpendotaLivePlayer = TypedDict('ModelOpendotaLivePlayer', {
    'hero_id': NotRequired[int],
    'name': NotRequired[str],
    'team_code': NotRequired[Literal['0', '1']],
    'team_slot': NotRequired[Literal['1', '2', '3', '4', '5']],
}, total=False)

ModelOpendotaLeaguesResponse = TypedDict('ModelOpendotaLeaguesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'leagues': NotRequired[list[ModelOpendotaLeague]],
    'source_url': NotRequired[str],
    'tier_filter': NotRequired[str],
}, total=False)

ModelOpendotaLeague = TypedDict('ModelOpendotaLeague', {
    'banner': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'ticket': NotRequired[str],
    'tier': NotRequired[str],
}, total=False)

ModelOpendotaLeagueMatchesResponse = TypedDict('ModelOpendotaLeagueMatchesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'league_id': NotRequired[int],
    'matches': NotRequired[list[ModelOpendotaLeagueMatch]],
    'source_url': NotRequired[str],
    'team_id': NotRequired[int],
}, total=False)

ModelOpendotaLeagueMatch = TypedDict('ModelOpendotaLeagueMatch', {
    'dire_name': NotRequired[str],
    'dire_score': NotRequired[int],
    'dire_team_id': NotRequired[int],
    'duration_seconds': NotRequired[int],
    'league_id': NotRequired[int],
    'match_id': NotRequired[int],
    'radiant_name': NotRequired[str],
    'radiant_score': NotRequired[int],
    'radiant_team_id': NotRequired[int],
    'radiant_win': NotRequired[bool],
    'series_id': NotRequired[int],
    'series_type': NotRequired[int],
    'start_time': NotRequired[str],
}, total=False)

ModelOpendotaLeagueMatchIdsResponse = TypedDict('ModelOpendotaLeagueMatchIdsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'league_id': NotRequired[int],
    'match_ids': NotRequired[list[int]],
    'source_url': NotRequired[str],
}, total=False)

ModelOpendotaLeagueDetailResponse = TypedDict('ModelOpendotaLeagueDetailResponse', {
    'fetched_at': NotRequired[str],
    'league': NotRequired[ModelOpendotaLeague],
    'source_url': NotRequired[str],
    'teams': NotRequired[list[ModelOpendotaTeam]],
}, total=False)

ModelOpendotaItemsResponse = TypedDict('ModelOpendotaItemsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'items': NotRequired[list[ModelOpendotaItemSummary]],
    'qualities': NotRequired[list[str]],
    'source_url': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelOpendotaItemSummary = TypedDict('ModelOpendotaItemSummary', {
    'abilities': NotRequired[list[ModelOpendotaItemAbility]],
    'attributes': NotRequired[list[ModelOpendotaItemAttribute]],
    'behavior': NotRequired[str],
    'components': NotRequired[list[str]],
    'cooldown': NotRequired[str],
    'cost_gold': NotRequired[int],
    'id': NotRequired[int],
    'key': NotRequired[str],
    'mana_cost': NotRequired[str],
    'name': NotRequired[str],
    'quality': NotRequired[str],
}, total=False)

ModelOpendotaItemAttribute = TypedDict('ModelOpendotaItemAttribute', {
    'key': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelOpendotaItemAbility = TypedDict('ModelOpendotaItemAbility', {
    'description': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelOpendotaHeroesResponse = TypedDict('ModelOpendotaHeroesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'heroes': NotRequired[list[ModelOpendotaHero]],
    'source_url': NotRequired[str],
}, total=False)

ModelOpendotaHero = TypedDict('ModelOpendotaHero', {
    'attack_type': NotRequired[Literal['Melee', 'Ranged']],
    'id': NotRequired[int],
    'localized_name': NotRequired[str],
    'name': NotRequired[str],
    'primary_attr': NotRequired[Literal['agi', 'all', 'int', 'str']],
}, total=False)

ModelOpendotaHeroStatsResponse = TypedDict('ModelOpendotaHeroStatsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'heroes': NotRequired[list[ModelOpendotaHeroStat]],
    'source_url': NotRequired[str],
}, total=False)

ModelOpendotaHeroStat = TypedDict('ModelOpendotaHeroStat', {
    'attack_range': NotRequired[int],
    'attack_type': NotRequired[Literal['Melee', 'Ranged']],
    'base_armor': NotRequired[float],
    'base_attack_max': NotRequired[int],
    'base_attack_min': NotRequired[int],
    'base_health': NotRequired[int],
    'base_mana': NotRequired[int],
    'id': NotRequired[int],
    'localized_name': NotRequired[str],
    'move_speed': NotRequired[int],
    'name': NotRequired[str],
    'primary_attr': NotRequired[Literal['agi', 'all', 'int', 'str']],
    'pro': NotRequired[ModelOpendotaPickWin],
    'public': NotRequired[ModelOpendotaPickWin],
    'rank_brackets': NotRequired[list[ModelOpendotaRankBracket]],
    'roles': NotRequired[list[str]],
    'turbo': NotRequired[ModelOpendotaPickWin],
}, total=False)

ModelOpendotaPickWin = TypedDict('ModelOpendotaPickWin', {
    'bans': NotRequired[int],
    'picks': NotRequired[int],
    'win_rate_percent': NotRequired[float],
    'wins': NotRequired[int],
}, total=False)

ModelOpendotaRankBracket = TypedDict('ModelOpendotaRankBracket', {
    'bracket': NotRequired[Literal['1', '2', '3', '4', '5', '6', '7', '8']],
    'name': NotRequired[Literal['Herald', 'Guardian', 'Crusader', 'Archon', 'Legend', 'Ancient', 'Divine', 'Immortal']],
    'picks': NotRequired[int],
    'win_rate_percent': NotRequired[float],
    'wins': NotRequired[int],
}, total=False)

ModelOpendotaHeroMatchupsResponse = TypedDict('ModelOpendotaHeroMatchupsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'hero_id': NotRequired[int],
    'matchups': NotRequired[list[ModelOpendotaHeroRecord]],
    'source_url': NotRequired[str],
}, total=False)

ModelOpendotaHeroMatchesResponse = TypedDict('ModelOpendotaHeroMatchesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'hero_id': NotRequired[int],
    'localized_name': NotRequired[str],
    'matches': NotRequired[list[ModelOpendotaHeroMatchRow]],
    'source_url': NotRequired[str],
}, total=False)

ModelOpendotaHeroMatchRow = TypedDict('ModelOpendotaHeroMatchRow', {
    'assists': NotRequired[int],
    'deaths': NotRequired[int],
    'duration_seconds': NotRequired[int],
    'kills': NotRequired[int],
    'league_id': NotRequired[int],
    'league_name': NotRequired[str],
    'match_id': NotRequired[int],
    'played_radiant': NotRequired[bool],
    'start_time': NotRequired[str],
    'won': NotRequired[bool],
}, total=False)

ModelOpendotaHeroItemsResponse = TypedDict('ModelOpendotaHeroItemsResponse', {
    'fetched_at': NotRequired[str],
    'hero_id': NotRequired[int],
    'phases': NotRequired[list[ModelOpendotaItemPhase]],
    'source_url': NotRequired[str],
}, total=False)

ModelOpendotaItemPhase = TypedDict('ModelOpendotaItemPhase', {
    'items': NotRequired[list[ModelOpendotaItemCount]],
    'phase': NotRequired[Literal['start_game', 'early_game', 'mid_game', 'late_game']],
}, total=False)

ModelOpendotaItemCount = TypedDict('ModelOpendotaItemCount', {
    'count': NotRequired[int],
    'item_id': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelOpendotaHeroDurationsResponse = TypedDict('ModelOpendotaHeroDurationsResponse', {
    'bins': NotRequired[list[ModelOpendotaDurationBin]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'hero_id': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelOpendotaDurationBin = TypedDict('ModelOpendotaDurationBin', {
    'games': NotRequired[int],
    'start_minute': NotRequired[int],
    'win_rate_percent': NotRequired[float],
    'wins': NotRequired[int],
}, total=False)

ModelOpendotaHeroDescriptionsResponse = TypedDict('ModelOpendotaHeroDescriptionsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'hero_id': NotRequired[int],
    'heroes': NotRequired[list[ModelOpendotaHeroDescription]],
    'include_lore': NotRequired[bool],
    'source_url': NotRequired[str],
}, total=False)

ModelOpendotaHeroDescription = TypedDict('ModelOpendotaHeroDescription', {
    'hero_id': NotRequired[int],
    'key': NotRequired[str],
    'lore': NotRequired[str],
    'name': NotRequired[str],
    'scepter': NotRequired[ModelOpendotaAghanimUpgrade],
    'shard': NotRequired[ModelOpendotaAghanimUpgrade],
}, total=False)

ModelOpendotaAghanimUpgrade = TypedDict('ModelOpendotaAghanimUpgrade', {
    'available': NotRequired[bool],
    'description': NotRequired[str],
    'new_skill': NotRequired[bool],
    'skill_name': NotRequired[str],
}, total=False)

ModelOpendotaFindMatchesResponse = TypedDict('ModelOpendotaFindMatchesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'matches': NotRequired[list[ModelOpendotaFindMatchRow]],
    'source_url': NotRequired[str],
    'team_a_hero_ids': NotRequired[list[int]],
    'team_b_hero_ids': NotRequired[list[int]],
}, total=False)

ModelOpendotaFindMatchRow = TypedDict('ModelOpendotaFindMatchRow', {
    'dire': NotRequired[list[ModelOpendotaPickedHero]],
    'match_id': NotRequired[int],
    'radiant': NotRequired[list[ModelOpendotaPickedHero]],
    'radiant_win': NotRequired[bool],
    'start_time': NotRequired[str],
    'team_a_side': NotRequired[Literal['radiant', 'dire']],
    'team_a_win': NotRequired[bool],
}, total=False)

ModelOpendotaConstantsResponse = TypedDict('ModelOpendotaConstantsResponse', {
    'count': NotRequired[int],
    'entries': NotRequired[list[ModelOpendotaConstantEntry]],
    'fetched_at': NotRequired[str],
    'resource': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelOpendotaConstantEntry = TypedDict('ModelOpendotaConstantEntry', {
    'balanced': NotRequired[bool],
    'date': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'text': NotRequired[str],
    'value': NotRequired[int],
}, total=False)

ModelOpendotaBenchmarksResponse = TypedDict('ModelOpendotaBenchmarksResponse', {
    'benchmarks': NotRequired[list[ModelOpendotaBenchmark]],
    'bracket': NotRequired[int],
    'bracket_name': NotRequired[str],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'hero_id': NotRequired[int],
    'hero_name': NotRequired[str],
    'role': NotRequired[Literal['core', 'support']],
    'source_url': NotRequired[str],
}, total=False)

ModelOpendotaBenchmark = TypedDict('ModelOpendotaBenchmark', {
    'metric': NotRequired[str],
    'points': NotRequired[list[ModelOpendotaBenchmarkPoint]],
}, total=False)

ModelOpendotaBenchmarkPoint = TypedDict('ModelOpendotaBenchmarkPoint', {
    'percentile': NotRequired[float],
    'value': NotRequired[float],
}, total=False)

ModelOpendotaAbilitiesResponse = TypedDict('ModelOpendotaAbilitiesResponse', {
    'abilities': NotRequired[list[ModelOpendotaAbilitySummary]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelOpendotaAbilitySummary = TypedDict('ModelOpendotaAbilitySummary', {
    'behavior': NotRequired[list[str]],
    'bkb_pierce': NotRequired[str],
    'cooldown': NotRequired[str],
    'damage_type': NotRequired[str],
    'description': NotRequired[str],
    'dispellable': NotRequired[str],
    'innate': NotRequired[bool],
    'key': NotRequired[str],
    'mana_cost': NotRequired[str],
    'name': NotRequired[str],
    'target_team': NotRequired[str],
    'target_type': NotRequired[str],
}, total=False)

OpendotaAbilitiesResponse = Any
OpendotaAbilitiesParams = TypedDict('OpendotaAbilitiesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

OpendotaBenchmarksResponse = Any
OpendotaBenchmarksParams = TypedDict('OpendotaBenchmarksParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'hero_id': Required[int],
    'bracket': NotRequired[int],
    'role': NotRequired[Literal['core', 'support']],
}, total=False)

OpendotaConstantsResponse = Any
OpendotaConstantsParams = TypedDict('OpendotaConstantsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'resource': Required[Literal['game_mode', 'lobby_type', 'patch', 'region', 'cluster', 'item_ids', 'ability_ids', 'permanent_buffs', 'xp_level', 'countries', 'order_types', 'player_colors', 'chat_wheel', 'item_colors', 'ancients', 'skillshots']],
}, total=False)

OpendotaFindMatchesResponse = Any
OpendotaFindMatchesParams = TypedDict('OpendotaFindMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_a': NotRequired[str],
    'team_b': NotRequired[str],
}, total=False)

OpendotaHeroDescriptionsResponse = Any
OpendotaHeroDescriptionsParams = TypedDict('OpendotaHeroDescriptionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'hero_id': NotRequired[int],
    'include_lore': NotRequired[bool],
}, total=False)

OpendotaHeroDurationsResponse = Any
OpendotaHeroDurationsParams = TypedDict('OpendotaHeroDurationsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'hero_id': Required[int],
}, total=False)

OpendotaHeroItemsResponse = Any
OpendotaHeroItemsParams = TypedDict('OpendotaHeroItemsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'hero_id': Required[int],
}, total=False)

OpendotaHeroMatchesResponse = Any
OpendotaHeroMatchesParams = TypedDict('OpendotaHeroMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'hero_id': Required[int],
}, total=False)

OpendotaHeroMatchupsResponse = Any
OpendotaHeroMatchupsParams = TypedDict('OpendotaHeroMatchupsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'hero_id': Required[int],
}, total=False)

OpendotaHeroStatsResponse = Any
OpendotaHeroStatsParams = TypedDict('OpendotaHeroStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'primary_attr': NotRequired[Literal['agi', 'all', 'int', 'str']],
    'attack_type': NotRequired[Literal['Melee', 'Ranged']],
    'role': NotRequired[Literal['Carry', 'Disabler', 'Durable', 'Escape', 'Initiator', 'Nuker', 'Pusher', 'Support']],
    'sort': NotRequired[Literal['id', 'name', 'pro_pick', 'pro_win', 'pro_ban', 'pro_win_rate', 'pub_pick', 'pub_win', 'pub_win_rate', 'turbo_pick', 'turbo_win_rate']],
    'desc': NotRequired[bool],
    'limit': NotRequired[int],
}, total=False)

OpendotaHeroesResponse = Any
OpendotaHeroesParams = TypedDict('OpendotaHeroesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

OpendotaItemsResponse = Any
OpendotaItemsParams = TypedDict('OpendotaItemsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': NotRequired[str],
    'quality': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

OpendotaLeagueResponse = Any
OpendotaLeagueParams = TypedDict('OpendotaLeagueParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[int],
}, total=False)

OpendotaLeagueMatchIdsResponse = Any
OpendotaLeagueMatchIdsParams = TypedDict('OpendotaLeagueMatchIdsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[int],
}, total=False)

OpendotaLeagueMatchesResponse = Any
OpendotaLeagueMatchesParams = TypedDict('OpendotaLeagueMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league_id': Required[int],
    'team_id': NotRequired[int],
}, total=False)

OpendotaLeaguesResponse = Any
OpendotaLeaguesParams = TypedDict('OpendotaLeaguesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tier': NotRequired[Literal['amateur', 'excluded', 'premium', 'professional', 'unrated']],
}, total=False)

OpendotaLiveResponse = Any
OpendotaLiveParams = TypedDict('OpendotaLiveParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

OpendotaMatchResponse = Any
OpendotaMatchParams = TypedDict('OpendotaMatchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[int],
}, total=False)

OpendotaPatchNotesResponse = Any
OpendotaPatchNotesParams = TypedDict('OpendotaPatchNotesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'patch': NotRequired[str],
}, total=False)

OpendotaProMatchesResponse = Any
OpendotaProMatchesParams = TypedDict('OpendotaProMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'less_than_match_id': NotRequired[int],
}, total=False)

OpendotaProPlayersResponse = Any
OpendotaProPlayersParams = TypedDict('OpendotaProPlayersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': NotRequired[int],
    'q': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

OpendotaPublicMatchesResponse = Any
OpendotaPublicMatchesParams = TypedDict('OpendotaPublicMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'min_rank': NotRequired[Literal['11', '12', '13', '14', '15', '21', '22', '23', '24', '25', '31', '32', '33', '34', '35', '41', '42', '43', '44', '45', '51', '52', '53', '54', '55', '61', '62', '63', '64', '65', '71', '72', '73', '74', '75', '81', '82', '83', '84', '85']],
    'max_rank': NotRequired[Literal['11', '12', '13', '14', '15', '21', '22', '23', '24', '25', '31', '32', '33', '34', '35', '41', '42', '43', '44', '45', '51', '52', '53', '54', '55', '61', '62', '63', '64', '65', '71', '72', '73', '74', '75', '81', '82', '83', '84', '85']],
    'less_than_match_id': NotRequired[int],
}, total=False)

OpendotaRankDistributionResponse = Any
OpendotaRankDistributionParams = TypedDict('OpendotaRankDistributionParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

OpendotaRecordsResponse = Any
OpendotaRecordsParams = TypedDict('OpendotaRecordsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'field': Required[Literal['kills', 'deaths', 'assists', 'last_hits', 'denies', 'gold_per_min', 'xp_per_min', 'hero_damage', 'tower_damage', 'hero_healing', 'duration']],
}, total=False)

OpendotaScenariosResponse = Any
OpendotaScenariosParams = TypedDict('OpendotaScenariosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'kind': Required[Literal['item-timings', 'lane-roles', 'misc']],
    'hero_id': NotRequired[int],
    'item': NotRequired[str],
    'lane_role': NotRequired[int],
    'scenario': NotRequired[Literal['courier_kill', 'first_blood', 'neg_chat_1min', 'pos_chat_1min']],
    'limit': NotRequired[int],
}, total=False)

OpendotaTeamResponse = Any
OpendotaTeamParams = TypedDict('OpendotaTeamParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[int],
}, total=False)

OpendotaTeamHeroesResponse = Any
OpendotaTeamHeroesParams = TypedDict('OpendotaTeamHeroesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[int],
}, total=False)

OpendotaTeamMatchesResponse = Any
OpendotaTeamMatchesParams = TypedDict('OpendotaTeamMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[int],
}, total=False)

OpendotaTeamPlayersResponse = Any
OpendotaTeamPlayersParams = TypedDict('OpendotaTeamPlayersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[int],
}, total=False)

OpendotaTeamsResponse = Any
OpendotaTeamsParams = TypedDict('OpendotaTeamsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'page': NotRequired[int],
}, total=False)

class OpendotaGroup:
    @overload
    def abilities(self, **params: Unpack[OpendotaAbilitiesStreamParams]) -> BinaryIO: ...
    @overload
    def abilities(self, **params: Unpack[OpendotaAbilitiesTextResponseParams]) -> str: ...
    @overload
    def abilities(self, **params: Unpack[OpendotaAbilitiesDefaultParams]) -> OpendotaAbilitiesResponse: ...
    @overload
    def benchmarks(self, **params: Unpack[OpendotaBenchmarksStreamParams]) -> BinaryIO: ...
    @overload
    def benchmarks(self, **params: Unpack[OpendotaBenchmarksTextResponseParams]) -> str: ...
    @overload
    def benchmarks(self, **params: Unpack[OpendotaBenchmarksDefaultParams]) -> OpendotaBenchmarksResponse: ...
    @overload
    def constants(self, **params: Unpack[OpendotaConstantsStreamParams]) -> BinaryIO: ...
    @overload
    def constants(self, **params: Unpack[OpendotaConstantsTextResponseParams]) -> str: ...
    @overload
    def constants(self, **params: Unpack[OpendotaConstantsDefaultParams]) -> OpendotaConstantsResponse: ...
    @overload
    def find_matches(self, **params: Unpack[OpendotaFindMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def find_matches(self, **params: Unpack[OpendotaFindMatchesTextResponseParams]) -> str: ...
    @overload
    def find_matches(self, **params: Unpack[OpendotaFindMatchesDefaultParams]) -> OpendotaFindMatchesResponse: ...
    @overload
    def hero_descriptions(self, **params: Unpack[OpendotaHeroDescriptionsStreamParams]) -> BinaryIO: ...
    @overload
    def hero_descriptions(self, **params: Unpack[OpendotaHeroDescriptionsTextResponseParams]) -> str: ...
    @overload
    def hero_descriptions(self, **params: Unpack[OpendotaHeroDescriptionsDefaultParams]) -> OpendotaHeroDescriptionsResponse: ...
    @overload
    def hero_durations(self, **params: Unpack[OpendotaHeroDurationsStreamParams]) -> BinaryIO: ...
    @overload
    def hero_durations(self, **params: Unpack[OpendotaHeroDurationsTextResponseParams]) -> str: ...
    @overload
    def hero_durations(self, **params: Unpack[OpendotaHeroDurationsDefaultParams]) -> OpendotaHeroDurationsResponse: ...
    @overload
    def hero_items(self, **params: Unpack[OpendotaHeroItemsStreamParams]) -> BinaryIO: ...
    @overload
    def hero_items(self, **params: Unpack[OpendotaHeroItemsTextResponseParams]) -> str: ...
    @overload
    def hero_items(self, **params: Unpack[OpendotaHeroItemsDefaultParams]) -> OpendotaHeroItemsResponse: ...
    @overload
    def hero_matches(self, **params: Unpack[OpendotaHeroMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def hero_matches(self, **params: Unpack[OpendotaHeroMatchesTextResponseParams]) -> str: ...
    @overload
    def hero_matches(self, **params: Unpack[OpendotaHeroMatchesDefaultParams]) -> OpendotaHeroMatchesResponse: ...
    @overload
    def hero_matchups(self, **params: Unpack[OpendotaHeroMatchupsStreamParams]) -> BinaryIO: ...
    @overload
    def hero_matchups(self, **params: Unpack[OpendotaHeroMatchupsTextResponseParams]) -> str: ...
    @overload
    def hero_matchups(self, **params: Unpack[OpendotaHeroMatchupsDefaultParams]) -> OpendotaHeroMatchupsResponse: ...
    @overload
    def hero_stats(self, **params: Unpack[OpendotaHeroStatsStreamParams]) -> BinaryIO: ...
    @overload
    def hero_stats(self, **params: Unpack[OpendotaHeroStatsTextResponseParams]) -> str: ...
    @overload
    def hero_stats(self, **params: Unpack[OpendotaHeroStatsDefaultParams]) -> OpendotaHeroStatsResponse: ...
    @overload
    def heroes(self, **params: Unpack[OpendotaHeroesStreamParams]) -> BinaryIO: ...
    @overload
    def heroes(self, **params: Unpack[OpendotaHeroesTextResponseParams]) -> str: ...
    @overload
    def heroes(self, **params: Unpack[OpendotaHeroesDefaultParams]) -> OpendotaHeroesResponse: ...
    @overload
    def items(self, **params: Unpack[OpendotaItemsStreamParams]) -> BinaryIO: ...
    @overload
    def items(self, **params: Unpack[OpendotaItemsTextResponseParams]) -> str: ...
    @overload
    def items(self, **params: Unpack[OpendotaItemsDefaultParams]) -> OpendotaItemsResponse: ...
    @overload
    def league(self, **params: Unpack[OpendotaLeagueStreamParams]) -> BinaryIO: ...
    @overload
    def league(self, **params: Unpack[OpendotaLeagueTextResponseParams]) -> str: ...
    @overload
    def league(self, **params: Unpack[OpendotaLeagueDefaultParams]) -> OpendotaLeagueResponse: ...
    @overload
    def league_match_ids(self, **params: Unpack[OpendotaLeagueMatchIdsStreamParams]) -> BinaryIO: ...
    @overload
    def league_match_ids(self, **params: Unpack[OpendotaLeagueMatchIdsTextResponseParams]) -> str: ...
    @overload
    def league_match_ids(self, **params: Unpack[OpendotaLeagueMatchIdsDefaultParams]) -> OpendotaLeagueMatchIdsResponse: ...
    @overload
    def league_matches(self, **params: Unpack[OpendotaLeagueMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def league_matches(self, **params: Unpack[OpendotaLeagueMatchesTextResponseParams]) -> str: ...
    @overload
    def league_matches(self, **params: Unpack[OpendotaLeagueMatchesDefaultParams]) -> OpendotaLeagueMatchesResponse: ...
    @overload
    def leagues(self, **params: Unpack[OpendotaLeaguesStreamParams]) -> BinaryIO: ...
    @overload
    def leagues(self, **params: Unpack[OpendotaLeaguesTextResponseParams]) -> str: ...
    @overload
    def leagues(self, **params: Unpack[OpendotaLeaguesDefaultParams]) -> OpendotaLeaguesResponse: ...
    @overload
    def live(self, **params: Unpack[OpendotaLiveStreamParams]) -> BinaryIO: ...
    @overload
    def live(self, **params: Unpack[OpendotaLiveTextResponseParams]) -> str: ...
    @overload
    def live(self, **params: Unpack[OpendotaLiveDefaultParams]) -> OpendotaLiveResponse: ...
    @overload
    def match(self, **params: Unpack[OpendotaMatchStreamParams]) -> BinaryIO: ...
    @overload
    def match(self, **params: Unpack[OpendotaMatchTextResponseParams]) -> str: ...
    @overload
    def match(self, **params: Unpack[OpendotaMatchDefaultParams]) -> OpendotaMatchResponse: ...
    @overload
    def patch_notes(self, **params: Unpack[OpendotaPatchNotesStreamParams]) -> BinaryIO: ...
    @overload
    def patch_notes(self, **params: Unpack[OpendotaPatchNotesTextResponseParams]) -> str: ...
    @overload
    def patch_notes(self, **params: Unpack[OpendotaPatchNotesDefaultParams]) -> OpendotaPatchNotesResponse: ...
    @overload
    def pro_matches(self, **params: Unpack[OpendotaProMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def pro_matches(self, **params: Unpack[OpendotaProMatchesTextResponseParams]) -> str: ...
    @overload
    def pro_matches(self, **params: Unpack[OpendotaProMatchesDefaultParams]) -> OpendotaProMatchesResponse: ...
    @overload
    def pro_players(self, **params: Unpack[OpendotaProPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def pro_players(self, **params: Unpack[OpendotaProPlayersTextResponseParams]) -> str: ...
    @overload
    def pro_players(self, **params: Unpack[OpendotaProPlayersDefaultParams]) -> OpendotaProPlayersResponse: ...
    @overload
    def public_matches(self, **params: Unpack[OpendotaPublicMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def public_matches(self, **params: Unpack[OpendotaPublicMatchesTextResponseParams]) -> str: ...
    @overload
    def public_matches(self, **params: Unpack[OpendotaPublicMatchesDefaultParams]) -> OpendotaPublicMatchesResponse: ...
    @overload
    def rank_distribution(self, **params: Unpack[OpendotaRankDistributionStreamParams]) -> BinaryIO: ...
    @overload
    def rank_distribution(self, **params: Unpack[OpendotaRankDistributionTextResponseParams]) -> str: ...
    @overload
    def rank_distribution(self, **params: Unpack[OpendotaRankDistributionDefaultParams]) -> OpendotaRankDistributionResponse: ...
    @overload
    def records(self, **params: Unpack[OpendotaRecordsStreamParams]) -> BinaryIO: ...
    @overload
    def records(self, **params: Unpack[OpendotaRecordsTextResponseParams]) -> str: ...
    @overload
    def records(self, **params: Unpack[OpendotaRecordsDefaultParams]) -> OpendotaRecordsResponse: ...
    @overload
    def scenarios(self, **params: Unpack[OpendotaScenariosStreamParams]) -> BinaryIO: ...
    @overload
    def scenarios(self, **params: Unpack[OpendotaScenariosTextResponseParams]) -> str: ...
    @overload
    def scenarios(self, **params: Unpack[OpendotaScenariosDefaultParams]) -> OpendotaScenariosResponse: ...
    @overload
    def team(self, **params: Unpack[OpendotaTeamStreamParams]) -> BinaryIO: ...
    @overload
    def team(self, **params: Unpack[OpendotaTeamTextResponseParams]) -> str: ...
    @overload
    def team(self, **params: Unpack[OpendotaTeamDefaultParams]) -> OpendotaTeamResponse: ...
    @overload
    def team_heroes(self, **params: Unpack[OpendotaTeamHeroesStreamParams]) -> BinaryIO: ...
    @overload
    def team_heroes(self, **params: Unpack[OpendotaTeamHeroesTextResponseParams]) -> str: ...
    @overload
    def team_heroes(self, **params: Unpack[OpendotaTeamHeroesDefaultParams]) -> OpendotaTeamHeroesResponse: ...
    @overload
    def team_matches(self, **params: Unpack[OpendotaTeamMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def team_matches(self, **params: Unpack[OpendotaTeamMatchesTextResponseParams]) -> str: ...
    @overload
    def team_matches(self, **params: Unpack[OpendotaTeamMatchesDefaultParams]) -> OpendotaTeamMatchesResponse: ...
    @overload
    def team_players(self, **params: Unpack[OpendotaTeamPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def team_players(self, **params: Unpack[OpendotaTeamPlayersTextResponseParams]) -> str: ...
    @overload
    def team_players(self, **params: Unpack[OpendotaTeamPlayersDefaultParams]) -> OpendotaTeamPlayersResponse: ...
    @overload
    def teams(self, **params: Unpack[OpendotaTeamsStreamParams]) -> BinaryIO: ...
    @overload
    def teams(self, **params: Unpack[OpendotaTeamsTextResponseParams]) -> str: ...
    @overload
    def teams(self, **params: Unpack[OpendotaTeamsDefaultParams]) -> OpendotaTeamsResponse: ...

OperationId = Literal[
    'opendota-abilities',
    'opendota-benchmarks',
    'opendota-constants',
    'opendota-find-matches',
    'opendota-hero-descriptions',
    'opendota-hero-durations',
    'opendota-hero-items',
    'opendota-hero-matches',
    'opendota-hero-matchups',
    'opendota-hero-stats',
    'opendota-heroes',
    'opendota-items',
    'opendota-league',
    'opendota-league-match-ids',
    'opendota-league-matches',
    'opendota-leagues',
    'opendota-live',
    'opendota-match',
    'opendota-patch-notes',
    'opendota-pro-matches',
    'opendota-pro-players',
    'opendota-public-matches',
    'opendota-rank-distribution',
    'opendota-records',
    'opendota-scenarios',
    'opendota-team',
    'opendota-team-heroes',
    'opendota-team-matches',
    'opendota-team-players',
    'opendota-teams',
]

class CrawloraClient:
    opendota: OpendotaGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-abilities'],
        params: OpendotaAbilitiesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaAbilitiesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-benchmarks'],
        params: OpendotaBenchmarksParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaBenchmarksResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-constants'],
        params: OpendotaConstantsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaConstantsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-find-matches'],
        params: OpendotaFindMatchesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaFindMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-hero-descriptions'],
        params: OpendotaHeroDescriptionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaHeroDescriptionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-hero-durations'],
        params: OpendotaHeroDurationsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaHeroDurationsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-hero-items'],
        params: OpendotaHeroItemsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaHeroItemsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-hero-matches'],
        params: OpendotaHeroMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaHeroMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-hero-matchups'],
        params: OpendotaHeroMatchupsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaHeroMatchupsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-hero-stats'],
        params: OpendotaHeroStatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaHeroStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-heroes'],
        params: OpendotaHeroesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaHeroesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-items'],
        params: OpendotaItemsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaItemsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-league'],
        params: OpendotaLeagueParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaLeagueResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-league-match-ids'],
        params: OpendotaLeagueMatchIdsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaLeagueMatchIdsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-league-matches'],
        params: OpendotaLeagueMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaLeagueMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-leagues'],
        params: OpendotaLeaguesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaLeaguesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-live'],
        params: OpendotaLiveParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaLiveResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-match'],
        params: OpendotaMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaMatchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-patch-notes'],
        params: OpendotaPatchNotesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaPatchNotesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-pro-matches'],
        params: OpendotaProMatchesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaProMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-pro-players'],
        params: OpendotaProPlayersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaProPlayersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-public-matches'],
        params: OpendotaPublicMatchesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaPublicMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-rank-distribution'],
        params: OpendotaRankDistributionParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaRankDistributionResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-records'],
        params: OpendotaRecordsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaRecordsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-scenarios'],
        params: OpendotaScenariosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaScenariosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-team'],
        params: OpendotaTeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaTeamResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-team-heroes'],
        params: OpendotaTeamHeroesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaTeamHeroesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-team-matches'],
        params: OpendotaTeamMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaTeamMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-team-players'],
        params: OpendotaTeamPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaTeamPlayersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['opendota-teams'],
        params: OpendotaTeamsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaTeamsResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-abilities'],
        params: OpendotaAbilitiesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaAbilitiesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-benchmarks'],
        params: OpendotaBenchmarksParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaBenchmarksResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-constants'],
        params: OpendotaConstantsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaConstantsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-find-matches'],
        params: OpendotaFindMatchesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaFindMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-hero-descriptions'],
        params: OpendotaHeroDescriptionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaHeroDescriptionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-hero-durations'],
        params: OpendotaHeroDurationsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaHeroDurationsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-hero-items'],
        params: OpendotaHeroItemsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaHeroItemsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-hero-matches'],
        params: OpendotaHeroMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaHeroMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-hero-matchups'],
        params: OpendotaHeroMatchupsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaHeroMatchupsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-hero-stats'],
        params: OpendotaHeroStatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaHeroStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-heroes'],
        params: OpendotaHeroesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaHeroesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-items'],
        params: OpendotaItemsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaItemsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-league'],
        params: OpendotaLeagueParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaLeagueResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-league-match-ids'],
        params: OpendotaLeagueMatchIdsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaLeagueMatchIdsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-league-matches'],
        params: OpendotaLeagueMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaLeagueMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-leagues'],
        params: OpendotaLeaguesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaLeaguesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-live'],
        params: OpendotaLiveParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaLiveResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-match'],
        params: OpendotaMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaMatchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-patch-notes'],
        params: OpendotaPatchNotesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaPatchNotesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-pro-matches'],
        params: OpendotaProMatchesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaProMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-pro-players'],
        params: OpendotaProPlayersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaProPlayersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-public-matches'],
        params: OpendotaPublicMatchesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaPublicMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-rank-distribution'],
        params: OpendotaRankDistributionParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaRankDistributionResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-records'],
        params: OpendotaRecordsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaRecordsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-scenarios'],
        params: OpendotaScenariosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaScenariosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-team'],
        params: OpendotaTeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaTeamResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-team-heroes'],
        params: OpendotaTeamHeroesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaTeamHeroesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-team-matches'],
        params: OpendotaTeamMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaTeamMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-team-players'],
        params: OpendotaTeamPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaTeamPlayersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['opendota-teams'],
        params: OpendotaTeamsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> OpendotaTeamsResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class OpenDotaClient(CrawloraClient):
    def __enter__(self) -> OpenDotaClient: ...
    @overload
    def abilities(self, **params: Unpack[OpendotaAbilitiesStreamParams]) -> BinaryIO: ...
    @overload
    def abilities(self, **params: Unpack[OpendotaAbilitiesTextResponseParams]) -> str: ...
    @overload
    def abilities(self, **params: Unpack[OpendotaAbilitiesDefaultParams]) -> OpendotaAbilitiesResponse: ...
    @overload
    def benchmarks(self, **params: Unpack[OpendotaBenchmarksStreamParams]) -> BinaryIO: ...
    @overload
    def benchmarks(self, **params: Unpack[OpendotaBenchmarksTextResponseParams]) -> str: ...
    @overload
    def benchmarks(self, **params: Unpack[OpendotaBenchmarksDefaultParams]) -> OpendotaBenchmarksResponse: ...
    @overload
    def constants(self, **params: Unpack[OpendotaConstantsStreamParams]) -> BinaryIO: ...
    @overload
    def constants(self, **params: Unpack[OpendotaConstantsTextResponseParams]) -> str: ...
    @overload
    def constants(self, **params: Unpack[OpendotaConstantsDefaultParams]) -> OpendotaConstantsResponse: ...
    @overload
    def find_matches(self, **params: Unpack[OpendotaFindMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def find_matches(self, **params: Unpack[OpendotaFindMatchesTextResponseParams]) -> str: ...
    @overload
    def find_matches(self, **params: Unpack[OpendotaFindMatchesDefaultParams]) -> OpendotaFindMatchesResponse: ...
    @overload
    def hero_descriptions(self, **params: Unpack[OpendotaHeroDescriptionsStreamParams]) -> BinaryIO: ...
    @overload
    def hero_descriptions(self, **params: Unpack[OpendotaHeroDescriptionsTextResponseParams]) -> str: ...
    @overload
    def hero_descriptions(self, **params: Unpack[OpendotaHeroDescriptionsDefaultParams]) -> OpendotaHeroDescriptionsResponse: ...
    @overload
    def hero_durations(self, **params: Unpack[OpendotaHeroDurationsStreamParams]) -> BinaryIO: ...
    @overload
    def hero_durations(self, **params: Unpack[OpendotaHeroDurationsTextResponseParams]) -> str: ...
    @overload
    def hero_durations(self, **params: Unpack[OpendotaHeroDurationsDefaultParams]) -> OpendotaHeroDurationsResponse: ...
    @overload
    def hero_items(self, **params: Unpack[OpendotaHeroItemsStreamParams]) -> BinaryIO: ...
    @overload
    def hero_items(self, **params: Unpack[OpendotaHeroItemsTextResponseParams]) -> str: ...
    @overload
    def hero_items(self, **params: Unpack[OpendotaHeroItemsDefaultParams]) -> OpendotaHeroItemsResponse: ...
    @overload
    def hero_matches(self, **params: Unpack[OpendotaHeroMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def hero_matches(self, **params: Unpack[OpendotaHeroMatchesTextResponseParams]) -> str: ...
    @overload
    def hero_matches(self, **params: Unpack[OpendotaHeroMatchesDefaultParams]) -> OpendotaHeroMatchesResponse: ...
    @overload
    def hero_matchups(self, **params: Unpack[OpendotaHeroMatchupsStreamParams]) -> BinaryIO: ...
    @overload
    def hero_matchups(self, **params: Unpack[OpendotaHeroMatchupsTextResponseParams]) -> str: ...
    @overload
    def hero_matchups(self, **params: Unpack[OpendotaHeroMatchupsDefaultParams]) -> OpendotaHeroMatchupsResponse: ...
    @overload
    def hero_stats(self, **params: Unpack[OpendotaHeroStatsStreamParams]) -> BinaryIO: ...
    @overload
    def hero_stats(self, **params: Unpack[OpendotaHeroStatsTextResponseParams]) -> str: ...
    @overload
    def hero_stats(self, **params: Unpack[OpendotaHeroStatsDefaultParams]) -> OpendotaHeroStatsResponse: ...
    @overload
    def heroes(self, **params: Unpack[OpendotaHeroesStreamParams]) -> BinaryIO: ...
    @overload
    def heroes(self, **params: Unpack[OpendotaHeroesTextResponseParams]) -> str: ...
    @overload
    def heroes(self, **params: Unpack[OpendotaHeroesDefaultParams]) -> OpendotaHeroesResponse: ...
    @overload
    def items(self, **params: Unpack[OpendotaItemsStreamParams]) -> BinaryIO: ...
    @overload
    def items(self, **params: Unpack[OpendotaItemsTextResponseParams]) -> str: ...
    @overload
    def items(self, **params: Unpack[OpendotaItemsDefaultParams]) -> OpendotaItemsResponse: ...
    @overload
    def league(self, **params: Unpack[OpendotaLeagueStreamParams]) -> BinaryIO: ...
    @overload
    def league(self, **params: Unpack[OpendotaLeagueTextResponseParams]) -> str: ...
    @overload
    def league(self, **params: Unpack[OpendotaLeagueDefaultParams]) -> OpendotaLeagueResponse: ...
    @overload
    def league_match_ids(self, **params: Unpack[OpendotaLeagueMatchIdsStreamParams]) -> BinaryIO: ...
    @overload
    def league_match_ids(self, **params: Unpack[OpendotaLeagueMatchIdsTextResponseParams]) -> str: ...
    @overload
    def league_match_ids(self, **params: Unpack[OpendotaLeagueMatchIdsDefaultParams]) -> OpendotaLeagueMatchIdsResponse: ...
    @overload
    def league_matches(self, **params: Unpack[OpendotaLeagueMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def league_matches(self, **params: Unpack[OpendotaLeagueMatchesTextResponseParams]) -> str: ...
    @overload
    def league_matches(self, **params: Unpack[OpendotaLeagueMatchesDefaultParams]) -> OpendotaLeagueMatchesResponse: ...
    @overload
    def leagues(self, **params: Unpack[OpendotaLeaguesStreamParams]) -> BinaryIO: ...
    @overload
    def leagues(self, **params: Unpack[OpendotaLeaguesTextResponseParams]) -> str: ...
    @overload
    def leagues(self, **params: Unpack[OpendotaLeaguesDefaultParams]) -> OpendotaLeaguesResponse: ...
    @overload
    def live(self, **params: Unpack[OpendotaLiveStreamParams]) -> BinaryIO: ...
    @overload
    def live(self, **params: Unpack[OpendotaLiveTextResponseParams]) -> str: ...
    @overload
    def live(self, **params: Unpack[OpendotaLiveDefaultParams]) -> OpendotaLiveResponse: ...
    @overload
    def match(self, **params: Unpack[OpendotaMatchStreamParams]) -> BinaryIO: ...
    @overload
    def match(self, **params: Unpack[OpendotaMatchTextResponseParams]) -> str: ...
    @overload
    def match(self, **params: Unpack[OpendotaMatchDefaultParams]) -> OpendotaMatchResponse: ...
    @overload
    def patch_notes(self, **params: Unpack[OpendotaPatchNotesStreamParams]) -> BinaryIO: ...
    @overload
    def patch_notes(self, **params: Unpack[OpendotaPatchNotesTextResponseParams]) -> str: ...
    @overload
    def patch_notes(self, **params: Unpack[OpendotaPatchNotesDefaultParams]) -> OpendotaPatchNotesResponse: ...
    @overload
    def pro_matches(self, **params: Unpack[OpendotaProMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def pro_matches(self, **params: Unpack[OpendotaProMatchesTextResponseParams]) -> str: ...
    @overload
    def pro_matches(self, **params: Unpack[OpendotaProMatchesDefaultParams]) -> OpendotaProMatchesResponse: ...
    @overload
    def pro_players(self, **params: Unpack[OpendotaProPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def pro_players(self, **params: Unpack[OpendotaProPlayersTextResponseParams]) -> str: ...
    @overload
    def pro_players(self, **params: Unpack[OpendotaProPlayersDefaultParams]) -> OpendotaProPlayersResponse: ...
    @overload
    def public_matches(self, **params: Unpack[OpendotaPublicMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def public_matches(self, **params: Unpack[OpendotaPublicMatchesTextResponseParams]) -> str: ...
    @overload
    def public_matches(self, **params: Unpack[OpendotaPublicMatchesDefaultParams]) -> OpendotaPublicMatchesResponse: ...
    @overload
    def rank_distribution(self, **params: Unpack[OpendotaRankDistributionStreamParams]) -> BinaryIO: ...
    @overload
    def rank_distribution(self, **params: Unpack[OpendotaRankDistributionTextResponseParams]) -> str: ...
    @overload
    def rank_distribution(self, **params: Unpack[OpendotaRankDistributionDefaultParams]) -> OpendotaRankDistributionResponse: ...
    @overload
    def records(self, **params: Unpack[OpendotaRecordsStreamParams]) -> BinaryIO: ...
    @overload
    def records(self, **params: Unpack[OpendotaRecordsTextResponseParams]) -> str: ...
    @overload
    def records(self, **params: Unpack[OpendotaRecordsDefaultParams]) -> OpendotaRecordsResponse: ...
    @overload
    def scenarios(self, **params: Unpack[OpendotaScenariosStreamParams]) -> BinaryIO: ...
    @overload
    def scenarios(self, **params: Unpack[OpendotaScenariosTextResponseParams]) -> str: ...
    @overload
    def scenarios(self, **params: Unpack[OpendotaScenariosDefaultParams]) -> OpendotaScenariosResponse: ...
    @overload
    def team(self, **params: Unpack[OpendotaTeamStreamParams]) -> BinaryIO: ...
    @overload
    def team(self, **params: Unpack[OpendotaTeamTextResponseParams]) -> str: ...
    @overload
    def team(self, **params: Unpack[OpendotaTeamDefaultParams]) -> OpendotaTeamResponse: ...
    @overload
    def team_heroes(self, **params: Unpack[OpendotaTeamHeroesStreamParams]) -> BinaryIO: ...
    @overload
    def team_heroes(self, **params: Unpack[OpendotaTeamHeroesTextResponseParams]) -> str: ...
    @overload
    def team_heroes(self, **params: Unpack[OpendotaTeamHeroesDefaultParams]) -> OpendotaTeamHeroesResponse: ...
    @overload
    def team_matches(self, **params: Unpack[OpendotaTeamMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def team_matches(self, **params: Unpack[OpendotaTeamMatchesTextResponseParams]) -> str: ...
    @overload
    def team_matches(self, **params: Unpack[OpendotaTeamMatchesDefaultParams]) -> OpendotaTeamMatchesResponse: ...
    @overload
    def team_players(self, **params: Unpack[OpendotaTeamPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def team_players(self, **params: Unpack[OpendotaTeamPlayersTextResponseParams]) -> str: ...
    @overload
    def team_players(self, **params: Unpack[OpendotaTeamPlayersDefaultParams]) -> OpendotaTeamPlayersResponse: ...
    @overload
    def teams(self, **params: Unpack[OpendotaTeamsStreamParams]) -> BinaryIO: ...
    @overload
    def teams(self, **params: Unpack[OpendotaTeamsTextResponseParams]) -> str: ...
    @overload
    def teams(self, **params: Unpack[OpendotaTeamsDefaultParams]) -> OpendotaTeamsResponse: ...

class AsyncOpenDotaClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncOpenDotaClient: ...
    opendota: _AsyncOpendotaGroup
    @overload
    async def abilities(self, **params: Unpack[OpendotaAbilitiesStreamParams]) -> BinaryIO: ...
    @overload
    async def abilities(self, **params: Unpack[OpendotaAbilitiesTextResponseParams]) -> str: ...
    @overload
    async def abilities(self, **params: Unpack[OpendotaAbilitiesDefaultParams]) -> OpendotaAbilitiesResponse: ...
    @overload
    async def benchmarks(self, **params: Unpack[OpendotaBenchmarksStreamParams]) -> BinaryIO: ...
    @overload
    async def benchmarks(self, **params: Unpack[OpendotaBenchmarksTextResponseParams]) -> str: ...
    @overload
    async def benchmarks(self, **params: Unpack[OpendotaBenchmarksDefaultParams]) -> OpendotaBenchmarksResponse: ...
    @overload
    async def constants(self, **params: Unpack[OpendotaConstantsStreamParams]) -> BinaryIO: ...
    @overload
    async def constants(self, **params: Unpack[OpendotaConstantsTextResponseParams]) -> str: ...
    @overload
    async def constants(self, **params: Unpack[OpendotaConstantsDefaultParams]) -> OpendotaConstantsResponse: ...
    @overload
    async def find_matches(self, **params: Unpack[OpendotaFindMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def find_matches(self, **params: Unpack[OpendotaFindMatchesTextResponseParams]) -> str: ...
    @overload
    async def find_matches(self, **params: Unpack[OpendotaFindMatchesDefaultParams]) -> OpendotaFindMatchesResponse: ...
    @overload
    async def hero_descriptions(self, **params: Unpack[OpendotaHeroDescriptionsStreamParams]) -> BinaryIO: ...
    @overload
    async def hero_descriptions(self, **params: Unpack[OpendotaHeroDescriptionsTextResponseParams]) -> str: ...
    @overload
    async def hero_descriptions(self, **params: Unpack[OpendotaHeroDescriptionsDefaultParams]) -> OpendotaHeroDescriptionsResponse: ...
    @overload
    async def hero_durations(self, **params: Unpack[OpendotaHeroDurationsStreamParams]) -> BinaryIO: ...
    @overload
    async def hero_durations(self, **params: Unpack[OpendotaHeroDurationsTextResponseParams]) -> str: ...
    @overload
    async def hero_durations(self, **params: Unpack[OpendotaHeroDurationsDefaultParams]) -> OpendotaHeroDurationsResponse: ...
    @overload
    async def hero_items(self, **params: Unpack[OpendotaHeroItemsStreamParams]) -> BinaryIO: ...
    @overload
    async def hero_items(self, **params: Unpack[OpendotaHeroItemsTextResponseParams]) -> str: ...
    @overload
    async def hero_items(self, **params: Unpack[OpendotaHeroItemsDefaultParams]) -> OpendotaHeroItemsResponse: ...
    @overload
    async def hero_matches(self, **params: Unpack[OpendotaHeroMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def hero_matches(self, **params: Unpack[OpendotaHeroMatchesTextResponseParams]) -> str: ...
    @overload
    async def hero_matches(self, **params: Unpack[OpendotaHeroMatchesDefaultParams]) -> OpendotaHeroMatchesResponse: ...
    @overload
    async def hero_matchups(self, **params: Unpack[OpendotaHeroMatchupsStreamParams]) -> BinaryIO: ...
    @overload
    async def hero_matchups(self, **params: Unpack[OpendotaHeroMatchupsTextResponseParams]) -> str: ...
    @overload
    async def hero_matchups(self, **params: Unpack[OpendotaHeroMatchupsDefaultParams]) -> OpendotaHeroMatchupsResponse: ...
    @overload
    async def hero_stats(self, **params: Unpack[OpendotaHeroStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def hero_stats(self, **params: Unpack[OpendotaHeroStatsTextResponseParams]) -> str: ...
    @overload
    async def hero_stats(self, **params: Unpack[OpendotaHeroStatsDefaultParams]) -> OpendotaHeroStatsResponse: ...
    @overload
    async def heroes(self, **params: Unpack[OpendotaHeroesStreamParams]) -> BinaryIO: ...
    @overload
    async def heroes(self, **params: Unpack[OpendotaHeroesTextResponseParams]) -> str: ...
    @overload
    async def heroes(self, **params: Unpack[OpendotaHeroesDefaultParams]) -> OpendotaHeroesResponse: ...
    @overload
    async def items(self, **params: Unpack[OpendotaItemsStreamParams]) -> BinaryIO: ...
    @overload
    async def items(self, **params: Unpack[OpendotaItemsTextResponseParams]) -> str: ...
    @overload
    async def items(self, **params: Unpack[OpendotaItemsDefaultParams]) -> OpendotaItemsResponse: ...
    @overload
    async def league(self, **params: Unpack[OpendotaLeagueStreamParams]) -> BinaryIO: ...
    @overload
    async def league(self, **params: Unpack[OpendotaLeagueTextResponseParams]) -> str: ...
    @overload
    async def league(self, **params: Unpack[OpendotaLeagueDefaultParams]) -> OpendotaLeagueResponse: ...
    @overload
    async def league_match_ids(self, **params: Unpack[OpendotaLeagueMatchIdsStreamParams]) -> BinaryIO: ...
    @overload
    async def league_match_ids(self, **params: Unpack[OpendotaLeagueMatchIdsTextResponseParams]) -> str: ...
    @overload
    async def league_match_ids(self, **params: Unpack[OpendotaLeagueMatchIdsDefaultParams]) -> OpendotaLeagueMatchIdsResponse: ...
    @overload
    async def league_matches(self, **params: Unpack[OpendotaLeagueMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def league_matches(self, **params: Unpack[OpendotaLeagueMatchesTextResponseParams]) -> str: ...
    @overload
    async def league_matches(self, **params: Unpack[OpendotaLeagueMatchesDefaultParams]) -> OpendotaLeagueMatchesResponse: ...
    @overload
    async def leagues(self, **params: Unpack[OpendotaLeaguesStreamParams]) -> BinaryIO: ...
    @overload
    async def leagues(self, **params: Unpack[OpendotaLeaguesTextResponseParams]) -> str: ...
    @overload
    async def leagues(self, **params: Unpack[OpendotaLeaguesDefaultParams]) -> OpendotaLeaguesResponse: ...
    @overload
    async def live(self, **params: Unpack[OpendotaLiveStreamParams]) -> BinaryIO: ...
    @overload
    async def live(self, **params: Unpack[OpendotaLiveTextResponseParams]) -> str: ...
    @overload
    async def live(self, **params: Unpack[OpendotaLiveDefaultParams]) -> OpendotaLiveResponse: ...
    @overload
    async def match(self, **params: Unpack[OpendotaMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def match(self, **params: Unpack[OpendotaMatchTextResponseParams]) -> str: ...
    @overload
    async def match(self, **params: Unpack[OpendotaMatchDefaultParams]) -> OpendotaMatchResponse: ...
    @overload
    async def patch_notes(self, **params: Unpack[OpendotaPatchNotesStreamParams]) -> BinaryIO: ...
    @overload
    async def patch_notes(self, **params: Unpack[OpendotaPatchNotesTextResponseParams]) -> str: ...
    @overload
    async def patch_notes(self, **params: Unpack[OpendotaPatchNotesDefaultParams]) -> OpendotaPatchNotesResponse: ...
    @overload
    async def pro_matches(self, **params: Unpack[OpendotaProMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def pro_matches(self, **params: Unpack[OpendotaProMatchesTextResponseParams]) -> str: ...
    @overload
    async def pro_matches(self, **params: Unpack[OpendotaProMatchesDefaultParams]) -> OpendotaProMatchesResponse: ...
    @overload
    async def pro_players(self, **params: Unpack[OpendotaProPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def pro_players(self, **params: Unpack[OpendotaProPlayersTextResponseParams]) -> str: ...
    @overload
    async def pro_players(self, **params: Unpack[OpendotaProPlayersDefaultParams]) -> OpendotaProPlayersResponse: ...
    @overload
    async def public_matches(self, **params: Unpack[OpendotaPublicMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def public_matches(self, **params: Unpack[OpendotaPublicMatchesTextResponseParams]) -> str: ...
    @overload
    async def public_matches(self, **params: Unpack[OpendotaPublicMatchesDefaultParams]) -> OpendotaPublicMatchesResponse: ...
    @overload
    async def rank_distribution(self, **params: Unpack[OpendotaRankDistributionStreamParams]) -> BinaryIO: ...
    @overload
    async def rank_distribution(self, **params: Unpack[OpendotaRankDistributionTextResponseParams]) -> str: ...
    @overload
    async def rank_distribution(self, **params: Unpack[OpendotaRankDistributionDefaultParams]) -> OpendotaRankDistributionResponse: ...
    @overload
    async def records(self, **params: Unpack[OpendotaRecordsStreamParams]) -> BinaryIO: ...
    @overload
    async def records(self, **params: Unpack[OpendotaRecordsTextResponseParams]) -> str: ...
    @overload
    async def records(self, **params: Unpack[OpendotaRecordsDefaultParams]) -> OpendotaRecordsResponse: ...
    @overload
    async def scenarios(self, **params: Unpack[OpendotaScenariosStreamParams]) -> BinaryIO: ...
    @overload
    async def scenarios(self, **params: Unpack[OpendotaScenariosTextResponseParams]) -> str: ...
    @overload
    async def scenarios(self, **params: Unpack[OpendotaScenariosDefaultParams]) -> OpendotaScenariosResponse: ...
    @overload
    async def team(self, **params: Unpack[OpendotaTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[OpendotaTeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[OpendotaTeamDefaultParams]) -> OpendotaTeamResponse: ...
    @overload
    async def team_heroes(self, **params: Unpack[OpendotaTeamHeroesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_heroes(self, **params: Unpack[OpendotaTeamHeroesTextResponseParams]) -> str: ...
    @overload
    async def team_heroes(self, **params: Unpack[OpendotaTeamHeroesDefaultParams]) -> OpendotaTeamHeroesResponse: ...
    @overload
    async def team_matches(self, **params: Unpack[OpendotaTeamMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_matches(self, **params: Unpack[OpendotaTeamMatchesTextResponseParams]) -> str: ...
    @overload
    async def team_matches(self, **params: Unpack[OpendotaTeamMatchesDefaultParams]) -> OpendotaTeamMatchesResponse: ...
    @overload
    async def team_players(self, **params: Unpack[OpendotaTeamPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def team_players(self, **params: Unpack[OpendotaTeamPlayersTextResponseParams]) -> str: ...
    @overload
    async def team_players(self, **params: Unpack[OpendotaTeamPlayersDefaultParams]) -> OpendotaTeamPlayersResponse: ...
    @overload
    async def teams(self, **params: Unpack[OpendotaTeamsStreamParams]) -> BinaryIO: ...
    @overload
    async def teams(self, **params: Unpack[OpendotaTeamsTextResponseParams]) -> str: ...
    @overload
    async def teams(self, **params: Unpack[OpendotaTeamsDefaultParams]) -> OpendotaTeamsResponse: ...

class _AsyncOpendotaGroup:
    @overload
    async def abilities(self, **params: Unpack[OpendotaAbilitiesStreamParams]) -> BinaryIO: ...
    @overload
    async def abilities(self, **params: Unpack[OpendotaAbilitiesTextResponseParams]) -> str: ...
    @overload
    async def abilities(self, **params: Unpack[OpendotaAbilitiesDefaultParams]) -> OpendotaAbilitiesResponse: ...
    @overload
    async def benchmarks(self, **params: Unpack[OpendotaBenchmarksStreamParams]) -> BinaryIO: ...
    @overload
    async def benchmarks(self, **params: Unpack[OpendotaBenchmarksTextResponseParams]) -> str: ...
    @overload
    async def benchmarks(self, **params: Unpack[OpendotaBenchmarksDefaultParams]) -> OpendotaBenchmarksResponse: ...
    @overload
    async def constants(self, **params: Unpack[OpendotaConstantsStreamParams]) -> BinaryIO: ...
    @overload
    async def constants(self, **params: Unpack[OpendotaConstantsTextResponseParams]) -> str: ...
    @overload
    async def constants(self, **params: Unpack[OpendotaConstantsDefaultParams]) -> OpendotaConstantsResponse: ...
    @overload
    async def find_matches(self, **params: Unpack[OpendotaFindMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def find_matches(self, **params: Unpack[OpendotaFindMatchesTextResponseParams]) -> str: ...
    @overload
    async def find_matches(self, **params: Unpack[OpendotaFindMatchesDefaultParams]) -> OpendotaFindMatchesResponse: ...
    @overload
    async def hero_descriptions(self, **params: Unpack[OpendotaHeroDescriptionsStreamParams]) -> BinaryIO: ...
    @overload
    async def hero_descriptions(self, **params: Unpack[OpendotaHeroDescriptionsTextResponseParams]) -> str: ...
    @overload
    async def hero_descriptions(self, **params: Unpack[OpendotaHeroDescriptionsDefaultParams]) -> OpendotaHeroDescriptionsResponse: ...
    @overload
    async def hero_durations(self, **params: Unpack[OpendotaHeroDurationsStreamParams]) -> BinaryIO: ...
    @overload
    async def hero_durations(self, **params: Unpack[OpendotaHeroDurationsTextResponseParams]) -> str: ...
    @overload
    async def hero_durations(self, **params: Unpack[OpendotaHeroDurationsDefaultParams]) -> OpendotaHeroDurationsResponse: ...
    @overload
    async def hero_items(self, **params: Unpack[OpendotaHeroItemsStreamParams]) -> BinaryIO: ...
    @overload
    async def hero_items(self, **params: Unpack[OpendotaHeroItemsTextResponseParams]) -> str: ...
    @overload
    async def hero_items(self, **params: Unpack[OpendotaHeroItemsDefaultParams]) -> OpendotaHeroItemsResponse: ...
    @overload
    async def hero_matches(self, **params: Unpack[OpendotaHeroMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def hero_matches(self, **params: Unpack[OpendotaHeroMatchesTextResponseParams]) -> str: ...
    @overload
    async def hero_matches(self, **params: Unpack[OpendotaHeroMatchesDefaultParams]) -> OpendotaHeroMatchesResponse: ...
    @overload
    async def hero_matchups(self, **params: Unpack[OpendotaHeroMatchupsStreamParams]) -> BinaryIO: ...
    @overload
    async def hero_matchups(self, **params: Unpack[OpendotaHeroMatchupsTextResponseParams]) -> str: ...
    @overload
    async def hero_matchups(self, **params: Unpack[OpendotaHeroMatchupsDefaultParams]) -> OpendotaHeroMatchupsResponse: ...
    @overload
    async def hero_stats(self, **params: Unpack[OpendotaHeroStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def hero_stats(self, **params: Unpack[OpendotaHeroStatsTextResponseParams]) -> str: ...
    @overload
    async def hero_stats(self, **params: Unpack[OpendotaHeroStatsDefaultParams]) -> OpendotaHeroStatsResponse: ...
    @overload
    async def heroes(self, **params: Unpack[OpendotaHeroesStreamParams]) -> BinaryIO: ...
    @overload
    async def heroes(self, **params: Unpack[OpendotaHeroesTextResponseParams]) -> str: ...
    @overload
    async def heroes(self, **params: Unpack[OpendotaHeroesDefaultParams]) -> OpendotaHeroesResponse: ...
    @overload
    async def items(self, **params: Unpack[OpendotaItemsStreamParams]) -> BinaryIO: ...
    @overload
    async def items(self, **params: Unpack[OpendotaItemsTextResponseParams]) -> str: ...
    @overload
    async def items(self, **params: Unpack[OpendotaItemsDefaultParams]) -> OpendotaItemsResponse: ...
    @overload
    async def league(self, **params: Unpack[OpendotaLeagueStreamParams]) -> BinaryIO: ...
    @overload
    async def league(self, **params: Unpack[OpendotaLeagueTextResponseParams]) -> str: ...
    @overload
    async def league(self, **params: Unpack[OpendotaLeagueDefaultParams]) -> OpendotaLeagueResponse: ...
    @overload
    async def league_match_ids(self, **params: Unpack[OpendotaLeagueMatchIdsStreamParams]) -> BinaryIO: ...
    @overload
    async def league_match_ids(self, **params: Unpack[OpendotaLeagueMatchIdsTextResponseParams]) -> str: ...
    @overload
    async def league_match_ids(self, **params: Unpack[OpendotaLeagueMatchIdsDefaultParams]) -> OpendotaLeagueMatchIdsResponse: ...
    @overload
    async def league_matches(self, **params: Unpack[OpendotaLeagueMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def league_matches(self, **params: Unpack[OpendotaLeagueMatchesTextResponseParams]) -> str: ...
    @overload
    async def league_matches(self, **params: Unpack[OpendotaLeagueMatchesDefaultParams]) -> OpendotaLeagueMatchesResponse: ...
    @overload
    async def leagues(self, **params: Unpack[OpendotaLeaguesStreamParams]) -> BinaryIO: ...
    @overload
    async def leagues(self, **params: Unpack[OpendotaLeaguesTextResponseParams]) -> str: ...
    @overload
    async def leagues(self, **params: Unpack[OpendotaLeaguesDefaultParams]) -> OpendotaLeaguesResponse: ...
    @overload
    async def live(self, **params: Unpack[OpendotaLiveStreamParams]) -> BinaryIO: ...
    @overload
    async def live(self, **params: Unpack[OpendotaLiveTextResponseParams]) -> str: ...
    @overload
    async def live(self, **params: Unpack[OpendotaLiveDefaultParams]) -> OpendotaLiveResponse: ...
    @overload
    async def match(self, **params: Unpack[OpendotaMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def match(self, **params: Unpack[OpendotaMatchTextResponseParams]) -> str: ...
    @overload
    async def match(self, **params: Unpack[OpendotaMatchDefaultParams]) -> OpendotaMatchResponse: ...
    @overload
    async def patch_notes(self, **params: Unpack[OpendotaPatchNotesStreamParams]) -> BinaryIO: ...
    @overload
    async def patch_notes(self, **params: Unpack[OpendotaPatchNotesTextResponseParams]) -> str: ...
    @overload
    async def patch_notes(self, **params: Unpack[OpendotaPatchNotesDefaultParams]) -> OpendotaPatchNotesResponse: ...
    @overload
    async def pro_matches(self, **params: Unpack[OpendotaProMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def pro_matches(self, **params: Unpack[OpendotaProMatchesTextResponseParams]) -> str: ...
    @overload
    async def pro_matches(self, **params: Unpack[OpendotaProMatchesDefaultParams]) -> OpendotaProMatchesResponse: ...
    @overload
    async def pro_players(self, **params: Unpack[OpendotaProPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def pro_players(self, **params: Unpack[OpendotaProPlayersTextResponseParams]) -> str: ...
    @overload
    async def pro_players(self, **params: Unpack[OpendotaProPlayersDefaultParams]) -> OpendotaProPlayersResponse: ...
    @overload
    async def public_matches(self, **params: Unpack[OpendotaPublicMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def public_matches(self, **params: Unpack[OpendotaPublicMatchesTextResponseParams]) -> str: ...
    @overload
    async def public_matches(self, **params: Unpack[OpendotaPublicMatchesDefaultParams]) -> OpendotaPublicMatchesResponse: ...
    @overload
    async def rank_distribution(self, **params: Unpack[OpendotaRankDistributionStreamParams]) -> BinaryIO: ...
    @overload
    async def rank_distribution(self, **params: Unpack[OpendotaRankDistributionTextResponseParams]) -> str: ...
    @overload
    async def rank_distribution(self, **params: Unpack[OpendotaRankDistributionDefaultParams]) -> OpendotaRankDistributionResponse: ...
    @overload
    async def records(self, **params: Unpack[OpendotaRecordsStreamParams]) -> BinaryIO: ...
    @overload
    async def records(self, **params: Unpack[OpendotaRecordsTextResponseParams]) -> str: ...
    @overload
    async def records(self, **params: Unpack[OpendotaRecordsDefaultParams]) -> OpendotaRecordsResponse: ...
    @overload
    async def scenarios(self, **params: Unpack[OpendotaScenariosStreamParams]) -> BinaryIO: ...
    @overload
    async def scenarios(self, **params: Unpack[OpendotaScenariosTextResponseParams]) -> str: ...
    @overload
    async def scenarios(self, **params: Unpack[OpendotaScenariosDefaultParams]) -> OpendotaScenariosResponse: ...
    @overload
    async def team(self, **params: Unpack[OpendotaTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[OpendotaTeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[OpendotaTeamDefaultParams]) -> OpendotaTeamResponse: ...
    @overload
    async def team_heroes(self, **params: Unpack[OpendotaTeamHeroesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_heroes(self, **params: Unpack[OpendotaTeamHeroesTextResponseParams]) -> str: ...
    @overload
    async def team_heroes(self, **params: Unpack[OpendotaTeamHeroesDefaultParams]) -> OpendotaTeamHeroesResponse: ...
    @overload
    async def team_matches(self, **params: Unpack[OpendotaTeamMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_matches(self, **params: Unpack[OpendotaTeamMatchesTextResponseParams]) -> str: ...
    @overload
    async def team_matches(self, **params: Unpack[OpendotaTeamMatchesDefaultParams]) -> OpendotaTeamMatchesResponse: ...
    @overload
    async def team_players(self, **params: Unpack[OpendotaTeamPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def team_players(self, **params: Unpack[OpendotaTeamPlayersTextResponseParams]) -> str: ...
    @overload
    async def team_players(self, **params: Unpack[OpendotaTeamPlayersDefaultParams]) -> OpendotaTeamPlayersResponse: ...
    @overload
    async def teams(self, **params: Unpack[OpendotaTeamsStreamParams]) -> BinaryIO: ...
    @overload
    async def teams(self, **params: Unpack[OpendotaTeamsTextResponseParams]) -> str: ...
    @overload
    async def teams(self, **params: Unpack[OpendotaTeamsDefaultParams]) -> OpendotaTeamsResponse: ...

OpendotaAbilitiesDefaultParams = TypedDict('OpendotaAbilitiesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

OpendotaAbilitiesTextResponseParams = TypedDict('OpendotaAbilitiesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

OpendotaAbilitiesStreamParams = TypedDict('OpendotaAbilitiesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

OpendotaBenchmarksDefaultParams = TypedDict('OpendotaBenchmarksDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'hero_id': Required[int],
    'bracket': NotRequired[int],
    'role': NotRequired[Literal['core', 'support']],
}, total=False)

OpendotaBenchmarksTextResponseParams = TypedDict('OpendotaBenchmarksTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'hero_id': Required[int],
    'bracket': NotRequired[int],
    'role': NotRequired[Literal['core', 'support']],
}, total=False)

OpendotaBenchmarksStreamParams = TypedDict('OpendotaBenchmarksStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'hero_id': Required[int],
    'bracket': NotRequired[int],
    'role': NotRequired[Literal['core', 'support']],
}, total=False)

OpendotaConstantsDefaultParams = TypedDict('OpendotaConstantsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'resource': Required[Literal['game_mode', 'lobby_type', 'patch', 'region', 'cluster', 'item_ids', 'ability_ids', 'permanent_buffs', 'xp_level', 'countries', 'order_types', 'player_colors', 'chat_wheel', 'item_colors', 'ancients', 'skillshots']],
}, total=False)

OpendotaConstantsTextResponseParams = TypedDict('OpendotaConstantsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'resource': Required[Literal['game_mode', 'lobby_type', 'patch', 'region', 'cluster', 'item_ids', 'ability_ids', 'permanent_buffs', 'xp_level', 'countries', 'order_types', 'player_colors', 'chat_wheel', 'item_colors', 'ancients', 'skillshots']],
}, total=False)

OpendotaConstantsStreamParams = TypedDict('OpendotaConstantsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'resource': Required[Literal['game_mode', 'lobby_type', 'patch', 'region', 'cluster', 'item_ids', 'ability_ids', 'permanent_buffs', 'xp_level', 'countries', 'order_types', 'player_colors', 'chat_wheel', 'item_colors', 'ancients', 'skillshots']],
}, total=False)

OpendotaFindMatchesDefaultParams = TypedDict('OpendotaFindMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_a': NotRequired[str],
    'team_b': NotRequired[str],
}, total=False)

OpendotaFindMatchesTextResponseParams = TypedDict('OpendotaFindMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_a': NotRequired[str],
    'team_b': NotRequired[str],
}, total=False)

OpendotaFindMatchesStreamParams = TypedDict('OpendotaFindMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_a': NotRequired[str],
    'team_b': NotRequired[str],
}, total=False)

OpendotaHeroDescriptionsDefaultParams = TypedDict('OpendotaHeroDescriptionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'hero_id': NotRequired[int],
    'include_lore': NotRequired[bool],
}, total=False)

OpendotaHeroDescriptionsTextResponseParams = TypedDict('OpendotaHeroDescriptionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'hero_id': NotRequired[int],
    'include_lore': NotRequired[bool],
}, total=False)

OpendotaHeroDescriptionsStreamParams = TypedDict('OpendotaHeroDescriptionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'hero_id': NotRequired[int],
    'include_lore': NotRequired[bool],
}, total=False)

OpendotaHeroDurationsDefaultParams = TypedDict('OpendotaHeroDurationsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'hero_id': Required[int],
}, total=False)

OpendotaHeroDurationsTextResponseParams = TypedDict('OpendotaHeroDurationsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'hero_id': Required[int],
}, total=False)

OpendotaHeroDurationsStreamParams = TypedDict('OpendotaHeroDurationsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'hero_id': Required[int],
}, total=False)

OpendotaHeroItemsDefaultParams = TypedDict('OpendotaHeroItemsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'hero_id': Required[int],
}, total=False)

OpendotaHeroItemsTextResponseParams = TypedDict('OpendotaHeroItemsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'hero_id': Required[int],
}, total=False)

OpendotaHeroItemsStreamParams = TypedDict('OpendotaHeroItemsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'hero_id': Required[int],
}, total=False)

OpendotaHeroMatchesDefaultParams = TypedDict('OpendotaHeroMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'hero_id': Required[int],
}, total=False)

OpendotaHeroMatchesTextResponseParams = TypedDict('OpendotaHeroMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'hero_id': Required[int],
}, total=False)

OpendotaHeroMatchesStreamParams = TypedDict('OpendotaHeroMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'hero_id': Required[int],
}, total=False)

OpendotaHeroMatchupsDefaultParams = TypedDict('OpendotaHeroMatchupsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'hero_id': Required[int],
}, total=False)

OpendotaHeroMatchupsTextResponseParams = TypedDict('OpendotaHeroMatchupsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'hero_id': Required[int],
}, total=False)

OpendotaHeroMatchupsStreamParams = TypedDict('OpendotaHeroMatchupsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'hero_id': Required[int],
}, total=False)

OpendotaHeroStatsDefaultParams = TypedDict('OpendotaHeroStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'primary_attr': NotRequired[Literal['agi', 'all', 'int', 'str']],
    'attack_type': NotRequired[Literal['Melee', 'Ranged']],
    'role': NotRequired[Literal['Carry', 'Disabler', 'Durable', 'Escape', 'Initiator', 'Nuker', 'Pusher', 'Support']],
    'sort': NotRequired[Literal['id', 'name', 'pro_pick', 'pro_win', 'pro_ban', 'pro_win_rate', 'pub_pick', 'pub_win', 'pub_win_rate', 'turbo_pick', 'turbo_win_rate']],
    'desc': NotRequired[bool],
    'limit': NotRequired[int],
}, total=False)

OpendotaHeroStatsTextResponseParams = TypedDict('OpendotaHeroStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'primary_attr': NotRequired[Literal['agi', 'all', 'int', 'str']],
    'attack_type': NotRequired[Literal['Melee', 'Ranged']],
    'role': NotRequired[Literal['Carry', 'Disabler', 'Durable', 'Escape', 'Initiator', 'Nuker', 'Pusher', 'Support']],
    'sort': NotRequired[Literal['id', 'name', 'pro_pick', 'pro_win', 'pro_ban', 'pro_win_rate', 'pub_pick', 'pub_win', 'pub_win_rate', 'turbo_pick', 'turbo_win_rate']],
    'desc': NotRequired[bool],
    'limit': NotRequired[int],
}, total=False)

OpendotaHeroStatsStreamParams = TypedDict('OpendotaHeroStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'primary_attr': NotRequired[Literal['agi', 'all', 'int', 'str']],
    'attack_type': NotRequired[Literal['Melee', 'Ranged']],
    'role': NotRequired[Literal['Carry', 'Disabler', 'Durable', 'Escape', 'Initiator', 'Nuker', 'Pusher', 'Support']],
    'sort': NotRequired[Literal['id', 'name', 'pro_pick', 'pro_win', 'pro_ban', 'pro_win_rate', 'pub_pick', 'pub_win', 'pub_win_rate', 'turbo_pick', 'turbo_win_rate']],
    'desc': NotRequired[bool],
    'limit': NotRequired[int],
}, total=False)

OpendotaHeroesDefaultParams = TypedDict('OpendotaHeroesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

OpendotaHeroesTextResponseParams = TypedDict('OpendotaHeroesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

OpendotaHeroesStreamParams = TypedDict('OpendotaHeroesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

OpendotaItemsDefaultParams = TypedDict('OpendotaItemsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': NotRequired[str],
    'quality': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

OpendotaItemsTextResponseParams = TypedDict('OpendotaItemsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': NotRequired[str],
    'quality': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

OpendotaItemsStreamParams = TypedDict('OpendotaItemsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': NotRequired[str],
    'quality': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

OpendotaLeagueDefaultParams = TypedDict('OpendotaLeagueDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': Required[int],
}, total=False)

OpendotaLeagueTextResponseParams = TypedDict('OpendotaLeagueTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': Required[int],
}, total=False)

OpendotaLeagueStreamParams = TypedDict('OpendotaLeagueStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': Required[int],
}, total=False)

OpendotaLeagueMatchIdsDefaultParams = TypedDict('OpendotaLeagueMatchIdsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': Required[int],
}, total=False)

OpendotaLeagueMatchIdsTextResponseParams = TypedDict('OpendotaLeagueMatchIdsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': Required[int],
}, total=False)

OpendotaLeagueMatchIdsStreamParams = TypedDict('OpendotaLeagueMatchIdsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': Required[int],
}, total=False)

OpendotaLeagueMatchesDefaultParams = TypedDict('OpendotaLeagueMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league_id': Required[int],
    'team_id': NotRequired[int],
}, total=False)

OpendotaLeagueMatchesTextResponseParams = TypedDict('OpendotaLeagueMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league_id': Required[int],
    'team_id': NotRequired[int],
}, total=False)

OpendotaLeagueMatchesStreamParams = TypedDict('OpendotaLeagueMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league_id': Required[int],
    'team_id': NotRequired[int],
}, total=False)

OpendotaLeaguesDefaultParams = TypedDict('OpendotaLeaguesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'tier': NotRequired[Literal['amateur', 'excluded', 'premium', 'professional', 'unrated']],
}, total=False)

OpendotaLeaguesTextResponseParams = TypedDict('OpendotaLeaguesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'tier': NotRequired[Literal['amateur', 'excluded', 'premium', 'professional', 'unrated']],
}, total=False)

OpendotaLeaguesStreamParams = TypedDict('OpendotaLeaguesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'tier': NotRequired[Literal['amateur', 'excluded', 'premium', 'professional', 'unrated']],
}, total=False)

OpendotaLiveDefaultParams = TypedDict('OpendotaLiveDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

OpendotaLiveTextResponseParams = TypedDict('OpendotaLiveTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

OpendotaLiveStreamParams = TypedDict('OpendotaLiveStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

OpendotaMatchDefaultParams = TypedDict('OpendotaMatchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[int],
}, total=False)

OpendotaMatchTextResponseParams = TypedDict('OpendotaMatchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[int],
}, total=False)

OpendotaMatchStreamParams = TypedDict('OpendotaMatchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[int],
}, total=False)

OpendotaPatchNotesDefaultParams = TypedDict('OpendotaPatchNotesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'patch': NotRequired[str],
}, total=False)

OpendotaPatchNotesTextResponseParams = TypedDict('OpendotaPatchNotesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'patch': NotRequired[str],
}, total=False)

OpendotaPatchNotesStreamParams = TypedDict('OpendotaPatchNotesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'patch': NotRequired[str],
}, total=False)

OpendotaProMatchesDefaultParams = TypedDict('OpendotaProMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'less_than_match_id': NotRequired[int],
}, total=False)

OpendotaProMatchesTextResponseParams = TypedDict('OpendotaProMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'less_than_match_id': NotRequired[int],
}, total=False)

OpendotaProMatchesStreamParams = TypedDict('OpendotaProMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'less_than_match_id': NotRequired[int],
}, total=False)

OpendotaProPlayersDefaultParams = TypedDict('OpendotaProPlayersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': NotRequired[int],
    'q': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

OpendotaProPlayersTextResponseParams = TypedDict('OpendotaProPlayersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': NotRequired[int],
    'q': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

OpendotaProPlayersStreamParams = TypedDict('OpendotaProPlayersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': NotRequired[int],
    'q': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

OpendotaPublicMatchesDefaultParams = TypedDict('OpendotaPublicMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'min_rank': NotRequired[Literal['11', '12', '13', '14', '15', '21', '22', '23', '24', '25', '31', '32', '33', '34', '35', '41', '42', '43', '44', '45', '51', '52', '53', '54', '55', '61', '62', '63', '64', '65', '71', '72', '73', '74', '75', '81', '82', '83', '84', '85']],
    'max_rank': NotRequired[Literal['11', '12', '13', '14', '15', '21', '22', '23', '24', '25', '31', '32', '33', '34', '35', '41', '42', '43', '44', '45', '51', '52', '53', '54', '55', '61', '62', '63', '64', '65', '71', '72', '73', '74', '75', '81', '82', '83', '84', '85']],
    'less_than_match_id': NotRequired[int],
}, total=False)

OpendotaPublicMatchesTextResponseParams = TypedDict('OpendotaPublicMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'min_rank': NotRequired[Literal['11', '12', '13', '14', '15', '21', '22', '23', '24', '25', '31', '32', '33', '34', '35', '41', '42', '43', '44', '45', '51', '52', '53', '54', '55', '61', '62', '63', '64', '65', '71', '72', '73', '74', '75', '81', '82', '83', '84', '85']],
    'max_rank': NotRequired[Literal['11', '12', '13', '14', '15', '21', '22', '23', '24', '25', '31', '32', '33', '34', '35', '41', '42', '43', '44', '45', '51', '52', '53', '54', '55', '61', '62', '63', '64', '65', '71', '72', '73', '74', '75', '81', '82', '83', '84', '85']],
    'less_than_match_id': NotRequired[int],
}, total=False)

OpendotaPublicMatchesStreamParams = TypedDict('OpendotaPublicMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'min_rank': NotRequired[Literal['11', '12', '13', '14', '15', '21', '22', '23', '24', '25', '31', '32', '33', '34', '35', '41', '42', '43', '44', '45', '51', '52', '53', '54', '55', '61', '62', '63', '64', '65', '71', '72', '73', '74', '75', '81', '82', '83', '84', '85']],
    'max_rank': NotRequired[Literal['11', '12', '13', '14', '15', '21', '22', '23', '24', '25', '31', '32', '33', '34', '35', '41', '42', '43', '44', '45', '51', '52', '53', '54', '55', '61', '62', '63', '64', '65', '71', '72', '73', '74', '75', '81', '82', '83', '84', '85']],
    'less_than_match_id': NotRequired[int],
}, total=False)

OpendotaRankDistributionDefaultParams = TypedDict('OpendotaRankDistributionDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

OpendotaRankDistributionTextResponseParams = TypedDict('OpendotaRankDistributionTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

OpendotaRankDistributionStreamParams = TypedDict('OpendotaRankDistributionStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

OpendotaRecordsDefaultParams = TypedDict('OpendotaRecordsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'field': Required[Literal['kills', 'deaths', 'assists', 'last_hits', 'denies', 'gold_per_min', 'xp_per_min', 'hero_damage', 'tower_damage', 'hero_healing', 'duration']],
}, total=False)

OpendotaRecordsTextResponseParams = TypedDict('OpendotaRecordsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'field': Required[Literal['kills', 'deaths', 'assists', 'last_hits', 'denies', 'gold_per_min', 'xp_per_min', 'hero_damage', 'tower_damage', 'hero_healing', 'duration']],
}, total=False)

OpendotaRecordsStreamParams = TypedDict('OpendotaRecordsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'field': Required[Literal['kills', 'deaths', 'assists', 'last_hits', 'denies', 'gold_per_min', 'xp_per_min', 'hero_damage', 'tower_damage', 'hero_healing', 'duration']],
}, total=False)

OpendotaScenariosDefaultParams = TypedDict('OpendotaScenariosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'kind': Required[Literal['item-timings', 'lane-roles', 'misc']],
    'hero_id': NotRequired[int],
    'item': NotRequired[str],
    'lane_role': NotRequired[int],
    'scenario': NotRequired[Literal['courier_kill', 'first_blood', 'neg_chat_1min', 'pos_chat_1min']],
    'limit': NotRequired[int],
}, total=False)

OpendotaScenariosTextResponseParams = TypedDict('OpendotaScenariosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'kind': Required[Literal['item-timings', 'lane-roles', 'misc']],
    'hero_id': NotRequired[int],
    'item': NotRequired[str],
    'lane_role': NotRequired[int],
    'scenario': NotRequired[Literal['courier_kill', 'first_blood', 'neg_chat_1min', 'pos_chat_1min']],
    'limit': NotRequired[int],
}, total=False)

OpendotaScenariosStreamParams = TypedDict('OpendotaScenariosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'kind': Required[Literal['item-timings', 'lane-roles', 'misc']],
    'hero_id': NotRequired[int],
    'item': NotRequired[str],
    'lane_role': NotRequired[int],
    'scenario': NotRequired[Literal['courier_kill', 'first_blood', 'neg_chat_1min', 'pos_chat_1min']],
    'limit': NotRequired[int],
}, total=False)

OpendotaTeamDefaultParams = TypedDict('OpendotaTeamDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': Required[int],
}, total=False)

OpendotaTeamTextResponseParams = TypedDict('OpendotaTeamTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': Required[int],
}, total=False)

OpendotaTeamStreamParams = TypedDict('OpendotaTeamStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': Required[int],
}, total=False)

OpendotaTeamHeroesDefaultParams = TypedDict('OpendotaTeamHeroesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': Required[int],
}, total=False)

OpendotaTeamHeroesTextResponseParams = TypedDict('OpendotaTeamHeroesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': Required[int],
}, total=False)

OpendotaTeamHeroesStreamParams = TypedDict('OpendotaTeamHeroesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': Required[int],
}, total=False)

OpendotaTeamMatchesDefaultParams = TypedDict('OpendotaTeamMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': Required[int],
}, total=False)

OpendotaTeamMatchesTextResponseParams = TypedDict('OpendotaTeamMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': Required[int],
}, total=False)

OpendotaTeamMatchesStreamParams = TypedDict('OpendotaTeamMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': Required[int],
}, total=False)

OpendotaTeamPlayersDefaultParams = TypedDict('OpendotaTeamPlayersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': Required[int],
}, total=False)

OpendotaTeamPlayersTextResponseParams = TypedDict('OpendotaTeamPlayersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': Required[int],
}, total=False)

OpendotaTeamPlayersStreamParams = TypedDict('OpendotaTeamPlayersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': Required[int],
}, total=False)

OpendotaTeamsDefaultParams = TypedDict('OpendotaTeamsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'page': NotRequired[int],
}, total=False)

OpendotaTeamsTextResponseParams = TypedDict('OpendotaTeamsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'page': NotRequired[int],
}, total=False)

OpendotaTeamsStreamParams = TypedDict('OpendotaTeamsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'page': NotRequired[int],
}, total=False)
