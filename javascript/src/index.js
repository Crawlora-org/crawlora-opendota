import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class OpenDotaClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-opendota-js/0.1.0" });
    this["abilities"] = (...args) => this.request("opendota-abilities", ...args);
    this["benchmarks"] = (...args) => this.request("opendota-benchmarks", ...args);
    this["constants"] = (...args) => this.request("opendota-constants", ...args);
    this["findMatches"] = (...args) => this.request("opendota-find-matches", ...args);
    this["heroDescriptions"] = (...args) => this.request("opendota-hero-descriptions", ...args);
    this["heroDurations"] = (...args) => this.request("opendota-hero-durations", ...args);
    this["heroItems"] = (...args) => this.request("opendota-hero-items", ...args);
    this["heroMatches"] = (...args) => this.request("opendota-hero-matches", ...args);
    this["heroMatchups"] = (...args) => this.request("opendota-hero-matchups", ...args);
    this["heroStats"] = (...args) => this.request("opendota-hero-stats", ...args);
    this["heroes"] = (...args) => this.request("opendota-heroes", ...args);
    this["items"] = (...args) => this.request("opendota-items", ...args);
    this["league"] = (...args) => this.request("opendota-league", ...args);
    this["leagueMatchIds"] = (...args) => this.request("opendota-league-match-ids", ...args);
    this["leagueMatches"] = (...args) => this.request("opendota-league-matches", ...args);
    this["leagues"] = (...args) => this.request("opendota-leagues", ...args);
    this["live"] = (...args) => this.request("opendota-live", ...args);
    this["match"] = (...args) => this.request("opendota-match", ...args);
    this["patchNotes"] = (...args) => this.request("opendota-patch-notes", ...args);
    this["proMatches"] = (...args) => this.request("opendota-pro-matches", ...args);
    this["proPlayers"] = (...args) => this.request("opendota-pro-players", ...args);
    this["publicMatches"] = (...args) => this.request("opendota-public-matches", ...args);
    this["rankDistribution"] = (...args) => this.request("opendota-rank-distribution", ...args);
    this["records"] = (...args) => this.request("opendota-records", ...args);
    this["scenarios"] = (...args) => this.request("opendota-scenarios", ...args);
    this["team"] = (...args) => this.request("opendota-team", ...args);
    this["teamHeroes"] = (...args) => this.request("opendota-team-heroes", ...args);
    this["teamMatches"] = (...args) => this.request("opendota-team-matches", ...args);
    this["teamPlayers"] = (...args) => this.request("opendota-team-players", ...args);
    this["teams"] = (...args) => this.request("opendota-teams", ...args);
  }
}

export { OpenDotaClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default OpenDotaClient;
