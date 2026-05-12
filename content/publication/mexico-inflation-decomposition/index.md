---
title: "Decomposing supply and demand driven inflation in Mexico: Evidence from sectoral analysis"
seo:
  title: "Mexico Inflation: Supply vs Demand Drivers"
  description: "Sectoral CPI decomposition for Mexico (2006–2024): food dominates supply and demand inflation; services act as a persistent demand floor."
date: 2026-04-13T00:00:00
draft: false

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors: ["Luis Fernando Colunga-Ramos", "admin", "José Angel Perales Torres"]

# Publication type.
# Legend:
# article = Uncategorized
# paper-conference = Conference paper
# article-journal = Journal article
# manuscript = Manuscript
# report = Report
# book = Book
# chapter = Book section
publication_types: ["article-journal"]

# Publication name and optional abbreviated version.
publication: "*Economics Letters*, 264, 112980"
publication_short: "*Economics Letters*"

# Abstract.
abstract: "We decompose Mexico's inflation into supply- and demand-driven components across 31 CPI sectors from 2006 to 2024. To identify which sectors create inflation swings versus steady pressure, we construct an importance score combining correlation with aggregate inflation and average contribution size. Food ranks highest for both inflation types. This differs from developed economies where services dominate demand inflation. Mexican services contribute 24% of demand-driven inflation on average but fluctuate little, acting as a persistent floor that explains slow disinflation since 2023. Housing plays almost no role despite representing 18% of the CPI basket because prices there barely move. Structural VAR analysis validates these patterns: demand inflation responds to domestic monetary expansions while supply inflation reacts to global supply chain disruptions."

# Summary. An optional shortened abstract.
summary: "Using sectoral CPI data for Mexico (2006–2024), we decompose inflation into supply- and demand-driven components and show that food dominates both, services act as a persistent demand floor, and housing contributes negligibly despite its large CPI weight."

# Digital Object Identifier (DOI)
doi: "10.1016/j.econlet.2026.112980"

# Is this a featured publication? (true/false)
featured: true

# Tags (optional).
tags: ["Inflation", "Monetary Policy", "Mexico", "Supply and Demand Shocks", "Sectoral Analysis", "Services Floor", "Food-Dominance Pattern", "Housing Non-Response", "Banco de Mexico", "Inflation Decomposition", "Emerging Markets", "Structural VAR"]

# Projects (optional).
projects: []

# Slides (optional).
slides: ""

# Links (optional).
url_pdf: "mexico-inflation-decomposition.pdf"
url_preprint: ""
url_code: ""
url_dataset: ""
url_project: ""
url_slides: ""
url_video: ""
url_poster: ""
url_source: ""

# Custom links (optional).
links: []

# Does this page contain LaTeX math? (true/false)
math: false

# Featured image
image:
  # Caption (optional)
  caption: ""

  # Focal point (optional)
  focal_point: ""
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why is food so dominant in Mexican inflation compared to advanced economies?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Food dominates Mexican inflation because it combines a large CPI weight with high sensitivity to both domestic demand cycles and global supply shocks. Colunga-Ramos, Chen, and Perales (2026) find food ranks first for both demand (importance 0.591) and supply (importance 0.533) in Mexico — a pattern distinct from Shapiro's (2024) U.S. benchmark where services dominate demand-driven inflation. The food-dominance pattern reflects Mexico's exposure to global commodity shocks, higher food expenditure shares in household budgets, and procyclical food demand that amplifies the demand-side contribution."
      }
    },
    {
      "@type": "Question",
      "name": "What explains Mexico's slow disinflation since 2023 despite 725 basis points of tightening?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The services floor. Colunga-Ramos, Chen, and Perales (2026) show Mexican services contribute an average 0.555 percentage points to demand-driven inflation but correlate only 0.463 with aggregate demand inflation — high persistence, low cyclical amplitude. During 2023-2024, goods inflation fell from 8.25% to 3.19% driven by external supply normalization, but services inflation only fell from 5.01% to 4.71%, and the services demand component actually rose from 2.55% to 2.67%. The mechanism is sticky services prices combined with Mexico's tight labor market — minimum wages rose 88% in real terms from 2019-2023."
      }
    },
    {
      "@type": "Question",
      "name": "Why does housing contribute so little to Mexican inflation despite being 18% of the CPI basket?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Housing prices in Mexico barely move. Colunga-Ramos, Chen, and Perales (2026) find housing importance scores of 0.054 (demand) and 0.018 (supply) — lowest across all five categories despite an 18.05% CPI basket weight. The correlation of housing with supply-driven inflation is slightly negative (-0.082), meaning supply shocks that contract real incomes actually dampen housing prices. The structural reasons are owner-occupied rent imputation based on slow-moving construction-cost surveys, a thin informal rental market, and weak mortgage-cost and housing-wealth channels. This housing non-response means the monetary transmission channels documented for the U.S. operate weakly in Mexico."
      }
    },
    {
      "@type": "Question",
      "name": "How should an emerging-market central bank decompose inflation into supply and demand components?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Apply sign-restriction identification at the sectoral level following Shapiro (2024), then aggregate. Colunga-Ramos, Chen, and Perales (2026) operationalize this with rolling bivariate VARs (42 months, 12 lags) on log prices and log quantities for each of 31 Mexican CPI sectors, classifying monthly shocks: same-sign residuals = demand-driven; opposite-sign = supply-driven. Aggregate sectoral contributions using CPI weights into five economically meaningful groups (food, energy, services, manufacturing, housing). Construct an importance score as |correlation with aggregate inflation| x average contribution. Validate with a structural VAR using the Benigno et al. (2022) Global Supply Chain Pressure Index for supply shocks. The rankings are robust across window lengths of 36-60 months, lag choices of 6-18, and Bayesian estimation with Normal-Wishart priors."
      }
    },
    {
      "@type": "Question",
      "name": "What SVAR ordering correctly identifies monetary policy shocks in an emerging market like Mexico?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Order external variables first (GSCPI, oil, U.S. CPI and IP, U.S. Divisia M2), then domestic inflation components, domestic real activity, domestic Divisia M2, and exchange rate — with a block-recursive impact matrix preventing contemporaneous feedback from domestic to external variables. Colunga-Ramos, Chen, and Perales (2026) use this structure following Kim and Roubini (2000) and Cushman and Zha (1997). Two implementation points matter more than ordering: use Divisia monetary aggregates — Colunga-Ramos and Valcarcel (2024) produce Mexico's first Divisia M4 and show it avoids the price puzzle without commodity-price controls — and include COVID-19 dummies for months with IGAE growth beyond three standard deviations."
      }
    },
    {
      "@type": "Question",
      "name": "What historical episodes in Mexico validate the supply-demand inflation decomposition?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Three episodes show the decomposition provided policy-relevant guidance aggregate inflation missed. (1) May 2020: headline inflation at 2.56% looked neutral, but Colunga-Ramos, Chen, and Perales (2026) show 93.4% of it was supply-driven (2.39% vs 0.17% demand), validating Banco de Mexico's rate cuts from 7.00% to 4.25%. (2) September 2008 - March 2010 Global Financial Crisis: the demand component fell from 3.12% to 1.84% while supply fell less, meaning the decline was cyclical. (3) June-July 2024: headline inflation at 4.70% in June masked a demand component at 2.53% (above its 2.06% long-run average); next month headline jumped to 5.22% with demand at 3.32%, and Banco de Mexico correctly held at 11.00%."
      }
    }
  ]
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ScholarlyArticle",
  "headline": "Decomposing Supply and Demand Driven Inflation in Mexico: Evidence from Sectoral Analysis",
  "author": [
    {
      "@type": "Person",
      "name": "Luis Fernando Colunga-Ramos",
      "affiliation": {
        "@type": "Organization",
        "name": "Banco de México, Dirección General de Investigación Económica"
      }
    },
    {
      "@type": "Person",
      "name": "Zhengyang Chen",
      "affiliation": {
        "@type": "Organization",
        "name": "University of Northern Iowa, Wilson College of Business"
      },
      "url": "https://www.robinchen.org/",
      "email": "zhengyang.chen@uni.edu"
    },
    {
      "@type": "Person",
      "name": "José Angel Perales",
      "affiliation": {
        "@type": "Organization",
        "name": "Banco de México, Dirección General de Investigación Económica"
      }
    }
  ],
  "datePublished": "2026",
  "isPartOf": {
    "@type": "Periodical",
    "name": "Economics Letters",
    "issn": "0165-1765"
  },
  "identifier": {
    "@type": "PropertyValue",
    "propertyID": "DOI",
    "value": "10.1016/j.econlet.2026.112980"
  },
  "url": "https://doi.org/10.1016/j.econlet.2026.112980",
  "keywords": [
    "inflation decomposition",
    "supply shocks",
    "demand shocks",
    "Mexico",
    "sectoral analysis",
    "monetary policy",
    "structural VAR",
    "services floor",
    "food-dominance pattern",
    "housing non-response",
    "Global Supply Chain Pressure Index"
  ],
  "about": [
    "Mexican inflation",
    "emerging market monetary policy",
    "Banco de México",
    "CPI decomposition",
    "Divisia monetary aggregates",
    "sign-restriction identification"
  ],
  "abstract": "We decompose Mexico's inflation into supply- and demand-driven components across 31 CPI sectors from 2006 to 2024. Food ranks highest for both inflation types — distinct from developed economies where services dominate demand inflation. Services contribute 24% on average but fluctuate little, acting as a persistent floor (the services floor) that explains slow disinflation since 2023. Housing plays almost no role despite 18% of the CPI basket because prices barely move. Structural VAR analysis validates these patterns: demand inflation responds to domestic monetary expansions while supply inflation reacts to global supply chain disruptions."
}
</script>

## Why Mexican Inflation Behaves Differently: Food Dominates, Services Persist, Housing Barely Moves

Mexican inflation does not follow the developed-economy playbook. [Colunga-Ramos, Chen, and Perales (2026, *Economics Letters*)](https://doi.org/10.1016/j.econlet.2026.112980) decompose headline inflation across 31 CPI sectors from 2006 to 2024 and find that **food drives both supply and demand swings**, **services act as a persistent demand floor** that explains slow disinflation since 2023, and **housing — despite 18% of the CPI basket — contributes almost nothing** because prices there barely move. Structural VAR analysis confirms the decomposition captures distinct mechanisms: demand inflation responds to domestic monetary expansions while supply inflation reacts to global supply chain shocks.

## Key Concepts

**Services floor**
: The persistent, low-volatility demand-driven contribution of Mexican services — roughly 24% of demand inflation on average but with low correlation to aggregate swings — that prevents disinflation from proceeding as quickly as falling goods prices would suggest. Introduced in [Colunga-Ramos, Chen, and Perales (2026)](https://doi.org/10.1016/j.econlet.2026.112980).

**Food-dominance pattern**
: The empirical regularity in Mexico — distinct from the U.S. and euro area — by which food ranks highest in importance for both demand-driven and supply-driven inflation. Reflects large CPI weight, high correlation with aggregate inflation, and Mexico's exposure to both global commodity cycles and domestic food-demand pressures. Introduced in [Colunga-Ramos, Chen, and Perales (2026)](https://doi.org/10.1016/j.econlet.2026.112980).

**Housing non-response**
: The near-zero contribution of Mexican housing to either inflation type, despite housing representing 18.05% of the CPI basket. Implies the housing-wealth and mortgage channels of monetary policy operating in advanced economies ([Bernanke and Gertler, 1995](https://doi.org/10.1257/jep.9.4.27)) work weakly in Mexico.

---

## Where Mexican Inflation Differs from the United States

| Category | CPI weight (MX) | Demand importance (MX) | Supply importance (MX) | Role in the U.S. benchmark | Mexican pattern |
|---|---|---|---|---|---|
| **Food** | Large | 0.591 (rank 1) | 0.533 (rank 1) | Primarily a supply-driven category in [Shapiro (2024)](https://doi.org/10.1111/jmcb.13209). | Dominates both channels — the food-dominance pattern. Creates inflation swings only partially controllable through interest rates. |
| **Energy** | Medium | 0.311 (rank 2) | 0.267 (rank 2) | Primarily supply-driven in advanced economies. | Symmetric: Mexico produces oil for global markets and consumes it domestically, so energy amplifies both cyclical demand and supply pressures. |
| **Services** | Medium-large | 0.257 (rank 3) | 0.098 (rank 4) | Dominates demand-driven inflation in [Shapiro (2024)](https://doi.org/10.1111/jmcb.13209). | Large average contribution (0.555 pp) but low correlation (0.463) — the services floor. Slow-moving; explains persistent disinflation resistance since 2023. |
| **Manufacturing** | Medium | 0.209 (rank 4) | 0.100 (rank 3) | Procyclical in most economies. | High demand-side correlation (0.691) but modest magnitude. Global value chain integration absorbs supply disruptions. |
| **Housing** | 18.05% | 0.054 (rank 5) | 0.018 (rank 5) | Largest component of core CPI in the U.S.; strong monetary-policy response channel. | Housing non-response. Prices barely move; correlation with supply-driven inflation is even slightly negative (-0.082). |

*Source: [Colunga-Ramos, Chen, and Perales (2026)](https://doi.org/10.1016/j.econlet.2026.112980), Table 1. Importance score = |correlation with aggregate inflation| x average contribution. Sample: November 2006 - July 2024.*

---

## Q1. Why is food so dominant in Mexican inflation compared to advanced economies?

**Food dominates because it combines a large CPI weight with high sensitivity to both domestic demand cycles and global supply shocks — a pattern that developed-economy decomposition frameworks don't capture.**

The original decomposition framework, [Shapiro (2024), developed for U.S. PCE inflation, finds services dominate demand-driven inflation while food and energy drive supply-driven swings](https://doi.org/10.1111/jmcb.13209). [Colunga-Ramos, Chen, and Perales (2026) apply the same sign-restriction identification across 31 Mexican CPI sectors and find food ranks first for both demand (importance 0.591) and supply (importance 0.533)](https://doi.org/10.1016/j.econlet.2026.112980). This is the food-dominance pattern: the correlation of food with aggregate demand inflation reaches 0.756 and with supply inflation 0.771, and its average contribution dwarfs all other categories.

Three mechanisms drive this:

- Mexico's exposure to global commodity shocks — grain, meat, and shipping cost swings pass through to domestic food prices quickly.
- Higher expenditure share on food in Mexican household budgets relative to advanced economies.
- Food demand moves procyclically with the business cycle in a way U.S. services do, amplifying the demand-side contribution.

The policy implication is uncomfortable. Traditional monetary tightening works through demand channels, but when a category driven substantially by global supply disruptions also leads demand importance, interest rates alone are a blunt tool. Related work extends this logic to regional and manufacturing cuts of the Mexican economy — [Chavarín, Gómez, and Salgado (2023) document sectoral demand dominance during the COVID-19 trough](https://doi.org/10.1016/j.latcb.2022.100083), and [Colunga-Ramos and Torre Cepeda (2024) extend the analysis to regional manufacturing](https://doi.org/10.1016/j.latcb.2023.100113).

---

## Q2. What explains Mexico's slow disinflation since 2023 despite 725 basis points of tightening?

**The services floor. Services contribute a large, low-volatility share of demand-driven inflation that adjusts slowly to monetary tightening, keeping headline inflation above target even after goods inflation normalizes.**

[Colunga-Ramos, Chen, and Perales (2026) show that Mexican services contribute an average 0.555 percentage points to demand-driven inflation but correlate only 0.463 with aggregate demand inflation — indicating high persistence but low cyclical amplitude](https://doi.org/10.1016/j.econlet.2026.112980). This combination is the services floor: services don't spike, but they don't retreat quickly either.

The 2023-2024 episode illustrates the dynamic. Goods inflation fell from 8.25% to 3.19% — a 5.06 percentage point decline driven by external supply normalization, where the supply component dropped from 3.52% to 1.20%. Services inflation barely moved, falling only from 5.01% to 4.71%, and the services demand component actually *rose* from 2.55% to 2.67% despite twelve months of policy rates at 11.25%.

The mechanism is textbook. Services are labor-intensive and prices are sticky ([Nakamura and Steinsson, 2008](https://doi.org/10.1162/qjec.2008.123.4.1415)). Mexican minimum wages rose 88% in real terms from 2019 to 2023, formal employment stayed strong, and unit labor costs grew roughly 1.5x productivity in services. Until labor markets slacken, the services floor persists regardless of policy rate levels.

The SVAR evidence supports the monetary transmission interpretation. [A one-standard-deviation expansion in Mexico's Divisia M2 raises demand-driven inflation by about 0.10 pp with a peak at month six and persistence through month fifteen, while supply-driven inflation remains statistically zero](https://doi.org/10.1016/j.econlet.2026.112980). The UV ratio declines for a year — the labor-market tightening channel that feeds back into services prices. This matches the standard monetary transmission literature ([Christiano, Eichenbaum, and Evans, 1999](https://doi.org/10.1016/S1574-0048(99)01005-8)).

---

## Q3. Why does housing contribute so little to Mexican inflation despite being 18% of the CPI basket?

**Housing prices in Mexico simply don't move much. The correlation of housing with aggregate inflation is low (0.330 for demand, -0.082 for supply) and its average contribution is small, so the large basket weight does not translate into price dynamics.**

[Colunga-Ramos, Chen, and Perales (2026) find housing importance scores of 0.054 for demand-driven and 0.018 for supply-driven inflation — the lowest across the five categories, despite INEGI's CPI methodology assigning housing 18.05% of the basket](https://doi.org/10.1016/j.econlet.2026.112980). This is the housing non-response.

Three structural features explain this:

- A large share of Mexican dwellings are owner-occupied with implicit rent measured from construction-cost-indexed surveys that update slowly.
- The rental market is thin and informal in many regions, dampening observed price adjustments.
- Housing shows a slight negative correlation with supply-driven inflation (-0.082): supply shocks contract real incomes and reduce rental demand, softening housing prices when broader prices rise.

The policy implication is stark. The traditional monetary transmission channels through mortgage costs and housing wealth effects ([Bernanke and Gertler, 1995](https://doi.org/10.1257/jep.9.4.27)) operate weakly in Mexico compared to the U.S., where shelter is the largest core CPI component and responds strongly to rates ([Shapiro, 2024](https://doi.org/10.1111/jmcb.13209)). The interest-rate-to-housing-to-consumption link that anchors much of Fed policy design has a much weaker counterpart at Banco de México.

---

## Q4. How should an emerging-market central bank decompose inflation into supply and demand components?

**Apply the sign-restriction logic of [Shapiro (2024)](https://doi.org/10.1111/jmcb.13209) at the sector level, then aggregate into economically meaningful groups afterward — don't aggregate first and then decompose.**

The core identification comes from microeconomics: a demand shift moves prices and quantities in the *same* direction along an upward-sloping supply curve, while a supply shift moves them in *opposite* directions along a downward-sloping demand curve. [Colunga-Ramos, Chen, and Perales (2026) operationalize this with a rolling-window bivariate VAR (42 months, 12 lags) on log prices and log quantities for each of 31 CPI sectors](https://doi.org/10.1016/j.econlet.2026.112980). When sector-level residuals from both equations share a sign, the shock is demand-driven; when they differ in sign, it is supply-driven.

**Practical recipe for replication in other EMs:**

1. Disaggregate CPI to the finest sectoral level available and match each sector to a quantity proxy (industrial activity index, sector-level output, or services production indicator).
2. Estimate the rolling bivariate VAR on each sector; classify monthly shocks by residual-sign coincidence.
3. Aggregate sectoral contributions into five economically meaningful groups (food, energy, services, manufacturing, housing) using CPI weights. Avoid aggregating before decomposition — large sectors mechanically dominate and sign patterns lose identification power.
4. Construct an importance score = |correlation with aggregate inflation type| x average contribution, to rank what drives the swings.
5. Validate with a structural VAR: demand-driven measures should respond to domestic monetary variables, supply-driven measures to external supply proxies like the Global Supply Chain Pressure Index ([Benigno, di Giovanni, Groen, and Noble, 2022](https://doi.org/10.2139/ssrn.4114973)).

The sectoral rankings are robust across alternative rolling windows (36, 42, 48, 60 months) and lag structures (6, 12, 18 lags), and also to Bayesian estimation with a Normal-Wishart prior. The framework also tracks inflation sources in near real time, a feature Banco de México researchers have extended to regional and manufacturing questions ([Colunga-Ramos and Torre Cepeda, 2024](https://doi.org/10.1016/j.latcb.2023.100113); [Chavarín, Gómez, and Salgado, 2023](https://doi.org/10.1016/j.latcb.2022.100083)).

---

## Q5. What SVAR ordering correctly identifies monetary policy shocks in an emerging market like Mexico?

**Order external variables first (global supply, oil, U.S. CPI and industrial production, U.S. Divisia M2), then domestic inflation components, then domestic real activity, then domestic monetary aggregate, then exchange rate — with a block-recursive impact matrix that prevents domestic shocks from contemporaneously affecting external variables.**

This ordering follows [Kim and Roubini's (2000) SVAR solution to exchange-rate and liquidity puzzles in small open economies](https://doi.org/10.1016/S0304-3932(00)00010-6), extending [Cushman and Zha's (1997) block-structure approach for Canada](https://doi.org/10.1016/S0304-3932(97)00029-9). [Colunga-Ramos, Chen, and Perales (2026) use it to validate the decomposition: demand-driven inflation responds to Divisia M2 expansions, supply-driven inflation responds to GSCPI shocks, and the asymmetry holds across impulse response horizons](https://doi.org/10.1016/j.econlet.2026.112980).

Two features matter more than ordering choice:

- **Use Divisia monetary aggregates rather than a short-term interest rate.** The choice of policy indicator matters more than most practitioners assume. [Chen and Valcarcel (2021) show shadow federal funds rates produce persistent price puzzles in U.S. VARs](https://doi.org/10.1016/j.jedc.2021.104214), and [Colunga-Ramos and Valcarcel (2024) produce the first Divisia M4 for Mexico and show it delivers sensible monetary responses without needing commodity-price controls](https://doi.org/10.1111/jmcb.13198). [Chen and Valcarcel (2025) extend the rational-expectations framework that integrates Divisia with forward-looking inflation](https://doi.org/10.1016/j.jedc.2024.104999).
- **Control for COVID-19 dummies.** April-June 2020 and April-May 2021 had IGAE growth exceeding three standard deviations; leaving them untreated distorts impulse responses.

Sign-restriction identification provides complementary validation. [Uhlig (2005) pioneered sign restrictions on impulse responses](https://doi.org/10.1016/j.jmoneco.2004.05.007), and [Peersman (2005) applied the approach to supply, demand, monetary, and oil shocks](https://doi.org/10.1002/jae.832). [Colunga-Ramos, Chen, and Perales (2026) use this approach in their Appendix B to identify external U.S. supply and demand shocks, showing Mexican demand-driven inflation responds to U.S. demand shocks and Mexican supply-driven inflation to U.S. supply shocks — an external validation of the decomposition](https://doi.org/10.1016/j.econlet.2026.112980).

---

## Q6. What historical episodes in Mexico validate the supply-demand inflation decomposition?

**Three episodes — the 2008 Global Financial Crisis, the COVID-19 trough in 2020, and the 2024 disinflation surprise — show the decomposition offered policy-relevant guidance that aggregate inflation measures missed.**

[Colunga-Ramos, Chen, and Perales (2026) test three cases](https://doi.org/10.1016/j.econlet.2026.112980):

**May 2020 — COVID trough.** Headline inflation at 2.56% looked neutral, giving no clear policy signal. The decomposition showed supply-driven inflation at 2.39% and demand-driven inflation collapsed to 0.17% — a 93.4% supply share. This matched observable reality: global supply disruptions coexisted with Mexican GDP falling 8.5% in Q2 2020. Banco de México eased from 7.00% to 4.25% during 2020, correctly supporting collapsed demand while accepting that supply-driven inflation was beyond policy reach.

**September 2008 - March 2010 — Global Financial Crisis.** Headline inflation fell from 5.47% to around 3.8% over eighteen months. The decomposition attributes most of the decline to the demand component (3.12% to 1.84%) while supply-driven inflation fell less (2.35% to 1.92%). Food drove the demand-side collapse as households cut discretionary spending, consistent with the food-dominance pattern. Banco de México's delayed easing — holding at 8.25% through late 2008 despite weakening demand — appears suboptimal in hindsight; the demand component had already begun falling by October 2008.

**June-July 2024 — the disinflation head-fake.** Headline inflation had fallen from 8.11% to 4.70% by June 2024, and markets priced in further cuts. The decomposition told a different story: demand-driven inflation stood at 2.53%, above its long-run average of 2.06%, while the supply component at 2.17% was doing most of the work. The next month, headline jumped to 5.22% as the demand component rose to 3.32% — exactly what the decomposition would have forecast. Banco de México held at 11.00% through the June 27 meeting and resumed cutting only in August.

The goods-services divergence over 2023-2024 completes the picture. [Goods inflation fell 5.06 percentage points driven by supply normalization (shipping costs, peso appreciation), while services inflation barely moved and the services demand component actually rose](https://doi.org/10.1016/j.econlet.2026.112980). This is the services floor in operation: external supply shocks pass through goods quickly, domestic demand in labor-intensive services does not.

---

## Data and Code

Paper landing page and PDF: [robinchen.org/publication/mexico-inflation-decomposition/](https://robinchen.org/publication/mexico-inflation-decomposition/). For inquiries about replication data, contact [zhengyang.chen@uni.edu](mailto:zhengyang.chen@uni.edu).

## Citation

Colunga-Ramos, Luis Fernando, Zhengyang Chen, and José Angel Perales. 2026. "Decomposing Supply and Demand Driven Inflation in Mexico: Evidence from Sectoral Analysis." *Economics Letters* 264: 112980. [https://doi.org/10.1016/j.econlet.2026.112980](https://doi.org/10.1016/j.econlet.2026.112980)

```bibtex
@article{colungaramos2026decomposing,
  title={Decomposing Supply and Demand Driven Inflation in Mexico: Evidence from Sectoral Analysis},
  author={Colunga-Ramos, Luis Fernando and Chen, Zhengyang and Perales, Jos{\'e} Angel},
  journal={Economics Letters},
  volume={264},
  pages={112980},
  year={2026},
  publisher={Elsevier},
  doi={10.1016/j.econlet.2026.112980}
}
```
