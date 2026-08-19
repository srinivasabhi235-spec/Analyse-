#!/usr/bin/env python3
"""
What role, specifically -- and why it is a different KIND of role.

Section 19 closed on a sentence: "the past cost him things he had not chosen
and returned a self; the future costs him things he will have chosen and
returns a role."  That leaves the obvious question unanswered.  WHICH ROLE?

The word is doing real work there and it should be made to earn it.  Three
things have to be established:

    1. what roles did the PAST give him?  (if it gave roles too, the
       distinction collapses)
    2. what roles does the chart name for the coming window, and when
    3. what KIND of authority the chart says those roles carry --
       because this chart is unusually specific about that, and the answer
       is not the obvious one

Nothing here is a new prediction.  Every date is already in the document; this
names what occupies them.
"""
from ephem_core import (SIGNS, GRAHAS, SUPPLIED, LORD, VIM, EXALT, varga,
                        sign_of, nak_of, short, rule, sub)

POS = dict(SUPPLIED)
LAG = sign_of(POS['Lagna'])
BIRTH_Y = 2002 + (31 + 28 + 31 + 15) / 365.25
hs = lambda g: (sign_of(POS[g]) - LAG) % 12 + 1
rules = lambda g: [i for i in range(1, 13) if LORD[(LAG + i - 1) % 12] == g]
house_sign = lambda n: (LAG + n - 1) % 12
occupants = lambda n: [g for g in GRAHAS if hs(g) == n]
SAV = {'Mesha': 21, 'Vrishabha': 22, 'Mithuna': 29, 'Karka': 28, 'Simha': 24,
       'Kanya': 29, 'Tula': 24, 'Vrischika': 28, 'Dhanu': 29, 'Makara': 29,
       'Kumbha': 41, 'Meena': 33}
BRANK = [5, 3, 8, 2, 6, 10, 4, 12, 7, 9, 11, 1]

# =============================================================================
rule('1.  WHAT ROLES DID THE PAST GIVE HIM?')
print("""
  If the Mangal years handed him roles too, the whole distinction collapses.
  So this has to be checked first.

  Ages 13.7 to 20.7.  The roles available at that age are:

      SON        — the 4th house (mother) and the 9th (father)
      STUDENT    — the 4th house and the 5th
      BROTHER    — the 3rd house

  Every one of those is a role you are PUT IN.  None is taken.  And look at
  what the chart does to each of them in exactly those years:
""")
for n, lbl in [(9, 'father / son'), (4, 'mother, home, schooling'),
               (3, 'siblings'), (5, 'education, mind')]:
    s = house_sign(n)
    print(f"      house {n:2d}  {lbl:26s} {SIGNS[s]:11s} "
          f"SAV {SAV[SIGNS[s]]:2d}  rank {BRANK[n-1]:2d}  {occupants(n) or 'empty'}")
print("""
  CORRECTION TO THE DRAFT.  I had written that the chart puts ALL FOUR of these
  under load.  It does not, and the numbers above say so plainly:

      LOADED      the 9th  — SAV 22, rank 7, four grahas incl. Rahu in MKS
                  the 3rd  — rank 8, Ketu in the severest gandanta pada
      SOUND       the 4th  — rank 2 of 12, SAV 29, EMPTY
                  the 5th  — rank 6, SAV 29, EMPTY

  Only two of the four carry direct weight.  The other two are structurally
  well built and receive nothing but Mangal's aspect.  So the pressure of those
  years fell on the FATHER and on SIBLINGS-AND-EFFORT, not on home and
  schooling as such -- which is also why the domestic base came through it.

  But the conclusion does not rest on all four being weak.  It rests on all
  four being ASSIGNED:

  THE PAST GAVE HIM NO ROLE.  It gave him positions he was born into.  What he
  came out with was a CAPABILITY -- the ability to work alone under pressure --
  which is a property of a person, not a position.
""")

# =============================================================================
rule('2.  WHAT THE COMING WINDOW ACTUALLY NAMES')
print("""
  Three roles, and the chart dates each one.  All three dates are already in
  this document; what follows only names what occupies them.
""")

ROLES = [
    ('HUSBAND', 'Rahu–Guru, to 31 January 2028', 7,
     """Guru rules the 7th and the 4th and runs the antardasha.  Transit Shani
      sits in the natal 7th until 3 June 2027 and transit Guru aspects it.
      Three independent activators of the 7th at once -- the clearest such
      window in the visible timeline."""),
    ('THE ONE RESPONSIBLE', 'Rahu–Shani, 31 Jan 2028 – 7 Dec 2030', 10,
     """Shani carries FOUR career credentials simultaneously: D10 lagna lord,
      Amatyakaraka, lord of the 41-bindu 6th, and occupant of D9's 10th.
      Nothing else in the chart carries more than two.  This is the sub-period
      the reading has always called the foundation."""),
    ('FATHER', 'inside Shani–Shukra, Feb–Jul 2029', 5,
     """The 5th is loaded far more heavily in this window than in the past one.
      Shani rules the 5th and runs the antardasha; Shukra is the Atmakaraka;
      transit Guru crosses the natal lagna across 2028."""),
]
for name, when, h, why in ROLES:
    s = house_sign(h)
    print(f"\n  {name}   —   {when}")
    print(f"      house {h}: {SIGNS[s]}, lord {LORD[s]}, SAV {SAV[SIGNS[s]]}, "
          f"Bhava rank {BRANK[h-1]} of 12")
    print(f"     {why}")

print("""
  ALL THREE ARE ROLES HE ENTERS RATHER THAN INHERITS.  That is the difference
  the word was carrying, and it holds: son, student and brother were assigned;
  husband, office-holder and father are taken on.
""")

# =============================================================================
rule('3.  WHAT KIND OF AUTHORITY — and it is not the obvious kind')
print("""
  Here the chart is unusually specific, and it says something most readings
  would soften.  Four measurements, all pointing the same way.
""")
print(f"""  1. THE 10TH LORD RANKS FOURTH AS A CAREER AGENT IN HIS OWN CHART.
     Budha rules the 10th and scores 3.77.  Shani, which rules nothing in the
     career houses, scores 7.96.  THE GRAHA WITH THE TITLE DOES NOT HAVE THE
     POWER.

  2. NO PANCHAMAHAPURUSHA YOGA.  With one kendra occupied, and that by a graha
     in an enemy sign, none of the five great-person yogas can form.  NOTHING
     IN THIS CHART CONFERS STATURE AUTOMATICALLY.

  3. BOTH JAIMINI AUTHORITY INDICATORS LAND ON THE EMPTY 12TH -- AND THE 12TH
     IS THE STRONGEST BHAVA IN THE CHART.  A second draft correction: I had
     read rank {BRANK[11]} as weakness.  It is the opposite -- rank 1 of 12,
     12.59 rupas, the best-built house he owns, and EMPTY.
     Meanwhile the 10th itself ranks {BRANK[9]} of 12.
     So the seat of authority is REAL and it is LOCATED OUT OF SIGHT:
     foreign, secluded, behind the scenes.  Not absent.  Unwitnessed.

  4. BUT THE 6TH CARRIES {SAV['Kumbha']} BINDUS, the highest of any sign, and the
     D10 ascendant is the same sign.  The house of SERVICE, competition and
     applied problem-solving is the strongest thing he owns by that measure.

  PUT TOGETHER:

      the role is RESPONSIBILITY WITHOUT TITLE.

  He becomes the person things are handed to.  Not the person whose name is on
  the door -- the chart is emphatic that this is not available and never
  becomes available on its own.  The one who is called when it is broken,
  contested or opaque, and who is trusted to resolve it.

  That is the authority of the EXPERT and the TRUSTED HAND, and it is exactly
  what a Kumbha D10 ascendant under Shani, a 41-bindu 6th, and Amala Yoga
  describe between them.
""")

# =============================================================================
rule('4.  THE THREE ROLES ARE THE SAME ROLE')
print("""
  This is the finding, and it took naming all three to see it.

      HUSBAND               someone depends on him and he is not free to leave
      THE ONE RESPONSIBLE   something depends on him and he is not free to
                            hand it back
      FATHER                someone depends on him absolutely, and there is no
                            version where he is not responsible

  ALL THREE ARE THE SAME STRUCTURE: being the one who does not get to put it
  down.  And the chart arranges them in ascending order of irrevocability,
  across thirty months.

  Set that against what section 37 established -- that this is a chart whose
  central mechanism is SETTING THINGS DOWN, and whose only occupant of the
  three houses of desire is the graha that removes attachment.

  THAT IS THE REAL DIFFICULTY OF THE COMING WINDOW, and it is not the
  hardship.  It is that a man built to release is being handed, in the space
  of thirty months, three things he structurally cannot release.
""")

# =============================================================================
rule('5.  AND WHAT MAKES IT SURVIVABLE')
print("""
  The reading has three answers to that and they are worth collecting, because
  they were each found for other reasons.

  1. THE 4TH IS RANK 2 AND THE UPAPADA SITS IN IT.  The marriage attaches to
     the second-strongest house in the chart.  Whatever else is strained, the
     domestic base is well built.

  2. THE MARRIAGE IS DURABLE PRECISELY BECAUSE ITS DISSOLUTION-HOUSE IS WEAK.
     Section 44 found the 8th from the Upapada is his 11th -- rank 11 of 12
     with both harsh shadow points.  The house that would END the marriage is
     too feeble to act.  The same configuration that thins his friendships is
     what makes the marriage hard to break.

  3. SHANI AND GURU ARE THE ONLY GRAHAS IN ADULT AVASTHA, and they govern
     everything from 38.7 onward.  The parts of him equipped for sustained
     obligation are precisely the parts that have already grown up.

  So the chart hands a releaser three unreleasable things, and then supplies
  the two grahas of endurance to carry them.  THAT IS THE ARRANGEMENT.  Not
  comfortable, and not incoherent.

  ONE HONEST QUALIFICATION.  None of this predicts that a marriage or a child
  occurs.  It says the chart activates those houses on those dates and that
  the roles it names are of a particular kind.  Whether a life fills them is
  not something Jyotisha can settle.
""")
print('=' * 92)
