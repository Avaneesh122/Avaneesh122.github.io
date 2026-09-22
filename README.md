# avaneesh-portfolio

Personal portfolio site, built with [Astro](https://astro.build) and deployed free on GitHub Pages.

## Develop

```bash
npm install
npm run dev
```

## Deploy (GitHub Pages, free)

1. Create a GitHub repo named **`Avaneesh122.github.io`** (must match this exactly for a user site at the root domain).
2. Push this project to it (`main` branch).
3. In the repo, go to **Settings → Pages → Build and deployment → Source** and select **GitHub Actions**.
4. Push to `main` — `.github/workflows/deploy.yml` builds and deploys automatically.
5. Site goes live at `https://avaneesh122.github.io`.

## Update content

- Bio / narrative: `src/components/About.astro`
- Featured projects: `src/components/Work.astro`
- Experience timeline: `src/components/Experience.astro`
- Skills: `src/components/Skills.astro`
- Contact links: `src/components/Contact.astro`
- Resume PDF: replace `public/resume.pdf` (regenerate via `python3 scripts/build_resume_pdf.py` if editing the source resume)
