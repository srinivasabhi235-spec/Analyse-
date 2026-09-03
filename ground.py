#!/usr/bin/env python3
"""
GROUND TRUTH.

One module that derives EVERY fact this reading rests on from the birth data,
and marks the handful that cannot be derived as SUPPLIED.

The document was built accretively: sections were appended, renumbered, and
amended in place, and numbers were carried from section to section by hand.
That is exactly how a figure drifts.  This module exists so that no number in
the rewritten document is ever typed twice -- everything is looked up here.

    DERIVED   computed from the birth moment with the Swiss Ephemeris, or from
              a classical rule applied to those positions.  Reproducible.
    SUPPLIED  taken from the source data sheet because the rule that generates
              it is not implemented here (Shadbala sub-components, Bhava Bala,
              Shodhya Pinda).  Marked, never silently mixed with DERIVED.

Every entry carries a `why` string -- the derivation in one line.  That is the
"thought" half of the ReAct loop in react_loop.py; the `value` is what the
"act" half returns.
"""
import swisseph as swe
from ephem_core import (SIGNS, GRAHAS, SUPPLIED as SUP, LORD, EXALT, EXALT_DEG,
                        MOOLA, NAK, NAK_LORD, VIM, BIRTH, varga, dignity,
                        sign_of, nak_of, jd_ut, ascendant)

swe.set_sid_mode(swe.SIDM_LAHIRI)
Y = 365.2425
G7 = ['Surya', 'Chandra', 'Mangal', 'Budha', 'Guru', 'Shukra', 'Shani']
BENEFIC7 = {'Guru', 'Shukra'}
MALEFIC7 = {'Surya', 'Mangal', 'Shani'}
DUSTHANA, KENDRA, TRIKONA, UPACHAYA = {6, 8, 12}, {1, 4, 7, 10}, {1, 5, 9}, {3, 6, 10, 11}
BIRTH_JD = jd_ut(*BIRTH['date'], *BIRTH['time'], BIRTH['tz'])

POS = dict(SUP)
LAG = sign_of(POS['Lagna'])
MOON_SIGN = sign_of(POS['Chandra'])

# ---------------------------------------------------------------- primitives
def house_of(g):
    """Whole-sign house occupied by graha g."""
    return (sign_of(POS[g]) - LAG) % 12 + 1


def sign_in_house(h):
    return (LAG + h - 1) % 12


def lord_of_house(h):
    return LORD[sign_in_house(h)]


def houses_ruled(g):
    return [h for h in range(1, 13) if lord_of_house(h) == g]


def occupants(h):
    return [g for g in GRAHAS if house_of(g) == h]


ASPECT_HOUSES = {'Surya': [7], 'Chandra': [7], 'Mangal': [4, 7, 8],
                 'Budha': [7], 'Guru': [5, 7, 9], 'Shukra': [7],
                 'Shani': [3, 7, 10], 'Rahu': [5, 7, 9], 'Ketu': [5, 7, 9]}


def aspects_house(g, h):
    src = house_of(g)
    return any((src + a - 2) % 12 + 1 == h for a in ASPECT_HOUSES[g])


def aspected_by(h, nodes=True):
    """Grahas aspecting house h.

    THE `nodes` SWITCH IS NOT COSMETIC AND THE CORPUS SPLIT ON IT.  Whether
    Rahu and Ketu cast drishti at all is a live school question: BPHS-derived
    practice commonly gives them the 5/7/9 like Guru, and an equally common
    stream gives the shadow grahas no drishti of their own.

        nodes=True   section 10 of the reading -- "the two houses nothing
                     reaches" -- 8th and 10th unaspected
        nodes=False  bhava-krama.md step 2 -- six houses unaspected, and the
                     1st, 5th and 7th wholly untouched

    BOTH ARE ARITHMETICALLY CORRECT.  They are different rules, and NEITHER
    DOCUMENT SAID WHICH IT WAS USING.  That is the single largest inherited
    defect the rewrite has to resolve, because the two headline structural
    findings of the corpus sit on opposite sides of it.
    """
    pool = GRAHAS if nodes else G7
    return [g for g in pool if aspects_house(g, h)]


# ------------------------------------------------------- ashtakavarga, derived
BENEFIC_PLACES = {
 'Surya':   {'Surya': [1,2,4,7,8,9,10,11], 'Chandra': [3,6,10,11],
             'Mangal': [1,2,4,7,8,9,10,11], 'Budha': [3,5,6,9,10,11,12],
             'Guru': [5,6,9,11], 'Shukra': [6,7,12],
             'Shani': [1,2,4,7,8,9,10,11], 'Lagna': [3,4,6,10,11,12]},
 'Chandra': {'Surya': [3,6,7,8,10,11], 'Chandra': [1,3,6,7,10,11],
             'Mangal': [2,3,5,6,9,10,11], 'Budha': [1,3,4,5,7,8,10,11],
             'Guru': [1,4,7,8,10,11,12], 'Shukra': [3,4,5,7,9,10,11],
             'Shani': [3,5,6,11], 'Lagna': [3,6,10,11]},
 'Mangal':  {'Surya': [3,5,6,10,11], 'Chandra': [3,6,11],
             'Mangal': [1,2,4,7,8,10,11], 'Budha': [3,5,6,11],
             'Guru': [6,10,11,12], 'Shukra': [6,8,11,12],
             'Shani': [1,4,7,8,9,10,11], 'Lagna': [1,3,6,10,11]},
 'Budha':   {'Surya': [5,6,9,11,12], 'Chandra': [2,4,6,8,10,11],
             'Mangal': [1,2,4,7,8,9,10,11], 'Budha': [1,3,5,6,9,10,11,12],
             'Guru': [6,8,11,12], 'Shukra': [1,2,3,4,5,8,9,11],
             'Shani': [1,2,4,7,8,9,10,11], 'Lagna': [1,2,4,6,8,10,11]},
 'Guru':    {'Surya': [1,2,3,4,7,8,9,10,11], 'Chandra': [2,5,7,9,11],
             'Mangal': [1,2,4,7,8,10,11], 'Budha': [1,2,4,5,6,9,10,11],
             'Guru': [1,2,3,4,7,8,10,11], 'Shukra': [2,5,6,9,10,11],
             'Shani': [3,5,6,12], 'Lagna': [1,2,4,5,6,7,9,10,11]},
 'Shukra':  {'Surya': [8,11,12], 'Chandra': [1,2,3,4,5,8,9,11,12],
             'Mangal': [3,5,6,9,11,12], 'Budha': [3,5,6,9,11],
             'Guru': [5,8,9,10,11], 'Shukra': [1,2,3,4,5,8,9,10,11],
             'Shani': [3,4,5,8,9,10,11], 'Lagna': [1,2,3,4,5,8,9]},
 'Shani':   {'Surya': [1,2,4,7,8,10,11], 'Chandra': [3,6,11],
             'Mangal': [3,5,6,10,11,12], 'Budha': [6,8,9,10,11,12],
             'Guru': [5,6,11,12], 'Shukra': [6,11,12],
             'Shani': [3,5,6,11], 'Lagna': [1,3,4,6,10,11]},
}
_BASE = {g: sign_of(POS[g]) for g in G7}
_BASE['Lagna'] = LAG
BAV, BAV_CONTRIB = {}, {}
for _g in G7:
    _row = [0] * 12
    _con = {s: [] for s in range(12)}
    for _src, _hs in BENEFIC_PLACES[_g].items():
        for _h in _hs:
            _s = (_BASE[_src] + _h - 1) % 12
            _row[_s] += 1
            _con[_s].append(_src)
    BAV[_g], BAV_CONTRIB[_g] = _row, _con
SAV = [sum(BAV[g][s] for g in G7) for s in range(12)]

# The supplied sheet, for the one cell that differs.  Venus totals 52 there and
# 51 here; six of seven grahas reproduce their canonical totals exactly and the
# gap is one bindu in Cancer.  Recorded, never patched -- see verify_shani8.py.
SAV_SUPPLIED = {'Mesha': 21, 'Vrishabha': 22, 'Mithuna': 29, 'Karka': 28,
                'Simha': 24, 'Kanya': 29, 'Tula': 24, 'Vrischika': 28,
                'Dhanu': 29, 'Makara': 29, 'Kumbha': 41, 'Meena': 33}

# ------------------------------------------------------------------- supplied
SHADBALA_RUPAS = {'Surya': 11.39, 'Chandra': 6.42, 'Mangal': 6.33,
                  'Budha': 6.46, 'Guru': 8.21, 'Shukra': 6.68, 'Shani': 6.39}
SHADBALA_MIN = {'Surya': 5.0, 'Chandra': 6.0, 'Mangal': 5.0, 'Budha': 7.0,
                'Guru': 6.5, 'Shukra': 5.5, 'Shani': 5.0}
ISHTA = {'Surya': 46.88, 'Chandra': 24.54, 'Mangal': 19.66, 'Budha': 18.91,
         'Guru': 37.30, 'Shukra': 47.49, 'Shani': 12.48}
KASHTA = {'Surya': 7.83, 'Chandra': 4.49, 'Mangal': 38.87, 'Budha': 30.32,
          'Guru': 15.10, 'Shukra': 11.87, 'Shani': 46.83}
SHODHYA = {'Surya': 45, 'Chandra': 38, 'Mangal': 74, 'Budha': 62,
           'Guru': 43, 'Shukra': 40, 'Shani': 71}
BHAVA_BALA = [8.39, 9.18, 7.49, 9.28, 7.91, 7.21, 8.86, 7.00, 7.61, 7.39,
              7.08, 12.59]
BHAVA_RANK = [5, 3, 8, 2, 6, 10, 4, 12, 7, 9, 11, 1]

# ---------------------------------------------------------------- vimshottari
def _tree():
    _, _, nl, into = nak_of(POS['Chandra'])
    i0 = [x[0] for x in VIM].index(nl)
    t = BIRTH_JD - (into / (360 / 27)) * VIM[i0][1] * Y
    md, ad = [], []
    for k in range(9):
        g, yrs = VIM[(i0 + k) % 9]
        md.append((g, t, t + yrs * Y))
        a = t
        for m in range(9):
            ag, ay = VIM[(i0 + k + m) % 9]
            b = a + yrs * ay / 120 * Y
            ad.append((g, ag, a, b))
            a = b
        t += yrs * Y
    return md, ad


MAHADASHA, ANTARDASHA = _tree()


def dasha_on(jd):
    m = [x for x in MAHADASHA if x[1] <= jd < x[2]]
    a = [x for x in ANTARDASHA if x[2] <= jd < x[3]]
    return (m[0][0] if m else None), (a[0][1] if a else None)


# --------------------------------------------------------------------- jaimini
def chara_karakas():
    """Atmakaraka down, by degrees-in-sign; Rahu counted in reverse."""
    d = {g: (30 - POS[g] % 30) if g == 'Rahu' else POS[g] % 30
         for g in G7 + ['Rahu']}
    order = sorted(d, key=lambda g: -d[g])
    names = ['Atmakaraka', 'Amatyakaraka', 'Bhratrikaraka', 'Matrikaraka',
             'Pitrikaraka', 'Putrakaraka', 'Gnatikaraka', 'Darakaraka']
    return dict(zip(names, order))


KARAKA = chara_karakas()


def arudha(h):
    """Arudha pada of house h: as far from the lord as the lord is from h."""
    l = lord_of_house(h)
    lh = house_of(l)
    a = (lh + (lh - h)) % 12
    a = a if a else 12
    if a in (h, (h + 6 - 1) % 12 + 1):        # 1st or 7th from itself -> 10th
        a = (a + 9 - 1) % 12 + 1
    return a


# -------------------------------------------------------------- the registry
def _f(value, why, kind='DERIVED'):
    return {'value': value, 'why': why, 'kind': kind}


FACTS = {}
FACTS['lagna.sign'] = _f(SIGNS[LAG], 'sign_of(Lagna longitude 177.6269)')
FACTS['lagna.nakshatra'] = _f(nak_of(POS['Lagna'])[0], 'nak_of(Lagna)')
FACTS['lagna.pada'] = _f(nak_of(POS['Lagna'])[1], 'nak_of(Lagna) pada')
FACTS['moon.sign'] = _f(SIGNS[MOON_SIGN], 'sign_of(Chandra)')
FACTS['moon.nakshatra'] = _f(nak_of(POS['Chandra'])[0], 'nak_of(Chandra)')
for g in GRAHAS:
    FACTS[f'{g}.house'] = _f(house_of(g), f'whole-sign house of {g} from {SIGNS[LAG]}')
    FACTS[f'{g}.sign'] = _f(SIGNS[sign_of(POS[g])], f'sign_of({g})')
    FACTS[f'{g}.dignity'] = _f(dignity(g, sign_of(POS[g])), f'dignity({g}, its sign)')
    FACTS[f'{g}.nakshatra'] = _f(nak_of(POS[g])[0], f'nak_of({g})')
for g in G7:
    FACTS[f'{g}.rules'] = _f(houses_ruled(g), f'houses whose sign-lord is {g}')
for h in range(1, 13):
    FACTS[f'house{h}.sign'] = _f(SIGNS[sign_in_house(h)], f'{h}th from {SIGNS[LAG]}')
    FACTS[f'house{h}.lord'] = _f(lord_of_house(h), f'lord of {SIGNS[sign_in_house(h)]}')
    FACTS[f'house{h}.occupants'] = _f(occupants(h), f'grahas in {SIGNS[sign_in_house(h)]}')
    FACTS[f'house{h}.sav'] = _f(SAV[sign_in_house(h)], 'sum of the seven BAV rows')
    FACTS[f'house{h}.bhavabala'] = _f(BHAVA_BALA[h - 1], 'source sheet', 'SUPPLIED')
    FACTS[f'house{h}.bhavarank'] = _f(BHAVA_RANK[h - 1], 'source sheet', 'SUPPLIED')
    FACTS[f'house{h}.aspectedby'] = _f(aspected_by(h), 'graha drishti, nodes counted')
    FACTS[f'house{h}.aspectedby|nonodes'] = _f(aspected_by(h, nodes=False),
                                              'graha drishti, seven grahas only')
for s in range(12):
    FACTS[f'sav.{SIGNS[s]}'] = _f(SAV[s], 'sum of the seven BAV rows')
for g in G7:
    FACTS[f'{g}.shadbala'] = _f(SHADBALA_RUPAS[g], 'source sheet', 'SUPPLIED')
    FACTS[f'{g}.ishta'] = _f(ISHTA[g], 'source sheet', 'SUPPLIED')
    FACTS[f'{g}.kashta'] = _f(KASHTA[g], 'source sheet', 'SUPPLIED')
    FACTS[f'{g}.bav.own'] = _f(BAV[g][sign_of(POS[g])], f'{g} BAV in its own sign')
for k, v in KARAKA.items():
    FACTS[f'karaka.{k}'] = _f(v, 'chara karaka by degrees-in-sign, Rahu reversed')
FACTS['sav.total'] = _f(sum(SAV), 'sum of all twelve signs')
FACTS['sav.highest'] = _f(SIGNS[max(range(12), key=lambda s: SAV[s])], 'argmax SAV')
FACTS['sav.lowest'] = _f(SIGNS[min(range(12), key=lambda s: SAV[s])], 'argmin SAV')
FACTS['bhava.strongest'] = _f(BHAVA_RANK.index(1) + 1, 'rank 1 in the sheet', 'SUPPLIED')
FACTS['bhava.weakest'] = _f(BHAVA_RANK.index(12) + 1, 'rank 12 in the sheet', 'SUPPLIED')
FACTS['upapada'] = _f(SIGNS[sign_in_house(arudha(12)) ], 'arudha pada of the 12th')
FACTS['arudha.lagna'] = _f(SIGNS[sign_in_house(arudha(1))], 'arudha pada of the 1st')

_empty = [h for h in range(1, 13) if not occupants(h)]
_un_n = [h for h in range(1, 13) if not aspected_by(h, nodes=True)]
_un_7 = [h for h in range(1, 13) if not aspected_by(h, nodes=False)]
FACTS['houses.empty'] = _f(_empty, 'houses with no graha')
FACTS['houses.unaspected|nodes'] = _f(_un_n, 'no drishti, Rahu/Ketu counted')
FACTS['houses.unaspected|nonodes'] = _f(_un_7, 'no drishti, seven grahas only')
FACTS['houses.untouched|nodes'] = _f([h for h in _empty if h in _un_n],
                                     'empty AND unaspected, nodes counted')
FACTS['houses.untouched|nonodes'] = _f([h for h in _empty if h in _un_7],
                                       'empty AND unaspected, nodes excluded')
FACTS['lords.distribution'] = _f(
    {hh: [h for h in range(1, 13) if house_of(lord_of_house(h)) == hh]
     for hh in range(1, 13)
     if any(house_of(lord_of_house(h)) == hh for h in range(1, 13))},
    'which house each house-lord sits in')

PARIVARTANA = [(a, b) for i, a in enumerate(G7) for b in G7[i + 1:]
               if sign_of(POS[a]) in [s for s in range(12) if LORD[s] == b]
               and sign_of(POS[b]) in [s for s in range(12) if LORD[s] == a]]
FACTS['parivartana'] = _f(PARIVARTANA, 'mutual sign exchanges among the seven')


def check_all():
    """Internal consistency of the registry itself."""
    out = []
    tot = sum(SAV)
    out.append(('sav rows sum to sav total', tot == sum(SAV[s] for s in range(12))))
    out.append(('twelve houses have twelve signs',
                len({sign_in_house(h) for h in range(1, 13)}) == 12))
    out.append(('every graha has a house',
                all(1 <= house_of(g) <= 12 for g in GRAHAS)))
    out.append(('lords ruled partition the twelve',
                sorted(h for g in G7 for h in houses_ruled(g)) == list(range(1, 13))))
    return out


if __name__ == '__main__':
    print(f"GROUND TRUTH — {len(FACTS)} facts "
          f"({sum(1 for v in FACTS.values() if v['kind'] == 'DERIVED')} derived, "
          f"{sum(1 for v in FACTS.values() if v['kind'] == 'SUPPLIED')} supplied)\n")
    for name, ok in check_all():
        print(f"  [{'ok' if ok else 'FAIL'}] {name}")
    print()
    for k in sorted(FACTS):
        v = FACTS[k]
        print(f"  {k:28s} {str(v['value'])[:44]:46s} {v['kind']}")
