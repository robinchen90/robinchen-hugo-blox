#!/usr/bin/env python3
"""
chen_cert.py — Robin Chen's personal credential issuance system.

Issues cryptographically signed "professor's list" recognition certificates
using Ed25519 signatures. The private signing key stays on your laptop;
the public verification key gets published on robinchen.org so anyone in
the world can verify a certificate's authenticity.

Commands:
  keygen              Generate a new keypair (run once, ever)
  issue <csv>         Sign certificates for everyone in the CSV
  verify <ref_id>     Verify a certificate you previously issued
  verify-file <path>  Verify any cert JSON file using only the public key
  publish-bundle      Copy the files that go on robinchen.org

CSV format: name,course,semester,note
The 'note' column is optional and lets you attach a personal sentence
to each certificate. Nothing in the CSV references grades or attendance
directly — that screening happens privately, before you build the CSV.
"""

import argparse
import csv
import hashlib
import json
import secrets
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    from nacl.signing import SigningKey, VerifyKey
    from nacl.encoding import HexEncoder
    from nacl.exceptions import BadSignatureError
except ImportError:
    sys.exit("PyNaCl not installed. Run: pip install pynacl")


KEY_DIR = Path.home() / ".chen-survived"
PRIVATE_KEY_PATH = KEY_DIR / "private.key"
PUBLIC_KEY_PATH = KEY_DIR / "public.key"

OUT = Path("./output")
LEDGER_PATH = OUT / "ledger.json"
CERTS_DIR = OUT / "certs"
PUBLIC_BUNDLE = OUT / "publish"
HUGO_CONTENT = OUT / "content" / "survived"
COURSE_BODIES_PATH = Path("./course_bodies.json")

DEFAULT_BODY = (
    "Earned a place on this list through consistent presence, sustained effort, "
    "and the kind of command of the material that comes from actually doing the work."
)


def load_course_bodies() -> dict:
    if COURSE_BODIES_PATH.exists():
        return json.loads(COURSE_BODIES_PATH.read_text())
    return {}


def ensure_dirs():
    KEY_DIR.mkdir(exist_ok=True, mode=0o700)
    OUT.mkdir(exist_ok=True)
    CERTS_DIR.mkdir(exist_ok=True)


def canonicalize(payload: dict) -> bytes:
    """Stable JSON serialization for signing. UTF-8 with sorted keys, no
    whitespace, no ASCII escapes. Matches what browser JS will compute when
    verifying client-side."""
    return json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def generate_ref_id(name: str) -> str:
    """Build a ref ID like 'SOK-9F2A' from a name plus 16 bits of entropy."""
    parts = [p for p in name.strip().split() if p]
    first = parts[0][0].upper() if parts else "X"
    last = parts[-1][:2].upper() if len(parts) > 1 else (parts[0][1:3] if parts else "XX").upper()
    suffix = secrets.token_hex(2).upper()
    return f"{first}{last}-{suffix}"


def cmd_keygen(args):
    ensure_dirs()
    if PRIVATE_KEY_PATH.exists() and not args.force:
        print(f"Private key already exists at {PRIVATE_KEY_PATH}")
        print("Use --force to overwrite. WARNING: this invalidates every certificate")
        print("you have ever issued. Almost never the right move.")
        return 1
    signing_key = SigningKey.generate()
    verify_key = signing_key.verify_key
    PRIVATE_KEY_PATH.write_bytes(signing_key.encode(encoder=HexEncoder))
    PRIVATE_KEY_PATH.chmod(0o600)
    PUBLIC_KEY_PATH.write_bytes(verify_key.encode(encoder=HexEncoder))
    pub_hex = verify_key.encode(encoder=HexEncoder).decode()
    print(f"Private key:  {PRIVATE_KEY_PATH}  (keep secret, back up offline)")
    print(f"Public key:   {PUBLIC_KEY_PATH}   (publish on robinchen.org)")
    print()
    print("Public key (hex):")
    print(f"  {pub_hex}")
    print()
    print("Next: host this at https://robinchen.org/.well-known/chen-pubkey.txt")
    return 0


def load_signing_key():
    if not PRIVATE_KEY_PATH.exists():
        sys.exit("No private key. Run: python chen_cert.py keygen")
    return SigningKey(PRIVATE_KEY_PATH.read_bytes(), encoder=HexEncoder)


def load_verify_key():
    if not PUBLIC_KEY_PATH.exists():
        sys.exit("No public key. Run: python chen_cert.py keygen")
    return VerifyKey(PUBLIC_KEY_PATH.read_bytes(), encoder=HexEncoder)


def cmd_issue(args):
    ensure_dirs()
    signing_key = load_signing_key()
    csv_path = Path(args.csv)
    if not csv_path.exists():
        sys.exit(f"CSV not found: {csv_path}")

    try:
        from cert_pdf import generate_pdf
    except ImportError:
        generate_pdf = None
        print("Note: cert_pdf module not found, skipping PDF generation")

    course_bodies = load_course_bodies()
    ledger = json.loads(LEDGER_PATH.read_text()) if LEDGER_PATH.exists() else []
    existing_ids = {e["ref_id"] for e in ledger}
    issued = []

    with csv_path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            name = row["name"].strip()
            course = row["course"].strip()
            semester = row["semester"].strip()
            note = (row.get("note") or "").strip()

            ref_id = generate_ref_id(name)
            while ref_id in existing_ids:
                ref_id = generate_ref_id(name)
            existing_ids.add(ref_id)

            body_text = course_bodies.get(course, DEFAULT_BODY)

            payload = {
                "ref_id": ref_id,
                "issued_to": name,
                "course": course,
                "semester": semester,
                "issued_date": datetime.now(timezone.utc).date().isoformat(),
                "issuer": "Robin Chen",
                "issuer_affiliation": "University of Northern Iowa",
                "issuer_disclaimer": "Personal recognition. Not an institutional credential.",
                "type": "professors-list-recognition-v1",
                "verification_url": f"https://robinchen.org/survived/{ref_id}",
                "public_key_url": "https://robinchen.org/.well-known/chen-pubkey.txt",
                "body_text": body_text,
            }
            if note:
                payload["personal_note"] = note

            message = canonicalize(payload)
            signature = signing_key.sign(message).signature.hex()

            cert = {
                "payload": payload,
                "signature": signature,
                "algorithm": "Ed25519",
            }

            (CERTS_DIR / f"{ref_id}.json").write_text(json.dumps(cert, indent=2))

            if generate_pdf is not None:
                generate_pdf(cert, CERTS_DIR / f"{ref_id}.pdf")

            HUGO_CONTENT.mkdir(parents=True, exist_ok=True)
            stub = (
                "---\n"
                f"title: \"Recognition for {name}\"\n"
                f"date: {payload['issued_date']}\n"
                f"ref_id: \"{ref_id}\"\n"
                f"issued_to: \"{name}\"\n"
                f"course: \"{course}\"\n"
                f"semester: \"{semester}\"\n"
                "type: \"survived\"\n"
                "layout: \"single\"\n"
                "---\n"
            )
            (HUGO_CONTENT / f"{ref_id}.md").write_text(stub)

            ledger.append({
                "ref_id": ref_id,
                "issued_date": payload["issued_date"],
                "course": course,
                "semester": semester,
                "payload_hash": hashlib.sha256(message).hexdigest(),
            })
            issued.append((ref_id, name, course, semester))
            print(f"  {ref_id}  ->  {name}  ({course}, {semester})")

    LEDGER_PATH.write_text(json.dumps(ledger, indent=2))
    print(f"\nIssued {len(issued)} certificate(s).")
    print(f"Cert files:  {CERTS_DIR}/")
    print(f"Ledger:      {LEDGER_PATH}")
    return 0


def _print_cert(cert):
    p = cert["payload"]
    print(f"  Ref ID:      {p['ref_id']}")
    print(f"  Issued to:   {p['issued_to']}")
    print(f"  Course:      {p['course']}")
    print(f"  Semester:    {p['semester']}")
    print(f"  Date:        {p['issued_date']}")
    print(f"  Issuer:      {p['issuer']}  ({p['issuer_affiliation']})")
    if p.get("personal_note"):
        print(f"  Note:        {p['personal_note']}")
    print(f"  URL:         {p['verification_url']}")
    print(f"  Signature:   {cert['signature'][:32]}...")


def cmd_verify(args):
    verify_key = load_verify_key()
    cert_path = CERTS_DIR / f"{args.ref_id}.json"
    if not cert_path.exists():
        sys.exit(f"No certificate at {cert_path}")
    cert = json.loads(cert_path.read_text())
    try:
        verify_key.verify(canonicalize(cert["payload"]), bytes.fromhex(cert["signature"]))
        print(f"VALID  {args.ref_id}\n")
        _print_cert(cert)
        return 0
    except BadSignatureError:
        print(f"INVALID  {args.ref_id}  -- signature does not match")
        return 2


def cmd_verify_file(args):
    """Verify any cert file using only the public key. Demonstrates that a
    third party (employer, hiring manager) can verify on their own machine
    using nothing but the public key from robinchen.org."""
    cert_path = Path(args.path)
    if not cert_path.exists():
        sys.exit(f"File not found: {cert_path}")
    cert = json.loads(cert_path.read_text())

    if args.pubkey:
        verify_key = VerifyKey(Path(args.pubkey).read_text().strip().encode(), encoder=HexEncoder)
    else:
        verify_key = load_verify_key()

    try:
        verify_key.verify(canonicalize(cert["payload"]), bytes.fromhex(cert["signature"]))
        print("VALID\n")
        _print_cert(cert)
        return 0
    except BadSignatureError:
        print("INVALID -- signature does not match the public key")
        return 2


def cmd_publish_bundle(args):
    """Assemble the files that go on robinchen.org into one folder."""
    if not LEDGER_PATH.exists():
        sys.exit("No ledger yet. Issue some certificates first.")
    PUBLIC_BUNDLE.mkdir(exist_ok=True)
    (PUBLIC_BUNDLE / "survived").mkdir(exist_ok=True)
    (PUBLIC_BUNDLE / ".well-known").mkdir(exist_ok=True)

    shutil.copy(PUBLIC_KEY_PATH, PUBLIC_BUNDLE / ".well-known" / "chen-pubkey.txt")
    shutil.copy(LEDGER_PATH, PUBLIC_BUNDLE / "survived" / "ledger.json")
    for cert_file in CERTS_DIR.glob("*.json"):
        shutil.copy(cert_file, PUBLIC_BUNDLE / "survived" / cert_file.name)
    for pdf_file in CERTS_DIR.glob("*.pdf"):
        shutil.copy(pdf_file, PUBLIC_BUNDLE / "survived" / pdf_file.name)

    print(f"Bundle ready at: {PUBLIC_BUNDLE}/")
    print("\nUpload these paths to robinchen.org preserving the directory structure:")
    print("  /.well-known/chen-pubkey.txt   (your public key)")
    print("  /survived/ledger.json           (list of all certificates issued)")
    print("  /survived/{ref_id}.json         (each cert, signed JSON for verification)")
    print("  /survived/{ref_id}.pdf          (each cert, shareable PDF)")
    return 0


def main():
    parser = argparse.ArgumentParser(prog="chen_cert.py")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("keygen", help="Generate the Ed25519 keypair (once, ever)")
    p1.add_argument("--force", action="store_true")
    p1.set_defaults(func=cmd_keygen)

    p2 = sub.add_parser("issue", help="Sign certificates from a CSV")
    p2.add_argument("csv")
    p2.set_defaults(func=cmd_issue)

    p3 = sub.add_parser("verify", help="Verify a cert by ref ID")
    p3.add_argument("ref_id")
    p3.set_defaults(func=cmd_verify)

    p4 = sub.add_parser("verify-file", help="Verify any cert JSON, optionally with a different pubkey")
    p4.add_argument("path")
    p4.add_argument("--pubkey", help="Path to alternate public key file")
    p4.set_defaults(func=cmd_verify_file)

    p5 = sub.add_parser("publish-bundle", help="Assemble the files for upload to robinchen.org")
    p5.set_defaults(func=cmd_publish_bundle)

    args = parser.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
