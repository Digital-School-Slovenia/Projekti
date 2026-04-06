# Rešitev / učiteljske usmeritve – 10 – Zanka `for` in `range`

## Kako voditi to uro

- ne razlagaj predolgo; daj jedro, potem pa naloge,
- po 10–15 minutah naredi prvi checkpoint,
- pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk,
- pri hitrih učencih najprej odpri dodatne naloge, šele nato prosto nadgrajevanje.

## Referenčni primeri iz tvojega izvornega paketa

### Izsek iz `00_ponovitev.py`

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

1. Izpiši števila od 1 do 10 z `for`.
2. Izpiši soda števila do 20.
3. Naredi pravokotnik iz zvezdic.

## Kaj šteje kot dober minimum

- delujoče jedro,
- vsaj ena dodatna rešena naloga,
- učenec zna povedati, kaj v kodi zares dela in kaj je popravil.

## Python datoteke v tej mapi

- `06_referencni_primer.py`
