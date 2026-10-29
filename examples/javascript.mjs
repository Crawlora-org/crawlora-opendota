import { OpenDotaClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new OpenDotaClient({ apiKey });

  const heroes = await client.heroes({  });
  console.log("heroes", heroes);
  const proMatches = await client.proMatches({  });
  console.log("proMatches", proMatches);
