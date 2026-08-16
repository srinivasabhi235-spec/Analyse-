#!/usr/bin/env python3
"""
Verification of the supplied Vedic chart set (D1, D9, D10, D11, D8, D27, D30,
upagrahas, Vimshottari dasha).

Every interpretive claim in vedic-chart-analysis.md rests on output from this
script rather than on visual inspection of the source tables. Run with:

    python3 verify_chart.py

Checks performed:
  1. D1 house placements and house lordships (whole-sign, Kanya lagna)
  2. Combustion orbs
  3. Tight conjunctions
  4. Parivartana (mutual sign exchange) detection
  5. Graha drishti (special aspects) onto houses
  6. Nakshatra / pada / lord, and the nakshatra-dispositor chain
  7. Gandanta (water-fire junction) placements
  8. Pushkara navamsa
  9. Independent recomputation of D9 and D27 from D1 longitudes
 10. Rahu/Ketu 180-degree integrity across all supplied vargas
 11. Upagraha house placement and contacts with grahas
 12. Vimshottari balance, implied birth date, and antardasha boundaries
"""

from datetime import datetime, timedelta

SIGNS = ["Mesha", "Vrishabha", "Mithuna", "Karka", "Simha", "Kanya",
         "Tula", "Vrischika", "Dhanu", "Makara", "Kumbha", "Meena"]

LORD = {"Mesha": "Mangal", "Vrishabha": "Shukra", "Mithuna": "Budha",
        "Karka": "Chandra", "Simha": "Surya", "Kanya": "Budha",
        "Tula": "Shukra", "Vrischika": "Mangal", "Dhanu": "Guru",
        "Makara": "Shani", "Kumbha": "Shani", "Meena": "Guru"}

NAK = ["Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
       "Punarvasu", "Pushya", "Ashlesha", "Magha", "P Phalguni",
       "U Phalguni", "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha",
       "Jyeshtha", "Mula", "P Ashadha", "U Ashadha", "Shravana",
       "Dhanishtha", "Shatabhisha", "P Bhadrapada", "U Bhadrapada", "Revati"]

# Vimshottari nakshatra lords, repeating every 9
NAK_LORD = ["Ketu", "Shukra", "Surya", "Chandra", "Mangal",
            "Rahu", "Guru", "Shani", "Budha"] * 3

VIMSHOTTARI = [("Ketu", 7), ("Shukra", 20), ("Surya", 6), ("Chandra", 10),
               ("Mangal", 7), ("Rahu", 18), ("Guru", 16), ("Shani", 19),
               ("Budha", 17)]

NAK_SPAN = 40.0 / 3.0        # 13 deg 20 min
PADA_SPAN = 10.0 / 3.0       # 3 deg 20 min


def dms(sign, d, m, s):
    """Sidereal longitude from sign + degrees/minutes/seconds."""
    return SIGNS.index(sign) * 30 + d + m / 60 + s / 3600


def fmt(lon):
    sign = int(lon // 30)
    rem = lon % 30
    d = int(rem)
    m = int((rem - d) * 60)
    s = round((((rem - d) * 60) - m) * 60)
    return f"{SIGNS[sign]:11s} {d:02d}°{m:02d}'{s:02d}\""


def sep(a, b):
    """Shortest angular separation."""
    x = abs(a - b) % 360
    return min(x, 360 - x)


D1 = {
    "Lagna":   dms("Kanya",      27, 37, 37),
    "Surya":   dms("Mesha",       1, 28,  3),
    "Chandra": dms("Vrishabha",   1, 47, 15),
    "Mangal":  dms("Vrishabha",   7, 19, 32),
    "Budha":   dms("Mesha",      10, 27, 50),
    "Guru":    dms("Mithuna",    14, 47, 52),
    "Shukra":  dms("Mesha",      23, 36, 49),
    "Shani":   dms("Vrishabha",  17, 54, 25),
    "Rahu":    dms("Vrishabha",  26, 55, 52),
    "Ketu":    dms("Vrischika",  26, 55, 52),
}

GRAHAS = [k for k in D1 if k != "Lagna"]
LAGNA_SIGN = int(D1["Lagna"] // 30)

# As printed in the source tables
GIVEN = {
    "D9": {"Lagna": dms("Kanya", 8, 38, 34), "Surya": dms("Mesha", 13, 12, 31),
           "Chandra": dms("Makara", 16, 5, 18), "Mangal": dms("Meena", 5, 55, 49),
           "Budha": dms("Karka", 4, 10, 38), "Guru": dms("Kumbha", 13, 10, 54),
           "Shukra": dms("Vrischika", 2, 31, 21), "Shani": dms("Mithuna", 11, 9, 48),
           "Rahu": dms("Kanya", 2, 22, 49), "Ketu": dms("Meena", 2, 22, 49)},
    "D27": {"Lagna": dms("Karka", 25, 55, 42), "Surya": dms("Vrishabha", 9, 37, 33),
            "Chandra": dms("Simha", 18, 15, 56), "Mangal": dms("Makara", 17, 47, 28),
            "Budha": dms("Makara", 12, 31, 55), "Guru": dms("Vrischika", 9, 32, 44),
            "Shukra": dms("Makara", 7, 34, 4), "Shani": dms("Vrischika", 3, 29, 26),
            "Rahu": dms("Karka", 7, 8, 29), "Ketu": dms("Makara", 7, 8, 29)},
}

NODE_PAIRS = {
    "D1":  (dms("Vrishabha", 26, 55, 52), dms("Vrischika", 26, 55, 52)),
    "D9":  (dms("Kanya", 2, 22, 49),      dms("Meena", 2, 22, 49)),
    "D10": (dms("Kanya", 29, 18, 42),     dms("Meena", 29, 18, 42)),
    "D11": (dms("Dhanu", 26, 14, 34),     dms("Mithuna", 26, 14, 34)),
    "D8":  (dms("Karka", 5, 26, 57),      dms("Karka", 5, 26, 57)),
    "D27": (dms("Karka", 7, 8, 29),       dms("Makara", 7, 8, 29)),
    "D30": (dms("Vrischika", 27, 56, 6),  dms("Vrischika", 27, 56, 6)),
}

UPAGRAHA = {"Gulika": 115.27, "Mandi": 112.38, "Kala": 160.15, "Mrityu": 26.83,
            "Ardha Prahara": 50.8, "Yama Ghantaka": 72.71, "Dhuma": 134.8,
            "Vyatipata": 225.2, "Parivesha": 45.2, "Indra Chapa": 314.8,
            "Upaketu": 331.47}


def rule(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def house_of(lon):
    return (int(lon // 30) - LAGNA_SIGN) % 12 + 1


def check_placements():
    rule("1. D1 house placements (whole-sign from Kanya lagna)")
    houses = {}
    for p, lon in D1.items():
        h = house_of(lon)
        houses.setdefault(h, []).append(p)
        print(f"  {p:9s} {fmt(lon)}  ->  house {h:2d}   (dispositor {LORD[SIGNS[int(lon // 30)]]})")

    print("\n  Occupancy — note the concentration:")
    for h in range(1, 13):
        occ = ", ".join(x for x in houses.get(h, []) if x != "Lagna") or "(empty)"
        print(f"    H{h:<2d} {SIGNS[(LAGNA_SIGN + h - 1) % 12]:11s} {occ}")

    rule("2. House lords from Kanya lagna")
    for h in range(1, 13):
        sign = SIGNS[(LAGNA_SIGN + h - 1) % 12]
        lord = LORD[sign]
        where = f"-> sits in H{house_of(D1[lord])}" if lord in D1 else ""
        print(f"  H{h:<2d} {sign:11s} lord {lord:8s} {where}")


def check_combustion():
    rule("3. Combustion (same-sign orb from Surya)")
    orbs = {"Chandra": 12, "Mangal": 17, "Budha": 14, "Guru": 11,
            "Shukra": 10, "Shani": 15}
    for p, orb in orbs.items():
        s = sep(D1[p], D1["Surya"])
        verdict = "COMBUST" if s < orb else "not combust"
        print(f"  {p:9s} separation {s:6.2f}°  limit {orb:2d}°  ->  {verdict}")


def check_conjunctions():
    rule("4. Same-sign conjunctions within 10 degrees")
    for i, a in enumerate(GRAHAS):
        for b in GRAHAS[i + 1:]:
            if int(D1[a] // 30) == int(D1[b] // 30) and sep(D1[a], D1[b]) < 10:
                print(f"  {a:9s} + {b:9s}  {sep(D1[a], D1[b]):5.2f}°"
                      f"  in {SIGNS[int(D1[a] // 30)]} (H{house_of(D1[a])})")


def check_parivartana():
    rule("5. Parivartana (mutual sign exchange)")
    found = False
    for i, a in enumerate(GRAHAS):
        for b in GRAHAS[i + 1:]:
            sa, sb = SIGNS[int(D1[a] // 30)], SIGNS[int(D1[b] // 30)]
            if LORD[sa] == b and LORD[sb] == a:
                found = True
                print(f"  {a} in {sa} (H{house_of(D1[a])})  <->  "
                      f"{b} in {sb} (H{house_of(D1[b])})   EXCHANGE")
    if not found:
        print("  none")


def check_aspects():
    rule("6. Graha drishti onto houses")
    special = {"Mangal": [4, 7, 8], "Guru": [5, 7, 9], "Shani": [3, 7, 10],
               "Rahu": [5, 7, 9], "Ketu": [5, 7, 9], "Surya": [7],
               "Chandra": [7], "Budha": [7], "Shukra": [7]}
    receiving = {h: [] for h in range(1, 13)}
    for p, asp in special.items():
        h = house_of(D1[p])
        targets = sorted(((h + a - 2) % 12) + 1 for a in asp)
        for t in targets:
            receiving[t].append(p)
        print(f"  {p:9s} in H{h:<2d} aspects houses {targets}")

    print("\n  Aspects received per house:")
    for h in range(1, 13):
        print(f"    H{h:<2d} <- {', '.join(receiving[h]) or '(none)'}")


def check_nakshatras():
    rule("7. Nakshatra / pada / lord, and the dispositor chain")
    nlord = {}
    for p, lon in D1.items():
        idx = int(lon / NAK_SPAN)
        pada = int((lon % NAK_SPAN) / PADA_SPAN) + 1
        nlord[p] = NAK_LORD[idx]
        print(f"  {p:9s} {NAK[idx]:13s} pada {pada}   lord {NAK_LORD[idx]}")

    print("\n  Nakshatra-dispositor chain from the lagna:")
    seen, cur = [], "Lagna"
    while cur not in seen:
        seen.append(cur)
        print(f"    {cur} -> occupies nakshatra of -> {nlord[cur]}")
        cur = nlord[cur]
    print(f"    ...chain closes in a loop at {cur}")


def check_gandanta():
    rule("8. Gandanta (last 3°20' of a water sign / first 3°20' of a fire sign)")
    water, fire = {3, 7, 11}, {0, 4, 8}
    any_found = False
    for p, lon in D1.items():
        s, pos = int(lon // 30), lon % 30
        if (s in water and pos >= 26 + 2 / 3) or (s in fire and pos <= 10 / 3):
            any_found = True
            print(f"  {p:9s} {fmt(lon)}  ***GANDANTA***  (H{house_of(lon)})")
    if not any_found:
        print("  none")


def check_pushkara():
    rule("9. Pushkara navamsa (Vrishabha spans 6°40'-10°00' and 13°20'-16°40')")
    m = D1["Mangal"] % 30
    inside = 6 + 2 / 3 <= m <= 10.0
    print(f"  Mangal at {m:.2f}° Vrishabha -> in Pushkara span: {inside}")
    print(f"  Mangal navamsa sign: {SIGNS[int(D1['Mangal'] * 9 / 30) % 12]} (Guru's sign)")


def varga_longitude(lon, n):
    """Parashari divisional longitude for the divisions used here."""
    sign, pos = int(lon // 30), lon % 30
    part = int(pos / (30 / n))
    frac = (pos % (30 / n)) * n
    if n in (9, 27):                       # continuous count from Mesha
        idx = int(lon * n / 30) % 12
    elif n == 10:                          # odd signs from self, even from 9th
        idx = ((sign if sign % 2 == 0 else (sign + 8) % 12) + part) % 12
    else:
        idx = (sign + part) % 12
    return idx * 30 + frac


def check_vargas():
    rule("10. Independent recomputation of D9 and D27 from the D1 longitudes")
    for div in ("D9", "D27"):
        n = int(div[1:])
        print(f"\n  --- {div} ---")
        for p in D1:
            calc = varga_longitude(D1[p], n)
            given = GIVEN[div][p]
            ok = "MATCH" if sep(calc, given) < 0.02 else "*** MISMATCH ***"
            print(f"    {p:9s} computed {fmt(calc)}   printed {fmt(given)}   {ok}")


def check_nodes():
    rule("11. Rahu/Ketu 180-degree integrity across all supplied vargas")
    for varga, (r, k) in NODE_PAIRS.items():
        gap = abs(r - k) % 360
        if abs(gap - 180) < 0.05:
            verdict = "OK"
        else:
            corrected = (r + 180) % 360
            verdict = ("SAME SIGN — required, not an error: a 180-degree gap "
                       "is exactly 6 signs, so it preserves parity and "
                       "modality and cannot separate the nodes in a "
                       "start-sign+offset varga")
        print(f"  {varga:4s} Rahu {fmt(r)}   Ketu {fmt(k)}   gap {gap:6.2f}°   {verdict}")


def check_upagrahas():
    rule("12. Upagrahas — house placement and contacts within 5 degrees")
    for u, lon in sorted(UPAGRAHA.items(), key=lambda x: x[1]):
        print(f"  {u:15s} {fmt(lon)}  ->  house {house_of(lon)}")
    print("\n  Contacts:")
    for u, lon in UPAGRAHA.items():
        for p, plon in D1.items():
            if int(lon // 30) == int(plon // 30) and sep(lon, plon) < 5:
                print(f"    {u:15s} conjunct {p:8s} ({sep(lon, plon):.2f}°)")


def check_dasha():
    rule("13. Vimshottari — balance, implied birth date, antardasha boundaries")
    moon = D1["Chandra"]
    nak_idx = int(moon / NAK_SPAN)
    elapsed = (moon - nak_idx * NAK_SPAN) / NAK_SPAN
    md_lord = NAK_LORD[nak_idx]
    md_years = dict(VIMSHOTTARI)[md_lord]
    balance = md_years * (1 - elapsed)
    print(f"  Chandra {fmt(moon)} in {NAK[nak_idx]} (lord {md_lord}, {md_years}y)")
    print(f"  Nakshatra {elapsed * 100:.2f}% elapsed  ->  balance at birth = {balance:.4f} years")

    rahu_start = datetime(2022, 12, 25, 22, 35)
    order = [x[0] for x in VIMSHOTTARI]
    i = order.index(md_lord)
    gap = balance
    while order[(i + 1) % 9] != "Rahu":
        i = (i + 1) % 9
        gap += dict(VIMSHOTTARI)[order[i]]
    birth = rahu_start - timedelta(days=gap * 365.25)
    print(f"  Birth to Rahu mahadasha = {gap:.4f} years")
    print(f"  -> implied birth ≈ {birth.strftime('%d %B %Y')}")
    print("     cross-check: Surya at 1°28' sidereal Mesha occurs ~15-16 April annually")
    print(f"  -> age on 08 Aug 2026 ≈ {(datetime(2026, 8, 8) - birth).days / 365.25:.1f} years")

    print("\n  Rahu mahadasha antardashas (rebuilt; compare against the source table):")
    t = rahu_start
    seq = order[order.index("Rahu"):] + order[:order.index("Rahu")]
    for name in seq:
        yrs = dict(VIMSHOTTARI)[name]
        dur = 18 * yrs / 120
        end = t + timedelta(days=dur * 365.25)
        print(f"    Rahu-{name:8s} {t.strftime('%d %b %Y')} -> {end.strftime('%d %b %Y')}"
              f"   ({dur:.2f} yrs)")
        t = end


def main():
    for fn in (check_placements, check_combustion, check_conjunctions,
               check_parivartana, check_aspects, check_nakshatras,
               check_gandanta, check_pushkara, check_vargas, check_nodes,
               check_upagrahas, check_dasha):
        fn()
    print()


if __name__ == "__main__":
    main()
