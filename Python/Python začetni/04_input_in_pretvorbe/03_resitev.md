# Rešitev / učiteljske usmeritve – 04 – Vnos uporabnika in pretvorba tipov

## Kako voditi to uro

- ne razlagaj predolgo; daj jedro, potem pa naloge,
- po 10–15 minutah naredi prvi checkpoint,
- pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk,
- pri hitrih učencih najprej odpri dodatne naloge, šele nato prosto nadgrajevanje.

## Referenčni primeri iz tvojega izvornega paketa

### Izsek iz `03_vnosi.py`

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
