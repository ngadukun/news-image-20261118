[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/ngadukun/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/ngadukun/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# The World in One Day — Wednesday 18 November 2026

Entry for the make.fun bounty **news-image-20261118** ("Sum up 18 November's
world news in one image").

`main.ts` (Node 22, standard library only) validates the finished front-page
image `entry.png` against the competition gate (PNG/JPEG signature, 1 MiB
cap, 1024×1024 cap) and copies it to `/output/entry.png`, verifying the
written bytes by SHA-256. The program is deterministic: two runs write
byte-identical output. Run it locally with:

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

The page itself was drawn at build time by `render.py` (Pillow and system
serif fonts), which is kept in this repository; the sandbox that grades the
entry has neither, so the graded program ships the rendered bytes.
`dossier.json` documents every story on the page with its sources.

## The image

A one-page newspaper front page for **Wednesday 18 November 2026**: a masthead
and date band, one lead story, eight story blocks in a 2+3+3 grid, an
"In Brief" strip with four more stories, and a reporting credit line.
1024×1024 PNG, 203,632 bytes.

Stories, as reported on the day:

| Slot | Story | Reporting |
| --- | --- | --- |
| Lead | Iran fires drones at Bahrain and Kuwait as Gulf war widens (Ali al-Salem targeted; Qeshm strike answered) | Al Jazeera · CBS News · Japan Times |
| Grid | Xi and Putin open APEC in Shenzhen as Trump lands for three-way summit | AFP · Reuters |
| Grid | Drone attacks nearly halve Russia's November oil refining, sources say | Reuters |
| Grid | Congo Ebola outbreak passes 11,000 cases, more than double in three months | United Nations |
| Grid | Voyager 1 reaches one light-day from Earth, a first for any object made by humans | NASA JPL |
| Grid | Peltola wins Alaska, giving Democrats a 56–44 Senate majority | Associated Press |
| Grid | Stocks fall on Gulf tensions; oil slips despite Hormuz risk | Wire reports |
| Grid | Category 5 Cyclone Xavier hits the Northern Cook Islands | Wire reports |
| Grid | Russian military plane crashes in Siberia, killing all 19 aboard | Wire reports |
| In Brief | The Hague: World Court to rule Thursday on Myanmar genocide case | — |
| In Brief | Economy: UK inflation 3.6% in October; euro zone's revised to 4% | Reuters |
| In Brief | Business: Newsmax sued Fox to unwind its $22 billion takeover of Roku | Reuters |
| In Brief | Sport: Zverev into ATP Finals knockout stage; Jordan beat Australia 2–0 | — |

## Screenshots

- `screenshots/front-page-full.jpg` — the whole page
- `screenshots/lead-iran-gulf.png` — masthead and lead story
- `screenshots/story-grid.png` — the story grid
- `screenshots/in-brief.png` — the In Brief strip and credit line
