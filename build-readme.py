#!/usr/bin/env python3
"""Build README.md from data/. Run after changing anything under data/.

    python3 build-readme.py            write README.md
    python3 build-readme.py --check    exit 1 if README.md is out of date

The listings are the source of truth; the README is a rendering of them, so it
is never edited by hand. Prose belongs in HEADER below.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent
BUNDLE_KINDS = (("skills", "skills"), ("commands", "commands"), ("agents", "agents"), ("mcp_servers", "MCP servers"))

HEADER = """# Awesome Dutch AI Extensions

MCP servers, skills, and plugins that connect an AI assistant to a Dutch service, data source, standard, or authority.

The list below is a readable view, built from the data by `build-readme.py` — edit `data/`, not this file. The data is the point: one JSON file per listing in [`data/listings/`](data/listings), described in [`schema.json`](schema.json).

Each entry is tagged with what you install — MCP, Skill, or Plugin — and who publishes it: Official, Commercial, or Community. A maturity tag follows only when the entry is not live. Where an entry bundles skills, commands, agents, or MCP servers, they are named beneath it.

To add an integration, see [CONTRIBUTING.md](CONTRIBUTING.md).
"""


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def tags(listing, labels):
    """Type and origin always; maturity only when the listing is not live."""
    parts = [labels["type"][listing["type"]]["en"], labels["origin"][listing["origin"]]["en"]]
    if listing["status"] != "live":
        parts.append(labels["status"][listing["status"]]["en"])
    return " · ".join(parts)


def bundles(listing):
    named = [f"{label}: " + ", ".join(listing["bundles"][key]) for key, label in BUNDLE_KINDS if listing["bundles"][key]]
    return " · ".join(named)


def render():
    categories = load("data/categories.json")
    labels = load("data/labels.json")
    listings = [load(f"data/listings/{p.name}") for p in sorted((ROOT / "data" / "listings").glob("*.json"))]

    for listing in listings:
        if listing["category"] not in categories:
            sys.exit(f"{listing['id']}: category {listing['category']!r} is not in data/categories.json")

    out = [HEADER]
    for key, title in categories.items():
        rows = sorted((d for d in listings if d["category"] == key), key=lambda d: d["name"].lower())
        out.append(f"## {title['en']}\n")
        for listing in rows:
            line = f"- [{listing['name']}]({listing['source_url']}) — {listing['description_en']} _({tags(listing, labels)})_"
            if bundled := bundles(listing):
                line += f"\n  <br>Bundles — {bundled}"
            out.append(line)
        out.append("")
    return "\n".join(out).rstrip("\n") + "\n", len(listings)


def main():
    text, count = render()
    readme = ROOT / "README.md"

    if "--check" in sys.argv:
        current = readme.read_text(encoding="utf-8") if readme.exists() else ""
        if current != text:
            sys.exit("README.md is out of date — run: python3 build-readme.py")
        print(f"README.md is up to date ({count} listings).")
        return

    readme.write_text(text, encoding="utf-8")
    print(f"Wrote README.md — {count} listings across {len(load('data/categories.json'))} categories.")


if __name__ == "__main__":
    main()
