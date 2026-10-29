import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class OpenDotaClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  abilities(params?: OperationParamsMap["opendota-abilities"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  benchmarks(params: OperationParamsMap["opendota-benchmarks"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  constants(params: OperationParamsMap["opendota-constants"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  findMatches(params?: OperationParamsMap["opendota-find-matches"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  heroDescriptions(params?: OperationParamsMap["opendota-hero-descriptions"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  heroDurations(params: OperationParamsMap["opendota-hero-durations"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  heroItems(params: OperationParamsMap["opendota-hero-items"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  heroMatches(params: OperationParamsMap["opendota-hero-matches"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  heroMatchups(params: OperationParamsMap["opendota-hero-matchups"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  heroStats(params?: OperationParamsMap["opendota-hero-stats"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  heroes(params?: OperationParamsMap["opendota-heroes"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  items(params?: OperationParamsMap["opendota-items"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  league(params: OperationParamsMap["opendota-league"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  leagueMatchIds(params: OperationParamsMap["opendota-league-match-ids"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  leagueMatches(params: OperationParamsMap["opendota-league-matches"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  leagues(params?: OperationParamsMap["opendota-leagues"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  live(params?: OperationParamsMap["opendota-live"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  match(params: OperationParamsMap["opendota-match"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  patchNotes(params?: OperationParamsMap["opendota-patch-notes"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  proMatches(params?: OperationParamsMap["opendota-pro-matches"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  proPlayers(params?: OperationParamsMap["opendota-pro-players"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  publicMatches(params?: OperationParamsMap["opendota-public-matches"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  rankDistribution(params?: OperationParamsMap["opendota-rank-distribution"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  records(params: OperationParamsMap["opendota-records"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  scenarios(params: OperationParamsMap["opendota-scenarios"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  team(params: OperationParamsMap["opendota-team"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamHeroes(params: OperationParamsMap["opendota-team-heroes"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamMatches(params: OperationParamsMap["opendota-team-matches"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamPlayers(params: OperationParamsMap["opendota-team-players"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teams(params?: OperationParamsMap["opendota-teams"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  abilities(params?: OperationParamsMap["opendota-abilities"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  benchmarks(params: OperationParamsMap["opendota-benchmarks"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  constants(params: OperationParamsMap["opendota-constants"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  findMatches(params?: OperationParamsMap["opendota-find-matches"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  heroDescriptions(params?: OperationParamsMap["opendota-hero-descriptions"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  heroDurations(params: OperationParamsMap["opendota-hero-durations"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  heroItems(params: OperationParamsMap["opendota-hero-items"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  heroMatches(params: OperationParamsMap["opendota-hero-matches"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  heroMatchups(params: OperationParamsMap["opendota-hero-matchups"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  heroStats(params?: OperationParamsMap["opendota-hero-stats"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  heroes(params?: OperationParamsMap["opendota-heroes"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  items(params?: OperationParamsMap["opendota-items"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  league(params: OperationParamsMap["opendota-league"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  leagueMatchIds(params: OperationParamsMap["opendota-league-match-ids"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  leagueMatches(params: OperationParamsMap["opendota-league-matches"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  leagues(params?: OperationParamsMap["opendota-leagues"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  live(params?: OperationParamsMap["opendota-live"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  match(params: OperationParamsMap["opendota-match"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  patchNotes(params?: OperationParamsMap["opendota-patch-notes"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  proMatches(params?: OperationParamsMap["opendota-pro-matches"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  proPlayers(params?: OperationParamsMap["opendota-pro-players"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  publicMatches(params?: OperationParamsMap["opendota-public-matches"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  rankDistribution(params?: OperationParamsMap["opendota-rank-distribution"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  records(params: OperationParamsMap["opendota-records"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  scenarios(params: OperationParamsMap["opendota-scenarios"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  team(params: OperationParamsMap["opendota-team"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamHeroes(params: OperationParamsMap["opendota-team-heroes"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamMatches(params: OperationParamsMap["opendota-team-matches"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamPlayers(params: OperationParamsMap["opendota-team-players"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teams(params?: OperationParamsMap["opendota-teams"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  abilities(...args: OperationRequestArgs<"opendota-abilities">): Promise<OperationResponseMap["opendota-abilities"]>;
  benchmarks(...args: OperationRequestArgs<"opendota-benchmarks">): Promise<OperationResponseMap["opendota-benchmarks"]>;
  constants(...args: OperationRequestArgs<"opendota-constants">): Promise<OperationResponseMap["opendota-constants"]>;
  findMatches(...args: OperationRequestArgs<"opendota-find-matches">): Promise<OperationResponseMap["opendota-find-matches"]>;
  heroDescriptions(...args: OperationRequestArgs<"opendota-hero-descriptions">): Promise<OperationResponseMap["opendota-hero-descriptions"]>;
  heroDurations(...args: OperationRequestArgs<"opendota-hero-durations">): Promise<OperationResponseMap["opendota-hero-durations"]>;
  heroItems(...args: OperationRequestArgs<"opendota-hero-items">): Promise<OperationResponseMap["opendota-hero-items"]>;
  heroMatches(...args: OperationRequestArgs<"opendota-hero-matches">): Promise<OperationResponseMap["opendota-hero-matches"]>;
  heroMatchups(...args: OperationRequestArgs<"opendota-hero-matchups">): Promise<OperationResponseMap["opendota-hero-matchups"]>;
  heroStats(...args: OperationRequestArgs<"opendota-hero-stats">): Promise<OperationResponseMap["opendota-hero-stats"]>;
  heroes(...args: OperationRequestArgs<"opendota-heroes">): Promise<OperationResponseMap["opendota-heroes"]>;
  items(...args: OperationRequestArgs<"opendota-items">): Promise<OperationResponseMap["opendota-items"]>;
  league(...args: OperationRequestArgs<"opendota-league">): Promise<OperationResponseMap["opendota-league"]>;
  leagueMatchIds(...args: OperationRequestArgs<"opendota-league-match-ids">): Promise<OperationResponseMap["opendota-league-match-ids"]>;
  leagueMatches(...args: OperationRequestArgs<"opendota-league-matches">): Promise<OperationResponseMap["opendota-league-matches"]>;
  leagues(...args: OperationRequestArgs<"opendota-leagues">): Promise<OperationResponseMap["opendota-leagues"]>;
  live(...args: OperationRequestArgs<"opendota-live">): Promise<OperationResponseMap["opendota-live"]>;
  match(...args: OperationRequestArgs<"opendota-match">): Promise<OperationResponseMap["opendota-match"]>;
  patchNotes(...args: OperationRequestArgs<"opendota-patch-notes">): Promise<OperationResponseMap["opendota-patch-notes"]>;
  proMatches(...args: OperationRequestArgs<"opendota-pro-matches">): Promise<OperationResponseMap["opendota-pro-matches"]>;
  proPlayers(...args: OperationRequestArgs<"opendota-pro-players">): Promise<OperationResponseMap["opendota-pro-players"]>;
  publicMatches(...args: OperationRequestArgs<"opendota-public-matches">): Promise<OperationResponseMap["opendota-public-matches"]>;
  rankDistribution(...args: OperationRequestArgs<"opendota-rank-distribution">): Promise<OperationResponseMap["opendota-rank-distribution"]>;
  records(...args: OperationRequestArgs<"opendota-records">): Promise<OperationResponseMap["opendota-records"]>;
  scenarios(...args: OperationRequestArgs<"opendota-scenarios">): Promise<OperationResponseMap["opendota-scenarios"]>;
  team(...args: OperationRequestArgs<"opendota-team">): Promise<OperationResponseMap["opendota-team"]>;
  teamHeroes(...args: OperationRequestArgs<"opendota-team-heroes">): Promise<OperationResponseMap["opendota-team-heroes"]>;
  teamMatches(...args: OperationRequestArgs<"opendota-team-matches">): Promise<OperationResponseMap["opendota-team-matches"]>;
  teamPlayers(...args: OperationRequestArgs<"opendota-team-players">): Promise<OperationResponseMap["opendota-team-players"]>;
  teams(...args: OperationRequestArgs<"opendota-teams">): Promise<OperationResponseMap["opendota-teams"]>;
}
export { OpenDotaClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default OpenDotaClient;
