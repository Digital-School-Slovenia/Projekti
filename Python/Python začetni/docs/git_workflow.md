# Predlagan Git workflow

## Minimalni workflow

```bash
git checkout -b izboljsava-sklop-13
# uredi datoteke
python scripts/preveri_strukturo.py
git add .
git commit -m "Izboljsan sklop 13: nizi in oblikovanje izpisa"
git push
```

## Kdaj odpreti ločeno vejo

Odpri ločeno vejo za:
- večje vsebinske popravke sklopa,
- prerazporeditev nalog,
- dodajanje novih `.py` rešitev,
- spremembe v projektnih sklopih,
- spremembe, ki vplivajo na več map hkrati.

## Dober commit message

Primeri:
- `Dodane dodatne vaje za while delavnico`
- `Poenoten ucni scenarij za pygame uvod`
- `Dopolnjene uciteljske resitve za projekt Pac-Man`

## Smiselna navada

Če sprememba vpliva na izvedbo ure, popravi hkrati:
- `01_ucni_nacrt.md`
- `02_ucni_list.md`
- `08_uciteljski_scenarij_ure.md`
