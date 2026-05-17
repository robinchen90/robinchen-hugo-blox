# Chen survived cert system

A small Python CLI for issuing cryptographically signed personal recognition
certificates. Built for Robin Chen's professor's list — a private alternative
to institutional credentials, signed with your own key, verifiable forever.

## What it does

Each certificate is a JSON document signed with your Ed25519 private key. The
signature can be verified by anyone with your public key. The private key
never leaves your laptop. The public key lives on robinchen.org so that
anyone — employers, journalists, future-you — can confirm a certificate's
authenticity even decades after you issued it.

Key properties:

- **Forgery-resistant.** Anyone modifying the cert breaks the signature.
- **Site-independent.** Verification works without robinchen.org being online,
  as long as the recipient has the cert file and your public key.
- **Institutionally neutral.** Signed by you as an individual scholar. No
  UNI involvement, no UNI permission, no UNI exposure.

## Setup

```
pip install pynacl
python chen_cert.py keygen
```

This creates `~/.chen-survived/private.key` (keep secret, back up offline
to encrypted storage) and `~/.chen-survived/public.key` (publish on your
site at `/.well-known/chen-pubkey.txt`).

**Backup the private key now.** If you lose it, every certificate you ever
issue becomes unverifiable. Encrypted USB stick in a drawer, encrypted
cloud backup, whatever — just make sure it survives a laptop loss.

## Each semester

1. Privately screen your students using your real criteria (attendance ≥ 80%,
   final grade = A). This screening stays in your private spreadsheet and is
   never disclosed publicly.

2. Build a CSV of the students who passed the screening:

   ```
   name,course,semester,note
   Sara Okonkwo,Money and banking,Spring 2026,She asked the question that...
   ```

   The `note` column should describe what you witnessed about the student —
   their engagement, their work, their judgment. Never reference grades,
   attendance percentages, or any record-derived data. Speak as a witness,
   not as a registrar.

3. Email each student asking consent before issuing the cert and the
   accompanying public list entry. Save replies.

4. Issue:

   ```
   python chen_cert.py issue students.csv
   ```

   Each student gets a unique reference ID like `SOK-9F2A`. Cert files land
   in `output/certs/`.

5. Bundle for upload:

   ```
   python chen_cert.py publish-bundle
   ```

   Upload `output/publish/` to robinchen.org preserving directory structure.

6. Email each student their verification URL.

## Verifying

To verify a certificate you previously issued:

```
python chen_cert.py verify SOK-9F2A
```

To verify any certificate file using only the public key (this is what an
employer would do — the verification works with no access to your laptop
or your website):

```
python chen_cert.py verify-file cert.json --pubkey chen-pubkey.txt
```

## What the website needs

Three things hosted on robinchen.org:

1. `/.well-known/chen-pubkey.txt` — your public key in hex. One line of text.
2. `/survived/ledger.json` — list of all certificates issued.
3. `/survived/{ref_id}.json` — each certificate, one file per recipient.

That's enough for command-line verification. To make verification work in a
browser when someone visits the cert URL, the verification page needs a few
lines of JavaScript that fetches the cert JSON, fetches the public key, and
runs Ed25519 verification client-side using tweetnacl-js (~3KB library).
That page is a follow-up build — the cryptographic foundation is here.

## Key rotation and recovery

If your private key is ever compromised, generate a new one with `keygen
--force`. All certificates issued under the old key become unverifiable,
which is the right behavior — you don't want a stolen key to be trusted.
Maintain a public revocation note on robinchen.org if this ever happens.

In practice: back up the private key carefully, and you should never need to
rotate.

## What this isn't

This is not a replacement for a formal credential. It's a personal artifact
issued by you, in your name, as your individual judgment about a student's
work. The accompanying `issuer_disclaimer` field on every cert says so
explicitly. The credibility of the certificate rests entirely on your
reputation, which is the point.
