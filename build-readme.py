#!/usr/bin/env python3
"""Build README.md and assets/badges/ from data/. Run after changing anything under data/.

    python3 build-readme.py            write README.md and reconcile assets/badges
    python3 build-readme.py --check    exit 1 if either is out of date

The listings are the source of truth; the README is a rendering of them, so it
is never edited by hand. Prose belongs in HEADER below.
"""

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).parent
BADGES_DIR = ROOT / "assets" / "badges"

HEADER = """# Awesome Dutch AI Extensions

> MCP servers, skills, and plugins that connect an AI assistant to, or give it working knowledge of, a Dutch service, data source, standard, or authority.

To add an integration, see [CONTRIBUTING.md](CONTRIBUTING.md). Only ever edit the JSON in `data/` — one file per listing in [`data/listings/`](data/listings), described in [`schema.json`](schema.json). The list below is generated from it by `build-readme.py`.

_Every listing is tagged with its type and origin; a status badge appears only when it is **not** live (beta, preview, concept, abandoned). The type is the unit you install — where that unit bundles skills, commands, agents, or MCP servers, they are named under its description._
"""

# A row is one install unit, so a plugin bundling twelve skills is still one row —
# which would bury every name inside it. Render the contents as a <details> in the
# Description cell: GitHub allows the element inside a table cell, so the names are
# findable with Ctrl-F and the table keeps its four columns.
BUNDLE_KINDS = (
    ("skills", "skill", "skills", "Skills"),
    ("commands", "command", "commands", "Commands"),
    ("agents", "agent", "agents", "Agents"),
    ("mcp_servers", "MCP server", "MCP servers", "MCP servers"),
)

# Every field the catalogue reads. schema.json is the real contract, but nothing in
# this repo enforces it, so name the offending file rather than dying on a KeyError.
REQUIRED_FIELDS = (
    "name", "category", "description_en", "subject", "type", "bundles", "origin", "status", "source_url",
)


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


# --- badges -----------------------------------------------------------------
#
# Tags render as shields-style flat "strip" SVGs generated into assets/badges
# and committed, so the README makes zero external image requests (shields.io
# outages left every badge broken via GitHub's camo proxy). One SVG is emitted
# per tag COMBINATION, not per tag: browsers may wrap between separate <img>s in
# a table cell (even across &nbsp;), stacking the badges into a ragged column on
# GitHub — a single strip image cannot wrap.

FALLBACK_COLOR = "6a737d"
PILL_GAP = 4

# Per-character Verdana 11px advance widths. textLength pins each label to its
# computed width so rendering is identical regardless of installed fonts — but
# that only looks right if the computed width matches the text's natural width,
# so use real per-character metrics, not a flat average. Unknown glyphs fall
# back to 7px; keep tag text ASCII-alphabetic so nothing silently mis-sizes.
CHAR_WIDTHS = {
    "A": 7.5, "B": 7.5, "C": 7.6, "D": 8.4, "E": 6.9, "F": 6.3, "G": 8.4, "H": 8.2, "I": 4.6,
    "J": 5.0, "K": 7.5, "L": 6.1, "M": 9.4, "N": 8.2, "O": 8.7, "P": 7.0, "Q": 8.7, "R": 7.7,
    "S": 7.5, "T": 6.8, "U": 8.0, "V": 7.5, "W": 10.9, "X": 7.5, "Y": 6.8, "Z": 7.5,
    "a": 6.7, "b": 6.9, "c": 5.9, "d": 6.9, "e": 6.6, "f": 3.9, "g": 6.9, "h": 6.9, "i": 3.0,
    "j": 3.9, "k": 6.5, "l": 3.0, "m": 10.6, "n": 6.9, "o": 6.7, "p": 6.9, "q": 6.9, "r": 4.8,
    "s": 5.9, "t": 4.3, "u": 6.9, "v": 6.5, "w": 9.0, "x": 6.5, "y": 6.5, "z": 5.9,
    " ": 3.9, ".": 3.9, "-": 4.9,
}


def measure(text):
    return sum(CHAR_WIDTHS.get(ch, 7) for ch in text)


def esc(s):
    """SVG escaping — covers element content and the quoted aria-label attribute."""
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def strip_svg(parts):
    """Render a row of coloured pills into one strip SVG. Returns (svg, width)."""
    pills, x = [], 0
    for text, color in parts:
        text_width = math.floor(measure(text) + 0.5)
        width = text_width + 12
        pills.append((esc(text), color, x, width, text_width))
        x += width + PILL_GAP
    total = x - PILL_GAP
    label = esc(" · ".join(text for text, _ in parts))
    body = "".join(
        f'<clipPath id="r{i}"><rect x="{px}" width="{w}" height="20" rx="3"/></clipPath>'
        f'<g clip-path="url(#r{i})"><rect x="{px}" width="{w}" height="20" fill="#{color}"/>'
        f'<rect x="{px}" width="{w}" height="20" fill="url(#s)"/></g>'
        f'<g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif"'
        f' text-rendering="geometricPrecision" font-size="110">'
        f'<text aria-hidden="true" x="{fmt(px + w / 2)}" y="150" fill="#010101" fill-opacity=".3"'
        f' transform="scale(.1)" textLength="{tw * 10}">{text}</text>'
        f'<text x="{fmt(px + w / 2)}" y="140" transform="scale(.1)" textLength="{tw * 10}">{text}</text>'
        f"</g>"
        for i, (text, color, px, w, tw) in enumerate(pills)
    )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{total}" height="20" role="img"'
        f' aria-label="{label}">'
        f"<title>{label}</title>"
        f'<linearGradient id="s" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/>'
        f'<stop offset="1" stop-opacity=".1"/></linearGradient>'
        f"{body}</svg>\n"
    )
    return svg, total


def fmt(n):
    """Serialize a coordinate the way JS does — no trailing .0 on whole numbers."""
    scaled = n * 10
    return str(int(scaled)) if scaled == int(scaled) else str(scaled)


class Badges:
    """Collects the tag combinations the catalogue used, then reconciles the directory."""

    def __init__(self, labels):
        self.labels = labels
        self.needed = {}

    def tag_badge(self, listing):
        """Type and origin always; a status pill only when the listing is not live."""
        tokens = [("type", listing["type"]), ("origin", listing["origin"])]
        if listing["status"] != "live":
            tokens.append(("status", listing["status"]))
        parts = [
            (
                self.labels.get(group, {}).get(token, {}).get("en", token),
                self.labels.get(group, {}).get(token, {}).get("color", FALLBACK_COLOR),
            )
            for group, token in tokens
        ]
        file = "tags-" + "-".join(token for _, token in tokens) + ".svg"
        svg, width = strip_svg(parts)
        self.needed[file] = svg
        alt = " · ".join(text for text, _ in parts)
        return f"![{alt}](assets/badges/{file})", width

    def sync(self, check):
        """Write the needed strips and drop orphans. In check mode, touch nothing
        and return the missing/stale/orphaned files instead."""
        existing = sorted(p.name for p in BADGES_DIR.glob("*.svg")) if BADGES_DIR.exists() else []
        if check:
            stale = [
                file
                for file, svg in self.needed.items()
                if not (BADGES_DIR / file).exists() or (BADGES_DIR / file).read_text(encoding="utf-8") != svg
            ]
            return stale + [f"{f} (orphan)" for f in existing if f not in self.needed]
        BADGES_DIR.mkdir(parents=True, exist_ok=True)
        for file, svg in self.needed.items():
            (BADGES_DIR / file).write_text(svg, encoding="utf-8")
        for file in existing:
            if file not in self.needed:
                (BADGES_DIR / file).unlink()
        return []


# --- catalogue --------------------------------------------------------------


def escape_cell(s):
    """Table cells are pipe-delimited and the Name cell is wrapped in a [text](url)
    link — escape backslashes, pipes, and link brackets, and collapse newlines."""
    out = str(s).replace("\\", "\\\\").replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")
    return " ".join(out.splitlines())


def count_phrase(one, many, n):
    return f"{n} {one if n == 1 else many}"


def list_phrase(parts):
    """"a", "a and b", "a, b, and c"."""
    if len(parts) <= 1:
        return parts[0] if parts else ""
    if len(parts) == 2:
        return " and ".join(parts)
    return ", ".join(parts[:-1]) + ", and " + parts[-1]


def bundle_details(bundles):
    present = [k for k in BUNDLE_KINDS if bundles.get(k[0])]
    if not present:
        return ""
    summary = " · ".join(count_phrase(one, many, len(bundles[key])) for key, one, many, _ in present)
    # Bundled names are slugs, but a cell is pipe-delimited — never trust that,
    # and escape_cell covers backslashes and link brackets on the same pass.
    body = "<br>".join(
        f"<b>{label}</b> " + " · ".join(escape_cell(n) for n in bundles[key]) for key, _, _, label in present
    )
    return f" <details><summary>Bundles {summary}</summary>{body}</details>"


def tags_header(max_strip_width):
    """GitHub's auto table layout lets the description column starve the Tags
    column, and its img { max-width: 100% } then scales the strip down. Header
    text can't shrink, so pad the Tags header with &nbsp; until it is at least
    as wide as the table's widest strip (~4px per nbsp, "Tags" itself ~30px)."""
    pad = max(0, math.ceil((max_strip_width - 30) / 4))
    return f"| Name | Description | Subject | Tags{'&nbsp;' * pad} |"


def anchor(title):
    """GitHub heading anchor: lowercase, drop punctuation, spaces -> hyphens.
    Each space becomes its own hyphen — dropping "&" from "Legal & Compliance"
    leaves two spaces, and GitHub's anchor keeps both as "legal--compliance"."""
    kept = "".join(ch for ch in title.lower() if ch.isalnum() or ch in " _-")
    return kept.strip().replace(" ", "-")


# The index is a scan-first table: each category links to its section, shows how
# many listings it holds, and names the services it covers. The "Covers" cell is
# derived from the listings' subjects — most-listed first, so the biggest names in
# a category surface. Capped by width, not name count: a count cap lets a row of
# long names (Legal & Compliance) balloon to double the width of its neighbours.
COVERS_MAX_CHARS = 60


def short_subject(name):
    """Several subjects carry a disambiguating parenthetical ("NS (Nederlandse
    Spoorwegen)"). It earns its place in the Subject column but overruns a summary
    cell — drop it here."""
    if name.endswith(")") and "(" in name:
        return name[: name.rindex("(")].rstrip()
    return name


def covers_for(listings, subjects):
    freq = {}
    for listing in listings:
        for sid in listing["subject"]:
            name = short_subject(subjects.get(sid, {}).get("name", sid))
            freq[name] = freq.get(name, 0) + 1
    # Ties break on the name, case-insensitively: several subjects are lowercase by
    # brand ("bunq", "e-Boekhouden", "data.overheid.nl"), and a codepoint sort would
    # bury every one of them behind the capitalised names in its tie group.
    ranked = [name for name, _ in sorted(freq.items(), key=lambda kv: (-kv[1], kv[0].lower(), kv[0]))]
    # Greedy fill: take names in rank order while they fit the budget. The top
    # name always goes in, however long, so no cell is ever just "…".
    shown, width = [], 0
    for name in ranked:
        added = (2 if shown else 0) + len(name)
        if shown and width + added > COVERS_MAX_CHARS:
            break
        shown.append(name)
        width += added
    return ", ".join(shown) + (", …" if len(shown) < len(ranked) else "")


def index_table(categories, subjects):
    """The index is short enough to pad into aligned columns, which keeps the raw
    Markdown readable in a diff or an editor. (The listing tables are left ragged:
    their badge and description cells are far too wide for this to pay off.)"""
    headers = ["Category", "Listings", "Covers"]
    aligns = ["left", "right", "left"]
    rows = [
        [
            f"[{title}](#{anchor(title)})",
            str(len(listings)),
            escape_cell(covers_for(listings, subjects)),
        ]
        for title, listings in categories
    ]
    widths = [max([len(headers[i])] + [len(r[i]) for r in rows]) for i in range(3)]
    divider = ["-" * (w - 1) + ":" if a == "right" else "-" * w for w, a in zip(widths, aligns)]

    def pad_row(cells):
        return "| " + " | ".join(
            c.rjust(w) if a == "right" else c.ljust(w) for c, w, a in zip(cells, widths, aligns)
        ) + " |"

    return [pad_row(headers), pad_row(divider), *(pad_row(r) for r in rows)]


def render(check):
    category_titles = load("data/categories.json")
    labels = load("data/labels.json")
    subjects = load("data/subjects.json")
    listings = [load(f"data/listings/{p.name}") for p in sorted((ROOT / "data" / "listings").glob("*.json"))]

    for listing in listings:
        where = listing.get("id", "<listing with no id>")
        if missing := [f for f in REQUIRED_FIELDS if f not in listing]:
            sys.exit(f"{where}: missing required field(s): {', '.join(missing)}")
        if absent := [key for key, *_ in BUNDLE_KINDS if key not in listing["bundles"]]:
            sys.exit(f"{where}: bundles is missing {', '.join(absent)} — write [] when there are none")
        if listing["category"] not in category_titles:
            sys.exit(f"{where}: category {listing['category']!r} is not in data/categories.json")
        for sid in listing["subject"]:
            if sid not in subjects:
                sys.exit(f"{where}: subject {sid!r} is not in data/subjects.json")

    # Order follows the English title rather than the category key, so a reworded
    # title still sorts into the right place in the index.
    categories = sorted(
        (
            (title["en"], sorted((d for d in listings if d["category"] == key), key=lambda d: d["name"].lower()))
            for key, title in category_titles.items()
        ),
        key=lambda c: c[0].lower(),
    )

    badges = Badges(labels)
    out = [HEADER, *index_table(categories, subjects), ""]

    for title, rows in categories:
        out += [f"## {title}", ""]
        if not rows:
            out += ["_No listings yet._", ""]
            continue
        rendered, widths = [], []
        for listing in rows:
            markdown, width = badges.tag_badge(listing)
            widths.append(width)
            cells = [
                f"[{escape_cell(listing['name'])}]({listing['source_url']})",
                escape_cell(listing["description_en"]) + bundle_details(listing["bundles"]),
                escape_cell(" / ".join(subjects.get(s, {}).get("name", s) for s in listing["subject"])),
                markdown,
            ]
            rendered.append("| " + " | ".join(cells) + " |")
        out += [tags_header(max(widths)), "|---|---|---|---|", *rendered, ""]

    # The listing count alone understates the catalogue: most skills reach a user
    # inside a plugin, so a type tally reads as MCP-dominated when the skill count
    # is comparable. Spell the bundled totals out.
    totals = [
        (one, many, sum(len(d["bundles"][key]) for d in listings)) for key, one, many, _ in BUNDLE_KINDS
    ]
    bundled = [count_phrase(one, many, n) for one, many, n in totals if n]
    clause = f", bundling a further {list_phrase(bundled)}" if bundled else ""
    counted = count_phrase("listing", "listings", len(listings))
    across = count_phrase("category", "categories", len(categories))
    out += ["---", "", f"_{counted} across {across}{clause}._"]

    stale = badges.sync(check)
    return "\n".join(out).rstrip("\n") + "\n", len(listings), len(categories), stale


def main():
    check = "--check" in sys.argv
    text, count, category_count, stale = render(check)
    readme = ROOT / "README.md"

    if check:
        if stale:
            sys.exit(f"badge file(s) out of sync with data/: {', '.join(stale)} — run: python3 build-readme.py")
        current = readme.read_text(encoding="utf-8") if readme.exists() else ""
        if current != text:
            sys.exit("README.md is out of date — run: python3 build-readme.py")
        print(f"README.md and assets/badges are up to date ({count} listings).")
        return

    readme.write_text(text, encoding="utf-8")
    badge_count = len(list(BADGES_DIR.glob("*.svg")))
    print(f"Wrote README.md — {count} listings across {category_count} categories, {badge_count} badge strips.")


if __name__ == "__main__":
    main()
