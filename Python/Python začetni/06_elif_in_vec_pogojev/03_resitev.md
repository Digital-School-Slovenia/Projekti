# Rešitev – 06 – `elif`, `else` in več možnosti odločanja

Tukaj je jedro rešitve za sklop **06 – `elif`, `else` in več možnosti odločanja**. Pokaži en kratek primer. Potem naj učenci delajo.

## Kaj pokaži najprej

- Ne razlagaj predolgo; daj jedro, potem pa naloge
- Po 10–15 minutah naredi prvi kratek pregled
- Pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk
- Hitrejše učence najprej usmeri na dodatne naloge, šele nato na prosto nadgrajevanje.

## Primer rešitve

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
