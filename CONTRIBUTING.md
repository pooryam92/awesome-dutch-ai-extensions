# Contributing

Two ways to add an integration:

1. **Issue form (recommended)** — open [Add an integration](../../issues/new?template=integration-submission.yml). No JSON knowledge needed.
2. **Pull request** — add one file to `data/listings/` and, if needed, one line to `data/subjects.json`.

## What gets listed

- **Usable outside the publisher's own organisation.** Tooling that only works inside one company or agency — internal deploy platforms, credentials nobody else can obtain — is out of scope, however open the source is.
- **Meaningful Dutch coverage.** A multi-jurisdiction project qualifies on the strength of its Dutch content, not on the Netherlands appearing in a jurisdiction list.
- **Descriptions must match what the project says about itself.** Don't repeat a marketing claim the source contradicts — if the material is unreviewed, unfinished, or read-only, the description says so.
- **Commercial listings need public evidence.** A hosted, closed-source integration qualifies only if its public docs name the actual tools or scope and the service is reachable today. A waitlist, a pricing page, or a marketing site with no tool documentation is not a listing.

## Contains

One row is one installable unit, so a plugin holding eighteen skills is still one row. `contains` names everything that unit gives you, so a reader searching for *NEN 3610* or *box 3* can still find it.

```json
"contains": {
  "skills": ["inkomstenbelasting-boxen", "omzetbelasting-btw"],
  "commands": ["ib-aangifte", "btw-aangifte"],
  "agents": [],
  "mcp_servers": []
}
```

- **All four arrays are required, and at least one carries a name.** Empty means none of that kind — never "we didn't look" — and a listing where all four are empty holds nothing, which the schema refuses.
- **A listing lists itself.** A lone MCP server names its own server under `mcp_servers`, a lone copy-in skill names itself under `skills`. There is no separate field saying what a listing *is*: one kind of thing is that kind, several is a bundle, and the README's first badge is read off exactly that.
- **Use the publisher's names**: the directory holding each `SKILL.md`, the basename of each file in `commands/` and `agents/`, and the keys of the `mcpServers` config. Fall back to the listing's `id` where the publisher ships no name, as a vendor endpoint with no published config key does.
- **Leave out infrastructure.** Shared-resource pseudo-skills (`_shared`) and the publisher's own plumbing — a bundled Grafana or admin-API server is not something the listing offers you.
- **A multi-jurisdiction bundle lists only its Dutch entries.** OpenAccountants ships 781 skills; the eighteen `nl-*`/`netherlands-*` ones are what belong here. This is about jurisdiction-specific *content*, not about connectors: a bundled Slack or Box MCP server is where the user's own documents live, so it stays in even though nothing about it is Dutch.
- **Don't enumerate MCP tools.** `subject` and the description already carry that.

Wetsanalyse AI is the worked example of why one row needs four arrays: two skills and a `wettenbank` server, on a single row that no one word describes.

## Execution

Where the code has to run. This is the one limit a visitor's assistant cannot work around — products that register an MCP server from their own cloud cannot spawn a process on the visitor's machine, so a `local` listing simply does not appear there.

`local` — a process on the visitor's own machine: `npx`, `uvx`, `docker run`, a cloned repo.
`remote` — an HTTPS server the publisher already runs; the visitor pastes a URL.
`both` — the *same* server offered either way.
`none` — nothing executes, such as instructions you copy in.

- **Read it off the source, never off the shape.** A vendor's own documentation page can be local-only and a GitHub repo remote-only, and what a listing contains does not predict it either.
- **Shipping an HTTP transport is not `remote`.** Plenty of repos can be deployed as a server; unless the publisher already runs one at a URL you can paste, the visitor still has to start the process, so it is `local`.
- **A bundle takes its most restrictive part.** Any local-only server in it makes the whole listing `local`, because what a visitor needs to know is whether they can use the whole thing from a cloud-side product.
- **`none` means nothing runs, not that nobody checked.** A listing naming a server under `contains.mcp_servers` may not claim it, and the schema refuses that combination.

## Uses

One row per external party the listing reaches, keyed by registrable domain, each saying whether an account there stands between the visitor and the listing.

```json
"uses": [
  { "domain": "moneybird.nl", "account": true },
  { "domain": "rdw.nl", "account": false }
]
```

- **`false` is worth writing.** About half the catalogue reaches a genuinely open service — RDW, CBS, wetten.nl, KNMI — and an empty array would make that indistinguishable from a listing that reaches nothing at all. Empty is for the listings that really do reach nothing.
- **Write what it calls, not what it is about.** A listing serving its own copy of somebody's data reaches nobody, however famous the collection: `subject` says what it covers, `uses` says who it talks to, and the two are allowed to disagree.
- **One row per domain.** A service gets one row, whatever it costs the listing to reach it; two rows for the same domain contradict each other and `validate.py` rejects them.
- **Registrable domain, never the portal subdomain.** NS issues keys at `apiportal.ns.nl` and the value here is `ns.nl`.
- **The domain the listing actually calls, even when the party has several.** A subdomain reduces to its registrable domain, but a genuinely different domain does not fold into the one that looks tidier: KNMI's app API is `knmi.cloud`, WeFact's API is `mijnwefact.nl`, Moneybird's API and MCP endpoint are both `moneybird.com`, and the official-publications repository is `officiele-overheidspublicaties.nl` even though the search service next to it is `overheid.nl`. Two listings reaching the same organisation through different domains get different rows, and that is the record working: what a visitor's traffic goes to is a fact about the listing, not about the brand. Where the service does run one estate under a country domain, name the one a Dutch visitor deals with: `exactonline.nl`.
- **`account` is about the account, not its price or its form.** A free self-serve developer key and a paid subscription are both `true`; API key and OAuth are both `true`. What a service costs is a fact about the service, not about the listing.
- **`true` only when nothing works without it.** Where a listing reaches one party several ways — an open dataset and a keyed API on the same domain — the row is `false`, because the visitor can install it and get answers. The same domain can be `true` on one listing and `false` on another, and usually should be: `kvk.nl` is a wall for the two listings built on the paid API and free for the one that searches the open register.
- **A host that supplies data is a party; one that supplies a library is not.** A CDN serving a charting script is plumbing and gets no row. Where the data itself comes from somebody's static host, that is a party.
- **Name the services, not the hosting.** Where a third party runs a hosted server in front of someone else's service, the row is the service you have an account with. The host becomes a party of its own only when it asks for something itself — a subscription of its own on top of the service it wraps.

## Status

`live` · `beta` · `preview` — working software, in decreasing order of stability.
`concept` — a proof of concept or unreleased design; not something to depend on.
`abandoned` — no longer maintained, but still listed because it remains useful or is the only option for its subject. Delist rather than mark `abandoned` when it no longer runs at all.

## Layout

```
data/listings/<id>.json   one file per listing, filename = id
data/categories.json      category key -> { en, nl } title
data/subjects.json        subject key -> { name, kind? }
data/labels.json          display names and colours for kind / origin / status
schema.json               the listing schema; every field is required
README.md                 a readable view, generated — never edit by hand
assets/badges/            generated tag strips, one SVG per tag combination
build-readme.py           regenerates README.md and assets/badges from data/
validate.py               checks data/ against schema.json and across files
```

CI validates every pull request, and regenerates `README.md` and `assets/badges/`
after a merge — a PR only has to keep `data/` valid. To check that locally:

```
pip install "jsonschema[format-nongpl]"    # once
python3 validate.py                        # reports every problem in one pass
```

## Rules

- One file per artifact, named after its `id`. Every field in `schema.json` is required — there are no optional fields.
- Everything user-facing carries **both an English and a Dutch string** — `description_en`/`description_nl` per listing, `en`/`nl` per category title. One outcome-first sentence each for descriptions, same register, with product and vendor names left untranslated; Dutch titles use Dutch sentence case. The README renders the English strings today — the Dutch ones are stored for a Dutch surface, so write them even though nothing displays them yet.
- `category` is a key from `data/categories.json`. **The title lives in `categories.json`, not in a filename** — reword a category by editing its title, and no listing has to change. Adding a category means adding one entry there.
- `subject` is an array of keys from `data/subjects.json` — the Dutch service, data source, standard, or authority the integration connects to or covers. Reuse an existing key if it is already listed; add a registry entry (key + display `name`) if it isn't.
- Don't edit `README.md` or `assets/badges/` — CI regenerates both from `data/` after
  a merge. To preview locally, `python3 build-readme.py` (stdlib-only) renders every
  listing into its category table, sorted by name, and writes the badge strip each
  row points at; `--check` reports either being stale without writing. Each row
  comes out as:

  ```
  | [Name](source_url) | description_en <details><summary>Contains 2 skills</summary><b>Skills</b> a · b</details> | Subject | ![Kind · Origin](assets/badges/tags-kind-origin.svg) |
  ```

  The `<details>` opens from the second artifact on: a one-artifact listing names
  itself and the row already carries that name. The badge carries kind and origin
  always — kind derived from `contains`, not stored — and a third pill only when
  `status` is not `live`: `MCP · Community · Beta`. Its text
  and colours come from `data/labels.json`, so renaming or recolouring a label there
  changes every strip on the next run. Badges are self-hosted rather than fetched
  from shields.io, because an outage there broke every image through GitHub's camo
  proxy; one SVG per tag *combination*, since separate `<img>`s wrap inside a table
  cell. Prose outside the tables lives in `HEADER` in the script.

Submissions are reviewed manually. No accounts, no self-service listings.
