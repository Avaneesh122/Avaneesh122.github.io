# avaneesh-portfolio

Personal portfolio site, built with [Astro](https://astro.build) and deployed free on GitHub Pages.

## Develop

```bash
npm install
npm run dev
```

## Deploy (GitHub Pages, free)

1. Create a GitHub repo named **`Avaneesh122.github.io`** (must match this exactly for a user site at the root domain).
2. Push this project to it (`master` branch).
3. In the repo, go to **Settings → Pages → Build and deployment → Source** and select **GitHub Actions**.
4. Push to `master` — `.github/workflows/deploy.yml` builds and deploys automatically.
5. Site goes live at `https://avaneesh122.github.io`.

## Update content

- Bio / narrative: `src/components/About.astro`
- Featured projects: `src/components/Work.astro`
- Experience timeline: `src/components/Experience.astro`
- Skills: `src/components/Skills.astro`
- Contact links: `src/components/Contact.astro`
- Resume PDF: replace `public/resume.pdf` (regenerate via `python3 scripts/build_resume_pdf.py` if editing the source resume)
- Challenge Me / games: `src/components/ChallengeMe.astro`

## Live Clash Royale stats

The Clash Royale card in Challenge Me shows live trophies/arena, refreshed every 30 minutes by
`.github/workflows/clash-royale.yml`, which runs `scripts/fetch-clash-royale.mjs` and commits the
result to `public/clash-royale.json`. The site fetches that JSON client-side.

Setup (one-time):

1. Create an API key at [developer.clashroyale.com](https://developer.clashroyale.com). Supercell's
   API only allows fixed IPs, and GitHub Actions runners don't have one, so under **Allowed IP
   Addresses** whitelist `45.79.218.79` — [RoyaleAPI's proxy](https://docs.royaleapi.com/proxy.html)
   IP, not your own. Requests go through `proxy.royaleapi.dev` instead of `api.clashroyale.com`.
2. In this repo: **Settings → Secrets and variables → Actions → New repository secret**, name
   `CR_API_TOKEN`, paste the key value.
3. Until the secret is set, the workflow skips itself on schedule (no failing runs/emails) and the
   card just shows the friend-invite button with no stats row.
