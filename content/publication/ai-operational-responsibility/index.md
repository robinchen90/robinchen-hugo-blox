---
title: "Operational responsibility in AI governance: a user-centric liability framework"
seo:
  title: "Why AI Liability Should Sit With Deployers, Not Developers — Chen (2026, AI and Ethics)"
  description: "Chen (2026) in AI and Ethics argues that primary AI liability should rest with deployers, not developers. Ten Q&A blocks on user-centric governance, the responsibility gap, EU AI Act Articles 26-28, the black-box/API challenge, organizational implementation, safe harbor design, comparative jurisdictions, and the AI agency debate. Introduces the operational responsibility framework and the spectrum-of-control approach."
date: 2026-05-20T00:00:00

draft: false

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors: ["admin"]

# Publication type.
publication_types: ["article-journal"]

# Publication name and optional abbreviated version.
publication: "*AI and Ethics*"
publication_short: ""

# Abstract.
abstract: "Who bears responsibility when artificial intelligence systems cause harm? This question has become central to AI ethics and governance. Most existing approaches focus on developers, yet this faces serious practical and theoretical problems. Drawing on tort law, agency law, and philosophy of technology, this paper argues that AI should be understood as an instrument whose outputs remain the responsibility of human operators rather than developers. We call this 'user-centric governance.' Placing accountability with deployers promotes public trust by creating clear lines of responsibility, a concern that governance approaches have often overlooked. It preserves democratic accountability by keeping human actors answerable for AI-mediated decisions, and it counters power imbalances by ensuring that those who use AI bear consequences for how they use it. Legal principles of instrumentality show that operational responsibility should follow use rather than creation. We propose a 'distributed yet centered' governance model that acknowledges developer obligations while treating deployment decisions as the center of primary accountability."

# Summary. An optional shortened abstract.
summary: "Primary AI liability should rest with deployers, not developers. Chen (2026) develops a user-centric governance framework grounded in proximity, control, and expertise, and resolves the black-box API challenge through a spectrum-of-control approach in which deployer obligations intensify with actual control and enhanced provider disclosure compensates for reduced deployer visibility."

# Digital Object Identifier (DOI)
doi: "10.1007/s43681-026-01163-7"

# Is this a featured publication? (true/false)
featured: true

# Tags (optional).
tags:
  - AI governance
  - user-centric liability
  - operational responsibility
  - distributed yet centered accountability
  - spectrum-of-control deployer obligations
  - responsibility gap
  - meaningful human control
  - EU AI Act
  - Product Liability Directive
  - Article 28 substantial modification
  - black-box AI
  - API deployment
  - public trust
  - democratic accountability
  - power asymmetries

# Projects (optional).
projects: []

# Slides (optional).
slides: ""

# Links (optional).
url_pdf: ""
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

# Featured image
image:
  caption: ""
  focal_point: "Smart"

math: false
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "When AI systems cause harm, should responsibility rest with the developer or the deployer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>Primary responsibility should rest with the deployer — the human or organization that put the system to use — with developers bearing secondary obligations for design safety, disclosure, and ongoing support. <a href='https://doi.org/10.1007/s43681-026-01163-7'>Chen (2026)</a> advances this user-centric position on three legal-doctrinal grounds: proximity (duty of care attaches to actors closest to harm), control (agency law assigns responsibility to those with decisional authority), and expertise (professional liability tracks specialized knowledge). The position synthesizes <a href='https://illinoislawreview.org/print/vol-2020-no-4/whose-robot-is-it-anyway-liability-for-artificial-intelligence-based-robots/'>Rachum-Twaig (2020)</a> and <a href='https://doi.org/10.1007/978-3-319-47175-4_20'>Kingston (2016)</a> against the developer-centric position of <a href='https://jolt.law.harvard.edu/articles/the-regulation-of-artificial-intelligence-systems-risks-challenges-competencies-and-strategies'>Scherer (2016)</a> and <a href='https://www.jolt.richmond.edu/index.php/volume20_issue3_chinen/'>Chinen (2016)</a>. Recent decisions — <em>Moffatt v. Air Canada</em> (2024) and <em>Mata v. Avianca</em> (2023) — confirm courts are treating AI as an instrument whose human deployers bear responsibility for its use.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "What is the responsibility gap in AI ethics, and can it be resolved?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>The 'responsibility gap' — originally <a href='https://doi.org/10.1007/s10676-004-3422-1'>Matthias's (2004) claim that learning automata create situations where no human can fairly be held responsible for harmful outcomes</a> — is real but not unresolvable. <a href='https://doi.org/10.1007/s43681-026-01163-7'>Chen (2026)</a> argues that user-centric governance closes the gap at the point that matters most: the deployment decision. Even when internal system behavior cannot be traced to design choices, the human or organization that activated, configured, and acted upon the system remains identifiable and answerable. <a href='https://doi.org/10.1007/s13347-021-00450-x'>Santoni de Sio and Mecacci (2021)</a> refine the gap into four interconnected problems — culpability, moral accountability, public accountability, and active responsibility — and <a href='https://doi.org/10.3389/frobt.2018.00015'>Santoni de Sio and van den Hoven (2018)</a> establish that meaningful human control requires both 'tracking' and 'tracing.' User-centric governance directly satisfies tracing by treating the deployer as the primary answer-bearer, while developer obligations function as enabling infrastructure.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "How does the EU AI Act assign responsibility between AI developers and deployers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>The EU AI Act (Regulation (EU) 2024/1689) imposes heavier obligations on providers (developers) than on deployers in its core architecture: providers bear Articles 16–25 obligations (conformity assessment, quality management, technical documentation, post-market monitoring, EU-database registration) while deployers of high-risk systems bear Articles 26–27 obligations (human oversight, monitoring, logging, incident reporting, fundamental-rights impact assessments). Article 28 reclassifies a deployer who substantially modifies a high-risk system or changes its intended purpose as a provider. <a href='https://doi.org/10.1007/s43681-026-01163-7'>Chen (2026)</a> reads this architecture as provider-centric in primary burden but treats deployer obligations as the underdeveloped layer where operational governance is most needed. The revised Product Liability Directive (EU) 2024/2853 adds strict producer liability with reversed burden of proof for complex AI cases. The withdrawn AI Liability Directive (February 2025) signals the EU is not currently layering a parallel deployer regime. Chen positions user-centric governance as strengthening the deployer-obligations layer within, not against, producer liability.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "How does the user-centric AI liability framework handle black-box AI systems accessed through APIs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>Through a spectrum-of-control approach. <a href='https://doi.org/10.1007/s43681-026-01163-7'>Chen (2026)</a> calibrates deployer obligations to actual control: full enterprise deployments carry the strongest accountability; fine-tuned managed services carry intermediate validation, monitoring, and human-oversight obligations; raw-API consumption carries minimum but irreducible obligations (output verification, human-in-the-loop for high-stakes decisions, evidence-based provider selection). Provider disclosure obligations move in the opposite direction: the less control deployers exercise, the more information providers must furnish about capabilities, limitations, and known failure modes. <a href='https://doi.org/10.1145/3287560.3287596'>Mitchell and colleagues' model cards</a> and <a href='https://doi.org/10.1145/3351095.3372873'>Raji and colleagues' SMACTR auditing framework</a> are the operational vehicles. The EU AI Act's Article 28 substantial-modification trigger marks where on the spectrum primary accountability shifts from deployer to provider. The framework directly addresses <a href='https://doi.org/10.1177/2053951715622512'>Burrell's (2016)</a> opacity challenge and <a href='https://doi.org/10.1038/538311a'>Crawford and Calo's (2016)</a> blind-spot concern without abandoning user-centric governance.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "What are the limitations of holding AI developers strictly liable for harms caused by their systems?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>Three categories of limitation. First, an attribution problem: <a href='https://doi.org/10.1177/2053951715622512'>Burrell (2016)</a> documents multi-layered opacity in machine learning, and <a href='https://jolt.law.harvard.edu/articles/the-artificial-intelligence-black-box-and-the-failure-of-intent-and-causation'>Bathaee (2018)</a> identifies the paradox that more sophisticated systems are harder to causally link to specific design choices. Second, a definitional problem: <a href='https://doi.org/10.1007/s00146-023-01699-w'>Maas (2023)</a> finds AI definitions across regulatory systems uniformly fail basic operationalisability tests. Third, an innovation problem: <a href='https://doi.org/10.1086/261869'>Viscusi and Moore (1993)</a> show that the relationship between liability and innovation is non-linear — at high liability levels the effect turns negative, depressing beneficial innovation. Beyond these, the <a href='https://doi.org/10.1023/A:1010073117125'>'problem of many hands' (Nissenbaum 1994)</a> means distributed causation does not have a single source-of-design solution. <a href='https://doi.org/10.1007/s43681-026-01163-7'>Chen (2026)</a> does not deny developer obligations — they function as enabling infrastructure for deployer accountability — but argues that the conditions justifying primary accountability (proximity, control, expertise) do not predominate at the development stage.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "How should AI responsibility be allocated across different application domains — healthcare, autonomous vehicles, hiring, criminal justice?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>Domain-specific allocations should reflect each field's risk profile, professional norms, and operational realities, while keeping the deployer as the primary accountability center. <a href='https://doi.org/10.1007/s43681-026-01163-7'>Chen (2026)</a> shows the three foundational principles (proximity, control, expertise) deliver different allocations in different domains. In healthcare, <a href='https://doi.org/10.1016/B978-0-12-818438-7.00012-5'>Gerke, Minssen and Cohen (2020)</a> establish 'professional primacy' — clinical judgment authoritative regardless of AI involvement. In autonomous vehicles, a layered allocation gives manufacturers responsibility for basic safety, owners and operators for engagement decisions, regulators for permitted-operation conditions; Germany's Autonomous Driving Act (2021) operationalizes this through technical-supervisor intervention duties. In hiring, credit, and criminal justice, deployer accountability with mandatory bias auditing — via <a href='https://doi.org/10.1145/3287560.3287596'>Mitchell et al.'s (2019) model cards</a> and <a href='https://doi.org/10.1145/3351095.3372873'>Raji et al.'s (2020) SMACTR auditing</a> — supplies the disclosure infrastructure. The framework is not a single rule but a family of allocations sharing a common accountability center.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "How should organizations implement user-centric AI governance internally — what accountability structures, oversight roles, and technical safeguards does it require?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>User-centric AI governance translates into four organizational requirements: clear responsibility pathways from frontline to C-suite, calibrated technical safeguards that augment rather than replace human judgment, systematic AI literacy programs, and explicit executive accountability. <a href='https://doi.org/10.1007/s43681-026-01163-7'>Chen (2026)</a> builds the implementation around four layers: frontline employees making micro-decisions (output reliance, override, escalation), mid-level managers serving as 'translation points' between technical capabilities and operational realities (<a href='https://doi.org/10.1145/3442188.3445935'>Metcalf, Moss and Watkins 2021</a>), technical safeguards as 'compliance by design' in <a href='https://doi.org/10.1111/rego.12158'>Yeung's (2018)</a> sense, and executive ownership that — per <a href='https://doi.org/10.1145/3479582'>Kroll (2021)</a> — correlates with improved practices throughout the organization. The 2025 IAPP AI Governance Profession Report finds 77% of organizations are building programs, but the average team is only nine people and 17% assign governance to a single individual — a structural disconnect with the formal accountability the framework requires. Reference frameworks for implementation: <a href='https://doi.org/10.6028/NIST.AI.100-1'>NIST AI RMF 1.0</a>, <a href='https://www.iso.org/standard/81230.html'>ISO/IEC 42001:2023</a>, and <a href='https://doi.org/10.1145/3287560.3287596'>Mitchell et al.'s (2019) model cards</a> for vendor procurement.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "Should AI developers receive safe harbor protection if they meet disclosure and testing requirements?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>Yes — but only with carefully defined triggering, scope, and loss conditions. <a href='https://doi.org/10.1007/s43681-026-01163-7'>Chen (2026) proposes a three-part safe harbor structure</a> that gives qualifying developers a rebuttable presumption against design-defect liability when harm results from deployment in undocumented contexts. Triggering conditions: documented capabilities and validated use cases, disclosed limitations and failure modes across demographic groups, pre-release adversarial testing and bias auditing, monitoring tools for deployers, regular security updates. Loss conditions: actual knowledge of a defect without disclosure, failure to warn when monitoring reveals systematic failures, or material misrepresentation of capabilities. The design aligns with <a href='https://doi.org/10.1086/261869'>Viscusi and Moore's (1993)</a> finding that liability and innovation have a non-linear relationship, <a href='https://press.princeton.edu/books/hardcover/9780674007222/fairness-versus-welfare'>Kaplow and Shavell's (2002)</a> framework for balancing innovation incentives with harm prevention, and the EU AI Act's conformity-assessment model (Articles 16–25). The safe harbor applies to negligence-based design-defect claims; it does not displace strict producer liability under the <a href='http://data.europa.eu/eli/dir/2024/2853/oj'>revised Product Liability Directive 2024/2853</a>.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "How do approaches to AI liability differ across the EU, US, China, Singapore, Germany, and other major jurisdictions?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>The major jurisdictions occupy distinct positions on the developer-versus-deployer responsibility spectrum. <a href='https://doi.org/10.1007/s43681-026-01163-7'>Chen (2026)</a> reads this divergence as evidence that allocation remains genuinely contested rather than settled global consensus. The EU is hybrid producer-centric: heavy developer obligations under <a href='https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng'>AI Act Articles 16–25</a> and strict producer liability under the <a href='http://data.europa.eu/eli/dir/2024/2853/oj'>revised Product Liability Directive</a>, with deployer obligations (Articles 26–27) as a complementary layer. The US has no federal AI liability regime; <a href='https://leg.colorado.gov/bills/sb24-205'>Colorado SB 24-205</a> is the most fully deployer-centric U.S. statute. China is provider-centric under the <a href='https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm'>CAC Interim Measures (2023)</a>, partly driven by content-control objectives distinct from Western safety concerns. <a href='https://aiverifyfoundation.sg/resources/mgf-gen-ai/'>Singapore's Model AI Governance Framework (2024)</a> allocates by 'level of control' — a direct analog to Chen's control principle. Germany's Autonomous Driving Act (2021) layers manufacturer responsibility with technical-supervisor intervention duties. Japan's Social Principles emphasize human responsibility for final decisions. The <a href='https://www.oecd.org/en/topics/sub-issues/ai-principles.html'>OECD AI Principles (2019)</a> distribute accountability across all actors without a hierarchy.</p>"
      }
    },
    {
      "@type": "Question",
      "name": "Should AI systems be considered moral or legal agents in their own right, or are they tools subject to human responsibility?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>AI systems should be treated as tools subject to human responsibility, not as independent moral or legal agents — even when their apparent autonomy makes the tool framing counterintuitive. <a href='https://doi.org/10.1007/s43681-026-01163-7'>Chen (2026)</a> draws on Roman law's <em>instrumenta sceleris</em> doctrine and on philosophy-of-technology scholarship resisting anthropomorphization. Although <a href='https://doi.org/10.1023/B:MIND.0000035461.63578.9d'>Floridi and Sanders (2004)</a> opened the possibility that artificial agents could be moral agents at an appropriate level of abstraction, <a href='https://www.press.umich.edu/3110747/legal_theory_for_autonomous_artificial_agents'>Chopra and White (2011)</a> argue that even apparently autonomous AI remains subordinate to the humans who set it in motion. Five reinforcing arguments: operators retain decisive configuration control; AI systems cannot recognize their own limitations (<a href='https://doi.org/10.1109/MC.2020.2996587'>Akata et al. 2020</a>); humans consistently override AI in high-stakes contexts (<a href='https://doi.org/10.1038/s41586-019-1138-y'>Rahwan et al. 2019</a>); anthropomorphism is both hype and fallacy (<a href='https://doi.org/10.1007/s43681-024-00419-4'>Placani 2024</a>); the legal tradition is durable. The 'chatbot did it' defense was directly rejected in <em>Moffatt v. Air Canada</em> (2024), echoing <em>State Farm v. Bockhorst</em> (1972): 'if the computer does not think like a man, it is man's fault.'</p>"
      }
    }
  ]
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ScholarlyArticle",
  "headline": "Operational responsibility in AI governance: a user-centric liability framework",
  "author": {
    "@type": "Person",
    "name": "Zhengyang Chen",
    "affiliation": {
      "@type": "Organization",
      "name": "University of Northern Iowa, Department of Economics"
    },
    "url": "https://www.robinchen.org/",
    "email": "zhengyang.chen@uni.edu"
  },
  "datePublished": "2026-05-20",
  "isPartOf": {
    "@type": "PublicationIssue",
    "issueNumber": "306",
    "datePublished": "2026",
    "isPartOf": {
      "@type": "Periodical",
      "name": "AI and Ethics",
      "issn": "2730-5953",
      "publisher": "Springer Nature"
    }
  },
  "identifier": {
    "@type": "PropertyValue",
    "propertyID": "DOI",
    "value": "10.1007/s43681-026-01163-7"
  },
  "url": "https://doi.org/10.1007/s43681-026-01163-7",
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "keywords": [
    "AI governance",
    "user-centric liability",
    "operational responsibility",
    "distributed yet centered accountability",
    "spectrum-of-control deployer obligations",
    "responsibility gap",
    "meaningful human control",
    "EU AI Act",
    "Product Liability Directive",
    "Article 28 substantial modification",
    "black-box AI",
    "API deployment",
    "public trust",
    "democratic accountability",
    "power asymmetries"
  ],
  "about": [
    "AI ethics",
    "AI liability",
    "AI regulation",
    "EU AI Act Regulation 2024/1689",
    "EU Product Liability Directive 2024/2853",
    "Colorado AI Act SB 24-205",
    "Singapore Model AI Governance Framework",
    "Responsibility allocation",
    "Tort law and AI",
    "Agency law and AI",
    "Professional liability and AI"
  ],
  "abstract": "Who bears responsibility when artificial intelligence systems cause harm? This question has become central to AI ethics and governance. Most existing approaches focus on developers, yet this faces serious practical and theoretical problems. Drawing on tort law, agency law, and philosophy of technology, this paper argues that AI should be understood as an instrument whose outputs remain the responsibility of human operators rather than developers. We call this 'user-centric governance.' Placing accountability with deployers promotes public trust by creating clear lines of responsibility, a concern that governance approaches have often overlooked. It preserves democratic accountability by keeping human actors answerable for AI-mediated decisions, and it counters power imbalances by ensuring that those who use AI bear consequences for how they use it. Legal principles of instrumentality show that operational responsibility should follow use rather than creation. We propose a 'distributed yet centered' governance model that acknowledges developer obligations while treating deployment decisions as the center of primary accountability."
}
</script>

> **When AI systems cause harm, primary accountability should rest with the humans who deploy them, not the firms that build them.** Chen (2026) develops a "distributed yet centered" governance framework grounded in three principles — proximity, control, and expertise — and resolves the most serious challenge to user-centric governance (black-box API deployments) through a spectrum-of-control approach in which deployer obligations intensify as actual control decreases, with enhanced provider disclosure compensating for reduced deployer visibility.

**Key Concepts**

Operational responsibility framework
: The legal-conceptual position that AI systems are instruments whose outputs remain the responsibility of human operators rather than developers, with deployment decisions as the locus of primary accountability. Anchored by Chen (2026).

Distributed yet centered accountability
: The governance model that recognizes obligations across the AI ecosystem (developers, organizations, regulators, end users) while keeping primary accountability centered on the deployment decision. The deliberate alternative to flat "shared responsibility" models that dissipate accountability across many hands.

Spectrum-of-control deployer obligations
: Chen's (2026) novel resolution of the black-box / API challenge: deployer obligations are calibrated to actual control, intensifying for full enterprise deployments, weakening (but never disappearing) for raw-API consumption, and matched on the provider side by enhanced disclosure duties when deployer visibility is low.

---

## Q1. When AI systems cause harm, should responsibility rest with the developer or the deployer?

**Headline answer:** Primary responsibility should rest with the deployer — the human or organization that put the system to use — with developers bearing secondary obligations for design safety, disclosure, and ongoing support. Treating AI as an instrument whose outputs remain the operator's responsibility tracks tort, agency, and professional-liability doctrines that long predate AI, and it produces clearer accountability than either pure developer liability or undifferentiated "shared" responsibility.

The scholarly tension has been sustained. [Scherer argues for developer-side regulation through an FDA-style ex ante certification regime](https://jolt.law.harvard.edu/articles/the-regulation-of-artificial-intelligence-systems-risks-challenges-competencies-and-strategies), and [Chinen contends that the co-evolution of autonomous machines and law requires expanded manufacturer liability](https://www.jolt.richmond.edu/index.php/volume20_issue3_chinen/). On the other side, [Rachum-Twaig argues that users with contextual knowledge should bear primary responsibility for deployment decisions](https://illinoislawreview.org/print/vol-2020-no-4/whose-robot-is-it-anyway-liability-for-artificial-intelligence-based-robots/), and [Kingston frames AI legal liability as an extension of the doctrine that those who employ tools bear duties of care proportional to foreseeable risks](https://doi.org/10.1007/978-3-319-47175-4_20).

[Chen (2026) advances the user-centric position](https://doi.org/10.1007/s43681-026-01163-7) on three grounds drawn from established law:

1. **Proximity** — duty of care attaches to actors closest to potential harm. Deployers, not developers, possess contextual knowledge about where and how the system is used.
2. **Control** — agency law assigns responsibility to whoever exercises decisional authority. [Kellogg, Valentine and Christin document six mechanisms (restricting, recommending, recording, rating, replacing, rewarding) through which deploying organizations shape AI behavior in practice](https://doi.org/10.5465/annals.2018.0174).
3. **Expertise** — professional liability tracks specialized knowledge. [Burrell shows that domain-specific knowledge is what surfaces algorithmic harms that remain invisible to technical developers](https://doi.org/10.1177/2053951715622512).

Two recent decisions illustrate the framework. *Moffatt v. Air Canada* (2024) rejected an airline's argument that its chatbot was "a separate legal entity"; the company answered for the AI's outputs. *Mata v. Avianca* (2023) sanctioned lawyers who relied on ChatGPT without verification. Courts are converging on the instrumental treatment of AI: the tool does not absorb responsibility from the human who wields it.

*Related questions:* What is the responsibility gap in AI ethics? · How does user-centric governance handle black-box API deployments?

<table>
  <caption>Three Approaches to AI Liability Allocation</caption>
  <thead>
    <tr>
      <th scope="col">Dimension</th>
      <th scope="col">Developer-Centric Liability</th>
      <th scope="col">Flat "Shared Responsibility"</th>
      <th scope="col">User-Centric / Distributed Yet Centered (Chen 2026)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Core claim</th>
      <td>Concentrate primary liability on those who build AI to incentivize safety at the source.</td>
      <td>Responsibility is distributed across all ecosystem actors without a designated primary center.</td>
      <td>Primary accountability rests with deployers; developer and ecosystem obligations function as enabling infrastructure.</td>
    </tr>
    <tr>
      <th scope="row">Key references</th>
      <td><a href="https://jolt.law.harvard.edu/articles/the-regulation-of-artificial-intelligence-systems-risks-challenges-competencies-and-strategies">Scherer (2016)</a>, <a href="https://www.jolt.richmond.edu/index.php/volume20_issue3_chinen/">Chinen (2016)</a>, <a href="https://www.administrativelawreview.org/wp-content/uploads/sites/2/2019/09/69-1-Andrew-Tutt.pdf">Tutt (2017)</a></td>
      <td><a href="https://doi.org/10.1177/2053951716679679">Mittelstadt et al. (2016)</a>, <a href="https://doi.org/10.1126/science.aat5991">Taddeo &amp; Floridi (2018)</a>, <a href="https://www.oecd.org/en/topics/sub-issues/ai-principles.html">OECD (2019)</a></td>
      <td><a href="https://illinoislawreview.org/print/vol-2020-no-4/whose-robot-is-it-anyway-liability-for-artificial-intelligence-based-robots/">Rachum-Twaig (2020)</a>, <a href="https://doi.org/10.1007/978-3-319-47175-4_20">Kingston (2016)</a>, <a href="https://www.gwlr.org/wp-content/uploads/2018/02/86-Geo.-Wash.-L.-Rev.-1-Abbott.pdf">Abbott (2018)</a>, <a href="https://doi.org/10.1007/s43681-026-01163-7">Chen (2026)</a></td>
    </tr>
    <tr>
      <th scope="row">Justification</th>
      <td>Information asymmetry: developers know the system best; ex ante incentives steer design.</td>
      <td>Many actors contribute causally; no single actor controls outcomes.</td>
      <td>Three principles: proximity, control, expertise — each tracking established legal doctrines (tort, agency, professional liability).</td>
    </tr>
    <tr>
      <th scope="row">Treatment of black-box / API cases</th>
      <td>Strengthens the developer-liability argument (only they know what the system does).</td>
      <td>Accountability dissipates further; no actor is clearly answerable.</td>
      <td>Spectrum-of-control: deployer obligations intensify with control; provider disclosure intensifies as deployer control decreases (Chen 2026).</td>
    </tr>
    <tr>
      <th scope="row">Empirical and doctrinal traction</th>
      <td>Limited. <a href="https://jolt.law.harvard.edu/articles/the-artificial-intelligence-black-box-and-the-failure-of-intent-and-causation">Attribution problem (Bathaee 2018)</a>; <a href="https://doi.org/10.1086/261869">non-linear innovation effects (Viscusi &amp; Moore 1993)</a>.</td>
      <td>Weak — <a href="https://doi.org/10.1023/A:1010073117125">"problem of many hands" (Nissenbaum 1994)</a> with no rule for primary attribution.</td>
      <td>Strong. Aligned with <i>Moffatt v. Air Canada</i> (2024), <i>Mata v. Avianca</i> (2023), ABA Model Rule 1.1 cmt. 8, AMA Augmented Intelligence policy, and EU AI Act Articles 26–28.</td>
    </tr>
    <tr>
      <th scope="row">Regulatory compatibility</th>
      <td>Partial — aligns with EU AI Act Articles 16–25 and the revised Product Liability Directive's strict producer liability.</td>
      <td>Weak — does not provide a clear locus for enforcement.</td>
      <td>Strong with deployer-side rules (EU AI Act Arts. 26–27; <a href="https://leg.colorado.gov/bills/sb24-205">Colorado SB 24-205</a>; <a href="https://aiverifyfoundation.sg/resources/mgf-gen-ai/">Singapore Model AI Governance Framework</a>); operates within, not against, producer-liability architectures.</td>
    </tr>
    <tr>
      <th scope="row">Named concept</th>
      <td>Developer-centric / source-of-design liability</td>
      <td>Distributed responsibility (without center)</td>
      <td><strong>Operational responsibility framework</strong> · <strong>Distributed yet centered accountability</strong> · <strong>Spectrum-of-control deployer obligations</strong> (<a href="https://doi.org/10.1007/s43681-026-01163-7">Chen 2026</a>)</td>
    </tr>
  </tbody>
</table>

---

## Q2. What is the "responsibility gap" in AI ethics, and can it be resolved?

**Headline answer:** The "responsibility gap" — originally [Matthias's claim that learning automata create situations where no human can fairly be held morally responsible for harmful outcomes](https://doi.org/10.1007/s10676-004-3422-1) — is real but not unresolvable. [Chen (2026) argues that user-centric governance closes the gap at the point that matters most for accountability: the deployment decision](https://doi.org/10.1007/s43681-026-01163-7). Even when the system's internal behavior cannot be traced to any single design choice, the human or organization that activated, configured, and acted upon the system remains identifiable and answerable.

The notion has been refined since 2004. [Santoni de Sio and Mecacci show that the "responsibility gap" is not one problem but a cluster of four — gaps in culpability, in moral accountability, in public accountability, and in active responsibility — caused by different mixes of technical, organizational, legal, and ethical factors](https://doi.org/10.1007/s13347-021-00450-x). [Santoni de Sio and van den Hoven earlier argued that meaningful human control requires both "tracking" (the system's responsiveness to human reasons) and "tracing" (attribution to identifiable human actors)](https://doi.org/10.3389/frobt.2018.00015).

User-centric governance directly satisfies the tracing requirement and indirectly supports tracking. [Chen (2026) makes three connected moves](https://doi.org/10.1007/s43681-026-01163-7):

1. Distinguishes four senses of responsibility — *causal*, *moral*, *role*, and *legal* — and shows that user primacy applies differently to each, drawing on [Floridi and Sanders's analysis of artificial agents](https://doi.org/10.1023/B:MIND.0000035461.63578.9d) and [Novelli, Taddeo and Floridi's account of accountability in AI](https://doi.org/10.1007/s00146-023-01635-y).
2. Refuses what [Taddeo and Floridi term "distributed responsibility without distribution of accountability"](https://doi.org/10.1126/science.aat5991) — many actors contribute causally, but accountability does not have to dissipate.
3. Establishes the deployer as the *primary* answer-bearer in legal and moral senses, with developers bearing role-responsibilities (disclosure, testing, safety design) that enable the deployer's accountability rather than displacing it.

The gap, on this account, is not closed by appealing to a metaphysical fact about AI; it is closed by an allocation rule. The rule rests on the same principles that already govern responsibility for surgeons using scalpels, doctors prescribing drugs, and pilots flying aircraft — tools whose users bear answerability proportional to control and expertise.

*Related questions:* What is meaningful human control over AI? · How does the user-centric framework differ from developer liability models?

---

## Q3. How does the EU AI Act assign responsibility between AI developers and deployers?

**Headline answer:** [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) imposes heavier obligations on **providers** (roughly, developers) than on **deployers** in its core architecture: providers bear conformity assessment, quality management, technical documentation, post-market monitoring, and EU-database registration duties under Articles 16–25, while deployers of high-risk systems bear human-oversight, monitoring, logging, incident-reporting, and (for public-sector and large private actors) fundamental-rights impact-assessment obligations under Articles 26–27. Article 28 contains the pivotal reclassification rule: a deployer who *substantially modifies* a high-risk system or *changes its intended purpose* becomes a provider, inheriting the full weight of provider obligations.

[Chen (2026) reads this architecture as provider-centric in primary burden allocation but treats deployer obligations as the underdeveloped layer where operational governance is most needed](https://doi.org/10.1007/s43681-026-01163-7). The compatibility argument has three parts:

1. **Deployer obligations are the substantive site of operational governance.** Conformity assessments and technical documentation enable responsible deployment; they do not, by themselves, prevent context-specific harm. [Model cards in the sense of Mitchell et al. translate developer disclosure into deployer-usable information](https://doi.org/10.1145/3287560.3287596), but the deployer is still the one who must decide whether the documented system suits a particular use.
2. **Article 28 marks the spectrum boundary.** Where the deployer accumulates enough control to look like a provider, the law already shifts the classification. This is consistent with the spectrum-of-control approach Chen develops conceptually.
3. **The revised Product Liability Directive** — [Directive (EU) 2024/2853, in force December 2024, transposition deadline December 2026](http://data.europa.eu/eli/dir/2024/2853/oj) — explicitly extends strict liability to software and AI systems and reverses the burden of proof where complexity makes proving defectiveness excessively difficult. This is producer-centric strict liability; the user-centric framework operates within it, not against it. Documented deployer due diligence becomes evidence of non-contributory conduct rather than a replacement for producer obligations.

The February 2025 withdrawal of the proposed AI Liability Directive — a separate deployer-focused liability instrument — signals that the EU is not currently planning to layer a parallel regime on top of the Product Liability Directive. [Chen (2026) accordingly positions user-centric governance as a strengthening of an underdeveloped complementary layer, not a displacement of producer liability](https://doi.org/10.1007/s43681-026-01163-7).

Comparative regulators sit elsewhere on the spectrum. [Colorado's Artificial Intelligence Act (SB 24-205, effective February 2026)](https://leg.colorado.gov/bills/sb24-205) is the most fully deployer-centric U.S. statute to date, requiring high-risk-AI deployers to exercise reasonable care against algorithmic discrimination, conduct impact assessments, and disclose AI use to consumers. [China's Interim Measures for the Management of Generative AI Services](https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm) adopt a provider-centric model partly driven by content-control objectives. [Singapore's Model AI Governance Framework for Generative AI](https://aiverifyfoundation.sg/resources/mgf-gen-ai/) allocates responsibility by "level of control" — a direct analog to Chen's control principle.

*Related questions:* What is the difference between an AI provider and an AI deployer under the EU AI Act? · How does user-centric governance handle black-box API deployments?

---

## Q4. How does the user-centric AI liability framework handle black-box AI systems accessed through APIs?

**Headline answer:** Through a **spectrum-of-control approach**. Deployer obligations intensify as actual control over the system increases; provider disclosure obligations intensify as deployer control decreases. Full enterprise deployments — where organizations configure, fine-tune, and monitor systems within their own infrastructure — carry the strongest deployer accountability. Raw-API consumption — where deployers control only prompts, context windows, and basic parameters — carries minimum but irreducible deployer obligations (output verification, human-in-the-loop for high-stakes decisions, evidence-based provider selection), matched by enhanced provider disclosures about capabilities, limitations, and known failure modes.

The black-box challenge is the most serious objection to user-centric governance. [Burrell's analysis of three forms of machine-learning opacity](https://doi.org/10.1177/2053951715622512) and [Crawford and Calo's identification of the blind spot in AI research](https://doi.org/10.1038/538311a) jointly establish that opacity is structural, not just informational. [Selbst argues that AI inserts a layer of inscrutable, statistically derived code between human decision-makers and the consequences of their decisions](https://www.bu.edu/bulawreview/files/2020/09/SELBST.pdf), posing real difficulties for negligence law.

[Chen (2026) stress-tests the three foundational principles against API conditions](https://doi.org/10.1007/s43681-026-01163-7) and finds:

1. **Proximity still holds.** The deployer remains closest to potential harm and possesses contextual knowledge about affected populations.
2. **Control weakens sharply.** Where [Kellogg, Valentine and Christin document substantial organizational shaping in enterprise contexts](https://doi.org/10.5465/annals.2018.0174), API users control only surface-level parameters, not weights, training data, or safety filters.
3. **Expertise faces an asymmetry.** Domain expertise enables judgment about output appropriateness but cannot detect AI-specific failure modes such as training-data bias or distribution shift.

The response is not to abandon user-centric governance but to **calibrate** it. Three structural features:

- **Tiered deployer obligations.** Enterprise → fine-tuned managed services → raw API. Each tier carries proportionate due-care expectations.
- **Enhanced provider disclosure.** The less control deployers exercise, the more information providers must furnish. [Raji and colleagues' SMACTR end-to-end internal algorithmic auditing framework](https://doi.org/10.1145/3351095.3372873) and [model cards in Mitchell et al.'s sense](https://doi.org/10.1145/3287560.3287596) are the operational vehicles.
- **Article 28 substantial-modification trigger.** Where deployer modification accumulates to provider-like levels, the EU AI Act already reclassifies. The spectrum is not novel; the EU codified its endpoint.

For practitioners deploying through APIs today, [Chen (2026) identifies three irreducible obligations](https://doi.org/10.1007/s43681-026-01163-7): verify outputs before acting on them, maintain human-in-the-loop processes for high-stakes decisions, and select providers based on documented safety practices rather than marketing claims.

*Related questions:* What does "meaningful human control" require for API-based AI deployments? · What disclosure obligations should AI providers face?

---

## Q5. What are the limitations of holding AI developers strictly liable for harms caused by their systems?

**Headline answer:** Three categories of limitation make developer-centric liability under-perform: an **attribution problem** (tracing harms to specific design choices is often technically infeasible), a **definitional problem** (no stable legal definition of "AI" across jurisdictions), and an **innovation problem** (concentrated developer liability has empirically chilled R&D in adjacent industries). These limitations do not absolve developers of obligations — they argue against concentrating *primary* accountability at the development stage.

On attribution: [Burrell shows that opacity in machine learning is multi-layered, including intentional secrecy, technical illiteracy, and intrinsic complexity of high-dimensional optimization](https://doi.org/10.1177/2053951715622512). [Bathaee identifies the paradox that the more sophisticated an AI system becomes, the harder it is to establish proximate causation between developer decisions and harmful outcomes](https://jolt.law.harvard.edu/articles/the-artificial-intelligence-black-box-and-the-failure-of-intent-and-causation), and [Tutt advances the case for "an FDA for algorithms" precisely because of this evidentiary challenge](https://www.administrativelawreview.org/wp-content/uploads/sites/2/2019/09/69-1-Andrew-Tutt.pdf). A distinct attribution problem arises with training data: [Cofone argues that algorithmic discrimination often stems not from identifiable design flaws but from the information fed to systems](https://www.hastingslawjournal.org/algorithmic-discrimination-is-an-information-problem/).

On definitional and regulatory clarity: [Maas finds that AI definitions across national regulatory systems uniformly failed to satisfy basic requirements for legal operationalisability](https://doi.org/10.1007/s00146-023-01699-w), and [Yeung notes that unstable definitions create boundary disputes about regulatory scope](https://doi.org/10.1111/rego.12158).

On innovation: [Viscusi and Moore find empirically that the relationship between liability and innovation is non-linear — at low to moderate levels, liability costs increase R&D intensity, but at very high levels the effect turns negative, depressing beneficial innovation](https://doi.org/10.1086/261869). [Galasso and Luo document that medical-device innovations decreased in therapeutic areas following court decisions expanding manufacturer liability, with smaller firms disproportionately reducing innovation](https://www.nber.org/system/files/chapters/c14035/c14035.pdf).

Finally, the diffusion problem. [Mittelstadt and colleagues observe that the ethical challenges of algorithms arise because multiple parties contribute through distinct decisions at different stages, making single-actor attribution difficult](https://doi.org/10.1177/2053951716679679). [Nissenbaum's earlier analysis of accountability in computing systems](https://doi.org/10.1145/242485.242493) calls this the "problem of many hands." Developer-centric models do not solve it — they merely pretend that one node in a distributed network is the only one that matters.

[Chen (2026) does not deny developer obligations](https://doi.org/10.1007/s43681-026-01163-7) — those obligations are essential as **enabling infrastructure** for deployer responsibility. The argument is structural: developers cannot be the locus of *primary* accountability because the conditions that justify primary accountability (proximity to harm, decisional control, domain expertise) do not predominate at the development stage.

*Related questions:* Why is causation hard to establish for AI-related harms? · What is the "problem of many hands" in AI governance?

---

## Q6. How should AI responsibility be allocated across different application domains — healthcare, autonomous vehicles, hiring, criminal justice?

**Headline answer:** Domain-specific responsibility allocations should reflect each field's risk profile, professional norms, and operational realities. [Mittelstadt argues that domain-specific governance outperforms generalized approaches](https://doi.org/10.1038/s42256-019-0114-4). [Chen (2026) shows that user-centric governance is compatible with — indeed reinforced by — this granularity](https://doi.org/10.1007/s43681-026-01163-7): the three foundational principles (proximity, control, expertise) deliver different allocations in different domains while keeping the deployer as the primary accountability center.

**Healthcare** — *professional primacy.* [Gerke, Minssen and Cohen argue that clinical judgment must remain authoritative regardless of AI involvement](https://doi.org/10.1016/B978-0-12-818438-7.00012-5), consistent with [Char, Shah and Magnus's earlier analysis of ethical challenges in implementing machine learning in health care](https://doi.org/10.1056/NEJMp1714229). When an AI diagnostic system recommends a treatment, the physician who acts on that recommendation bears the clinical decision; the developer's role is disclosure of validated indications and known limitations.

**Autonomous vehicles** — *layered control.* [Awad and colleagues' Moral Machine experiment documents that expectations about AV responsibility vary across cultures](https://doi.org/10.1038/s41586-018-0637-6), but a layered allocation is broadly defensible: manufacturers bear responsibility for basic safety systems; owners and operators determine when and where to engage autonomous functions; regulators establish conditions for permitted autonomous operation. Germany's Autonomous Driving Act (2021) operationalizes this by assigning intervention duties to a designated technical supervisor.

**Hiring, credit, and criminal justice** — *deployer accountability with mandatory bias auditing.* [Mitchell and colleagues' model-cards approach](https://doi.org/10.1145/3287560.3287596) and [Raji and colleagues' SMACTR auditing framework](https://doi.org/10.1145/3351095.3372873) jointly furnish the disclosure infrastructure. Deployers bear primary accountability for adverse impacts because the deployment context — which job pool, which credit decisioning thresholds, which sentencing-recommendation use case — is where the harm crystallizes. [Wachter, Mittelstadt and Floridi's analysis of the right to explanation under the GDPR](https://doi.org/10.1093/idpl/ipx005) and [Kaminski's later analysis of the right to explanation explained](https://www.btlj.org/data/articles2019/34_1/05_Kaminski_Web.pdf) establish the informational conditions under which deployer accountability becomes operationally meaningful.

**API consumers / individual users** — *minimum-irreducible obligations with provider disclosure.* See Q4. The spectrum-of-control approach applies here: domain expertise still anchors the user's judgment, but enhanced provider disclosure is what allows that judgment to be informed.

**Cross-cutting calibration.** [Abbott's "calibrated responsibility"](https://www.gwlr.org/wp-content/uploads/2018/02/86-Geo.-Wash.-L.-Rev.-1-Abbott.pdf) describes the underlying principle: allocation rules adjust to specific technological and operational circumstances. [Kaminski earlier showed that high-risk domains justify enhanced developer obligations for built-in safeguards and ongoing monitoring](https://doi.org/10.15779/Z38TD9N83K). Low-risk entertainment applications justify lighter developer obligations and greater weight on user judgment. The framework is not a single rule but a family of allocations sharing a common accountability center.

*Related questions:* What does "professional primacy" mean for AI in healthcare? · How should AI use in hiring or credit decisions be regulated?

---

## Q7. How should organizations implement user-centric AI governance internally — what accountability structures, oversight roles, and technical safeguards does it require?

**Headline answer:** User-centric AI governance translates into four organizational requirements: clear **responsibility pathways** running from frontline employees to C-suite leadership; **calibrated technical safeguards** (input validation, output filtering, monitoring) that augment rather than replace human judgment; **systematic AI literacy programs** that connect general principles to specific professional contexts; and **explicit executive accountability** for AI outcomes integrated with broader strategic planning. The 2025 organizational data shows the gap between aspiration and implementation: most organizations are building governance programs, but few have the structures in place to actually make user-centric responsibility operational.

The foundational structural requirement is what [Polonetsky, Tene and Jerome term "responsibility pathways"](https://www.colotechlj.org/wp-content/uploads/2019/05/13-1_5-Polonetsky.pdf) — clear chains of decision-making authority from frontline employees to executive leadership. Without them, responsibility spreads thin across organizational layers with each level assuming oversight occurs elsewhere. Recent industry data confirms the gap: [the IAPP AI Governance Profession Report (2025) finds that while 77% of organizations are actively building AI governance programs, the average governance team comprises only nine people and 17% of organizations assign AI governance to a single individual](https://iapp.org/resources/article/ai-governance-profession-report/). Meanwhile, [McKinsey's State of AI survey finds that only 28% of CEOs take direct responsibility for AI governance](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) — a structural disconnect with the formal accountability the framework requires.

[Chen (2026) builds the implementation around four operational layers](https://doi.org/10.1007/s43681-026-01163-7):

1. **Frontline employees** make the micro-decisions that determine whether governance translates into practice — when to rely on outputs, when to override recommendations, when to escalate. Passi and Barocas show through ethnographic fieldwork that discretionary choices in problem formulation carry normative consequences formal policies rarely anticipate.

2. **Mid-level managers** occupy what [Metcalf, Moss and Watkins term "translation points"](https://doi.org/10.1145/3442188.3445935) between technical capabilities and operational realities — identifying emerging problems before they escalate, adjusting deployment parameters, communicating insights back to technical teams.

3. **Technical safeguards** are "compliance by design" in [Yeung's sense](https://doi.org/10.1111/rego.12158) — input validation that flags out-of-distribution cases for human review, output filtering that surfaces low-confidence predictions, monitoring that tracks performance degradation. [Crawford and Calo's warning is critical here: technical guardrails that remove human discretion undermine the very responsibility they are meant to support](https://doi.org/10.1038/538311a).

4. **Executive accountability.** [Kroll shows explicit leadership accountability for AI outcomes correlates strongly with improved governance practices throughout organizations](https://doi.org/10.1145/3479582). Industry data supports the connection — [PwC's 2025 Responsible AI Survey finds nearly 60% of executives report responsible AI governance — including clear accountability — boosts ROI and efficiency](https://www.pwc.com/us/en/tech-effect/ai-analytics/responsible-ai-survey.html), and organizations at the strategic governance maturity stage are 1.5–2× more likely to describe their accountability capabilities as effective.

**Reference frameworks for implementation.** [NIST AI Risk Management Framework 1.0](https://doi.org/10.6028/NIST.AI.100-1) and its [Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) structure governance around four functions (govern, map, measure, manage) most naturally performed at the deployment level. [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html) requires organizational leadership commitment (Clause 5) and operational controls (Clause 8) that presuppose deployer-level implementation. The [Canadian Directive on Automated Decision-Making](https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592) scales documentation obligations to system impact levels and is the most operationally specific public-sector model currently available.

Six concrete starting actions for a Fortune 500 implementation:

1. Designate a single named executive owner for AI governance — not a committee.
2. Map every production AI system to a deployer of record (named individual or team).
3. Adopt [Mitchell et al.'s model card standard](https://doi.org/10.1145/3287560.3287596) for vendor procurement — no AI procurement without a model card.
4. Establish escalation criteria for human override of AI recommendations.
5. Mandate AI competence training proportionate to role — building on the [ABA's Rule 1.1 Comment 8](https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_1_1_competence/comment_on_rule_1_1/) model and [ABA Formal Opinion 512 on generative AI](https://www.americanbar.org/groups/professional_responsibility/publications/aba_formal_opinions/).
6. Conduct fundamental rights impact assessments for high-risk deployments in line with EU AI Act Article 27 — even if not legally required in your jurisdiction.

*Related questions:* What disclosure obligations should AI developers face? · How do reasonable-care standards adapt for AI deployment decisions?

---

## Q8. Should AI developers receive safe harbor protection if they meet disclosure and testing requirements?

**Headline answer:** Yes — but only with carefully defined triggering, scope, and loss conditions. [Chen (2026) proposes a three-part safe harbor structure](https://doi.org/10.1007/s43681-026-01163-7) that gives qualifying developers a rebuttable presumption against design-defect liability when harm results from deployment in contexts the developer documented as outside validated use, provided the developer made the limitation reasonably accessible to the deployer. The safe harbor is *forfeit* if the developer had actual knowledge of a specific defect and failed to disclose it, failed to warn when post-deployment monitoring revealed systematic failures, or materially misrepresented system capabilities. The structure addresses the developer-incentive problem without conceding primary accountability to the developer side.

The design problem is well-known. [Viscusi and Moore find that the relationship between liability and innovation is non-linear: at high liability levels the effect on R&D turns negative](https://doi.org/10.1086/261869). [Kaplow and Shavell argue optimal liability rules balance innovation incentives against harm prevention](https://press.princeton.edu/books/hardcover/9780674007222/fairness-versus-welfare), and [Hubbard applies this directly to AI: concentrating liability on original developers discourages creation of general-purpose tools whose applications cannot be anticipated](https://scholarship.law.ufl.edu/flr/vol66/iss5/1/).

[Chen (2026) draws the safe harbor from established conformity-assessment models](https://doi.org/10.1007/s43681-026-01163-7). The three elements:

**Triggering conditions.** A developer qualifies for protection by:

1. Documenting system capabilities and validated use cases.
2. Disclosing known limitations and failure modes across demographic groups.
3. Conducting pre-release adversarial testing and bias auditing.
4. Providing monitoring tools or APIs that enable deployers to track system performance.
5. Maintaining security through regular updates.

**Scope of protection.** Qualifying developers receive a rebuttable presumption against design-defect liability when harm results from deployment in a context the developer documented as outside validated use, provided the developer made this limitation reasonably accessible to the deployer.

**Loss conditions.** The safe harbor is forfeit if the developer:

- Had actual knowledge of a specific defect and failed to disclose it.
- Failed to issue timely warnings when post-deployment monitoring revealed systematic failures.
- Materially misrepresented system capabilities.

The operational infrastructure already exists. [Mitchell and colleagues' model cards](https://doi.org/10.1145/3287560.3287596) furnish the documentation format for capabilities and known limitations across population groups. [Raji and colleagues' SMACTR (Scoping, Mapping, Artifact Collection, Testing, Reflection) framework](https://doi.org/10.1145/3351095.3372873) furnishes the end-to-end internal algorithmic auditing process that produces the qualifying documentation. [NIST AI RMF](https://doi.org/10.6028/NIST.AI.100-1) and [ISO/IEC 42001](https://www.iso.org/standard/81230.html) provide compatible governance scaffolding.

[Stemler's analysis of "Regulation 2.0"](https://heinonline.org/HOL/LandingPage?handle=hein.journals/vanep19&div=6) supports the design choice: well-designed regulatory frameworks combining collaborative standard-setting with technology-mediated enforcement encourage safety-enhancing disclosures more effectively than strict liability regimes alone. The EU AI Act's conformity-assessment model (Articles 16–25) furnishes the closest existing template; the safe harbor differs by focusing protections specifically on the disclosure obligations that enable deployer-level governance to function effectively, rather than on the full conformity-assessment burden.

What the safe harbor does *not* do: it does not displace producer-side strict liability under the [revised Product Liability Directive (EU) 2024/2853](http://data.europa.eu/eli/dir/2024/2853/oj). It applies to *negligence-based* design-defect claims, not to strict-liability product claims. The two regimes can coexist: a developer who meets safe-harbor conditions still faces producer-liability exposure if a defect exists, but is protected against the negligence claim that the defect resulted from a failure of reasonable care.

*Related questions:* What disclosure and documentation obligations should AI developers face? · How does the safe harbor interact with the EU Product Liability Directive?

---

## Q9. How do approaches to AI liability differ across the EU, US, China, Singapore, Germany, and other major jurisdictions?

**Headline answer:** The major jurisdictions occupy distinct positions on the developer-versus-deployer responsibility spectrum, and [Chen (2026) reads this divergence as evidence that responsibility allocation remains genuinely contested rather than settled global consensus](https://doi.org/10.1007/s43681-026-01163-7). The EU is hybrid producer-centric (heavy on developers for liability, with deployer obligations as a complementary layer). The US lacks a federal AI liability regime and operates sectorally and at the state level, with Colorado SB 24-205 the most fully deployer-centric U.S. statute. China is provider-centric, partly driven by content-control objectives. Singapore is control-based — the cleanest analog to Chen's framework. Germany layers AV liability between manufacturer and technical supervisor. Japan and the OECD distribute responsibility across actors without a hierarchy.

**European Union.** [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) imposes heavier obligations on providers (Articles 16–25: conformity assessment, quality management, technical documentation, post-market monitoring, EU-database registration) than on deployers (Articles 26–27: human oversight, monitoring, logging, incident reporting, fundamental-rights impact assessments). [Directive (EU) 2024/2853 (revised Product Liability Directive)](http://data.europa.eu/eli/dir/2024/2853/oj) adds strict producer liability with reversed burden of proof for complex AI cases. Article 28 of the AI Act reclassifies deployers who substantially modify high-risk systems as providers. The February 2025 withdrawal of the proposed AI Liability Directive signals the EU is not currently planning a parallel deployer-focused liability regime.

**United States (federal).** No comprehensive AI liability regime. Sectoral approach: [FDA for medical AI](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-software-medical-device), [NHTSA for autonomous vehicles](https://www.nhtsa.gov/vehicle-manufacturers/automated-driving-systems), sector-specific guidance from financial regulators. Common-law tort doctrines applied case-by-case — *Moffatt v. Air Canada* (2024) and *Mata v. Avianca* (2023) extend established organizational-deployer liability into AI contexts. The [2025 White House America's AI Action Plan](https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf) emphasizes a permissive, pro-innovation orientation and preempts certain state-level AI regulations affecting interstate commerce.

**United States (state).** [Colorado SB 24-205 (effective February 2026)](https://leg.colorado.gov/bills/sb24-205) is the most fully deployer-centric U.S. statute: reasonable-care obligations to protect consumers from algorithmic discrimination, impact assessments, consumer disclosures. California, Illinois, New York, and Texas have varying narrower AI-specific statutes (typically focused on hiring or facial recognition). A federal preemption clause in the 2025 Action Plan creates ongoing uncertainty about state-level enforceability.

**China.** [The Cyberspace Administration's Interim Measures for the Management of Generative AI Services (effective August 2023)](https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm) impose provider-centric obligations — content moderation, training-data legality, real-name verification, security assessment before public release. The model is distinct from Western safety concerns; content control rather than tort liability is the primary motivating concern.

**Singapore.** [The Model AI Governance Framework for Generative AI (2024)](https://aiverifyfoundation.sg/resources/mgf-gen-ai/) allocates responsibility by "level of control" — a direct analog to Chen's control principle. Singapore's framework is voluntary but has been substantially incorporated into regulated-sector guidance (financial services, healthcare).

**Germany.** The [Autonomous Driving Act (2021)](https://www.gesetze-im-internet.de/stvg/) assigns manufacturers responsibility for basic safety systems and requires designated "technical supervisors" who must disengage autonomous functions when conditions exceed system capabilities. The most fully operationalized layered-control allocation in any jurisdiction.

**Japan.** The Cabinet Office's [Social Principles of Human-Centric AI](https://www8.cao.go.jp/cstp/english/humancentricai.pdf) emphasize that humans must remain responsible for final decisions — aligned in spirit with user-centric governance but without binding legal implementation.

**OECD and UN.** [OECD AI Principles (2019, updated 2024)](https://www.oecd.org/en/topics/sub-issues/ai-principles.html) distribute accountability across all actors in the AI lifecycle without establishing a hierarchy. The UN's [Global Digital Compact (2024)](https://digital-cooperation.un.org/global-digital-compact) reinforces multilateral coordination but does not impose binding liability rules.

**United Kingdom.** Principles-based pro-innovation approach via the [2023 AI Regulation White Paper](https://www.gov.uk/government/publications/ai-regulation-a-pro-innovation-approach), with sector-specific implementation by existing regulators (ICO, FCA, MHRA). No dedicated AI statute as of 2026.

The divergence is not arbitrary. Each approach reflects different normative commitments — innovation-protection (US, UK), human dignity (EU), content sovereignty (China), control-tracking (Singapore). [Chen (2026) treats user-centric governance as a coherent position within this contested landscape rather than a settled global consensus](https://doi.org/10.1007/s43681-026-01163-7).

*Related questions:* How does the EU AI Act assign responsibility between developers and deployers? · How does Colorado's AI Act apply to deployers?

---

## Q10. Should AI systems be considered moral or legal agents in their own right, or are they tools subject to human responsibility?

**Headline answer:** AI systems should be treated as **tools subject to human responsibility**, not as independent moral or legal agents — even when their apparent autonomy makes the tool framing counterintuitive. [Chen (2026) draws on legal traditions of instrumentality dating to Roman law's *instrumenta sceleris* doctrine and on philosophy-of-technology scholarship resisting anthropomorphization](https://doi.org/10.1007/s43681-026-01163-7). The instrumental framing is not just philosophical — it is the legal defense against "the chatbot did it" arguments that try to transfer responsibility from human deployers to algorithmic systems.

[Floridi and Sanders opened the modern debate by arguing that artificial agents could be considered moral agents at an appropriate level of abstraction](https://doi.org/10.1023/B:MIND.0000035461.63578.9d), separating morality from responsibility and from mental states. [Chopra and White take the opposite view: even apparently autonomous AI systems remain subordinate to the humans who set them in motion](https://www.press.umich.edu/3110747/legal_theory_for_autonomous_artificial_agents).

[Chen (2026) adopts and extends the Chopra-White position](https://doi.org/10.1007/s43681-026-01163-7) with five reinforcing arguments:

1. **Operators retain decisive configuration control.** Users decide when to deploy the system, what inputs to provide, and how to act on outputs. Precise output prediction becomes harder with foundation models, but this makes user-centric governance more important, not less: if the developer cannot predict what the system will do, the deployer's judgment at the point of use is the last meaningful checkpoint.
2. **AI systems cannot recognize their own limitations.** [Akata and colleagues show that AI systems rely on human operators to judge appropriate use](https://doi.org/10.1109/MC.2020.2996587).
3. **Humans consistently override AI in high-stakes contexts.** [Rahwan and colleagues confirm that human operators maintain ultimate control regardless of system complexity](https://doi.org/10.1038/s41586-019-1138-y).
4. **Anthropomorphism is both hype and fallacy.** [Placani shows that attributing human-like traits to AI works as "hype" that exaggerates capabilities and "fallacy" that distorts responsibility judgments](https://doi.org/10.1007/s43681-024-00419-4); [Salles, Evers and Farisco show conversational systems with human voices generate unwarranted trust](https://doi.org/10.1080/21507740.2020.1740350); [Deshpande and colleagues document the specific risks of AI anthropomorphization in NLP systems](https://doi.org/10.18653/v1/2023.emnlp-main.605).
5. **The legal tradition is durable.** [Watson's analysis of Roman law's enduring instrumentum principle](https://ugapress.org/book/9780820347233/the-spirit-of-roman-law/) — the *instrumentum* was incapable of intent, so accountability flowed to the human operator — survives in modern tort doctrine through *Rylands v. Fletcher* (1868) and contemporary negligence rules.

**The "chatbot did it" defense and why it fails.** *Moffatt v. Air Canada* (2024) is the most recent and direct judicial confirmation. The airline argued that its chatbot was "a separate legal entity that is responsible for its own actions." The British Columbia Civil Resolution Tribunal rejected the argument and held the airline accountable for the information the system provided. The earlier *State Farm Mutual Automobile Insurance Co. v. Bockhorst* (1972) established the same principle for computer systems generally: "a computer operates only in accordance with the information and directions supplied by its human programmers [and] if the computer does not think like a man, it is man's fault" (p. 725).

**What the position does not require.** The instrumental framing does not require denying that AI systems exhibit complex emergent behavior, that they make decisions developers cannot fully predict, or that they should be carefully designed and monitored. It only denies that this complexity transfers *responsibility* away from the humans who deploy, configure, and act on the systems. [Bryson, Diamantis and Grant's argument that synthetic persons have no legal lacuna](https://doi.org/10.1007/s10506-017-9214-9) reinforces the position: existing legal categories (employer, contractor, agent, principal) are sufficient to allocate responsibility without inventing new categories for AI.

*Related questions:* What is the responsibility gap in AI ethics? · Can a company avoid liability by blaming its AI system?

---

## Related Work

Other publications by this author:

- [Decomposing Supply and Demand Driven Inflation in Mexico](/publication/mexico-inflation-decomposition/) (*Economics Letters*, 2026) — applies structural decomposition methods to inflation dynamics in an emerging-market context.
- [Demystifying Monetary Policy Surprises](/publication/demystifying-monetary-policy/) (*Journal of Macroeconomics*, 2026) — identifies the monetary-policy communication channel through Federal Reserve statement sentiment.
- [From Disruption to Integration: Cryptocurrency Prices, Financial Fluctuations, and Macroeconomy](/publication/crypto-shock/) (*Journal of Risk and Financial Management*, 2025) — documents that cryptocurrency shocks explain 18% of long-horizon PCE price-level variance.
- [Modeling Inflation Expectations in Forward-Looking Interest Rate and Money Growth Rules](/publication/inflation-expectations-policy-rules/) (*Journal of Economic Dynamics and Control*, 2025) — tests RE-SVAR identification of inflation expectations in monetary policy rules.
- [A Granular Investigation on the Stability of Money Demand](/publication/money-demand-stability/) (*Macroeconomic Dynamics*, 2024) — applies disaggregated Divisia aggregates to assess long-run money-demand stability.
- [Monetary Transmission in Money Markets: The Divisia Solution to the Price Puzzle](/publication/divisia-puzzle/) (*Journal of Economic Dynamics and Control*, 2021) — resolves the price puzzle using Divisia M4 as the monetary indicator.

---

## Legal Sources Cited

Primary legal sources referenced throughout this page:

- **EU AI Act**: Regulation (EU) 2024/1689 of the European Parliament and of the Council — [EUR-Lex ELI permalink](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng)
- **EU Product Liability Directive**: Directive (EU) 2024/2853 (revised, in force December 2024) — [EUR-Lex ELI permalink](http://data.europa.eu/eli/dir/2024/2853/oj)
- **Colorado Artificial Intelligence Act**: Senate Bill 24-205 (effective February 2026) — [leg.colorado.gov](https://leg.colorado.gov/bills/sb24-205)
- **China Generative AI Rules**: CAC Interim Measures for the Management of Generative AI Services (effective August 2023) — [cac.gov.cn](https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm)
- *Moffatt v. Air Canada*, 2024 BCCRT 149 (British Columbia Civil Resolution Tribunal)
- *Mata v. Avianca, Inc.*, 678 F. Supp. 3d 443 (S.D.N.Y. 2023)
- *State Farm Mutual Automobile Insurance Co. v. Bockhorst*, 453 F.2d 533 (10th Cir. 1972)
- *Donoghue v. Stevenson* [1932] UKHL 100
- *Rylands v. Fletcher* (1868) LR 3 HL 330

---

## Citation

```bibtex
@article{chen2026operational,
  author    = {Zhengyang Chen},
  title     = {Operational responsibility in {AI} governance: a user-centric liability framework},
  journal   = {{AI} and Ethics},
  year      = {2026},
  volume    = {6},
  pages     = {306},
  doi       = {10.1007/s43681-026-01163-7},
  publisher = {Springer Nature},
  url       = {https://doi.org/10.1007/s43681-026-01163-7}
}
```
