# Rešitev / učiteljske usmeritve – 11 – Seznami – osnove in izpis z zankami

## Kako voditi to uro

- ne razlagaj predolgo; daj jedro, potem pa naloge,
- po 10–15 minutah naredi prvi checkpoint,
- pri napaki naj učenec najprej prebere traceback ali opazuje vrednosti spremenljivk,
- pri hitrih učencih najprej odpri dodatne naloge, šele nato prosto nadgrajevanje.

## Referenčni primeri iz tvojega izvornega paketa

### Izsek iz `00_seznamiu.py`

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

1. november 2025.
2. **Naloga 1: “Seznam meni, kaj si danes jedel?”**
3. “🔴 1 – profesor je znova razočaran”

## Kaj šteje kot dober minimum

- delujoče jedro,
- vsaj ena dodatna rešena naloga,
- učenec zna povedati, kaj v kodi zares dela in kaj je popravil.

## Python datoteke v tej mapi

- `06_referencni_primer.py`
