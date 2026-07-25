#!/usr/bin/env node
// generate.mjs — orchestrates catalogue generation from /data into README.md.
// Reads the data + registries, renders the catalogue block and its badge files
// (lib/catalogue.mjs, lib/badges.mjs), then splices the block between the
// CATALOGUE markers (lib/readme.mjs). ONLY that region is generated; the
// surrounding prose is hand-authored and left untouched.
//   node scripts/generate.mjs           rewrites the block in README.md
//   node scripts/generate.mjs --check    exits non-zero if anything is out of sync (CI)

import { readFileSync, writeFileSync, readdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { createBadges } from "./lib/badges.mjs";
import { buildCatalogue } from "./lib/catalogue.mjs";
import { spliceCatalogue } from "./lib/readme.mjs";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const dataDir = join(root, "data");
const readmePath = join(root, "README.md");
const badgesDir = join(root, "assets", "badges");
const check = process.argv.includes("--check");

const readJson = (p) => JSON.parse(readFileSync(p, "utf8"));
const labels = readJson(join(dataDir, "labels.json"));
const targets = readJson(join(dataDir, "targets.json"));

// labels.json and targets.json are registries, not listing files —
// everything else in /data is a category of listings.
const REGISTRY_FILES = new Set(["labels.json", "targets.json"]);
// Each category file carries its own bilingual title, so a title can be reworded
// without renaming the file — the filename is only a stable slug. Order follows
// the English title rather than the filename, so a reworded title still sorts
// into the right place in the index.
const categories = readdirSync(dataDir)
  .filter((f) => f.endsWith(".json") && !REGISTRY_FILES.has(f))
  .map((file) => {
    const { title, listings } = readJson(join(dataDir, file));
    if (!title?.en || !Array.isArray(listings)) {
      console.error(`✖ ${file}: expected { title: { en, nl }, listings: [...] }. Run \`npm run validate\` for details.`);
      process.exit(1);
    }
    return { title: title.en, listings };
  })
  .sort((a, b) => a.title.localeCompare(b.title));

const badges = createBadges(labels, badgesDir);
const { block, count } = buildCatalogue(categories, { targets, badges });

const readme = readFileSync(readmePath, "utf8");
let rendered;
try {
  rendered = spliceCatalogue(readme, block);
} catch (err) {
  console.error(`✖ ${err.message}`);
  process.exit(1);
}

// Badge files are populated during buildCatalogue; reconcile them last.
const staleBadges = badges.sync(check);

if (check) {
  if (staleBadges.length) {
    console.error(`✖ badge file(s) out of sync with labels.json: ${staleBadges.join(", ")}. Run \`npm run generate\` and commit.`);
    process.exit(1);
  }
  if (readme !== rendered) {
    console.error("✖ README.md catalogue is out of sync with /data. Run `npm run generate` and commit.");
    process.exit(1);
  }
  console.log("✓ README.md catalogue and badge files are in sync with /data.");
} else {
  writeFileSync(readmePath, rendered);
  console.log(`✓ updated README.md catalogue (${count} listing(s)) and assets/badges.`);
}
