# Claude Code spec — The Professor's List on robinchen.org

**Goal:** Integrate the cryptographically signed cert system (chen_cert.py) with the existing Hugo Blox Builder site at robinchen.org. Add a "Professor's List" entry under `/project/` matching the existing Innovations cards (ClassHub, Bond Pricing Calculator, etc.), build a public list page at `/survived/`, and create a per-cert verification page at `/survived/{ref_id}/` that runs Ed25519 signature verification in the browser.

**Site framework:** Hugo Blox Builder 5.9.7 (Hugo + Wowchemy-derived theme). Content in `content/`, layouts in `layouts/`, static files in `static/`.

**Sharing model:** The verification URL is the canonical artifact. The PDF is a secondary keepsake that students can download from the URL. Every PDF embeds a QR code that points back to the verification URL, so trust always routes through the live page.

---

## Section 1 — Files to create

### A. New project entry

Path: `content/project/professors-list/index.md`

Front matter and body, modeled on existing entries like `content/project/econclasshub/index.md`. Use the existing project entries as a template — match their structure exactly so the card renders correctly on `/project/`.

```yaml
---
title: "The Professor's List"
date: 2026-05-17
external_link: ""
image:
  caption: ""
  focal_point: "Smart"
summary: "A cryptographically signed personal recognition for students who showed up, worked through real failure, and proved they can learn faster than the next mistake. Each cert is signed with my personal Ed25519 key — verifiable forever, independent of any institution."
tags:
  - Teaching
  - AI Era
  - Credentials
links:
  - name: "View the list"
    url: "/survived/"
    icon_pack: "fas"
    icon: "list"
weight: 1
---

Most credentials say a student passed. They do not say what the student survived.

The Professor's List is a personal recognition issued by me, not by any institution, to students whose work and engagement throughout a semester met a standard I set for myself. The list is short by design. Each entry comes with a cryptographically signed certificate that the student can share — verifiable forever, even if I leave the institution and even if this website goes offline.

Why now: when AI can produce a polished paper in thirty seconds, the durable skill of the AI era is not the polish. It is the capacity to fail, recover, and learn faster the next time. That capacity is what these recognitions attest to.
```

Also create a featured card image at `content/project/professors-list/featured.png` (a dark-background "Survived." graphic, ~1200x630, matching the cert aesthetic). If you do not have a graphic ready, render the certificate visual from this conversation as a PNG and use that.

### B. Public list landing page

Path: `content/survived/_index.md`

```yaml
---
title: "The Professor's List"
date: 2026-05-17
type: "survived"
layout: "list"
---

A short, personal list of students whose work and judgment I want on the public record. Updated each semester. The reasoning is mine, not the registrar's.

Students appear on this list when their work and engagement throughout a semester met a standard I set for myself: consistent presence, sustained effort, and the kind of command of the material that comes from actually showing up to do the work. The list is short by design.

Each entry below links to a signed certificate page. Click any name to verify the certificate in your browser — the signature check runs against my published public key and confirms the recognition was issued by me, not by anyone else, and has not been tampered with.
```

### C. Per-cert content stubs

These are generated automatically by chen_cert.py — you do not write them by hand. After running `python chen_cert.py issue <csv>`, the script produces files at `output/content/survived/{ref_id}.md`. Each file looks like:

```yaml
---
title: "Recognition for Marcus Holm"
date: 2025-12-17
ref_id: "MHO-5F6A"
issued_to: "Marcus Holm"
course: "Business forecasting"
semester: "Fall 2025"
type: "survived"
layout: "single"
---
```

Copy these into `content/survived/` in the Hugo site each semester.

### D. List layout (the `/survived/` index)

Path: `layouts/survived/list.html`

```html
{{ define "main" }}
<div class="container" style="max-width: 880px; padding: 4rem 1.5rem;">
  <h1 style="font-family: serif; font-size: 2.5rem; font-weight: 500; letter-spacing: -0.02em;">{{ .Title }}</h1>

  <div style="font-size: 1.05rem; line-height: 1.7; color: var(--bs-secondary, #555); margin: 1.5rem 0 3rem;">
    {{ .Content }}
  </div>

  <div id="cert-list" style="display: flex; flex-direction: column; gap: 0.75rem;">
    {{ range (where .Site.RegularPages "Type" "survived").ByDate.Reverse }}
    <a href="{{ .Permalink }}" style="display: block; padding: 1.1rem 1.4rem; border: 0.5px solid rgba(0,0,0,0.15); border-radius: 8px; text-decoration: none; color: inherit; transition: border-color 0.2s;">
      <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 1rem;">
        <h3 style="font-family: serif; font-size: 1.2rem; margin: 0; letter-spacing: -0.01em;">{{ .Params.issued_to }}</h3>
        <span style="font-size: 0.85rem; color: var(--bs-secondary, #888); letter-spacing: 0.03em;">{{ .Params.course }} · {{ .Params.semester }}</span>
      </div>
      <p style="margin: 0.4rem 0 0; font-size: 0.9rem; color: var(--bs-secondary, #777);">Click to verify certificate {{ .Params.ref_id }}</p>
    </a>
    {{ end }}
  </div>
</div>
{{ end }}
```

Note: This includes every name with a content stub. If you want consent gating (some students get a private cert but no public list entry), add a `public: true` field to the stub front matter and filter on it: `{{ range (where (where .Site.RegularPages "Type" "survived") ".Params.public" true) }}`.

### E. Single-cert layout (the verification page)

Path: `layouts/survived/single.html`

This is the heart of the system. It loads the signed cert JSON, fetches the public key, runs Ed25519 verification in the browser, and displays the cert with a "verified" or "invalid" badge.

```html
{{ define "main" }}
<div class="container" style="max-width: 800px; padding: 4rem 1.5rem;">
  <div id="cert-card" style="background: #0F1419; color: #E8E5DC; padding: 3rem 2.75rem 2.5rem; border-radius: 12px; font-family: serif;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 1.75rem; font-family: sans-serif; font-size: 11px; letter-spacing: 0.12em; color: #8C8779; flex-wrap: wrap; gap: 8px;">
      <span>THE PROFESSOR'S LIST · A NOTE OF RECOGNITION</span>
      <span style="font-family: serif; font-size: 14px; font-style: italic; color: #E8E5DC; letter-spacing: 0;">Robin Chen</span>
    </div>

    <h1 style="font-family: serif; font-size: 5rem; font-weight: 500; line-height: 0.95; margin: 0 0 0.5rem; letter-spacing: -0.03em; color: #E8E5DC;">Survived.</h1>

    <p id="cert-context" style="font-family: sans-serif; font-size: 14px; color: #A39E91; margin: 0 0 1.5rem; letter-spacing: 0.02em;">Loading...</p>

    <p id="cert-body" style="font-family: sans-serif; font-size: 15px; line-height: 1.7; color: #C9C4B5; margin: 0 0 2rem; max-width: 36rem;"></p>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; align-items: end; padding-top: 1.5rem; border-top: 0.5px solid #2A2F36;">
      <div>
        <p style="font-family: sans-serif; font-size: 10px; color: #8C8779; letter-spacing: 0.15em; margin: 0 0 4px;">A NOTE ABOUT</p>
        <p id="cert-name" style="font-family: serif; font-size: 1.6rem; font-weight: 500; color: #E8E5DC; margin: 0; letter-spacing: -0.01em;"></p>
        <p id="cert-meta" style="font-family: sans-serif; font-size: 11px; color: #8C8779; line-height: 1.7; margin: 8px 0 0;"></p>
      </div>
      <div style="text-align: right;">
        <p style="font-family: serif; font-style: italic; font-size: 1.4rem; color: #E8E5DC; margin: 0 0 4px;">Robin Chen</p>
        <p style="font-family: sans-serif; font-size: 10px; color: #8C8779; letter-spacing: 0.15em; margin: 0;">ASSISTANT PROFESSOR OF ECONOMICS</p>
      </div>
    </div>

    <p style="font-family: sans-serif; font-size: 10px; color: #6B675C; margin: 1.5rem 0 0; line-height: 1.5;">Personal recognition from Robin Chen as an individual scholar. Affiliation: University of Northern Iowa. Not an institutional credential and does not supplement, replace, or modify any record issued by the university.</p>
  </div>

  <div id="verify-status" style="margin-top: 1.5rem; padding: 1rem 1.25rem; border-radius: 8px; font-size: 0.95rem; display: flex; align-items: center; gap: 0.75rem;">
    <span id="verify-icon" style="font-size: 1.4rem;">⏳</span>
    <span id="verify-text">Verifying signature against published public key...</span>
  </div>

  <div style="margin-top: 1.5rem; display: flex; gap: 0.75rem; flex-wrap: wrap;">
    <a id="pdf-link" href="" style="padding: 0.6rem 1.1rem; border: 0.5px solid rgba(0,0,0,0.3); border-radius: 8px; text-decoration: none; color: inherit; font-size: 0.9rem;">Download PDF</a>
    <a href="/.well-known/chen-pubkey.txt" style="padding: 0.6rem 1.1rem; border: 0.5px solid rgba(0,0,0,0.3); border-radius: 8px; text-decoration: none; color: inherit; font-size: 0.9rem;">View public key</a>
    <a href="/survived/" style="padding: 0.6rem 1.1rem; border: 0.5px solid rgba(0,0,0,0.3); border-radius: 8px; text-decoration: none; color: inherit; font-size: 0.9rem;">All recognitions</a>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/tweetnacl/1.0.3/nacl.min.js"></script>
<script>
(async function() {
  const refId = "{{ .Params.ref_id }}";

  function hexToBytes(hex) {
    const bytes = new Uint8Array(hex.length / 2);
    for (let i = 0; i < bytes.length; i++) bytes[i] = parseInt(hex.substr(i * 2, 2), 16);
    return bytes;
  }

  function canonicalJson(obj) {
    if (obj === null) return "null";
    if (typeof obj === "boolean") return obj ? "true" : "false";
    if (typeof obj === "number") return String(obj);
    if (typeof obj === "string") return JSON.stringify(obj);
    if (Array.isArray(obj)) return "[" + obj.map(canonicalJson).join(",") + "]";
    const keys = Object.keys(obj).sort();
    return "{" + keys.map(k => JSON.stringify(k) + ":" + canonicalJson(obj[k])).join(",") + "}";
  }

  function setStatus(icon, text, color) {
    document.getElementById("verify-icon").textContent = icon;
    document.getElementById("verify-text").textContent = text;
    document.getElementById("verify-status").style.background = color;
  }

  try {
    const certResp = await fetch(`/survived/${refId}.json`);
    if (!certResp.ok) throw new Error("Certificate file not found");
    const cert = await certResp.json();
    const p = cert.payload;

    document.getElementById("cert-context").textContent = `${p.course} · ${p.semester}`;
    document.getElementById("cert-body").textContent = p.body_text || "";
    document.getElementById("cert-name").textContent = p.issued_to;
    document.getElementById("cert-meta").innerHTML = `Reference ${p.ref_id} · ${p.issued_date}<br>Issued ${p.issued_date}`;
    document.getElementById("pdf-link").href = `/survived/${refId}.pdf`;

    const pubKeyResp = await fetch("/.well-known/chen-pubkey.txt");
    const pubKeyHex = (await pubKeyResp.text()).trim();
    const pubKey = hexToBytes(pubKeyHex);
    const signature = hexToBytes(cert.signature);
    const message = new TextEncoder().encode(canonicalJson(p));

    const valid = nacl.sign.detached.verify(message, signature, pubKey);

    if (valid) {
      setStatus("✓", `Verified. This recognition was issued by Robin Chen on ${p.issued_date} and has not been modified.`, "rgba(60, 160, 100, 0.12)");
    } else {
      setStatus("✗", "Invalid signature. This certificate has been tampered with or does not match the published public key.", "rgba(200, 60, 60, 0.12)");
    }
  } catch (err) {
    setStatus("!", `Could not verify: ${err.message}`, "rgba(200, 150, 50, 0.12)");
  }
})();
</script>
{{ end }}
```

### F. Static files (no Hugo processing)

Upload directly under `static/`:

```
static/.well-known/chen-pubkey.txt    (your public key, one line of hex)
static/survived/ledger.json           (auto-generated)
static/survived/{ref_id}.json         (auto-generated, one per cert)
static/survived/{ref_id}.pdf          (auto-generated, one per cert)
```

These come from running `python chen_cert.py publish-bundle`. Copy the contents of `output/publish/` into the appropriate places in `static/`.

---

## Section 2 — End-to-end workflow each semester

1. **Screen students privately.** In your gradebook spreadsheet, filter students with attendance ≥ 80% and final grade = A. This stays on your laptop. Never gets disclosed publicly.

2. **Get consent.** Email each student something like: "You met the standard I set for the professor's list this semester. If you'd like to be named publicly at robinchen.org/survived/, reply yes. If not, you'll still receive your private certificate — only the public list entry requires consent." Save replies.

3. **Build the CSV.** Columns: `name,course,semester,note`. Leave `note` empty to use the course-standard body text. Fill in a personal sentence only for students you want to single out.

4. **Issue the certs.** Run on your laptop:
   ```
   python chen_cert.py issue students_fall2025.csv
   ```
   This produces:
   - `output/certs/{ref_id}.json` (signed cert payload)
   - `output/certs/{ref_id}.pdf` (shareable PDF with QR code)
   - `output/content/survived/{ref_id}.md` (Hugo content stub)

5. **Copy into the Hugo site.**
   - `output/content/survived/*.md` → `content/survived/`
   - `output/certs/*.json` → `static/survived/`
   - `output/certs/*.pdf` → `static/survived/`
   - `output/ledger.json` → `static/survived/ledger.json`

6. **Commit and deploy.**
   ```
   cd robinchen.org
   git add content/survived static/survived
   git commit -m "Add Fall 2025 professor's list recognitions"
   git push
   ```

7. **Email each student their URL.** Each student gets a personalized email with their `robinchen.org/survived/{ref_id}` link. Suggested template in Section 4.

---

## Section 3 — One-time setup (first time only)

Done once, ever:

1. **Generate the keypair on your laptop.**
   ```
   python chen_cert.py keygen
   ```
   This writes private key to `~/.chen-survived/private.key` (keep secret, back up offline to encrypted storage) and prints the public key in hex.

2. **Publish the public key.** Save the hex string to a file and place it at `static/.well-known/chen-pubkey.txt` in your Hugo site. One line of text. Commit and deploy.

3. **Create the project entry and list landing page** as specified in Section 1A and 1B.

4. **Create both layout files** as specified in Section 1D and 1E.

5. **Verify the system end-to-end** by issuing one test certificate, deploying, and clicking the verification URL in a browser. Confirm the green "verified" badge appears.

After this is done once, the per-semester workflow in Section 2 is the only thing you ever do again.

---

## Section 4 — Suggested student email template

Subject: Professor's list recognition — Fall 2025 forecasting

> Marcus,
>
> You met the standard I set for the professor's list this semester. The recognition lives here:
>
> https://robinchen.org/survived/MHO-5F6A
>
> The page is cryptographically signed with my personal key and verifiable by anyone — meaning this stays valid even if I leave UNI and even if this website ever goes offline. You can also download a PDF version from the page if you want to attach it to applications.
>
> The recognition speaks to what you actually did this semester: showed up, worked through real failure, and turned in work that improved between drafts. That capacity to recover from things going wrong is the durable skill that matters more than any single output, and it is what this list attests to.
>
> Congratulations.
>
> — Robin

---

## Section 5 — Important implementation notes

**Canonical JSON.** The Python signing code uses `json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)`. The JavaScript verification code (Section 1E) uses a matching `canonicalJson()` function. If you modify either, modify both — the bytes must be identical or the signature will not verify.

**TweetNaCl loading.** The verification page loads tweetnacl-js from cdnjs. If you have a strict Content-Security-Policy, allow `cdnjs.cloudflare.com` or self-host the 3KB library at `static/js/nacl.min.js` and change the script src.

**Hugo content type vs. layout.** The front matter `type: "survived"` tells Hugo to look in `layouts/survived/` for templates. The `layout: "single"` tells it to use `single.html`. If your Hugo Blox theme overrides these in unexpected ways, you may need to add the templates to your theme's expected location instead — check with `hugo --buildDrafts -v` for path warnings.

**Image for the project card.** Hugo Blox Builder expects `featured.png` or `featured.jpg` inside the project folder. If you do not have a graphic, generate one from the certificate HTML mockup at 1200x630 and save it as `content/project/professors-list/featured.png`.

**Permanent URLs.** Once a student has been told their URL, never change the ref_id or move the file. The URL is the credential. Treat each issued ref_id as immutable — if you need to correct a typo in someone's name, issue a new cert with a new ref_id and politely tell the student which one to use going forward (keep the old one alive so any existing shares still resolve).

**Public key rotation.** If your private key is ever compromised, generate a new keypair with `python chen_cert.py keygen --force`, publish the new public key, and add a revocation note at `static/survived/REVOCATION.md` explaining which old ref_ids are no longer trustworthy. In practice: back up the private key carefully and you should never need to rotate.

---

## Section 6 — Acceptance checklist

After Claude Code finishes:

- [ ] `https://robinchen.org/project/professors-list/` renders with the card, summary, and body text.
- [ ] The page is reachable from the "Innovations" card on `/project/`.
- [ ] `https://robinchen.org/.well-known/chen-pubkey.txt` returns a single line of hex (the public key).
- [ ] `https://robinchen.org/survived/` renders with the landing copy and a list of issued certs.
- [ ] `https://robinchen.org/survived/MHO-5F6A` (or whichever test ref_id) renders the cert and shows a green "verified" badge within a second of loading.
- [ ] Tampering test: edit `static/survived/MHO-5F6A.json` to change the student's name, redeploy, and confirm the page shows a red "invalid signature" badge.
- [ ] PDF download from the cert page works.
- [ ] QR code on the PDF scans to the same verification URL.

---

**End of spec.**
