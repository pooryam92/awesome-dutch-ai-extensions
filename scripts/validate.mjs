#!/usr/bin/env node
// validate.mjs — CI gate
// 1. Validate every /data/<category>.json against schema.json.
// 2. Fail on duplicate `id` across ALL files.
// 3. Fail on any enum token not present in labels.json (dangling token).
// 4. Fail on any target id not present in targets.json (dangling id),
//    and on malformed targets.json entries.
// Exits non-zero on any failure so CI blocks the merge.

import { readFileSync, readdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import Ajv from "ajv/dist/2020.js";
import addFormats from "ajv-formats";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const dataDir = join(root, "data");

const readJson = (p) => JSON.parse(readFileSync(p, "utf8"));

const schema = readJson(join(root, "schema.json"));
const labels = readJson(join(dataDir, "labels.json"));
const targets = readJson(join(dataDir, "targets.json"));

// labels.json and targets.json are registries, not listing files —
// everything else in /data is data.
const REGISTRY_FILES = new Set(["labels.json", "targets.json"]);
const categoryFiles = readdirSync(dataDir)
  .filter((f) => f.endsWith(".json") && !REGISTRY_FILES.has(f))
  .sort();

const ajv = new Ajv({ allErrors: true });
addFormats(ajv);
const validate = ajv.compile(schema);

// Which fields are label-backed enums, and which labels group backs each.
const ENUM_FIELDS = { type: "type", origin: "origin", status: "status" };

const errors = [];
const seenIds = new Map(); // id -> first file that used it

// Registry sanity: every targets.json entry needs a name; kind is optional
// but must be a known value when present.
const TARGET_KINDS = new Set(["provider", "dataset", "standard"]);
for (const [tid, entry] of Object.entries(targets)) {
  if (!entry?.name) errors.push(`targets.json[${tid}]: missing "name"`);
  if (entry?.kind != null && !TARGET_KINDS.has(entry.kind)) {
    errors.push(`targets.json[${tid}]: unknown kind "${entry.kind}"`);
  }
}

for (const file of categoryFiles) {
  const listings = readJson(join(dataDir, file));

  if (!validate(listings)) {
    for (const e of validate.errors) {
      // Surface the listing id alongside the file when the error is on a row,
      // so a per-listing failure points at the offending id, not just its index.
      const idx = Array.isArray(listings)
        ? Number(e.instancePath.match(/^\/(\d+)/)?.[1])
        : NaN;
      const id = Number.isInteger(idx) ? listings[idx]?.id : undefined;
      const where = `${file}${e.instancePath}${id ? ` (${id})` : ""}`;
      errors.push(`${where} ${e.message}`);
    }
  }

  if (!Array.isArray(listings)) continue;

  listings.forEach((row, i) => {
    const where = `${file}[${i}]${row?.id ? ` (${row.id})` : ""}`;

    // Duplicate id across all files.
    if (row?.id != null) {
      if (seenIds.has(row.id)) {
        errors.push(`${where}: duplicate id "${row.id}" (also in ${seenIds.get(row.id)})`);
      } else {
        seenIds.set(row.id, file);
      }
    }

    // Dangling enum tokens: every token must resolve in labels.json.
    for (const [field, group] of Object.entries(ENUM_FIELDS)) {
      const token = row?.[field];
      if (token != null && !(labels[group] && labels[group][token])) {
        errors.push(`${where}: ${field} token "${token}" has no label in labels.json[${group}]`);
      }
    }

    // Dangling target ids: every id must resolve in targets.json.
    if (Array.isArray(row?.target)) {
      for (const tid of row.target) {
        if (!targets[tid]) {
          errors.push(`${where}: target id "${tid}" has no entry in targets.json`);
        }
      }
    }
  });
}

if (errors.length) {
  console.error(`✖ validation failed (${errors.length} problem(s)):`);
  for (const e of errors) console.error(`  - ${e}`);
  process.exit(1);
}

console.log(
  `✓ ${categoryFiles.length} category file(s) valid; ${seenIds.size} unique listing(s), no dangling enum tokens.`
);
