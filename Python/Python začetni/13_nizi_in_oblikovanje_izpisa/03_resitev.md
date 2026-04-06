# Rešitev / učiteljske usmeritve – 13 – Nizi in oblikovanje izpisa

## Kako voditi to uro

- ne razlagaj predolgo; daj jedro, potem pa naloge,
- po 10–15 minutah naredi prvi checkpoint,
- pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk,
- pri hitrih učencih najprej odpri dodatne naloge, šele nato prosto nadgrajevanje.

# Referenčni primeri

```python
ime = input("Ime: ")
priimek = input("Priimek: ")

polno = f"{ime} {priimek}"
inic = f"{ime[0].upper()}.{priimek[0].upper()}."
print(f"Pozdravljen, {polno}!")
print(f"Tvoje inicialke so: {inic}")
print(f"Dolžina celega imena: {len(polno)}")
print(f"Velike črke: {polno.upper()}")
```

```python
izdelek = "Knjiga"
cena = 12.5
kolicina = 3
skupaj = cena * kolicina

print(f"{'IZDELEK':<15}{'KOL.':>5}{'CENA':>10}")
print(f"{izdelek:<15}{kolicina:>5}{cena:>10.2f}")
print(f"{'SKUPAJ':<20}{skupaj:>10.2f}")
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

1. Vprašaj za ime in izpiši dolžino imena.
2. Izpiši ime z velikimi in malimi črkami.
3. Preveri, ali se beseda začne z določeno črko.

## Kaj šteje kot dober minimum

- delujoče jedro,
- vsaj ena dodatna rešena naloga,
- učenec zna povedati, kaj v kodi zares dela in kaj je popravil.

## Python datoteke v tej mapi

- `06_referencni_primer.py`
