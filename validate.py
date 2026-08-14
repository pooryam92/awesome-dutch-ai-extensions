#!/usr/bin/env python3
"""Validate data/ against schema.json and check the cross-file references.

    python3 validate.py    report every problem, exit 1 if there are any

build-readme.py deliberately stays stdlib-only so anyone can regenerate the
README with no setup; it therefore checks only that the fields it renders are
present. This is the strict pass — types, patterns, enums, and date/URI formats
— and it needs jsonschema:

    pip install "jsonschema[format-nongpl]"

It also covers what JSON Schema cannot see, because those rules span files: a
listing's category and subjects must resolve to real registry entries, every
registry entry must be reachable from some listing, and data/labels.json must
carry a label for every enum value the schema allows — plus the kind tokens
build-readme.py derives from `contains`, which no enum lists.

Every problem is reported in one run — a contributor fixing a submission should
not have to rerun this once per typo.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
LISTINGS = ROOT / "data" / "listings"

# labels.json needs an entry per enum value, and each entry needs all three keys.
# A missing one is invisible on inspection: build-readme.py falls back to a grey
# pill and renders the raw token, so the badge looks deliberate rather than broken.
LABEL_GROUPS = ("origin", "status")
LABEL_KEYS = ("en", "nl", "color")

# The kind pill is derived from `contains` rather than stored, so its tokens are in
# no schema enum and have to be named here — the one label group nothing else lists.
KIND_TOKENS = ("mcp", "skill", "command", "agent", "bundle")
COLOR = re.compile(r"^[0-9a-f]{6}$")


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def schema_errors(schema, listings):
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError:
        sys.exit(
            'validate.py needs jsonschema — pip install "jsonschema[format-nongpl]"\n'
            "(format-nongpl is what makes the source_url and last_checked format "
            "checks actually run; plain jsonschema skips them silently.)"
        )

    # format is an annotation by default — opt in, or source_url and last_checked
    # are only ever checked for being strings.
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for name, listing in listings:
        for error in sorted(validator.iter_errors(listing), key=lambda e: list(e.path)):
            where = ".".join(str(p) for p in error.path) or "(root)"
            yield f"{name}: {where}: {error.message}"


def reference_errors(listings, categories, subjects):
    seen_urls, used_subjects = {}, set()

    for name, listing in listings:
        # The filename is the join key every other surface will use, so a listing
        # whose id drifts from its filename is ambiguous, not merely untidy.
        if listing.get("id") != Path(name).stem:
            yield f"{name}: id {listing.get('id')!r} does not match the filename"
        if listing.get("category") not in categories:
            yield f"{name}: category {listing.get('category')!r} is not in data/categories.json"
        for sid in listing.get("subject", []):
            used_subjects.add(sid)
            if sid not in subjects:
                yield f"{name}: subject {sid!r} is not in data/subjects.json"
        # Neutral wording on purpose: files are walked in sorted order, so the
        # one flagged is whichever sorts later — not necessarily the new one.
        url = listing.get("source_url")
        if url in seen_urls:
            yield f"{name}: source_url is a duplicate of {seen_urls[url]}"
        elif url:
            seen_urls[url] = name
        # One row per party is the whole point of `uses`; two rows for the same
        # domain contradict each other the moment their `account` flags differ,
        # and uniqueItems only catches the case where they do not.
        domains = [row.get("domain") for row in listing.get("uses", [])]
        for domain in sorted({d for d in domains if domains.count(d) > 1}):
            yield f"{name}: uses names {domain!r} more than once"

    # An unreferenced registry entry is dead weight that still shows up when the
    # next contributor greps for a key to reuse.
    for sid in sorted(set(subjects) - used_subjects):
        yield f"data/subjects.json: {sid!r} is not used by any listing"


def registry_errors(schema, categories, subjects, labels):
    for key, title in sorted(categories.items()):
        for lang in ("en", "nl"):
            if not title.get(lang):
                yield f"data/categories.json: {key!r} has no {lang} title"

    for key, subject in sorted(subjects.items()):
        if not subject.get("name"):
            yield f"data/subjects.json: {key!r} has no name"

    groups = [(group, schema["properties"][group]["enum"]) for group in LABEL_GROUPS]
    groups.append(("kind", KIND_TOKENS))
    for group, tokens in groups:
        for token in tokens:
            label = labels.get(group, {}).get(token)
            if label is None:
                yield f"data/labels.json: no {group} label for {token!r}"
                continue
            for key in LABEL_KEYS:
                if not label.get(key):
                    yield f"data/labels.json: {group}.{token} has no {key}"
            # Six lowercase hex digits, no leading "#" — the value is interpolated
            # straight into fill="#{color}", where a stray hash yields fill="##...".
            color = label.get("color", "")
            if color and not COLOR.match(color):
                yield f"data/labels.json: {group}.{token} color {color!r} is not six hex digits"


def main():
    schema = load("schema.json")
    categories = load("data/categories.json")
    subjects = load("data/subjects.json")
    labels = load("data/labels.json")
    listings = [(p.name, json.loads(p.read_text(encoding="utf-8"))) for p in sorted(LISTINGS.glob("*.json"))]

    problems = [
        *schema_errors(schema, listings),
        *reference_errors(listings, categories, subjects),
        *registry_errors(schema, categories, subjects, labels),
    ]

    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        sys.exit(f"\n{len(problems)} problem(s) in data/.")

    print(f"data/ is valid — {len(listings)} listings, {len(subjects)} subjects, {len(categories)} categories.")


if __name__ == "__main__":
    main()
