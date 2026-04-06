# Rešitev / učiteljske usmeritve – 07 – Random, mini kvizi in odločanje v praksi

## Kako voditi to uro

- ne razlagaj predolgo; daj jedro, potem pa naloge,
- po 10–15 minutah naredi prvi checkpoint,
- pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk,
- pri hitrih učencih najprej odpri dodatne naloge, šele nato prosto nadgrajevanje.

## Referenčni primeri iz tvojega izvornega paketa

### Izsek iz `kviz.py`

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

### Izsek iz `postevanka.py`

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

1. Začetna naloga
2. Uporabnik dobi 4
3. Če je sončno → Obleci pulover 🧥

## Kaj šteje kot dober minimum

- delujoče jedro,
- vsaj ena dodatna rešena naloga,
- učenec zna povedati, kaj v kodi zares dela in kaj je popravil.

## Python datoteke v tej mapi

- `06_referencni_primer.py`
