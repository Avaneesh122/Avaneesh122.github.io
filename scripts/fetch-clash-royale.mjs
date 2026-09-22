// Fetches live trophy/arena data for a Clash Royale player via the RoyaleAPI
// proxy (proxy.royaleapi.dev) and writes a small public JSON file the site
// reads client-side. Run by .github/workflows/clash-royale.yml on a schedule.
//
// Requires env var CR_API_TOKEN (a Supercell developer API key whose
// allowed IP is 45.79.218.79 — the RoyaleAPI proxy's fixed IP).

const PLAYER_TAG = "2LUQ22P2C"; // without leading #
const OUT_PATH = new URL("../public/clash-royale.json", import.meta.url);

const token = process.env.CR_API_TOKEN;
if (!token) {
  console.error("CR_API_TOKEN env var is not set");
  process.exit(1);
}

const res = await fetch(`https://proxy.royaleapi.dev/v1/players/%23${PLAYER_TAG}`, {
  headers: { Authorization: `Bearer ${token}` },
});

if (!res.ok) {
  console.error(`Clash Royale API request failed: ${res.status} ${res.statusText}`);
  console.error(await res.text());
  process.exit(1);
}

const player = await res.json();

const data = {
  tag: player.tag,
  name: player.name,
  trophies: player.trophies,
  bestTrophies: player.bestTrophies,
  arenaName: player.arena?.name ?? null,
  updatedAt: new Date().toISOString(),
};

const fs = await import("node:fs/promises");
await fs.writeFile(OUT_PATH, JSON.stringify(data, null, 2) + "\n");

console.log("Wrote", OUT_PATH.pathname, data);
