"""Rešitve domače naloge – 08 – Zanka `while` – osnove ponavljanja."""

# Namen: rešitve domače naloge po vrstnem redu iz 05_domaca_naloga.md.

print("Naloga 1")
korak = 0
while korak < 3:
    print("Vaja z while zanko")
    korak += 1

print("\nNaloga 2")
cilj = 12
zbirka = [3, 4, 5, 2]
vsota = 0
indeks = 0
while vsota < cilj and indeks < len(zbirka):
    vsota += zbirka[indeks]
    indeks += 1
print(f"Cilj {cilj} je dosezen z vsoto {vsota}.")

print("\nNaloga 3")
preostali_poskusi = 3
while preostali_poskusi > 0:
    preostali_poskusi -= 1
    if preostali_poskusi == 1:
        print("Se en poskus.")

print("\nNaloga 4")
print("Najpomembneje je, da se v while zanki stanje res spreminja, sicer se zanka ne ustavi.")
