# Rešitev – 04 – Vnos uporabnika in pretvorba tipov

Tukaj je jedro rešitve za sklop **04 – Vnos uporabnika in pretvorba tipov**. Pokaži en kratek primer. Potem naj učenci delajo.

## Kaj pokaži najprej

- Ne razlagaj predolgo; daj jedro, potem pa naloge
- Po 10–15 minutah naredi prvi kratek pregled
- Pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk
- Hitrejše učence najprej usmeri na dodatne naloge, šele nato na prosto nadgrajevanje.

## Primer rešitve

```python
tvoje_ime = input("Vnesi tvoje ime: ")
print(f"Živijo, {tvoje_ime}")

tvoja_starost = input("Vnesi svojo starost: ")
tvoja_starost = int(tvoja_starost)
print(f"Čez 10 let boš star {tvoja_starost + 10}")

tvoja_najljubsa_hrana = input("Vnesi svojo najljubso hrano: ")
print(f"Tvoja naljubsa hrana je: {tvoja_najljubsa_hrana}")

tvoj_naljubsi_ucitelj = input("Vnesi ime svojega najljubsega ucitelja:")
print(f"Tvoj naljubsi ucitelj: {tvoj_naljubsi_ucitelj}")
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
