SIGNS=['Mesha','Vrishabha','Mithuna','Karka','Simha','Kanya','Tula','Vrischika','Dhanu','Makara','Kumbha','Meena']
LORD={'Mesha':'Mangal','Vrishabha':'Shukra','Mithuna':'Budha','Karka':'Chandra','Simha':'Surya','Kanya':'Budha',
'Tula':'Shukra','Vrischika':'Mangal','Dhanu':'Guru','Makara':'Shani','Kumbha':'Shani','Meena':'Guru'}
NAK=['Ashwini','Bharani','Krittika','Rohini','Mrigashira','Ardra','Punarvasu','Pushya','Ashlesha','Magha',
'P Phalguni','U Phalguni','Hasta','Chitra','Swati','Vishakha','Anuradha','Jyeshtha','Mula','P Ashadha',
'U Ashadha','Shravana','Dhanishtha','Shatabhisha','P Bhadrapada','U Bhadrapada','Revati']
NL=['Ketu','Shukra','Surya','Chandra','Mangal','Rahu','Guru','Shani','Budha']*3
def d(s,a,b,c): return SIGNS.index(s)*30+a+b/60+c/3600
D1={'Lagna':d('Kanya',27,37,37),'Surya':d('Mesha',1,28,3),'Chandra':d('Vrishabha',1,47,15),
'Mangal':d('Vrishabha',7,19,32),'Budha':d('Mesha',10,27,50),'Guru':d('Mithuna',14,47,52),
'Shukra':d('Mesha',23,36,49),'Shani':d('Vrishabha',17,54,25),'Rahu':d('Vrishabha',26,55,52),
'Ketu':d('Vrischika',26,55,52)}
G7=['Surya','Chandra','Mangal','Budha','Guru','Shukra','Shani']
LAG=5
def hs(l): return (int(l//30)-LAG)%12+1
def sn(l): return SIGNS[int(l//30)]

print('================ 1. SANKHYA / AKRITI (NABHASA) YOGA ================')
occ=sorted(set(int(D1[g]//30) for g in G7))
houses=sorted(set(hs(D1[g]) for g in G7))
print(f'  7 grahas occupy {len(occ)} signs {[SIGNS[i] for i in occ]} -> Sankhya: SHOOLA yoga (3 signs)')
print(f'  Houses occupied: {houses} -> all within the 7th-10th band -> Akriti: SHAKTI yoga reading')

print()
print('================ 2. LUNAR / SOLAR YOGAS ================')
moon_s=int(D1['Chandra']//30)
s2=[g for g in G7 if g not in('Surya','Chandra') and int(D1[g]//30)==(moon_s+1)%12]
s12=[g for g in G7 if g not in('Surya','Chandra') and int(D1[g]//30)==(moon_s-1)%12]
print(f'  2nd from Moon (Mithuna): {s2}  |  12th from Moon (Mesha): {s12}')
print(f'  -> Sunapha + Anapha = DURUDHARA yoga.  KEMADRUMA: absent.')
sun_s=int(D1['Surya']//30)
v2=[g for g in G7 if g not in('Surya','Chandra') and int(D1[g]//30)==(sun_s+1)%12]
v12=[g for g in G7 if g not in('Surya','Chandra') and int(D1[g]//30)==(sun_s-1)%12]
print(f'  2nd from Sun: {v2} -> VESI yoga (malefic: Mangal+Shani). 12th from Sun: {v12} -> no Vasi.')
print(f'  Budha-Aditya: Surya+Budha same sign, sep {abs(D1["Budha"]-D1["Surya"]):.2f} deg -> forms, combust-compromised')
print(f'  Punarphoo / Vish: Chandra+Shani same sign (Vrishabha), sep {abs(D1["Shani"]-D1["Chandra"]):.2f} deg -> forms (wide)')
# Shakata
g_s=int(D1['Guru']//30); rel=(moon_s-g_s)%12+1
print(f'  Moon is {rel}th from Guru -> SHAKATA forms; Guru in kendra from lagna (10th) -> CANCELLED')
# Adhi from lagna
for h in (6,7,8):
    inh=[g for g in G7 if hs(D1[g])==h]
    print(f'  Lagnadhi check H{h}: {inh}')
print('  -> benefics Budha+Shukra in 8th but Surya with them -> Lagnadhi SPOILED')
# Kalasarpa
r=D1['Rahu']%360; k=D1['Ketu']%360
outside=[g for g in G7 if not ((k<(D1[g]%360)<r+360 and False) or True)]
def in_arc(x,a,b):
    x%=360; a%=360; b%=360
    return (a<x<b) if a<b else (x>a or x<b)
out=[g for g in G7 if not in_arc(D1[g],k,r)]
print(f'  Kalasarpa: grahas outside Ketu->Rahu arc: {out} -> ABSENT (Guru alone breaks it, from the kendra)')

print()
print('================ 3. FUNCTIONAL NATURE FOR KANYA LAGNA ================')
print('  Shukra 9+2 -> prime functional benefic | Budha 1+10 -> benefic')
print('  Guru 4+7 -> KENDRADHIPATI DOSHA (benefic ruling two kendras) + BADHAKESH (7th lord, dual lagna)')
print('  Mangal 3+8 -> functional malefic | Chandra 11 -> functional malefic | Shani 5+6 mixed | Surya 12 neutral')

print()
print('================ 4. BALADI + JAGRADADI AVASTHAS ================')
DIG={'Surya':'Jagrat (exalted)','Chandra':'Jagrat (exalted)','Mangal':'Svapna (neutral)','Budha':'Svapna (neutral)',
'Guru':'Sushupti (ENEMY sign)','Shukra':'Svapna (neutral)','Shani':'Svapna (friend)'}
for g in G7:
    l=D1[g]; s=int(l//30); pos=l%30; odd=(s%2==0)
    seq=['Bala','Kumara','Yuva','Vriddha','Mrita']
    if not odd: seq=seq[::-1]
    av=seq[int(pos//6)]
    print(f'  {g:8s} {pos:5.2f} deg {SIGNS[s]:10s} ({"odd" if odd else "even"}) -> {av:7s} | {DIG[g]}')
print('  NOTE: the two future MD lords Guru and Shani are the ONLY grahas in Yuva (full-fruit) avastha')

print()
print('================ 5. JAIMINI: CHARA KARAKAS (7-scheme) ================')
degs=sorted(((D1[g]%30,g) for g in G7), reverse=True)
names=['Atmakaraka','Amatyakaraka','Bhratrikaraka','Matrikaraka','Pitrikaraka','Putrakaraka','Darakaraka']
K={}
for (dg,g),nm in zip(degs,names):
    K[nm]=g; print(f'  {nm:14s} {g:8s} {dg:5.2f} deg')
print(f'  Karakamsa (AK Shukra navamsa sign): Vrischika -> occult/investigative soul-field')

print()
print('================ 6. ARUDHAS + SENSITIVE POINTS ================')
def arudha(house_sign_idx):
    lord=LORD[SIGNS[house_sign_idx]]; lidx=int(D1[lord]//30)
    cnt=(lidx-house_sign_idx)%12
    al=(lidx+cnt)%12
    if al==house_sign_idx or al==(house_sign_idx+6)%12: al=(al+9)%12
    return al
al=arudha(5)   # lagna Kanya idx5
ul=arudha(4)   # 12th house = Simha idx4
print(f'  Arudha Lagna: {SIGNS[al]} (house {(al-5)%12+1}) — Ketu sits there')
print(f'  Upapada:      {SIGNS[ul]} (house {(ul-5)%12+1}) — lord Guru in 10th; 2nd from UL ruled by Shani')
bb=((D1['Chandra']+D1['Rahu'])/2)%360
print(f'  Bhrigu Bindu: {bb%30:.2f} {sn(bb)} (9th) — {abs(bb-45.20):.2f} deg from Parivesha, {abs(bb-D1["Shani"]):.2f} from Shani')
lagd=int((D1['Lagna']%30)//10)+1
kh_sign=SIGNS[(5+7)%12]
print(f'  Lagna drekkana #{lagd} -> 22nd (Khara) drekkana = 3rd drekkana of {kh_sign} (20-30 deg)')
print(f'  Shukra at {D1["Shukra"]%30:.2f} Mesha -> INSIDE Khara drekkana; Mrityu upagraha 3.2 deg away')
yp=(D1['Surya']+D1['Chandra']+93+20/60)%360
yn=int(yp//(40/3)); avp=(yp+186+40/60)%360; an=int(avp//(40/3))
print(f'  Yogi point {yp%30:.2f} {sn(yp)} -> {NAK[yn]} -> YOGI = {NL[yn]}  (duplicate: {LORD[sn(yp)]})')
print(f'  Avayogi point -> {NAK[an]} -> AVAYOGI = {NL[an]}')
print('  -> Yogi KETU (nakshatra-chain terminus), Sahayogi Surya, Avayogi RAHU (current MD lord)')

print()
print('================ 7. MARANA KARAKA STHANA ================')
MKS={'Surya':12,'Chandra':8,'Mangal':7,'Budha':7,'Guru':3,'Shukra':6,'Shani':1,'Rahu':9}
for g,h in MKS.items():
    if g in D1 and hs(D1[g])==h: print(f'  {g} in H{h} -> IN MKS')
print('  -> only RAHU (mahadasha lord) sits in its MKS, the 9th')

print()
print('================ 8. DERIVED VARGAS D3 / D7 / D12 ================')
def d3(l):
    s=int(l//30); return (s+4*int((l%30)//10))%12
def d7(l):
    s=int(l//30); p=int((l%30)//(30/7))
    start=s if s%2==0 else (s+6)%12
    return (start+p)%12
def d12(l):
    s=int(l//30); return (s+int((l%30)//2.5))%12
for nm,fn in [('D3',d3),('D7',d7),('D12',d12)]:
    row=' '.join(f'{g[:2]}:{SIGNS[fn(D1[g])][:4]}' for g in ['Lagna']+G7)
    print(f'  {nm:4s} {row}')
print('  D3: lagna Vrishabha; KETU in its 3rd (Karka) — Ketu in the 3rd of BOTH D1 and D3')
print('  D7: lagna KANYA (4th varga with Kanya lagna); Guru in D7 lagna; Chandra+Shukra debilitated')
print('  D12: Surya exalted AND Chandra exalted — both parents dignified; father powerful')

print()
print('================ 9. KP STAR-LORD ROUTING ================')
for g in G7+['Rahu','Ketu']:
    i=int(D1[g]//(40/3)); sl=NL[i]
    tgt=f'H{hs(D1[sl])}' if sl in D1 else '-'
    rules={'Surya':'12','Chandra':'11','Mangal':'3,8','Budha':'1,10','Guru':'4,7','Shukra':'2,9','Shani':'5,6'}.get(sl,'-')
    print(f'  {g:8s} in {NAK[i]:12s} (star of {sl:7s}) -> delivers via {tgt} + houses {rules}')
print('  -> tally: house 8 five times, house 9 four times, house 3 three times.')
print('  -> the ONLY 1/10 delivery routes through KETU (in Budha star) — self+career via detachment/research')

print()
print('================ 10. PANCHANGA COMPLETION ================')
el=(D1['Chandra']-D1['Surya'])%360
tithi=int(el//12)+1
nit=int(((D1['Surya']+D1['Chandra'])%360)//(40/3))
YOGAS=['Vishkambha','Priti','Ayushman','Saubhagya','Shobhana','Atiganda','Sukarman']
kar=['Kimstughna','Bava','Balava','Kaulava','Taitila','Gara','Vanija','Vishti'][int(el//6)]
print(f'  Vara Monday (Chandra) | Nakshatra Krittika (Surya) | Tithi Shukla {tithi} = Tritiya, JAYA class')
print(f'  Nitya yoga #{nit+1} = {YOGAS[nit]} | Karana = {kar}')

print()
print('================ 11. ELEMENT TALLY ================')
EL=['Fire','Earth','Air','Water']
tal={}
for g in G7: tal[EL[int(D1[g]//30)%4]]=tal.get(EL[int(D1[g]//30)%4],0)+1
print(f'  {tal}  + lagna Earth  -> earth-fire dominant; air and water thin')

print()
print('================ 12. ASHTAMA SHANI (approx, +/-6 months) ================')
print('  Saturn in Dhanu (8th from natal Moon) ~ Dec 2047 - early 2050')
print('  -> overlaps Guru-Ketu and the first ~1.5y of Guru-Shukra; cleanest DKY run 2050-51')
