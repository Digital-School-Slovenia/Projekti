# Rešitev – 13 – Nizi in oblikovanje izpisa

Tukaj je jedro rešitve za sklop **13 – Nizi in oblikovanje izpisa**. Pokaži en kratek primer. Potem naj učenci delajo.

## Kaj pokaži najprej

- Ne razlagaj predolgo; daj jedro, potem pa naloge
- Po 10–15 minutah naredi prvi kratek pregled
- Pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk
- Hitrejše učence najprej usmeri na dodatne naloge, šele nato na prosto nadgrajevanje.

## Primer rešitve

### Primer 1

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

### Primer 2

```python
izdelek = "Knjiga"
cena = 12.5
kolicina = 3
skupaj = cena * kolicina

print(f"{'IZDELEK':<15}{'KOL.':>5}{'CENA':>10}")
print(f"{izdelek:<15}{kolicina:>5}{cena:>10.2f}")
print(f"{'SKUPAJ':<20}{skupaj:>10.2f}")
```

## Kaj mora do konca ure delovati

- Učenec zaključi obvezno jedro sklopa in ga zna demonstrirati
- Učenec zna povedati, kje v kodi je bilo treba kaj popraviti
- Vsaj enkrat samostojno preizkusi svojo rešitev med delom.

## Hitri pregled med uro

- Vprašaj za ime in izpiši dolžino imena.
- Izpiši ime z velikimi in malimi črkami.
- Preveri, ali se beseda začne z določeno črko.

## Tipične napake

- Manjkajoč `:` pri pogojih ali funkcijah
- Napačna zamaknitev bloka kode
- Pozabljena pretvorba `input()` v `int()` ali `float()`
- Napačno ime spremenljivke
- Učenec ne zažene programa po vsakem manjšem koraku.

## Datoteke v tej mapi

- `06_referencni_primer.py`
