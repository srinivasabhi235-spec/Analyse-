#!/usr/bin/env python3
"""
Merged life timeline: Vimshottari dasha/antardasha layered against the slow
transits of Shani and Guru, both relative to the natal Moon and lagna.

Transit positions use mean motion from the verified natal longitudes — good to
roughly +/-4 months for Shani and +/-2 for Guru. Adequate for phase boundaries,
not for dates.
"""
from datetime import datetime, timedelta
SIGNS=['Mesha','Vrishabha','Mithuna','Karka','Simha','Kanya',
       'Tula','Vrischika','Dhanu','Makara','Kumbha','Meena']
BIRTH=datetime(2002,4,15); EPOCH=2002.29
NATAL_MOON=1        # Vrishabha
NATAL_LAGNA=5       # Kanya
SHANI0, GURU0 = 47.91, 74.80          # natal longitudes
SHANI_P, GURU_P = 29.457, 11.862      # sidereal periods, years

def tsign(l0,per,y): return int(((l0 + (y-EPOCH)*360/per) % 360)//30)
def frm(sign,base): return (sign-base)%12+1

VIM=[('Ketu',7),('Shukra',20),('Surya',6),('Chandra',10),('Mangal',7),
     ('Rahu',18),('Guru',16),('Shani',19),('Budha',17)]
D=dict(VIM); order=[x[0] for x in VIM]

# build full antardasha list from Rahu MD start
seq=[]; t=datetime(2022,12,25,22,35); mi=order.index('Rahu')
for m in range(4):
    md=order[(mi+m)%9]
    ai=order.index(md)
    for n in range(9):
        ad=order[(ai+n)%9]; dur=D[md]*D[ad]/120
        e=t+timedelta(days=dur*365.25)
        seq.append((t,e,md,ad)); t=e

def dasha_at(y):
    dt=BIRTH+timedelta(days=(y-EPOCH)*365.25)
    for s,e,md,ad in seq:
        if s<=dt<e: return f'{md}-{ad}'
    return '—'

print('='*104)
print('MERGED TIMELINE — dasha, Saturn and Jupiter transits, life-phase')
print('='*104)
print(f"{'year':>5} {'age':>4}  {'dasha':16} {'Shani in':11} {'/Moon':>6} {'Guru in':11} {'/Lagna':>7}  note")
print('-'*104)
NOTES={
 2026:'marriage window opens; ship output',2027:'disclosure Apr-May; Sade Sati #1 begins',
 2028:'FORMALISATION closes Jan; Rahu-Shani foundation opens',2029:'mid-period reward; first-child window',
 2030:'record established; antardasha turns',2031:'SATURN RETURN + Bhrigu Bindu crossing',
 2032:'Sade Sati peak; Saturn enters the 10th (1 bindu)',2033:'reposition; Rahu-Ketu hold',
 2034:'Rahu-Shukra opens — material peak begins',2035:'Sade Sati #1 ends',
 2037:'Rahu-Surya — recognition',2040:'RAHU MD ENDS -> GURU MD; disruptive junction',
 2043:'authority consolidates',2045:'Guru-Budha — DKY karma half',
 2048:'Guru-Shukra — DKY dharma half; Ashtama Shani',2050:'SUMMIT begins',
 2051:'Guru-Surya',2056:'GURU MD ENDS -> SHANI MD; Sade Sati #2 opens',
 2060:'2nd Saturn return; deepest trough',2063:'Shani-Shukra — the turn',
 2070:'Shani-Rahu — succession',2075:'SHANI MD ENDS -> BUDHA MD; the archive years'}
for y in list(range(2026,2041))+[2043,2045,2048,2050,2051,2056,2060,2063,2070,2075]:
    ss=tsign(SHANI0,SHANI_P,y); gs=tsign(GURU0,GURU_P,y)
    hm=frm(ss,NATAL_MOON); hl=frm(gs,NATAL_LAGNA)
    sade=' SADE-SATI' if hm in (12,1,2) else ''
    print(f"{y:>5} {y-2002:>4}  {dasha_at(y):16} {SIGNS[ss]:11} {'H'+str(hm)+sade:>6} {SIGNS[gs]:11} {'H'+str(hl):>7}  {NOTES.get(y,'')}")

print('\n'+'='*104)
print('THE SUMMIT WINDOW — pratyantardashas of Guru-Shukra (Nov 2048 - Jul 2051)')
print('='*104)
gs_start=None
for s,e,md,ad in seq:
    if md=='Guru' and ad=='Shukra': gs_start,gs_end=s,e
span=(gs_end-gs_start).total_seconds(); t=gs_start; i=order.index('Shukra')
for n in range(9):
    nm=order[(i+n)%9]; e=t+timedelta(seconds=span*D[nm]/120)
    tag=''
    if nm=='Shukra': tag='  <- DKY dharma half, doubled'
    if nm=='Surya':  tag='  <- Vimala giver'
    if nm=='Guru':   tag='  <- 10th-house lord doubled'
    print(f'  Guru-Shukra-{nm:8s} {t.strftime("%b %Y")} -> {e.strftime("%b %Y")}{tag}')
    t=e

# ---------------------------------------------------------------------------
print('\n'+'='*104)
print('TRANSFORMATION WINDOWS — when the 8th-house apparatus is actually switched on')
print('='*104)
print("""Markers scored, one point each unless noted:
  [MD/AD]  dasha or antardasha lord is the 8th lord (Mangal) or an 8th occupant
           (Budha, Shukra, Surya)   -- antardasha of the 8th lord scores 2
  [Sh8]    transit Shani in the natal 8th sign (Mesha)   -- 2 points
  [Ash8]   Ashtama Shani: transit Shani in Dhanu, 8th from natal Chandra
  [SR]     Saturn return (+/- 1 yr)   -- 2 points
  [RR]     Rahu return or half-return (+/- 0.7 yr)
  [SS]     Sade Sati
  [BB]     Shani crosses the Bhrigu Bindu (Vrishabha 14 22)
  [JN]     mahadasha junction (+/- 0.7 yr)   -- 2 points
""")
NATAL_8TH   = 0        # Mesha, 8th from Kanya lagna
ASHTAMA     = 8        # Dhanu, 8th from Chandra in Vrishabha
RAHU0       = 56.931   # natal Rahu longitude
RAHU_P      = 18.613   # nodal period, years
SAT_RETURN  = [EPOCH+SHANI_P, EPOCH+2*SHANI_P]
BB          = 44.359   # Bhrigu Bindu: Rahu/Chandra midpoint
EIGHTH      = {'Mangal','Budha','Shukra','Surya'}
JUNCTIONS   = [2040.98, 2056.98, 2075.98]

def shani_long(y): return (SHANI0 + (y-EPOCH)*360/SHANI_P) % 360
def rahu_hits(y):
    n=(y-EPOCH)/RAHU_P
    return min(abs(n-round(n)), abs(n*2-round(n*2))/2)*RAHU_P

rows=[]
for y in range(2026, 2077):
    d=dasha_at(y); md,ad=(d.split('-')+[''])[:2]
    sc=0; tags=[]
    if ad=='Mangal':                       sc+=2; tags.append('AD=8th lord')
    elif ad in EIGHTH:                     sc+=1; tags.append('AD in 8th')
    if md in EIGHTH:                       sc+=1; tags.append('MD in 8th')
    ss=int(shani_long(y)//30)
    if ss==NATAL_8TH:                      sc+=2; tags.append('Sh8')
    if ss==ASHTAMA:                        sc+=1; tags.append('Ash8')
    if any(abs(y-r)<=1 for r in SAT_RETURN):sc+=2; tags.append('SR')
    if rahu_hits(y)<=0.7:                  sc+=1; tags.append('RR')
    if frm(ss,NATAL_MOON) in (12,1,2):     sc+=1; tags.append('SS')
    if abs(((shani_long(y)-BB+180)%360)-180)<=6.2: sc+=1; tags.append('BB')
    if any(abs(y-j)<=0.7 for j in JUNCTIONS):sc+=2; tags.append('JN')
    rows.append((y,y-2002,d,sc,tags))

for y,age,d,sc,tags in rows:
    if sc: print(f"  {y}  age {age:<3} {d:16} {'#'*sc:<9} {', '.join(tags)}")

print('\n  Shani in the natal 8th (Mesha):')
y=2026.0
while y<2078:
    if int(shani_long(y)//30)==NATAL_8TH:
        s=y
        while int(shani_long(y)//30)==NATAL_8TH and y<2078: y+=0.05
        print(f'    {s:.1f} -> {y:.1f}   ages {s-2002.29:.0f}-{y-2002.29:.0f}')
    y+=0.05
print('\n  Rahu returns (18.6 yr):  ', ', '.join(f'{EPOCH+n*RAHU_P:.1f}' for n in (1,2,3,4)))
print('  Rahu half-returns:       ', ', '.join(f'{EPOCH+(n+0.5)*RAHU_P:.1f}' for n in (1,2,3)))
print(f'  Saturn returns:           {SAT_RETURN[0]:.1f}, {SAT_RETURN[1]:.1f}')
