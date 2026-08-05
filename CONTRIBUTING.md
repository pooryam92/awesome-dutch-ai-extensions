# Contributing

Two ways to add an integration:

1. **Issue form (recommended)** — open [Add an integration](../../issues/new?template=integration-submission.yml). No JSON knowledge needed.
2. **Pull request** — add one file to `data/listings/` and, if needed, one line to `data/targets.json`.

## What gets listed

- **Usable outside the publisher's own organisation.** Tooling that only works inside one company or agency — internal deploy platforms, credentials nobody else can obtain — is out of scope, however open the source is.
- **Meaningful Dutch coverage.** A multi-jurisdiction project qualifies on the strength of its Dutch content, not on the Netherlands appearing in a jurisdiction list.
- **Descriptions must match what the project says about itself.** Don't repeat a marketing claim the source contradicts — if the material is unreviewed, unfinished, or read-only, the description says so.
- **Commercial listings need public evidence.** A hosted, closed-source integration qualifies only if its public docs name the actual tools or scope and the service is reachable today. A waitlist, a pricing page, or a marketing site with no tool documentation is not a listing.

## Type

Pick by **the outermost unit the publisher ships** — the type answers *how you install this*, never *what it can do*. A plugin row can hold a dozen skills; [Bundles](#bundles) is where they get named. The three tokens are the same words the Claude and Codex ecosystems use:

`mcp` — exposes tools to an agent over the Model Context Protocol, however the publisher markets it ("connector", "app", "AI integration" are all product names for an MCP server).
`skill` — one or more `SKILL.md` files you copy in yourself. No install manifest.
`plugin` — ships an install manifest or marketplace entry (`.claude-plugin/plugin.json`, a Codex plugin), whatever it bundles — a plugin bundling an MCP server is still `plugin`, because the outermost unit wins.

The `skill`/`plugin` line is manifest presence, not size — a plugin may ship a single `SKILL.md` at its root, and a `skill` listing may cover several files.

**Project configuration is not an install manifest.** Skills under `.claude/skills/` next to a project `.mcp.json` are `skill`: that setup works only inside the checkout it lives in, there is nothing to `/plugin install`, and adopting it means copying the skill directories out. Wetsanalyse AI is the worked example — two skills and a `wettenbank` server, named under [Bundles](#bundles), on a `skill` row.

## Bundles

One row is one installable unit, so a plugin holding eighteen skills is still one row. `bundles` names what is inside it, so a reader searching for *NEN 3610* or *box 3* can still find it.

```json
"bundles": {
  "skills": ["inkomstenbelasting-boxen", "omzetbelasting-btw"],
  "commands": ["ib-aangifte", "btw-aangifte"],
  "agents": [],
  "mcp_servers": []
}
```

- **All four arrays are required.** Empty means none of that kind — never "we didn't look".
- **A one-artifact listing bundles nothing.** For a lone MCP server or a single copy-in skill, the row *is* the artifact, so all four stay empty.
- **Use the publisher's names**: the directory holding each `SKILL.md`, the basename of each file in `commands/` and `agents/`, and the keys of the bundled `mcpServers` config.
- **Leave out infrastructure.** Shared-resource pseudo-skills (`_shared`) and the publisher's own plumbing — a bundled Grafana or admin-API server is not something the listing offers you.
- **A multi-jurisdiction bundle lists only its Dutch entries.** OpenAccountants ships 781 skills; the eighteen `nl-*`/`netherlands-*` ones are what belong here.
- **Don't enumerate MCP tools.** `target` and the description already carry that.

`mcp_servers` is what lets a single row say *server **and** skills* — the one thing the `type` token cannot express.

## Status

`live` · `beta` · `preview` — working software, in decreasing order of stability.
`concept` — a proof of concept or unreleased design; not something to depend on.
`abandoned` — no longer maintained, but still listed because it remains useful or is the only option for its target. Delist rather than mark `abandoned` when it no longer runs at all.

## Layout

```
data/listings/<id>.json   one file per listing, filename = id
data/categories.json      category key -> { en, nl } title
data/targets.json         target key -> { name, kind? }
data/labels.json          display names and colours for type / origin / status
schema.json               the listing schema; every field is required
README.md                 a readable view, generated — never edit by hand
build-readme.py           regenerates README.md from data/
```

## Rules

- One file per artifact, named after its `id`. Every field in `schema.json` is required — there are no optional fields.
- Everything user-facing carries **both an English and a Dutch string** — `description_en`/`description_nl` per listing, `en`/`nl` per category title. One outcome-first sentence each for descriptions, same register, with product and vendor names left untranslated; Dutch titles use Dutch sentence case. The README renders the English strings today — the Dutch ones are stored for a Dutch surface, so write them even though nothing displays them yet.
- `category` is a key from `data/categories.json`. **The title lives in `categories.json`, not in a filename** — reword a category by editing its title, and no listing has to change. Adding a category means adding one entry there.
- `target` is an array of keys from `data/targets.json` — the Dutch service, data source, standard, or authority the integration connects to or covers. Reuse an existing key if it is already listed; add a registry entry (key + display `name`) if it isn't.
- Don't edit `README.md`. Run `python3 build-readme.py` and commit the result — it
  renders every listing into the right category, sorted by name, with its tag and
  bundles line. Each row comes out as:

  ```
  - [Name](source_url) — description_en _(Type · Origin)_
    <br>Bundles — skills: a, b · commands: c · agents: d · MCP servers: e
  ```

  The tag carries the same three axes the data does: type and origin always, and
  a third term only when `status` is not `live` — `_(Plugin · Community · Beta)_`.
  The strings come from `data/labels.json`, so renaming a label there renames it
  everywhere. Prose outside the list lives in `HEADER` in the script.

Submissions are reviewed manually. No accounts, no self-service listings.
