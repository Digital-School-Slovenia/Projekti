# Rešitev – 10 – Zanka `for` in `range`

Tukaj je jedro rešitve za sklop **10 – Zanka `for` in `range`**. Pokaži en kratek primer. Potem naj učenci delajo.

## Kaj pokaži najprej

- Ne razlagaj predolgo; daj jedro, potem pa naloge
- Po 10–15 minutah naredi prvi kratek pregled
- Pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk
- Hitrejše učence najprej usmeri na dodatne naloge, šele nato na prosto nadgrajevanje.

## Primer rešitve

```python
from time import sleep

# # -----------
# # Prva naloga
# for stevec in range(1, 51, 1):
# print(stevec)
# sleep(0.05)
# 
# for stevec_nazaj in range(50, 0, -1):
#     print(stevec_nazaj)
#     sleep(0.05)
    
# -----------
# Druga naloga

# Uporabnik vnese stevilo ovck, bodi pozoren
# da je potrebno vnos spremeniti v stevilo int(....)
ovcke = int(input("Vnesi število ovčk: "))

for i in range(1, ovcke + 1):
    # Tole se izpisuje znotraj for zanke.
    print(f"Ovčka št. {i} skoči čez ograjo!")
    sleep(1) # uvozi knjiznico from time import sleep

# Po koncu for zanke se izpise se tole:
print("Zzz… zaspan kot Python 💤")
```

## Kaj mora do konca ure delovati

- Učenec zaključi obvezno jedro sklopa in ga zna demonstrirati
- Učenec zna povedati, kje v kodi je bilo treba kaj popraviti
- Vsaj enkrat samostojno preizkusi svojo rešitev med delom.

## Hitri pregled med uro

- Izpiši števila od 1 do 10 z `for`.
- Izpiši soda števila do 20.
- Naredi pravokotnik iz zvezdic.

## Tipične napake

- Manjkajoč `:` pri pogojih ali funkcijah
- Napačna zamaknitev bloka kode
- Pozabljena pretvorba `input()` v `int()` ali `float()`
- Napačno ime spremenljivke
- Učenec ne zažene programa po vsakem manjšem koraku.

## Datoteke v tej mapi

- `06_referencni_primer.py`
