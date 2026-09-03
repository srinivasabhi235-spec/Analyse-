#!/usr/bin/env python3
"""
"EVERYTHING IS A CLOSED LOOP, SO EVERY BAD TURNS INTO GOOD, RIGHT?"

THE INFERENCE DOES NOT FOLLOW, AND THE CHART SAYS SOMETHING MORE SPECIFIC.

Three things are computed here, and the first two are new to this reading:

    1  what a closed dispositor loop actually means -- authority, not valence
    2  WHICH KIND of parivartana the Mangal-Shukra exchange is.  The document
       names it sixteen times and has NEVER CLASSIFIED IT.  There are three
       classical types and they are not equally good.
    3  the one genuine bad-to-good doctrine the chart holds, and whether it
       fires -- plus the measured relationship between delivery and cost,
       which is the real answer and is not the comforting one.
"""
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, sign_of, dignity,
                        rule, sub)

POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
G7 = [g for g in GRAHAS if g not in ('Rahu', 'Ketu')]
rules = lambda g: [i + 1 for i in range(12) if LORD[(LAG + i) % 12] == g]
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
DUST, KEND, TRIK = {6, 8, 12}, {1, 4, 7, 10}, {1, 5, 9}
SP = {'Mangal': 212, 'Shani': 184, 'Budha': 152, 'Surya': 138,
      'Shukra': 95, 'Guru': 81, 'Chandra': 33}   # Rashi Pinda + Graha Pinda
ISHTA = {'Surya': 46.88, 'Chandra': 24.54, 'Mangal': 19.66, 'Budha': 18.91,
         'Guru': 37.30, 'Shukra': 47.49, 'Shani': 12.48}
KASHTA = {'Surya': 7.83, 'Chandra': 4.49, 'Mangal': 38.87, 'Budha': 30.32,
          'Guru': 15.10, 'Shukra': 11.87, 'Shani': 46.83}

# =============================================================================
rule('1.  WHAT A CLOSED LOOP ACTUALLY MEANS')
print("""
  A closed dispositor chain says that NO GRAHA IN THE CHART RESOLVES TO A FINAL
  AUTHORITY.  Every graha's field is owned by another graha, which is itself
  owned by another, and the chain never reaches a graha standing in its own
  sign.

  THAT IS A STATEMENT ABOUT DEPENDENCY.  IT IS NOT A STATEMENT ABOUT VALENCE.

  A loop of malefics is exactly as closed as a loop of benefics.  Closure
  describes the TOPOLOGY of authority -- who answers to whom -- and carries no
  information at all about whether what comes out of it is welcome.

  THERE IS NO CLASSICAL RULE THAT A CLOSED CHAIN CONVERTS ADVERSITY.  Nothing
  in the fifty-five chapters enumerated in sections 35 and 37 says anything of
  the kind, and section 6 has just measured that half of all charts have a
  single attractor anyway.  If closure transmuted difficulty, it would do so
  for half the population.
""")

# =============================================================================
rule('2.  WHICH KIND OF PARIVARTANA — NEVER CLASSIFIED UNTIL NOW')
a, b = set(rules('Mangal')), set(rules('Shukra'))
both = a | b
print(f"""
  The document names this exchange sixteen times and has never said WHICH KIND
  it is.  There are three, and the tradition does not treat them alike:

      MAHA PARIVARTANA    both lords rule only kendras and trikonas.
                          The auspicious one.  Great yoga.
      KHALA PARIVARTANA   one of the two rules the 3rd.
                          Mixed -- effort, agitation, mischief.
      DAINYA PARIVARTANA  one of the two rules the 6th, 8th or 12th.
                          DAINYA MEANS POVERTY, WRETCHEDNESS, DEPENDENCY.

  THIS CHART'S ONE EXCHANGE:

      Mangal rules the {' and the '.join(ordn(x) for x in sorted(a))}
      Shukra rules the {' and the '.join(ordn(x) for x in sorted(b))}

      dusthana lordship in the pair?   {sorted(both & DUST) or 'none'}  -- the 8TH
      3rd lordship in the pair?        {'yes' if 3 in both else 'no'}
""")
kind = 'DAINYA' if both & DUST else ('KHALA' if 3 in both else 'MAHA')
print(f"""      => IT IS A {kind} PARIVARTANA.  And it qualifies twice over: Mangal
         rules the 8th AND the 3rd, so the exchange is both Dainya and Khala.

  THIS IS THE OPPOSITE OF THE READING THE QUESTION ASSUMES.

  The chart's single sign exchange -- the attractor that every other graha
  drains into -- is the type the tradition classes as WRETCHED, not the type it
  classes as GREAT.  It is not an alchemy engine.  It is the reason the whole
  chart is administered from the 8th.

  ONE THING THAT GENUINELY SOFTENS IT, AND IT IS REAL.  Shukra's other lordship
  is the 9TH -- the strongest trikona.  So the exchange is a dusthana lord
  swapping with a graha that also owns the house of fortune.  DAINYA BY
  CLASSIFICATION, WITH A TRIKONA ATTACHED.  That is exactly the mixture this
  document has been describing from its title onward, and it is not the same
  thing as bad becoming good.
""")

# =============================================================================
rule('3.  THE ONE BAD-TO-GOOD DOCTRINE THE CHART HAS — AND IT IS DISPUTED')
vip = [(g, rules(g), hs(g)) for g in G7
       if set(rules(g)) & DUST and hs(g) in DUST]
for g, r, h in vip:
    print(f"      {g:8s} rules {r}, sits in the {ordn(h)} -- "
          f"{dignity(g, sign_of(POS[g]))}")
print(f"""
  VIPARITA RAJA YOGA is the only classical mechanism that says adversity
  produces good.  A dusthana lord in a dusthana destroys the harm it would
  otherwise do.  THE CHART HAS EXACTLY ONE: Surya, lord of the 12th, in the
  8th -- Vimala yoga.

  AND SECTION 36 PRICED THE DISPUTE ABOUT IT:

      SCHOOL A   the yoga stands, and Surya's strength helps it work
      SCHOOL B   the yoga is CANCELLED -- viparita requires an AFFLICTED
                 graha, and an exalted Surya is not afflicted

  SECTION 25 TOOK SCHOOL B.  So on this reading's own stated position, THE
  CHART'S ONLY BAD-TO-GOOD MECHANISM DOES NOT FIRE.

  Even on School A it would convert ONE house -- the 12th -- and not the chart.
""")

# =============================================================================
rule('4.  WHAT THE READING ACTUALLY MEASURED')


def spearman(x, y):
    rx = {k: i for i, k in enumerate(sorted(x, key=lambda k: -x[k]))}
    ry = {k: i for i, k in enumerate(sorted(y, key=lambda k: -y[k]))}
    n = len(x)
    return 1 - 6 * sum((rx[k] - ry[k]) ** 2 for k in x) / (n * (n * n - 1))


rho = spearman(SP, KASHTA)
print(f"""
  Section 59 tested the claim "he gets it all but with pain" by correlating
  DELIVERY (Shodhya Pinda) against COST (Kashta phala) across the seven grahas.

      Spearman rho = {rho:+.2f}

  {'  '.join('')}THE GRAHAS THAT DELIVER MOST ARE THE GRAHAS THAT COST MOST.
""")
print(f"  {'graha':9s}{'delivery':>10s}{'cost':>9s}{'Ishta':>8s}{'net':>9s}")
for g in sorted(SP, key=lambda k: -SP[k]):
    print(f"  {g:9s}{SP[g]:10d}{KASHTA[g]:9.2f}{ISHTA[g]:8.2f}"
          f"{ISHTA[g]-KASHTA[g]:+9.2f}")
print(f"""
  THAT IS NOT "BAD TURNS INTO GOOD".  IT IS SOMETHING ELSE AND IT IS STRICTER:

      THE GOOD AND THE COST ARE THE SAME OBJECT.

  Nothing converts.  Mangal, Shani and Budha carry the highest delivery in the
  chart and the highest cost in the chart, and they rule the 8th, the 6th and
  the 10th.  The transformation, the adversity and the career are the same
  three grahas doing both jobs at once -- not a bad thing turning into a good
  one, but one thing that is both from the start.

  AND ONE EXEMPTION, WHICH THE DOCUMENT HAS ALWAYS NAMED:

      SURYA -- Ishta {ISHTA['Surya']:.2f}, Kashta {KASHTA['Surya']:.2f}, net {ISHTA['Surya']-KASHTA['Surya']:+.2f}.
      The one graha that gives most and charges least.  AND IT RULES THE 12TH.

  He gets everything he grips, painfully.  THE ONE THING HE GETS FREELY IS
  WHAT HE STOPS GRIPPING.
""")

# =============================================================================
rule('5.  THE ANSWER')
print("""
  NO -- AND THE THING THAT IS TRUE INSTEAD IS BETTER THAN THE THING ASSUMED.

  1  A CLOSED LOOP IS ABOUT AUTHORITY, NOT ABOUT GOOD AND BAD.  It says nothing
     resolves to a final owner.  Half of all charts are like that.

  2  THE LOOP ITSELF IS CLASSIFIED WRETCHED, NOT GREAT.  The Mangal-Shukra
     exchange is a DAINYA parivartana -- it involves the 8th lord -- and also
     Khala, because Mangal rules the 3rd.  It is not the auspicious Maha type.
     Nobody in this document had classified it before now.

  3  THE ONE ALCHEMY MECHANISM THE CHART OWNS IS DISPUTED AND THIS READING
     RULED IT OUT.  Vimala yoga, and section 25 takes the cancelling side.

  4  WHAT IS MEASURED INSTEAD IS rho = +0.82 BETWEEN DELIVERY AND COST.  The
     good and the cost are not sequential.  THEY ARE THE SAME OBJECT.

  THE DOCUMENT HAS SAID THIS FROM ITS TITLE ONWARD: the difficulty and the
  fortune are the same object.  That is not a consolation and it is not a
  sentence of doom.  IT MEANS THE PRICE IS NOT A PENALTY ATTACHED TO THE
  REWARD.  IT IS PART OF WHAT THE REWARD IS.
""")
print('=' * 92)
