---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  # Hero Section
  - block: hero
    content:
      title: Zhengyang (Robin) Chen
      text: |
        **Assistant Professor | Researcher | Educator**

        Advancing our understanding of monetary policy transmission, Fed policy rules, and structural identification in macroeconomic models.
      cta:
        label: View Research
        url: '#featured'
      cta_alt:
        label: Teaching Resources
        url: '/teaching/'
      cta_note:
        label: ''
    design:
      background:
        gradient_start: '#500778'
        gradient_end: '#2E1A47'
        text_color_light: true
      spacing:
        padding: ['100px', '0', '100px', '0']

  # Stats Block
  - block: markdown
    content:
      title: ''
      text: |
        <div class="stats-block">
          <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 2rem;">
            <div class="stat-box" style="text-align: center; padding: 2rem 2.5rem; min-width: 180px; border-radius: 16px;">
              <div class="stat-number">9+</div>
              <div class="stat-label">Publications</div>
            </div>
            <div class="stat-box" style="text-align: center; padding: 2rem 2.5rem; min-width: 180px; border-radius: 16px;">
              <div class="stat-number">20+</div>
              <div class="stat-label">Presentations</div>
            </div>
            <div class="stat-box" style="text-align: center; padding: 2rem 2.5rem; min-width: 180px; border-radius: 16px;">
              <div class="stat-number">6+</div>
              <div class="stat-label">Years Teaching</div>
            </div>
            <div class="stat-box" style="text-align: center; padding: 2rem 2.5rem; min-width: 180px; border-radius: 16px;">
              <div class="stat-number">500+</div>
              <div class="stat-label">Students Taught</div>
            </div>
          </div>
        </div>
    design:
      columns: '1'

  # About/Biography
  - block: about.biography
    id: about
    content:
      title: Biography
      username: admin

  # Research Areas Features
  - block: features
    content:
      title: Research Areas
      items:
        - name: Monetary Policy Transmission
          description: Investigating how monetary policy decisions affect the economy through various transmission channels, including money markets and financial stress.
          icon: chart-line
          icon_pack: fas
        - name: Fed Policy Rules
          description: Analyzing Federal Reserve policy frameworks, inflation expectations, and the effectiveness of different monetary policy rules.
          icon: university
          icon_pack: fas
        - name: Structural VAR Identification
          description: Developing and applying advanced econometric techniques for causal identification in macroeconomic models, including SVAR and narrative approaches.
          icon: project-diagram
          icon_pack: fas
        - name: Money Demand & Aggregation
          description: Examining the stability of money demand, safe asset aggregation, and the role of monetary aggregates in economic analysis.
          icon: coins
          icon_pack: fas
        - name: Cryptocurrency & Macro
          description: Studying the integration of cryptocurrency markets with traditional financial systems and their macroeconomic transmission effects.
          icon: bitcoin
          icon_pack: fab
        - name: Economic Education
          description: Creating innovative teaching tools and interactive platforms to enhance student understanding of complex economic concepts.
          icon: graduation-cap
          icon_pack: fas
    design:
      columns: '2'

  # Featured Publications
  - block: collection
    id: featured
    content:
      title: Featured Publications
      filters:
        folders:
          - publication
        featured_only: true
    design:
      columns: '2'
      view: card

  # Recent Publications
  - block: collection
    content:
      title: Recent Publications
      text: |-
        {{% callout note %}}
        Quickly discover relevant content by [filtering publications](./publication/).
        {{% /callout %}}
      filters:
        folders:
          - publication
        exclude_featured: true
    design:
      columns: '2'
      view: citation

  # Teaching Timeline
  - block: experience
    id: teaching
    content:
      title: Teaching Experience
      items:
        - title: Instructor
          company: University of Northern Iowa
          company_url: 'https://www.uni.edu'
          location: Cedar Falls, Iowa
          date_start: '2018-05-15'
          date_end: ''
          description: |
            Teaching courses in Money & Banking, Macroeconomics, and developing interactive educational tools.

            **Key Achievements:**
            * Developed Bond Price Calculator used by 500+ students
            * Created ClassHub attendance and peer evaluation platform
            * Recipient of teaching excellence recognition
        - title: Graduate Teaching Assistant
          company: University of Texas at Dallas
          company_url: 'https://www.utdallas.edu'
          location: Richardson, Texas
          date_start: '2015-08-01'
          date_end: '2018-05-01'
          description: |
            Supported undergraduate economics courses and conducted recitation sessions.
    design:
      columns: '2'

  # Projects
  - block: collection
    id: projects
    content:
      title: Teaching Projects
      subtitle: Interactive Educational Tools
      text: ''
      filters:
        folders:
          - project
      count: 0
    design:
      columns: '2'
      view: showcase

  # Recent Posts
  - block: collection
    id: posts
    content:
      title: Recent Posts
      subtitle: ''
      text: ''
      count: 5
      filters:
        folders:
          - post
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      offset: 0
      order: desc
    design:
      columns: '2'
      view: compact

  # Contact
  - block: contact
    id: contact
    content:
      title: Contact
      subtitle:
      text:
      email: zhengyang.chen@uni.edu
      phone:
      address:
        street: 2382 Minnesota St, CBB 202
        city: Cedar Falls
        region: IA
        postcode: '50614'
        country: United States
        country_code: US
      coordinates:
        latitude: '42.5186'
        longitude: '-92.4549'
      contact_links:
      autolink: true
    design:
      columns: '2'
---
