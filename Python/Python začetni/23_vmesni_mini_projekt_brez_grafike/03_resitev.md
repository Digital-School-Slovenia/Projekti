# Rešitev / učiteljske usmeritve – 23 – Vmesni mini projekt brez grafike

## Kako vodiš to uro

- ne prodajaj 15 različnih idej; naj vsak učenec hitro izbere eno,
- v prvih 20–30 minutah mora nastati minimalno delujoče jedro,
- vsak naslednji kos je nadgradnja, ne nova smer projekta,
- učitelj naj bolj sprašuje kot razlaga.

## Referenčno ogrodje

```python
def izpisi_meni():
    print("1 - dodaj")
    print("2 - odstrani")
    print("3 - pokaži")
    print("4 - konec")

podatki = []

while True:
    izpisi_meni()
    izbira = input("Izbira: ").strip()

    if izbira == "1":
        vrednost = input("Dodaj: ").strip()
        if vrednost:
            podatki.append(vrednost)
    elif izbira == "2":
        vrednost = input("Odstrani: ").strip()
        if vrednost in podatki:
            podatki.remove(vrednost)
    elif izbira == "3":
        print(podatki)
    elif izbira == "4":
        break
    else:
        print("Neveljavna izbira.")
```

## Učiteljski checkpointi

1. Program se zažene in pokaže meni.
2. Ena možnost v meniju že res deluje.
3. Učenec zna pokazati cel uporabniški tok od začetka do konca.

## Kaj šteje kot dober minimum

- program ima jasno temo,
- uporabnik lahko nekaj doda, vidi in zaključi program,
- koda ni ena sama neskončna gmota brez vsaj osnovne strukture.

## Python datoteke v tej mapi

- `06_uciteljska_resitev.py`
