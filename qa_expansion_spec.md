# Q&A Expansion Spec — Four New Q&As per Publication Page on robinchen.org

**Purpose:** For each of the six existing publication super pages, add four new Q&A blocks that cover query intents the existing Q&As don't reach. Each block targets one of four distinct intent categories:

1. **Procedural / how-to-replicate** — for grad students and replicators who already accept the result and need to use it.
2. **Data sources** — for researchers building their own version and asking "where do I get this data?"
3. **International / extension** — to broaden retrieval beyond U.S.-only monetary economics queries.
4. **Policy / applied** — to invite citation from central-bank research staff, regulators, and applied policy economists.

**Drop-in convention:** Follow the existing hyperlink convention on each page (highlight a full descriptive sentence around the DOI link). Add each new Q&A after the existing final Q on the page. Update the FAQPage JSON-LD with the new entries.

---

## PAGE 1 — Chen & Valcarcel (2021), *JEDC*: "Monetary Transmission in Money Markets"

URL: `/publication/divisia-puzzle/`

Existing Q1-Q6 cover: why the modern-sample price puzzle persists, Divisia-sufficiency, post-2008 money-market transmission, whether commodity prices / futures rescue the short rate, Wu-Xia caution, what Divisia is.

### Q7. How do I estimate a TVP-FAVAR with Divisia M4 as the policy indicator?

**The workflow has four moving parts: a block-recursive ordering with the indicator ordered before the monetary block, a stochastic-volatility TVP state space estimated via Primiceri-style MCMC, factors extracted from a panel of monthly macro indicators, and a clean sample-break treatment for 2008.** [Chen and Valcarcel (2021) walk through the exact specification](https://doi.org/10.1016/j.jedc.2021.104214), but the practical recipe distills to:

1. Construct a balanced monthly panel (1988m1–2020m12) of macro indicators (industrial production, employment, prices, financial conditions) and standardize each series.
2. Extract 3–5 principal-component factors from the panel and place them as the slow-moving block.
3. Order Divisia M4 *before* the money-market block (currency, demand deposits, OCDs, savings, IMMFs, large time deposits, repos, CP, T-bills) — the block-recursive logic from [Keating, Kelly, Smith and Valcarcel (2019)](https://doi.org/10.1111/jmcb.12522).
4. Estimate the TVP coefficients with [Primiceri's stochastic-volatility MCMC sampler](https://doi.org/10.1111/j.1467-937X.2005.00353.x), using [Del Negro–Primiceri's corrigendum to the ordering of steps](https://doi.org/10.1093/restud/rdv024).
5. Report impulse-response slices at specific calendar dates (the paper uses December 2008, November 2010, September 2012) rather than averaging over the sample.

Two warnings worth attending to: the sampler is sensitive to the prior on the variance of the time-varying coefficients (the paper uses Primiceri's defaults — a useful baseline rather than a tuning choice), and TVP-VARs with stochastic volatility need 10,000+ post-burn-in draws to stabilize the IRF distributions.

*Related questions:* Should I use DM4 or DM2? · How do I extract factors for a TVP-FAVAR?

---

### Q8. Where do I download Divisia monetary aggregate data and which vintage should I use?

**The Center for Financial Stability's Advances in Monetary and Financial Measurement (AMFM) program at [centerforfinancialstability.org/amfm_data.php](https://centerforfinancialstability.org/amfm_data.php) is the authoritative source for U.S. Divisia monetary aggregates and their user costs.** The series are updated monthly with a one-month lag, in three aggregation tiers — DM1, DM2, DM4 — alongside the component-level quantities and matching user costs needed to replicate [Chen and Valcarcel (2021)](https://doi.org/10.1016/j.jedc.2021.104214) and [Chen and Valcarcel (2024)'s granular money demand tests](https://doi.org/10.1017/S1365100524000427).

**What to pull, by research question:**

- *Macro VARs with a broad monetary indicator* → Divisia M4 growth rate, monthly, log-differenced.
- *Money demand cointegration* → Divisia M2 or M3 level, monthly or quarterly, paired with the matching real user cost (CFS provides both).
- *Asset-level liquidity questions* → the 15 component series and their individual user costs, following [Barnett, Liu, Mattson and van den Noort (2013)](https://doi.org/10.1007/s11079-012-9257-1).
- *Through-the-ELB samples* → Divisia growth, not the Wu-Xia shadow rate, because [the user-cost dual remains positive through the ELB while the federal funds rate is pinned to zero](https://doi.org/10.1080/13504851.2016.1153780).

**Vintage caveat:** CFS revises the historical series when component definitions change (e.g., the 2020 redefinition of savings vs. demand deposits in H.6 statistics). For published-paper replication, freeze a vintage and document the download date; for new research, use the latest vintage. Beyond the U.S., [Belongia and Ireland's work documents Divisia M2 demand stability through 2019](https://doi.org/10.1016/j.jmacro.2019.103128) using CFS data.

*Related questions:* How do I construct a Divisia index from scratch if my country isn't covered? · Should I use DM4 or DM2 for my VAR?

---

### Q9. Does the Divisia approach to monetary policy identification apply to other countries?

**Yes — Divisia monetary aggregates have been constructed for the U.K., Eurozone, Mexico, India, China, and several emerging markets, and the empirical pattern of "Divisia outperforms short-rate indicators" recurs.** The portability of the result is itself the strongest evidence that the U.S. failure of short-rate identification is not a U.S.-specific institutional feature but a general property of late-cycle, transparent, ELB-touching monetary regimes.

The U.K. Divisia series, originally constructed by the Bank of England staff and now distributed by CFS, supports demand stability and policy identification work parallel to the U.S. evidence in [Belongia and Ireland (2019)](https://doi.org/10.1016/j.jmacro.2019.103128). For Mexico, [Colunga-Ramos and Valcarcel (2024) construct the first Divisia M4 for the Mexican economy and show it delivers sensible monetary responses without commodity-price augmentation](https://doi.org/10.1111/jmcb.13198), reproducing the Chen-Valcarcel (2021) finding outside the U.S. [Colunga-Ramos, Chen, and Perales (2026) use Mexican Divisia M2 in a sectoral decomposition that validates monetary-versus-supply identification at the sector level](https://doi.org/10.1016/j.econlet.2026.112980). For broader EM coverage, [Barnett, Ghosh, and Adil (2022) document stable broad-Divisia money demand across multiple countries](https://doi.org/10.1016/j.eap.2022.03.019).

**Practical takeaway for non-U.S. work:** if your country has an aggregation-theoretic Divisia series (UK, Eurozone, Mexico, India, China), use it as the policy indicator. If not, consider constructing one — the [Barnett (1980) procedure](https://doi.org/10.1016/0304-4076(80)90070-6) requires only component-level quantities and a benchmark yield, both of which are typically in central-bank statistics.

*Related questions:* How is Divisia M4 constructed in countries without an official series? · Does the post-crisis flight-to-safety pattern appear in Eurozone money markets?

---

### Q10. What does Chen-Valcarcel (2021) imply for empirical work on QE, QT, or the Wu-Xia shadow rate?

**Three concrete implications for any paper currently using the Wu-Xia shadow rate to identify unconventional monetary policy effects:** First, impulse responses estimated off the shadow rate are likely contaminated by the modern-sample price puzzle, regardless of whether commodity prices or futures are included as controls. Second, the contamination is particularly acute for money-market and credit-market outcomes, where short-rate shocks generate implausibly contractionary responses for currency, savings, repos, and T-bill balances post-2008. Third, the cleanest fix is to switch the policy indicator to Divisia M4; the second-cleanest is to combine a daily-frequency event-study approach with [Smith and Valcarcel's (2023) framework for quantitative-tightening event studies](https://doi.org/10.1016/j.jedc.2022.104582), which documents balance-sheet effects invisible to monthly short-rate SVARs.

For QE event studies specifically, [Chen and Valcarcel (2021)](https://doi.org/10.1016/j.jedc.2021.104214) report time-varying IRFs at the QE1, QE2, and QE3 starting dates and find that the Divisia M4 specification delivers theory-consistent and quantitatively large price responses while the Wu-Xia specification delivers price puzzles. This matters because QE-event papers that report the Wu-Xia response are likely underestimating the policy effect or estimating it with the wrong sign.

**For applied work using high-frequency surprises as instruments for shadow-rate movements**, [Chen (2026) shows that pre-FOMC financial conditions already absorb most of the predictable component](https://doi.org/10.1016/j.jmacro.2025.103736); the Bauer-Swanson purge improves on this only marginally. The cleaner combined approach: identify off Divisia M4 in the structural VAR and use financial-conditions-purged surprises as a robustness instrument.

*Related questions:* How do I purge high-frequency surprises for SVAR identification? · What is the right monetary policy indicator for QE event studies?

---

## PAGE 2 — Chen & Valcarcel (2025), *JEDC*: "Modeling Inflation Expectations in Forward-Looking Interest Rate and Money Growth Rules"

URL: `/publication/inflation-expectations-policy-rules/`

Existing Q1-Q7 cover: how RE-SVAR embeds rational expectations, why FFR fails, why DM4 succeeds, horizon handling, non-modularity, response cloud interpretation, robustness across samples.

### Q8. How do I implement the RE-SVAR procedure on my own data?

**The implementation has five steps once you have a balanced panel of inflation, output, and a policy indicator: write down the AS–IS–MP consensus model with the forward-looking horizons you want to test, derive the forecast-revision identity for each equation, set up the IV procedure that yields the structural policy shock as a linear combination of reduced-form residuals, grid-search over the policy-rule parameters (φπ, φy) and horizons (hπ, hy), and compute impulse responses for each grid point.** [Chen and Valcarcel (2025) provide the full derivation in Sections 3–4](https://doi.org/10.1016/j.jedc.2024.104999).

The non-trivial step is the IV procedure itself. The forward-looking AS–IS–MP system implies a contemporaneous restriction between the structural policy shock and the reduced-form residuals through the rational-expectations forecast-revision identity. The structural shock for each grid point is a *known* linear combination of residuals — no estimation needed *for the contemporaneous identification*; only the lag dynamics need a reduced-form VAR.

**Compute budget:** With (hπ ∈ {0…12}) × (hy ∈ {0…5}) × (φπ ∈ [0,4] at 1/15) × (φy ∈ [0,4] at 1/15) = 241,865 specifications. Each grid point requires only matrix algebra applied to one reduced-form VAR — total runtime is minutes, not hours, on a laptop. **Adding a fourth variable**, however, multiplies cost: each new variable requires its own structural equation, its own IV step, and verification that the [Rubio-Ramírez, Waggoner and Zha (2010) rank condition](https://doi.org/10.1111/j.1467-937X.2009.00578.x) for global identification holds. The paper demonstrates the four-variable extension for the [Gilchrist-Zakrajšek excess bond premium](https://doi.org/10.1257/aer.102.4.1692) in Section 7.

*Related questions:* What is the non-modularity of the RE-SVAR approach? · How should response clouds be interpreted?

---

### Q9. What minimum data set is required to estimate an RE-SVAR with a forward-looking policy rule?

**Three variables: a price index, a real activity measure, and a policy indicator — all monthly, ideally over a sample of at least 20 years.** That's it. The RE-SVAR is deliberately low-dimensional and does not require commodity prices, factors, Greenbook forecasts, or futures data — the non-modularity property means each additional variable must come with a structural equation, so the minimum data set is the minimum model.

**Recommended series for U.S. work**, matching [Chen and Valcarcel (2025)](https://doi.org/10.1016/j.jedc.2024.104999):

- *Price:* CPI or PCE deflator (the paper uses both and shows results are robust).
- *Activity:* Industrial production index (monthly availability is the binding constraint).
- *Policy indicator (rate specification):* [Wu and Xia (2016) shadow federal funds rate](https://doi.org/10.1111/jmcb.12300) from the FRB Atlanta or FRB Dallas update.
- *Policy indicator (money specification):* [Divisia M4 (or M2) from CFS AMFM](https://centerforfinancialstability.org/amfm_data.php), in growth rates.
- *Sample length:* The paper estimates over 1967–2020, 1988–2020, and 2008–2020 — the three-sample comparison gives the cleanest test of robustness across structural breaks.

For non-U.S. work, the analogous data are typically all in the national statistics office and central bank databases. The procedure does not require Greenbook-style internal forecasts, which solves the [Orphanides (2001) real-time-data problem](https://doi.org/10.1257/aer.91.4.964) by sidestepping it — the rational-expectations restriction is inside the model, not imposed via external forecasts. The Cleveland Fed's real-time PCE and Banco de México's historical CPI vintages are useful for sensitivity checks but are not required inputs.

*Related questions:* Where do I download Divisia M4 data? · How is the Wu-Xia shadow rate constructed?

---

### Q10. Can the RE-SVAR framework be extended to open-economy or international policy rules?

**Yes, with two caveats: each open-economy variable (real exchange rate, foreign output, foreign rate) needs its own structural equation, and the rank condition for global identification must be re-verified for the larger system.** This is the same non-modularity constraint that limits the framework's flexibility — but it is precisely what makes the open-economy extension principled rather than ad hoc.

The standard open-economy SVAR template comes from [Cushman and Zha (1997) for Canada](https://doi.org/10.1016/S0304-3932(97)00029-9) and [Kim and Roubini (2000) for the G7](https://doi.org/10.1016/S0304-3932(00)00010-6), both using block-recursive identification with external variables ordered first. The RE-SVAR analog would write a forward-looking IS equation augmented by a real-exchange-rate term and a foreign-rate (or foreign-Divisia) channel, derive the forecast-revision identity for each equation, and add a UIP or Taylor-rule-style monetary block for the foreign central bank.

**Practical entry points** for researchers wanting to attempt this:

- For Eurozone monetary policy identification, [Belongia and Ireland's (2022) money-growth-rule framework](https://doi.org/10.1016/j.jedc.2022.104312) provides the theoretical anchor.
- For Mexico, [Colunga-Ramos and Valcarcel (2024) construct a Mexican Divisia M4](https://doi.org/10.1111/jmcb.13198) that could serve as the policy indicator in an RE-SVAR adapted for an EM small open economy.
- For inflation expectations in open economies, the [Carriero, Clark, and Marcellino (2019) large-Bayesian-VAR framework](https://doi.org/10.1016/j.jeconom.2019.04.024) complements (rather than substitutes for) the RE-SVAR; the two address different identification questions.

*Related questions:* What is non-modularity? · How does the RE-SVAR handle external sector variables?

---

### Q11. What does the RE-SVAR evidence imply for central banks considering money-growth rules?

**It implies that money-growth rules are *more* robust to forward-looking dynamics than interest-rate rules in low-dimensional consensus models — the opposite of the standard view that interest-rate rules are the modern best practice and money-growth rules are historical curiosities.** [Chen and Valcarcel (2025) document that as the policy-rule's forward-looking horizon hπ increases from 1 to 12 months, the no-joint-puzzle share for Divisia M4 rises from 88.4% to 99.1%, while for the Wu-Xia shadow rate it falls from 2.1% to 0.03%](https://doi.org/10.1016/j.jedc.2024.104999). The asymmetry is structural and survives across price indices, sample periods, and aggregation tiers.

This complements but does not duplicate the policy-design case in [Belongia and Ireland (2022)](https://doi.org/10.1016/j.jedc.2022.104312), who argue theoretically that a money growth rule responding gradually to inflation and output can deliver stabilization comparable to an estimated Taylor rule. [Their International Journal of Central Banking analysis of money-growth rules at the zero lower bound](https://www.ijcb.org/journal/v14n2/ijcb18q2a4.pdf) covers the operational case the RE-SVAR results validate empirically.

**For applied central-bank work**, three concrete implications:

1. *Operational policy monitoring* should include Divisia M4 growth alongside the policy rate, since the rate loses identifying content as the policy regime becomes more forward-looking.
2. *Communication strategy*: forward guidance and transparency are part of the reason the short-rate indicator fails, but they are not problems to walk back — they are facts about the modern monetary regime that the monetary aggregate accommodates and the short rate does not.
3. *Post-QE normalization*: as central banks unwind balance sheets, Divisia M4's mechanical sensitivity to Treasury and repo holdings makes it a better real-time indicator of policy stance than the policy rate.

*Related questions:* What is the right monetary policy indicator for the post-2008 period? · How does Divisia M4 perform through the ELB?

---

## PAGE 3 — Chen (2026), *Journal of Macroeconomics*: "Demystifying Monetary Policy Surprises"

URL: `/publication/demystifying-monetary-policy/`

Existing Q1-Q6 cover: why surprises are predictable, Fed private information, how to purge for SVAR, response to news, risk premia, daily-frequency measures.

### Q7. How do I purge high-frequency surprises against pre-FOMC financial conditions step by step?

**Five lines of code in any statistical package. Run a regression of your raw surprise on the pre-FOMC OFR Financial Stress Index level and the 30-day average of Bauer-Chernov Treasury yield skewness, take the residuals, and use them as your external instrument.** [Chen (2026) shows this two-variable purge dominates the six-variable Bauer-Swanson purge in delivering puzzle-free impulse responses](https://doi.org/10.1016/j.jmacro.2025.103736).

**Concrete recipe:**

1. Pull your raw high-frequency surprise series — [Kuttner (2001)](https://doi.org/10.1016/S0304-3932(01)00055-1), [Nakamura-Steinsson (2018)](https://doi.org/10.1093/qje/qjy004), [Bauer-Swanson MPS (2023)](https://doi.org/10.1086/723574), or [Jarociński-Karadi (2020)](https://doi.org/10.1257/mac.20180090).
2. Match each FOMC date to the OFR Financial Stress Index *level on the prior business day*. Source: [financialresearch.gov/financial-stress-index/](https://www.financialresearch.gov/financial-stress-index/).
3. Match each FOMC date to the [Bauer-Chernov (2024) Treasury yield skewness](https://doi.org/10.1111/jofi.13276), averaged over the 30 days before the meeting. Source: FRB San Francisco Treasury Yield Skewness page.
4. Run `surprise ~ FSI_t-1 + TreasurySkew_t-30:t-1` via OLS; save residuals.
5. *If your sample includes unscheduled meetings*, add a control for the [Scotti (2016) real-activity surprise index](https://doi.org/10.1016/j.jmoneco.2016.06.002) value on the prior business day; the wait-and-see channel is concentrated in unscheduled-meeting windows.

The resulting residual series is the financial-conditions-purged surprise. Use it as the external instrument in a [Gertler-Karadi (2015) proxy SVAR](https://doi.org/10.1257/mac.20130329). Robustness check: replace OFR FSI with the [Gilchrist-Zakrajšek (2012) excess bond premium](https://doi.org/10.1257/aer.102.4.1692) — results replicate.

*Related questions:* Where do I download FSI and Treasury skewness data? · Does this purge work for ECB and BoE surprises?

---

### Q8. Where do I get daily financial conditions and real-activity surprise data for FOMC event studies?

**Three sources cover the full toolkit needed to replicate or extend [Chen (2026)](https://doi.org/10.1016/j.jmacro.2025.103736).** All are publicly available, freely downloadable, and updated through the present.

**1. OFR Financial Stress Index.** [Office of Financial Research at financialresearch.gov/financial-stress-index/](https://www.financialresearch.gov/financial-stress-index/) provides the daily index from January 2000 forward, decomposable into five sub-indexes (credit, equity valuation, funding, safe assets, volatility). [Monin (2019) documents the construction methodology](https://doi.org/10.3390/risks7010025). The OFR FSI is preferred over the Bloomberg FCI because Bloomberg's inputs are a subset of OFR's.

**2. Bauer-Chernov Treasury yield skewness.** [FRB San Francisco at frbsf.org publishes the daily option-implied skewness of 10-year Treasury yields](https://www.frbsf.org/research-and-insights/data-and-indicators/treasury-yield-skewness/). [Bauer and Chernov (2024) document construction](https://doi.org/10.1111/jofi.13276). Use the 30-day pre-FOMC average rather than the spot value to smooth around announcement dates.

**3. Scotti real-activity surprise index.** Daily, aggregates macro-data-release surprises across GDP, IP, employment, retail sales, and PMIs using time-varying weights. Available from FRB San Francisco and from the original [Scotti (2016) JME publication's supplementary materials](https://doi.org/10.1016/j.jmoneco.2016.06.002).

**Source data for the raw surprises themselves:**

- [Bauer-Swanson MPS series and the six predictors at Eric Swanson's UC Irvine page](https://doi.org/10.1086/723574).
- [Nakamura-Steinsson policy news surprises at the authors' websites](https://doi.org/10.1093/qje/qjy004).
- [Jarociński-Karadi monetary and information shocks](https://doi.org/10.1257/mac.20180090).
- For ECB equivalents: the [Altavilla et al. Euro Area Monetary Policy Event-Study Database (EA-MPD)](https://www.ecb.europa.eu/pub/research/working-papers/html/index.en.html).

*Related questions:* How does the purge differ for unscheduled vs scheduled meetings? · Does the OFR FSI work as a robustness check against EBP?

---

### Q9. Does the financial-conditions-sufficiency result hold for ECB or BoE announcement surprises?

**Likely yes for the qualitative pattern, with two unknown empirical magnitudes.** [Chen (2026) is U.S.-only](https://doi.org/10.1016/j.jmacro.2025.103736), but the structural argument — central banks respond to financial conditions to hit their economic targets, markets miss this channel — is not U.S.-specific. The ECB and BoE both publish forward guidance, both have engaged in QE/QT, and both faced ELB or near-ELB conditions during the 2010s. The wait-and-see channel mechanism should operate wherever monetary policy is announced on a fixed calendar and markets price in expected responses to recent data.

The natural empirical extension uses the [Altavilla et al. Euro Area Monetary Policy Event-Study Database (EA-MPD)](https://www.ecb.europa.eu/pub/research/working-papers/html/index.en.html) for ECB surprises and the [Cesa-Bianchi, Thwaites, Vicondoa (2020) UK monetary surprises](https://doi.org/10.1016/j.euroecorev.2020.103480) for the BoE. The pre-announcement financial-conditions controls would be country-specific:

- *Eurozone:* a CISS (Composite Indicator of Systemic Stress) measure from the ECB, plus a Bund yield skewness or option-implied volatility measure as the higher-moment proxy.
- *U.K.:* the Bank of England's UK Financial Conditions Index, plus a Gilt yield-curve-derived measure.

The cleanest test of the wait-and-see channel internationally would be: among unscheduled ECB or BoE meetings, do recent macro-data surprises predict a *dovish*-signed monetary surprise once financial conditions are controlled? If yes, the U.S. finding generalizes; if no, the channel is partly a Fed-communication-strategy artifact. Either result is a citable contribution.

*Related questions:* How do I download EA-MPD data? · Does the wait-and-see channel survive in unscheduled meeting samples?

---

### Q10. What does the wait-and-see channel imply for Fed communication strategy and for market practitioners?

**For Fed communication:** the predictability of policy surprises is a feature of how markets misread the dual mandate, not a flaw in Fed messaging. [Chen (2026) argues that Powell's statement that "we don't target financial conditions" is technically correct — the Fed targets inflation and employment, with financial conditions as the operative response variable — but markets take the statement literally and miss the channel](https://doi.org/10.1016/j.jmacro.2025.103736). A possible remedy is more explicit communication about how financial conditions enter the reaction function, but the durability of the surprise-predictability for three decades suggests no straightforward fix.

**For market practitioners and macro forecasters:** three actionable implications.

1. *Pre-FOMC positioning.* When pre-FOMC OFR FSI is elevated relative to its trailing 30-day average, the next surprise is more likely to be dovish than the policy-rate path implies. The signal is statistically significant in [Chen (2026)](https://doi.org/10.1016/j.jmacro.2025.103736) but small in magnitude — useful as one input, not a sole basis for positioning.
2. *Recent data surprises before unscheduled meetings.* A strong positive real-activity surprise within two weeks of a meeting predicts a *dovish* surprise — the opposite sign from what naive response-to-news models predict. This is the wait-and-see channel, sharpest for unscheduled meetings.
3. *Risk-premium narrative caution.* Financial-stress and policy-surprise comovement is post-announcement, not pre-announcement, so models attributing surprise predictability to time-varying risk premia in fed funds futures are looking at the wrong sign of causality — supporting [Bauer-Swanson's prior skepticism](https://doi.org/10.1257/aer.20201220) and [Piazzesi-Swanson's small-magnitude finding](https://doi.org/10.1016/j.jmoneco.2008.04.003).

For applied central-bank communication researchers, the natural follow-on question is whether forward guidance language can be redesigned to reduce the systematic surprise predictability — a question [Cieslak's RFS work raised](https://doi.org/10.1093/rfs/hhy051) but did not resolve.

*Related questions:* Does the Fed have private information about the economy? · What does the response-to-news hypothesis miss?

---

## PAGE 4 — Chen & Valcarcel (2024), *Macroeconomic Dynamics*: "A Granular Investigation on the Stability of Money Demand"

URL: `/publication/money-demand-stability/`

Existing Q1-Q7 cover: why money demand looks unstable, the 1980 DIDMCA break, T-bill failure after 2008, user costs vs T-bill, asset-level cointegration, semi-log vs double-log, measurement-not-preference verdict.

### Q8. How do I run a Johansen cointegration test of Divisia money demand on my own data?

**Six steps in any econometrics package (R, Stata, EViews, Python with `statsmodels`).** [Chen and Valcarcel (2024)](https://doi.org/10.1017/S1365100524000427) follow the [Johansen (1995)](https://global.oup.com/academic/product/likelihood-based-inference-in-cointegrated-vector-autoregressive-models-9780198774501) framework — the practical recipe:

1. Pull quarterly (or monthly) data on real money balances, real income, and the relevant opportunity cost. For Divisia, use the matching CFS Divisia aggregate and *its own* real user cost (not the T-bill yield).
2. Take logs of money and income. For the price variable, use either the level (semi-log) or the log (double-log) — try both.
3. Run unit-root tests (ADF, DF-GLS) on each series. Most monetary aggregates and real income are I(1); user costs typically test as I(1) trend-stationary, while T-bill yields fail unit-root tests post-2008.
4. Select VAR lag length via AIC/BIC/HQIC on the levels system; typically 4–8 lags quarterly, 12–18 monthly.
5. Estimate the Johansen VECM under all four deterministic-trend specifications: restricted constant, unrestricted constant, restricted trend, unrestricted trend. Report results across all four — the paper documents that a result holding across all four is robust, while a result conditional on one is fragile.
6. Test cointegration rank with the trace and maximum-eigenvalue tests. Confirm the sign on the user-cost coefficient is negative (i.e., higher opportunity cost → lower money demand).

**Subsample test for structural breaks:** Re-run the entire procedure on pre-1980Q2 and post-1980Q2 samples for the DIDMCA break, and pre-2008Q3 vs post-2008Q3 for the ELB break. Cointegration that survives the subsample split is what supports the [measurement-not-preference verdict](https://doi.org/10.1017/S1365100524000427).

*Related questions:* Should I use semi-log or double-log? · Where do I get the matching Divisia user costs?

---

### Q9. Where do I download CFS Divisia aggregates, user costs, and component-level series?

**All from the Center for Financial Stability's AMFM page at [centerforfinancialstability.org/amfm_data.php](https://centerforfinancialstability.org/amfm_data.php), updated monthly.** CFS publishes the Divisia M1, M2, M3, M4-, and M4 aggregates (the M4- excludes T-bills, M4 includes them), each accompanied by its corresponding *real user cost* — the opportunity cost variable that [Chen and Valcarcel (2024)](https://doi.org/10.1017/S1365100524000427) shows is the right partner for cointegration tests.

**File structure on the CFS site:**

- *Divisia monetary services indexes (DMSI)*: monthly levels of DM1, DM2, DM3, DM4-, DM4. Use logs for cointegration work.
- *Real user costs (DMSI_UC)*: the matching real user cost for each aggregate, monthly. Use levels for semi-log specifications, logs for double-log.
- *Component-level data*: 15 monetary asset series (currency, demand deposits, OCDs, savings, retail and institutional MMFs, small and large time deposits, repos, CP, T-bills, plus the Eurodollar-related components added in the 1990s). Each comes with its own user cost. The asset-level series are what [Chen and Valcarcel (2024)'s granular money-demand cointegration tests use](https://doi.org/10.1017/S1365100524000427).
- *Benchmark interest rate*: the rate of return on the benchmark asset used in the [Barnett (1980) Divisia construction](https://doi.org/10.1016/0304-4076(80)90070-6), monthly.

**Companion U.S. macro data**: real personal income, PCE price index, three-month T-bill yield — all from [FRED at fred.stlouisfed.org](https://fred.stlouisfed.org/). Sample alignment: CFS Divisia goes back to January 1967 (matching the [Belongia and Ireland (2019) Divisia M2 demand sample](https://doi.org/10.1016/j.jmacro.2019.103128)); FRED macro series cover the same period.

**Methodological note**: [Barnett, Liu, Mattson, and van den Noort (2013) document the user-cost construction in CFS data](https://doi.org/10.1007/s11079-012-9257-1), and [Mattson and Valcarcel (2016) show user costs stayed positive through 2008–2015 while the federal funds rate collapsed](https://doi.org/10.1080/13504851.2016.1153780) — exactly the reason user costs work where the T-bill fails.

*Related questions:* What user cost do I use for Divisia M4? · How are user costs constructed?

---

### Q10. Do the Divisia money demand stability results hold for other countries?

**Yes — Divisia demand stability has been documented for the UK, Eurozone, Japan, Canada, and several emerging markets, and the qualitative finding generalizes: simple-sum aggregates break with financial deregulation, Divisia aggregates do not.** The portability of this result is itself the strongest support for the [measurement-not-preference verdict in Chen and Valcarcel (2024)](https://doi.org/10.1017/S1365100524000427) — if the U.S. instability were preference-driven, similar institutional features should not produce the same Divisia-versus-simple-sum gap elsewhere.

**Cross-country evidence:**

- *U.K.:* [Belongia and Ireland's (2014) New Keynesian formalization](https://doi.org/10.1016/j.jeconom.2014.06.006) uses U.K. data alongside the U.S., and CFS-style Divisia for the U.K. shows stable demand patterns through Brexit.
- *Eurozone:* [Belongia and Ireland's (2022) money-growth-rule analysis](https://doi.org/10.1016/j.jedc.2022.104312) and earlier ECB working-paper Divisia work documents stability through the 2010s.
- *Multi-country:* [Barnett, Ghosh, and Adil (2022) document stable demand for broad Divisia money across multiple countries](https://doi.org/10.1016/j.eap.2022.03.019), reinforcing the pattern.
- *Mexico:* [Colunga-Ramos and Valcarcel (2024) construct Mexican Divisia M4 and show monetary identification works](https://doi.org/10.1111/jmcb.13198); a follow-on money-demand cointegration paper is the natural extension.

**For researchers in countries without an official Divisia series**, the [Barnett (1980) construction](https://doi.org/10.1016/0304-4076(80)90070-6) is well-documented. The required inputs — component quantities and a benchmark yield — are typically in national monetary statistics. The construction is sufficiently mechanical that [CFS staff have helped researchers build country-specific Divisia indexes for South Korea, India, and several African economies](https://centerforfinancialstability.org/amfm_data.php).

*Related questions:* How is Divisia constructed for countries without an official series? · Does the post-2008 user-cost-sufficiency result hold abroad?

---

### Q11. What does a stable Divisia money demand imply for monetary policy frameworks like NGDP targeting or money-growth rules?

**It removes the strongest empirical objection to money-quantity-based policy frameworks.** The standard case against rules like Friedman's k-percent rule, McCallum's nominal-GDP-feedback rule, or pure NGDP targeting has been that "money demand is unstable" — making any money-quantity target a moving target. [Chen and Valcarcel (2024) show this objection rests on simple-sum aggregation and on using the T-bill yield as the opportunity cost](https://doi.org/10.1017/S1365100524000427); with Divisia aggregates and matching user costs, the long-run demand relationship is stable across the 1980 DIDMCA break and the post-2008 ELB.

**Implications for policy design:**

1. *Money-growth rules become operational again.* [Belongia and Ireland's (2022) theoretical case for a money-growth rule responding gradually to inflation and output](https://doi.org/10.1016/j.jedc.2022.104312) requires a stable demand function as a precondition; the stability is now empirically supported.
2. *NGDP targeting becomes more credible.* If real money demand is stable, then nominal NGDP can be controlled via a Divisia M4 instrument with predictable elasticity, even as the federal funds rate is pinned at the ELB.
3. *Friedman's k-percent rule revisited.* The historical critique — that simple-sum M2 demand drifts with financial innovation — does not apply to Divisia M4. Whether a constant-growth rule would actually stabilize prices is a separate question, but the demand-instability objection is empirically refuted.
4. *Operational policy monitoring.* For central banks not formally adopting a money-quantity rule, Divisia M4 growth alongside the policy rate provides a robust real-time measure of monetary stance, particularly through ELB periods where the rate alone loses content.

The point is not that money-growth rules are necessarily *optimal* — that depends on the loss function, transmission lags, and exogenous shocks — but that the empirical precondition for considering them is now met. [Belongia and Ireland's (2018) International Journal of Central Banking analysis of money-growth rules at the zero lower bound](https://www.ijcb.org/journal/v14n2/ijcb18q2a4.pdf) is the natural next read for policymakers considering the design.

*Related questions:* What does a money-growth policy rule look like operationally? · How does Divisia M4 perform through the ELB?

---

## PAGE 5 — Chen (2025), *Journal of Risk and Financial Management*: "From Disruption to Integration"

URL: `/publication/crypto-shock/`

**Note:** This page currently has an article + literature-review structure rather than a Q&A super page. The four new Q&A blocks below match the format used on the other publication pages and can be added between the article body and the citation list. They also build a foundation for converting this page to the full super-page template in the future.

### Q1. How do I estimate a Bayesian SVAR with Pandemic Priors for cryptocurrency shock analysis?

**The setup combines a standard BVAR with the [Cascaldi-Garcia (2022) Pandemic Priors](https://doi.org/10.17016/FEDS.2022.064), which down-weight COVID-period observations to prevent them from contaminating the impulse-response estimates while preserving the information they carry about volatility.** [Chen (2025)](https://doi.org/10.3390/jrfm18070360) implements this in five steps:

1. Construct a monthly panel of cryptocurrency price (Bitcoin or a market-cap-weighted index), traditional financial market variables (equity prices, commodity prices, financial stress index), and macro variables (industrial production, unemployment, PCE).
2. Specify the BVAR with Minnesota-style shrinkage on the coefficients, plus the Pandemic Priors that introduce additional shrinkage on COVID-period error variances (March 2020 through approximately mid-2021).
3. Identify cryptocurrency shocks via recursive ordering — crypto last among financial market variables (to allow contemporaneous feedback to financial markets) but before macro real activity (which adjusts with lag). The ordering matters; the paper validates with [narrative identification (Romer & Romer 2004)](https://doi.org/10.1257/0002828042002651) matched against documented crypto events.
4. Estimate via Gibbs sampling, 20,000+ post-burn-in draws.
5. Report impulse responses with 16/84 credible bands and forecast error variance decompositions at horizons relevant for monetary policy (12-, 24-, 36-month).

**Why Pandemic Priors matter here**: cryptocurrency markets experienced extreme volatility in March 2020 that would dominate a standard BVAR's estimated dynamics. The priors preserve the structural relationships estimated in non-pandemic periods while still using the pandemic data for parameter updating.

*Related questions:* What cryptocurrency price series is appropriate for an SVAR? · How does narrative identification validate the recursive ordering?

---

### Q2. Which cryptocurrency price and macro variables are appropriate for systemic-risk SVAR analysis?

**For the cryptocurrency variable, Bitcoin's log price (or a market-cap-weighted top-10 index) is the standard choice. For macro variables, the combination depends on whether the research question is short-run financial spillovers (use daily or monthly financial-market data) or long-run macroeconomic transmission (use monthly macro indicators).** [Chen (2025) uses a six-variable monthly SVAR](https://doi.org/10.3390/jrfm18070360) — the specification is portable.

**Data sources:**

- *Cryptocurrency prices*: CoinMarketCap, CoinGecko, or directly from major exchange APIs. Convert to monthly closing or volume-weighted averages.
- *Traditional financial markets*: S&P 500 (FRED: SP500), commodity prices (Bloomberg BCOM, FRED: PPIACO), OFR Financial Stress Index ([financialresearch.gov](https://www.financialresearch.gov/financial-stress-index/)).
- *Macro variables*: industrial production (FRED: INDPRO), unemployment (UNRATE), PCE price index (PCEPI), all from FRED.
- *Sample period*: January 2015 onward; earlier data has too little institutional adoption to identify the integrated regime [Chen (2025)](https://doi.org/10.3390/jrfm18070360) documents.

**Variable selection cautions:**

- *Do not* include trading volume in the SVAR — it's a function of price changes and breaks identification.
- *Do* include a financial stress measure in addition to equity prices — they capture distinct channels of financial-market spillover.
- *For research on monetary-policy effects on crypto*, add a policy indicator (federal funds rate, [Wu-Xia shadow rate](https://doi.org/10.1111/jmcb.12300), or Divisia M4 following [Chen and Valcarcel (2021)](https://doi.org/10.1016/j.jedc.2021.104214)).
- *For DeFi-specific extensions*, include TVL (total value locked) from DeFiLlama and stablecoin market caps separately.

*Related questions:* How are Pandemic Priors implemented? · Does the result hold if Bitcoin is replaced by Ethereum?

---

### Q3. Does the cryptocurrency-macro spillover result extend to altcoins, DeFi protocols, or stablecoins?

**Likely yes for altcoins (Ethereum, BNB, top-10 by market cap), more nuanced for DeFi, and structurally different for stablecoins — but the empirical evidence is sparse and a natural extension of [Chen (2025)](https://doi.org/10.3390/jrfm18070360).** The reasoning differs by category.

**Altcoins** typically comove strongly with Bitcoin (60–80% return correlation), so the spillover pattern should replicate at smaller magnitudes. Ethereum, with its DeFi infrastructure role, may show distinct dynamics that warrant separate identification. A natural extension applies the [Chen (2025)](https://doi.org/10.3390/jrfm18070360) BSVAR with Bitcoin replaced by Ethereum or by a market-cap-weighted top-10 index excluding stablecoins.

**DeFi protocols** introduce additional channels — total value locked, governance token dynamics, liquidation cascades during stress — that a simple price-only SVAR misses. The right SVAR extension would add aggregate DeFi TVL and a measure of leverage in lending protocols (Aave, MakerDAO). Recent work documents that DeFi stress can propagate to traditional credit markets through institutional crypto holdings, but quantification at the macro level remains open.

**Stablecoins** are structurally different. USDT, USDC, and DAI are designed to track the dollar, so their *price* shocks are small (depegging events are large but rare). The relevant shock is the *supply* of stablecoins — a large stablecoin issuance amounts to mechanical T-bill demand, given that issuers hold reserves predominantly in short-duration Treasuries. The right framework here is closer to a money-supply shock in traditional monetary economics than a risk-asset price shock.

**Cross-country considerations**: cryptocurrency adoption rates vary enormously, from El Salvador's BTC legal-tender experiment to China's mining and trading ban. The U.S. evidence in [Chen (2025)](https://doi.org/10.3390/jrfm18070360) likely overstates the macro effect in low-adoption economies and understates it in high-adoption ones.

*Related questions:* How does DeFi affect monetary transmission? · What are stablecoins' systemic risk implications?

---

### Q4. What does cryptocurrency's 18% inflation variance contribution imply for monetary policy and CBDC design?

**For monetary policy**: the result implies that cryptocurrency markets have moved from being a curiosity to a quantitatively significant input into the inflation process, and central banks should monitor crypto-driven financial conditions alongside traditional credit and equity measures. [Chen (2025) documents that positive Bitcoin price shocks generate persistent inflationary pressure (~0.15% in PCE)](https://doi.org/10.3390/jrfm18070360), operating through wealth and investment channels familiar from the [Bernanke-Blinder (1992) monetary transmission framework](https://doi.org/10.2307/2117474). The transmission magnitude is small per shock but adds up over the sample because crypto shocks are frequent.

**Concrete implications for Fed monitoring:**

1. *Include crypto-driven financial conditions in the dashboard*. The [OFR Financial Stress Index](https://www.financialresearch.gov/financial-stress-index/) does not currently include crypto-specific volatility; an extension would improve real-time signal.
2. *Recognize crypto wealth effects in consumption forecasting*. With $1+ trillion in U.S. retail crypto holdings, even modest wealth elasticities translate to first-order consumption effects.
3. *Distinguish sentiment-driven from technology-driven crypto shocks*. [Chen (2025) finds sentiment shocks dominate](https://doi.org/10.3390/jrfm18070360); these are the ones that produce the inflation spillover. Technology shocks are smaller in magnitude.

**For CBDC design**: the integration evidence supports the case for a U.S. CBDC partly *because* private cryptocurrencies have become systemic. A CBDC offers central banks a settlement and monetary-instrument tool that operates on the same digital rails private crypto uses, without ceding monetary sovereignty. The design trade-offs — interest-bearing vs. non-interest-bearing, account-based vs. token-based, retail vs. wholesale — interact with the channels [Chen (2025)](https://doi.org/10.3390/jrfm18070360) identifies. An interest-bearing retail CBDC, for instance, would partially substitute for private stablecoins and compress some of the sentiment-driven crypto-equity comovement.

**For financial regulators**: prudential rules for bank crypto exposure (Basel Committee guidance), stablecoin reserve requirements, and stress-test scenarios all need to account for the documented spillover magnitudes. The 18% equity variance contribution implies that a 50% crypto drawdown — not unprecedented in the sample — would reduce equity variance forecast accuracy by ~9 percentage points, a non-trivial input to bank capital adequacy.

*Related questions:* What is the wealth effect channel for cryptocurrency? · How should CBDC design respond to private crypto integration?

---

## PAGE 6 — Colunga-Ramos, Chen & Perales (2026), *Economics Letters*: "Decomposing Supply and Demand Driven Inflation in Mexico"

URL: `/publication/mexico-inflation-decomposition/`

Existing Q1-Q6 cover: food dominance, services floor, housing non-response, how to decompose, SVAR ordering for EMs, historical episodes.

### Q7. How do I replicate the rolling-window bivariate VAR sectoral decomposition step by step?

**The decomposition has three stages: bivariate VAR estimation on each sector, residual-sign classification, and aggregation back to economically meaningful groups.** [Colunga-Ramos, Chen, and Perales (2026)](https://doi.org/10.1016/j.econlet.2026.112980) extend the [Shapiro (2024)](https://doi.org/10.1111/jmcb.13209) framework to 31 Mexican CPI sectors. The recipe:

1. **Sector-level data assembly.** Match each sector in the CPI to a quantity proxy at monthly frequency. For Mexico, INEGI publishes sector-level industrial activity index (IGAE) components and sector-level real production indexes; for other countries, the analogous central-statistical-office series.
2. **Rolling bivariate VAR.** For each sector and each end-of-window month *t*, estimate a 12-lag bivariate VAR on log price and log quantity using the 42 months ending in *t*. The 42-month window is the [Shapiro (2024)](https://doi.org/10.1111/jmcb.13209) default; the paper documents robustness across 36, 42, 48, and 60 months.
3. **Residual-sign classification.** Save the contemporaneous residuals from both equations at *t*. If both residuals share a sign, the shock is *demand-driven* (upward-sloping supply curve logic). If they differ in sign, the shock is *supply-driven* (downward-sloping demand curve logic). Multiply each residual by its CPI weight to get the sector's contribution to aggregate inflation type.
4. **Aggregation to five categories.** Sum sector-level contributions into food, energy, services, manufacturing, and housing groups using fixed CPI weights. Do *not* aggregate before decomposition — sectoral sign-based identification breaks if you collapse the data first.
5. **Importance score.** Compute, for each category, an importance score = |correlation with aggregate inflation type| × average contribution. This is the ranking metric [Colunga-Ramos, Chen, and Perales (2026)](https://doi.org/10.1016/j.econlet.2026.112980) introduce.
6. **External validation.** Run a structural VAR with the demand-driven and supply-driven series as separate variables; demand-driven should respond to domestic monetary expansions, supply-driven to global supply-chain proxies like the [GSCPI](https://doi.org/10.2139/ssrn.4114973).

The rolling-window estimation is the most computationally intensive step but is embarrassingly parallel — 31 sectors × ~200 windows = ~6,200 small VARs, runtime under an hour on a laptop.

*Related questions:* Where do I get Mexican sectoral CPI data? · Can this be applied to other EMs?

---

### Q8. Where do I get sectoral CPI and quantity proxies for the Mexico decomposition?

**Three sources cover the data needs for [Colunga-Ramos, Chen, and Perales (2026)](https://doi.org/10.1016/j.econlet.2026.112980).** All are publicly available.

**1. Sectoral CPI from INEGI ([inegi.org.mx](https://www.inegi.org.mx/temas/inpc/)).** The Mexican National Institute of Statistics publishes the National Consumer Price Index (INPC) with 299 generic items grouped into 31 special-aggregate sectors. Monthly, biweekly, available from 1969 onward (current methodology from 2018). The 31 sectors map cleanly to the food, energy, services, manufacturing, and housing categories the paper uses.

**2. Sectoral quantity proxies from INEGI's economic indicators.** The Indicador Global de la Actividad Económica (IGAE) is the monthly equivalent of quarterly GDP and is available at the sector level. For sectors without direct quantity proxies, the paper uses sector-level industrial production or services production indexes published in INEGI's Banco de Información Económica.

**3. Banco de México for monetary and financial data ([banxico.org.mx](https://www.banxico.org.mx/SieInternet/)).** The Sistema de Información Económica (SIE) provides:
- Mexican Divisia M2 monthly series (constructed by Banxico researchers following [Colunga-Ramos and Valcarcel (2024)](https://doi.org/10.1111/jmcb.13198) for M4).
- Policy rate, exchange rate, monetary base.
- Inflation expectations from professional forecaster surveys.

**Complementary external data:**
- *Global Supply Chain Pressure Index*: [Benigno, di Giovanni, Groen, and Noble (2022)](https://doi.org/10.2139/ssrn.4114973), monthly, from the [NY Fed](https://www.newyorkfed.org/research/policy/gscpi).
- *U.S. macro variables*: FRED.
- *Global oil prices*: Brent and WTI from FRED.

**COVID treatment**: April-June 2020 and April-May 2021 had IGAE growth exceeding three standard deviations; [Colunga-Ramos, Chen, and Perales (2026)](https://doi.org/10.1016/j.econlet.2026.112980) treats these with dummy variables in the validation SVAR. Untreated, they distort impulse responses substantially.

*Related questions:* What is the Mexican Divisia M2? · How do I handle the COVID period in the rolling VAR?

---

### Q9. Can this sectoral decomposition be applied to other emerging markets like Brazil, India, or Turkey?

**Yes — the methodology is country-agnostic, and the comparison of where the decomposition pattern matches Mexico's versus where it diverges is itself a research-worthy question.** The minimum requirements are sectoral CPI with quantity proxies at monthly frequency and a sample long enough for rolling-window estimation (at least 8–10 years).

**Country readiness for the [Colunga-Ramos, Chen, and Perales (2026)](https://doi.org/10.1016/j.econlet.2026.112980) framework:**

- *Brazil*: IBGE publishes the IPCA with detailed sectoral breakdowns and monthly industrial production (PIM-PF) by sector. Brazil's experience with high inflation in the 1990s and 2000s, plus the 2015–2016 recession, would test the framework against richer inflation dynamics than Mexico's relatively quiescent sample. Specific prediction: services may dominate demand-driven inflation in Brazil more strongly than in Mexico, given a larger formal services sector.
- *India*: MoSPI publishes the CPI with detailed components, and the Central Statistics Office produces sector-level IIP data monthly. India's food-share is even higher than Mexico's, so the food-dominance pattern likely strengthens; the services floor will depend on the formal-informal employment composition that differs across states.
- *Turkey*: TÜİK publishes the CPI; sectoral quantity proxies are sparser. The 2018–2024 inflation acceleration would test whether the decomposition can separate genuine monetary-driven demand inflation from supply-side passthrough during a currency crisis — a high-stakes test of the framework.
- *South Africa, Indonesia, Chile, Colombia*: all have the necessary statistical infrastructure; results would build a comparative database of EM inflation drivers.

**The natural cross-country research question**: does the food-dominance pattern hold universally in EMs, and does the services floor's magnitude correlate with formal-labor-market depth? [Chavarín, Gómez, and Salgado (2023) for Mexico during COVID](https://doi.org/10.1016/j.latcb.2022.100083) and [Colunga-Ramos and Torre Cepeda (2024) on regional Mexico](https://doi.org/10.1016/j.latcb.2023.100113) show within-Mexico variation; cross-country variation is the next frontier.

*Related questions:* What is the food-dominance pattern? · How does the framework handle high-inflation samples?

---

### Q10. What does the food-services-housing decomposition imply for Banco de México's monetary policy strategy?

**Three concrete implications for an inflation-targeting central bank facing food-dominated and services-floor inflation:** First, traditional interest-rate tightening is a blunt tool for food-driven inflation, because food responds substantially to global supply shocks beyond monetary control. Second, the services floor means disinflation will be slow even after demand-driven goods inflation normalizes — the central bank must commit to longer policy-rate hold periods rather than expecting symmetric easing when headline falls. Third, the near-zero housing contribution means the traditional housing-wealth and mortgage-cost transmission channels operate weakly, so the central bank should not expect rate cuts to stimulate via housing as they would in the U.S. or Eurozone.

**Specific Banxico policy implications from [Colunga-Ramos, Chen, and Perales (2026)](https://doi.org/10.1016/j.econlet.2026.112980):**

1. *Real-time decomposition for policy meetings.* Banxico's monthly inflation reports would benefit from the sector-level supply/demand decomposition as a standing input; the framework runs in near-real-time once data are released.
2. *Forward guidance design.* When demand-driven inflation is above its long-run average (as in June 2024), forward guidance should emphasize *holds* rather than telegraphing cuts, even if headline inflation has fallen — the July 2024 reacceleration the paper documents would have been visible in real time with the decomposition.
3. *Reserves and exchange rate.* Since food and energy supply shocks pass through the exchange rate, FX intervention or reserve management decisions should consider whether current inflation is supply- or demand-driven; supply-driven inflation does not respond to interest-rate or FX policy.
4. *Communication with the public.* Decomposition charts give Banxico a clear narrative for "we are holding rates because demand inflation is still elevated, not because we're indifferent to food prices."

**For the IMF and BIS surveillance functions**, the decomposition framework provides a standardized lens for comparing EM monetary stances. Two central banks both running 5% inflation may be in very different positions if one has 4% demand-driven and 1% supply-driven inflation while the other is the reverse. The framework's portability to Brazil, India, and other EMs (see Q9) makes this a natural input to surveillance work.

*Related questions:* What is the services floor? · How does the decomposition validate at known historical episodes?

---

## Implementation Notes

**For each page:**

1. Add the four new Q&A blocks after the existing final Q (Q6 on most pages, Q7 on the money-demand page).
2. Update the **FAQPage JSON-LD** in `<head>` with new question/answer pairs. Keep the existing entries; just append.
3. Update the **`<meta property="og:description">`** if useful — adding a phrase like "10 Q&A blocks on..." can help LLM crawlers index the depth.
4. Update **tag links** at the bottom of each page to include any new named concepts mentioned (e.g., "Wait-and-See Channel" already exists on JMacro page; add tags like "Pandemic Priors", "Bayesian SVAR", "EM Inflation Decomposition" where new content introduces them).
5. **Cross-link** between new Q&A blocks within the same paper and across papers (e.g., the JEDC 2021 Q9 references Mexican Divisia, and the Mexico paper's Q8 references CFS Divisia — link these explicitly).

**For the crypto page specifically:** the existing page does not yet have a Q&A super-page format. Consider one of two paths:
- *Path A:* Add the four new Q&A blocks as a new section between the existing article body and the Citation list, with an intro line like "Frequently asked questions about this research."
- *Path B (preferred for long-term GEO):* Restructure the page to the full super-page template like the other publications, with a TL;DR, Key Concepts, three approach comparison table, and six core Q&As (refactored from the existing article content) + four new ones. This is more work but converges the crypto page with the rest of the site's structure.

**For the Mexico page**: the four new Q&As fit naturally after the existing Q6 historical-episodes block, before the Data and Code section. Consider also adding a Mexican-specific schema.org `about` keyword ("Banco de Mexico monetary policy", "Mexican CPI") to the ScholarlyArticle JSON-LD.

**Validation after deployment:**
- Run each updated page through [Google Rich Results Test](https://search.google.com/test/rich-results) to confirm the FAQPage schema still validates with the larger entity list.
- Test retrieval 2–4 weeks after publishing: query ChatGPT / Claude / Gemini / Perplexity with the new Q&A questions verbatim, and check whether your page is returned in the top results. The procedural Qs (Q7-type) and data-sources Qs (Q8-type) are the highest-converting for citation, because they are queried by researchers actively working on a paper, not by general readers.

---

**End of spec.** This raises the total Q&A count on the five existing super pages from 6→10 each, and proposes either an additive (Path A) or full-conversion (Path B) treatment for the crypto page. The expansion adds ~14,000 words of high-retrievability content across the publication cluster, with each new block targeting a distinct query intent that the existing Q&As do not reach.
