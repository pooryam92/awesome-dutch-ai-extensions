// catalogue.mjs — turns listing data into the Markdown catalogue block.
// Presentation only; the badge renderer and targets registry are injected.

// Table cells are pipe-delimited and the Name cell is wrapped in a [text](url)
// link — escape backslashes, pipes, and link brackets, and collapse newlines.
const escapeCell = (s) =>
  String(s)
    .replace(/\\/g, "\\\\")
    .replace(/\|/g, "\\|")
    .replace(/\[/g, "\\[")
    .replace(/\]/g, "\\]")
    .replace(/\r?\n/g, " ");

const TABLE_DIVIDER = "|---|---|---|---|";

// GitHub's auto table layout lets the description column starve the Tags
// column, and its img { max-width: 100% } then scales the strip down. Header
// text can't shrink, so pad the Tags header with &nbsp; until it is at least
// as wide as the table's widest strip (~4px per nbsp, "Tags" itself ~30px).
const tagsHeader = (maxStripWidth) => {
  const pad = Math.max(0, Math.ceil((maxStripWidth - 30) / 4));
  return `| Name | Description | Target | Tags${"&nbsp;".repeat(pad)} |`;
};

// GitHub heading anchor: lowercase, drop punctuation, spaces -> hyphens.
const anchor = (title) =>
  title
    .toLowerCase()
    .replace(/[^\w\s-]/g, "")
    .trim()
    .replace(/\s+/g, "-");

// The index is a scan-first table: each category links to its section, shows how
// many listings it holds, and names the services it covers. The "Covers" cell is
// derived from the listings' targets — most-listed first, so the biggest names in
// a category surface. Capped by width, not name count: a count cap lets a row of
// long names (Legal Compliance) balloon to double the width of its neighbours.
const COVERS_MAX_CHARS = 60;

// Several targets carry a disambiguating parenthetical ("NS (Nederlandse
// Spoorwegen)", "Energieregulering (ACM/TenneT/RVO/SodM)"). It earns its place in
// the Target column but overruns a summary cell — drop it here.
const shortTarget = (name) => name.replace(/\s*\([^)]*\)$/, "");

const coversFor = (listings, targets) => {
  const freq = new Map();
  for (const r of listings) {
    for (const tid of r.target) {
      const name = shortTarget(targets[tid]?.name ?? tid);
      freq.set(name, (freq.get(name) ?? 0) + 1);
    }
  }
  const ranked = [...freq.entries()]
    .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
    .map(([name]) => name);
  // Greedy fill: take names in rank order while they fit the budget. The top
  // name always goes in, however long, so no cell is ever just "…".
  const shown = [];
  let width = 0;
  for (const name of ranked) {
    const added = (shown.length ? 2 : 0) + name.length; // ", " separator
    if (shown.length && width + added > COVERS_MAX_CHARS) break;
    shown.push(name);
    width += added;
  }
  return shown.join(", ") + (shown.length < ranked.length ? ", …" : "");
};

// The index is short enough to pad into aligned columns, which keeps the raw
// Markdown readable in a diff or an editor. (The listing tables are left ragged:
// their badge and description cells are far too wide for this to pay off.)
// Counts read best right-aligned; the two text columns left. Every header here is
// at least 4 characters, so a padded column is always wide enough for its divider
// ("---" or "--:") without a minimum-width guard.
const padRow = (cells, widths, aligns) =>
  `| ${cells.map((c, i) => (aligns[i] === "right" ? c.padStart(widths[i]) : c.padEnd(widths[i]))).join(" | ")} |`;

const indexTable = (categories, targets) => {
  const columns = [
    { header: "Category", align: "left", cell: (c) => `[${c.title}](#${anchor(c.title)})` },
    { header: "Listings", align: "right", cell: (c) => String(c.listings.length) },
    { header: "Covers", align: "left", cell: (c) => escapeCell(coversFor(c.listings, targets)) },
  ];
  const aligns = columns.map((col) => col.align);
  const rows = categories.map((c) => columns.map((col) => col.cell(c)));
  const widths = columns.map((col, i) =>
    Math.max(col.header.length, ...rows.map((r) => r[i].length)),
  );
  const divider = columns.map((col, i) =>
    col.align === "right" ? "-".repeat(widths[i] - 1) + ":" : "-".repeat(widths[i]),
  );
  return [
    padRow(columns.map((col) => col.header), widths, aligns),
    padRow(divider, widths, aligns),
    ...rows.map((r) => padRow(r, widths, aligns)),
  ];
};

// buildCatalogue(categories, { targets, badges }) -> { block, count }
//   categories: [{ title, listings }] — each rendered as its own table.
//   block:      the Markdown string to splice between the CATALOGUE markers.
//   count:      total listings rendered (for the CLI summary line).
export const buildCatalogue = (categories, { targets, badges }) => {
  const targetNames = (ids) => ids.map((tid) => targets[tid]?.name ?? tid).join(" / ");

  const listingRow = (r) => {
    const tags = badges.tagBadge(r);
    const cells = [
      `[${escapeCell(r.name)}](${r.source_url})`,
      escapeCell(r.description_en),
      escapeCell(targetNames(r.target)),
      tags.markdown,
    ];
    return { row: `| ${cells.join(" | ")} |`, tagWidth: tags.width };
  };

  const block = [
    "_Every listing is tagged with its type and origin; a status badge appears only when it is **not** live (beta, preview, concept, abandoned)._",
    "",
    ...indexTable(categories, targets),
    "",
  ];

  let count = 0;
  for (const { title, listings } of categories) {
    block.push(`## ${title}`, "");
    if (listings.length === 0) {
      block.push("_No listings yet._", "");
      continue;
    }
    const rows = [...listings].sort((a, b) => a.name.localeCompare(b.name)).map(listingRow);
    block.push(tagsHeader(Math.max(...rows.map((r) => r.tagWidth))), TABLE_DIVIDER);
    for (const r of rows) {
      block.push(r.row);
      count++;
    }
    block.push("");
  }
  block.push("---", "");
  block.push(`_Curated — ${count} listing(s) across ${categories.length} categories._`);

  return { block: block.join("\n"), count };
};
