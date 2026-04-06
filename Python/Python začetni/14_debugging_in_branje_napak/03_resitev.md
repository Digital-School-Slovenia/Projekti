# Rešitev – 14 – Debugging in branje napak

Tukaj je jedro rešitve za sklop **14 – Debugging in branje napak**. Pokaži en kratek primer. Potem naj učenci delajo.

## Kaj pokaži najprej

- Danes napake niso problem, ampak učni material
- Učencem ne popravljaj kode takoj; najprej naj preberejo traceback
- Vprašaj: katera vrstica, katera vrsta napake, katera vrednost je čudna
- Uporabljaj `print()` debugging in kratke kratek pregled pogovore.

## Primer rešitve

```python
# pokvarjeno
starost = input("Koliko si star? ")
print(starost + 10)

# popravljeno
starost = int(input("Koliko si star? "))
print(starost + 10)
```

## Kako to pokaži

- Najprej odpri pokvarjen primer.
- Pred popravkom vprašaj: *Na kateri vrstici je napaka?*
- Šele nato pokaži popravljeno verzijo.

## Kaj mora do konca ure delovati

- Učenec popravi več kratkih programov
- Pri vsaj treh primerih zna razložiti, kaj je bilo narobe
- Zna opisati svoj osnovni postopek za debugging.

## Hitri pregled med uro

- Učenec zna pokazati vrstico napake.
- Učenec zna povedati, ali gre za sintaktično, tipno ali logično napako.
- Učenec pri vsaj eni nalogi uporabi `print()` za preverjanje stanja.

## Tipične napake

- Branje samo zadnje vrstice napake in ignoriranje konteksta
- Naključno brisanje kode brez razumevanja problema
- Popravljanje petih stvari hkrati
- Brez ponovnega zagona po popravku.

## Datoteke v tej mapi

- `06_pokvarjeni_programi.py`
- `07_popravljene_resitve.py`
