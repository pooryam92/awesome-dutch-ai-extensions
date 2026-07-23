# Awesome Dutch Agent Integrations

> A curated list of MCP servers, skills, and plugins that connect AI assistants to Dutch services, data, and standards.

A curated directory of **Dutch agent-integrations** — MCP servers, skills, and plugins that connect an AI assistant to, or give it working knowledge of, a Dutch service, data source, standard, or authority.

Each listing shows, at a glance, whether it is official, commercial, or community, and how mature it is.

To add an integration, see [CONTRIBUTING.md](CONTRIBUTING.md). Only ever edit the JSON in `/data` — the catalogue below is generated from it by `scripts/generate.mjs`.

<!-- BEGIN CATALOGUE — generated from /data by scripts/generate.mjs. Do not edit between these markers; run `npm run generate`. -->

_Every listing is tagged with its type and origin; a status badge appears only when it is **not** live (beta, preview, concept, abandoned)._

| Category                                    | Listings | Covers                                                        |
| ------------------------------------------- | -------: | ------------------------------------------------------------- |
| [Accounting Finance](#accounting-finance)   |       14 | Exact Online, Moneybird, bunq, e-Boekhouden, Mollie, Nmbrs, … |
| [Consumer Daily Life](#consumer-daily-life) |        7 | Albert Heijn, Picnic, Aldi, Buienradar, DA, …                 |
| [Developer Standards](#developer-standards) |        3 | Developer Overheid API Register, Geonovum, internet.nl        |
| [Ecommerce Logistics](#ecommerce-logistics) |        6 | Marktplaats, bol.com, Postcode.eu, PostNL                     |
| [Government Services](#government-services) |        4 | KVK, RDW, wetten.overheid.nl                                  |
| [Housing Property](#housing-property)       |        4 | Funda, Kadaster, Kamernet, Monumenten                         |
| [Legal Compliance](#legal-compliance)       |       11 | Belastingdienst, wetten.overheid.nl, Rechtspraak.nl           |
| [Mobility Travel](#mobility-travel)         |        6 | NS, OVapi, ANWB, CBS ODiN                                     |
| [Open Data Culture](#open-data-culture)     |       15 | CBS StatLine, KNMI, data.overheid.nl, Gemeente Amsterdam, …   |

## Accounting Finance

| Name | Description | Target | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [bunq Partner MCP](https://github.com/bunq/partner-mcp) | Automate bunq banking through the Partner API — onboarding, KYC, accounts, payments, cards, and compliance. | bunq | ![MCP · Official · Beta](assets/badges/tags-mcp-official-beta.svg) |
| [e-Boekhouden MCP](https://github.com/CodeMill-Solutions/e-boekhouden-mcp) | Read and write e-Boekhouden administration using your own API credentials. | e-Boekhouden | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [Finance MCP](https://financemcp.nl/) | Query Exact Online bookkeeping read-only through a hosted EU MCP endpoint, with more Dutch accounting platforms planned. | Exact Online | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |
| [finance-skills-nl](https://github.com/start2scale/finance-skills-nl) | Draft month-close packages, reconcile the general ledger, and audit Excel models for Dutch SME finance teams, with every output flagged for human sign-off. | Raad voor de Jaarverslaggeving (RJ) | ![Plugin · Community · Beta](assets/badges/tags-plugin-community-beta.svg) |
| [Ledger Botje](https://ledgerbotje.nl/) | Handle Exact Online invoices, orders, inventory, and deliveries through a hosted MCP. | Exact Online | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |
| [Mollie MCP](https://docs.mollie.com/docs/mollie-mcp-server) | Manage the full Mollie stack — payments, customers, invoices, subscriptions, balances, settlements, terminals, and webhooks. | Mollie | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [Moneybird MCP](https://developer.moneybird.com/tools/mcp) | Keep Moneybird bookkeeping up to date — invoices, contacts, and ledger data. | Moneybird | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [moneybird-mcp-server](https://github.com/vanderheijden86/moneybird-mcp-server) | Work with Moneybird contacts, sales invoices, financial accounts, payments, products, projects, and time entries, with custom API requests for the rest. | Moneybird | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [Nmbrs AI Connector](https://www.nmbrs.com/ai-connector) | Run Dutch payroll actions in Nmbrs, with every write gated behind explicit confirmation. | Nmbrs | ![MCP · Official · Beta](assets/badges/tags-mcp-official-beta.svg) |
| [Praat met je Boekhouding](https://praatmetjeboekhouding.nl/en/exact-online-mcp-server) | Query Exact Online bookkeeping across 86 tools — invoicing, BTW/ICP, and reporting — read-only by default. | Exact Online | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |
| [Simplicate MCP](https://developer.simplicate.com/docs/mcp/getting_started/) | Work with Simplicate project, CRM, and invoicing data through a per-domain hosted endpoint. | Simplicate | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [Twinfield MCP](https://github.com/CodeMill-Solutions/twinfield-mcp) | Query and update Twinfield bookkeeping over its SOAP API. | Twinfield | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [WeFact MCP](https://github.com/NickAldewereld/wefact-mcp) | Manage WeFact debtors, invoices, products, and subscriptions. | WeFact | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [Yuki MCP](https://github.com/Dytto-ai/yuki-mcp) | Operate Yuki accounting across 102 actions, with write operations gated for safety. | Yuki | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

## Consumer Daily Life

| Name | Description | Target | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [ah-mcp](https://github.com/mrserzhan/ah-mcp) | Browse Albert Heijn products and Bonus deals, and manage your cart, orders, lists, and receipts. | Albert Heijn | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [buienradar-mcp-server](https://github.com/wpnbos/buienradar-mcp-server) | Pull a Buienradar rain nowcast — a 2-hour precipitation forecast by coordinates. | Buienradar | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [homewizard-mcp-server](https://github.com/mrksmts/homewizard-mcp-server) | Read live HomeWizard P1 smart-meter data — power, per-phase voltages and currents, cumulative kWh, and gas — over the local API, read-only. | HomeWizard | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [mcp-picnic](https://github.com/ivo-toby/mcp-picnic) | Shop Picnic groceries — search products and manage the cart, orders, and deliveries. | Picnic | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [nl-supermarkt-mcp](https://github.com/Samvox1/nl-supermarkt-mcp) | Search products, compare prices, and plan groceries across Dutch supermarkets and drugstores. | Albert Heijn / Jumbo / Lidl / Aldi / Plus / DekaMarkt / Dirk / Vomar / Hoogvliet / Spar / Picnic / Poiesz / Kruidvat / Etos / Trekpleister / DA / Holland & Barrett / Douglas / De Online Drogist | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [orderfood](https://github.com/henkas/orderfood) | Search Thuisbezorgd.nl restaurants, read menus, and build a cart — placing the order is not supported, because checkout needs a browser payment flow. | Thuisbezorgd.nl | ![MCP · Community · Beta](assets/badges/tags-mcp-community-beta.svg) |
| [unofficial-magister-mcp](https://github.com/israelroldan/unofficial-magister-mcp) | Look up Dutch school schedules from Magister — daily and weekly timetables plus drop-off and pick-up times, for student and parent accounts. | Magister | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

## Developer Standards

| Name | Description | Target | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [mcp-developer-overheid-api-register](https://github.com/dstotijn/mcp-developer-overheid-api-register) | Search the Developer Overheid API Register for Dutch government APIs and their source repositories. | Developer Overheid API Register | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [skills-geo](https://github.com/developer-overheid-nl/skills-geo) | Skills for Geonovum geo-standards — OGC API, NEN 3610, INSPIRE, and 3D geo-information. | Geonovum | ![Plugin · Official](assets/badges/tags-plugin-official.svg) |
| [skills-internet](https://github.com/developer-overheid-nl/skills-internet) | Skills for internet.nl standards — IPv6, DNSSEC, TLS, DMARC/DKIM/SPF, and DANE. | internet.nl | ![Plugin · Official](assets/badges/tags-plugin-official.svg) |

## Ecommerce Logistics

| Name | Description | Target | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [bol-mcp](https://github.com/BartWaardenburg/bol-mcp) | Reach bol.com's Retailer API through 76 tools spanning orders, offers, and product listings. | bol.com | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [marktplaats-2dehands-mcp](https://github.com/gjoris/marktplaats-2dehands-mcp) | Search Marktplaats and 2dehands listings, categories, and sellers, with saved searches that return only what is new; an optional login adds your own messages, ads, favourites, and bids. | Marktplaats | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [marktplaats-mcp](https://github.com/PonClick/marktplaats-mcp) | Search and read listings from Marktplaats.nl. | Marktplaats | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [marktplaats-mcp (jasp-nerd)](https://github.com/jasp-nerd/marktplaats-mcp) | Search Marktplaats and 2dehands classifieds with seller-trust signals and new-listing monitoring, no account needed. | Marktplaats | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [postcode-eu-ai-tools](https://github.com/postcode-nl/postcode-eu-ai-tools-python) | Validate and autocomplete Dutch addresses through the official Postcode.eu API. | Postcode.eu | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [PostNL MCP](https://github.com/BartWaardenburg/postnl-mcp) | Create shipments and track PostNL parcels, barcodes, and pickup-point locations. | PostNL | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

## Government Services

| Name | Description | Target | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [kvk-connect (MinBZK)](https://github.com/MinBZK/kvk-connect) | Query and track KVK Handelsregister company data — profiles, history, search, and change notifications — from a self-hosted store you run with your own KVK API key. | KVK | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [kvk-mcp](https://github.com/BartWaardenburg/kvk-mcp) | Query the KVK Handelsregister for Dutch company profiles and search, across 10 tools. | KVK | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [poc-machine-law](https://github.com/MinBZK/poc-machine-law) | Query Dutch legislation and check benefits eligibility through the RegelRecht machine-law server. | wetten.overheid.nl | ![MCP · Official · Beta](assets/badges/tags-mcp-official-beta.svg) |
| [rdw-mcp](https://github.com/rantuma/rdw-mcp) | Query RDW vehicle-registration and open data — keyless, no credentials needed. | RDW | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

## Housing Property

| Name | Description | Target | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [kadaster-mcp](https://github.com/jolietjakeblues/kadaster-mcp) | Query the Kadaster Knowledge Graph of Dutch land-registry and parcel data. | Kadaster | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [kamernet-mcp](https://github.com/jasp-nerd/kamernet-mcp) | Search Kamernet rooms, studios, and apartments, read full bilingual listings, and monitor new ones against your budget. | Kamernet | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [makelaar-mcp](https://github.com/spyrosavl/makelaar-mcp) | Search Funda listings and run NHG, NIBUD, mortgage, and closing-cost calculations. | Funda | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [mcp-monumenten](https://github.com/woonstadrotterdam/mcp-monumenten) | Look up a Dutch building's monument status from BAG, RCE, and municipal records. | Monumenten | ![MCP · Official](assets/badges/tags-mcp-official.svg) |

## Legal Compliance

| Name | Description | Target | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [aangifte-ib-skill](https://github.com/mischacoster/aangifte-ib-skill) | A skill that prepares a sourced Dutch personal income-tax return with an adaptive interview and review dossier. | Belastingdienst | ![Skill · Community](assets/badges/tags-skill-community.svg) |
| [Belastingzaken skills](https://github.com/johnhout/knowledge-work-belastingzaken) | Eight commands and eight skills for Dutch income tax, BTW, VPB, payroll tax, deductions, and objections — no filing, professional review required. | Belastingdienst | ![Plugin · Community](assets/badges/tags-plugin-community.svg) |
| [dutch-finance-planner-skill](https://github.com/jonnekleijer/dutch-finance-planner-skill) | Coach personal finances for the Netherlands through a guided interview — box 1/2/3, toeslagen, AOW/pension, mortgage/HRA, the 30% ruling, and gift/inheritance tax. | Belastingdienst | ![Skill · Community](assets/badges/tags-skill-community.svg) |
| [FALCON / nl-ai-lawyer](https://github.com/FutureAtoms/FALCON-futureatoms-legal-counsel-of-netherlands) | Advise on Dutch law — employment/CAO, AVG, tax, real estate, and immigration — through 14 skills and 7 specialist agents. | wetten.overheid.nl / Rechtspraak.nl | ![Plugin · Community](assets/badges/tags-plugin-community.svg) |
| [IURA (iura-nl)](https://github.com/iura-ai/IURA-Plugins) | Draft and review Dutch legal documents — contracts, NDAs, juridische notities, and conclusie van antwoord — grounded in Dutch jurisprudence via the IURA MCP. | wetten.overheid.nl / Rechtspraak.nl | ![Plugin · Commercial · Preview](assets/badges/tags-plugin-commercial-preview.svg) |
| [nl-eli-mcp](https://github.com/matematicsolutions/nl-eli-mcp) | Retrieve versioned Dutch legislation (BWB) and Rechtspraak rulings, keyless. | wetten.overheid.nl / Rechtspraak.nl | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [nl-tax-agent-skills](https://github.com/cyanxxy/nl-tax-agent-skills) | Turn your own tax documents into a source-cited workpack mapped to Mijn Belastingdienst fields for the income-tax return and voorlopige aanslag — you still enter the figures yourself. | Belastingdienst | ![Plugin · Community](assets/badges/tags-plugin-community.svg) |
| [OpenAccountants Plugin](https://github.com/openaccountants/openaccountants) | Classify transactions and apply Dutch tax guidance — VAT, income tax, payroll, and zzp deductions — sourced to Wet IB 2001; the Dutch package is not yet accountant-signed off. | Belastingdienst | ![Plugin · Community](assets/badges/tags-plugin-community.svg) |
| [rechtspraak-mcp](https://github.com/Prudai/rechtspraak-mcp) | Search Rechtspraak open data and resolve legal citations through LiDO, across six tools. | Rechtspraak.nl | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [Wetsanalyse AI](https://github.com/palmw01/wetsanalyse-ai) | Produce source-traceable analyses of Dutch legislation with the JAS method and formalise them into Belastingdienst RegelSpraak, through a skill plus a bundled wettenbank MCP with human-review checkpoints. | wetten.overheid.nl / Belastingdienst | ![Plugin · Community](assets/badges/tags-plugin-community.svg) |
| [wetten-overheid-tools](https://github.com/palmw01/wetten-overheid-tools) | Search Dutch legislation on wetten.overheid.nl and retrieve its structure, articles, and terms. | wetten.overheid.nl | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

## Mobility Travel

| Name | Description | Target | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [anwb-mcp](https://github.com/BartWaardenburg/anwb-mcp) | Pull ANWB traffic incidents, plan routes with turn-by-turn directions, and search locations. | ANWB | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [NS MCP Server](https://github.com/r-huijts/ns-mcp-server) | Look up NS train departures and disruptions and plan train journeys. | NS (Nederlandse Spoorwegen) | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [ns-travel-mcp](https://github.com/lauragift21/ns-travel-mcp) | Plan NS journeys and check real-time train data and disruption alerts. | NS (Nederlandse Spoorwegen) | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [ov-mcp](https://github.com/laulauland/ov-mcp) | Search Dutch public-transport stops, find stops near a coordinate, and look up routes across every operator from the national GTFS feed, without an API key. | OVapi | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [ovapi-mcp-server](https://github.com/henrrrik/ovapi-mcp-server) | Look up Dutch bus, tram, metro, and ferry departures from the OVapi real-time feed — search stops, find stops nearby, and inspect lines and journeys. | OVapi | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [SB OGC MCP](https://github.com/Studio-Bereikbaar/sb-ogc-mcp) | Query Dutch mobility data through Studio Bereikbaar's OGC API — the CBS ODiN travel survey, national traffic-model networks, administrative boundaries, and accessibility maps. | CBS ODiN | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |

## Open Data Culture

| Name | Description | Target | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [baarn-raadsinformatie](https://github.com/tiemenrtuinstra/baarn-raadsinformatie) | Search Gemeente Baarn council meetings, agendas, and documents via the Notubiz API, with keyword and semantic search. | Gemeente Baarn | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [data-cleaning-dutch](https://github.com/linksmith/data-cleaning-dutch) | Clean Dutch government CSV and Excel exports in pandas — semicolon separators with comma decimals, encoding detection, Dutch missing-value markers, day-first dates, postcode validation, and merged cells. | CBS StatLine / Kadaster | ![Skill · Community](assets/badges/tags-skill-community.svg) |
| [dutch-choropleth-maps](https://github.com/linksmith/dutch-choropleth-maps) | Build choropleth maps of Dutch regions — detect gemeente, wijk, or buurt level from CBS region codes, fetch PDOK boundaries, reproject from RD to WGS84, and render with geopandas, Folium, or Plotly. | PDOK / CBS StatLine | ![Skill · Community](assets/badges/tags-skill-community.svg) |
| [knmi-mcp](https://github.com/wolkwork/knmi-mcp) | Pull KNMI real-time weather observations (10-minute measurements) for Dutch locations. | KNMI | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [knmi-mcp (dstotijn)](https://github.com/dstotijn/knmi-mcp) | Query KNMI weather observations and forecasts through KNMI's open data API. | KNMI | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [mcp-cbs-cijfers-open-data](https://github.com/dstotijn/mcp-cbs-cijfers-open-data) | Makes official Dutch statistics from CBS (StatLine) accessible for AI assistants. | CBS StatLine | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [mcp-gemeente-amsterdam](https://github.com/aronmartin/mcp-gemeente-amsterdam) | Query Amsterdam's open APIs across buildings, WOZ, parking, waste, monuments, permits, soil, and more from one server. | Gemeente Amsterdam | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [nl-gov-mcp](https://github.com/WAINUTAI/nl-gov-mcp) | Reach 39 Dutch government data sources through one server — CBS, RDW, KNMI, PDOK, Rechtspraak, DUO, and more. | CBS StatLine / RDW / KNMI / Rechtspraak.nl | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [nl-opendata-mcp](https://github.com/soulnai/nl-opendata-mcp) | Search, query, download, and locally analyse CBS (OData) and data.overheid.nl datasets in CSV or Parquet. | CBS StatLine / data.overheid.nl | ![MCP · Community · Beta](assets/badges/tags-mcp-community-beta.svg) |
| [oorlogsbronnen-mcp](https://github.com/r-huijts/oorlogsbronnen-mcp) | Search Oorlogsbronnen's archive of 12 million Dutch WWII sources. | Oorlogsbronnen | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [open-utrecht-datasets](https://github.com/Terminal-WOO/open-utrecht-datasets) | Search, explore, and download Municipality of Utrecht open datasets across six tools, with experimental Woo-relevance tagging (full Woo-document search is planned). | Gemeente Utrecht | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [openarchieven-mcp](https://github.com/coret/openarchieven-mcp-server) | Search Open Archieven genealogy records through a no-auth hosted endpoint. | Open Archieven | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [OpenTK MCP](https://github.com/r-huijts/opentk-mcp) | Query Tweede Kamer (Dutch parliament) debates, motions, and documents. | Tweede Kamer | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [rce-cho-mcp](https://github.com/jolietjakeblues/rce-cho-mcp) | Query the RCE Cultuurhistorische Objecten linked-data set over SPARQL, with ontology inspection, thesaurus label lookup, and query validation. | Rijksdienst voor het Cultureel Erfgoed (RCE) | ![MCP · Community · Beta](assets/badges/tags-mcp-community-beta.svg) |
| [Rijksmuseum MCP](https://github.com/r-huijts/rijksmuseum-mcp) | Search and browse the Rijksmuseum's art collection by artist, work, and theme. | Rijksmuseum | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

---

_Curated — 70 listing(s) across 9 categories._

<!-- END CATALOGUE -->
