SIGNS=['Mesha','Vrishabha','Mithuna','Karka','Simha','Kanya','Tula','Vrischika','Dhanu','Makara','Kumbha','Meena']
S=SIGNS.index
G=['Surya','Chandra','Mangal','Budha','Guru','Shukra','Shani','Rahu','Ketu']
# Benefic/malefic per this chart: Budha combust & with malefic Surya -> malefic (confirmed by its
# Paksha Bala of 49.89, the malefic value, in the supplied table). Chandra waxing -> benefic.
BEN={'Guru','Shukra','Chandra'}

CHARTS={
 'D1  Rashi':   ('Kanya',   dict(Surya='Mesha',Chandra='Vrishabha',Mangal='Vrishabha',Budha='Mesha',
                 Guru='Mithuna',Shukra='Mesha',Shani='Vrishabha',Rahu='Vrishabha',Ketu='Vrischika')),
 'D9  Navamsha':('Kanya',   dict(Surya='Mesha',Chandra='Makara',Mangal='Meena',Budha='Karka',
                 Guru='Kumbha',Shukra='Vrischika',Shani='Mithuna',Rahu='Kanya',Ketu='Meena')),
 'D10 Dashamsha':('Kumbha', dict(Surya='Mesha',Chandra='Makara',Mangal='Meena',Budha='Karka',
                 Guru='Tula',Shukra='Vrischika',Shani='Mithuna',Rahu='Kanya',Ketu='Meena')),
 'D11 Rudramsha':('Kanya',  dict(Surya='Mesha',Chandra='Meena',Mangal='Vrishabha',Budha='Karka',
                 Guru='Karka',Shukra='Dhanu',Shani='Kanya',Rahu='Dhanu',Ketu='Mithuna')),
 'D8  Ashtamsha':('Meena',  dict(Surya='Mesha',Chandra='Dhanu',Mangal='Makara',Budha='Mithuna',
                 Guru='Vrischika',Shukra='Tula',Shani='Mesha',Rahu='Karka',Ketu='Makara')),
 'D27 Bhamsha': ('Karka',   dict(Surya='Vrishabha',Chandra='Simha',Mangal='Makara',Budha='Makara',
                 Guru='Vrischika',Shukra='Makara',Shani='Vrischika',Rahu='Karka',Ketu='Makara')),
 'D30 Trimsha': ('Vrischika',dict(Surya='Mesha',Chandra='Vrishabha',Mangal='Kanya',Budha='Dhanu',
                 Guru='Dhanu',Shukra='Mithuna',Shani='Meena',Rahu='Vrischika',Ketu='Vrishabha')),
}
KEN={1,4,7,10}; TRI={1,5,9}; UPA={3,6,10,11}; DUS={6,8,12}

print('='*78); print('HOUSE-CLASS CENSUS ACROSS THE MAJOR VARGAS'); print('='*78)
print('Benefics here: Guru, Shukra, Chandra   |   Malefics: Surya, Mangal, Budha, Shani, Rahu, Ketu')
print('(Budha counted malefic — combust with Surya; its Paksha Bala of 49.89 is the malefic value)')
summary={}
for name,(lag,pos) in CHARTS.items():
    li=S(lag)
    H={g:(S(pos[g])-li)%12+1 for g in G}
    k=[g for g in G if H[g] in KEN]; t=[g for g in G if H[g] in TRI]
    u=[g for g in G if H[g] in UPA]; d=[g for g in G if H[g] in DUS]
    kb=[g for g in k if g in BEN]; um=[g for g in u if g not in BEN]; db=[g for g in d if g in BEN]
    summary[name]=(len(k),len(t),len(u),len(d),len(kb),len(um),len(db))
    print(f'\n--- {name}  (lagna {lag}) ---')
    print('   ' + '  '.join(f'{g[:2]}:{H[g]}' for g in G))
    print(f'   KENDRA   {len(k)}: {", ".join(k) or "EMPTY"}')
    print(f'   TRIKONA  {len(t)}: {", ".join(t) or "EMPTY"}')
    print(f'   UPACHAYA {len(u)}: {", ".join(u) or "EMPTY"}')
    print(f'   DUSTHANA {len(d)}: {", ".join(d) or "EMPTY"}')
    print(f'   -> benefics in kendra: {len(kb)} | malefics in upachaya: {len(um)} (both productive)')
    print(f'   -> benefics wasted in dusthana: {len(db)}')

print('\n'+'='*78); print('COMPARATIVE TABLE'); print('='*78)
print(f"{'chart':16s}{'KEN':>5}{'TRI':>5}{'UPA':>5}{'DUS':>5}   {'ben-in-KEN':>11}{'mal-in-UPA':>12}{'ben-in-DUS':>12}")
for n,(a,b,c,e,f,g_,h) in summary.items():
    print(f'{n:16s}{a:5d}{b:5d}{c:5d}{e:5d}   {f:11d}{g_:12d}{h:12d}')

print('\n'+'='*78); print('PRODUCTIVE-PLACEMENT NET (ben-in-KEN + mal-in-UPA − ben-in-DUS)'); print('='*78)
for n,(a,b,c,e,f,g_,h) in sorted(summary.items(), key=lambda x:-(x[1][4]+x[1][5]-x[1][6])):
    print(f'  {n:16s} {f}+{g_}-{h} = {f+g_-h:+d}')
