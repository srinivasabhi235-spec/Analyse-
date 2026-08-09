#!/usr/bin/env python3
"""
The complete Shodashavarga (16 divisional charts) computed from the verified D1
longitudes, plus Vimshopaka Bala and the Vaiseshikamsha dignity census.

Calibration: the D9 and D27 produced here reproduce the supplied source tables
exactly (see verify_chart.py), which validates the varga machinery.
"""
SIGNS = ['Mesha','Vrishabha','Mithuna','Karka','Simha','Kanya',
         'Tula','Vrischika','Dhanu','Makara','Kumbha','Meena']
S = SIGNS.index
G = ['Surya','Chandra','Mangal','Budha','Guru','Shukra','Shani']

def d(sg,a,b,c): return S(sg)*30 + a + b/60 + c/3600
D1 = {'Lagna':d('Kanya',27,37,37), 'Surya':d('Mesha',1,28,3),
      'Chandra':d('Vrishabha',1,47,15), 'Mangal':d('Vrishabha',7,19,32),
      'Budha':d('Mesha',10,27,50), 'Guru':d('Mithuna',14,47,52),
      'Shukra':d('Mesha',23,36,49), 'Shani':d('Vrishabha',17,54,25),
      'Rahu':d('Vrishabha',26,55,52), 'Ketu':d('Vrischika',26,55,52)}

MOV={0,3,6,9}; FIX={1,4,7,10}          # movable / fixed sign indices
def sgn(l): return int(l//30)
def pos(l): return l%30

def v(l, n):
    """Divisional sign index for division n, standard Parashari rules."""
    s, p = sgn(l), pos(l)
    if n == 1:  return s
    if n == 2:  return 4 if (p<15) == (s%2==0) else 3          # Simha/Karka hora
    if n == 3:  return (s + 4*int(p//10)) % 12
    if n == 4:  return (s + 3*int(p//7.5)) % 12
    if n == 7:  return ((s if s%2==0 else (s+6)%12) + int(p/(30/7))) % 12
    if n == 9:  return int(l*9/30) % 12
    if n == 10: return ((s if s%2==0 else (s+8)%12) + int(p/3)) % 12
    if n == 12: return (s + int(p/2.5)) % 12
    if n == 16: return ((0 if s in MOV else 4 if s in FIX else 8) + int(p/1.875)) % 12
    if n == 20: return ((0 if s in MOV else 8 if s in FIX else 4) + int(p/1.5)) % 12
    if n == 24: return ((4 if s%2==0 else 3) + int(p/1.25)) % 12
    if n == 27: return int(l*27/30) % 12
    if n == 30:                                                # special scheme
        if s%2==0: lim=[(5,0),(10,10),(18,8),(25,2),(30,6)]    # Ma Sa Ju Me Ve
        else:      lim=[(5,1),(12,5),(20,11),(25,9),(30,7)]    # Ve Me Ju Sa Ma
        for hi,sg_ in lim:
            if p < hi: return sg_
        return lim[-1][1]
    if n == 40: return ((0 if s%2==0 else 6) + int(p/0.75)) % 12
    if n == 45: return ((0 if s in MOV else 4 if s in FIX else 8) + int(p/(2/3))) % 12
    if n == 60: return (s + int(p*2)) % 12
    raise ValueError(n)

OWN={'Surya':[4],'Chandra':[3],'Mangal':[0,7],'Budha':[2,5],
     'Guru':[8,11],'Shukra':[1,6],'Shani':[9,10]}
EXAL={'Surya':0,'Chandra':1,'Mangal':9,'Budha':5,'Guru':3,'Shukra':11,'Shani':6}
DEB={g:(x+6)%12 for g,x in EXAL.items()}
FRIEND={'Surya':['Chandra','Mangal','Guru'],'Chandra':['Surya','Budha'],
        'Mangal':['Surya','Chandra','Guru'],'Budha':['Surya','Shukra'],
        'Guru':['Surya','Chandra','Mangal'],'Shukra':['Budha','Shani'],
        'Shani':['Budha','Shukra']}
ENEMY={'Surya':['Shukra','Shani'],'Chandra':[],'Mangal':['Budha'],
       'Budha':['Chandra'],'Guru':['Budha','Shukra'],
       'Shukra':['Surya','Chandra'],'Shani':['Surya','Chandra','Mangal']}
LORD={0:'Mangal',1:'Shukra',2:'Budha',3:'Chandra',4:'Surya',5:'Budha',
      6:'Shukra',7:'Mangal',8:'Guru',9:'Shani',10:'Shani',11:'Guru'}

def dignity(g, si):
    if si == EXAL[g]: return 'exalted', 20
    if si == DEB[g]:  return 'debilitated', 3
    if si in OWN[g]:  return 'own', 20
    l = LORD[si]
    if l == g:          return 'own', 20
    if l in FRIEND[g]:  return 'friend', 15
    if l in ENEMY[g]:   return 'enemy', 7
    return 'neutral', 10

VARGAS=[(1,'D1',3.5),(2,'D2',1),(3,'D3',1),(4,'D4',0.5),(7,'D7',0.5),(9,'D9',3),
        (10,'D10',0.5),(12,'D12',0.5),(16,'D16',2),(20,'D20',0.5),(24,'D24',0.5),
        (27,'D27',0.5),(30,'D30',1),(40,'D40',0.5),(45,'D45',0.5),(60,'D60',4)]

print('='*94)
print('THE COMPLETE SHODASHAVARGA — 16 DIVISIONAL CHARTS')
print('='*94)
hdr = 'graha    ' + ''.join(f'{nm:>6}' for _,nm,_ in VARGAS)
print(hdr); print('-'*len(hdr))
for g in ['Lagna']+G+['Rahu','Ketu']:
    row=f'{g:9s}'
    for n,_,_ in VARGAS:
        row += f'{SIGNS[v(D1[g],n)][:5]:>6}'
    print(row)

print('\n'+'='*94)
print('SEVEN CHARTS NOT PREVIOUSLY COMPUTED — house positions')
print('='*94)
for n,nm,_ in VARGAS:
    if nm in ('D1','D3','D7','D9','D10','D12','D24','D27','D30'): continue
    lag=v(D1['Lagna'],n)
    print(f'\n--- {nm} (lagna {SIGNS[lag]}) ---')
    for g in G+['Rahu','Ketu']:
        si=v(D1[g],n); h=(si-lag)%12+1
        dg = dignity(g,si)[0] if g in G else '—'
        mark = '  <<<' if dg in ('exalted','own','debilitated') else ''
        print(f'   {g:8s} {SIGNS[si]:11s} H{h:<3d} {dg}{mark}')

print('\n'+'='*94)
print('VIMSHOPAKA BALA (Shodashavarga weighted, out of 20)')
print('='*94)
res={}
for g in G:
    tot=0
    for n,nm,w in VARGAS:
        tot += w * dignity(g, v(D1[g],n))[1]
    res[g]=tot/20
for g,sc in sorted(res.items(), key=lambda x:-x[1]):
    if sc>=15: verdict='EXCELLENT'
    elif sc>=10: verdict='good'
    elif sc>=7: verdict='moderate'
    else: verdict='weak'
    print(f'  {g:8s} {sc:6.2f} / 20   {verdict}')

print('\n'+'='*94)
print('VAISESHIKAMSHA — dignity count across all 16 vargas')
print('='*94)
TITLE=[(2,'Parijatamsha'),(3,'Uttamamsha'),(4,'Gopuramsha'),(5,'Simhasanamsha'),
       (6,'Parvatamsha'),(7,'Devalokamsha'),(8,'Brahmalokamsha'),(9,'Airavatamsha'),
       (10,'Shridhamamsha')]
for g in G:
    good=sum(1 for n,_,_ in VARGAS if dignity(g,v(D1[g],n))[0] in ('exalted','own','friend'))
    exa =sum(1 for n,_,_ in VARGAS if dignity(g,v(D1[g],n))[0]=='exalted')
    own =sum(1 for n,_,_ in VARGAS if dignity(g,v(D1[g],n))[0]=='own')
    deb =sum(1 for n,_,_ in VARGAS if dignity(g,v(D1[g],n))[0]=='debilitated')
    t=''
    for k,nm in TITLE:
        if good>=k: t=nm
    print(f'  {g:8s} dignified in {good:2d}/16   (exalted {exa}, own {own}, debilitated {deb})   {t}')
