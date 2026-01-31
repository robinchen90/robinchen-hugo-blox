---
title: Research
type: widget_page

# Optional banner image (relative to `assets/media/` folder).
banner:
  caption: ''
  image: ''

sections:
  # Published Articles
  - block: collection
    id: publications
    content:
      title: Publications
      text: ""
      filters:
        folders:
          - publication
        publication_type: 'article-journal'
    design:
      view: citation
      columns: '1'

  # Working Papers
  - block: collection
    id: working-papers
    content:
      title: Working Papers
      text: ""
      filters:
        folders:
          - publication
        publication_type: 'manuscript'
    design:
      view: citation
      columns: '1'
---
