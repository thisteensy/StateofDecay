# State of Decay

An interactive map of political protests, demonstrations, marches, and strikes in the United States from January 2017 to the present.

**[View the map →](https://thisteensy.github.io/StateofDecay/protest_map.html)**

---

## What is this?

This visualization maps nearly a decade of protest activity across the United States — from the Women's March in January 2017 through the anti-deportation wave of early 2026. Each dot on the map represents a real event: a march, a rally, a walkout, a vigil, a strike. The size of the dot reflects the estimated crowd size where known. The color reflects the type of event.

Scrub through the timeline at the bottom to watch the decade unfold. Hit play and watch it animate. Zoom in to explore individual cities. Click any dot to open a detail panel showing what people were saying and chanting.

Some things you might notice:

- The extraordinary geographic spread of the Movement for Black Lives in June 2020
- The wave of school walkouts in spring 2018 following the Parkland shooting
- How protest activity shifted from marches and protests toward demonstrations and strikes after 2021
- The surge of anti-ICE and anti-deportation activity in January 2026 following the death of Renee Good

---

## The data

The underlying data comes from the [Crowd Counting Consortium](https://sites.google.com/view/crowdcountingconsortium/home), a research project co-directed by faculty at Harvard University and the University of Connecticut. CCC systematically documents political crowds in the United States using news reports, social media, and public submissions.

The dataset covers three phases:

| Period | Source |
|--------|--------|
| 2017–2020 | Harvard Dataverse ([DOI: 10.7910/DVN/YQAUMR](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YQAUMR)) |
| 2021–2024 | Harvard Dataverse ([DOI: 10.7910/DVN/9MMYDI](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/9MMYDI)) |
| 2025–present | Harvard Dataverse ([DOI: 10.7910/DVN/RI9JFU](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/RI9JFU)) |

The three datasets use different schemas and naming conventions — this project normalizes them into a single consistent format. The 2025-present data is updated weekly by CCC; this repository automatically downloads and regenerates the visualization data every Wednesday via GitHub Actions.

Crowd size estimates are inherently imprecise and often contested. Where a range is given (low/high), this map displays the midpoint. Events without size estimates appear as small fixed-size dots. Roughly 37% of events in the dataset have crowd size estimates.

---

## How it works

The map is a single HTML file using [D3.js](https://d3js.org/) for both the geographic visualization and the timeline. No backend, no framework, no build step.

**Key technical details:**
- US state boundaries from [us-atlas](https://github.com/topojson/us-atlas) via jsDelivr
- Map projection: `d3.geoAlbersUsa`
- Circle sizing: square root scale, domain 1–1,100,000, range 1.5–18px
- Tooltip hit detection: [Voronoi tessellation](https://en.wikipedia.org/wiki/Voronoi_diagram) over visible dots, active at zoom level ≥ 2
- Event clustering: dots within 24px screen-space are grouped into a single tooltip
- Data normalization: `normalize.py` merges and cleans the three source files

**To run locally:**
```bash
git clone https://github.com/thisteensy/StateofDecay.git
cd StateofDecay
python3 -m http.server 8080
# Open http://localhost:8080/protest_map.html
```

---

## Major events annotated

The timeline highlights the following coordinated national events in blue (or amber for January 6):

| Date | Event |
|------|-------|
| Jan 21, 2017 | Women's March |
| Apr 22, 2017 | March for Science |
| Mar 14, 2018 | National School Walkout |
| Mar 24, 2018 | March for Our Lives |
| Jun 30, 2018 | Families Belong Together |
| Nov 8, 2018 | Rally to Protect Mueller Investigation |
| Jul 12, 2019 | Lights for Liberty |
| Sep 20, 2019 | Global Climate Strike |
| Dec 17, 2019 | Impeach Trump |
| May 28 – Jun 14, 2020 | Movement for Black Lives uprising |
| Jan 6, 2021 | Capitol rally |
| Oct 2, 2021 | Abortion rights day of action |
| May 14, 2022 | Abortion rights day of action |
| Jun 24, 2022 | Response to Dobbs decision |
| Oct 2, 2022 | Women's Wave |
| Apr 5, 2025 | Hands Off! |
| Apr 19, 2025 | Hands Off! II |
| Jun 14, 2025 | No Kings |
| Oct 18, 2025 | No Kings II |
| Jan 10, 2026 | Justice for Renee Good |
| Jan 20, 2026 | Inauguration protests |
| Jan 30, 2026 | Anti-deportation wave |

---

## Data attribution

All protest data is sourced from the Crowd Counting Consortium. If you use this data in your own work, please cite the CCC directly. This project is an independent visualization and is not affiliated with or endorsed by the Crowd Counting Consortium, Harvard University, or the University of Connecticut.

> Crowd Counting Consortium. *Protest event data, United States, 2017–present.* Harvard Dataverse.

---

## License

The visualization code is MIT licensed. The underlying protest data is the intellectual property of the Crowd Counting Consortium — please refer to their terms for any research use.# StateofDecay
Visualization of Crowd Counting Consortium US Protest Data
