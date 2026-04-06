"""Rešitve dodatnih nalog – 20 – Slovarji – vaje, zanke in seznam slovarjev."""

# Namen: rešitve dodatnih nalog po vrstnem redu iz 04_dodatne_naloge.md.

profil = {"ime": "Ana", "tocke": 120, "rang": "zlati"}

print("Naloga 1")
print(profil)


def povecaj_tocke(profil_igralca, kolicina):
    profil_igralca["tocke"] += kolicina


povecaj_tocke(profil, 30)
print("\nNaloga 2")
print(profil)

print("\nNaloga 3")
print("rang" in profil)

print("\nNaloga 4")
for kljuc, vrednost in profil.items():
    print(f"{kljuc} -> {vrednost}")

print("\nNaloga 5")
if profil["tocke"] >= 150:
    print("kategorija: legenda")
elif profil["tocke"] >= 100:
    print("kategorija: napreden")
else:
    print("kategorija: zacetnik")

igralci = [
    {"ime": "Ana", "tocke": 150},
    {"ime": "Bor", "tocke": 95},
    {"ime": "Cene", "tocke": 180},
]

print("\nNaloga 6")
for igralec in igralci:
    print(f"{igralec['ime']}: {igralec['tocke']}")

print("\nNaloga 7")
najboljsi = max(igralci, key=lambda igralec: igralec["tocke"])
print(najboljsi)

print("\nNaloga 8")
nad_sto = [igralec for igralec in igralci if igralec["tocke"] > 100]
print(nad_sto)

print("\nNaloga 9")
urejeni = sorted(igralci, key=lambda igralec: igralec["tocke"], reverse=True)
for mesto, igralec in enumerate(urejeni, start=1):
    print(f"{mesto}. {igralec['ime']} - {igralec['tocke']}")
