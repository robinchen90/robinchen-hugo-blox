---
title: "ClassHub - Attendance & Peer Evaluation Platform"
date: 2024-02-01T00:00:00

# Project summary to display on homepage
summary: "A web app that helps instructors manage attendance and peer evaluations in team-based courses with presentations and group projects."

# Tags: can be used for filtering projects
tags: ["Teaching", "Education Technology", "Web Application", "Classroom Management"]

# Slides (optional)
slides: ""

# Links (optional)
url_pdf: ""
url_slides: ""
url_video: ""
url_code: ""

# Custom links (optional)
links:
  - icon_pack: fas
    icon: users
    name: Access ClassHub
    url: "https://econclasshub.netlify.app/"

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder
image:
  # Caption (optional)
  caption: "ClassHub - Attendance & Peer Evaluation Platform"

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point: "Smart"
---

**For:** Team-based courses with presentations and group projects

<a href="https://econclasshub.netlify.app/" target="_blank" class="btn btn-primary btn-lg">Access ClassHub →</a>

## Overview

ClassHub is a web app that helps instructors manage attendance and peer evaluations in team-based courses.

## Key Features

| Feature | How It Works |
|---------|--------------|
| **Attendance** | Generate time-limited codes; students submit via phone/laptop |
| **Teams** | Students create or join teams; instructors view rosters |
| **Peer Evaluation** | Anonymous teammate ratings on contribution (rank + score) |
| **Team Rankings** | Students rate other teams' presentations (content, delivery, creativity) |
| **Dashboard** | Instructors see all data, manage records, export results |

## Problems Solved

| Traditional Method | With ClassHub |
|-------------------|---------------|
| Paper sign-ins (slow, fakeable) | Digital codes with timestamps |
| Free-riders in teams | Peer evaluations document contributions |
| Manual data entry | Automatic record-keeping |
| Scattered tools | One integrated platform |

## Benefits

**For Instructors:**
- Save time on attendance and grading
- Identify struggling students early
- Data-backed grade adjustments for team members

**For Students:**
- Fair recognition for contributions
- Develop professional feedback skills
- Mobile-friendly, instant sync

## Technical Overview

| Spec | Detail |
|------|--------|
| Type | Web app (works on any device) |
| Auth | Firebase Authentication |
| Database | Firebase Firestore (real-time) |
| Hosting | Netlify |
| Cost | Free for typical class sizes |
| Capacity | 200+ concurrent users |

## Quick Start

**Instructor (one-time setup ~15 min):**
1. Create Firebase project
2. Deploy to Netlify
3. Create class → share join code

**Students:**
1. Register with instructor's code
2. Join class
3. Submit attendance / complete evaluations
