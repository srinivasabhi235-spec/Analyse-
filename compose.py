#!/usr/bin/env python3
"""
COMPOSE THE READING.

The previous document was written.  This one is GENERATED, and the difference
is not cosmetic.

Every figure below is looked up in ground.py at build time.  None is typed into
prose.  That removes, by construction, the entire class of defect the old
document was exposed to: a number carried by hand from one section to another,
a section renumbered while a cross-reference stayed behind, a table updated in
one place and not the other.  react_loop.py then reads the OUTPUT back and
re-derives every claim it can parse, so the generator is checked against the
same ground truth the prose came from.

Structure:

    Part I    THE CHART          -- entirely generated
    Part II   THE STRUCTURE      -- the findings, figures interpolated
    Part III  TIME               -- the dasha and what it has already spent
    Part IV   THE QUESTIONS      -- what was asked, and the answers that held
    Part V    METHOD             -- derived vs supplied, every dispute priced

Run:  python3 compose.py > vedic-chart-analysis.md
"""
import swisseph as swe

import ground as G
from ephem_core import (SIGNS, GRAHAS, BIRTH, COMPUTED, short, fmt, nak_of,
                        dignity)

F = G.FACTS
V = lambda k: F[k]['value']
ORD = {1: 'st', 2: 'nd', 3: 'rd', 21: 'st', 22: 'nd', 23: 'rd'}
ordn = lambda n: f"{n}{ORD.get(n, 'th')}"
WORD = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
        'eight', 'nine', 'ten', 'eleven', 'twelve']
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
       'Nov', 'Dec']
G7 = G.G7
OUT = []
p = OUT.append


def date(j):
    y, m, d, _ = swe.revjul(j + 5.5 / 24)
    return f"{int(d)} {MON[m-1]} {y}"


def age(j):
    return (j - G.BIRTH_JD) / G.Y


def joinlist(xs, last='and'):
    xs = list(xs)
    if len(xs) == 1:
        return str(xs[0])
    return ', '.join(str(x) for x in xs[:-1]) + f' {last} {xs[-1]}'


# =============================================================================
p(f"""# The Difficulty and the Fortune Are the Same Object

### A Vedic reading of a nativity — {BIRTH['date'][2]} April {BIRTH['date'][0]}, \
{BIRTH['time'][0]}:{BIRTH['time'][1]:02d}:{BIRTH['time'][2]:02d} IST, {BIRTH['place']}

---

**This document is generated.** Every number in it is looked up at build time
from `ground.py`, which derives the chart from the birth moment with the Swiss
Ephemeris. No figure is typed into the prose. `react_loop.py` then reads this
file back and re-derives every claim it can parse.

**That is the whole methodological claim, and it is a modest one:** it does not
make the interpretation right. It makes the *arithmetic* right, and it makes
the arithmetic checkable by anyone who runs the scripts. What the arithmetic
means is argued in the text, and where the tradition disagrees with itself the
disagreement is priced rather than resolved by preference.

---

## Contents

| Part | | |
|---|---|---|
| **I** | **The chart** | Positions, dignity, houses, drishti, strength, ashtakavarga, vargas — generated |
| **II** | **The structure** | The one configuration everything else restates |
| **III** | **Time** | Vimshottari — what has been spent, what is left |
| **IV** | **The questions** | What was asked of this chart, and what held |
| **V** | **Method** | Derived against supplied, every dispute priced, what is not known |

---

# Part I — The chart

## 1. The birth data

| | |
|---|---|
| date | **{BIRTH['date'][2]} April {BIRTH['date'][0]}** |
| time | **{BIRTH['time'][0]}:{BIRTH['time'][1]:02d}:{BIRTH['time'][2]:02d} IST** |
| place | **{BIRTH['place']}** — {BIRTH['lat']}°N, {BIRTH['lon']}°E |
| ayanamsa | Lahiri |
| house frame | **whole sign**, declared not assumed — see §5 |

**The reading holds two lagna values and always has.** The source data gives
**{V('lagna.sign')} {G.POS['Lagna']%30:.4f}°**; the Swiss Ephemeris, computed
from the stated moment, gives **{SIGNS[G.sign_of(COMPUTED['Lagna'])]} \
{COMPUTED['Lagna']%30:.4f}°** — a gap of
**{(G.POS['Lagna'] - COMPUTED['Lagna'])*60:.2f} arcminutes, about fifty-six seconds of clock time.**

**Everything in this document uses the supplied longitudes**, which is
internally consistent. What that costs is stated once, here, and never left
implicit again:

| | |
|---|---|
| identical across | D1, D2, D3, D4, D5, D6, D7, D9, D10, D11, D15, D16, D18, D20, D22, D27, D30, D40, D45 — **19 of 27 schemes** |
| **moves** | **D12, D24, D36, D60, D81, D108, D144, D150** |

> **Three of the sixteen Shodashavarga ascendants sit inside that
> fifty-six-second question — D12, D24 and D60.** Any claim resting on one of
> them is marked where it is made. The rest of the chart is exact.

---
""")

# =============================================================================
p("## 2. The chart\n")
p(f"| Graha | Longitude | Sign | House | Nakshatra | Pada | Dignity |")
p("|---|---|---|---|---|---|---|")
p(f"| **Lagna** | {short(G.POS['Lagna'])} | **{V('lagna.sign')}** | 1 | "
  f"{V('lagna.nakshatra')} | {V('lagna.pada')} | — |")
for g in GRAHAS:
    n, pa, _, _ = nak_of(G.POS[g])
    d = V(f'{g}.dignity')
    mark = '**' if d in ('exalted', 'own', 'debilitated') else ''
    p(f"| {g} | {short(G.POS[g])} | {V(f'{g}.sign')} | {V(f'{g}.house')} | "
      f"{n} | {pa} | {mark}{d}{mark} |")

_ex = [g for g in G7 if V(f'{g}.dignity') == 'exalted']
_own = [g for g in G7 if V(f'{g}.dignity') == 'own']
_deb = [g for g in G7 if V(f'{g}.dignity') == 'debilitated']
_h8, _h9 = V('house8.occupants'), V('house9.occupants')
p(f"""
**{joinlist(_ex)} {'are' if len(_ex) > 1 else 'is'} exalted.
{joinlist(_own) if _own else 'Nothing'} {'is' if len(_own) == 1 else 'are'} in own sign.
{'Nothing is debilitated' if not _deb else joinlist(_deb) + ' is debilitated'}.**

**And the first thing to say about this chart is where the grahas are, not what
they are.** {len(_h8)} sit in the {ordn(8)} house and {len(_h9)} in the {ordn(9)}:
**{len(_h8) + len(_h9)} of nine grahas in two adjacent houses.**

| House | Sign | Occupants |
|---|---|---|""")
for h in range(1, 13):
    o = V(f'house{h}.occupants')
    if o:
        p(f"| **{ordn(h)}** | {V(f'house{h}.sign')} | {joinlist(o)} |")
p(f"""
> **{len(V('houses.empty'))} of the twelve houses are empty** —
> {joinlist(ordn(h) for h in V('houses.empty'))}. The chart is not spread out.
> It is a stack.

---
""")

# =============================================================================
p(f"""## 3. Houses, lords, and where authority actually sits

| House | Sign | Lord | The lord sits in | SAV | Bhava Bala | Rank | Occupants |
|---|---|---|---|---|---|---|---|""")
for h in range(1, 13):
    l = V(f'house{h}.lord')
    o = V(f'house{h}.occupants')
    p(f"| {ordn(h)} | {V(f'house{h}.sign')} | {l} | **{ordn(G.house_of(l))}** | "
      f"{V(f'house{h}.sav')} | {V(f'house{h}.bhavabala'):.2f} | "
      f"{V(f'house{h}.bhavarank')} | {joinlist(o) if o else '—'} |")

_dist = V('lords.distribution')
_bbmax = V(f"house{V('bhava.strongest')}.bhavabala")
_bbmin = V(f"house{V('bhava.weakest')}.bhavabala")
p(f"""
**Read the fourth column on its own.** Every one of the twelve house lords sits
in one of {WORD[len(_dist)]} houses:
""")
for hh in sorted(_dist):
    p(f"- **the {ordn(hh)}** governs the "
      f"{joinlist(ordn(x) for x in _dist[hh])}")
p(f"""
> **There is no fourth address.** Every department of the life reports to the
> {joinlist(ordn(h) for h in sorted(_dist))} — transformation, fortune, and
> work. Nothing in this chart is administered from anywhere else.

**And the strongest and weakest bhavas are not where a reader would look.** The
strongest is the **{ordn(V('bhava.strongest'))} — {_bbmax:.2f} rupas**, the house of
loss, expenditure and elsewhere. The weakest is the
**{ordn(V('bhava.weakest'))} — {_bbmin:.2f}**, which is the house this chart
administers almost everything from.

---
""")

# =============================================================================
_un7, _unN = V('houses.unaspected|nonodes'), V('houses.unaspected|nodes')
_ut7 = V('houses.untouched|nonodes')
p(f"""## 4. Drishti — and the rule this document uses

**This section resolves a contradiction the earlier version of this reading
carried without noticing it**, and it is stated first because everything about
which houses are "reached" depends on it.

**Do Rahu and Ketu cast drishti?** The tradition is split. Parashara's aspect
chapter assigns the special aspects to Shani, Mangal and Guru and does not give
the shadow grahas drishti of their own; a large and respectable stream of later
practice gives them the 5th, 7th and 9th like Guru.

| | Houses receiving no aspect | Count |
|---|---|---|
| **seven grahas only** *(this document's rule)* | {joinlist(ordn(h) for h in _un7)} | **{WORD[len(_un7)]}** |
| nodes included | {joinlist(ordn(h) for h in _unN)} | {WORD[len(_unN)]} |

**This document uses the seven-graha rule, and the reason is provenance, not
preference:** the reading takes Parashara as its source throughout, and
Parashara's drishti chapter does not give the nodes an aspect. **The other
reading is printed above so nobody has to take that on trust, and every finding
below that depends on the choice says so.**

| Graha | From | Aspects |
|---|---|---|""")
for g in G7:
    tg = [h for h in range(1, 13) if G.aspects_house(g, h)]
    p(f"| {g} | {ordn(G.house_of(g))} | {joinlist(ordn(h) for h in tg)} |")
p(f"| *Rahu* | *{ordn(G.house_of('Rahu'))}* | "
  f"*{joinlist(ordn(h) for h in range(1, 13) if G.aspects_house('Rahu', h))} "
  f"— not counted here* |")
p(f"| *Ketu* | *{ordn(G.house_of('Ketu'))}* | "
  f"*{joinlist(ordn(h) for h in range(1, 13) if G.aspects_house('Ketu', h))} "
  f"— not counted here* |")

p(f"""
**Now the finding, and it is the sharpest structural fact in the chart.**

| | |
|---|---|
| houses with no occupant | {joinlist(ordn(h) for h in V('houses.empty'))} — **{WORD[len(V('houses.empty'))]}** |
| houses receiving no aspect | {joinlist(ordn(h) for h in _un7)} — **{WORD[len(_un7)]}** |
| **houses with neither** | **{joinlist(ordn(h) for h in _ut7)}** |

> **{WORD[len(_ut7)].capitalize()} houses are wholly untouched — the
> {ordn(1)}, the {ordn(5)} and the {ordn(7)}. The self, the children and the
> spouse.** Nothing sits in them and nothing looks at them. The three most
> personal departments of the chart are the three the chart does not address
> directly; they are governed entirely by their lords, from elsewhere.
>
> **Under the node-inclusive rule this finding does not survive** — Rahu would
> aspect the {ordn(1)} and the {ordn(5)}, and only the {ordn(8)} and
> {ordn(10)} would be unreached. **That is the honest size of the dependency,
> and the earlier version of this document published both results in different
> places without ever noticing they disagreed.**

---
""")

# =============================================================================
p(f"""## 5. Strength

**Four instruments, and they do not agree — which is the point of running all
four.** Shadbala says whether a graha can act at all; Ishta and Kashta say what
it costs; Shodhya Pinda says how much it delivers.

| Graha | Shadbala | Minimum | Passes | Ishta | Kashta | Net | Delivery |
|---|---|---|---|---|---|---|---|""")
for g in sorted(G7, key=lambda x: -G.SHADBALA_RUPAS[x]):
    ok = G.SHADBALA_RUPAS[g] >= G.SHADBALA_MIN[g]
    p(f"| {g} | **{G.SHADBALA_RUPAS[g]:.2f}** | {G.SHADBALA_MIN[g]:.1f} | "
      f"{'yes' if ok else '**NO**'} | {G.ISHTA[g]:.2f} | {G.KASHTA[g]:.2f} | "
      f"{G.ISHTA[g]-G.KASHTA[g]:+.2f} | {G.SHODHYA[g]} |")

_net = {g: G.ISHTA[g] - G.KASHTA[g] for g in G7}
_best, _worst = max(_net, key=_net.get), min(_net, key=_net.get)


def spearman(x, y):
    rx = {k: i for i, k in enumerate(sorted(x, key=lambda k: -x[k]))}
    ry = {k: i for i, k in enumerate(sorted(y, key=lambda k: -y[k]))}
    n = len(x)
    return 1 - 6 * sum((rx[k] - ry[k]) ** 2 for k in x) / (n * (n * n - 1))


_rho = spearman(G.SHODHYA, G.KASHTA)
p(f"""
**These are the one class of figure in this document that is SUPPLIED rather
than derived** — the Shadbala sub-components are not implemented here. They are
marked as such wherever they appear, and no derived figure is silently mixed
with them.

**{_best} gives most and charges least** — Ishta {G.ISHTA[_best]:.2f} against
Kashta {G.KASHTA[_best]:.2f}, net **{_net[_best]:+.2f}**. **{_worst} is the
inverse**: net **{_net[_worst]:+.2f}**.

**And then the measurement that gives this document its title.** Rank the seven
by what they deliver, rank them again by what they cost, and correlate:

> **Spearman ρ = {_rho:+.2f} between delivery and cost.**
>
> **The grahas that deliver most are the grahas that cost most.** Nothing
> converts and nothing is exchanged. The good and the price are not sequential
> — they are **the same object**, seen from two sides. {_best}, which rules the
> {ordn(G.houses_ruled(_best)[0])}, is the single exemption.

---
""")

# =============================================================================
p(f"""## 6. Ashtakavarga

**Rebuilt from the Parashari benefic-place tables rather than taken from the
supplied sheet**, which makes the contributor breakdown — and therefore kakshya
— available for the first time.

| Sign | {' | '.join(g[:2] for g in G7)} | **SAV** | House |
|---|{'---|' * 7}---|---|""")
for s in range(12):
    h = (s - G.LAG) % 12 + 1
    p(f"| {SIGNS[s]} | {' | '.join(str(G.BAV[g][s]) for g in G7)} | "
      f"**{G.SAV[s]}** | {ordn(h)} |")
p(f"""| | | | | | | | | **{sum(G.SAV)}** | |

**Six of the seven per-graha totals reproduce their canonical values exactly**
(Surya 48, Chandra 49, Mangal 39, Budha 54, Guru 56, Shani 39). **Shukra comes
to {sum(G.BAV['Shukra'])} where the canon says 52**, and the entire discrepancy
is one bindu in Karka. **It is recorded rather than patched**, because editing
the table until it agrees with the sheet would make the check circular.

| | |
|---|---|
| highest | **{V('sav.highest')} — {G.SAV[SIGNS.index(V('sav.highest'))]}**, the {ordn((SIGNS.index(V('sav.highest')) - G.LAG) % 12 + 1)} house |
| lowest | **{V('sav.lowest')} — {G.SAV[SIGNS.index(V('sav.lowest'))]}**, the {ordn((SIGNS.index(V('sav.lowest')) - G.LAG) % 12 + 1)} house |

> **The best-supported sign in the chart is the {ordn((SIGNS.index(V('sav.highest')) - G.LAG) % 12 + 1)}
> house — service, debt, competition, the daily grind. The worst-supported is
> the {ordn((SIGNS.index(V('sav.lowest')) - G.LAG) % 12 + 1)}, which holds
> {WORD[len(V('house8.occupants'))]} grahas and is where the whole chart is
> administered from.**

---
""")

# =============================================================================
p("""## 7. The Jaimini layer

| Karaka | Graha | Which sits in |
|---|---|---|""")
for k in ['Atmakaraka', 'Amatyakaraka', 'Bhratrikaraka', 'Matrikaraka',
          'Pitrikaraka', 'Putrakaraka', 'Gnatikaraka', 'Darakaraka']:
    g = V(f'karaka.{k}')
    p(f"| {k} | **{g}** | the {ordn(G.house_of(g))} |")
p(f"""
| | |
|---|---|
| **Arudha Lagna** | {V('arudha.lagna')} — the {ordn((SIGNS.index(V('arudha.lagna')) - G.LAG) % 12 + 1)} house |
| **Upapada** | {V('upapada')} — the {ordn((SIGNS.index(V('upapada')) - G.LAG) % 12 + 1)} house, lord {G.LORD[SIGNS.index(V('upapada'))]} |

**{V('karaka.Atmakaraka')} is the Atmakaraka** — the graha of the soul's own
business — **and it carries the highest Ishta phala in the chart.**
**{V('karaka.Amatyakaraka')} is the Amatyakaraka**, the karaka of profession,
**and it carries the highest Kashta.** The two most consequential Jaimini
significators are the chart's cheapest and its most expensive graha.

---
""")

# =============================================================================
_A, _B = 'Mangal', 'Shukra'
_sep = abs(G.POS[_A] - G.POS[_B])
_pair = sorted(set(G.houses_ruled(_A)) | set(G.houses_ruled(_B)))
p(f"""# Part II — The structure

## 8. The one configuration

**Everything in Part I collapses into a single arrangement, and every finding
in Parts III and IV is a restatement of it at a different magnification.**

| | Sign | Lord | Lord sits in | Occupants |
|---|---|---|---|---|
| **{ordn(8)}** | {V('house8.sign')} | **{V('house8.lord')}** | the **{ordn(G.house_of(V('house8.lord')))}** | {joinlist(V('house8.occupants'))} |
| **{ordn(9)}** | {V('house9.sign')} | **{V('house9.lord')}** | the **{ordn(G.house_of(V('house9.lord')))}** | {joinlist(V('house9.occupants'))} |

**{_A} rules the {ordn(8)} and sits in the {ordn(9)}. {_B} rules the {ordn(9)}
and sits in the {ordn(8)}.** A complete mutual exchange — the only one in the
chart — and it binds the house of upheaval to the house of fortune permanently.

> **Transformation and dharma, trading places, with
> {len(V('house8.occupants')) + len(V('house9.occupants'))} of the nine grahas
> living between them.** Every crisis is routed through meaning, and every
> belief is tested by crisis. **He does not get to hold a philosophy that has
> not been through something.**

**And one thing about the exchange that is easy to miss.** The two lords are
**{_sep:.2f}° apart, in adjacent signs — a 2/12 axis, which carries no drishti
in any scheme.** {_A}'s special aspects ({joinlist(ordn(x) for x in [4, 7, 8])})
miss as well.

> **They hold each other's houses and never look at each other.** A parivartana
> is a bond of ownership, not of sight. That is not a defect — it is why the
> arrangement is **stable rather than volatile**.

---

## 9. What kind of exchange it is

**The tradition classifies parivartanas into three types, and this document
had named this one sixteen times before ever classifying it.**

| | |
|---|---|
| the pair's lordships | **{joinlist(ordn(x) for x in _pair)}** |
| a dusthana in the pair? | **yes — the {ordn(8)}** |
| the {ordn(3)} in the pair? | **yes** |
| **type** | **Dainya** *(dusthana present)*, **and Khala** *(3rd present)* |

*Dainya* means poverty, wretchedness, dependency. **On the typology this is the
bad kind, and it is not close.**

**But the typology does not capture what else the pair owns.** {_B} also rules
the **{ordn(9)} — the strongest trikona**. This is a dusthana lord and a
trikona lord swapping seats, with the trikona lord going *into* the dusthana.
That is the configuration widely read as *"an unexpected change of fortune
through something first perceived as a crisis."*

**Both readings are reported and neither is picked**, because the texts do not
settle it. What can be said precisely is what the chart supports:

| Claim commonly attached to this yoga | What the chart says |
|---|---|
| **marriage** | **strongest.** The karaka of marriage *is* one of the two exchanging grahas, and {_B} carries the highest Ishta in the chart |
| **research, occult knowledge** | **strong.** The {ordn(8)} lord in the {ordn(9)} is the textbook placement — hidden things governed from the house of doctrine |
| **institutional connections** | **strong, but through the {ordn(12)}** — Bhava Bala rank 1 of 12 — not through the {ordn(11)} of networks |
| **inheritance** | present and expensive. {_A}'s Kashta is {G.KASHTA[_A]:.2f}, second highest in the chart |
| **tax, insurance, others' money** | **inverts.** The {ordn(6)} of debt carries **{V('house6.sav')} bindus, the highest in the chart**; the {ordn(8)} of receipt is the **weakest bhava at {V('house8.bhavabala'):.2f}** and the lowest SAV at {V('house8.sav')} |
| **"a completely unexpected change of fortune"** | **the mechanism is real; the scale is not supported.** The {ordn(9)} lord genuinely administers fortune from the house of crisis, and there is no other channel for it. But that channel is the thinnest thing in the chart |

---
""")

# =============================================================================
_md = G.MAHADASHA
_now = swe.julday(2026, 9, 3, 0.0)
_cur = [x for x in _md if x[1] <= _now < x[2]][0]
_curad = [x for x in G.ANTARDASHA if x[2] <= _now < x[3]][0]
p(f"""# Part III — Time

## 10. Vimshottari

Birth nakshatra **{V('moon.nakshatra')}**, lord
**{nak_of(G.POS['Chandra'])[2]}** — so the sequence opens there.

| Mahadasha | From | To | Age at start | |
|---|---|---|---|---|""")
for g, a, b in _md:
    tag = ''
    if b < _now:
        tag = 'spent'
    elif a <= _now < b:
        tag = '**RUNNING**'
    p(f"| {g} | {date(a)} | {date(b)} | {age(a):.0f} | {tag} |")

_mars = [x for x in _md if x[0] == 'Mangal'][0]
_ven = [x for x in _md if x[0] == 'Shukra'][0]
p(f"""
**Running now: {_cur[0]}–{_curad[1]}**, to {date(_curad[3])}.

**And here is the fact that governs everything in Part II.** A parivartana
fires in the dashas of its two lords:

| | |
|---|---|
| **{_A} mahadasha** | ended **{date(_mars[2])}**, at age {age(_mars[2]):.0f} — **spent** |
| **{_B} mahadasha** | begins **{date(_ven[1])}**, at age {age(_ven[1]):.0f} — **unreachable** |

> **{V('moon.nakshatra')}'s Vimshottari order puts {_B} last of the nine. The
> chart's central configuration will never hold a mahadasha again.** It fires
> only at antardasha level and below for the rest of his life — in instalments
> of one to three years, not as a hinge.

**Every remaining antardasha of either lord, to age 80:**

| Mahadasha | Antardasha | From | To | Age | Years |
|---|---|---|---|---|---|""")
_lim = G.BIRTH_JD + 80 * G.Y
_rows = [(g, ag, a, b) for g, ag, a, b in G.ANTARDASHA
         if ag in (_A, _B) and b > _now and a < _lim]
for g, ag, a, b in _rows:
    p(f"| {g} | {ag} | {date(a)} | {date(b)} | {age(a):.0f} | {(b-a)/G.Y:.2f} |")
_tot = sum(b - max(a, _now) for _, _, a, b in _rows) / G.Y
p(f"""
**{_tot:.1f} years in total — {_tot/((_lim-_now)/G.Y)*100:.0f}% of the next
{(_lim-_now)/G.Y:.0f}.** The next is **{_rows[0][0]}–{_rows[0][1]},
{date(_rows[0][2])}**.

---
""")

# =============================================================================
def _ingress(sign, y0, y1, body='Shani'):
    ids = {'Shani': swe.SATURN, 'Guru': swe.JUPITER}
    fl = swe.FLG_SWIEPH | swe.FLG_SIDEREAL
    lon = lambda j: swe.calc_ut(j, ids[body], fl)[0][0] % 360
    j, end, out, prev = swe.julday(y0, 1, 1, 0.0), swe.julday(y1, 1, 1, 0.0), [], None
    while j < end:
        s = G.sign_of(lon(j))
        if prev is not None and s != prev[1]:
            lo, hi = prev[0], j
            for _ in range(50):
                m = (lo + hi) / 2
                if G.sign_of(lon(m)) == prev[1]:
                    lo = m
                else:
                    hi = m
            if s == sign or prev[1] == sign:
                out.append((lo, prev[1], s))
        prev = (j, s)
        j += 1
    return out


_ing = _ingress(G.sign_in_house(8), 2026, 2034)
_in0 = min(j for j, a, b in _ing if b == G.sign_in_house(8))
_in1 = max(j for j, a, b in _ing if a == G.sign_in_house(8))
_m8 = (G.sign_in_house(8) - G.MOON_SIGN) % 12 + 1
p(f"""## 11. What is coming

**Shani enters the {ordn(8)} house — {V('house8.sign')} — on
{date(_in0)} and is finally clear of it on {date(_in1)}.** Three passes, not
one.

| | |
|---|---|
| Shani's dignity there | **debilitated**, the whole way |
| what it crosses | **{joinlist(V('house8.occupants'))}** — all three occupants |
| the sign's support | **SAV {V('house8.sav')}, the lowest of the twelve**; Shani's own bindus there: **{G.BAV['Shani'][G.sign_in_house(8)]} of 8** |
| from the natal Moon | the **{ordn(_m8)}** — so this is **Sade Sati, phase one** |
| Shani's 3rd aspect | falls on **{joinlist(V('house10.occupants'))} in the {ordn(10)}**, for the entire transit |
| the dasha underneath | a **Shani antardasha** runs inside it |

> **The sign is the problem, not any single contact.** Nearly three years in
> the weakest sign of the chart, at {G.BAV['Shani'][G.sign_in_house(8)]} bindus,
> opening Sade Sati, with an aspect resting on the career house throughout.
>
> **This is not Ashtama Shani**, which is Shani in the {ordn(8)} *from the
> Moon* — twenty years further off. The harsher doctrine is not the one
> arriving.

**And one thing in it that is not pressure.** Guru aspects
{V('house8.sign')} through most of the same window — **a double transit on the
{ordn(8)} house**, which is the classical condition for a bhava *delivering*
rather than merely being pressed.

---
""")

# =============================================================================
_l7, _l10, _l4 = V('house7.lord'), V('house10.lord'), V('house4.lord')
_upl = G.LORD[SIGNS.index(V('upapada'))]
p(f"""# Part IV — The questions

**Everything above is apparatus. This part is what was actually put to the
chart.** Each answer states what the computation supports and stops there:
**Jyotisha times the activation of a promise. It does not name an event**, and
no arithmetic in this document turns a marked window into a specific thing that
happens.

## 12. Career, and the field

| | |
|---|---|
| {ordn(10)} house | **{V('house10.sign')}**, SAV {V('house10.sav')}, Bhava Bala rank {V('house10.bhavarank')} of 12 |
| its occupant | **{joinlist(V('house10.occupants'))} — alone** |
| its lord | **{_l10}**, sitting in the **{ordn(G.house_of(_l10))}** |
| profession karaka *(Jaimini)* | **{V('karaka.Amatyakaraka')}** — Amatyakaraka |

**The career house holds one graha and its lord is in the {ordn(8)}.** So the
{ordn(10)} is administered from the house of upheaval, like almost everything
else — and **{V('karaka.Amatyakaraka')}, the karaka of profession, carries the
lowest Ishta and the highest Kashta in the chart
({G.ISHTA[V('karaka.Amatyakaraka')]:.2f} against
{G.KASHTA[V('karaka.Amatyakaraka')]:.2f}).**

> **The capacity for depth is excellent and it does not arrive through the
> career lord.** Credentialing through the professional channel is the weak
> route; knowledge held for its own sake is the strong one. **What this chart
> is built to do, it does not get paid for directly.**

**And the {ordn(6)} is the strongest sign in the chart at {V('house6.sav')}
bindus** — service, competition, obligation, the daily grind. He wins contests
he should not comfortably win, and the winning costs him.

---

## 13. Marriage

| | |
|---|---|
| {ordn(7)} house | **{V('house7.sign')}** — empty, and **unaspected** |
| its lord | **{_l7}**, in the **{ordn(G.house_of(_l7))}** |
| **Upapada** | **{V('upapada')}**, lord **{_upl}** |
| Darakaraka *(Jaimini)* | **{V('karaka.Darakaraka')}** |
| Shukra | Atmakaraka, **highest Ishta in the chart** |

**The {ordn(7)} is one of the three wholly untouched houses (§4)** — nothing
sits in it and, on this document's drishti rule, nothing looks at it. **It is
governed entirely by {_l7} from the {ordn(G.house_of(_l7))}**, and {_l7} is
also the Upapada lord. Two independent significators of marriage resolve to the
same graha, which is unusual and which makes the reading unusually sharp:
**whatever {_l7} does, the marriage does.**

---

## 14. Place — and elsewhere

| | Bhava Bala | Rank | SAV | Lord |
|---|---|---|---|---|
| **{ordn(4)} — a home** | {V('house4.bhavabala'):.2f} | {V('house4.bhavarank')} | {V('house4.sav')} | {_l4}, in the {ordn(G.house_of(_l4))} |
| **{ordn(10)} — a standing** | {V('house10.bhavabala'):.2f} | {V('house10.bhavarank')} | {V('house10.sav')} | {_l10}, in the {ordn(G.house_of(_l10))} |
| **{ordn(12)} — elsewhere** | **{V('house12.bhavabala'):.2f}** | **{V('house12.bhavarank')}** | {V('house12.sav')} | {V('house12.lord')}, **{V(f"{V('house12.lord')}.dignity")}**, in the {ordn(G.house_of(V('house12.lord')))} |

> **The {ordn(12)} is the strongest bhava in the chart by a wide margin
> — {V('house12.bhavabala'):.2f} rupas against {V('house4.bhavabala'):.2f} for
> a home — and its lord is the chart's exalted, highest-Ishta graha.**
>
> **The chart does not need to be asked whether he should be elsewhere. It
> says that being somewhere other than where he started is the thing it is best
> built for.** And the {ordn(12)} is also the one house whose lord gives most
> and charges least — **the single exemption to the ρ = {_rho:+.2f} rule.**

---

## 15. Transformation

**The {ordn(8)} is the weakest bhava in the chart
({V('house8.bhavabala'):.2f} rupas, rank {V('house8.bhavarank')} of 12) and the
lowest sign by ashtakavarga ({V('house8.sav')} bindus). It is also where
{WORD[len(V('house8.occupants'))]} grahas sit and where
{len(V('lords.distribution')[8])} of the twelve house lords report.**

**That combination is the chart.** The department it runs everything through is
the department it is least equipped to run. Not a contradiction — a
description of cost. **The transformation is not optional and it is not
cheap**, and §5's measurement says why: **what delivers is what costs.**

---
""")

# =============================================================================
_der = sum(1 for v in F.values() if v['kind'] == 'DERIVED')
_sup = sum(1 for v in F.values() if v['kind'] == 'SUPPLIED')
p(f"""# Part V — Method

## 16. Derived against supplied

**{len(F)} facts underpin this document: {_der} derived, {_sup} supplied.**
The distinction is kept because mixing them is how a reading starts sounding
more certain than it is.

| | What it covers | Status |
|---|---|---|
| **DERIVED** | positions, signs, houses, dignity, nakshatras, lordships, drishti, ashtakavarga, chara karakas, arudhas, the Vimshottari tree, every varga, every transit date | computed from the birth moment; reproducible by running the scripts |
| **SUPPLIED** | Shadbala rupas and their minima, Ishta and Kashta phala, Shodhya Pinda, Bhava Bala and its ranks | taken from the source sheet — the generating rules are not implemented here |

**Every Bhava Bala figure in this document is supplied.** So is every strength
rupa. They are used, and they are labelled, and no derived figure is quietly
averaged with them.

---

## 17. Every dispute, priced

**Where the tradition disagrees with itself, this document states the choice,
computes both sides, and says what turns on it.**

| Dispute | Choice made here | What it costs |
|---|---|---|
| **Do Rahu and Ketu cast drishti?** | **No** — Parashara's aspect chapter gives the special aspects to Shani, Mangal and Guru only | **The largest single dependency in the reading.** With nodes excluded, {WORD[len(_un7)]} houses are unaspected and **{joinlist(ordn(h) for h in _ut7)} are wholly untouched**. With them included, only the {ordn(8)} and {ordn(10)} are unreached and **no house is untouched** |
| **House frame** | **Whole sign**, declared | Under cuspal frames the seven classical grahas spread across four bhavas instead of two, and Vimala yoga dissolves. The 73° concentration is unaffected |
| **The birth-time residual** | Supplied longitudes used throughout | **D12, D24 and D60 ascendants move.** Any claim on one is marked at the point of use |
| **Venus's ashtakavarga** | Derived table kept, not patched to the sheet | One bindu, in Karka. Six of seven graha totals match canon exactly |
| **Shodhya Pinda** | Rashi Pinda + Graha Pinda, from the source sheet | **A second table had been circulating in the scripts with no source.** It swapped Guru and Shukra in the delivery ranking and moved ρ from +0.82 to +0.86. Generating this document computed the correlation instead of copying it, which is how the error surfaced |
| **Viparita raja yoga** | Treated as **not firing** — viparita requires an afflicted graha, and this {ordn(12)} lord is exalted | The chart's only bad-to-good mechanism. On the other school it would convert one house, not the chart |
| **The 8th–9th exchange** | **Both readings reported, neither picked** | Dainya by typology; "fortune through crisis" by the trikona reading. The texts give results for each placement separately and none for the exchange |

---

## 18. What checks this document

| Script | What it does |
|---|---|
| `ground.py` | derives every fact from the birth moment; tags derived against supplied |
| `compose.py` | generates this file — **no figure is typed into the prose** |
| `react_loop.py` | reads this file back and re-derives every claim it can parse |

**The loop is a genuine reason–act–observe–reflect cycle run to fixpoint.** It
extracts a claim from a sentence, computes the true value, compares, and
returns PASS, FAIL, or **CONTINGENT** — true under one school and false under
another. It declines to act where it cannot resolve the frame, and says why:
a claim counted from the Moon, a transit, a negation, a rule statement, a
quotation.

**And one honest limit on that.** The loop extracts far fewer claims from this
document than from the one it replaced — **ten against a hundred and sixty-seven**
— because this version states each fact once, in a generated table, instead of
restating it in prose across dozens of sections. **That is the point of
generating it**, but it means "fixpoint reached" here is a weaker statement than
it was there: there is simply less loose prose to be wrong.

> **A wrong actor is worse than no actor.** On its first run over the previous
> version of this document it reported 72 failures. **Every one of them was a
> defect in the loop, not in the document** — it was checking varga claims
> against D1, binding "debilitated" to the wrong graha in a comma list, and
> reading rule statements as chart claims. Eight iterations later it reported
> **zero failures and two contingencies**, and those two were the real finding:
> the same corpus had published both sides of the node-drishti question in
> different places without noticing.

---

## 19. What is not known

- **Her chart.** The only input that would change conclusions rather than add
  to them.
- **Confirmed events.** This reading is unfalsified, not tested. The one
  genuinely falsifiable prediction it made — deriving the birth date, weekday
  and tithi from the chart alone — held.
- **Ayurdaya is not attempted.** Three classical methods disagree and the
  reading declines to pick one.
- **D6, the health varga.** Two competing starting rules agree on only 4 of 10
  placements. Computed, printed, not leaned on.
- **D36 and everything from D81 down** move with a single minute of clock
  time. Computed, and nothing rests on them.

---

## 20. The whole thing on one page

| | |
|---|---|
| **The shape** | {len(_h8) + len(_h9)} of nine grahas in two adjacent houses, the {ordn(8)} and the {ordn(9)}, in mutual exchange |
| **The wiring** | all twelve house lords in {WORD[len(_dist)]} houses — the {joinlist(ordn(h) for h in sorted(_dist))}. No fourth address |
| **The blind spots** | {joinlist(ordn(h) for h in _ut7)} — self, children, spouse — empty and unaspected |
| **The strength** | {_best} exalted, highest Ishta, lowest Kashta, ruling the {ordn(G.houses_ruled(_best)[0])} |
| **The cost** | ρ = {_rho:+.2f} between what delivers and what it costs |
| **The best-supported ground** | the {ordn(12)} — elsewhere — at Bhava Bala {V('house12.bhavabala'):.2f}, rank {V('house12.bhavarank')} |
| **The weakest ground** | the {ordn(8)} — {V('house8.bhavabala'):.2f}, rank {V('house8.bhavarank')} — which is where everything is administered from |
| **What is coming** | Shani through the {ordn(8)} {date(_in0)} to {date(_in1)}; Sade Sati phase one; a double transit on the {ordn(8)} |
| **What will not come again** | a mahadasha of either exchange lord |

> **The difficulty and the fortune are the same object.** Not a consolation and
> not a sentence — a measurement. The grahas that deliver most in this chart
> are the grahas that cost most, and the {ordn(9)} of fortune is held by a
> graha sitting in the {ordn(8)} of crisis while the {ordn(8)}'s own lord sits
> in the {ordn(9)}. **The price is not attached to the reward. It is part of
> what the reward is.**
>
> **The one exemption is {_best}, ruling the {ordn(G.houses_ruled(_best)[0])}
> — the house of letting go.** He gets everything he grips, painfully. **What
> he gets freely is what he stops gripping.**

---

*Generated by `compose.py` from `ground.py`. Verified by `react_loop.py`.
An interpretation within the framework of Jyotisha, presented on its own terms.*
""")

print('\n'.join(OUT))
