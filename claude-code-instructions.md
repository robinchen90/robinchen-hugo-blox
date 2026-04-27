# Claude Code Instructions: SEO & LLM-Accessibility Improvements for robinchen.org

**Project:** Hugo Blox Builder static site (Hugo + Wowchemy/Hugo Academic theme).
**Goal:** Add machine-readable metadata, schema markup, and standard files. Do NOT change any visible content, layout, or design. All changes are at the engineering/template layer.

**Working directory:** The Hugo site root (the folder containing `config.toml` or `hugo.toml`, `content/`, `layouts/`, `themes/`, `static/`, etc.).

---

## Pre-flight: Orient yourself in the codebase

Before making changes, run these and report findings:

```bash
ls -la
cat hugo.toml 2>/dev/null || cat config.toml 2>/dev/null || cat config.yaml 2>/dev/null
ls themes/
ls layouts/ 2>/dev/null
ls content/
ls static/ 2>/dev/null
```

Confirm:
- Hugo config file format (toml/yaml)
- Theme name and version (likely `hugo-blox-builder` or `wowchemy`)
- Whether `layouts/` exists at the project root for overrides
- Whether `static/` exists for serving raw files at the site root

If `layouts/` does not exist at the project root, create it. All template overrides go there, NOT inside `themes/` (theme files get overwritten on theme updates).

---

## Task 1 — Create `/llms.txt` at the site root

**File to create:** `static/llms.txt`

Hugo serves anything in `static/` at the site root, so `static/llms.txt` becomes `https://robinchen.org/llms.txt`.

**Content:**

```markdown
# Robin Chen
> Assistant Professor of Economics, University of Northern Iowa.
> Research: monetary policy transmission, structural VAR identification,
> Divisia monetary aggregates, Federal Reserve policy rules.

## Published research
- [Decomposing Supply and Demand Driven Inflation in Mexico](https://robinchen.org/publication/mexico-inflation-decomposition/): Economics Letters (2026).
- [Demystifying Monetary Policy Surprises](https://robinchen.org/publication/demystifying-monetary-policy/): Journal of Macroeconomics (2026).
- [From Disruption to Integration: Cryptocurrency Prices, Financial Fluctuations, and Macroeconomy](https://robinchen.org/publication/crypto-shock/): JRFM (2025).
- [Modeling Inflation Expectations in Forward-Looking Interest Rate and Money Growth Rules](https://robinchen.org/publication/inflation-expectations-policy-rules/): JEDC (2025).
- [A Granular Investigation on the Stability of Money Demand](https://robinchen.org/publication/money-demand-stability/): Macroeconomic Dynamics (2024).
- [Monetary Transmission in Money Markets](https://robinchen.org/publication/divisia-puzzle/): JEDC (2021).

## Profile
- [Homepage](https://robinchen.org/)
- [Google Scholar](https://scholar.google.com/citations?user=fAkfUpYAAAAJ)
- [University profile](https://business.uni.edu/economics/directory/zhengyang-robin-chen)
```

**Verification:** After running `hugo server` locally, confirm `http://localhost:1313/llms.txt` returns this exact text.

---

## Task 2 — Verify and update `robots.txt` and `sitemap.xml`

### `robots.txt`

**Check:** Look at `static/robots.txt` and `themes/*/static/robots.txt`. Hugo also auto-generates one if `enableRobotsTXT = true` is set in config.

**Action:** Ensure the config has:

```toml
enableRobotsTXT = true
```

Then create `static/robots.txt` with:

```
User-agent: *
Allow: /

# Major search engines
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

# LLM crawlers — explicitly allow
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: CCBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: https://robinchen.org/sitemap.xml
```

If the user wants to BLOCK any crawler, change `Allow: /` to `Disallow: /` for that user-agent. Ask before assuming.

### `sitemap.xml`

Hugo auto-generates this. Confirm in `hugo.toml`:

```toml
[sitemap]
  changefreq = "weekly"
  priority = 0.5
  filename = "sitemap.xml"
```

After build, verify `public/sitemap.xml` exists and lists all publication URLs.

---

## Task 3 — Enable Git-based `lastmod` dates

In `hugo.toml` (or `config.toml`), add or confirm:

```toml
enableGitInfo = true
```

This makes `.Lastmod` and `.GitInfo.AuthorDate` populate from git commit history. The sitemap and JSON-LD `dateModified` fields will automatically reflect actual modification dates.

**Verification:** Run `hugo` and inspect `public/sitemap.xml` — `<lastmod>` entries should be ISO 8601 dates from git history, not all identical to today.

---

## Task 4 — Add `Person` JSON-LD to the homepage

**File to create or edit:** `layouts/partials/custom_head.html` (Wowchemy/Hugo Blox provides this hook by convention; check `themes/*/layouts/partials/` to confirm the exact filename — it may be `head_custom.html` or `custom/head.html` depending on theme version).

**If the partial already exists**, append to it. **If not**, create it.

**Content to add (only renders on the homepage):**

```html
{{ if .IsHome }}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Zhengyang Chen",
  "alternateName": "Robin Chen",
  "jobTitle": "Assistant Professor of Economics",
  "affiliation": {
    "@type": "Organization",
    "name": "University of Northern Iowa",
    "url": "https://business.uni.edu/economics/directory/zhengyang-robin-chen"
  },
  "alumniOf": [
    {"@type": "Organization", "name": "University of Texas at Dallas"},
    {"@type": "Organization", "name": "Johns Hopkins University"},
    {"@type": "Organization", "name": "Guangdong University of Foreign Studies"}
  ],
  "url": "https://robinchen.org/",
  "email": "zhengyang.chen@uni.edu",
  "sameAs": [
    "https://scholar.google.com/citations?user=fAkfUpYAAAAJ",
    "https://www.researchgate.net/profile/Zhengyang-Chen-7",
    "https://www.linkedin.com/in/robinchen90/",
    "https://business.uni.edu/economics/directory/zhengyang-robin-chen"
  ]
}
</script>
{{ end }}
```

**ACTION REQUIRED:** Ask the user for their ORCID iD. If they have one, add it to the `sameAs` array as `https://orcid.org/XXXX-XXXX-XXXX-XXXX`. If they don't have one, leave a comment in the file: `<!-- TODO: Add ORCID once registered at https://orcid.org -->`.

**Verification:** Build the site, view homepage source, confirm the JSON-LD block is present in `<head>`. Run the rendered HTML through https://validator.schema.org and https://search.google.com/test/rich-results.

---

## Task 5 — Add `BreadcrumbList` JSON-LD to publication pages

**File to create:** `layouts/partials/breadcrumb_jsonld.html`

**Content:**

```html
{{ if eq .Section "publication" }}
{{ if not .IsSection }}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "{{ .Site.BaseURL }}"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Research",
      "item": "{{ .Site.BaseURL }}publication/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": {{ .Title | jsonify }},
      "item": "{{ .Permalink }}"
    }
  ]
}
</script>
{{ end }}
{{ end }}
```

Then include it in `custom_head.html`:

```html
{{ partial "breadcrumb_jsonld.html" . }}
```

**Verification:** Inspect `<head>` on a publication page (e.g., `/publication/mexico-inflation-decomposition/`) and confirm the BreadcrumbList JSON-LD is present and valid.

---

## Task 6 — Add `FAQPage` JSON-LD partial for Q&A publication pages

This is the biggest single task. It applies to publication pages that have FAQ-style Q&A sections (currently `/publication/mexico-inflation-decomposition/` and `/publication/demystifying-monetary-policy/`).

### Step 6.1 — Create the partial

**File to create:** `layouts/partials/faq_jsonld.html`

**Content:**

```html
{{ with .Params.faq }}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{ range $index, $item := . }}
    {{ if $index }},{{ end }}
    {
      "@type": "Question",
      "name": {{ $item.question | jsonify }},
      "acceptedAnswer": {
        "@type": "Answer",
        "text": {{ $item.answer | jsonify }}
      }
    }
    {{ end }}
  ]
}
</script>
{{ end }}
```

### Step 6.2 — Wire it into `custom_head.html`

```html
{{ partial "faq_jsonld.html" . }}
```

### Step 6.3 — Add `faq:` block to publication front matter

Edit `content/publication/mexico-inflation-decomposition/index.md` (or `.markdown` — check the actual filename). At the top, in the YAML front matter, add a new `faq:` field. The questions and answers should match what's already visible on the page; just **copy them, don't rewrite**.

Pattern:

```yaml
faq:
  - question: "Why is food so dominant in Mexican inflation compared to advanced economies?"
    answer: "Food dominates because it combines a large CPI weight with high sensitivity to both domestic demand cycles and global supply shocks — a pattern that developed-economy decomposition frameworks don't capture..."
  - question: "What explains Mexico's slow disinflation since 2023 despite 725 basis points of tightening?"
    answer: "The services floor. Services contribute a large, low-volatility share of demand-driven inflation that adjusts slowly to monetary tightening..."
  # ... continue for all 6 Q&As on the page
```

**Important:** The `answer` field should be plain text, no Markdown links, no HTML. Strip these from the visible content when copying. JSON-LD `text` fields cannot contain markup.

Repeat the same exercise for `content/publication/demystifying-monetary-policy/index.md`.

### Step 6.4 — Validate

After building, run both pages through:

- https://search.google.com/test/rich-results
- https://validator.schema.org

Both should report no errors. Pages should be eligible for FAQ rich results in Google search.

---

## Task 7 — Verify `ScholarlyArticle` JSON-LD on publication pages

Hugo Blox emits `ScholarlyArticle` schema by default via the publication template. Inspect `<head>` on a published paper page and confirm the JSON-LD includes:

- `headline` — paper title
- `author` array with names and affiliations
- `datePublished` — ISO 8601
- `isPartOf` with journal name and ISSN
- `identifier` with DOI
- `url` — DOI link
- `keywords` array
- `abstract`

If any field is missing, override the publication template at `layouts/publication/single.html` and add the missing fields. Do NOT modify files inside `themes/`.

If the user has an ORCID, also add it to each author's identifier:

```json
"author": [
  {
    "@type": "Person",
    "name": "Zhengyang Chen",
    "identifier": "https://orcid.org/XXXX-XXXX-XXXX-XXXX"
  }
]
```

**Verification:** Run a publication URL through https://validator.schema.org. No errors expected.

---

## Task 8 — Verify per-page `<meta name="description">`

Inspect `<head>` on each publication page. Confirm there is a `<meta name="description" content="...">` tag and it is unique to that page (not the site default).

For Hugo Blox, this typically pulls from the `summary` field in front matter. Check each publication's front matter has a `summary:` field set to a one-sentence description (~150 characters). If any are missing, add them — copy the existing TL;DR text from the page.

This is an audit task: only modify files where the description is missing.

---

## Task 9 — Verify OpenGraph and Twitter Card tags

Inspect `<head>` on a publication page. Confirm these tags exist (Hugo Blox should set them by default):

```html
<meta property="og:type" content="article">
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:url" content="...">
<meta property="og:image" content="...">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="...">
<meta name="twitter:description" content="...">
```

If any are missing, override the head template. Do NOT replace existing tags if they're already correct.

---

## Task 10 — Verify canonical URLs

Inspect `<head>` on every page type (homepage, publication page, project page, conference page, author page). Each must have:

```html
<link rel="canonical" href="https://robinchen.org/[exact-path]/">
```

pointing to itself. Hugo Blox sets this by default. If any page is missing it, add via head template override.

---

## Task 11 — Verify HTTP headers

Run from terminal:

```bash
curl -I https://robinchen.org/
curl -I https://robinchen.org/publication/mexico-inflation-decomposition/
curl -I https://robinchen.org/publication/mexico-inflation-decomposition/mexico-inflation-decomposition.pdf
```

Confirm:

- HTML pages return `Content-Type: text/html; charset=UTF-8`
- PDFs return `Content-Type: application/pdf`
- No `X-Robots-Tag: noindex` is present anywhere
- HTTPS is enforced (HTTP requests redirect to HTTPS)
- `Last-Modified` headers are present

If the site is hosted on Netlify, header configuration goes in `netlify.toml` or `_headers` at the project root. If on GitHub Pages, headers are mostly fixed but content-type for PDFs should work automatically. If on another host, check that platform's docs.

If any header is wrong, fix it via the host's config file. Report what platform the user is on if unclear.

---

## Task 12 — Final build and validation

After all changes, run:

```bash
hugo --minify
```

Then check `public/` for the build output. Open `public/llms.txt`, `public/robots.txt`, `public/sitemap.xml`, and `public/index.html` to spot-check.

Run these external validators on the deployed site (after the user pushes the changes live):

1. https://validator.schema.org — paste the homepage URL and one publication URL each
2. https://search.google.com/test/rich-results — same two URLs
3. https://www.opengraph.xyz — verify OpenGraph tags
4. https://cards-dev.twitter.com/validator — verify Twitter Cards (if Twitter still has this tool)

Report any errors back to the user.

---

## What NOT to do

- Do NOT modify any files inside `themes/`. All overrides go in `layouts/` at the project root.
- Do NOT change any content under `content/` except adding `faq:` and `summary:` fields to front matter where instructed. Do NOT edit the visible page body text, headings, or formatting.
- Do NOT add new visible UI elements, badges, widgets, or design changes.
- Do NOT change CSS or JavaScript files.
- Do NOT remove or replace existing JSON-LD blocks unless they are clearly broken — add new ones alongside if uncertain.
- Do NOT touch working-paper / unpublished pages — the user wants these to remain as-is.

---

## Summary of files created or modified

After all tasks, the change set should be roughly:

**Created:**
- `static/llms.txt`
- `static/robots.txt` (if not auto-generated correctly)
- `layouts/partials/custom_head.html` (or extension of existing)
- `layouts/partials/breadcrumb_jsonld.html`
- `layouts/partials/faq_jsonld.html`

**Modified:**
- `hugo.toml` (add `enableGitInfo`, `enableRobotsTXT`, sitemap config)
- `content/publication/mexico-inflation-decomposition/index.md` (add `faq:` and verify `summary:` in front matter only)
- `content/publication/demystifying-monetary-policy/index.md` (same)
- Other publication front matter files only if `summary:` is missing
- `netlify.toml` or `_headers` if header issues are found

**Untouched:**
- All files under `themes/`
- All visible content in publication page bodies
- All design, CSS, layout files
- Working-paper pages

---

## Reporting back

When done, give the user:

1. Which tasks completed successfully
2. Which tasks were blocked (e.g., missing ORCID, unclear hosting platform)
3. The full list of files created and modified
4. Any validator errors that need follow-up
5. The exact `git diff --stat` summary so they can see the change scope

Then ask the user to commit, push, and run the external validators on the deployed site.
