# Q&A Expansion — AI Governance Super Page (Q7–Q10)

**Companion to:** `ai_governance_superpage_spec.md`

**Purpose:** Add four Q&A blocks (Q7–Q10) targeting citation scenarios that the original six do not reach. Each new Q is mapped to a distinct researcher/practitioner archetype who would cite this paper during a literature review.

**Citation-scenario mapping:**

| Q | Citation scenario | Primary cited-by population |
|---|---|---|
| Q7 | Building an internal AI governance program | Corporate counsel, compliance officers, CISO/CDO offices, organizational governance scholars |
| Q8 | Drafting AI liability reform recommendations | Policy analysts (Brookings, CSET, Brennan Center, AI Now Institute), regulatory affairs offices |
| Q9 | Writing a comparative AI regulation paper | International law scholars, policy researchers at multilateral organizations (OECD, UN, ITU), regulatory affairs in MNCs |
| Q10 | Engaging the AI moral-agency or legal-personhood debate | Philosophy of technology scholars, tort law scholars, AI ethics researchers, lawyers writing on "the chatbot did it" defenses |

---

## Q7. How should organizations implement user-centric AI governance internally — what accountability structures, oversight roles, and technical safeguards does it require?

**Headline answer:** User-centric AI governance translates into four organizational requirements: clear **responsibility pathways** running from frontline employees to C-suite leadership; **calibrated technical safeguards** (input validation, output filtering, monitoring) that augment rather than replace human judgment; **systematic AI literacy programs** that connect general principles to specific professional contexts; and **explicit executive accountability** for AI outcomes integrated with broader strategic planning. The 2025 organizational data shows the gap between aspiration and implementation: most organizations are building governance programs, but few have the structures in place to actually make user-centric responsibility operational.

The foundational structural requirement is what <a href="https://www.colotechlj.org/wp-content/uploads/2019/05/13-1_5-Polonetsky.pdf">Polonetsky, Tene and Jerome term "responsibility pathways"</a> — clear chains of decision-making authority from frontline employees to executive leadership. Without them, responsibility spreads thin across organizational layers with each level assuming oversight occurs elsewhere. Recent industry data confirms the gap: <a href="https://iapp.org/resources/article/ai-governance-profession-report/">the IAPP AI Governance Profession Report (2025) finds that while 77% of organizations are actively building AI governance programs, the average governance team comprises only nine people and 17% of organizations assign AI governance to a single individual</a>. Meanwhile, <a href="https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai">McKinsey's State of AI survey finds that only 28% of CEOs take direct responsibility for AI governance</a> — a structural disconnect with the formal accountability the framework requires.

<a href="https://doi.org/10.1007/s43681-026-01163-7">Chen (2026) builds the implementation around four operational layers</a>:

1. **Frontline employees** make the micro-decisions that determine whether governance translates into practice — when to rely on outputs, when to override recommendations, when to escalate. <a href="https://doi.org/10.1145/3287560.3287596">Passi and Barocas show through ethnographic fieldwork that discretionary choices in problem formulation carry normative consequences formal policies rarely anticipate</a>.

2. **Mid-level managers** occupy what <a href="https://doi.org/10.1145/3442188.3445935">Metcalf, Moss and Watkins term "translation points"</a> between technical capabilities and operational realities — identifying emerging problems before they escalate, adjusting deployment parameters, communicating insights back to technical teams.

3. **Technical safeguards** are "compliance by design" in <a href="https://doi.org/10.1111/rego.12158">Yeung's sense</a> — input validation that flags out-of-distribution cases for human review, output filtering that surfaces low-confidence predictions, monitoring that tracks performance degradation. <a href="https://doi.org/10.1038/538311a">Crawford and Calo's warning is critical here: technical guardrails that remove human discretion undermine the very responsibility they are meant to support</a>.

4. **Executive accountability.** <a href="https://doi.org/10.1145/3479582">Kroll shows explicit leadership accountability for AI outcomes correlates strongly with improved governance practices throughout organizations</a>. Industry data supports the connection — <a href="https://www.pwc.com/us/en/tech-effect/ai-analytics/responsible-ai-survey.html">PwC's 2025 Responsible AI Survey finds nearly 60% of executives report responsible AI governance — including clear accountability — boosts ROI and efficiency</a>, and organizations at the strategic governance maturity stage are 1.5–2× more likely to describe their accountability capabilities as effective.

**Reference frameworks for implementation.** <a href="https://doi.org/10.6028/NIST.AI.100-1">NIST AI Risk Management Framework 1.0</a> and its <a href="https://doi.org/10.6028/NIST.AI.600-1">Generative AI Profile</a> structure governance around four functions (govern, map, measure, manage) most naturally performed at the deployment level. <a href="https://www.iso.org/standard/81230.html">ISO/IEC 42001:2023</a> requires organizational leadership commitment (Clause 5) and operational controls (Clause 8) that presuppose deployer-level implementation. The <a href="https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592">Canadian Directive on Automated Decision-Making</a> scales documentation obligations to system impact levels and is the most operationally specific public-sector model currently available.

Six concrete starting actions for a Fortune 500 implementation:

1. Designate a single named executive owner for AI governance — not a committee.
2. Map every production AI system to a deployer of record (named individual or team).
3. Adopt <a href="https://doi.org/10.1145/3287560.3287596">Mitchell et al.'s model card standard</a> for vendor procurement — no AI procurement without a model card.
4. Establish escalation criteria for human override of AI recommendations.
5. Mandate AI competence training proportionate to role — building on the <a href="https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_1_1_competence/comment_on_rule_1_1/">ABA's Rule 1.1 Comment 8</a> model and <a href="https://www.americanbar.org/groups/professional_responsibility/publications/aba_formal_opinions/">ABA Formal Opinion 512 on generative AI</a>.
6. Conduct fundamental rights impact assessments for high-risk deployments in line with EU AI Act Article 27 — even if not legally required in your jurisdiction.

*Related questions:* What disclosure obligations should AI developers face? · How do reasonable-care standards adapt for AI deployment decisions?

---

## Q8. Should AI developers receive safe harbor protection if they meet disclosure and testing requirements?

**Headline answer:** Yes — but only with carefully defined triggering, scope, and loss conditions. <a href="https://doi.org/10.1007/s43681-026-01163-7">Chen (2026) proposes a three-part safe harbor structure</a> that gives qualifying developers a rebuttable presumption against design-defect liability when harm results from deployment in contexts the developer documented as outside validated use, provided the developer made the limitation reasonably accessible to the deployer. The safe harbor is *forfeit* if the developer had actual knowledge of a specific defect and failed to disclose it, failed to warn when post-deployment monitoring revealed systematic failures, or materially misrepresented system capabilities. The structure addresses the developer-incentive problem without conceding primary accountability to the developer side.

The design problem is well-known. <a href="https://doi.org/10.1086/261869">Viscusi and Moore find that the relationship between liability and innovation is non-linear: at high liability levels the effect on R&D turns negative</a>. <a href="https://press.princeton.edu/books/hardcover/9780674007222/fairness-versus-welfare">Kaplow and Shavell argue optimal liability rules balance innovation incentives against harm prevention</a>, and <a href="https://scholarship.law.ufl.edu/flr/vol66/iss5/1/">Hubbard applies this directly to AI: concentrating liability on original developers discourages creation of general-purpose tools whose applications cannot be anticipated</a>.

<a href="https://doi.org/10.1007/s43681-026-01163-7">Chen (2026) draws the safe harbor from established conformity-assessment models</a>. The three elements:

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

The operational infrastructure already exists. <a href="https://doi.org/10.1145/3287560.3287596">Mitchell and colleagues' model cards</a> furnish the documentation format for capabilities and known limitations across population groups. <a href="https://doi.org/10.1145/3351095.3372873">Raji and colleagues' SMACTR (Scoping, Mapping, Artifact Collection, Testing, Reflection) framework</a> furnishes the end-to-end internal algorithmic auditing process that produces the qualifying documentation. <a href="https://doi.org/10.6028/NIST.AI.100-1">NIST AI RMF</a> and <a href="https://www.iso.org/standard/81230.html">ISO/IEC 42001</a> provide compatible governance scaffolding.

<a href="https://heinonline.org/HOL/LandingPage?handle=hein.journals/vanep19&div=6">Stemler's analysis of "Regulation 2.0"</a> supports the design choice: well-designed regulatory frameworks combining collaborative standard-setting with technology-mediated enforcement encourage safety-enhancing disclosures more effectively than strict liability regimes alone. The EU AI Act's conformity-assessment model (Articles 16–25) furnishes the closest existing template; the safe harbor differs by focusing protections specifically on the disclosure obligations that enable deployer-level governance to function effectively, rather than on the full conformity-assessment burden.

What the safe harbor does *not* do: it does not displace producer-side strict liability under the <a href="http://data.europa.eu/eli/dir/2024/2853/oj">revised Product Liability Directive (EU) 2024/2853</a>. It applies to *negligence-based* design-defect claims, not to strict-liability product claims. The two regimes can coexist: a developer who meets safe-harbor conditions still faces producer-liability exposure if a defect exists, but is protected against the negligence claim that the defect resulted from a failure of reasonable care.

*Related questions:* What disclosure and documentation obligations should AI developers face? · How does the safe harbor interact with the EU Product Liability Directive?

---

## Q9. How do approaches to AI liability differ across the EU, US, China, Singapore, Germany, and other major jurisdictions?

**Headline answer:** The major jurisdictions occupy distinct positions on the developer-versus-deployer responsibility spectrum, and <a href="https://doi.org/10.1007/s43681-026-01163-7">Chen (2026) reads this divergence as evidence that responsibility allocation remains genuinely contested rather than settled global consensus</a>. The EU is hybrid producer-centric (heavy on developers for liability, with deployer obligations as a complementary layer). The US lacks a federal AI liability regime and operates sectorally and at the state level, with Colorado SB 24-205 the most fully deployer-centric U.S. statute. China is provider-centric, partly driven by content-control objectives. Singapore is control-based — the cleanest analog to Chen's framework. Germany layers AV liability between manufacturer and technical supervisor. Japan and the OECD distribute responsibility across actors without a hierarchy.

**European Union.** <a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng">Regulation (EU) 2024/1689</a> imposes heavier obligations on providers (Articles 16–25: conformity assessment, quality management, technical documentation, post-market monitoring, EU-database registration) than on deployers (Articles 26–27: human oversight, monitoring, logging, incident reporting, fundamental-rights impact assessments). <a href="http://data.europa.eu/eli/dir/2024/2853/oj">Directive (EU) 2024/2853 (revised Product Liability Directive)</a> adds strict producer liability with reversed burden of proof for complex AI cases. Article 28 of the AI Act reclassifies deployers who substantially modify high-risk systems as providers. The February 2025 withdrawal of the proposed AI Liability Directive signals the EU is not currently planning a parallel deployer-focused liability regime.

**United States (federal).** No comprehensive AI liability regime. Sectoral approach: <a href="https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-software-medical-device">FDA for medical AI</a>, <a href="https://www.nhtsa.gov/vehicle-manufacturers/automated-driving-systems">NHTSA for autonomous vehicles</a>, sector-specific guidance from financial regulators. Common-law tort doctrines applied case-by-case — *Moffatt v. Air Canada* (2024) and *Mata v. Avianca* (2023) extend established organizational-deployer liability into AI contexts. The <a href="https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf">2025 White House America's AI Action Plan</a> emphasizes a permissive, pro-innovation orientation and preempts certain state-level AI regulations affecting interstate commerce.

**United States (state).** <a href="https://leg.colorado.gov/bills/sb24-205">Colorado SB 24-205 (effective February 2026)</a> is the most fully deployer-centric U.S. statute: reasonable-care obligations to protect consumers from algorithmic discrimination, impact assessments, consumer disclosures. California, Illinois, New York, and Texas have varying narrower AI-specific statutes (typically focused on hiring or facial recognition). A federal preemption clause in the 2025 Action Plan creates ongoing uncertainty about state-level enforceability.

**China.** <a href="https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm">The Cyberspace Administration's Interim Measures for the Management of Generative AI Services (effective August 2023)</a> impose provider-centric obligations — content moderation, training-data legality, real-name verification, security assessment before public release. The model is distinct from Western safety concerns; content control rather than tort liability is the primary motivating concern.

**Singapore.** <a href="https://aiverifyfoundation.sg/resources/mgf-gen-ai/">The Model AI Governance Framework for Generative AI (2024)</a> allocates responsibility by "level of control" — a direct analog to Chen's control principle. Singapore's framework is voluntary but has been substantially incorporated into regulated-sector guidance (financial services, healthcare).

**Germany.** The <a href="https://www.gesetze-im-internet.de/stvg/">Autonomous Driving Act (2021)</a> assigns manufacturers responsibility for basic safety systems and requires designated "technical supervisors" who must disengage autonomous functions when conditions exceed system capabilities. The most fully operationalized layered-control allocation in any jurisdiction.

**Japan.** The Cabinet Office's <a href="https://www8.cao.go.jp/cstp/english/humancentricai.pdf">Social Principles of Human-Centric AI</a> emphasize that humans must remain responsible for final decisions — aligned in spirit with user-centric governance but without binding legal implementation.

**OECD and UN.** <a href="https://www.oecd.org/en/topics/sub-issues/ai-principles.html">OECD AI Principles (2019, updated 2024)</a> distribute accountability across all actors in the AI lifecycle without establishing a hierarchy. The UN's <a href="https://digital-cooperation.un.org/global-digital-compact">Global Digital Compact (2024)</a> reinforces multilateral coordination but does not impose binding liability rules.

**United Kingdom.** Principles-based pro-innovation approach via the <a href="https://www.gov.uk/government/publications/ai-regulation-a-pro-innovation-approach">2023 AI Regulation White Paper</a>, with sector-specific implementation by existing regulators (ICO, FCA, MHRA). No dedicated AI statute as of 2026.

The divergence is not arbitrary. Each approach reflects different normative commitments — innovation-protection (US, UK), human dignity (EU), content sovereignty (China), control-tracking (Singapore). <a href="https://doi.org/10.1007/s43681-026-01163-7">Chen (2026) treats user-centric governance as a coherent position within this contested landscape rather than a settled global consensus</a>.

*Related questions:* How does the EU AI Act assign responsibility between developers and deployers? · How does Colorado's AI Act apply to deployers?

---

## Q10. Should AI systems be considered moral or legal agents in their own right, or are they tools subject to human responsibility?

**Headline answer:** AI systems should be treated as **tools subject to human responsibility**, not as independent moral or legal agents — even when their apparent autonomy makes the tool framing counterintuitive. <a href="https://doi.org/10.1007/s43681-026-01163-7">Chen (2026) draws on legal traditions of instrumentality dating to Roman law's *instrumenta sceleris* doctrine and on philosophy-of-technology scholarship resisting anthropomorphization</a>. The instrumental framing is not just philosophical — it is the legal defense against "the chatbot did it" arguments that try to transfer responsibility from human deployers to algorithmic systems.

<a href="https://doi.org/10.1023/B:MIND.0000035461.63578.9d">Floridi and Sanders opened the modern debate by arguing that artificial agents could be considered moral agents at an appropriate level of abstraction</a>, separating morality from responsibility and from mental states. <a href="https://www.press.umich.edu/3110747/legal_theory_for_autonomous_artificial_agents">Chopra and White take the opposite view: even apparently autonomous AI systems remain subordinate to the humans who set them in motion</a>.

<a href="https://doi.org/10.1007/s43681-026-01163-7">Chen (2026) adopts and extends the Chopra-White position</a> with five reinforcing arguments:

1. **Operators retain decisive configuration control.** Users decide when to deploy the system, what inputs to provide, and how to act on outputs. Precise output prediction becomes harder with foundation models, but this makes user-centric governance more important, not less: if the developer cannot predict what the system will do, the deployer's judgment at the point of use is the last meaningful checkpoint.
2. **AI systems cannot recognize their own limitations.** <a href="https://doi.org/10.1109/MC.2020.2996587">Akata and colleagues show that AI systems rely on human operators to judge appropriate use</a>.
3. **Humans consistently override AI in high-stakes contexts.** <a href="https://doi.org/10.1038/s41586-019-1138-y">Rahwan and colleagues confirm that human operators maintain ultimate control regardless of system complexity</a>.
4. **Anthropomorphism is both hype and fallacy.** <a href="https://doi.org/10.1007/s43681-024-00419-4">Placani shows that attributing human-like traits to AI works as "hype" that exaggerates capabilities and "fallacy" that distorts responsibility judgments</a>; <a href="https://doi.org/10.1080/21507740.2020.1740350">Salles, Evers and Farisco show conversational systems with human voices generate unwarranted trust</a>; <a href="https://doi.org/10.18653/v1/2023.emnlp-main.605">Deshpande and colleagues document the specific risks of AI anthropomorphization in NLP systems</a>.
5. **The legal tradition is durable.** <a href="https://ugapress.org/book/9780820347233/the-spirit-of-roman-law/">Watson's analysis of Roman law's enduring instrumentum principle</a> — the *instrumentum* was incapable of intent, so accountability flowed to the human operator — survives in modern tort doctrine through *Rylands v. Fletcher* (1868) and contemporary negligence rules.

**The "chatbot did it" defense and why it fails.** *Moffatt v. Air Canada* (2024) is the most recent and direct judicial confirmation. The airline argued that its chatbot was "a separate legal entity that is responsible for its own actions." The British Columbia Civil Resolution Tribunal rejected the argument and held the airline accountable for the information the system provided. The earlier *State Farm Mutual Automobile Insurance Co. v. Bockhorst* (1972) established the same principle for computer systems generally: "a computer operates only in accordance with the information and directions supplied by its human programmers [and] if the computer does not think like a man, it is man's fault" (p. 725).

**What the position does not require.** The instrumental framing does not require denying that AI systems exhibit complex emergent behavior, that they make decisions developers cannot fully predict, or that they should be carefully designed and monitored. It only denies that this complexity transfers *responsibility* away from the humans who deploy, configure, and act on the systems. <a href="https://doi.org/10.1007/s10506-017-9214-9">Bryson, Diamantis and Grant's argument that synthetic persons have no legal lacuna</a> reinforces the position: existing legal categories (employer, contractor, agent, principal) are sufficient to allocate responsibility without inventing new categories for AI.

*Related questions:* What is the responsibility gap in AI ethics? · Can a company avoid liability by blaming its AI system?

---

## JSON-LD additions (splice into existing FAQPage schema)

Add the following four `Question` objects to the `mainEntity` array in the existing FAQPage JSON-LD (Section 3 of the original spec). The full updated array will have 10 entries.

```json
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
```

---

## DOI / URL Reference Ledger — additions for Q7–Q10

Add these to the existing Section 7 ledger. Reference URLs are publisher- or institution-hosted where available; SSRN substitutes only where no journal-hosted version exists.

| Reference | DOI / URL |
|---|---|
| 2025 White House America's AI Action Plan | https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf |
| ABA Formal Opinion 512 (Generative AI Tools) | https://www.americanbar.org/groups/professional_responsibility/publications/aba_formal_opinions/ |
| ABA Model Rule 1.1 Comment 8 | https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_1_1_competence/comment_on_rule_1_1/ |
| Canadian Directive on Automated Decision-Making | https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592 |
| Chopra & White (2011) book | https://www.press.umich.edu/3110747/legal_theory_for_autonomous_artificial_agents |
| Deshpande et al. (2023) EMNLP | https://doi.org/10.18653/v1/2023.emnlp-main.605 |
| FDA AI/ML SaMD page | https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-software-medical-device |
| Germany Autonomous Driving Act (StVG) | https://www.gesetze-im-internet.de/stvg/ |
| IAPP AI Governance Profession Report 2025 | https://iapp.org/resources/article/ai-governance-profession-report/ |
| Japan Social Principles of Human-Centric AI | https://www8.cao.go.jp/cstp/english/humancentricai.pdf |
| Kaplow & Shavell (2002) Fairness vs. Welfare | https://press.princeton.edu/books/hardcover/9780674007222/fairness-versus-welfare |
| Kroll (2021) ACM Hum.-Comput. Interact. | https://doi.org/10.1145/3479582 |
| McKinsey State of AI (2025) | https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai |
| Metcalf, Moss & Watkins (2021) FAccT | https://doi.org/10.1145/3442188.3445935 |
| NHTSA Automated Driving Systems | https://www.nhtsa.gov/vehicle-manufacturers/automated-driving-systems |
| NIST AI Generative AI Profile (NIST AI 600-1) | https://doi.org/10.6028/NIST.AI.600-1 |
| PwC 2025 Responsible AI Survey | https://www.pwc.com/us/en/tech-effect/ai-analytics/responsible-ai-survey.html |
| Stemler (2016) Vand. J. Ent. & Tech. L. | https://heinonline.org/HOL/LandingPage?handle=hein.journals/vanep19&div=6 |
| UK AI Regulation White Paper (2023) | https://www.gov.uk/government/publications/ai-regulation-a-pro-innovation-approach |
| UN Global Digital Compact (2024) | https://digital-cooperation.un.org/global-digital-compact |
| Watson (1998) Spirit of Roman Law | https://ugapress.org/book/9780820347233/the-spirit-of-roman-law/ |

---

## Updated Implementation Checklist (additions to Section 6 of the original spec)

- [ ] Add Q7–Q10 prose to the page body after Q6, each with proper `<h2>` headings and anchor IDs (`#q7`, `#q8`, `#q9`, `#q10`) so the glossary and table of contents can link to them.
- [ ] Splice the four new `Question` entries into the FAQPage JSON-LD `mainEntity` array. The full array now has 10 entries.
- [ ] Add the new DOI / URL entries to the reference ledger.
- [ ] Update the meta description and OG description to reflect the broader scope: replace "Six Q&A blocks" with "Ten Q&A blocks" and add "organizational implementation, safe harbor design, comparative jurisdictions, AI agency debate" to the description.
- [ ] If the page has a table of contents (recommended for 10 Qs), add anchor links for Q7–Q10.
- [ ] Re-validate FAQPage JSON-LD at https://search.google.com/test/rich-results and https://validator.schema.org after the splice.
- [ ] Update `llms.txt` to mention the four new question topics if you list specific topics there.
- [ ] Test retrieval 2–4 weeks after publishing with the new question types verbatim: "how should my company implement AI governance," "AI developer safe harbor," "compare EU US China AI regulation," "are AI systems moral agents."

---

## Design Rationale — additions to Section 8 of the original spec

**Why these specific four additions?**

The original six Q&As cover the *intellectual* terrain of the paper — the thesis, the philosophical concept, the regulatory backdrop, the technical objection, the defensive corollary, and the domain coverage. They are addressed primarily to academic readers doing literature reviews.

The four additions target *applied* and *adjacent-discipline* citation scenarios that the six did not reach:

- **Q7 (organizational implementation)** captures the corporate-counsel / compliance-officer query population. This is a high-citation-density group because Fortune 500 governance teams produce internal reports, whitepapers, and conference presentations that cite academic frameworks. The Q is procedural — the "five things to do" framing maps directly to slide-deck and policy-document use.
- **Q8 (safe harbor design)** surfaces one of the paper's most concrete *original policy proposals* (Section 5.1.2 of the paper), which is otherwise buried beneath the conceptual framework. Policy analysts and regulatory-affairs scholars cite original policy proposals at much higher rates than they cite theoretical frameworks. Making the three-part structure (triggering / scope / loss) extractable is high-leverage.
- **Q9 (comparative jurisdictions)** is the highest-traffic *international* query type in the AI governance literature. By covering EU, US, China, Singapore, Germany, Japan, OECD, and UK in one extractable block with hyperlinks to primary sources, the page becomes the canonical comparative reference. This also picks up traffic originating from research communities outside the Anglo-American tradition.
- **Q10 (AI agency / personhood)** captures the philosophy-of-technology and AI-personhood debate, which is intellectually adjacent but not identical to the responsibility-gap discussion in Q2. The "chatbot did it" framing makes the answer memorable and directly actionable for lawyers writing motions. It also positions the paper to be retrieved when someone asks about Floridi-Sanders on AI agency or about *Moffatt v. Air Canada*.

**Why not add more?**

Diminishing returns. Beyond ten Qs, the page risks becoming a treatise rather than a retrievable reference. The selection above gives one Q per distinct citation scenario — adding more would either duplicate scenarios (e.g., a second healthcare-specific Q overlapping Q6) or stretch into territory the paper does not strongly support (e.g., AI safety research, alignment, existential risk — adjacent but not central to your framework).

**Cross-paper consistency.**

This ten-Q structure matches the expansion pattern previously applied to the JEDC 2021, JMacro 2026, and Mexico Inflation super pages — preserving the format consistency that LLM crawlers index as a signal of a coherent research domain. The four added Qs follow the same anchor-citation, named-concept, and inline-hyperlink conventions as Q1–Q6.

---

**End of expansion spec.** This document is a *delta* on the original `ai_governance_superpage_spec.md`. Apply it by: (1) inserting Q7–Q10 prose after Q6 in Section 1; (2) splicing the four new `Question` objects into the FAQPage JSON-LD `mainEntity` array; (3) appending the new ledger entries to Section 7; (4) updating the checklist and rationale. The original Q1–Q6 do not need any changes.
