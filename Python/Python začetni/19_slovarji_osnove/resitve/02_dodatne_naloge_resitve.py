"""Rešitve dodatnih nalog – 19 – Slovarji – osnove."""

# Namen: rešitve dodatnih nalog po vrstnem redu iz 04_dodatne_naloge.md.

def izpisi_kljuce(slovar):
    for kljuc in slovar:
        print(kljuc)


def izpisi_vrednosti(slovar):
    for vrednost in slovar.values():
        print(vrednost)


def vsebuje_kljuc(slovar, kljuc):
    return kljuc in slovar


def povecaj_tocke(igralec, koliko):
    igralec["tocke"] += koliko
    return igralec


if __name__ == "__main__":
    ucenec = {"ime": "Ana", "starost": 13, "razred": "8.a"}

    print("Naloga 1")
    print(ucenec)

    print("\nNaloga 2")
    print(ucenec["ime"])
    print(ucenec["starost"])

    print("\nNaloga 3")
    ucenec["hobi"] = "risanje"
    print(ucenec["hobi"])

    print("\nNaloga 4")
    ucenec["razred"] = "9.a"
    print(ucenec)

    print("\nNaloga 5")
    print(vsebuje_kljuc(ucenec, "hobi"))
    print(vsebuje_kljuc(ucenec, "telefon"))

    print("\nNaloga 6")
    izpisi_kljuce(ucenec)

    print("\nNaloga 7")
    izpisi_vrednosti(ucenec)

    print("\nNaloga 8")
    igralec = {"ime": "Luka", "tocke": 12}
    print(povecaj_tocke(igralec, 5))

    print("\nNaloga 9")
    print("Seznam je dober, ko nas zanima vrstni red elementov.")
    print("Slovar je boljši, ko želimo hitro priti do podatka po imenu ključa.")
