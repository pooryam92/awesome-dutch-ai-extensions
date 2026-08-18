# Awesome Dutch AI Extensions

> MCP servers, skills, and the bundles that carry them — connecting an AI assistant to, or giving it working knowledge of, a Dutch service, data source, standard, or authority.

To add an integration, see [CONTRIBUTING.md](CONTRIBUTING.md). Only ever edit the JSON in `data/` — one file per listing in [`data/listings/`](data/listings), described in [`schema.json`](schema.json). The list below is generated from it by `build-readme.py`.

_Every listing is tagged with what it is and where it came from; a status badge appears only when it is **not** live (beta, preview, concept, abandoned). What it is comes from what it contains — one kind of thing is that kind, several is a bundle — and where a listing holds more than one artifact, they are named under its description._

| Category                      | Listings | Covers                                                     |
| ----------------------------- | -------: | ---------------------------------------------------------- |
| [Accounting](#accounting)     |       19 | Exact Online, Moneybird, Twinfield, WeFact, AFAS Profit, … |
| [Business](#business)         |        5 | KVK, Adyen, internet.nl, Mollie                            |
| [Data](#data)                 |        8 | CBS StatLine, CBS ODiN, Geonovum, Kadaster, PDOK, …        |
| [Education](#education)       |        1 | Magister                                                   |
| [Government](#government)     |        8 | CBS StatLine, data.overheid.nl, DUO, Tweede Kamer, BAG, …  |
| [Groceries](#groceries)       |        7 | Albert Heijn, Jumbo, Plus, Picnic, Aldi, DA, …             |
| [History](#history)           |        6 | Rijksdienst voor het Cultureel Erfgoed, Rijksmuseum, …     |
| [Housing](#housing)           |        6 | PDOK, BAG, CBS StatLine, EP-Online, Funda, HomeWizard, …   |
| [Language](#language)         |        3 | Nederlands, Inburgeringsexamen, Staatsexamen NT2           |
| [Law](#law)                   |        6 | wetten.overheid.nl, Rechtspraak.nl, AVG, Belastingdienst   |
| [Marketplaces](#marketplaces) |        5 | Marktplaats, bol.com, PostNL                               |
| [Money](#money)               |        6 | Belastingdienst, Bitvavo, bunq                             |
| [Travel](#travel)             |        6 | NS, OVapi, ANWB, RDW                                       |
| [Weather](#weather)           |        2 | KNMI                                                       |

## Accounting

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [AFAS AI Connect](https://github.com/iwebdevnl/afas-ai-connect) | Reach an AFAS Profit environment through an AppConnector an administrator enables once, for outstanding items, aging, and result and balance figures, with every booking prepared as a draft you confirm. <details><summary>Contains 4 commands · 1 MCP server</summary><b>Commands</b> afas-balans · afas-omzet · afas-openstaande-debiteuren · afas-ouderdomsanalyse<br><b>MCP servers</b> afas</details> | AFAS Profit | ![Bundle · Commercial](assets/badges/tags-bundle-commercial.svg) |
| [e-Boekhouden MCP](https://github.com/CodeMill-Solutions/e-boekhouden-mcp) | Read and write e-Boekhouden administration using your own API credentials. | e-Boekhouden | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [Exact Online AI Connect](https://github.com/iwebdevnl/exact-online-ai-connect) | Query Exact Online administrations and generate aging, P&L, and balance-sheet reports through a hosted MCP, where every write lands as a draft you approve first. <details><summary>Contains 10 skills · 4 commands · 1 MCP server</summary><b>Skills</b> btw-aangifte-assistent · cashflow-analyse · creditcard-aflettering · debiteurenbeheer · exact-afletter-logica · grootboek-anomalie-detectie · management-informatie · periodeafsluiting · reporting · resultatenrekening-analyse<br><b>Commands</b> exact-balans · exact-omzet · exact-openstaande-debiteuren · exact-ouderdomsanalyse<br><b>MCP servers</b> exact-online</details> | Exact Online | ![Bundle · Commercial](assets/badges/tags-bundle-commercial.svg) |
| [exact-mcp](https://github.com/lemon-official/exact-mcp) | Read and write Exact Online orders and accounting data with encrypted OAuth tokens, allowlisted OData queries, and per-division rate-limit handling. | Exact Online | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [Finance MCP](https://financemcp.nl/) | Query Exact Online bookkeeping read-only through a hosted EU MCP endpoint, with more Dutch accounting platforms planned. | Exact Online | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |
| [finance-skills-nl](https://github.com/start2scale/finance-skills-nl) | Draft month-close packages, reconcile the general ledger, and audit Excel models for Dutch SME finance teams, with every output flagged for human sign-off. <details><summary>Contains 9 skills</summary><b>Skills</b> ai-readiness-mkb · doorrol-schema · excel-controle · grootboek-aansluiting · maandafsluiting · transitorische-posten · variantie-toelichting · verschillen-traceren · xlsx-author</details> | Raad voor de Jaarverslaggeving (RJ) | ![Skill · Community · Beta](assets/badges/tags-skill-community-beta.svg) |
| [Ledger Botje](https://ledgerbotje.nl/) | Handle Exact Online invoices, orders, inventory, and deliveries through a hosted MCP. | Exact Online | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |
| [Moneybird MCP](https://developer.moneybird.com/tools/mcp) | Keep Moneybird bookkeeping up to date — invoices, contacts, and ledger data. | Moneybird | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [moneybird-mcp-server](https://github.com/vanderheijden86/moneybird-mcp-server) | Work with Moneybird contacts, sales invoices, financial accounts, payments, products, projects, and time entries, with custom API requests for the rest. | Moneybird | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [Nmbrs AI Connector](https://www.nmbrs.com/ai-connector) | Run Dutch payroll actions in Nmbrs, with every write gated behind explicit confirmation. | Nmbrs | ![MCP · Official · Beta](assets/badges/tags-mcp-official-beta.svg) |
| [OpenAccountants Plugin](https://github.com/openaccountants/openaccountants) | Classify transactions and apply Dutch tax guidance — VAT, income tax, payroll, and zzp deductions — sourced to Wet IB 2001; the Dutch package is not yet accountant-signed off. <details><summary>Contains 18 skills · 1 command · 1 MCP server</summary><b>Skills</b> netherlands-bookkeeping · netherlands-crypto-tax · netherlands-financial-statements · netherlands-formation · netherlands-payroll · netherlands-references · netherlands-tax-optimization · netherlands-transfer-pricing · netherlands-vat-return · nl-corporate-tax · nl-deductions · nl-freelance-intake · nl-income-tax · nl-individual-return · nl-payroll-tax · nl-return-assembly · nl-tax-objection · nl-zzp-deductions<br><b>Commands</b> openaccountants<br><b>MCP servers</b> openaccountants</details> | Belastingdienst | ![Bundle · Community](assets/badges/tags-bundle-community.svg) |
| [Praat met je Boekhouding](https://praatmetjeboekhouding.nl/en/exact-online-mcp-server) | Query Exact Online bookkeeping across 111 tools — invoicing, BTW/ICP, and reporting — read-only by default. | Exact Online | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |
| [rompslomp-mcp](https://github.com/lmolema/rompslomp-mcp) | Manage Rompslomp bookkeeping across 61 tools — invoices, contacts, payments, quotations, journal entries, hours, and rides. | Rompslomp | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [Simplicate MCP](https://developer.simplicate.com/docs/mcp/getting_started/) | Work with Simplicate project, CRM, and invoicing data through a per-domain hosted endpoint. | Simplicate | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [Twinfield AI Connect](https://github.com/iwebdevnl/twinfield-ai-connect) | Put a Twinfield administration behind your assistant without installing anything, for outstanding items, aging, and result and balance figures, where every booking waits for your confirmation before it posts. <details><summary>Contains 4 commands · 1 MCP server</summary><b>Commands</b> twinfield-balans · twinfield-omzet · twinfield-openstaande-debiteuren · twinfield-ouderdomsanalyse<br><b>MCP servers</b> twinfield</details> | Twinfield | ![Bundle · Commercial](assets/badges/tags-bundle-commercial.svg) |
| [Twinfield MCP](https://github.com/CodeMill-Solutions/twinfield-mcp) | Query and update Twinfield bookkeeping over its SOAP API. | Twinfield | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [WeFact MCP](https://github.com/NickAldewereld/wefact-mcp) | Manage WeFact debtors, invoices, products, and subscriptions. | WeFact | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [wefact-mcp (CodeMill)](https://github.com/CodeMill-Solutions/wefact-mcp) | Work a WeFact administration across all 17 API controllers — invoices, subscriptions, quotes, purchase invoices, bank transactions and CRM — read-only until you enable writes, with a separate opt-in before any tool emails a customer; it installs from a clone, because the npm package its README documents was never published. | WeFact | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [Yuki MCP](https://github.com/CodeMill-Solutions/yuki-mcp) | Book invoices, journal entries and archive documents in Yuki over its SOAP API — it writes as well as reads, and starts from a node path because the package ships no npx entry point. | Yuki | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

## Business

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [Adyen MCP](https://docs.adyen.com/development-resources/mcp-server/) | Take Adyen payments — sessions, payment links, refunds, and cancellations — and manage merchant accounts, terminals, and webhooks, enabling only the tools a use case needs. | Adyen | ![MCP · Official · Preview](assets/badges/tags-mcp-official-preview.svg) |
| [kvk-connect (MinBZK)](https://github.com/MinBZK/kvk-connect) | Query and track KVK Handelsregister company data — profiles, history, search, and change notifications — from a self-hosted store you run with your own KVK API key. | KVK | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [kvk-mcp](https://github.com/BartWaardenburg/kvk-mcp) | Query the KVK Handelsregister for Dutch company profiles and search, across 10 tools. | KVK | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [Mollie MCP](https://docs.mollie.com/docs/mollie-mcp-server) | Manage the full Mollie stack — payments, customers, invoices, subscriptions, balances, settlements, terminals, and webhooks. | Mollie | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [skills-internet](https://github.com/developer-overheid-nl/skills-internet) | Skills for internet.nl standards — IPv6, DNSSEC, TLS, DMARC/DKIM/SPF, and DANE. <details><summary>Contains 5 skills</summary><b>Skills</b> inet · inet-api · inet-mail · inet-toolbox · inet-web</details> | internet.nl | ![Skill · Community](assets/badges/tags-skill-community.svg) |

## Data

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [cbs-statline-skill](https://github.com/linksmith/cbs-statline-skill) | Find CBS StatLine tables, read their metadata, and download and combine them for analysis, with recipes for Dutch housing and energy statistics and warnings for tables being retired. | CBS StatLine | ![Skill · Community](assets/badges/tags-skill-community.svg) |
| [data-analysis-journalism](https://github.com/linksmith/data-analysis-journalism) | Run an eight-step exploratory analysis over a Dutch open dataset and report it as story leads in Dutch — headline finding, key figures, and outliers set against the national average. | CBS StatLine | ![Skill · Community · Beta](assets/badges/tags-skill-community-beta.svg) |
| [data-cleaning-dutch](https://github.com/linksmith/data-cleaning-dutch) | Clean Dutch government CSV and Excel exports in pandas — semicolon separators with comma decimals, encoding detection, Dutch missing-value markers, day-first dates, postcode validation, and merged cells. | CBS StatLine / Kadaster | ![Skill · Community](assets/badges/tags-skill-community.svg) |
| [dutch-choropleth-maps](https://github.com/linksmith/dutch-choropleth-maps) | Build choropleth maps of Dutch regions — detect gemeente, wijk, or buurt level from CBS region codes, fetch PDOK boundaries, reproject from RD to WGS84, and render with geopandas, Folium, or Plotly. | PDOK / CBS StatLine | ![Skill · Community](assets/badges/tags-skill-community.svg) |
| [mcp-cbs-cijfers-open-data](https://github.com/dstotijn/mcp-cbs-cijfers-open-data) | Makes official Dutch statistics from CBS (StatLine) accessible for AI assistants. | CBS StatLine | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [postcode-eu-ai-tools](https://github.com/postcode-nl/postcode-eu-ai-tools-python) | Validate and autocomplete Dutch addresses through the official Postcode.eu API. | Postcode.eu | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [SB OGC MCP](https://github.com/Studio-Bereikbaar/sb-ogc-mcp) | Query Dutch mobility data through Studio Bereikbaar's OGC API — the CBS ODiN travel survey, national traffic-model networks, administrative boundaries, and accessibility maps. | CBS ODiN | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |
| [skills-geo](https://github.com/developer-overheid-nl/skills-geo) | Skills for Geonovum geo-standards — OGC API, NEN 3610, INSPIRE, and 3D geo-information. <details><summary>Contains 6 skills</summary><b>Skills</b> geo · geo-3d · geo-api · geo-inspire · geo-meta · geo-model</details> | Geonovum | ![Skill · Community](assets/badges/tags-skill-community.svg) |

## Education

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [unofficial-magister-mcp](https://github.com/israelroldan/unofficial-magister-mcp) | Look up Dutch school schedules from Magister — daily and weekly timetables plus drop-off and pick-up times, for student and parent accounts. | Magister | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

## Government

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [baarn-raadsinformatie](https://github.com/tiemenrtuinstra/baarn-raadsinformatie) | Search Gemeente Baarn council meetings, agendas, and documents via the Notubiz API, with keyword and semantic search. | Gemeente Baarn | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [Data Journalist AI Agent Plugin](https://github.com/linksmith/data-journalist-ai-agent-plugin-with-skills) | Research Dutch investigative stories with API patterns for CBS, DUO, KVK, Woogle, and officielebekendmakingen, browser lookups where no API exists, Woo request drafting, and investigation state tracking. <details><summary>Contains 4 skills · 2 commands · 1 agent</summary><b>Skills</b> browser-lookup · dutch-sources · story-state · woo-draft<br><b>Commands</b> new-investigation · weekly-digest<br><b>Agents</b> research-assistant</details> | CBS StatLine / DUO (Dienst Uitvoering Onderwijs) / KVK / Woogle / officielebekendmakingen.nl / RVO (Rijksdienst voor Ondernemend Nederland) / NVWA / BIG-register | ![Bundle · Community · Beta](assets/badges/tags-bundle-community-beta.svg) |
| [mcp-developer-overheid-api-register](https://github.com/dstotijn/mcp-developer-overheid-api-register) | Search the developer.overheid.nl API Register for Dutch government APIs and their source repositories. | developer.overheid.nl API Register | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [mcp-gemeente-amsterdam](https://github.com/aronmartin/mcp-gemeente-amsterdam) | Query Amsterdam's open APIs across buildings, WOZ, parking, waste, monuments, permits, soil, and more from one server. | Gemeente Amsterdam | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [nl-gov-mcp](https://github.com/WAINUTAI/nl-gov-mcp) | Reach 39 Dutch government data sources through one server — CBS, RDW, KNMI, PDOK, Rechtspraak, DUO, and more. | CBS StatLine / RDW / KNMI / Rechtspraak.nl / PDOK / Kadaster / Rijksdienst voor het Cultureel Erfgoed (RCE) / wetten.overheid.nl / OVapi / NS (Nederlandse Spoorwegen) / data.overheid.nl / Tweede Kamer / DUO (Dienst Uitvoering Onderwijs) / BAG (Basisregistratie Adressen en Gebouwen) | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [nl-opendata-mcp](https://github.com/soulnai/nl-opendata-mcp) | Search, query, download, and locally analyse CBS (OData) and data.overheid.nl datasets in CSV or Parquet. | CBS StatLine / data.overheid.nl | ![MCP · Community · Beta](assets/badges/tags-mcp-community-beta.svg) |
| [open-utrecht-datasets](https://github.com/Terminal-WOO/open-utrecht-datasets) | Search, explore, and download Municipality of Utrecht open datasets across six tools, with experimental Woo-relevance tagging (full Woo-document search is planned). | Gemeente Utrecht | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [OpenTK MCP](https://github.com/r-huijts/opentk-mcp) | Query Tweede Kamer (Dutch parliament) debates, motions, and documents. | Tweede Kamer | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

## Groceries

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [ah-mcp](https://github.com/mrserzhan/ah-mcp) | Browse Albert Heijn products and Bonus deals, and manage your cart, orders, lists, and receipts. | Albert Heijn | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [Albert Heijn Automation](https://github.com/robinbril/Albert-Heijn-Automation) | Plan meals and fill your Albert Heijn list from your own purchase history — cross the bonus folder with what you actually buy, and read the basket back as an eating pattern. <details><summary>Contains 1 skill · 1 MCP server</summary><b>Skills</b> albert-heijn<br><b>MCP servers</b> ah</details> | Albert Heijn | ![Bundle · Community](assets/badges/tags-bundle-community.svg) |
| [mcp-picnic](https://github.com/ivo-toby/mcp-picnic) | Shop Picnic groceries — search products and manage the cart, orders, and deliveries. | Picnic | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [nl-supermarkt-mcp](https://github.com/Samvox1/nl-supermarkt-mcp) | Search products, compare prices, and plan groceries across Dutch supermarkets and drugstores. | Albert Heijn / Jumbo / Lidl / Aldi / Plus / DekaMarkt / Dirk / Vomar / Hoogvliet / Spar / Picnic / Poiesz / Kruidvat / Etos / Trekpleister / DA / Holland & Barrett / Douglas / De Online Drogist | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [orderfood](https://github.com/henkas/orderfood) | Search Thuisbezorgd.nl restaurants, read menus, and build a cart — placing the order is not supported, because checkout needs a browser payment flow. | Thuisbezorgd.nl | ![MCP · Community · Beta](assets/badges/tags-mcp-community-beta.svg) |
| [Pepesto Agent to Cart](https://www.pepesto.com/agent-to-cart/) | Hand a shopping list from any MCP client to the Pepesto app to fill an Albert Heijn, Jumbo, or Plus cart — the connector returns a deep link to open on your phone, not a priced basket. | Albert Heijn / Jumbo / Plus | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |
| [Pepesto MCP Server](https://github.com/pepesto-solutions/pepesto-mcp) | Turn a recipe URL, text, or photo into a matched Albert Heijn, Jumbo, or Plus basket with live prices — it ends at a checkout link and does not place the order. | Albert Heijn / Jumbo / Plus | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |

## History

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [mcp-monumenten](https://github.com/woonstadrotterdam/mcp-monumenten) | Look up a Dutch building's monument status from BAG, RCE, and municipal records. | Monumenten / Rijksdienst voor het Cultureel Erfgoed (RCE) | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [oorlogsbronnen-mcp](https://github.com/r-huijts/oorlogsbronnen-mcp) | Search Oorlogsbronnen's archive of 12 million Dutch WWII sources. | Oorlogsbronnen | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [openarchieven-mcp](https://github.com/coret/openarchieven-mcp-server) | Search Open Archieven genealogy records through a no-auth hosted endpoint. | Open Archieven | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [rce-cho-mcp](https://github.com/jolietjakeblues/rce-cho-mcp) | Query the RCE Cultuurhistorische Objecten linked-data set over SPARQL, with ontology inspection, thesaurus label lookup, and query validation. | Rijksdienst voor het Cultureel Erfgoed (RCE) | ![MCP · Community · Beta](assets/badges/tags-mcp-community-beta.svg) |
| [Rijksmuseum MCP](https://github.com/r-huijts/rijksmuseum-mcp) | Search and browse the Rijksmuseum's art collection by artist, work, and theme. | Rijksmuseum | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [rijksmuseum-mcp+](https://github.com/kintopp/rijksmuseum-mcp-plus) | Research the Rijksmuseum collection in depth with semantic and Iconclass search, provenance analysis, similarity comparisons and geographic queries — over an enriched copy of the museum's metadata, not its live API. <details><summary>Contains 1 skill · 1 MCP server</summary><b>Skills</b> rijksmuseum-mcp-plus<br><b>MCP servers</b> rijksmuseum-mcp-plus</details> | Rijksmuseum / Iconclass | ![Bundle · Community · Preview](assets/badges/tags-bundle-community-preview.svg) |

## Housing

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [homewizard-mcp-server](https://github.com/mrksmts/homewizard-mcp-server) | Read live HomeWizard P1 smart-meter data — power, per-phase voltages and currents, cumulative kWh, and gas — over the local API, read-only. | HomeWizard | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [kadaster-mcp](https://github.com/jolietjakeblues/kadaster-mcp) | Query the Kadaster Knowledge Graph of Dutch land-registry and parcel data. | Kadaster | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [kamernet-mcp](https://github.com/jasp-nerd/kamernet-mcp) | Search Kamernet rooms, studios, and apartments, read full bilingual listings, and monitor new ones against your budget. | Kamernet | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [makelaar-mcp](https://github.com/spyrosavl/makelaar-mcp) | Search Funda listings and run NHG, NIBUD, mortgage, and closing-cost calculations. | Funda | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [mcp-metadata-demo](https://github.com/DaveGold/mcp-metadata-demo) | Profile a Dutch building from its address by fusing BAG and EP-Online, returning construction era, energy label, and advisory alerts against Bouwbesluit, BENG, and Paris Proof thresholds. | BAG (Basisregistratie Adressen en Gebouwen) / EP-Online / PDOK | ![MCP · Community · Concept](assets/badges/tags-mcp-community-concept.svg) |
| [wonen-energie-alternatieve-bronnen](https://github.com/linksmith/wonen-energie-alternatieve-bronnen) | Combine grid-operator gas consumption per postcode with the PDOK/CBS buurtkaart to reach neighbourhood-level housing and energy findings when StatLine falls short, with the uncertainty spelled out. | Netbeheerdata (Liander / Enexis / Stedin) / PDOK / CBS StatLine | ![Skill · Community · Beta](assets/badges/tags-skill-community-beta.svg) |

## Language

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [Dutch Fluency MCP](https://mcp.dutchfluency.com/) | Practise Dutch with CEFR placement tests, sentence correction, and NT2 and inburgering exam preparation. | Nederlands (taal) / Staatsexamen NT2 / Inburgeringsexamen | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |
| [Dutch Native](https://github.com/brunocous/dutch-native) | Rewrite Dutch text so it reads as native rather than translated, in either Netherlands or Belgian Dutch. | Nederlands (taal) | ![Skill · Community](assets/badges/tags-skill-community.svg) |
| [The Dutch Directory](https://thedutchdirectory.com/mcp) | Compare ways to learn Dutch — schools, universities, tutors, apps, podcasts, and exams — through editorial shortlists, city gaps, and NT2 and inburgering study paths; it maps the market rather than teaching, and flags its own publisher's entries. | Nederlands (taal) / Staatsexamen NT2 / Inburgeringsexamen | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |

## Law

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [ICTRecht Legal GenAI Resources](https://github.com/ICTRecht/Legal-GenAI-Resources) | Summarise and compare contracts against Dutch and EU law — DPAs, NDAs, and copyright transfers — with prompts and templates validated by an IT-law firm. <details><summary>Contains 2 skills · 3 commands · 5 MCP servers</summary><b>Skills</b> samenvatten · vergelijken<br><b>Commands</b> DPA · NDA · overdracht auteursrecht<br><b>MCP servers</b> atlassian · box · egnyte · ms365 · slack</details> | AVG (Algemene verordening gegevensbescherming) | ![Bundle · Commercial · Preview](assets/badges/tags-bundle-commercial-preview.svg) |
| [nl-eli-mcp](https://github.com/matematicsolutions/nl-eli-mcp) | Retrieve versioned Dutch legislation (BWB) and Rechtspraak rulings, keyless. | wetten.overheid.nl / Rechtspraak.nl | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [poc-machine-law](https://github.com/MinBZK/poc-machine-law) | Query Dutch legislation and check benefits eligibility through the RegelRecht machine-law server. | wetten.overheid.nl | ![MCP · Official · Concept](assets/badges/tags-mcp-official-concept.svg) |
| [rechtspraak-mcp](https://github.com/Prudai/rechtspraak-mcp) | Search Rechtspraak open data and resolve legal citations through LiDO, across six tools. | Rechtspraak.nl | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [Wetsanalyse AI](https://github.com/palmw01/wetsanalyse-ai) | Produce source-traceable analyses of Dutch legislation with the JAS method and formalise them into Belastingdienst RegelSpraak, through a skill plus a bundled wettenbank MCP with human-review checkpoints. <details><summary>Contains 2 skills · 1 MCP server</summary><b>Skills</b> regelspraak · wetsanalyse<br><b>MCP servers</b> wettenbank</details> | wetten.overheid.nl / Belastingdienst | ![Bundle · Community](assets/badges/tags-bundle-community.svg) |
| [wetten-overheid-tools](https://github.com/palmw01/wetten-overheid-tools) | Search Dutch legislation on wetten.overheid.nl and retrieve its structure, articles, and terms. | wetten.overheid.nl | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

## Marketplaces

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [bol-mcp](https://github.com/BartWaardenburg/bol-mcp) | Reach bol.com's Retailer API through 76 tools spanning orders, offers, and product listings. | bol.com | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [marktplaats-2dehands-mcp](https://github.com/gjoris/marktplaats-2dehands-mcp) | Search Marktplaats and 2dehands listings, categories, and sellers, with saved searches that return only what is new; an optional login adds your own messages, ads, favourites, and bids. | Marktplaats | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [marktplaats-mcp](https://github.com/PonClick/marktplaats-mcp) | Search and read listings from Marktplaats.nl. | Marktplaats | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [marktplaats-mcp (jasp-nerd)](https://github.com/jasp-nerd/marktplaats-mcp) | Search Marktplaats and 2dehands classifieds with seller-trust signals and new-listing monitoring, no account needed. | Marktplaats | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [PostNL MCP](https://github.com/BartWaardenburg/postnl-mcp) | Create shipments and track PostNL parcels, barcodes, and pickup-point locations. | PostNL | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

## Money

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [aangifte-ib-skill](https://github.com/mischacoster/aangifte-ib-skill) | A skill that prepares a sourced Dutch personal income-tax return with an adaptive interview and review dossier. | Belastingdienst | ![Skill · Community](assets/badges/tags-skill-community.svg) |
| [Belastingzaken skills](https://github.com/johnhout/knowledge-work-belastingzaken) | Eight commands and eight skills for Dutch income tax, BTW, VPB, payroll tax, deductions, and objections — no filing, professional review required. <details><summary>Contains 8 skills · 8 commands</summary><b>Skills</b> aftrekposten-en-regelingen · belasting-intake-en-dossiervorming · bezwaar-en-correspondentie · inkomstenbelasting-boxen · loonheffingen-en-werkkosten · officiele-bronverificatie · omzetbelasting-btw · vennootschapsbelasting-vpb<br><b>Commands</b> aftrekcheck · bezwaar-brief · btw-aangifte · ib-aangifte · intake · loonheffingen · tax-calendar · vpb-aangifte</details> | Belastingdienst | ![Bundle · Community](assets/badges/tags-bundle-community.svg) |
| [bitvavo-mcp](https://github.com/aderik/bitvavo-mcp) | Inspect a Bitvavo account read-only — balances, portfolio value, trades, deposits, withdrawals, and average-cost P&L; it ships no trading or withdrawal tools. | Bitvavo | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [bunq Partner MCP](https://github.com/bunq/partner-mcp) | Automate bunq banking through the Partner API — onboarding, KYC, accounts, payments, cards, and compliance. | bunq | ![MCP · Official · Beta](assets/badges/tags-mcp-official-beta.svg) |
| [dutch-finance-planner-skill](https://github.com/jonnekleijer/dutch-finance-planner-skill) | Coach personal finances for the Netherlands through a guided interview — box 1/2/3, toeslagen, AOW/pension, mortgage/HRA, the 30% ruling, and gift/inheritance tax. | Belastingdienst | ![Skill · Community](assets/badges/tags-skill-community.svg) |
| [nl-tax-agent-skills](https://github.com/cyanxxy/nl-tax-agent-skills) | Turn your own tax documents into a source-cited workpack mapped to Mijn Belastingdienst fields for the income-tax return and voorlopige aanslag — you still enter the figures yourself. <details><summary>Contains 11 skills · 1 agent</summary><b>Skills</b> nl-tax-annual-return · nl-tax-box1-home · nl-tax-box2 · nl-tax-box3 · nl-tax-evidence-indexer · nl-tax-field-mapper · nl-tax-intake · nl-tax-partner-deductions · nl-tax-provisional-assessment · nl-tax-submit-companion · nl-tax-winst<br><b>Agents</b> nl-tax-specialist-reviewer</details> | Belastingdienst | ![Bundle · Community](assets/badges/tags-bundle-community.svg) |

## Travel

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [anwb-mcp](https://github.com/BartWaardenburg/anwb-mcp) | Pull ANWB traffic incidents, plan routes with turn-by-turn directions, and search locations. | ANWB | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [NS MCP Server](https://github.com/r-huijts/ns-mcp-server) | Look up NS train departures and disruptions and plan train journeys. | NS (Nederlandse Spoorwegen) | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [ns-travel-mcp](https://github.com/lauragift21/ns-travel-mcp) | Plan NS journeys and check real-time train data and disruption alerts. | NS (Nederlandse Spoorwegen) | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [ov-mcp](https://github.com/laulauland/ov-mcp) | Search Dutch public-transport stops, find stops near a coordinate, and look up routes across every operator from the national GTFS feed, without an API key. | OVapi | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [ovapi-mcp-server](https://github.com/henrrrik/ovapi-mcp-server) | Look up Dutch bus, tram, metro, and ferry departures from the OVapi real-time feed — search stops, find stops nearby, and inspect lines and journeys. | OVapi | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [rdw-mcp](https://github.com/rantuma/rdw-mcp) | Query RDW vehicle-registration and open data — keyless, no credentials needed. | RDW | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

## Weather

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [knmi-mcp](https://github.com/wolkwork/knmi-mcp) | Pull KNMI real-time weather observations (10-minute measurements) for Dutch locations. | KNMI | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [knmi-mcp (dstotijn)](https://github.com/dstotijn/knmi-mcp) | Query KNMI weather observations and forecasts through KNMI's open data API. | KNMI | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

---

_88 listings across 14 categories, holding 85 skills, 26 commands, 2 agents, and 78 MCP servers._
