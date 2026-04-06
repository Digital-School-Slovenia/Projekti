# Rešitev – 05 – Pogoji `if` – osnove odločanja

Tukaj je jedro rešitve za sklop **05 – Pogoji `if` – osnove odločanja**. Pokaži en kratek primer. Potem naj učenci delajo.

## Kaj pokaži najprej

- Ne razlagaj predolgo; daj jedro, potem pa naloge
- Po 10–15 minutah naredi prvi kratek pregled
- Pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk
- Hitrejše učence najprej usmeri na dodatne naloge, šele nato na prosto nadgrajevanje.

## Primer rešitve

```python
# 1. naloga
tvoje_ime = input("Vpiši ime: ")

if tvoje_ime == "Brina":
    print("Legendica!")
else:
    print("Nisi Brina, a si vseeno kul 😀")
    
# 2. naloga
izbira = input("Ali imaš rad pico? ")

if izbira == "da":
    print("Tudi jaz!")
else:
    print("Kako lahko živiš brez pice???")

# 3. naloga
naljubsa_barva = input("Tvoj naj barva? ")

if naljubsa_barva == 'modra':
    print("Super izbira")
else:
    print("To je pa drzna izbira")
```

## Kaj mora do konca ure delovati

- Učenec zaključi obvezno jedro sklopa in ga zna demonstrirati
- Učenec zna povedati, kje v kodi je bilo treba kaj popraviti
- Vsaj enkrat samostojno preizkusi svojo rešitev med delom.

## Hitri pregled med uro

- Naloge
- Napiši program, ki uporabnika vpraša za ime. Če je ime enako tvojemu imenu naj se izpiše »Legenda!« sicer pa »Nisi TVOJE_IME, a si vseeno kul!«
- Napiši program, ki te vpraša koliko mačk imaš:

## Tipične napake

- Manjkajoč `:` pri pogojih ali funkcijah
- Napačna zamaknitev bloka kode
- Pozabljena pretvorba `input()` v `int()` ali `float()`
- Napačno ime spremenljivke
- Učenec ne zažene programa po vsakem manjšem koraku.

## Datoteke v tej mapi

- `06_referencni_primer.py`
