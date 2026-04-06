# Rešitev / učiteljske usmeritve – 14 – Debugging in branje napak

## Kako vodiš to uro

- danes napake niso problem, ampak učni material,
- učencem ne popravljaj kode takoj; najprej naj preberejo traceback,
- vprašaj: katera vrstica, katera vrsta napake, katera vrednost je čudna,
- uporabljaj `print()` debugging in kratke checkpoint pogovore.

## Minimalni referenčni primer

```python
# pokvarjeno
starost = input("Koliko si star? ")
print(starost + 10)

# popravljeno
starost = int(input("Koliko si star? "))
print(starost + 10)
```

## Učiteljski checkpointi

1. Učenec zna pokazati vrstico napake.
2. Učenec zna povedati, ali gre za sintaktično, tipno ali logično napako.
3. Učenec pri vsaj eni nalogi uporabi `print()` za preverjanje stanja.

## Tipične napake

- branje samo zadnje vrstice napake in ignoriranje konteksta,
- naključno brisanje kode brez razumevanja problema,
- popravljanje petih stvari hkrati,
- brez ponovnega zagona po popravku.

## Kaj šteje kot uspeh

- učenec popravi več kratkih programov,
- pri vsaj treh primerih zna razložiti, kaj je bilo narobe,
- zna opisati svoj osnovni postopek za debugging.

## Python datoteke v tej mapi

- `06_pokvarjeni_programi.py`
- `07_popravljene_resitve.py`
