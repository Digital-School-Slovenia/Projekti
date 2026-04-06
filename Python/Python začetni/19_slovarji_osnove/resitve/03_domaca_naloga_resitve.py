# Rešitve domače naloge – 19 Slovarji osnove


def izpisi_profil(profil):
    for kljuc, vrednost in profil.items():
        print(f"{kljuc}: {vrednost}")


def povecaj_tocke(profil, kolicina):
    posodobljen_profil = profil.copy()
    posodobljen_profil["tocke"] += kolicina
    return posodobljen_profil


def preveri_kljuc(profil, kljuc):
    return kljuc in profil


if __name__ == "__main__":
    profil = {"ime": "Ana", "starost": 12, "tocke": 150}

    print("Naloga 1")
    izpisi_profil(profil)

    print("\nNaloga 2")
    print(povecaj_tocke(profil, 25))

    print("\nNaloga 3")
    print(preveri_kljuc(profil, "ime"))
    print(preveri_kljuc(profil, "hobi"))

    # Naloga 4 – primer kratkega odgovora:
    # Ustavil sem se pri kopiranju slovarja, ker nisem želel prepisati originalnih podatkov.
