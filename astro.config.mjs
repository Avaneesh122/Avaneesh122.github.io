import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://avaneesh122.github.io",
  outDir: "./dist",
  build: {
    assets: "assets",
  },
});
