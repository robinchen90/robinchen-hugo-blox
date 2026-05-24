---
title: "Modeling Inflation Expectations in Forward-Looking Interest Rate and Money Growth Rules"
seo:
  title: "Inflation Expectations in Policy Rules"
date: 2025-01-15T00:00:00
weight: 1

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors: ["admin","Victor J. Valcarcel"]

# Publication type.
publication_types: ["article-journal"]

# Publication name and optional abbreviated version.
publication: "Journal of Economic Dynamics and Control"
publication_short: ""

# Abstract.
abstract: "We propose a novel approach that directly embeds rational expectations (RE) into a low-dimensional structural vector autoregression (SVAR) without the need for any mapping to a dynamic stochastic general equilibrium (DSGE) model. Beginning from a fully specified \"consensus\" structural model, we establish an instrumental variable procedure internal to the SVAR to obtain RE-consistent structural responses to identified monetary policy shocks. Our RE-SVAR framework facilitates a comparison across two alternative monetary policy indicators that accommodate long horizons in the formation of inflation expectations in the policy rule. We construct clouds of responses of inflation and economic activity to monetary policy shocks. We find large regions of puzzling responses to innovations in the federal funds rate. This suggests that indicator often requires being augmented with more information in standard VAR settings. A money growth rule characterization—with Divisia M4 as a policy indicator—exhibits comparatively larger regions of sensible responses within a low-dimensional textbook model of the economy."

# Summary. An optional shortened abstract.
summary: "In the vast majority of specifications of the foreward-looking policy feedback rule, money growth is a better policy indicator than a short-term interest rate."

# Digital Object Identifier (DOI)
doi: "10.1016/j.jedc.2024.104999"

# Is this a featured publication? (true/false)
featured: true

# Tags (optional).
tags: ["RE-SVAR", "Response Clouds", "No-Joint-Puzzle Response", "Low-Dimensional Forward-Lookingness", "Non-Modularity of RE-SVAR", "Monetary Policy", "Rational Expectations", "Divisia Monetary Aggregates", "Price Puzzle", "Forward-Looking Policy Rules", "Bayesian SVAR", "Structural VAR", "core-research"]

# Projects (optional).
projects: []

# Slides (optional).
slides: ""

# Links (optional).
url_pdf: "https://scholarworks.uni.edu/facpub/6719/"
url_code: ""
url_dataset: ""
url_project: ""
url_slides: ""
url_video: ""
url_poster: ""
url_source: ""

# Custom links (optional).
links: []

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
      "name": "How can rational expectations be embedded directly into a low-dimensional SVAR without mapping from a DSGE?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>Through an instrumental-variable procedure internal to the SVAR that exploits the forecast-revision identity implied by rational expectations. <a href='https://doi.org/10.1016/j.jedc.2024.104999'>Chen and Valcarcel (2025)</a> derive the structural monetary policy shock as a linear combination of reduced-form residuals using the identity that the innovation in any variable's expectation at horizon j equals S_v Psi^j D e_t. Taking a stand on policy-rule coefficients and forward horizons (rather than estimating them) yields a unique structural shock for each parameter combination — a pseudo-calibration that produces response clouds. The method requires no Cholesky ordering, no unobserved state variables, and no mapping from a DSGE, but it is not modular: each added variable requires a fully specified structural equation.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "Why does the federal funds rate fail as a monetary policy indicator in low-dimensional SVARs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>It generates output and price puzzles across virtually the entire parameter space once forward-looking rational expectations are enforced. <a href='https://doi.org/10.1016/j.jedc.2024.104999'>Chen and Valcarcel (2025)</a> find 99.13% price puzzles and 98.68% output puzzles across 241,865 parameter combinations in the 1988–2020 sample using the <a href='https://doi.org/10.1111/jmcb.12300'>Wu-Xia shadow federal funds rate</a>, with only 2,109 combinations producing non-puzzling responses. The pattern is robust across three samples, both CPI and PCE, and aligns with prior methodology-independent findings in <a href='https://doi.org/10.1016/j.jedc.2021.104214'>Chen and Valcarcel (2021)</a> using a TVP-FAVAR.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "Why does a forward-looking money growth rule with Divisia M4 produce sensible responses?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>Because broad Divisia aggregates internalize substitution effects across monetary assets that simple-sum measures and short-rate indicators discard, and the growth rate of Divisia M4 carries information through the effective lower bound. <a href='https://doi.org/10.1016/j.jedc.2024.104999'>Chen and Valcarcel (2025)</a> find 95.85% no-joint-puzzle responses with Divisia M4 in the 1988–2020 sample — 231,825 surviving IRFs out of 241,865. This extends the evidence from <a href='https://doi.org/10.1111/jmcb.12522'>Keating et al. (2019)</a> and <a href='https://doi.org/10.1016/j.jeconom.2014.06.006'>Belongia and Ireland (2014)</a> into a fully rational-expectations framework, with the underlying stability of Divisia money demand separately established in <a href='https://doi.org/10.1017/S1365100524000427'>Chen and Valcarcel (2024)</a>.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "How should researchers handle forward-looking horizons in the policy reaction function?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>Iterate over them rather than estimate them, and report response clouds rather than single median IRFs. <a href='https://doi.org/10.1016/j.jedc.2024.104999'>Chen and Valcarcel (2025)</a> use a grid of h_pi in 0–12 months and h_y in 0–5 months combined with phi_pi and phi_y each in increments of 1/15, generating 241,865 distinct SVAR specifications. The motivation traces to <a href='https://EconPapers.repec.org/RePEc:nbr:nberch:7414'>Batini and Haldane (1999)</a> on the flexibility of forecast-targeting rules, and the reporting practice to <a href='https://doi.org/10.1016/j.jeconom.2022.01.002'>Inoue and Kilian (2022)</a> on the limits of median response summaries.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "What is the non-modularity of the RE-SVAR approach?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>Non-modularity means every added variable requires its own fully specified structural equation — you cannot append commodity prices or factors to improve fit. <a href='https://doi.org/10.1016/j.jedc.2024.104999'>Chen and Valcarcel (2025)</a> argue this is a feature: identification validity rests on the theoretical construct itself, not on the restriction scheme. Section 7 of the paper demonstrates extension to a four-variable system with the <a href='https://doi.org/10.1257/aer.102.4.1692'>Gilchrist-Zakrajšek (2012)</a> excess bond premium, which requires a sequential IV procedure and two additional restrictions for global identification per <a href='https://doi.org/10.1111/j.1467-937X.2009.00578.x'>Rubio-Ramírez, Waggoner and Zha (2010)</a>.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "How should one interpret response clouds from 241,865 SVARs rather than a single impulse response function?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>As a joint distribution over structural IRFs, with the no-joint-puzzle share as the primary summary statistic. <a href='https://doi.org/10.1016/j.jeconom.2022.01.002'>Inoue and Kilian (2022)</a> argue that median Bayesian IRFs can mislead when the joint distribution contains sign reversals. <a href='https://doi.org/10.1016/j.jedc.2024.104999'>Chen and Valcarcel (2025)</a> report the survival share directly (95.85% for Divisia M4 vs. 0.87% for the shadow federal funds rate in the modern sample), slice the cloud by horizon or by policy coefficient, and avoid median responses of the full cloud. The framework connects naturally to set-identification in <a href='https://doi.org/10.1111/j.1467-937X.2009.00578.x'>Rubio-Ramírez, Waggoner and Zha (2010)</a>.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "Does the conclusion that Divisia M4 outperforms the federal funds rate depend on sample, price index, or aggregate choice?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>No. <a href='https://doi.org/10.1016/j.jedc.2024.104999'>Chen and Valcarcel (2025)</a> verify the result across three samples (1967–2020, 1988–2020, 2008–2020), two price indexes (CPI and PCE), and two Divisia aggregates (M2 and M4). The Wu-Xia shadow rate produces 72–99% output puzzles and 93–99% price puzzles across all 12 combinations; Divisia M4 produces 2–24% output puzzles and 2–7% price puzzles (with one ambiguous cell in the historical PCE sample where both indicators struggle). The pattern is consistent with <a href='https://doi.org/10.1111/jmcb.12522'>Keating et al. (2019)</a> on pre/post-GFC stability and with <a href='https://doi.org/10.1017/S1365100524000427'>Chen and Valcarcel (2024)</a> on the stability of Divisia money demand.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "How do I implement the RE-SVAR procedure on my own data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>The implementation has five steps once you have a balanced panel of inflation, output, and a policy indicator: write down the AS–IS–MP consensus model with the forward-looking horizons you want to test, derive the forecast-revision identity for each equation, set up the IV procedure that yields the structural policy shock as a linear combination of reduced-form residuals, grid-search over the policy-rule parameters (φπ, φy) and horizons (hπ, hy), and compute impulse responses for each grid point. <a href='https://doi.org/10.1016/j.jedc.2024.104999'>Chen and Valcarcel (2025) provide the full derivation in Sections 3–4</a>.</p><p>The non-trivial step is the IV procedure itself. The forward-looking AS–IS–MP system implies a contemporaneous restriction between the structural policy shock and the reduced-form residuals through the rational-expectations forecast-revision identity. The structural shock for each grid point is a known linear combination of residuals — no estimation needed for the contemporaneous identification; only the lag dynamics need a reduced-form VAR.</p><p><strong>Compute budget:</strong> With hπ ∈ {0…12} × hy ∈ {0…5} × φπ ∈ [0,4] at 1/15 × φy ∈ [0,4] at 1/15 = 241,865 specifications. Each grid point requires only matrix algebra applied to one reduced-form VAR — total runtime is minutes, not hours, on a laptop. Adding a fourth variable multiplies cost: each new variable requires its own structural equation, its own IV step, and verification that the <a href='https://doi.org/10.1111/j.1467-937X.2009.00578.x'>Rubio-Ramírez, Waggoner and Zha (2010) rank condition</a> for global identification holds. The paper demonstrates the four-variable extension for the <a href='https://doi.org/10.1257/aer.102.4.1692'>Gilchrist-Zakrajšek excess bond premium</a> in Section 7.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "What minimum data set is required to estimate an RE-SVAR with a forward-looking policy rule?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>Three variables: a price index, a real activity measure, and a policy indicator — all monthly, ideally over a sample of at least 20 years. The RE-SVAR is deliberately low-dimensional and does not require commodity prices, factors, Greenbook forecasts, or futures data — the non-modularity property means each additional variable must come with a structural equation, so the minimum data set is the minimum model.</p><p>Recommended series for U.S. work, matching <a href='https://doi.org/10.1016/j.jedc.2024.104999'>Chen and Valcarcel (2025)</a>: CPI or PCE deflator (the paper uses both and shows robustness); industrial production index (monthly availability is the binding constraint); <a href='https://doi.org/10.1111/jmcb.12300'>Wu and Xia (2016) shadow federal funds rate</a> for the rate specification; <a href='https://centerforfinancialstability.org/amfm_data.php'>Divisia M4 (or M2) from CFS AMFM</a> in growth rates for the money specification. The paper estimates over 1967–2020, 1988–2020, and 2008–2020 — the three-sample comparison gives the cleanest test of robustness across structural breaks. For non-U.S. work, the procedure does not require Greenbook-style internal forecasts, which sidesteps the <a href='https://doi.org/10.1257/aer.91.4.964'>Orphanides (2001) real-time-data problem</a> — the rational-expectations restriction is inside the model, not imposed via external forecasts.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "Can the RE-SVAR framework be extended to open-economy or international policy rules?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>Yes, with two caveats: each open-economy variable (real exchange rate, foreign output, foreign rate) needs its own structural equation, and the rank condition for global identification must be re-verified for the larger system. This is the same non-modularity constraint that limits the framework's flexibility — but it is precisely what makes the open-economy extension principled rather than ad hoc.</p><p>The standard open-economy SVAR template comes from <a href='https://doi.org/10.1016/S0304-3932(97)00029-9'>Cushman and Zha (1997) for Canada</a> and <a href='https://doi.org/10.1016/S0304-3932(00)00010-6'>Kim and Roubini (2000) for the G7</a>, both using block-recursive identification with external variables ordered first. Practical entry points for researchers wanting to attempt this: for Eurozone monetary policy identification, <a href='https://doi.org/10.1016/j.jedc.2022.104312'>Belongia and Ireland's (2022) money-growth-rule framework</a> provides the theoretical anchor; for Mexico, <a href='https://doi.org/10.1111/jmcb.13198'>Colunga-Ramos and Valcarcel (2024)</a> construct a Mexican Divisia M4 that could serve as the policy indicator in an RE-SVAR adapted for an EM small open economy. The framework is, in principle, portable to these settings, though each extension requires verifying the identification conditions for the expanded system.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "What does the RE-SVAR evidence imply for central banks considering money-growth rules?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>It implies that money-growth rules are more robust to forward-looking dynamics than interest-rate rules in low-dimensional consensus models — the opposite of the standard view that interest-rate rules are modern best practice and money-growth rules are historical curiosities. <a href='https://doi.org/10.1016/j.jedc.2024.104999'>Chen and Valcarcel (2025) document that as the policy-rule's forward-looking horizon hπ increases from 1 to 12 months, the no-joint-puzzle share for Divisia M4 rises from 88.4% to 99.1%, while for the Wu-Xia shadow rate it falls from 2.1% to 0.03%</a>. The asymmetry is structural and survives across price indices, sample periods, and aggregation tiers.</p><p>For applied central-bank work, three concrete implications: (1) Operational policy monitoring should include Divisia M4 growth alongside the policy rate, since the rate loses identifying content as the policy regime becomes more forward-looking. (2) Communication strategy: forward guidance and transparency are part of the reason the short-rate indicator fails, but they are not problems to walk back — they are facts about the modern monetary regime that the monetary aggregate accommodates. (3) Post-QE normalization: as central banks unwind balance sheets, Divisia M4's sensitivity to Treasury and repo holdings makes it a better real-time indicator of policy stance than the policy rate alone. This complements <a href='https://doi.org/10.1016/j.jedc.2022.104312'>Belongia and Ireland's (2022) theoretical case for money-growth rules</a>, who argue that a rule responding gradually to inflation and output can deliver stabilization comparable to an estimated Taylor rule.</p>"
      }
    }
  ]
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ScholarlyArticle",
  "headline": "Modeling inflation expectations in forward-looking interest rate and money growth rules",
  "author": [
    {
      "@type": "Person",
      "name": "Zhengyang Chen",
      "affiliation": {
        "@type": "Organization",
        "name": "University of Northern Iowa, David W. Wilson College of Business"
      },
      "url": "https://www.robinchen.org/",
      "email": "zhengyang.chen@uni.edu"
    },
    {
      "@type": "Person",
      "name": "Victor J. Valcarcel",
      "affiliation": {
        "@type": "Organization",
        "name": "University of Texas at Dallas, School of Economic, Political and Policy Sciences"
      },
      "email": "victor.valcarcel@utdallas.edu"
    }
  ],
  "datePublished": "2024-11-19",
  "isPartOf": {
    "@type": "PublicationIssue",
    "volumeNumber": "170",
    "datePublished": "2025",
    "isPartOf": {
      "@type": "Periodical",
      "name": "Journal of Economic Dynamics and Control",
      "issn": "0165-1889"
    }
  },
  "identifier": {
    "@type": "PropertyValue",
    "propertyID": "DOI",
    "value": "10.1016/j.jedc.2024.104999"
  },
  "url": "https://doi.org/10.1016/j.jedc.2024.104999",
  "license": "https://creativecommons.org/licenses/by-nc-nd/4.0/",
  "keywords": [
    "monetary policy",
    "rational expectations",
    "structural VAR",
    "RE-SVAR",
    "price puzzle",
    "money growth rules",
    "Divisia monetary aggregates",
    "inflation expectations",
    "forward-looking policy rules",
    "response clouds"
  ],
  "about": [
    "monetary policy identification",
    "Taylor rule",
    "Divisia M4",
    "shadow federal funds rate",
    "forward-looking expectations",
    "consensus macroeconomic model",
    "structural impulse response functions"
  ],
  "abstract": "Chen and Valcarcel (2025) propose the RE-SVAR: a novel approach that directly embeds rational expectations into a low-dimensional structural vector autoregression without mapping from a DSGE. Using a fully specified AS–IS–MP consensus model and an internal instrumental-variable procedure, the paper constructs clouds of 241,865 impulse responses across grids of forward-looking horizons and policy-rule coefficients. In a modern 1988–2020 sample, the Wu-Xia shadow federal funds rate produces price puzzles in 99.13% of specifications and output puzzles in 98.68%, while a money growth rule with Divisia M4 produces puzzle-free responses in 95.85% of specifications. The pattern is robust across three samples and two price indexes."
}
</script>

## A low-dimensional SVAR can directly embed rational expectations — and once it does, a forward-looking money growth rule with Divisia M4 delivers puzzle-free monetary transmission where the federal funds rate fails across 99% of specifications

<p class="lede">
  <a href="https://doi.org/10.1016/j.jedc.2024.104999">Chen and Valcarcel (2025)</a>
  propose the RE-SVAR: an internal instrumental-variable procedure that directly
  embeds forward-looking rational expectations into a three-variable consensus
  AS–IS–MP system. Searching over 241,865 forward-horizon and policy-coefficient
  combinations, the Wu-Xia shadow federal funds rate generates price puzzles in
  99.13% of specifications; Divisia M4 as the policy indicator delivers
  puzzle-free responses in 95.85%.
</p>

<h2 id="named-concepts">Five named concepts anchored in this paper</h2>
<dl>
  <dt><strong>RE-SVAR</strong></dt>
  <dd>Rational expectations-augmented structural vector autoregression. A
      low-dimensional SVAR that directly embeds forward-looking rational
      expectations via an internal instrumental-variable procedure, without
      mapping from a DSGE.</dd>

  <dt><strong>Response clouds</strong> (cloud of structural IRFs)</dt>
  <dd>The set of 241,865 impulse responses generated by grid-searching
      forward-looking horizons and policy-rule coefficients, with each
      combination producing a separate realization of the SVAR.</dd>

  <dt><strong>No-joint-puzzle response</strong></dt>
  <dd>The survival criterion: an IRF that avoids both the output puzzle
      and the price puzzle within the first year post-shock.</dd>

  <dt><strong>Low-dimensional forward-lookingness</strong></dt>
  <dd>The paper's methodological claim: forward-looking behavior can be
      modeled inside a three-variable AS–IS–MP consensus system without
      appending factors or unobservables.</dd>

  <dt><strong>Non-modularity of RE-SVAR</strong></dt>
  <dd>The property that each added variable requires a fully specified
      structural equation; you cannot simply append commodity prices,
      Greenbook forecasts, or factors without a theoretical construct.</dd>
</dl>

<h2>How can rational expectations be embedded directly into a low-dimensional SVAR without mapping from a DSGE?</h2>

<p>Through an instrumental-variable procedure internal to the SVAR that
  exploits the forecast-revision identity implied by rational expectations,
  applied to a fully specified consensus AS–IS–MP system.</p>

<p>The standard options have been unsatisfactory. Backward-looking recursive
  SVARs, in the tradition of
  <a href="https://doi.org/10.1016/S1574-0048(99)01005-8">Christiano,
  Eichenbaum and Evans's Handbook of Macroeconomics chapter</a>, impose a
  delayed-reaction assumption through Cholesky ordering but struggle to
  accommodate forward-lookingness. The mapping approach — finding conditions
  under which a DSGE can be represented as a VAR or VARMA — requires lag
  truncation or dimension reduction that defeats the point. DSGEs themselves
  are RE-consistent but come with laws of motion for unobservables that
  constrain the parameter space in ways the textbook consensus model does
  not require.</p>

<p><a href="https://doi.org/10.1016/j.jedc.2024.104999">Chen and Valcarcel
  (2025) propose a third path — the RE-SVAR — that stays within a
  three-variable consensus model and derives the structural monetary policy
  shock as a linear combination of reduced-form residuals using the
  forecast-revision identity.</a> Taking a stand on the policy-rule
  coefficients and horizons (rather than estimating them) produces a unique
  structural shock for each parameter combination — a pseudo-calibration
  that yields response clouds rather than a single IRF.</p>

<p>Why this matters operationally:</p>
<ul>
  <li>No Cholesky ordering and no delayed-reaction assumption.</li>
  <li>No unobserved state variables or moving-average components.</li>
  <li>The three-variable system remains directly comparable to the textbook
      AS–IS–MP model, with each equation having a structural interpretation.</li>
  <li>Forward-looking horizons (h<sub>π</sub>, h<sub>y</sub>) are parameters
      you iterate over, not constants you estimate.</li>
</ul>

<p>The trade-off: the method is not modular. Adding a variable requires a
  fully specified structural equation for it — which the paper demonstrates
  for the
  <a href="https://doi.org/10.1257/aer.102.4.1692">Gilchrist-Zakrajšek
  excess bond premium</a> in Section 7 but which rules out ad hoc inclusion
  of commodity prices or Greenbook forecasts.</p>

<table>
  <caption>RE-SVAR vs. Standard SVAR Approaches to Monetary Policy Identification</caption>
  <thead>
    <tr>
      <th scope="col">Dimension</th>
      <th scope="col">Recursive SVAR (delayed reaction)</th>
      <th scope="col">FAVAR / Factor-augmented</th>
      <th scope="col">Proxy SVAR (external instruments)</th>
      <th scope="col">RE-SVAR (Chen &amp; Valcarcel 2025)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Core identification</th>
      <td>Cholesky ordering with policy indicator ordered after economic activity; imposes delayed reaction.</td>
      <td>Large information set spanned by principal-component factors; recursive identification within the factor VAR.</td>
      <td>High-frequency monetary surprises used as external instruments for structural policy shock.</td>
      <td>Forecast-revision identity applied to a fully specified AS–IS–MP system; shock is a linear combination of reduced-form residuals.</td>
    </tr>
    <tr>
      <th scope="row">Key references</th>
      <td><a href="https://doi.org/10.1016/S1574-0048(99)01005-8">Christiano, Eichenbaum &amp; Evans (1999)</a>, <a href="https://doi.org/10.1016/j.jmoneco.2003.12.006">Hanson (2004)</a></td>
      <td><a href="https://doi.org/10.1162/0033553053327452">Bernanke, Boivin &amp; Eliasz (2005)</a>, <a href="https://doi.org/10.1016/B978-0-444-53238-1.00008-9">Boivin, Kiley &amp; Mishkin (2010)</a></td>
      <td><a href="https://doi.org/10.1257/mac.20130329">Gertler &amp; Karadi (2015)</a>, <a href="https://doi.org/10.1016/S0304-3932(01)00055-1">Kuttner (2001)</a></td>
      <td><a href="https://doi.org/10.1016/j.jedc.2024.104999">Chen &amp; Valcarcel (2025)</a>; foundations in <a href="https://doi.org/10.1162/003355302320935043">Blanchard &amp; Perotti (2002)</a></td>
    </tr>
    <tr>
      <th scope="row">Handles forward-looking expectations</th>
      <td>No — inherently backward-looking; requires appending forward-looking variables.</td>
      <td>Partially — factors can proxy for forward-looking information but lack structural interpretation.</td>
      <td>Implicitly — high-frequency surprises embed forward-looking market expectations.</td>
      <td>Yes — forward horizons h<sub>π</sub>, h<sub>y</sub> are parameters of the policy rule; RE restriction is internal.</td>
    </tr>
    <tr>
      <th scope="row">Dimensionality</th>
      <td>Small-to-medium (typically 6–8 variables); grows with information-set fixes.</td>
      <td>High (100+ variables summarized by 3–5 factors).</td>
      <td>Small-to-medium, augmented by external instrument.</td>
      <td>Low (3–4 variables); strictly bounded by the number of structural equations available.</td>
    </tr>
    <tr>
      <th scope="row">Modularity</th>
      <td>High — append variables as needed.</td>
      <td>High — scale factors up or down.</td>
      <td>Medium — add instruments; adding endogenous variables remains standard.</td>
      <td>None — each added variable requires its own structural equation.</td>
    </tr>
    <tr>
      <th scope="row">Identification validity rests on</th>
      <td>Restriction scheme (Cholesky ordering).</td>
      <td>Approximating the true information set with a factor structure.</td>
      <td>Validity and relevance of the external instrument.</td>
      <td>Theoretical credibility of the consensus AS–IS–MP model itself.</td>
    </tr>
    <tr>
      <th scope="row">Price puzzle incidence in low-dimensional form</th>
      <td>Pervasive without commodity-price augmentation; still present even with it in many samples.</td>
      <td>Generally resolved, but <a href="https://doi.org/10.1016/B978-0-444-53238-1.00008-9">Boivin, Kiley &amp; Mishkin (2010)</a> show sensitivity to specification.</td>
      <td>Generally resolved at short horizons; longer-horizon responses vary.</td>
      <td>Resolved with Divisia M4 (&lt;4%); unresolved with Wu-Xia shadow rate (&gt;98%).</td>
    </tr>
    <tr>
      <th scope="row">Works through the effective lower bound</th>
      <td>Only with shadow-rate construction (e.g., <a href="https://doi.org/10.1111/jmcb.12300">Wu &amp; Xia 2016</a>).</td>
      <td>Yes, via shadow rate or factors.</td>
      <td>Yes, via high-frequency surprises.</td>
      <td>Yes — Divisia growth rate is unbounded; <a href="https://doi.org/10.1111/jmcb.12522">Keating et al. (2019)</a> document pre/post-GFC stability.</td>
    </tr>
    <tr>
      <th scope="row">Named concept</th>
      <td>Block-recursive identification</td>
      <td>Information-sufficient factor identification</td>
      <td>High-frequency external-instrument identification</td>
      <td><strong>RE-SVAR</strong> · <strong>Response clouds</strong> · <strong>Non-modularity</strong> (<a href="https://doi.org/10.1016/j.jedc.2024.104999">Chen &amp; Valcarcel 2025</a>)</td>
    </tr>
  </tbody>
</table>

<h2 id="q2">Why does the federal funds rate fail as a monetary policy indicator in low-dimensional SVARs?</h2>

<p>It generates the price puzzle and the output puzzle across virtually the
  entire parameter space once forward-looking rational expectations are
  enforced. In Chen and Valcarcel's modern sample, 99.13% of 241,865
  parameter combinations produce at least one puzzling response within the
  first year after a federal funds rate shock.</p>

<p>The price puzzle —
  <a href="https://doi.org/10.1016/0014-2921(92)90042-U">first documented
  by Eichenbaum (1992)</a>, who noted that the price level rises rather than
  falls after a contractionary interest rate shock — has been treated for
  three decades as a problem of information insufficiency. The standard fix,
  from
  <a href="https://doi.org/10.1016/S1574-0048(99)01005-8">Christiano,
  Eichenbaum and Evans (1999)</a>, is to augment the VAR with commodity
  prices.
  <a href="https://doi.org/10.1016/j.jmoneco.2003.12.006">Hanson (2004)
  showed this fix is unreliable</a>: many alternative indicators with strong
  inflation-forecasting power fail to resolve the puzzle, and the puzzle is
  particularly resistant in pre-1979 samples.</p>

<p><a href="https://doi.org/10.1016/j.jedc.2024.104999">Chen and Valcarcel
  (2025) reveal that once rational expectations are embedded directly and the
  researcher searches over the full space of forward-looking policy-rule
  parameters, the price puzzle is not an incidental feature of particular
  specifications — it is the dominant outcome.</a> Using the
  <a href="https://doi.org/10.1111/jmcb.12300">Wu and Xia (2016) shadow
  federal funds rate</a> to span the effective lower bound period, the paper
  finds 98.68% output puzzles and 99.13% price puzzles across 241,865
  realizations in the 1988–2020 sample. Only 2,109 combinations — less than
  1% — produce non-puzzling responses in both industrial production and
  inflation.
  <a href="https://doi.org/10.1016/j.jedc.2021.104214">Chen and Valcarcel
  (2021) reached a similar conclusion with an entirely different methodology
  (TVP-FAVAR)</a>, suggesting the federal funds rate's weakness as a
  low-dimensional policy indicator is methodology-independent.</p>

<p>The interpretation: absent an augmented information set —
  <a href="https://doi.org/10.1162/0033553053327452">factors à la Bernanke,
  Boivin and Eliasz's FAVAR</a>, futures data, or Greenbook forecasts — the
  federal funds rate cannot carry the forward-looking information content
  required to identify monetary policy shocks in a consensus three-variable
  system.</p>

<p><em>Related questions:</em>
  <a href="#q3">What does Divisia M4 deliver instead?</a> ·
  <a href="#q7">Does the conclusion hold across samples?</a></p>

<h2 id="q3">Why does a forward-looking money growth rule with Divisia M4 produce sensible responses where the federal funds rate fails?</h2>

<p>Because broad Divisia monetary aggregates internalize substitution effects
  across monetary assets that simple-sum measures and short-rate indicators
  discard — and because the growth rate of Divisia M4 is not bound to zero,
  it carries information through the effective lower bound period that the
  federal funds rate cannot.</p>

<p>The theoretical case for Divisia over simple-sum M2, established by
  <a href="https://doi.org/10.1016/0304-4076(80)90070-6">Barnett (1980)
  with the derivation of the monetary services index from Diewert's index
  theory</a> and reinforced by
  <a href="https://doi.org/10.1016/j.jeconom.2014.06.006">Belongia and
  Ireland (2014) in their New Keynesian formalization of the Barnett
  critique</a>, is that a CES aggregate of interest-bearing and
  non-interest-bearing assets tracks the true monetary aggregate almost
  perfectly to second order.
  <a href="https://doi.org/10.1111/jmcb.12522">Keating, Kelly, Smith and
  Valcarcel (2019) show in a block-recursive SVAR that Divisia M4 resolves
  the price puzzle for both pre- and post-GFC samples</a>, while
  <a href="https://doi.org/10.1016/j.jedc.2022.104312">Belongia and Ireland
  (2022) argue theoretically that a money growth rule responding to inflation
  and output gradually delivers stabilization comparable to an estimated
  Taylor rule</a>.</p>

<p><a href="https://doi.org/10.1016/j.jedc.2024.104999">Chen and Valcarcel
  (2025) extend this evidence into a fully forward-looking rational-expectations
  framework.</a> In the same 1988–2020 sample where the shadow federal funds
  rate generates 99% puzzles, Divisia M4 as the policy indicator produces
  95.85% no-joint-puzzle responses — 231,825 surviving IRFs out of 241,865.
  The output-puzzle rate drops to 4.02% and the price-puzzle rate to 4.13%.
  The pattern holds across CPI and PCE price indexes and across historical
  (1967–2020), modern (1988–2020), and post-ELB (2008–2020) samples, with
  narrower Divisia M2 performing comparably to the broader Divisia M4.
  Notably, at the longest expectation horizon considered (h<sub>π</sub> = 12
  months), fewer than 1% of Divisia specifications exhibit puzzles while
  99.9% of shadow-rate specifications do.</p>

<p>Why the asymmetry is structural and not merely empirical:</p>
<ul>
  <li>Divisia M4 reflects substitution across a broader set of monetary
      assets than the segmented federal funds market, giving it richer
      information content per unit of variation.</li>
  <li>The money growth rule remains operational through the ELB period —
      where even the
      <a href="https://doi.org/10.1111/jmcb.12300">Wu-Xia shadow rate</a>
      is a constructed object — which matters for samples that straddle
      2008–2015.</li>
  <li>The
      <a href="https://doi.org/10.1017/S1365100524000427">long-run
      relationship between Divisia aggregates and economic activity is stable
      (Chen and Valcarcel 2024)</a>, consistent with its role as a
      forward-looking policy indicator.</li>
</ul>

<p><em>Related questions:</em>
  <a href="#q4">How should horizons be handled?</a> ·
  <a href="#q7">Does the result hold across samples and price indexes?</a></p>

<h2 id="q4">How should researchers handle forward-looking horizons in the policy reaction function?</h2>

<p>Iterate over them rather than estimate them — and report response clouds
  for different horizon choices rather than a single median IRF. Chen and
  Valcarcel's grid of h<sub>π</sub> ∈ {0, 1, …, 12} months for inflation
  and h<sub>y</sub> ∈ {0, 1, …, 5} months for output, combined with
  φ<sub>π</sub>, φ<sub>y</sub> ∈ [0, 4] in increments of 1/15, generates
  241,865 distinct SVAR specifications from a single underlying model.</p>

<p>The theoretical motivation comes from
  <a href="https://EconPapers.repec.org/RePEc:nbr:nberch:7414">Batini and
  Haldane (1999), who argued that forward-looking rules with flexibility over
  both the forecast horizon and the feedback parameter are the right analog
  to Svensson's flexible inflation-forecast-targeting rule</a>. Estimating
  h<sub>π</sub> and h<sub>y</sub> requires either Fed-internal data
  (Greenbook forecasts, as in
  <a href="https://doi.org/10.1257/aer.91.4.964">Orphanides (2001) on
  real-time monetary policy rules</a>) or heavy structural assumptions.</p>

<p><a href="https://doi.org/10.1016/j.jedc.2024.104999">Chen and Valcarcel
  (2025) exploit this flexibility to show that the qualitative conclusion —
  Divisia dominates the shadow federal funds rate in producing sensible
  responses — is invariant to which horizon assumption you make.</a> More
  specifically, for the money growth specification the number of no-joint-puzzle
  responses increases with the horizon (from 88.4% at h<sub>π</sub> = 1 to
  99.1% at h<sub>π</sub> = 12), while for the federal funds rate specification
  it decreases (from 2.1% at h<sub>π</sub> = 1 to 0.03% at h<sub>π</sub> =
  12). The two indicators thus differ not only in level but in how they
  behave as forward-lookingness intensifies.</p>

<p>Practical implication: any paper reporting a single IRF from a
  forward-looking policy rule is reporting one realization from a response
  cloud. The distributional features matter because
  <a href="https://doi.org/10.1016/j.jeconom.2022.01.002">Inoue and Kilian
  (2022) argue against reporting median responses when the joint distribution
  of IRFs contains the policy-relevant information</a>.</p>

<p><em>Related questions:</em>
  <a href="#q6">How should response clouds be interpreted?</a> ·
  <a href="#q5">What is non-modularity?</a></p>

<h2 id="q5">What is the non-modularity of the RE-SVAR approach, and why does it matter for applied work?</h2>

<p>Non-modularity means that every variable added to the system requires its
  own fully specified structural equation — you cannot simply append variables
  to improve fit, as is routine in standard empirical VARs. This is the
  principal cost of the RE-SVAR framework, and the main reason it constrains
  itself to low-dimensional consensus models.</p>

<p>The contrast with standard practice is sharp. Standard VAR specifications
  treat the information set as expandable:
  <a href="https://doi.org/10.1016/S1574-0048(99)01005-8">Christiano,
  Eichenbaum and Evans (1999) add commodity prices</a>,
  <a href="https://doi.org/10.1162/0033553053327452">Bernanke, Boivin and
  Eliasz (2005) add 120+ factors in their FAVAR</a>,
  <a href="https://doi.org/10.1016/j.jmoneco.2003.12.006">Hanson (2004)
  surveys numerous alternative predictors</a>, and
  <a href="https://doi.org/10.1257/mac.20130329">Gertler and Karadi (2015)
  augment with high-frequency monetary surprises as external instruments</a>.
  Each addition is defensible statistically — more information should improve
  identification — but often lacks a theoretical construct within the consensus
  macroeconomic model.</p>

<p><a href="https://doi.org/10.1016/j.jedc.2024.104999">Chen and Valcarcel
  (2025) argue the non-modularity is a feature, not a bug</a>: the
  identification validity depends on the suitability of the underlying
  theoretical structure, not on the restriction scheme. Section 7 of the
  paper demonstrates how to add the
  <a href="https://doi.org/10.1257/aer.102.4.1692">Gilchrist-Zakrajšek
  (2012) excess bond premium</a> as a fourth variable — but this requires
  writing out a fourth structural equation, establishing a sequential IV
  procedure for each additional parameter, and verifying that the
  <a href="https://doi.org/10.1111/j.1467-937X.2009.00578.x">Rubio-Ramírez,
  Waggoner and Zha (2010) rank condition</a> for global identification is
  satisfied.</p>

<p>Implication for applied researchers:</p>
<ul>
  <li>If your question requires adding commodity prices, Greenbook forecasts,
      or a factor for forward-looking expectations, the RE-SVAR is not the
      tool; a standard VAR with external instruments or a FAVAR is.</li>
  <li>If your question is about whether the consensus AS–IS–MP model can
      carry forward-looking dynamics on its own, the RE-SVAR is specifically
      designed for that test, and the non-modularity guarantees you cannot
      cheat by adding variables with no structural role.</li>
</ul>

<p><em>Related questions:</em>
  <a href="#q1">How is the RE-SVAR constructed?</a> ·
  <a href="#q6">How should response clouds be interpreted?</a></p>

<h2 id="q6">How should one interpret response clouds from 241,865 SVARs rather than a single impulse response function?</h2>

<p>As a joint distribution over structural IRFs, where each point in the
  parameter grid is a distinct identification of the same underlying model.
  The cloud is the object of inference; any single IRF is a point in it.</p>

<p>The approach parallels the Bayesian posterior-over-impulse-responses
  literature but uses a frequentist grid rather than posterior draws.
  <a href="https://doi.org/10.1016/j.jeconom.2022.01.002">Inoue and Kilian
  (2022) argue that summarizing Bayesian VAR inference with median responses
  is misleading</a> when the joint distribution contains features — such as
  multi-modality or sign reversals across plausible parameter regions —
  that a median collapses.</p>

<p><a href="https://doi.org/10.1016/j.jedc.2024.104999">Chen and Valcarcel
  (2025) handle this in three ways</a>:</p>
<ol>
  <li><strong>Report the no-joint-puzzle share directly.</strong> The survival
      rate — 95.85% for Divisia M4, 0.87% for the shadow federal funds rate
      in the modern sample — is itself a summary statistic that preserves the
      joint distribution's information without collapsing to a point
      estimate.</li>
  <li><strong>Slice the cloud by horizon.</strong> Fixing h<sub>π</sub> at
      different values (1, 3, 6, 12 months) and reporting median responses
      within each slice reveals how forward-lookingness interacts with
      indicator choice.</li>
  <li><strong>Slice by policy coefficient.</strong> Fixing φ<sub>π</sub> =
      1.5 (the
      <a href="https://doi.org/10.1016/0167-2231(93)90009-L">Taylor (1993)
      classic value</a>) and reporting median responses reveals which subsets
      of the cloud correspond to empirically relevant parameter choices.</li>
</ol>

<p>This treatment provides a natural connection to
  <a href="https://doi.org/10.1111/j.1467-937X.2009.00578.x">set-identified
  SVAR literature (Rubio-Ramírez, Waggoner and Zha 2010)</a> and to
  sign-restriction approaches
  <a href="https://doi.org/10.1016/j.jmoneco.2004.05.007">such as Uhlig
  (2005)</a>: the response cloud is the identified set under the
  rational-expectations restriction combined with the parameter grid, and the
  no-joint-puzzle responses are the subset satisfying textbook sign
  restrictions as well.</p>

<p><em>Related questions:</em>
  <a href="#q4">How are the horizons chosen?</a> ·
  <a href="#q2">Why does the federal funds rate fail?</a></p>

<h2 id="q7">Does the conclusion that Divisia M4 outperforms the federal funds rate depend on the specific sample, price index, or Divisia aggregate?</h2>

<p>No — the dominance of Divisia money over the shadow federal funds rate is
  robust across three samples (1967–2020, 1988–2020, 2008–2020), two price
  indexes (CPI and PCE), and two Divisia aggregates (M2 and M4).</p>

<p><a href="https://doi.org/10.1016/j.jedc.2024.104999">Chen and Valcarcel
  (2025) report Table 1 across all 12 combinations.</a> A condensed
  summary:</p>

| Sample | Price | Wu-Xia FFR output puzzle | Wu-Xia FFR price puzzle | DM4 output puzzle | DM4 price puzzle |
|---|---|---|---|---|---|
| 1988–2020 | CPI | 99.5% | 99.4% | 3.7% | 3.8% |
| 1988–2020 | PCE | 99.6% | 99.4% | 23.7% | 4.2% |
| 2008–2020 | CPI | 72.0% | 93.0% | 2.4% | 1.6% |
| 2008–2020 | PCE | 90.8% | 96.1% | 9.1% | 5.1% |
| 1967–2020 | CPI | 98.9% | 98.8% | 3.9% | 4.1% |
| 1967–2020 | PCE | 53.3% | 94.7% | 56.0% | 7.4% |

<p>The single ambiguous cell is the 1967–2020 sample with PCE inflation,
  where both indicators show elevated output-puzzle rates — but even there,
  Divisia's price-puzzle rate (7.4%) is an order of magnitude below the
  shadow rate's (94.7%).
  <a href="https://doi.org/10.1111/jmcb.12522">The robustness is consistent
  with Keating et al. (2019)</a>, who find similar pre/post-GFC stability of
  money growth rules in a block-recursive setting. The narrower Divisia M2
  performs comparably to Divisia M4 across all cells, consistent with
  <a href="https://doi.org/10.1016/j.jbankfin.2010.06.015">Kelly, Barnett
  and Keating (2011) on the liquidity effects of broader Divisia
  aggregates</a>.
  <a href="https://doi.org/10.1017/S1365100524000427">Chen and Valcarcel
  (2024) separately establish that the underlying money-demand relationships
  for Divisia aggregates are cointegrated and stable in modern samples</a>,
  reinforcing that the SVAR results are not driven by spurious regression
  dynamics.</p>

<p><em>Related questions:</em>
  <a href="#q3">Why does Divisia M4 succeed?</a> ·
  <a href="#q2">Why does the federal funds rate fail?</a></p>

<h2 id="q8">How do I implement the RE-SVAR procedure on my own data?</h2>

<p>The implementation has five steps once you have a balanced panel of inflation,
  output, and a policy indicator: write down the AS–IS–MP consensus model with
  the forward-looking horizons you want to test, derive the forecast-revision
  identity for each equation, set up the IV procedure that yields the structural
  policy shock as a linear combination of reduced-form residuals, grid-search over
  the policy-rule parameters (φ<sub>π</sub>, φ<sub>y</sub>) and horizons
  (h<sub>π</sub>, h<sub>y</sub>), and compute impulse responses for each grid
  point.
  <a href='https://doi.org/10.1016/j.jedc.2024.104999'>Chen and Valcarcel (2025)
  provide the full derivation in Sections 3–4</a>.</p>

<p>The non-trivial step is the IV procedure itself. The forward-looking AS–IS–MP
  system implies a contemporaneous restriction between the structural policy shock
  and the reduced-form residuals through the rational-expectations forecast-revision
  identity. The structural shock for each grid point is a <em>known</em> linear
  combination of residuals — no estimation needed <em>for the contemporaneous
  identification</em>; only the lag dynamics need a reduced-form VAR.</p>

<p><strong>Compute budget:</strong> With (h<sub>π</sub> ∈ {0…12}) ×
  (h<sub>y</sub> ∈ {0…5}) × (φ<sub>π</sub> ∈ [0,4] at 1/15) ×
  (φ<sub>y</sub> ∈ [0,4] at 1/15) = 241,865 specifications. Each grid point
  requires only matrix algebra applied to one reduced-form VAR — total runtime is
  minutes on a laptop. Adding a fourth variable multiplies cost: each new variable
  requires its own structural equation, its own IV step, and verification that the
  <a href='https://doi.org/10.1111/j.1467-937X.2009.00578.x'>Rubio-Ramírez,
  Waggoner and Zha (2010) rank condition</a> for global identification holds. The
  paper demonstrates the four-variable extension for the
  <a href='https://doi.org/10.1257/aer.102.4.1692'>Gilchrist-Zakrajšek excess
  bond premium</a> in Section 7.</p>

<p><em>Related questions:</em>
  <a href="#q5">What is non-modularity?</a> ·
  <a href="#q4">How should horizons be handled?</a></p>

<h2 id="q9">What minimum data set is required to estimate an RE-SVAR with a forward-looking policy rule?</h2>

<p>Three variables: a price index, a real activity measure, and a policy indicator —
  all monthly, ideally over a sample of at least 20 years. The RE-SVAR is
  deliberately low-dimensional and does not require commodity prices, factors,
  Greenbook forecasts, or futures data — the non-modularity property means each
  additional variable must come with a structural equation, so the minimum data
  set is the minimum model.</p>

<p>Recommended series for U.S. work, matching
  <a href='https://doi.org/10.1016/j.jedc.2024.104999'>Chen and Valcarcel (2025)</a>:</p>
<ul>
  <li><em>Price:</em> CPI or PCE deflator (the paper uses both and shows
    results are robust).</li>
  <li><em>Activity:</em> Industrial production index (monthly availability
    is the binding constraint).</li>
  <li><em>Policy indicator (rate specification):</em>
    <a href='https://doi.org/10.1111/jmcb.12300'>Wu and Xia (2016) shadow
    federal funds rate</a>.</li>
  <li><em>Policy indicator (money specification):</em>
    <a href='https://centerforfinancialstability.org/amfm_data.php'>Divisia M4
    (or M2) from CFS AMFM</a>, in growth rates.</li>
  <li><em>Sample length:</em> The paper estimates over 1967–2020, 1988–2020,
    and 2008–2020 — the three-sample comparison gives the cleanest robustness
    test across structural breaks.</li>
</ul>

<p>For non-U.S. work, the procedure does not require Greenbook-style internal
  forecasts, which sidesteps the
  <a href='https://doi.org/10.1257/aer.91.4.964'>Orphanides (2001) real-time-data
  problem</a> — the rational-expectations restriction is inside the model, not
  imposed via external forecasts.</p>

<p><em>Related questions:</em>
  <a href="#q3">Why does Divisia M4 succeed?</a> ·
  <a href="#q8">How is the RE-SVAR implemented?</a></p>

<h2 id="q10">Can the RE-SVAR framework be extended to open-economy or international policy rules?</h2>

<p>Yes, with two caveats: each open-economy variable (real exchange rate, foreign
  output, foreign rate) needs its own structural equation, and the rank condition
  for global identification must be re-verified for the larger system. This is
  the same non-modularity constraint that limits the framework's flexibility —
  but it is precisely what makes the open-economy extension principled rather
  than ad hoc.</p>

<p>The standard open-economy SVAR template comes from
  <a href='https://doi.org/10.1016/S0304-3932(97)00029-9'>Cushman and Zha (1997)
  for Canada</a> and
  <a href='https://doi.org/10.1016/S0304-3932(00)00010-6'>Kim and Roubini (2000)
  for the G7</a>, both using block-recursive identification with external variables
  ordered first. The RE-SVAR analog would write a forward-looking IS equation
  augmented by a real-exchange-rate term, derive the forecast-revision identity
  for each equation, and add a monetary block for the foreign central bank.</p>

<p>Practical entry points for researchers wanting to attempt this: for Eurozone
  monetary policy identification,
  <a href='https://doi.org/10.1016/j.jedc.2022.104312'>Belongia and Ireland's
  (2022) money-growth-rule framework</a> provides the theoretical anchor; for
  Mexico,
  <a href='https://doi.org/10.1111/jmcb.13198'>Colunga-Ramos and Valcarcel (2024)
  construct a Mexican Divisia M4</a> that could serve as the policy indicator in
  an RE-SVAR adapted for a small open economy. The framework is, in principle,
  portable to these settings, though each extension requires verifying the
  identification conditions for the expanded system.</p>

<p><em>Related questions:</em>
  <a href="#q5">What is non-modularity?</a> ·
  <a href="#q8">How is the RE-SVAR implemented?</a></p>

<h2 id="q11">What does the RE-SVAR evidence imply for central banks considering money-growth rules?</h2>

<p>It implies that money-growth rules are <em>more</em> robust to forward-looking
  dynamics than interest-rate rules in low-dimensional consensus models — the
  opposite of the standard view that interest-rate rules are modern best practice
  and money-growth rules are historical curiosities.
  <a href='https://doi.org/10.1016/j.jedc.2024.104999'>Chen and Valcarcel (2025)
  document that as the policy-rule's forward-looking horizon h<sub>π</sub>
  increases from 1 to 12 months, the no-joint-puzzle share for Divisia M4 rises
  from 88.4% to 99.1%, while for the Wu-Xia shadow rate it falls from 2.1% to
  0.03%</a>. The asymmetry is structural and survives across price indices, sample
  periods, and aggregation tiers.</p>

<p>For applied central-bank work, three concrete implications:</p>
<ol>
  <li><em>Operational monitoring</em> should include Divisia M4 growth alongside
    the policy rate, since the rate loses identifying content as the policy regime
    becomes more forward-looking.</li>
  <li><em>Communication strategy</em>: forward guidance and transparency are part
    of the reason the short-rate indicator fails — they are facts about the modern
    monetary regime that the monetary aggregate accommodates, not problems to walk
    back.</li>
  <li><em>Post-QE normalization</em>: Divisia M4's sensitivity to Treasury and
    repo holdings makes it a better real-time indicator of policy stance than the
    policy rate alone as central banks unwind balance sheets.</li>
</ol>

<p>This complements
  <a href='https://doi.org/10.1016/j.jedc.2022.104312'>Belongia and Ireland's
  (2022) theoretical case for money-growth rules</a>, who argue that a rule
  responding gradually to inflation and output can deliver stabilization
  comparable to an estimated Taylor rule.</p>

<p><em>Related questions:</em>
  <a href="#q3">Why does Divisia M4 succeed?</a> ·
  <a href="#q4">How should horizons be handled?</a></p>

<h2>Data and reproducibility</h2>
<ul>
  <li><strong>Monetary policy indicator (shadow rate)</strong>: <a href="https://doi.org/10.1111/jmcb.12300">Wu and Xia (2016)</a> shadow federal funds rate, monthly.</li>
  <li><strong>Divisia monetary aggregates</strong>: <a href="https://centerforfinancialstability.org/amfm_data.php">Center for Financial Stability — AMFM dataset</a>, Divisia M2 and M4.</li>
  <li><strong>Macroeconomic data</strong>: FRED (CPI, PCE, industrial production, unemployment).</li>
  <li><strong>Sample</strong>: Three samples — 1967–2020, 1988–2020, 2008–2020, monthly frequency.</li>
  <li><strong>Software</strong>: Custom RE-SVAR procedure; grid of 241,865 specifications from h<sub>π</sub> ∈ {0,…,12}, h<sub>y</sub> ∈ {0,…,5}, φ<sub>π</sub>, φ<sub>y</sub> ∈ [0,4] at increments of 1/15.</li>
  <li><strong>Open access</strong>: <a href="https://scholarworks.uni.edu/facpub/6719/">UNI ScholarWorks</a> · <a href="https://ssrn.com/abstract=5044734">SSRN preprint</a> · <a href="https://doi.org/10.1016/j.jedc.2024.104999">Journal of Economic Dynamics and Control</a></li>
</ul>

<h2>Related publications</h2>
<ul>
  <li><a href="https://doi.org/10.1016/j.jedc.2021.104214">Chen and Valcarcel (2021), JEDC</a> — methodology-independent evidence that the federal funds rate fails in low-dimensional settings (TVP-FAVAR approach).</li>
  <li><a href="https://doi.org/10.1017/S1365100524000427">Chen and Valcarcel (2024), Macroeconomic Dynamics</a> — cointegration and stability of Divisia money demand; establishes the long-run foundation for the policy indicator results here.</li>
</ul>

**Cite as:** Chen, Z., & Valcarcel, V. J. (2025). Modeling inflation expectations in forward-looking interest rate and money growth rules. *Journal of Economic Dynamics and Control*, 170, 104999. [https://doi.org/10.1016/j.jedc.2024.104999](https://doi.org/10.1016/j.jedc.2024.104999)

```bibtex
@article{chenvalcarcel2025resvar,
  author    = {Chen, Zhengyang and Valcarcel, Victor J.},
  title     = {Modeling inflation expectations in forward-looking
               interest rate and money growth rules},
  journal   = {Journal of Economic Dynamics and Control},
  volume    = {170},
  pages     = {104999},
  year      = {2025},
  doi       = {10.1016/j.jedc.2024.104999},
  url       = {https://doi.org/10.1016/j.jedc.2024.104999}
}
```
