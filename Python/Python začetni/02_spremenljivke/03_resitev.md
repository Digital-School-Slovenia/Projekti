# Rešitev / učiteljske usmeritve – 02 – Spremenljivke in poimenovanje podatkov

## Kako voditi to uro

- ne razlagaj predolgo; daj jedro, potem pa naloge,
- po 10–15 minutah naredi prvi checkpoint,
- pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk,
- pri hitrih učencih najprej odpri dodatne naloge, šele nato prosto nadgrajevanje.

## Referenčni primeri iz tvojega izvornega paketa

### Izsek iz `01_spremenljivke.py`

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

## Tipične napake

- manjkajoč `:` pri pogojih ali funkcijah,
- napačna zamaknitev bloka kode,
- pozabljena pretvorba `input()` v `int()` ali `float()`,
- napačno ime spremenljivke,
- učenec ne zažene programa po vsakem manjšem koraku.

## Minimalni kriterij uspeha

- učenec zaključi obvezno jedro sklopa in ga zna demonstrirati,
- učenec zna povedati, kje v kodi je bilo treba kaj popraviti,
- vsaj enkrat samostojno uporabi testiranje med delom.

## Učiteljski checkpointi

1. Izpiše tvoje ime.
2. Izpiše tvojo najljubšo hrano.
3. Ustvari spremenljivko `najljubsi_predmet` in jo izpiši v stavku.

## Kaj šteje kot dober minimum

- delujoče jedro,
- vsaj ena dodatna rešena naloga,
- učenec zna povedati, kaj v kodi zares dela in kaj je popravil.

## Python datoteke v tej mapi

- `06_referencni_primer.py`
