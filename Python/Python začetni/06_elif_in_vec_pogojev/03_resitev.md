# Rešitev / učiteljske usmeritve – 06 – `elif`, `else` in več možnosti odločanja

## Kako voditi to uro

- ne razlagaj predolgo; daj jedro, potem pa naloge,
- po 10–15 minutah naredi prvi checkpoint,
- pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk,
- pri hitrih učencih najprej odpri dodatne naloge, šele nato prosto nadgrajevanje.

## Referenčni primeri iz tvojega izvornega paketa

### Izsek iz `02_nadaljevanje_if.py`

```python
# semafor_barva = input("Vnesi barvo na semaforju: ")
# # SPREMENIM BESEDO V VELIKE CRKE
# semafor_barva = semafor_barva.upper() # .lower()
# 
# if semafor_barva == "ZELENA":
#     print("Lahko voziš")
# elif semafor_barva == "RUMENA":
#     print("Upočasnuj vozilo")
# elif semafor_barva == "RDECA":
#     print("Stoj!")
   
    
# 1. naloga

# Uporabnik vpise koliko mack ima z input()
stevilo_mack = input("Stevilo mack: ")

# Vnos spremenimo v stevilo z int()
stevilo_mack = int(stevilo_mack)

# Preverimo pogoje ... 
if stevilo_mack > 10:
    print("Ti si uradno macja oseba 🐱")
elif stevilo_mack < 10 and stevilo_mack >= 5:
    print("Cisto normalno macje zivljenje.")
else:
    # Ce noben pogoj NE velja se izpise spodnje
    print("Nimas veliko mack")
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
