"""Resitve domace naloge - 20 Slovarji vaje."""

def oceni_profil(profil):
    if profil["tocke"] >= 150:
        return "Odlicen igralec."
    if profil["tocke"] >= 100:
        return "Zelo dober napredek."
    return "Se malo vaje in bo slo."


def izpisi_slovar(slovar):
    for kljuc, vrednost in slovar.items():
        print(f"{kljuc}: {vrednost}")


def izpisi_uporabnike(uporabniki):
    for uporabnik in uporabniki:
        print(f"{uporabnik['ime']} ima {uporabnik['tocke']} tock.")


profil = {"ime": "Nina", "tocke": 108}
uporabniki = [
    {"ime": "Nina", "tocke": 108},
    {"ime": "Luka", "tocke": 67},
    {"ime": "Eva", "tocke": 155},
]

print(oceni_profil(profil))
izpisi_slovar(profil)
izpisi_uporabnike(uporabniki)
print("Ustavil bi se lahko pri zanki cez seznam slovarjev, zato pomaga, da najprej izpisem en sam primer uporabnika.")