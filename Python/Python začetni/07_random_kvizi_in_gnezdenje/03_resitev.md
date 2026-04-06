# Rešitev – 07 – Random, mini kvizi in odločanje v praksi

Tukaj je jedro rešitve za sklop **07 – Random, mini kvizi in odločanje v praksi**. Pokaži en kratek primer. Potem naj učenci delajo.

## Kaj pokaži najprej

- Ne razlagaj predolgo; daj jedro, potem pa naloge
- Po 10–15 minutah naredi prvi kratek pregled
- Pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk
- Hitrejše učence najprej usmeri na dodatne naloge, šele nato na prosto nadgrajevanje.

## Primer rešitve

### Primer 1

```python
# Definiramo tocke
tocke = 0

# Dolocimo vprasanja
vprasanje1 = "Kje živijo pingvini? "
vprasanje2 = "Kako se prižge računalnik"
vprasanje3 = "Ali ima Viktor rad burek"
vprasanje4 = "...."

print("Dobrodošel v kvizu")
print("------")

# 1. vprasanje
print(vprasanje1)
print("A: Južni pol  B: Severni pol  C: Mars  D: Kanada")
odgovor = input("Vnesi odgovor:" )
if odgovor == "A":
    tocke = tocke + 1

# 2. vprasanje
print(vprasanje1)
print("A: Pritisnise tipko  B: Polijes z vodo  C: Ga pobozas  D: Ne vem")
odgovor = input("Vnesi odgovor:" )

match odgovor:
    case "A":
        tocke = tocke + 1
    case _:
        pass

# Na koncu izpisite rezultat
print("------")
print(f"Na kvizu si zbral toliko točk: {tocke}")
```

### Primer 2

```python
# Iz knjiznice random dodamo funkcijo randint
from random import randint

# Izberimo dve nakljucni stevili med 1 in 12
a = randint(1, 12)
b = randint(1, 12)

# Izracunamo rezultat mnozenja
rezultat = a * b

# Vnesemo stevilo in ga spremenimo v integer (stevilo)
vnos = input(f"Koliko je {a} * {b}: ")
vnos = int(vnos)

# Preverimo pravilnost.
if vnos == rezultat:
    print("Odgovor je pravilen!")
else:
    print(f"Žal si se zmotil pravilno je {rezultat}.")
```

## Kaj mora do konca ure delovati

- Učenec zaključi obvezno jedro sklopa in ga zna demonstrirati
- Učenec zna povedati, kje v kodi je bilo treba kaj popraviti
- Vsaj enkrat samostojno preizkusi svojo rešitev med delom.

## Hitri pregled med uro

- Začetna naloga
- Uporabnik dobi 4
- Če je sončno → Obleci pulover 🧥

## Tipične napake

- Manjkajoč `:` pri pogojih ali funkcijah
- Napačna zamaknitev bloka kode
- Pozabljena pretvorba `input()` v `int()` ali `float()`
- Napačno ime spremenljivke
- Učenec ne zažene programa po vsakem manjšem koraku.

## Datoteke v tej mapi

- `06_referencni_primer.py`
