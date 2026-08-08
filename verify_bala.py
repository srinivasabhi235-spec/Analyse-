G = ["Surya","Chandra","Mangal","Budha","Guru","Shukra","Shani"]
def row(*v): return dict(zip(G, v))

sthana = row(297.16,202.10,154.39,158.49,255.77,201.13,174.30)
comp_sthana = {
 "Uchcha":      row(57.16,59.60,26.89,8.49,53.27,51.13,9.30),
 "SaptaVargiya":row(165.00,97.50,97.50,90.00,112.50,90.00,120.00),
 "OjaYugma":    row(30.00,30.00,0.00,15.00,30.00,15.00,15.00),
 "Kendradi":    row(30.00,15.00,15.00,30.00,60.00,30.00,15.00),
 "Drekkana":    row(15.00,0.00,15.00,15.00,0.00,15.00,15.00)}

kala = row(254.64,103.47,151.05,156.69,159.51,91.73,143.65)
comp_kala = {
 "NataUnnata":  row(30.22,29.78,29.78,60.00,30.22,30.22,29.78),
 "Paksha":      row(49.89,20.21,49.89,49.89,10.11,10.11,49.89),
 "TriBhaga":    row(0,0,0,0,60.00,0,60.00),
 "Varshadhipati":row(0,0,15.00,0,0,0,0),
 "Masadhipati": row(30.00,0,0,0,0,0,0),
 "Varadhipati": row(0,45.00,0,0,0,0,0),
 "Horadhipati": row(60.00,0,0,0,0,0,0),
 "Ayana":       row(84.53,8.48,56.38,46.80,59.18,51.40,3.98),
 "Yuddha":      row(0,0,0,0,0,0,0)}

disha   = row(31.56,18.33,43.51,4.28,25.72,21.06,43.24)
chesta  = row(38.45,10.11,14.37,42.15,26.12,44.11,16.75)
naisarg = row(60.00,51.43,17.14,25.71,34.29,42.86,8.57)
drishti = row(1.67,-0.04,-0.73,0.54,-8.58,0.00,-2.99)
total   = row(683.48,385.39,379.73,387.86,492.83,400.89,383.53)
rupas   = row(11.39,6.42,6.33,6.46,8.21,6.68,6.39)
minreq  = row(5.00,6.00,5.00,7.00,6.50,5.50,5.00)
ratio   = row(2.2782,1.0705,1.2657,0.9234,1.2636,1.2148,1.2784)
rank    = row(1,6,3,7,4,5,2)
ishta   = row(46.88,24.54,19.66,18.91,37.30,47.49,12.48)
kashta  = row(7.83,4.49,38.87,30.32,15.10,11.87,46.83)

def ok(a,b,tol=0.02): return "OK" if abs(a-b)<=tol else "*** MISMATCH ***"

print("=== Shadbala internal consistency ===")
for g in G:
    s = sum(c[g] for c in comp_sthana.values())
    k = sum(c[g] for c in comp_kala.values())
    t = sthana[g]+disha[g]+kala[g]+chesta[g]+naisarg[g]+drishti[g]
    print(f"  {g:8s} Sthana {s:7.2f} vs {sthana[g]:7.2f} {ok(s,sthana[g]):16s}"
          f" Kala {k:7.2f} vs {kala[g]:7.2f} {ok(k,kala[g]):16s}"
          f" Total {t:7.2f} vs {total[g]:7.2f} {ok(t,total[g])}")

print("\n=== Rupas, ratio, rank ===")
by_ratio = sorted(G, key=lambda g:-rupas[g]/minreq[g])
for g in G:
    r, rt = total[g]/60, rupas[g]/minreq[g]
    verdict = "BELOW MINIMUM" if rt < 1 else ""
    print(f"  {g:8s} rupas {r:6.2f} ({ok(r,rupas[g],0.01)})  ratio {rt:6.4f} vs {ratio[g]:6.4f}"
          f"  rank {by_ratio.index(g)+1} vs {rank[g]}  {verdict}")

print("\n=== Net benefic capacity (Ishta - Kashta) ===")
for g in sorted(G, key=lambda g:-(ishta[g]-kashta[g])):
    n = ishta[g]-kashta[g]
    print(f"  {g:8s} ishta {ishta[g]:6.2f}  kashta {kashta[g]:6.2f}  net {n:+7.2f}")

# ---------------- Bhava Bala ----------------
print("\n=== Bhava Bala consistency ===")
adhip = [387.86,400.89,379.73,492.83,383.53,383.53,492.83,379.73,400.89,387.86,385.39,683.48]
bdish = [60,50,20,0,50,10,30,40,50,30,10,40]
bdrik = [55.38,99.83,49.46,64.03,41.29,39.21,8.59,0.00,5.53,25.37,29.70,31.69]
bpind = [503.25,550.72,449.18,556.87,474.81,432.74,531.42,419.73,456.42,443.23,425.09,755.17]
brup  = [8.39,9.18,7.49,9.28,7.91,7.21,8.86,7.00,7.61,7.39,7.08,12.59]
brank = [5,3,8,2,6,10,4,12,7,9,11,1]
LORDS = ["Budha","Shukra","Mangal","Guru","Shani","Shani","Guru","Mangal","Shukra","Budha","Chandra","Surya"]
ROM = "I II III IV V VI VII VIII IX X XI XII".split()
order = sorted(range(12), key=lambda i:-bpind[i])
for i in range(12):
    t = adhip[i]+bdish[i]+bdrik[i]
    lord_ok = "OK" if abs(adhip[i]-total[LORDS[i]])<0.02 else "*** LORD MISMATCH ***"
    print(f"  H{ROM[i]:<4s} lord {LORDS[i]:8s} {lord_ok:20s} pinda {t:7.2f} vs {bpind[i]:7.2f} {ok(t,bpind[i]):16s}"
          f" rupas {bpind[i]/60:5.2f} ({ok(bpind[i]/60,brup[i],0.01)})  rank {order.index(i)+1} vs {brank[i]}")

# ---------------- Ashtakavarga ----------------
print("\n=== Sarvashtakavarga ===")
SIGNS = ["Mesha","Vrishabha","Mithuna","Karka","Simha","Kanya",
         "Tula","Vrischika","Dhanu","Makara","Kumbha","Meena"]
# columns: Lagna, Surya, Chandra, Mangal, Budha, Guru, Shukra, Shani
AV = {
 "Mesha":     (4,2,2,1,4,4,5,3,21), "Vrishabha": (4,3,2,3,4,5,3,2,22),
 "Mithuna":   (3,4,6,4,6,5,3,1,29), "Karka":     (8,3,6,2,2,5,5,5,28),
 "Simha":     (2,4,2,4,6,4,4,0,24), "Kanya":     (3,2,4,4,3,6,5,5,29),
 "Tula":      (4,4,6,1,2,3,3,5,24), "Vrischika": (5,5,4,5,4,3,3,4,28),
 "Dhanu":     (2,5,2,2,7,6,5,2,29), "Makara":    (2,4,5,2,4,6,6,2,29),
 "Kumbha":    (7,7,6,6,7,5,5,5,41), "Meena":     (5,5,4,5,5,4,5,5,33)}
tot = 0
for s in SIGNS:
    v = AV[s]; calc = sum(v[1:8]); tot += v[8]
    house = (SIGNS.index(s)-5) % 12 + 1
    print(f"  {s:11s} H{house:<2d} sum(Su..Sh) {calc:2d} vs printed {v[8]:2d} {ok(calc,v[8],0)}")
print(f"  TOTAL {tot} (classical Sarvashtakavarga total is 337) -> {ok(tot,337,0)}")

print("\n  By house, sorted:")
hs = sorted(((SIGNS.index(s)-5)%12+1, s, AV[s][8]) for s in SIGNS)
for h,s,v in sorted(hs, key=lambda x:-x[2]):
    mark = "  <-- highest" if v==41 else ("  <-- lowest" if v==21 else "")
    print(f"    H{h:<2d} {s:11s} {v:2d}{mark}")
print(f"  average per sign = {337/12:.2f}")

# ---------------- Shodhya Pinda ----------------
print("\n=== Shodhya Pinda ===")
SP = {"Lagna":(95,70,165),"Surya":(120,18,138),"Chandra":(33,0,33),"Mangal":(164,48,212),
      "Budha":(94,58,152),"Guru":(61,20,81),"Shukra":(78,17,95),"Shani":(133,51,184)}
for k,(r,g,s) in sorted(SP.items(), key=lambda x:-x[1][2]):
    print(f"  {k:8s} rashi {r:3d} + graha {g:3d} = {r+g:3d} vs printed {s:3d} {ok(r+g,s,0)}")

# ---------------- cross-checks against D1 ----------------
print("\n=== Cross-checks against the D1 longitudes ===")
from datetime import date
sun, moon, budha = 1.4675, 31.7875, 10.4639
elong = (moon-sun) % 360
print(f"  Moon-Sun elongation {elong:.2f}deg -> tithi {int(elong//12)+1} (Shukla paksha, ~{elong/12.19:.1f} days after new moon)")
pb = 60*elong/180
print(f"  Paksha bala: benefic {pb:.2f} (printed Guru/Shukra {comp_kala['Paksha']['Guru']}), "
      f"malefic {60-pb:.2f} (printed Surya {comp_kala['Paksha']['Surya']}), Moon x2 = {2*pb:.2f} (printed {comp_kala['Paksha']['Chandra']})")
deb = 345.0
print(f"  Budha uchcha bala: 60*({budha}-{deb-360})/180 = {60*((budha-(deb-360))%360)/180:.2f} vs printed {comp_sthana['Uchcha']['Budha']}")
d = date(2002,4,15)
print(f"  Vara bala 45 -> Chandra -> birth weekday must be Monday. 15 Apr 2002 = {d.strftime('%A')}")
print(f"  Hora bala 60 -> Surya hora. On Monday the Surya hora is the 5th and 12th from sunrise.")
lag = 177.6269
print(f"  Ascendant {lag:.2f}deg is {(lag-sun)%360:.1f}deg past the Sun -> birth ~late afternoon/early evening")

# ---------------- Reduced Ashtakavarga -> Shodhya Pinda ----------------
print("\n=== Reduced Ashtakavarga rebuilds Shodhya Pinda ===")
# reduced (shodhita) bindus, columns: Lagna, Surya, Chandra, Mangal, Budha, Guru, Shukra, Shani
RED = {"Mesha": (2,0,0,0,0,0,1,3), "Vrishabha": (2,1,0,1,1,0,0,0),
       "Mithuna": (0,0,0,3,4,2,0,0), "Karka": (3,0,2,0,0,2,2,1),
       "Simha": (0,2,0,3,2,0,0,0), "Kanya": (1,0,2,0,0,0,2,3),
       "Tula": (0,0,0,0,0,0,0,4), "Vrischika": (0,2,0,3,2,0,0,0),
       "Dhanu": (0,2,0,1,0,1,1,1), "Makara": (0,2,3,0,1,1,2,0),
       "Kumbha": (4,2,0,5,1,1,2,4), "Meena": (0,2,0,1,0,1,1,1)}
IDX = {"Lagna":0, "Surya":1, "Chandra":2, "Mangal":3, "Budha":4,
       "Guru":5, "Shukra":6, "Shani":7}
RASHI_GUNA = {"Mesha":7, "Vrishabha":10, "Mithuna":8, "Karka":4, "Simha":10,
              "Kanya":5, "Tula":7, "Vrischika":8, "Dhanu":9, "Makara":5,
              "Kumbha":11, "Meena":12}
GRAHA_GUNA = {"Surya":5, "Chandra":5, "Mangal":8, "Budha":5,
              "Guru":10, "Shukra":7, "Shani":5}
OCCUPIES = {"Surya":"Mesha", "Chandra":"Vrishabha", "Mangal":"Vrishabha",
            "Budha":"Mesha", "Guru":"Mithuna", "Shukra":"Mesha", "Shani":"Vrishabha"}

every = True
for name, (r_given, g_given, s_given) in SP.items():
    c = IDX[name]
    rashi = sum(RED[s][c] * RASHI_GUNA[s] for s in SIGNS)
    graha = sum(RED[OCCUPIES[g]][c] * GRAHA_GUNA[g] for g in G)
    good = (rashi == r_given) and (graha == g_given) and (rashi + graha == s_given)
    every &= good
    print(f"  {name:8s} rashi {rashi:3d} vs {r_given:3d} | graha {graha:3d} vs {g_given:3d}"
          f" | shodhya {rashi+graha:3d} vs {s_given:3d}   {'OK' if good else '*** MISMATCH ***'}")
print(f"  Reduced Ashtakavarga fully reproduces Shodhya Pinda: {every}")

print("\n  Note: the 'Sarv' column of the Reduced Ashtakavarga is NOT the sum of the")
print("  reduced graha columns (which do verify above), so it is a separately derived")
print("  quantity and is excluded from the reading:")
RED_SARV = {"Mesha":4, "Vrishabha":5, "Mithuna":0, "Karka":0, "Simha":7, "Kanya":0,
            "Tula":5, "Vrischika":0, "Dhanu":0, "Makara":0, "Kumbha":0, "Meena":5}
for s in SIGNS:
    tot = sum(RED[s][1:8])
    if tot != RED_SARV[s]:
        print(f"    {s:11s} columns sum to {tot:2d}, printed Sarv is {RED_SARV[s]:2d}")
