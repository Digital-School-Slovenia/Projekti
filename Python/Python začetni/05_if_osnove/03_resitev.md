# Rešitev / učiteljske usmeritve – 05 – Pogoji `if` – osnove odločanja

## Kako voditi to uro

- ne razlagaj predolgo; daj jedro, potem pa naloge,
- po 10–15 minutah naredi prvi checkpoint,
- pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk,
- pri hitrih učencih najprej odpri dodatne naloge, šele nato prosto nadgrajevanje.

## Referenčni primeri iz tvojega izvornega paketa

### Izsek iz `01_osnovni_if.py`

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

1. ## Naloge
2. Napiši program, ki uporabnika vpraša za ime. Če je ime enako tvojemu imenu naj se izpiše »Legenda!« sicer pa »Nisi TVOJE_IME, a si vseeno kul!«
3. Napiši program, ki te vpraša koliko mačk imaš:

## Kaj šteje kot dober minimum

- delujoče jedro,
- vsaj ena dodatna rešena naloga,
- učenec zna povedati, kaj v kodi zares dela in kaj je popravil.

## Python datoteke v tej mapi

- `06_referencni_primer.py`
