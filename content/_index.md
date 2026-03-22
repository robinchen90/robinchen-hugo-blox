---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
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
          description: Developing and applying advanced econometric techniques for causal identification in structural VAR.
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

  # Recent Publications
  - block: collection
    content:
      title: Recent Publications
      text: |-
        {{% callout note %}}
        Quickly discover relevant content by [filtering publications](./publication/).
        {{% /callout %}}
      count: 5
      filters:
        folders:
          - publication
        exclude_featured: false
      sort_by: 'Date'
      sort_ascending: false
    design:
      columns: '2'
      view: citation

  # Teaching Timeline
  - block: experience
    id: teaching
    content:
      title: Teaching Experience
      items:
        - title: Assistant Professor of Economics
          company: University of Northern Iowa
          company_url: 'https://business.uni.edu/economics/directory/zhengyang-robin-chen'
          location: Cedar Falls, Iowa
          date_start: '2023-08-20'
          date_end: ''
          description: |
            Undergraduate:

            * ECON1041 Principles of Macroeconomics
            * ECON2132 Money and Banking
            * ECON3371 Economic and Business Forecasting

            Developed interactive educational tools including Bond Price Calculator and ClassHub platform.

        - title: Assistant Professor in Economics
          company: St. Cloud State University
          company_url: 'https://www.stcloudstate.edu/'
          location: St. Cloud, Minnesota
          date_start: '2021-08-20'
          date_end: '2023-05-30'
          description: |
            Undergraduate:

            * ECON205 Principles of Macroeconomics
            * ECON470 Intermediate Economic and Business Forecasting
            * ECON471 Money and Banking

            Graduate:

            * ECON570 Intermediate Economic and Business Forecasting
            * ECON571 Money and Banking
            * ECON605 Macroeconomic Theory
            * ECON670 Advanced Economic and Business Forecasting

        - title: Visiting Assistant Professor in Economics
          company: Birmingham-Southern College
          company_url: ''
          location: Birmingham, Alabama
          date_start: '2020-09-01'
          date_end: '2021-08-01'
          description: |
            With full curricular and evaluation responsibilities:

            * EC360 Time Series Visualization and Forecasting (Approved)
            * EC201 Principles of Macroeconomics
            * EC308 Macroeconomics
            * EC303 Money and Banking

        - title: Instructor
          company: UT Dallas
          company_url: 'https://www.utdallas.edu'
          location: Richardson, Texas
          date_start: '2018-05-15'
          date_end: '2019-05-30'
          description: |
            With full curricular and evaluation responsibilities:

            * ECON2301 Principles of Macroeconomics (5 semesters, Summer 2018 to Fall 2019)

        - title: Teaching Assistant
          company: UT Dallas
          company_url: 'https://www.utdallas.edu'
          location: Richardson, Texas
          date_start: '2015-09-01'
          date_end: '2020-05-31'
          description: |
            Teaching assistant for Dr. Victor Valcarcel:

            * ECON2301 Principles of Macroeconomics (2 terms)
            * ECON3312 Money and Banking (3 terms)
            * ECON7302 Macroeconomics Theory II (2 terms)
    design:
      columns: '2'

  # Grants & Fellowships
  - block: accomplishments
    id: funding
    content:
      title: 'Grants & Fellowships'
      subtitle: ''
      text: ''
      date_format: Jan 2006
      items:
        - title: 'Summer Research Award'
          certificate_url: ''
          date_start: '2026-05-01'
          date_end: '2026-08-31'
          description: '$10,000'
          organization: 'Wilson College of Business, UNI'
          organization_url: ''
          url: ''
          icon: ''

        - title: 'RSP Capacity Building Grant | Principal Investigator'
          certificate_url: ''
          date_start: '2026-02-01'
          date_end: '2027-10-31'
          description: '$15,000'
          organization: 'Office of Research & Sponsored Programs, UNI'
          organization_url: 'https://rsp.uni.edu'
          url: 'https://rsp.uni.edu/internal-funding'
          icon: ''

        - title: 'RSP Capacity Building Grant | Co-Principal Investigator'
          certificate_url: ''
          date_start: '2026-02-01'
          date_end: '2027-10-31'
          description: '$7,425'
          organization: 'Office of Research & Sponsored Programs, UNI'
          organization_url: 'https://rsp.uni.edu'
          url: 'https://rsp.uni.edu/internal-funding'
          icon: ''

        - title: 'Tim Williams Junior Faculty Fellowship'
          certificate_url: ''
          date_start: '2025-06-01'
          date_end: '2026-06-30'
          description: "→ [Demystifying Monetary Policy Surprises: Fed Response to Financial Conditions and Wait-and-See for New Economic Data](/publication/demystifying-monetary-policy/)"
          organization: 'Wilson College of Business, UNI'
          organization_url: ''
          url: 'https://business.uni.edu/faculty-staff/named-professorships'
          icon: ''

        - title: 'Summer Research Fellowship'
          certificate_url: ''
          date_start: '2025-05-01'
          date_end: '2025-08-31'
          description: "$3,800 + match to 1/9 salary\n\n→ [Modeling Inflation Expectations in Forward-Looking Interest Rate and Money Growth Rules](/publication/inflation-expectations-policy-rules/)"
          organization: 'Division of Graduate Studies + Wilson College of Business, UNI'
          organization_url: ''
          url: 'https://grad.uni.edu/info-faculty-staff/summer-fellowship'
          icon: ''

        - title: 'Pre-Tenure Faculty Grant'
          certificate_url: ''
          date_start: '2025-01-01'
          date_end: '2026-05-31'
          description: '$1,500'
          organization: "Provost's Office, UNI"
          organization_url: ''
          url: 'https://provost.uni.edu/pre-tenure-faculty-grant'
          icon: ''

        - title: 'Wilson College of Business Faculty Research Stipend'
          certificate_url: ''
          date_start: '2024-05-01'
          date_end: '2024-08-31'
          description: "→ [A Granular Investigation on the Stability of Money Demand](/publication/money-demand-stability/)"
          organization: 'Wilson College of Business, UNI'
          organization_url: ''
          url: ''
          icon: ''
    design:
      columns: '2'

  # Innovations
  - block: collection
    id: projects
    content:
      title: Teaching Innovations
      subtitle: Interactive Educational Tools
      text: ''
      filters:
        folders:
          - project
      count: 0
    design:
      columns: '2'
      view: showcase

  # Recent Posts - Hidden
  # - block: collection
  #   id: posts
  #   content:
  #     title: Recent Posts
  #     subtitle: ''
  #     text: ''
  #     count: 5
  #     filters:
  #       folders:
  #         - post
  #       author: ""
  #       category: ""
  #       tag: ""
  #       exclude_featured: false
  #       exclude_future: false
  #       exclude_past: false
  #       publication_type: ""
  #     offset: 0
  #     order: desc
  #   design:
  #     columns: '2'
  #     view: compact

  # Contact
  - block: contact
    id: contact
    content:
      title: Contact
      subtitle:
      text:
      email: zhengyang.chen at uni.edu
      phone:
      address:
        street: 2382 Minnesota St, CBB 202
        city: Cedar Falls
        region: IA
        postcode: '50614'
        country: United States
        country_code: US
      contact_links:
      autolink: true
    design:
      columns: '2'
---
