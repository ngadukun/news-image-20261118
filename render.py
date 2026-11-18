#!/usr/bin/env python3
"""Build-time renderer for the news-image-20261118 entry.

Draws the one-page newspaper front page for Wednesday 18 November 2026 and
writes entry.png (1024x1024). This script is a build tool only: it runs on
the author's machine with Pillow and system serif fonts. The graded program
is main.ts (Node 22, standard library only), which copies entry.png to
/output/entry.png in the sandbox, where no fonts or Pillow exist.

Every headline and fact below is the news of Wednesday 18 November 2026 as
reported that day; see dossier.json for story-by-story sources.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
MARGIN = 40
CW = W - 2 * MARGIN  # content width

PAPER = (248, 244, 235)
INK = (20, 19, 16)
GRAY = (96, 92, 84)
RED = (142, 31, 31)
NAVY = (31, 58, 110)
GREEN = (30, 91, 58)

F = "/usr/share/fonts/truetype"
SERIF_BLACK = f"{F}/noto/NotoSerifDisplay-Black.ttf"
SERIF_BOLD = f"{F}/noto/NotoSerif-Bold.ttf"
SANS = f"{F}/noto/NotoSans-Regular.ttf"
SANS_BOLD = f"{F}/noto/NotoSans-Bold.ttf"
SANS_OBL = f"{F}/noto/NotoSans-Italic.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def text_w(s, fnt):
    return d.textlength(s, font=fnt)


def wrap(text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        trial = f"{cur} {w_}".strip()
        if text_w(trial, fnt) <= width:
            cur = trial
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def centered(text, y, fnt, fill=INK, spacing=0):
    if spacing:
        total = sum(text_w(ch, fnt) for ch in text) + spacing * (len(text) - 1)
        x = (W - total) / 2
        for ch in text:
            d.text((x, y), ch, font=fnt, fill=fill)
            x += text_w(ch, fnt) + spacing
    else:
        d.text(((W - text_w(text, fnt)) / 2, y), text, font=fnt, fill=fill)


def rule(y, thickness=2, x0=MARGIN, x1=W - MARGIN):
    d.rectangle([x0, y, x1, y + thickness - 1], fill=INK)


def block(x, y, width, color, kicker, headline, body, credit,
          head_size, body_size=16, head_lh=1.08, body_lh=1.26):
    """Draw one story block; return the y just below its credit line."""
    kf = font(SANS_BOLD, 15)
    d.rectangle([x, y + 3, x + 26, y + 9], fill=color)
    d.text((x + 34, y), kicker, font=kf, fill=color)
    y += 24
    hf = font(SERIF_BOLD, head_size)
    for line in wrap(headline, hf, width):
        d.text((x, y), line, font=hf, fill=INK)
        y += int(head_size * head_lh)
    y += 4
    bf = font(SANS, body_size)
    for line in wrap(body, bf, width):
        d.text((x, y), line, font=bf, fill=INK)
        y += int(body_size * body_lh)
    y += 3
    d.text((x, y), credit, font=font(SANS_OBL, 13), fill=GRAY)
    return y + 14


# ---- masthead -------------------------------------------------------------
centered("ONE DAY · ONE IMAGE · THE WORLD'S NEWS", 28, font(SANS, 15),
         fill=GRAY, spacing=3)
rule(60, 3)

mast = "THE WORLD IN ONE DAY"
size = 66
while text_w(mast, font(SERIF_BLACK, size)) > CW:
    size -= 1
centered(mast, 74, font(SERIF_BLACK, size))

band_y = 150
d.rectangle([MARGIN, band_y, W - MARGIN, band_y + 50], fill=INK)
date = "WEDNESDAY · 18 NOVEMBER 2026"
df = font(SANS_BOLD, 29)
d.text(((W - text_w(date, df)) / 2, band_y + 10), date, font=df,
       fill=(255, 255, 255))
rule(band_y + 58, 2)

# ---- lead -----------------------------------------------------------------
y = block(
    MARGIN, band_y + 62, CW, RED,
    "IRAN WAR · THE GULF",
    "Iran fires drones at Bahrain and Kuwait as Gulf war widens",
    "Bahrain and Kuwait said they intercepted drones and missiles after "
    "Iran's army targeted Ali al-Salem air base, a day after U.S. jets "
    "struck a Revolutionary Guard missile site on Qeshm Island. Saudi "
    "Arabia condemned the attacks; Qatar announced new talks with Iran.",
    "Al Jazeera · CBS News · Japan Times",
    head_size=36,
)
rule(y + 2, 2)
y += 8

# ---- grid row A: two columns ----------------------------------------------
col2 = (CW - 16) // 2
ya = block(
    MARGIN, y, col2, NAVY,
    "APEC · SHENZHEN",
    "Xi and Putin open APEC in Shenzhen as Trump lands for three-way summit",
    "Xi pledged to fight trade protectionism and Putin attacked Western "
    "sanctions as the summit opened. Trump landed in Shenzhen on "
    "Wednesday; the Kremlin set one hour for Thursday's three-leader "
    "meeting.",
    "AFP · Reuters",
    head_size=21,
)
yb = block(
    MARGIN + col2 + 16, y, col2, RED,
    "UKRAINE WAR",
    "Drone attacks nearly halve Russia's November oil refining, sources say",
    "Ukrainian drones have cut Russian refineries' crude processing by "
    "45% since late October, industry sources told Reuters, disrupting 15 "
    "of 35 major refineries and tightening fuel supplies.",
    "Reuters",
    head_size=21,
)
y = max(ya, yb)
rule(y + 2, 1)
y += 8

# ---- grid rows B and C: three columns --------------------------------------
col3 = (CW - 32) // 3


def row3(y, stories):
    ends = []
    for i, s in enumerate(stories):
        ends.append(block(MARGIN + i * (col3 + 16), y, col3, *s,
                          head_size=18, body_size=14))
    return max(ends)


y = row3(y, [
    (GREEN, "HEALTH · DR CONGO",
     "Congo Ebola outbreak passes 11,000 cases, more than double in three months",
     "The UN said cases topped 11,000, with 5,400 deaths in eight "
     "provinces — the second-largest Ebola outbreak on record.",
     "United Nations"),
    (NAVY, "SPACE",
     "Voyager 1 reaches one light-day from Earth, a first for any object made by humans",
     "NASA's JPL said the probe, launched in 1977, crossed the distance "
     "light takes 24 hours to travel — some 16 billion miles — on "
     "Wednesday.",
     "NASA JPL"),
    (RED, "UNITED STATES",
     "Peltola wins Alaska, giving Democrats a 56–44 Senate majority",
     "Democrat Mary Peltola defeated Republican incumbent Dan Sullivan — "
     "her party's ninth flip of the midterms and its largest Senate "
     "majority since 2009.",
     "Associated Press"),
])
rule(y + 2, 1)
y += 8

y = row3(y, [
    (NAVY, "MARKETS",
     "Stocks fall on Gulf tensions; oil slips despite Hormuz risk",
     "The S&P 500 fell 1.03% and Europe's Stoxx 50 lost 2.15% as Gulf "
     "fighting worsened. Brent eased to $92.47 on a U.S. stock build; "
     "gold fell 2.05%.",
     "Wire reports"),
    (GREEN, "DISASTER · PACIFIC",
     "Category 5 Cyclone Xavier hits the Northern Cook Islands",
     "Xavier reached category 5 over the northern Cook Islands with gusts "
     "up to 315 km/h, bearing down on the atoll of Manihiki.",
     "Wire reports"),
    (RED, "DISASTER · RUSSIA",
     "Russian military plane crashes in Siberia, killing all 19 aboard",
     "A Russian military transport aircraft crashed in the Kemerovo region "
     "of Siberia, killing all 19 people on board.",
     "Wire reports"),
])
rule(y + 2, 2)
y += 8

# ---- in brief ---------------------------------------------------------------
briefs = [
    ("The Hague:", " The World Court will rule Thursday on whether Myanmar "
     "committed genocide against the Rohingya."),
    ("Economy:", " UK inflation rose to 3.6% in October; the euro zone's "
     "was revised to 4%."),
    ("Business:", " Newsmax sued Fox to unwind its $22 billion takeover "
     "of Roku."),
    ("Sport:", " Zverev reached the ATP Finals knockout stage in Turin, "
     "and Jordan beat Australia 2–0 in Doha."),
]
bf, bb = font(SANS, 15), font(SANS_BOLD, 15)
x = MARGIN
d.text((x, y), "IN BRIEF", font=bb, fill=INK)
x += text_w("IN BRIEF ", bb)
for lead, rest in briefs:
    for txt, fnt in ((lead, bb), (rest, bf)):
        for word in txt.split(" "):
            if not word:
                continue
            wpx = text_w(word + " ", fnt)
            if x + wpx > W - MARGIN:
                x = MARGIN
                y += 21
            d.text((x, y), word, font=fnt, fill=INK)
            x += wpx
y += 22
rule(y, 2)

# ---- footer -------------------------------------------------------------------
centered(
    "Reporting: Reuters · AFP · Associated Press · Al Jazeera · United "
    "Nations · NASA JPL — the news of Wednesday 18 November 2026, as "
    "reported that day",
    y + 10, font(SANS_OBL, 13), fill=GRAY)

img.save("entry.png", optimize=True)
print("entry.png written; content bottom at y =", y + 40)
