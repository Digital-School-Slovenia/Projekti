# Rešitev – 16 – Funkcije – `return`, seznami in razdelitev problema

Tukaj je jedro rešitve za sklop **16 – Funkcije – `return`, seznami in razdelitev problema**. Pokaži en kratek primer. Potem naj učenci delajo.

## Kaj pokaži najprej

- Ne razlagaj predolgo; daj jedro, potem pa naloge
- Po 10–15 minutah naredi prvi kratek pregled
- Pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk
- Hitrejše učence najprej usmeri na dodatne naloge, šele nato na prosto nadgrajevanje.

## Primer rešitve

```python
def povprecje(seznam):
    if not seznam:
        return 0
    return sum(seznam) / len(seznam)

def filtriraj_pozitivna(seznam):
    rezultat = []
    for stevilo in seznam:
        if stevilo > 0:
            rezultat.append(stevilo)
    return rezultat

ocene = [5, 4, 5, 3, 4]
print("Povprečje:", povprecje(ocene))
print("Pozitivna števila:", filtriraj_pozitivna([-2, 5, 0, 7, -1, 3]))
```

## Kaj mora do konca ure delovati

- Učenec zaključi obvezno jedro sklopa in ga zna demonstrirati
- Učenec zna povedati, kje v kodi je bilo treba kaj popraviti
- Vsaj enkrat samostojno preizkusi svojo rešitev med delom.

## Hitri pregled med uro

- 🟢 lažje
- 🟡 srednje
- Sprejme število sledilcev

## Tipične napake

- Manjkajoč `:` pri pogojih ali funkcijah
- Napačna zamaknitev bloka kode
- Pozabljena pretvorba `input()` v `int()` ali `float()`
- Napačno ime spremenljivke
- Učenec ne zažene programa po vsakem manjšem koraku.

## Datoteke v tej mapi

- `06_referencni_primer.py`
