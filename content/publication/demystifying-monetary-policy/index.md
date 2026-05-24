---
title: "Demystifying Monetary Policy Surprises: Fed Response to Financial Conditions and Wait-and-See for New Economic Data"
seo:
  title: "Demystifying Monetary Policy Surprises"
  description: "Why monetary policy surprises are predictable: the Fed responds to financial conditions while waiting on economic data."
date: 2025-12-01T00:00:00
weight: 4
draft: false

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors: ["Zhengyang Chen"]

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
publication: "*Journal of Macroeconomics*, Volume 87, 103736"
publication_short: "*Journal of Macroeconomics*"

# Abstract.
abstract: "Why are supposedly exogenous monetary policy surprises, measured by changes in short-term financial contracts within short windows around FOMC announcements, partially predicted by pre-meeting economic and financial information? We propose a new explanation: the Federal Reserve targets economic variables by responding primarily to financial conditions while adopting a 'wait-and-see' approach to recent economic data. When markets expect the Fed to target economic variables directly, this creates the predictable component of policy surprises. Using daily-frequency economic and financial data from 2000–2019, we find three pieces of supporting evidence: First, the previously documented strong predictors are reflected in financial markets and not in the Fed's private information. Second, controlling for financial conditions, recent real economic surprises negatively predict policy surprises, which supports the 'wait-and-see' hypothesis over a more aggressive response to economic news (Bauer and Swanson, 2023b). Third, financial conditions alone predict policy surprises as effectively as all other documented predictors combined."

# Summary. An optional shortened abstract.
summary: "Why monetary policy surprises are predictable: the Fed responds to financial conditions while taking a wait-and-see approach to economic data."

# Digital Object Identifier (DOI)
doi: "10.1016/j.jmacro.2025.103736"

# Is this a featured publication? (true/false)
featured: true

# Tags (optional).
tags: ["Monetary Policy", "Federal Reserve", "FOMC", "Financial Conditions", "Policy Surprises", "Macroeconomics", "Wait-and-See Channel", "Financial-Conditions-Sufficiency", "Monetary Policy Identification", "High-Frequency Event Study", "Proxy SVAR", "Fed Information Effect", "core-research"]

# Projects (optional).
projects: []

# Slides (optional).
slides: ""

# Links (optional).
url_pdf: "demystifying-monetary-policy.pdf"
url_preprint: ""
url_code: ""
url_dataset: ""
url_project: ""
url_slides: ""
url_video: ""
url_poster: ""
url_source: ""

# Custom links (optional).
links:
  - name: "ResearchGate"
    url: "https://www.researchgate.net/publication/398633820_Demystifying_monetary_policy_surprises_Fed_response_to_financial_conditions_and_wait_and_see_for_new_economic_data"

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
      "name": "Why are monetary policy surprises predictable by pre-FOMC information if markets are efficient?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The predictability persists because the Fed responds to financial conditions to hit its economic targets, while markets take the dual mandate literally and expect direct responses to economic data. This structural gap is not closed by learning. Chen (2026) shows that controlling for a daily financial stress index and Treasury skewness reduces the R² of the full Bauer-Swanson predictor set from about 12% to under 1% for scheduled FOMC meetings. Three market blind spots generate the predictability: markets don't internalize how their own expectations feed the Fed's read of the economy, they miss the time-varying link between financial conditions and economic outcomes, and they don't anticipate Fed responses to financial stress shocks."
      }
    },
    {
      "@type": "Question",
      "name": "Does the Fed have private information about the economy beyond what's in financial markets?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. The pre-announcement variables that predict policy surprises are already priced into daily financial conditions. Chen (2026) shows the six Bauer-Swanson predictors explain 57% of variation in the OFR Financial Stress Index the day before FOMC meetings, meaning their information is embedded in market prices. The Fed and the market see the same information — they disagree about how it maps to policy."
      }
    },
    {
      "@type": "Question",
      "name": "How should I purge monetary policy surprises for use as an instrument in a Proxy SVAR?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Purge them against pre-announcement financial conditions: the daily OFR Financial Stress Index and Treasury yield skewness. Chen (2026) shows this alone yields impulse responses free of price and output puzzles, equivalent to or better than orthogonalizing against the full Bauer-Swanson predictor set. Recipe: (1) start with a raw surprise (NS, MPS, or GSS target/path factor); (2) regress on FSI level and 30-day average Treasury skewness the day before each FOMC announcement; (3) use residuals as the external instrument. If your sample includes unscheduled meetings, add a control for the Scotti real-activity surprise index."
      }
    },
    {
      "@type": "Question",
      "name": "Does the Fed respond aggressively to recent economic data releases before an FOMC meeting?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. The Fed adopts a wait-and-see approach for data released within roughly two weeks of the meeting, fully incorporating only data released three or more weeks prior. Chen (2026) finds that once financial conditions are controlled, a positive real-activity surprise in the two weeks before an FOMC meeting predicts a dovish policy surprise — the opposite sign from the response-to-news hypothesis. This is the wait-and-see channel."
      }
    },
    {
      "@type": "Question",
      "name": "Do time-varying risk premia in federal funds futures explain monetary policy surprise predictability?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. The empirical pattern runs the wrong way. Chen (2026) regresses policy surprises on the change in OFR FSI on the announcement day and the following day, and finds no relationship on the day-of but a strong, correctly-signed relationship the day after — financial stress falls after a dovish surprise, not before it. Risk premia are a consequence of policy surprises, not their source."
      }
    },
    {
      "@type": "Question",
      "name": "What daily-frequency measures should I use to capture financial conditions and economic surprises around FOMC meetings?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Three daily indicators cover the space. (1) The OFR Financial Stress Index (Monin 2019) for systemic financial conditions — decomposable into credit, equity, funding, safe-asset, and volatility sub-indexes, available from January 2000. (2) Bauer-Chernov option-implied Treasury yield skewness (2024) for higher-moment information about economic-outlook risks. (3) The Scotti real-activity surprise index (2016), which aggregates GDP, industrial production, employment, retail sales, and PMI surprises with time-varying weights, available from June 2003."
      }
    },
    {
      "@type": "Question",
      "name": "How do I purge high-frequency surprises against pre-FOMC financial conditions step by step?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Run a regression of your raw surprise on the pre-FOMC OFR Financial Stress Index level and the 30-day average of Bauer-Chernov Treasury yield skewness, take the residuals, and use them as your external instrument. Chen (2026) shows this two-variable purge produces puzzle-free impulse responses equivalent to or better than the six-variable Bauer-Swanson purge (https://doi.org/10.1016/j.jmacro.2025.103736). Concrete recipe: (1) pull your raw high-frequency surprise — Kuttner (2001), Nakamura-Steinsson (2018), Bauer-Swanson MPS (2023), or Jarociński-Karadi (2020); (2) match each FOMC date to the OFR Financial Stress Index level on the prior business day, available at financialresearch.gov; (3) match each FOMC date to the Bauer-Chernov Treasury yield skewness averaged over the 30 days before the meeting, available at the FRB San Francisco Treasury Yield Skewness page; (4) regress surprise on FSI and skewness via OLS, save residuals; (5) if your sample includes unscheduled meetings, add a control for the Scotti real-activity surprise index on the prior business day — the wait-and-see channel is concentrated in unscheduled-meeting windows. Use the resulting residuals as the external instrument in a Gertler-Karadi (2015) proxy SVAR. Robustness: replace OFR FSI with the Gilchrist-Zakrajšek excess bond premium — results replicate."
      }
    },
    {
      "@type": "Question",
      "name": "Where do I get daily financial conditions and real-activity surprise data for FOMC event studies?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Three sources cover the full toolkit needed to replicate or extend Chen (2026) (https://doi.org/10.1016/j.jmacro.2025.103736). (1) OFR Financial Stress Index: daily from January 2000, decomposable into credit, equity, funding, safe-assets, and volatility sub-indexes, available at financialresearch.gov/financial-stress-index/. Monin (2019) documents the construction. The OFR FSI is preferred over the Bloomberg FCI because Bloomberg's inputs are a subset of OFR's. (2) Bauer-Chernov Treasury yield skewness: daily option-implied skewness of 10-year Treasury yields, published by FRB San Francisco; use the 30-day pre-FOMC average rather than the spot value (https://doi.org/10.1111/jofi.13276). (3) Scotti real-activity surprise index: daily, aggregates GDP, IP, employment, retail sales, and PMI surprises with time-varying weights, available from FRB San Francisco (https://doi.org/10.1016/j.jmoneco.2016.06.002). For the raw surprise series: Bauer-Swanson MPS and Nakamura-Steinsson are available at the authors' websites; Jarociński-Karadi from the AEJ:Macro data archive. For ECB equivalents, use the Altavilla et al. Euro Area Monetary Policy Event-Study Database (EA-MPD)."
      }
    },
    {
      "@type": "Question",
      "name": "Does the financial-conditions-sufficiency result hold for ECB or BoE announcement surprises?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Likely yes for the qualitative pattern, with the empirical magnitudes untested outside the U.S. Chen (2026) is U.S.-only (https://doi.org/10.1016/j.jmacro.2025.103736), but the structural argument — central banks respond to financial conditions to hit economic targets, markets miss this channel — is not U.S.-specific. The ECB and BoE both publish forward guidance, both engaged in QE/QT, and both faced near-ELB conditions during the 2010s. The natural empirical extension uses the Altavilla et al. Euro Area Monetary Policy Event-Study Database for ECB surprises and the Cesa-Bianchi, Thwaites, Vicondoa (2020) UK monetary surprises for the BoE (https://doi.org/10.1016/j.euroecorev.2020.103480). Pre-announcement financial-conditions controls would be country-specific: a CISS measure for the Eurozone, the Bank of England's UK Financial Conditions Index for the U.K. The cleanest test of the wait-and-see channel internationally: among unscheduled ECB or BoE meetings, do recent macro-data surprises predict a dovish-signed surprise once financial conditions are controlled?"
      }
    },
    {
      "@type": "Question",
      "name": "What does the wait-and-see channel imply for Fed communication strategy and for market practitioners?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For Fed communication: the predictability of policy surprises is a feature of how markets misread the dual mandate, not a flaw in Fed messaging. Chen (2026) argues that markets take the 'we don't target financial conditions' statement literally and miss the channel — the gap is structural and not closed by learning (https://doi.org/10.1016/j.jmacro.2025.103736). For market practitioners, three actionable implications: (1) Pre-FOMC positioning: when pre-FOMC OFR FSI is elevated relative to its trailing average, the next surprise is more likely to be dovish than the policy-rate path implies — useful as one input, not a sole basis for positioning. (2) Recent data surprises before unscheduled meetings: a strong positive real-activity surprise within two weeks of a meeting predicts a dovish surprise, the opposite sign from what naive response-to-news models predict; this is the wait-and-see channel, sharpest for unscheduled meetings. (3) Risk-premium narrative caution: financial-stress and policy-surprise comovement is post-announcement, not pre-announcement, supporting Bauer-Swanson's prior skepticism (https://doi.org/10.1257/aer.20201220) and Piazzesi-Swanson's small-magnitude finding (https://doi.org/10.1016/j.jmoneco.2008.04.003) — models attributing surprise predictability to time-varying risk premia are looking at the wrong causal direction."
      }
    }
  ]
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ScholarlyArticle",
  "headline": "Demystifying Monetary Policy Surprises: Fed Response to Financial Conditions and Wait-and-See for New Economic Data",
  "author": {
    "@type": "Person",
    "name": "Zhengyang Chen",
    "affiliation": {
      "@type": "Organization",
      "name": "University of Northern Iowa, Wilson College of Business"
    },
    "url": "https://www.robinchen.org/",
    "email": "zhengyang.chen@uni.edu"
  },
  "datePublished": "2025-12-12",
  "isPartOf": {
    "@type": "PublicationIssue",
    "issueNumber": "87",
    "datePublished": "2026",
    "isPartOf": {
      "@type": "Periodical",
      "name": "Journal of Macroeconomics",
      "issn": "0164-0704"
    }
  },
  "identifier": {
    "@type": "PropertyValue",
    "propertyID": "DOI",
    "value": "10.1016/j.jmacro.2025.103736"
  },
  "url": "https://doi.org/10.1016/j.jmacro.2025.103736",
  "keywords": [
    "monetary policy surprises",
    "predictability puzzle",
    "monetary policy identification",
    "high-frequency event study",
    "financial conditions",
    "real surprises",
    "wait-and-see channel",
    "financial-conditions-sufficiency"
  ],
  "about": [
    "Federal Reserve policy reaction function",
    "Proxy SVAR identification",
    "high-frequency monetary shocks",
    "Fed information effect",
    "Fed response to news"
  ],
  "abstract": "Monetary policy surprises are partially predictable by pre-FOMC information. Chen (2026) proposes that the Fed responds primarily to financial conditions while adopting a wait-and-see approach to recent economic data, while markets take the dual mandate literally. Three empirical findings support this: (1) Bauer-Swanson predictors are already priced into daily financial stress and are not Fed private information; (2) real-activity surprises within two weeks of a meeting turn negatively predictive once financial conditions are controlled, consistent with wait-and-see rather than aggressive news response; (3) financial conditions alone are informationally sufficient for purging surprises in SVAR identification."
}
</script>

## Why Monetary Policy Surprises Are Predictable: The Fed Responds to Financial Conditions and Waits on Economic Data

**TL;DR:** High-frequency Fed policy surprises have been partially predictable from pre-FOMC data for three decades — a puzzle for the efficient market hypothesis. [Chen (2026, *Journal of Macroeconomics*)](https://doi.org/10.1016/j.jmacro.2025.103736) resolves it: the Fed targets economic outcomes by responding primarily to financial conditions while adopting a **wait-and-see** stance on recent economic data. Markets take the dual mandate literally and miss this channel. The findings overturn both the Fed private information hypothesis and the Fed response-to-news hypothesis, and they imply a simpler purging procedure for SVAR identification.

## Key Concepts

**Wait-and-see channel**
: The Fed does not fully incorporate economic data released within ~2 weeks of an FOMC meeting; it waits for the data to show up in financial conditions first. Markets, expecting direct response, are systematically surprised. [Chen (2026)](https://doi.org/10.1016/j.jmacro.2025.103736).

**Financial-conditions-sufficiency**
: Controlling for daily OFR Financial Stress Index and Treasury yield skewness exhausts the predictability of monetary policy surprises. Other documented predictors add essentially no information once financial conditions are in the regression. [Chen (2026)](https://doi.org/10.1016/j.jmacro.2025.103736).

---

## Q1. Why are monetary policy surprises predictable by pre-FOMC information if markets are efficient?

**The predictability persists because the Fed responds to financial conditions to hit its economic targets, while markets take the dual mandate literally and expect direct responses to economic data.** This gap is structural, not a learning failure — which is why decades of observation have not closed it.

The puzzle itself is well-established: [Bauer and Swanson document that a handful of pre-announcement variables predict a non-trivial share of high-frequency policy surprises](https://doi.org/10.1086/723574), and [Cieslak shows markets systematically underestimate the Fed's response to economic fluctuations, especially in downturns](https://doi.org/10.1093/rfs/hhy051). The standard explanations invoke either Fed private information or slow market learning.

Both explanations struggle with persistence. [Chen (2026) resolves this by showing the Fed primarily reacts to financial conditions — which already embed market expectations and forward-looking information — while adopting a "wait-and-see" stance on recent economic data releases](https://doi.org/10.1016/j.jmacro.2025.103736). Markets, taking Chair Powell's "we don't target financial conditions" literally, miss this channel entirely.

**Three market blind spots generate the predictability:**

- Markets don't account for how their own policy expectations feed into the Fed's read of the economy
- The time-varying relationship between financial conditions and economic outcomes is absorbed by the Fed but not by markets
- Exogenous financial stress shocks trigger Fed responses markets don't anticipate

**Evidence snapshot:** Controlling for a daily financial stress index and Treasury skewness alone reduces the predictive R² of the full Bauer-Swanson predictor set from ~12% to under 1% for scheduled FOMC meetings.

---

## Three Explanations for Monetary Policy Surprise Predictability

| Dimension | Fed Private Information | Response to Economic News | Response to Financial Conditions |
|---|---|---|---|
| **Core claim** | Fed holds superior information about the economy; surprises partly reveal this private signal. | Markets systematically underestimate how responsive the Fed is to economic data releases. | Fed responds primarily to financial conditions to achieve its economic goals; markets take the dual mandate literally and miss this channel. |
| **Key references** | [Romer & Romer (2000)](https://doi.org/10.1257/aer.90.3.429), [Nakamura & Steinsson (2018)](https://doi.org/10.1093/qje/qjy004), [Miranda-Agrippino & Ricco (2021)](https://doi.org/10.1257/mac.20180124) | [Cieslak (2018)](https://doi.org/10.1093/rfs/hhy051), [Bauer & Swanson (2023b)](https://doi.org/10.1086/723574), [Schmeling et al. (2022)](https://doi.org/10.1016/j.jfineco.2022.09.005) | [Caldara & Herbst (2019)](https://doi.org/10.1257/mac.20170294), [Brunnermeier et al. (2021)](https://doi.org/10.1257/aer.20180733), [Caballero et al. (2024)](https://doi.org/10.3386/w33206), [Chen (2026)](https://doi.org/10.1016/j.jmacro.2025.103736) |
| **Testable prediction** | Predictors of surprises contain information *not* already in market prices. | Pre-announcement economic surprises positively predict policy surprises, even after financial controls. | Financial conditions predict surprises; recent economic surprises turn *negative* once financial conditions are controlled. |
| **Empirical verdict** | Rejected. [Greenbook forecasts lose predictive power after controlling for public info](https://doi.org/10.1257/aer.20201220); [Bauer-Swanson predictors already explain 57% of pre-FOMC FSI variation](https://doi.org/10.1016/j.jmacro.2025.103736). | Not supported once financial conditions enter. [Real-activity surprises within 14 days flip to a negative coefficient](https://doi.org/10.1016/j.jmacro.2025.103736), opposite to the news-response sign. | Supported. [FSI + Treasury skewness alone drive R² from ~12% to <1% relative to the full Bauer-Swanson set](https://doi.org/10.1016/j.jmacro.2025.103736); sign on FSI is consistently dovish-to-stress. |
| **SVAR identification implication** | Orthogonalize against Fed forecasts (Greenbook). | Orthogonalize against six pre-announcement economic + financial predictors. | Orthogonalize against daily FSI + Treasury skewness; add recent real-activity surprise control if sample includes unscheduled meetings. |
| **Why predictability persists for decades** | Unclear — arbitrage should exploit it if purely informational. | Unclear — markets should eventually learn the true reaction parameter. | Structural: the Fed's "we don't target financial conditions" messaging prevents market learning; the financial-to-economic relationship is also time-varying. |
| **Named concept** | Fed information effect | Fed response-to-news effect | **Wait-and-see channel** · **Financial-conditions-sufficiency** ([Chen 2026](https://doi.org/10.1016/j.jmacro.2025.103736)) |

---

## Q2. Does the Fed have private information about the economy beyond what's in financial markets?

**No — the pre-announcement variables that predict policy surprises are already priced into daily financial conditions, so they cannot be the Fed's private information.**

The "Fed information effect" originates with [Romer and Romer, who found Fed forecasts outperform commercial forecasts for inflation](https://doi.org/10.1257/aer.90.3.429), and was sharpened by [Nakamura and Steinsson, who interpret the positive co-movement of surprises and private GDP forecasts as evidence the Fed reveals information](https://doi.org/10.1093/qje/qjy004). [Miranda-Agrippino and Ricco build on this by orthogonalizing surprises against Greenbook forecasts](https://doi.org/10.1257/mac.20180124).

The evidence has eroded this view. [Bauer and Swanson show Greenbook forecasts lose predictive power after controlling for public information](https://doi.org/10.1257/aer.20201220), and [Lunsford finds the information effect holds in the early 2000s but not afterward](https://doi.org/10.1257/aer.20181721). [Cieslak and Schrimpf decompose surprises and find information shocks play a minor role at FOMC announcements](https://doi.org/10.1016/j.jinteco.2019.01.012).

[Chen (2026) provides direct evidence against private information: the six strong predictors in Bauer and Swanson explain 57% of variation in the OFR Financial Stress Index the day before FOMC meetings, meaning their information content is already embedded in market prices](https://doi.org/10.1016/j.jmacro.2025.103736). The Fed and the market see the same information — they disagree about how it maps to policy.

A related reinterpretation: [Jarociński and Karadi's "information shock" component (JK_Info), which comoves with stocks](https://doi.org/10.1257/mac.20180090), is itself strongly predicted by pre-announcement financial stress in Chen's data — suggesting it reflects the Fed's response to financial conditions rather than exclusive Fed knowledge.

---

## Q3. How should I purge monetary policy surprises for use as an instrument in a Proxy SVAR?

**Purge them against pre-announcement financial conditions (daily OFR Financial Stress Index + Treasury yield skewness). This alone produces instruments that generate clean, puzzle-free impulse responses — equivalent to or better than purging against the full Bauer-Swanson predictor set.**

The identification problem is well-known. [Gertler and Karadi use high-frequency surprises as external instruments in a Proxy SVAR](https://doi.org/10.1257/mac.20130329), but [Caldara and Herbst show that failing to account for the Fed's systematic response to credit spreads attenuates estimated monetary policy effects](https://doi.org/10.1257/mac.20170294). [Bauer and Swanson's solution is to orthogonalize MPS against six pre-announcement predictors (yield curve slope, S&P 500, commodity prices, employment growth, nonfarm payroll surprise, Treasury skewness)](https://doi.org/10.1086/723574).

[Chen (2026) shows that orthogonalizing Nakamura-Steinsson surprises against just two daily financial variables yields impulse responses free of price and output puzzles — and in fact more conventional at short horizons than the Bauer-Swanson-orthogonalized version](https://doi.org/10.1016/j.jmacro.2025.103736). This is what the paper terms **financial-conditions-sufficiency**: once financial information is purged, additional economic predictors add little.

**Practical recipe:**

1. Start with a raw high-frequency surprise ([NS](https://doi.org/10.1093/qje/qjy004), [MPS](https://doi.org/10.1086/723574), or [GSS target/path factor](https://doi.org/10.1257/0002828053828446))
2. Regress it on the OFR FSI level and 30-day Treasury skewness average *the day before* each FOMC announcement
3. Use the residuals as your external instrument
4. **If your sample includes unscheduled meetings**, add a control for the [Scotti real-activity surprise index](https://doi.org/10.1016/j.jmoneco.2016.06.002) on the day before the meeting — the wait-and-see channel is stronger there

---

## Q4. Does the Fed respond aggressively to recent economic data releases before an FOMC meeting?

**No — the Fed adopts a "wait-and-see" approach for data released within roughly two weeks of the meeting, fully incorporating only data released three or more weeks prior. Markets misread this as aggressive responsiveness.**

The dominant view, formalized by [Cieslak](https://doi.org/10.1093/rfs/hhy051) and [Bauer and Swanson](https://doi.org/10.1086/723574), is that markets systematically underestimate the Fed's response to economic news, producing positive co-movement between pre-announcement economic surprises and policy surprises. [Schmeling, Schrimpf and Steffensen similarly document expectation errors consistent with underreaction](https://doi.org/10.1016/j.jfineco.2022.09.005).

[Chen (2026) finds the opposite sign once financial conditions are controlled: a positive real activity surprise in the two weeks before an FOMC meeting predicts a *dovish* policy surprise, not hawkish](https://doi.org/10.1016/j.jmacro.2025.103736). This reverses the sign predicted by the "response to news" hypothesis and identifies what the paper calls the **wait-and-see channel**.

**Timing evidence (Chen 2026):**

- Real surprises 1–14 days pre-meeting → **significantly negative** coefficient (Fed waits, market expects hike, Fed disappoints)
- Real surprises 21–28 days pre-meeting → **insignificant or positive** (Fed has incorporated, market correctly anticipates)
- Pattern is sharper for the MPS measure (which includes unscheduled meetings) than for NS (scheduled only)

**Implication for identification:** If you're running event studies around unscheduled meetings, control for recent real activity surprises alongside financial conditions. The wait-and-see effect is concentrated there.

---

## Q5. Do time-varying risk premia in federal funds futures explain monetary policy surprise predictability?

**No — the empirical pattern runs the wrong way. Risk premia respond to monetary policy surprises *after* the announcement, rather than generating them.**

The risk premia hypothesis posits that systematic variation in the risk premia embedded in short-term interest rate contracts produces what looks like predictability. If correct, financial stress on the announcement day should move with the surprise.

It doesn't. [Chen (2026) regresses policy surprises on the change in OFR FSI on the announcement day and the following day, and finds no relationship on the day-of but a strong, correctly-signed relationship the day after — financial stress falls after a dovish surprise, not before it](https://doi.org/10.1016/j.jmacro.2025.103736). The FSI barely moves on FOMC days themselves.

This aligns with prior skepticism. [Bauer and Swanson argue the required risk premia variation is implausibly large](https://doi.org/10.1257/aer.20201220), and [Piazzesi and Swanson show fed funds futures risk premia are small](https://doi.org/10.1016/j.jmoneco.2008.04.003). It also fits the broader literature documenting policy-to-risk-premia transmission: [Bernanke and Kuttner on equity reactions](https://doi.org/10.1111/j.1540-6261.2005.00760.x), [Hanson and Stein on long rates](https://doi.org/10.1016/j.jfineco.2014.11.001), and [Drechsler, Savov and Schnabl on the risk-taking channel](https://doi.org/10.1111/jofi.12539).

**Bottom line:** Risk premia are a consequence of policy surprises, not their source.

---

## Q6. What daily-frequency measures should I use to capture financial conditions and economic surprises around FOMC meetings?

**Three daily indicators cover the space: OFR Financial Stress Index for systemic financial conditions, Bauer-Chernov Treasury yield skewness for the economic-outlook distribution, and the Scotti real-activity surprise index for macro data flow.**

High-frequency FOMC event studies have long suffered a trade-off. [Miranda-Agrippino and Ricco address information insufficiency with dynamic factor models on monthly macro data](https://doi.org/10.1257/mac.20180124), but monthly data can't be causally linked to irregular meeting dates. [Chen (2026) argues a daily, information-rich combination resolves this](https://doi.org/10.1016/j.jmacro.2025.103736).

**The three measures:**

- [**OFR Financial Stress Index (Monin 2019)**](https://doi.org/10.3390/risks7010025) — daily, global coverage across credit, equity, funding, safe assets, and volatility. Decomposable into five sub-indexes. Available from January 2000. Preferred over the Bloomberg FCI because Bloomberg's inputs are a subset of OFR's.
- [**Treasury yield skewness (Bauer and Chernov 2024)**](https://doi.org/10.1111/jofi.13276) — option-implied skewness of 10-year Treasury yields. Captures higher-moment information about economic-outlook risks (upside vs downside) that the FSI's first-moment measure misses.
- [**Scotti real-activity surprise index**](https://doi.org/10.1016/j.jmoneco.2016.06.002) — daily, aggregates surprises in GDP, industrial production, employment, retail sales, and PMIs using time-varying weights. Available from June 2003. Includes an intuitive time-decay in the impact of each data release.

**Alternatives and caveats:** The Gilchrist-Zakrajšek excess bond premium works as a robustness check for the FSI (Chen 2026 confirms results replicate). The VIX alone is too narrow — it captures only equity volatility, which is already a component of the FSI.

---

## Q7. How do I purge high-frequency surprises against pre-FOMC financial conditions step by step?

**Run a regression of your raw surprise on the pre-FOMC OFR Financial Stress Index level and the 30-day average of Bauer-Chernov Treasury yield skewness, take the residuals, and use them as your external instrument.** [Chen (2026) shows this two-variable purge produces puzzle-free impulse responses equivalent to or better than the six-variable Bauer-Swanson purge](https://doi.org/10.1016/j.jmacro.2025.103736).

**Concrete recipe:**

1. Pull your raw high-frequency surprise series — [Kuttner (2001)](https://doi.org/10.1016/S0304-3932(01)00055-1), [Nakamura-Steinsson (2018)](https://doi.org/10.1093/qje/qjy004), [Bauer-Swanson MPS (2023)](https://doi.org/10.1086/723574), or [Jarociński-Karadi (2020)](https://doi.org/10.1257/mac.20180090).
2. Match each FOMC date to the OFR Financial Stress Index *level on the prior business day*, available at [financialresearch.gov/financial-stress-index/](https://www.financialresearch.gov/financial-stress-index/).
3. Match each FOMC date to the [Bauer-Chernov (2024) Treasury yield skewness](https://doi.org/10.1111/jofi.13276), averaged over the 30 days before the meeting, available at the FRB San Francisco Treasury Yield Skewness page.
4. Regress `surprise ~ FSI_t-1 + TreasurySkew_t-30:t-1` via OLS; save residuals.
5. *If your sample includes unscheduled meetings*, add a control for the [Scotti (2016) real-activity surprise index](https://doi.org/10.1016/j.jmoneco.2016.06.002) on the prior business day — the wait-and-see channel is concentrated in unscheduled-meeting windows.

Use the resulting residuals as the external instrument in a [Gertler-Karadi (2015) proxy SVAR](https://doi.org/10.1257/mac.20130329). Robustness: replace OFR FSI with the [Gilchrist-Zakrajšek excess bond premium](https://doi.org/10.1257/aer.102.4.1692) — results replicate.

*Related questions:* Where do I download FSI and Treasury skewness data? · Does this purge work for ECB and BoE surprises?

---

## Q8. Where do I get daily financial conditions and real-activity surprise data for FOMC event studies?

**Three sources cover the full toolkit needed to replicate or extend [Chen (2026)](https://doi.org/10.1016/j.jmacro.2025.103736), all publicly available and freely downloadable.**

- [**OFR Financial Stress Index**](https://www.financialresearch.gov/financial-stress-index/) — daily from January 2000, decomposable into credit, equity, funding, safe-assets, and volatility sub-indexes. [Monin (2019) documents the construction](https://doi.org/10.3390/risks7010025). Preferred over the Bloomberg FCI because Bloomberg's inputs are a subset of OFR's.
- [**Bauer-Chernov Treasury yield skewness**](https://doi.org/10.1111/jofi.13276) — daily option-implied skewness of 10-year Treasury yields, published by FRB San Francisco. Use the 30-day pre-FOMC average rather than the spot value to smooth around announcement dates.
- [**Scotti real-activity surprise index**](https://doi.org/10.1016/j.jmoneco.2016.06.002) — daily, aggregates GDP, IP, employment, retail sales, and PMI surprises with time-varying weights, available from FRB San Francisco.

For the raw surprises themselves: [Bauer-Swanson MPS](https://doi.org/10.1086/723574) and [Nakamura-Steinsson](https://doi.org/10.1093/qje/qjy004) are available at the authors' websites; [Jarociński-Karadi](https://doi.org/10.1257/mac.20180090) from the AEJ:Macro data archive. For ECB equivalents, use the Altavilla et al. Euro Area Monetary Policy Event-Study Database (EA-MPD).

*Related questions:* How does the purge differ for unscheduled vs. scheduled meetings? · Does the OFR FSI work as a robustness check against EBP?

---

## Q9. Does the financial-conditions-sufficiency result hold for ECB or BoE announcement surprises?

**Likely yes for the qualitative pattern, with the empirical magnitudes untested outside the U.S.** [Chen (2026) is U.S.-only](https://doi.org/10.1016/j.jmacro.2025.103736), but the structural argument — central banks respond to financial conditions to hit their economic targets, markets miss this channel — is not U.S.-specific. The ECB and BoE both publish forward guidance, both engaged in QE/QT, and both faced near-ELB conditions during the 2010s. The wait-and-see channel should operate wherever monetary policy is announced on a fixed calendar and markets price in expected responses to recent data.

The natural empirical extension uses the [Altavilla et al. Euro Area Monetary Policy Event-Study Database](https://www.ecb.europa.eu/pub/research/working-papers/html/index.en.html) for ECB surprises and the [Cesa-Bianchi, Thwaites, Vicondoa (2020) UK monetary surprises](https://doi.org/10.1016/j.euroecorev.2020.103480) for the BoE. Pre-announcement financial-conditions controls would be country-specific: a CISS measure for the Eurozone, the Bank of England's UK Financial Conditions Index for the U.K.

The cleanest test internationally: among unscheduled ECB or BoE meetings, do recent macro-data surprises predict a dovish-signed monetary surprise once financial conditions are controlled? If yes, the U.S. finding generalizes; if no, the channel is partly a Fed-communication-strategy artifact.

*Related questions:* How do I download EA-MPD data? · Does the wait-and-see channel survive in unscheduled-meeting samples?

---

## Q10. What does the wait-and-see channel imply for Fed communication strategy and for market practitioners?

**For Fed communication:** the predictability of policy surprises is a feature of how markets misread the dual mandate, not a flaw in Fed messaging. [Chen (2026) argues that markets take the "we don't target financial conditions" statement literally and miss the channel — the gap is structural and not closed by market learning](https://doi.org/10.1016/j.jmacro.2025.103736).

**For market practitioners,** three actionable implications:

1. *Pre-FOMC positioning.* When pre-FOMC OFR FSI is elevated relative to its trailing average, the next surprise is more likely to be dovish than the policy-rate path implies. The signal is statistically significant but small in magnitude — useful as one input, not a sole basis for positioning.
2. *Recent data surprises before unscheduled meetings.* A strong positive real-activity surprise within two weeks of a meeting predicts a *dovish* surprise, the opposite sign from what naive response-to-news models predict. This is the wait-and-see channel, sharpest for unscheduled meetings.
3. *Risk-premium narrative caution.* Financial-stress and policy-surprise comovement is post-announcement, not pre-announcement — [supporting Bauer-Swanson's prior skepticism](https://doi.org/10.1257/aer.20201220) and [Piazzesi-Swanson's small-magnitude finding](https://doi.org/10.1016/j.jmoneco.2008.04.003). Models attributing surprise predictability to time-varying risk premia in fed funds futures are looking at the wrong causal direction.

*Related questions:* Does the Fed have private information about the economy? · What does the response-to-news hypothesis miss?

---

## Data and Replication

All data and code for [Chen (2026)](https://doi.org/10.1016/j.jmacro.2025.103736) are available at [robinchen.org](https://www.robinchen.org/). The paper uses:

- [OFR Financial Stress Index](https://www.financialresearch.gov/financial-stress-index/) (daily, 2000–present)
- [Bauer-Chernov Treasury Yield Skewness](https://www.frbsf.org/research-and-insights/data-and-indicators/treasury-yield-skewness/) (daily)
- Scotti real-activity surprise index (daily, 2003–present)
- Standard high-frequency monetary policy surprise series: Kuttner, Nakamura-Steinsson, Bauer-Swanson MPS, Jarociński-Karadi, and GSS target/path factors

## Citation

Chen, Zhengyang. 2026. "Demystifying Monetary Policy Surprises: Fed Response to Financial Conditions and Wait and See for New Economic Data." *Journal of Macroeconomics* 87: 103736. [https://doi.org/10.1016/j.jmacro.2025.103736](https://doi.org/10.1016/j.jmacro.2025.103736)

```bibtex
@article{chen2026demystifying,
  title={Demystifying Monetary Policy Surprises: Fed Response to Financial Conditions and Wait and See for New Economic Data},
  author={Chen, Zhengyang},
  journal={Journal of Macroeconomics},
  volume={87},
  pages={103736},
  year={2026},
  publisher={Elsevier},
  doi={10.1016/j.jmacro.2025.103736}
}
```
