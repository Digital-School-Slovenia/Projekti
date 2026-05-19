"""Rešitve domače naloge – 32 – Projekt – Mini Wolfenstein."""

# Namen: rešitve domače naloge po vrstnem redu iz 05_domaca_naloga.md.

nastavitve = {
    "sirina_okna": 900,
    "visina_okna": 600,
    "hitrost": 0.08,
    "rotacija": 0.05,
}

opis_mehanike = [
    "Igralec se premika po mrezi in ne sme skozi stene.",
    "Raycasting za vsak stolpec pogleda, kje zadene steno.",
    "Minimap prikaze polozaj igralca in stene od zgoraj.",
]


def odkleni_vrata_ce_imas_kljuc(ima_kljuc):
    return "Vrata odklenjena" if ima_kljuc else "Najprej poisci kljuc"


print(nastavitve)
for vrstica in opis_mehanike:
    print(vrstica)
print(odkleni_vrata_ce_imas_kljuc(True))
