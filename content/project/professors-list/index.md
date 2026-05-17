---
title: "The Professor's List · A Note of Recognition"
date: 2026-05-17T00:00:00

summary: "Personal, cryptographically-signed recognition for students who showed up, worked through the hard parts, and survived the course."

tags: ["Teaching", "Recognition", "Cryptography"]

slides: ""
url_pdf: ""
url_slides: ""
url_video: ""
url_code: ""

links:
  - icon_pack: fas
    icon: award
    name: Browse The List
    url: /survived/

image:
  caption: "The Professor's List — a personal note of recognition"
  focal_point: "Smart"
---

<a href="/survived/" class="btn btn-primary btn-lg">Browse The List →</a>

## What is this?

The Professor's List is a personal recognition I issue to students who showed up — not just attended, but joined the room, worked through the frustrating parts, and completed an original project from scratch. Each certificate is a note from me as an individual, not a UNI credential.

Every certificate is **cryptographically signed** with my Ed25519 private key and verified in your browser against my public key. Anyone can confirm that a certificate is authentic, unaltered, and issued by me — without trusting any third party.

## How verification works

Each certificate carries a unique reference ID (like `MHO-5F6A`). When you visit the verification page, your browser:

1. Fetches the signed certificate JSON from this site
2. Fetches my public key from `/.well-known/chen-pubkey.txt`
3. Recomputes the canonical form of the certificate and checks the Ed25519 signature
4. Shows a green **✓ Verified** badge if the signature matches, or a red **⚠ Tampered** warning if not

This means you can verify the certificate entirely offline — download the JSON and the public key, and run the same check with any Ed25519 library.

## What this is not

This is not a UNI transcript entry, grade modifier, or institutional credential. It does not replace or supplement any record issued by the University of Northern Iowa. It is a personal gesture — something to keep if it means something to you.
