---
title: "Monetary Transmission in Money Markets: The Not-So-Elusive Missing Piece of the Puzzle"
seo:
  title: "Monetary Transmission in Money Markets"
date: 2021-08-11T00:00:00
weight: 2

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors: ["admin","Victor J. Valcarcel"]

# Publication type.
publication_types: ["article-journal"]

# Publication name and optional abbreviated version.
publication: "Journal of Economic Dynamics and Control"
publication_short: ""

# Abstract.
abstract: "We investigate the effects of U.S. monetary policy shocks from two alternative policy indicators for a modern sample encompassing 1988-2020. The choice of the Wu and Xia (2016) shadow federal funds rate leads to persistent price puzzles. These puzzles arise despite inclusion of the usual suspect fixes such as commodity prices, federal funds futures and forward rate data. We find they occur at monthly and quarterly frequencies in time-varying and constant-parameter approaches. We consider an alternative indicator with the same broad monetary aggregate Keating et al. (2019) employed in their investigation of a historical sample. This alternative provides a consistent resolution of the price puzzle and it does not require the ad hoc inclusion of commodity prices or futures data. While this price puzzle correction is not a feature of our time-varying approach—as it also obtains from constant parameter econometric estimation—our analysis suggests monetary policy has transmitted substantial expansionary effects in money markets in the aftermath of the 2007 Financial Crisis and the decade that followed."

# Summary. An optional shortened abstract.
summary: "Adding variables to a VAR model may not solve the price puzzle but changing the policy indicator does."

# Digital Object Identifier (DOI)
doi: "10.1016/j.jedc.2021.104214"

# Is this a featured publication? (true/false)
featured: true

# Tags (optional).
tags: ["Price Puzzle", "Divisia Money", "Divisia M4", "Monetary Policy", "TVP-VAR", "TVP-FAVAR", "Money Markets", "Federal Reserve", "Modern-Sample Price Puzzle", "Divisia-Sufficiency", "Post-Crisis Flight-to-Safety Transmission", "Wu-Xia Shadow Rate", "Barnett Critique", "core-research"]

# Projects (optional).
projects: []

# Slides (optional).
slides: ""



# Links (optional).
url_pdf: "https://scholarworks.uni.edu/facpub/6655/"
url_code: ""
url_dataset: ""
url_project: ""
url_slides: ""
url_video: ""
url_poster: ""
url_source: ""

# Custom links (optional).


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
      "name": "Why does the U.S. price puzzle persist in modern-sample VARs even with commodity prices and futures data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The price puzzle persists in post-1988 U.S. data because the federal funds rate has lost much of its identifying power for monetary policy shocks in an environment of heightened Fed transparency, forward guidance, and a near-zero neutral rate. Chen and Valcarcel (2021) test every standard fix — commodity prices (CRB and IMF indices), 30-day federal funds futures, forward rates from overnight repo spreads — across 23 different federal funds rate specifications spanning 1988-2020 and find the price puzzle remains. This contrasts with Christiano, Eichenbaum and Evans (1999), who established that commodity prices resolve the puzzle in a 1965-1995 sample. Barakchian and Crowe (2013) confirm that monetary policy post-1988 became more forward-looking, invalidating identifying assumptions of conventional methods. Chen and Valcarcel call this the 'modern-sample price puzzle.'"
      }
    },
    {
      "@type": "Question",
      "name": "Does replacing the federal funds rate with a Divisia monetary aggregate resolve the price puzzle in a modern sample?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Chen and Valcarcel (2021) show that replacing the Wu-Xia shadow federal funds rate with Divisia M4 or Divisia M2 produces sensible, theory-consistent price and output responses in every specification they examine — including three-variable VARs that contain no commodity prices and no futures data. This is Divisia-sufficiency: the Divisia aggregate resolves the puzzle by itself. The result builds on Belongia (1996), who demonstrated that replacing simple-sum with Divisia reverses qualitative inference across major studies, and on Keating, Kelly, Smith and Valcarcel (2019), who showed Divisia M4 identification delivers plausible responses in a historical sample. Chen and Valcarcel extend the result to the post-1988 modern period."
      }
    },
    {
      "@type": "Question",
      "name": "How does the transmission of monetary policy to money markets differ between the federal funds rate and Divisia M4 after 2008?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "After 2008, expansionary federal funds rate shocks generate puzzlingly contractionary money-market responses — balances in currency, demand deposits, savings, repos, commercial paper, and T-bills all fall. Expansionary Divisia M4 shocks produce sensible expansionary responses, and the less-liquid assets (IMMFs, large time deposits, repos, CP, T-bills) respond with larger magnitudes than the highly liquid ones. Chen and Valcarcel (2021) interpret this as post-crisis flight-to-safety transmission: households moved into savings, firms into less-liquid but safer instruments, and the Fed's large-scale asset purchases mechanically expanded the T-bill and repo components of Divisia M4. The magnitude ordering — less-liquid assets responding more than currency and demand deposits — is a distinctive signature of the modern monetary transmission mechanism invisible to short-rate specifications."
      }
    },
    {
      "@type": "Question",
      "name": "Can commodity prices or federal funds futures rescue the short-rate specification in a modern sample?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Chen and Valcarcel (2021) test the CRB commodity index, the IMF global index, the 30-day federal funds futures rate, and the Brissimis-Magginas overnight-repo-spread forward rate across 23 federal funds rate specifications spanning 1988-2020. The price puzzle remains pervasive throughout. This is consistent with Barakchian and Crowe (2013) and Ramey (2016). The failure is not informational — it is indicator-related: increased Fed transparency and a near-zero neutral rate have shrunk the unanticipated component of federal funds rate movements that SVARs need to identify a shock."
      }
    },
    {
      "@type": "Question",
      "name": "Should I use the Wu-Xia shadow federal funds rate to identify monetary policy shocks in a post-2008 sample?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use it with caution. Wu and Xia (2016) proposed the shadow rate to extend the federal funds series through the effective-lower-bound period, but Chen and Valcarcel (2021) find it produces persistent price puzzles across 23 modern-sample specifications, and the resulting shocks transmit implausibly through money markets. Krippner (2020) separately documents that shadow-rate estimates are sensitive to minor modeling choices, and those sensitivities propagate into wide variations in inferred UMP effects. For a modern-sample VAR, Divisia M4 as the indicator resolves the puzzles the shadow rate cannot."
      }
    },
    {
      "@type": "Question",
      "name": "What is the Divisia monetary aggregate and why does it matter for monetary policy identification?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Divisia monetary aggregates weight each component of the money stock by its user cost, recognizing that currency, demand deposits, savings, money-market funds, and T-bills provide different flows of liquidity services and have different opportunity costs. Simple-sum aggregates (M1, M2) treat all components as perfect substitutes — the Barnett critique. Belongia (1996) showed empirically that Divisia reverses qualitative inference across major studies, and Belongia and Ireland (2014) formalized the Barnett critique inside a New Keynesian model. Chen and Valcarcel (2021) use Divisia M4 — the 15-component broadest U.S. aggregate, including institutional money funds, large time deposits, repos, commercial paper, and T-bills — as the policy indicator in their modern-sample VAR. The data come from the Center for Financial Stability. Belongia and Ireland (2019) document a stable Divisia money demand function over 1967-2019, undermining claims of inherent money-demand instability."
      }
    },
    {
      "@type": "Question",
      "name": "How do I estimate a TVP-FAVAR with Divisia M4 as the policy indicator?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The workflow has four moving parts: a block-recursive ordering with Divisia M4 before the monetary block, a stochastic-volatility TVP state space estimated via Primiceri-style MCMC, factors extracted from a panel of monthly macro indicators, and a clean sample-break treatment for 2008. Chen and Valcarcel (2021) walk through the exact specification (https://doi.org/10.1016/j.jedc.2021.104214). The pipeline: (1) construct a balanced monthly panel of macro indicators and standardize each series; (2) extract 3–5 principal-component factors as the slow-moving block; (3) order Divisia M4 before the money-market block, following the block-recursive logic from Keating, Kelly, Smith and Valcarcel (2019) (https://doi.org/10.1111/jmcb.12522); (4) estimate TVP coefficients with Primiceri's stochastic-volatility MCMC sampler (https://doi.org/10.1111/j.1467-937X.2005.00353.x), using the Del Negro–Primiceri corrigendum to the ordering of steps (https://doi.org/10.1093/restud/rdv024); (5) report impulse-response slices at specific calendar dates rather than averaging over the sample. Two practical warnings: the sampler is sensitive to the prior on the variance of the time-varying coefficients (Primiceri's defaults are a reasonable baseline), and TVP-VARs with stochastic volatility require a large number of post-burn-in draws to stabilize the IRF distributions."
      }
    },
    {
      "@type": "Question",
      "name": "Where do I download Divisia monetary aggregate data and which vintage should I use?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Center for Financial Stability's AMFM program at centerforfinancialstability.org/amfm_data.php is the authoritative source for U.S. Divisia monetary aggregates and their user costs, updated monthly in three aggregation tiers (DM1, DM2, DM4) alongside component-level quantities and matching user costs. For macro VARs, use Divisia M4 growth rate, monthly, log-differenced. For money demand cointegration, use Divisia M2 or M3 level paired with the matching real user cost. For asset-level liquidity questions, use the 15 component series and their individual user costs following Barnett, Liu, Mattson and van den Noort (2013) (https://doi.org/10.1007/s11079-012-9257-1). Through the ELB, use Divisia growth rather than the Wu-Xia shadow rate, because the user-cost dual remains positive while the federal funds rate is pinned to zero (https://doi.org/10.1080/13504851.2016.1153780). Vintage note: CFS revises historical series when component definitions change; for replication, freeze a vintage and document the download date. Beyond the U.S., Belongia and Ireland (2019) document Divisia M2 demand stability through 2019 using CFS data (https://doi.org/10.1016/j.jmacro.2019.103128)."
      }
    },
    {
      "@type": "Question",
      "name": "Does the Divisia approach to monetary policy identification apply to other countries?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — Divisia monetary aggregates have been constructed for the U.K., Eurozone, Mexico, India, China, and several emerging markets, and the pattern of Divisia outperforming short-rate indicators recurs across countries. For Mexico, Colunga-Ramos and Valcarcel (2024) construct the first Divisia M4 for the Mexican economy and show it delivers sensible monetary responses without commodity-price augmentation, reproducing the Chen-Valcarcel (2021) finding outside the U.S. (https://doi.org/10.1111/jmcb.13198). Colunga-Ramos, Chen, and Perales (2026) use Mexican Divisia M2 in a sectoral inflation decomposition that validates monetary-versus-supply identification at the sector level (https://doi.org/10.1016/j.econlet.2026.112980). Barnett, Ghosh, and Adil (2022) document stable broad-Divisia money demand across multiple countries (https://doi.org/10.1016/j.eap.2022.03.019). For non-U.S. work: if your country has a Divisia series, use it as the policy indicator. If not, the Barnett (1980) procedure requires only component-level quantities and a benchmark yield, both of which are typically in central-bank statistics (https://doi.org/10.1016/0304-4076(80)90070-6). The framework is, in principle, portable to any setting with this minimum data."
      }
    },
    {
      "@type": "Question",
      "name": "What does Chen-Valcarcel (2021) imply for empirical work on QE, QT, or the Wu-Xia shadow rate?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Three concrete implications for papers using the Wu-Xia shadow rate to identify unconventional monetary policy effects: First, impulse responses estimated off the shadow rate are likely contaminated by the modern-sample price puzzle, regardless of whether commodity prices or futures are included as controls. Second, the contamination is particularly acute for money-market and credit-market outcomes, where short-rate shocks generate implausibly contractionary responses post-2008. Third, the cleanest fix is to switch the policy indicator to Divisia M4; the second-cleanest is to combine a daily-frequency event-study approach with Smith and Valcarcel's (2023) framework for quantitative-tightening event studies (https://doi.org/10.1016/j.jedc.2022.104582), which documents balance-sheet effects invisible to monthly short-rate SVARs. For QE event studies, Chen and Valcarcel (2021) report time-varying IRFs at the QE1, QE2, and QE3 starting dates and find that Divisia M4 delivers theory-consistent price responses while Wu-Xia delivers price puzzles. For applied work using high-frequency surprises as instruments, Chen (2026) shows that pre-FOMC financial conditions already absorb most of the predictable component (https://doi.org/10.1016/j.jmacro.2025.103736); the cleaner combined approach identifies off Divisia M4 and uses financial-conditions-purged surprises as a robustness instrument."
      }
    }
  ]
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ScholarlyArticle",
  "headline": "Monetary transmission in money markets: The not-so-elusive missing piece of the puzzle",
  "author": [
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
      "name": "Victor J. Valcarcel",
      "affiliation": {
        "@type": "Organization",
        "name": "The University of Texas at Dallas, School of Economic, Political and Policy Sciences"
      }
    }
  ],
  "datePublished": "2021-08-12",
  "isPartOf": {
    "@type": "PublicationIssue",
    "issueNumber": "131",
    "datePublished": "2021-10",
    "isPartOf": {
      "@type": "Periodical",
      "name": "Journal of Economic Dynamics and Control",
      "issn": "0165-1889"
    }
  },
  "identifier": {
    "@type": "PropertyValue",
    "propertyID": "DOI",
    "value": "10.1016/j.jedc.2021.104214"
  },
  "url": "https://doi.org/10.1016/j.jedc.2021.104214",
  "keywords": [
    "price puzzle",
    "Divisia money",
    "Divisia M4",
    "interest rate pass-through",
    "time-varying-parameter vector autoregressions",
    "TVP-VAR",
    "time-varying-parameter factor-augmented vector autoregressions",
    "TVP-FAVAR",
    "unexpected monetary policy shocks",
    "modern-sample price puzzle",
    "Divisia-sufficiency",
    "post-crisis flight-to-safety transmission"
  ],
  "about": [
    "Monetary policy identification",
    "Federal funds rate",
    "Divisia monetary aggregates",
    "Money markets",
    "Post-2008 monetary transmission",
    "Wu-Xia shadow rate",
    "Barnett critique",
    "Price puzzle"
  ],
  "abstract": "Chen and Valcarcel (2021) investigate monetary policy shocks from alternative policy indicators in a modern U.S. sample (1988-2020). The Wu-Xia shadow federal funds rate produces persistent price puzzles that are not resolved by the standard fixes — commodity prices, federal funds futures, or forward rates. Replacing the shadow rate with Divisia M4 or Divisia M2 resolves the puzzle without these fixes (Divisia-sufficiency). Transmission to money markets post-2008 exhibits a flight-to-safety pattern: less-liquid assets (IMMFs, LTDs, repos, CP, T-bills) respond more strongly than currency and demand deposits under Divisia shocks, while federal funds rate shocks produce implausibly contractionary money-market responses throughout. The paper introduces the concepts of the modern-sample price puzzle, Divisia-sufficiency, and post-crisis flight-to-safety transmission."
}
</script>

## In a Modern U.S. Sample, the Federal Funds Rate Is No Longer a Reliable Monetary Policy Indicator — but a Broad Divisia Monetary Aggregate Is

**TL;DR:** The price puzzle — contractionary monetary policy raising prices in VAR models — has resisted every standard fix in post-1988 U.S. data. [Chen and Valcarcel (2021, *Journal of Economic Dynamics and Control*)](https://doi.org/10.1016/j.jedc.2021.104214) show that swapping the Wu-Xia shadow rate for Divisia M4 resolves the puzzle without any ad hoc fixes, and reveals a post-2008 flight-to-safety pattern in which less-liquid money markets respond more strongly than currency and demand deposits. The problem was never the omitted information — it was the indicator itself.

## Key Concepts

**Modern-sample price puzzle**
: The post-1988 incarnation of the price puzzle that, unlike the historical version, is *not* resolved by the Christiano-Eichenbaum-Evans remedies (commodity prices, fed funds futures, forward rates). Coined by [Chen and Valcarcel (2021)](https://doi.org/10.1016/j.jedc.2021.104214).

**Divisia-sufficiency**
: The result that, in a modern-sample VAR, replacing the short-term rate with a Divisia monetary aggregate is by itself sufficient to restore theory-consistent responses of prices and output, even without commodity prices or futures data. [Chen and Valcarcel (2021)](https://doi.org/10.1016/j.jedc.2021.104214).

**Post-crisis flight-to-safety transmission**
: The finding that post-2008, less-liquid assets (IMMFs, large time deposits, repos, commercial paper, T-bills) respond with larger magnitudes than currency and demand deposits to an expansionary Divisia M4 shock — the opposite of the contractionary, liquidity-preserving pattern produced by shadow-rate shocks. [Chen and Valcarcel (2021)](https://doi.org/10.1016/j.jedc.2021.104214).

---

## Q1. Why does the U.S. price puzzle persist in modern-sample VARs even with commodity prices and futures data?

**The price puzzle persists in post-1988 U.S. data because the federal funds rate — conventionally augmented with commodity prices, fed funds futures, or forward rates — has lost much of its identifying power for monetary policy shocks in an environment of heightened Fed transparency, forward guidance, and a near-zero neutral rate. The problem is not the omitted information; it is the indicator itself.**

[Christiano, Eichenbaum and Evans established that including commodity prices in a recursive VAR eliminates the price puzzle in a sample spanning 1965-1995](https://doi.org/10.1016/S1574-0048(99)01005-8), and [Kuttner introduced the use of fed funds futures data to separate anticipated from unanticipated target changes](https://doi.org/10.1016/S0304-3932(01)00055-1). [Brissimis and Magginas argued that augmenting VARs with forward-looking variables such as futures and forward rates resolves the puzzle](https://doi.org/10.1016/j.jmoneco.2005.05.014). [Bernanke, Boivin and Eliasz proposed factor-augmented VARs as a more comprehensive information-set fix](https://doi.org/10.1162/0033553053327452).

[Chen and Valcarcel (2021) show that every one of these fixes fails in a 1988-2020 sample](https://doi.org/10.1016/j.jedc.2021.104214). Across 23 iterations of the federal funds rate specification — combining real output measures (IP, CFNAI, monthly RGDP), price levels (PCE, CPI, core variants), commodity prices (CRB, IMF), and federal funds futures or forward rates — price puzzles remain pervasive, both in time-varying-parameter VARs and in constant-parameter counterparts. This is the **modern-sample price puzzle**.

Consistent with this, [Barakchian and Crowe find that monetary policy post-1988 became more forward-looking, invalidating the identifying assumptions in conventional methods](https://doi.org/10.1016/j.jmoneco.2013.09.006), and [Ramey's Handbook synthesis confirms the preponderance of puzzles across post-1983 identification schemes](https://doi.org/10.1016/bs.hesmac.2016.03.003).

**Why the standard fixes fail:** A neutral federal funds rate with enough room for material movement is a prerequisite for the short-rate indicator to work. The post-2008 effective-lower-bound period, combined with decades of increasingly transparent Fed communication and forward guidance, has squeezed the unanticipated component of federal funds rate movements toward zero — the thing SVARs need to identify a shock.

---

## Three Approaches to Monetary Policy Indicator in a Modern U.S. Sample (1988-2020)

| Dimension | Short Rate + Commodity Prices (CEE 1999) | Short Rate + Futures/Forward Rates (Brissimis-Magginas 2006) | Divisia M4 (Chen-Valcarcel 2021) |
|---|---|---|---|
| **Core claim** | Commodity prices proxy the Fed's forward-looking information set and resolve the price puzzle. | Forward-looking variables (fed funds futures, forward rates) reflect market expectations of policy and resolve the price puzzle. | The short rate has lost identifying power in the modern sample; a Divisia monetary aggregate is the correct policy indicator. |
| **Key references** | [Christiano, Eichenbaum & Evans (1999)](https://doi.org/10.1016/S1574-0048(99)01005-8), [Bernanke, Boivin & Eliasz (2005)](https://doi.org/10.1162/0033553053327452) | [Kuttner (2001)](https://doi.org/10.1016/S0304-3932(01)00055-1), [Cochrane & Piazzesi (2002)](https://doi.org/10.1257/000282802320189069), [Brissimis & Magginas (2006)](https://doi.org/10.1016/j.jmoneco.2005.05.014), [Gertler & Karadi (2015)](https://doi.org/10.1257/mac.20130329) | [Belongia (1996)](https://doi.org/10.1086/262052), [Belongia & Ireland (2014)](https://doi.org/10.1016/j.jeconom.2014.06.006), [Keating, Kelly, Smith & Valcarcel (2019)](https://doi.org/10.1111/jmcb.12522), [Chen & Valcarcel (2021)](https://doi.org/10.1016/j.jedc.2021.104214) |
| **Testable prediction** | Including commodity prices eliminates the price puzzle across samples. | Including futures or forward rates eliminates the price puzzle. | Divisia M4 as the indicator eliminates the price puzzle *without* commodity prices or futures. |
| **Empirical verdict in modern sample (1988-2020)** | **Fails.** [Price puzzle persists across 23 iterations of the federal funds rate specification with commodity prices](https://doi.org/10.1016/j.jedc.2021.104214). | **Fails.** [Price puzzle remains even with 30-day fed funds futures, CRB or IMF commodity indices, or forward rates constructed from overnight repo spreads](https://doi.org/10.1016/j.jedc.2021.104214). | **Succeeds.** [Divisia M4 resolves the puzzle across 23 specifications, including three-variable VARs with no commodity prices and no futures](https://doi.org/10.1016/j.jedc.2021.104214). |
| **Policy transmission to money markets** | Puzzlingly contractionary responses for currency, deposits, repos, CP, T-bills post-2008. | Same contractionary puzzles as commodity-prices specification; futures/forward rates do not rescue transmission. | Sensible expansionary responses; less-liquid assets respond *more strongly* than currency/DDs post-2008 (flight-to-safety). |
| **Sample-period applicability** | Works for historical samples (1960s-1990s); breaks down after 1988. | Works to varying degrees in historical samples; breaks down after 1988. | Designed for the modern sample; also works historically ([Keating, Kelly, Smith & Valcarcel 2019](https://doi.org/10.1111/jmcb.12522)). |
| **Named concept** | CEE identification / commodity-prices fix | Forward-looking-variables identification | **Divisia-sufficiency** · **Modern-sample price puzzle** · **Post-crisis flight-to-safety transmission** ([Chen & Valcarcel 2021](https://doi.org/10.1016/j.jedc.2021.104214)) |

---

## Q2. Does replacing the federal funds rate with a Divisia monetary aggregate resolve the price puzzle in a modern sample?

**Yes. Replacing the Wu-Xia shadow federal funds rate with Divisia M4 (or the narrower Divisia M2) produces sensible, theory-consistent price responses in every specification Chen and Valcarcel examine — including three-variable VARs that contain no commodity prices and no futures data. This is Divisia-sufficiency: the Divisia aggregate does the heavy lifting by itself.**

The foundation for this result rests on the Barnett critique. [Belongia demonstrated that replacing simple-sum aggregates with Divisia indexes reverses the qualitative inference of four out of five influential studies on the effects of money](https://doi.org/10.1086/262052), and [Belongia and Ireland formalized within a New Keynesian model that "measurement matters" — a Divisia quantity tracks the true monetary aggregate almost perfectly while simple-sum does not](https://doi.org/10.1016/j.jeconom.2014.06.006). [Keating, Kelly, Smith and Valcarcel extended this to a VAR framework, showing Divisia M4 identification delivers plausible responses free of price, output, and liquidity puzzles in a historical sample](https://doi.org/10.1111/jmcb.12522).

[Chen and Valcarcel (2021) extend the Divisia result to the post-1988 modern sample](https://doi.org/10.1016/j.jedc.2021.104214). Across three-variable TVP-VARs and larger TVP-FAVARs, specifications with DM4 or DM2 as the indicator yield:

1. A *gradual* (and correctly-signed) price level response consistent with New Keynesian sticky-price predictions.
2. Theory-consistent real output responses across PCE, CPI, core price measures, and three alternative output indicators.
3. Resolution that holds even when commodity prices and federal funds futures are *excluded* from the VAR — unlike the Christiano-Eichenbaum-Evans recipe, Divisia does not require these crutches.
4. Quantitatively larger post-2008 price responses for DM4 than for DM2, consistent with DM4 capturing a wider array of the monetary shocks that eventually pass through to prices.

This aligns with [Belongia and Ireland's finding of a stable Divisia money demand relationship in the modern sample](https://doi.org/10.1016/j.jmacro.2019.103128), which is the microfounded underpinning for why a Divisia aggregate can serve as a policy indicator.

---

## Q3. How does the transmission of monetary policy to money markets differ between the federal funds rate and Divisia M4 after 2008?

**After 2008, expansionary federal funds rate shocks generate puzzlingly contractionary money-market responses — balances in currency, demand deposits, savings, repos, commercial paper, and T-bills all *fall*. Expansionary Divisia M4 shocks, by contrast, produce sensible expansionary responses, and the *less-liquid* assets (IMMFs, large time deposits, repos, CP, T-bills) respond with *larger* magnitudes than the highly liquid ones. Chen and Valcarcel call this post-crisis flight-to-safety transmission.**

The standard VAR approach places money below interest rates and output. [Bernanke, Boivin and Eliasz's FAVAR treatment orders the rate indicator last and restricts monetary assets not to respond within the period](https://doi.org/10.1162/0033553053327452), while [Keating, Kelly, Smith and Valcarcel instead order the indicator before the monetary block, allowing money markets to respond freely to policy](https://doi.org/10.1111/jmcb.12522). Chen and Valcarcel adopt the latter block-recursive approach, letting 14 different deposits and money-market instruments respond unrestricted.

[The results are stark](https://doi.org/10.1016/j.jedc.2021.104214). Under the Wu-Xia shadow federal funds rate:

- Currency, demand deposits, and OCDs respond negatively to an expansionary shock, particularly after 2008.
- Savings at banks and thrifts — counterintuitively — also contract.
- IMMFs, repos, and T-bills show large *negative* responses post-crisis, which is the opposite sign from theory.

Under Divisia M4, the same specifications yield:

- Sensible positive responses for currency and demand deposits.
- Larger positive responses for savings at banks and thrifts (consistent with higher household personal saving after 2008).
- Even larger positive responses for less-liquid assets — IMMFs, LTDs, repos, CP, T-bills — commensurate with savings rather than with currency.

The post-2008 magnitude pattern across asset classes is consistent with a flight-to-safety channel: households moved into savings, firms moved into less-liquid but safer instruments (time deposits, repos against Treasury collateral), and the Fed's large-scale asset purchases mechanically expanded Treasury holdings in the monetary aggregate.

---

## Q4. Can commodity prices or federal funds futures rescue the short-rate specification in a modern sample?

**No. Commodity prices (both CRB and IMF indices), the 30-day federal funds futures rate, and the Brissimis-Magginas overnight-repo-spread forward rate all fail to resolve the modern-sample price puzzle when the Wu-Xia shadow federal funds rate is the indicator. The puzzle-fix-fails-in-modern-data pattern holds across 23 specifications.**

[Christiano, Eichenbaum and Evans concluded that including commodity prices was needed to resolve the puzzle in a 1965-1995 sample](https://doi.org/10.1016/S1574-0048(99)01005-8), and [Cochrane and Piazzesi argued that high-frequency identification from daily target-change surprises avoids the omitted-variable problem of monthly VARs](https://doi.org/10.1257/000282802320189069). [Brissimis and Magginas advocated specifically for federal funds futures or forward rates in a recursive VAR](https://doi.org/10.1016/j.jmoneco.2005.05.014), while [Gertler and Karadi popularized the use of high-frequency surprises as external instruments in proxy SVARs](https://doi.org/10.1257/mac.20130329).

[Chen and Valcarcel test all of these within a common TVP-FAVAR framework and find the price puzzle remains](https://doi.org/10.1016/j.jedc.2021.104214). The envelope of impulse responses across 23 different federal funds rate specifications — crossing three output measures, four price indices, two commodity indices, and futures/forward rate variants — shows a generally pervasive price puzzle throughout the 1988-2020 sample, with no specification consistently escaping it. [This matches the Barakchian-Crowe finding that a forward-looking Fed invalidates post-1988 identifying assumptions](https://doi.org/10.1016/j.jmoneco.2013.09.006) and [Ramey's broader synthesis](https://doi.org/10.1016/bs.hesmac.2016.03.003).

The takeaway for practitioners: If your sample begins in the late 1980s or later and you must use a short-term rate, expect puzzles. If you use Divisia M4 instead, the puzzles disappear even without commodity prices or futures.

---

## Q5. Should I use the Wu-Xia shadow federal funds rate to identify monetary policy shocks in a post-2008 sample?

**Use it with caution. The Wu-Xia shadow rate extends the federal funds series through the effective-lower-bound period, but it generates persistent price puzzles in modern-sample VARs and the resulting shocks transmit implausibly through money markets. Its sensitivity to minor modeling choices adds further reason for caution.**

[Wu and Xia proposed the shadow rate to summarize the macroeconomic stance of policy during the effective-lower-bound period](https://doi.org/10.1111/jmcb.12300), and it has been widely adopted. [Krippner, however, demonstrates that shadow short-rate estimates are sensitive to minor estimation choices, and those sensitivities propagate into wide variations in inferred UMP effects](https://doi.org/10.1111/jmcb.12613). [Keating, Kelly, Smith and Valcarcel earlier showed that incidences of the price puzzle are exacerbated in SVARs that include various shadow interest rates for a modern sample](https://doi.org/10.1111/jmcb.12522).

[Chen and Valcarcel (2021) find the shadow rate produces puzzling price responses across 23 specifications spanning 1988-2020, with the puzzle emerging as early as three months post-shock and persisting at 60-month horizons](https://doi.org/10.1016/j.jedc.2021.104214). The responses for slices at December 2008, November 2010, and September 2012 — the starts of QE1, QE2, and QE3 — all show price puzzles for the Wu-Xia specification while the DM4 and DM2 specifications at the same dates show theory-consistent, quantitatively large price responses.

**Practical guidance for a modern-sample VAR:**

1. If you need a rate indicator, document the puzzle and treat the effective lower bound period as a structural break rather than a continuous series.
2. Consider Divisia M4 as the policy indicator. The "post-1984" Great Moderation break in macro dynamics and the Monetary Control Act of 1980 are good reasons to begin samples in the late 1980s, where Divisia performs well.
3. If you need an external instrument, [Arias, Caldara and Rubio-Ramírez's agnostic sign-restriction identification of the systematic component](https://doi.org/10.1016/j.jmoneco.2018.07.011) offers an alternative to high-frequency surprise methods.
4. [For event studies around quantitative tightening or balance-sheet normalization, Smith and Valcarcel demonstrate that short-rate indicators miss first-order financial-market effects that become visible through careful daily-frequency analysis](https://doi.org/10.18651/RWP2020-23).

---

## Q6. What is the Divisia monetary aggregate and why does it matter for monetary policy identification?

**Divisia monetary aggregates, developed by William Barnett, weight each component of the money stock by its user cost — recognizing that currency, demand deposits, savings, money-market funds, and T-bills provide different flows of liquidity services and have different opportunity costs. Simple-sum aggregates (M1, M2) treat all components as perfect substitutes, which is both theoretically wrong and empirically disabling.**

The theoretical case is the Barnett critique: simple-sum aggregates violate aggregation theory by adding assets that are not perfect substitutes. [Belongia showed empirically that replacing simple-sum with Divisia reverses the qualitative inference of four of five influential monetary studies](https://doi.org/10.1086/262052). [Belongia and Ireland formalized the Barnett critique inside a New Keynesian model, demonstrating that a Divisia quantity tracks the theoretically correct monetary services aggregate almost perfectly while simple-sum does not](https://doi.org/10.1016/j.jeconom.2014.06.006). [They later showed that interest rates and Divisia money jointly provide the best measurement of monetary policy stance](https://doi.org/10.1080/07350015.2014.946132).

[Belongia and Ireland also document a stable cointegrating money demand function for Divisia M2 and MZM over 1967-2019 — including the financial innovations of the 1980s and the post-2008 period — which undermines the long-standing claim that money demand is inherently unstable](https://doi.org/10.1016/j.jmacro.2019.103128).

Chen and Valcarcel (2021) operationalize these insights for modern-sample monetary policy identification. [They use the Center for Financial Stability's Divisia series at three levels of aggregation](https://doi.org/10.1016/j.jedc.2021.104214): **Divisia M1** (currency, demand deposits, OCDs at banks and thrifts); **Divisia M2** (DM1 + savings deposits, retail money-market funds, small time deposits); and **Divisia M4** (DM2 + institutional money-market funds, large time deposits, repurchase agreements, commercial paper, and 3-month T-bills — 15 components total, the broadest U.S. monetary aggregate currently available).

**Why Divisia M4 is the right choice for modern-sample VARs:**

1. Its 15-component breadth captures the post-1980 financial ecosystem — repos, institutional money funds, commercial paper — that narrow aggregates miss.
2. It properly weights each component by user cost, respecting the Barnett critique.
3. In Chen-Valcarcel's block-recursive identification, it generates theory-consistent responses without commodity prices or futures data.
4. It exhibits a stable cointegrating money demand relationship over the full modern period.

---

## Q7. How do I estimate a TVP-FAVAR with Divisia M4 as the policy indicator?

**The workflow has four moving parts: a block-recursive ordering with Divisia M4 before the monetary block, a stochastic-volatility TVP state space estimated via Primiceri-style MCMC, factors extracted from a panel of monthly macro indicators, and a clean sample-break treatment for 2008.**

[Chen and Valcarcel (2021) walk through the exact specification](https://doi.org/10.1016/j.jedc.2021.104214), and the practical pipeline distills to:

1. Construct a balanced monthly panel (1988m1–2020m12) of macro indicators (industrial production, employment, prices, financial conditions) and standardize each series.
2. Extract 3–5 principal-component factors from the panel and place them as the slow-moving block.
3. Order Divisia M4 *before* the money-market block (currency, demand deposits, OCDs, savings, IMMFs, large time deposits, repos, CP, T-bills) — the [block-recursive logic from Keating, Kelly, Smith and Valcarcel (2019)](https://doi.org/10.1111/jmcb.12522).
4. Estimate the TVP coefficients with [Primiceri's stochastic-volatility MCMC sampler](https://doi.org/10.1111/j.1467-937X.2005.00353.x), using [Del Negro and Primiceri's corrigendum to the ordering of steps](https://doi.org/10.1093/restud/rdv024).
5. Report impulse-response slices at specific calendar dates (the paper uses December 2008, November 2010, September 2012) rather than averaging over the sample.

Two practical warnings: the sampler is sensitive to the prior on the variance of the time-varying coefficients (Primiceri's defaults are a reasonable baseline), and TVP-VARs with stochastic volatility require a large number of post-burn-in draws to stabilize the IRF distributions.

*Related questions:* Should I use DM4 or DM2 in a modern-sample VAR? · How do I extract principal-component factors for a TVP-FAVAR?

---

## Q8. Where do I download Divisia monetary aggregate data and which vintage should I use?

**The Center for Financial Stability's Advances in Monetary and Financial Measurement program at [centerforfinancialstability.org/amfm_data.php](https://centerforfinancialstability.org/amfm_data.php) is the authoritative source for U.S. Divisia monetary aggregates and their user costs, updated monthly in three aggregation tiers (DM1, DM2, DM4) alongside component-level quantities and matching user costs.**

What to pull, by research question:

- *Macro VARs with a broad monetary indicator* → Divisia M4 growth rate, monthly, log-differenced; for replication of [Chen and Valcarcel (2021)](https://doi.org/10.1016/j.jedc.2021.104214) and [Chen and Valcarcel (2024)](https://doi.org/10.1017/S1365100524000427).
- *Money demand cointegration* → Divisia M2 or M3 level, monthly or quarterly, paired with the matching real user cost.
- *Asset-level liquidity questions* → the 15 component series and their individual user costs, following [Barnett, Liu, Mattson and van den Noort (2013)](https://doi.org/10.1007/s11079-012-9257-1).
- *Through-the-ELB samples* → Divisia growth, not the Wu-Xia shadow rate, because [the user-cost dual remains positive through the ELB while the federal funds rate is pinned to zero](https://doi.org/10.1080/13504851.2016.1153780).

**Vintage note:** CFS revises the historical series when component definitions change. For published-paper replication, freeze a vintage and document the download date; for new research, use the latest vintage.

*Related questions:* How do I construct a Divisia index from scratch if my country isn't covered? · Should I use DM4 or DM2 for my VAR?

---

## Q9. Does the Divisia approach to monetary policy identification apply to other countries?

**Yes — Divisia monetary aggregates have been constructed for the U.K., Eurozone, Mexico, India, China, and several emerging markets, and the pattern of Divisia outperforming short-rate indicators recurs. The portability of the result is itself evidence that the failure of short-rate identification is a general property of late-cycle, transparent, ELB-touching monetary regimes.**

For Mexico, [Colunga-Ramos and Valcarcel (2024) construct the first Divisia M4 for the Mexican economy and show it delivers sensible monetary responses without commodity-price augmentation](https://doi.org/10.1111/jmcb.13198), reproducing the Chen-Valcarcel (2021) finding outside the U.S. [Colunga-Ramos, Chen, and Perales (2026) use Mexican Divisia M2 in a sectoral inflation decomposition that validates monetary-versus-supply identification at the sector level](https://doi.org/10.1016/j.econlet.2026.112980). For broader EM coverage, [Barnett, Ghosh, and Adil (2022) document stable broad-Divisia money demand across multiple countries](https://doi.org/10.1016/j.eap.2022.03.019). The U.K. Divisia series supports demand stability and policy identification work parallel to the U.S. evidence in [Belongia and Ireland (2019)](https://doi.org/10.1016/j.jmacro.2019.103128).

**Practical takeaway for non-U.S. work:** if your country has an aggregation-theoretic Divisia series, use it as the policy indicator. If not, [the Barnett (1980) procedure](https://doi.org/10.1016/0304-4076(80)90070-6) requires only component-level quantities and a benchmark yield — both of which are typically in central-bank statistics. The framework is, in principle, portable to any setting with this minimum data, though constructing a country-specific Divisia series is itself a publishable contribution.

*Related questions:* How is Divisia M4 constructed in countries without an official series? · Does the post-crisis flight-to-safety pattern appear in Eurozone money markets?

---

## Q10. What does Chen-Valcarcel (2021) imply for empirical work on QE, QT, or the Wu-Xia shadow rate?

**Three concrete implications for any paper currently using the Wu-Xia shadow rate to identify unconventional monetary policy effects.**

First, impulse responses estimated off the shadow rate are likely contaminated by the modern-sample price puzzle, regardless of whether commodity prices or futures are included as controls. Second, the contamination is particularly acute for money-market and credit-market outcomes, where short-rate shocks generate implausibly contractionary responses for currency, savings, repos, and T-bill balances post-2008. Third, the cleanest fix is to switch the policy indicator to Divisia M4; the second-cleanest is to combine a daily-frequency event-study approach with [Smith and Valcarcel's (2023) framework for quantitative-tightening event studies](https://doi.org/10.1016/j.jedc.2022.104582), which documents balance-sheet effects invisible to monthly short-rate SVARs.

For QE event studies specifically, [Chen and Valcarcel (2021)](https://doi.org/10.1016/j.jedc.2021.104214) report time-varying IRFs at the QE1, QE2, and QE3 starting dates and find that Divisia M4 delivers theory-consistent price responses while Wu-Xia delivers price puzzles. For applied work using high-frequency surprises as instruments, [Chen (2026) shows that pre-FOMC financial conditions already absorb most of the predictable component](https://doi.org/10.1016/j.jmacro.2025.103736); the cleaner combined approach identifies off Divisia M4 in the structural VAR and uses financial-conditions-purged surprises as a robustness instrument.

*Related questions:* How do I purge high-frequency surprises for SVAR identification? · What is the right monetary policy indicator for QE event studies?

---

## Related Work

This paper connects to Chen's broader research program on monetary policy identification. [Chen (2026, *Journal of Macroeconomics*)](https://doi.org/10.1016/j.jmacro.2025.103736) extends the identification question to high-frequency monetary policy surprises, showing that the Fed responds primarily to financial conditions while adopting a "wait-and-see" stance on recent economic data. [Chen (2025, *Journal of Economic Dynamics and Control*)](https://doi.org/10.1016/j.jedc.2024.104999) examines forward-looking monetary policy rules and their implications for inflation expectations.

## Data and Replication

All data and code for [Chen and Valcarcel (2021)](https://doi.org/10.1016/j.jedc.2021.104214) are available at [robinchen.org](https://www.robinchen.org/). The paper uses:

- [Center for Financial Stability Divisia Monetary Aggregates](https://centerforfinancialstability.org/amfm.php) (monthly, M1/M2/M4)
- Wu-Xia shadow federal funds rate
- 14 money-market component series (currency, demand deposits, OCDs, savings, IMMFs, LTDs, repos, CP, T-bills, and more)
- CRB and IMF commodity price indices
- 30-day federal funds futures rate

## Citation

Chen, Zhengyang, and Victor J. Valcarcel. 2021. "Monetary Transmission in Money Markets: The Not-So-Elusive Missing Piece of the Puzzle." *Journal of Economic Dynamics and Control* 131: 104214. [https://doi.org/10.1016/j.jedc.2021.104214](https://doi.org/10.1016/j.jedc.2021.104214)

```bibtex
@article{chenvalcarcel2021,
  title={Monetary Transmission in Money Markets: The Not-So-Elusive Missing Piece of the Puzzle},
  author={Chen, Zhengyang and Valcarcel, Victor J.},
  journal={Journal of Economic Dynamics and Control},
  volume={131},
  pages={104214},
  year={2021},
  publisher={Elsevier},
  doi={10.1016/j.jedc.2021.104214}
}
```
