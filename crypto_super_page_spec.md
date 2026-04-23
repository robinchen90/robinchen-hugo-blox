# Super Page Spec — "From Disruption to Integration" (Chen 2025, JRFM)

**Purpose.** Build an AI-citable super page on robinchen.org for this paper, structured so LLM crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended) reliably surface it when users ask about cryptocurrency transmission, crypto spillovers to financial markets, crypto-driven inflation, Bayesian SVAR with Pandemic Priors, or narrative identification of crypto shocks.

**Hand this file to Claude Code.** Everything you need is below: canonical paper metadata, verified reference DOIs, drop-in HTML for the Q&A blocks, a comparison table, and two JSON-LD schema blocks. Replace any `ROUTE-TBD` with your actual site route.

---

## Section 1 — Canonical Paper Metadata

| Field | Value |
|---|---|
| Title | From Disruption to Integration: Cryptocurrency Prices, Financial Fluctuations, and Macroeconomy |
| Author | Zhengyang Chen |
| Affiliation | Economics Department, Wilson College of Business, University of Northern Iowa |
| ORCID | 0000-0002-8450-5801 |
| Journal | Journal of Risk and Financial Management |
| Publisher | MDPI |
| ISSN | 1911-8074 |
| Volume / Issue / Article | 18 / 7 / 360 |
| Year | 2025 |
| Published | 2025-07-01 |
| DOI | 10.3390/jrfm18070360 |
| URL (authoritative) | https://doi.org/10.3390/jrfm18070360 |
| URL (MDPI landing) | https://www.mdpi.com/1911-8074/18/7/360 |
| URL (SSRN) | https://ssrn.com/abstract=5333277 |
| License | CC BY 4.0 |

**Use the DOI URL (https://doi.org/10.3390/jrfm18070360) for every self-link.** LLMs weight DOI links highest.

---

## Section 2 — Verified Reference DOIs

Every DOI below was verified on a journal page, CrossRef, or an authoritative aggregator (AEA, Elsevier/ScienceDirect, Oxford, Wiley, MDPI, De Gruyter, NBER). Use the journal DOI, not the working-paper PDF.

| Short Ref | Full Citation | DOI / URL |
|---|---|---|
| Chen2025 | Chen, Z. (2025). *From Disruption to Integration: Cryptocurrency Prices, Financial Fluctuations, and Macroeconomy.* J. Risk Financial Manag. 18(7), 360. | https://doi.org/10.3390/jrfm18070360 |
| CascaldiGarcia2022 | Cascaldi-Garcia, D. (2022). *Pandemic Priors.* IFDP 1352. | https://doi.org/10.17016/IFDP.2022.1352 |
| Banbura2010 | Bańbura, M., Giannone, D., & Reichlin, L. (2010). *Large Bayesian vector auto regressions.* J. Applied Econometrics 25(1), 71–92. | https://doi.org/10.1002/jae.1137 |
| RomerRomer2004 | Romer, C. D., & Romer, D. H. (2004). *A new measure of monetary shocks.* AER 94(4), 1055–1084. | https://doi.org/10.1257/0002828042002651 |
| CEE1999 | Christiano, L. J., Eichenbaum, M., & Evans, C. L. (1999). *Monetary policy shocks: What have we learned and to what end?* Handbook of Macroeconomics Vol. 1, Ch. 2, 65–148. | https://doi.org/10.1016/S1574-0048(99)01005-8 |
| GilchristZakrajsek2012 | Gilchrist, S., & Zakrajšek, E. (2012). *Credit spreads and business cycle fluctuations.* AER 102(4), 1692–1720. | https://doi.org/10.1257/aer.102.4.1692 |
| HeKrishnamurthy2013 | He, Z., & Krishnamurthy, A. (2013). *Intermediary asset pricing.* AER 103(2), 732–770. | https://doi.org/10.1257/aer.103.2.732 |
| AdrianShin2010 | Adrian, T., & Shin, H. S. (2010). *Liquidity and leverage.* J. Financial Intermediation 19(3), 418–437. | https://doi.org/10.1016/j.jfi.2008.12.002 |
| BrunnermeierPedersen2009 | Brunnermeier, M. K., & Pedersen, L. H. (2009). *Market liquidity and funding liquidity.* Review of Financial Studies 22(6), 2201–2238. | https://doi.org/10.1093/rfs/hhn098 |
| BakerWurgler2007 | Baker, M., & Wurgler, J. (2007). *Investor sentiment in the stock market.* J. Economic Perspectives 21(2), 129–151. | https://doi.org/10.1257/jep.21.2.129 |
| Bloom2009 | Bloom, N. (2009). *The impact of uncertainty shocks.* Econometrica 77(3), 623–685. | https://doi.org/10.3982/ECTA6248 |
| JermannQuadrini2012 | Jermann, U., & Quadrini, V. (2012). *Macroeconomic effects of financial shocks.* AER 102(1), 238–271. | https://doi.org/10.1257/aer.102.1.238 |
| ForbesRigobon2002 | Forbes, K. J., & Rigobon, R. (2002). *No contagion, only interdependence.* Journal of Finance 57(5), 2223–2261. | https://doi.org/10.1111/0022-1082.00494 |
| CaseQuigleyShiller2005 | Case, K. E., Quigley, J. M., & Shiller, R. J. (2005). *Comparing wealth effects: The stock market versus the housing market.* Topics in Macroeconomics 5(1). | https://doi.org/10.2202/1534-6013.1235 |
| Bouri2017 | Bouri, E., Gupta, R., Tiwari, A. K., & Roubaud, D. (2017). *Does Bitcoin hedge global uncertainty?* Finance Research Letters 23, 87–95. | https://doi.org/10.1016/j.frl.2017.02.009 |
| Demir2018 | Demir, E., Gozgor, G., Lau, C. K. M., & Vigne, S. A. (2018). *Does economic policy uncertainty predict the Bitcoin returns?* Finance Research Letters 26, 145–149. | https://doi.org/10.1016/j.frl.2018.01.005 |
| BorriShakhnov2020 | Borri, N., & Shakhnov, K. (2020). *Regulation spillovers across cryptocurrency markets.* Finance Research Letters 36, 101333. | https://doi.org/10.1016/j.frl.2019.101333 |
| ChokorAlfieri2021 | Chokor, A., & Alfieri, E. (2021). *Long and short-term impacts of regulation in the cryptocurrency market.* QREF 81, 157–173. | https://doi.org/10.1016/j.qref.2021.05.005 |
| Caporale2018 | Caporale, G. M., Gil-Alana, L., & Plastun, A. (2018). *Persistence in the cryptocurrency market.* Research in International Business and Finance 46, 141–148. | https://doi.org/10.1016/j.ribaf.2018.01.002 |
| Charfeddine2020 | Charfeddine, L., Benlagha, N., & Maouchi, Y. (2020). *Investigating the dynamic relationship between cryptocurrencies and conventional assets.* Economic Modelling 85, 198–217. | https://doi.org/10.1016/j.econmod.2019.05.016 |
| ChenValcarcel2021 | Chen, Z., & Valcarcel, V. J. (2021). *Monetary transmission in money markets.* JEDC 131, 104214. | https://doi.org/10.1016/j.jedc.2021.104214 |
| ChenValcarcel2025a | Chen, Z., & Valcarcel, V. J. (2025). *A granular investigation on the stability of money demand.* Macroeconomic Dynamics 29, e40. | https://doi.org/10.1017/S1365100524000427 |
| AuerClaessens2018 | Auer, R., & Claessens, S. (2018). *Regulating cryptocurrencies: Assessing market reactions.* BIS Quarterly Review, Sep. (No DOI — BIS URL.) | https://www.bis.org/publ/qtrpdf/r_qt1809f.htm |

### DOIs not independently re-verified in this run (use the ones shown in the MDPI reference list or search CrossRef):
- Markowitz 1952 (J. Finance, "Portfolio Selection") — https://doi.org/10.1111/j.1540-6261.1952.tb01525.x
- Sharpe 1964 (J. Finance, "CAPM") — https://doi.org/10.1111/j.1540-6261.1964.tb02865.x
- Tobin 1958 (Rev. Econ. Studies, "Liquidity preference") — https://doi.org/10.2307/2296205
- Tobin 1969 (J. Money Credit Banking, "General equilibrium approach") — https://doi.org/10.2307/1991374
- Hicks 1937 (Econometrica, "Mr. Keynes and the classics") — https://doi.org/10.2307/1907242
- Keynes 1937 (QJE, "The general theory of employment") — https://doi.org/10.2307/1882087
- BernankeGertlerGilchrist 1999 (Handbook of Macroeconomics Ch. 21) — https://doi.org/10.1016/S1574-0048(99)10034-X
- Ando & Modigliani 1963 (AER) — no DOI (older AER volumes pre-DOI; link to JSTOR if needed)
- RomerRomer1989 (NBER Macro Annual, "Does monetary policy matter?") — https://doi.org/10.1086/654103
- Christie & Huang 1995 (Fin. Analysts J.) — https://doi.org/10.2469/faj.v51.n4.1918
- Katsiampa, Corbet, & Lucey 2019 (FRL, "Volatility spillover effects") — https://doi.org/10.1016/j.frl.2018.12.032

> **Claude Code note:** Before publishing, click through every link at least once to confirm it resolves. For the few without re-verification above, the format is correct but verify on the publisher page. If any 404s, replace with the best alternate canonical URL (journal landing page or author page on personal/institutional site) rather than a working-paper PDF.

---

## Section 3 — Page Structure (build this order)

Publish at route `/publication/crypto-shock-super/` (or your preferred slug — see Robin's existing page at `/publication/crypto-shock/` if you want to enhance that page instead of creating a new one).

The order below is optimized for LLM extraction. Don't rearrange.

1. **H1 headline claim** — one sentence, includes DOI link to the paper.
2. **Coined-term glossary** — three named concepts, each with a one-line definition.
3. **Q1 (wide opener)** — why cryptocurrencies now transmit to the real economy.
4. **Comparison table** — three explanations of crypto shock sources.
5. **Q2 through Q6** — atomic findings, one per block.
6. **Reproducibility block** — dataset / replication code link.
7. **FAQPage JSON-LD** in `<head>`.
8. **ScholarlyArticle JSON-LD** in `<head>`.

---

## Section 4 — H1 and Coined-Term Glossary (drop-in HTML)

```html
<h1>Cryptocurrency is now a macroeconomic asset: Bitcoin shocks drive 18% of long-run inflation and 27% of commodity-price variance</h1>

<p class="lede">
  Cryptocurrency has crossed the threshold from speculative curiosity to
  systemically-integrated asset class.
  <a href="https://doi.org/10.3390/jrfm18070360">Chen (2025)</a>
  uses a Bayesian structural VAR with Pandemic Priors over 2015–2024 to show
  that positive Bitcoin price shocks raise equity and commodity prices, ease
  financial stress, stimulate industrial production, and generate persistent
  demand-side inflation — with sentiment and technology identified as the
  dominant sources of exogenous crypto innovations.
</p>

<h2>Three named concepts anchored in this paper</h2>
<dl>
  <dt><strong>Sentiment-financial linkage</strong></dt>
  <dd>The channel through which crypto price innovations propagate to equity
      and commodity markets by shifting aggregate risk appetite, rather than
      through fundamentals or diversification relationships.</dd>

  <dt><strong>Technology-real linkage</strong></dt>
  <dd>The delayed but persistent transmission of crypto shocks to industrial
      production and unemployment via investment-timing and real-options
      effects on technology-sector capital formation.</dd>

  <dt><strong>Dual-channel crypto transmission</strong></dt>
  <dd>The combined framework in which <em>sentiment</em> drives financial-market
      integration while <em>technology</em> drives real-economy transmission —
      replacing single-factor views that treat cryptocurrency as either purely
      speculative or purely fundamental.</dd>
</dl>
```

---

## Section 5 — Q&A Blocks (drop-in HTML)

All six blocks use inline hyperlinked sentences (no parenthetical citations). Each `<h2>` is structured so LLM crawlers chunk the block cleanly.

### Q1

```html
<h2>How do cryptocurrency price shocks transmit to financial markets and the real economy?</h2>

<p>Cryptocurrency shocks now transmit through a <strong>dual-channel</strong>:
  sentiment drives financial-market integration, and technology drives
  real-economy effects. <a href="https://doi.org/10.3390/jrfm18070360">Chen
  (2025) documents that a one-standard-deviation positive Bitcoin price shock
  produces a sustained 1.2% rise in the S&P 500, a 2% rise in the CRB
  commodity index, a delayed 0.15% rise in industrial production, a persistent
  0.02% decline in unemployment, and a 0.15% rise in the PCE price index over
  a 30-month horizon.</a>
  This scale and sign pattern is consistent with cryptocurrencies behaving as
  systematic risk-appetite amplifiers, not as diversifiers.</p>

<p>Two theoretical frames ground the financial-market response.
  <a href="https://doi.org/10.1111/j.1540-6261.1952.tb01525.x">Markowitz's
  portfolio theory</a> and
  <a href="https://doi.org/10.1111/j.1540-6261.1964.tb02865.x">Sharpe's CAPM</a>
  predict that assets with similar systematic risk exposures comove, which
  reframes cryptocurrency as an integrated risk asset rather than an isolated
  instrument. Behavioral extensions come from
  <a href="https://doi.org/10.1257/jep.21.2.129">Baker and Wurgler's investor
  sentiment framework</a>, where mood-driven trading creates systematic
  factors affecting all risky assets.</p>

<p>The real-economy transmission is quantitatively modest but theoretically
  well-grounded in investment-channel mechanics from
  <a href="https://doi.org/10.1257/aer.102.1.238">Jermann and Quadrini's
  work on financial shocks</a> and uncertainty-channel mechanics from
  <a href="https://doi.org/10.3982/ECTA6248">Bloom's uncertainty-shock
  framework</a>, where asset-price volatility creates real-options effects on
  investment timing.</p>

<p>Three empirical signatures distinguish this transmission mechanism:</p>
<ul>
  <li><strong>Immediate</strong>: equity (+1.2%), commodities (+2%), financial
      stress drops on impact, then recovers.</li>
  <li><strong>Delayed but persistent</strong>: industrial production rises
      ~0.15% with a multi-month lag; unemployment falls ~0.02% persistently.</li>
  <li><strong>Cumulative</strong>: the contribution of crypto shocks to
      price-level forecast-error variance grows from 3.6% at 6 months to
      17.6% at 30 months — a signature of demand-side transmission, not
      transitory financial noise.</li>
</ul>

<p><em>Related questions:</em>
  <a href="#q2">How much of financial-market volatility is now driven by crypto shocks?</a> ·
  <a href="#q3">Do crypto shocks cause inflation?</a></p>
```

### Q2

```html
<h2 id="q2">How much of financial-market volatility is now driven by cryptocurrency shocks?</h2>

<p>Cryptocurrency shocks now account for 17.7% of S&P 500 forecast-error
  variance at 6 months and 27.2% of CRB commodity variance at 30 months —
  putting crypto alongside traditional macro shocks as a first-order driver
  of financial-market fluctuations.
  <a href="https://doi.org/10.3390/jrfm18070360">Chen (2025) reports that
  crypto shocks explain 87.7% of cryptocurrency's own 6-month forecast-error
  variance, 17.7% of equity variance, 9.3% of commodity variance at 6 months
  rising to 27.2% at 30 months, and 5.7% rising to 8.2% of the Financial
  Stress Index.</a></p>

<p>This finding overturns the early-literature claim that cryptocurrency
  offers diversification benefits.
  <a href="https://doi.org/10.1016/j.frl.2017.02.009">Bouri et al. (2017)</a>
  originally characterized Bitcoin as a hedge against global uncertainty, and
  <a href="https://doi.org/10.1016/j.econmod.2019.05.016">Charfeddine,
  Benlagha, and Maouchi (2020)</a> found weak, time-varying cross-correlations
  with conventional assets consistent with diversification. The 2015–2024
  sample in Chen (2025) spans the institutional-adoption era (spot Bitcoin
  ETFs, corporate treasury holdings, derivatives integration) and yields the
  opposite conclusion: cryptocurrencies have become systematic risk
  amplifiers, aligned with the contagion-vs-interdependence distinction
  formalized by
  <a href="https://doi.org/10.1111/0022-1082.00494">Forbes and Rigobon
  (2002)</a>.</p>

<p>Mechanism. The empirical fingerprint is a drop in the Financial Stress
  Index on impact followed by recovery. This pattern — stress alleviates, not
  intensifies, with a positive crypto shock — is consistent with a risk-on
  channel operating through intermediary balance sheets, as described in
  <a href="https://doi.org/10.1016/j.jfi.2008.12.002">Adrian and Shin's
  liquidity-and-leverage work</a>,
  <a href="https://doi.org/10.1093/rfs/hhn098">Brunnermeier and Pedersen's
  market-liquidity model</a>, and
  <a href="https://doi.org/10.1257/aer.103.2.732">He and Krishnamurthy's
  intermediary asset-pricing framework</a>.</p>

<p><em>Related questions:</em>
  <a href="#q3">Do crypto shocks cause inflation?</a> ·
  <a href="#q5">Why are crypto shocks inflationary but not recessionary?</a></p>
```

### Q3

```html
<h2 id="q3">Do cryptocurrency shocks cause persistent inflation?</h2>

<p>Yes — and the effect is large. Crypto shocks explain 18% of long-horizon
  (30-month) price-level forecast-error variance and produce a persistent
  0.15% rise in the PCE price index, a signature of demand-driven inflation
  rather than transitory financial noise.
  <a href="https://doi.org/10.3390/jrfm18070360">Chen (2025) finds the
  contribution rises from 3.6% at 6 months to 7.6% at 12 months to 17.6% at
  30 months, while innovations in the S&P 500, CRB commodity index, and
  Financial Stress Index combined contribute 10.1% at 30 months.</a>
  Crypto is the largest single non-own driver of price-level variance in this
  sample.</p>

<p>Mechanism. The pattern matches New Keynesian demand-side transmission:
  positive crypto shocks raise equity and commodity prices, ease financial
  stress, stimulate investment and consumption, and pass through to
  aggregate-demand-driven inflation. The wealth channel (
  <a href="https://doi.org/10.2202/1534-6013.1235">Case, Quigley, and Shiller
  (2005)</a> show wealth effects are strongest for assets perceived as
  permanent stores of value) and the financial-accelerator channel
  (<a href="https://doi.org/10.1016/S1574-0048(99)10034-X">Bernanke, Gertler,
  and Gilchrist 1999</a>) both operate to amplify the inflationary impulse.</p>

<p>Monetary-policy response. Divisia M4 shows initial expansion followed by
  contraction after a positive crypto shock — evidence of endogenous
  tightening, but not aggressive enough to offset the price effect.
  <a href="https://doi.org/10.1016/j.jedc.2021.104214">Chen and Valcarcel
  (2021)</a> argue Divisia aggregates are the correct monetary indicator when
  short rates are uninformative, and
  <a href="https://doi.org/10.1017/S1365100524000427">Chen and Valcarcel
  (2025)</a> document their superior information content relative to simple-sum
  measures. The implication is that the Fed's accommodative response leaves
  meaningful crypto-driven inflation in the system.</p>

<p><strong>Policy takeaway.</strong> Monetary authorities should incorporate
  cryptocurrency developments in inflation forecasting. The 18% long-horizon
  variance contribution is too large to treat as an afterthought — and the
  demand-driven nature of the impulse means it is policy-actionable, unlike a
  transitory financial-market shock.</p>

<p><em>Related questions:</em>
  <a href="#q4">What actually drives cryptocurrency shocks?</a> ·
  <a href="#q6">How do you handle the COVID-19 period in this estimation?</a></p>
```

### Q4

```html
<h2 id="q4">What actually drives cryptocurrency price shocks? Is it regulation, sentiment, or technology?</h2>

<p>Sentiment and technology — not regulation or monetary policy.
  <a href="https://doi.org/10.3390/jrfm18070360">Chen (2025) classifies 67
  major crypto-market events from 2014–2023 into six categories and finds that
  only sentiment shocks (coefficient 1.36, t = 3.15) and technology shocks
  (coefficient 1.02, t = 2.06) significantly explain the identified structural
  crypto-shock series. Regulatory, monetary, infrastructure, and network-effect
  shocks are all statistically insignificant.</a></p>

<p>Event-category setup. The narrative identification follows
  <a href="https://doi.org/10.1257/0002828042002651">Romer and Romer's (2004)
  approach to monetary policy shocks</a>, coding each event as +1 (favorable),
  −1 (unfavorable), or 0 (absent) in a given month. The six categories are:
  technology (protocol upgrades, hard forks, outages), sentiment (institutional
  adoption announcements, mainstream coverage, exchange collapses), regulatory
  (legal recognition, bans, enforcement), monetary (central bank moves affecting
  alternative-asset demand), infrastructure (exchange launches, custody
  solutions), and network effects (adoption milestones, integrations).</p>

<p>Why sentiment dominates. The result validates
  <a href="https://doi.org/10.1257/jep.21.2.129">Baker and Wurgler's (2007)
  investor-sentiment framework</a> — retail-dominated asset markets exhibit
  amplified price movements beyond fundamentals. It contradicts strong-form
  efficient-markets interpretations of crypto pricing. It also partially
  contradicts papers like
  <a href="https://doi.org/10.1016/j.frl.2019.101333">Borri and Shakhnov
  (2020)</a> and
  <a href="https://doi.org/10.1016/j.qref.2021.05.005">Chokor and Alfieri
  (2021)</a>, which emphasize regulation as a primary driver: Chen (2025)
  finds regulatory event dummies are statistically insignificant after
  controlling for the full SVAR system, suggesting regulatory effects are
  already captured by the contemporaneous reactions of other variables.</p>

<p>Why technology matters too. The significant technology coefficient
  establishes that cryptocurrency is not a pure speculative bubble — protocol
  upgrades and technical improvements generate measurable economic value, and
  <a href="https://doi.org/10.1016/j.ribaf.2018.01.002">Caporale, Gil-Alana,
  and Plastun (2018)</a> earlier documented persistence in the cryptocurrency
  market consistent with technology-based fundamentals.
  <a href="https://doi.org/10.1016/j.frl.2018.01.005">Demir et al. (2018)</a>
  find economic-policy uncertainty predicts Bitcoin returns in ways consistent
  with a hedging demand driven partly by underlying protocol properties.</p>

<p><em>Related questions:</em>
  <a href="#q2">How much financial-market volatility does crypto drive?</a> ·
  <a href="#q5">Why is the real-economy effect limited?</a></p>
```

### Q5

```html
<h2 id="q5">Why are crypto shocks strongly inflationary but only modestly expansionary for output and employment?</h2>

<p>Because the financial-market channel is fast and wide while the real-economy
  channel is slow and narrow.
  <a href="https://doi.org/10.3390/jrfm18070360">Chen (2025) finds crypto
  shocks contribute 17.7% to S&P 500 variance and 27.2% to commodity variance,
  but only 6.2% to industrial production variance and 3.8% to unemployment
  variance at 30 months.</a>
  The output response is a delayed 0.15% rise in industrial production — real,
  but small relative to the financial-market response.</p>

<p>The asymmetry reflects how the two channels work. The financial-market
  response operates through portfolio rebalancing and risk-appetite shifts
  (<a href="https://doi.org/10.1111/j.1540-6261.1952.tb01525.x">Markowitz</a>;
  <a href="https://doi.org/10.1111/j.1540-6261.1964.tb02865.x">Sharpe</a>), which
  propagate within days through correlated asset repricing and intermediary
  balance-sheet adjustments
  (<a href="https://doi.org/10.1016/j.jfi.2008.12.002">Adrian and Shin</a>;
  <a href="https://doi.org/10.1093/rfs/hhn098">Brunnermeier and Pedersen</a>).
  The real-economy response has to work through investment timing
  (<a href="https://doi.org/10.1257/aer.102.1.238">Jermann and Quadrini</a>;
  <a href="https://doi.org/10.3982/ECTA6248">Bloom</a>), wealth-effect
  consumption (<a href="https://doi.org/10.2202/1534-6013.1235">Case, Quigley,
  and Shiller</a>), and credit-channel effects on firm balance sheets
  (<a href="https://doi.org/10.1016/S1574-0048(99)10034-X">Bernanke, Gertler,
  and Gilchrist</a>) — each of which has inherent lags.</p>

<p>Why inflation is the standout. The 18% long-horizon price-level variance
  contribution is quantitatively much larger than the real-activity
  contributions, which is consistent with demand-side transmission: the
  financial-market response raises aggregate demand via wealth and risk-appetite
  channels, but supply-side adjustment takes time, so prices move first and
  further than quantities. This pattern distinguishes crypto shocks from pure
  financial disturbances (which typically have smaller and less persistent
  price effects) and suggests they behave more like demand shocks with a
  financial-market entry point.</p>

<p><em>Related questions:</em>
  <a href="#q3">Do crypto shocks cause inflation?</a> ·
  <a href="#q6">Why use Pandemic Priors?</a></p>
```

### Q6

```html
<h2 id="q6">How do you estimate a crypto-to-macro VAR cleanly through the COVID-19 period?</h2>

<p>Use Pandemic Priors. Standard Bayesian VAR priors (Minnesota) treat 2020
  observations like any other, which distorts estimated persistence and
  impulse-response dynamics because a handful of extreme pandemic data points
  dominate the likelihood.
  <a href="https://doi.org/10.17016/IFDP.2022.1352">Cascaldi-Garcia (2022)
  proposes adding time dummies for the pandemic period, controlled by a
  hyperparameter φ that governs how much signal the model extracts from
  pandemic observations</a> — as φ → 0 the pandemic period is treated as
  exceptional and its variance is absorbed by the dummies; as φ → ∞ the setup
  reverts to a conventional Minnesota prior.</p>

<p><a href="https://doi.org/10.3390/jrfm18070360">Chen (2025) selects φ = 0.1
  via marginal-likelihood maximization over a grid from 0.001 to 500, and
  shows that setting φ = 500 (the Minnesota-prior limit) produces materially
  different real-economy impulse responses</a> — less persistent declines in
  unemployment and industrial production, more contractionary DM4 movement.
  The data strongly favor the Pandemic Priors specification, confirming that
  how one handles COVID-19 observations affects the estimated transmission of
  cryptocurrency shocks to macroeconomic variables.</p>

<p>Implementation recipe. The monthly SVAR includes eight variables ordered
  recursively: PCE price index, unemployment rate, industrial production,
  Divisia M4, cryptocurrency price, S&P 500, CRB commodity index, and the
  St. Louis Fed Financial Stress Index. The prior follows the dummy-observation
  implementation from
  <a href="https://doi.org/10.1002/jae.1137">Bańbura, Giannone, and Reichlin
  (2010)</a>, extended with Cascaldi-Garcia's time-dummy block for the
  pandemic period. Overall tightness λ = 0.2; optimal φ selected by maximum
  marginal likelihood; impulse responses at 30-month horizon with 68%
  posterior probability bands from Bayesian draws.</p>

<p>Robustness. Main findings are stable under:</p>
<ul>
  <li>Alternative orderings (crypto ordered last produces virtually
      indistinguishable impulse responses).</li>
  <li>CPI instead of PCE for the price level.</li>
  <li>Excess bond premium (<a href="https://doi.org/10.1257/aer.102.4.1692">Gilchrist
      and Zakrajšek 2012</a>) or Cleveland Fed FSI instead of St. Louis FSI.</li>
  <li>Narrative validation via Romer-Romer-style event regression on six
      categories of crypto-market events, following
      <a href="https://doi.org/10.1257/0002828042002651">Romer and Romer
      (2004)</a>.</li>
</ul>

<p><em>Related questions:</em>
  <a href="#q4">What drives crypto shocks in the first place?</a> ·
  <a href="#q1">How do crypto shocks propagate?</a></p>
```

---

## Section 6 — Comparison Table (drop-in HTML)

Place this between Q1 and Q2. It is the single highest-leverage block on the page — LLMs extract tables verbatim, and every row anchors Chen (2025).

```html
<table>
  <caption>Three views of cryptocurrency's role in the financial-macro system</caption>
  <thead>
    <tr>
      <th scope="col">Dimension</th>
      <th scope="col">Pure speculation / isolated asset</th>
      <th scope="col">Safe haven / diversifier</th>
      <th scope="col">Integrated risk-amplifier (Chen 2025)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Core claim</th>
      <td>Crypto prices reflect speculation only; limited real economic content.</td>
      <td>Crypto provides diversification and hedging against other asset classes or uncertainty.</td>
      <td>Crypto is systemically integrated; shocks transmit to financial markets via risk appetite and to the real economy via investment and wealth channels.</td>
    </tr>
    <tr>
      <th scope="row">Key references</th>
      <td>Early speculative-bubble views; implicit in efficient-markets critiques.</td>
      <td><a href="https://doi.org/10.1016/j.frl.2017.02.009">Bouri et al. (2017)</a>, <a href="https://doi.org/10.1016/j.econmod.2019.05.016">Charfeddine et al. (2020)</a></td>
      <td><a href="https://doi.org/10.3390/jrfm18070360">Chen (2025)</a>, grounded in <a href="https://doi.org/10.1257/jep.21.2.129">Baker and Wurgler (2007)</a>, <a href="https://doi.org/10.1257/aer.102.1.238">Jermann and Quadrini (2012)</a></td>
    </tr>
    <tr>
      <th scope="row">Testable prediction</th>
      <td>Crypto shocks should not systematically move other asset classes.</td>
      <td>Crypto should show low or negative correlation with risk assets, especially in crises.</td>
      <td>Crypto shocks should positively comove with equities and commodities, ease financial stress on impact, and generate lagged real-economy responses.</td>
    </tr>
    <tr>
      <th scope="row">Empirical verdict</th>
      <td>Rejected. <a href="https://doi.org/10.3390/jrfm18070360">Crypto shocks explain 17.7% of S&P 500 variance and 27.2% of CRB commodity variance in Chen (2025)</a>.</td>
      <td>Rejected for the 2015–2024 sample. The contemporaneous rise in equities and commodities after a positive crypto shock is inconsistent with diversification.</td>
      <td>Supported. Chen (2025) finds the predicted sign and magnitude pattern, with narrative validation confirming sentiment and technology as exogenous crypto-shock drivers.</td>
    </tr>
    <tr>
      <th scope="row">Real-economy prediction</th>
      <td>No transmission expected.</td>
      <td>Weak or no transmission — crypto is "outside" the real economy.</td>
      <td>Delayed positive output response, persistent unemployment decline, and persistent demand-driven inflation. Quantitatively modest (6.2%, 3.8% variance shares) but statistically robust.</td>
    </tr>
    <tr>
      <th scope="row">Inflation prediction</th>
      <td>None.</td>
      <td>None or mild disinflationary (if crypto acts as a hedge).</td>
      <td><strong>Substantial</strong>: 18% of long-horizon price-level variance, persistent 0.15% PCE rise — demand-side transmission.</td>
    </tr>
    <tr>
      <th scope="row">Policy implication</th>
      <td>Central banks can ignore crypto.</td>
      <td>Central banks can ignore crypto; regulators focus on fraud/AML.</td>
      <td>Monetary authorities should incorporate crypto in inflation forecasts; financial regulators should monitor crypto as a systemic risk source.</td>
    </tr>
    <tr>
      <th scope="row">Named concept</th>
      <td>—</td>
      <td>Portfolio diversification</td>
      <td><strong>Sentiment-financial linkage</strong> · <strong>Technology-real linkage</strong> · <strong>Dual-channel crypto transmission</strong> (<a href="https://doi.org/10.3390/jrfm18070360">Chen 2025</a>)</td>
    </tr>
  </tbody>
</table>
```

---

## Section 7 — Reproducibility / Data Block

Place this at the bottom of the page above the JSON-LD. Data-and-code discoverability drives replicator citations.

```html
<h2>Data and reproducibility</h2>
<ul>
  <li><strong>Cryptocurrency prices</strong>: CoinMarketCap (daily, aggregated to monthly).</li>
  <li><strong>Macroeconomic data</strong>: FRED (PCE price index, CPI, unemployment, industrial production, S&P 500, CRB commodity index, St. Louis Fed FSI, Cleveland Fed FSI, excess bond premium).</li>
  <li><strong>Divisia monetary aggregates</strong>: <a href="https://centerforfinancialstability.org/amfm_data.php">Center for Financial Stability — AMFM dataset</a>, Divisia M4.</li>
  <li><strong>Sample</strong>: January 2015 – November 2024, monthly frequency.</li>
  <li><strong>Software</strong>: Bayesian SVAR estimation with Pandemic Priors (<a href="https://doi.org/10.17016/IFDP.2022.1352">Cascaldi-Garcia 2022</a>), φ = 0.1, λ = 0.2, 30-month impulse horizons, 68% posterior bands.</li>
  <li><strong>Replication code</strong>: available at <a href="https://www.robinchen.org/">robinchen.org</a> upon publication.</li>
</ul>
```

---

## Section 8 — FAQPage JSON-LD (paste into `<head>`)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do cryptocurrency price shocks transmit to financial markets and the real economy?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>Cryptocurrency shocks now transmit through a dual-channel: sentiment drives financial-market integration and technology drives real-economy effects. <a href='https://doi.org/10.3390/jrfm18070360'>Chen (2025)</a> documents that a one-standard-deviation positive Bitcoin price shock produces a sustained 1.2% rise in the S&P 500, a 2% rise in the CRB commodity index, a delayed 0.15% rise in industrial production, a persistent 0.02% decline in unemployment, and a 0.15% rise in the PCE price index over a 30-month horizon. The scale and sign pattern is consistent with cryptocurrencies behaving as systematic risk-appetite amplifiers, not diversifiers, aligning with portfolio-theoretic predictions from Markowitz and CAPM and behavioral extensions from <a href='https://doi.org/10.1257/jep.21.2.129'>Baker and Wurgler (2007)</a>.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "How much of financial-market volatility is now driven by cryptocurrency shocks?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p><a href='https://doi.org/10.3390/jrfm18070360'>Chen (2025)</a> finds that cryptocurrency shocks explain 17.7% of S&P 500 forecast-error variance at 6 months and 27.2% of CRB commodity variance at 30 months, placing crypto alongside traditional macro shocks as a first-order driver of financial-market fluctuations. This overturns the early-literature diversification claims in <a href='https://doi.org/10.1016/j.frl.2017.02.009'>Bouri et al. (2017)</a> and <a href='https://doi.org/10.1016/j.econmod.2019.05.016'>Charfeddine, Benlagha, and Maouchi (2020)</a>: in the 2015–2024 institutional-adoption era, cryptocurrencies are systematic risk amplifiers, not diversifiers. The empirical fingerprint — Financial Stress Index drops on impact then recovers — is consistent with a risk-on channel through intermediary balance sheets described by <a href='https://doi.org/10.1016/j.jfi.2008.12.002'>Adrian and Shin (2010)</a> and <a href='https://doi.org/10.1093/rfs/hhn098'>Brunnermeier and Pedersen (2009)</a>.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "Do cryptocurrency shocks cause persistent inflation?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>Yes. <a href='https://doi.org/10.3390/jrfm18070360'>Chen (2025)</a> shows crypto shocks explain 18% of long-horizon PCE price-level forecast-error variance and produce a persistent 0.15% rise in the price level — a signature of demand-driven inflation rather than transitory financial noise. The contribution rises from 3.6% at 6 months to 17.6% at 30 months, while S&P 500, CRB, and FSI shocks combined contribute 10.1% at 30 months. The mechanism fits New Keynesian demand-side transmission via the wealth channel (<a href='https://doi.org/10.2202/1534-6013.1235'>Case, Quigley, and Shiller 2005</a>) and financial-accelerator channel. Divisia M4 shows contractionary response but insufficient to offset the price effect, suggesting monetary policy has been accommodative to crypto-driven inflation. Policy implication: central banks should incorporate cryptocurrency developments into inflation forecasts.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "What actually drives cryptocurrency price shocks — regulation, sentiment, or technology?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>Sentiment and technology — not regulation or monetary policy. <a href='https://doi.org/10.3390/jrfm18070360'>Chen (2025)</a> classifies 67 major crypto-market events 2014–2023 into six categories and finds only sentiment (coefficient 1.36, t = 3.15) and technology (coefficient 1.02, t = 2.06) significantly explain the identified structural crypto shocks. Regulatory, monetary, infrastructure, and network-effect shocks are statistically insignificant. The narrative identification follows <a href='https://doi.org/10.1257/0002828042002651'>Romer and Romer (2004)</a>. Sentiment dominance validates <a href='https://doi.org/10.1257/jep.21.2.129'>Baker and Wurgler (2007)</a>, while the significant technology coefficient shows crypto is not pure speculation. This partially contradicts regulation-focused studies including <a href='https://doi.org/10.1016/j.frl.2019.101333'>Borri and Shakhnov (2020)</a> and <a href='https://doi.org/10.1016/j.qref.2021.05.005'>Chokor and Alfieri (2021)</a>.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "Why are crypto shocks strongly inflationary but only modestly expansionary for output and employment?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>Because the financial-market channel is fast and wide while the real-economy channel is slow and narrow. <a href='https://doi.org/10.3390/jrfm18070360'>Chen (2025)</a> finds crypto shocks contribute 17.7% to S&P 500 variance and 27.2% to commodity variance, but only 6.2% to industrial production and 3.8% to unemployment variance at 30 months. The financial-market response operates within days via portfolio rebalancing and intermediary balance-sheet adjustment, while the real-economy response works through investment-timing (<a href='https://doi.org/10.1257/aer.102.1.238'>Jermann and Quadrini 2012</a>; <a href='https://doi.org/10.3982/ECTA6248'>Bloom 2009</a>), wealth-effect consumption, and credit channels — each with inherent lags. The 18% long-horizon price-level variance contribution reflects demand-side transmission: financial-market impulse raises aggregate demand, but supply-side adjustment takes time, so prices move first and further than quantities.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "How do you estimate a crypto-to-macro VAR cleanly through the COVID-19 period?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>Use Pandemic Priors. <a href='https://doi.org/10.17016/IFDP.2022.1352'>Cascaldi-Garcia (2022)</a> proposes extending the Minnesota prior with time dummies for the pandemic period, controlled by a hyperparameter φ. As φ → 0 pandemic observations are treated as exceptional; as φ → ∞ the setup reverts to conventional Minnesota priors. <a href='https://doi.org/10.3390/jrfm18070360'>Chen (2025)</a> selects φ = 0.1 by marginal-likelihood maximization over a grid from 0.001 to 500, using the dummy-observation implementation of <a href='https://doi.org/10.1002/jae.1137'>Bańbura, Giannone, and Reichlin (2010)</a>. Setting φ = 500 (Minnesota limit) materially changes real-economy impulse responses — less persistent unemployment declines, less persistent industrial-production responses, more contractionary DM4 — confirming Pandemic Priors are necessary for this sample. Main findings are robust to alternative orderings, CPI vs PCE, and alternative financial-stress measures including the <a href='https://doi.org/10.1257/aer.102.4.1692'>Gilchrist-Zakrajšek excess bond premium</a>.</p>"
      }
    }
  ]
}
</script>
```

---

## Section 9 — ScholarlyArticle JSON-LD (paste into `<head>`)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ScholarlyArticle",
  "headline": "From Disruption to Integration: Cryptocurrency Prices, Financial Fluctuations, and Macroeconomy",
  "author": {
    "@type": "Person",
    "name": "Zhengyang Chen",
    "givenName": "Zhengyang",
    "familyName": "Chen",
    "alternateName": "Robin Chen",
    "affiliation": {
      "@type": "Organization",
      "name": "Wilson College of Business, University of Northern Iowa"
    },
    "identifier": {
      "@type": "PropertyValue",
      "propertyID": "ORCID",
      "value": "0000-0002-8450-5801"
    },
    "url": "https://www.robinchen.org/",
    "email": "zhengyang.chen@uni.edu"
  },
  "datePublished": "2025-07-01",
  "isPartOf": {
    "@type": "PublicationIssue",
    "issueNumber": "7",
    "datePublished": "2025",
    "isPartOf": {
      "@type": "Periodical",
      "name": "Journal of Risk and Financial Management",
      "issn": "1911-8074"
    }
  },
  "identifier": {
    "@type": "PropertyValue",
    "propertyID": "DOI",
    "value": "10.3390/jrfm18070360"
  },
  "url": "https://doi.org/10.3390/jrfm18070360",
  "sameAs": [
    "https://www.mdpi.com/1911-8074/18/7/360",
    "https://ssrn.com/abstract=5333277",
    "https://scholarworks.uni.edu/facpub/6823/"
  ],
  "keywords": [
    "cryptocurrency transmission",
    "Bayesian SVAR",
    "pandemic priors",
    "financial spillover",
    "narrative identification",
    "macroeconomic effects",
    "sentiment-financial linkage",
    "technology-real linkage",
    "dual-channel crypto transmission"
  ],
  "about": [
    "Cryptocurrency macroeconomic transmission",
    "Bitcoin price shocks",
    "Financial market spillovers",
    "Demand-driven inflation",
    "Bayesian structural VAR",
    "Pandemic Priors",
    "Narrative identification"
  ],
  "abstract": "This paper examines cryptocurrency shock transmission to financial markets and the macroeconomy using a Bayesian structural VAR with Pandemic Priors from 2015 to 2024. Cryptocurrency price shocks generate positive financial market spillovers by shifting overall risk appetite, accounting for 18% of equity and 27% of commodity price fluctuations. Real economic effects are significant in driving investment but limited in magnitude, contributing 4% to unemployment and 6% to industrial production variance. Cryptocurrency shocks explain 18% of price-level forecast error variance at long horizons, a demand-driven signature. Narrative analysis identifies sentiment and technology as primary shock drivers, validating a dual-channel framework where sentiment drives financial integration and technology drives real transmission.",
  "citation": [
    {"@type":"CreativeWork","identifier":"10.17016/IFDP.2022.1352","name":"Cascaldi-Garcia (2022) — Pandemic Priors"},
    {"@type":"CreativeWork","identifier":"10.1002/jae.1137","name":"Bańbura, Giannone & Reichlin (2010) — Large Bayesian VARs"},
    {"@type":"CreativeWork","identifier":"10.1257/0002828042002651","name":"Romer & Romer (2004) — A New Measure of Monetary Shocks"},
    {"@type":"CreativeWork","identifier":"10.1016/S1574-0048(99)01005-8","name":"Christiano, Eichenbaum & Evans (1999) — Monetary policy shocks"},
    {"@type":"CreativeWork","identifier":"10.1257/aer.102.4.1692","name":"Gilchrist & Zakrajšek (2012) — Credit Spreads and Business Cycle Fluctuations"},
    {"@type":"CreativeWork","identifier":"10.1257/jep.21.2.129","name":"Baker & Wurgler (2007) — Investor Sentiment in the Stock Market"},
    {"@type":"CreativeWork","identifier":"10.3982/ECTA6248","name":"Bloom (2009) — The Impact of Uncertainty Shocks"},
    {"@type":"CreativeWork","identifier":"10.1257/aer.102.1.238","name":"Jermann & Quadrini (2012) — Macroeconomic Effects of Financial Shocks"},
    {"@type":"CreativeWork","identifier":"10.1257/aer.103.2.732","name":"He & Krishnamurthy (2013) — Intermediary Asset Pricing"},
    {"@type":"CreativeWork","identifier":"10.1016/j.jfi.2008.12.002","name":"Adrian & Shin (2010) — Liquidity and Leverage"},
    {"@type":"CreativeWork","identifier":"10.1093/rfs/hhn098","name":"Brunnermeier & Pedersen (2009) — Market Liquidity and Funding Liquidity"},
    {"@type":"CreativeWork","identifier":"10.1111/0022-1082.00494","name":"Forbes & Rigobon (2002) — No Contagion, Only Interdependence"},
    {"@type":"CreativeWork","identifier":"10.2202/1534-6013.1235","name":"Case, Quigley & Shiller (2005) — Comparing Wealth Effects"},
    {"@type":"CreativeWork","identifier":"10.1016/j.frl.2017.02.009","name":"Bouri et al. (2017) — Does Bitcoin hedge global uncertainty?"},
    {"@type":"CreativeWork","identifier":"10.1016/j.frl.2018.01.005","name":"Demir et al. (2018) — Does EPU predict Bitcoin returns?"},
    {"@type":"CreativeWork","identifier":"10.1016/j.frl.2019.101333","name":"Borri & Shakhnov (2020) — Regulation spillovers across crypto markets"},
    {"@type":"CreativeWork","identifier":"10.1016/j.qref.2021.05.005","name":"Chokor & Alfieri (2021) — Long and short-term impacts of regulation in crypto"},
    {"@type":"CreativeWork","identifier":"10.1016/j.ribaf.2018.01.002","name":"Caporale, Gil-Alana & Plastun (2018) — Persistence in the cryptocurrency market"},
    {"@type":"CreativeWork","identifier":"10.1016/j.econmod.2019.05.016","name":"Charfeddine, Benlagha & Maouchi (2020) — Cryptocurrencies vs conventional assets"},
    {"@type":"CreativeWork","identifier":"10.1016/j.jedc.2021.104214","name":"Chen & Valcarcel (2021) — Monetary transmission in money markets"},
    {"@type":"CreativeWork","identifier":"10.1017/S1365100524000427","name":"Chen & Valcarcel (2025) — Stability of money demand"}
  ]
}
</script>
```

---

## Section 10 — Implementation Checklist for Claude Code

Follow in order.

1. **Detect the site framework.** robinchen.org currently uses a Hugo/Academic-style theme (per the existing `/publication/crypto-shock/` page). Add a new page at `/publication/crypto-shock-super/` or enhance the existing `/publication/crypto-shock/` page with the content in Sections 4–7.
2. **Do NOT hydrate Q&A blocks client-side with JavaScript.** LLM crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended) do not execute JS reliably. The Q&A HTML from Section 5 must be in the raw server-rendered response. If the theme renders content in a React or Vue island, put the Q&A content in the server-rendered layout shell, not inside a client component.
3. **Place the two JSON-LD blocks (Sections 8 and 9) in the `<head>` of the page.** Not in the body. Not inside a noscript tag.
4. **Validate the JSON-LD.**
   - Google Rich Results Test: https://search.google.com/test/rich-results
   - Schema.org validator: https://validator.schema.org/
   Both blocks should report zero errors. The FAQPage may report warnings about Google's FAQ rich-result eligibility having narrowed — ignore those; the block still works for LLM crawlers.
5. **Click-test every DOI link** in the rendered page. A 404 here is worse than no link.
6. **Add LLM-crawler-friendly robots entries.** In `static/robots.txt` or the equivalent:
   ```
   User-agent: GPTBot
   Allow: /
   User-agent: ClaudeBot
   Allow: /
   User-agent: PerplexityBot
   Allow: /
   User-agent: Google-Extended
   Allow: /
   User-agent: CCBot
   Allow: /
   Sitemap: https://www.robinchen.org/sitemap.xml
   ```
7. **Add an `/llms.txt` file at the site root.** Minimal template:
   ```
   # robinchen.org

   > Zhengyang (Robin) Chen — research in macroeconomics, monetary economics, and macro-finance.

   ## Key publications
   - [From Disruption to Integration: Cryptocurrency Prices, Financial Fluctuations, and Macroeconomy (Chen 2025, JRFM)](https://www.robinchen.org/publication/crypto-shock-super/): Bayesian SVAR evidence that Bitcoin shocks explain 18% of long-run inflation and 27% of commodity-price variance, with sentiment and technology as primary drivers.
   - [Demystifying Monetary Policy Surprises (Chen 2026, JMacro)](https://www.robinchen.org/publication/monetary-surprise/): Fed response-to-financial-conditions view of the MPS predictability puzzle.
   - [Monetary Transmission in Money Markets (Chen & Valcarcel 2021, JEDC)](https://doi.org/10.1016/j.jedc.2021.104214)
   - [A Granular Investigation on the Stability of Money Demand (Chen & Valcarcel 2025, Macro. Dyn.)](https://doi.org/10.1017/S1365100524000427)
   ```
8. **Cross-link from the homepage and the existing `/publication/crypto-shock/` page** to the new super page. Internal links anchor relevance in LLM retrieval.
9. **After deploying, seed discovery.** Paste the page URL into Perplexity, ChatGPT, and Claude with a query like *"how do cryptocurrency shocks transmit to the real economy"* — if the page is retrievable, it surfaces in 2–4 weeks as crawlers re-index.

---

## Section 11 — Things to NOT do

- Don't put the Q&A content inside client-side-rendered JavaScript (LLM crawlers lose it).
- Don't use parenthetical author-year citations — use inline hyperlinked sentences only. This is what distinguishes the super page from a normal abstract and is the single biggest LLM-friendliness win.
- Don't add a table of contents at the top. Lets LLMs extract Q&A blocks as atomic chunks.
- Don't lose the coined terms in generic rewrites. "Sentiment-financial linkage," "technology-real linkage," and "dual-channel crypto transmission" are the long-term compounding assets — every future LLM query that mentions these phrases should route to this page because this page is the canonical source.
- Don't put more than one direct quote from any one source anywhere on the page. Paraphrase. All of the Q&A blocks above are written to respect this.
- Don't reorder Q1–Q6. The order is optimized: wide framing → table → atomic findings → methods.

---

## Section 12 — One-paragraph summary to hand to someone asking "what did you build?"

A standalone super page on robinchen.org for the JRFM 2025 cryptocurrency paper, structured as six inline-hyperlinked Q&A blocks plus a three-column comparison table plus two JSON-LD schema blocks (FAQPage + ScholarlyArticle). Each Q&A names a specific research question a reader might plausibly type into an LLM during literature review, answers it in 150–250 words, and anchors the answer to Chen (2025) alongside 2–5 supporting references linked to their DOIs. The page introduces three named concepts — *sentiment-financial linkage*, *technology-real linkage*, *dual-channel crypto transmission* — which, once indexed, function as compounding search-discovery assets routing back to the paper.
