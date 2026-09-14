# Awesome Dutch AI Extensions

> MCP servers, skills, and the bundles that carry them — connecting an AI assistant to, or giving it working knowledge of, a Dutch service, data source, standard, or authority.

To add an integration, see [CONTRIBUTING.md](CONTRIBUTING.md). Only ever edit the JSON in `data/` — one file per listing in [`data/listings/`](data/listings), described in [`schema.json`](schema.json). The list below is generated from it by `build-readme.py`.

_Every listing is tagged with what it is and where it came from. What it is comes from what it contains — one kind of thing is that kind, several is a bundle — and where a listing holds more than one artifact, they are named under its description. A status badge appears only when a listing is **not** live, and always because the publisher said so or because we checked — never inferred from a version number._

_Every listing was checked against its source on or after 9 September 2026._

| Category                      | Listings | Covers                                                     |
| ----------------------------- | -------: | ---------------------------------------------------------- |
| [Accounting](#accounting)     |       24 | Exact Online, Moneybird, e-Boekhouden, Twinfield, …        |
| [Business](#business)         |       10 | KVK, Adyen, bol.com, Intermediair, internet.nl, Mollie, …  |
| [Data](#data)                 |        8 | CBS StatLine, CBS ODiN, Geonovum, Kadaster, PDOK, …        |
| [Education](#education)       |        1 | Magister                                                   |
| [Government](#government)     |        9 | CBS StatLine, officielebekendmakingen.nl, Tweede Kamer, …  |
| [Groceries](#groceries)       |        7 | Albert Heijn, Jumbo, Plus, Picnic, Aldi, DA, …             |
| [Health](#health)             |        1 | AGB-register                                               |
| [History](#history)           |        5 | Rijksdienst voor het Cultureel Erfgoed, Alle Friezen, …    |
| [Housing](#housing)           |        4 | CBS StatLine, Kadaster, Kamernet, Netbeheerdata, …         |
| [Language](#language)         |        2 | Nederlands, Inburgeringsexamen                             |
| [Law](#law)                   |       11 | Rechtspraak.nl, wetten.overheid.nl, AVG, NIS2-richtlijn, … |
| [Marketplaces](#marketplaces) |        5 | Marktplaats, bol.com, PostNL                               |
| [Money](#money)               |        7 | Belastingdienst, Autoverzekering.nl, Bitvavo, bunq         |
| [Travel](#travel)             |        7 | NS, OVapi, RDW, ANWB                                       |
| [Weather](#weather)           |        2 | KNMI                                                       |

## Accounting

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [AFAS AI Connect](https://github.com/iwebdevnl/afas-ai-connect) | View outstanding items, balance sheets and profit and loss in AFAS Profit and prepare postings. <details><summary>Contains 4 commands · 1 MCP server</summary><b>Commands</b> afas-balans · afas-omzet · afas-openstaande-debiteuren · afas-ouderdomsanalyse<br><b>MCP servers</b> afas</details> | AFAS Profit | ![Bundle · Commercial](assets/badges/tags-bundle-commercial.svg) |
| [Bouw Botje](https://bouwbotje.nl/) | Manage Exact Online Bouw projects, calculations, hour logs and instalment invoices for Dutch construction and installation firms. | Exact Online | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |
| [e-Boekhouden MCP](https://github.com/CodeMill-Solutions/e-boekhouden-mcp) | View your e-Boekhouden accounts and post invoices, payments and expenses. | e-Boekhouden | ![MCP · Community · Install broken](assets/badges/tags-mcp-community-broken.svg) |
| [Exact Online AI Connect](https://github.com/iwebdevnl/exact-online-ai-connect) | Analyse cash flow, receivables and profit in Exact Online and prepare VAT returns and period closing with bundled skills. <details><summary>Contains 10 skills · 4 commands · 1 MCP server</summary><b>Skills</b> btw-aangifte-assistent · cashflow-analyse · creditcard-aflettering · debiteurenbeheer · exact-afletter-logica · grootboek-anomalie-detectie · management-informatie · periodeafsluiting · reporting · resultatenrekening-analyse<br><b>Commands</b> exact-balans · exact-omzet · exact-openstaande-debiteuren · exact-ouderdomsanalyse<br><b>MCP servers</b> exact-online</details> | Exact Online | ![Bundle · Commercial](assets/badges/tags-bundle-commercial.svg) |
| [exact-mcp](https://github.com/lemon-official/exact-mcp) | Create sales orders and goods deliveries in Exact Online, find unpaid invoices, and view or update other accounting records. | Exact Online | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [Finance MCP](https://financemcp.nl/) | View and compare accounting data from Exact Online, Moneybird, Business Central, Twinfield and e-Boekhouden.nl through one connection. | Exact Online / Moneybird / Microsoft Dynamics 365 Business Central / Twinfield / e-Boekhouden | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |
| [finance-skills-nl](https://github.com/start2scale/finance-skills-nl) | Check Excel models and ledger discrepancies and prepare month-end closing under Dutch reporting rules. <details><summary>Contains 9 skills</summary><b>Skills</b> ai-readiness-mkb · doorrol-schema · excel-controle · grootboek-aansluiting · maandafsluiting · transitorische-posten · variantie-toelichting · verschillen-traceren · xlsx-author</details> | Raad voor de Jaarverslaggeving (RJ) | ![Skill · Community](assets/badges/tags-skill-community.svg) |
| [iXBRL Skill](https://github.com/MaxSchoon/ixbrl) | Prepare and check an iXBRL annual account for deposit at the KVK: pin the right NT taxonomy version, apply the SBR filing rules and validate the package with Arelle before it goes in. | SBR (Standard Business Reporting) / KVK / Raad voor de Jaarverslaggeving (RJ) / AFM (Autoriteit Financiële Markten) | ![Skill · Community](assets/badges/tags-skill-community.svg) |
| [Jortt MCP](https://www.jortt.nl/koppelingen/mcp-koppeling/) | View your Jortt accounts, create invoices and book expenses. | Jortt | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [Ledger Botje](https://ledgerbotje.nl/) | Manage Exact Online orders, stock, production and invoices, down to warehouses, batches and serial numbers. | Exact Online | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |
| [Moneybird MCP](https://developer.moneybird.com/tools/mcp) | View your Moneybird accounts and create or update contacts, invoices and time entries. | Moneybird | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [Moneybird MCP (Espaye)](https://github.com/Espaye/moneybird-mcp-server) | Match bank transactions to the invoices they settle, read VAT, profit-and-loss and ledger reports, and search contacts and invoices in Moneybird; writing back is off until you enable it. | Moneybird | ![MCP · Community · Beta](assets/badges/tags-mcp-community-beta.svg) |
| [moneybird-mcp-server](https://github.com/vanderheijden86/moneybird-mcp-server) | View Moneybird invoices, contacts, estimates and time entries, and use custom API calls to create, update or delete records. | Moneybird | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [OpenAccountants Plugin](https://github.com/openaccountants/openaccountants/tree/main/plugins/openaccountants) | Prepare Dutch bookkeeping and tax returns with sources on VAT, income tax and self-employed deductions. <details><summary>Contains 1 command · 1 MCP server</summary><b>Commands</b> openaccountants<br><b>MCP servers</b> openaccountants</details> | Belastingdienst | ![Bundle · Community](assets/badges/tags-bundle-community.svg) |
| [Paperdork MCP](https://paperdork.nl/paperdork-en-ai-koppelen-dit-kan-je-doen-met-onze-mcp-integratie/) | Send invoices and payment reminders and record expenses, time and mileage in Paperdork. | Paperdork | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [pp-e-boekhouden](https://github.com/mvanhorn/printing-press-library/tree/main/library/payments/e-boekhouden) | Create financial reports from your e-Boekhouden accounts, find invoices without payments and enter transactions. <details><summary>Contains 1 skill · 1 MCP server</summary><b>Skills</b> pp-e-boekhouden<br><b>MCP servers</b> e-boekhouden</details> | e-Boekhouden | ![Bundle · Community](assets/badges/tags-bundle-community.svg) |
| [Praat met je Boekhouding](https://praatmetjeboekhouding.nl/en/exact-online-mcp-server) | Ask questions about your invoices, VAT and financial reports in Exact Online. | Exact Online | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |
| [rompslomp-mcp](https://github.com/lmolema/rompslomp-mcp) | Create and update invoices, quotes, expenses and payments in Rompslomp, maintain contacts and record journal entries, time and mileage. | Rompslomp | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [Simplicate MCP](https://developer.simplicate.com/docs/mcp/getting_started/) | Log time and mileage on Simplicate projects, find contacts and invoices, and create or update sales opportunities. | Simplicate | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [Twinfield AI Connect](https://github.com/iwebdevnl/twinfield-ai-connect) | View outstanding items, ageing reports, balance sheets and profit and loss in Twinfield and prepare postings. <details><summary>Contains 4 commands · 1 MCP server</summary><b>Commands</b> twinfield-balans · twinfield-omzet · twinfield-openstaande-debiteuren · twinfield-ouderdomsanalyse<br><b>MCP servers</b> twinfield</details> | Twinfield | ![Bundle · Commercial](assets/badges/tags-bundle-commercial.svg) |
| [Twinfield MCP](https://github.com/CodeMill-Solutions/twinfield-mcp) | View Twinfield transactions, customers and suppliers and draft purchase invoices, sales invoices and journal entries. | Twinfield | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [WeFact MCP](https://github.com/NickAldewereld/wefact-mcp) | Manage customers, send or credit invoices and view products, subscriptions and purchase invoices in WeFact. | WeFact | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [wefact-mcp (CodeMill)](https://github.com/CodeMill-Solutions/wefact-mcp) | Manage invoices, quotes and subscriptions in WeFact and send emails to customers. | WeFact | ![MCP · Community · Install broken](assets/badges/tags-mcp-community-broken.svg) |
| [Yuki MCP](https://github.com/CodeMill-Solutions/yuki-mcp) | View your Yuki accounts and outstanding invoices, post purchase and sales invoices and journal entries, and add documents to the archive. | Yuki | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

## Business

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [Adyen MCP](https://docs.adyen.com/development-resources/mcp-server/) | Create payment links, process payments and refunds, and manage Adyen payment terminals and webhooks. | Adyen | ![MCP · Official · Preview](assets/badges/tags-mcp-official-preview.svg) |
| [Bol MCP van Rylee](https://rylee.nl/nl/solutions/bol-mcp) | Analyse your bol.com sales, profit, stock, returns and advertising using data from Rylee. | bol.com | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [Intermediair Jobs](https://www.intermediair.nl/.well-known/mcp.json) | Search Intermediair's hbo and wo vacancies by role, place and radius, contract and salary, and fetch the full posting; a subset of the same DPG listings as Nationale Vacaturebank. | Intermediair | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [kvk-connect (MinBZK)](https://github.com/MinBZK/kvk-connect) | Search company records and their change history in your own KVK database. | KVK | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [kvk-mcp](https://github.com/BartWaardenburg/kvk-mcp) | Find companies, branches and trade names in the KVK Handelsregister and view change notifications. | KVK | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [Mollie MCP](https://docs.mollie.com/docs/mollie-mcp-server) | Create payment links and manage payments, customers, invoices and subscriptions in Mollie. | Mollie | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [Nationale Vacaturebank Jobs](https://www.nationalevacaturebank.nl/.well-known/mcp.json) | Search Nationale Vacaturebank vacancies by role, place and radius, contract, education level and salary, and fetch the full posting. | Nationale Vacaturebank | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [pp-tenderned](https://github.com/mvanhorn/printing-press-library/tree/main/library/sales-and-crm/tenderned) | Search TenderNed tenders, including those below EU thresholds, look up contracting authorities and download specifications. <details><summary>Contains 1 skill · 1 MCP server</summary><b>Skills</b> pp-tenderned<br><b>MCP servers</b> tenderned</details> | TenderNed | ![Bundle · Community](assets/badges/tags-bundle-community.svg) |
| [Sendcloud MCP](https://sendcloud.dev/docs/getting-started/mcp-server) | Create shipping labels, track parcels and arrange returns and pickups in Sendcloud; shipments created on your live account can incur charges. | Sendcloud | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [skills-internet](https://github.com/developer-overheid-nl/skills-internet) | Check website and email settings against internet.nl standards, with configuration guidance and checks across multiple domains at once. <details><summary>Contains 5 skills</summary><b>Skills</b> inet · inet-api · inet-mail · inet-toolbox · inet-web</details> | internet.nl | ![Skill · Community · Concept](assets/badges/tags-skill-community-concept.svg) |

## Data

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [cbs-statline-skill](https://github.com/linksmith/cbs-statline-skill) | Find, download and combine CBS tables for research, with extra guidance on housing and energy statistics and checks for outdated tables. | CBS StatLine | ![Skill · Community](assets/badges/tags-skill-community.svg) |
| [data-analysis-journalism](https://github.com/linksmith/data-analysis-journalism) | Find story leads in cleaned Dutch data: compare regions, spot trends and outliers, and develop follow-up questions. | CBS StatLine | ![Skill · Community](assets/badges/tags-skill-community.svg) |
| [data-cleaning-dutch](https://github.com/linksmith/data-cleaning-dutch) | Clean Dutch CSV and Excel files for analysis: fix dates, decimal commas and column headers, and identify missing values. | CBS StatLine / Kadaster | ![Skill · Community](assets/badges/tags-skill-community.svg) |
| [dutch-choropleth-maps](https://github.com/linksmith/dutch-choropleth-maps) | Map Dutch statistics by municipality, district or neighbourhood, using boundaries from the matching year and checking for missing data. | PDOK / CBS StatLine | ![Skill · Community](assets/badges/tags-skill-community.svg) |
| [mcp-cbs-cijfers-open-data](https://github.com/dstotijn/mcp-cbs-cijfers-open-data) | Find CBS tables, inspect what the figures represent and select data by criteria such as period, region or population group. | CBS StatLine | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [postcode-eu-ai-tools](https://github.com/postcode-nl/postcode-eu-ai-tools-python) | Complete Dutch addresses from a postcode and house number and validate international addresses with Postcode.eu. | Postcode.eu | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [SB OGC MCP](https://github.com/Studio-Bereikbaar/sb-ogc-mcp) | Compare travel patterns between Dutch locations and create accessibility maps using CBS travel data and Studio Bereikbaar traffic networks. | CBS ODiN | ![MCP · Commercial · Preview](assets/badges/tags-mcp-commercial-preview.svg) |
| [skills-geo](https://github.com/developer-overheid-nl/skills-geo) | Choose and apply Dutch standards for geo APIs, metadata and 3D data with explanations and examples. <details><summary>Contains 6 skills</summary><b>Skills</b> geo · geo-3d · geo-api · geo-inspire · geo-meta · geo-model</details> | Geonovum | ![Skill · Community · Concept](assets/badges/tags-skill-community-concept.svg) |

## Education

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [unofficial-magister-mcp](https://github.com/israelroldan/unofficial-magister-mcp) | Check daily and weekly Magister timetables and school start and finish times for dropping off and picking up your child. | Magister | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

## Government

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [baarn-raadsinformatie](https://github.com/tiemenrtuinstra/baarn-raadsinformatie) | Search Baarn council meetings, agendas and documents by keyword or meaning, using information from Notubiz. | Gemeente Baarn | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [BesluitBron](https://besluitbron.nl/nl/onboarding/unified) | Search the decisions of Dutch municipalities, provinces, water authorities, parliament and the courts from one connector, and cite the underlying document for every answer. | Open Raadsinformatie / OpenBesluitvorming / Tweede Kamer / officielebekendmakingen.nl / Rechtspraak.nl / Open Archivaris | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [Data Journalist AI Agent Plugin](https://github.com/linksmith/data-journalist-ai-agent-plugin-with-skills) | Investigate stories with Dutch data sources, draft public information requests and track facts, sources and open questions for each investigation. <details><summary>Contains 4 skills · 2 commands · 1 agent</summary><b>Skills</b> browser-lookup · dutch-sources · story-state · woo-draft<br><b>Commands</b> new-investigation · weekly-digest<br><b>Agents</b> research-assistant</details> | CBS StatLine / DUO (Dienst Uitvoering Onderwijs) / KVK / Woogle / officielebekendmakingen.nl / RVO (Rijksdienst voor Ondernemend Nederland) / NVWA / BIG-register | ![Bundle · Community](assets/badges/tags-bundle-community.svg) |
| [mcp-gemeente-amsterdam](https://github.com/aronmartin/mcp-gemeente-amsterdam) | Look up Amsterdam addresses, monuments, waste collection and parking in municipal data. | Gemeente Amsterdam | ![MCP · Community · Abandoned](assets/badges/tags-mcp-community-abandoned.svg) |
| [NeoDemos](https://github.com/NeoDemosHQ/neodemos-plugins) | Draft Rotterdam council motions and questions in the format the RvO prescribes, review concept texts and pull CBS figures for the city; searching the council archive itself needs a paid account. | Gemeente Rotterdam / Open Raadsinformatie / CBS StatLine | ![MCP · Community · Preview](assets/badges/tags-mcp-community-preview.svg) |
| [nl-gov-mcp](https://github.com/WAINUTAI/nl-gov-mcp) | Combine statistics, parliamentary documents, court rulings and other Dutch government data with source references. | CBS StatLine / RDW / KNMI / Rechtspraak.nl / PDOK / Kadaster / Rijksdienst voor het Cultureel Erfgoed (RCE) / wetten.overheid.nl / OVapi / NS (Nederlandse Spoorwegen) / data.overheid.nl / Tweede Kamer / DUO (Dienst Uitvoering Onderwijs) / BAG (Basisregistratie Adressen en Gebouwen) / TenderNed / officielebekendmakingen.nl | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [nl-opendata-mcp](https://github.com/soulnai/nl-opendata-mcp) | Find and filter datasets from CBS and data.overheid.nl and download them for analysis. | CBS StatLine / data.overheid.nl | ![MCP · Community · Concept](assets/badges/tags-mcp-community-concept.svg) |
| [open-utrecht-datasets](https://github.com/Terminal-WOO/open-utrecht-datasets) | Find open datasets from Utrecht and data.overheid.nl, view download links and identify datasets relevant to your public information research. | Gemeente Utrecht | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [OpenTK MCP](https://github.com/r-huijts/opentk-mcp) | Research parliamentary documents, votes and MPs through OpenTK, and identify relevant passages before reading long documents. | Tweede Kamer | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

## Groceries

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [ah-mcp](https://github.com/mrserzhan/ah-mcp) | Find AH products, Bonus and Vandaag-af clearance deals, fill your lists or cart, and view past orders and receipts. | Albert Heijn | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [Albert Heijn Automation](https://github.com/robinbril/Albert-Heijn-Automation) | Plan meals and fill your AH list or cart using past purchases, recipes and relevant Bonus deals. <details><summary>Contains 1 skill · 1 MCP server</summary><b>Skills</b> albert-heijn<br><b>MCP servers</b> ah</details> | Albert Heijn | ![Bundle · Community](assets/badges/tags-bundle-community.svg) |
| [mcp-picnic](https://github.com/ivo-toby/mcp-picnic) | Find products, offers and recipes at Picnic, fill your cart, check delivery slots and track your order and driver. | Picnic | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [nl-supermarkt-mcp](https://github.com/Samvox1/nl-supermarkt-mcp) | Compare supermarket prices and supermarket and drugstore deals using Checkjebon and Folderz, and build a shopping list within your budget. | Albert Heijn / Jumbo / Lidl / Aldi / Plus / DekaMarkt / Dirk / Vomar / Hoogvliet / Spar / Picnic / Poiesz / Kruidvat / Etos / Trekpleister / DA / Holland & Barrett / Douglas / De Online Drogist | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [orderfood](https://github.com/henkas/orderfood) | Find restaurants and menus on Uber Eats and Thuisbezorgd and fill your cart. | Thuisbezorgd.nl | ![MCP · Community · Install broken](assets/badges/tags-mcp-community-broken.svg) |
| [Pepesto Agent to Cart](https://www.pepesto.com/agent-to-cart/) | Send your shopping list to the Pepesto app for a basket with products and prices at Albert Heijn, Jumbo or Plus. | Albert Heijn / Jumbo / Plus | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |
| [Pepesto MCP Server](https://github.com/pepesto-solutions/pepesto-mcp) | Turn recipes into baskets with prices and checkout links for Albert Heijn, Jumbo or Plus using paid API credit; sending a shopping list to the app is free. | Albert Heijn / Jumbo / Plus | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |

## Health

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [Vektis MCP](https://github.com/pooryam92/vektis-mcp) | Find care providers by name or AGB code and practices also by town or postcode in the Vektis AGB-register; view contacts, registration status, qualifications, recognitions and relationships. | AGB-register (Vektis) | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

## History

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [GeneaGenie](https://www.geneagenie.be/nl/ai/) | Find family records, combine discoveries with your own family tree data, confirm matches and manage your searches. | Alle Friezen / Alle Groningers / Brabants Historisch Informatie Centrum (BHIC) / Rijksarchief (België) / Familiekunde Vlaanderen | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [mcp-monumenten](https://github.com/woonstadrotterdam/mcp-monumenten) | Check a Dutch address or BAG identifier to see whether a property is a monument or lies in a protected townscape. | Monumenten / Rijksdienst voor het Cultureel Erfgoed (RCE) | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [openarchieven-mcp](https://github.com/coret/openarchieven-mcp-server) | Search birth, marriage and death records in Open Archieven, follow source references and search transcriptions of historical documents. | Open Archieven | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [rce-cho-mcp](https://github.com/jolietjakeblues/rce-cho-mcp) | Research monuments and other heritage in RCE data, with help interpreting concepts and validating your SPARQL queries. | Rijksdienst voor het Cultureel Erfgoed (RCE) | ![MCP · Community · Beta](assets/badges/tags-mcp-community-beta.svg) |
| [rijksmuseum-mcp+](https://github.com/kintopp/rijksmuseum-mcp-plus) | Find artworks by meaning, Iconclass or location and explore provenance and similarities in an enriched copy of the Rijksmuseum collection. <details><summary>Contains 1 skill · 1 MCP server</summary><b>Skills</b> rijksmuseum-mcp-plus<br><b>MCP servers</b> rijksmuseum-mcp-plus</details> | Rijksmuseum / Iconclass | ![Bundle · Community · Preview](assets/badges/tags-bundle-community-preview.svg) |

## Housing

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [kadaster-mcp](https://github.com/jolietjakeblues/kadaster-mcp) | Research parcels and restrictions affecting them in the Kadaster Knowledge Graph, with tools to build queries, compare locations and check query results. | Kadaster | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [kamernet-mcp](https://github.com/jasp-nerd/kamernet-mcp) | Search Kamernet for rooms, studios and apartments within your budget, compare rent, deposits and address-registration options, and check new listings. | Kamernet | ![MCP · Community · Beta](assets/badges/tags-mcp-community-beta.svg) |
| [Overstappen.nl MCP](https://www.overstappen.nl/energie/) | Compare Dutch energy contracts by address, electricity and gas use and solar feed-in, with tariffs, discounts and estimated annual costs, then continue to Overstappen.nl to switch. | Overstappen.nl | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [wonen-energie-alternatieve-bronnen](https://github.com/linksmith/wonen-energie-alternatieve-bronnen) | Research housing and energy by neighbourhood using grid-operator data and PDOK/CBS maps and turn the findings into tables and charts. | Netbeheerdata (Liander / Enexis / Stedin) / PDOK / CBS StatLine | ![Skill · Community](assets/badges/tags-skill-community.svg) |

## Language

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [Dutch Fluency MCP](https://mcp.dutchfluency.com/) | Get Dutch sentence corrections with explanations, estimate your language level and practise KNM civic integration questions. | Nederlands (taal) / Inburgeringsexamen | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |
| [Dutch Native](https://github.com/brunocous/dutch-native) | Write and rewrite natural Dutch for the Netherlands or Belgium, with guidance on literal English translations, stiff sentences and unsuitable word choices. | Nederlands (taal) | ![Skill · Community](assets/badges/tags-skill-community.svg) |

## Law

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [Ansvar Gateway](https://ansvar.eu/coverage/netherlands) | Search Dutch laws, case law and information on privacy and cybersecurity with source references in the Ansvar knowledge base. | wetten.overheid.nl / Rechtspraak.nl / AVG (Algemene verordening gegevensbescherming) | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |
| [ICTRecht Legal GenAI Resources](https://github.com/ICTRecht/Legal-GenAI-Resources) | Summarise contracts, compare versions and draft NDAs and data processing agreements with ICTRecht prompts and skills for Dutch law. <details><summary>Contains 2 skills · 3 commands · 5 MCP servers</summary><b>Skills</b> samenvatten · vergelijken<br><b>Commands</b> DPA · NDA · overdracht auteursrecht<br><b>MCP servers</b> atlassian · box · egnyte · ms365 · slack</details> | AVG (Algemene verordening gegevensbescherming) | ![Bundle · Commercial](assets/badges/tags-bundle-commercial.svg) |
| [ICTRecht Plugin Suite](https://github.com/ICTRecht/claude-plugin) | Review contracts, privacy issues and EU rules with workflows for each legal role. <details><summary>Contains 47 skills</summary><b>Skills</b> aansprakelijkheid · advies-structuur · ai-act-classificatie · ai-ip · algemene-voorwaarden · ap-contact · auteursrecht · avg-rechten · betrokkenen-contact · cold-start-interview · compliance-check · contract-review · cyberweerbaarheid-act · data-act · data-governance · data-sharing · datalek · datalek-toets · dataverdrag-analyse · dma-analyse · doorgifte · doorgifte-advies · dpia · dpia-toets · dsa-verplichtingen · fg-advies · fg-jaarverslag · geschil-voorbereiding · grondslag · grondslag-advies · handelsnaam-domeinnaam · ie-clausules · juridisch-memo · merkenrecht · nda-review · nis2-check · onderhandeling-prep · open-data · regelgeving-scan · register-toets · risico-analyse · sla-review · software-licenties · toezichtsplan · verwerkingsregister · vok-review · vok-toets</details> | AVG (Algemene verordening gegevensbescherming) / AI-verordening (AI Act) / NIS2-richtlijn | ![Skill · Commercial](assets/badges/tags-skill-commercial.svg) |
| [IURA NL](https://github.com/iura-ai/IURA-Plugins/tree/main/iura-nl) | Review contracts, draft court documents and search Dutch case law with IURA. <details><summary>Contains 7 skills · 1 MCP server</summary><b>Skills</b> conclusie-van-antwoord · contractbeoordeling · iura · juridische-notitie · nda-generatie · nda-triaging · tabellarische-beoordeling<br><b>MCP servers</b> IURA NL</details> | Rechtspraak.nl | ![Bundle · Commercial](assets/badges/tags-bundle-commercial.svg) |
| [LegalMike Golden Retriever](https://legalmike.ai/golden-retriever-mcp/) | Ask one question about Dutch law and get a reasoned answer from case law, legislation, disciplinary law, local rules, EU law and parliamentary papers, citing ECLI and CELEX. | Rechtspraak.nl / wetten.overheid.nl / Tuchtrecht.nl | ![MCP · Commercial](assets/badges/tags-mcp-commercial.svg) |
| [NIS2 MSP-skillset](https://github.com/Dxfferent/nis2-quickscan) | Help IT service clients assess NIS2 scope and incident reporting, discuss their quickscan report and set up the quickscan for sale under your own brand. <details><summary>Contains 6 skills</summary><b>Skills</b> nis2-scope-check · nis2-meldplicht-coach · nis2-rapport-adviseur · nis2-installatie · nis2-crm-koppeling · nis2-msp-gtm</details> | NIS2-richtlijn | ![Skill · Commercial](assets/badges/tags-skill-commercial.svg) |
| [nl-eli-mcp](https://github.com/matematicsolutions/nl-eli-mcp) | Retrieve Dutch legislation in force on a chosen date with official source references, and find court rulings by date, court or ECLI. | wetten.overheid.nl / Rechtspraak.nl | ![MCP · Community · Preview](assets/badges/tags-mcp-community-preview.svg) |
| [pp-rechtspraak](https://github.com/mvanhorn/printing-press-library/tree/main/library/other/rechtspraak) | Search Dutch rulings by word and phrase, exclude terms, follow cases through cassation and export source references. <details><summary>Contains 1 skill · 1 MCP server</summary><b>Skills</b> pp-rechtspraak<br><b>MCP servers</b> rechtspraak</details> | Rechtspraak.nl | ![Bundle · Community](assets/badges/tags-bundle-community.svg) |
| [rechtspraak-mcp](https://github.com/Prudai/rechtspraak-mcp) | Find Dutch rulings by date, court or legal area, read their full text and use LiDO to follow citations between rulings and laws. | Rechtspraak.nl | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [Wetsanalyse AI](https://github.com/palmw01/wetsanalyse-ai) | Mark rights, conditions and deadlines in Dutch legislation using the JAS method, with article references and a legal professional reviewing each proposed marking. | wetten.overheid.nl | ![Skill · Community](assets/badges/tags-skill-community.svg) |
| [wetten-overheid-tools](https://github.com/palmw01/wetten-overheid-tools) | Find Dutch laws, explore their structure and retrieve specific articles or passages containing a search term from the official Wettenbank. | wetten.overheid.nl | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

## Marketplaces

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [bol-mcp](https://github.com/BartWaardenburg/bol-mcp) | Manage offers, stock, orders, shipments and returns as a bol seller, and check invoices, commissions and sales figures. | bol.com | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [marktplaats-2dehands-mcp](https://github.com/gjoris/marktplaats-2dehands-mcp) | Search Marktplaats and 2dehands, save searches to find new ads, read messages and view your own ads, favourites and bids. | Marktplaats | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [marktplaats-mcp](https://github.com/PonClick/marktplaats-mcp) | Search Marktplaats by price, distance and details such as RAM or bike size, and view the full ad, photos and seller ratings. | Marktplaats | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [marktplaats-mcp (jasp-nerd)](https://github.com/jasp-nerd/marktplaats-mcp) | Search Marktplaats and 2dehands, check seller ratings and verification, and find ads posted since your previous search. | Marktplaats | ![MCP · Community · Beta](assets/badges/tags-mcp-community-beta.svg) |
| [PostNL MCP](https://github.com/BartWaardenburg/postnl-mcp) | Create PostNL shipments and shipping labels, track parcels, find pickup points and calculate delivery dates and time slots. | PostNL | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

## Money

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [aangifte-ib-skill](https://github.com/mischacoster/aangifte-ib-skill) | Prepare your Dutch income tax return through an interview about your situation and a dossier with sources for each field. | Belastingdienst | ![Skill · Community](assets/badges/tags-skill-community.svg) |
| [Autoverzekering.nl MCP](https://www.autoverzekering.nl/) | Compare Dutch car-insurance policies by license plate, birth date, postcode, claim-free years and coverage (WA to volledig casco), then continue to Autoverzekering.nl to take out a policy. | Autoverzekering.nl | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [Belastingzaken skills](https://github.com/johnhout/knowledge-work-belastingzaken) | Prepare tax returns and objection letters for individuals, sole traders and Dutch limited companies, checking official sources. <details><summary>Contains 8 skills · 8 commands · 4 MCP servers</summary><b>Skills</b> aftrekposten-en-regelingen · belasting-intake-en-dossiervorming · bezwaar-en-correspondentie · inkomstenbelasting-boxen · loonheffingen-en-werkkosten · officiele-bronverificatie · omzetbelasting-btw · vennootschapsbelasting-vpb<br><b>Commands</b> aftrekcheck · bezwaar-brief · btw-aangifte · ib-aangifte · intake · loonheffingen · tax-calendar · vpb-aangifte<br><b>MCP servers</b> bigquery · ms365 · notion · slack</details> | Belastingdienst | ![Bundle · Community](assets/badges/tags-bundle-community.svg) |
| [bitvavo-mcp](https://github.com/aderik/bitvavo-mcp) | View the value, profit and loss of your Bitvavo holdings and include purchases and conversions made in the app by importing your transaction CSV. | Bitvavo | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [bunq Partner MCP](https://github.com/bunq/partner-mcp) | As a bunq partner, handle customer onboarding, identity checks, accounts, payments and cards. | bunq | ![MCP · Official](assets/badges/tags-mcp-official.svg) |
| [dutch-finance-planner-skill](https://github.com/jonnekleijer/dutch-finance-planner-skill) | Build a monthly budget and action plan for saving, debt and retirement through a personal interview, taking Dutch taxes and benefits into account. | Belastingdienst | ![Skill · Community](assets/badges/tags-skill-community.svg) |
| [nl-tax-agent-skills](https://github.com/cyanxxy/nl-tax-agent-skills) | Prepare your 2025 Dutch income tax return or 2026 provisional assessment with sources for each field. <details><summary>Contains 11 skills · 1 agent</summary><b>Skills</b> nl-tax-annual-return · nl-tax-box1-home · nl-tax-box2 · nl-tax-box3 · nl-tax-evidence-indexer · nl-tax-field-mapper · nl-tax-intake · nl-tax-partner-deductions · nl-tax-provisional-assessment · nl-tax-submit-companion · nl-tax-winst<br><b>Agents</b> nl-tax-specialist-reviewer</details> | Belastingdienst | ![Bundle · Community](assets/badges/tags-bundle-community.svg) |

## Travel

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [anwb-mcp](https://github.com/BartWaardenburg/anwb-mcp) | Check ANWB traffic jams and roadworks and plan driving, cycling or walking routes, including EV routes with charging stops. | ANWB | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [NS MCP Server](https://github.com/r-huijts/ns-mcp-server) | Plan NS train journeys, check departures, arrivals and disruptions, and look up ticket prices, station facilities and available OV-fiets bikes. | NS (Nederlandse Spoorwegen) | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [ns-travel-mcp](https://github.com/lauragift21/ns-travel-mcp) | Plan NS train journeys, check live departures and look up disruptions and engineering works. | NS (Nederlandse Spoorwegen) | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [ov-mcp](https://github.com/laulauland/ov-mcp) | Find public transport stops by name or location and look up Dutch operators’ routes in the national timetable. | OVapi | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [ovapi-mcp-server](https://github.com/henrrrik/ovapi-mcp-server) | Check bus, tram, metro and ferry departures through OVapi, find nearby stops and see a journey’s stops in order. | OVapi | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [rdw-mcp](https://github.com/rantuma/rdw-mcp) | Get a vehicle report by Dutch licence plate with registration, fuel, emissions, axle and body data from open RDW records, as readable text and JSON. | RDW | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [rdw-mcp-server](https://github.com/jodur/RDW-MCP) | Look up vehicle details, inspection expiry, fuel, emissions and towing limits by Dutch licence plate in open RDW records. | RDW | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

## Weather

| Name | Description | Subject | Tags&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
|---|---|---|---|
| [knmi-mcp](https://github.com/wolkwork/knmi-mcp) | Check temperature, rainfall and wind at the KNMI weather station nearest your location, with readings every ten minutes. | KNMI | ![MCP · Community](assets/badges/tags-mcp-community.svg) |
| [knmi-mcp (dstotijn)](https://github.com/dstotijn/knmi-mcp) | Check KNMI weather for your Dutch town, including current conditions, hourly and daily forecasts, and weather warnings. | KNMI | ![MCP · Community](assets/badges/tags-mcp-community.svg) |

---

_103 listings across 15 categories, holding 130 skills, 26 commands, 2 agents, and 93 MCP servers._
