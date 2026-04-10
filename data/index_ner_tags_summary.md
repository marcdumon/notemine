---
title: "NER / Tagging / Summarisation Benchmark Index"
created: "2026-04-10"
purpose: "Ground-truth metadata index for evaluating LLM-based Named Entity Recognition, tagging, and summarisation across 20 synthetic Obsidian WebClipper documents (10 EN, 10 NL)."
---

# NER / Tagging / Summarisation Benchmark Index

Each entry contains:
- **File** — filename and language/length category
- **Summary** — 2-3 sentence ground-truth summary
- **Tags** — expected topic tags
- **NER** — named entities by type (PER = person, ORG = organisation, LOC = location, DATE = date/time expression, PROD = product/model, MISC = other named entity)

---

## 1. `short_tech_news_openai_announcement_en.md`
**Lang/Length:** English / Short (~220 words)

**Summary:** OpenAI CEO Sam Altman announced GPT-5 at the Moscone Center in San Francisco on March 15, 2025, claiming it outperforms Google DeepMind's Gemini Ultra 2.0 on the MMLU benchmark. Microsoft confirmed GPT-5 integration into Azure AI Studio and Microsoft Copilot by April 2025. AI safety researcher Geoffrey Hinton and EU regulators called for independent safety evaluations before deployment.

**Tags:** `ai` `openai` `gpt-5` `tech-conference` `san-francisco` `microsoft` `llm`

**NER:**
| Entity | Type |
|---|---|
| Sam Altman | PER |
| Geoffrey Hinton | PER |
| Satya Nadella | PER |
| OpenAI | ORG |
| Microsoft | ORG |
| Google DeepMind | ORG |
| Moscone Center | LOC |
| San Francisco | LOC |
| Redmond, Washington | LOC |
| European Union | LOC |
| March 15, 2025 | DATE |
| April 2025 | DATE |
| January 2025 | DATE |
| GPT-5 | PROD |
| Gemini Ultra 2.0 | PROD |
| Azure AI Studio | PROD |
| Microsoft Copilot | PROD |
| EU AI Act | MISC |
| MMLU benchmark | MISC |

---

## 2. `short_tech_nieuws_openai_aankondiging_nl.md`
**Lang/Length:** Dutch / Short (~220 words)

**Summary:** OpenAI-topman Sam Altman kondigde GPT-5 aan op 15 maart 2025 in het Moscone Center in San Francisco en beweerde dat het beter presteert dan Google DeepMind's Gemini Ultra 2.0 op de MMLU-benchmark. Microsoft bevestigde integratie van GPT-5 in Azure AI Studio en Microsoft Copilot vóór april 2025. AI-veiligheidsonderzoeker Geoffrey Hinton en EU-regelgevers riepen op tot onafhankelijke evaluaties vóór inzet.

**Tags:** `ai` `openai` `gpt-5` `technologieconferentie` `san-francisco` `microsoft` `llm`

**NER:**
| Entity | Type |
|---|---|
| Sam Altman | PER |
| Geoffrey Hinton | PER |
| Satya Nadella | PER |
| OpenAI | ORG |
| Microsoft | ORG |
| Google DeepMind | ORG |
| Moscone Center | LOC |
| San Francisco | LOC |
| Redmond, Washington | LOC |
| Europese Unie | LOC |
| 15 maart 2025 | DATE |
| april 2025 | DATE |
| januari 2025 | DATE |
| GPT-5 | PROD |
| Gemini Ultra 2.0 | PROD |
| Azure AI Studio | PROD |
| Microsoft Copilot | PROD |
| EU AI Act | MISC |
| MMLU-benchmark | MISC |

---

## 3. `short_recipe_dutch_stamppot_en.md`
**Lang/Length:** English / Short (~160 words)

**Summary:** A recipe for classic Dutch stamppot boerenkool met worst, combining mashed potatoes with curly kale and smoked sausage (rookworst). The recipe includes ingredients, step-by-step instructions, and a seasonal note that stamppot is traditionally eaten from October to March in the Netherlands. Brands Unox and Hema are cited as traditional rookworst producers.

**Tags:** `recipe` `dutch-cuisine` `stamppot` `boerenkool` `winter` `comfort-food` `netherlands`

**NER:**
| Entity | Type |
|---|---|
| Liesbeth Verhoeven | PER |
| Netherlands | LOC |
| Unox | ORG |
| Hema | ORG |
| Albert Heijn | ORG |
| Jumbo | ORG |
| October to March | DATE |
| Bildtstar | PROD |
| Eigenheimer | PROD |

---

## 4. `short_recept_stamppot_nl.md`
**Lang/Length:** Dutch / Short (~160 words)

**Summary:** Recept voor klassieke Nederlandse stamppot boerenkool met worst, waarbij gestampte aardappelen worden gecombineerd met krulboerenkool en rookworst. Het recept bevat ingrediënten, stapsgewijze bereidingsinstructies en een seizoensnoot dat stamppot traditioneel van oktober tot maart wordt gegeten in Nederland. Merken Unox en Hema worden vermeld als traditionele rookworstproducenten.

**Tags:** `recept` `hollandse-keuken` `stamppot` `boerenkool` `winter` `comfort-food` `nederland`

**NER:**
| Entity | Type |
|---|---|
| Liesbeth Verhoeven | PER |
| Nederland | LOC |
| Unox | ORG |
| Hema | ORG |
| Albert Heijn | ORG |
| Jumbo | ORG |
| oktober tot maart | DATE |
| Bildtstar | PROD |
| Eigenheimer | PROD |

---

## 5. `short_sports_news_ajax_champions_league_en.md`
**Lang/Length:** English / Short (~210 words)

**Summary:** Ajax defeated Bayern Munich 2-1 at the Johan Cruyff Arena in Amsterdam on April 8, 2025, in the first leg of the UEFA Champions League quarter-final. Goals from Brian Brobbey and Devyne Rensch secured the win, with Harry Kane scoring a late consolation for Bayern. The second leg is scheduled for April 15 at the Allianz Arena in Munich.

**Tags:** `ajax` `champions-league` `uefa` `football` `bayernmunich` `amsterdam` `sports`

**NER:**
| Entity | Type |
|---|---|
| Brian Brobbey | PER |
| Devyne Rensch | PER |
| Harry Kane | PER |
| Francesco Farioli | PER |
| Vincent Kompany | PER |
| Just Spee | PER |
| Ajax | ORG |
| Bayern Munich | ORG |
| UEFA | ORG |
| KNVB | ORG |
| Tottenham Hotspur | ORG |
| Johan Cruyff Arena | LOC |
| Amsterdam | LOC |
| Allianz Arena | LOC |
| Munich | LOC |
| April 8, 2025 | DATE |
| April 15 | DATE |
| 2019 | DATE |
| Champions League | MISC |

---

## 6. `short_sport_nieuws_ajax_champions_league_nl.md`
**Lang/Length:** Dutch / Short (~210 words)

**Summary:** Ajax versloeg Bayern München op 8 april 2025 met 2-1 in de Johan Cruyff Arena in Amsterdam in de eerste wedstrijd van de kwartfinale van de UEFA Champions League. Doelpunten van Brian Brobbey en Devyne Rensch bezorgden Ajax de zege, terwijl Harry Kane laat terugdeed voor Bayern. De return staat gepland voor 15 april op de Allianz Arena in München.

**Tags:** `ajax` `champions-league` `uefa` `voetbal` `bayernmunchen` `amsterdam` `sport`

**NER:**
| Entity | Type |
|---|---|
| Brian Brobbey | PER |
| Devyne Rensch | PER |
| Harry Kane | PER |
| Francesco Farioli | PER |
| Vincent Kompany | PER |
| Just Spee | PER |
| Ajax | ORG |
| Bayern München | ORG |
| UEFA | ORG |
| KNVB | ORG |
| Tottenham Hotspur | ORG |
| Johan Cruyff Arena | LOC |
| Amsterdam | LOC |
| Allianz Arena | LOC |
| München | LOC |
| 8 april 2025 | DATE |
| 15 april | DATE |
| 2019 | DATE |
| Champions League | MISC |

---

## 7. `short_review_samsung_galaxy_s25_ultra_en.md`
**Lang/Length:** English / Short (~190 words)

**Summary:** A product review of the Samsung Galaxy S25 Ultra, which features a Snapdragon 8 Elite chip, 200 MP camera, and costs €1,349. The reviewer benchmarks it against the Apple iPhone 16 Pro Max and Google Pixel 9 Pro, awarding it a 9/10 score. Samsung Galaxy AI features powered by Google Gemini are praised as genuinely useful.

**Tags:** `samsung` `galaxy-s25-ultra` `android` `smartphone` `review` `snapdragon` `camera`

**NER:**
| Entity | Type |
|---|---|
| Joris Hendriksen | PER |
| Samsung | ORG |
| Qualcomm | ORG |
| TSMC | ORG |
| Apple | ORG |
| Google | ORG |
| Galaxy S25 Ultra | PROD |
| Snapdragon 8 Elite | PROD |
| Snapdragon 8 Gen 3 | PROD |
| iPhone 16 Pro Max | PROD |
| Pixel 9 Pro | PROD |
| ISOCELL HP9 | PROD |
| ProVisual Engine | PROD |
| Google Gemini | PROD |
| Geekbench 6 | MISC |

---

## 8. `short_recensie_samsung_galaxy_s25_ultra_nl.md`
**Lang/Length:** Dutch / Short (~190 words)

**Summary:** Een productrecensie van de Samsung Galaxy S25 Ultra met een Snapdragon 8 Elite-chip, 200 MP-camera en een adviesprijs van €1.349. De recensent vergelijkt het toestel met de Apple iPhone 16 Pro Max en Google Pixel 9 Pro en kent een score toe van 9/10. Samsung Galaxy AI-functies aangedreven door Google Gemini worden geroemd als echt nuttig.

**Tags:** `samsung` `galaxy-s25-ultra` `android` `smartphone` `recensie` `snapdragon` `camera`

**NER:**
| Entity | Type |
|---|---|
| Joris Hendriksen | PER |
| Samsung | ORG |
| Qualcomm | ORG |
| TSMC | ORG |
| Apple | ORG |
| Google | ORG |
| Galaxy S25 Ultra | PROD |
| Snapdragon 8 Elite | PROD |
| Snapdragon 8 Gen 3 | PROD |
| iPhone 16 Pro Max | PROD |
| Pixel 9 Pro | PROD |
| ISOCELL HP9 | PROD |
| ProVisual Engine | PROD |
| Google Gemini | PROD |
| Geekbench 6 | MISC |

---

## 9. `medium_climate_blog_paris_agreement_en.md`
**Lang/Length:** English / Medium (~430 words)

**Summary:** Ten years after the Paris Agreement was signed in Le Bourget, France, global CO₂ emissions have reached record levels and temperatures are at 1.45°C above pre-industrial baseline. While the EU has cut emissions by 32%, major emitters like Brazil (deforestation) and India (2070 net zero target) are falling short. The upcoming COP30 summit in Belém, Brazil, is cited as a critical test of international resolve.

**Tags:** `climate-change` `paris-agreement` `ipcc` `emissions` `policy` `cop30` `fossil-fuels` `net-zero`

**NER:**
| Entity | Type |
|---|---|
| Elena Fischer | PER |
| Friederike Otto | PER |
| Pierre Friedlingstein | PER |
| Ursula von der Leyen | PER |
| Luiz Inácio Lula da Silva | PER |
| Greta Thunberg | PER |
| António Guterres | PER |
| Katharine Hayhoe | PER |
| Wael Sawan | PER |
| Le Bourget | LOC |
| France | LOC |
| Brazil | LOC |
| Amazon Basin | LOC |
| São José dos Campos | LOC |
| Belém | LOC |
| IPCC | ORG |
| Grantham Institute | ORG |
| Imperial College London | ORG |
| Global Carbon Project | ORG |
| University of Exeter | ORG |
| International Energy Agency | ORG |
| European Union | ORG |
| INPE | ORG |
| Youth Climate Coalition | ORG |
| Climate Council | ORG |
| InfluenceMap | ORG |
| Shell | ORG |
| BP | ORG |
| ExxonMobil | ORG |
| Saudi Aramco | ORG |
| The Nature Conservancy | ORG |
| Texas Tech University | ORG |
| Ørsted | ORG |
| Iberdrola | ORG |
| BloombergNEF | ORG |
| December 12, 2015 | DATE |
| 2024 | DATE |
| November 2025 | DATE |
| COP30 | MISC |
| Paris Agreement | MISC |
| European Green Deal | MISC |

---

## 10. `medium_klimaat_blog_parijs_akkoord_nl.md`
**Lang/Length:** Dutch / Medium (~430 words)

**Summary:** Tien jaar na het Akkoord van Parijs in Le Bourget, Frankrijk, hebben de mondiale CO₂-emissies recordhoogten bereikt en liggen temperaturen op 1,45°C boven het pre-industriële referentieniveau. Hoewel de EU de uitstoot met 32% heeft verminderd, schieten grote uitstoters als Brazilië (ontbossing) en India (netto-nuldoelstelling 2070) tekort. De aankomende COP30-top in Belém, Brazilië, geldt als een cruciale test voor de internationale vastberadenheid.

**Tags:** `klimaatverandering` `parijs-akkoord` `ipcc` `uitstoot` `beleid` `cop30` `fossiele-brandstoffen` `netto-nul`

**NER:** *(same entities as EN equivalent, in Dutch orthography where applicable)*
| Entity | Type |
|---|---|
| Elena Fischer | PER |
| Friederike Otto | PER |
| Pierre Friedlingstein | PER |
| Ursula von der Leyen | PER |
| Luiz Inácio Lula da Silva | PER |
| Greta Thunberg | PER |
| António Guterres | PER |
| Katharine Hayhoe | PER |
| Wael Sawan | PER |
| Le Bourget | LOC |
| Frankrijk | LOC |
| Brazilië | LOC |
| Amazonegebied | LOC |
| São José dos Campos | LOC |
| Belém | LOC |
| IPCC | ORG |
| Grantham Institute | ORG |
| Imperial College London | ORG |
| Global Carbon Project | ORG |
| Universiteit van Exeter | ORG |
| Internationaal Energieagentschap | ORG |
| Europese Unie | ORG |
| INPE | ORG |
| Youth Climate Coalition | ORG |
| Climate Council | ORG |
| InfluenceMap | ORG |
| Shell | ORG |
| BP | ORG |
| ExxonMobil | ORG |
| Saudi Aramco | ORG |
| The Nature Conservancy | ORG |
| Texas Tech University | ORG |
| Ørsted | ORG |
| Iberdrola | ORG |
| BloombergNEF | ORG |
| 12 december 2015 | DATE |
| 2024 | DATE |
| november 2025 | DATE |
| COP30 | MISC |
| Akkoord van Parijs | MISC |
| Europese Green Deal | MISC |

---

## 11. `medium_history_dutch_golden_age_en.md`
**Lang/Length:** English / Medium (~380 words)

**Summary:** An encyclopaedic overview of the Dutch Golden Age (1588-1702), covering the founding of the VOC in Amsterdam in 1602 and its role in global trade from Batavia to New Amsterdam. The article covers major artists Rembrandt van Rijn and Johannes Vermeer, scientists Christiaan Huygens and Antonie van Leeuwenhoek, and philosopher Baruch Spinoza. The Dutch government's 2022 apology for the WIC's role in the transatlantic slave trade is noted.

**Tags:** `dutch-history` `golden-age` `voc` `rembrandt` `amsterdam` `17th-century` `trade` `colonialism`

**NER:**
| Entity | Type |
|---|---|
| Hanneke Oosterhout | PER |
| Jan Pieterszoon Coen | PER |
| Rembrandt van Rijn | PER |
| Johannes Vermeer | PER |
| Christiaan Huygens | PER |
| Antonie van Leeuwenhoek | PER |
| Baruch Spinoza | PER |
| Nicolaes Tulp | PER |
| Amsterdam | LOC |
| Leiden | LOC |
| Delft | LOC |
| The Hague | LOC |
| Batavia | LOC |
| New Amsterdam | LOC |
| West Africa | LOC |
| Brazil | LOC |
| Maluku Islands | LOC |
| Republic of the Seven United Netherlands | ORG |
| VOC (Vereenigde Oost-Indische Compagnie) | ORG |
| WIC (Westindische Compagnie) | ORG |
| Amsterdam Stock Exchange | ORG |
| UNESCO | ORG |
| March 20, 1602 | DATE |
| 1619 | DATE |
| 1621 | DATE |
| 1642 | DATE |
| 1656 | DATE |
| 1674 | DATE |
| December 2022 | DATE |
| The Night Watch | MISC |
| The Anatomy Lesson of Dr. Nicolaes Tulp | MISC |
| Girl with a Pearl Earring | MISC |
| Ethics | MISC |
| Franco-Dutch War | MISC |
| Glorious Revolution | MISC |
| Grachtengordel | MISC |

---

## 12. `medium_geschiedenis_gouden_eeuw_nl.md`
**Lang/Length:** Dutch / Medium (~380 words)

**Summary:** Een encyclopedisch overzicht van de Nederlandse Gouden Eeuw (1588-1702), met de oprichting van de VOC in Amsterdam in 1602 en haar rol in de wereldhandel van Batavia tot Nieuw-Amsterdam. Het artikel behandelt grote kunstenaars Rembrandt van Rijn en Johannes Vermeer, wetenschappers Christiaan Huygens en Antonie van Leeuwenhoek, en filosoof Baruch Spinoza. De excuses van de Nederlandse regering in 2022 voor de rol van de WIC in de trans-Atlantische slavenhandel worden vermeld.

**Tags:** `nederlandse-geschiedenis` `gouden-eeuw` `voc` `rembrandt` `amsterdam` `17e-eeuw` `handel` `kolonialisme`

**NER:**
| Entity | Type |
|---|---|
| Hanneke Oosterhout | PER |
| Jan Pieterszoon Coen | PER |
| Rembrandt van Rijn | PER |
| Johannes Vermeer | PER |
| Christiaan Huygens | PER |
| Antonie van Leeuwenhoek | PER |
| Baruch Spinoza | PER |
| Nicolaes Tulp | PER |
| Amsterdam | LOC |
| Leiden | LOC |
| Delft | LOC |
| Den Haag | LOC |
| Batavia | LOC |
| Nieuw-Amsterdam | LOC |
| West-Afrika | LOC |
| Brazilië | LOC |
| Molukken | LOC |
| Republiek der Zeven Verenigde Nederlanden | ORG |
| VOC (Vereenigde Oost-Indische Compagnie) | ORG |
| WIC (Westindische Compagnie) | ORG |
| Amsterdamse Effectenbeurs | ORG |
| UNESCO | ORG |
| 20 maart 1602 | DATE |
| 1619 | DATE |
| 1621 | DATE |
| 1642 | DATE |
| 1656 | DATE |
| 1674 | DATE |
| december 2022 | DATE |
| De Nachtwacht | MISC |
| De Anatomische Les van Dr. Nicolaes Tulp | MISC |
| Meisje met de parel | MISC |
| Ethica | MISC |
| Frans-Nederlandse Oorlog | MISC |
| Glorieuze Revolutie | MISC |
| Grachtengordel | MISC |

---

## 13. `medium_travel_guide_amsterdam_en.md`
**Lang/Length:** English / Medium (~470 words)

**Summary:** A practical 2025 travel guide to Amsterdam covering transport (Schiphol airport, GVB trams, cycling), must-see museums (Rijksmuseum, Van Gogh Museum, Anne Frank House), neighbourhoods (Jordaan, Amsterdam-Noord, NDSM Wharf), and dining (Café de Jaren, Restaurant Blauw). The guide also notes Amsterdam's overtourism policies under Mayor Femke Halsema, including a €3 tourist tax and Airbnb restrictions.

**Tags:** `amsterdam` `travel` `netherlands` `museums` `food` `cycling` `tourism` `jordaan` `canal`

**NER:**
| Entity | Type |
|---|---|
| Clara van Houten | PER |
| Femke Halsema | PER |
| Vincent van Gogh | PER |
| Anne Frank | PER |
| Rembrandt | PER |
| Amsterdam | LOC |
| Jordaan | LOC |
| Amsterdam-Noord | LOC |
| NDSM Wharf | LOC |
| De Wallen | LOC |
| Museumplein | LOC |
| Museumstraat | LOC |
| Westermarkt | LOC |
| Amstel River | LOC |
| Amstelveenseweg | LOC |
| Netherlands | LOC |
| Paris | LOC |
| London | LOC |
| Royal Schiphol Group | ORG |
| GVB | ORG |
| MacBike | ORG |
| Black Bikes | ORG |
| Rijksmuseum | ORG |
| Van Gogh Museum | ORG |
| Anne Frank House | ORG |
| Café de Jaren | ORG |
| Restaurant Blauw | ORG |
| 2025 | DATE |
| 2023 | DATE |
| 1942–1944 | DATE |
| OV-chipkaart | MISC |
| Intercity Direct | MISC |
| De Negen Straatjes | MISC |

---

## 14. `medium_reisgids_amsterdam_nl.md`
**Lang/Length:** Dutch / Medium (~470 words)

**Summary:** Een praktische reisgids voor Amsterdam in 2025 met informatie over vervoer (Schiphol, GVB trams, fietsen), must-see musea (Rijksmuseum, Van Gogh Museum, Anne Frank Huis), wijken (Jordaan, Amsterdam-Noord, NDSM-werf) en eten (Café de Jaren, Restaurant Blauw). De gids vermeldt ook Amsterdams overtoerismebeleid onder burgemeester Femke Halsema, inclusief een toeristenbelasting van €3 en Airbnb-beperkingen.

**Tags:** `amsterdam` `reizen` `nederland` `musea` `eten` `fietsen` `toerisme` `jordaan` `gracht`

**NER:**
| Entity | Type |
|---|---|
| Clara van Houten | PER |
| Femke Halsema | PER |
| Vincent van Gogh | PER |
| Anne Frank | PER |
| Rembrandt | PER |
| Amsterdam | LOC |
| Jordaan | LOC |
| Amsterdam-Noord | LOC |
| NDSM-werf | LOC |
| De Wallen | LOC |
| Museumplein | LOC |
| Museumstraat | LOC |
| Westermarkt | LOC |
| Amstel | LOC |
| Amstelveenseweg | LOC |
| Nederland | LOC |
| Parijs | LOC |
| Londen | LOC |
| Royal Schiphol Group | ORG |
| GVB | ORG |
| MacBike | ORG |
| Black Bikes | ORG |
| Rijksmuseum | ORG |
| Van Gogh Museum | ORG |
| Anne Frank Huis | ORG |
| Café de Jaren | ORG |
| Restaurant Blauw | ORG |
| 2025 | DATE |
| 2023 | DATE |
| 1942–1944 | DATE |
| OV-chipkaart | MISC |
| Intercity Direct | MISC |
| De Negen Straatjes | MISC |

---

## 15. `long_ai_healthcare_oncology_research_en.md`
**Lang/Length:** English / Long (~830 words)

**Summary:** A clinical trial at Amsterdam UMC involving 2,847 patients found that AI-assisted pathology (PathAI Colorectal Classifier v3.1) improved early-stage colorectal cancer diagnostic accuracy from 91.7% to 96.3% and reduced reporting time by 38.7%. The trial, led by Dr. Jan de Vries and Prof. Maria Santos, was published in The Lancet Digital Health and received CE marking under EU MDR. Philips Healthcare and PathAI announced a commercial partnership to roll out the technology to 35 Dutch hospitals by Q1 2026.

**Tags:** `ai` `oncology` `cancer-diagnosis` `amsterdam-umc` `deep-learning` `pathology` `clinical-trial` `healthcare` `machine-learning`

**NER:**
| Entity | Type |
|---|---|
| Jan de Vries | PER |
| Maria Santos | PER |
| Kwame Asante | PER |
| Eric Lim | PER |
| Mariana Costa | PER |
| Amsterdam | LOC |
| Nijmegen | LOC |
| Rotterdam | LOC |
| Groningen | LOC |
| Maastricht | LOC |
| Utrecht | LOC |
| Boston | LOC |
| London | LOC |
| Amsterdam UMC | ORG |
| Academic Medical Center (AMC) | ORG |
| VU University Medical Center (VUmc) | ORG |
| Cancer Center Amsterdam | ORG |
| Radboud University Medical Center | ORG |
| Erasmus MC | ORG |
| UMCG | ORG |
| Maastricht UMC+ | ORG |
| KNAW | ORG |
| Dutch Cancer Registry (IKNL) | ORG |
| Dutch Association of Pathology (NVVP) | ORG |
| PathAI Inc. | ORG |
| Google Health | ORG |
| Delft University of Technology | ORG |
| ZonMW | ORG |
| Autoriteit Persoonsgegevens | ORG |
| SURFsara | ORG |
| SURF | ORG |
| Royal Brompton Hospital | ORG |
| European Society for Medical Oncology (ESMO) | ORG |
| KWF Kankerbestrijding | ORG |
| European Research Council (ERC) | ORG |
| Philips Healthcare | ORG |
| The Lancet Digital Health | MISC |
| January 2023 | DATE |
| December 2024 | DATE |
| June 3, 2025 | DATE |
| November 2024 | DATE |
| Q1 2026 | DATE |
| 2027 | DATE |
| PathAI Colorectal Classifier v3.1 | PROD |
| IntelliSite Pathology Solution | PROD |
| Horizon Europe | MISC |
| EU Medical Device Regulation (MDR 2017/745) | MISC |
| Declaration of Helsinki | MISC |

---

## 16. `long_ai_gezondheidszorg_oncologie_onderzoek_nl.md`
**Lang/Length:** Dutch / Long (~830 words)

**Summary:** Een klinische studie bij Amsterdam UMC met 2.847 patiënten toonde aan dat AI-ondersteunde pathologie (PathAI Colorectal Classifier v3.1) de diagnostische nauwkeurigheid voor vroegstadium darmkanker verbeterde van 91,7% naar 96,3% en de rapportagetijd met 38,7% verkortte. De studie, geleid door dr. Jan de Vries en prof. Maria Santos, werd gepubliceerd in The Lancet Digital Health en ontving CE-markering onder EU MDR. Philips Healthcare en PathAI kondigden een commercieel partnerschap aan om de technologie vóór Q1 2026 uit te rollen naar 35 Nederlandse ziekenhuizen.

**Tags:** `ai` `oncologie` `kankerdiagnose` `amsterdam-umc` `deep-learning` `pathologie` `klinisch-onderzoek` `gezondheidszorg` `machinaal-leren`

**NER:** *(same entities as EN equivalent, with Dutch name variants where applicable)*
| Entity | Type |
|---|---|
| Jan de Vries | PER |
| Maria Santos | PER |
| Kwame Asante | PER |
| Eric Lim | PER |
| Mariana Costa | PER |
| Amsterdam | LOC |
| Nijmegen | LOC |
| Rotterdam | LOC |
| Groningen | LOC |
| Maastricht | LOC |
| Utrecht | LOC |
| Boston | LOC |
| Londen | LOC |
| Amsterdam UMC | ORG |
| Academisch Medisch Centrum (AMC) | ORG |
| VU Universitair Medisch Centrum (VUmc) | ORG |
| Cancer Center Amsterdam | ORG |
| Radboud Universitair Medisch Centrum | ORG |
| Erasmus MC | ORG |
| UMCG | ORG |
| Maastricht UMC+ | ORG |
| KNAW | ORG |
| Nederlandse Kankerregistratie (IKNL) | ORG |
| Nederlandse Vereniging voor Pathologie (NVVP) | ORG |
| PathAI Inc. | ORG |
| Google Health | ORG |
| Technische Universiteit Delft | ORG |
| ZonMW | ORG |
| Autoriteit Persoonsgegevens | ORG |
| SURFsara | ORG |
| SURF | ORG |
| Royal Brompton Hospital | ORG |
| European Society for Medical Oncology (ESMO) | ORG |
| KWF Kankerbestrijding | ORG |
| Europese Onderzoeksraad (ERC) | ORG |
| Philips Healthcare | ORG |
| The Lancet Digital Health | MISC |
| januari 2023 | DATE |
| december 2024 | DATE |
| 3 juni 2025 | DATE |
| november 2024 | DATE |
| Q1 2026 | DATE |
| 2027 | DATE |
| PathAI Colorectal Classifier v3.1 | PROD |
| IntelliSite Pathology Solution | PROD |
| Horizon Europe | MISC |
| EU MDR 2017/745 | MISC |
| Verklaring van Helsinki | MISC |

---

## 17. `long_interview_climate_scientist_sea_level_en.md`
**Lang/Length:** English / Long (~720 words)

**Summary:** An interview with Dr. Maria van den Berg, professor of coastal hydrology at TU Delft and senior fellow at Deltares, about sea level rise risks to the Netherlands. She warns that current Dutch flood defence standards are based on outdated projections and advocates for adaptive pathway planning, citing Rotterdam as a world leader in adaptation. She criticises the Schoof cabinet's €14 million cut to KNMI's budget as a false economy that undermines the science needed to design flood defences.

**Tags:** `climate-science` `sea-level-rise` `netherlands` `delta-works` `rotterdam` `interview` `knmi` `deltares` `flooding`

**NER:**
| Entity | Type |
|---|---|
| Maria van den Berg | PER |
| Tobias Schout | PER |
| Peter Glas | PER |
| Mona Keijzer | PER |
| Delft | LOC |
| Rotterdam | LOC |
| Zeeland | LOC |
| Benthemplein | LOC |
| Rijnhaven | LOC |
| Netherlands | LOC |
| Greenland | LOC |
| Antarctica | LOC |
| West Antarctica | LOC |
| Sharm el-Sheikh | LOC |
| Delft University of Technology (TU Delft) | ORG |
| Deltares | ORG |
| NWO | ORG |
| IPCC | ORG |
| KNMI | ORG |
| ECMWF | ORG |
| NOAA | ORG |
| Municipality of Rotterdam | ORG |
| Port of Rotterdam Authority | ORG |
| Ministry of Infrastructure and Water Management | ORG |
| De Urbanisten | ORG |
| WUR | ORG |
| Utrecht University | ORG |
| VU Amsterdam | ORG |
| NRC | ORG |
| 1997 | DATE |
| 2017 | DATE |
| November 2024 | DATE |
| 1953 | DATE |
| 1854 | DATE |
| Oosterscheldekering | MISC |
| Maeslantkering | MISC |
| Haringvlietdam | MISC |
| Delta Works | MISC |
| Dutch Water Act | MISC |
| Haarlemmermeer | MISC |
| Zuiderzeewerken | MISC |
| Water Square | MISC |
| RISES-AM | MISC |
| SSP5-8.5 | MISC |
| COP27 | MISC |

---

## 18. `long_interview_klimaatwetenschapper_zeespiegel_nl.md`
**Lang/Length:** Dutch / Long (~720 words)

**Summary:** Een interview met dr. Maria van den Berg, hoogleraar kustwaterhuishouding aan TU Delft en senior fellow bij Deltares, over de risico's van zeespiegelstijging voor Nederland. Ze waarschuwt dat de huidige Nederlandse waterkerings-normen zijn gebaseerd op verouderde prognoses en pleit voor adaptief padontwerp, waarbij Rotterdam wordt aangehaald als wereldleider op het gebied van adaptatie. Ze bekritiseert de bezuiniging van het kabinet-Schoof van 14 miljoen euro op het KNMI-budget als een schijnbesparing die de wetenschap ondermijnt die nodig is om waterkeringen te ontwerpen.

**Tags:** `klimaatwetenschap` `zeespiegelstijging` `nederland` `deltawerken` `rotterdam` `interview` `knmi` `deltares` `overstromingen`

**NER:**
| Entity | Type |
|---|---|
| Maria van den Berg | PER |
| Tobias Schout | PER |
| Peter Glas | PER |
| Mona Keijzer | PER |
| Delft | LOC |
| Rotterdam | LOC |
| Zeeland | LOC |
| Benthemplein | LOC |
| Rijnhaven | LOC |
| Nederland | LOC |
| Groenland | LOC |
| Antarctica | LOC |
| West-Antarctica | LOC |
| Sharm el-Sheikh | LOC |
| Technische Universiteit Delft (TU Delft) | ORG |
| Deltares | ORG |
| NWO | ORG |
| IPCC | ORG |
| KNMI | ORG |
| ECMWF | ORG |
| NOAA | ORG |
| Gemeente Rotterdam | ORG |
| Havenbedrijf Rotterdam | ORG |
| Ministerie van Infrastructuur en Waterstaat | ORG |
| De Urbanisten | ORG |
| WUR | ORG |
| Universiteit Utrecht | ORG |
| VU Amsterdam | ORG |
| NRC | ORG |
| 1997 | DATE |
| 2017 | DATE |
| november 2024 | DATE |
| 1953 | DATE |
| 1854 | DATE |
| Oosterscheldekering | MISC |
| Maeslantkering | MISC |
| Haringvlietdam | MISC |
| Deltawerken | MISC |
| Waterwet | MISC |
| Haarlemmermeer | MISC |
| Zuiderzeewerken | MISC |
| Waterplein | MISC |
| RISES-AM | MISC |
| SSP5-8.5 | MISC |
| COP27 | MISC |
| Watersnoodramp | MISC |
| kabinet-Schoof | MISC |

---

## 19. `long_opinion_eu_ai_act_digital_policy_en.md`
**Lang/Length:** English / Long (~780 words)

**Summary:** An opinion piece arguing that while the EU AI Act is a genuine regulatory achievement, its implementation is undermined by slow member-state enforcement, lobbying-induced dilution, and structural timing lags behind fast-moving AI development. The author compares the Act's likely trajectory to the GDPR's slow enforcement and argues that effective AI governance also requires European sovereign compute, a transatlantic agreement, civil society funding, and clarity on what fundamental rights the regulation is meant to protect.

**Tags:** `eu-ai-act` `digital-policy` `european-union` `regulation` `chatgpt` `facial-recognition` `gdpr` `fundamental-rights` `big-tech`

**NER:**
| Entity | Type |
|---|---|
| Thomas Weber | PER |
| Ursula von der Leyen | PER |
| Margrethe Vestager | PER |
| Max Schrems | PER |
| Matt Clifford | PER |
| Yoshua Bengio | PER |
| European Union | LOC |
| Brussels | LOC |
| Dublin | LOC |
| Berlin | LOC |
| European Parliament | ORG |
| European Commission | ORG |
| European AI Office | ORG |
| DG CONNECT | ORG |
| Internal Market and Consumer Protection Committee (IMCO) | ORG |
| Irish Data Protection Commission (DPC) | ORG |
| Meta | ORG |
| Microsoft | ORG |
| Palantir | ORG |
| IBM | ORG |
| Apple | ORG |
| Google | ORG |
| OpenAI | ORG |
| AlgorithmWatch | ORG |
| Bits of Freedom | ORG |
| Gesellschaft für Freiheitsrechte | ORG |
| Access Now | ORG |
| noyb (None of Your Business) | ORG |
| UK AI Safety Institute | ORG |
| The Guardian | ORG |
| EuroHPC | ORG |
| March 13, 2024 | DATE |
| April 2021 | DATE |
| August 2025 | DATE |
| May 2018 | DATE |
| January 2023 | DATE |
| November 2024 | DATE |
| October 2023 | DATE |
| GPT-4 | PROD |
| GPT-5 | PROD |
| Gemini | PROD |
| Llama | PROD |
| Claude | PROD |
| EU AI Act | MISC |
| GDPR | MISC |
| CPRA | MISC |
| EU Charter of Fundamental Rights | MISC |

---

## 20. `long_opinie_eu_ai_act_digitaal_beleid_nl.md`
**Lang/Length:** Dutch / Long (~780 words)

**Summary:** Een opiniestuk dat betoogt dat de EU AI Act, hoewel een echte regelgevende prestatie, wordt ondermijnd door trage handhaving door lidstaten, lobbyinvloeden die tot verdunning hebben geleid en structurele tijdsvertragingen achter snelle AI-ontwikkeling. De auteur vergelijkt het waarschijnlijke traject van de wet met de trage handhaving van de AVG en betoogt dat effectieve AI-governance ook Europese soevereine computerinfrastructuur, een trans-Atlantische overeenkomst, civiele samenlevingfinanciering en duidelijkheid vereist over welke grondrechten de regelgeving beoogt te beschermen.

**Tags:** `eu-ai-act` `digitaal-beleid` `europese-unie` `regelgeving` `chatgpt` `gezichtsherkenning` `avg` `grondrechten` `big-tech`

**NER:**
| Entity | Type |
|---|---|
| Thomas Weber | PER |
| Ursula von der Leyen | PER |
| Margrethe Vestager | PER |
| Max Schrems | PER |
| Matt Clifford | PER |
| Yoshua Bengio | PER |
| Europese Unie | LOC |
| Brussel | LOC |
| Dublin | LOC |
| Berlijn | LOC |
| Europees Parlement | ORG |
| Europese Commissie | ORG |
| European AI Office | ORG |
| DG CONNECT | ORG |
| Commissie IMCO | ORG |
| Ierse Data Protection Commission (DPC) | ORG |
| Meta | ORG |
| Microsoft | ORG |
| Palantir | ORG |
| IBM | ORG |
| Apple | ORG |
| Google | ORG |
| OpenAI | ORG |
| AlgorithmWatch | ORG |
| Bits of Freedom | ORG |
| Gesellschaft für Freiheitsrechte | ORG |
| Access Now | ORG |
| noyb (None of Your Business) | ORG |
| UK AI Safety Institute | ORG |
| The Guardian | ORG |
| EuroHPC | ORG |
| Autoriteit Persoonsgegevens (AP) | ORG |
| 13 maart 2024 | DATE |
| april 2021 | DATE |
| augustus 2025 | DATE |
| mei 2018 | DATE |
| januari 2023 | DATE |
| november 2024 | DATE |
| oktober 2023 | DATE |
| GPT-4 | PROD |
| GPT-5 | PROD |
| Gemini | PROD |
| Llama | PROD |
| Claude | PROD |
| EU AI Act | MISC |
| AVG | MISC |
| CPRA | MISC |
| EU-Handvest van de grondrechten | MISC |

---

## Corpus Summary

| # | Filename | Lang | Length | Word count (approx) |
|---|---|---|---|---|
| 1 | short_tech_news_openai_announcement_en.md | EN | Short | ~220 |
| 2 | short_tech_nieuws_openai_aankondiging_nl.md | NL | Short | ~220 |
| 3 | short_recipe_dutch_stamppot_en.md | EN | Short | ~160 |
| 4 | short_recept_stamppot_nl.md | NL | Short | ~160 |
| 5 | short_sports_news_ajax_champions_league_en.md | EN | Short | ~210 |
| 6 | short_sport_nieuws_ajax_champions_league_nl.md | NL | Short | ~210 |
| 7 | short_review_samsung_galaxy_s25_ultra_en.md | EN | Short | ~190 |
| 8 | short_recensie_samsung_galaxy_s25_ultra_nl.md | NL | Short | ~190 |
| 9 | medium_climate_blog_paris_agreement_en.md | EN | Medium | ~430 |
| 10 | medium_klimaat_blog_parijs_akkoord_nl.md | NL | Medium | ~430 |
| 11 | medium_history_dutch_golden_age_en.md | EN | Medium | ~380 |
| 12 | medium_geschiedenis_gouden_eeuw_nl.md | NL | Medium | ~380 |
| 13 | medium_travel_guide_amsterdam_en.md | EN | Medium | ~470 |
| 14 | medium_reisgids_amsterdam_nl.md | NL | Medium | ~470 |
| 15 | long_ai_healthcare_oncology_research_en.md | EN | Long | ~830 |
| 16 | long_ai_gezondheidszorg_oncologie_onderzoek_nl.md | NL | Long | ~830 |
| 17 | long_interview_climate_scientist_sea_level_en.md | EN | Long | ~720 |
| 18 | long_interview_klimaatwetenschapper_zeespiegel_nl.md | NL | Long | ~720 |
| 19 | long_opinion_eu_ai_act_digital_policy_en.md | EN | Long | ~780 |
| 20 | long_opinie_eu_ai_act_digitaal_beleid_nl.md | NL | Long | ~780 |
