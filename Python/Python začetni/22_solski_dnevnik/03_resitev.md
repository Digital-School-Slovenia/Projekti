# Rešitev – 22 – Slovarji v praksi – mini šolski dnevnik

Tukaj je jedro rešitve za sklop **22 – Slovarji v praksi – mini šolski dnevnik**. Pokaži en kratek primer. Potem naj učenci delajo.

## Kaj pokaži najprej

- Ne razlagaj predolgo; daj jedro, potem pa naloge
- Po 10–15 minutah naredi prvi kratek pregled
- Pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk
- Hitrejše učence najprej usmeri na dodatne naloge, šele nato na prosto nadgrajevanje.

## Primer rešitve

```python
dnevnik = {
    "Ana": {"razred": 7, "matematika": 4, "anglescina": 5, "sport": 5},
    "Klara": {"razred": 7, "matematika": 3, "anglescina": 3, "sport": 5},
    "Luka": {"razred": 8, "matematika": 5, "anglescina": 5, "sport": 4},
}

def izpisi_ucenca(ime):
    if ime not in dnevnik:
        print("Tega učenca ni v dnevniku.")
        return

    podatki = dnevnik[ime]
    print(f"Učenec: {ime}")
    print(f"Razred: {podatki['razred']}")
    for predmet, ocena in podatki.items():
        if predmet != 'razred':
            print(f"- {predmet}: {ocena}")

def povprecje_ucenca(ime):
    podatki = dnevnik[ime]
    ocene = []
    for predmet, ocena in podatki.items():
        if predmet != 'razred':
            ocene.append(ocena)
    return sum(ocene) / len(ocene)

for ime in dnevnik:
    print(f"{ime}: povprečje = {povprecje_ucenca(ime):.2f}")
```

## Kaj mora do konca ure delovati

- Učenec zaključi obvezno jedro sklopa in ga zna demonstrirati
- Učenec zna povedati, kje v kodi je bilo treba kaj popraviti
- Vsaj enkrat samostojno preizkusi svojo rešitev med delom.

## Hitri pregled med uro

- Zunanji slovar: **ime učenca → podatki**
- Notranji slovar: **razred + predmeti**
- Uporabi `for kljuc in ucenec:`

## Tipične napake

- Manjkajoč `:` pri pogojih ali funkcijah
- Napačna zamaknitev bloka kode
- Pozabljena pretvorba `input()` v `int()` ali `float()`
- Napačno ime spremenljivke
- Učenec ne zažene programa po vsakem manjšem koraku.

## Datoteke v tej mapi

- `06_uciteljska_resitev.py`
