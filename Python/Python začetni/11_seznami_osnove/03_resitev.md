# Rešitev – 11 – Seznami – osnove in izpis z zankami

Tukaj je jedro rešitve za sklop **11 – Seznami – osnove in izpis z zankami**. Pokaži en kratek primer. Potem naj učenci delajo.

## Kaj pokaži najprej

- Ne razlagaj predolgo; daj jedro, potem pa naloge
- Po 10–15 minutah naredi prvi kratek pregled
- Pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk
- Hitrejše učence najprej usmeri na dodatne naloge, šele nato na prosto nadgrajevanje.

## Primer rešitve

```python
# POMOC ZA 4. NALOGO
# -------
# USTVARI PRAZEN SEZNAM
playlist = []

# VNESIMO VREDNOSTI V SEZNAM
for i in range(5):
    pesem = input("Kako se imenuje pesem: ")
    # DODAMO TO PESEM V SEZNAM
    playlist.append(pesem) # APPEND APPEND!!!!
    
# IZPISEMO PESMI V SEZNAMU. TO PA ZE ZNATE :)

# POMOC ZA 5. NALOGO
# -------

seznam_ocen = [...]

for ocena in seznam_ocen:
    # PRIMER POGOJEV S POGOJNIM STAVKOM (IF/ELIF/ELSE)
    if ocena == 5:
        print("🟢 5 – profesor je presrečen")
    elif ocena == 4:
        print("🟡 4 – profesor je še kar zadovoljen")
        
        
        
kosarica = []

while True:
    izdelek = input("Dodaj izdelek: ")
    if izdelek.lower("konec"):
        break
    else:
        kosarica.append(izdelek)
        
# Z BONUSOM:
while True:
    print("Izberi možnost")
    print("...  dodaj (pritisni A)")
    print("...  odstrani i-ti izdelek (pritisni R)")
    print("...  koncaj program (pritisni X)")
    izbrana_moznost = input("--> Izbira: ")
    match izbrana_moznost.lower()
        case "a":
            ...
        case "d":
            ...
        case "X":
            ...
        case _:
            print("Ne obstaja ta možnost")

# NAPIŠEŠ KODO PO WHILE ZANKI ...
```

## Kaj mora do konca ure delovati

- Učenec zaključi obvezno jedro sklopa in ga zna demonstrirati
- Učenec zna povedati, kje v kodi je bilo treba kaj popraviti
- Vsaj enkrat samostojno preizkusi svojo rešitev med delom.

## Hitri pregled med uro

- November 2025.
- **Naloga 1: "Seznam meni, kaj si danes jedel?"**
- "🔴 1 – profesor je znova razočaran"

## Tipične napake

- Manjkajoč `:` pri pogojih ali funkcijah
- Napačna zamaknitev bloka kode
- Pozabljena pretvorba `input()` v `int()` ali `float()`
- Napačno ime spremenljivke
- Učenec ne zažene programa po vsakem manjšem koraku.

## Datoteke v tej mapi

- `06_referencni_primer.py`
