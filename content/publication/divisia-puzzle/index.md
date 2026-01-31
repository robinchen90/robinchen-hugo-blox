---
title: "Monetary Transmission in Money Markets: The Not-So-Elusive Missing Piece of the Puzzle"
date: 2021-08-11T00:00:00

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors: ["admin","Victor J. Valcarcel"]

# Publication type.
publication_types: ["article-journal"]

# Publication name and optional abbreviated version.
publication: "Journal of Economic Dynamics and Control"
publication_short: "JEDC"

# Abstract.
abstract: "We investigate the effects of U.S. monetary policy shocks from two alternative policy indicators for a modern sample encompassing 1988-2020. The choice of the Wu and Xia (2016) shadow federal funds rate leads to persistent price puzzles. These puzzles arise despite inclusion of the usual suspect fixes such as commodity prices, federal funds futures and forward rate data. We find they occur at monthly and quarterly frequencies in time-varying and constant-parameter approaches. We consider an alternative indicator with the same broad monetary aggregate Keating et al. (2019) employed in their investigation of a historical sample. This alternative provides a consistent resolution of the price puzzle and it does not require the ad hoc inclusion of commodity prices or futures data. While this price puzzle correction is not a feature of our time-varying approach—as it also obtains from constant parameter econometric estimation—our analysis suggests monetary policy has transmitted substantial expansionary effects in money markets in the aftermath of the 2007 Financial Crisis and the decade that followed."

# Summary. An optional shortened abstract.
summary: "Adding variables to a VAR model may not solve the price puzzle but changing the policy indicator does."

# Digital Object Identifier (DOI)
doi: "10.1016/j.jedc.2021.104214"

# Is this a featured publication? (true/false)
featured: false

# Tags (optional).
tags: []

# Projects (optional).
projects: []

# Slides (optional).
slides: ""



# Links (optional).
url_pdf: "https://doi.org/10.1016/j.jedc.2021.104214"
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
 "@type": "ScholarlyArticle",
 "name": "Resolving the Price Puzzle: How Monetary Aggregates Restore Sanity to Monetary Policy Analysis",
 "headline": "Comprehensive Analysis of Chen & Valcarcel (2021) on Monetary Transmission Through Divisia Aggregates",
 "description": "Detailed examination of how properly measured monetary aggregates resolve persistent price puzzles in VAR models and provide superior insights into monetary policy transmission mechanisms",
 "keywords": "monetary policy, price puzzle, Divisia aggregates, VAR models, monetary transmission, Federal Reserve, money markets, time-varying parameters",
 "datePublished": "2025-01-14",
 "citation": [
   "Chen, Z., & Valcarcel, V. J. (2021). Monetary transmission in money markets: The not-so-elusive missing piece of the puzzle. Journal of Economic Dynamics and Control, 131, 104214. https://doi.org/10.1016/j.jedc.2021.104214",
   "Christiano, L. J., Eichenbaum, M., & Evans, C. L. (1999). Monetary policy shocks: What have we learned and to what end? Handbook of Macroeconomics, 1, 65-148.",
   "Eichenbaum, M. (1992). Comments on interpreting the time series facts: The effects of monetary policy. European Economic Review, 36(4), 1001-1011.",
   "Belongia, M. T., & Ireland, P. N. (2014). The barnett critique after three decades: A new keynesian analysis. Journal of Econometrics, 183(1), 5-21.",
   "Barnett, W. A. (1980). Economic monetary aggregates: An application of index number and aggregation theory. Journal of Econometrics, 14(1), 11-48.",
   "Primiceri, G. E. (2005). Time varying structural vector autoregressions and monetary policy. Review of Economic Studies, 72(3), 821-852.",
   "Bernanke, B. S., Boivin, J., & Eliasz, P. (2005). Measuring the effects of monetary policy: A factor-augmented vector autoregressive (FAVAR) approach. Quarterly Journal of Economics, 120(1), 387-422.",
   "Wu, J. C., & Xia, F. D. (2016). Measuring the macroeconomic impact of monetary policy at the zero lower bound. Journal of Money, Credit and Banking, 48(2-3), 253-291.",
   "Barakchian, S. M., & Crowe, C. (2013). Monetary policy matters: Evidence from new shocks data. Journal of Monetary Economics, 60(8), 950-966.",
   "Ramey, V. A. (2016). Macroeconomic shocks and their propagation. Handbook of Macroeconomics, 2, 71-162.",
   "Keating, J. W., Kelly, L. J., Smith, A. L., & Valcarcel, V. J. (2019). A model of monetary policy shocks for financial crises and normal conditions. Journal of Money, Credit and Banking, 51(1), 227-259.",
   "Koop, G., & Korobilis, D. (2014). A new index of financial conditions. European Economic Review, 71, 101-116.",
   "Taylor, J. B. (1993). Discretion versus policy rules in practice. Carnegie-Rochester Conference Series on Public Policy, 39, 195-214.",
   "Friedman, M., & Schwartz, A. J. (1963). A Monetary History of the United States, 1867-1960. Princeton University Press.",
   "Sims, C. A. (1992). Interpreting the macroeconomic time series facts: The effects of monetary policy. European Economic Review, 36(5), 975-1000."
 ]
}
</script>

# Monetary Transmission in Money Markets: The Not-So-Elusive Missing Piece of the Puzzle

## The Problem: When Standard Monetary Models Don't Work

For decades, economists have tried to understand how Federal Reserve policy affects the economy. The standard approach has been to focus on the **federal funds rate** - the interest rate banks charge each other for overnight loans - as the primary tool for measuring monetary policy effects. However, this approach has consistently produced a puzzling result known as the **"price puzzle"** (first identified by Eichenbaum, 1992).

The price puzzle occurs when economic models show that lowering interest rates (which should stimulate the economy and raise prices) actually leads to falling prices instead - the opposite of what economic theory predicts. This has been a persistent problem in monetary economics, with researchers trying various fixes like including commodity prices or federal funds futures data, as suggested by influential work like Christiano et al. (1999).

## The Alternative: Bringing Money Back into Monetary Economics

Chen and Valcarcel investigate whether using **monetary aggregates** instead of interest rates can solve this puzzle. Monetary aggregates are measures of the total money supply in the economy. However, rather than using the Federal Reserve's traditional "simple-sum" measures (like M1 and M2), they focus on **Divisia monetary aggregates** - more sophisticated measures developed by William Barnett in the 1980s.

Divisia aggregates are superior because they recognize that different types of money (cash, checking accounts, savings accounts, etc.) provide different levels of liquidity services and should be weighted accordingly, rather than simply added together. As Belongia and Ireland (2014) noted, "virtually all monetary economists today would concede that the Divisia aggregates proposed by Barnett are both theoretically and empirically superior to their simple-sum counterparts."

## Key Findings

Using data from 1988 to 2020, the authors employ advanced econometric techniques called **time-varying parameter vector autoregressions (TVP-VAR)** and **factor-augmented VARs (TVP-FAVAR)** to compare how the economy responds to shocks in different monetary policy indicators.

### 1. Interest Rate Models Consistently Fail
The researchers find that models using the **Wu and Xia (2016) shadow federal funds rate** - an extended measure that accounts for near-zero interest rates during and after the 2007-2008 financial crisis - consistently produce price puzzles. Even when they include the traditional "fixes" like commodity prices or federal funds futures data, the puzzle persists.

### 2. Divisia Money Resolves the Puzzles
In stark contrast, when they replace the federal funds rate with Divisia monetary aggregates (particularly DM4, the broadest measure), the price puzzles disappear entirely. The economic responses become sensible: expansionary monetary policy leads to higher output and prices, as theory predicts.

### 3. Money Markets Show Dramatic Changes After 2008
The study also examines how monetary policy affects specific money markets (currency, bank deposits, money market funds, Treasury bills, etc.). They find that the 2007 financial crisis marked a significant shift in how monetary policy transmits through these markets, with much larger responses in the post-crisis period.

## Why This Matters

The findings have important implications for both economic research and policy:

**For Research**: The results suggest that the long-standing focus on interest rates in monetary models may be misguided, particularly in the modern era. As the authors note, increased Federal Reserve transparency and forward guidance may have made interest rate movements more predictable and less informative about monetary policy stance.

**For Policy**: The research indicates that traditional measures of monetary policy effectiveness may be inadequate. During periods like quantitative easing (when the Fed purchased large amounts of securities), monetary aggregates may provide better insight into policy transmission than interest rates.

**For Understanding the Modern Economy**: The study highlights how financial innovation and the shift from reserve scarcity to abundance (post-2008) has fundamentally altered monetary transmission mechanisms.

## The Broader Context

This work builds on a growing literature questioning the New Keynesian consensus that largely abandoned monetary aggregates in favor of interest rate rules. Earlier work by Keating et al. (2019) and Belongia and Ireland (2015, 2018) has similarly argued for rehabilitating the role of money in monetary models.

The authors conclude that "putting money back in monetary models offers a viable alternative" in an environment where key short-term rates are persistently low and the banking system has transitioned to abundant reserves. Rather than being an obsolete relic, properly measured money may indeed be "the missing piece of the puzzle" in understanding modern monetary transmission.

---

**References:**

- Belongia, M.T., Ireland, P.N. (2014). The barnett critique after three decades: A new keynesian analysis. *Journal of Econometrics*, 183, 5-21.

- Chen, Z., Valcarcel, V.J. (2021). Monetary transmission in money markets: The not-so-elusive missing piece of the puzzle. *Journal of Economic Dynamics and Control*, 131, 104214.

- Christiano, L.J., Eichenbaum, M., Evans, C.L. (1999). Monetary policy shocks: What have we learned and to what end? *Handbook of Macroeconomics*, Volume 1A, 65-148.

- Eichenbaum, M. (1992). Comments on interpreting the time series facts: The effects of monetary policy. *European Economic Review*, 36, 1001-1011.

- Keating, J.W., Kelly, L.J., Smith, A.L., Valcarcel, V.J. (2019). A model of monetary policy shocks for financial crises and normal conditions. *Journal of Money, Credit and Banking*, 51, 227-259.

---

**Chen, Zhengyang, and Victor J. Valcarcel.** "Monetary transmission in money markets: The not-so-elusive missing piece of the puzzle." *Journal of Economic Dynamics and Control* 131 (October 2021): 104214. https://doi.org/10.1016/j.jedc.2021.104214.
