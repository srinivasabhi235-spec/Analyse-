#!/usr/bin/env python3
"""
THE ReAct LOOP.

Reason -> Act -> Observe -> Reflect, run to fixpoint over the whole document.

The reading was built by appending.  Sections were inserted, everything after
them was renumbered, figures were carried from one section to the next by hand,
and corrections were annotated in place.  Every one of those operations is a
chance for a number to drift, and prose review does not catch drift -- it reads
fluently either way.

So this does not review the prose.  It EXTRACTS EVERY CHECKABLE CLAIM FROM THE
TEXT and re-derives each one from ground.py:

    REASON    a pattern says "this sentence is asserting X about Y"
    ACT       compute the true value of X for Y from the birth data
    OBSERVE   what came back
    REFLECT   PASS, FAIL, or CONTINGENT -- true under one school and false
              under another, which is not an error but MUST be labelled

CONTINGENT IS THE VERDICT THAT MATTERS.  A claim that is simply wrong gets
fixed once.  A claim that is true under a rule the document never declared will
keep coming back, and will contradict a different section that quietly chose
the other rule.  The corpus already contains exactly one such contradiction
between its two most quotable structural findings, and the loop found it.

Usage:
    python3 react_loop.py [file ...]        report
    python3 react_loop.py --fails           failures only
    python3 react_loop.py --trace <n>       show the reasoning for claim n
"""
import re
import sys
from collections import Counter

import ground as G
from ephem_core import SIGNS, GRAHAS

ORD = {1: 'st', 2: 'nd', 3: 'rd', 21: 'st', 22: 'nd', 23: 'rd'}
ordn = lambda n: f"{n}{ORD.get(n, 'th')}"
NUM = {w: i for i, w in enumerate(
    ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
     'nine', 'ten', 'eleven', 'twelve'])}
GNAMES = '|'.join(GRAHAS)
SNAMES = '|'.join(SIGNS)
PASS, FAIL, CONTINGENT = 'PASS', 'FAIL', 'CONTINGENT'
VARGAS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 18, 20, 22,
          24, 27, 30, 36, 40, 45, 60, 81, 108, 144, 150)


VARGA_NAME = {'hora': 2, 'drekkana': 3, 'decanate': 3, 'chaturthamsha': 4,
              'saptamsha': 7, 'sapthamsa': 7, 'navamsa': 9, 'navamsha': 9,
              'dashamsha': 10, 'dasamsa': 10, 'dvadashamsha': 12,
              'shodashamsha': 16, 'vimshamsha': 20, 'siddhamsha': 24,
              'bhamsha': 27, 'trimshamsha': 30, 'khavedamsha': 40,
              'akshavedamsha': 45, 'shashtiamsha': 60, 'nava-navamsa': 81}

# A line carrying any of these is not asserting a natal whole-sign placement.
# Each pattern is a REASON TO NOT ACT, and the loop records why rather than
# guessing -- a wrong actor is worse than no actor.
NOT_A_NATAL_CLAIM = [
    (r'\bfrom the (?:natal )?(?:Moon|Chandra|Karakamsa|Upapada|Arudha|lagna)',
     'counted from a reference point other than the lagna'),
    (r'\bfrom (?:Chandra|Karakamsa|the Upapada|the Arudha)\b',
     'counted from a reference point other than the lagna'),
    (r'\btransit\b|\bgochara\b|\bSade Sati\b|\bingress\b|\bcrosses\b',
     'a transit claim, not a natal placement'),
    (r'\bis not\b|\bnot exalted\b|\bnot debilitated\b|\bnever\b',
     'a negation'),
    (r'directional strength|\bdigbala\b|\bdig bala\b',
     'directional strength names a house without placing the graha there'),
    (r'\bafflicts\b|\bis favourable in\b|\bbenefic in\b|\bthe rule\b'
     r'|\bwould\b|\bif \b',
     'a statement of a rule, not of this chart'),
    (r'\bD\d+ lagna\b|\bLagna \*\*',
     'names a varga ascendant rather than a placement'),
    (r'\*"',
     'a quotation of another section'),
    (r'\bKarakamsa\b',
     'counted from the Karakamsa, not the lagna'),
    (r'\bits \d+(?:st|nd|rd|th)\b|\brepeating its\b|\bits lagna\b',
     "a possessive house ('its 8th') belongs to a varga this line does not name"),
    (r'\b(?:19|20)\d{2}\b|\bthat span\b|\bfor most of\b',
     'a dated claim — a transit window, not a natal placement'),
    (r'\|\s*(?:No|Yes)\s*[—-]|^\|\s*\d+\.',
     'a rule-test table row: the left cell states the rule, not the chart'),
    (r'\bas \*\*|\bacross a set\b|\bmost \w+ graha\b',
     'a comparison or a cross-varga census, not a placement'),
]


def frame_of(line, carried):
    """Which chart is this line talking about?  Returns (varga_n, reason)."""
    for pat, why in NOT_A_NATAL_CLAIM:
        if re.search(pat, line, re.I):
            return None, why
    # A BINDING construction attaches the claim to the varga wherever it sits
    # in the line: "in the 7th OF D9", "D12'S 12th", "exalted: D27".
    b = re.search(r"""(?:of|in)\s+(?:the\s+)?\**D(\d+)\b|\bD(\d+)'s\b|[:—-]\s*\**D(\d+)\b""", line)
    if b:
        n = int(next(x for x in b.groups() if x))
        if n in VARGAS:
            return n, None
    m = re.search(r'\bD(\d+)\b', line)
    if m and int(m.group(1)) in VARGAS:
        # Positional: '| in the 10th · D10 trikona |' asserts a NATAL 10th and
        # then qualifies it.  A bare D-label only frames what follows it.
        return (int(m.group(1)), None) if m.start() < 12 else (carried, None)
    for nm, n in VARGA_NAME.items():
        if re.search(rf'\b{nm}\b', line, re.I):
            return n, None
    return carried, None


TRANSIT_SECTION = re.compile(
    r'^#{2,3} .*(transit|through the|gochara|grahan|eclipse|Sade Sati'
    r'|travels|when will|when would|timing)', re.I)


def carried_frame(line, cur):
    """What chart the surrounding block is about.

    A '**D24 - Siddhamsha.**' lead-in sets it, and so does a SECTION HEADING
    that names a varga -- '## 46. The D81, computed' means the whole section is
    talking about D81, including blockquotes several paragraphs down that never
    repeat the name.  Blank lines no longer reset it; only a new heading does.
    """
    m = re.match(r'\*\*D(\d+)[ .·]', line.strip())
    if m:
        return int(m.group(1))
    # bhava-krama's step 5 is written '**5. Varga (D11).**' and frames the
    # sentences after it, including one that says only 'exalted there'.
    m = re.search(r'\*\*\d+\. Varga \(D(\d+)\)', line)
    if m:
        return int(m.group(1))
    if re.match(r'^#{2,4} ', line):
        h = re.search(r'\bD(\d+)\b', line)
        return int(h.group(1)) if h else 1
    return cur


class Claim:
    __slots__ = ('file', 'line', 'kind', 'subject', 'asserted', 'observed',
                 'verdict', 'why', 'text', 'varga', 'ctx')

    def __init__(self, file, line, kind, subject, asserted, text, varga=1):
        self.file, self.line, self.kind = file, line, kind
        self.subject, self.asserted, self.text = subject, asserted, text
        self.varga = varga
        self.ctx = None
        self.observed = self.verdict = self.why = None


# ---------------------------------------------------------------- extractors
# Each returns (kind, subject, asserted) tuples for one line of text.

def _bind_back(line, pos, maxdist=40):
    """The graha a trailing predicate attaches to: the NEAREST one before it.

    The first version of this bound to the FIRST graha within a span, so
    "Chandra in own sign, Shukra, and Mangal debilitated" attached
    'debilitated' to Chandra.  Every one of those was reported as a document
    error and none of them was.  Nearest-binding is the fix.
    """
    head = line[:pos]
    cut = max(head.rfind(';'), head.rfind('. '), head.rfind('|'))
    last = None
    for m in re.finditer(rf'\b({GNAMES})\b', head):
        if m.start() > cut:
            last = m
    if last and pos - last.end() <= maxdist:
        return last.group(1)
    return None


def x_house(line):
    """'Guru ... in the 10th' — bound to the nearest preceding graha."""
    for m in re.finditer(r'\b(?:in|occupies) the (\d+)(?:st|nd|rd|th)\b', line):
        g = _bind_back(line, m.start())
        if g:
            yield ('house', g, int(m.group(1)))


def _sign_near(line, gpos, dpos, dend=None):
    """A sign named between the graha and the dignity word, or just after it.

    Reference and transit tables read '| Mangal | Karka | ... | debilitated |'
    and '| Chandra | Vrischika | debilitated |'.  Those are TRUE statements
    about the graha IN THAT SIGN, not about its natal sign, and the first
    version of this actor called every one of them an error.
    """
    lo, hi = min(gpos, dpos), max(gpos, dpos)
    m = re.search(rf'\b({SNAMES})\b', line[lo:hi])
    if m:
        return m.group(1)
    m = re.match(rf'\s+in\s+\**({SNAMES})\b', line[dend if dend else hi:])
    return m.group(1) if m else None


def x_dignity(line):
    """'Surya ... exalted' backward, and 'exalted Surya' forward."""
    for m in re.finditer(r'\b(exalted|debilitated)\b', line):
        f = re.match(rf'\s+(?:in\s+\w+\s+)?({GNAMES})\b', line[m.end():])
        if f:
            g, gp = f.group(1), m.end() + f.start(1)
        else:
            g = _bind_back(line, m.start(), 28)
            if not g:
                continue
            gp = line[:m.start()].rfind(g)
        yield ('dignity', g, m.group(1),
               _sign_near(line, gp, m.start(), m.end()))


def x_lord(line):
    """'Budha, the 10th lord' / 'the 9th lord Shukra' / 'its lord Surya'."""
    for m in re.finditer(rf'\b({GNAMES})\b,? (?:the |is the )'
                         rf'(\d+)(?:st|nd|rd|th) lord\b', line):
        yield ('lord', int(m.group(2)), m.group(1))
    for m in re.finditer(rf'\bthe (\d+)(?:st|nd|rd|th) lord,? ({GNAMES})\b',
                         line):
        yield ('lord', int(m.group(1)), m.group(2))


def x_house_sign(line):
    """'the 8th house is Mesha' / 'the 10th is Mithuna'."""
    for m in re.finditer(rf'\bthe (\d+)(?:st|nd|rd|th)(?: house)? is '
                         rf'\**({SNAMES})\b', line):
        yield ('house_sign', int(m.group(1)), m.group(2))


def x_sav(line):
    """'SAV 41' / 'Kumbha at 41' in a bindu context."""
    for m in re.finditer(rf'\b({SNAMES})\b[^|.]{{0,18}}?\bSAV (\d+)\b', line):
        yield ('sav', m.group(1), int(m.group(2)))
    for m in re.finditer(rf'\bSAV of ({SNAMES})\b[^|.]{{0,14}}?(\d+)\b', line):
        yield ('sav', m.group(1), int(m.group(2)))


def x_karaka(line):
    for m in re.finditer(rf'\b(Atmakaraka|Amatyakaraka|Darakaraka|'
                         rf'Putrakaraka)\b[^.|]{{0,14}}?\b({GNAMES})\b', line):
        yield ('karaka', m.group(1), m.group(2))
    for m in re.finditer(rf'\b({GNAMES})\b[^.|]{{0,20}}?\bis the (Atmakaraka|'
                         rf'Amatyakaraka|Darakaraka|Putrakaraka)\b', line):
        yield ('karaka', m.group(2), m.group(1))


def x_bhavarank(line):
    """'Bhava Bala 12.59 — rank 1 of 12'."""
    for m in re.finditer(r'\bthe (\d+)(?:st|nd|rd|th) house[^|.]{0,60}?'
                         r'rank (\d+) of 12', line):
        yield ('bhavarank', int(m.group(1)), int(m.group(2)))


def x_upapada(line):
    if re.search(r'from (?:the )?Upapada', line, re.I):
        return                      # "the 2nd from Upapada" is a different point
    for m in re.finditer(rf'\bUpapada\b(?: is| lands in|,)?[^.|]{{0,14}}?'
                         rf'\b({SNAMES})\b', line):
        yield ('upapada', None, m.group(1))


def x_unaspected(line):
    """The contested one: how many houses receive no aspect."""
    for m in re.finditer(r'houses receiving \*\*no aspect\*\*[^|]*\|\s*'
                         r'([\d, ]+)\s*—\s*\*\*(\w+)\*\*', line):
        yield ('unaspected_set',
               tuple(int(x) for x in m.group(1).replace(' ', '').split(',')),
               NUM.get(m.group(2), -1))
    for m in re.finditer(r'the (two|three|four|five|six) houses nothing '
                         r'reaches', line):
        yield ('unaspected_count', None, NUM[m.group(1)])


EXTRACTORS = [x_house, x_dignity, x_lord, x_house_sign, x_sav, x_karaka,
              x_bhavarank, x_upapada, x_unaspected]


# --------------------------------------------------------------------- actors
def act(c):
    """Compute the truth. Returns (observed, verdict, why)."""
    k, s, a = c.kind, c.subject, c.asserted

    v = c.varga

    if k == 'house':
        if v == 1:
            o = G.house_of(s)
            return o, PASS if o == a else FAIL, f'{s} is in the {ordn(o)}'
        gl = G.varga(G.POS['Lagna'], v)
        o = (G.varga(G.POS[s], v) - gl) % 12 + 1
        return o, PASS if o == a else FAIL, f'{s} is in the {ordn(o)} of D{v}'

    if k == 'dignity':
        if c.ctx:                       # the line names the sign — judge there
            sg, lbl = SIGNS.index(c.ctx), ' (sign named in the line)'
        elif v == 1:
            sg, lbl = G.sign_of(G.POS[s]), ''
        else:
            sg, lbl = G.varga(G.POS[s], v), f' of D{v}'
        o = G.dignity(s, sg)
        return o, PASS if o == a else FAIL, f'{s} is {o} in {SIGNS[sg]}{lbl}'

    if k == 'lord':
        o = G.lord_of_house(s)
        return o, PASS if o == a else FAIL, f'lord of the {ordn(s)} is {o}'

    if k == 'house_sign':
        o = SIGNS[G.sign_in_house(s)]
        return o, PASS if o == a else FAIL, f'the {ordn(s)} is {o}'

    if k == 'sav':
        o = G.SAV[SIGNS.index(s)]
        sup = G.SAV_SUPPLIED[s]
        if a == o:
            return o, PASS, f'SAV({s}) = {o} derived'
        if a == sup:
            return o, CONTINGENT, (f'SAV({s}) = {o} derived, {sup} on the '
                                   f'supplied sheet — the one-bindu Venus gap')
        return o, FAIL, f'SAV({s}) = {o}'

    if k == 'karaka':
        o = G.KARAKA[s]
        return o, PASS if o == a else FAIL, f'{s} is {o}'

    if k == 'bhavarank':
        o = G.BHAVA_RANK[s - 1]
        return o, PASS if o == a else FAIL, f'{ordn(s)} house rank {o} (supplied)'

    if k == 'upapada':
        o = G.FACTS['upapada']['value']
        return o, PASS if o == a else FAIL, f'arudha of the 12th is {o}'

    if k == 'unaspected_set':
        # s is the house tuple the text lists; a is the count it gives them.
        wn = tuple(G.FACTS['houses.unaspected|nodes']['value'])
        w7 = tuple(G.FACTS['houses.unaspected|nonodes']['value'])
        if s == w7 and a == len(w7):
            return w7, CONTINGENT, ('correct ONLY if Rahu and Ketu cast no '
                                    f'drishti; counting them it is {list(wn)}')
        if s == wn and a == len(wn):
            return wn, CONTINGENT, ('correct ONLY if the nodes DO aspect; '
                                    f'without them it is {list(w7)}')
        return w7, FAIL, (f'neither rule gives {list(s)} at {a}: nodes-excluded '
                          f'is {list(w7)}, nodes-included {list(wn)}')

    if k == 'unaspected_count':
        wn = len(G.FACTS['houses.unaspected|nodes']['value'])
        w7 = len(G.FACTS['houses.unaspected|nonodes']['value'])
        if a == wn:
            return wn, CONTINGENT, (f'{wn} with node drishti, {w7} without — '
                                    f'the document never declares which')
        if a == w7:
            return w7, CONTINGENT, (f'{w7} without node drishti, {wn} with — '
                                    f'the document never declares which')
        return wn, FAIL, f'{wn} with nodes, {w7} without'

    return None, PASS, 'no actor'


# ----------------------------------------------------------------- the loop
SKIP = re.compile(r'^\s*(```|\||>?\s*\*?\[?(Amended|Corrected|Retracted))')


SKIPPED = Counter()


def harvest(path):
    claims, cur, in_transit = [], 1, False
    for n, line in enumerate(open(path), 1):
        if line.startswith('```'):
            continue
        if line.startswith('## '):
            in_transit = bool(TRANSIT_SECTION.match(line))
        cur = carried_frame(line, cur)
        varga, why_skip = frame_of(line, cur)
        if in_transit and not why_skip:
            why_skip = ('inside a transit section — a dignity or house here '
                        'describes where a graha IS NOW, not the natal chart')
        hits = []
        for fn in EXTRACTORS:
            for row in fn(line):
                hits.append(row if len(row) == 4 else row + (None,))
        if why_skip:
            if hits:
                SKIPPED[why_skip] += len(hits)
            continue
        for kind, subj, asrt, ctx in hits:
            c = Claim(path, n, kind, subj, asrt, line.strip(), varga)
            c.ctx = ctx
            claims.append(c)
    return claims


def run(paths):
    claims = [c for p in paths for c in harvest(p)]
    for c in claims:
        c.observed, c.verdict, c.why = act(c)
    return claims


def report(claims, only_fails=False):
    tally = Counter(c.verdict for c in claims)
    by_kind = Counter(c.kind for c in claims)
    print('=' * 92)
    print('  ReAct LOOP — reason, act, observe, reflect')
    print('=' * 92)
    print(f"\n  {len(claims)} claims extracted from {len({c.file for c in claims})} file(s)\n")
    for k, v in sorted(by_kind.items(), key=lambda x: -x[1]):
        print(f"      {k:18s}{v:5d}")
    if SKIPPED:
        print(f"\n  NOT ACTED ON — the reasoner declined rather than guessed:")
        for why, n in SKIPPED.most_common():
            print(f"      {n:5d}  {why}")
    print(f"\n      {'PASS':18s}{tally[PASS]:5d}")
    print(f"      {'CONTINGENT':18s}{tally[CONTINGENT]:5d}   "
          f"true under one school, false under another")
    print(f"      {'FAIL':18s}{tally[FAIL]:5d}\n")

    for verdict in (FAIL, CONTINGENT):
        bad = [c for c in claims if c.verdict == verdict]
        if not bad:
            continue
        print('=' * 92)
        print(f'  {verdict} — {len(bad)}')
        print('=' * 92)
        seen = set()
        for c in bad:
            key = (c.kind, str(c.subject), str(c.asserted))
            if key in seen and verdict == FAIL:
                continue
            seen.add(key)
            print(f"\n  {c.file}:{c.line}  [{c.kind}]")
            print(f"      asserted   {c.subject} -> {c.asserted}")
            print(f"      observed   {c.observed}")
            print(f"      because    {c.why}")
            print(f"      in text    {c.text[:100]}")
    return tally


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    paths = args or ['vedic-chart-analysis.md']
    cl = run(paths)
    t = report(cl, '--fails' in sys.argv)
    print('\n' + '=' * 92)
    if t[FAIL] == 0 and t[CONTINGENT] == 0:
        print('  FIXPOINT REACHED — every extracted claim re-derives, and none '
              'is school-dependent.')
    elif t[FAIL] == 0:
        print(f'  NO FAILURES.  {t[CONTINGENT]} claims are CONTINGENT and must '
              f'be labelled in the text.')
    else:
        print(f'  {t[FAIL]} FAILURES.  Not a fixpoint — iterate.')
    print('=' * 92)
    sys.exit(1 if t[FAIL] else 0)
