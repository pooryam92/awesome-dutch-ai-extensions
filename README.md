# Awesome Dutch AI Extensions

MCP servers, skills, and plugins that connect an AI assistant to a Dutch service, data source, standard, or authority.

The list below is a readable view, built from the data by `build-readme.py` — edit `data/`, not this file. The data is the point: one JSON file per listing in [`data/listings/`](data/listings), described in [`schema.json`](schema.json).

Each entry is tagged with what you install — MCP, Skill, or Plugin — and who publishes it: Official, Commercial, or Community. A maturity tag follows only when the entry is not live. Where an entry bundles skills, commands, agents, or MCP servers, they are named beneath it.

To add an integration, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Accounting Finance

- [Adyen MCP](https://docs.adyen.com/development-resources/mcp-server/) — Take Adyen payments — sessions, payment links, refunds, and cancellations — and manage merchant accounts, terminals, and webhooks, enabling only the tools a use case needs. _(MCP · Official · Preview)_
- [bitvavo-mcp](https://github.com/aderik/bitvavo-mcp) — Inspect a Bitvavo account read-only — balances, portfolio value, trades, deposits, withdrawals, and average-cost P&L; it ships no trading or withdrawal tools. _(MCP · Community)_
- [bunq Partner MCP](https://github.com/bunq/partner-mcp) — Automate bunq banking through the Partner API — onboarding, KYC, accounts, payments, cards, and compliance. _(MCP · Official · Beta)_
- [e-Boekhouden MCP](https://github.com/CodeMill-Solutions/e-boekhouden-mcp) — Read and write e-Boekhouden administration using your own API credentials. _(MCP · Community)_
- [Exact Online AI Connect](https://github.com/iwebdevnl/exact-online-ai-connect) — Query Exact Online administrations and generate aging, P&L, and balance-sheet reports through a hosted MCP, where every write lands as a draft you approve first. _(Plugin · Commercial)_
  <br>Bundles — skills: btw-aangifte-assistent, cashflow-analyse, creditcard-aflettering, debiteurenbeheer, exact-afletter-logica, grootboek-anomalie-detectie, management-informatie, periodeafsluiting, reporting, resultatenrekening-analyse · commands: balans, omzet, openstaande-debiteuren, ouderdomsanalyse · MCP servers: exact-online
- [exact-mcp](https://github.com/lemon-official/exact-mcp) — Read and write Exact Online orders and accounting data with encrypted OAuth tokens, allowlisted OData queries, and per-division rate-limit handling. _(MCP · Community)_
- [Finance MCP](https://financemcp.nl/) — Query Exact Online bookkeeping read-only through a hosted EU MCP endpoint, with more Dutch accounting platforms planned. _(MCP · Commercial)_
- [finance-skills-nl](https://github.com/start2scale/finance-skills-nl) — Draft month-close packages, reconcile the general ledger, and audit Excel models for Dutch SME finance teams, with every output flagged for human sign-off. _(Plugin · Community · Beta)_
  <br>Bundles — skills: ai-readiness-mkb, doorrol-schema, excel-controle, grootboek-aansluiting, maandafsluiting, transitorische-posten, variantie-toelichting, verschillen-traceren, xlsx-author
- [Ledger Botje](https://ledgerbotje.nl/) — Handle Exact Online invoices, orders, inventory, and deliveries through a hosted MCP. _(MCP · Commercial)_
- [Mollie MCP](https://docs.mollie.com/docs/mollie-mcp-server) — Manage the full Mollie stack — payments, customers, invoices, subscriptions, balances, settlements, terminals, and webhooks. _(MCP · Official)_
- [Moneybird MCP](https://developer.moneybird.com/tools/mcp) — Keep Moneybird bookkeeping up to date — invoices, contacts, and ledger data. _(MCP · Official)_
- [moneybird-mcp-server](https://github.com/vanderheijden86/moneybird-mcp-server) — Work with Moneybird contacts, sales invoices, financial accounts, payments, products, projects, and time entries, with custom API requests for the rest. _(MCP · Community)_
- [Nmbrs AI Connector](https://www.nmbrs.com/ai-connector) — Run Dutch payroll actions in Nmbrs, with every write gated behind explicit confirmation. _(MCP · Official · Beta)_
- [Praat met je Boekhouding](https://praatmetjeboekhouding.nl/en/exact-online-mcp-server) — Query Exact Online bookkeeping across 111 tools — invoicing, BTW/ICP, and reporting — read-only by default. _(MCP · Commercial)_
- [rompslomp-mcp](https://github.com/lmolema/rompslomp-mcp) — Manage Rompslomp bookkeeping across 61 tools — invoices, contacts, payments, quotations, journal entries, hours, and rides. _(MCP · Community)_
- [Simplicate MCP](https://developer.simplicate.com/docs/mcp/getting_started/) — Work with Simplicate project, CRM, and invoicing data through a per-domain hosted endpoint. _(MCP · Official)_
- [Twinfield MCP](https://github.com/CodeMill-Solutions/twinfield-mcp) — Query and update Twinfield bookkeeping over its SOAP API. _(MCP · Community)_
- [WeFact MCP](https://github.com/NickAldewereld/wefact-mcp) — Manage WeFact debtors, invoices, products, and subscriptions. _(MCP · Community)_

## Consumer Daily Life

- [ah-mcp](https://github.com/mrserzhan/ah-mcp) — Browse Albert Heijn products and Bonus deals, and manage your cart, orders, lists, and receipts. _(MCP · Community)_
- [buienradar-mcp-server](https://github.com/wpnbos/buienradar-mcp-server) — Pull a Buienradar rain nowcast — a 2-hour precipitation forecast by coordinates. _(MCP · Community)_
- [homewizard-mcp-server](https://github.com/mrksmts/homewizard-mcp-server) — Read live HomeWizard P1 smart-meter data — power, per-phase voltages and currents, cumulative kWh, and gas — over the local API, read-only. _(MCP · Community)_
- [mcp-picnic](https://github.com/ivo-toby/mcp-picnic) — Shop Picnic groceries — search products and manage the cart, orders, and deliveries. _(MCP · Community)_
- [nl-supermarkt-mcp](https://github.com/Samvox1/nl-supermarkt-mcp) — Search products, compare prices, and plan groceries across Dutch supermarkets and drugstores. _(MCP · Community)_
- [orderfood](https://github.com/henkas/orderfood) — Search Thuisbezorgd.nl restaurants, read menus, and build a cart — placing the order is not supported, because checkout needs a browser payment flow. _(MCP · Community · Beta)_
- [unofficial-magister-mcp](https://github.com/israelroldan/unofficial-magister-mcp) — Look up Dutch school schedules from Magister — daily and weekly timetables plus drop-off and pick-up times, for student and parent accounts. _(MCP · Community)_

## Developer Standards

- [mcp-developer-overheid-api-register](https://github.com/dstotijn/mcp-developer-overheid-api-register) — Search the Developer Overheid API Register for Dutch government APIs and their source repositories. _(MCP · Community)_
- [skills-geo](https://github.com/developer-overheid-nl/skills-geo) — Skills for Geonovum geo-standards — OGC API, NEN 3610, INSPIRE, and 3D geo-information. _(Plugin · Community)_
  <br>Bundles — skills: geo, geo-3d, geo-api, geo-inspire, geo-meta, geo-model
- [skills-internet](https://github.com/developer-overheid-nl/skills-internet) — Skills for internet.nl standards — IPv6, DNSSEC, TLS, DMARC/DKIM/SPF, and DANE. _(Plugin · Community)_
  <br>Bundles — skills: inet, inet-api, inet-mail, inet-toolbox, inet-web

## Ecommerce Logistics

- [bol-mcp](https://github.com/BartWaardenburg/bol-mcp) — Reach bol.com's Retailer API through 76 tools spanning orders, offers, and product listings. _(MCP · Community)_
- [marktplaats-2dehands-mcp](https://github.com/gjoris/marktplaats-2dehands-mcp) — Search Marktplaats and 2dehands listings, categories, and sellers, with saved searches that return only what is new; an optional login adds your own messages, ads, favourites, and bids. _(MCP · Community)_
- [marktplaats-mcp](https://github.com/PonClick/marktplaats-mcp) — Search and read listings from Marktplaats.nl. _(MCP · Community)_
- [marktplaats-mcp (jasp-nerd)](https://github.com/jasp-nerd/marktplaats-mcp) — Search Marktplaats and 2dehands classifieds with seller-trust signals and new-listing monitoring, no account needed. _(MCP · Community)_
- [postcode-eu-ai-tools](https://github.com/postcode-nl/postcode-eu-ai-tools-python) — Validate and autocomplete Dutch addresses through the official Postcode.eu API. _(MCP · Official)_
- [PostNL MCP](https://github.com/BartWaardenburg/postnl-mcp) — Create shipments and track PostNL parcels, barcodes, and pickup-point locations. _(MCP · Community)_

## Government Services

- [kvk-connect (MinBZK)](https://github.com/MinBZK/kvk-connect) — Query and track KVK Handelsregister company data — profiles, history, search, and change notifications — from a self-hosted store you run with your own KVK API key. _(MCP · Official)_
- [kvk-mcp](https://github.com/BartWaardenburg/kvk-mcp) — Query the KVK Handelsregister for Dutch company profiles and search, across 10 tools. _(MCP · Community)_
- [poc-machine-law](https://github.com/MinBZK/poc-machine-law) — Query Dutch legislation and check benefits eligibility through the RegelRecht machine-law server. _(MCP · Official · Concept)_
- [rdw-mcp](https://github.com/rantuma/rdw-mcp) — Query RDW vehicle-registration and open data — keyless, no credentials needed. _(MCP · Community)_

## Housing Property

- [kadaster-mcp](https://github.com/jolietjakeblues/kadaster-mcp) — Query the Kadaster Knowledge Graph of Dutch land-registry and parcel data. _(MCP · Community)_
- [kamernet-mcp](https://github.com/jasp-nerd/kamernet-mcp) — Search Kamernet rooms, studios, and apartments, read full bilingual listings, and monitor new ones against your budget. _(MCP · Community)_
- [makelaar-mcp](https://github.com/spyrosavl/makelaar-mcp) — Search Funda listings and run NHG, NIBUD, mortgage, and closing-cost calculations. _(MCP · Community)_
- [mcp-monumenten](https://github.com/woonstadrotterdam/mcp-monumenten) — Look up a Dutch building's monument status from BAG, RCE, and municipal records. _(MCP · Official)_

## Legal Compliance

- [aangifte-ib-skill](https://github.com/mischacoster/aangifte-ib-skill) — A skill that prepares a sourced Dutch personal income-tax return with an adaptive interview and review dossier. _(Skill · Community)_
- [Belastingzaken skills](https://github.com/johnhout/knowledge-work-belastingzaken) — Eight commands and eight skills for Dutch income tax, BTW, VPB, payroll tax, deductions, and objections — no filing, professional review required. _(Plugin · Community)_
  <br>Bundles — skills: aftrekposten-en-regelingen, belasting-intake-en-dossiervorming, bezwaar-en-correspondentie, inkomstenbelasting-boxen, loonheffingen-en-werkkosten, officiele-bronverificatie, omzetbelasting-btw, vennootschapsbelasting-vpb · commands: aftrekcheck, bezwaar-brief, btw-aangifte, ib-aangifte, intake, loonheffingen, tax-calendar, vpb-aangifte
- [dutch-finance-planner-skill](https://github.com/jonnekleijer/dutch-finance-planner-skill) — Coach personal finances for the Netherlands through a guided interview — box 1/2/3, toeslagen, AOW/pension, mortgage/HRA, the 30% ruling, and gift/inheritance tax. _(Plugin · Community)_
  <br>Bundles — skills: financial-planner
- [nl-eli-mcp](https://github.com/matematicsolutions/nl-eli-mcp) — Retrieve versioned Dutch legislation (BWB) and Rechtspraak rulings, keyless. _(MCP · Community)_
- [nl-tax-agent-skills](https://github.com/cyanxxy/nl-tax-agent-skills) — Turn your own tax documents into a source-cited workpack mapped to Mijn Belastingdienst fields for the income-tax return and voorlopige aanslag — you still enter the figures yourself. _(Plugin · Community)_
  <br>Bundles — skills: nl-tax-annual-return, nl-tax-box1-home, nl-tax-box2, nl-tax-box3, nl-tax-evidence-indexer, nl-tax-field-mapper, nl-tax-intake, nl-tax-partner-deductions, nl-tax-provisional-assessment, nl-tax-submit-companion, nl-tax-winst · agents: nl-tax-specialist-reviewer
- [OpenAccountants Plugin](https://github.com/openaccountants/openaccountants) — Classify transactions and apply Dutch tax guidance — VAT, income tax, payroll, and zzp deductions — sourced to Wet IB 2001; the Dutch package is not yet accountant-signed off. _(Plugin · Community)_
  <br>Bundles — skills: netherlands-bookkeeping, netherlands-crypto-tax, netherlands-financial-statements, netherlands-formation, netherlands-payroll, netherlands-references, netherlands-tax-optimization, netherlands-transfer-pricing, netherlands-vat-return, nl-corporate-tax, nl-deductions, nl-freelance-intake, nl-income-tax, nl-individual-return, nl-payroll-tax, nl-return-assembly, nl-tax-objection, nl-zzp-deductions · commands: openaccountants · MCP servers: openaccountants
- [rechtspraak-mcp](https://github.com/Prudai/rechtspraak-mcp) — Search Rechtspraak open data and resolve legal citations through LiDO, across six tools. _(MCP · Community)_
- [Wetsanalyse AI](https://github.com/palmw01/wetsanalyse-ai) — Produce source-traceable analyses of Dutch legislation with the JAS method and formalise them into Belastingdienst RegelSpraak, through a skill plus a bundled wettenbank MCP with human-review checkpoints. _(Skill · Community)_
  <br>Bundles — skills: regelspraak, wetsanalyse · MCP servers: wettenbank
- [wetten-overheid-tools](https://github.com/palmw01/wetten-overheid-tools) — Search Dutch legislation on wetten.overheid.nl and retrieve its structure, articles, and terms. _(MCP · Community)_

## Mobility Travel

- [anwb-mcp](https://github.com/BartWaardenburg/anwb-mcp) — Pull ANWB traffic incidents, plan routes with turn-by-turn directions, and search locations. _(MCP · Community)_
- [NS MCP Server](https://github.com/r-huijts/ns-mcp-server) — Look up NS train departures and disruptions and plan train journeys. _(MCP · Community)_
- [ns-travel-mcp](https://github.com/lauragift21/ns-travel-mcp) — Plan NS journeys and check real-time train data and disruption alerts. _(MCP · Community)_
- [ov-mcp](https://github.com/laulauland/ov-mcp) — Search Dutch public-transport stops, find stops near a coordinate, and look up routes across every operator from the national GTFS feed, without an API key. _(MCP · Community)_
- [ovapi-mcp-server](https://github.com/henrrrik/ovapi-mcp-server) — Look up Dutch bus, tram, metro, and ferry departures from the OVapi real-time feed — search stops, find stops nearby, and inspect lines and journeys. _(MCP · Community)_
- [SB OGC MCP](https://github.com/Studio-Bereikbaar/sb-ogc-mcp) — Query Dutch mobility data through Studio Bereikbaar's OGC API — the CBS ODiN travel survey, national traffic-model networks, administrative boundaries, and accessibility maps. _(MCP · Commercial)_

## Open Data Culture

- [baarn-raadsinformatie](https://github.com/tiemenrtuinstra/baarn-raadsinformatie) — Search Gemeente Baarn council meetings, agendas, and documents via the Notubiz API, with keyword and semantic search. _(MCP · Community)_
- [cbs-statline-skill](https://github.com/linksmith/cbs-statline-skill) — Find CBS StatLine tables, read their metadata, and download and combine them for analysis, with recipes for Dutch housing and energy statistics and warnings for tables being retired. _(Plugin · Community)_
  <br>Bundles — skills: cbs-statline-skill
- [Data Journalist AI Agent Plugin](https://github.com/linksmith/data-journalist-ai-agent-plugin-with-skills) — Research Dutch investigative stories with API patterns for CBS, DUO, KVK, Woogle, and officielebekendmakingen, browser lookups where no API exists, Woo request drafting, and investigation state tracking. _(Plugin · Community · Beta)_
  <br>Bundles — skills: browser-lookup, dutch-sources, story-state, woo-draft · commands: new-investigation, weekly-digest · agents: research-assistant
- [data-analysis-journalism](https://github.com/linksmith/data-analysis-journalism) — Run an eight-step exploratory analysis over a Dutch open dataset and report it as story leads in Dutch — headline finding, key figures, and outliers set against the national average. _(Skill · Community · Beta)_
- [data-cleaning-dutch](https://github.com/linksmith/data-cleaning-dutch) — Clean Dutch government CSV and Excel exports in pandas — semicolon separators with comma decimals, encoding detection, Dutch missing-value markers, day-first dates, postcode validation, and merged cells. _(Skill · Community)_
- [dutch-choropleth-maps](https://github.com/linksmith/dutch-choropleth-maps) — Build choropleth maps of Dutch regions — detect gemeente, wijk, or buurt level from CBS region codes, fetch PDOK boundaries, reproject from RD to WGS84, and render with geopandas, Folium, or Plotly. _(Skill · Community)_
- [knmi-mcp](https://github.com/wolkwork/knmi-mcp) — Pull KNMI real-time weather observations (10-minute measurements) for Dutch locations. _(MCP · Community)_
- [knmi-mcp (dstotijn)](https://github.com/dstotijn/knmi-mcp) — Query KNMI weather observations and forecasts through KNMI's open data API. _(MCP · Community)_
- [mcp-cbs-cijfers-open-data](https://github.com/dstotijn/mcp-cbs-cijfers-open-data) — Makes official Dutch statistics from CBS (StatLine) accessible for AI assistants. _(MCP · Community)_
- [mcp-gemeente-amsterdam](https://github.com/aronmartin/mcp-gemeente-amsterdam) — Query Amsterdam's open APIs across buildings, WOZ, parking, waste, monuments, permits, soil, and more from one server. _(MCP · Community)_
- [nl-gov-mcp](https://github.com/WAINUTAI/nl-gov-mcp) — Reach 39 Dutch government data sources through one server — CBS, RDW, KNMI, PDOK, Rechtspraak, DUO, and more. _(MCP · Community)_
- [nl-opendata-mcp](https://github.com/soulnai/nl-opendata-mcp) — Search, query, download, and locally analyse CBS (OData) and data.overheid.nl datasets in CSV or Parquet. _(MCP · Community · Beta)_
- [oorlogsbronnen-mcp](https://github.com/r-huijts/oorlogsbronnen-mcp) — Search Oorlogsbronnen's archive of 12 million Dutch WWII sources. _(MCP · Community)_
- [open-utrecht-datasets](https://github.com/Terminal-WOO/open-utrecht-datasets) — Search, explore, and download Municipality of Utrecht open datasets across six tools, with experimental Woo-relevance tagging (full Woo-document search is planned). _(MCP · Community)_
- [openarchieven-mcp](https://github.com/coret/openarchieven-mcp-server) — Search Open Archieven genealogy records through a no-auth hosted endpoint. _(MCP · Official)_
- [OpenTK MCP](https://github.com/r-huijts/opentk-mcp) — Query Tweede Kamer (Dutch parliament) debates, motions, and documents. _(MCP · Community)_
- [rce-cho-mcp](https://github.com/jolietjakeblues/rce-cho-mcp) — Query the RCE Cultuurhistorische Objecten linked-data set over SPARQL, with ontology inspection, thesaurus label lookup, and query validation. _(MCP · Community · Beta)_
- [Rijksmuseum MCP](https://github.com/r-huijts/rijksmuseum-mcp) — Search and browse the Rijksmuseum's art collection by artist, work, and theme. _(MCP · Community)_
- [wonen-energie-alternatieve-bronnen](https://github.com/linksmith/wonen-energie-alternatieve-bronnen) — Combine grid-operator gas consumption per postcode with the PDOK/CBS buurtkaart to reach neighbourhood-level housing and energy findings when StatLine falls short, with the uncertainty spelled out. _(Skill · Community · Beta)_
