# Rešitev – 17 – Ponovitvene vaje – funkcije in problemsko razmišljanje

Tukaj je jedro rešitve za sklop **17 – Ponovitvene vaje – funkcije in problemsko razmišljanje**. Pokaži en kratek primer. Potem naj učenci delajo.

## Kaj pokaži najprej

- Ne razlagaj predolgo; daj jedro, potem pa naloge
- Po 10–15 minutah naredi prvi kratek pregled
- Pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk
- Hitrejše učence najprej usmeri na dodatne naloge, šele nato na prosto nadgrajevanje.

## Primer rešitve

```python
def je_palindrom(beseda):
    beseda = beseda.lower().replace(" ", "")
    return beseda == beseda[::-1]

def st_prestopov(meja, podatki):
    stevec = 0
    for vrednost in podatki:
        if vrednost > meja:
            stevec += 1
    return stevec

print(je_palindrom("Kajak"))
print(st_prestopov(10, [4, 12, 9, 18, 3, 11]))
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
