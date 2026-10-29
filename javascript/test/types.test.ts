import { OpenDotaClient } from "../src/index.js";

const client = new OpenDotaClient({ apiKey: "test-key" });
void client.benchmarks({"hero_id": 1});
void client.request("opendota-benchmarks", {"hero_id": 1});
const streamResponse: Promise<Response> = client.request("opendota-benchmarks", {"hero_id": 1}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("opendota-benchmarks", {"hero_id": 1}, { responseType: "stream" });
const directStream: Promise<Response> = client.benchmarks({"hero_id": 1}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("opendota-benchmarks", {"hero_id": 1, "bracket": 1, "role": "core"}, { responseType: "text" });
const rawText: Promise<string> = client.request("opendota-benchmarks", {"hero_id": 1}, { responseType: "text" });
void rawText;


void client.abilities();
void client.request("opendota-abilities");
// @ts-expect-error The selected operation requires its documented params.
void client.benchmarks();
