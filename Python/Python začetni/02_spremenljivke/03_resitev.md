# Rešitev – 02 – Spremenljivke in poimenovanje podatkov

Tukaj je jedro rešitve za sklop **02 – Spremenljivke in poimenovanje podatkov**. Pokaži en kratek primer. Potem naj učenci delajo.

## Kaj pokaži najprej

- Ne razlagaj predolgo; daj jedro, potem pa naloge
- Po 10–15 minutah naredi prvi kratek pregled
- Pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk
- Hitrejše učence najprej usmeri na dodatne naloge, šele nato na prosto nadgrajevanje.

## Primer rešitve

```python
# Razlaga ...
#cena = 10 	# integer, cela stevila
#stevilo_pi = 3.14 # float, realna stevila
#ime = "Manca" # string, niz
#crka = "A" # string, niz
#je_resnica = True # boolean (True/False), DA/NE

ime = "Manca"
starost = 28
print(f"Moje ime je {ime} in stara sem {starost} let.")

sendvici_na_dan = 1.3
sendvici_v_letu = sendvici_na_dan * 365
print(f"V enem letu pojem {sendvici_v_letu} sendvicev.")

najljubsi_predmet = "Matematika"
print(f"Moj najljubsi predmet je {najljubsi_predmet}, ampak smo včasih")

pice_na_teden = 3
print(f"Pojem {pice_na_teden * 40} pic v šolskem letu")

supermoc = "Prijaznost"
print(f"Moja supermoč je, da sem {supermoc}")
```

## Kaj mora do konca ure delovati

- Učenec zaključi obvezno jedro sklopa in ga zna demonstrirati
- Učenec zna povedati, kje v kodi je bilo treba kaj popraviti
- Vsaj enkrat samostojno preizkusi svojo rešitev med delom.

## Hitri pregled med uro

- Izpiše tvoje ime.
- Izpiše tvojo najljubšo hrano.
- Ustvari spremenljivko `najljubsi_predmet` in jo izpiši v stavku.

## Tipične napake

- Manjkajoč `:` pri pogojih ali funkcijah
- Napačna zamaknitev bloka kode
- Pozabljena pretvorba `input()` v `int()` ali `float()`
- Napačno ime spremenljivke
- Učenec ne zažene programa po vsakem manjšem koraku.

## Datoteke v tej mapi

- `06_referencni_primer.py`
